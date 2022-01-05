from dataclasses import dataclass
from bindings.csw.abstract_id_type import AbstractIdType

__NAMESPACE__ = "http://www.opengis.net/ogc"


@dataclass
class Id(AbstractIdType):
    class Meta:
        name = "_Id"
        namespace = "http://www.opengis.net/ogc"
