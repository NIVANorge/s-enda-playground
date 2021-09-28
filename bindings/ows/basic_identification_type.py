from dataclasses import dataclass, field
from typing import List, Optional
from bindings.ows.additional_parameters import AdditionalParameters
from bindings.ows.description_type import DescriptionType
from bindings.ows.identifier import Identifier
from bindings.ows.metadata import Metadata

__NAMESPACE__ = "http://www.opengis.net/ows/2.0"


@dataclass
class BasicIdentificationType(DescriptionType):
    """
    Basic metadata identifying and describing a set of data.

    :ivar identifier: Optional unique identifier or name of this
        dataset.
    :ivar additional_parameters:
    :ivar metadata: Optional unordered list of additional metadata about
        this data(set). A list of optional metadata elements for this
        data identification could be specified in the Implementation
        Specification for this service.
    """
    identifier: Optional[Identifier] = field(
        default=None,
        metadata={
            "name": "Identifier",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows/2.0",
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
