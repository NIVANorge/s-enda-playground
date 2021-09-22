from dataclasses import dataclass, field
from typing import Optional
from bindings.csw_publication.actuate_type import ActuateType
from bindings.csw_publication.concatenated_operation import ConcatenatedOperation
from bindings.csw_publication.coordinate_operation import CoordinateOperation
from bindings.csw_publication.general_conversion_ref_type import (
    Conversion,
    GeneralConversion,
)
from bindings.csw_publication.general_transformation import GeneralTransformation
from bindings.csw_publication.operation_2 import Operation2
from bindings.csw_publication.pass_through_operation import PassThroughOperation
from bindings.csw_publication.show_type import ShowType
from bindings.csw_publication.single_operation import SingleOperation
from bindings.csw_publication.transformation import Transformation
from bindings.csw_publication.type_type import TypeType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class CoordinateOperationRefType:
    """
    Association to a coordinate operation, either referencing or containing the
    definition of that coordinate operation.
    """
    transformation: Optional[Transformation] = field(
        default=None,
        metadata={
            "name": "Transformation",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    general_transformation: Optional[GeneralTransformation] = field(
        default=None,
        metadata={
            "name": "_GeneralTransformation",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    conversion: Optional[Conversion] = field(
        default=None,
        metadata={
            "name": "Conversion",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    general_conversion: Optional[GeneralConversion] = field(
        default=None,
        metadata={
            "name": "_GeneralConversion",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    operation: Optional[Operation2] = field(
        default=None,
        metadata={
            "name": "_Operation",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    pass_through_operation: Optional[PassThroughOperation] = field(
        default=None,
        metadata={
            "name": "PassThroughOperation",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    single_operation: Optional[SingleOperation] = field(
        default=None,
        metadata={
            "name": "_SingleOperation",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    concatenated_operation: Optional[ConcatenatedOperation] = field(
        default=None,
        metadata={
            "name": "ConcatenatedOperation",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    coordinate_operation: Optional[CoordinateOperation] = field(
        default=None,
        metadata={
            "name": "_CoordinateOperation",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
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
    remote_schema: Optional[str] = field(
        default=None,
        metadata={
            "name": "remoteSchema",
            "type": "Attribute",
            "namespace": "http://www.opengis.net/gml",
        }
    )
