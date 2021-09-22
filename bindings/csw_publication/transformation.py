from dataclasses import dataclass
from bindings.csw_publication.transformation_type import TransformationType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class Transformation(TransformationType):
    class Meta:
        namespace = "http://www.opengis.net/gml"
