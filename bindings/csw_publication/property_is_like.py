from dataclasses import dataclass
from bindings.csw_publication.property_is_like_type import PropertyIsLikeType

__NAMESPACE__ = "http://www.opengis.net/ogc"


@dataclass
class PropertyIsLike(PropertyIsLikeType):
    class Meta:
        namespace = "http://www.opengis.net/ogc"
