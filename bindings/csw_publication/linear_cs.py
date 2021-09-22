from dataclasses import dataclass
from bindings.csw_publication.linear_cstype import LinearCstype

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class LinearCs(LinearCstype):
    class Meta:
        name = "LinearCS"
        namespace = "http://www.opengis.net/gml"
