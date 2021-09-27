from dataclasses import dataclass
from bindings.gmd.abstract_meta_data_type import AbstractMetaDataType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class AbstractMetaData(AbstractMetaDataType):
    class Meta:
        namespace = "http://www.opengis.net/gml"
