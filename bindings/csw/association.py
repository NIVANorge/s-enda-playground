from dataclasses import dataclass
from bindings.csw.feature_array_property_type import AssociationType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class Association(AssociationType):
    class Meta:
        name = "_association"
        namespace = "http://www.opengis.net/gml"
