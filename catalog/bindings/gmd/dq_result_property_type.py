from dataclasses import dataclass, field
from typing import Optional, Union
from bindings.gmd.abstract_dq_result import AbstractDqResult
from bindings.gmd.actuate_value import ActuateValue
from bindings.gmd.dq_conformance_result import DqConformanceResult
from bindings.gmd.dq_quantitative_result import DqQuantitativeResult
from bindings.gmd.nil_reason_enumeration_value import NilReasonEnumerationValue
from bindings.gmd.show_value import ShowValue

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class DqResultPropertyType:
    class Meta:
        name = "DQ_Result_PropertyType"

    dq_quantitative_result: Optional[DqQuantitativeResult] = field(
        default=None,
        metadata={
            "name": "DQ_QuantitativeResult",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    dq_conformance_result: Optional[DqConformanceResult] = field(
        default=None,
        metadata={
            "name": "DQ_ConformanceResult",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    abstract_dq_result: Optional[AbstractDqResult] = field(
        default=None,
        metadata={
            "name": "AbstractDQ_Result",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    type: str = field(
        init=False,
        default="simple",
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    href: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    role: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    arcrole: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    show: Optional[ShowValue] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    actuate: Optional[ActuateValue] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    uuidref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    nil_reason: Optional[Union[str, NilReasonEnumerationValue]] = field(
        default=None,
        metadata={
            "name": "nilReason",
            "type": "Attribute",
            "namespace": "http://www.isotc211.org/2005/gco",
            "pattern": r"other:\w{2,}",
        },
    )
