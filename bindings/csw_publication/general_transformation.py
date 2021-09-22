from dataclasses import dataclass
from bindings.csw_publication.abstract_general_transformation_type import AbstractGeneralTransformationType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class GeneralTransformation(AbstractGeneralTransformationType):
    class Meta:
        name = "_GeneralTransformation"
        namespace = "http://www.opengis.net/gml"
