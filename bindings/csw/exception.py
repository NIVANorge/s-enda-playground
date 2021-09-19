from dataclasses import dataclass
from bindings.csw.exception_type import ExceptionType

__NAMESPACE__ = "http://www.opengis.net/ows"


@dataclass
class Exception(ExceptionType):
    class Meta:
        namespace = "http://www.opengis.net/ows"
