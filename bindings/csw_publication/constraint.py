from dataclasses import dataclass
from bindings.csw_publication.query_constraint_type import QueryConstraintType

__NAMESPACE__ = "http://www.opengis.net/cat/csw/2.0.2"


@dataclass
class Constraint(QueryConstraintType):
    class Meta:
        namespace = "http://www.opengis.net/cat/csw/2.0.2"
