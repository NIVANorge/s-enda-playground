from dataclasses import dataclass, field
from typing import Optional
from bindings.csw.capabilities_base_type import CapabilitiesBaseType
from bindings.csw.filter_capabilities import FilterCapabilities

__NAMESPACE__ = "http://www.opengis.net/cat/csw/2.0.2"


@dataclass
class CapabilitiesType(CapabilitiesBaseType):
    """This type extends ows:CapabilitiesBaseType defined in OGC-05-008 to
    include information about supported OGC filter components.

    A profile may extend this type to describe additional capabilities.
    """

    filter_capabilities: Optional[FilterCapabilities] = field(
        default=None,
        metadata={
            "name": "Filter_Capabilities",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
            "required": True,
        },
    )
