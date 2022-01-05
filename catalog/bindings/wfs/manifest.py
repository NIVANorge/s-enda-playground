from dataclasses import dataclass
from bindings.wfs.manifest_type import ManifestType

__NAMESPACE__ = "http://www.opengis.net/ows/1.1"


@dataclass
class Manifest(ManifestType):
    class Meta:
        namespace = "http://www.opengis.net/ows/1.1"
