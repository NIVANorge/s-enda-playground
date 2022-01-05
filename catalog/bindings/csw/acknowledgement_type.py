from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDateTime
from bindings.csw.echoed_request_type import EchoedRequestType

__NAMESPACE__ = "http://www.opengis.net/cat/csw/2.0.2"


@dataclass
class AcknowledgementType:
    """This is a general acknowledgement response message for all requests that
    may be processed in an asynchronous manner.

    EchoedRequest - Echoes the submitted request message
    RequestId     - identifier for polling purposes (if no response
    handler is available, or the URL scheme is
    unsupported)
    """
    echoed_request: Optional[EchoedRequestType] = field(
        default=None,
        metadata={
            "name": "EchoedRequest",
            "type": "Element",
            "namespace": "http://www.opengis.net/cat/csw/2.0.2",
            "required": True,
        }
    )
    request_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "RequestId",
            "type": "Element",
            "namespace": "http://www.opengis.net/cat/csw/2.0.2",
        }
    )
    time_stamp: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "timeStamp",
            "type": "Attribute",
            "required": True,
        }
    )
