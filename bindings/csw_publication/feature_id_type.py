from dataclasses import dataclass, field
from typing import Optional
from bindings.csw_publication.abstract_id_type import AbstractIdType

__NAMESPACE__ = "http://www.opengis.net/ogc"


@dataclass
class FeatureIdType(AbstractIdType):
    fid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
