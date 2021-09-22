from dataclasses import dataclass
from bindings.csw_publication.oblique_cartesian_cstype import ObliqueCartesianCstype

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class ObliqueCartesianCs(ObliqueCartesianCstype):
    class Meta:
        name = "ObliqueCartesianCS"
        namespace = "http://www.opengis.net/gml"
