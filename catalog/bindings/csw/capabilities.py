from dataclasses import dataclass
from bindings.csw.capabilities_type import CapabilitiesType

__NAMESPACE__ = "http://www.opengis.net/cat/csw/2.0.2"


@dataclass
class Capabilities(CapabilitiesType):
    class Meta:
        namespace = "http://www.opengis.net/cat/csw/2.0.2"
