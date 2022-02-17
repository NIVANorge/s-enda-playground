from dataclasses import dataclass
from bindings.csw.temporal_datum_ref_type import TemporalDatumRefType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class TemporalDatumRef(TemporalDatumRefType):
    class Meta:
        name = "temporalDatumRef"
        namespace = "http://www.opengis.net/gml"
