from dataclasses import dataclass
from bindings.ows.additional_parameters_type import AdditionalParametersType

__NAMESPACE__ = "http://www.opengis.net/ows/2.0"


@dataclass
class AdditionalParameters(AdditionalParametersType):
    """
    Unordered list of one or more AdditionalParameters.
    """

    class Meta:
        namespace = "http://www.opengis.net/ows/2.0"
