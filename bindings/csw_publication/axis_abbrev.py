from dataclasses import dataclass
from bindings.csw_publication.code_type_2 import CodeType2

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class AxisAbbrev(CodeType2):
    """The abbreviation used for this coordinate system axis.

    This abbreviation can be used to identify the ordinates in a
    coordinate tuple. Examples are X and Y. The codeSpace attribute can
    reference a source of more information on a set of standardized
    abbreviations, or on this abbreviation.
    """
    class Meta:
        name = "axisAbbrev"
        namespace = "http://www.opengis.net/gml"
