from dataclasses import dataclass
from bindings.csw.code_type_2 import CodeType2

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class Category(CodeType2):
    """A term representing a classification.

    It has an optional XML attribute codeSpace, whose value is a URI
    which identifies a dictionary, codelist or authority for the term.
    """
    class Meta:
        namespace = "http://www.opengis.net/gml"
