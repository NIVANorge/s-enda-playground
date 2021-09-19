from dataclasses import dataclass, field
from typing import Optional
from bindings.csw.definition_type import DefinitionType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class AbstractGeneralOperationParameterType(DefinitionType):
    """
    Abstract definition of a parameter or group of parameters used by an
    operation method.
    """
    minimum_occurs: Optional[int] = field(
        default=None,
        metadata={
            "name": "minimumOccurs",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
