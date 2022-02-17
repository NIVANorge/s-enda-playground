from dataclasses import dataclass
from bindings.wfs.language_string_type import LanguageStringType

__NAMESPACE__ = "http://www.opengis.net/ows/1.1"


@dataclass
class Title1(LanguageStringType):
    """
    Title of this resource, normally used for display to a human.
    """

    class Meta:
        name = "Title"
        namespace = "http://www.opengis.net/ows/1.1"
