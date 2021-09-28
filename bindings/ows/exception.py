from dataclasses import dataclass
from bindings.ows.exception_type import ExceptionType

__NAMESPACE__ = "http://www.opengis.net/ows/2.0"


@dataclass
class Exception(ExceptionType):
    class Meta:
        namespace = "http://www.opengis.net/ows/2.0"
