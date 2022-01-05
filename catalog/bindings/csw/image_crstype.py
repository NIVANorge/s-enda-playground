from dataclasses import dataclass, field
from typing import Optional
from bindings.csw.abstract_reference_system_type import AbstractReferenceSystemType
from bindings.csw.uses_cartesian_cs import UsesCartesianCs
from bindings.csw.uses_image_datum import UsesImageDatum
from bindings.csw.uses_oblique_cartesian_cs import UsesObliqueCartesianCs

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class ImageCrstype(AbstractReferenceSystemType):
    """An engineering coordinate reference system applied to locations in
    images.

    Image coordinate reference systems are treated as a separate sub-
    type because a separate user community exists for images with its
    own terms of reference.
    """
    class Meta:
        name = "ImageCRSType"

    uses_cartesian_cs: Optional[UsesCartesianCs] = field(
        default=None,
        metadata={
            "name": "usesCartesianCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    uses_oblique_cartesian_cs: Optional[UsesObliqueCartesianCs] = field(
        default=None,
        metadata={
            "name": "usesObliqueCartesianCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    uses_image_datum: Optional[UsesImageDatum] = field(
        default=None,
        metadata={
            "name": "usesImageDatum",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        }
    )
