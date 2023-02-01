import geocoder
import folium

g = geocoder.ip('85.91.209.254')
my_adress = g.latlng
print(my_adress)

my_map = folium.Map(location=my_adress, zoom_start=12)

folium.CircleMarker(location=my_adress, radius=50).add_to(my_map)
folium.CircleMarker(location=[55.0055, 31.0000], radius=50).add_to(my_map)

folium.Marker(my_adress).add_to(my_map)
folium.Marker([55.0055, 31.0000]).add_to(my_map)

my_map.save('my_map.html')