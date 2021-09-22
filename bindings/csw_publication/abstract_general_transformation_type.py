from dataclasses import dataclass
from bindings.csw_publication.general_conversion_ref_type import AbstractCoordinateOperationType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class AbstractGeneralTransformationType(AbstractCoordinateOperationType):
    """An abstract operation on coordinates that usually includes a change of
    Datum.

    The parameters of a coordinate transformation are empirically
    derived from data containing the coordinates of a series of points
    in both coordinate reference systems. This computational process is
    usually "over-determined", allowing derivation of error (or
    accuracy) estimates for the transformation. Also, the stochastic
    nature of the parameters may result in multiple (different) versions
    of the same coordinate transformation. This abstract complexType is
    expected to be extended for well-known operation methods with many
    Transformation instances, in Application Schemas that define
    operation-method-specialized value element names and contents. This
    transformation uses an operation method with associated parameter
    values. However, operation methods and parameter values are directly
    associated with concrete subtypes, not with this abstract type. All
    concrete types derived from this type shall extend this type to
    include a "usesMethod" element that references one "OperationMethod"
    element. Similarly, all concrete types derived from this type shall
    extend this type to include one or more elements each named
    "uses...Value" that each use the type of an element substitutable
    for the "_generalParameterValue" element.
    """
