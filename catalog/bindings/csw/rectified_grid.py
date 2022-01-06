from dataclasses import dataclass
from bindings.csw.rectified_grid_type import RectifiedGridType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class RectifiedGrid(RectifiedGridType):
    """
    Should be substitutionGroup="gml:Grid" but changed in order to accomplish
    Xerces-J schema validation.
    """

    class Meta:
        namespace = "http://www.opengis.net/gml"
