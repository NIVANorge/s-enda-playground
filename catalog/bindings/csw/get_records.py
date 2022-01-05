from dataclasses import dataclass
from bindings.csw.get_records_type import GetRecordsType

__NAMESPACE__ = "http://www.opengis.net/cat/csw/2.0.2"


@dataclass
class GetRecords(GetRecordsType):
    class Meta:
        namespace = "http://www.opengis.net/cat/csw/2.0.2"
