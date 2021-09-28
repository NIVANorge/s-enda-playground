from dataclasses import dataclass
from bindings.wfs.property_is_like_type import PropertyIsLikeType

__NAMESPACE__ = "http://www.opengis.net/fes/2.0"


@dataclass
class PropertyIsLike(PropertyIsLikeType):
    class Meta:
        namespace = "http://www.opengis.net/fes/2.0"
