from dataclasses import dataclass
from bindings.gmd.cartesian_csproperty_type import CartesianCspropertyType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class CartesianCsref(CartesianCspropertyType):
    class Meta:
        name = "cartesianCSRef"
        namespace = "http://www.opengis.net/gml"
