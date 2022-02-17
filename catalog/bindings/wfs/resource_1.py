from dataclasses import dataclass

__NAMESPACE__ = "http://www.opengis.net/ows/1.1"


@dataclass
class Resource1:
    """XML encoded GetResourceByID operation response.

    The complexType used by this element shall be specified by each
    specific OWS.
    """

    class Meta:
        name = "Resource"
        namespace = "http://www.opengis.net/ows/1.1"
