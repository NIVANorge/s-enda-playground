from dataclasses import dataclass, field
from typing import List
from xml.etree.ElementTree import QName
from bindings.wfs.base_request_type import BaseRequestType

__NAMESPACE__ = "http://www.opengis.net/wfs/2.0"


@dataclass
class DescribeFeatureTypeType(BaseRequestType):
    type_name: List[QName] = field(
        default_factory=list,
        metadata={
            "name": "TypeName",
            "type": "Element",
            "namespace": "http://www.opengis.net/wfs/2.0",
        }
    )
    output_format: str = field(
        default="application/gml+xml; version=3.2",
        metadata={
            "name": "outputFormat",
            "type": "Attribute",
        }
    )
