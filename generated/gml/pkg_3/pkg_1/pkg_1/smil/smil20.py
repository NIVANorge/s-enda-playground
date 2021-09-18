from dataclasses import dataclass, field
from enum import Enum
from typing import Optional
from generated.gml.pkg_3.pkg_1.pkg_1.smil.smil20_language import (
    AnimateColorType,
    AnimateMotionType,
    AnimateType,
    SetType,
)

__NAMESPACE__ = "http://www.w3.org/2001/SMIL20/"


class AnimAddAccumAttrsAccumulate(Enum):
    NONE = "none"
    SUM = "sum"


class AnimAddAccumAttrsAdditive(Enum):
    REPLACE = "replace"
    SUM = "sum"


class AnimModeAttrsCalcMode(Enum):
    DISCRETE = "discrete"
    LINEAR = "linear"
    PACED = "paced"


class AnimNamedTargetAttrsAttributeType(Enum):
    XML = "XML"
    CSS = "CSS"
    AUTO = "auto"


class FillDefaultType(Enum):
    REMOVE = "remove"
    FREEZE = "freeze"
    HOLD = "hold"
    AUTO = "auto"
    INHERIT = "inherit"
    TRANSITION = "transition"


class FillTimingAttrsType(Enum):
    REMOVE = "remove"
    FREEZE = "freeze"
    HOLD = "hold"
    AUTO = "auto"
    DEFAULT = "default"
    TRANSITION = "transition"


class RestartDefaultType(Enum):
    NEVER = "never"
    ALWAYS = "always"
    WHEN_NOT_ACTIVE = "whenNotActive"
    INHERIT = "inherit"


class RestartTimingType(Enum):
    NEVER = "never"
    ALWAYS = "always"
    WHEN_NOT_ACTIVE = "whenNotActive"
    DEFAULT = "default"


class SyncBehaviorDefaultType(Enum):
    CAN_SLIP = "canSlip"
    LOCKED = "locked"
    INDEPENDENT = "independent"
    INHERIT = "inherit"


class SyncBehaviorType(Enum):
    CAN_SLIP = "canSlip"
    LOCKED = "locked"
    INDEPENDENT = "independent"
    DEFAULT = "default"


@dataclass
class Animate(AnimateType):
    class Meta:
        name = "animate"
        namespace = "http://www.w3.org/2001/SMIL20/"


@dataclass
class AnimateColor(AnimateColorType):
    class Meta:
        name = "animateColor"
        namespace = "http://www.w3.org/2001/SMIL20/"


@dataclass
class AnimateColorPrototype:
    class Meta:
        name = "animateColorPrototype"

    attribute_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "attributeName",
            "type": "Attribute",
            "required": True,
        }
    )
    attribute_type: AnimNamedTargetAttrsAttributeType = field(
        default=AnimNamedTargetAttrsAttributeType.AUTO,
        metadata={
            "name": "attributeType",
            "type": "Attribute",
        }
    )
    additive: AnimAddAccumAttrsAdditive = field(
        default=AnimAddAccumAttrsAdditive.REPLACE,
        metadata={
            "type": "Attribute",
        }
    )
    accumulate: AnimAddAccumAttrsAccumulate = field(
        default=AnimAddAccumAttrsAccumulate.NONE,
        metadata={
            "type": "Attribute",
        }
    )
    to: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    from_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "from",
            "type": "Attribute",
        }
    )
    by: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    values: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class AnimateMotion(AnimateMotionType):
    class Meta:
        name = "animateMotion"
        namespace = "http://www.w3.org/2001/SMIL20/"


@dataclass
class AnimateMotionPrototype:
    class Meta:
        name = "animateMotionPrototype"

    additive: AnimAddAccumAttrsAdditive = field(
        default=AnimAddAccumAttrsAdditive.REPLACE,
        metadata={
            "type": "Attribute",
        }
    )
    accumulate: AnimAddAccumAttrsAccumulate = field(
        default=AnimAddAccumAttrsAccumulate.NONE,
        metadata={
            "type": "Attribute",
        }
    )
    to: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    from_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "from",
            "type": "Attribute",
        }
    )
    by: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    values: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    origin: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class AnimatePrototype:
    class Meta:
        name = "animatePrototype"

    attribute_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "attributeName",
            "type": "Attribute",
            "required": True,
        }
    )
    attribute_type: AnimNamedTargetAttrsAttributeType = field(
        default=AnimNamedTargetAttrsAttributeType.AUTO,
        metadata={
            "name": "attributeType",
            "type": "Attribute",
        }
    )
    additive: AnimAddAccumAttrsAdditive = field(
        default=AnimAddAccumAttrsAdditive.REPLACE,
        metadata={
            "type": "Attribute",
        }
    )
    accumulate: AnimAddAccumAttrsAccumulate = field(
        default=AnimAddAccumAttrsAccumulate.NONE,
        metadata={
            "type": "Attribute",
        }
    )
    to: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    from_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "from",
            "type": "Attribute",
        }
    )
    by: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    values: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class Set(SetType):
    class Meta:
        name = "set"
        namespace = "http://www.w3.org/2001/SMIL20/"


@dataclass
class SetPrototype:
    class Meta:
        name = "setPrototype"

    attribute_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "attributeName",
            "type": "Attribute",
            "required": True,
        }
    )
    attribute_type: AnimNamedTargetAttrsAttributeType = field(
        default=AnimNamedTargetAttrsAttributeType.AUTO,
        metadata={
            "name": "attributeType",
            "type": "Attribute",
        }
    )
    to: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
