from dataclasses import dataclass, field
from typing import List, Optional
from generated.xlink import (
    ActuateType,
    ShowType,
    TypeType,
)

__NAMESPACE__ = "http://www.opengis.net/ows"


@dataclass
class Abstract:
    """
    Brief narrative description of this resource, normally used for display to
    a human.
    """
    class Meta:
        namespace = "http://www.opengis.net/ows"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )


@dataclass
class AddressType:
    """
    Location of the responsible individual or organization.

    :ivar delivery_point: Address line for the location.
    :ivar city: City of the location.
    :ivar administrative_area: State or province of the location.
    :ivar postal_code: ZIP or other postal code.
    :ivar country: Country of the physical address.
    :ivar electronic_mail_address: Address of the electronic mailbox of
        the responsible organization or individual.
    """
    delivery_point: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DeliveryPoint",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows",
        }
    )
    city: Optional[str] = field(
        default=None,
        metadata={
            "name": "City",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows",
        }
    )
    administrative_area: Optional[str] = field(
        default=None,
        metadata={
            "name": "AdministrativeArea",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows",
        }
    )
    postal_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "PostalCode",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows",
        }
    )
    country: Optional[str] = field(
        default=None,
        metadata={
            "name": "Country",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows",
        }
    )
    electronic_mail_address: List[str] = field(
        default_factory=list,
        metadata={
            "name": "ElectronicMailAddress",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows",
        }
    )


@dataclass
class CodeType:
    """Name or code with an (optional) authority.

    If the codeSpace attribute is present, its value should reference a
    dictionary, thesaurus, or authority for the name or code, such as
    the organisation who assigned the value, or the dictionary from
    which it is taken. Type copied from basicTypes.xsd of GML 3 with
    documentation edited, for possible use outside the
    ServiceIdentification section of a service metadata document.
    """
    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
    code_space: Optional[str] = field(
        default=None,
        metadata={
            "name": "codeSpace",
            "type": "Attribute",
        }
    )


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


@dataclass
class TelephoneType:
    """
    Telephone numbers for contacting the responsible individual or
    organization.

    :ivar voice: Telephone number by which individuals can speak to the
        responsible organization or individual.
    :ivar facsimile: Telephone number of a facsimile machine for the
        responsible organization or individual.
    """
    voice: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Voice",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows",
        }
    )
    facsimile: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Facsimile",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows",
        }
    )


@dataclass
class Title:
    """
    Title of this resource, normally used for display to a human.
    """
    class Meta:
        namespace = "http://www.opengis.net/ows"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )


@dataclass
class KeywordsType:
    """Unordered list of one or more commonly used or formalised word(s) or
    phrase(s) used to describe the subject.

    When needed, the optional "type" can name the type of the associated
    list of keywords that shall all have the same type. Also when
    needed, the codeSpace attribute of that "type" can reference the
    type name authority and/or thesaurus. For OWS use, the optional
    thesaurusName element was omitted as being complex information that
    could be referenced by the codeSpace attribute of the Type element.
    """
    keyword: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Keyword",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows",
            "min_occurs": 1,
        }
    )
    type: Optional[CodeType] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows",
        }
    )


@dataclass
class OnlineResourceType:
    """Reference to on-line resource from which data can be obtained.

    For OWS use in the service metadata document, the CI_OnlineResource
    class was XML encoded as the attributeGroup "xlink:simpleAttrs", as
    used in GML.
    """
    type: TypeType = field(
        init=False,
        default=TypeType.SIMPLE,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    href: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    role: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        }
    )
    arcrole: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    show: Optional[ShowType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    actuate: Optional[ActuateType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )


@dataclass
class Role(CodeType):
    """Function performed by the responsible party.

    Possible values of this Role shall include the values and the
    meanings listed in Subclause B.5.5 of ISO 19115:2003.
    """
    class Meta:
        namespace = "http://www.opengis.net/ows"


@dataclass
class ContactType:
    """Information required to enable contact with the responsible person
    and/or organization.

    For OWS use in the service metadata document, the optional
    hoursOfService and contactInstructions elements were retained, as
    possibly being useful in the ServiceProvider section.

    :ivar phone: Telephone numbers at which the organization or
        individual may be contacted.
    :ivar address: Physical and email address at which the organization
        or individual may be contacted.
    :ivar online_resource: On-line information that can be used to
        contact the individual or organization. OWS specifics: The
        xlink:href attribute in the xlink:simpleAttrs attribute group
        shall be used to reference this resource. Whenever practical,
        the xlink:href attribute with type anyURI should be a URL from
        which more contact information can be electronically retrieved.
        The xlink:title attribute with type "string" can be used to name
        this set of information. The other attributes in the
        xlink:simpleAttrs attribute group should not be used.
    :ivar hours_of_service: Time period (including time zone) when
        individuals can contact the organization or individual.
    :ivar contact_instructions: Supplemental instructions on how or when
        to contact the individual or organization.
    """
    phone: Optional[TelephoneType] = field(
        default=None,
        metadata={
            "name": "Phone",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows",
        }
    )
    address: Optional[AddressType] = field(
        default=None,
        metadata={
            "name": "Address",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows",
        }
    )
    online_resource: Optional[OnlineResourceType] = field(
        default=None,
        metadata={
            "name": "OnlineResource",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows",
        }
    )
    hours_of_service: Optional[str] = field(
        default=None,
        metadata={
            "name": "HoursOfService",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows",
        }
    )
    contact_instructions: Optional[str] = field(
        default=None,
        metadata={
            "name": "ContactInstructions",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows",
        }
    )


@dataclass
class Keywords(KeywordsType):
    class Meta:
        namespace = "http://www.opengis.net/ows"


@dataclass
class ContactInfo(ContactType):
    """
    Address of the responsible party.
    """
    class Meta:
        namespace = "http://www.opengis.net/ows"


@dataclass
class ResponsiblePartySubsetType:
    """Identification of, and means of communication with, person responsible
    for the server.

    For OWS use in the ServiceProvider section of a service metadata
    document, the optional organizationName element was removed, since
    this type is always used with the ProviderName element which
    provides that information. The mandatory "role" element was changed
    to optional, since no clear use of this information is known in the
    ServiceProvider section.
    """
    individual_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "IndividualName",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows",
        }
    )
    position_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "PositionName",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows",
        }
    )
    contact_info: Optional[ContactInfo] = field(
        default=None,
        metadata={
            "name": "ContactInfo",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows",
        }
    )
    role: Optional[Role] = field(
        default=None,
        metadata={
            "name": "Role",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows",
        }
    )


@dataclass
class ResponsiblePartyType:
    """Identification of, and means of communication with, person responsible
    for the server.

    At least one of IndividualName, OrganisationName, or PositionName
    shall be included.
    """
    individual_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "IndividualName",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows",
        }
    )
    organisation_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "OrganisationName",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows",
        }
    )
    position_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "PositionName",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows",
        }
    )
    contact_info: Optional[ContactInfo] = field(
        default=None,
        metadata={
            "name": "ContactInfo",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows",
        }
    )
    role: Optional[Role] = field(
        default=None,
        metadata={
            "name": "Role",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows",
            "required": True,
        }
    )


@dataclass
class PointOfContact(ResponsiblePartyType):
    """Identification of, and means of communication with, person(s)
    responsible for the resource(s).

    For OWS use in the ServiceProvider section of a service metadata
    document, the optional organizationName element was removed, since
    this type is always used with the ProviderName element which
    provides that information. The optional individualName element was
    made mandatory, since either the organizationName or individualName
    element is mandatory. The mandatory "role" element was changed to
    optional, since no clear use of this information is known in the
    ServiceProvider section.
    """
    class Meta:
        namespace = "http://www.opengis.net/ows"
