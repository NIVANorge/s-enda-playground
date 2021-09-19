from dataclasses import dataclass
from bindings.csw.simple_literal import SimpleLiteral

__NAMESPACE__ = "http://purl.org/dc/elements/1.1/"


@dataclass
class Contributor(SimpleLiteral):
    """An entity responsible for making contributions to the content of the
    resource.

    Examples of Contributor include a person, an organization, or a
    service. Typically, the name of a Contributor should be used to
    indicate the entity.
    """
    class Meta:
        name = "contributor"
        namespace = "http://purl.org/dc/elements/1.1/"
