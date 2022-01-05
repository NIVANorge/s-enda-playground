from dataclasses import dataclass
from bindings.gmd.abstract_crstype import AbstractCoordinateOperationType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class AbstractOperation(AbstractCoordinateOperationType):
    class Meta:
        namespace = "http://www.opengis.net/gml"
