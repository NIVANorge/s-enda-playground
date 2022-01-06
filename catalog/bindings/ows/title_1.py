from dataclasses import dataclass
from bindings.ows.language_string_type import LanguageStringType

__NAMESPACE__ = "http://www.opengis.net/ows/2.0"


@dataclass
class Title1(LanguageStringType):
    """
    Title of this resource, normally used for display to humans.
    """

    class Meta:
        name = "Title"
        namespace = "http://www.opengis.net/ows/2.0"
