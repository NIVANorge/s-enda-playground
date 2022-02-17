from dataclasses import dataclass, field
from typing import List
from bindings.ows.basic_identification_type import BasicIdentificationType
from bindings.ows.reference_group import ReferenceGroup

__NAMESPACE__ = "http://www.opengis.net/ows/2.0"


@dataclass
class ManifestType(BasicIdentificationType):
    """
    Unordered list of one or more groups of references to remote and/or local
    resources.
    """

    reference_group: List[ReferenceGroup] = field(
        default_factory=list,
        metadata={
            "name": "ReferenceGroup",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows/2.0",
            "min_occurs": 1,
        },
    )
