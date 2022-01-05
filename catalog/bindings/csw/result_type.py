from enum import Enum

__NAMESPACE__ = "http://www.opengis.net/cat/csw/2.0.2"


class ResultType(Enum):
    """
    :cvar RESULTS: Include results in the response.
    :cvar HITS: Provide a result set summary, but no results.
    :cvar VALIDATE: Validate the request and return an Acknowledgement
        message if it is valid. Continue processing the request
        asynchronously.
    """
    RESULTS = "results"
    HITS = "hits"
    VALIDATE = "validate"
