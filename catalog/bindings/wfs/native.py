from dataclasses import dataclass
from bindings.wfs.native_type import NativeType

__NAMESPACE__ = "http://www.opengis.net/wfs/2.0"


@dataclass
class Native(NativeType):
    class Meta:
        namespace = "http://www.opengis.net/wfs/2.0"
