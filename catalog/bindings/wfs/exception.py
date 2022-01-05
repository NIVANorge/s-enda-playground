from dataclasses import dataclass
from bindings.wfs.exception_type import ExceptionType

__NAMESPACE__ = "http://www.opengis.net/ows/1.1"


@dataclass
class Exception(ExceptionType):
    class Meta:
        namespace = "http://www.opengis.net/ows/1.1"
