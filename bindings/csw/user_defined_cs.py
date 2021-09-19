from dataclasses import dataclass
from bindings.csw.user_defined_cstype import UserDefinedCstype

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class UserDefinedCs(UserDefinedCstype):
    class Meta:
        name = "UserDefinedCS"
        namespace = "http://www.opengis.net/gml"
