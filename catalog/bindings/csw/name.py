from dataclasses import dataclass
from bindings.csw.code_type_2 import CodeType2

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class Name(CodeType2):
    """Label for the object, normally a descriptive name.

    An object may have several names, typically assigned by different
    authorities.  The authority for a name is indicated by the value of
    its (optional) codeSpace attribute.  The name may or may not be
    unique, as determined by the rules of the organization responsible
    for the codeSpace.
    """

    class Meta:
        name = "name"
        namespace = "http://www.opengis.net/gml"
