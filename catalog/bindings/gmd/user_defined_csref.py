from dataclasses import dataclass
from bindings.gmd.user_defined_csproperty_type import UserDefinedCspropertyType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class UserDefinedCsref(UserDefinedCspropertyType):
    class Meta:
        name = "userDefinedCSRef"
        namespace = "http://www.opengis.net/gml"
