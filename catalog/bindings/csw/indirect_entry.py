from dataclasses import dataclass
from bindings.csw.indirect_entry_type import IndirectEntryType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class IndirectEntry(IndirectEntryType):
    class Meta:
        name = "indirectEntry"
        namespace = "http://www.opengis.net/gml"
