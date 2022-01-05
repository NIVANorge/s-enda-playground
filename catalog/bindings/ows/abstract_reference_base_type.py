from dataclasses import dataclass, field
from typing import Optional
from bindings.ows.actuate_type import ActuateType
from bindings.ows.show_type import ShowType

__NAMESPACE__ = "http://www.opengis.net/ows/2.0"


@dataclass
class AbstractReferenceBaseType:
    """Base for a reference to a remote or local resource.

    This type contains only a restricted and annotated set of the
    attributes from the xlink:simpleAttrs attributeGroup.

    :ivar type:
    :ivar href: Reference to a remote resource or local payload. A
        remote resource is typically addressed by a URL. For a local
        payload (such as a multipart mime message), the xlink:href must
        start with the prefix cid:.
    :ivar role: Reference to a resource that describes the role of this
        reference. When no value is supplied, no particular role value
        is to be inferred.
    :ivar arcrole: Although allowed, this attribute is not expected to
        be useful in this application of xlink:simpleAttrs.
    :ivar title: Describes the meaning of the referenced resource in a
        human-readable fashion.
    :ivar show: Although allowed, this attribute is not expected to be
        useful in this application of xlink:simpleAttrs.
    :ivar actuate: Although allowed, this attribute is not expected to
        be useful in this application of xlink:simpleAttrs.
    """
    type: str = field(
        init=False,
        default="simple",
        metadata={
            "type": "Attribute",
            "namespace": "http://www.opengis.net/ows/2.0",
        }
    )
    href: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "required": True,
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
