import cf
from numpy import array, float32

#
# field: sea_water_electrical_conductivity
field = cf.Field()
field.set_properties(
    {
        "title": "Data collection for some Boye, Norway",
        "buoy_type": "Wavescan",
        "geospatial_lat_min": 63.08360291,
        "geospatial_lat_max": 63.08715057,
        "geospatial_lon_min": 8.15149307,
        "geospatial_lon_max": 8.15889359,
        "data_owner": "Norwegian Institute for Water Research",
        "summary": "",
        "station_name": "Some station",
        "position_ref": "ETRS 89",
        "buoy_manufacturer": "Fugro Norway AS",
        "buoy_serialno": "WS161",
        "water_depth": "495m",
        "keywords_vocabulary": "GCMD:GCMD Keywords",
        "keywords": [
            "Atmosphere > Atmospheric winds\n",
            "Oceans  > Ocean Circulation  > Ocean Currents\n",
            "Oceans  > Ocean Pressure\n",
            "Oceans  > Ocean Temperature\n",
            "Oceans  > Ocean Waves\n",
            "Oceans  > Ocean Winds\n",
            "Oceans  > Salinity/Density\n",
        ],
        "geospatial_vertical_positive": "down",
        "processing_level": "Missing data has been filled with fillValue.",
        "Conventions": "CF-1.6, ACDD-1.3",
        "netcdf_version": "4",
        "publisher_name": "MET Norway",
        "publisher_email": "post[..]met.no",
        "publisher_url": "met.no",
        "licence": 'Freely distributed. Must credit the source of data, e.g. "Data from the Norwegian Meteorological Institute", "Based on data from the Norwegian Meteorological Institute". Data and products are licensed under Norwegian license for public data (NLOD) and Creative Commons Attribution 3.0 Norway. See http://met.no/English/Data_Policy_and_Data_Services/.',
        "date_created": "2021-12-01T01:17:07Z",
        "sensor_type": "SBE37-SIP",
        "sensor_manufacturer": "Sea Bird Electronics Inc., 13431 NE 20th street, Bellevue, 98005 Washington, USA",
        "sensor_level": "b.s.l.",
        "sensor_serialno": "37-15244,37-15416,37-15408,37-15401",
        "measurement_update_period": "10 s",
        "status": "in progress",
        "featureType": "timeSeries",
        "time_coverage_start": "2021-12-01T00:00:00",
        "time_coverage_end": "2021-12-15T11:59:50",
        "history": "ncrcat one month of hourly data files. Buoy WS142 was serviced 09 01 2019 Buoy out of position for ADCP replacement (new batteries required) 2019 08 06 10:37-11:38 WS142 was out of position for battery replacement from 2021 23 11:00 to 2021 24 12:20 UTC WS142 was recovered 2021 27 08:00 WS161 was deployed 2021 27 13:50 UTC",
        "_FillValue": 9999.0,
        "standard_name": "sea_water_electrical_conductivity",
        "long_name": "Conductivity at depth",
        "units": "mS cm-1",
        "valid_range": array([10.0, 50.0], dtype=float32),
    }
)
field.nc_set_variable("Conductivity")
data = []
field.set_data(data)
#
# netCDF global attributes
field.nc_set_global_attributes(
    {
        "title": None,
        "buoy_type": None,
        "geospatial_lat_min": None,
        "geospatial_lat_max": None,
        "geospatial_lon_min": None,
        "geospatial_lon_max": None,
        "data_owner": None,
        "data_collecting_contractor": None,
        "summary": None,
        "station_name": None,
        "position_ref": None,
        "buoy_manufacturer": None,
        "buoy_serialno": None,
        "water_depth": None,
        "keywords_vocabulary": None,
        "keywords": None,
        "geospatial_vertical_positive": None,
        "processing_level": None,
        "Conventions": None,
        "netcdf_version": None,
        "publisher_name": None,
        "publisher_email": None,
        "publisher_url": None,
        "licence": None,
        "date_created": None,
        "sensor_type": None,
        "sensor_manufacturer": None,
        "sensor_level": None,
        "sensor_serialno": None,
        "measurement_update_period": None,
        "status": None,
        "featureType": None,
        "time_coverage_start": None,
        "time_coverage_end": None,
        "history": None,
    }
)
#
# domain_axis: ncdim%time
c = cf.DomainAxis()
c.set_size(124920)
c.nc_set_dimension("time")
fc.nc_set_unlimited({True})
field.set_construct(c, key="domainaxis0", copy=False)
#
# domain_axis: ncdim%depth
c = cf.DomainAxis()
c.set_size(4)
c.nc_set_dimension("depth")
field.set_construct(c, key="domainaxis1", copy=False)
#
# dimension_coordinate: time
c = cf.DimensionCoordinate()
c.set_properties(
    {
        "standard_name": "time",
        "long_name": "Time of measurement",
        "units": "seconds since 1970-01-01 00:00:00 UTC",
        "axis": "T",
        "comment": "End of the 10 s sampling period",
        "calendar": "standard",
    }
)
c.nc_set_variable("time")
c.set_data(data)
field.set_construct(c, axes=("domainaxis0",), key="dimensioncoordinate0", copy=False)
#
# dimension_coordinate: depth
c = cf.DimensionCoordinate()
c.set_properties(
    {
        "standard_name": "depth",
        "long_name": "Depth of measurement",
        "positive": "down",
        "units": "m",
        "axis": "Z",
        "reference": "sea_level",
        "coordinate_reference_frame": "urn:ogc:def:crs:EPSG::CRF 5831",
    }
)
c.nc_set_variable("depth")
c.set_data(data)

field.set_construct(c, axes=("domainaxis1",), key="dimensioncoordinate1", copy=False)
#
# field data axes
field.set_data_axes(("domainaxis0", "domainaxis1"))
