from dataclasses import dataclass, field
from typing import Optional
from bindings.csw.abstract_meta_data import AbstractMetaData
from bindings.csw.actuate_type import ActuateType
from bindings.csw.show_type import ShowType
from bindings.csw.type_type import TypeType

__NAMESPACE__ = "http://www.opengis.net/ows"


@dataclass
class MetadataType:
    """This element either references or contains more metadata about the
    element that includes this element.

    To reference metadata stored remotely, at least the xlinks:href
    attribute in xlink:simpleAttrs shall be included. Either at least
    one of the attributes in xlink:simpleAttrs or a substitute for the
    AbstractMetaData element shall be included, but not both. An
    Implementation Specification can restrict the contents of this
    element to always be a reference or always contain metadata.
    (Informative: This element was adapted from the metaDataProperty
    element in GML 3.0.)

    :ivar abstract_meta_data:
    :ivar type:
    :ivar href:
    :ivar role:
    :ivar arcrole:
    :ivar title:
    :ivar show:
    :ivar actuate:
    :ivar about: Optional reference to the aspect of the element which
        includes this "metadata" element that this metadata provides
        more information about.
    """
    abstract_meta_data: Optional[AbstractMetaData] = field(
        default=None,
        metadata={
            "name": "AbstractMetaData",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows",
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
    about: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
