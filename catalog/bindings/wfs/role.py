from dataclasses import dataclass
from bindings.wfs.code_type import CodeType

__NAMESPACE__ = "http://www.opengis.net/ows/1.1"


@dataclass
class Role(CodeType):
    """Function performed by the responsible party.

    Possible values of this Role shall include the values and the
    meanings listed in Subclause B.5.5 of ISO 19115:2003.
    """

    class Meta:
        namespace = "http://www.opengis.net/ows/1.1"
