# 3/3 AIRBNB 
# The dataset 
df = pd.read_csv('C:\\...\\DATA\\AirbnbIstanbul.csv')

# Manipulation of the dataset
df = df.drop_duplicates()
df = df[df['latitude'] != 'n/a']
df = df[df['longitude'] != 'n/a']

# Filtering the dataset
df = df[df['neighbourhood'].isin(['Kadikoy', 'Fatih', "Üsküdar", "Beyoğlu", 'Besiktas'])]
df = df[df['room_type'].isin(['Entire home/apt'])]
df = df[df['price'] < 1000]

# Save the cleaned data to a new csv file
df.to_csv('final_airbnb.csv', index=False)

df = df.dropna(subset=['neighbourhood'])


# Create the function to make an API request to the Nominatim with latitude and longitude as inputs
# Return the semt (neighborhood), ilçe (district) and coordinates

def get_semt(lat, lon):
    request_text = f"https://nominatim.openstreetmap.org/reverse?lat={lat}&lon={lon}&format=json&zoom=18"
    response = requests.get(request_text)
    response = response.json()
    
    if "suburb" in response["address"]:
        semt = response["address"]["suburb"]
    else:
        semt = response["address"]["neighbourhood"]

    semt = semt.replace(" Mahallesi", "")
    ilce = response["address"]["town"]

    return semt, ilce, lat, lon


# Check the funtion ourput format by giving a sample coordinates

lat = 40.962856
lon = 29.061369

semt, ilce, latitude, longitude = get_semt(lat, lon)
print(f"Neighborhood: {semt}")
print(f"District: {ilce}")
print(f"Latitude: {latitude}")
print(f"Longitude: {longitude}")


# Up to here neighborhoods, districts and coordinates are stored for every entry in the Airbnb file


# From here, after obtaining the neighborhoods, calculate the average price of listings by subsetting neighborhood

#Extract the prices and locations from the csv file and store it in the related dictionaries for further mapping and analyzing purposes
prices = {}
locations = {}

# To keep track of the number of entries processed
counter = 0  

with open('final_airbnb.csv', 'r',  encoding='utf-8') as file:
    csv_file = csv.DictReader(file)

    for row in csv_file:
        lat, lon = float(row['latitude']), float(row['longitude'])
        price = int(row['price'])
        semt, ilce, lat, lon = get_semt(lat, lon)

        if semt in prices:
            prices[semt].append(price)
        else:
            prices[semt] = [price]
            locations[semt] = (lat, lon)
        
        # Increment the counter after each search
        counter += 1

        # For efficiency purposes, the loop stops when 700 rows have been processed
        if counter == 1000:
            break



### MAP CREATIONS

# First map will only show the population distribution among Istanbul's neighborhood
# From the "merged" file created earlier, neighborhood name by "name" and the total population by "TOPLAM" will suffice
# The results account the whole area so Choropleth type will suit better
# key_on is the common parameter for both geoJSON and population CSV file

m = folium.Map(location=[41.0082, 28.9784], zoom_start=10)

choropleth = folium.Choropleth(
    geo_data=merged.__geo_interface__, 
    name='choropleth',
    data=merged,
    columns=['name', 'TOPLAM'],
    key_on='feature.properties.name',
    fill_color='YlOrRd',
    fill_opacity=1,
    line_opacity=0.2,
    legend_name='Population in Istanbul Districts'
)

choropleth.add_to(m)



# Second map will pin the each cafes to the map

for df in [dfcafes]:
    for lat, lon, name in df[['Latitude', 'Longitude', 'Name']].values.tolist():
        folium.Marker(
            location=[lat, lon],
            popup=name,
            icon=folium.Icon(icon="cloud"),
        ).add_to(m)

m.save('ist_pop_cafe.html')

m

# The third map will calculate the average AIRBNB price for each neighborhood and show it via circle by diameter 

# Compute the average prices
average_prices = {semt: sum(price_list) / len(price_list) for semt, price_list in prices.items()}

# Add markers for each Airbnb location
for semt, (lat, lon) in locations.items():
    average_price = average_prices[semt]

    # Create a string that contains the information you want to display
    info = f"Semt: {semt}<br>Average Price: {average_price:.2f}"

    # Create a popup with the information
    popup = folium.Popup(info, max_width=250)

    # Add a circle marker for the location to the map
    folium.CircleMarker(
        location=[lat, lon],
        radius=average_price / 20, 
        color="darkgrey",
        fill=True,
        fill_color="green",
        fill_opacity=0.6,
        popup=popup
    ).add_to(m)

m.save('istanbul_last.html')

m