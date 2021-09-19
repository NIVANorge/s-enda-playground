from dataclasses import dataclass
from bindings.csw.code_type_2 import CodeType2

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class MeridianName(CodeType2):
    """The name by which this prime meridian is identified.

    The meridianName most common value is Greenwich, and that value
    shall be used when the greenwichLongitude value is zero.
    """
    class Meta:
        name = "meridianName"
        namespace = "http://www.opengis.net/gml"
