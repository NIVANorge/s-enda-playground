from dataclasses import dataclass, field
from typing import Optional, Union
from bindings.gmd.binary import Binary
from bindings.gmd.nil_reason_enumeration_value import NilReasonEnumerationValue

__NAMESPACE__ = "http://www.isotc211.org/2005/gco"


@dataclass
class BinaryPropertyType:
    class Meta:
        name = "Binary_PropertyType"

    binary: Optional[Binary] = field(
        default=None,
        metadata={
            "name": "Binary",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gco",
        },
    )
    nil_reason: Optional[Union[str, NilReasonEnumerationValue]] = field(
        default=None,
        metadata={
            "name": "nilReason",
            "type": "Attribute",
            "namespace": "http://www.isotc211.org/2005/gco",
            "pattern": r"other:\w{2,}",
        },
    )
