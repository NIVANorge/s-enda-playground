from dataclasses import dataclass
from bindings.csw.dcmirecord_type import DcmirecordType

__NAMESPACE__ = "http://www.opengis.net/cat/csw/2.0.2"


@dataclass
class Dcmirecord(DcmirecordType):
    class Meta:
        name = "DCMIRecord"
        namespace = "http://www.opengis.net/cat/csw/2.0.2"
