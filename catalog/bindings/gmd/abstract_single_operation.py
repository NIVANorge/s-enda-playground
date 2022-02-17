from dataclasses import dataclass
from bindings.gmd.abstract_crstype import AbstractCoordinateOperationType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class AbstractSingleOperation(AbstractCoordinateOperationType):
    """
    gml:AbstractSingleOperation is a single (not concatenated) coordinate
    operation.
    """

    class Meta:
        namespace = "http://www.opengis.net/gml"
