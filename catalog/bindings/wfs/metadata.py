from dataclasses import dataclass
from bindings.wfs.metadata_type import MetadataType

__NAMESPACE__ = "http://www.opengis.net/ows/1.1"


@dataclass
class Metadata(MetadataType):
    class Meta:
        namespace = "http://www.opengis.net/ows/1.1"
