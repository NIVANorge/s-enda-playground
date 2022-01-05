from dataclasses import dataclass, field
from typing import Optional, Union
from bindings.gmd.abstract_dq_logical_consistency import AbstractDqLogicalConsistency
from bindings.gmd.actuate_value import ActuateValue
from bindings.gmd.dq_conceptual_consistency import DqConceptualConsistency
from bindings.gmd.dq_domain_consistency import DqDomainConsistency
from bindings.gmd.dq_format_consistency import DqFormatConsistency
from bindings.gmd.dq_topological_consistency import DqTopologicalConsistency
from bindings.gmd.nil_reason_enumeration_value import NilReasonEnumerationValue
from bindings.gmd.show_value import ShowValue

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class DqLogicalConsistencyPropertyType:
    class Meta:
        name = "DQ_LogicalConsistency_PropertyType"

    dq_conceptual_consistency: Optional[DqConceptualConsistency] = field(
        default=None,
        metadata={
            "name": "DQ_ConceptualConsistency",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    dq_domain_consistency: Optional[DqDomainConsistency] = field(
        default=None,
        metadata={
            "name": "DQ_DomainConsistency",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    dq_format_consistency: Optional[DqFormatConsistency] = field(
        default=None,
        metadata={
            "name": "DQ_FormatConsistency",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    dq_topological_consistency: Optional[DqTopologicalConsistency] = field(
        default=None,
        metadata={
            "name": "DQ_TopologicalConsistency",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    abstract_dq_logical_consistency: Optional[AbstractDqLogicalConsistency] = field(
        default=None,
        metadata={
            "name": "AbstractDQ_LogicalConsistency",
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
