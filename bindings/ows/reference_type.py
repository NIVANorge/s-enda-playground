from dataclasses import dataclass, field
from typing import List, Optional
from bindings.ows.abstract import Abstract
from bindings.ows.abstract_reference_base_type import AbstractReferenceBaseType
from bindings.ows.additional_parameters import AdditionalParameters
from bindings.ows.identifier import Identifier
from bindings.ows.metadata import Metadata

__NAMESPACE__ = "http://www.opengis.net/ows/2.0"


@dataclass
class ReferenceType(AbstractReferenceBaseType):
    """
    Complete reference to a remote or local resource, allowing including
    metadata about that resource.

    :ivar identifier: Optional unique identifier of the referenced
        resource.
    :ivar abstract:
    :ivar format: The format of the referenced resource. This element is
        omitted when the mime type is indicated in the http header of
        the reference.
    :ivar additional_parameters:
    :ivar metadata: Optional unordered list of additional metadata about
        this resource. A list of optional metadata elements for this
        ReferenceType could be specified in the Implementation
        Specification for each use of this type in a specific OWS.
    """
    identifier: Optional[Identifier] = field(
        default=None,
        metadata={
            "name": "Identifier",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows/2.0",
        }
    )
    abstract: List[Abstract] = field(
        default_factory=list,
        metadata={
            "name": "Abstract",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows/2.0",
        }
    )
    format: Optional[str] = field(
        default=None,
        metadata={
            "name": "Format",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows/2.0",
            "pattern": r"(application|audio|image|text|video|message|multipart|model)/.+(;\s*.+=.+)*",
        }
    )
    additional_parameters: List[AdditionalParameters] = field(
        default_factory=list,
        metadata={
            "name": "AdditionalParameters",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows/2.0",
        }
    )
    metadata: List[Metadata] = field(
        default_factory=list,
        metadata={
            "name": "Metadata",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows/2.0",
        }
    )
