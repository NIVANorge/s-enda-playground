from dataclasses import dataclass
from bindings.csw_publication.oblique_cartesian_csref_type import ObliqueCartesianCsrefType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class ObliqueCartesianCsref(ObliqueCartesianCsrefType):
    class Meta:
        name = "obliqueCartesianCSRef"
        namespace = "http://www.opengis.net/gml"
