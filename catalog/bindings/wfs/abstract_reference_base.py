from dataclasses import dataclass
from bindings.wfs.abstract_reference_base_type import AbstractReferenceBaseType

__NAMESPACE__ = "http://www.opengis.net/ows/1.1"


@dataclass
class AbstractReferenceBase(AbstractReferenceBaseType):
    class Meta:
        namespace = "http://www.opengis.net/ows/1.1"
