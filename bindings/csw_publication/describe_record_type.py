from dataclasses import dataclass, field
from typing import List
from xml.etree.ElementTree import QName
from bindings.csw_publication.request_base_type import RequestBaseType

__NAMESPACE__ = "http://www.opengis.net/cat/csw/2.0.2"


@dataclass
class DescribeRecordType(RequestBaseType):
    """This request allows a user to discover elements of the information model
    supported by the catalogue. If no TypeName elements are included, then all
    of the schemas for the information model must be returned.

    schemaLanguage - preferred schema language
    (W3C XML Schema by default)
    outputFormat - preferred output format (application/xml by default)
    """
    type_name: List[QName] = field(
        default_factory=list,
        metadata={
            "name": "TypeName",
            "type": "Element",
            "namespace": "http://www.opengis.net/cat/csw/2.0.2",
        }
    )
    output_format: str = field(
        default="application/xml",
        metadata={
            "name": "outputFormat",
            "type": "Attribute",
        }
    )
    schema_language: str = field(
        default="http://www.w3.org/XML/Schema",
        metadata={
            "name": "schemaLanguage",
            "type": "Attribute",
        }
    )
