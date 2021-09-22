from dataclasses import dataclass
from bindings.csw_publication.simple_literal import SimpleLiteral

__NAMESPACE__ = "http://purl.org/dc/elements/1.1/"


@dataclass
class Date(SimpleLiteral):
    """A date of an event in the lifecycle of the resource.

    Typically, Date will be associated with the creation or availability
    of the resource. Recommended best practice for encoding the date
    value is defined in a profile of ISO 8601 and includes (among
    others) dates of the form YYYY-MM-DD.
    """
    class Meta:
        name = "date"
        namespace = "http://purl.org/dc/elements/1.1/"
