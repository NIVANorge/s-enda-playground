from dataclasses import dataclass
from bindings.csw.domain_set_type import DomainSetType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class MultiPointDomainType(DomainSetType):
    pass
