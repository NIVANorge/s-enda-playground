from dataclasses import dataclass
from bindings.csw.envelope_type import EnvelopeType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class Envelope(EnvelopeType):
    class Meta:
        namespace = "http://www.opengis.net/gml"
