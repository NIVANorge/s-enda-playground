from dataclasses import dataclass, field
from typing import Optional, Union
from bindings.gmd.abstract_md_spatial_representation import (
    AbstractMdSpatialRepresentation,
)
from bindings.gmd.actuate_value import ActuateValue
from bindings.gmd.md_georectified import MdGeorectified
from bindings.gmd.md_georeferenceable import MdGeoreferenceable
from bindings.gmd.md_grid_spatial_representation import MdGridSpatialRepresentation
from bindings.gmd.md_vector_spatial_representation import MdVectorSpatialRepresentation
from bindings.gmd.nil_reason_enumeration_value import NilReasonEnumerationValue
from bindings.gmd.show_value import ShowValue

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdSpatialRepresentationPropertyType:
    class Meta:
        name = "MD_SpatialRepresentation_PropertyType"

    md_vector_spatial_representation: Optional[MdVectorSpatialRepresentation] = field(
        default=None,
        metadata={
            "name": "MD_VectorSpatialRepresentation",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    md_georectified: Optional[MdGeorectified] = field(
        default=None,
        metadata={
            "name": "MD_Georectified",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    md_georeferenceable: Optional[MdGeoreferenceable] = field(
        default=None,
        metadata={
            "name": "MD_Georeferenceable",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    md_grid_spatial_representation: Optional[MdGridSpatialRepresentation] = field(
        default=None,
        metadata={
            "name": "MD_GridSpatialRepresentation",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    abstract_md_spatial_representation: Optional[
        AbstractMdSpatialRepresentation
    ] = field(
        default=None,
        metadata={
            "name": "AbstractMD_SpatialRepresentation",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    type: str = field(
        init=False,
        default="simple",
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    href: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    role: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    arcrole: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    show: Optional[ShowValue] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    actuate: Optional[ActuateValue] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    uuidref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    nil_reason: Optional[Union[str, NilReasonEnumerationValue]] = field(
        default=None,
        metadata={
            "name": "nilReason",
            "type": "Attribute",
            "namespace": "http://www.isotc211.org/2005/gco",
            "pattern": r"other:\w{2,}",
        },
    )
