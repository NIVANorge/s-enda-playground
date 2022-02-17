from dataclasses import dataclass, field
from typing import List, Optional
from bindings.gmd.abstract_md_identification_type import AbstractMdIdentificationType
from bindings.gmd.character_string_property_type import CharacterStringPropertyType
from bindings.gmd.ex_extent_property_type import ExExtentPropertyType
from bindings.gmd.md_character_set_code_property_type import (
    MdCharacterSetCodePropertyType,
)
from bindings.gmd.md_resolution_property_type import MdResolutionPropertyType
from bindings.gmd.md_spatial_representation_type_code_property_type import (
    MdSpatialRepresentationTypeCodePropertyType,
)
from bindings.gmd.md_topic_category_code_property_type import (
    MdTopicCategoryCodePropertyType,
)

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdDataIdentificationType(AbstractMdIdentificationType):
    class Meta:
        name = "MD_DataIdentification_Type"

    spatial_representation_type: List[
        MdSpatialRepresentationTypeCodePropertyType
    ] = field(
        default_factory=list,
        metadata={
            "name": "spatialRepresentationType",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    spatial_resolution: List[MdResolutionPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "spatialResolution",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    language: List[CharacterStringPropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "min_occurs": 1,
        },
    )
    character_set: List[MdCharacterSetCodePropertyType] = field(
        default_factory=list,
        metadata={
            "name": "characterSet",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    topic_category: List[MdTopicCategoryCodePropertyType] = field(
        default_factory=list,
        metadata={
            "name": "topicCategory",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    environment_description: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "name": "environmentDescription",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    extent: List[ExExtentPropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    supplemental_information: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "name": "supplementalInformation",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
