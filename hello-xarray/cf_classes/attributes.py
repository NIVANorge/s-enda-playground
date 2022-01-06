from dataclasses import dataclass
from typing import List, Literal

from xarray_dataclasses import Attr


@dataclass
class DatasetAttributes:
    title: Attr[str]
    date_created: Attr[Literal["datetime64[ns]"]]
    keywords: Attr[List[str]]
    featureType: Attr[str] = "timeSeries"
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
    history: Attr[str] = "Initial data"
