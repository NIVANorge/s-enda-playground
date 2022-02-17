from dataclasses import dataclass
from bindings.gmd.definition_proxy_type import DefinitionProxyType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class DefinitionProxy(DefinitionProxyType):
    class Meta:
        namespace = "http://www.opengis.net/gml"
