from dataclasses import dataclass
from bindings.csw.envelope_type import EnvelopeType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class BoundingBox2(EnvelopeType):
    """
    A bounding box (or envelope) defining the spatial domain of this object.
    """
    class Meta:
        name = "boundingBox"
        namespace = "http://www.opengis.net/gml"
