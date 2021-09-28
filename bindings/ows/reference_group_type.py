from dataclasses import dataclass, field
from typing import List
from bindings.ows.abstract_reference_base import AbstractReferenceBase
from bindings.ows.basic_identification_type import BasicIdentificationType
from bindings.ows.reference import Reference
from bindings.ows.service_reference import ServiceReference

__NAMESPACE__ = "http://www.opengis.net/ows/2.0"


@dataclass
class ReferenceGroupType(BasicIdentificationType):
    """Logical group of one or more references to remote and/or local
    resources, allowing including metadata about that group.

    A Group can be used instead of a Manifest that can only contain one
    group.
    """
    service_reference: List[ServiceReference] = field(
        default_factory=list,
        metadata={
            "name": "ServiceReference",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows/2.0",
        }
    )
    reference: List[Reference] = field(
        default_factory=list,
        metadata={
            "name": "Reference",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows/2.0",
        }
    )
    abstract_reference_base: List[AbstractReferenceBase] = field(
        default_factory=list,
        metadata={
            "name": "AbstractReferenceBase",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows/2.0",
        }
    )
