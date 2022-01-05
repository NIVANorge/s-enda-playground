from dataclasses import dataclass
from bindings.csw.topo_primitive_member_type import TopoPrimitiveMemberType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class TopoPrimitiveMember(TopoPrimitiveMemberType):
    class Meta:
        name = "topoPrimitiveMember"
        namespace = "http://www.opengis.net/gml"
