from dataclasses import dataclass
from bindings.csw_publication.abstract_datum_type import AbstractDatumType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class TemporalDatumBaseType(AbstractDatumType):
    """Partially defines the origin of a temporal coordinate reference system.

    This type restricts the AbstractDatumType to remove the
    "anchorPoint" and "realizationEpoch" elements.
    """
