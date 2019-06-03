import folium
import pandas

data=pandas.read_excel("Volcanoes.xlsx",sheet_name=0)
data = data.dropna(how='any',axis=0)

lat =  list(data["Latitude"])
lon =  list(data["Longitude"])
elev = list(data["Elevation"])
name=  list(data["Volcano Name"])

def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'
map = folium.Map(location=[50.21,8.80], zoom_start=2, tiles="Mapbox Bright")

fgv = folium.FeatureGroup(name="Volcanoes")

for lt, ln, el,s in zip(lat, lon, elev,name):
    fgv.add_child(folium.CircleMarker(location=[lt, ln], radius = 4, popup=str(s)+":"+str(el)+" m",
    fill_color=color_producer(el), fill=True,  color = 'grey', fill_opacity=0.9))

fgp = folium.FeatureGroup(name="Population")

fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000
else 'orange' if 10000000 <= x['properties']['POP2005'] < 30000000 else 'red','weight':1}))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())

map.save("Map1.html")
