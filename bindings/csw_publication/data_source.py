from dataclasses import dataclass
from bindings.csw_publication.string_or_ref_type import StringOrRefType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class DataSource(StringOrRefType):
    class Meta:
        name = "dataSource"
        namespace = "http://www.opengis.net/gml"
