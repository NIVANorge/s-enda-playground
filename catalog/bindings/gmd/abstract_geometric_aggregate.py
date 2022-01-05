from dataclasses import dataclass
from bindings.gmd.abstract_geometric_aggregate_type import AbstractGeometricAggregateType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class AbstractGeometricAggregate(AbstractGeometricAggregateType):
    """
    gml:AbstractGeometricAggregate is the abstract head of the substitution
    group for all geometric aggregates.
    """
    class Meta:
        namespace = "http://www.opengis.net/gml"
