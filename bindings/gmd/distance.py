from dataclasses import dataclass
from bindings.gmd.length_type import LengthType

__NAMESPACE__ = "http://www.isotc211.org/2005/gco"


@dataclass
class Distance(LengthType):
    class Meta:
        namespace = "http://www.isotc211.org/2005/gco"
