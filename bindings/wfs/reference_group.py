from dataclasses import dataclass
from bindings.wfs.reference_group_type import ReferenceGroupType

__NAMESPACE__ = "http://www.opengis.net/ows/1.1"


@dataclass
class ReferenceGroup(ReferenceGroupType):
    class Meta:
        namespace = "http://www.opengis.net/ows/1.1"
