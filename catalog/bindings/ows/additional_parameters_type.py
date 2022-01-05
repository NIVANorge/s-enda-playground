from dataclasses import dataclass
from bindings.ows.additional_parameters_base_type import AdditionalParametersBaseType

__NAMESPACE__ = "http://www.opengis.net/ows/2.0"


@dataclass
class AdditionalParametersType(AdditionalParametersBaseType):
    pass
