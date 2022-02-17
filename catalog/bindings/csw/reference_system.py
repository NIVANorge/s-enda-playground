from dataclasses import dataclass
from bindings.csw.abstract_reference_system_type import AbstractReferenceSystemType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class ReferenceSystem(AbstractReferenceSystemType):
    class Meta:
        name = "_ReferenceSystem"
        namespace = "http://www.opengis.net/gml"
