from dataclasses import dataclass
from bindings.csw_publication.arc_string_type import ArcStringType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class ArcString(ArcStringType):
    class Meta:
        namespace = "http://www.opengis.net/gml"
