from dataclasses import dataclass
from bindings.csw_publication.abstract_gmltype import AbstractGmltype

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class Gml(AbstractGmltype):
    """
    Global element which acts as the head of a substitution group that may
    include any element which is a GML feature, object, geometry or complex
    value.
    """
    class Meta:
        name = "_GML"
        namespace = "http://www.opengis.net/gml"
