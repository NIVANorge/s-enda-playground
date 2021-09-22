from dataclasses import dataclass, field
from typing import Optional
from bindings.csw_publication.base_style_descriptor_type import BaseStyleDescriptorType
from bindings.csw_publication.label_type import LabelType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class LabelStyleType(BaseStyleDescriptorType):
    """
    [complexType of] The style descriptor for labels of a feature, geometry or
    topology.
    """
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        }
    )
    label: Optional[LabelType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        }
    )
