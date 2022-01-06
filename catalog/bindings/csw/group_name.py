from dataclasses import dataclass
from bindings.csw.code_type_2 import CodeType2

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class GroupName(CodeType2):
    """
    The name by which this operation parameter group is identified.
    """

    class Meta:
        name = "groupName"
        namespace = "http://www.opengis.net/gml"
