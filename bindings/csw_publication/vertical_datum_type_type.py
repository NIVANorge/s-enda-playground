from dataclasses import dataclass
from bindings.csw_publication.code_type_2 import CodeType2

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class VerticalDatumTypeType(CodeType2):
    """
    Type of a vertical datum.
    """
