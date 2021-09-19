from dataclasses import dataclass
from bindings.csw.harvest_type import HarvestType

__NAMESPACE__ = "http://www.opengis.net/cat/csw/2.0.2"


@dataclass
class Harvest(HarvestType):
    class Meta:
        namespace = "http://www.opengis.net/cat/csw/2.0.2"
