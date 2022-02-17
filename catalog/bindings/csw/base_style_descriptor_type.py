from dataclasses import dataclass, field
from typing import List, Optional
from bindings.csw.abstract_gmltype import AbstractGmltype
from bindings.csw.animate_2 import Animate2
from bindings.csw.animate_color_2 import AnimateColor2
from bindings.csw.animate_motion_2 import AnimateMotion2
from bindings.csw.scale_type import ScaleType
from bindings.csw.set_2 import Set2
from bindings.csw.style_variation_type import StyleVariationType

__NAMESPACE__ = "http://www.opengis.net/gml"


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
        },
    )
    style_variation: List[StyleVariationType] = field(
        default_factory=list,
        metadata={
            "name": "styleVariation",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    animate: List[Animate2] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2001/SMIL20/",
        },
    )
    animate_motion: List[AnimateMotion2] = field(
        default_factory=list,
        metadata={
            "name": "animateMotion",
            "type": "Element",
            "namespace": "http://www.w3.org/2001/SMIL20/",
        },
    )
    animate_color: List[AnimateColor2] = field(
        default_factory=list,
        metadata={
            "name": "animateColor",
            "type": "Element",
            "namespace": "http://www.w3.org/2001/SMIL20/",
        },
    )
    set: List[Set2] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2001/SMIL20/",
        },
    )
