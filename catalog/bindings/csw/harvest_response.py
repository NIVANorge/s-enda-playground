from dataclasses import dataclass
from bindings.csw.harvest_response_type import HarvestResponseType

__NAMESPACE__ = "http://www.opengis.net/cat/csw/2.0.2"


@dataclass
class HarvestResponse(HarvestResponseType):
    """The content of the response varies depending on the presence of the
    ResponseHandler element.

    If present, then the catalogue should verify the request and respond
    immediately with an csw:Acknowledgement element in the response. The
    catalogue must then attempt to harvest the resource at some later
    time and send the response message to the location specified by the
    value of the ResponseHandler element using the indicated protocol
    (e.g. ftp, mailto, http). If the ResponseHandler element is absent,
    then the catalogue must attempt to harvest the resource immediately
    and include a TransactionResponse element in the response. In any
    case, if the harvest attempt is successful the response shall
    include summary representations of the newly created catalogue
    item(s).
    """
    class Meta:
        namespace = "http://www.opengis.net/cat/csw/2.0.2"
