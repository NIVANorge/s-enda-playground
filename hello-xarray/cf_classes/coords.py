from dataclasses import dataclass
from typing import Literal

import numpy as np
from xarray_dataclasses import AsDataArray, AsDataset, Attr, Coord, Coordof, Data, Name

from cf_classes.literals import DEPTH, TIME


@dataclass
class TimeAxis:
    """Specs for the Time axis."""

    data: Data[TIME, Literal["datetime64[ns]"]]
    standard_name: Attr[str] = "time"
    long_name: Attr[str] = "Time of measurement"
    axis: Attr[str] = "T"
    # units is filled by xarray, based on time interval


@dataclass
class DepthAxis:
    """Specs for the Z axis."""

    data: Data[DEPTH, np.int16]
    standard_name: Attr[str] = ("depth",)
    long_name: Attr[str] = "Depth of measurement"
    positive: Attr[str] = "down"
    units: Attr[str] = "m"
    axis: Attr[str] = "Z"
    reference: Attr[str] = "sea_level"
    coordinate_reference_frame: Attr[str] = "urn:ogc:def:crs:EPSG::CRF 5831"
