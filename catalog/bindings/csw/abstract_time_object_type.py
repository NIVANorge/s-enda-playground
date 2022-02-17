from dataclasses import dataclass
from bindings.csw.abstract_gmltype import AbstractGmltype

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class AbstractTimeObjectType(AbstractGmltype):
    """
    The abstract supertype for temporal objects.
    """
