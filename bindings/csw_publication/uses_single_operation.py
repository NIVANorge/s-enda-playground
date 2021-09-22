from dataclasses import dataclass
from bindings.csw_publication.single_operation_ref_type import SingleOperationRefType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class UsesSingleOperation(SingleOperationRefType):
    """
    Association to a single operation.
    """
    class Meta:
        name = "usesSingleOperation"
        namespace = "http://www.opengis.net/gml"
