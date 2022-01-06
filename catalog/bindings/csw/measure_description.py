from dataclasses import dataclass
from bindings.csw.code_type_2 import CodeType2

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class MeasureDescription(CodeType2):
    """
    A description of the position accuracy parameter(s) provided.
    """

    class Meta:
        name = "measureDescription"
        namespace = "http://www.opengis.net/gml"
