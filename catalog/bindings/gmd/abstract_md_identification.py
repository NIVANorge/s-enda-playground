from dataclasses import dataclass
from bindings.gmd.abstract_md_identification_type import AbstractMdIdentificationType

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class AbstractMdIdentification(AbstractMdIdentificationType):
    class Meta:
        name = "AbstractMD_Identification"
        namespace = "http://www.isotc211.org/2005/gmd"
