from dataclasses import dataclass
from bindings.csw.meta_data_property_type import MetaDataPropertyType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class MetaDataProperty(MetaDataPropertyType):
    """
    Contains or refers to a metadata package that contains metadata properties.
    """

    class Meta:
        name = "metaDataProperty"
        namespace = "http://www.opengis.net/gml"
