from dataclasses import dataclass
from bindings.gmd.reference_type import ReferenceType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class AbstractReference(ReferenceType):
    """
    gml:abstractReference may be used as the head of a subtitution group of
    more specific elements providing a value by-reference.
    """
    class Meta:
        name = "abstractReference"
        namespace = "http://www.opengis.net/gml"
