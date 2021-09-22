from dataclasses import dataclass, field
from typing import List, Optional
from bindings.csw_publication.coordinate_operation_name import CoordinateOperationName
from bindings.csw_publication.cs_name import CsName
from bindings.csw_publication.datum_name import DatumName
from bindings.csw_publication.description_2 import Description2
from bindings.csw_publication.ellipsoid_name import EllipsoidName
from bindings.csw_publication.group_name import GroupName
from bindings.csw_publication.meridian_name import MeridianName
from bindings.csw_publication.meta_data_property import MetaDataProperty
from bindings.csw_publication.method_name import MethodName
from bindings.csw_publication.name import Name
from bindings.csw_publication.parameter_name import ParameterName
from bindings.csw_publication.srs_name import SrsName

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class PrimeMeridianBaseType:
    """
    Basic encoding for prime meridian objects, simplifying and restricting the
    DefinitionType as needed.
    """
    meta_data_property: List[MetaDataProperty] = field(
        default_factory=list,
        metadata={
            "name": "metaDataProperty",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    description: Optional[Description2] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    group_name: List[GroupName] = field(
        default_factory=list,
        metadata={
            "name": "groupName",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    parameter_name: List[ParameterName] = field(
        default_factory=list,
        metadata={
            "name": "parameterName",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    method_name: List[MethodName] = field(
        default_factory=list,
        metadata={
            "name": "methodName",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    coordinate_operation_name: List[CoordinateOperationName] = field(
        default_factory=list,
        metadata={
            "name": "coordinateOperationName",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    ellipsoid_name: List[EllipsoidName] = field(
        default_factory=list,
        metadata={
            "name": "ellipsoidName",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    meridian_name: Optional[MeridianName] = field(
        default=None,
        metadata={
            "name": "meridianName",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        }
    )
    datum_name: List[DatumName] = field(
        default_factory=list,
        metadata={
            "name": "datumName",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    cs_name: List[CsName] = field(
        default_factory=list,
        metadata={
            "name": "csName",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    srs_name: List[SrsName] = field(
        default_factory=list,
        metadata={
            "name": "srsName",
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
