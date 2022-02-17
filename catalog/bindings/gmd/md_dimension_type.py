from dataclasses import dataclass, field
from typing import Optional
from bindings.gmd.abstract_object_type import AbstractObjectType
from bindings.gmd.integer_property_type import IntegerPropertyType
from bindings.gmd.md_dimension_name_type_code_property_type import (
    MdDimensionNameTypeCodePropertyType,
)
from bindings.gmd.measure_property_type import MeasurePropertyType

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdDimensionType(AbstractObjectType):
    class Meta:
        name = "MD_Dimension_Type"

    dimension_name: Optional[MdDimensionNameTypeCodePropertyType] = field(
        default=None,
        metadata={
            "name": "dimensionName",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "required": True,
        },
    )
    dimension_size: Optional[IntegerPropertyType] = field(
        default=None,
        metadata={
            "name": "dimensionSize",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "required": True,
        },
    )
    resolution: Optional[MeasurePropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
