from dataclasses import dataclass, field
from typing import Optional
from bindings.csw.coordinate_operation_name import CoordinateOperationName
from bindings.csw.cs_name import CsName
from bindings.csw.datum_name import DatumName
from bindings.csw.ellipsoid_name import EllipsoidName
from bindings.csw.group_name import GroupName
from bindings.csw.meridian_name import MeridianName
from bindings.csw.method_name import MethodName
from bindings.csw.name import Name
from bindings.csw.parameter_name import ParameterName
from bindings.csw.remarks import Remarks
from bindings.csw.srs_name import SrsName

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class IdentifierType:
    """An identification of a CRS object.

    The first use of the IdentifierType for an object, if any, is
    normally the primary identification code, and any others are
    aliases.

    :ivar group_name:
    :ivar parameter_name:
    :ivar method_name:
    :ivar coordinate_operation_name:
    :ivar ellipsoid_name:
    :ivar meridian_name:
    :ivar datum_name:
    :ivar cs_name:
    :ivar srs_name:
    :ivar name: The code or name for this Identifier, often from a
        controlled list or pattern defined by a code space. The optional
        codeSpace attribute is normally included to identify or
        reference a code space within which one or more codes are
        defined. This code space is often defined by some authority
        organization, where one organization may define multiple code
        spaces. The range and format of each Code Space identifier is
        defined by that code space authority. Information about that
        code space authority can be included as metaDataProperty
        elements which are optionally allowed in all CRS objects.
    :ivar version:
    :ivar remarks: Remarks about this code or alias.
    """
    group_name: Optional[GroupName] = field(
        default=None,
        metadata={
            "name": "groupName",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    parameter_name: Optional[ParameterName] = field(
        default=None,
        metadata={
            "name": "parameterName",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    method_name: Optional[MethodName] = field(
        default=None,
        metadata={
            "name": "methodName",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    coordinate_operation_name: Optional[CoordinateOperationName] = field(
        default=None,
        metadata={
            "name": "coordinateOperationName",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    ellipsoid_name: Optional[EllipsoidName] = field(
        default=None,
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
        }
    )
    datum_name: Optional[DatumName] = field(
        default=None,
        metadata={
            "name": "datumName",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    cs_name: Optional[CsName] = field(
        default=None,
        metadata={
            "name": "csName",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    srs_name: Optional[SrsName] = field(
        default=None,
        metadata={
            "name": "srsName",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    name: Optional[Name] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    version: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    remarks: Optional[Remarks] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
