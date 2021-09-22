from dataclasses import dataclass
from bindings.csw_publication.relative_internal_positional_accuracy_type import RelativeInternalPositionalAccuracyType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class RelativeInternalPositionalAccuracy(RelativeInternalPositionalAccuracyType):
    class Meta:
        name = "relativeInternalPositionalAccuracy"
        namespace = "http://www.opengis.net/gml"
