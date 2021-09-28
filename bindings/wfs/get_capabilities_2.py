from dataclasses import dataclass
from bindings.wfs.get_capabilities_type_2 import GetCapabilitiesType2

__NAMESPACE__ = "http://www.opengis.net/wfs/2.0"


@dataclass
class GetCapabilities2(GetCapabilitiesType2):
    class Meta:
        name = "GetCapabilities"
        namespace = "http://www.opengis.net/wfs/2.0"
