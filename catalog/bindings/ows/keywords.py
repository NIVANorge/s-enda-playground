from dataclasses import dataclass
from bindings.ows.keywords_type import KeywordsType

__NAMESPACE__ = "http://www.opengis.net/ows/2.0"


@dataclass
class Keywords(KeywordsType):
    class Meta:
        namespace = "http://www.opengis.net/ows/2.0"
