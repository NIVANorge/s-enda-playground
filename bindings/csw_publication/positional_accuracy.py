from dataclasses import dataclass
from bindings.csw_publication.abstract_positional_accuracy_type import AbstractPositionalAccuracyType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class PositionalAccuracy(AbstractPositionalAccuracyType):
    class Meta:
        name = "_positionalAccuracy"
        namespace = "http://www.opengis.net/gml"
