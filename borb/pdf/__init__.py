"""
    This file is part of the borb (R) project.
    Copyright (c) 2020-2040 borb Group NV
    Authors: Joris Schellekens, et al.

    This program is free software; you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License version 3
    as published by the Free Software Foundation with the addition of the
    following permission added to Section 15 as permitted in Section 7(a):
    FOR ANY PART OF THE COVERED WORK IN WHICH THE COPYRIGHT IS OWNED BY
    BORB GROUP. BORB GROUP DISCLAIMS THE WARRANTY OF NON INFRINGEMENT
    OF THIRD PARTY RIGHTS

    This program is distributed in the hope that it will be useful, but
    WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY
    or FITNESS FOR A PARTICULAR PURPOSE.

    See the GNU Affero General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with this program; if not, see http://www.gnu.org/licenses or write to
    the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor,
    Boston, MA, 02110-1301 USA.

    The interactive user interfaces in modified source and object code versions
    of this program must display Appropriate Legal Notices, as required under
    Section 5 of the GNU Affero General Public License.
    In accordance with Section 7(b) of the GNU Affero General Public License,
    a covered work must retain the producer line in every PDF that is created
    or manipulated using borb.

    You can be released from the requirements of the license by purchasing
    a commercial license. Buying such a license is mandatory as soon as you
    develop commercial activities involving the borb software without
    disclosing the source code of your own applications.

    These activities include: offering paid services to customers as an ASP,
    serving PDFs on the fly in a web application, shipping borb with a closed
    source product.

    For more information, please contact borb Software Corp. at this
    address: joris.schellekens.1989@gmail.com
"""

# Color
from .canvas.color.color import (
    Color,
    RGBColor,
    CMYKColor,
    GrayColor,
    HSVColor,
    HexColor,
    HSVColor,
    X11Color,
)
from .canvas.color.pantone import Pantone

# Image
from .canvas.layout.image.barcode import Barcode
from .canvas.layout.image.barcode import BarcodeType
from .canvas.layout.image.chart import Chart
from .canvas.layout.image.image import Image
from .canvas.layout.layout_element import Alignment

# List
from .canvas.layout.list.list import List
from .canvas.layout.list.ordered_list import OrderedList
from .canvas.layout.list.roman_list import RomanNumeralOrderedList
from .canvas.layout.list.unordered_list import UnorderedList

# PageLayout
from .canvas.layout.page_layout.page_layout import PageLayout
from .canvas.layout.page_layout.multi_column_layout import MultiColumnLayout
from .canvas.layout.page_layout.multi_column_layout import SingleColumnLayout
from .canvas.layout.page_layout.single_column_layout_with_overflow import (
    SingleColumnLayoutWithOverflow,
)

# Flow
from .canvas.layout.page_layout.inline_flow import InlineFlow
from .canvas.layout.page_layout.block_flow import BlockFlow

# Shape
from .canvas.layout.shape.connected_shape import ConnectedShape
from .canvas.layout.shape.disconnected_shape import DisconnectedShape
from .canvas.layout.smart_art.smart_art import SmartArt

# Table
from .canvas.layout.table.fixed_column_width_table import FixedColumnWidthTable
from .canvas.layout.table.flexible_column_width_table import FlexibleColumnWidthTable
from .canvas.layout.table.table import Table, TableCell
from .canvas.layout.table.table_util import TableUtil
from .canvas.layout.text.heading import Heading

# Forms
from .canvas.layout.forms.form_field import FormField
from .canvas.layout.forms.text_field import TextField
from .canvas.layout.forms.text_area import TextArea
from .canvas.layout.forms.drop_down_list import DropDownList
from .canvas.layout.forms.country_drop_down_list import CountryDropDownList
from .canvas.layout.forms.check_box import CheckBox
from .canvas.layout.forms.push_button import PushButton, JavaScriptPushButton

# Paragraph
from .canvas.layout.text.paragraph import Paragraph
from .canvas.layout.text.heterogeneous_paragraph import HeterogeneousParagraph
from .canvas.layout.text.heading import Heading
from .canvas.layout.text.chunk_of_text import ChunkOfText
from .canvas.lipsum.lipsum import Lipsum

# Document, Page, PDF
from .document.document import Document
from .page.page import Page
from .pdf import PDF
