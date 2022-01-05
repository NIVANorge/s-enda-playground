from dataclasses import dataclass
from bindings.wfs.element_type import ElementType

__NAMESPACE__ = "http://www.opengis.net/wfs/2.0"


@dataclass
class Element(ElementType):
    class Meta:
        namespace = "http://www.opengis.net/wfs/2.0"
