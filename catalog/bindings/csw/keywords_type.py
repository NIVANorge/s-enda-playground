from dataclasses import dataclass, field
from typing import List, Optional
from bindings.csw.code_type_1 import CodeType1

__NAMESPACE__ = "http://www.opengis.net/ows"


@dataclass
class KeywordsType:
    """Unordered list of one or more commonly used or formalised word(s) or
    phrase(s) used to describe the subject.

    When needed, the optional "type" can name the type of the associated
    list of keywords that shall all have the same type. Also when
    needed, the codeSpace attribute of that "type" can reference the
    type name authority and/or thesaurus. For OWS use, the optional
    thesaurusName element was omitted as being complex information that
    could be referenced by the codeSpace attribute of the Type element.
    """

    keyword: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Keyword",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows",
            "min_occurs": 1,
        },
    )
    type: Optional[CodeType1] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows",
        },
    )
