from dataclasses import dataclass
from bindings.ows.get_resource_by_id_type import GetResourceByIdType

__NAMESPACE__ = "http://www.opengis.net/ows/2.0"


@dataclass
class GetResourceById(GetResourceByIdType):
    class Meta:
        name = "GetResourceByID"
        namespace = "http://www.opengis.net/ows/2.0"
