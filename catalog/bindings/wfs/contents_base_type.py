from dataclasses import dataclass, field
from typing import List
from bindings.wfs.dataset_description_summary_base_type import DatasetDescriptionSummary
from bindings.wfs.other_source import OtherSource

__NAMESPACE__ = "http://www.opengis.net/ows/1.1"


@dataclass
class ContentsBaseType:
    """Contents of typical Contents section of an OWS service metadata
    (Capabilities) document.

    This type shall be extended and/or restricted if needed for specific
    OWS use to include the specific metadata needed.

    :ivar dataset_description_summary: Unordered set of summary
        descriptions for the datasets available from this OWS server.
        This set shall be included unless another source is referenced
        and all this metadata is available from that source.
    :ivar other_source: Unordered set of references to other sources of
        metadata describing the coverage offerings available from this
        server.
    """
    dataset_description_summary: List[DatasetDescriptionSummary] = field(
        default_factory=list,
        metadata={
            "name": "DatasetDescriptionSummary",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows/1.1",
        }
    )
    other_source: List[OtherSource] = field(
        default_factory=list,
        metadata={
            "name": "OtherSource",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows/1.1",
        }
    )
