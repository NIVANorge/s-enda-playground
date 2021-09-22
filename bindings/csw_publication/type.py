from dataclasses import dataclass
from bindings.csw_publication.simple_literal import SimpleLiteral

__NAMESPACE__ = "http://purl.org/dc/elements/1.1/"


@dataclass
class TypeType(SimpleLiteral):
    """The nature or genre of the content of the resource.

    Type includes terms describing general categories, functions,
    genres, or aggregation levels for content. Recommended best practice
    is to select a value from a controlled vocabulary (for example, the
    DCMI Type Vocabulary). To describe the physical or digital
    manifestation of the resource, use the Format element.
    """
    class Meta:
        name = "type"
        namespace = "http://purl.org/dc/elements/1.1/"
