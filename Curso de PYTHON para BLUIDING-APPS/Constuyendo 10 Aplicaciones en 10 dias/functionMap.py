import folium
import pandas as pd

path_file_txt = "C:/Users/JOSHUASANCH3/Documents/_REPOSITORIES/PYTHON-GITHUB/PYTHON-LERNING/Curso de PYTHON para BLUIDING-APPS/Constuyendo 10 Aplicaciones en 10 dias/_test_jupyter/volcanes.txt"

# This code is for creating a map with markers using Folium and pandas.
data = pd.read_csv(path_file_txt, on_bad_lines="skip")
lat = list(data["Latitud"])  # Replace with the actual column name for latitude
lon = list(data["Longitud"])  # Replace with the actual column name for longitude
elev = list(data["Elevacion"])  # Replace with the actual column name for elevation
name = list(data["Nombre"])  # Replace with the actual column name for name


def color_producer(elevation):
    """Function to determine the color of the marker based on elevation."""
    if elevation < 1000:
        return "green"
    elif 1000 <= elevation < 3000:
        return "orange"
    else:
        return "red"


# The CSV file should contain latitude and longitude columns for the markers.
my_map = folium.Map(location=[38.58, -99.09], zoom_start=6, titles="Mapbox Bright")

# The map is centered at the specified latitude and longitude with a zoom level of 6.
fgv = folium.FeatureGroup(name="My Map")

# Adding a feature group to the map for better organization of markers.
for lt, ln, el, name in zip(lat, lon, elev, name):
    fgv.add_child(
        folium.CircleMarker(
            location=(lt, ln),
            radius=6,
            popup=name + "\n" + str(el) + " m",
            fill_color=color_producer(el),
            color="grey",
            fill_opacity=0.7,
        )
    )

# other function
fgp = folium.FeatureGroup(name="Population")

fgp.add_child(
    folium.GeoJson(
        data=open("World.json", "r+", encoding="utf-8-sig"),
        style_function=lambda x: (
            {"fillColor": "yellow"}
            if x["properties"]["POP2005"] < 10000000
            else (
                {"fillColor": "orange"}
                if 10000000 <= x["properties"]["POP2005"] < 20000000
                else {"fillColor": "red"}
            )
        ),
    )
)
# Ensure the parentheses are properly closed.
# It appears to be intended for adding GeoJSON data to the map, but the file path is missing.

my_map.add_child(fgv)  ## Adding the feature group with volcano markers to the map.
my_map.add_child(fgp)  ## Adding the feature group with population data to the map.
my_map.add_child(
    folium.LayerControl()
)  ## Adding a layer control to toggle between different feature groups.
path_save_file = "C:/Users/JOSHUASANCH3/Documents/_REPOSITORIES/PYTHON-GITHUB/PYTHON-LERNING/Curso de PYTHON para BLUIDING-APPS/Constuyendo 10 Aplicaciones en 10 dias/Mapl.html"
my_map.save(path_save_file)  # Save the map to an HTML file.
