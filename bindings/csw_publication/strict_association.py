from dataclasses import dataclass
from bindings.csw_publication.feature_array_property_type import AssociationType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class StrictAssociation(AssociationType):
    """
    must carry a reference to an object or contain an object but not both.
    """
    class Meta:
        name = "_strictAssociation"
        namespace = "http://www.opengis.net/gml"
