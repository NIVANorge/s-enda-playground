from dataclasses import dataclass

__NAMESPACE__ = "http://www.opengis.net/ows/2.0"


@dataclass
class AnyValue:
    """
    Specifies that any value is allowed for this parameter.
    """
    class Meta:
        namespace = "http://www.opengis.net/ows/2.0"
