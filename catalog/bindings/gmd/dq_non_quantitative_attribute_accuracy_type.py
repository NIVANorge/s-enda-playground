from dataclasses import dataclass
from bindings.gmd.abstract_dq_thematic_accuracy_type import AbstractDqThematicAccuracyType

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class DqNonQuantitativeAttributeAccuracyType(AbstractDqThematicAccuracyType):
    class Meta:
        name = "DQ_NonQuantitativeAttributeAccuracy_Type"
