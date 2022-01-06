from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.opengis.net/ows"


@dataclass
class Abstract1:
    """
    Brief narrative description of this resource, normally used for display to
    a human.
    """

    class Meta:
        name = "Abstract"
        namespace = "http://www.opengis.net/ows"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
