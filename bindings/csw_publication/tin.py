from dataclasses import dataclass
from bindings.csw_publication.tin_type import TinType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class Tin(TinType):
    class Meta:
        namespace = "http://www.opengis.net/gml"
