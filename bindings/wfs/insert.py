from dataclasses import dataclass
from bindings.wfs.insert_type import InsertType

__NAMESPACE__ = "http://www.opengis.net/wfs/2.0"


@dataclass
class Insert(InsertType):
    class Meta:
        namespace = "http://www.opengis.net/wfs/2.0"
