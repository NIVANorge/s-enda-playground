from dataclasses import dataclass
from bindings.csw_publication.abstract_meta_data_type import AbstractMetaDataType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class GenericMetaDataType(AbstractMetaDataType):
    """
    Deprecated with GML version 3.1.0.
    """
