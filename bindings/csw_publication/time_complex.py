from dataclasses import dataclass
from bindings.csw_publication.abstract_time_complex_type import AbstractTimeComplexType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class TimeComplex(AbstractTimeComplexType):
    """This abstract element acts as the head of the substitution group for
    temporal complexes.

    Temporal complex is an aggregation of temporal primitives as its
    components, represents a temporal geometric complex and a temporal
    topology complex. N.B. Temporal geometric complex is not defined in
    this schema.
    """
    class Meta:
        name = "_TimeComplex"
        namespace = "http://www.opengis.net/gml"
