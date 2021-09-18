from dataclasses import dataclass, field
from typing import List, Optional
from generated.gml.pkg_3.pkg_1.pkg_1.base.basic_types import CodeType
from generated.gml.pkg_3.pkg_1.pkg_1.base.dictionary import DefinitionType
from generated.gml.pkg_3.pkg_1.pkg_1.base.gml_base import (
    ReferenceType,
    StringOrRefType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class FormulaType:
    """Paremeters of a simple formula by which a value using this unit of
    measure can be converted to the corresponding value using the preferred
    unit of measure.

    The formula element contains elements a, b, c and d, whose values use the XML Schema type "double". These values are used in the formula y = (a + bx) / (c + dx), where x is a value using this unit, and y is the corresponding value using the preferred unit. The elements a and d are optional, and if values are not provided, those parameters are considered to be zero. If values are not provided for both a and d, the formula is equivalent to a fraction with numerator and denominator parameters.
    """
    a: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    b: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        }
    )
    c: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        }
    )
    d: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )


@dataclass
class UnitOfMeasureType:
    """Reference to a unit of measure definition that applies to all the
    numerical values described by the element containing this element.

    Notice that a complexType which needs to include the uom attribute
    can do so by extending this complexType. Alternately, this
    complexType can be used as a pattern for a new complexType.

    :ivar uom: Reference to a unit of measure definition, usually within
        the same XML document but possibly outside the XML document
        which contains this reference. For a reference within the same
        XML document, the "#" symbol should be used, followed by a text
        abbreviation of the unit name. However, the "#" symbol may be
        optional, and still may be interpreted as a reference.
    """
    uom: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class ConversionToPreferredUnitType(UnitOfMeasureType):
    """Relation of a unit to the preferred unit for this quantity type,
    specified by an arithmetic conversion (scaling and/or offset).

    A preferred unit is either a base unit or a derived unit selected
    for all units of one quantity type. The mandatory attribute "uom"
    shall reference the preferred unit that this conversion applies to.
    The conversion is specified by one of two alternative elements:
    "factor" or "formula".

    :ivar factor: Specification of the scale factor by which a value
        using this unit of measure can be multiplied to obtain the
        corresponding value using the preferred unit of measure.
    :ivar formula: Specification of the formula by which a value using
        this unit of measure can be converted to obtain the
        corresponding value using the preferred unit of measure.
    """
    factor: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    formula: Optional[FormulaType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )


@dataclass
class DerivationUnitTermType(UnitOfMeasureType):
    """Definition of one unit term for a derived unit of measure.

    This unit term references another unit of measure (uom) and provides
    an integer exponent applied to that unit in defining the compound
    unit. The exponent can be positive or negative, but not zero.
    """
    exponent: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class CatalogSymbol(CodeType):
    """For global understanding of a unit of measure, it is often possible to
    reference an item in a catalog of units, using a symbol in that catalog.

    The "codeSpace" attribute in "CodeType" identifies a namespace for
    the catalog symbol value, and might reference the catalog. The
    "string" value in "CodeType" contains the value of a symbol that is
    unique within this catalog namespace. This symbol often appears
    explicitly in the catalog, but it could be a combination of symbols
    using a specified algebra of units. For example, the symbol "cm"
    might indicate that it is the "m" symbol combined with the "c"
    prefix.
    """
    class Meta:
        name = "catalogSymbol"
        namespace = "http://www.opengis.net/gml"


@dataclass
class QuantityType(StringOrRefType):
    """Informal description of the phenomenon or type of quantity that is
    measured or observed.

    For example, "length", "angle", "time", "pressure", or
    "temperature". When the quantity is the result of an observation or
    measurement, this term is known as Observable Type or Measurand.
    """
    class Meta:
        name = "quantityType"
        namespace = "http://www.opengis.net/gml"


@dataclass
class UnitOfMeasure(UnitOfMeasureType):
    class Meta:
        name = "unitOfMeasure"
        namespace = "http://www.opengis.net/gml"


@dataclass
class UnitDefinitionType(DefinitionType):
    """Definition of a unit of measure (or uom).

    The definition includes a quantityType property, which indicates the
    phenomenon to which the units apply, and a catalogSymbol, which
    gives the short symbol used for this unit. This element is used when
    the relationship of this unit to other units or units systems is
    unknown.
    """
    quantity_type: Optional[QuantityType] = field(
        default=None,
        metadata={
            "name": "quantityType",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        }
    )
    catalog_symbol: Optional[CatalogSymbol] = field(
        default=None,
        metadata={
            "name": "catalogSymbol",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )


@dataclass
class ConversionToPreferredUnit(ConversionToPreferredUnitType):
    """
    This element is included when this unit has an accurate conversion to the
    preferred unit for this quantity type.
    """
    class Meta:
        name = "conversionToPreferredUnit"
        namespace = "http://www.opengis.net/gml"


@dataclass
class DerivationUnitTerm(DerivationUnitTermType):
    class Meta:
        name = "derivationUnitTerm"
        namespace = "http://www.opengis.net/gml"


@dataclass
class RoughConversionToPreferredUnit(ConversionToPreferredUnitType):
    """
    This element is included when the correct definition of this unit is
    unknown, but this unit has a rough or inaccurate conversion to the
    preferred unit for this quantity type.
    """
    class Meta:
        name = "roughConversionToPreferredUnit"
        namespace = "http://www.opengis.net/gml"


@dataclass
class BaseUnitType(UnitDefinitionType):
    """Definition of a unit of measure which is a base unit from the system of
    units.

    A base unit cannot be derived by combination of other base units
    within this system.  Sometimes known as "fundamental unit".
    """
    units_system: Optional[ReferenceType] = field(
        default=None,
        metadata={
            "name": "unitsSystem",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        }
    )


@dataclass
class ConventionalUnitType(UnitDefinitionType):
    """Definition of a unit of measure which is related to a preferred unit for
    this quantity type through a conversion formula.

    A method for deriving this unit by algebraic combination of more
    primitive units, may also be provided.
    """
    conversion_to_preferred_unit: Optional[ConversionToPreferredUnit] = field(
        default=None,
        metadata={
            "name": "conversionToPreferredUnit",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    rough_conversion_to_preferred_unit: Optional[RoughConversionToPreferredUnit] = field(
        default=None,
        metadata={
            "name": "roughConversionToPreferredUnit",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    derivation_unit_term: List[DerivationUnitTerm] = field(
        default_factory=list,
        metadata={
            "name": "derivationUnitTerm",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )


@dataclass
class DerivedUnitType(UnitDefinitionType):
    """Definition of a unit of measure which is defined through algebraic
    combination of more primitive units, which are usually base units from a
    particular system of units.

    Derived units based directly on base units are usually preferred for
    quantities other than the base units or fundamental quantities
    within a system.  If a derived unit is not the preferred unit, the
    ConventionalUnit element should be used instead.
    """
    derivation_unit_term: List[DerivationUnitTerm] = field(
        default_factory=list,
        metadata={
            "name": "derivationUnitTerm",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "min_occurs": 1,
        }
    )


@dataclass
class UnitDefinition(UnitDefinitionType):
    class Meta:
        namespace = "http://www.opengis.net/gml"


@dataclass
class BaseUnit(BaseUnitType):
    class Meta:
        namespace = "http://www.opengis.net/gml"


@dataclass
class ConventionalUnit(ConventionalUnitType):
    class Meta:
        namespace = "http://www.opengis.net/gml"


@dataclass
class DerivedUnit(DerivedUnitType):
    class Meta:
        namespace = "http://www.opengis.net/gml"
