from dataclasses import dataclass
from bindings.csw_publication.derivation_unit_term_type import DerivationUnitTermType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class DerivationUnitTerm(DerivationUnitTermType):
    class Meta:
        name = "derivationUnitTerm"
        namespace = "http://www.opengis.net/gml"
