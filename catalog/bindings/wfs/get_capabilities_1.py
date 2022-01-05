from dataclasses import dataclass
from bindings.wfs.get_capabilities_type_1 import GetCapabilitiesType1

__NAMESPACE__ = "http://www.opengis.net/ows/1.1"


@dataclass
class GetCapabilities1(GetCapabilitiesType1):
    class Meta:
        name = "GetCapabilities"
        namespace = "http://www.opengis.net/ows/1.1"
