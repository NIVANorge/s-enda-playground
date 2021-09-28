from dataclasses import dataclass
from bindings.wfs.delete_type import DeleteType

__NAMESPACE__ = "http://www.opengis.net/wfs/2.0"


@dataclass
class Delete(DeleteType):
    class Meta:
        namespace = "http://www.opengis.net/wfs/2.0"
