from dataclasses import dataclass
from bindings.gmd.code_type import CodeType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class AnchorPoint(CodeType):
    class Meta:
        name = "anchorPoint"
        namespace = "http://www.opengis.net/gml"
