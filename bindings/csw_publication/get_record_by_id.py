from dataclasses import dataclass
from bindings.csw_publication.get_record_by_id_type import GetRecordByIdType

__NAMESPACE__ = "http://www.opengis.net/cat/csw/2.0.2"


@dataclass
class GetRecordById(GetRecordByIdType):
    class Meta:
        namespace = "http://www.opengis.net/cat/csw/2.0.2"
