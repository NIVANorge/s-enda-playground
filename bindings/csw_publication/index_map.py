from dataclasses import dataclass
from bindings.csw_publication.index_map_type import IndexMapType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class IndexMap(IndexMapType):
    class Meta:
        namespace = "http://www.opengis.net/gml"
