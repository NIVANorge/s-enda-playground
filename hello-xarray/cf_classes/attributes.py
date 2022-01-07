from dataclasses import dataclass
from typing import List, Literal

from xarray_dataclasses import Attr

@dataclass
class LatitudeAttrs:
    standard_name: Attr[str] = "latitude"
    units: Attr[str] = "degree_north"
    valid_min: Attr[float] = -90.0
    valid_max: Attr[float] = 90.0


@dataclass
class LongitudeAttrs:
    standard_name: Attr[str] = "longitude"
    units: Attr[str] = "degree_east"
    valid_min: Attr[float] = -180.0
    valid_max: Attr[float] = 180.0


@dataclass
class SalinityAttrs:
    standard_name: Attr[str] = "sea_water_salinity"
    long_name: Attr[str] = "Salinity at depth"
    units: Attr[str] = "1e-3"
    valid_min: Attr[float] = 10.0
    valid_max: Attr[float] = 40.0


@dataclass
class ConductivityAttrs:
    standard_name: Attr[str] = "sea_water_electrical_conductivity"
    long_name: Attr[str] = "Conductivity at depth"
    units: Attr[str] = "mS cm-1"
    valid_min: Attr[float] = 10.0
    valid_max: Attr[float] = 50.0


@dataclass
class WaterTemperatureAttrs:
    standard_name: Attr[str] = "sea_water_temperature"
    long_name: Attr[str] = "Water Temperature at depth"
    units: Attr[str] = "degree_Celsius"
    valid_min: Attr[float] = 0.0
    valid_max: Attr[float] = 25.0


@dataclass
class TimeAttrs:
    """Specs for the Time axis."""

    standard_name: Attr[str] = "time"
    long_name: Attr[str] = "Time of measurement"
    axis: Attr[str] = "T"
    # units is filled by xarray, based on time interval


@dataclass
class DepthAttrs:
    """Specs for the Z axis."""

    standard_name: Attr[str] = "depth"
    long_name: Attr[str] = "Depth of measurement"
    positive: Attr[str] = "down"
    units: Attr[str] = "m"
    axis: Attr[str] = "Z"
    reference: Attr[str] = "sea_level"
    coordinate_reference_frame: Attr[str] = "urn:ogc:def:crs:EPSG::CRF 5831"

@dataclass
class DatasetAttrs:
    title: Attr[str]
    date_created: Attr[Literal["datetime64[ns]"]]
    keywords: Attr[List[str]]
    featureType: Attr[Literal["timeSeries", "trajectory"]]
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
    netcdf_version: Attr[str] = "4"
    publisher_name: Attr[str] = "NIVA"
    publisher_email: Attr[str] = "post[..]niva.no"
    publisher_url: Attr[str] = "niva.no"
    licence: Attr[
        str
    ] = 'Freely distributed. Must credit the source of data, e.g. "Data fra Norsk Institut for Vannforskning", "Based on data from the Norwegian Institute for Water Research". Data and products are licensed under Norwegian license for public data (NLOD) and Creative Commons Attribution 3.0 Norway. See http://met.no/English/Data_Policy_and_Data_Services/.'
    position_ref: Attr[str] = "ETRS 89"
    history: Attr[str] = "Initial data"
