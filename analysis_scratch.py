"""
By: Tayo Castro
Description: Some early exploration of geographic data related to the Wild Basin Wilderness Preserve.
"""

# Library Imports
import matplotlib as mpl
import matplotlib.pyplot as plt
import geopandas as gpd
from shapely.geometry import Point

"""
Reading in Shapefiles
"""

PRESERVE_LATITUDE = 30.310278
PRESERVE_LONGITUDE = -97.823333
LOCATION = Point(PRESERVE_LATITUDE, PRESERVE_LONGITUDE)

# loc_df = gpd.GeoDataFrame(geometry=[LOCATION], crs="EPSG:4326").to_crs(epsg=4269)
#
# maj_aquifer_df = gpd.read_file(r"data\major_aquifers\NEW_major_aquifers_dd.shp")  # Major aquifer file
# min_aquifer_df = gpd.read_file(r"data\minor_aquifers\Minor_Aquifers.shp", crs="EPSG:7019")  # Minor aquifer file
# subbasin_df = gpd.read_file(r"data\USGS_HUC_8_Shapefile\USGS_HUC_8_Subbasin.shp")  # Subbasin file
precip_df = gpd.read_file(r"data\Precipitation_Shapefile\TX_Precip_1981_2010_NRCS.shp")  # Precipitation file
# rivers_df = gpd.read_file(r"data\Major_Rivers_dd83\MajorRivers_dd83.shp")  # Rivers file
# river_basins_df = gpd.read_file(r"data\Major_River_Basins_Shapefile\TWDB_MRBs_2014.shp")  # River basins file
# reservoirs_df = gpd.read_file(r"data\existing_reservoirs\TWDB_SWP2012_Major_Reservoirs.shp", crs="EPSG:7019")  # Reservoirs file
groundwater_df = gpd.read_file(r"data\TWDB_Groundwater\TWDB_Groundwater.shp")  # Groundwater file
floodplan_df = gpd.read_file(r"data\Regional_Flood_Planning_Groups\Regional_Flood_Planning_Groups.shp")  # Flood planning file
#
wildlife_df = gpd.read_file(r"data\WildlifeManagementAreas\WildlifeManagementAreas.shp")  # WIldlife shapefile
#
# geology_df = gpd.read_file(r"data\Tx_GeologyGeneral_USGS\Tx_GeologyGeneral_USGS.shp")  # Geology shapefile
#
parks_df = gpd.read_file(r"data\Tx_StateParks_STRATMAP\Tx_StateParks_STRATMAP.shp")
#
# df_list = [maj_aquifer_df, min_aquifer_df, subbasin_df, precip_df, rivers_df, river_basins_df, reservoirs_df, groundwater_df,
#            floodplan_df]
#
# for x in df_list:
#     print(str(x.crs))
#     print(x.geometry.is_valid)

"""
Data Processing
"""





"""
Plotting
"""

fig, ax = plt.subplots(figsize=(15,15))
ax.set_facecolor("indigo")

# reservoirs_df.plot(column="STATUS", alpha=0.5, ax=ax, legend=True, label="Reservoirs")  # Different projection
# min_aquifer_df.plot(alpha=0.2, color="green", ax=ax) # Probably a different projection
# groundwater_df.plot(alpha=0.4, column="WaterQuali", ax=ax, label="Groundwater")

# loc_df.plot(color="white", ax=ax)
# print(maj_aquifer_df.columns)

# maj_aquifer_df.plot(alpha=0.7, color="green", ax=ax, legend=True, label="Major Aquifers")
# subbasin_df.plot(alpha=0.1, color="indigo", ax=ax, legend=True)
# rivers_df.plot(column="METERS", alpha=0.4, ax=ax, legend=True, label="Rivers")
# river_basins_df.plot(alpha=0.2, color="cyan", ax=ax, legend=True)
# precip_df.plot(alpha=0.1, color="lavender", ax=ax, legend=True)
#
# geology_df.plot(alpha=0.1, color="black", ax=ax, legend=True)
# wildlife_df.plot(alpha=0.4, column="LoCode", ax=ax, legend=True, label="Wildlife")
#
# parks_df.plot(alpha=0.2, color="orange", ax=ax, legend=True)



# precip_df.describe()
precip_df.plot(column="Inches", alpha=0.5, label="Precipitation (inches)", legend=True, ax=ax)
groundwater_df.plot(column="WaterQuali", alpha=0.5, label="Groundwater Quality", legend=True, ax=ax, s=0.3)
floodplan_df.plot(alpha=0.3, label="Flood Plan", legend=True, ax=ax)
# groundwater_df.plot(x="Elevation", y="WellDepth", kind="scatter", s=1, alpha=0.1, title="Elevation vs. Well Depth", ax=ax)

# groundwater_df.plot(x="WaterQuali", kind="bar")


# ax.set_yscale("log")
# ax.set_xscale("log")
# groundwater_df["WaterQuali"].hist(bins=2)  # Slightly less quality water than bad quality water. We probably care where good water is


# Create custom legends
# handles, labels = ax.get_legend_handles_labels()
# ax.legend(handles, labels, title='One legend', loc='upper left')

# Create additional legend manually
# Adjust the bbox_to_anchor parameter to position the legend as desired
# ax.legend(title='Another legend', loc='upper right', bbox_to_anchor=(1.05, 3))
plt.show()
"""
Console Output
"""
floodplan_df.describe()
print(floodplan_df.columns)
print(floodplan_df.describe())