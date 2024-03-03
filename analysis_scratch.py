"""
By: Tayo Castro
Description: Some early exploration of geographic data related to the Wild Basin Wilderness Preserve.
"""

# Library Imports
import matplotlib as mpl
import matplotlib.pyplot as plt
import geopandas as gpd

# Reading in Shapefiles
terrain_df = gpd.read_file(r"data\USGS_HUC_8_Shapefile\USGS_HUC_8_Subbasin.shp")

terrain_df.plot()
plt.show()