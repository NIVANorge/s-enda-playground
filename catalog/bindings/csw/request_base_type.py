from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.opengis.net/cat/csw/2.0.2"


@dataclass
class RequestBaseType:
    """Base type for all request messages except GetCapabilities.

    The attributes identify the relevant service type and version.
    """
    service: str = field(
        init=False,
        default="CSW",
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    version: str = field(
        init=False,
        default="2.0.2",
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
