from dataclasses import dataclass
from bindings.csw.summary_record_type import SummaryRecordType

__NAMESPACE__ = "http://www.opengis.net/cat/csw/2.0.2"


@dataclass
class SummaryRecord(SummaryRecordType):
    class Meta:
        namespace = "http://www.opengis.net/cat/csw/2.0.2"
