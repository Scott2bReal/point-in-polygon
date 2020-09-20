from shapely.geometry import Point, Polygon
import geopandas as gpd
import matplotlib.pyplot as plt
import shapely.speedups

shapely.speedups.enable()

# Enable KML reading
gpd.io.file.fiona.drvsupport.supported_drivers['KML'] = 'rw'

# Read that KML
fp = "/home/scott/Downloads/handlebar.kml"
polys = gpd.read_file(fp, driver='KML')

print(f'Polygon: {polys}')

drange = polys.loc[polys['Name']=='handlebar']

point = Point(-87.696965, 41.912757)

pip_mask = point.within(drange.loc[0, 'geometry'])

print(pip_mask)
