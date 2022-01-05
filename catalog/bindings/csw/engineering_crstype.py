from dataclasses import dataclass, field
from typing import Optional
from bindings.csw.abstract_reference_system_type import AbstractReferenceSystemType
from bindings.csw.uses_cs import UsesCs
from bindings.csw.uses_engineering_datum import UsesEngineeringDatum

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class EngineeringCrstype(AbstractReferenceSystemType):
    """A contextually local coordinate reference system; which can be divided
    into two broad categories:

    - earth-fixed systems applied to engineering activities on or near the surface of the earth;
    - CRSs on moving platforms such as road vehicles, vessels, aircraft, or spacecraft.
    For further information, see OGC Abstract Specification Topic 2.
    """
    class Meta:
        name = "EngineeringCRSType"

    uses_cs: Optional[UsesCs] = field(
        default=None,
        metadata={
            "name": "usesCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        }
    )
    uses_engineering_datum: Optional[UsesEngineeringDatum] = field(
        default=None,
        metadata={
            "name": "usesEngineeringDatum",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        }
    )
