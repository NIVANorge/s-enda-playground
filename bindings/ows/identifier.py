from dataclasses import dataclass
from bindings.ows.code_type import CodeType

__NAMESPACE__ = "http://www.opengis.net/ows/2.0"


@dataclass
class Identifier(CodeType):
    """
    Unique identifier or name of this dataset.
    """
    class Meta:
        namespace = "http://www.opengis.net/ows/2.0"
