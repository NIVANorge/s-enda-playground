from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.opengis.net/ows/2.0"


@dataclass
class Spacing:
    """
    The regular distance or spacing between the allowed values in a range.
    """

    class Meta:
        namespace = "http://www.opengis.net/ows/2.0"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
