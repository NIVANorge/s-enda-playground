from dataclasses import dataclass, field
from typing import Tuple, Literal, Union

import numpy as np
from xarray_dataclasses import Attr, Coordof, Data, Name

from cf_classes.literals import TIME

from cf_classes.attributes import (
    DatasetAttrs,
)

@dataclass
class TrajectoryId:
    data: Data[None, np.str_]
    name: Name[str] = 'trajectory_id'
    cf_role: Attr[str] = "trajectory_id"
    long_name: Attr[str] = "trajectory"


@dataclass
class _TrajectoryAttrs:
    trajectory_name: Attr[str]


@dataclass
class TrajectoryAttrs(DatasetAttrs, _TrajectoryAttrs):
    featureType: Attr[str] = "trajectory"
