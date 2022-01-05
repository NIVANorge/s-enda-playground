from dataclasses import dataclass
from bindings.csw.code_type_2 import CodeType2

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class DatumName(CodeType2):
    """
    The name by which this datum is identified.
    """
    class Meta:
        name = "datumName"
        namespace = "http://www.opengis.net/gml"
