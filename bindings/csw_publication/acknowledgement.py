from dataclasses import dataclass
from bindings.csw_publication.acknowledgement_type import AcknowledgementType

__NAMESPACE__ = "http://www.opengis.net/cat/csw/2.0.2"


@dataclass
class Acknowledgement(AcknowledgementType):
    class Meta:
        namespace = "http://www.opengis.net/cat/csw/2.0.2"
