from dataclasses import dataclass, field
from typing import List
from bindings.csw_publication.domain_values_type import DomainValuesType

__NAMESPACE__ = "http://www.opengis.net/cat/csw/2.0.2"


@dataclass
class GetDomainResponseType:
    """Returns the actual values for some property.

    In general this is a subset of the value domain (that is, set of
    permissible values), although in some cases these may be the same.
    """
    domain_values: List[DomainValuesType] = field(
        default_factory=list,
        metadata={
            "name": "DomainValues",
            "type": "Element",
            "namespace": "http://www.opengis.net/cat/csw/2.0.2",
            "min_occurs": 1,
        }
    )
