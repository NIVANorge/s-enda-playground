from dataclasses import dataclass
from bindings.csw.code_type_2 import CodeType2

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class DerivedCrstypeType(CodeType2):
    """
    Type of a derived coordinate reference system.
    """

    class Meta:
        name = "DerivedCRSTypeType"
