from dataclasses import dataclass, field
from typing import Optional
from bindings.csw.constraint import Constraint

__NAMESPACE__ = "http://www.opengis.net/cat/csw/2.0.2"


@dataclass
class DeleteType:
    """
    Deletes one or more catalogue items that satisfy some set of conditions.
    """

    constraint: Optional[Constraint] = field(
        default=None,
        metadata={
            "name": "Constraint",
            "type": "Element",
            "namespace": "http://www.opengis.net/cat/csw/2.0.2",
            "required": True,
        },
    )
    type_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "typeName",
            "type": "Attribute",
        },
    )
    handle: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
