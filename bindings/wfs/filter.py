from dataclasses import dataclass
from bindings.wfs.filter_type import FilterType

__NAMESPACE__ = "http://www.opengis.net/fes/2.0"


@dataclass
class Filter(FilterType):
    class Meta:
        namespace = "http://www.opengis.net/fes/2.0"
