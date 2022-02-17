from bindings.gmd.abstract_association_role import AbstractAssociationRole
from bindings.gmd.abstract_continuous_coverage import AbstractContinuousCoverage
from bindings.gmd.abstract_continuous_coverage_type import (
    AbstractContinuousCoverageType,
)
from bindings.gmd.abstract_coordinate_operation import AbstractCoordinateOperation
from bindings.gmd.abstract_coordinate_system import AbstractCoordinateSystem
from bindings.gmd.abstract_coordinate_system_type import AbstractCoordinateSystemType
from bindings.gmd.abstract_coverage import AbstractCoverage
from bindings.gmd.abstract_coverage_type import AbstractCoverageType
from bindings.gmd.abstract_crstype import (
    AbstractCrs,
    AbstractCrstype,
    AbstractCoordinateOperationType,
    AbstractDatumType,
    AbstractGeneralConversion,
    AbstractGeneralConversionType,
    AbstractGeneralDerivedCrs,
    AbstractGeneralDerivedCrstype,
    AbstractSingleCrs,
    CrspropertyType,
    CompoundCrs,
    CompoundCrstype,
    ConversionType,
    Conversion1,
    DerivedCrs,
    DerivedCrstype1,
    ExExtent,
    ExExtentType,
    ExVerticalExtent,
    ExVerticalExtentPropertyType,
    ExVerticalExtentType,
    EngineeringCrs,
    EngineeringCrstype,
    EngineeringDatumPropertyType,
    EngineeringDatumType,
    EngineeringDatum1,
    GeneralConversionPropertyType,
    GeocentricCrs,
    GeocentricCrstype,
    GeodeticCrs,
    GeodeticCrspropertyType,
    GeodeticCrstype,
    GeodeticDatumPropertyType,
    GeodeticDatumType,
    GeodeticDatum1,
    GeographicCrs,
    GeographicCrspropertyType,
    GeographicCrstype,
    ImageCrs,
    ImageCrstype,
    ImageDatumPropertyType,
    ImageDatumType,
    ImageDatum1,
    ProjectedCrs,
    ProjectedCrstype,
    ScCrsPropertyType,
    SingleCrspropertyType,
    TemporalCrs,
    TemporalCrstype,
    TemporalDatumBaseType,
    TemporalDatumPropertyType,
    TemporalDatumType,
    TemporalDatum1,
    VerticalCrs,
    VerticalCrstype,
    VerticalDatumPropertyType,
    VerticalDatumType,
    VerticalDatum1,
    BaseCrs,
    BaseGeodeticCrs,
    BaseGeographicCrs,
    ComponentReferenceSystem,
    Conversion2,
    DefinedByConversion,
    DomainOfValidity,
    EngineeringDatum2,
    GeodeticDatum2,
    ImageDatum2,
    IncludesSingleCrs,
    SourceCrs,
    TargetCrs,
    TemporalDatum2,
    UsesEngineeringDatum,
    UsesGeodeticDatum,
    UsesImageDatum,
    UsesTemporalDatum,
    UsesVerticalDatum,
    VerticalDatum2,
)
from bindings.gmd.abstract_curve import AbstractCurve
from bindings.gmd.abstract_curve_segment import AbstractCurveSegment
from bindings.gmd.abstract_curve_segment_type import AbstractCurveSegmentType
from bindings.gmd.abstract_curve_type import AbstractCurveType
from bindings.gmd.abstract_datum import AbstractDatum
from bindings.gmd.abstract_discrete_coverage import AbstractDiscreteCoverage
from bindings.gmd.abstract_discrete_coverage_type import AbstractDiscreteCoverageType
from bindings.gmd.abstract_dq_completeness import AbstractDqCompleteness
from bindings.gmd.abstract_dq_completeness_type import AbstractDqCompletenessType
from bindings.gmd.abstract_dq_element import AbstractDqElement
from bindings.gmd.abstract_dq_element_type import AbstractDqElementType
from bindings.gmd.abstract_dq_logical_consistency import AbstractDqLogicalConsistency
from bindings.gmd.abstract_dq_logical_consistency_type import (
    AbstractDqLogicalConsistencyType,
)
from bindings.gmd.abstract_dq_positional_accuracy import AbstractDqPositionalAccuracy
from bindings.gmd.abstract_dq_positional_accuracy_type import (
    AbstractDqPositionalAccuracyType,
)
from bindings.gmd.abstract_dq_result import AbstractDqResult
from bindings.gmd.abstract_dq_result_type import AbstractDqResultType
from bindings.gmd.abstract_dq_temporal_accuracy import AbstractDqTemporalAccuracy
from bindings.gmd.abstract_dq_temporal_accuracy_type import (
    AbstractDqTemporalAccuracyType,
)
from bindings.gmd.abstract_dq_thematic_accuracy import AbstractDqThematicAccuracy
from bindings.gmd.abstract_dq_thematic_accuracy_type import (
    AbstractDqThematicAccuracyType,
)
from bindings.gmd.abstract_ex_geographic_extent import AbstractExGeographicExtent
from bindings.gmd.abstract_ex_geographic_extent_type import (
    AbstractExGeographicExtentType,
)
from bindings.gmd.abstract_feature import AbstractFeature
from bindings.gmd.abstract_feature_member_type import AbstractFeatureMemberType
from bindings.gmd.abstract_feature_type import AbstractFeatureType
from bindings.gmd.abstract_general_operation_parameter import (
    AbstractGeneralOperationParameter,
)
from bindings.gmd.abstract_general_operation_parameter_property_type import (
    AbstractGeneralOperationParameterPropertyType,
    OperationParameterGroup,
    OperationParameterGroupType,
    GeneralOperationParameter,
    UsesParameter,
)
from bindings.gmd.abstract_general_operation_parameter_ref import (
    AbstractGeneralOperationParameterRef,
)
from bindings.gmd.abstract_general_operation_parameter_type import (
    AbstractGeneralOperationParameterType,
)
from bindings.gmd.abstract_general_parameter_value import AbstractGeneralParameterValue
from bindings.gmd.abstract_general_parameter_value_property_type import (
    AbstractGeneralParameterValuePropertyType,
    ParameterValueGroup,
    ParameterValueGroupType,
    IncludesValue,
    ParameterValue2,
    UsesValue,
)
from bindings.gmd.abstract_general_parameter_value_type import (
    AbstractGeneralParameterValueType,
)
from bindings.gmd.abstract_general_transformation import AbstractGeneralTransformation
from bindings.gmd.abstract_general_transformation_type import (
    AbstractGeneralTransformationType,
)
from bindings.gmd.abstract_generic_name import AbstractGenericName
from bindings.gmd.abstract_geometric_aggregate import AbstractGeometricAggregate
from bindings.gmd.abstract_geometric_aggregate_type import (
    AbstractGeometricAggregateType,
)
from bindings.gmd.abstract_geometric_primitive import AbstractGeometricPrimitive
from bindings.gmd.abstract_geometric_primitive_type import (
    AbstractGeometricPrimitiveType,
)
from bindings.gmd.abstract_geometry import AbstractGeometry
from bindings.gmd.abstract_geometry_type import AbstractGeometryType
from bindings.gmd.abstract_gml import AbstractGml
from bindings.gmd.abstract_gmltype import AbstractGmltype
from bindings.gmd.abstract_gridded_surface import AbstractGriddedSurface
from bindings.gmd.abstract_gridded_surface_type import AbstractGriddedSurfaceType
from bindings.gmd.abstract_implicit_geometry import AbstractImplicitGeometry
from bindings.gmd.abstract_inline_property import AbstractInlineProperty
from bindings.gmd.abstract_md_content_information import AbstractMdContentInformation
from bindings.gmd.abstract_md_content_information_type import (
    AbstractMdContentInformationType,
)
from bindings.gmd.abstract_md_identification import AbstractMdIdentification
from bindings.gmd.abstract_md_identification_type import AbstractMdIdentificationType
from bindings.gmd.abstract_md_spatial_representation import (
    AbstractMdSpatialRepresentation,
)
from bindings.gmd.abstract_md_spatial_representation_type import (
    AbstractMdSpatialRepresentationType,
)
from bindings.gmd.abstract_member_type import AbstractMemberType
from bindings.gmd.abstract_meta_data import AbstractMetaData
from bindings.gmd.abstract_meta_data_type import AbstractMetaDataType
from bindings.gmd.abstract_metadata_property_type import AbstractMetadataPropertyType
from bindings.gmd.abstract_object_1 import AbstractObject1
from bindings.gmd.abstract_object_2 import AbstractObject2
from bindings.gmd.abstract_object_type import AbstractObjectType
from bindings.gmd.abstract_operation import AbstractOperation
from bindings.gmd.abstract_parametric_curve_surface import (
    AbstractParametricCurveSurface,
)
from bindings.gmd.abstract_parametric_curve_surface_type import (
    AbstractParametricCurveSurfaceType,
)
from bindings.gmd.abstract_reference import AbstractReference
from bindings.gmd.abstract_ring import AbstractRing
from bindings.gmd.abstract_ring_property_type import AbstractRingPropertyType
from bindings.gmd.abstract_ring_type import AbstractRingType
from bindings.gmd.abstract_rs_reference_system import AbstractRsReferenceSystem
from bindings.gmd.abstract_rs_reference_system_type import AbstractRsReferenceSystemType
from bindings.gmd.abstract_scalar_value import AbstractScalarValue
from bindings.gmd.abstract_scalar_value_list import AbstractScalarValueList
from bindings.gmd.abstract_single_operation import AbstractSingleOperation
from bindings.gmd.abstract_solid import AbstractSolid
from bindings.gmd.abstract_solid_type import AbstractSolidType
from bindings.gmd.abstract_strict_association_role import AbstractStrictAssociationRole
from bindings.gmd.abstract_surface import AbstractSurface
from bindings.gmd.abstract_surface_patch import AbstractSurfacePatch
from bindings.gmd.abstract_surface_patch_type import AbstractSurfacePatchType
from bindings.gmd.abstract_surface_type import AbstractSurfaceType
from bindings.gmd.abstract_time_complex import AbstractTimeComplex
from bindings.gmd.abstract_time_complex_type import AbstractTimeComplexType
from bindings.gmd.abstract_time_object import AbstractTimeObject
from bindings.gmd.abstract_time_object_type import AbstractTimeObjectType
from bindings.gmd.abstract_time_slice import AbstractTimeSlice
from bindings.gmd.abstract_time_slice_type import AbstractTimeSliceType
from bindings.gmd.abstract_topo_primitive import AbstractTopoPrimitive
from bindings.gmd.abstract_topology import AbstractTopology
from bindings.gmd.abstract_topology_type import AbstractTopologyType
from bindings.gmd.abstract_value import AbstractValue
from bindings.gmd.actuate_value import ActuateValue
from bindings.gmd.affine_cs_1 import AffineCs1
from bindings.gmd.affine_cs_2 import AffineCs2
from bindings.gmd.affine_csproperty_type import AffineCspropertyType
from bindings.gmd.affine_cstype import AffineCstype
from bindings.gmd.affine_placement import AffinePlacement
from bindings.gmd.affine_placement_type import AffinePlacementType
from bindings.gmd.aggregation_type import AggregationType
from bindings.gmd.anchor_definition import AnchorDefinition
from bindings.gmd.anchor_point import AnchorPoint
from bindings.gmd.angle_1 import Angle1
from bindings.gmd.angle_2 import Angle2
from bindings.gmd.angle_choice_type import AngleChoiceType
from bindings.gmd.angle_property_type import AnglePropertyType
from bindings.gmd.angle_type import AngleType
from bindings.gmd.arc import Arc
from bindings.gmd.arc_by_bulge import ArcByBulge
from bindings.gmd.arc_by_bulge_type import ArcByBulgeType
from bindings.gmd.arc_by_center_point import ArcByCenterPoint
from bindings.gmd.arc_by_center_point_type import ArcByCenterPointType
from bindings.gmd.arc_string import ArcString
from bindings.gmd.arc_string_by_bulge import ArcStringByBulge
from bindings.gmd.arc_string_by_bulge_type import ArcStringByBulgeType
from bindings.gmd.arc_string_type import ArcStringType
from bindings.gmd.arc_type import ArcType
from bindings.gmd.area_type import AreaType
from bindings.gmd.association_name import AssociationName
from bindings.gmd.axis import Axis
from bindings.gmd.axis_abbrev import AxisAbbrev
from bindings.gmd.axis_direction import AxisDirection
from bindings.gmd.bag_type import (
    AbstractFeatureCollection,
    AbstractFeatureCollectionType,
    Array,
    ArrayAssociationType,
    ArrayType,
    AssociationRoleType,
    Bag,
    BagType,
    DirectedObservation,
    DirectedObservationAtDistance,
    DirectedObservationAtDistanceType,
    DirectedObservationType,
    FeatureArrayPropertyType,
    FeatureCollection,
    FeatureCollectionType,
    FeaturePropertyType,
    Observation,
    ObservationType,
    ProcedurePropertyType,
    ResultType,
    TargetPropertyType,
    FeatureMember,
    FeatureMembers,
    Member,
    Members,
    ResultOf,
    Subject,
    Target,
    Using,
)
from bindings.gmd.base_unit import BaseUnit
from bindings.gmd.base_unit_type import BaseUnitType
from bindings.gmd.bezier import Bezier
from bindings.gmd.bezier_type import BezierType
from bindings.gmd.binary import Binary
from bindings.gmd.binary_property_type import BinaryPropertyType
from bindings.gmd.binary_type import BinaryType
from bindings.gmd.boolean_1 import Boolean1
from bindings.gmd.boolean_2 import Boolean2
from bindings.gmd.boolean_list import BooleanList
from bindings.gmd.boolean_property_type_1 import BooleanPropertyType1
from bindings.gmd.boolean_property_type_2 import BooleanPropertyType2
from bindings.gmd.boolean_value import BooleanValue
from bindings.gmd.bounded_by import BoundedBy
from bindings.gmd.bounded_feature_type import BoundedFeatureType
from bindings.gmd.bounding_shape_type import BoundingShapeType
from bindings.gmd.bspline import Bspline
from bindings.gmd.bspline_type import BsplineType
from bindings.gmd.cartesian_cs_1 import CartesianCs1
from bindings.gmd.cartesian_cs_2 import CartesianCs2
from bindings.gmd.cartesian_csproperty_type import CartesianCspropertyType
from bindings.gmd.cartesian_csref import CartesianCsref
from bindings.gmd.cartesian_cstype import CartesianCstype
from bindings.gmd.catalog_symbol import CatalogSymbol
from bindings.gmd.category import Category
from bindings.gmd.category_extent import CategoryExtent
from bindings.gmd.category_extent_type import CategoryExtentType
from bindings.gmd.category_list import CategoryList
from bindings.gmd.category_property_type import CategoryPropertyType
from bindings.gmd.center_line_of import CenterLineOf
from bindings.gmd.center_of import CenterOf
from bindings.gmd.character_string import CharacterString
from bindings.gmd.character_string_property_type import CharacterStringPropertyType
from bindings.gmd.ci_address import CiAddress
from bindings.gmd.ci_address_property_type import CiAddressPropertyType
from bindings.gmd.ci_address_type import CiAddressType
from bindings.gmd.ci_citation_type import (
    CiCitation,
    CiCitationPropertyType,
    CiCitationType,
    MdIdentifier,
    MdIdentifierPropertyType,
    MdIdentifierType,
    RsIdentifier,
    RsIdentifierType,
)
from bindings.gmd.ci_contact import CiContact
from bindings.gmd.ci_contact_property_type import CiContactPropertyType
from bindings.gmd.ci_contact_type import CiContactType
from bindings.gmd.ci_date import CiDate
from bindings.gmd.ci_date_property_type import CiDatePropertyType
from bindings.gmd.ci_date_type import CiDateType
from bindings.gmd.ci_date_type_code import CiDateTypeCode
from bindings.gmd.ci_date_type_code_property_type import CiDateTypeCodePropertyType
from bindings.gmd.ci_on_line_function_code import CiOnLineFunctionCode
from bindings.gmd.ci_on_line_function_code_property_type import (
    CiOnLineFunctionCodePropertyType,
)
from bindings.gmd.ci_online_resource import CiOnlineResource
from bindings.gmd.ci_online_resource_property_type import CiOnlineResourcePropertyType
from bindings.gmd.ci_online_resource_type import CiOnlineResourceType
from bindings.gmd.ci_presentation_form_code import CiPresentationFormCode
from bindings.gmd.ci_presentation_form_code_property_type import (
    CiPresentationFormCodePropertyType,
)
from bindings.gmd.ci_responsible_party import CiResponsibleParty
from bindings.gmd.ci_responsible_party_property_type import (
    CiResponsiblePartyPropertyType,
)
from bindings.gmd.ci_responsible_party_type import CiResponsiblePartyType
from bindings.gmd.ci_role_code import CiRoleCode
from bindings.gmd.ci_role_code_property_type import CiRoleCodePropertyType
from bindings.gmd.ci_series import CiSeries
from bindings.gmd.ci_series_property_type import CiSeriesPropertyType
from bindings.gmd.ci_series_type import CiSeriesType
from bindings.gmd.ci_telephone import CiTelephone
from bindings.gmd.ci_telephone_property_type import CiTelephonePropertyType
from bindings.gmd.ci_telephone_type import CiTelephoneType
from bindings.gmd.circle import Circle
from bindings.gmd.circle_by_center_point import CircleByCenterPoint
from bindings.gmd.circle_by_center_point_type import CircleByCenterPointType
from bindings.gmd.circle_type import CircleType
from bindings.gmd.clothoid import Clothoid
from bindings.gmd.clothoid_type import ClothoidType
from bindings.gmd.code_list_type import CodeListType
from bindings.gmd.code_list_value_type import CodeListValueType
from bindings.gmd.code_or_nil_reason_list_type import CodeOrNilReasonListType
from bindings.gmd.code_type import CodeType
from bindings.gmd.code_with_authority_type import CodeWithAuthorityType
from bindings.gmd.compass_point_enumeration import CompassPointEnumeration
from bindings.gmd.composite_curve_type import (
    CompositeCurve,
    CompositeCurveType,
    Curve,
    CurvePropertyType,
    CurveSegmentArrayPropertyType,
    CurveType,
    OffsetCurve,
    OffsetCurveType,
    OrientableCurve,
    OrientableCurveType,
    BaseCurve,
    CurveMember,
    Segments,
)
from bindings.gmd.composite_surface_type import (
    CompositeSurface,
    CompositeSurfaceType,
    OrientableSurface,
    OrientableSurfaceType,
    SurfacePropertyType,
    BaseSurface,
    SurfaceMember,
)
from bindings.gmd.compound_crsproperty_type import CompoundCrspropertyType
from bindings.gmd.compound_crsref import CompoundCrsref
from bindings.gmd.concatenated_operation_property_type import (
    ConcatenatedOperationPropertyType,
)
from bindings.gmd.concatenated_operation_ref import ConcatenatedOperationRef
from bindings.gmd.cone import Cone
from bindings.gmd.cone_type import ConeType
from bindings.gmd.container_property_type import (
    AbstractTopoPrimitiveType,
    ContainerPropertyType,
    DirectedEdgePropertyType,
    DirectedFacePropertyType,
    DirectedNodePropertyType,
    DirectedTopoSolidPropertyType,
    Edge,
    EdgeType,
    Face,
    FaceType,
    IsolatedPropertyType,
    Node,
    NodeType,
    TopoSolid,
    TopoSolidType,
    Container,
    DirectedEdge,
    DirectedFace,
    DirectedNode,
    DirectedTopoSolid,
    Isolated,
)
from bindings.gmd.conventional_unit import ConventionalUnit
from bindings.gmd.conventional_unit_type import ConventionalUnitType
from bindings.gmd.conversion_property_type import ConversionPropertyType
from bindings.gmd.conversion_ref import ConversionRef
from bindings.gmd.conversion_to_preferred_unit import ConversionToPreferredUnit
from bindings.gmd.conversion_to_preferred_unit_type import ConversionToPreferredUnitType
from bindings.gmd.coordinate_operation_accuracy import CoordinateOperationAccuracy
from bindings.gmd.coordinate_operation_ref import CoordinateOperationRef
from bindings.gmd.coordinate_system import CoordinateSystem
from bindings.gmd.coordinate_system_axis import CoordinateSystemAxis
from bindings.gmd.coordinate_system_axis_property_type import (
    CoordinateSystemAxisPropertyType,
)
from bindings.gmd.coordinate_system_axis_ref import CoordinateSystemAxisRef
from bindings.gmd.coordinate_system_axis_type import CoordinateSystemAxisType
from bindings.gmd.coordinate_system_property_type import CoordinateSystemPropertyType
from bindings.gmd.coordinate_system_ref import CoordinateSystemRef
from bindings.gmd.coordinates import Coordinates
from bindings.gmd.coordinates_type import CoordinatesType
from bindings.gmd.count import Count
from bindings.gmd.count_extent import CountExtent
from bindings.gmd.count_list import CountList
from bindings.gmd.count_property_type import CountPropertyType
from bindings.gmd.country import Country
from bindings.gmd.country_property_type import CountryPropertyType
from bindings.gmd.coverage_function import CoverageFunction
from bindings.gmd.coverage_function_type import CoverageFunctionType
from bindings.gmd.coverage_mapping_rule import CoverageMappingRule
from bindings.gmd.crs_ref import CrsRef
from bindings.gmd.cubic_spline import CubicSpline
from bindings.gmd.cubic_spline_type import CubicSplineType
from bindings.gmd.curve_array_property import CurveArrayProperty
from bindings.gmd.curve_array_property_type import CurveArrayPropertyType
from bindings.gmd.curve_interpolation_type import CurveInterpolationType
from bindings.gmd.curve_members import CurveMembers
from bindings.gmd.curve_property import CurveProperty
from bindings.gmd.cylinder import Cylinder
from bindings.gmd.cylinder_type import CylinderType
from bindings.gmd.cylindrical_cs import CylindricalCs
from bindings.gmd.cylindrical_csproperty_type import CylindricalCspropertyType
from bindings.gmd.cylindrical_csref import CylindricalCsref
from bindings.gmd.cylindrical_cstype import CylindricalCstype
from bindings.gmd.data_block import DataBlock
from bindings.gmd.data_block_type import DataBlockType
from bindings.gmd.data_source import DataSource
from bindings.gmd.data_source_reference import DataSourceReference
from bindings.gmd.date import Date
from bindings.gmd.date_property_type import DatePropertyType
from bindings.gmd.date_time import DateTime
from bindings.gmd.date_time_property_type import DateTimePropertyType
from bindings.gmd.datum_property_type import DatumPropertyType
from bindings.gmd.datum_ref import DatumRef
from bindings.gmd.decimal import DecimalType
from bindings.gmd.decimal_minutes import DecimalMinutes
from bindings.gmd.decimal_property_type import DecimalPropertyType
from bindings.gmd.default_code_space import DefaultCodeSpace
from bindings.gmd.definition import Definition
from bindings.gmd.definition_base_type import DefinitionBaseType
from bindings.gmd.definition_proxy import DefinitionProxy
from bindings.gmd.definition_proxy_type import DefinitionProxyType
from bindings.gmd.definition_ref import DefinitionRef
from bindings.gmd.definition_type import DefinitionType
from bindings.gmd.degrees import Degrees
from bindings.gmd.degrees_type import DegreesType
from bindings.gmd.degrees_type_direction import DegreesTypeDirection
from bindings.gmd.derivation_unit_term import DerivationUnitTerm
from bindings.gmd.derivation_unit_term_type import DerivationUnitTermType
from bindings.gmd.derived_crsproperty_type import DerivedCrspropertyType
from bindings.gmd.derived_crsref import DerivedCrsref
from bindings.gmd.derived_crstype import DerivedCrstype
from bindings.gmd.derived_unit import DerivedUnit
from bindings.gmd.derived_unit_type import DerivedUnitType
from bindings.gmd.description import Description
from bindings.gmd.description_reference import DescriptionReference
from bindings.gmd.dictionary_entry_type import (
    DefinitionCollection,
    Dictionary,
    DictionaryEntryType,
    DictionaryType,
    DefinitionMember,
    DictionaryEntry,
)
from bindings.gmd.direct_position_list_type import DirectPositionListType
from bindings.gmd.direct_position_type import DirectPositionType
from bindings.gmd.direction import Direction
from bindings.gmd.direction_description_type import DirectionDescriptionType
from bindings.gmd.direction_property_type import DirectionPropertyType
from bindings.gmd.direction_vector_type import DirectionVectorType
from bindings.gmd.distance import Distance
from bindings.gmd.distance_property_type import DistancePropertyType
from bindings.gmd.dms_angle import DmsAngle
from bindings.gmd.dms_angle_value import DmsAngleValue
from bindings.gmd.dmsangle_type import DmsangleType
from bindings.gmd.domain_set import DomainSet
from bindings.gmd.domain_set_type import DomainSetType
from bindings.gmd.double_or_nil_reason_tuple_list import DoubleOrNilReasonTupleList
from bindings.gmd.dq_absolute_external_positional_accuracy import (
    DqAbsoluteExternalPositionalAccuracy,
)
from bindings.gmd.dq_absolute_external_positional_accuracy_property_type import (
    DqAbsoluteExternalPositionalAccuracyPropertyType,
)
from bindings.gmd.dq_absolute_external_positional_accuracy_type import (
    DqAbsoluteExternalPositionalAccuracyType,
)
from bindings.gmd.dq_accuracy_of_atime_measurement import DqAccuracyOfAtimeMeasurement
from bindings.gmd.dq_accuracy_of_atime_measurement_property_type import (
    DqAccuracyOfAtimeMeasurementPropertyType,
)
from bindings.gmd.dq_accuracy_of_atime_measurement_type import (
    DqAccuracyOfAtimeMeasurementType,
)
from bindings.gmd.dq_completeness_commission import DqCompletenessCommission
from bindings.gmd.dq_completeness_commission_property_type import (
    DqCompletenessCommissionPropertyType,
)
from bindings.gmd.dq_completeness_commission_type import DqCompletenessCommissionType
from bindings.gmd.dq_completeness_omission import DqCompletenessOmission
from bindings.gmd.dq_completeness_omission_property_type import (
    DqCompletenessOmissionPropertyType,
)
from bindings.gmd.dq_completeness_omission_type import DqCompletenessOmissionType
from bindings.gmd.dq_completeness_property_type import DqCompletenessPropertyType
from bindings.gmd.dq_conceptual_consistency import DqConceptualConsistency
from bindings.gmd.dq_conceptual_consistency_property_type import (
    DqConceptualConsistencyPropertyType,
)
from bindings.gmd.dq_conceptual_consistency_type import DqConceptualConsistencyType
from bindings.gmd.dq_conformance_result import DqConformanceResult
from bindings.gmd.dq_conformance_result_property_type import (
    DqConformanceResultPropertyType,
)
from bindings.gmd.dq_conformance_result_type import DqConformanceResultType
from bindings.gmd.dq_data_quality import DqDataQuality
from bindings.gmd.dq_data_quality_property_type import DqDataQualityPropertyType
from bindings.gmd.dq_data_quality_type import DqDataQualityType
from bindings.gmd.dq_domain_consistency import DqDomainConsistency
from bindings.gmd.dq_domain_consistency_property_type import (
    DqDomainConsistencyPropertyType,
)
from bindings.gmd.dq_domain_consistency_type import DqDomainConsistencyType
from bindings.gmd.dq_element_property_type import DqElementPropertyType
from bindings.gmd.dq_evaluation_method_type_code import DqEvaluationMethodTypeCode
from bindings.gmd.dq_evaluation_method_type_code_property_type import (
    DqEvaluationMethodTypeCodePropertyType,
)
from bindings.gmd.dq_format_consistency import DqFormatConsistency
from bindings.gmd.dq_format_consistency_property_type import (
    DqFormatConsistencyPropertyType,
)
from bindings.gmd.dq_format_consistency_type import DqFormatConsistencyType
from bindings.gmd.dq_gridded_data_positional_accuracy import (
    DqGriddedDataPositionalAccuracy,
)
from bindings.gmd.dq_gridded_data_positional_accuracy_property_type import (
    DqGriddedDataPositionalAccuracyPropertyType,
)
from bindings.gmd.dq_gridded_data_positional_accuracy_type import (
    DqGriddedDataPositionalAccuracyType,
)
from bindings.gmd.dq_logical_consistency_property_type import (
    DqLogicalConsistencyPropertyType,
)
from bindings.gmd.dq_non_quantitative_attribute_accuracy import (
    DqNonQuantitativeAttributeAccuracy,
)
from bindings.gmd.dq_non_quantitative_attribute_accuracy_property_type import (
    DqNonQuantitativeAttributeAccuracyPropertyType,
)
from bindings.gmd.dq_non_quantitative_attribute_accuracy_type import (
    DqNonQuantitativeAttributeAccuracyType,
)
from bindings.gmd.dq_positional_accuracy_property_type import (
    DqPositionalAccuracyPropertyType,
)
from bindings.gmd.dq_quantitative_attribute_accuracy import (
    DqQuantitativeAttributeAccuracy,
)
from bindings.gmd.dq_quantitative_attribute_accuracy_property_type import (
    DqQuantitativeAttributeAccuracyPropertyType,
)
from bindings.gmd.dq_quantitative_attribute_accuracy_type import (
    DqQuantitativeAttributeAccuracyType,
)
from bindings.gmd.dq_quantitative_result import DqQuantitativeResult
from bindings.gmd.dq_quantitative_result_property_type import (
    DqQuantitativeResultPropertyType,
)
from bindings.gmd.dq_quantitative_result_type import DqQuantitativeResultType
from bindings.gmd.dq_relative_internal_positional_accuracy import (
    DqRelativeInternalPositionalAccuracy,
)
from bindings.gmd.dq_relative_internal_positional_accuracy_property_type import (
    DqRelativeInternalPositionalAccuracyPropertyType,
)
from bindings.gmd.dq_relative_internal_positional_accuracy_type import (
    DqRelativeInternalPositionalAccuracyType,
)
from bindings.gmd.dq_result_property_type import DqResultPropertyType
from bindings.gmd.dq_scope import DqScope
from bindings.gmd.dq_scope_property_type import DqScopePropertyType
from bindings.gmd.dq_scope_type import DqScopeType
from bindings.gmd.dq_temporal_accuracy_property_type import (
    DqTemporalAccuracyPropertyType,
)
from bindings.gmd.dq_temporal_consistency import DqTemporalConsistency
from bindings.gmd.dq_temporal_consistency_property_type import (
    DqTemporalConsistencyPropertyType,
)
from bindings.gmd.dq_temporal_consistency_type import DqTemporalConsistencyType
from bindings.gmd.dq_temporal_validity import DqTemporalValidity
from bindings.gmd.dq_temporal_validity_property_type import (
    DqTemporalValidityPropertyType,
)
from bindings.gmd.dq_temporal_validity_type import DqTemporalValidityType
from bindings.gmd.dq_thematic_accuracy_property_type import (
    DqThematicAccuracyPropertyType,
)
from bindings.gmd.dq_thematic_classification_correctness import (
    DqThematicClassificationCorrectness,
)
from bindings.gmd.dq_thematic_classification_correctness_property_type import (
    DqThematicClassificationCorrectnessPropertyType,
)
from bindings.gmd.dq_thematic_classification_correctness_type import (
    DqThematicClassificationCorrectnessType,
)
from bindings.gmd.dq_topological_consistency import DqTopologicalConsistency
from bindings.gmd.dq_topological_consistency_property_type import (
    DqTopologicalConsistencyPropertyType,
)
from bindings.gmd.dq_topological_consistency_type import DqTopologicalConsistencyType
from bindings.gmd.ds_association import DsAssociation
from bindings.gmd.ds_association_property_type import DsAssociationPropertyType
from bindings.gmd.ds_association_type import DsAssociationType
from bindings.gmd.ds_association_type_code import DsAssociationTypeCode
from bindings.gmd.ds_association_type_code_property_type import (
    DsAssociationTypeCodePropertyType,
)
from bindings.gmd.ds_initiative_property_type import DsInitiativePropertyType
from bindings.gmd.ds_initiative_type_code import DsInitiativeTypeCode
from bindings.gmd.ds_initiative_type_code_property_type import (
    DsInitiativeTypeCodePropertyType,
)
from bindings.gmd.ds_other_aggregate_property_type import DsOtherAggregatePropertyType
from bindings.gmd.ds_platform_property_type import DsPlatformPropertyType
from bindings.gmd.ds_production_series_property_type import (
    DsProductionSeriesPropertyType,
)
from bindings.gmd.ds_sensor_property_type import DsSensorPropertyType
from bindings.gmd.ds_series_property_type import DsSeriesPropertyType
from bindings.gmd.ds_stereo_mate_property_type import DsStereoMatePropertyType
from bindings.gmd.duration import Duration
from bindings.gmd.dynamic_feature import DynamicFeature
from bindings.gmd.dynamic_feature_member_type import (
    DynamicFeatureCollection,
    DynamicFeatureCollectionType,
    DynamicFeatureMemberType,
    DynamicMembers,
)
from bindings.gmd.dynamic_feature_type import DynamicFeatureType
from bindings.gmd.edge_of import EdgeOf
from bindings.gmd.ellipsoid_1 import Ellipsoid1
from bindings.gmd.ellipsoid_2 import Ellipsoid2
from bindings.gmd.ellipsoid_property_type import EllipsoidPropertyType
from bindings.gmd.ellipsoid_ref import EllipsoidRef
from bindings.gmd.ellipsoid_type import EllipsoidType
from bindings.gmd.ellipsoidal_cs_1 import EllipsoidalCs1
from bindings.gmd.ellipsoidal_cs_2 import EllipsoidalCs2
from bindings.gmd.ellipsoidal_csproperty_type import EllipsoidalCspropertyType
from bindings.gmd.ellipsoidal_csref import EllipsoidalCsref
from bindings.gmd.ellipsoidal_cstype import EllipsoidalCstype
from bindings.gmd.engineering_crsproperty_type import EngineeringCrspropertyType
from bindings.gmd.engineering_crsref import EngineeringCrsref
from bindings.gmd.engineering_datum_ref import EngineeringDatumRef
from bindings.gmd.envelope import Envelope
from bindings.gmd.envelope_type import EnvelopeType
from bindings.gmd.envelope_with_time_period import EnvelopeWithTimePeriod
from bindings.gmd.envelope_with_time_period_type import EnvelopeWithTimePeriodType
from bindings.gmd.ex_bounding_polygon import ExBoundingPolygon
from bindings.gmd.ex_bounding_polygon_property_type import ExBoundingPolygonPropertyType
from bindings.gmd.ex_bounding_polygon_type import ExBoundingPolygonType
from bindings.gmd.ex_extent_property_type import ExExtentPropertyType
from bindings.gmd.ex_geographic_bounding_box import ExGeographicBoundingBox
from bindings.gmd.ex_geographic_bounding_box_property_type import (
    ExGeographicBoundingBoxPropertyType,
)
from bindings.gmd.ex_geographic_bounding_box_type import ExGeographicBoundingBoxType
from bindings.gmd.ex_geographic_description import ExGeographicDescription
from bindings.gmd.ex_geographic_description_property_type import (
    ExGeographicDescriptionPropertyType,
)
from bindings.gmd.ex_geographic_description_type import ExGeographicDescriptionType
from bindings.gmd.ex_geographic_extent_property_type import (
    ExGeographicExtentPropertyType,
)
from bindings.gmd.ex_spatial_temporal_extent import ExSpatialTemporalExtent
from bindings.gmd.ex_spatial_temporal_extent_property_type import (
    ExSpatialTemporalExtentPropertyType,
)
from bindings.gmd.ex_spatial_temporal_extent_type import ExSpatialTemporalExtentType
from bindings.gmd.ex_temporal_extent import ExTemporalExtent
from bindings.gmd.ex_temporal_extent_property_type import ExTemporalExtentPropertyType
from bindings.gmd.ex_temporal_extent_type import ExTemporalExtentType
from bindings.gmd.extent_of import ExtentOf
from bindings.gmd.exterior import Exterior
from bindings.gmd.feature_property import FeatureProperty
from bindings.gmd.file import File
from bindings.gmd.file_type import FileType
from bindings.gmd.file_value_model_type import FileValueModelType
from bindings.gmd.formula import Formula
from bindings.gmd.formula_type import FormulaType
from bindings.gmd.general_conversion_ref import GeneralConversionRef
from bindings.gmd.general_transformation_property_type import (
    GeneralTransformationPropertyType,
)
from bindings.gmd.general_transformation_ref import GeneralTransformationRef
from bindings.gmd.generic_meta_data import GenericMetaData
from bindings.gmd.generic_meta_data_type import GenericMetaDataType
from bindings.gmd.generic_name_property_type import GenericNamePropertyType
from bindings.gmd.geocentric_crsproperty_type import GeocentricCrspropertyType
from bindings.gmd.geocentric_crsref import GeocentricCrsref
from bindings.gmd.geodesic import Geodesic
from bindings.gmd.geodesic_string import GeodesicString
from bindings.gmd.geodesic_string_type import GeodesicStringType
from bindings.gmd.geodesic_type import GeodesicType
from bindings.gmd.geodetic_datum_ref import GeodeticDatumRef
from bindings.gmd.geographic_crsref import GeographicCrsref
from bindings.gmd.geometric_complex import GeometricComplex
from bindings.gmd.geometric_complex_property_type import GeometricComplexPropertyType
from bindings.gmd.geometric_complex_type import GeometricComplexType
from bindings.gmd.geometric_primitive_property_type import (
    GeometricPrimitivePropertyType,
)
from bindings.gmd.geometry_array_property_type import (
    GeometryArrayPropertyType,
    GeometryPropertyType,
    MultiGeometry,
    MultiGeometryType,
    GeometryMember,
    GeometryMembers,
)
from bindings.gmd.gm_object_property_type import GmObjectPropertyType
from bindings.gmd.gm_point_property_type import GmPointPropertyType
from bindings.gmd.greenwich_longitude import GreenwichLongitude
from bindings.gmd.grid import Grid
from bindings.gmd.grid_coverage import GridCoverage
from bindings.gmd.grid_coverage_type import GridCoverageType
from bindings.gmd.grid_domain import GridDomain
from bindings.gmd.grid_domain_type import GridDomainType
from bindings.gmd.grid_envelope_type import GridEnvelopeType
from bindings.gmd.grid_function import GridFunction
from bindings.gmd.grid_function_type import GridFunctionType
from bindings.gmd.grid_length_type import GridLengthType
from bindings.gmd.grid_limits_type import GridLimitsType
from bindings.gmd.grid_type import GridType
from bindings.gmd.group import Group
from bindings.gmd.history import History
from bindings.gmd.history_property_type import HistoryPropertyType
from bindings.gmd.identified_object_type import IdentifiedObjectType
from bindings.gmd.identifier import Identifier
from bindings.gmd.image_crsproperty_type import ImageCrspropertyType
from bindings.gmd.image_crsref import ImageCrsref
from bindings.gmd.image_datum_ref import ImageDatumRef
from bindings.gmd.includes_parameter import IncludesParameter
from bindings.gmd.increment_order import IncrementOrder
from bindings.gmd.indirect_entry import IndirectEntry
from bindings.gmd.indirect_entry_type import IndirectEntryType
from bindings.gmd.inline_property_type import InlinePropertyType
from bindings.gmd.integer import Integer
from bindings.gmd.integer_property_type import IntegerPropertyType
from bindings.gmd.integer_value import IntegerValue
from bindings.gmd.integer_value_list import IntegerValueList
from bindings.gmd.interior import Interior
from bindings.gmd.knot_property_type import KnotPropertyType
from bindings.gmd.knot_type import KnotType
from bindings.gmd.knot_types_type import KnotTypesType
from bindings.gmd.language_code import LanguageCode
from bindings.gmd.language_code_property_type import LanguageCodePropertyType
from bindings.gmd.length import Length
from bindings.gmd.length_property_type import LengthPropertyType
from bindings.gmd.length_type import LengthType
from bindings.gmd.li_lineage import LiLineage
from bindings.gmd.li_lineage_property_type import LiLineagePropertyType
from bindings.gmd.li_lineage_type import LiLineageType
from bindings.gmd.li_process_step_property_type import (
    LiProcessStep,
    LiProcessStepPropertyType,
    LiProcessStepType,
    LiSource,
    LiSourcePropertyType,
    LiSourceType,
)
from bindings.gmd.line_string import LineString
from bindings.gmd.line_string_segment import LineStringSegment
from bindings.gmd.line_string_segment_array_property_type import (
    LineStringSegmentArrayPropertyType,
)
from bindings.gmd.line_string_segment_type import LineStringSegmentType
from bindings.gmd.line_string_type import LineStringType
from bindings.gmd.linear_cs import LinearCs
from bindings.gmd.linear_csproperty_type import LinearCspropertyType
from bindings.gmd.linear_csref import LinearCsref
from bindings.gmd.linear_cstype import LinearCstype
from bindings.gmd.linear_ring import LinearRing
from bindings.gmd.linear_ring_property_type import LinearRingPropertyType
from bindings.gmd.linear_ring_type import LinearRingType
from bindings.gmd.local_name import LocalName
from bindings.gmd.local_name_property_type import LocalNamePropertyType
from bindings.gmd.localised_character_string import LocalisedCharacterString
from bindings.gmd.localised_character_string_property_type import (
    LocalisedCharacterStringPropertyType,
)
from bindings.gmd.localised_character_string_type import LocalisedCharacterStringType
from bindings.gmd.location import Location
from bindings.gmd.location_key_word import LocationKeyWord
from bindings.gmd.location_name import LocationName
from bindings.gmd.location_property_type import LocationPropertyType
from bindings.gmd.location_reference import LocationReference
from bindings.gmd.location_string import LocationString
from bindings.gmd.mapping_rule import MappingRule
from bindings.gmd.mapping_rule_type import MappingRuleType
from bindings.gmd.maximum_occurs import MaximumOccurs
from bindings.gmd.maximum_value import MaximumValue
from bindings.gmd.md_aggregate_information import MdAggregateInformation
from bindings.gmd.md_aggregate_information_property_type import (
    MdAggregateInformationPropertyType,
)
from bindings.gmd.md_aggregate_information_type import MdAggregateInformationType
from bindings.gmd.md_application_schema_information import (
    MdApplicationSchemaInformation,
)
from bindings.gmd.md_application_schema_information_property_type import (
    MdApplicationSchemaInformationPropertyType,
)
from bindings.gmd.md_application_schema_information_type import (
    MdApplicationSchemaInformationType,
)
from bindings.gmd.md_band import MdBand
from bindings.gmd.md_band_property_type import MdBandPropertyType
from bindings.gmd.md_band_type import MdBandType
from bindings.gmd.md_browse_graphic import MdBrowseGraphic
from bindings.gmd.md_browse_graphic_property_type import MdBrowseGraphicPropertyType
from bindings.gmd.md_browse_graphic_type import MdBrowseGraphicType
from bindings.gmd.md_cell_geometry_code import MdCellGeometryCode
from bindings.gmd.md_cell_geometry_code_property_type import (
    MdCellGeometryCodePropertyType,
)
from bindings.gmd.md_character_set_code import MdCharacterSetCode
from bindings.gmd.md_character_set_code_property_type import (
    MdCharacterSetCodePropertyType,
)
from bindings.gmd.md_classification_code import MdClassificationCode
from bindings.gmd.md_classification_code_property_type import (
    MdClassificationCodePropertyType,
)
from bindings.gmd.md_constraints import MdConstraints
from bindings.gmd.md_constraints_property_type import MdConstraintsPropertyType
from bindings.gmd.md_constraints_type import MdConstraintsType
from bindings.gmd.md_content_information_property_type import (
    MdContentInformationPropertyType,
)
from bindings.gmd.md_coverage_content_type_code import MdCoverageContentTypeCode
from bindings.gmd.md_coverage_content_type_code_property_type import (
    MdCoverageContentTypeCodePropertyType,
)
from bindings.gmd.md_coverage_description import MdCoverageDescription
from bindings.gmd.md_coverage_description_property_type import (
    MdCoverageDescriptionPropertyType,
)
from bindings.gmd.md_coverage_description_type import MdCoverageDescriptionType
from bindings.gmd.md_data_identification import MdDataIdentification
from bindings.gmd.md_data_identification_property_type import (
    MdDataIdentificationPropertyType,
)
from bindings.gmd.md_data_identification_type import MdDataIdentificationType
from bindings.gmd.md_datatype_code import MdDatatypeCode
from bindings.gmd.md_datatype_code_property_type import MdDatatypeCodePropertyType
from bindings.gmd.md_digital_transfer_options import MdDigitalTransferOptions
from bindings.gmd.md_digital_transfer_options_property_type import (
    MdDigitalTransferOptionsPropertyType,
)
from bindings.gmd.md_digital_transfer_options_type import MdDigitalTransferOptionsType
from bindings.gmd.md_dimension import MdDimension
from bindings.gmd.md_dimension_name_type_code import MdDimensionNameTypeCode
from bindings.gmd.md_dimension_name_type_code_property_type import (
    MdDimensionNameTypeCodePropertyType,
)
from bindings.gmd.md_dimension_property_type import MdDimensionPropertyType
from bindings.gmd.md_dimension_type import MdDimensionType
from bindings.gmd.md_distribution import MdDistribution
from bindings.gmd.md_distribution_property_type import MdDistributionPropertyType
from bindings.gmd.md_distribution_type import MdDistributionType
from bindings.gmd.md_distribution_units import MdDistributionUnits
from bindings.gmd.md_distribution_units_property_type import (
    MdDistributionUnitsPropertyType,
)
from bindings.gmd.md_distributor_property_type import (
    MdDistributor,
    MdDistributorPropertyType,
    MdDistributorType,
    MdFormat,
    MdFormatPropertyType,
    MdFormatType,
)
from bindings.gmd.md_extended_element_information import MdExtendedElementInformation
from bindings.gmd.md_extended_element_information_property_type import (
    MdExtendedElementInformationPropertyType,
)
from bindings.gmd.md_extended_element_information_type import (
    MdExtendedElementInformationType,
)
from bindings.gmd.md_feature_catalogue_description import MdFeatureCatalogueDescription
from bindings.gmd.md_feature_catalogue_description_property_type import (
    MdFeatureCatalogueDescriptionPropertyType,
)
from bindings.gmd.md_feature_catalogue_description_type import (
    MdFeatureCatalogueDescriptionType,
)
from bindings.gmd.md_geometric_object_type_code import MdGeometricObjectTypeCode
from bindings.gmd.md_geometric_object_type_code_property_type import (
    MdGeometricObjectTypeCodePropertyType,
)
from bindings.gmd.md_geometric_objects import MdGeometricObjects
from bindings.gmd.md_geometric_objects_property_type import (
    MdGeometricObjectsPropertyType,
)
from bindings.gmd.md_geometric_objects_type import MdGeometricObjectsType
from bindings.gmd.md_georectified import MdGeorectified
from bindings.gmd.md_georectified_property_type import MdGeorectifiedPropertyType
from bindings.gmd.md_georectified_type import MdGeorectifiedType
from bindings.gmd.md_georeferenceable import MdGeoreferenceable
from bindings.gmd.md_georeferenceable_property_type import (
    MdGeoreferenceablePropertyType,
)
from bindings.gmd.md_georeferenceable_type import MdGeoreferenceableType
from bindings.gmd.md_grid_spatial_representation import MdGridSpatialRepresentation
from bindings.gmd.md_grid_spatial_representation_property_type import (
    MdGridSpatialRepresentationPropertyType,
)
from bindings.gmd.md_grid_spatial_representation_type import (
    MdGridSpatialRepresentationType,
)
from bindings.gmd.md_identification_property_type import MdIdentificationPropertyType
from bindings.gmd.md_image_description import MdImageDescription
from bindings.gmd.md_image_description_property_type import (
    MdImageDescriptionPropertyType,
)
from bindings.gmd.md_image_description_type import MdImageDescriptionType
from bindings.gmd.md_imaging_condition_code import MdImagingConditionCode
from bindings.gmd.md_imaging_condition_code_property_type import (
    MdImagingConditionCodePropertyType,
)
from bindings.gmd.md_keyword_type_code import MdKeywordTypeCode
from bindings.gmd.md_keyword_type_code_property_type import (
    MdKeywordTypeCodePropertyType,
)
from bindings.gmd.md_keywords import MdKeywords
from bindings.gmd.md_keywords_property_type import MdKeywordsPropertyType
from bindings.gmd.md_keywords_type import MdKeywordsType
from bindings.gmd.md_legal_constraints import MdLegalConstraints
from bindings.gmd.md_legal_constraints_property_type import (
    MdLegalConstraintsPropertyType,
)
from bindings.gmd.md_legal_constraints_type import MdLegalConstraintsType
from bindings.gmd.md_maintenance_frequency_code import MdMaintenanceFrequencyCode
from bindings.gmd.md_maintenance_frequency_code_property_type import (
    MdMaintenanceFrequencyCodePropertyType,
)
from bindings.gmd.md_maintenance_information import MdMaintenanceInformation
from bindings.gmd.md_maintenance_information_property_type import (
    MdMaintenanceInformationPropertyType,
)
from bindings.gmd.md_maintenance_information_type import MdMaintenanceInformationType
from bindings.gmd.md_medium import MdMedium
from bindings.gmd.md_medium_format_code import MdMediumFormatCode
from bindings.gmd.md_medium_format_code_property_type import (
    MdMediumFormatCodePropertyType,
)
from bindings.gmd.md_medium_name_code import MdMediumNameCode
from bindings.gmd.md_medium_name_code_property_type import MdMediumNameCodePropertyType
from bindings.gmd.md_medium_property_type import MdMediumPropertyType
from bindings.gmd.md_medium_type import MdMediumType
from bindings.gmd.md_metadata_extension_information import (
    MdMetadataExtensionInformation,
)
from bindings.gmd.md_metadata_extension_information_property_type import (
    MdMetadataExtensionInformationPropertyType,
)
from bindings.gmd.md_metadata_extension_information_type import (
    MdMetadataExtensionInformationType,
)
from bindings.gmd.md_metadata_property_type import (
    AbstractDsAggregate,
    AbstractDsAggregateType,
    DsAggregatePropertyType,
    DsDataSet,
    DsDataSetPropertyType,
    DsDataSetType,
    DsInitiative,
    DsInitiativeType,
    DsOtherAggregate,
    DsOtherAggregateType,
    DsPlatform,
    DsPlatformType,
    DsProductionSeries,
    DsProductionSeriesType,
    DsSensor,
    DsSensorType,
    DsSeries,
    DsSeriesType,
    DsStereoMate,
    DsStereoMateType,
    MdMetadata,
    MdMetadataPropertyType,
    MdMetadataType,
)
from bindings.gmd.md_obligation_code import MdObligationCode
from bindings.gmd.md_obligation_code_property_type import MdObligationCodePropertyType
from bindings.gmd.md_obligation_code_type import MdObligationCodeType
from bindings.gmd.md_pixel_orientation_code import MdPixelOrientationCode
from bindings.gmd.md_pixel_orientation_code_property_type import (
    MdPixelOrientationCodePropertyType,
)
from bindings.gmd.md_pixel_orientation_code_type import MdPixelOrientationCodeType
from bindings.gmd.md_portrayal_catalogue_reference import MdPortrayalCatalogueReference
from bindings.gmd.md_portrayal_catalogue_reference_property_type import (
    MdPortrayalCatalogueReferencePropertyType,
)
from bindings.gmd.md_portrayal_catalogue_reference_type import (
    MdPortrayalCatalogueReferenceType,
)
from bindings.gmd.md_progress_code import MdProgressCode
from bindings.gmd.md_progress_code_property_type import MdProgressCodePropertyType
from bindings.gmd.md_range_dimension import MdRangeDimension
from bindings.gmd.md_range_dimension_property_type import MdRangeDimensionPropertyType
from bindings.gmd.md_range_dimension_type import MdRangeDimensionType
from bindings.gmd.md_reference_system import MdReferenceSystem
from bindings.gmd.md_reference_system_property_type import MdReferenceSystemPropertyType
from bindings.gmd.md_reference_system_type import MdReferenceSystemType
from bindings.gmd.md_representative_fraction import MdRepresentativeFraction
from bindings.gmd.md_representative_fraction_property_type import (
    MdRepresentativeFractionPropertyType,
)
from bindings.gmd.md_representative_fraction_type import MdRepresentativeFractionType
from bindings.gmd.md_resolution import MdResolution
from bindings.gmd.md_resolution_property_type import MdResolutionPropertyType
from bindings.gmd.md_resolution_type import MdResolutionType
from bindings.gmd.md_restriction_code import MdRestrictionCode
from bindings.gmd.md_restriction_code_property_type import MdRestrictionCodePropertyType
from bindings.gmd.md_scope_code import MdScopeCode
from bindings.gmd.md_scope_code_property_type import MdScopeCodePropertyType
from bindings.gmd.md_scope_description import MdScopeDescription
from bindings.gmd.md_scope_description_property_type import (
    MdScopeDescriptionPropertyType,
)
from bindings.gmd.md_scope_description_type import MdScopeDescriptionType
from bindings.gmd.md_security_constraints import MdSecurityConstraints
from bindings.gmd.md_security_constraints_property_type import (
    MdSecurityConstraintsPropertyType,
)
from bindings.gmd.md_security_constraints_type import MdSecurityConstraintsType
from bindings.gmd.md_service_identification import MdServiceIdentification
from bindings.gmd.md_service_identification_property_type import (
    MdServiceIdentificationPropertyType,
)
from bindings.gmd.md_service_identification_type import MdServiceIdentificationType
from bindings.gmd.md_spatial_representation_property_type import (
    MdSpatialRepresentationPropertyType,
)
from bindings.gmd.md_spatial_representation_type_code import (
    MdSpatialRepresentationTypeCode,
)
from bindings.gmd.md_spatial_representation_type_code_property_type import (
    MdSpatialRepresentationTypeCodePropertyType,
)
from bindings.gmd.md_standard_order_process import MdStandardOrderProcess
from bindings.gmd.md_standard_order_process_property_type import (
    MdStandardOrderProcessPropertyType,
)
from bindings.gmd.md_standard_order_process_type import MdStandardOrderProcessType
from bindings.gmd.md_topic_category_code import MdTopicCategoryCode
from bindings.gmd.md_topic_category_code_property_type import (
    MdTopicCategoryCodePropertyType,
)
from bindings.gmd.md_topic_category_code_type import MdTopicCategoryCodeType
from bindings.gmd.md_topology_level_code import MdTopologyLevelCode
from bindings.gmd.md_topology_level_code_property_type import (
    MdTopologyLevelCodePropertyType,
)
from bindings.gmd.md_usage import MdUsage
from bindings.gmd.md_usage_property_type import MdUsagePropertyType
from bindings.gmd.md_usage_type import MdUsageType
from bindings.gmd.md_vector_spatial_representation import MdVectorSpatialRepresentation
from bindings.gmd.md_vector_spatial_representation_property_type import (
    MdVectorSpatialRepresentationPropertyType,
)
from bindings.gmd.md_vector_spatial_representation_type import (
    MdVectorSpatialRepresentationType,
)
from bindings.gmd.measure_1 import Measure1
from bindings.gmd.measure_2 import Measure2
from bindings.gmd.measure_list_type import MeasureListType
from bindings.gmd.measure_or_nil_reason_list_type import MeasureOrNilReasonListType
from bindings.gmd.measure_property_type import MeasurePropertyType
from bindings.gmd.measure_type import MeasureType
from bindings.gmd.member_name import MemberName
from bindings.gmd.member_name_property_type import MemberNamePropertyType
from bindings.gmd.member_name_type import MemberNameType
from bindings.gmd.meta_data_property import MetaDataProperty
from bindings.gmd.meta_data_property_type import MetaDataPropertyType
from bindings.gmd.method import Method
from bindings.gmd.method_formula import MethodFormula
from bindings.gmd.minimum_occurs import MinimumOccurs
from bindings.gmd.minimum_value import MinimumValue
from bindings.gmd.minutes import Minutes
from bindings.gmd.modified_coordinate import ModifiedCoordinate
from bindings.gmd.moving_object_status import MovingObjectStatus
from bindings.gmd.moving_object_status_type import MovingObjectStatusType
from bindings.gmd.multi_center_line_of import MultiCenterLineOf
from bindings.gmd.multi_center_of import MultiCenterOf
from bindings.gmd.multi_coverage import MultiCoverage
from bindings.gmd.multi_curve import MultiCurve
from bindings.gmd.multi_curve_coverage import MultiCurveCoverage
from bindings.gmd.multi_curve_coverage_type import MultiCurveCoverageType
from bindings.gmd.multi_curve_domain import MultiCurveDomain
from bindings.gmd.multi_curve_domain_type import MultiCurveDomainType
from bindings.gmd.multi_curve_property import MultiCurveProperty
from bindings.gmd.multi_curve_property_type import MultiCurvePropertyType
from bindings.gmd.multi_curve_type import MultiCurveType
from bindings.gmd.multi_edge_of import MultiEdgeOf
from bindings.gmd.multi_extent_of import MultiExtentOf
from bindings.gmd.multi_geometry_property import MultiGeometryProperty
from bindings.gmd.multi_geometry_property_type import MultiGeometryPropertyType
from bindings.gmd.multi_location import MultiLocation
from bindings.gmd.multi_point import MultiPoint
from bindings.gmd.multi_point_coverage import MultiPointCoverage
from bindings.gmd.multi_point_coverage_type import MultiPointCoverageType
from bindings.gmd.multi_point_domain import MultiPointDomain
from bindings.gmd.multi_point_domain_type import MultiPointDomainType
from bindings.gmd.multi_point_property import MultiPointProperty
from bindings.gmd.multi_point_property_type import MultiPointPropertyType
from bindings.gmd.multi_point_type import MultiPointType
from bindings.gmd.multi_position import MultiPosition
from bindings.gmd.multi_solid import MultiSolid
from bindings.gmd.multi_solid_coverage import MultiSolidCoverage
from bindings.gmd.multi_solid_coverage_type import MultiSolidCoverageType
from bindings.gmd.multi_solid_domain import MultiSolidDomain
from bindings.gmd.multi_solid_domain_type import MultiSolidDomainType
from bindings.gmd.multi_solid_property import MultiSolidProperty
from bindings.gmd.multi_solid_property_type import MultiSolidPropertyType
from bindings.gmd.multi_solid_type import MultiSolidType
from bindings.gmd.multi_surface import MultiSurface
from bindings.gmd.multi_surface_coverage import MultiSurfaceCoverage
from bindings.gmd.multi_surface_coverage_type import MultiSurfaceCoverageType
from bindings.gmd.multi_surface_domain import MultiSurfaceDomain
from bindings.gmd.multi_surface_domain_type import MultiSurfaceDomainType
from bindings.gmd.multi_surface_property import MultiSurfaceProperty
from bindings.gmd.multi_surface_property_type import MultiSurfacePropertyType
from bindings.gmd.multi_surface_type import MultiSurfaceType
from bindings.gmd.multiplicity import Multiplicity
from bindings.gmd.multiplicity_property_type import MultiplicityPropertyType
from bindings.gmd.multiplicity_range import MultiplicityRange
from bindings.gmd.multiplicity_range_property_type import MultiplicityRangePropertyType
from bindings.gmd.multiplicity_range_type import MultiplicityRangeType
from bindings.gmd.multiplicity_type import MultiplicityType
from bindings.gmd.name import Name
from bindings.gmd.nil_reason_enumeration_value import NilReasonEnumerationValue
from bindings.gmd.null import Null
from bindings.gmd.number_property_type import NumberPropertyType
from bindings.gmd.object_reference_property_type import ObjectReferencePropertyType
from bindings.gmd.oblique_cartesian_cs import ObliqueCartesianCs
from bindings.gmd.oblique_cartesian_csproperty_type import (
    ObliqueCartesianCspropertyType,
)
from bindings.gmd.oblique_cartesian_csref import ObliqueCartesianCsref
from bindings.gmd.oblique_cartesian_cstype import ObliqueCartesianCstype
from bindings.gmd.operation_method import OperationMethod
from bindings.gmd.operation_method_property_type import OperationMethodPropertyType
from bindings.gmd.operation_method_ref import OperationMethodRef
from bindings.gmd.operation_method_type import OperationMethodType
from bindings.gmd.operation_parameter_1 import OperationParameter1
from bindings.gmd.operation_parameter_2 import OperationParameter2
from bindings.gmd.operation_parameter_group_property_type import (
    OperationParameterGroupPropertyType,
)
from bindings.gmd.operation_parameter_group_ref import OperationParameterGroupRef
from bindings.gmd.operation_parameter_property_type import (
    OperationParameterPropertyType,
)
from bindings.gmd.operation_parameter_ref import OperationParameterRef
from bindings.gmd.operation_parameter_type import OperationParameterType
from bindings.gmd.operation_property_type import OperationPropertyType
from bindings.gmd.operation_ref import OperationRef
from bindings.gmd.operation_version import OperationVersion
from bindings.gmd.origin import Origin
from bindings.gmd.parameter_value_1 import ParameterValue1
from bindings.gmd.parameter_value_type import ParameterValueType
from bindings.gmd.pass_through_operation_property_type import (
    PassThroughOperationPropertyType,
)
from bindings.gmd.pass_through_operation_ref import PassThroughOperationRef
from bindings.gmd.pass_through_operation_type import (
    ConcatenatedOperation,
    ConcatenatedOperationType,
    CoordinateOperationPropertyType,
    PassThroughOperation,
    PassThroughOperationType,
    CoordOperation,
    UsesOperation,
    UsesSingleOperation,
)
from bindings.gmd.patches import Patches
from bindings.gmd.pixel_in_cell import PixelInCell
from bindings.gmd.point import Point
from bindings.gmd.point_array_property import PointArrayProperty
from bindings.gmd.point_array_property_type import PointArrayPropertyType
from bindings.gmd.point_member import PointMember
from bindings.gmd.point_members import PointMembers
from bindings.gmd.point_property import PointProperty
from bindings.gmd.point_property_type import PointPropertyType
from bindings.gmd.point_rep import PointRep
from bindings.gmd.point_type import PointType
from bindings.gmd.polar_cs import PolarCs
from bindings.gmd.polar_csproperty_type import PolarCspropertyType
from bindings.gmd.polar_csref import PolarCsref
from bindings.gmd.polar_cstype import PolarCstype
from bindings.gmd.polygon import Polygon
from bindings.gmd.polygon_patch import PolygonPatch
from bindings.gmd.polygon_patch_array_property_type import PolygonPatchArrayPropertyType
from bindings.gmd.polygon_patch_type import PolygonPatchType
from bindings.gmd.polygon_patches import PolygonPatches
from bindings.gmd.polygon_type import PolygonType
from bindings.gmd.polyhedral_surface import PolyhedralSurface
from bindings.gmd.polyhedral_surface_type import PolyhedralSurfaceType
from bindings.gmd.pos import Pos
from bindings.gmd.pos_list import PosList
from bindings.gmd.position import Position
from bindings.gmd.prime_meridian_1 import PrimeMeridian1
from bindings.gmd.prime_meridian_2 import PrimeMeridian2
from bindings.gmd.prime_meridian_property_type import PrimeMeridianPropertyType
from bindings.gmd.prime_meridian_ref import PrimeMeridianRef
from bindings.gmd.prime_meridian_type import PrimeMeridianType
from bindings.gmd.priority_location import PriorityLocation
from bindings.gmd.priority_location_property_type import PriorityLocationPropertyType
from bindings.gmd.projected_crsproperty_type import ProjectedCrspropertyType
from bindings.gmd.projected_crsref import ProjectedCrsref
from bindings.gmd.pt_free_text import PtFreeText
from bindings.gmd.pt_free_text_property_type import PtFreeTextPropertyType
from bindings.gmd.pt_free_text_type import PtFreeTextType
from bindings.gmd.pt_locale import PtLocale
from bindings.gmd.pt_locale_container import PtLocaleContainer
from bindings.gmd.pt_locale_container_property_type import PtLocaleContainerPropertyType
from bindings.gmd.pt_locale_container_type import PtLocaleContainerType
from bindings.gmd.pt_locale_property_type import PtLocalePropertyType
from bindings.gmd.pt_locale_type import PtLocaleType
from bindings.gmd.quantity import Quantity
from bindings.gmd.quantity_extent import QuantityExtent
from bindings.gmd.quantity_extent_type import QuantityExtentType
from bindings.gmd.quantity_list import QuantityList
from bindings.gmd.quantity_property_type import QuantityPropertyType
from bindings.gmd.quantity_type import QuantityType
from bindings.gmd.quantity_type_reference import QuantityTypeReference
from bindings.gmd.range_meaning import RangeMeaning
from bindings.gmd.range_parameters import RangeParameters
from bindings.gmd.range_parameters_type import RangeParametersType
from bindings.gmd.range_set import RangeSet
from bindings.gmd.range_set_type import RangeSetType
from bindings.gmd.real import Real
from bindings.gmd.real_property_type import RealPropertyType
from bindings.gmd.realization_epoch import RealizationEpoch
from bindings.gmd.record import Record
from bindings.gmd.record_property_type import RecordPropertyType
from bindings.gmd.record_type import RecordType
from bindings.gmd.record_type_property_type import RecordTypePropertyType
from bindings.gmd.record_type_type import RecordTypeType
from bindings.gmd.rectangle import Rectangle
from bindings.gmd.rectangle_type import RectangleType
from bindings.gmd.rectified_grid import RectifiedGrid
from bindings.gmd.rectified_grid_coverage import RectifiedGridCoverage
from bindings.gmd.rectified_grid_coverage_type import RectifiedGridCoverageType
from bindings.gmd.rectified_grid_domain import RectifiedGridDomain
from bindings.gmd.rectified_grid_domain_type import RectifiedGridDomainType
from bindings.gmd.rectified_grid_type import RectifiedGridType
from bindings.gmd.reference_type import ReferenceType
from bindings.gmd.related_time_type_relative_position import (
    RelatedTimeTypeRelativePosition,
)
from bindings.gmd.remarks import Remarks
from bindings.gmd.reverse_property_name import ReversePropertyName
from bindings.gmd.ring import Ring
from bindings.gmd.ring_property_type import RingPropertyType
from bindings.gmd.ring_type import RingType
from bindings.gmd.rough_conversion_to_preferred_unit import (
    RoughConversionToPreferredUnit,
)
from bindings.gmd.rs_identifier_property_type import RsIdentifierPropertyType
from bindings.gmd.rs_reference_system_property_type import RsReferenceSystemPropertyType
from bindings.gmd.scale import Scale
from bindings.gmd.scale_property_type import ScalePropertyType
from bindings.gmd.scale_type import ScaleType
from bindings.gmd.scope import Scope
from bindings.gmd.scoped_name import ScopedName
from bindings.gmd.scoped_name_property_type import ScopedNamePropertyType
from bindings.gmd.second_defining_parameter_1 import SecondDefiningParameter1
from bindings.gmd.second_defining_parameter_2 import SecondDefiningParameter2
from bindings.gmd.second_defining_parameter_is_sphere import (
    SecondDefiningParameterIsSphere,
)
from bindings.gmd.seconds import Seconds
from bindings.gmd.semi_major_axis import SemiMajorAxis
from bindings.gmd.sequence_rule_enumeration import SequenceRuleEnumeration
from bindings.gmd.sequence_rule_type import SequenceRuleType
from bindings.gmd.shell import Shell
from bindings.gmd.shell_property_type import ShellPropertyType
from bindings.gmd.shell_type import ShellType
from bindings.gmd.show_value import ShowValue
from bindings.gmd.sign_type import SignType
from bindings.gmd.single_crsref import SingleCrsref
from bindings.gmd.single_operation_property_type import SingleOperationPropertyType
from bindings.gmd.single_operation_ref import SingleOperationRef
from bindings.gmd.solid import Solid
from bindings.gmd.solid_array_property import SolidArrayProperty
from bindings.gmd.solid_array_property_type import SolidArrayPropertyType
from bindings.gmd.solid_members import SolidMembers
from bindings.gmd.solid_property import SolidProperty
from bindings.gmd.solid_property_type import (
    CompositeSolid,
    CompositeSolidType,
    SolidPropertyType,
    SolidMember,
)
from bindings.gmd.solid_type import SolidType
from bindings.gmd.source_dimensions import SourceDimensions
from bindings.gmd.speed_type import SpeedType
from bindings.gmd.sphere import Sphere
from bindings.gmd.sphere_type import SphereType
from bindings.gmd.spherical_cs_1 import SphericalCs1
from bindings.gmd.spherical_cs_2 import SphericalCs2
from bindings.gmd.spherical_csproperty_type import SphericalCspropertyType
from bindings.gmd.spherical_csref import SphericalCsref
from bindings.gmd.spherical_cstype import SphericalCstype
from bindings.gmd.status import Status
from bindings.gmd.status_reference import StatusReference
from bindings.gmd.string_or_ref_type import StringOrRefType
from bindings.gmd.string_value import StringValue
from bindings.gmd.succession_type import SuccessionType
from bindings.gmd.surface import Surface
from bindings.gmd.surface_array_property import SurfaceArrayProperty
from bindings.gmd.surface_array_property_type import SurfaceArrayPropertyType
from bindings.gmd.surface_interpolation_type import SurfaceInterpolationType
from bindings.gmd.surface_members import SurfaceMembers
from bindings.gmd.surface_patch_array_property_type import SurfacePatchArrayPropertyType
from bindings.gmd.surface_property import SurfaceProperty
from bindings.gmd.surface_type import SurfaceType
from bindings.gmd.target_dimensions import TargetDimensions
from bindings.gmd.target_element import TargetElement
from bindings.gmd.temporal_crsproperty_type import TemporalCrspropertyType
from bindings.gmd.temporal_crsref import TemporalCrsref
from bindings.gmd.temporal_cs import TemporalCs
from bindings.gmd.temporal_csproperty_type import TemporalCspropertyType
from bindings.gmd.temporal_csref import TemporalCsref
from bindings.gmd.temporal_cstype import TemporalCstype
from bindings.gmd.temporal_datum_ref import TemporalDatumRef
from bindings.gmd.time_calendar import TimeCalendar
from bindings.gmd.time_calendar_era import TimeCalendarEra
from bindings.gmd.time_calendar_era_property_type import TimeCalendarEraPropertyType
from bindings.gmd.time_calendar_era_type import TimeCalendarEraType
from bindings.gmd.time_calendar_property_type import TimeCalendarPropertyType
from bindings.gmd.time_calendar_type import TimeCalendarType
from bindings.gmd.time_clock import TimeClock
from bindings.gmd.time_clock_property_type import TimeClockPropertyType
from bindings.gmd.time_clock_type import TimeClockType
from bindings.gmd.time_coordinate_system import TimeCoordinateSystem
from bindings.gmd.time_coordinate_system_type import TimeCoordinateSystemType
from bindings.gmd.time_cs_1 import TimeCs1
from bindings.gmd.time_cs_2 import TimeCs2
from bindings.gmd.time_csproperty_type import TimeCspropertyType
from bindings.gmd.time_cstype import TimeCstype
from bindings.gmd.time_edge_property_type import (
    AbstractTimeGeometricPrimitive,
    AbstractTimeGeometricPrimitiveType,
    AbstractTimePrimitive,
    AbstractTimePrimitiveType,
    AbstractTimeTopologyPrimitive,
    AbstractTimeTopologyPrimitiveType,
    RelatedTimeType,
    TimeEdge,
    TimeEdgePropertyType,
    TimeEdgeType,
    TimeInstant,
    TimeInstantPropertyType,
    TimeInstantType,
    TimeNode,
    TimeNodePropertyType,
    TimeNodeType,
    TimePeriod,
    TimePeriodPropertyType,
    TimePeriodType,
    TimePrimitivePropertyType,
)
from bindings.gmd.time_indeterminate_value_type import TimeIndeterminateValueType
from bindings.gmd.time_interval import TimeInterval
from bindings.gmd.time_interval_length_type import TimeIntervalLengthType
from bindings.gmd.time_ordinal_era_type import (
    TimeOrdinalEra,
    TimeOrdinalEraPropertyType,
    TimeOrdinalEraType,
)
from bindings.gmd.time_ordinal_reference_system import TimeOrdinalReferenceSystem
from bindings.gmd.time_ordinal_reference_system_type import (
    TimeOrdinalReferenceSystemType,
)
from bindings.gmd.time_position import TimePosition
from bindings.gmd.time_position_type import TimePositionType
from bindings.gmd.time_reference_system import TimeReferenceSystem
from bindings.gmd.time_reference_system_type import TimeReferenceSystemType
from bindings.gmd.time_topology_complex import TimeTopologyComplex
from bindings.gmd.time_topology_complex_property_type import (
    TimeTopologyComplexPropertyType,
)
from bindings.gmd.time_topology_complex_type import TimeTopologyComplexType
from bindings.gmd.time_topology_primitive_property_type import (
    TimeTopologyPrimitivePropertyType,
)
from bindings.gmd.time_type import TimeType
from bindings.gmd.time_unit_type_value import TimeUnitTypeValue
from bindings.gmd.tin import Tin
from bindings.gmd.tin_type import TinType
from bindings.gmd.tm_period_duration import TmPeriodDuration
from bindings.gmd.tm_period_duration_property_type import TmPeriodDurationPropertyType
from bindings.gmd.tm_primitive_property_type import TmPrimitivePropertyType
from bindings.gmd.topo_complex_member_type import (
    TopoComplex,
    TopoComplexMemberType,
    TopoComplexType,
    MaximalComplex,
    SubComplex,
    SuperComplex,
)
from bindings.gmd.topo_complex_property import TopoComplexProperty
from bindings.gmd.topo_curve import TopoCurve
from bindings.gmd.topo_curve_property import TopoCurveProperty
from bindings.gmd.topo_curve_property_type import TopoCurvePropertyType
from bindings.gmd.topo_curve_type import TopoCurveType
from bindings.gmd.topo_point import TopoPoint
from bindings.gmd.topo_point_property import TopoPointProperty
from bindings.gmd.topo_point_property_type import TopoPointPropertyType
from bindings.gmd.topo_point_type import TopoPointType
from bindings.gmd.topo_primitive_array_association_type import (
    TopoPrimitiveArrayAssociationType,
)
from bindings.gmd.topo_primitive_member import TopoPrimitiveMember
from bindings.gmd.topo_primitive_member_type import TopoPrimitiveMemberType
from bindings.gmd.topo_primitive_members import TopoPrimitiveMembers
from bindings.gmd.topo_surface import TopoSurface
from bindings.gmd.topo_surface_property import TopoSurfaceProperty
from bindings.gmd.topo_surface_property_type import TopoSurfacePropertyType
from bindings.gmd.topo_surface_type import TopoSurfaceType
from bindings.gmd.topo_volume import TopoVolume
from bindings.gmd.topo_volume_property import TopoVolumeProperty
from bindings.gmd.topo_volume_property_type import TopoVolumePropertyType
from bindings.gmd.topo_volume_type import TopoVolumeType
from bindings.gmd.track import Track
from bindings.gmd.transformation import Transformation
from bindings.gmd.transformation_property_type import TransformationPropertyType
from bindings.gmd.transformation_ref import TransformationRef
from bindings.gmd.transformation_type import TransformationType
from bindings.gmd.triangle import Triangle
from bindings.gmd.triangle_patch_array_property_type import (
    TrianglePatchArrayPropertyType,
)
from bindings.gmd.triangle_patches import TrianglePatches
from bindings.gmd.triangle_type import TriangleType
from bindings.gmd.triangulated_surface import TriangulatedSurface
from bindings.gmd.triangulated_surface_type import TriangulatedSurfaceType
from bindings.gmd.tuple_list import TupleList
from bindings.gmd.type_name import TypeName
from bindings.gmd.type_name_property_type import TypeNamePropertyType
from bindings.gmd.type_name_type import TypeNameType
from bindings.gmd.unit_definition import UnitDefinition
from bindings.gmd.unit_definition_type import UnitDefinitionType
from bindings.gmd.unit_of_measure import UnitOfMeasure
from bindings.gmd.unit_of_measure_property_type import UnitOfMeasurePropertyType
from bindings.gmd.unit_of_measure_type import UnitOfMeasureType
from bindings.gmd.unlimited_integer import UnlimitedInteger
from bindings.gmd.unlimited_integer_property_type import UnlimitedIntegerPropertyType
from bindings.gmd.unlimited_integer_type import UnlimitedIntegerType
from bindings.gmd.uom_angle_property_type import UomAnglePropertyType
from bindings.gmd.uom_area_property_type import UomAreaPropertyType
from bindings.gmd.uom_length_property_type import UomLengthPropertyType
from bindings.gmd.uom_scale_property_type import UomScalePropertyType
from bindings.gmd.uom_time_property_type import UomTimePropertyType
from bindings.gmd.uom_velocity_property_type import UomVelocityPropertyType
from bindings.gmd.uom_volume_property_type import UomVolumePropertyType
from bindings.gmd.url import Url
from bindings.gmd.url_property_type import UrlPropertyType
from bindings.gmd.user_defined_cs import UserDefinedCs
from bindings.gmd.user_defined_csproperty_type import UserDefinedCspropertyType
from bindings.gmd.user_defined_csref import UserDefinedCsref
from bindings.gmd.user_defined_cstype import UserDefinedCstype
from bindings.gmd.uses_affine_cs import UsesAffineCs
from bindings.gmd.uses_axis import UsesAxis
from bindings.gmd.uses_cartesian_cs import UsesCartesianCs
from bindings.gmd.uses_cs import UsesCs
from bindings.gmd.uses_ellipsoid import UsesEllipsoid
from bindings.gmd.uses_ellipsoidal_cs import UsesEllipsoidalCs
from bindings.gmd.uses_method import UsesMethod
from bindings.gmd.uses_oblique_cartesian_cs import UsesObliqueCartesianCs
from bindings.gmd.uses_prime_meridian import UsesPrimeMeridian
from bindings.gmd.uses_spherical_cs import UsesSphericalCs
from bindings.gmd.uses_temporal_cs import UsesTemporalCs
from bindings.gmd.uses_time_cs import UsesTimeCs
from bindings.gmd.uses_vertical_cs import UsesVerticalCs
from bindings.gmd.valid_time import ValidTime
from bindings.gmd.value import Value
from bindings.gmd.value_array_property_type import (
    CompositeValue,
    CompositeValueType,
    ValueArray,
    ValueArrayPropertyType,
    ValueArrayType,
    ValuePropertyType,
    ValueComponent,
    ValueComponents,
)
from bindings.gmd.value_file import ValueFile
from bindings.gmd.value_list import ValueList
from bindings.gmd.value_of_parameter import ValueOfParameter
from bindings.gmd.value_property import ValueProperty
from bindings.gmd.values_of_group import ValuesOfGroup
from bindings.gmd.vector import Vector
from bindings.gmd.vector_type import VectorType
from bindings.gmd.vertical_crsproperty_type import VerticalCrspropertyType
from bindings.gmd.vertical_crsref import VerticalCrsref
from bindings.gmd.vertical_cs_1 import VerticalCs1
from bindings.gmd.vertical_cs_2 import VerticalCs2
from bindings.gmd.vertical_csproperty_type import VerticalCspropertyType
from bindings.gmd.vertical_csref import VerticalCsref
from bindings.gmd.vertical_cstype import VerticalCstype
from bindings.gmd.vertical_datum_ref import VerticalDatumRef
from bindings.gmd.volume_type import VolumeType

__all__ = [
    "AbstractAssociationRole",
    "AbstractContinuousCoverage",
    "AbstractContinuousCoverageType",
    "AbstractCoordinateOperation",
    "AbstractCoordinateSystem",
    "AbstractCoordinateSystemType",
    "AbstractCoverage",
    "AbstractCoverageType",
    "AbstractCrs",
    "AbstractCrstype",
    "AbstractCoordinateOperationType",
    "AbstractDatumType",
    "AbstractGeneralConversion",
    "AbstractGeneralConversionType",
    "AbstractGeneralDerivedCrs",
    "AbstractGeneralDerivedCrstype",
    "AbstractSingleCrs",
    "CrspropertyType",
    "CompoundCrs",
    "CompoundCrstype",
    "ConversionType",
    "Conversion1",
    "DerivedCrs",
    "DerivedCrstype1",
    "ExExtent",
    "ExExtentType",
    "ExVerticalExtent",
    "ExVerticalExtentPropertyType",
    "ExVerticalExtentType",
    "EngineeringCrs",
    "EngineeringCrstype",
    "EngineeringDatumPropertyType",
    "EngineeringDatumType",
    "EngineeringDatum1",
    "GeneralConversionPropertyType",
    "GeocentricCrs",
    "GeocentricCrstype",
    "GeodeticCrs",
    "GeodeticCrspropertyType",
    "GeodeticCrstype",
    "GeodeticDatumPropertyType",
    "GeodeticDatumType",
    "GeodeticDatum1",
    "GeographicCrs",
    "GeographicCrspropertyType",
    "GeographicCrstype",
    "ImageCrs",
    "ImageCrstype",
    "ImageDatumPropertyType",
    "ImageDatumType",
    "ImageDatum1",
    "ProjectedCrs",
    "ProjectedCrstype",
    "ScCrsPropertyType",
    "SingleCrspropertyType",
    "TemporalCrs",
    "TemporalCrstype",
    "TemporalDatumBaseType",
    "TemporalDatumPropertyType",
    "TemporalDatumType",
    "TemporalDatum1",
    "VerticalCrs",
    "VerticalCrstype",
    "VerticalDatumPropertyType",
    "VerticalDatumType",
    "VerticalDatum1",
    "BaseCrs",
    "BaseGeodeticCrs",
    "BaseGeographicCrs",
    "ComponentReferenceSystem",
    "Conversion2",
    "DefinedByConversion",
    "DomainOfValidity",
    "EngineeringDatum2",
    "GeodeticDatum2",
    "ImageDatum2",
    "IncludesSingleCrs",
    "SourceCrs",
    "TargetCrs",
    "TemporalDatum2",
    "UsesEngineeringDatum",
    "UsesGeodeticDatum",
    "UsesImageDatum",
    "UsesTemporalDatum",
    "UsesVerticalDatum",
    "VerticalDatum2",
    "AbstractCurve",
    "AbstractCurveSegment",
    "AbstractCurveSegmentType",
    "AbstractCurveType",
    "AbstractDatum",
    "AbstractDiscreteCoverage",
    "AbstractDiscreteCoverageType",
    "AbstractDqCompleteness",
    "AbstractDqCompletenessType",
    "AbstractDqElement",
    "AbstractDqElementType",
    "AbstractDqLogicalConsistency",
    "AbstractDqLogicalConsistencyType",
    "AbstractDqPositionalAccuracy",
    "AbstractDqPositionalAccuracyType",
    "AbstractDqResult",
    "AbstractDqResultType",
    "AbstractDqTemporalAccuracy",
    "AbstractDqTemporalAccuracyType",
    "AbstractDqThematicAccuracy",
    "AbstractDqThematicAccuracyType",
    "AbstractExGeographicExtent",
    "AbstractExGeographicExtentType",
    "AbstractFeature",
    "AbstractFeatureMemberType",
    "AbstractFeatureType",
    "AbstractGeneralOperationParameter",
    "AbstractGeneralOperationParameterPropertyType",
    "OperationParameterGroup",
    "OperationParameterGroupType",
    "GeneralOperationParameter",
    "UsesParameter",
    "AbstractGeneralOperationParameterRef",
    "AbstractGeneralOperationParameterType",
    "AbstractGeneralParameterValue",
    "AbstractGeneralParameterValuePropertyType",
    "ParameterValueGroup",
    "ParameterValueGroupType",
    "IncludesValue",
    "ParameterValue2",
    "UsesValue",
    "AbstractGeneralParameterValueType",
    "AbstractGeneralTransformation",
    "AbstractGeneralTransformationType",
    "AbstractGenericName",
    "AbstractGeometricAggregate",
    "AbstractGeometricAggregateType",
    "AbstractGeometricPrimitive",
    "AbstractGeometricPrimitiveType",
    "AbstractGeometry",
    "AbstractGeometryType",
    "AbstractGml",
    "AbstractGmltype",
    "AbstractGriddedSurface",
    "AbstractGriddedSurfaceType",
    "AbstractImplicitGeometry",
    "AbstractInlineProperty",
    "AbstractMdContentInformation",
    "AbstractMdContentInformationType",
    "AbstractMdIdentification",
    "AbstractMdIdentificationType",
    "AbstractMdSpatialRepresentation",
    "AbstractMdSpatialRepresentationType",
    "AbstractMemberType",
    "AbstractMetaData",
    "AbstractMetaDataType",
    "AbstractMetadataPropertyType",
    "AbstractObject1",
    "AbstractObject2",
    "AbstractObjectType",
    "AbstractOperation",
    "AbstractParametricCurveSurface",
    "AbstractParametricCurveSurfaceType",
    "AbstractReference",
    "AbstractRing",
    "AbstractRingPropertyType",
    "AbstractRingType",
    "AbstractRsReferenceSystem",
    "AbstractRsReferenceSystemType",
    "AbstractScalarValue",
    "AbstractScalarValueList",
    "AbstractSingleOperation",
    "AbstractSolid",
    "AbstractSolidType",
    "AbstractStrictAssociationRole",
    "AbstractSurface",
    "AbstractSurfacePatch",
    "AbstractSurfacePatchType",
    "AbstractSurfaceType",
    "AbstractTimeComplex",
    "AbstractTimeComplexType",
    "AbstractTimeObject",
    "AbstractTimeObjectType",
    "AbstractTimeSlice",
    "AbstractTimeSliceType",
    "AbstractTopoPrimitive",
    "AbstractTopology",
    "AbstractTopologyType",
    "AbstractValue",
    "ActuateValue",
    "AffineCs1",
    "AffineCs2",
    "AffineCspropertyType",
    "AffineCstype",
    "AffinePlacement",
    "AffinePlacementType",
    "AggregationType",
    "AnchorDefinition",
    "AnchorPoint",
    "Angle1",
    "Angle2",
    "AngleChoiceType",
    "AnglePropertyType",
    "AngleType",
    "Arc",
    "ArcByBulge",
    "ArcByBulgeType",
    "ArcByCenterPoint",
    "ArcByCenterPointType",
    "ArcString",
    "ArcStringByBulge",
    "ArcStringByBulgeType",
    "ArcStringType",
    "ArcType",
    "AreaType",
    "AssociationName",
    "Axis",
    "AxisAbbrev",
    "AxisDirection",
    "AbstractFeatureCollection",
    "AbstractFeatureCollectionType",
    "Array",
    "ArrayAssociationType",
    "ArrayType",
    "AssociationRoleType",
    "Bag",
    "BagType",
    "DirectedObservation",
    "DirectedObservationAtDistance",
    "DirectedObservationAtDistanceType",
    "DirectedObservationType",
    "FeatureArrayPropertyType",
    "FeatureCollection",
    "FeatureCollectionType",
    "FeaturePropertyType",
    "Observation",
    "ObservationType",
    "ProcedurePropertyType",
    "ResultType",
    "TargetPropertyType",
    "FeatureMember",
    "FeatureMembers",
    "Member",
    "Members",
    "ResultOf",
    "Subject",
    "Target",
    "Using",
    "BaseUnit",
    "BaseUnitType",
    "Bezier",
    "BezierType",
    "Binary",
    "BinaryPropertyType",
    "BinaryType",
    "Boolean1",
    "Boolean2",
    "BooleanList",
    "BooleanPropertyType1",
    "BooleanPropertyType2",
    "BooleanValue",
    "BoundedBy",
    "BoundedFeatureType",
    "BoundingShapeType",
    "Bspline",
    "BsplineType",
    "CartesianCs1",
    "CartesianCs2",
    "CartesianCspropertyType",
    "CartesianCsref",
    "CartesianCstype",
    "CatalogSymbol",
    "Category",
    "CategoryExtent",
    "CategoryExtentType",
    "CategoryList",
    "CategoryPropertyType",
    "CenterLineOf",
    "CenterOf",
    "CharacterString",
    "CharacterStringPropertyType",
    "CiAddress",
    "CiAddressPropertyType",
    "CiAddressType",
    "CiCitation",
    "CiCitationPropertyType",
    "CiCitationType",
    "MdIdentifier",
    "MdIdentifierPropertyType",
    "MdIdentifierType",
    "RsIdentifier",
    "RsIdentifierType",
    "CiContact",
    "CiContactPropertyType",
    "CiContactType",
    "CiDate",
    "CiDatePropertyType",
    "CiDateType",
    "CiDateTypeCode",
    "CiDateTypeCodePropertyType",
    "CiOnLineFunctionCode",
    "CiOnLineFunctionCodePropertyType",
    "CiOnlineResource",
    "CiOnlineResourcePropertyType",
    "CiOnlineResourceType",
    "CiPresentationFormCode",
    "CiPresentationFormCodePropertyType",
    "CiResponsibleParty",
    "CiResponsiblePartyPropertyType",
    "CiResponsiblePartyType",
    "CiRoleCode",
    "CiRoleCodePropertyType",
    "CiSeries",
    "CiSeriesPropertyType",
    "CiSeriesType",
    "CiTelephone",
    "CiTelephonePropertyType",
    "CiTelephoneType",
    "Circle",
    "CircleByCenterPoint",
    "CircleByCenterPointType",
    "CircleType",
    "Clothoid",
    "ClothoidType",
    "CodeListType",
    "CodeListValueType",
    "CodeOrNilReasonListType",
    "CodeType",
    "CodeWithAuthorityType",
    "CompassPointEnumeration",
    "CompositeCurve",
    "CompositeCurveType",
    "Curve",
    "CurvePropertyType",
    "CurveSegmentArrayPropertyType",
    "CurveType",
    "OffsetCurve",
    "OffsetCurveType",
    "OrientableCurve",
    "OrientableCurveType",
    "BaseCurve",
    "CurveMember",
    "Segments",
    "CompositeSurface",
    "CompositeSurfaceType",
    "OrientableSurface",
    "OrientableSurfaceType",
    "SurfacePropertyType",
    "BaseSurface",
    "SurfaceMember",
    "CompoundCrspropertyType",
    "CompoundCrsref",
    "ConcatenatedOperationPropertyType",
    "ConcatenatedOperationRef",
    "Cone",
    "ConeType",
    "AbstractTopoPrimitiveType",
    "ContainerPropertyType",
    "DirectedEdgePropertyType",
    "DirectedFacePropertyType",
    "DirectedNodePropertyType",
    "DirectedTopoSolidPropertyType",
    "Edge",
    "EdgeType",
    "Face",
    "FaceType",
    "IsolatedPropertyType",
    "Node",
    "NodeType",
    "TopoSolid",
    "TopoSolidType",
    "Container",
    "DirectedEdge",
    "DirectedFace",
    "DirectedNode",
    "DirectedTopoSolid",
    "Isolated",
    "ConventionalUnit",
    "ConventionalUnitType",
    "ConversionPropertyType",
    "ConversionRef",
    "ConversionToPreferredUnit",
    "ConversionToPreferredUnitType",
    "CoordinateOperationAccuracy",
    "CoordinateOperationRef",
    "CoordinateSystem",
    "CoordinateSystemAxis",
    "CoordinateSystemAxisPropertyType",
    "CoordinateSystemAxisRef",
    "CoordinateSystemAxisType",
    "CoordinateSystemPropertyType",
    "CoordinateSystemRef",
    "Coordinates",
    "CoordinatesType",
    "Count",
    "CountExtent",
    "CountList",
    "CountPropertyType",
    "Country",
    "CountryPropertyType",
    "CoverageFunction",
    "CoverageFunctionType",
    "CoverageMappingRule",
    "CrsRef",
    "CubicSpline",
    "CubicSplineType",
    "CurveArrayProperty",
    "CurveArrayPropertyType",
    "CurveInterpolationType",
    "CurveMembers",
    "CurveProperty",
    "Cylinder",
    "CylinderType",
    "CylindricalCs",
    "CylindricalCspropertyType",
    "CylindricalCsref",
    "CylindricalCstype",
    "DataBlock",
    "DataBlockType",
    "DataSource",
    "DataSourceReference",
    "Date",
    "DatePropertyType",
    "DateTime",
    "DateTimePropertyType",
    "DatumPropertyType",
    "DatumRef",
    "DecimalType",
    "DecimalMinutes",
    "DecimalPropertyType",
    "DefaultCodeSpace",
    "Definition",
    "DefinitionBaseType",
    "DefinitionProxy",
    "DefinitionProxyType",
    "DefinitionRef",
    "DefinitionType",
    "Degrees",
    "DegreesType",
    "DegreesTypeDirection",
    "DerivationUnitTerm",
    "DerivationUnitTermType",
    "DerivedCrspropertyType",
    "DerivedCrsref",
    "DerivedCrstype",
    "DerivedUnit",
    "DerivedUnitType",
    "Description",
    "DescriptionReference",
    "DefinitionCollection",
    "Dictionary",
    "DictionaryEntryType",
    "DictionaryType",
    "DefinitionMember",
    "DictionaryEntry",
    "DirectPositionListType",
    "DirectPositionType",
    "Direction",
    "DirectionDescriptionType",
    "DirectionPropertyType",
    "DirectionVectorType",
    "Distance",
    "DistancePropertyType",
    "DmsAngle",
    "DmsAngleValue",
    "DmsangleType",
    "DomainSet",
    "DomainSetType",
    "DoubleOrNilReasonTupleList",
    "DqAbsoluteExternalPositionalAccuracy",
    "DqAbsoluteExternalPositionalAccuracyPropertyType",
    "DqAbsoluteExternalPositionalAccuracyType",
    "DqAccuracyOfAtimeMeasurement",
    "DqAccuracyOfAtimeMeasurementPropertyType",
    "DqAccuracyOfAtimeMeasurementType",
    "DqCompletenessCommission",
    "DqCompletenessCommissionPropertyType",
    "DqCompletenessCommissionType",
    "DqCompletenessOmission",
    "DqCompletenessOmissionPropertyType",
    "DqCompletenessOmissionType",
    "DqCompletenessPropertyType",
    "DqConceptualConsistency",
    "DqConceptualConsistencyPropertyType",
    "DqConceptualConsistencyType",
    "DqConformanceResult",
    "DqConformanceResultPropertyType",
    "DqConformanceResultType",
    "DqDataQuality",
    "DqDataQualityPropertyType",
    "DqDataQualityType",
    "DqDomainConsistency",
    "DqDomainConsistencyPropertyType",
    "DqDomainConsistencyType",
    "DqElementPropertyType",
    "DqEvaluationMethodTypeCode",
    "DqEvaluationMethodTypeCodePropertyType",
    "DqFormatConsistency",
    "DqFormatConsistencyPropertyType",
    "DqFormatConsistencyType",
    "DqGriddedDataPositionalAccuracy",
    "DqGriddedDataPositionalAccuracyPropertyType",
    "DqGriddedDataPositionalAccuracyType",
    "DqLogicalConsistencyPropertyType",
    "DqNonQuantitativeAttributeAccuracy",
    "DqNonQuantitativeAttributeAccuracyPropertyType",
    "DqNonQuantitativeAttributeAccuracyType",
    "DqPositionalAccuracyPropertyType",
    "DqQuantitativeAttributeAccuracy",
    "DqQuantitativeAttributeAccuracyPropertyType",
    "DqQuantitativeAttributeAccuracyType",
    "DqQuantitativeResult",
    "DqQuantitativeResultPropertyType",
    "DqQuantitativeResultType",
    "DqRelativeInternalPositionalAccuracy",
    "DqRelativeInternalPositionalAccuracyPropertyType",
    "DqRelativeInternalPositionalAccuracyType",
    "DqResultPropertyType",
    "DqScope",
    "DqScopePropertyType",
    "DqScopeType",
    "DqTemporalAccuracyPropertyType",
    "DqTemporalConsistency",
    "DqTemporalConsistencyPropertyType",
    "DqTemporalConsistencyType",
    "DqTemporalValidity",
    "DqTemporalValidityPropertyType",
    "DqTemporalValidityType",
    "DqThematicAccuracyPropertyType",
    "DqThematicClassificationCorrectness",
    "DqThematicClassificationCorrectnessPropertyType",
    "DqThematicClassificationCorrectnessType",
    "DqTopologicalConsistency",
    "DqTopologicalConsistencyPropertyType",
    "DqTopologicalConsistencyType",
    "DsAssociation",
    "DsAssociationPropertyType",
    "DsAssociationType",
    "DsAssociationTypeCode",
    "DsAssociationTypeCodePropertyType",
    "DsInitiativePropertyType",
    "DsInitiativeTypeCode",
    "DsInitiativeTypeCodePropertyType",
    "DsOtherAggregatePropertyType",
    "DsPlatformPropertyType",
    "DsProductionSeriesPropertyType",
    "DsSensorPropertyType",
    "DsSeriesPropertyType",
    "DsStereoMatePropertyType",
    "Duration",
    "DynamicFeature",
    "DynamicFeatureCollection",
    "DynamicFeatureCollectionType",
    "DynamicFeatureMemberType",
    "DynamicMembers",
    "DynamicFeatureType",
    "EdgeOf",
    "Ellipsoid1",
    "Ellipsoid2",
    "EllipsoidPropertyType",
    "EllipsoidRef",
    "EllipsoidType",
    "EllipsoidalCs1",
    "EllipsoidalCs2",
    "EllipsoidalCspropertyType",
    "EllipsoidalCsref",
    "EllipsoidalCstype",
    "EngineeringCrspropertyType",
    "EngineeringCrsref",
    "EngineeringDatumRef",
    "Envelope",
    "EnvelopeType",
    "EnvelopeWithTimePeriod",
    "EnvelopeWithTimePeriodType",
    "ExBoundingPolygon",
    "ExBoundingPolygonPropertyType",
    "ExBoundingPolygonType",
    "ExExtentPropertyType",
    "ExGeographicBoundingBox",
    "ExGeographicBoundingBoxPropertyType",
    "ExGeographicBoundingBoxType",
    "ExGeographicDescription",
    "ExGeographicDescriptionPropertyType",
    "ExGeographicDescriptionType",
    "ExGeographicExtentPropertyType",
    "ExSpatialTemporalExtent",
    "ExSpatialTemporalExtentPropertyType",
    "ExSpatialTemporalExtentType",
    "ExTemporalExtent",
    "ExTemporalExtentPropertyType",
    "ExTemporalExtentType",
    "ExtentOf",
    "Exterior",
    "FeatureProperty",
    "File",
    "FileType",
    "FileValueModelType",
    "Formula",
    "FormulaType",
    "GeneralConversionRef",
    "GeneralTransformationPropertyType",
    "GeneralTransformationRef",
    "GenericMetaData",
    "GenericMetaDataType",
    "GenericNamePropertyType",
    "GeocentricCrspropertyType",
    "GeocentricCrsref",
    "Geodesic",
    "GeodesicString",
    "GeodesicStringType",
    "GeodesicType",
    "GeodeticDatumRef",
    "GeographicCrsref",
    "GeometricComplex",
    "GeometricComplexPropertyType",
    "GeometricComplexType",
    "GeometricPrimitivePropertyType",
    "GeometryArrayPropertyType",
    "GeometryPropertyType",
    "MultiGeometry",
    "MultiGeometryType",
    "GeometryMember",
    "GeometryMembers",
    "GmObjectPropertyType",
    "GmPointPropertyType",
    "GreenwichLongitude",
    "Grid",
    "GridCoverage",
    "GridCoverageType",
    "GridDomain",
    "GridDomainType",
    "GridEnvelopeType",
    "GridFunction",
    "GridFunctionType",
    "GridLengthType",
    "GridLimitsType",
    "GridType",
    "Group",
    "History",
    "HistoryPropertyType",
    "IdentifiedObjectType",
    "Identifier",
    "ImageCrspropertyType",
    "ImageCrsref",
    "ImageDatumRef",
    "IncludesParameter",
    "IncrementOrder",
    "IndirectEntry",
    "IndirectEntryType",
    "InlinePropertyType",
    "Integer",
    "IntegerPropertyType",
    "IntegerValue",
    "IntegerValueList",
    "Interior",
    "KnotPropertyType",
    "KnotType",
    "KnotTypesType",
    "LanguageCode",
    "LanguageCodePropertyType",
    "Length",
    "LengthPropertyType",
    "LengthType",
    "LiLineage",
    "LiLineagePropertyType",
    "LiLineageType",
    "LiProcessStep",
    "LiProcessStepPropertyType",
    "LiProcessStepType",
    "LiSource",
    "LiSourcePropertyType",
    "LiSourceType",
    "LineString",
    "LineStringSegment",
    "LineStringSegmentArrayPropertyType",
    "LineStringSegmentType",
    "LineStringType",
    "LinearCs",
    "LinearCspropertyType",
    "LinearCsref",
    "LinearCstype",
    "LinearRing",
    "LinearRingPropertyType",
    "LinearRingType",
    "LocalName",
    "LocalNamePropertyType",
    "LocalisedCharacterString",
    "LocalisedCharacterStringPropertyType",
    "LocalisedCharacterStringType",
    "Location",
    "LocationKeyWord",
    "LocationName",
    "LocationPropertyType",
    "LocationReference",
    "LocationString",
    "MappingRule",
    "MappingRuleType",
    "MaximumOccurs",
    "MaximumValue",
    "MdAggregateInformation",
    "MdAggregateInformationPropertyType",
    "MdAggregateInformationType",
    "MdApplicationSchemaInformation",
    "MdApplicationSchemaInformationPropertyType",
    "MdApplicationSchemaInformationType",
    "MdBand",
    "MdBandPropertyType",
    "MdBandType",
    "MdBrowseGraphic",
    "MdBrowseGraphicPropertyType",
    "MdBrowseGraphicType",
    "MdCellGeometryCode",
    "MdCellGeometryCodePropertyType",
    "MdCharacterSetCode",
    "MdCharacterSetCodePropertyType",
    "MdClassificationCode",
    "MdClassificationCodePropertyType",
    "MdConstraints",
    "MdConstraintsPropertyType",
    "MdConstraintsType",
    "MdContentInformationPropertyType",
    "MdCoverageContentTypeCode",
    "MdCoverageContentTypeCodePropertyType",
    "MdCoverageDescription",
    "MdCoverageDescriptionPropertyType",
    "MdCoverageDescriptionType",
    "MdDataIdentification",
    "MdDataIdentificationPropertyType",
    "MdDataIdentificationType",
    "MdDatatypeCode",
    "MdDatatypeCodePropertyType",
    "MdDigitalTransferOptions",
    "MdDigitalTransferOptionsPropertyType",
    "MdDigitalTransferOptionsType",
    "MdDimension",
    "MdDimensionNameTypeCode",
    "MdDimensionNameTypeCodePropertyType",
    "MdDimensionPropertyType",
    "MdDimensionType",
    "MdDistribution",
    "MdDistributionPropertyType",
    "MdDistributionType",
    "MdDistributionUnits",
    "MdDistributionUnitsPropertyType",
    "MdDistributor",
    "MdDistributorPropertyType",
    "MdDistributorType",
    "MdFormat",
    "MdFormatPropertyType",
    "MdFormatType",
    "MdExtendedElementInformation",
    "MdExtendedElementInformationPropertyType",
    "MdExtendedElementInformationType",
    "MdFeatureCatalogueDescription",
    "MdFeatureCatalogueDescriptionPropertyType",
    "MdFeatureCatalogueDescriptionType",
    "MdGeometricObjectTypeCode",
    "MdGeometricObjectTypeCodePropertyType",
    "MdGeometricObjects",
    "MdGeometricObjectsPropertyType",
    "MdGeometricObjectsType",
    "MdGeorectified",
    "MdGeorectifiedPropertyType",
    "MdGeorectifiedType",
    "MdGeoreferenceable",
    "MdGeoreferenceablePropertyType",
    "MdGeoreferenceableType",
    "MdGridSpatialRepresentation",
    "MdGridSpatialRepresentationPropertyType",
    "MdGridSpatialRepresentationType",
    "MdIdentificationPropertyType",
    "MdImageDescription",
    "MdImageDescriptionPropertyType",
    "MdImageDescriptionType",
    "MdImagingConditionCode",
    "MdImagingConditionCodePropertyType",
    "MdKeywordTypeCode",
    "MdKeywordTypeCodePropertyType",
    "MdKeywords",
    "MdKeywordsPropertyType",
    "MdKeywordsType",
    "MdLegalConstraints",
    "MdLegalConstraintsPropertyType",
    "MdLegalConstraintsType",
    "MdMaintenanceFrequencyCode",
    "MdMaintenanceFrequencyCodePropertyType",
    "MdMaintenanceInformation",
    "MdMaintenanceInformationPropertyType",
    "MdMaintenanceInformationType",
    "MdMedium",
    "MdMediumFormatCode",
    "MdMediumFormatCodePropertyType",
    "MdMediumNameCode",
    "MdMediumNameCodePropertyType",
    "MdMediumPropertyType",
    "MdMediumType",
    "MdMetadataExtensionInformation",
    "MdMetadataExtensionInformationPropertyType",
    "MdMetadataExtensionInformationType",
    "AbstractDsAggregate",
    "AbstractDsAggregateType",
    "DsAggregatePropertyType",
    "DsDataSet",
    "DsDataSetPropertyType",
    "DsDataSetType",
    "DsInitiative",
    "DsInitiativeType",
    "DsOtherAggregate",
    "DsOtherAggregateType",
    "DsPlatform",
    "DsPlatformType",
    "DsProductionSeries",
    "DsProductionSeriesType",
    "DsSensor",
    "DsSensorType",
    "DsSeries",
    "DsSeriesType",
    "DsStereoMate",
    "DsStereoMateType",
    "MdMetadata",
    "MdMetadataPropertyType",
    "MdMetadataType",
    "MdObligationCode",
    "MdObligationCodePropertyType",
    "MdObligationCodeType",
    "MdPixelOrientationCode",
    "MdPixelOrientationCodePropertyType",
    "MdPixelOrientationCodeType",
    "MdPortrayalCatalogueReference",
    "MdPortrayalCatalogueReferencePropertyType",
    "MdPortrayalCatalogueReferenceType",
    "MdProgressCode",
    "MdProgressCodePropertyType",
    "MdRangeDimension",
    "MdRangeDimensionPropertyType",
    "MdRangeDimensionType",
    "MdReferenceSystem",
    "MdReferenceSystemPropertyType",
    "MdReferenceSystemType",
    "MdRepresentativeFraction",
    "MdRepresentativeFractionPropertyType",
    "MdRepresentativeFractionType",
    "MdResolution",
    "MdResolutionPropertyType",
    "MdResolutionType",
    "MdRestrictionCode",
    "MdRestrictionCodePropertyType",
    "MdScopeCode",
    "MdScopeCodePropertyType",
    "MdScopeDescription",
    "MdScopeDescriptionPropertyType",
    "MdScopeDescriptionType",
    "MdSecurityConstraints",
    "MdSecurityConstraintsPropertyType",
    "MdSecurityConstraintsType",
    "MdServiceIdentification",
    "MdServiceIdentificationPropertyType",
    "MdServiceIdentificationType",
    "MdSpatialRepresentationPropertyType",
    "MdSpatialRepresentationTypeCode",
    "MdSpatialRepresentationTypeCodePropertyType",
    "MdStandardOrderProcess",
    "MdStandardOrderProcessPropertyType",
    "MdStandardOrderProcessType",
    "MdTopicCategoryCode",
    "MdTopicCategoryCodePropertyType",
    "MdTopicCategoryCodeType",
    "MdTopologyLevelCode",
    "MdTopologyLevelCodePropertyType",
    "MdUsage",
    "MdUsagePropertyType",
    "MdUsageType",
    "MdVectorSpatialRepresentation",
    "MdVectorSpatialRepresentationPropertyType",
    "MdVectorSpatialRepresentationType",
    "Measure1",
    "Measure2",
    "MeasureListType",
    "MeasureOrNilReasonListType",
    "MeasurePropertyType",
    "MeasureType",
    "MemberName",
    "MemberNamePropertyType",
    "MemberNameType",
    "MetaDataProperty",
    "MetaDataPropertyType",
    "Method",
    "MethodFormula",
    "MinimumOccurs",
    "MinimumValue",
    "Minutes",
    "ModifiedCoordinate",
    "MovingObjectStatus",
    "MovingObjectStatusType",
    "MultiCenterLineOf",
    "MultiCenterOf",
    "MultiCoverage",
    "MultiCurve",
    "MultiCurveCoverage",
    "MultiCurveCoverageType",
    "MultiCurveDomain",
    "MultiCurveDomainType",
    "MultiCurveProperty",
    "MultiCurvePropertyType",
    "MultiCurveType",
    "MultiEdgeOf",
    "MultiExtentOf",
    "MultiGeometryProperty",
    "MultiGeometryPropertyType",
    "MultiLocation",
    "MultiPoint",
    "MultiPointCoverage",
    "MultiPointCoverageType",
    "MultiPointDomain",
    "MultiPointDomainType",
    "MultiPointProperty",
    "MultiPointPropertyType",
    "MultiPointType",
    "MultiPosition",
    "MultiSolid",
    "MultiSolidCoverage",
    "MultiSolidCoverageType",
    "MultiSolidDomain",
    "MultiSolidDomainType",
    "MultiSolidProperty",
    "MultiSolidPropertyType",
    "MultiSolidType",
    "MultiSurface",
    "MultiSurfaceCoverage",
    "MultiSurfaceCoverageType",
    "MultiSurfaceDomain",
    "MultiSurfaceDomainType",
    "MultiSurfaceProperty",
    "MultiSurfacePropertyType",
    "MultiSurfaceType",
    "Multiplicity",
    "MultiplicityPropertyType",
    "MultiplicityRange",
    "MultiplicityRangePropertyType",
    "MultiplicityRangeType",
    "MultiplicityType",
    "Name",
    "NilReasonEnumerationValue",
    "Null",
    "NumberPropertyType",
    "ObjectReferencePropertyType",
    "ObliqueCartesianCs",
    "ObliqueCartesianCspropertyType",
    "ObliqueCartesianCsref",
    "ObliqueCartesianCstype",
    "OperationMethod",
    "OperationMethodPropertyType",
    "OperationMethodRef",
    "OperationMethodType",
    "OperationParameter1",
    "OperationParameter2",
    "OperationParameterGroupPropertyType",
    "OperationParameterGroupRef",
    "OperationParameterPropertyType",
    "OperationParameterRef",
    "OperationParameterType",
    "OperationPropertyType",
    "OperationRef",
    "OperationVersion",
    "Origin",
    "ParameterValue1",
    "ParameterValueType",
    "PassThroughOperationPropertyType",
    "PassThroughOperationRef",
    "ConcatenatedOperation",
    "ConcatenatedOperationType",
    "CoordinateOperationPropertyType",
    "PassThroughOperation",
    "PassThroughOperationType",
    "CoordOperation",
    "UsesOperation",
    "UsesSingleOperation",
    "Patches",
    "PixelInCell",
    "Point",
    "PointArrayProperty",
    "PointArrayPropertyType",
    "PointMember",
    "PointMembers",
    "PointProperty",
    "PointPropertyType",
    "PointRep",
    "PointType",
    "PolarCs",
    "PolarCspropertyType",
    "PolarCsref",
    "PolarCstype",
    "Polygon",
    "PolygonPatch",
    "PolygonPatchArrayPropertyType",
    "PolygonPatchType",
    "PolygonPatches",
    "PolygonType",
    "PolyhedralSurface",
    "PolyhedralSurfaceType",
    "Pos",
    "PosList",
    "Position",
    "PrimeMeridian1",
    "PrimeMeridian2",
    "PrimeMeridianPropertyType",
    "PrimeMeridianRef",
    "PrimeMeridianType",
    "PriorityLocation",
    "PriorityLocationPropertyType",
    "ProjectedCrspropertyType",
    "ProjectedCrsref",
    "PtFreeText",
    "PtFreeTextPropertyType",
    "PtFreeTextType",
    "PtLocale",
    "PtLocaleContainer",
    "PtLocaleContainerPropertyType",
    "PtLocaleContainerType",
    "PtLocalePropertyType",
    "PtLocaleType",
    "Quantity",
    "QuantityExtent",
    "QuantityExtentType",
    "QuantityList",
    "QuantityPropertyType",
    "QuantityType",
    "QuantityTypeReference",
    "RangeMeaning",
    "RangeParameters",
    "RangeParametersType",
    "RangeSet",
    "RangeSetType",
    "Real",
    "RealPropertyType",
    "RealizationEpoch",
    "Record",
    "RecordPropertyType",
    "RecordType",
    "RecordTypePropertyType",
    "RecordTypeType",
    "Rectangle",
    "RectangleType",
    "RectifiedGrid",
    "RectifiedGridCoverage",
    "RectifiedGridCoverageType",
    "RectifiedGridDomain",
    "RectifiedGridDomainType",
    "RectifiedGridType",
    "ReferenceType",
    "RelatedTimeTypeRelativePosition",
    "Remarks",
    "ReversePropertyName",
    "Ring",
    "RingPropertyType",
    "RingType",
    "RoughConversionToPreferredUnit",
    "RsIdentifierPropertyType",
    "RsReferenceSystemPropertyType",
    "Scale",
    "ScalePropertyType",
    "ScaleType",
    "Scope",
    "ScopedName",
    "ScopedNamePropertyType",
    "SecondDefiningParameter1",
    "SecondDefiningParameter2",
    "SecondDefiningParameterIsSphere",
    "Seconds",
    "SemiMajorAxis",
    "SequenceRuleEnumeration",
    "SequenceRuleType",
    "Shell",
    "ShellPropertyType",
    "ShellType",
    "ShowValue",
    "SignType",
    "SingleCrsref",
    "SingleOperationPropertyType",
    "SingleOperationRef",
    "Solid",
    "SolidArrayProperty",
    "SolidArrayPropertyType",
    "SolidMembers",
    "SolidProperty",
    "CompositeSolid",
    "CompositeSolidType",
    "SolidPropertyType",
    "SolidMember",
    "SolidType",
    "SourceDimensions",
    "SpeedType",
    "Sphere",
    "SphereType",
    "SphericalCs1",
    "SphericalCs2",
    "SphericalCspropertyType",
    "SphericalCsref",
    "SphericalCstype",
    "Status",
    "StatusReference",
    "StringOrRefType",
    "StringValue",
    "SuccessionType",
    "Surface",
    "SurfaceArrayProperty",
    "SurfaceArrayPropertyType",
    "SurfaceInterpolationType",
    "SurfaceMembers",
    "SurfacePatchArrayPropertyType",
    "SurfaceProperty",
    "SurfaceType",
    "TargetDimensions",
    "TargetElement",
    "TemporalCrspropertyType",
    "TemporalCrsref",
    "TemporalCs",
    "TemporalCspropertyType",
    "TemporalCsref",
    "TemporalCstype",
    "TemporalDatumRef",
    "TimeCalendar",
    "TimeCalendarEra",
    "TimeCalendarEraPropertyType",
    "TimeCalendarEraType",
    "TimeCalendarPropertyType",
    "TimeCalendarType",
    "TimeClock",
    "TimeClockPropertyType",
    "TimeClockType",
    "TimeCoordinateSystem",
    "TimeCoordinateSystemType",
    "TimeCs1",
    "TimeCs2",
    "TimeCspropertyType",
    "TimeCstype",
    "AbstractTimeGeometricPrimitive",
    "AbstractTimeGeometricPrimitiveType",
    "AbstractTimePrimitive",
    "AbstractTimePrimitiveType",
    "AbstractTimeTopologyPrimitive",
    "AbstractTimeTopologyPrimitiveType",
    "RelatedTimeType",
    "TimeEdge",
    "TimeEdgePropertyType",
    "TimeEdgeType",
    "TimeInstant",
    "TimeInstantPropertyType",
    "TimeInstantType",
    "TimeNode",
    "TimeNodePropertyType",
    "TimeNodeType",
    "TimePeriod",
    "TimePeriodPropertyType",
    "TimePeriodType",
    "TimePrimitivePropertyType",
    "TimeIndeterminateValueType",
    "TimeInterval",
    "TimeIntervalLengthType",
    "TimeOrdinalEra",
    "TimeOrdinalEraPropertyType",
    "TimeOrdinalEraType",
    "TimeOrdinalReferenceSystem",
    "TimeOrdinalReferenceSystemType",
    "TimePosition",
    "TimePositionType",
    "TimeReferenceSystem",
    "TimeReferenceSystemType",
    "TimeTopologyComplex",
    "TimeTopologyComplexPropertyType",
    "TimeTopologyComplexType",
    "TimeTopologyPrimitivePropertyType",
    "TimeType",
    "TimeUnitTypeValue",
    "Tin",
    "TinType",
    "TmPeriodDuration",
    "TmPeriodDurationPropertyType",
    "TmPrimitivePropertyType",
    "TopoComplex",
    "TopoComplexMemberType",
    "TopoComplexType",
    "MaximalComplex",
    "SubComplex",
    "SuperComplex",
    "TopoComplexProperty",
    "TopoCurve",
    "TopoCurveProperty",
    "TopoCurvePropertyType",
    "TopoCurveType",
    "TopoPoint",
    "TopoPointProperty",
    "TopoPointPropertyType",
    "TopoPointType",
    "TopoPrimitiveArrayAssociationType",
    "TopoPrimitiveMember",
    "TopoPrimitiveMemberType",
    "TopoPrimitiveMembers",
    "TopoSurface",
    "TopoSurfaceProperty",
    "TopoSurfacePropertyType",
    "TopoSurfaceType",
    "TopoVolume",
    "TopoVolumeProperty",
    "TopoVolumePropertyType",
    "TopoVolumeType",
    "Track",
    "Transformation",
    "TransformationPropertyType",
    "TransformationRef",
    "TransformationType",
    "Triangle",
    "TrianglePatchArrayPropertyType",
    "TrianglePatches",
    "TriangleType",
    "TriangulatedSurface",
    "TriangulatedSurfaceType",
    "TupleList",
    "TypeName",
    "TypeNamePropertyType",
    "TypeNameType",
    "UnitDefinition",
    "UnitDefinitionType",
    "UnitOfMeasure",
    "UnitOfMeasurePropertyType",
    "UnitOfMeasureType",
    "UnlimitedInteger",
    "UnlimitedIntegerPropertyType",
    "UnlimitedIntegerType",
    "UomAnglePropertyType",
    "UomAreaPropertyType",
    "UomLengthPropertyType",
    "UomScalePropertyType",
    "UomTimePropertyType",
    "UomVelocityPropertyType",
    "UomVolumePropertyType",
    "Url",
    "UrlPropertyType",
    "UserDefinedCs",
    "UserDefinedCspropertyType",
    "UserDefinedCsref",
    "UserDefinedCstype",
    "UsesAffineCs",
    "UsesAxis",
    "UsesCartesianCs",
    "UsesCs",
    "UsesEllipsoid",
    "UsesEllipsoidalCs",
    "UsesMethod",
    "UsesObliqueCartesianCs",
    "UsesPrimeMeridian",
    "UsesSphericalCs",
    "UsesTemporalCs",
    "UsesTimeCs",
    "UsesVerticalCs",
    "ValidTime",
    "Value",
    "CompositeValue",
    "CompositeValueType",
    "ValueArray",
    "ValueArrayPropertyType",
    "ValueArrayType",
    "ValuePropertyType",
    "ValueComponent",
    "ValueComponents",
    "ValueFile",
    "ValueList",
    "ValueOfParameter",
    "ValueProperty",
    "ValuesOfGroup",
    "Vector",
    "VectorType",
    "VerticalCrspropertyType",
    "VerticalCrsref",
    "VerticalCs1",
    "VerticalCs2",
    "VerticalCspropertyType",
    "VerticalCsref",
    "VerticalCstype",
    "VerticalDatumRef",
    "VolumeType",
]
