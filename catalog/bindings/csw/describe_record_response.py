from dataclasses import dataclass
from bindings.csw.describe_record_response_type import DescribeRecordResponseType

__NAMESPACE__ = "http://www.opengis.net/cat/csw/2.0.2"


@dataclass
class DescribeRecordResponse(DescribeRecordResponseType):
    class Meta:
        namespace = "http://www.opengis.net/cat/csw/2.0.2"
