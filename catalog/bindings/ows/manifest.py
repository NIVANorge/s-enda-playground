from dataclasses import dataclass
from bindings.ows.manifest_type import ManifestType

__NAMESPACE__ = "http://www.opengis.net/ows/2.0"


@dataclass
class Manifest(ManifestType):
    class Meta:
        namespace = "http://www.opengis.net/ows/2.0"
