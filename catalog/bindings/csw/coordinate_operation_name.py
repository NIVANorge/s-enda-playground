from dataclasses import dataclass
from bindings.csw.code_type_2 import CodeType2

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class CoordinateOperationName(CodeType2):
    """
    The name by which this coordinate operation is identified.
    """
    class Meta:
        name = "coordinateOperationName"
        namespace = "http://www.opengis.net/gml"
