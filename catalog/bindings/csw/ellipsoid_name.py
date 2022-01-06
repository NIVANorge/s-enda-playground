from dataclasses import dataclass
from bindings.csw.code_type_2 import CodeType2

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class EllipsoidName(CodeType2):
    """
    The name by which this ellipsoid is identified.
    """

    class Meta:
        name = "ellipsoidName"
        namespace = "http://www.opengis.net/gml"
