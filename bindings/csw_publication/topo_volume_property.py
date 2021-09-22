from dataclasses import dataclass
from bindings.csw_publication.topo_volume_property_type import TopoVolumePropertyType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class TopoVolumeProperty(TopoVolumePropertyType):
    class Meta:
        name = "topoVolumeProperty"
        namespace = "http://www.opengis.net/gml"
