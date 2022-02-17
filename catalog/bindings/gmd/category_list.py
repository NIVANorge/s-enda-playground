from dataclasses import dataclass
from bindings.gmd.code_or_nil_reason_list_type import CodeOrNilReasonListType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class CategoryList(CodeOrNilReasonListType):
    class Meta:
        namespace = "http://www.opengis.net/gml"
