from dataclasses import dataclass
from bindings.csw.cartesian_cstype import CartesianCstype

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class CartesianCs(CartesianCstype):
    class Meta:
        name = "CartesianCS"
        namespace = "http://www.opengis.net/gml"
