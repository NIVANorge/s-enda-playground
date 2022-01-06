from dataclasses import dataclass
from bindings.gmd.abstract_time_complex_type import AbstractTimeComplexType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class AbstractTimeComplex(AbstractTimeComplexType):
    """
    gml:AbstractTimeComplex is an aggregation of temporal primitives and acts
    as the head of a substitution group for temporal complexes.
    """

    class Meta:
        namespace = "http://www.opengis.net/gml"
