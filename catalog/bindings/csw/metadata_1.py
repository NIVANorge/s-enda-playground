from dataclasses import dataclass
from bindings.csw.metadata_type import MetadataType

__NAMESPACE__ = "http://www.opengis.net/ows"


@dataclass
class Metadata1(MetadataType):
    class Meta:
        name = "Metadata"
        namespace = "http://www.opengis.net/ows"
