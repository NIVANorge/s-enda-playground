from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.opengis.net/cat/csw/2.0.2"


@dataclass
class DistributedSearchType:
    """Governs the behaviour of a distributed search.

    hopCount     - the maximum number of message hops before
    the search is terminated. Each catalogue node
    decrements this value when the request is received,
    and must not forward the request if hopCount=0.
    """

    hop_count: int = field(
        default=2,
        metadata={
            "name": "hopCount",
            "type": "Attribute",
        },
    )
