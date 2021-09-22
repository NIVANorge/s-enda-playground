from dataclasses import dataclass
from bindings.csw_publication.record_type import RecordType

__NAMESPACE__ = "http://www.opengis.net/cat/csw/2.0.2"


@dataclass
class Record(RecordType):
    class Meta:
        namespace = "http://www.opengis.net/cat/csw/2.0.2"
