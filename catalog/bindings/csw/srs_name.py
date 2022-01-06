from dataclasses import dataclass
from bindings.csw.code_type_2 import CodeType2

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class SrsName(CodeType2):
    """
    The name by which this reference system is identified.
    """

    class Meta:
        name = "srsName"
        namespace = "http://www.opengis.net/gml"
