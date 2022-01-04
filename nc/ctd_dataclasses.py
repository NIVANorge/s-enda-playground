from dataclasses import dataclass
from typing import List, Literal, Tuple
from datetime import datetime
from xarray_dataclasses import AsDataArray, AsDataset, Attr, Coord, Data, Name, Coordof, Dataof
import numpy as np

DEPTH = Literal["depth"]
TIME = Literal["time"]
LATITUDE = Literal["latitude"]
LONGITUDE = Literal["longitude"]
WATERTEMP = Literal["WaterTemp"]

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
class Latitude(AsDataArray):
    data: Data[TIME, np.float64]
    name: Name[str] = "latitude"
    time: Coordof[TimeAxis] = 0
    standard_name: Attr[str] = "latitude"
    units: Attr[str] = "degree_north"
    valid_min: Attr[float] = -90.0
    valid_max: Attr[float] = 90.0

@dataclass
class Longitude(AsDataArray):
    data: Data[TIME, np.float64]
    name: Name[str] = "longitude"
    time: Coordof[TimeAxis] = 0
    standard_name: Attr[str] = "longitude"
    units: Attr[str] = "degree_east"
    valid_min: Attr[float] = -180.0
    valid_max: Attr[float] = 180.0

@dataclass
class Salinity(AsDataArray):
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
class Conductivity(AsDataArray):
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
class WaterTemp(AsDataArray):
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
    title: str
    date_created: Literal["datetime64[ns]"]
    keywords: List[str]
    geospatial_lat_min: float = 0
    geospatial_lat_max: float = 0
    geospatial_lon_min: float = 0
    geospatial_lon_max: float = 0
    keywords_vocabulary: str = "GCM:GCMD Keywords"
    data_owner: str = "Norwegian Institute for Water Research"
    summary: str = ""
    geospatial_vertical_positive: str = "down"
    processing_level: str = "Missing data has been filled with fillValue."
    Conventions: str = "CF-1.6, ACDD-1.3"
    netcdf_version: str ="4"
    publisher_name: str ="NIVA"
    publisher_email: str = "post[..]niva.no"
    publisher_url: str = "niva.no"
    licence: str = "Freely distributed. Must credit the source of data, e.g. \"Data fra Norsk Institut for Vannforskning\", \"Based on data from the Norwegian Institute for Water Research\". Data and products are licensed under Norwegian license for public data (NLOD) and Creative Commons Attribution 3.0 Norway. See http://met.no/English/Data_Policy_and_Data_Services/.",
    position_ref: str = "ETRS 89"

@dataclass
class BoyeHeader:
    time_coverage_start: datetime
    time_coverage_end: datetime
    buoy_type: str = "Wavescan"
    buoy_manufacturer: str = "Fugro Norway AS"
    buoy_serialno: str = "WS161"
    water_depth: str = "495m"
    station_name: str = "E39 G Halsafjorden"
    sensor_type: str = "SBE37-SIP"
    sensor_manufacturer: str = "Sea Bird Electronics Inc., 13431 NE 20th street, Bellevue, 98005 Washington, USA"
    sensor_level: str = "b.s.l."
    sensor_serialno: str = "37-15244,37-15416,37-15408,37-15401"
    measurement_update_period: str = "10 s"
    status: str = "in progress"
    featureType: str = "timeSeries"
    #history: str