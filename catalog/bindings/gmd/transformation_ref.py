from dataclasses import dataclass
from bindings.gmd.transformation_property_type import TransformationPropertyType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class TransformationRef(TransformationPropertyType):
    class Meta:
        name = "transformationRef"
        namespace = "http://www.opengis.net/gml"
