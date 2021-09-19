from dataclasses import dataclass
from bindings.csw.simple_literal import SimpleLiteral

__NAMESPACE__ = "http://purl.org/dc/elements/1.1/"


@dataclass
class Publisher(SimpleLiteral):
    """An entity responsible for making the resource available.

    Examples of Publisher include a person, an organization, or a
    service. Typically, the name of a Publisher should be used to
    indicate the entity.
    """
    class Meta:
        name = "publisher"
        namespace = "http://purl.org/dc/elements/1.1/"
