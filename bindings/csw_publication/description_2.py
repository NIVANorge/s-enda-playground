from dataclasses import dataclass
from bindings.csw_publication.string_or_ref_type import StringOrRefType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class Description2(StringOrRefType):
    """
    Contains a simple text description of the object, or refers to an external
    description.
    """
    class Meta:
        name = "description"
        namespace = "http://www.opengis.net/gml"
