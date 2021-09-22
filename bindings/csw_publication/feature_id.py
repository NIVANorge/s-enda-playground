from dataclasses import dataclass
from bindings.csw_publication.feature_id_type import FeatureIdType

__NAMESPACE__ = "http://www.opengis.net/ogc"


@dataclass
class FeatureId(FeatureIdType):
    class Meta:
        namespace = "http://www.opengis.net/ogc"
