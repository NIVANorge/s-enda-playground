from dataclasses import dataclass, field
from typing import List, Optional
from xsdata.models.datatype import XmlDuration
from bindings.csw.request_base_type import RequestBaseType

__NAMESPACE__ = "http://www.opengis.net/cat/csw/2.0.2"


@dataclass
class HarvestType(RequestBaseType):
    """Requests that the catalogue attempt to harvest a resource from some
    network location identified by the source URL.

    Source          - a URL from which the resource is retrieved
    ResourceType    - normally a URI that specifies the type of the resource
    (DCMES v1.1) being harvested if it is known.
    ResourceFormat  - a media type indicating the format of the
    resource being harvested.  The default is
    "application/xml".
    ResponseHandler - a reference to some endpoint to which the
    response shall be forwarded when the
    harvest operation has been completed
    HarvestInterval - an interval expressed using the ISO 8601 syntax;
    it specifies the interval between harvest
    attempts (e.g., P6M indicates an interval of
    six months).
    """
    source: Optional[str] = field(
        default=None,
        metadata={
            "name": "Source",
            "type": "Element",
            "namespace": "http://www.opengis.net/cat/csw/2.0.2",
            "required": True,
        }
    )
    resource_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "ResourceType",
            "type": "Element",
            "namespace": "http://www.opengis.net/cat/csw/2.0.2",
            "required": True,
        }
    )
    resource_format: Optional[str] = field(
        default=None,
        metadata={
            "name": "ResourceFormat",
            "type": "Element",
            "namespace": "http://www.opengis.net/cat/csw/2.0.2",
        }
    )
    harvest_interval: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "HarvestInterval",
            "type": "Element",
            "namespace": "http://www.opengis.net/cat/csw/2.0.2",
        }
    )
    response_handler: List[str] = field(
        default_factory=list,
        metadata={
            "name": "ResponseHandler",
            "type": "Element",
            "namespace": "http://www.opengis.net/cat/csw/2.0.2",
        }
    )
