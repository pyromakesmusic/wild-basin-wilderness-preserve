"""
By: Tayo Castro
Description: Some early exploration of geographic data related to the Wild Basin Wilderness Preserve.
"""

# Library Imports
import matplotlib as mpl
import matplotlib.pyplot as plt
import geopandas as gpd

"""
Reading in Shapefiles
"""

maj_aquifer_df = gpd.read_file(r"data\major_aquifers\NEW_major_aquifers_dd.shp")  # Major aquifer file
min_aquifer_df = gpd.read_file(r"data\minor_aquifers\Minor_Aquifers.shp")  # Minor aquifer file
subbasin_df = gpd.read_file(r"data\USGS_HUC_8_Shapefile\USGS_HUC_8_Subbasin.shp")  # Subbasin file
precip_df = gpd.read_file(r"data\Precipitation_Shapefile\TX_Precip_1981_2010_NRCS.shp")  # Precipitation file
rivers_df = gpd.read_file(r"data\Major_Rivers_dd83\MajorRivers_dd83.shp")  # Rivers file
river_basins_df = gpd.read_file(r"data\Major_River_Basins_Shapefile\TWDB_MRBs_2014.shp")  # River basins file
reservoirs_df = gpd.read_file(r"data\existing_reservoirs\TWDB_SWP2012_Major_Reservoirs.shp")  # Reservoirs file
groundwater_df = gpd.read_file(r"data\TWDB_Groundwater\TWDB_Groundwater.shp")  # Groundwater file
floodplan_df = gpd.read_file(r"data\Regional_Flood_Planning_Groups\Regional_Flood_Planning_Groups.shp")  # Flood planning file

df_list = [maj_aquifer_df, min_aquifer_df, subbasin_df, precip_df, rivers_df, river_basins_df, reservoirs_df, groundwater_df,
           floodplan_df]

for x in df_list:
    print(x, str(x.crs))
"""
Plotting
"""
fig, ax = plt.subplots(figsize=(15,15))

# reservoirs_df.plot(alpha=0.2, color="indigo", ax=ax)  # Different projection
# min_aquifer_df.plot(alpha=0.2, color="green", ax=ax) # Probably a different projection
# groundwater_df.plot(alpha=0.2, color="lavender", ax=ax)


maj_aquifer_df.plot(alpha=0.2, color="green", ax=ax)
subbasin_df.plot(alpha=0.2, color="indigo", ax=ax)
rivers_df.plot(alpha=0.2, color="blue", ax=ax)
river_basins_df.plot(alpha=0.2, color="cyan", ax=ax)
precip_df.plot(alpha=0.2, color="lavender", ax=ax)
# plt.legend()
plt.show()