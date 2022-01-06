from dataclasses import dataclass
from bindings.gmd.abstract_time_object_type import AbstractTimeObjectType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class AbstractTimeObject(AbstractTimeObjectType):
    """
    gml:AbstractTimeObject acts as the head of a substitution group for all
    temporal primitives and complexes.
    """

    class Meta:
        namespace = "http://www.opengis.net/gml"
