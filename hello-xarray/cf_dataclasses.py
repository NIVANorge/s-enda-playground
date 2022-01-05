from dataclasses import dataclass
from typing import List, Literal, Tuple
from datetime import datetime
from xarray_dataclasses import AsDataArray, AsDataset, Attr, Coord, Data, Name, Coordof, Dataof
import numpy as np

DEPTH = Literal["depth"]
TIME = Literal["time"]
LATITUDE = Literal["latitude"]
LONGITUDE = Literal["longitude"]

@dataclass
class TimeAxis:
    """Specs for the x axis."""
    data: Data[TIME, Literal["datetime64[ns]"]]
    standard_name: Attr[str] = "time"
    long_name: Attr[str] = "Time of measurement"
    axis: Attr[str] = "T"
    # units is filled by xarray, based on time interval

@dataclass
class DepthAxis:
    """Specs for the y axis."""
    data: Data[DEPTH, np.int16]
    standard_name: Attr[str] = "depth",
    long_name: Attr[str] = "Depth of measurement"
    positive: Attr[str] = "down"
    units: Attr[str] = "m"
    axis: Attr[str] = "Z"
    reference: Attr[str] = "sea_level"
    coordinate_reference_frame: Attr[str] = "urn:ogc:def:crs:EPSG::CRF 5831"
    
@dataclass
class Latitude:
    data: Data[TIME, np.float64]
    name: Name[str] = "latitude"
    time: Coordof[TimeAxis] = 0
    standard_name: Attr[str] = "latitude"
    units: Attr[str] = "degree_north"
    valid_min: Attr[float] = -90.0
    valid_max: Attr[float] = 90.0

@dataclass
class Longitude:
    data: Data[TIME, np.float64]
    name: Name[str] = "longitude"
    time: Coordof[TimeAxis] = 0
    standard_name: Attr[str] = "longitude"
    units: Attr[str] = "degree_east"
    valid_min: Attr[float] = -180.0
    valid_max: Attr[float] = 180.0

@dataclass
class Salinity:
    data: Data[Tuple[TIME, DEPTH], np.float32]
    name: Name[str] = "salinity"
    time: Coordof[TimeAxis] = 0
    depth: Coordof[DepthAxis] = 0
    standard_name: Attr[str] = "sea_water_salinity"
    long_name: Attr[str] = "Salinity at depth"
    units: Attr[str] = "1e-3"
    valid_min: Attr[float]= 10.0
    valid_max: Attr[float]= 40.0

@dataclass
class Conductivity:
    data: Data[Tuple[TIME, DEPTH], np.float32]
    name: Name[str] = "conductivity"
    time: Coordof[TimeAxis] = 0
    depth: Coordof[DepthAxis] = 0
    standard_name: Attr[str] = "sea_water_electrical_conductivity"
    long_name: Attr[str] = "Conductivity at depth"
    units: Attr[str] = "mS cm-1"
    valid_min: Attr[float]= 10.0
    valid_max: Attr[float]= 50.0

@dataclass
class WaterTemperature:
    data: Data[Tuple[TIME, DEPTH], np.float32]
    name: Name[str] = "sea_water_temperature"
    time: Coordof[TimeAxis] = 0
    depth: Coordof[DepthAxis] = 0
    standard_name: Attr[str] = "sea_water_temperature"
    long_name: Attr[str] = "Water Temperature at depth"
    units: Attr[str] = "degree_Celsius"
    valid_min: Attr[float]= 0.0
    valid_max: Attr[float]= 25.0

@dataclass
class CTDDatasetAttributes:
    title: Attr[str]
    date_created: Attr[Literal["datetime64[ns]"]]
    keywords: Attr[List[str]]
    geospatial_lat_min: Attr[float] = 0
    geospatial_lat_max: Attr[float] = 0
    geospatial_lon_min: Attr[float] = 0
    geospatial_lon_max: Attr[float] = 0
    keywords_vocabulary: Attr[str] = "GCM:GCMD Keywords"
    data_owner: Attr[str] = "Norwegian Institute for Water Research"
    summary: Attr[str] = ""
    geospatial_vertical_positive: Attr[str] = "down"
    processing_level: Attr[str] = "Missing data has been filled with fillValue."
    Conventions: Attr[str] = "CF-1.6, ACDD-1.3"
    netcdf_version: Attr[str] ="4"
    publisher_name: Attr[str] ="NIVA"
    publisher_email: Attr[str] = "post[..]niva.no"
    publisher_url: Attr[str] = "niva.no"
    licence: Attr[str] = "Freely distributed. Must credit the source of data, e.g. \"Data fra Norsk Institut for Vannforskning\", \"Based on data from the Norwegian Institute for Water Research\". Data and products are licensed under Norwegian license for public data (NLOD) and Creative Commons Attribution 3.0 Norway. See http://met.no/English/Data_Policy_and_Data_Services/."
    position_ref: Attr[str] = "ETRS 89"
    history: Attr[str] = "I did something to this dataset"
    featureType: Attr[str] = "timeSeries"

@dataclass
class BoyeHeader:
    time_coverage_start: datetime
    time_coverage_end: datetime
    buoy_type: str = "some type"
    buoy_manufacturer: str = "some manufacture"
    buoy_serialno: str = "number"
    water_depth: str = "495m"
    station_name: str = "Station name"
    sensor_type: str = "some sensor type"
    measurement_update_period: str = "10 s"
    status: str = "in progress"
    #history: str