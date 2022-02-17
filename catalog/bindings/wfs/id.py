from dataclasses import dataclass
from bindings.wfs.abstract_id_type import AbstractIdType

__NAMESPACE__ = "http://www.opengis.net/fes/2.0"


@dataclass
class Id(AbstractIdType):
    class Meta:
        name = "_Id"
        namespace = "http://www.opengis.net/fes/2.0"
