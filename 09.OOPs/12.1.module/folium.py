import folium
from folium import Map

# Create a map centered at a specific location
mymap = folium.Map(location=[27.179542068271548,78.02158395314139], zoom_start=10)

# Add a marker with a popup
# folium.Marker(location=[27.179542068271548, 78.02158395314139], popup='Marker Popup').add_to(mymap)

# Save the map as an HTML file
mymap.save('map.html')
