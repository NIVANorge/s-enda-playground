
from dataclasses import dataclass, field
from typing import Literal, List

import numpy as np
from xarray_dataclasses import Attr, Coordof, Data, Name, AsDataset, Dataof

from cfxarray.literals import TIME
from cfxarray.common import WGS1984
from cfxarray.time import DataByTime, TimeAxis, LongitudeByTime, LatitudeByTime
from cfxarray.attributes import DatasetAttrs
from cfxarray.trajectory import TrajectoryId

@dataclass
class Salinity:
    data: Data[TIME, np.float32]
    standard_name: Attr[str] = "sea_water_salinity"
    long_name: Attr[str] = "Salinity at some place"
    units: Attr[str] = "1e-3"

@dataclass
class Temperature:
    data: Data[TIME, np.float32]
    standard_name: Attr[str] = "sea_water_temperature"
    long_name: Attr[str] = "Temperature some place"
    units: Attr[str] = "degree_Celsius"

@dataclass
class SampleDataSet(AsDataset):
    salinity: Dataof[Salinity]
    temperature: Dataof[Temperature]
    trajectory_id: Dataof[TrajectoryId]
    crs: Dataof[WGS1984] = 0
    time: Coordof[TimeAxis] = 0
    lat: Coordof[LatitudeByTime] = 0
    lon: Coordof[LongitudeByTime] = 0
    title: Attr[str] = ""
    date_created: Attr[Literal["datetime64[ns]"]] = ""
    keywords: Attr[List[str]] = field(default_factory=lambda: [""])
    time_coverage_start: Attr[str] = ""
    time_coverage_end: Attr[str] = ""
    geospatial_lat_min: Attr[float] = 0.0
    geospatial_lat_max: Attr[float] = 0.0
    geospatial_lon_min: Attr[float] = 0.0
    geospatial_lon_max: Attr[float] = 0.0
    keywords_vocabulary: Attr[str] = "GCM:GCMD Keywords"
    data_owner: Attr[str] = "Norwegian Institute for Water Research"
    summary: Attr[str] = ""
    geospatial_vertical_positive: Attr[str] = "down"
    processing_level: Attr[str] = "Missing data has been filled with fillValue."
    Conventions: Attr[str] = "CF-1.6, ACDD-1.3"
    netcdf_version: Attr[str] = "4"
    publisher_name: Attr[str] = "NIVA"
    publisher_email: Attr[str] = "post[..]niva.no"
    publisher_url: Attr[str] = "niva.no"
    licence: Attr[
        str
    ] = 'Freely distributed. Must credit the source of data, e.g. "Data fra Norsk Institut for Vannforskning", "Based on data from the Norwegian Institute for Water Research". Data and products are licensed under Norwegian license for public data (NLOD) and Creative Commons Attribution 3.0 Norway.'
    history: Attr[str] = "Initial data"