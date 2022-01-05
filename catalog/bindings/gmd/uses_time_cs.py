from dataclasses import dataclass
from bindings.gmd.time_csproperty_type import TimeCspropertyType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class UsesTimeCs(TimeCspropertyType):
    class Meta:
        name = "usesTimeCS"
        namespace = "http://www.opengis.net/gml"
