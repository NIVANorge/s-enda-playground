from dataclasses import dataclass
from bindings.wfs.title_elt_type import TitleEltType

__NAMESPACE__ = "http://www.w3.org/1999/xlink"


@dataclass
class Title3(TitleEltType):
    class Meta:
        name = "title"
        namespace = "http://www.w3.org/1999/xlink"
