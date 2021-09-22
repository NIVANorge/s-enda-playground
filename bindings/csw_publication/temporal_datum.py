from dataclasses import dataclass
from bindings.csw_publication.temporal_datum_type import TemporalDatumType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class TemporalDatum(TemporalDatumType):
    class Meta:
        namespace = "http://www.opengis.net/gml"
