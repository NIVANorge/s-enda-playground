from dataclasses import dataclass
from bindings.wfs.extension_ops_type import ExtensionOpsType

__NAMESPACE__ = "http://www.opengis.net/fes/2.0"


@dataclass
class ExtensionOps(ExtensionOpsType):
    class Meta:
        name = "extensionOps"
        namespace = "http://www.opengis.net/fes/2.0"
