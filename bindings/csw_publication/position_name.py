from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.opengis.net/ows"


@dataclass
class PositionName:
    """
    Role or position of the responsible person.
    """
    class Meta:
        namespace = "http://www.opengis.net/ows"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
