from dataclasses import dataclass, field
from typing import Union
from bindings.wfs.lang_value import LangValue

__NAMESPACE__ = "http://www.opengis.net/wfs/2.0"


@dataclass
class Abstract2:
    class Meta:
        name = "Abstract"
        namespace = "http://www.opengis.net/wfs/2.0"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
    lang: Union[str, LangValue] = field(
        default="en",
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
