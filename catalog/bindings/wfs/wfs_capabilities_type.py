from dataclasses import dataclass, field
from typing import Optional
from bindings.wfs.actuate_type import ActuateType
from bindings.wfs.capabilities_base_type import CapabilitiesBaseType
from bindings.wfs.feature_type_list import FeatureTypeList
from bindings.wfs.filter_capabilities import FilterCapabilities
from bindings.wfs.show_type import ShowType
from bindings.wfs.type_type import TypeType

__NAMESPACE__ = "http://www.opengis.net/wfs/2.0"


@dataclass
class WfsCapabilitiesType(CapabilitiesBaseType):
    class Meta:
        name = "WFS_CapabilitiesType"

    wsdl: Optional["WfsCapabilitiesType.Wsdl"] = field(
        default=None,
        metadata={
            "name": "WSDL",
            "type": "Element",
            "namespace": "http://www.opengis.net/wfs/2.0",
        }
    )
    feature_type_list: Optional[FeatureTypeList] = field(
        default=None,
        metadata={
            "name": "FeatureTypeList",
            "type": "Element",
            "namespace": "http://www.opengis.net/wfs/2.0",
        }
    )
    filter_capabilities: Optional[FilterCapabilities] = field(
        default=None,
        metadata={
            "name": "Filter_Capabilities",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
        }
    )

    @dataclass
    class Wsdl:
        any_element: Optional[object] = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "namespace": "##any",
            }
        )
        type: TypeType = field(
            init=False,
            default=TypeType.SIMPLE,
            metadata={
                "type": "Attribute",
                "namespace": "http://www.w3.org/1999/xlink",
            }
        )
        href: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "namespace": "http://www.w3.org/1999/xlink",
            }
        )
        role: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "namespace": "http://www.w3.org/1999/xlink",
                "min_length": 1,
            }
        )
        arcrole: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "namespace": "http://www.w3.org/1999/xlink",
                "min_length": 1,
            }
        )
        title: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "namespace": "http://www.w3.org/1999/xlink",
            }
        )
        show: Optional[ShowType] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "namespace": "http://www.w3.org/1999/xlink",
            }
        )
        actuate: Optional[ActuateType] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "namespace": "http://www.w3.org/1999/xlink",
            }
        )
