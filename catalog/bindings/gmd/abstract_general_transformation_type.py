from dataclasses import dataclass
from bindings.gmd.abstract_crstype import AbstractCoordinateOperationType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class AbstractGeneralTransformationType(AbstractCoordinateOperationType):
    pass
