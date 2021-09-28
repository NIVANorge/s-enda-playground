from dataclasses import dataclass, field
from typing import Optional, Union
from xsdata.models.datatype import XmlDateTime
from bindings.wfs.abstract_id_type import AbstractIdType
from bindings.wfs.version_action_tokens import VersionActionTokens

__NAMESPACE__ = "http://www.opengis.net/fes/2.0"


@dataclass
class ResourceIdType(AbstractIdType):
    rid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    previous_rid: Optional[str] = field(
        default=None,
        metadata={
            "name": "previousRid",
            "type": "Attribute",
        }
    )
    version: Optional[Union[VersionActionTokens, int, XmlDateTime]] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    start_date: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "startDate",
            "type": "Attribute",
        }
    )
    end_date: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "endDate",
            "type": "Attribute",
        }
    )
