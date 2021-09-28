from dataclasses import dataclass
from bindings.ows.get_capabilities_type import GetCapabilitiesType

__NAMESPACE__ = "http://www.opengis.net/ows/2.0"


@dataclass
class GetCapabilities(GetCapabilitiesType):
    class Meta:
        namespace = "http://www.opengis.net/ows/2.0"
