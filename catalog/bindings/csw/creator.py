from dataclasses import dataclass
from bindings.csw.simple_literal import SimpleLiteral

__NAMESPACE__ = "http://purl.org/dc/elements/1.1/"


@dataclass
class Creator(SimpleLiteral):
    """An entity primarily responsible for making the content of the resource.

    Examples of Creator include a person, an organization, or a service.
    Typically, the name of a Creator should be used to indicate the
    entity.
    """
    class Meta:
        name = "creator"
        namespace = "http://purl.org/dc/elements/1.1/"
