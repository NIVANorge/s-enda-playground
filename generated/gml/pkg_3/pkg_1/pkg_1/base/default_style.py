from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional
from generated.gml.pkg_3.pkg_1.pkg_1.base.gml_base import AbstractGmltype
from generated.gml.pkg_3.pkg_1.pkg_1.base.measures import ScaleType
from generated.gml.pkg_3.pkg_1.pkg_1.smil.smil20 import (
    Animate,
    AnimateColor,
    AnimateMotion,
    Set,
)
from generated.xlink import (
    ActuateType,
    ShowType,
    TypeType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


class AesheticCriteriaType(Enum):
    """
    Graph-specific styling property.
    """
    MIN_CROSSINGS = "MIN_CROSSINGS"
    MIN_AREA = "MIN_AREA"
    MIN_BENDS = "MIN_BENDS"
    MAX_BENDS = "MAX_BENDS"
    UNIFORM_BENDS = "UNIFORM_BENDS"
    MIN_SLOPES = "MIN_SLOPES"
    MIN_EDGE_LENGTH = "MIN_EDGE_LENGTH"
    MAX_EDGE_LENGTH = "MAX_EDGE_LENGTH"
    UNIFORM_EDGE_LENGTH = "UNIFORM_EDGE_LENGTH"
    MAX_ANGULAR_RESOLUTION = "MAX_ANGULAR_RESOLUTION"
    MIN_ASPECT_RATIO = "MIN_ASPECT_RATIO"
    MAX_SYMMETRIES = "MAX_SYMMETRIES"


class DrawingTypeType(Enum):
    """
    Graph-specific styling property.
    """
    POLYLINE = "POLYLINE"
    ORTHOGONAL = "ORTHOGONAL"


class GraphTypeType(Enum):
    """
    Graph-specific styling property.
    """
    TREE = "TREE"
    BICONNECTED = "BICONNECTED"


@dataclass
class LabelType:
    """
    Label is mixed -- composed of text and XPath expressions used to extract
    the useful information from the feature.
    """
    transform: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "LabelExpression",
                    "type": str,
                    "namespace": "http://www.opengis.net/gml",
                },
            ),
        }
    )


class LineTypeType(Enum):
    """
    Graph-specific styling property.
    """
    STRAIGHT = "STRAIGHT"
    BENT = "BENT"


class QueryGrammarEnumeration(Enum):
    """
    Used to specify the grammar of the feature query mechanism.
    """
    XPATH = "xpath"
    XQUERY = "xquery"
    OTHER = "other"


@dataclass
class StyleVariationType:
    """
    Used to vary individual graphic parameters and attributes of the style,
    symbol or text.
    """
    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
    style_property: Optional[str] = field(
        default=None,
        metadata={
            "name": "styleProperty",
            "type": "Attribute",
            "required": True,
        }
    )
    feature_property_range: Optional[str] = field(
        default=None,
        metadata={
            "name": "featurePropertyRange",
            "type": "Attribute",
        }
    )


class SymbolTypeEnumeration(Enum):
    """
    Used to specify the type of the symbol used.
    """
    SVG = "svg"
    XPATH = "xpath"
    OTHER = "other"


@dataclass
class AbstractStyleType(AbstractGmltype):
    """[complexType of] The value of the top-level property.

    It is an abstract element. Used as the head element of the
    substitution group for extensibility purposes.
    """


@dataclass
class BaseStyleDescriptorType(AbstractGmltype):
    """
    Base complex type for geometry, topology, label and graph styles.
    """
    spatial_resolution: Optional[ScaleType] = field(
        default=None,
        metadata={
            "name": "spatialResolution",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    style_variation: List[StyleVariationType] = field(
        default_factory=list,
        metadata={
            "name": "styleVariation",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    animate: List[Animate] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2001/SMIL20/",
        }
    )
    animate_motion: List[AnimateMotion] = field(
        default_factory=list,
        metadata={
            "name": "animateMotion",
            "type": "Element",
            "namespace": "http://www.w3.org/2001/SMIL20/",
        }
    )
    animate_color: List[AnimateColor] = field(
        default_factory=list,
        metadata={
            "name": "animateColor",
            "type": "Element",
            "namespace": "http://www.w3.org/2001/SMIL20/",
        }
    )
    set: List[Set] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2001/SMIL20/",
        }
    )


@dataclass
class SymbolType:
    """[complexType of] The symbol property.

    Allows for remote referencing of symbols.
    """
    any_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        }
    )
    symbol_type: Optional[SymbolTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "symbolType",
            "type": "Attribute",
            "required": True,
        }
    )
    transform: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    about: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
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
class GraphStyleType(BaseStyleDescriptorType):
    """[complexType of] The style descriptor for a graph consisting of a number
    of features.

    Describes graph-specific style attributes.
    """
    planar: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    directed: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    grid: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    min_distance: Optional[float] = field(
        default=None,
        metadata={
            "name": "minDistance",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    min_angle: Optional[float] = field(
        default=None,
        metadata={
            "name": "minAngle",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    graph_type: Optional[GraphTypeType] = field(
        default=None,
        metadata={
            "name": "graphType",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    drawing_type: Optional[DrawingTypeType] = field(
        default=None,
        metadata={
            "name": "drawingType",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    line_type: Optional[LineTypeType] = field(
        default=None,
        metadata={
            "name": "lineType",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    aesthetic_criteria: List[AesheticCriteriaType] = field(
        default_factory=list,
        metadata={
            "name": "aestheticCriteria",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )


@dataclass
class LabelStyleType(BaseStyleDescriptorType):
    """
    [complexType of] The style descriptor for labels of a feature, geometry or
    topology.
    """
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        }
    )
    label: Optional[LabelType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        }
    )


@dataclass
class Style2(AbstractStyleType):
    """The value of the top-level property.

    It is an abstract element. Used as the head element of the
    substitution group for extensibility purposes.
    """
    class Meta:
        name = "_Style"
        namespace = "http://www.opengis.net/gml"


@dataclass
class Symbol(SymbolType):
    """The symbol property.

    Extends the gml:AssociationType to allow for remote referencing of
    symbols.
    """
    class Meta:
        name = "symbol"
        namespace = "http://www.opengis.net/gml"


@dataclass
class GraphStyle1(GraphStyleType):
    """The style descriptor for a graph consisting of a number of features.

    Describes graph-specific style attributes.
    """
    class Meta:
        name = "GraphStyle"
        namespace = "http://www.opengis.net/gml"


@dataclass
class LabelStyle1(LabelStyleType):
    """
    The style descriptor for labels of a feature, geometry or topology.
    """
    class Meta:
        name = "LabelStyle"
        namespace = "http://www.opengis.net/gml"


@dataclass
class GraphStylePropertyType:
    graph_style: Optional[GraphStyle1] = field(
        default=None,
        metadata={
            "name": "GraphStyle",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    about: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
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
class LabelStylePropertyType:
    label_style: Optional[LabelStyle1] = field(
        default=None,
        metadata={
            "name": "LabelStyle",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    about: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
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
class GraphStyle2(GraphStylePropertyType):
    class Meta:
        name = "graphStyle"
        namespace = "http://www.opengis.net/gml"


@dataclass
class LabelStyle2(LabelStylePropertyType):
    class Meta:
        name = "labelStyle"
        namespace = "http://www.opengis.net/gml"


@dataclass
class GeometryStyleType(BaseStyleDescriptorType):
    """
    [complexType of] The style descriptor for geometries of a feature.

    :ivar symbol:
    :ivar style: Deprecated in GML version 3.1.0. Use symbol with inline
        content instead.
    :ivar label_style:
    :ivar geometry_property:
    :ivar geometry_type:
    """
    symbol: Optional[Symbol] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    label_style: Optional[LabelStyle2] = field(
        default=None,
        metadata={
            "name": "labelStyle",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    geometry_property: Optional[str] = field(
        default=None,
        metadata={
            "name": "geometryProperty",
            "type": "Attribute",
        }
    )
    geometry_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "geometryType",
            "type": "Attribute",
        }
    )


@dataclass
class TopologyStyleType(BaseStyleDescriptorType):
    """[complexType of] The style descriptor for topologies of a feature.

    Describes individual topology elements styles.

    :ivar symbol:
    :ivar style: Deprecated in GML version 3.1.0. Use symbol with inline
        content instead.
    :ivar label_style:
    :ivar topology_property:
    :ivar topology_type:
    """
    symbol: Optional[Symbol] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    label_style: Optional[LabelStyle2] = field(
        default=None,
        metadata={
            "name": "labelStyle",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    topology_property: Optional[str] = field(
        default=None,
        metadata={
            "name": "topologyProperty",
            "type": "Attribute",
        }
    )
    topology_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "topologyType",
            "type": "Attribute",
        }
    )


@dataclass
class GeometryStyle1(GeometryStyleType):
    """
    The style descriptor for geometries of a feature.
    """
    class Meta:
        name = "GeometryStyle"
        namespace = "http://www.opengis.net/gml"


@dataclass
class TopologyStyle1(TopologyStyleType):
    """The style descriptor for topologies of a feature.

    Describes individual topology elements styles.
    """
    class Meta:
        name = "TopologyStyle"
        namespace = "http://www.opengis.net/gml"


@dataclass
class GeometryStylePropertyType:
    geometry_style: Optional[GeometryStyle1] = field(
        default=None,
        metadata={
            "name": "GeometryStyle",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    about: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
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
class TopologyStylePropertyType:
    topology_style: Optional[TopologyStyle1] = field(
        default=None,
        metadata={
            "name": "TopologyStyle",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    about: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
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
class GeometryStyle2(GeometryStylePropertyType):
    class Meta:
        name = "geometryStyle"
        namespace = "http://www.opengis.net/gml"


@dataclass
class TopologyStyle2(TopologyStylePropertyType):
    class Meta:
        name = "topologyStyle"
        namespace = "http://www.opengis.net/gml"


@dataclass
class FeatureStyleType(AbstractGmltype):
    """
    [complexType of] The style descriptor for features.
    """
    feature_constraint: Optional[str] = field(
        default=None,
        metadata={
            "name": "featureConstraint",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    geometry_style: List[GeometryStyle2] = field(
        default_factory=list,
        metadata={
            "name": "geometryStyle",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    topology_style: List[TopologyStyle2] = field(
        default_factory=list,
        metadata={
            "name": "topologyStyle",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    label_style: Optional[LabelStyle2] = field(
        default=None,
        metadata={
            "name": "labelStyle",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    feature_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "featureType",
            "type": "Attribute",
        }
    )
    base_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "baseType",
            "type": "Attribute",
        }
    )
    query_grammar: Optional[QueryGrammarEnumeration] = field(
        default=None,
        metadata={
            "name": "queryGrammar",
            "type": "Attribute",
        }
    )


@dataclass
class FeatureStyle1(FeatureStyleType):
    """
    The style descriptor for features.
    """
    class Meta:
        name = "FeatureStyle"
        namespace = "http://www.opengis.net/gml"


@dataclass
class FeatureStylePropertyType:
    feature_style: Optional[FeatureStyle1] = field(
        default=None,
        metadata={
            "name": "FeatureStyle",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    about: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
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
class FeatureStyle2(FeatureStylePropertyType):
    class Meta:
        name = "featureStyle"
        namespace = "http://www.opengis.net/gml"


@dataclass
class StyleType(AbstractStyleType):
    """[complexType of] Predefined concrete value of the top-level property.

    Encapsulates all other styling information.
    """
    feature_style: List[FeatureStyle2] = field(
        default_factory=list,
        metadata={
            "name": "featureStyle",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "min_occurs": 1,
        }
    )
    graph_style: Optional[GraphStyle2] = field(
        default=None,
        metadata={
            "name": "graphStyle",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )


@dataclass
class Style1(StyleType):
    """Predefined concrete value of the top-level property.

    Encapsulates all other styling information.
    """
    class Meta:
        name = "Style"
        namespace = "http://www.opengis.net/gml"


@dataclass
class DefaultStylePropertyType:
    """[complexType of] Top-level property.

    Used in application schemas to "attach" the styling information to
    GML data. The link between the data and the style should be
    established through this property only.
    """
    style: Optional[Style1] = field(
        default=None,
        metadata={
            "name": "Style",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    opengis_net_gml_style: Optional[Style2] = field(
        default=None,
        metadata={
            "name": "_Style",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    about: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
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
class DefaultStyle(DefaultStylePropertyType):
    """Top-level property.

    Used in application schemas to "attach" the styling information to
    GML data. The link between the data and the style should be
    established through this property only.
    """
    class Meta:
        name = "defaultStyle"
        namespace = "http://www.opengis.net/gml"
