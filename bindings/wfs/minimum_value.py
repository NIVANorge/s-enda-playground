from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.opengis.net/ows/1.1"


@dataclass
class MinimumValue:
    """
    Minimum value of this numeric parameter.
    """
    class Meta:
        namespace = "http://www.opengis.net/ows/1.1"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
