from dataclasses import dataclass
from bindings.csw_publication.simple_literal import SimpleLiteral

__NAMESPACE__ = "http://purl.org/dc/elements/1.1/"


@dataclass
class Description1(SimpleLiteral):
    """An account of the content of the resource.

    Examples of Description include, but are not limited to, an
    abstract, table of contents, reference to a graphical representation
    of content, or free-text account of the content.
    """
    class Meta:
        name = "description"
        namespace = "http://purl.org/dc/elements/1.1/"
