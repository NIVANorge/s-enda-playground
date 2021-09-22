from dataclasses import dataclass
from bindings.csw_publication.grid_domain_type import GridDomainType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class GridDomain(GridDomainType):
    class Meta:
        name = "gridDomain"
        namespace = "http://www.opengis.net/gml"
