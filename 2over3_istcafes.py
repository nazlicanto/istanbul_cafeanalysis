# The list of 178 neighborhoods of all Beşiktaş, Kadıkoy, Beyoğlu, Fatih and Üsküdar
neighborhood_list = ["Abbasağa, Beşiktaş",
                    "Akat, Beşiktaş",
                    "Arnavutköy, Beşiktaş",
                    "Balmumcu, Beşiktaş",
                    ...
                    ...
                    "Zeynep Kamil, Üsküdar"]

result_dict = {}

# Searching the neighborhood through Nominatim API
for neighborhood in neighborhood_list:
    request_text = urllib.parse.quote(neighborhood + " Istanbul")
    request_text = f"https://nominatim.openstreetmap.org/search?q={request_text}&polygon_geojson=1&format=json"
    response = requests.get(request_text)

    # Decoding API response
    response = response.json()


# Check the response, if there is a valid response with added "Istanbul" query, take the first result
# Store the selected attributes on the given variables: name, borders of the neighborhood
# Print the neighborhood name from(query, from the list) is no result available

    if response:
        neighborhood_result = response[0]
        decoded_name = urllib.parse.unquote(neighborhood_result['display_name']) 
        feature = {
            "type": "Feature",
            "properties": {
                "name": decoded_name  
            },
            "geometry": neighborhood_result['geojson']
        }
        result_dict[neighborhood] = feature
    else:
        print(f"No results for {neighborhood}")



# Convert the outcome data GeoJSON format for mapping purposes 
geojson_data = {
    "type": "FeatureCollection",
    "features": list(result_dict.values())

}

# Save the GeoJSON into "resultv2.json" for further purposes
with open('resultv2.json', 'w') as fp:
    json.dump(geojson_data, fp)


# Retrieve the data with your fav geographic data reader
# Check the dataframe by printing the head
districts = gpd.read_file('resultv2.json')
print(districts.head())


# Recall the population data 
population = pd.read_csv("C:\\Users\\...DATASETS\\tüiklast2.csv")

# Merge the population data with the districts dataframe
merged = districts.set_index('name').join(population.set_index('name')).reset_index()


# Visualize the merge file which neighborhood, names, boundry coordinates and populations
# Color Shading ~ Choropleth

m = folium.Map(location=[41.0082, 28.9784], zoom_start=10)

choropleth = folium.Choropleth(
    geo_data=merged.__geo_interface__, 
    name='choropleth',
    data=merged,
    columns=['name', 'TOPLAM'],
    key_on='feature.properties.name',
    fill_color='OrRd',
    fill_opacity=1,
    line_opacity=0.2,
    legend_name='Population in Istanbul Districts'
)

choropleth.add_to(m)

m