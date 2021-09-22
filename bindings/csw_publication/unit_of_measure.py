from dataclasses import dataclass
from bindings.csw_publication.unit_of_measure_type import UnitOfMeasureType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class UnitOfMeasure(UnitOfMeasureType):
    class Meta:
        name = "unitOfMeasure"
        namespace = "http://www.opengis.net/gml"
