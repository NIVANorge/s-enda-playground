from dataclasses import dataclass
from bindings.ows.metadata_type import MetadataType

__NAMESPACE__ = "http://www.opengis.net/ows/2.0"


@dataclass
class AdditionalParametersBaseType(MetadataType):
    pass
