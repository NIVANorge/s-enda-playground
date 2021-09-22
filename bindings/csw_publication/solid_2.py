from dataclasses import dataclass
from bindings.csw_publication.abstract_solid_type import AbstractSolidType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class Solid2(AbstractSolidType):
    """
    The "_Solid" element is the abstract head of the substituition group for
    all (continuous) solid elements.
    """
    class Meta:
        name = "_Solid"
        namespace = "http://www.opengis.net/gml"
