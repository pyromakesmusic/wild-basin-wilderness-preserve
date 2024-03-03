"""
By: Tayo Castro
Description: Some early exploration of geographic data related to the Wild Basin Wilderness Preserve.
"""

# Library Imports
import matplotlib as mpl
import matplotlib.pyplot as plt
import geopandas as gpd

# Reading in Shapefiles
maj_aquifer_df = gpd.read_file(r"data\major_aquifers\NEW_major_aquifers_dd.shp")
subbasin_df = gpd.read_file(r"data\USGS_HUC_8_Shapefile\USGS_HUC_8_Subbasin.shp") # Subbasin file
precip_df = gpd.read_file(r"data\Precipitation_Shapefile\TX_Precip_1981_2010_NRCS.shp")

maj_aquifer_df.plot()
plt.show()