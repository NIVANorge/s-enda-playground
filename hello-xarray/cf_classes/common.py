from xarray_dataclasses import Attr, Data, Name
from typing import Literal
from dataclasses import dataclass

from xarray_dataclasses import Coordof
import numpy as np

from cf_classes.literals import TIME


from cf_classes.attributes import TimeAttrs, DataVarAttrs

@dataclass
class WGS1984:
    data: Data[None, np.int8] = 0
    name: Name[str] = "crs"
    grid_mapping_name: Attr[str] = "latitude_longitude"
    longitude_of_prime_meridian: Attr[str] = 0.0
    semi_major_axis: Attr[str] = 6378137.0
    inverse_flattening: Attr[str] = 298.257223563
