from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.opengis.net/ows"


@dataclass
class OrganisationName:
    """
    Name of the responsible organization.
    """
    class Meta:
        namespace = "http://www.opengis.net/ows"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
