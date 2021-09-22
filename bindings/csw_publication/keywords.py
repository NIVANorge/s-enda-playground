from dataclasses import dataclass
from bindings.csw_publication.keywords_type import KeywordsType

__NAMESPACE__ = "http://www.opengis.net/ows"


@dataclass
class Keywords(KeywordsType):
    class Meta:
        namespace = "http://www.opengis.net/ows"
