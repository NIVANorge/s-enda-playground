from dataclasses import dataclass, field
from typing import Optional
from bindings.csw_publication.abstract_reference_system_type import AbstractReferenceSystemType
from bindings.csw_publication.uses_ellipsoidal_cs import UsesEllipsoidalCs
from bindings.csw_publication.uses_geodetic_datum import UsesGeodeticDatum

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class GeographicCrstype(AbstractReferenceSystemType):
    """
    A coordinate reference system based on an ellipsoidal approximation of the
    geoid; this provides an accurate representation of the geometry of
    geographic features for a large portion of the earth's surface.
    """
    class Meta:
        name = "GeographicCRSType"

    uses_ellipsoidal_cs: Optional[UsesEllipsoidalCs] = field(
        default=None,
        metadata={
            "name": "usesEllipsoidalCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        }
    )
    uses_geodetic_datum: Optional[UsesGeodeticDatum] = field(
        default=None,
        metadata={
            "name": "usesGeodeticDatum",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        }
    )
