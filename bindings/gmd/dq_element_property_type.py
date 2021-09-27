from dataclasses import dataclass, field
from typing import Optional, Union
from bindings.gmd.abstract_dq_completeness import AbstractDqCompleteness
from bindings.gmd.abstract_dq_element import AbstractDqElement
from bindings.gmd.abstract_dq_logical_consistency import AbstractDqLogicalConsistency
from bindings.gmd.abstract_dq_positional_accuracy import AbstractDqPositionalAccuracy
from bindings.gmd.abstract_dq_temporal_accuracy import AbstractDqTemporalAccuracy
from bindings.gmd.abstract_dq_thematic_accuracy import AbstractDqThematicAccuracy
from bindings.gmd.actuate_value import ActuateValue
from bindings.gmd.dq_absolute_external_positional_accuracy import DqAbsoluteExternalPositionalAccuracy
from bindings.gmd.dq_accuracy_of_atime_measurement import DqAccuracyOfAtimeMeasurement
from bindings.gmd.dq_completeness_commission import DqCompletenessCommission
from bindings.gmd.dq_completeness_omission import DqCompletenessOmission
from bindings.gmd.dq_conceptual_consistency import DqConceptualConsistency
from bindings.gmd.dq_domain_consistency import DqDomainConsistency
from bindings.gmd.dq_format_consistency import DqFormatConsistency
from bindings.gmd.dq_gridded_data_positional_accuracy import DqGriddedDataPositionalAccuracy
from bindings.gmd.dq_non_quantitative_attribute_accuracy import DqNonQuantitativeAttributeAccuracy
from bindings.gmd.dq_quantitative_attribute_accuracy import DqQuantitativeAttributeAccuracy
from bindings.gmd.dq_relative_internal_positional_accuracy import DqRelativeInternalPositionalAccuracy
from bindings.gmd.dq_temporal_consistency import DqTemporalConsistency
from bindings.gmd.dq_temporal_validity import DqTemporalValidity
from bindings.gmd.dq_thematic_classification_correctness import DqThematicClassificationCorrectness
from bindings.gmd.dq_topological_consistency import DqTopologicalConsistency
from bindings.gmd.nil_reason_enumeration_value import NilReasonEnumerationValue
from bindings.gmd.show_value import ShowValue

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class DqElementPropertyType:
    class Meta:
        name = "DQ_Element_PropertyType"

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
    dq_absolute_external_positional_accuracy: Optional[DqAbsoluteExternalPositionalAccuracy] = field(
        default=None,
        metadata={
            "name": "DQ_AbsoluteExternalPositionalAccuracy",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    dq_gridded_data_positional_accuracy: Optional[DqGriddedDataPositionalAccuracy] = field(
        default=None,
        metadata={
            "name": "DQ_GriddedDataPositionalAccuracy",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    dq_relative_internal_positional_accuracy: Optional[DqRelativeInternalPositionalAccuracy] = field(
        default=None,
        metadata={
            "name": "DQ_RelativeInternalPositionalAccuracy",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    abstract_dq_positional_accuracy: Optional[AbstractDqPositionalAccuracy] = field(
        default=None,
        metadata={
            "name": "AbstractDQ_PositionalAccuracy",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    dq_thematic_classification_correctness: Optional[DqThematicClassificationCorrectness] = field(
        default=None,
        metadata={
            "name": "DQ_ThematicClassificationCorrectness",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    dq_non_quantitative_attribute_accuracy: Optional[DqNonQuantitativeAttributeAccuracy] = field(
        default=None,
        metadata={
            "name": "DQ_NonQuantitativeAttributeAccuracy",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    dq_quantitative_attribute_accuracy: Optional[DqQuantitativeAttributeAccuracy] = field(
        default=None,
        metadata={
            "name": "DQ_QuantitativeAttributeAccuracy",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    abstract_dq_thematic_accuracy: Optional[AbstractDqThematicAccuracy] = field(
        default=None,
        metadata={
            "name": "AbstractDQ_ThematicAccuracy",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    dq_accuracy_of_atime_measurement: Optional[DqAccuracyOfAtimeMeasurement] = field(
        default=None,
        metadata={
            "name": "DQ_AccuracyOfATimeMeasurement",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    dq_temporal_consistency: Optional[DqTemporalConsistency] = field(
        default=None,
        metadata={
            "name": "DQ_TemporalConsistency",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    dq_temporal_validity: Optional[DqTemporalValidity] = field(
        default=None,
        metadata={
            "name": "DQ_TemporalValidity",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    abstract_dq_temporal_accuracy: Optional[AbstractDqTemporalAccuracy] = field(
        default=None,
        metadata={
            "name": "AbstractDQ_TemporalAccuracy",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    abstract_dq_element: Optional[AbstractDqElement] = field(
        default=None,
        metadata={
            "name": "AbstractDQ_Element",
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
