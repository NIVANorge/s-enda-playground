from dataclasses import dataclass
from bindings.csw.code_type_2 import CodeType2

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class MethodFormula(CodeType2):
    """Formula(s) used by this operation method.

    The value may be a reference to a publication. Note that the
    operation method may not be analytic, in which case this element
    references or contains the procedure, not an analytic formula.
    """

    class Meta:
        name = "methodFormula"
        namespace = "http://www.opengis.net/gml"
