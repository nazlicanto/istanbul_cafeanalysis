# Istanbul Neighborhood Analysis
This project analyzes Istanbul neighborhoods in terms of population, café locations, and Airbnb rental prices. It provides insights into café distribution, population density, and average rental prices in different neighborhoods.

## Data Sources
	Café data: Yelp Fusion API
	Neighborhood Polygon/Geometry data: OpenStreetMap Nominatim API
	Population Data: TUIK Istanbul Population (https://datauik.gov.tr/Kategori/GetKategori?p=Nufus-ve-Demografi-109)
	Airbnb data: Airbnb Istanbul dataset (https://www.kaggle.com/datasets/kavanozkafa/airbnb-istanbul-dataset)

## Methods
### Café data retrieval 
The Yelp Fusion API is used to search for cafes in Istanbul. The API is queried with latitude and longitude coordinates for each neighborhood, and the café data is extracted from the API response.

### Neighborhood border retrieval
The OpenStreetMap Nominatim API is used to retrieve p data for Istanbul neighborhoods. The API is queried with neighborhood names and the population data is extracted from the API response.

### Airbnb data analysis: 
The Airbnb dataset for Istanbul is used to analyze rental prices. The data is filtered based on criteria such as neighborhood, room type, and price. Average prices are calculated for each neighborhood.

### Map visualization: 
The collected data is visualized using Folium, a Python library for creating interactive maps. Choropleth maps are created to display population data, café locations are marked with icons, and Airbnb markers are sized based on average rental prices.


## Results
The project provides visual representations of café locations, population density, and Airbnb rental prices in Istanbul neighborhoods. the readme document (continued):

Café Analysis: The café analysis reveals the distribution of cafes across Istanbul neighborhoods, highlighting areas with high café density.

Population Analysis: The population data obtained from OpenStreetMap Nominatim API is visualized using choropleth maps, providing insights into population density and variations across neighborhoods.

Airbnb Rental Prices: The analysis of Airbnb rental prices focuses on selected neighborhoods and filters the data based on criteria such as room type and price. Average prices are calculated for each neighborhood, and the results are displayed as circle markers on the map, with marker size indicating the average price.

The generated map visualization (istanbul_map.html) provides an interactive and visual representation of the collected data, allowing users to explore café locations, population density, and Airbnb rental prices in Istanbul neighborhoods.

