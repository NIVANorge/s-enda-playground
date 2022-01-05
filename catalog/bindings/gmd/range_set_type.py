from dataclasses import dataclass, field
from typing import List, Optional, Union
from bindings.gmd.abstract_scalar_value_list import AbstractScalarValueList
from bindings.gmd.category_list import CategoryList
from bindings.gmd.data_block import DataBlock
from bindings.gmd.file import File
from bindings.gmd.nil_reason_enumeration_value import NilReasonEnumerationValue
from bindings.gmd.quantity_list import QuantityList
from bindings.gmd.value_array_property_type import ValueArray

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class RangeSetType:
    value_array: List[ValueArray] = field(
        default_factory=list,
        metadata={
            "name": "ValueArray",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    quantity_list: List[QuantityList] = field(
        default_factory=list,
        metadata={
            "name": "QuantityList",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    count_list: List[List[Union[str, NilReasonEnumerationValue]]] = field(
        default_factory=list,
        metadata={
            "name": "CountList",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "pattern": r"other:\w{2,}",
            "tokens": True,
        }
    )
    category_list: List[CategoryList] = field(
        default_factory=list,
        metadata={
            "name": "CategoryList",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    boolean_list: List[List[Union[str, NilReasonEnumerationValue]]] = field(
        default_factory=list,
        metadata={
            "name": "BooleanList",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "pattern": r"other:\w{2,}",
            "tokens": True,
        }
    )
    abstract_scalar_value_list: List[AbstractScalarValueList] = field(
        default_factory=list,
        metadata={
            "name": "AbstractScalarValueList",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    data_block: Optional[DataBlock] = field(
        default=None,
        metadata={
            "name": "DataBlock",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    file: Optional[File] = field(
        default=None,
        metadata={
            "name": "File",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
