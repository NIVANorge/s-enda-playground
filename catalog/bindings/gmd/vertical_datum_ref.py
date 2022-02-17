from dataclasses import dataclass
from bindings.gmd.abstract_crstype import VerticalDatumPropertyType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class VerticalDatumRef(VerticalDatumPropertyType):
    class Meta:
        name = "verticalDatumRef"
        namespace = "http://www.opengis.net/gml"
