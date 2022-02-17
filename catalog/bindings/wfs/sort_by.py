from dataclasses import dataclass
from bindings.wfs.sort_by_type import SortByType

__NAMESPACE__ = "http://www.opengis.net/fes/2.0"


@dataclass
class SortBy(SortByType):
    class Meta:
        namespace = "http://www.opengis.net/fes/2.0"
