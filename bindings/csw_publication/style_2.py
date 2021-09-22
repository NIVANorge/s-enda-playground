from dataclasses import dataclass
from bindings.csw_publication.abstract_style_type import AbstractStyleType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class Style2(AbstractStyleType):
    """The value of the top-level property.

    It is an abstract element. Used as the head element of the
    substitution group for extensibility purposes.
    """
    class Meta:
        name = "_Style"
        namespace = "http://www.opengis.net/gml"
