from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.opengis.net/ows"


@dataclass
class IndividualName:
    """
    Name of the responsible person: surname, given name, title separated by a
    delimiter.
    """
    class Meta:
        namespace = "http://www.opengis.net/ows"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
