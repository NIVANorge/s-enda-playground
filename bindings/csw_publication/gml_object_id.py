from dataclasses import dataclass
from bindings.csw_publication.gml_object_id_type import GmlObjectIdType

__NAMESPACE__ = "http://www.opengis.net/ogc"


@dataclass
class GmlObjectId(GmlObjectIdType):
    class Meta:
        namespace = "http://www.opengis.net/ogc"
