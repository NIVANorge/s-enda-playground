from dataclasses import dataclass
from bindings.csw.abstract_meta_data_type import AbstractMetaDataType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class MetaData2(AbstractMetaDataType):
    """
    Abstract element which acts as the head of a substitution group for
    packages of MetaData properties.
    """

    class Meta:
        name = "_MetaData"
        namespace = "http://www.opengis.net/gml"
