from dataclasses import dataclass
from bindings.csw.transformation_ref_type import TransformationRefType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class TransformationRef(TransformationRefType):
    class Meta:
        name = "transformationRef"
        namespace = "http://www.opengis.net/gml"
