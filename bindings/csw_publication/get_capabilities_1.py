from dataclasses import dataclass
from bindings.csw_publication.get_capabilities_type_1 import GetCapabilitiesType1

__NAMESPACE__ = "http://www.opengis.net/ows"


@dataclass
class GetCapabilities1(GetCapabilitiesType1):
    class Meta:
        name = "GetCapabilities"
        namespace = "http://www.opengis.net/ows"
