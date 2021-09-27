from dataclasses import dataclass, field
from typing import Optional, Union
from bindings.gmd.abstract_dq_completeness import AbstractDqCompleteness
from bindings.gmd.actuate_value import ActuateValue
from bindings.gmd.dq_completeness_commission import DqCompletenessCommission
from bindings.gmd.dq_completeness_omission import DqCompletenessOmission
from bindings.gmd.nil_reason_enumeration_value import NilReasonEnumerationValue
from bindings.gmd.show_value import ShowValue

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class DqCompletenessPropertyType:
    class Meta:
        name = "DQ_Completeness_PropertyType"

    dq_completeness_commission: Optional[DqCompletenessCommission] = field(
        default=None,
        metadata={
            "name": "DQ_CompletenessCommission",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    dq_completeness_omission: Optional[DqCompletenessOmission] = field(
        default=None,
        metadata={
            "name": "DQ_CompletenessOmission",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    abstract_dq_completeness: Optional[AbstractDqCompleteness] = field(
        default=None,
        metadata={
            "name": "AbstractDQ_Completeness",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
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
    uuidref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    nil_reason: Optional[Union[str, NilReasonEnumerationValue]] = field(
        default=None,
        metadata={
            "name": "nilReason",
            "type": "Attribute",
            "namespace": "http://www.isotc211.org/2005/gco",
            "pattern": r"other:\w{2,}",
        }
    )
