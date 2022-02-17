from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "http://www.opengis.net/ows/2.0"


@dataclass
class GetResourceByIdType:
    """Request to a service to perform the GetResourceByID operation.

    This operation allows a client to retrieve one or more identified
    resources, including datasets and resources that describe datasets
    or parameters. In this XML encoding, no "request" parameter is
    included, since the element name specifies the specific operation.

    :ivar resource_id: Unordered list of zero or more resource
        identifiers. These identifiers can be listed in the Contents
        section of the service metadata (Capabilities) document. For
        more information on this parameter, see Subclause 9.4.2.1 of the
        OWS Common specification.
    :ivar output_format: Optional reference to the data format to be
        used for response to this operation request. This element shall
        be included when multiple output formats are available for the
        selected resource(s), and the client desires a format other than
        the specified default, if any.
    :ivar service:
    :ivar version:
    """

    resource_id: List[str] = field(
        default_factory=list,
        metadata={
            "name": "ResourceID",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows/2.0",
        },
    )
    output_format: Optional[str] = field(
        default=None,
        metadata={
            "name": "OutputFormat",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows/2.0",
            "pattern": r"(application|audio|image|text|video|message|multipart|model)/.+(;\s*.+=.+)*",
        },
    )
    service: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    version: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"\d+\.\d?\d\.\d?\d",
        },
    )
