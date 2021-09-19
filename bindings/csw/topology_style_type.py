from dataclasses import dataclass, field
from typing import Optional
from bindings.csw.base_style_descriptor_type import BaseStyleDescriptorType
from bindings.csw.label_style_2 import LabelStyle2
from bindings.csw.symbol import Symbol

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class TopologyStyleType(BaseStyleDescriptorType):
    """[complexType of] The style descriptor for topologies of a feature.

    Describes individual topology elements styles.

    :ivar symbol:
    :ivar style: Deprecated in GML version 3.1.0. Use symbol with inline
        content instead.
    :ivar label_style:
    :ivar topology_property:
    :ivar topology_type:
    """
    symbol: Optional[Symbol] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    label_style: Optional[LabelStyle2] = field(
        default=None,
        metadata={
            "name": "labelStyle",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    topology_property: Optional[str] = field(
        default=None,
        metadata={
            "name": "topologyProperty",
            "type": "Attribute",
        }
    )
    topology_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "topologyType",
            "type": "Attribute",
        }
    )
