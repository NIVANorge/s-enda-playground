from dataclasses import dataclass
from bindings.csw_publication.abstract_record_type import AbstractRecordType

__NAMESPACE__ = "http://www.opengis.net/cat/csw/2.0.2"


@dataclass
class AbstractRecord(AbstractRecordType):
    class Meta:
        namespace = "http://www.opengis.net/cat/csw/2.0.2"
