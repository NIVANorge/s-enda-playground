from dataclasses import dataclass
from bindings.csw.record_property_type import RecordPropertyType

__NAMESPACE__ = "http://www.opengis.net/cat/csw/2.0.2"


@dataclass
class RecordProperty(RecordPropertyType):
    """
    The RecordProperty element is used to specify the new value of a record
    property in an update statement.
    """

    class Meta:
        namespace = "http://www.opengis.net/cat/csw/2.0.2"
