from dataclasses import dataclass
from bindings.csw.abstract_time_object_type import AbstractTimeObjectType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class AbstractTimeComplexType(AbstractTimeObjectType):
    """
    The abstract supertype for temporal complexes.
    """
