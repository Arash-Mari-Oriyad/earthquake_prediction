import pandas as pd
import numpy as np
import geopandas as gpd
import matplotlib.pyplot as plt
from shapely.geometry import Point, Polygon
from geopandas import GeoDataFrame


# df = pd.read_csv("Long_Lats.csv", delimiter=',', skiprows=0, low_memory=False)
df = pd.DataFrame(data={'longitude': [77, 82, 110, 93],
                        'latitude': [33, 41, 24, 37]})

geometry = [Point(xy) for xy in zip(df['longitude'], df['latitude'])]

gdf = GeoDataFrame(df, geometry=geometry)

world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
# gdf.plot(ax=world.plot(figsize=(10, 6)), marker='o', color='red', markersize=15)

singapore = world.loc[world['name'] == 'Singapore']
boundaries = singapore['geometry']
boundaries.plot()

# -------------------------------------------------------------------

# df = pd.read_csv('kc_house_data_train.csv')
# df = df[['id', 'price', 'sqft_living', 'waterfront', 'zipcode', 'long', 'lat']]
# df.head()

kings_county_map = gpd.read_file('CHN_adm/CHN_adm1.shp')
kings_county_map.plot()

# plt.show()
plt.savefig('figure_1.svg', format='svg')

# ---------------------------------------------------------------------

world = gpd.read_file(gpd.datasets.get_path("naturalearth_lowres"))

polygon = Polygon([(75, 23), (75, 45), (119, 45), (119, 23), (75, 23)])
poly_gdf = gpd.GeoDataFrame([1], geometry=[polygon], crs=world.crs)

fig, ax = plt.subplots(1, 1, figsize=(12, 8))
world.plot(ax=ax)
poly_gdf.boundary.plot(ax=ax, color="red")
ax.set_title("All Unclipped World Data", fontsize=20)
ax.set_axis_off()