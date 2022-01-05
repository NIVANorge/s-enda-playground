from dataclasses import dataclass
from bindings.wfs.resource_id_type import ResourceIdType

__NAMESPACE__ = "http://www.opengis.net/fes/2.0"


@dataclass
class ResourceId(ResourceIdType):
    class Meta:
        namespace = "http://www.opengis.net/fes/2.0"
