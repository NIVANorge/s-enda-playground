from dataclasses import dataclass
from bindings.csw.element_set_name_type import ElementSetNameType

__NAMESPACE__ = "http://www.opengis.net/cat/csw/2.0.2"


@dataclass
class ElementSetName(ElementSetNameType):
    class Meta:
        namespace = "http://www.opengis.net/cat/csw/2.0.2"
