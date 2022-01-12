
from dataclasses import dataclass, field
from typing import Tuple, Literal

import numpy as np
from xarray_dataclasses import Attr, Data, Coordof, Name

from cf_classes.literals import TIME
from cf_classes.attributes import TimeAttrs, DataVarAttrs
from cf_classes.common import TimeAxis 

@dataclass
class TrajectoryId:
    data: Data[None, np.str_]
    cf_role: Attr[str] = "trajectory_id"
    long_name: Attr[str] = "trajectory"


