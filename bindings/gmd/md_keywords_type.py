from dataclasses import dataclass, field
from typing import List, Optional
from bindings.gmd.abstract_object_type import AbstractObjectType
from bindings.gmd.character_string_property_type import CharacterStringPropertyType
from bindings.gmd.ci_citation_type import CiCitationPropertyType
from bindings.gmd.md_keyword_type_code_property_type import MdKeywordTypeCodePropertyType

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdKeywordsType(AbstractObjectType):
    """
    Keywords, their type and reference source.
    """
    class Meta:
        name = "MD_Keywords_Type"

    keyword: List[CharacterStringPropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "min_occurs": 1,
        }
    )
    type: Optional[MdKeywordTypeCodePropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    thesaurus_name: Optional[CiCitationPropertyType] = field(
        default=None,
        metadata={
            "name": "thesaurusName",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
