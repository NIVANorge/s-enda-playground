from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.opengis.net/ows"


@dataclass
class Title1:
    """
    Title of this resource, normally used for display to a human.
    """

    class Meta:
        name = "Title"
        namespace = "http://www.opengis.net/ows"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
