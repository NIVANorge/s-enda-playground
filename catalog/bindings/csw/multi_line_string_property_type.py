from dataclasses import dataclass, field
from typing import Optional
from bindings.csw.actuate_type import ActuateType
from bindings.csw.multi_line_string import MultiLineString
from bindings.csw.show_type import ShowType
from bindings.csw.type_type import TypeType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class MultiLineStringPropertyType:
    """This type is deprecated with GML 3 and shall not be used.

    It is included for backwards compatibility with GML 2. Use
    MultiCurvePropertyType instead. A property that has a collection of
    line strings as its value domain can either be an appropriate
    geometry element encapsulated in an element of this type or an XLink
    reference to a remote geometry element (where remote includes
    geometry elements located elsewhere in the same document). Either
    the reference or the contained element must be given, but neither
    both nor none.
    """

    multi_line_string: Optional[MultiLineString] = field(
        default=None,
        metadata={
            "name": "MultiLineString",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    type: TypeType = field(
        init=False,
        default=TypeType.SIMPLE,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    href: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    role: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        },
    )
    arcrole: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        },
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    show: Optional[ShowType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    actuate: Optional[ActuateType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    remote_schema: Optional[str] = field(
        default=None,
        metadata={
            "name": "remoteSchema",
            "type": "Attribute",
            "namespace": "http://www.opengis.net/gml",
        },
    )
