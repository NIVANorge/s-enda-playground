from dataclasses import dataclass, field
from typing import List, Optional
from bindings.gmd.description import Description
from bindings.gmd.description_reference import DescriptionReference
from bindings.gmd.identifier import Identifier
from bindings.gmd.meta_data_property import MetaDataProperty
from bindings.gmd.name import Name

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class AbstractGmltype:
    class Meta:
        name = "AbstractGMLType"

    meta_data_property: List[MetaDataProperty] = field(
        default_factory=list,
        metadata={
            "name": "metaDataProperty",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    description: Optional[Description] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    description_reference: Optional[DescriptionReference] = field(
        default=None,
        metadata={
            "name": "descriptionReference",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    identifier: Optional[Identifier] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    name: List[Name] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        }
    )
