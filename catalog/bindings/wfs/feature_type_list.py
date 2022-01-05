from dataclasses import dataclass
from bindings.wfs.feature_type_list_type import FeatureTypeListType

__NAMESPACE__ = "http://www.opengis.net/wfs/2.0"


@dataclass
class FeatureTypeList(FeatureTypeListType):
    class Meta:
        namespace = "http://www.opengis.net/wfs/2.0"
