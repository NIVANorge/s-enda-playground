from dataclasses import dataclass
from bindings.csw_publication.topo_volume_type import TopoVolumeType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class TopoVolume(TopoVolumeType):
    class Meta:
        namespace = "http://www.opengis.net/gml"
