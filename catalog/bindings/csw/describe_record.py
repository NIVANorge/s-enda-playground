from dataclasses import dataclass
from bindings.csw.describe_record_type import DescribeRecordType

__NAMESPACE__ = "http://www.opengis.net/cat/csw/2.0.2"


@dataclass
class DescribeRecord(DescribeRecordType):
    class Meta:
        namespace = "http://www.opengis.net/cat/csw/2.0.2"
