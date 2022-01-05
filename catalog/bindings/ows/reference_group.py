from dataclasses import dataclass
from bindings.ows.reference_group_type import ReferenceGroupType

__NAMESPACE__ = "http://www.opengis.net/ows/2.0"


@dataclass
class ReferenceGroup(ReferenceGroupType):
    class Meta:
        namespace = "http://www.opengis.net/ows/2.0"
