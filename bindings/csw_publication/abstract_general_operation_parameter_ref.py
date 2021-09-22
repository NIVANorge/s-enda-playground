from dataclasses import dataclass
from bindings.csw_publication.abstract_general_operation_parameter_ref_type import AbstractGeneralOperationParameterRefType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class AbstractGeneralOperationParameterRef(AbstractGeneralOperationParameterRefType):
    class Meta:
        name = "abstractGeneralOperationParameterRef"
        namespace = "http://www.opengis.net/gml"
