from dataclasses import dataclass
from bindings.csw_publication.domain_set_type import DomainSetType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class DomainSet(DomainSetType):
    class Meta:
        name = "domainSet"
        namespace = "http://www.opengis.net/gml"
