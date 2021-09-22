from dataclasses import dataclass
from bindings.csw_publication.string_or_ref_type import StringOrRefType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class MappingRule(StringOrRefType):
    """
    Description of a rule for associating members from the domainSet with
    members of the rangeSet.
    """
    class Meta:
        namespace = "http://www.opengis.net/gml"
