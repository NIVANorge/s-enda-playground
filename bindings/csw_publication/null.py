from dataclasses import dataclass, field
from typing import Union
from bindings.csw_publication.null_enumeration_value import NullEnumerationValue

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class Null:
    class Meta:
        namespace = "http://www.opengis.net/gml"

    value: Union[str, NullEnumerationValue] = field(
        default="",
        metadata={
            "pattern": r"other:\w{2,}",
        }
    )
