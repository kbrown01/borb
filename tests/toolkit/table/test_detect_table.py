import random
import unittest
from decimal import Decimal
from pathlib import Path
from typing import List

import typing

from borb.pdf.canvas.color.color import X11Color
from borb.pdf.canvas.geometry.rectangle import Rectangle
from borb.pdf.canvas.layout.layout_element import Alignment
from borb.pdf.canvas.layout.page_layout.multi_column_layout import SingleColumnLayout
from borb.pdf.canvas.layout.page_layout.page_layout import PageLayout
from borb.pdf.canvas.layout.table.flexible_column_width_table import FlexibleColumnWidthTable
from borb.pdf.canvas.layout.table.table import Table, TableCell
from borb.pdf.canvas.layout.text.paragraph import Paragraph
from borb.pdf.document import Document
from borb.pdf.page.page import Page
from borb.pdf.pdf import PDF
from borb.toolkit.table.table_detection_by_lines import TableDetectionByLines


class TableDefinition:

    def __init__(self,
                 number_of_rows: int,
                 number_of_columns: int,
                 cell_definition: typing.List[typing.Tuple[int, int]]):
        assert number_of_rows > 0
        assert number_of_columns > 0
        assert sum([x[0] * x[1] for x in cell_definition]) == number_of_rows * number_of_columns
        self._number_of_rows = number_of_rows
        self._number_of_columns = number_of_columns
        self._cell_definition = cell_definition


class TestDetectTable(unittest.TestCase):

    # fmt: off
    TABLES_TO_GENERATE: typing.List[TableDefinition] = [TableDefinition(1, 1, [(1, 1)]),
                                                        TableDefinition(2, 2, [(1, 1), (1, 1), (1, 1), (1, 1)]),
                                                        TableDefinition(2, 2, [(1, 2), (1, 1), (1, 1)]),
                                                        TableDefinition(2, 2, [(2, 1), (1, 1), (1, 1)]),
                                                        TableDefinition(2, 3, [(1, 1), (2, 1), (1, 1), (1, 1), (1, 1)]),
                                                        TableDefinition(3, 3, [(3, 1), (1, 1), (1, 1), (2, 1), (1, 1), (1, 1)]),
                                                        TableDefinition(3, 6, [(1, 3), (1, 3), (1, 2), (1, 2), (1, 2), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1)]),
                                                        ]
    # fmt: on

    def __init__(self, methodName="runTest"):
        super().__init__(methodName)
        # find output dir
        p: Path = Path(__file__).parent
        while "output" not in [x.stem for x in p.iterdir() if x.is_dir()]:
            p = p.parent
        p = p / "output"
        self.output_dir = Path(p, Path(__file__).stem.replace(".py", ""))
        if not self.output_dir.exists():
            self.output_dir.mkdir()

    def _generate_table(self, table_definition: TableDefinition) -> Table:
        t: FlexibleColumnWidthTable = FlexibleColumnWidthTable(number_of_rows=table_definition._number_of_rows,
                                                                   number_of_columns=table_definition._number_of_columns)
        for i, cd in enumerate(table_definition._cell_definition):
            t.add(TableCell(Paragraph(str(i)),
                            row_span=cd[0],
                            col_span=cd[1]))

        # set padding
        t.set_padding_on_all_cells(Decimal(5), Decimal(5), Decimal(5), Decimal(5))

        # return
        return t

    def test_generate_pdfs_with_tables(self):

        for i, td in enumerate(TestDetectTable.TABLES_TO_GENERATE):

            # create Document
            print("Generating PDF with Table [%d / %d] .." % (i+1, len(TestDetectTable.TABLES_TO_GENERATE)))
            d: Document = Document()

            # add Page
            p: Page = Page()
            d.append_page(p)

            # set LayoutManager
            l: PageLayout = SingleColumnLayout(p)

            # add random amount of text
            for _ in range(0, random.randint(1, 4)):
                l.add(Paragraph("""
                Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
                Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. 
                Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. 
                Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
                """))

            # add Table
            table: Table = self._generate_table(td)
            table._horizontal_alignment = random.choice([Alignment.LEFT, Alignment.CENTERED, Alignment.RIGHT])
            l.add(table)

            # add random amount of text
            for _ in range(0, random.randint(1, 4)):
                l.add(Paragraph("""
                Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
                Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. 
                Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. 
                Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
                """))

            # derive name
            number_with_zero_prefixed: str = str(i)
            while len(number_with_zero_prefixed) < 3:
                number_with_zero_prefixed = "0" + number_with_zero_prefixed

            # store
            with open(self.output_dir / ("input_%s.pdf" % number_with_zero_prefixed), "wb") as pdf_file_handle:
                PDF.dumps(pdf_file_handle, d)

    def test_find_table(self):

        input_files: typing.List[Path] = [x for x in self.output_dir.iterdir() if x.is_file() and x.name.startswith("input")]
        for i, input_file in enumerate(input_files):

            # open Document
            print("Scanning PDF (%s) with Table [%d / %d] .." % (input_file.name, i+1, len(input_files)))
            doc: typing.Optional[Document] = None
            with open(input_file, "rb") as input_pdf_handle:
                l: TableDetectionByLines = TableDetectionByLines()
                doc = PDF.loads(input_pdf_handle, [l])

            assert doc is not None

            table_bounding_boxes: typing.List[Rectangle] = l.get_table_bounding_boxes_per_page(0)
            tables: typing.List[Table] = l.get_tables_per_page(0)

            # add annotation around table
            for r in table_bounding_boxes:
                r = r.grow(Decimal(5))
                doc.get_page(0).append_square_annotation(r, stroke_color=X11Color("Red"))

            # add annotation around each cell
            if len(tables) > 0:
                for tc in tables[0]._content:
                    r = tc.get_bounding_box()
                    r = r.shrink(Decimal(2))
                    doc.get_page(0).append_square_annotation(r,
                                                             stroke_color=X11Color("Green"),
                                                             fill_color=X11Color("Green"))

            # determine output name
            output_file: Path = input_file.parent / input_file.name.replace("input","output")

            # store
            with open(output_file, "wb") as output_file_handle:
                PDF.dumps(output_file_handle, doc)