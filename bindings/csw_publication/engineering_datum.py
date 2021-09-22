from dataclasses import dataclass
from bindings.csw_publication.engineering_datum_type import EngineeringDatumType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class EngineeringDatum(EngineeringDatumType):
    class Meta:
        namespace = "http://www.opengis.net/gml"
