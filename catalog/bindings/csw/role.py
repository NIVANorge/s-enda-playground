from dataclasses import dataclass
from bindings.csw.code_type_1 import CodeType1

__NAMESPACE__ = "http://www.opengis.net/ows"


@dataclass
class Role(CodeType1):
    """Function performed by the responsible party.

    Possible values of this Role shall include the values and the
    meanings listed in Subclause B.5.5 of ISO 19115:2003.
    """

    class Meta:
        namespace = "http://www.opengis.net/ows"
