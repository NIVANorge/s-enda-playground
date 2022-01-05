from dataclasses import dataclass
from bindings.wfs.get_resource_by_id_type import GetResourceByIdType

__NAMESPACE__ = "http://www.opengis.net/ows/1.1"


@dataclass
class GetResourceById(GetResourceByIdType):
    class Meta:
        name = "GetResourceByID"
        namespace = "http://www.opengis.net/ows/1.1"
