from dataclasses import dataclass
from bindings.csw.simple_literal import SimpleLiteral

__NAMESPACE__ = "http://purl.org/dc/elements/1.1/"


@dataclass
class Rights(SimpleLiteral):
    """Information about rights held in and over the resource.

    Typically, Rights will contain a rights management statement for the
    resource, or reference a service providing such information. Rights
    information often encompasses Intellectual Property Rights (IPR),
    Copyright, and various Property Rights. If the Rights element is
    absent, no assumptions may be made about any rights held in or over
    the resource.
    """
    class Meta:
        name = "rights"
        namespace = "http://purl.org/dc/elements/1.1/"
