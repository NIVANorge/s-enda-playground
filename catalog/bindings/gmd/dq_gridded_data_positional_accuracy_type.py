from dataclasses import dataclass
from bindings.gmd.abstract_dq_positional_accuracy_type import (
    AbstractDqPositionalAccuracyType,
)

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class DqGriddedDataPositionalAccuracyType(AbstractDqPositionalAccuracyType):
    class Meta:
        name = "DQ_GriddedDataPositionalAccuracy_Type"
