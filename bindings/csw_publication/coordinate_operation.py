from dataclasses import dataclass
from bindings.csw_publication.general_conversion_ref_type import AbstractCoordinateOperationType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class CoordinateOperation(AbstractCoordinateOperationType):
    class Meta:
        name = "_CoordinateOperation"
        namespace = "http://www.opengis.net/gml"
