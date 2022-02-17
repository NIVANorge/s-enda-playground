from dataclasses import dataclass
from bindings.wfs.wfs_capabilities_type import WfsCapabilitiesType

__NAMESPACE__ = "http://www.opengis.net/wfs/2.0"


@dataclass
class WfsCapabilities(WfsCapabilitiesType):
    class Meta:
        name = "WFS_Capabilities"
        namespace = "http://www.opengis.net/wfs/2.0"
