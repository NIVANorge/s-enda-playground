from enum import Enum

__NAMESPACE__ = "http://www.opengis.net/cat/csw/2.0.2"


class ElementSetType(Enum):
    """
    Named subsets of catalogue object properties; these views are mapped to a
    specific information model and are defined in an application profile.
    """

    BRIEF = "brief"
    SUMMARY = "summary"
    FULL = "full"
