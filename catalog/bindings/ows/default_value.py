from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.opengis.net/ows/2.0"


@dataclass
class DefaultValue:
    """
    The default value for a quantity for which multiple values are allowed.
    """

    class Meta:
        namespace = "http://www.opengis.net/ows/2.0"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
