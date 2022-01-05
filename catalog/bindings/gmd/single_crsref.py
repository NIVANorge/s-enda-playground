from dataclasses import dataclass
from bindings.gmd.abstract_crstype import SingleCrspropertyType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class SingleCrsref(SingleCrspropertyType):
    class Meta:
        name = "singleCRSRef"
        namespace = "http://www.opengis.net/gml"
