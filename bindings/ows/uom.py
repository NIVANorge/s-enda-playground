from dataclasses import dataclass
from bindings.ows.domain_metadata_type import DomainMetadataType

__NAMESPACE__ = "http://www.opengis.net/ows/2.0"


@dataclass
class Uom(DomainMetadataType):
    """Definition of the unit of measure of this set of values.

    In this case, the xlink:href attribute can reference a URN for a
    well-known unit of measure (uom). For example, such a URN could be a
    UOM identification URN defined in the "ogc" URN namespace.
    """
    class Meta:
        name = "UOM"
        namespace = "http://www.opengis.net/ows/2.0"
