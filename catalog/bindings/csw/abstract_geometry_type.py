from dataclasses import dataclass, field
from typing import List, Optional
from bindings.csw.coordinate_operation_name import CoordinateOperationName
from bindings.csw.cs_name import CsName
from bindings.csw.datum_name import DatumName
from bindings.csw.description_1 import Description1
from bindings.csw.ellipsoid_name import EllipsoidName
from bindings.csw.group_name import GroupName
from bindings.csw.meridian_name import MeridianName
from bindings.csw.meta_data_property import MetaDataProperty
from bindings.csw.method_name import MethodName
from bindings.csw.name import Name
from bindings.csw.parameter_name import ParameterName

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class AbstractGeometryType:
    """All geometry elements are derived directly or indirectly from this
    abstract supertype. A geometry element may have an identifying attribute
    ("gml:id"), a name (attribute "name") and a description (attribute
    "description"). It may be associated.

    with a spatial reference system (attribute "srsName"). The following rules shall be adhered: - Every geometry type shall derive
    from this abstract type. - Every geometry element (i.e. an element of a geometry type) shall be directly or indirectly in the
    substitution group of _Geometry.

    :ivar meta_data_property:
    :ivar description:
    :ivar group_name:
    :ivar parameter_name:
    :ivar method_name:
    :ivar coordinate_operation_name:
    :ivar ellipsoid_name:
    :ivar meridian_name:
    :ivar datum_name:
    :ivar cs_name:
    :ivar gid: This attribute is included for backward compatibility
        with GML 2 and is deprecated with GML 3. This identifer is
        superceded by "gml:id" inherited from AbstractGMLType. The
        attribute "gid" should not be used anymore and may be deleted in
        future versions of GML without further notice.
    :ivar name: Multiple names may be provided.  These will often be
        distinguished by being assigned by different authorities, as
        indicated by the value of the codeSpace attribute.  In an
        instance document there will usually only be one name per
        authority.
    :ivar id:
    :ivar srs_name_attribute: In general this reference points to a CRS
        instance of gml:CoordinateReferenceSystemType (see
        coordinateReferenceSystems.xsd). For well known references it is
        not required that the CRS description exists at the location the
        URI points to. If no srsName attribute is given, the CRS must be
        specified as part of the larger context this geometry element is
        part of, e.g. a geometric element like point, curve, etc. It is
        expected that this attribute will be specified at the direct
        position level only in rare cases.
    :ivar srs_dimension: The "srsDimension" is the length of coordinate
        sequence (the number of entries in the list). This dimension is
        specified by the coordinate reference system. When the srsName
        attribute is omitted, this attribute shall be omitted.
    :ivar axis_labels: Ordered list of labels for all the axes of this
        CRS. The gml:axisAbbrev value should be used for these axis
        labels, after spaces and forbiddden characters are removed. When
        the srsName attribute is included, this attribute is optional.
        When the srsName attribute is omitted, this attribute shall also
        be omitted.
    :ivar uom_labels: Ordered list of unit of measure (uom) labels for
        all the axes of this CRS. The value of the string in the
        gml:catalogSymbol should be used for this uom labels, after
        spaces and forbiddden characters are removed. When the
        axisLabels attribute is included, this attribute shall also be
        included. When the axisLabels attribute is omitted, this
        attribute shall also be omitted.
    """

    meta_data_property: List[MetaDataProperty] = field(
        default_factory=list,
        metadata={
            "name": "metaDataProperty",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    description: Optional[Description1] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    group_name: List[GroupName] = field(
        default_factory=list,
        metadata={
            "name": "groupName",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    parameter_name: List[ParameterName] = field(
        default_factory=list,
        metadata={
            "name": "parameterName",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    method_name: List[MethodName] = field(
        default_factory=list,
        metadata={
            "name": "methodName",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    coordinate_operation_name: List[CoordinateOperationName] = field(
        default_factory=list,
        metadata={
            "name": "coordinateOperationName",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    ellipsoid_name: List[EllipsoidName] = field(
        default_factory=list,
        metadata={
            "name": "ellipsoidName",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    meridian_name: List[MeridianName] = field(
        default_factory=list,
        metadata={
            "name": "meridianName",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    datum_name: List[DatumName] = field(
        default_factory=list,
        metadata={
            "name": "datumName",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    cs_name: List[CsName] = field(
        default_factory=list,
        metadata={
            "name": "csName",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    gid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    name: List[Name] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    srs_name_attribute: Optional[str] = field(
        default=None,
        metadata={
            "name": "srsName",
            "type": "Attribute",
        },
    )
    srs_dimension: Optional[int] = field(
        default=None,
        metadata={
            "name": "srsDimension",
            "type": "Attribute",
        },
    )
    axis_labels: List[str] = field(
        default_factory=list,
        metadata={
            "name": "axisLabels",
            "type": "Attribute",
            "tokens": True,
        },
    )
    uom_labels: List[str] = field(
        default_factory=list,
        metadata={
            "name": "uomLabels",
            "type": "Attribute",
            "tokens": True,
        },
    )
