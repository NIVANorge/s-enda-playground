from dataclasses import dataclass
from bindings.wfs.keywords_type import KeywordsType

__NAMESPACE__ = "http://www.opengis.net/ows/1.1"


@dataclass
class Keywords(KeywordsType):
    class Meta:
        namespace = "http://www.opengis.net/ows/1.1"
