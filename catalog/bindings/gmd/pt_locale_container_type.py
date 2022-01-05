from dataclasses import dataclass, field
from typing import List, Optional
from bindings.gmd.character_string_property_type import CharacterStringPropertyType
from bindings.gmd.ci_date_property_type import CiDatePropertyType
from bindings.gmd.ci_responsible_party_property_type import CiResponsiblePartyPropertyType
from bindings.gmd.localised_character_string_property_type import LocalisedCharacterStringPropertyType
from bindings.gmd.pt_locale_property_type import PtLocalePropertyType

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class PtLocaleContainerType:
    class Meta:
        name = "PT_LocaleContainer_Type"

    description: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "required": True,
        }
    )
    locale: Optional[PtLocalePropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "required": True,
        }
    )
    date: List[CiDatePropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "min_occurs": 1,
        }
    )
    responsible_party: List[CiResponsiblePartyPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "responsibleParty",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "min_occurs": 1,
        }
    )
    localised_string: List[LocalisedCharacterStringPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "localisedString",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "min_occurs": 1,
        }
    )
