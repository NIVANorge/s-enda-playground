from dataclasses import dataclass
from bindings.csw.abstract_feature_type import AbstractFeatureType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class BoundedFeatureType(AbstractFeatureType):
    """
    Makes boundedBy mandatory.
    """
