from dataclasses import dataclass
from bindings.csw.code_or_null_list_type import CodeOrNullListType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class CategoryExtentType(CodeOrNullListType):
    """Restriction of list type to store a 2-point range of ordinal values.

    If one member is a null, then this is a single ended interval.
    """
