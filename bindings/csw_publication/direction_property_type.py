from dataclasses import dataclass, field
from typing import Optional
from bindings.csw_publication.actuate_type import ActuateType
from bindings.csw_publication.code_type_2 import CodeType2
from bindings.csw_publication.compass_point_enumeration import CompassPointEnumeration
from bindings.csw_publication.direction_vector import DirectionVector
from bindings.csw_publication.show_type import ShowType
from bindings.csw_publication.string_or_ref_type import StringOrRefType
from bindings.csw_publication.type_type import TypeType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class DirectionPropertyType:
    direction_vector: Optional[DirectionVector] = field(
        default=None,
        metadata={
            "name": "DirectionVector",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    compass_point: Optional[CompassPointEnumeration] = field(
        default=None,
        metadata={
            "name": "CompassPoint",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    direction_keyword: Optional[CodeType2] = field(
        default=None,
        metadata={
            "name": "DirectionKeyword",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    direction_string: Optional[StringOrRefType] = field(
        default=None,
        metadata={
            "name": "DirectionString",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    type: TypeType = field(
        init=False,
        default=TypeType.SIMPLE,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    href: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    role: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        }
    )
    arcrole: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    show: Optional[ShowType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    actuate: Optional[ActuateType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    remote_schema: Optional[str] = field(
        default=None,
        metadata={
            "name": "remoteSchema",
            "type": "Attribute",
            "namespace": "http://www.opengis.net/gml",
        }
    )
