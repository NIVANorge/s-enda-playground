from dataclasses import dataclass
from bindings.csw.filter_type import FilterType

__NAMESPACE__ = "http://www.opengis.net/ogc"


@dataclass
class Filter(FilterType):
    class Meta:
        namespace = "http://www.opengis.net/ogc"
