from dataclasses import dataclass
from bindings.wfs.service_reference_type import ServiceReferenceType

__NAMESPACE__ = "http://www.opengis.net/ows/1.1"


@dataclass
class ServiceReference(ServiceReferenceType):
    class Meta:
        namespace = "http://www.opengis.net/ows/1.1"
