from dataclasses import dataclass
from bindings.csw.get_domain_type import GetDomainType

__NAMESPACE__ = "http://www.opengis.net/cat/csw/2.0.2"


@dataclass
class GetDomain(GetDomainType):
    class Meta:
        namespace = "http://www.opengis.net/cat/csw/2.0.2"
