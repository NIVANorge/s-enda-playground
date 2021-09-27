from dataclasses import dataclass, field
from typing import Optional, Union
from bindings.gmd.abstract_crstype import (
    AbstractGeneralConversion,
    Conversion1,
)
from bindings.gmd.abstract_general_transformation import AbstractGeneralTransformation
from bindings.gmd.abstract_operation import AbstractOperation
from bindings.gmd.abstract_single_operation import AbstractSingleOperation
from bindings.gmd.actuate_value import ActuateValue
from bindings.gmd.nil_reason_enumeration_value import NilReasonEnumerationValue
from bindings.gmd.pass_through_operation_type import PassThroughOperation
from bindings.gmd.show_value import ShowValue
from bindings.gmd.transformation import Transformation

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class SingleOperationPropertyType:
    """
    gml:SingleOperationPropertyType is a property type for association roles to
    a single operation, either referencing or containing the definition of that
    single operation.
    """
    pass_through_operation: Optional[PassThroughOperation] = field(
        default=None,
        metadata={
            "name": "PassThroughOperation",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    transformation: Optional[Transformation] = field(
        default=None,
        metadata={
            "name": "Transformation",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    abstract_general_transformation: Optional[AbstractGeneralTransformation] = field(
        default=None,
        metadata={
            "name": "AbstractGeneralTransformation",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    conversion: Optional[Conversion1] = field(
        default=None,
        metadata={
            "name": "Conversion",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    abstract_general_conversion: Optional[AbstractGeneralConversion] = field(
        default=None,
        metadata={
            "name": "AbstractGeneralConversion",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    abstract_operation: Optional[AbstractOperation] = field(
        default=None,
        metadata={
            "name": "AbstractOperation",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    abstract_single_operation: Optional[AbstractSingleOperation] = field(
        default=None,
        metadata={
            "name": "AbstractSingleOperation",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    type: str = field(
        init=False,
        default="simple",
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
        }
    )
    arcrole: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    show: Optional[ShowValue] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    actuate: Optional[ActuateValue] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    nil_reason: Optional[Union[str, NilReasonEnumerationValue]] = field(
        default=None,
        metadata={
            "name": "nilReason",
            "type": "Attribute",
            "pattern": r"other:\w{2,}",
        }
    )
    remote_schema: Optional[str] = field(
        default=None,
        metadata={
            "name": "remoteSchema",
            "type": "Attribute",
            "namespace": "http://www.opengis.net/gml",
        }
    )
