import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import shapefile as shp
plt.style.use('ggplot')


# Plot all addresses within Guilford County
addressPoints = pd.read_csv('data/GIS/AddressPoints.csv', sep = ',', keep_default_na = False, low_memory = False)

#print((addressPoints['X']).head())

m1 = Basemap(
    projection = 'cyl',
    llcrnrlon = -80.2,
    llcrnrlat = 35.82,
    urcrnrlon = -79.4,
    urcrnrlat = 36.3
)


m1.drawcounties(color = 'black')
plt.scatter(
    addressPoints['X'],
    addressPoints['Y'],
    s = 2,
    c = 'red',
    alpha = .4)

plt.title('Guilford County Addresses')
plt.show()
