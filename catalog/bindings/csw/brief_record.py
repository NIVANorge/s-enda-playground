from dataclasses import dataclass
from bindings.csw.brief_record_type import BriefRecordType

__NAMESPACE__ = "http://www.opengis.net/cat/csw/2.0.2"


@dataclass
class BriefRecord(BriefRecordType):
    class Meta:
        namespace = "http://www.opengis.net/cat/csw/2.0.2"
