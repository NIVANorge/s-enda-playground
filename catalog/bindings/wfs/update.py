from dataclasses import dataclass
from bindings.wfs.update_type import UpdateType

__NAMESPACE__ = "http://www.opengis.net/wfs/2.0"


@dataclass
class Update(UpdateType):
    class Meta:
        namespace = "http://www.opengis.net/wfs/2.0"
