from dataclasses import dataclass
from bindings.csw_publication.measure_or_null_list_type import MeasureOrNullListType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class QuantityList(MeasureOrNullListType):
    """A space separated list of amounts or nulls.

    The amounts use the XML Schema type double.  A single XML attribute
    uom (unit of measure) is required, whose value is a URI which
    identifies the definition of the scale or units by which all the
    amounts in the list must be multiplied.
    """
    class Meta:
        namespace = "http://www.opengis.net/gml"
