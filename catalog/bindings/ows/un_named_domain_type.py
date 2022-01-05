from dataclasses import dataclass, field
from typing import List, Optional
from bindings.ows.additional_parameters import AdditionalParameters
from bindings.ows.allowed_values import AllowedValues
from bindings.ows.any_value import AnyValue
from bindings.ows.data_type import DataType
from bindings.ows.meaning import Meaning
from bindings.ows.metadata import Metadata
from bindings.ows.no_values import NoValues
from bindings.ows.reference_system import ReferenceSystem
from bindings.ows.uom import Uom
from bindings.ows.values_reference import ValuesReference

__NAMESPACE__ = "http://www.opengis.net/ows/2.0"


@dataclass
class UnNamedDomainType:
    """
    Valid domain (or allowed set of values) of one quantity, with needed
    metadata but without a quantity name or identifier.

    :ivar allowed_values:
    :ivar any_value:
    :ivar no_values:
    :ivar values_reference:
    :ivar default_value: Optional default value for this quantity, which
        should be included when this quantity has a default value.
    :ivar meaning: Meaning metadata should be referenced or included for
        each quantity.
    :ivar data_type: This data type metadata should be referenced or
        included for each quantity.
    :ivar uom: Identifier of unit of measure of this set of values.
        Should be included then this set of values has units (and not a
        more complete reference system).
    :ivar reference_system: Identifier of reference system used by this
        set of values. Should be included then this set of values has a
        reference system (not just units).
    :ivar additional_parameters:
    :ivar metadata: Optional unordered list of other metadata about this
        quantity. A list of required and optional other metadata
        elements for this quantity should be specified in the
        Implementation Specification for this service.
    """
    allowed_values: Optional[AllowedValues] = field(
        default=None,
        metadata={
            "name": "AllowedValues",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows/2.0",
        }
    )
    any_value: Optional[AnyValue] = field(
        default=None,
        metadata={
            "name": "AnyValue",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows/2.0",
        }
    )
    no_values: Optional[NoValues] = field(
        default=None,
        metadata={
            "name": "NoValues",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows/2.0",
        }
    )
    values_reference: Optional[ValuesReference] = field(
        default=None,
        metadata={
            "name": "ValuesReference",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows/2.0",
        }
    )
    default_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "DefaultValue",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows/2.0",
        }
    )
    meaning: Optional[Meaning] = field(
        default=None,
        metadata={
            "name": "Meaning",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows/2.0",
        }
    )
    data_type: Optional[DataType] = field(
        default=None,
        metadata={
            "name": "DataType",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows/2.0",
        }
    )
    uom: Optional[Uom] = field(
        default=None,
        metadata={
            "name": "UOM",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows/2.0",
        }
    )
    reference_system: Optional[ReferenceSystem] = field(
        default=None,
        metadata={
            "name": "ReferenceSystem",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows/2.0",
        }
    )
    additional_parameters: List[AdditionalParameters] = field(
        default_factory=list,
        metadata={
            "name": "AdditionalParameters",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows/2.0",
        }
    )
    metadata: List[Metadata] = field(
        default_factory=list,
        metadata={
            "name": "Metadata",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows/2.0",
        }
    )
