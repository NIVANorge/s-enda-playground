from dataclasses import dataclass, field
from typing import List, Optional
from bindings.csw_publication.abstract_general_transformation_type import AbstractGeneralTransformationType
from bindings.csw_publication.uses_method import UsesMethod
from bindings.csw_publication.uses_value import UsesValue

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class TransformationType(AbstractGeneralTransformationType):
    """A concrete operation on coordinates that usually includes a change of
    datum.

    The parameters of a coordinate transformation are empirically
    derived from data containing the coordinates of a series of points
    in both coordinate reference systems. This computational process is
    usually "over-determined", allowing derivation of error (or
    accuracy) estimates for the transformation. Also, the stochastic
    nature of the parameters may result in multiple (different) versions
    of the same coordinate transformation. This concrete complexType can
    be used for all operation methods, without using an Application
    Schema that defines operation-method-specialized element names and
    contents, especially for methods with only one Transformation
    instance.

    :ivar uses_method:
    :ivar uses_value: Unordered set of composition associations to the
        set of parameter values used by this transformation operation.
    """
    uses_method: Optional[UsesMethod] = field(
        default=None,
        metadata={
            "name": "usesMethod",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        }
    )
    uses_value: List[UsesValue] = field(
        default_factory=list,
        metadata={
            "name": "usesValue",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
