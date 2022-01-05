from dataclasses import dataclass
from bindings.ows.nil_value_type import NilValueType

__NAMESPACE__ = "http://www.opengis.net/ows/2.0"


@dataclass
class NilValue(NilValueType):
    class Meta:
        name = "nilValue"
        namespace = "http://www.opengis.net/ows/2.0"
