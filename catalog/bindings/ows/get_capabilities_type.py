from dataclasses import dataclass, field
from typing import List, Optional
from bindings.ows.accept_formats_type import AcceptFormatsType
from bindings.ows.accept_versions_type import AcceptVersionsType
from bindings.ows.sections_type import SectionsType

__NAMESPACE__ = "http://www.opengis.net/ows/2.0"


@dataclass
class GetCapabilitiesType:
    """XML encoded GetCapabilities operation request.

    This operation allows clients to retrieve service metadata about a
    specific service instance. In this XML encoding, no "request"
    parameter is included, since the element name specifies the specific
    operation. This base type shall be extended by each specific OWS to
    include the additional required "service" attribute, with the
    correct value for that OWS.

    :ivar accept_versions: When omitted, server shall return latest
        supported version.
    :ivar sections: When omitted or not supported by server, server
        shall return complete service metadata (Capabilities) document.
    :ivar accept_formats: When omitted or not supported by server,
        server shall return service metadata document using the MIME
        type "text/xml".
    :ivar accept_languages: Ordered list of languages desired by the
        client for all human readable text in the response, in order of
        preference. For every element, the first matching language
        available from the server shall be present in the response.
    :ivar update_sequence: When omitted or not supported by server,
        server shall return latest complete service metadata document.
    """
    accept_versions: Optional[AcceptVersionsType] = field(
        default=None,
        metadata={
            "name": "AcceptVersions",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows/2.0",
        }
    )
    sections: Optional[SectionsType] = field(
        default=None,
        metadata={
            "name": "Sections",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows/2.0",
        }
    )
    accept_formats: Optional[AcceptFormatsType] = field(
        default=None,
        metadata={
            "name": "AcceptFormats",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows/2.0",
        }
    )
    accept_languages: Optional["GetCapabilitiesType.AcceptLanguages"] = field(
        default=None,
        metadata={
            "name": "AcceptLanguages",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows/2.0",
        }
    )
    update_sequence: Optional[str] = field(
        default=None,
        metadata={
            "name": "updateSequence",
            "type": "Attribute",
        }
    )

    @dataclass
    class AcceptLanguages:
        language: List[str] = field(
            default_factory=list,
            metadata={
                "name": "Language",
                "type": "Element",
                "namespace": "http://www.opengis.net/ows/2.0",
                "min_occurs": 1,
            }
        )
