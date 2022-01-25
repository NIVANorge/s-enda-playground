from typing import List, Tuple, Union, Any

from datetime import datetime

import xarray as xr

from cfxarray.attributes import (
    VariableAttrs,
)
from dataclasses import asdict, dataclass
from toolz import curry
from cfxarray.dims import TIME, DEPTH

@curry
def variablearray(
    dims: Union[Tuple, str],
    data: List[Any],
    name: str,
    standard_name: str,
    long_name: str,
    units: str,
) -> xr.DataArray:
    return xr.DataArray(
        name=name,
        dims=dims,
        data=data,
        attrs=asdict(
            VariableAttrs(
                standard_name=standard_name,
                long_name=long_name,
                units=units,
            )
        ),
    )


arraybytime = variablearray(TIME)

arraybydepth = variablearray(DEPTH)