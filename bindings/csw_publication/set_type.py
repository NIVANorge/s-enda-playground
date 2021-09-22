from dataclasses import dataclass, field
from decimal import Decimal
from typing import Dict, List, Optional, Union
from bindings.csw_publication.fill_default_type import FillDefaultType
from bindings.csw_publication.fill_timing_attrs_type import FillTimingAttrsType
from bindings.csw_publication.lang_value import LangValue
from bindings.csw_publication.restart_default_type import RestartDefaultType
from bindings.csw_publication.restart_timing_type import RestartTimingType
from bindings.csw_publication.set_prototype import SetPrototype
from bindings.csw_publication.sync_behavior_default_type import SyncBehaviorDefaultType
from bindings.csw_publication.sync_behavior_type import SyncBehaviorType

__NAMESPACE__ = "http://www.w3.org/2001/SMIL20/Language"


@dataclass
class SetType(SetPrototype):
    class Meta:
        name = "setType"

    other_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    class_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    alt: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    longdesc: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    begin: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    end: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    dur: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    repeat_dur: Optional[str] = field(
        default=None,
        metadata={
            "name": "repeatDur",
            "type": "Attribute",
        }
    )
    repeat_count: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "repeatCount",
            "type": "Attribute",
            "min_inclusive": Decimal("0.0"),
        }
    )
    repeat: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    min: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    max: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    sync_behavior: SyncBehaviorType = field(
        default=SyncBehaviorType.DEFAULT,
        metadata={
            "name": "syncBehavior",
            "type": "Attribute",
        }
    )
    sync_tolerance: Optional[str] = field(
        default=None,
        metadata={
            "name": "syncTolerance",
            "type": "Attribute",
        }
    )
    sync_behavior_default: SyncBehaviorDefaultType = field(
        default=SyncBehaviorDefaultType.INHERIT,
        metadata={
            "name": "syncBehaviorDefault",
            "type": "Attribute",
        }
    )
    sync_tolerance_default: str = field(
        default="inherit",
        metadata={
            "name": "syncToleranceDefault",
            "type": "Attribute",
        }
    )
    restart: RestartTimingType = field(
        default=RestartTimingType.DEFAULT,
        metadata={
            "type": "Attribute",
        }
    )
    restart_default: RestartDefaultType = field(
        default=RestartDefaultType.INHERIT,
        metadata={
            "name": "restartDefault",
            "type": "Attribute",
        }
    )
    fill: FillTimingAttrsType = field(
        default=FillTimingAttrsType.DEFAULT,
        metadata={
            "type": "Attribute",
        }
    )
    fill_default: FillDefaultType = field(
        default=FillDefaultType.INHERIT,
        metadata={
            "name": "fillDefault",
            "type": "Attribute",
        }
    )
    target_element: Optional[str] = field(
        default=None,
        metadata={
            "name": "targetElement",
            "type": "Attribute",
        }
    )
    skip_content: bool = field(
        default=True,
        metadata={
            "name": "skip-content",
            "type": "Attribute",
        }
    )
    any_attributes: Dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        }
    )
