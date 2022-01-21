from xarray_dataclasses import Attr, Data, Name
from dataclasses import dataclass

import numpy as np


@dataclass
class WGS1984:
    data: Data[None, np.int8] = 0
    name: Name[str] = "crs"
    grid_mapping_name: Attr[str] = "latitude_longitude"
    longitude_of_prime_meridian: Attr[str] = 0.0
    semi_major_axis: Attr[str] = 6378137.0
    inverse_flattening: Attr[str] = 298.257223563
