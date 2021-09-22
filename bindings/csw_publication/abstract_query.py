from dataclasses import dataclass
from bindings.csw_publication.abstract_query_type import AbstractQueryType

__NAMESPACE__ = "http://www.opengis.net/cat/csw/2.0.2"


@dataclass
class AbstractQuery(AbstractQueryType):
    class Meta:
        namespace = "http://www.opengis.net/cat/csw/2.0.2"
