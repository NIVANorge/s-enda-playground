from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.opengis.net/ows/2.0"


@dataclass
class IndividualName:
    """
    Name of the responsible person: surname, given name, title separated by a
    delimiter.
    """
    class Meta:
        namespace = "http://www.opengis.net/ows/2.0"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
