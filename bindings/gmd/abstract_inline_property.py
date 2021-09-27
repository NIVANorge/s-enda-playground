from dataclasses import dataclass
from bindings.gmd.inline_property_type import InlinePropertyType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class AbstractInlineProperty(InlinePropertyType):
    """
    gml:abstractInlineProperty may be used as the head of a subtitution group
    of more specific elements providing a value inline.
    """
    class Meta:
        name = "abstractInlineProperty"
        namespace = "http://www.opengis.net/gml"
