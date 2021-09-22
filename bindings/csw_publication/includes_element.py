from dataclasses import dataclass
from bindings.csw_publication.covariance_element_type import CovarianceElementType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class IncludesElement(CovarianceElementType):
    class Meta:
        name = "includesElement"
        namespace = "http://www.opengis.net/gml"
