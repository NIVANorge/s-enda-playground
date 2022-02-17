from dataclasses import dataclass
from bindings.csw.topo_complex_member_type import TopoComplexMemberType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class TopoComplexProperty(TopoComplexMemberType):
    class Meta:
        name = "topoComplexProperty"
        namespace = "http://www.opengis.net/gml"
