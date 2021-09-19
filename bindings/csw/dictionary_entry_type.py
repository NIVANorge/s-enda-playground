from dataclasses import dataclass, field
from typing import List, Optional
from bindings.csw.abstract_general_operation_parameter_ref_type import OperationParameterGroup
from bindings.csw.actuate_type import ActuateType
from bindings.csw.base_unit import BaseUnit
from bindings.csw.cartesian_cs import CartesianCs
from bindings.csw.concatenated_operation import ConcatenatedOperation
from bindings.csw.conventional_unit import ConventionalUnit
from bindings.csw.coordinate_operation import CoordinateOperation
from bindings.csw.coordinate_reference_system import CoordinateReferenceSystem
from bindings.csw.coordinate_system import CoordinateSystem
from bindings.csw.coordinate_system_axis import CoordinateSystemAxis
from bindings.csw.crs import Crs
from bindings.csw.cylindrical_cs import CylindricalCs
from bindings.csw.datum import Datum
from bindings.csw.definition import Definition
from bindings.csw.definition_proxy import DefinitionProxy
from bindings.csw.definition_type import DefinitionType
from bindings.csw.derived_unit import DerivedUnit
from bindings.csw.ellipsoid import Ellipsoid
from bindings.csw.ellipsoidal_cs import EllipsoidalCs
from bindings.csw.engineering_crs import EngineeringCrs
from bindings.csw.engineering_datum import EngineeringDatum
from bindings.csw.general_conversion_ref_type import (
    CompoundCrs,
    Conversion,
    DerivedCrs,
    ProjectedCrs,
    GeneralConversion,
    GeneralDerivedCrs,
)
from bindings.csw.general_operation_parameter import GeneralOperationParameter
from bindings.csw.general_transformation import GeneralTransformation
from bindings.csw.geocentric_crs import GeocentricCrs
from bindings.csw.geodetic_datum import GeodeticDatum
from bindings.csw.geographic_crs import GeographicCrs
from bindings.csw.image_crs import ImageCrs
from bindings.csw.image_datum import ImageDatum
from bindings.csw.indirect_entry import IndirectEntry
from bindings.csw.linear_cs import LinearCs
from bindings.csw.oblique_cartesian_cs import ObliqueCartesianCs
from bindings.csw.operation_2 import Operation2
from bindings.csw.operation_method import OperationMethod
from bindings.csw.operation_parameter import OperationParameter
from bindings.csw.pass_through_operation import PassThroughOperation
from bindings.csw.polar_cs import PolarCs
from bindings.csw.prime_meridian import PrimeMeridian
from bindings.csw.reference_system import ReferenceSystem
from bindings.csw.show_type import ShowType
from bindings.csw.single_operation import SingleOperation
from bindings.csw.spherical_cs import SphericalCs
from bindings.csw.temporal_crs import TemporalCrs
from bindings.csw.temporal_cs import TemporalCs
from bindings.csw.temporal_datum import TemporalDatum
from bindings.csw.time_calendar import TimeCalendar
from bindings.csw.time_calendar_era import TimeCalendarEra
from bindings.csw.time_clock import TimeClock
from bindings.csw.time_coordinate_system import TimeCoordinateSystem
from bindings.csw.time_ordinal_reference_system import TimeOrdinalReferenceSystem
from bindings.csw.time_reference_system import TimeReferenceSystem
from bindings.csw.transformation import Transformation
from bindings.csw.type_type import TypeType
from bindings.csw.unit_definition import UnitDefinition
from bindings.csw.user_defined_cs import UserDefinedCs
from bindings.csw.vertical_crs import VerticalCrs
from bindings.csw.vertical_cs import VerticalCs
from bindings.csw.vertical_datum import VerticalDatum

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class DictionaryEntryType:
    """An entry in a dictionary of definitions.

    An instance of this type contains or refers to a definition object.
    The number of definitions contained in this dictionaryEntry is
    restricted to one, but a DefinitionCollection or Dictionary that
    contains multiple definitions can be substituted if needed.
    Specialized descendents of this dictionaryEntry might be restricted
    in an application schema to allow only including specified types of
    definitions as valid entries in a dictionary.

    :ivar time_calendar_era:
    :ivar time_clock:
    :ivar time_calendar:
    :ivar time_ordinal_reference_system:
    :ivar time_coordinate_system:
    :ivar time_reference_system:
    :ivar operation_parameter_group:
    :ivar operation_parameter:
    :ivar general_operation_parameter:
    :ivar operation_method:
    :ivar transformation:
    :ivar general_transformation:
    :ivar conversion:
    :ivar general_conversion:
    :ivar operation:
    :ivar pass_through_operation:
    :ivar single_operation:
    :ivar concatenated_operation:
    :ivar coordinate_operation:
    :ivar ellipsoid:
    :ivar prime_meridian:
    :ivar geodetic_datum:
    :ivar temporal_datum:
    :ivar vertical_datum:
    :ivar image_datum:
    :ivar engineering_datum:
    :ivar datum:
    :ivar oblique_cartesian_cs:
    :ivar cylindrical_cs:
    :ivar polar_cs:
    :ivar spherical_cs:
    :ivar user_defined_cs:
    :ivar linear_cs:
    :ivar temporal_cs:
    :ivar vertical_cs:
    :ivar cartesian_cs:
    :ivar ellipsoidal_cs:
    :ivar coordinate_system:
    :ivar coordinate_system_axis:
    :ivar compound_crs:
    :ivar temporal_crs:
    :ivar image_crs:
    :ivar engineering_crs:
    :ivar derived_crs:
    :ivar projected_crs:
    :ivar general_derived_crs:
    :ivar geocentric_crs:
    :ivar vertical_crs:
    :ivar geographic_crs:
    :ivar coordinate_reference_system:
    :ivar crs:
    :ivar reference_system:
    :ivar conventional_unit:
    :ivar derived_unit:
    :ivar base_unit:
    :ivar unit_definition:
    :ivar definition_proxy:
    :ivar definition_collection:
    :ivar dictionary:
    :ivar definition: This element in a dictionary entry contains the
        actual definition.
    :ivar type:
    :ivar href:
    :ivar role:
    :ivar arcrole:
    :ivar title:
    :ivar show:
    :ivar actuate:
    :ivar remote_schema:
    """
    time_calendar_era: Optional[TimeCalendarEra] = field(
        default=None,
        metadata={
            "name": "TimeCalendarEra",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    time_clock: Optional[TimeClock] = field(
        default=None,
        metadata={
            "name": "TimeClock",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    time_calendar: Optional[TimeCalendar] = field(
        default=None,
        metadata={
            "name": "TimeCalendar",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    time_ordinal_reference_system: Optional[TimeOrdinalReferenceSystem] = field(
        default=None,
        metadata={
            "name": "TimeOrdinalReferenceSystem",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    time_coordinate_system: Optional[TimeCoordinateSystem] = field(
        default=None,
        metadata={
            "name": "TimeCoordinateSystem",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    time_reference_system: Optional[TimeReferenceSystem] = field(
        default=None,
        metadata={
            "name": "_TimeReferenceSystem",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    operation_parameter_group: Optional[OperationParameterGroup] = field(
        default=None,
        metadata={
            "name": "OperationParameterGroup",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    operation_parameter: Optional[OperationParameter] = field(
        default=None,
        metadata={
            "name": "OperationParameter",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    general_operation_parameter: Optional[GeneralOperationParameter] = field(
        default=None,
        metadata={
            "name": "_GeneralOperationParameter",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    operation_method: Optional[OperationMethod] = field(
        default=None,
        metadata={
            "name": "OperationMethod",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    transformation: Optional[Transformation] = field(
        default=None,
        metadata={
            "name": "Transformation",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    general_transformation: Optional[GeneralTransformation] = field(
        default=None,
        metadata={
            "name": "_GeneralTransformation",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    conversion: Optional[Conversion] = field(
        default=None,
        metadata={
            "name": "Conversion",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    general_conversion: Optional[GeneralConversion] = field(
        default=None,
        metadata={
            "name": "_GeneralConversion",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    operation: Optional[Operation2] = field(
        default=None,
        metadata={
            "name": "_Operation",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    pass_through_operation: Optional[PassThroughOperation] = field(
        default=None,
        metadata={
            "name": "PassThroughOperation",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    single_operation: Optional[SingleOperation] = field(
        default=None,
        metadata={
            "name": "_SingleOperation",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    concatenated_operation: Optional[ConcatenatedOperation] = field(
        default=None,
        metadata={
            "name": "ConcatenatedOperation",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    coordinate_operation: Optional[CoordinateOperation] = field(
        default=None,
        metadata={
            "name": "_CoordinateOperation",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    ellipsoid: Optional[Ellipsoid] = field(
        default=None,
        metadata={
            "name": "Ellipsoid",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    prime_meridian: Optional[PrimeMeridian] = field(
        default=None,
        metadata={
            "name": "PrimeMeridian",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    geodetic_datum: Optional[GeodeticDatum] = field(
        default=None,
        metadata={
            "name": "GeodeticDatum",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    temporal_datum: Optional[TemporalDatum] = field(
        default=None,
        metadata={
            "name": "TemporalDatum",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    vertical_datum: Optional[VerticalDatum] = field(
        default=None,
        metadata={
            "name": "VerticalDatum",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    image_datum: Optional[ImageDatum] = field(
        default=None,
        metadata={
            "name": "ImageDatum",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    engineering_datum: Optional[EngineeringDatum] = field(
        default=None,
        metadata={
            "name": "EngineeringDatum",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    datum: Optional[Datum] = field(
        default=None,
        metadata={
            "name": "_Datum",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    oblique_cartesian_cs: Optional[ObliqueCartesianCs] = field(
        default=None,
        metadata={
            "name": "ObliqueCartesianCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    cylindrical_cs: Optional[CylindricalCs] = field(
        default=None,
        metadata={
            "name": "CylindricalCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    polar_cs: Optional[PolarCs] = field(
        default=None,
        metadata={
            "name": "PolarCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    spherical_cs: Optional[SphericalCs] = field(
        default=None,
        metadata={
            "name": "SphericalCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    user_defined_cs: Optional[UserDefinedCs] = field(
        default=None,
        metadata={
            "name": "UserDefinedCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    linear_cs: Optional[LinearCs] = field(
        default=None,
        metadata={
            "name": "LinearCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    temporal_cs: Optional[TemporalCs] = field(
        default=None,
        metadata={
            "name": "TemporalCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    vertical_cs: Optional[VerticalCs] = field(
        default=None,
        metadata={
            "name": "VerticalCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    cartesian_cs: Optional[CartesianCs] = field(
        default=None,
        metadata={
            "name": "CartesianCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    ellipsoidal_cs: Optional[EllipsoidalCs] = field(
        default=None,
        metadata={
            "name": "EllipsoidalCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    coordinate_system: Optional[CoordinateSystem] = field(
        default=None,
        metadata={
            "name": "_CoordinateSystem",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    coordinate_system_axis: Optional[CoordinateSystemAxis] = field(
        default=None,
        metadata={
            "name": "CoordinateSystemAxis",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    compound_crs: Optional[CompoundCrs] = field(
        default=None,
        metadata={
            "name": "CompoundCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    temporal_crs: Optional[TemporalCrs] = field(
        default=None,
        metadata={
            "name": "TemporalCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    image_crs: Optional[ImageCrs] = field(
        default=None,
        metadata={
            "name": "ImageCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    engineering_crs: Optional[EngineeringCrs] = field(
        default=None,
        metadata={
            "name": "EngineeringCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    derived_crs: Optional[DerivedCrs] = field(
        default=None,
        metadata={
            "name": "DerivedCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    projected_crs: Optional[ProjectedCrs] = field(
        default=None,
        metadata={
            "name": "ProjectedCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    general_derived_crs: Optional[GeneralDerivedCrs] = field(
        default=None,
        metadata={
            "name": "_GeneralDerivedCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    geocentric_crs: Optional[GeocentricCrs] = field(
        default=None,
        metadata={
            "name": "GeocentricCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    vertical_crs: Optional[VerticalCrs] = field(
        default=None,
        metadata={
            "name": "VerticalCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    geographic_crs: Optional[GeographicCrs] = field(
        default=None,
        metadata={
            "name": "GeographicCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    coordinate_reference_system: Optional[CoordinateReferenceSystem] = field(
        default=None,
        metadata={
            "name": "_CoordinateReferenceSystem",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    crs: Optional[Crs] = field(
        default=None,
        metadata={
            "name": "_CRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    reference_system: Optional[ReferenceSystem] = field(
        default=None,
        metadata={
            "name": "_ReferenceSystem",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    conventional_unit: Optional[ConventionalUnit] = field(
        default=None,
        metadata={
            "name": "ConventionalUnit",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    derived_unit: Optional[DerivedUnit] = field(
        default=None,
        metadata={
            "name": "DerivedUnit",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    base_unit: Optional[BaseUnit] = field(
        default=None,
        metadata={
            "name": "BaseUnit",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    unit_definition: Optional[UnitDefinition] = field(
        default=None,
        metadata={
            "name": "UnitDefinition",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    definition_proxy: Optional[DefinitionProxy] = field(
        default=None,
        metadata={
            "name": "DefinitionProxy",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    definition_collection: Optional["DefinitionCollection"] = field(
        default=None,
        metadata={
            "name": "DefinitionCollection",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    dictionary: Optional["Dictionary"] = field(
        default=None,
        metadata={
            "name": "Dictionary",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    definition: Optional[Definition] = field(
        default=None,
        metadata={
            "name": "Definition",
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


@dataclass
class DefinitionMember(DictionaryEntryType):
    class Meta:
        name = "definitionMember"
        namespace = "http://www.opengis.net/gml"


@dataclass
class DictionaryEntry(DictionaryEntryType):
    class Meta:
        name = "dictionaryEntry"
        namespace = "http://www.opengis.net/gml"


@dataclass
class DictionaryType(DefinitionType):
    """A non-abstract bag that is specialized for use as a dictionary which
    contains a set of definitions.

    These definitions are referenced from other places, in the same and
    different XML documents. In this restricted type, the inherited
    optional "description" element can be used for a description of this
    dictionary. The inherited optional "name" element can be used for
    the name(s) of this dictionary. The inherited "metaDataProperty"
    elements can be used to reference or contain more information about
    this dictionary. The inherited required gml:id attribute allows the
    dictionary to be referenced using this handle.

    :ivar definition_member:
    :ivar dictionary_entry: An entry in this dictionary. The content of
        an entry can itself be a lower level dictionary or definition
        collection. This element follows the standard GML property
        model, so the value may be provided directly or by reference.
        Note that if the value is provided by reference, this definition
        does not carry a handle (gml:id) in this context, so does not
        allow external references to this specific entry in this
        context. When used in this way the referenced definition will
        usually be in a dictionary in the same XML document.
    :ivar indirect_entry: An identified reference to a remote entry in
        this dictionary, to be used when this entry should be identified
        to allow external references to this specific entry.
    """
    definition_member: List[DefinitionMember] = field(
        default_factory=list,
        metadata={
            "name": "definitionMember",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "sequential": True,
        }
    )
    dictionary_entry: List[DictionaryEntry] = field(
        default_factory=list,
        metadata={
            "name": "dictionaryEntry",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "sequential": True,
        }
    )
    indirect_entry: List[IndirectEntry] = field(
        default_factory=list,
        metadata={
            "name": "indirectEntry",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "sequential": True,
        }
    )


@dataclass
class DefinitionCollection(DictionaryType):
    class Meta:
        namespace = "http://www.opengis.net/gml"


@dataclass
class Dictionary(DictionaryType):
    class Meta:
        namespace = "http://www.opengis.net/gml"
