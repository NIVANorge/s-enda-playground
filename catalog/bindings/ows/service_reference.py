from dataclasses import dataclass
from bindings.ows.service_reference_type import ServiceReferenceType

__NAMESPACE__ = "http://www.opengis.net/ows/2.0"


@dataclass
class ServiceReference(ServiceReferenceType):
    class Meta:
        namespace = "http://www.opengis.net/ows/2.0"
