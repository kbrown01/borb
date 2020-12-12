from typing import Optional, List, Any, Union

from ptext.io.tokenize.types.pdf_name import PDFName
from ptext.pdf.canvas.event.event_listener import EventListener

from ptext.io.transform.base_transformer import BaseTransformer, TransformerContext
from ptext.io.transform.types import StringWithParentAttribute


class DefaultNameTransformer(BaseTransformer):
    """
    This implementation of BaseTransformer converts PDFName to str
    """

    def can_be_transformed(self, object: Union["io.IOBase", "PDFObject"]) -> bool:
        return isinstance(object, PDFName)

    def transform(
        self,
        object_to_transform: Union["io.IOBase", "PDFObject"],
        parent_object: Any,
        context: Optional[TransformerContext] = None,
        event_listeners: List[EventListener] = [],
    ) -> Any:
        return StringWithParentAttribute(object_to_transform.name).set_parent(
            parent_object
        )