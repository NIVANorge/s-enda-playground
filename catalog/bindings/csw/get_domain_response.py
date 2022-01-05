from dataclasses import dataclass
from bindings.csw.get_domain_response_type import GetDomainResponseType

__NAMESPACE__ = "http://www.opengis.net/cat/csw/2.0.2"


@dataclass
class GetDomainResponse(GetDomainResponseType):
    class Meta:
        namespace = "http://www.opengis.net/cat/csw/2.0.2"
