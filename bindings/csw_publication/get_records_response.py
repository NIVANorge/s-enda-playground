from dataclasses import dataclass
from bindings.csw_publication.get_records_response_type import GetRecordsResponseType

__NAMESPACE__ = "http://www.opengis.net/cat/csw/2.0.2"


@dataclass
class GetRecordsResponse(GetRecordsResponseType):
    class Meta:
        namespace = "http://www.opengis.net/cat/csw/2.0.2"
