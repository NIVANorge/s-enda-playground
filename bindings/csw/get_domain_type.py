from dataclasses import dataclass, field
from typing import Optional
from bindings.csw.request_base_type import RequestBaseType

__NAMESPACE__ = "http://www.opengis.net/cat/csw/2.0.2"


@dataclass
class GetDomainType(RequestBaseType):
    """
    Requests the actual values of some specified request parameter or other
    data element.
    """
    property_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "PropertyName",
            "type": "Element",
            "namespace": "http://www.opengis.net/cat/csw/2.0.2",
        }
    )
    parameter_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "ParameterName",
            "type": "Element",
            "namespace": "http://www.opengis.net/cat/csw/2.0.2",
        }
    )
