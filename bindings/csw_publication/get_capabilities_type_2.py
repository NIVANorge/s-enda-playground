from dataclasses import dataclass, field
from bindings.csw_publication.get_capabilities_type_1 import GetCapabilitiesType1

__NAMESPACE__ = "http://www.opengis.net/cat/csw/2.0.2"


@dataclass
class GetCapabilitiesType2(GetCapabilitiesType1):
    """Request for a description of service capabilities.

    See OGC 05-008 for more information.
    """
    class Meta:
        name = "GetCapabilitiesType"

    service: str = field(
        default="http://www.opengis.net/cat/csw",
        metadata={
            "type": "Attribute",
        }
    )
