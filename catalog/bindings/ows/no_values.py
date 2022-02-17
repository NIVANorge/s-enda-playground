from dataclasses import dataclass

__NAMESPACE__ = "http://www.opengis.net/ows/2.0"


@dataclass
class NoValues:
    """
    Specifies that no values are allowed for this parameter or quantity.
    """

    class Meta:
        namespace = "http://www.opengis.net/ows/2.0"
