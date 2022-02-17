from enum import Enum

__NAMESPACE__ = "http://www.opengis.net/gml"


class SuccessionType(Enum):
    """Feature succession is a semantic relationship derived from evaluation of
    observer, and Feature Substitution, Feature Division and Feature Fusion are
    defined as associations between previous features and next features in the
    temporal context. Successions shall be represented in either following two
    ways.

    * define a temporal topological complex element as a feature element
    * define an association same as temporal topological complex between features.
    """

    SUBSTITUTION = "substitution"
    DIVISION = "division"
    FUSION = "fusion"
    INITIATION = "initiation"
