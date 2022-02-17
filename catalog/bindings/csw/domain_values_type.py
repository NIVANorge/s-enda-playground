from dataclasses import dataclass, field
from typing import Optional
from xml.etree.ElementTree import QName
from bindings.csw.conceptual_scheme_type import ConceptualSchemeType
from bindings.csw.list_of_values_type import ListOfValuesType
from bindings.csw.range_of_values_type import RangeOfValuesType

__NAMESPACE__ = "http://www.opengis.net/cat/csw/2.0.2"


@dataclass
class DomainValuesType:
    property_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "PropertyName",
            "type": "Element",
            "namespace": "http://www.opengis.net/cat/csw/2.0.2",
        },
    )
    parameter_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "ParameterName",
            "type": "Element",
            "namespace": "http://www.opengis.net/cat/csw/2.0.2",
        },
    )
    list_of_values: Optional[ListOfValuesType] = field(
        default=None,
        metadata={
            "name": "ListOfValues",
            "type": "Element",
            "namespace": "http://www.opengis.net/cat/csw/2.0.2",
        },
    )
    conceptual_scheme: Optional[ConceptualSchemeType] = field(
        default=None,
        metadata={
            "name": "ConceptualScheme",
            "type": "Element",
            "namespace": "http://www.opengis.net/cat/csw/2.0.2",
        },
    )
    range_of_values: Optional[RangeOfValuesType] = field(
        default=None,
        metadata={
            "name": "RangeOfValues",
            "type": "Element",
            "namespace": "http://www.opengis.net/cat/csw/2.0.2",
        },
    )
    type: Optional[QName] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    uom: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
