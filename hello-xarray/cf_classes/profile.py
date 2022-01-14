from dataclasses import dataclass, field
from typing import Literal
import numpy as np

from xarray_dataclasses import Attr, Coordof, Data, Name

from cf_classes.literals import DEPTH
from cf_classes.attributes import DatasetAttrs, DataVarAttrs, DepthAttrs
from cf_classes.dimless import Latitude, Longitude, Time

@dataclass
class ProfileId:
    data: Data[None, Literal["|S64"]]
    name: Name[str] = "profile_id"
    long_name: Attr[str] = "Profile ID"
    cf_role: Attr[str] = "profile_id"


@dataclass
class _ProfileAttrs:
    profile_name: Attr[str]


@dataclass
class ProfileAttrs(DatasetAttrs, _ProfileAttrs):
    featureType: Attr[str] = "profile"

@dataclass
class DepthData:
    data: Data[DEPTH, np.float32]

@dataclass
class Depth(DepthAttrs, DepthData):
    pass

@dataclass
class DepthProfileVariable(DataVarAttrs):
    data: Data[DEPTH, np.float32]
    name: Name[str]
    time: Coordof[Time]
    lat: Coordof[Latitude]
    lon: Coordof[Longitude]
    depth: Coordof[Depth]
    grid_mapping: Attr[str] = "crs"
    coordinates: Attr[str] = "time lat lon depth"
