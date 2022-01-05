from dataclasses import dataclass
from bindings.csw.set_type import SetType

__NAMESPACE__ = "http://www.w3.org/2001/SMIL20/"


@dataclass
class Set2(SetType):
    class Meta:
        name = "set"
        namespace = "http://www.w3.org/2001/SMIL20/"
