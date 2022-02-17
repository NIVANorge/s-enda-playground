from dataclasses import dataclass
from bindings.ows.abstract_reference_base_type import AbstractReferenceBaseType

__NAMESPACE__ = "http://www.opengis.net/ows/2.0"


@dataclass
class AbstractReferenceBase(AbstractReferenceBaseType):
    class Meta:
        namespace = "http://www.opengis.net/ows/2.0"
