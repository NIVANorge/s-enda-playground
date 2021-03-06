from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class AbstractScalarValue:
    """
    gml:AbstractScalarValue is an abstract element which acts as the head of a
    substitution group which contains gml:Boolean, gml:Category, gml:Count and
    gml:Quantity, and (transitively) the elements in their substitution groups.
    """

    class Meta:
        namespace = "http://www.opengis.net/gml"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )
