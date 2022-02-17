from dataclasses import dataclass
from bindings.csw.code_type_1 import CodeType1

__NAMESPACE__ = "http://www.opengis.net/ows"


@dataclass
class Identifier1(CodeType1):
    """
    Unique identifier or name of this dataset.
    """

    class Meta:
        name = "Identifier"
        namespace = "http://www.opengis.net/ows"
