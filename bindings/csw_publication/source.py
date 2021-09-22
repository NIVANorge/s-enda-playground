from dataclasses import dataclass
from bindings.csw_publication.simple_literal import SimpleLiteral

__NAMESPACE__ = "http://purl.org/dc/elements/1.1/"


@dataclass
class Source(SimpleLiteral):
    """A Reference to a resource from which the present resource is derived.

    The present resource may be derived from the Source resource in
    whole or in part. Recommended best practice is to identify the
    referenced resource by means of a string or number conforming to a
    formal identification system.
    """
    class Meta:
        name = "source"
        namespace = "http://purl.org/dc/elements/1.1/"
