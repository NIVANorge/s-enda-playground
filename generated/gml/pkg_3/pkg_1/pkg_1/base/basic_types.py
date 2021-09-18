from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional, Union

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class CodeListType:
    """List of values on a uniform nominal scale.

    List of text tokens. In a list context a token should not include
    any spaces, so xsd:Name is used instead of xsd:string. If a
    codeSpace attribute is present, then its value is a reference to a
    Reference System for the value, a dictionary or code list.
    """
    value: List[str] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        }
    )
    code_space: Optional[str] = field(
        default=None,
        metadata={
            "name": "codeSpace",
            "type": "Attribute",
        }
    )


@dataclass
class CodeType:
    """Name or code with an (optional) authority.

    Text token. If the codeSpace attribute is present, then its value
    should identify a dictionary, thesaurus or authority for the term,
    such as the organisation who assigned the value, or the dictionary
    from which it is taken. A text string with an optional codeSpace
    attribute.
    """
    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
    code_space: Optional[str] = field(
        default=None,
        metadata={
            "name": "codeSpace",
            "type": "Attribute",
        }
    )


@dataclass
class CoordinatesType:
    """Tables or arrays of tuples.

    May be used for text-encoding of values from a table. Actually just
    a string, but allows the user to indicate which characters are used
    as separators. The value of the 'cs' attribute is the separator for
    coordinate values, and the value of the 'ts' attribute gives the
    tuple separator (a single space by default); the default values may
    be changed to reflect local usage. Defaults to CSV within a tuple,
    space between tuples. However, any string content will be schema-
    valid.
    """
    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
    decimal: str = field(
        default=".",
        metadata={
            "type": "Attribute",
        }
    )
    cs: str = field(
        default=",",
        metadata={
            "type": "Attribute",
        }
    )
    ts: str = field(
        default=" ",
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class MeasureListType:
    """List of numbers with a uniform scale.

    The value of uom (Units Of Measure) attribute is a reference to a
    Reference System for the amount, either a ratio or position scale.
    """
    value: List[float] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        }
    )
    uom: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class MeasureType:
    """Number with a scale.

    The value of uom (Units Of Measure) attribute is a reference to a
    Reference System for the amount, either a ratio or position scale.
    """
    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uom: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


class NullEnumerationValue(Enum):
    INAPPLICABLE = "inapplicable"
    MISSING = "missing"
    TEMPLATE = "template"
    UNKNOWN = "unknown"
    WITHHELD = "withheld"


class SignType(Enum):
    """Utility type used in various places.

    - e.g. to indicate the direction of topological objects;
    "+" for forwards, or "-" for backwards.
    """
    VALUE = "-"
    VALUE_1 = "+"


@dataclass
class CodeOrNullListType:
    """List of values on a uniform nominal scale.

    List of text tokens. In a list context a token should not include
    any spaces, so xsd:Name is used instead of xsd:string. A member of
    the list may be a typed null. If a codeSpace attribute is present,
    then its value is a reference to a Reference System for the value, a
    dictionary or code list.
    """
    value: List[Union[str, NullEnumerationValue]] = field(
        default_factory=list,
        metadata={
            "pattern": r"other:\w{2,}",
            "tokens": True,
        }
    )
    code_space: Optional[str] = field(
        default=None,
        metadata={
            "name": "codeSpace",
            "type": "Attribute",
        }
    )


@dataclass
class MeasureOrNullListType:
    """List of numbers with a uniform scale.

    A member of the list may be a typed null. The value of uom (Units Of
    Measure) attribute is a reference to a Reference System for the
    amount, either a ratio or position scale.
    """
    value: List[Union[str, NullEnumerationValue]] = field(
        default_factory=list,
        metadata={
            "pattern": r"other:\w{2,}",
            "tokens": True,
        }
    )
    uom: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class Null:
    class Meta:
        namespace = "http://www.opengis.net/gml"

    value: Union[str, NullEnumerationValue] = field(
        default="",
        metadata={
            "pattern": r"other:\w{2,}",
        }
    )
