from dataclasses import dataclass
from bindings.gmd.polar_csproperty_type import PolarCspropertyType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class PolarCsref(PolarCspropertyType):
    class Meta:
        name = "polarCSRef"
        namespace = "http://www.opengis.net/gml"
