from dataclasses import dataclass
from bindings.wfs.envelope_property_type import EnvelopePropertyType

__NAMESPACE__ = "http://www.opengis.net/wfs/2.0"


@dataclass
class BoundedBy(EnvelopePropertyType):
    class Meta:
        name = "boundedBy"
        namespace = "http://www.opengis.net/wfs/2.0"
