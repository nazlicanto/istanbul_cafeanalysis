# Istanbul Neighborhood Analysis
The project analyzes Istanbul neighborhoods in terms of population, café locations, and Airbnb rental prices. It provides insights into café distribution, population density, and average rental prices in different neighborhoods. The polygon values regards to Istanbul's neighborhoods(mahalle) are not publicly available, so we will be mapping them as well. 


## Data Sources
	Café data: Yelp Fusion API
	Neighborhood Polygon/Geometry data: OpenStreetMap Nominatim API
	Population Data: TUIK Istanbul Population (https://datauik.gov.tr/Kategori/GetKategori?p=Nufus-ve-Demografi-109)
	Airbnb data: Airbnb Istanbul dataset (https://www.kaggle.com/datasets/kavanozkafa/airbnb-istanbul-dataset)

## Methods
### Café data retrieval 
The Yelp Fusion API is used to search for cafes in Istanbul. The API is queried with latitude and longitude coordinates for each neighborhood and "coffee" term has been requested. The café data is extracted from the API response.

### Neighborhood border retrieval
The OpenStreetMap Nominatim API is used to retrieve neighborhood data for Istanbul neighborhoods. The API is queried with neighborhood names and the population data is extracted from the API response.

### Airbnb data analysis: 
The Airbnb dataset for Istanbul is used to analyze rental prices. The data is filtered based on criteria such as neighborhood, room type(house/room selections has been separated), and price. Average prices are calculated for each neighborhood.

### Map visualization: 
The collected data is visualized using Folium for creating interactive maps. Choropleth maps are created to display population data, café locations are marked with icons, and Airbnb markers are sized based on average rental prices.


## Results
The project provides visual representations of the boundaries of neighborhoods, café locations, population density among neighborhoods and Airbnb rental prices in Istanbul.

Geospatial Data: The polygon data retrieved from OpenStreetMap Nominatim API map the boundaries among neighborhoods of Istanbul.

Café Analysis: The café analysis reveals the distribution of cafes across Istanbul neighborhoods.

Population Analysis: The population data obtained from OpenStreetMap Nominatim API is visualized using choropleth maps, providing insights into population density.

Airbnb Rental Prices: The analysis of Airbnb rental prices focuses on selected neighborhoods and filters the data based on criteria such as room type and price. Average prices are calculated for each neighborhood, and the results are displayed as circle markers on the map, with marker size indicating the average price.

The generated map visualization (istanbul_map.html) provides an interactive and visual representation of the collected data, allowing users to explore café locations, population density, and Airbnb rental prices in Istanbul neighborhoods.

