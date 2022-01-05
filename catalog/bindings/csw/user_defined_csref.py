from dataclasses import dataclass
from bindings.csw.user_defined_csref_type import UserDefinedCsrefType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class UserDefinedCsref(UserDefinedCsrefType):
    class Meta:
        name = "userDefinedCSRef"
        namespace = "http://www.opengis.net/gml"
