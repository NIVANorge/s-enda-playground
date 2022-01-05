from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.opengis.net/ows/2.0"


@dataclass
class OrganisationName:
    """
    Name of the responsible organization.
    """
    class Meta:
        namespace = "http://www.opengis.net/ows/2.0"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
