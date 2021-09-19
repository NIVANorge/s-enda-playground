from dataclasses import dataclass
from bindings.csw.general_conversion_ref_type import AbstractCoordinateOperationType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class SingleOperation(AbstractCoordinateOperationType):
    """
    A single (not concatenated) coordinate operation.
    """
    class Meta:
        name = "_SingleOperation"
        namespace = "http://www.opengis.net/gml"
