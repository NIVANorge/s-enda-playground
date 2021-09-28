from dataclasses import dataclass
from bindings.wfs.language_string_type import LanguageStringType

__NAMESPACE__ = "http://www.opengis.net/ows/1.1"


@dataclass
class Abstract1(LanguageStringType):
    """
    Brief narrative description of this resource, normally used for display to
    a human.
    """
    class Meta:
        name = "Abstract"
        namespace = "http://www.opengis.net/ows/1.1"
