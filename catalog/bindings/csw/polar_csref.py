from dataclasses import dataclass
from bindings.csw.polar_csref_type import PolarCsrefType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class PolarCsref(PolarCsrefType):
    class Meta:
        name = "polarCSRef"
        namespace = "http://www.opengis.net/gml"
