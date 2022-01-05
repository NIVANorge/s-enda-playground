from dataclasses import dataclass
from bindings.csw.sort_by_type import SortByType

__NAMESPACE__ = "http://www.opengis.net/ogc"


@dataclass
class SortBy(SortByType):
    class Meta:
        namespace = "http://www.opengis.net/ogc"
