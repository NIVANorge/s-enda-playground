from dataclasses import dataclass
from bindings.gmd.abstract_dq_logical_consistency_type import AbstractDqLogicalConsistencyType

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class DqConceptualConsistencyType(AbstractDqLogicalConsistencyType):
    class Meta:
        name = "DQ_ConceptualConsistency_Type"
