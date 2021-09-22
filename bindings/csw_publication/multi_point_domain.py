from dataclasses import dataclass
from bindings.csw_publication.multi_point_domain_type import MultiPointDomainType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class MultiPointDomain(MultiPointDomainType):
    class Meta:
        name = "multiPointDomain"
        namespace = "http://www.opengis.net/gml"
