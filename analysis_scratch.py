"""
By: Tayo Castro
Description: Some early exploration of geographic data related to the Wild Basin Wilderness Preserve.
"""

# Library Imports
import matplotlib as mpl
import matplotlib.pyplot as plt
import geopandas as gpd

# Reading in Shapefiles
maj_aquifer_df = gpd.read_file(r"data\major_aquifers\NEW_major_aquifers_dd.shp")  # Major aquifer file
min_aquifer_df = gpd.read_file(r"data\minor_aquifers\Minor_Aquifers.shp")  # Minor aquifer file
subbasin_df = gpd.read_file(r"data\USGS_HUC_8_Shapefile\USGS_HUC_8_Subbasin.shp")  # Subbasin file
precip_df = gpd.read_file(r"data\Precipitation_Shapefile\TX_Precip_1981_2010_NRCS.shp")  # Precipitation file
rivers_df = gpd.read_file(r"data\Major_Rivers_dd83\MajorRivers_dd83.shp")  # Rivers file
river_basins_df = gpd.read_file(r"data\Major_River_Basins_Shapefile\TWDB_MRBs_2014.shp")  # River basins file
reservoirs_df = gpd.read_file(r"data\existing_reservoirs\TWDB_SWP2012_Major_Reservoirs.shp")  # Reservoirs file



min_aquifer_df.plot()
plt.show()