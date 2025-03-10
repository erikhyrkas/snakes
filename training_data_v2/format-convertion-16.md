Please transform the following plain text data into markdown:
Device ID: device-0088 | Device Type: Motion Detector | Location: Hallway | Battery Level (%): 54.7 | Timestamp: 2023-12-15 01:05:07
Device ID: device-0018 | Device Type: Pressure Sensor | Location: Hallway | Battery Level (%): 63.5 | Timestamp: 2022-03-05 11:28:20
Device ID: device-0087 | Device Type: Light Sensor | Location: Hallway | Battery Level (%): 32.7 | Timestamp: 2021-01-22 14:07:33
Device ID: device-0070 | Device Type: Pressure Sensor | Location: Garage | Battery Level (%): 77.5 | Timestamp: 2022-12-08 14:27:36
Device ID: device-0047 | Device Type: Pressure Sensor | Location: Living Room | Battery Level (%): 59.3 | Timestamp: 2023-03-25 06:04:03
Device ID: device-0087 | Device Type: Light Sensor | Location: Hallway | Battery Level (%): 47.4 | Timestamp: 2022-12-27 08:15:15
Device ID: device-0048 | Device Type: Humidity Sensor | Location: Bedroom | Battery Level (%): 56.8 | Timestamp: 2023-12-16 03:23:23
Device ID: device-0070 | Device Type: Motion Detector | Location: Kitchen | Battery Level (%): 80.8 | Timestamp: 2022-08-06 21:12:30
<start>
| Device ID | Device Type | Location | Battery Level (%) | Timestamp |
| --- | --- | --- | --- | --- |
| device-0088 | Motion Detector | Hallway | 54.7 | 2023-12-15 01:05:07 |
| device-0018 | Pressure Sensor | Hallway | 63.5 | 2022-03-05 11:28:20 |
| device-0087 | Light Sensor | Hallway | 32.7 | 2021-01-22 14:07:33 |
| device-0070 | Pressure Sensor | Garage | 77.5 | 2022-12-08 14:27:36 |
| device-0047 | Pressure Sensor | Living Room | 59.3 | 2023-03-25 06:04:03 |
| device-0087 | Light Sensor | Hallway | 47.4 | 2022-12-27 08:15:15 |
| device-0048 | Humidity Sensor | Bedroom | 56.8 | 2023-12-16 03:23:23 |
| device-0070 | Motion Detector | Kitchen | 80.8 | 2022-08-06 21:12:30 |
<end>Can you change this Markdown into yaml?
| Restaurant Name | Cuisine | Location | Rating | Price Range |
| --- | --- | --- | --- | --- |
| Pasta Palace | Mexican | Chicago | 4 | $$ |
| Burger Haven | Mediterranean | Phoenix | 1 | $$$$ |
| The Golden Spoon | Japanese | New York | 5 | $ |
| Taco Town | Chinese | Chicago | 3 | $ |
| The Golden Spoon | American | Chicago | 4 | $$ |
| Sushi World | Mexican | Phoenix | 3 | $$ |
| Pizza Planet | French | Phoenix | 4 | $$$ |<start>
- Cuisine: Mexican
  Location: Chicago
  Price Range: $$
  Rating: 4
  Restaurant Name: Pasta Palace
- Cuisine: Mediterranean
  Location: Phoenix
  Price Range: $$$$
  Rating: 1
  Restaurant Name: Burger Haven
- Cuisine: Japanese
  Location: New York
  Price Range: $
  Rating: 5
  Restaurant Name: The Golden Spoon
- Cuisine: Chinese
  Location: Chicago
  Price Range: $
  Rating: 3
  Restaurant Name: Taco Town
- Cuisine: American
  Location: Chicago
  Price Range: $$
  Rating: 4
  Restaurant Name: The Golden Spoon
- Cuisine: Mexican
  Location: Phoenix
  Price Range: $$
  Rating: 3
  Restaurant Name: Sushi World
- Cuisine: French
  Location: Phoenix
  Price Range: $$$
  Rating: 4
  Restaurant Name: Pizza Planet
<end>Here's some Json data, can you convert it to MARKDOWN?
[
    {
        "Device ID": "device-0051",
        "Device Type": "Motion Detector",
        "Location": "Living Room",
        "Battery Level (%)": 36.7,
        "Reading Value": 34.28,
        "Timestamp": "2022-05-11 00:07:08"
    },
    {
        "Device ID": "device-0072",
        "Device Type": "Light Sensor",
        "Location": "Office",
        "Battery Level (%)": 67.0,
        "Reading Value": 10.6,
        "Timestamp": "2021-09-11 13:47:02"
    },
    {
        "Device ID": "device-0062",
        "Device Type": "Light Sensor",
        "Location": "Garage",
        "Battery Level (%)": 22.5,
        "Reading Value": 67.37,
        "Timestamp": "2022-10-05 04:45:18"
    },
    {
        "Device ID": "device-0077",
        "Device Type": "Pressure Sensor",
        "Location": "Garage",
        "Battery Level (%)": 56.3,
        "Reading Value": 70.65,
        "Timestamp": "2021-07-15 16:52:52"
    },
    {
        "Device ID": "device-0003",
        "Device Type": "Temperature Sensor",
        "Location": "Bathroom",
        "Battery Level (%)": 42.3,
        "Reading Value": 47.97,
        "Timestamp": "2021-10-26 10:16:22"
    },
    {
        "Device ID": "device-0086",
        "Device Type": "Humidity Sensor",
        "Location": "Office",
        "Battery Level (%)": 48.4,
        "Reading Value": -4.48,
        "Timestamp": "2023-02-03 15:44:26"
    }
]<start>
| Device ID | Device Type | Location | Battery Level (%) | Reading Value | Timestamp |
| --- | --- | --- | --- | --- | --- |
| device-0051 | Motion Detector | Living Room | 36.7 | 34.28 | 2022-05-11 00:07:08 |
| device-0072 | Light Sensor | Office | 67.0 | 10.6 | 2021-09-11 13:47:02 |
| device-0062 | Light Sensor | Garage | 22.5 | 67.37 | 2022-10-05 04:45:18 |
| device-0077 | Pressure Sensor | Garage | 56.3 | 70.65 | 2021-07-15 16:52:52 |
| device-0003 | Temperature Sensor | Bathroom | 42.3 | 47.97 | 2021-10-26 10:16:22 |
| device-0086 | Humidity Sensor | Office | 48.4 | -4.48 | 2023-02-03 15:44:26 |
<end>Here's some Yml data, can you convert it to Csv?
- Close Price: 168.42
  Company: MediaGroup
  Date: '2022-04-02'
  High Price: 1398.96
  Low Price: 168.42
  Open Price: 1398.96
  Volume: 6091287
- Close Price: 1481.64
  Company: BioLife
  Date: '2018-11-01'
  High Price: 1481.64
  Low Price: 662.12
  Open Price: 1388.74
  Volume: 5743102
- Close Price: 800.38
  Company: TechnoCorp
  Date: '2023-08-21'
  High Price: 800.38
  Low Price: 403.03
  Open Price: 403.03
  Volume: 8724683
- Close Price: 1167.92
  Company: RetailWorld
  Date: '2015-08-11'
  High Price: 1235.82
  Low Price: 159.41
  Open Price: 1235.82
  Volume: 521022
<start>
Company,Date,Open Price,Close Price,High Price,Low Price,Volume
MediaGroup,2022-04-02,1398.96,168.42,1398.96,168.42,6091287
BioLife,2018-11-01,1388.74,1481.64,1481.64,662.12,5743102
TechnoCorp,2023-08-21,403.03,800.38,800.38,403.03,8724683
RetailWorld,2015-08-11,1235.82,1167.92,1235.82,159.41,521022
<end>Please transform the following yml data into Markdown:
- Location: Miami
  Price Range: $$$$
  Restaurant Name: Sushi World
- Location: Miami
  Price Range: $
  Restaurant Name: Pizza Planet
- Location: Miami
  Price Range: $$$
  Restaurant Name: Pizza Planet
- Location: Phoenix
  Price Range: $$$$$
  Restaurant Name: The Golden Spoon
<start>
| Restaurant Name | Location | Price Range |
| --- | --- | --- |
| Sushi World | Miami | $$$$ |
| Pizza Planet | Miami | $ |
| Pizza Planet | Miami | $$$ |
| The Golden Spoon | Phoenix | $$$$$ |
<end>Can you change this Plain text into Csv?
Device ID: device-0068 | Device Type: Pressure Sensor | Location: Bathroom | Battery Level (%): 78.7 | Reading Value: -30.94 | Timestamp: 2022-01-08 20:04:14
Device ID: device-0041 | Device Type: Motion Detector | Location: Bedroom | Battery Level (%): 58.5 | Reading Value: -33.04 | Timestamp: 2022-07-05 03:45:23
Device ID: device-0085 | Device Type: Light Sensor | Location: Garage | Battery Level (%): 92.3 | Reading Value: -21.85 | Timestamp: 2022-08-11 14:22:52
Device ID: device-0028 | Device Type: Motion Detector | Location: Office | Battery Level (%): 79.5 | Reading Value: 35.75 | Timestamp: 2022-06-03 20:04:23
Device ID: device-0079 | Device Type: Light Sensor | Location: Living Room | Battery Level (%): 28.9 | Reading Value: -25.65 | Timestamp: 2022-10-24 00:30:38
Device ID: device-0062 | Device Type: Light Sensor | Location: Garage | Battery Level (%): 23.6 | Reading Value: 82.5 | Timestamp: 2021-08-05 10:58:29
Device ID: device-0082 | Device Type: Humidity Sensor | Location: Living Room | Battery Level (%): 22.3 | Reading Value: 73.54 | Timestamp: 2023-08-22 21:42:44
Device ID: device-0022 | Device Type: Temperature Sensor | Location: Garden | Battery Level (%): 28.9 | Reading Value: 58.81 | Timestamp: 2022-04-24 14:02:56
<start>
Device ID,Device Type,Location,Battery Level (%),Reading Value,Timestamp
device-0068,Pressure Sensor,Bathroom,78.7,-30.94,2022-01-08 20:04:14
device-0041,Motion Detector,Bedroom,58.5,-33.04,2022-07-05 03:45:23
device-0085,Light Sensor,Garage,92.3,-21.85,2022-08-11 14:22:52
device-0028,Motion Detector,Office,79.5,35.75,2022-06-03 20:04:23
device-0079,Light Sensor,Living Room,28.9,-25.65,2022-10-24 00:30:38
device-0062,Light Sensor,Garage,23.6,82.5,2021-08-05 10:58:29
device-0082,Humidity Sensor,Living Room,22.3,73.54,2023-08-22 21:42:44
device-0022,Temperature Sensor,Garden,28.9,58.81,2022-04-24 14:02:56
<end>Here's some yml data, can you convert it to json?
- Humidity (%): 29
  Location: Phoenix
  Wind Speed (km/h): 23.2
- Humidity (%): 90
  Location: Miami
  Wind Speed (km/h): 16.6
- Humidity (%): 56
  Location: Houston
  Wind Speed (km/h): 5.9
- Humidity (%): 49
  Location: Phoenix
  Wind Speed (km/h): 15.6
- Humidity (%): 41
  Location: Houston
  Wind Speed (km/h): 5.0
<start>
[
    {
        "Location": "Phoenix",
        "Humidity (%)": 29,
        "Wind Speed (km/h)": 23.2
    },
    {
        "Location": "Miami",
        "Humidity (%)": 90,
        "Wind Speed (km/h)": 16.6
    },
    {
        "Location": "Houston",
        "Humidity (%)": 56,
        "Wind Speed (km/h)": 5.9
    },
    {
        "Location": "Phoenix",
        "Humidity (%)": 49,
        "Wind Speed (km/h)": 15.6
    },
    {
        "Location": "Houston",
        "Humidity (%)": 41,
        "Wind Speed (km/h)": 5.0
    }
]
<end>Transform this JSON structure to a YAML format:
[
    {
        "Location": "Los Angeles",
        "Condition": "Snowy",
        "Wind Speed (km/h)": 23.5
    },
    {
        "Location": "Seattle",
        "Condition": "Rainy",
        "Wind Speed (km/h)": 0.7
    },
    {
        "Location": "New York",
        "Condition": "Sunny",
        "Wind Speed (km/h)": 18.8
    },
    {
        "Location": "Seattle",
        "Condition": "Stormy",
        "Wind Speed (km/h)": 5.2
    },
    {
        "Location": "Miami",
        "Condition": "Rainy",
        "Wind Speed (km/h)": 10.4
    }
]<start>
- Condition: Snowy
  Location: Los Angeles
  Wind Speed (km/h): 23.5
- Condition: Rainy
  Location: Seattle
  Wind Speed (km/h): 0.7
- Condition: Sunny
  Location: New York
  Wind Speed (km/h): 18.8
- Condition: Stormy
  Location: Seattle
  Wind Speed (km/h): 5.2
- Condition: Rainy
  Location: Miami
  Wind Speed (km/h): 10.4
<end>Here's some MARKDOWN data, can you convert it to Yaml?
| Location | Condition | Temperature (C) | Wind Speed (km/h) | Day |
| --- | --- | --- | --- | --- |
| Denver | Sunny | 24.7 | 23.2 | Friday |
| Chicago | Stormy | 14.2 | 22.0 | Monday |
| Phoenix | Windy | 7.0 | 25.8 | Wednesday |
| Phoenix | Snowy | 6.5 | 6.2 | Saturday |
| Denver | Sunny | 32.4 | 0.6 | Saturday |
| Denver | Rainy | 15.3 | 15.2 | Thursday |<start>
- Condition: Sunny
  Day: Friday
  Location: Denver
  Temperature (C): 24.7
  Wind Speed (km/h): 23.2
- Condition: Stormy
  Day: Monday
  Location: Chicago
  Temperature (C): 14.2
  Wind Speed (km/h): 22.0
- Condition: Windy
  Day: Wednesday
  Location: Phoenix
  Temperature (C): 7.0
  Wind Speed (km/h): 25.8
- Condition: Snowy
  Day: Saturday
  Location: Phoenix
  Temperature (C): 6.5
  Wind Speed (km/h): 6.2
- Condition: Sunny
  Day: Saturday
  Location: Denver
  Temperature (C): 32.4
  Wind Speed (km/h): 0.6
- Condition: Rainy
  Day: Thursday
  Location: Denver
  Temperature (C): 15.3
  Wind Speed (km/h): 15.2
<end>Convert this Plain text to Csv:
Open Price: 1492.86 | Close Price: 364.25 | Low Price: 364.25 | Volume: 8236716
Open Price: 1005.87 | Close Price: 470.53 | Low Price: 470.53 | Volume: 4070234
Open Price: 188.73 | Close Price: 1173.4 | Low Price: 188.73 | Volume: 7145305
Open Price: 930.31 | Close Price: 1005.87 | Low Price: 902.61 | Volume: 3136391
<start>
Open Price,Close Price,Low Price,Volume
1492.86,364.25,364.25,8236716
1005.87,470.53,470.53,4070234
188.73,1173.4,188.73,7145305
930.31,1005.87,902.61,3136391
<end>Please transform the following json data into plain text:
[
    {
        "Product Name": "Widget",
        "SKU": "SKU-1047",
        "Price": 132.71,
        "Stock Quantity": 434,
        "Category": "Toys",
        "Supplier Name": "Globex"
    },
    {
        "Product Name": "Contraption",
        "SKU": "SKU-1053",
        "Price": 140.79,
        "Stock Quantity": 113,
        "Category": "Toys",
        "Supplier Name": "Umbrella Corp"
    },
    {
        "Product Name": "Device",
        "SKU": "SKU-1083",
        "Price": 241.82,
        "Stock Quantity": 319,
        "Category": "Toys",
        "Supplier Name": "ACME Corp"
    },
    {
        "Product Name": "Widget",
        "SKU": "SKU-1043",
        "Price": 405.28,
        "Stock Quantity": 95,
        "Category": "Toys",
        "Supplier Name": "Globex"
    },
    {
        "Product Name": "Device",
        "SKU": "SKU-1001",
        "Price": 96.95,
        "Stock Quantity": 385,
        "Category": "Household",
        "Supplier Name": "Umbrella Corp"
    },
    {
        "Product Name": "Thingamajig",
        "SKU": "SKU-1056",
        "Price": 338.01,
        "Stock Quantity": 472,
        "Category": "Sports",
        "Supplier Name": "Umbrella Corp"
    },
    {
        "Product Name": "Instrument",
        "SKU": "SKU-1069",
        "Price": 375.01,
        "Stock Quantity": 473,
        "Category": "Toys",
        "Supplier Name": "Wayne Enterprises"
    },
    {
        "Product Name": "Gadget",
        "SKU": "SKU-1024",
        "Price": 491.23,
        "Stock Quantity": 447,
        "Category": "Sports",
        "Supplier Name": "Globex"
    }
]<start>
Product Name: Widget | SKU: SKU-1047 | Price: 132.71 | Stock Quantity: 434 | Category: Toys | Supplier Name: Globex
Product Name: Contraption | SKU: SKU-1053 | Price: 140.79 | Stock Quantity: 113 | Category: Toys | Supplier Name: Umbrella Corp
Product Name: Device | SKU: SKU-1083 | Price: 241.82 | Stock Quantity: 319 | Category: Toys | Supplier Name: ACME Corp
Product Name: Widget | SKU: SKU-1043 | Price: 405.28 | Stock Quantity: 95 | Category: Toys | Supplier Name: Globex
Product Name: Device | SKU: SKU-1001 | Price: 96.95 | Stock Quantity: 385 | Category: Household | Supplier Name: Umbrella Corp
Product Name: Thingamajig | SKU: SKU-1056 | Price: 338.01 | Stock Quantity: 472 | Category: Sports | Supplier Name: Umbrella Corp
Product Name: Instrument | SKU: SKU-1069 | Price: 375.01 | Stock Quantity: 473 | Category: Toys | Supplier Name: Wayne Enterprises
Product Name: Gadget | SKU: SKU-1024 | Price: 491.23 | Stock Quantity: 447 | Category: Sports | Supplier Name: Globex
<end>Transform this Json structure to a csv format:
[
    {
        "Company": "Foodies",
        "Sector": "Healthcare",
        "Market Cap": "Large Cap"
    },
    {
        "Company": "RetailHub",
        "Sector": "Aerospace",
        "Market Cap": "Mega Cap"
    },
    {
        "Company": "FinanceWorks",
        "Sector": "Retail",
        "Market Cap": "Mega Cap"
    },
    {
        "Company": "GlobalTrade",
        "Sector": "Retail",
        "Market Cap": "Mega Cap"
    },
    {
        "Company": "BioPharm",
        "Sector": "Automotive",
        "Market Cap": "Mega Cap"
    },
    {
        "Company": "TechCorp",
        "Sector": "Retail",
        "Market Cap": "Large Cap"
    }
]<start>
Company,Sector,Market Cap
Foodies,Healthcare,Large Cap
RetailHub,Aerospace,Mega Cap
FinanceWorks,Retail,Mega Cap
GlobalTrade,Retail,Mega Cap
BioPharm,Automotive,Mega Cap
TechCorp,Retail,Large Cap
<end>Here's some Plain text data, can you convert it to MARKDOWN?
Database Name: MetricsDB | Queries per Second: 2004.44 | Cache Hit Ratio (%): 73.79 | Connection Count: 153 | Average Latency (ms): 58.02 | Timestamp: 2021-10-02 00:30:40
Database Name: SessionsDB | Queries per Second: 3696.74 | Cache Hit Ratio (%): 75.34 | Connection Count: 255 | Average Latency (ms): 62.02 | Timestamp: 2022-07-06 22:02:57
Database Name: LogsDB | Queries per Second: 936.5 | Cache Hit Ratio (%): 76.92 | Connection Count: 41 | Average Latency (ms): 86.0 | Timestamp: 2022-04-16 05:00:40
Database Name: SessionsDB | Queries per Second: 3661.49 | Cache Hit Ratio (%): 94.61 | Connection Count: 150 | Average Latency (ms): 11.75 | Timestamp: 2023-12-04 21:32:22
Database Name: ProductsDB | Queries per Second: 594.86 | Cache Hit Ratio (%): 89.66 | Connection Count: 41 | Average Latency (ms): 11.75 | Timestamp: 2022-02-18 21:48:13
Database Name: MetricsDB | Queries per Second: 4925.19 | Cache Hit Ratio (%): 76.42 | Connection Count: 303 | Average Latency (ms): 96.04 | Timestamp: 2022-08-07 08:58:34
Database Name: ProfilesDB | Queries per Second: 2073.79 | Cache Hit Ratio (%): 76.42 | Connection Count: 437 | Average Latency (ms): 45.11 | Timestamp: 2021-07-13 11:52:46
Database Name: ProductsDB | Queries per Second: 819.6 | Cache Hit Ratio (%): 74.52 | Connection Count: 191 | Average Latency (ms): 4.49 | Timestamp: 2022-05-20 22:56:53
Database Name: InventoryDB | Queries per Second: 3309.55 | Cache Hit Ratio (%): 92.55 | Connection Count: 195 | Average Latency (ms): 72.71 | Timestamp: 2021-09-19 16:48:48
<start>
| Database Name | Queries per Second | Cache Hit Ratio (%) | Connection Count | Average Latency (ms) | Timestamp |
| --- | --- | --- | --- | --- | --- |
| MetricsDB | 2004.44 | 73.79 | 153 | 58.02 | 2021-10-02 00:30:40 |
| SessionsDB | 3696.74 | 75.34 | 255 | 62.02 | 2022-07-06 22:02:57 |
| LogsDB | 936.5 | 76.92 | 41 | 86.0 | 2022-04-16 05:00:40 |
| SessionsDB | 3661.49 | 94.61 | 150 | 11.75 | 2023-12-04 21:32:22 |
| ProductsDB | 594.86 | 89.66 | 41 | 11.75 | 2022-02-18 21:48:13 |
| MetricsDB | 4925.19 | 76.42 | 303 | 96.04 | 2022-08-07 08:58:34 |
| ProfilesDB | 2073.79 | 76.42 | 437 | 45.11 | 2021-07-13 11:52:46 |
| ProductsDB | 819.6 | 74.52 | 191 | 4.49 | 2022-05-20 22:56:53 |
| InventoryDB | 3309.55 | 92.55 | 195 | 72.71 | 2021-09-19 16:48:48 |
<end>Please transform the following PLAIN TEXT data into Yml:
Restaurant Name: Vegan Delight | Cuisine: Japanese | Location: Los Angeles | Rating: 4 | Price Range: $$$
Restaurant Name: Taco Town | Cuisine: Mexican | Location: Los Angeles | Rating: 2 | Price Range: $$
Restaurant Name: The Steakhouse | Cuisine: American | Location: Seattle | Rating: 2 | Price Range: $$$
<start>
- Cuisine: Japanese
  Location: Los Angeles
  Price Range: $$$
  Rating: 4
  Restaurant Name: Vegan Delight
- Cuisine: Mexican
  Location: Los Angeles
  Price Range: $$
  Rating: 2
  Restaurant Name: Taco Town
- Cuisine: American
  Location: Seattle
  Price Range: $$$
  Rating: 2
  Restaurant Name: The Steakhouse
<end>Please transform the following Json data into yml:
[
    {
        "Location": "New York",
        "Condition": "Stormy",
        "Temperature (C)": 21.7,
        "Humidity (%)": 82,
        "Wind Speed (km/h)": 24.5,
        "Day": "Tuesday"
    },
    {
        "Location": "Denver",
        "Condition": "Snowy",
        "Temperature (C)": 39.1,
        "Humidity (%)": 65,
        "Wind Speed (km/h)": 28.4,
        "Day": "Thursday"
    },
    {
        "Location": "Houston",
        "Condition": "Sunny",
        "Temperature (C)": 35.6,
        "Humidity (%)": 52,
        "Wind Speed (km/h)": 15.6,
        "Day": "Monday"
    },
    {
        "Location": "Miami",
        "Condition": "Snowy",
        "Temperature (C)": 11.6,
        "Humidity (%)": 69,
        "Wind Speed (km/h)": 11.1,
        "Day": "Thursday"
    },
    {
        "Location": "Los Angeles",
        "Condition": "Windy",
        "Temperature (C)": 9.9,
        "Humidity (%)": 84,
        "Wind Speed (km/h)": 21.1,
        "Day": "Saturday"
    },
    {
        "Location": "Denver",
        "Condition": "Rainy",
        "Temperature (C)": -1.4,
        "Humidity (%)": 84,
        "Wind Speed (km/h)": 0.3,
        "Day": "Saturday"
    }
]<start>
- Condition: Stormy
  Day: Tuesday
  Humidity (%): 82
  Location: New York
  Temperature (C): 21.7
  Wind Speed (km/h): 24.5
- Condition: Snowy
  Day: Thursday
  Humidity (%): 65
  Location: Denver
  Temperature (C): 39.1
  Wind Speed (km/h): 28.4
- Condition: Sunny
  Day: Monday
  Humidity (%): 52
  Location: Houston
  Temperature (C): 35.6
  Wind Speed (km/h): 15.6
- Condition: Snowy
  Day: Thursday
  Humidity (%): 69
  Location: Miami
  Temperature (C): 11.6
  Wind Speed (km/h): 11.1
- Condition: Windy
  Day: Saturday
  Humidity (%): 84
  Location: Los Angeles
  Temperature (C): 9.9
  Wind Speed (km/h): 21.1
- Condition: Rainy
  Day: Saturday
  Humidity (%): 84
  Location: Denver
  Temperature (C): -1.4
  Wind Speed (km/h): 0.3
<end>Please transform the following JSON data into Plain text:
[
    {
        "Location": "Hallway",
        "Battery Level (%)": 89.4,
        "Reading Value": -14.07
    },
    {
        "Location": "Bathroom",
        "Battery Level (%)": 55.0,
        "Reading Value": -36.96
    },
    {
        "Location": "Living Room",
        "Battery Level (%)": 58.9,
        "Reading Value": 74.86
    },
    {
        "Location": "Garden",
        "Battery Level (%)": 43.5,
        "Reading Value": 81.6
    },
    {
        "Location": "Kitchen",
        "Battery Level (%)": 58.9,
        "Reading Value": 54.33
    },
    {
        "Location": "Bedroom",
        "Battery Level (%)": 68.8,
        "Reading Value": 0.43
    }
]<start>
Location: Hallway | Battery Level (%): 89.4 | Reading Value: -14.07
Location: Bathroom | Battery Level (%): 55.0 | Reading Value: -36.96
Location: Living Room | Battery Level (%): 58.9 | Reading Value: 74.86
Location: Garden | Battery Level (%): 43.5 | Reading Value: 81.6
Location: Kitchen | Battery Level (%): 58.9 | Reading Value: 54.33
Location: Bedroom | Battery Level (%): 68.8 | Reading Value: 0.43
<end>Here's some json data, can you convert it to markdown?
[
    {
        "Database Name": "ProfilesDB",
        "Queries per Second": 2476.21,
        "Cache Hit Ratio (%)": 84.52,
        "Connection Count": 346,
        "Average Latency (ms)": 50.61,
        "Timestamp": "2023-12-13 14:58:25"
    },
    {
        "Database Name": "SalesDB",
        "Queries per Second": 2089.48,
        "Cache Hit Ratio (%)": 89.2,
        "Connection Count": 494,
        "Average Latency (ms)": 87.81,
        "Timestamp": "2021-12-18 19:08:50"
    },
    {
        "Database Name": "SessionsDB",
        "Queries per Second": 4642.36,
        "Cache Hit Ratio (%)": 79.74,
        "Connection Count": 326,
        "Average Latency (ms)": 96.34,
        "Timestamp": "2023-09-01 12:40:15"
    },
    {
        "Database Name": "ProductsDB",
        "Queries per Second": 3126.98,
        "Cache Hit Ratio (%)": 71.02,
        "Connection Count": 54,
        "Average Latency (ms)": 27.24,
        "Timestamp": "2021-08-13 21:59:22"
    },
    {
        "Database Name": "SalesDB",
        "Queries per Second": 604.02,
        "Cache Hit Ratio (%)": 78.08,
        "Connection Count": 326,
        "Average Latency (ms)": 14.79,
        "Timestamp": "2022-01-03 22:21:38"
    },
    {
        "Database Name": "SessionsDB",
        "Queries per Second": 129.77,
        "Cache Hit Ratio (%)": 84.5,
        "Connection Count": 487,
        "Average Latency (ms)": 12.91,
        "Timestamp": "2022-03-13 10:54:12"
    },
    {
        "Database Name": "ProductsDB",
        "Queries per Second": 4406.97,
        "Cache Hit Ratio (%)": 93.53,
        "Connection Count": 260,
        "Average Latency (ms)": 4.73,
        "Timestamp": "2022-02-23 08:57:24"
    },
    {
        "Database Name": "ProductsDB",
        "Queries per Second": 586.58,
        "Cache Hit Ratio (%)": 90.25,
        "Connection Count": 383,
        "Average Latency (ms)": 12.34,
        "Timestamp": "2021-09-22 16:16:40"
    },
    {
        "Database Name": "SalesDB",
        "Queries per Second": 1350.28,
        "Cache Hit Ratio (%)": 71.01,
        "Connection Count": 285,
        "Average Latency (ms)": 68.78,
        "Timestamp": "2021-12-08 10:47:06"
    },
    {
        "Database Name": "LogsDB",
        "Queries per Second": 773.89,
        "Cache Hit Ratio (%)": 71.01,
        "Connection Count": 222,
        "Average Latency (ms)": 72.33,
        "Timestamp": "2023-05-27 00:02:02"
    }
]<start>
| Database Name | Queries per Second | Cache Hit Ratio (%) | Connection Count | Average Latency (ms) | Timestamp |
| --- | --- | --- | --- | --- | --- |
| ProfilesDB | 2476.21 | 84.52 | 346 | 50.61 | 2023-12-13 14:58:25 |
| SalesDB | 2089.48 | 89.2 | 494 | 87.81 | 2021-12-18 19:08:50 |
| SessionsDB | 4642.36 | 79.74 | 326 | 96.34 | 2023-09-01 12:40:15 |
| ProductsDB | 3126.98 | 71.02 | 54 | 27.24 | 2021-08-13 21:59:22 |
| SalesDB | 604.02 | 78.08 | 326 | 14.79 | 2022-01-03 22:21:38 |
| SessionsDB | 129.77 | 84.5 | 487 | 12.91 | 2022-03-13 10:54:12 |
| ProductsDB | 4406.97 | 93.53 | 260 | 4.73 | 2022-02-23 08:57:24 |
| ProductsDB | 586.58 | 90.25 | 383 | 12.34 | 2021-09-22 16:16:40 |
| SalesDB | 1350.28 | 71.01 | 285 | 68.78 | 2021-12-08 10:47:06 |
| LogsDB | 773.89 | 71.01 | 222 | 72.33 | 2023-05-27 00:02:02 |
<end>Transform this Json structure to a Plain text format:
[
    {
        "Company": "BioLife",
        "Date": "2013-05-21",
        "Open Price": 485.43,
        "Volume": 1462461
    },
    {
        "Company": "FinanceTrust",
        "Date": "2016-01-23",
        "Open Price": 1294.36,
        "Volume": 3019256
    },
    {
        "Company": "RetailWorld",
        "Date": "2012-10-24",
        "Open Price": 1098.19,
        "Volume": 9829219
    },
    {
        "Company": "HealthGen",
        "Date": "2019-07-20",
        "Open Price": 620.89,
        "Volume": 9829219
    },
    {
        "Company": "AeroSystems",
        "Date": "2013-08-02",
        "Open Price": 1294.36,
        "Volume": 7945357
    },
    {
        "Company": "GreenEnergy",
        "Date": "2019-01-24",
        "Open Price": 1294.36,
        "Volume": 5466834
    },
    {
        "Company": "FinanceTrust",
        "Date": "2022-06-10",
        "Open Price": 1342.23,
        "Volume": 6213775
    },
    {
        "Company": "HealthGen",
        "Date": "2012-01-01",
        "Open Price": 927.1,
        "Volume": 6643759
    },
    {
        "Company": "HealthGen",
        "Date": "2022-01-20",
        "Open Price": 927.1,
        "Volume": 3793851
    }
]<start>
Company: BioLife | Date: 2013-05-21 | Open Price: 485.43 | Volume: 1462461
Company: FinanceTrust | Date: 2016-01-23 | Open Price: 1294.36 | Volume: 3019256
Company: RetailWorld | Date: 2012-10-24 | Open Price: 1098.19 | Volume: 9829219
Company: HealthGen | Date: 2019-07-20 | Open Price: 620.89 | Volume: 9829219
Company: AeroSystems | Date: 2013-08-02 | Open Price: 1294.36 | Volume: 7945357
Company: GreenEnergy | Date: 2019-01-24 | Open Price: 1294.36 | Volume: 5466834
Company: FinanceTrust | Date: 2022-06-10 | Open Price: 1342.23 | Volume: 6213775
Company: HealthGen | Date: 2012-01-01 | Open Price: 927.1 | Volume: 6643759
Company: HealthGen | Date: 2022-01-20 | Open Price: 927.1 | Volume: 3793851
<end>Can you change this Yaml into Plain text?
- Average Latency (ms): 78.17
  Cache Hit Ratio (%): 75.64
  Connection Count: 138
  Database Name: SalesDB
  Queries per Second: 2050.74
  Timestamp: '2023-01-20 10:38:52'
- Average Latency (ms): 55.37
  Cache Hit Ratio (%): 96.2
  Connection Count: 285
  Database Name: OrdersDB
  Queries per Second: 2679.74
  Timestamp: '2023-02-04 02:03:52'
- Average Latency (ms): 16.78
  Cache Hit Ratio (%): 80.45
  Connection Count: 76
  Database Name: AnalyticsDB
  Queries per Second: 1000.02
  Timestamp: '2021-12-06 07:46:57'
- Average Latency (ms): 29.47
  Cache Hit Ratio (%): 72.82
  Connection Count: 97
  Database Name: LogsDB
  Queries per Second: 1955.92
  Timestamp: '2021-10-26 17:45:03'
- Average Latency (ms): 41.32
  Cache Hit Ratio (%): 86.34
  Connection Count: 285
  Database Name: OrdersDB
  Queries per Second: 1130.35
  Timestamp: '2023-03-08 04:25:26'
- Average Latency (ms): 43.55
  Cache Hit Ratio (%): 73.58
  Connection Count: 41
  Database Name: MetricsDB
  Queries per Second: 3502.29
  Timestamp: '2022-10-04 03:30:02'
- Average Latency (ms): 89.17
  Cache Hit Ratio (%): 77.67
  Connection Count: 344
  Database Name: MetricsDB
  Queries per Second: 700.75
  Timestamp: '2022-11-10 13:07:45'
- Average Latency (ms): 7.06
  Cache Hit Ratio (%): 71.98
  Connection Count: 122
  Database Name: ProfilesDB
  Queries per Second: 2447.86
  Timestamp: '2021-07-20 14:17:55'
- Average Latency (ms): 21.1
  Cache Hit Ratio (%): 92.46
  Connection Count: 331
  Database Name: AnalyticsDB
  Queries per Second: 2565.78
  Timestamp: '2022-08-11 17:47:13'
- Average Latency (ms): 58.81
  Cache Hit Ratio (%): 84.36
  Connection Count: 183
  Database Name: UserDB
  Queries per Second: 803.63
  Timestamp: '2023-01-24 20:54:36'
<start>
Database Name: SalesDB | Queries per Second: 2050.74 | Cache Hit Ratio (%): 75.64 | Connection Count: 138 | Average Latency (ms): 78.17 | Timestamp: 2023-01-20 10:38:52
Database Name: OrdersDB | Queries per Second: 2679.74 | Cache Hit Ratio (%): 96.2 | Connection Count: 285 | Average Latency (ms): 55.37 | Timestamp: 2023-02-04 02:03:52
Database Name: AnalyticsDB | Queries per Second: 1000.02 | Cache Hit Ratio (%): 80.45 | Connection Count: 76 | Average Latency (ms): 16.78 | Timestamp: 2021-12-06 07:46:57
Database Name: LogsDB | Queries per Second: 1955.92 | Cache Hit Ratio (%): 72.82 | Connection Count: 97 | Average Latency (ms): 29.47 | Timestamp: 2021-10-26 17:45:03
Database Name: OrdersDB | Queries per Second: 1130.35 | Cache Hit Ratio (%): 86.34 | Connection Count: 285 | Average Latency (ms): 41.32 | Timestamp: 2023-03-08 04:25:26
Database Name: MetricsDB | Queries per Second: 3502.29 | Cache Hit Ratio (%): 73.58 | Connection Count: 41 | Average Latency (ms): 43.55 | Timestamp: 2022-10-04 03:30:02
Database Name: MetricsDB | Queries per Second: 700.75 | Cache Hit Ratio (%): 77.67 | Connection Count: 344 | Average Latency (ms): 89.17 | Timestamp: 2022-11-10 13:07:45
Database Name: ProfilesDB | Queries per Second: 2447.86 | Cache Hit Ratio (%): 71.98 | Connection Count: 122 | Average Latency (ms): 7.06 | Timestamp: 2021-07-20 14:17:55
Database Name: AnalyticsDB | Queries per Second: 2565.78 | Cache Hit Ratio (%): 92.46 | Connection Count: 331 | Average Latency (ms): 21.1 | Timestamp: 2022-08-11 17:47:13
Database Name: UserDB | Queries per Second: 803.63 | Cache Hit Ratio (%): 84.36 | Connection Count: 183 | Average Latency (ms): 58.81 | Timestamp: 2023-01-24 20:54:36
<end>Can you change this csv into Json?
Name,Birth Month
Scarlett,December
Lincoln,May
Edith,July
Greg,January
Lillian,September
<start>
[
    {
        "Name": "Scarlett",
        "Birth Month": "December"
    },
    {
        "Name": "Lincoln",
        "Birth Month": "May"
    },
    {
        "Name": "Edith",
        "Birth Month": "July"
    },
    {
        "Name": "Greg",
        "Birth Month": "January"
    },
    {
        "Name": "Lillian",
        "Birth Month": "September"
    }
]
<end>Can you change this json into markdown?
[
    {
        "Product Name": "Contraption",
        "Price": 362.85,
        "Stock Quantity": 482,
        "Category": "Household",
        "Supplier Name": "Globex"
    },
    {
        "Product Name": "Thingamajig",
        "Price": 112.49,
        "Stock Quantity": 236,
        "Category": "Household",
        "Supplier Name": "Umbrella Corp"
    },
    {
        "Product Name": "Whatchamacallit",
        "Price": 146.66,
        "Stock Quantity": 123,
        "Category": "Electronics",
        "Supplier Name": "Globex"
    },
    {
        "Product Name": "Gadget",
        "Price": 156.51,
        "Stock Quantity": 23,
        "Category": "Automotive",
        "Supplier Name": "ACME Corp"
    },
    {
        "Product Name": "Gadget",
        "Price": 68.84,
        "Stock Quantity": 212,
        "Category": "Household",
        "Supplier Name": "Wonka Industries"
    },
    {
        "Product Name": "Widget",
        "Price": 109.04,
        "Stock Quantity": 406,
        "Category": "Electronics",
        "Supplier Name": "Wayne Enterprises"
    },
    {
        "Product Name": "Doohickey",
        "Price": 168.29,
        "Stock Quantity": 100,
        "Category": "Automotive",
        "Supplier Name": "ACME Corp"
    },
    {
        "Product Name": "Gizmo",
        "Price": 162.67,
        "Stock Quantity": 285,
        "Category": "Electronics",
        "Supplier Name": "Globex"
    }
]<start>
| Product Name | Price | Stock Quantity | Category | Supplier Name |
| --- | --- | --- | --- | --- |
| Contraption | 362.85 | 482 | Household | Globex |
| Thingamajig | 112.49 | 236 | Household | Umbrella Corp |
| Whatchamacallit | 146.66 | 123 | Electronics | Globex |
| Gadget | 156.51 | 23 | Automotive | ACME Corp |
| Gadget | 68.84 | 212 | Household | Wonka Industries |
| Widget | 109.04 | 406 | Electronics | Wayne Enterprises |
| Doohickey | 168.29 | 100 | Automotive | ACME Corp |
| Gizmo | 162.67 | 285 | Electronics | Globex |
<end>Transform this yml structure to a csv format:
- Distance (miles): 2933.9
  Duration (hours): 20.0
  Fuel Used (gallons): 31.8
  Start Location: Miami
  Trip Name: Lakeside Retreat
- Distance (miles): 901.2
  Duration (hours): 69.6
  Fuel Used (gallons): 21.2
  Start Location: Houston
  Trip Name: Canyon Trek
- Distance (miles): 556.8
  Duration (hours): 33.6
  Fuel Used (gallons): 62.8
  Start Location: Chicago
  Trip Name: Desert Drive
- Distance (miles): 1508.4
  Duration (hours): 8.7
  Fuel Used (gallons): 10.4
  Start Location: Los Angeles
  Trip Name: Mountain Adventure
- Distance (miles): 321.7
  Duration (hours): 38.4
  Fuel Used (gallons): 22.7
  Start Location: New York
  Trip Name: City Explorer
- Distance (miles): 399.8
  Duration (hours): 21.7
  Fuel Used (gallons): 88.6
  Start Location: Houston
  Trip Name: Forest Journey
- Distance (miles): 2683.4
  Duration (hours): 17.5
  Fuel Used (gallons): 17.4
  Start Location: Phoenix
  Trip Name: Highway Odyssey
<start>
Trip Name,Start Location,Distance (miles),Duration (hours),Fuel Used (gallons)
Lakeside Retreat,Miami,2933.9,20.0,31.8
Canyon Trek,Houston,901.2,69.6,21.2
Desert Drive,Chicago,556.8,33.6,62.8
Mountain Adventure,Los Angeles,1508.4,8.7,10.4
City Explorer,New York,321.7,38.4,22.7
Forest Journey,Houston,399.8,21.7,88.6
Highway Odyssey,Phoenix,2683.4,17.5,17.4
<end>Can you change this YAML into PLAIN TEXT?
- Birth Month: January
  Name: Jamie
- Birth Month: February
  Name: Suzanne
- Birth Month: September
  Name: Piper
- Birth Month: April
  Name: Minnie
- Birth Month: August
  Name: Gregg
- Birth Month: September
  Name: Zoey
- Birth Month: June
  Name: Bianca
- Birth Month: December
  Name: Tina
- Birth Month: April
  Name: Dennis
<start>
Name: Jamie | Birth Month: January
Name: Suzanne | Birth Month: February
Name: Piper | Birth Month: September
Name: Minnie | Birth Month: April
Name: Gregg | Birth Month: August
Name: Zoey | Birth Month: September
Name: Bianca | Birth Month: June
Name: Tina | Birth Month: December
Name: Dennis | Birth Month: April
<end>Please transform the following Markdown data into YML:
| Name | Age | City | Income |
| --- | --- | --- | --- |
| Avery | 29 | Los Angeles | 115000 |
| Diego | 32 | Baltimore | 205000 |
| Cassidy | 21 | Washington | 335000 |
| Paige | 48 | Memphis | 345000 |
| Bryson | 39 | Columbus | 85000 |<start>
- Age: 29
  City: Los Angeles
  Income: 115000
  Name: Avery
- Age: 32
  City: Baltimore
  Income: 205000
  Name: Diego
- Age: 21
  City: Washington
  Income: 335000
  Name: Cassidy
- Age: 48
  City: Memphis
  Income: 345000
  Name: Paige
- Age: 39
  City: Columbus
  Income: 85000
  Name: Bryson
<end>Here's some yaml data, can you convert it to Json?
- Close Price: 451.39
  Date: '2014-08-17'
  Low Price: 451.39
  Open Price: 1010.87
- Close Price: 52.53
  Date: '2015-03-16'
  Low Price: 52.53
  Open Price: 582.65
- Close Price: 586.43
  Date: '2011-09-16'
  Low Price: 511.41
  Open Price: 511.41
- Close Price: 451.33
  Date: '2020-11-08'
  Low Price: 451.33
  Open Price: 817.09
- Close Price: 985.79
  Date: '2020-10-21'
  Low Price: 526.05
  Open Price: 526.05
- Close Price: 755.59
  Date: '2013-02-21'
  Low Price: 582.65
  Open Price: 582.65
- Close Price: 873.73
  Date: '2019-10-03'
  Low Price: 382.17
  Open Price: 382.17
- Close Price: 171.01
  Date: '2013-07-28'
  Low Price: 171.01
  Open Price: 646.64
- Close Price: 894.03
  Date: '2010-03-07'
  Low Price: 52.53
  Open Price: 511.41
<start>
[
    {
        "Date": "2014-08-17",
        "Open Price": 1010.87,
        "Close Price": 451.39,
        "Low Price": 451.39
    },
    {
        "Date": "2015-03-16",
        "Open Price": 582.65,
        "Close Price": 52.53,
        "Low Price": 52.53
    },
    {
        "Date": "2011-09-16",
        "Open Price": 511.41,
        "Close Price": 586.43,
        "Low Price": 511.41
    },
    {
        "Date": "2020-11-08",
        "Open Price": 817.09,
        "Close Price": 451.33,
        "Low Price": 451.33
    },
    {
        "Date": "2020-10-21",
        "Open Price": 526.05,
        "Close Price": 985.79,
        "Low Price": 526.05
    },
    {
        "Date": "2013-02-21",
        "Open Price": 582.65,
        "Close Price": 755.59,
        "Low Price": 582.65
    },
    {
        "Date": "2019-10-03",
        "Open Price": 382.17,
        "Close Price": 873.73,
        "Low Price": 382.17
    },
    {
        "Date": "2013-07-28",
        "Open Price": 646.64,
        "Close Price": 171.01,
        "Low Price": 171.01
    },
    {
        "Date": "2010-03-07",
        "Open Price": 511.41,
        "Close Price": 894.03,
        "Low Price": 52.53
    }
]
<end>Convert this plain text to yaml:
Title: Escape from Earth | Director: Orin Shadowalker | Genre: Comedy | Box Office Earnings (M): 116.78
Title: Edge of Infinity | Director: Orin Shadowalker | Genre: Sci-Fi | Box Office Earnings (M): 969.12
Title: Escape from Earth | Director: Lira Silverleaf | Genre: Sci-Fi | Box Office Earnings (M): 528.82
Title: The Endless Horizon | Director: Lira Silverleaf | Genre: Sci-Fi | Box Office Earnings (M): 705.26
<start>
- Box Office Earnings (M): 116.78
  Director: Orin Shadowalker
  Genre: Comedy
  Title: Escape from Earth
- Box Office Earnings (M): 969.12
  Director: Orin Shadowalker
  Genre: Sci-Fi
  Title: Edge of Infinity
- Box Office Earnings (M): 528.82
  Director: Lira Silverleaf
  Genre: Sci-Fi
  Title: Escape from Earth
- Box Office Earnings (M): 705.26
  Director: Lira Silverleaf
  Genre: Sci-Fi
  Title: The Endless Horizon
<end>Convert this markdown to CSV:
| Title | Author | Genre | Publication Year | Rating |
| --- | --- | --- | --- | --- |
| The Silent Grove | Draven Blackthorn | Mystery | 1967 | 4.5 |
| Tales of the Brave | Rowan Ashborne | Romance | 2002 | 4.7 |
| The Silent Grove | Orion Frostblade | Horror | 1997 | 1.1 |
| Shadows of Solitude | Draven Blackthorn | Horror | 2006 | 4.9 |
| Tales of the Brave | Elara Moonshadow | Fantasy | 1973 | 3.4 |
| The Last Sky | Isla Windrider | Horror | 1974 | 1.1 |
| The Crystal Key | Draven Blackthorn | Non-Fiction | 1981 | 1.6 |
| The Forgotten World | Elara Moonshadow | Non-Fiction | 1961 | 2.3 |
| Legends of the Rift | Draven Blackthorn | Mystery | 1979 | 3.7 |
| The Silent Grove | Rowan Ashborne | Non-Fiction | 1965 | 2.5 |<start>
Title,Author,Genre,Publication Year,Rating
The Silent Grove,Draven Blackthorn,Mystery,1967,4.5
Tales of the Brave,Rowan Ashborne,Romance,2002,4.7
The Silent Grove,Orion Frostblade,Horror,1997,1.1
Shadows of Solitude,Draven Blackthorn,Horror,2006,4.9
Tales of the Brave,Elara Moonshadow,Fantasy,1973,3.4
The Last Sky,Isla Windrider,Horror,1974,1.1
The Crystal Key,Draven Blackthorn,Non-Fiction,1981,1.6
The Forgotten World,Elara Moonshadow,Non-Fiction,1961,2.3
Legends of the Rift,Draven Blackthorn,Mystery,1979,3.7
The Silent Grove,Rowan Ashborne,Non-Fiction,1965,2.5
<end>Please transform the following MARKDOWN data into Json:
| Date | Open Price | High Price | Low Price |
| --- | --- | --- | --- |
| 2022-03-26 | 71.76 | 1004.35 | 71.76 |
| 2020-03-12 | 1377.09 | 1377.09 | 506.41 |
| 2014-01-16 | 1117.23 | 1117.23 | 240.47 |
| 2015-01-14 | 1075.74 | 1075.74 | 532.17 |<start>
[
    {
        "Date": "2022-03-26",
        "Open Price": 71.76,
        "High Price": 1004.35,
        "Low Price": 71.76
    },
    {
        "Date": "2020-03-12",
        "Open Price": 1377.09,
        "High Price": 1377.09,
        "Low Price": 506.41
    },
    {
        "Date": "2014-01-16",
        "Open Price": 1117.23,
        "High Price": 1117.23,
        "Low Price": 240.47
    },
    {
        "Date": "2015-01-14",
        "Open Price": 1075.74,
        "High Price": 1075.74,
        "Low Price": 532.17
    }
]
<end>Convert this JSON to Plain text:
[
    {
        "Date": "2010-08-27",
        "Open Price": 240.73,
        "Close Price": 69.69,
        "High Price": 1468.74,
        "Low Price": 69.69,
        "Volume": 4581096
    },
    {
        "Date": "2012-07-24",
        "Open Price": 1358.94,
        "Close Price": 553.42,
        "High Price": 1358.94,
        "Low Price": 553.42,
        "Volume": 6622259
    },
    {
        "Date": "2019-02-04",
        "Open Price": 1115.67,
        "Close Price": 1206.86,
        "High Price": 1206.86,
        "Low Price": 332.43,
        "Volume": 7906314
    },
    {
        "Date": "2014-06-25",
        "Open Price": 1113.55,
        "Close Price": 405.1,
        "High Price": 1113.55,
        "Low Price": 405.1,
        "Volume": 2626805
    },
    {
        "Date": "2016-11-14",
        "Open Price": 1088.6,
        "Close Price": 1474.36,
        "High Price": 1474.36,
        "Low Price": 1088.6,
        "Volume": 6332087
    },
    {
        "Date": "2019-07-16",
        "Open Price": 766.97,
        "Close Price": 1373.22,
        "High Price": 1373.22,
        "Low Price": 766.97,
        "Volume": 6247516
    },
    {
        "Date": "2016-02-04",
        "Open Price": 1296.93,
        "Close Price": 1190.03,
        "High Price": 1296.93,
        "Low Price": 1190.03,
        "Volume": 9334981
    }
]<start>
Date: 2010-08-27 | Open Price: 240.73 | Close Price: 69.69 | High Price: 1468.74 | Low Price: 69.69 | Volume: 4581096
Date: 2012-07-24 | Open Price: 1358.94 | Close Price: 553.42 | High Price: 1358.94 | Low Price: 553.42 | Volume: 6622259
Date: 2019-02-04 | Open Price: 1115.67 | Close Price: 1206.86 | High Price: 1206.86 | Low Price: 332.43 | Volume: 7906314
Date: 2014-06-25 | Open Price: 1113.55 | Close Price: 405.1 | High Price: 1113.55 | Low Price: 405.1 | Volume: 2626805
Date: 2016-11-14 | Open Price: 1088.6 | Close Price: 1474.36 | High Price: 1474.36 | Low Price: 1088.6 | Volume: 6332087
Date: 2019-07-16 | Open Price: 766.97 | Close Price: 1373.22 | High Price: 1373.22 | Low Price: 766.97 | Volume: 6247516
Date: 2016-02-04 | Open Price: 1296.93 | Close Price: 1190.03 | High Price: 1296.93 | Low Price: 1190.03 | Volume: 9334981
<end>Can you change this csv into plain text?
Product Name,Stock Quantity,Category
Apparatus,103,Toys
Apparatus,211,Sports
Instrument,435,Sports
Device,486,Sports
Contraption,110,Sports
<start>
Product Name: Apparatus | Stock Quantity: 103 | Category: Toys
Product Name: Apparatus | Stock Quantity: 211 | Category: Sports
Product Name: Instrument | Stock Quantity: 435 | Category: Sports
Product Name: Device | Stock Quantity: 486 | Category: Sports
Product Name: Contraption | Stock Quantity: 110 | Category: Sports
<end>Please transform the following yml data into plain text:
- Average Latency (ms): 88.13
  Cache Hit Ratio (%): 70.04
  Connection Count: 319
  Database Name: SessionsDB
  Queries per Second: 2114.55
  Timestamp: '2021-09-16 10:33:22'
- Average Latency (ms): 72.66
  Cache Hit Ratio (%): 85.55
  Connection Count: 247
  Database Name: SalesDB
  Queries per Second: 2721.11
  Timestamp: '2022-07-23 15:12:15'
- Average Latency (ms): 74.19
  Cache Hit Ratio (%): 95.51
  Connection Count: 127
  Database Name: ProfilesDB
  Queries per Second: 2527.87
  Timestamp: '2023-01-06 14:24:04'
- Average Latency (ms): 7.15
  Cache Hit Ratio (%): 78.15
  Connection Count: 367
  Database Name: UserDB
  Queries per Second: 727.32
  Timestamp: '2021-06-05 00:45:54'
- Average Latency (ms): 5.61
  Cache Hit Ratio (%): 85.1
  Connection Count: 237
  Database Name: ProductsDB
  Queries per Second: 4343.91
  Timestamp: '2021-05-25 06:53:57'
- Average Latency (ms): 47.05
  Cache Hit Ratio (%): 85.55
  Connection Count: 176
  Database Name: ProductsDB
  Queries per Second: 2195.12
  Timestamp: '2021-01-24 11:15:15'
- Average Latency (ms): 53.95
  Cache Hit Ratio (%): 92.07
  Connection Count: 69
  Database Name: ProfilesDB
  Queries per Second: 4029.56
  Timestamp: '2021-05-24 08:48:36'
- Average Latency (ms): 97.01
  Cache Hit Ratio (%): 79.96
  Connection Count: 367
  Database Name: InventoryDB
  Queries per Second: 993.14
  Timestamp: '2022-12-04 20:24:28'
- Average Latency (ms): 87.86
  Cache Hit Ratio (%): 76.27
  Connection Count: 103
  Database Name: LogsDB
  Queries per Second: 201.45
  Timestamp: '2022-08-05 20:54:38'
<start>
Database Name: SessionsDB | Queries per Second: 2114.55 | Cache Hit Ratio (%): 70.04 | Connection Count: 319 | Average Latency (ms): 88.13 | Timestamp: 2021-09-16 10:33:22
Database Name: SalesDB | Queries per Second: 2721.11 | Cache Hit Ratio (%): 85.55 | Connection Count: 247 | Average Latency (ms): 72.66 | Timestamp: 2022-07-23 15:12:15
Database Name: ProfilesDB | Queries per Second: 2527.87 | Cache Hit Ratio (%): 95.51 | Connection Count: 127 | Average Latency (ms): 74.19 | Timestamp: 2023-01-06 14:24:04
Database Name: UserDB | Queries per Second: 727.32 | Cache Hit Ratio (%): 78.15 | Connection Count: 367 | Average Latency (ms): 7.15 | Timestamp: 2021-06-05 00:45:54
Database Name: ProductsDB | Queries per Second: 4343.91 | Cache Hit Ratio (%): 85.1 | Connection Count: 237 | Average Latency (ms): 5.61 | Timestamp: 2021-05-25 06:53:57
Database Name: ProductsDB | Queries per Second: 2195.12 | Cache Hit Ratio (%): 85.55 | Connection Count: 176 | Average Latency (ms): 47.05 | Timestamp: 2021-01-24 11:15:15
Database Name: ProfilesDB | Queries per Second: 4029.56 | Cache Hit Ratio (%): 92.07 | Connection Count: 69 | Average Latency (ms): 53.95 | Timestamp: 2021-05-24 08:48:36
Database Name: InventoryDB | Queries per Second: 993.14 | Cache Hit Ratio (%): 79.96 | Connection Count: 367 | Average Latency (ms): 97.01 | Timestamp: 2022-12-04 20:24:28
Database Name: LogsDB | Queries per Second: 201.45 | Cache Hit Ratio (%): 76.27 | Connection Count: 103 | Average Latency (ms): 87.86 | Timestamp: 2022-08-05 20:54:38
<end>Convert this Csv to MARKDOWN:
Database Name,Queries per Second,Cache Hit Ratio (%),Connection Count,Average Latency (ms),Timestamp
AnalyticsDB,972.41,88.7,386,51.57,2023-10-15 07:26:46
ProfilesDB,2187.25,88.32,61,73.71,2023-01-20 00:34:20
InventoryDB,1130.81,87.22,401,20.47,2021-06-09 03:28:35
<start>
| Database Name | Queries per Second | Cache Hit Ratio (%) | Connection Count | Average Latency (ms) | Timestamp |
| --- | --- | --- | --- | --- | --- |
| AnalyticsDB | 972.41 | 88.7 | 386 | 51.57 | 2023-10-15 07:26:46 |
| ProfilesDB | 2187.25 | 88.32 | 61 | 73.71 | 2023-01-20 00:34:20 |
| InventoryDB | 1130.81 | 87.22 | 401 | 20.47 | 2021-06-09 03:28:35 |
<end>Convert this CSV to markdown:
Title,Publication Year,Rating
Whispers of the Abyss,1953,4.6
A Journey Through Time,1984,1.9
Tales of the Brave,2009,4.3
Tales of the Brave,2015,4.8
Echoes of Eternity,1967,3.4
The Silent Grove,1991,1.6
Echoes of Eternity,1958,2.8
Legends of the Rift,1977,4.5
The Silent Grove,1998,2.6
<start>
| Title | Publication Year | Rating |
| --- | --- | --- |
| Whispers of the Abyss | 1953 | 4.6 |
| A Journey Through Time | 1984 | 1.9 |
| Tales of the Brave | 2009 | 4.3 |
| Tales of the Brave | 2015 | 4.8 |
| Echoes of Eternity | 1967 | 3.4 |
| The Silent Grove | 1991 | 1.6 |
| Echoes of Eternity | 1958 | 2.8 |
| Legends of the Rift | 1977 | 4.5 |
| The Silent Grove | 1998 | 2.6 |
<end>Here's some PLAIN TEXT data, can you convert it to Markdown?
Restaurant Name: The Golden Spoon | Cuisine: Chinese | Location: Houston
Restaurant Name: The Steakhouse | Cuisine: Chinese | Location: New York
Restaurant Name: Vegan Delight | Cuisine: Italian | Location: Los Angeles
Restaurant Name: Burger Haven | Cuisine: Italian | Location: Chicago
Restaurant Name: Taco Town | Cuisine: Chinese | Location: Miami
Restaurant Name: Pasta Palace | Cuisine: Chinese | Location: New York
Restaurant Name: The Steakhouse | Cuisine: American | Location: New York
<start>
| Restaurant Name | Cuisine | Location |
| --- | --- | --- |
| The Golden Spoon | Chinese | Houston |
| The Steakhouse | Chinese | New York |
| Vegan Delight | Italian | Los Angeles |
| Burger Haven | Italian | Chicago |
| Taco Town | Chinese | Miami |
| Pasta Palace | Chinese | New York |
| The Steakhouse | American | New York |
<end>Transform this yml structure to a plain text format:
- Company: MediaGroup
  Date: '2014-12-10'
  High Price: 1026.37
  Low Price: 503.59
  Volume: 9984806
- Company: HealthGen
  Date: '2023-04-18'
  High Price: 1442.13
  Low Price: 14.41
  Volume: 3110169
- Company: GreenEnergy
  Date: '2023-09-09'
  High Price: 1369.37
  Low Price: 157.07
  Volume: 7653813
<start>
Company: MediaGroup | Date: 2014-12-10 | High Price: 1026.37 | Low Price: 503.59 | Volume: 9984806
Company: HealthGen | Date: 2023-04-18 | High Price: 1442.13 | Low Price: 14.41 | Volume: 3110169
Company: GreenEnergy | Date: 2023-09-09 | High Price: 1369.37 | Low Price: 157.07 | Volume: 7653813
<end>Here's some PLAIN TEXT data, can you convert it to JSON?
Location: Denver | Condition: Windy | Temperature (C): 29.8 | Humidity (%): 91 | Day: Saturday
Location: Houston | Condition: Stormy | Temperature (C): 9.5 | Humidity (%): 66 | Day: Saturday
Location: Seattle | Condition: Foggy | Temperature (C): 9.3 | Humidity (%): 90 | Day: Monday
Location: Los Angeles | Condition: Stormy | Temperature (C): 16.4 | Humidity (%): 75 | Day: Sunday
Location: Houston | Condition: Cloudy | Temperature (C): 15.2 | Humidity (%): 62 | Day: Friday
<start>
[
    {
        "Location": "Denver",
        "Condition": "Windy",
        "Temperature (C)": 29.8,
        "Humidity (%)": 91,
        "Day": "Saturday"
    },
    {
        "Location": "Houston",
        "Condition": "Stormy",
        "Temperature (C)": 9.5,
        "Humidity (%)": 66,
        "Day": "Saturday"
    },
    {
        "Location": "Seattle",
        "Condition": "Foggy",
        "Temperature (C)": 9.3,
        "Humidity (%)": 90,
        "Day": "Monday"
    },
    {
        "Location": "Los Angeles",
        "Condition": "Stormy",
        "Temperature (C)": 16.4,
        "Humidity (%)": 75,
        "Day": "Sunday"
    },
    {
        "Location": "Houston",
        "Condition": "Cloudy",
        "Temperature (C)": 15.2,
        "Humidity (%)": 62,
        "Day": "Friday"
    }
]
<end>Can you change this JSON into plain text?
[
    {
        "Title": "Shadows of Solitude",
        "Publication Year": 1970
    },
    {
        "Title": "The Forgotten World",
        "Publication Year": 1991
    },
    {
        "Title": "Shadows of Solitude",
        "Publication Year": 1970
    },
    {
        "Title": "The Last Sky",
        "Publication Year": 2008
    },
    {
        "Title": "Legends of the Rift",
        "Publication Year": 1975
    },
    {
        "Title": "Tales of the Brave",
        "Publication Year": 2002
    },
    {
        "Title": "The Last Sky",
        "Publication Year": 1978
    },
    {
        "Title": "The Last Sky",
        "Publication Year": 1986
    }
]<start>
Title: Shadows of Solitude | Publication Year: 1970
Title: The Forgotten World | Publication Year: 1991
Title: Shadows of Solitude | Publication Year: 1970
Title: The Last Sky | Publication Year: 2008
Title: Legends of the Rift | Publication Year: 1975
Title: Tales of the Brave | Publication Year: 2002
Title: The Last Sky | Publication Year: 1978
Title: The Last Sky | Publication Year: 1986
<end>Transform this Yaml structure to a csv format:
- Cuisine: Chinese
  Location: New York
  Price Range: $
  Rating: 4
  Restaurant Name: Curry Corner
- Cuisine: Indian
  Location: Phoenix
  Price Range: $
  Rating: 2
  Restaurant Name: The Steakhouse
- Cuisine: Mediterranean
  Location: New York
  Price Range: $
  Rating: 2
  Restaurant Name: Taco Town
- Cuisine: Mexican
  Location: Houston
  Price Range: $$
  Rating: 2
  Restaurant Name: The Golden Spoon
- Cuisine: Mediterranean
  Location: San Francisco
  Price Range: $$$
  Rating: 2
  Restaurant Name: Pizza Planet
- Cuisine: Indian
  Location: Los Angeles
  Price Range: $$
  Rating: 4
  Restaurant Name: Pasta Palace
<start>
Restaurant Name,Cuisine,Location,Rating,Price Range
Curry Corner,Chinese,New York,4,$
The Steakhouse,Indian,Phoenix,2,$
Taco Town,Mediterranean,New York,2,$
The Golden Spoon,Mexican,Houston,2,$$
Pizza Planet,Mediterranean,San Francisco,2,$$$
Pasta Palace,Indian,Los Angeles,4,$$
<end>Here's some YML data, can you convert it to Markdown?
- Condition: Stormy
  Day: Monday
  Humidity (%): 31
  Location: Chicago
  Temperature (C): -2.0
  Wind Speed (km/h): 27.5
- Condition: Rainy
  Day: Friday
  Humidity (%): 73
  Location: Miami
  Temperature (C): 8.1
  Wind Speed (km/h): 18.5
- Condition: Rainy
  Day: Sunday
  Humidity (%): 27
  Location: Denver
  Temperature (C): 23.6
  Wind Speed (km/h): 13.4
- Condition: Foggy
  Day: Tuesday
  Humidity (%): 68
  Location: Denver
  Temperature (C): -2.9
  Wind Speed (km/h): 6.3
- Condition: Stormy
  Day: Tuesday
  Humidity (%): 42
  Location: Houston
  Temperature (C): 38.7
  Wind Speed (km/h): 6.3
- Condition: Stormy
  Day: Wednesday
  Humidity (%): 78
  Location: Miami
  Temperature (C): -7.8
  Wind Speed (km/h): 1.8
- Condition: Cloudy
  Day: Sunday
  Humidity (%): 37
  Location: Los Angeles
  Temperature (C): 32.3
  Wind Speed (km/h): 22.4
- Condition: Cloudy
  Day: Saturday
  Humidity (%): 59
  Location: Denver
  Temperature (C): -4.6
  Wind Speed (km/h): 7.6
- Condition: Foggy
  Day: Friday
  Humidity (%): 56
  Location: Los Angeles
  Temperature (C): 33.7
  Wind Speed (km/h): 17.8
<start>
| Location | Condition | Temperature (C) | Humidity (%) | Wind Speed (km/h) | Day |
| --- | --- | --- | --- | --- | --- |
| Chicago | Stormy | -2.0 | 31 | 27.5 | Monday |
| Miami | Rainy | 8.1 | 73 | 18.5 | Friday |
| Denver | Rainy | 23.6 | 27 | 13.4 | Sunday |
| Denver | Foggy | -2.9 | 68 | 6.3 | Tuesday |
| Houston | Stormy | 38.7 | 42 | 6.3 | Tuesday |
| Miami | Stormy | -7.8 | 78 | 1.8 | Wednesday |
| Los Angeles | Cloudy | 32.3 | 37 | 22.4 | Sunday |
| Denver | Cloudy | -4.6 | 59 | 7.6 | Saturday |
| Los Angeles | Foggy | 33.7 | 56 | 17.8 | Friday |
<end>Can you change this Markdown into yml?
| Age | Birth Month | City |
| --- | --- | --- |
| 23 | April | Fort Worth |
| 44 | March | Columbus |
| 28 | January | Milwaukee |
| 56 | September | Memphis |
| 30 | June | Oklahoma City |
| 29 | March | New York |
| 31 | September | Los Angeles |
| 45 | December | Las Vegas |
| 55 | November | Austin |<start>
- Age: 23
  Birth Month: April
  City: Fort Worth
- Age: 44
  Birth Month: March
  City: Columbus
- Age: 28
  Birth Month: January
  City: Milwaukee
- Age: 56
  Birth Month: September
  City: Memphis
- Age: 30
  Birth Month: June
  City: Oklahoma City
- Age: 29
  Birth Month: March
  City: New York
- Age: 31
  Birth Month: September
  City: Los Angeles
- Age: 45
  Birth Month: December
  City: Las Vegas
- Age: 55
  Birth Month: November
  City: Austin
<end>Please transform the following plain text data into MARKDOWN:
Title: The Forgotten World | Genre: Fantasy | Publication Year: 2002
Title: Echoes of Eternity | Genre: Thriller | Publication Year: 1953
Title: Shadows of Solitude | Genre: Mystery | Publication Year: 2021
Title: Whispers of the Abyss | Genre: Romance | Publication Year: 1958
Title: A Journey Through Time | Genre: Mystery | Publication Year: 1953
<start>
| Title | Genre | Publication Year |
| --- | --- | --- |
| The Forgotten World | Fantasy | 2002 |
| Echoes of Eternity | Thriller | 1953 |
| Shadows of Solitude | Mystery | 2021 |
| Whispers of the Abyss | Romance | 1958 |
| A Journey Through Time | Mystery | 1953 |
<end>Transform this Markdown structure to a PLAIN TEXT format:
| Device ID | Device Type | Location | Battery Level (%) | Reading Value | Timestamp |
| --- | --- | --- | --- | --- | --- |
| device-0093 | Light Sensor | Garden | 46.2 | 74.08 | 2023-01-13 19:03:10 |
| device-0038 | Motion Detector | Office | 66.7 | 39.7 | 2021-10-09 10:39:47 |
| device-0096 | Motion Detector | Bathroom | 85.2 | -6.11 | 2021-11-03 18:46:40 |
| device-0076 | Light Sensor | Garage | 62.0 | -38.4 | 2023-12-07 00:15:48 |
| device-0018 | Humidity Sensor | Living Room | 69.0 | -4.99 | 2023-07-22 09:15:39 |
| device-0043 | Light Sensor | Office | 23.8 | 81.77 | 2022-08-13 15:13:16 |
| device-0080 | Light Sensor | Garden | 14.6 | -18.54 | 2021-04-15 23:49:29 |
| device-0070 | Temperature Sensor | Office | 83.9 | 30.43 | 2022-05-12 03:54:50 |
| device-0065 | Humidity Sensor | Garage | 15.0 | 3.39 | 2021-05-13 08:05:00 |<start>
Device ID: device-0093 | Device Type: Light Sensor | Location: Garden | Battery Level (%): 46.2 | Reading Value: 74.08 | Timestamp: 2023-01-13 19:03:10
Device ID: device-0038 | Device Type: Motion Detector | Location: Office | Battery Level (%): 66.7 | Reading Value: 39.7 | Timestamp: 2021-10-09 10:39:47
Device ID: device-0096 | Device Type: Motion Detector | Location: Bathroom | Battery Level (%): 85.2 | Reading Value: -6.11 | Timestamp: 2021-11-03 18:46:40
Device ID: device-0076 | Device Type: Light Sensor | Location: Garage | Battery Level (%): 62.0 | Reading Value: -38.4 | Timestamp: 2023-12-07 00:15:48
Device ID: device-0018 | Device Type: Humidity Sensor | Location: Living Room | Battery Level (%): 69.0 | Reading Value: -4.99 | Timestamp: 2023-07-22 09:15:39
Device ID: device-0043 | Device Type: Light Sensor | Location: Office | Battery Level (%): 23.8 | Reading Value: 81.77 | Timestamp: 2022-08-13 15:13:16
Device ID: device-0080 | Device Type: Light Sensor | Location: Garden | Battery Level (%): 14.6 | Reading Value: -18.54 | Timestamp: 2021-04-15 23:49:29
Device ID: device-0070 | Device Type: Temperature Sensor | Location: Office | Battery Level (%): 83.9 | Reading Value: 30.43 | Timestamp: 2022-05-12 03:54:50
Device ID: device-0065 | Device Type: Humidity Sensor | Location: Garage | Battery Level (%): 15.0 | Reading Value: 3.39 | Timestamp: 2021-05-13 08:05:00
<end>Please transform the following csv data into Markdown:
Database Name,Queries per Second,Cache Hit Ratio (%),Average Latency (ms),Timestamp
SessionsDB,2019.72,74.52,23.99,2021-01-12 20:04:10
ProductsDB,914.7,82.64,46.06,2023-08-16 08:26:00
SalesDB,2673.63,76.79,55.46,2023-12-15 15:50:24
SalesDB,3800.29,91.09,30.9,2023-11-03 08:10:25
<start>
| Database Name | Queries per Second | Cache Hit Ratio (%) | Average Latency (ms) | Timestamp |
| --- | --- | --- | --- | --- |
| SessionsDB | 2019.72 | 74.52 | 23.99 | 2021-01-12 20:04:10 |
| ProductsDB | 914.7 | 82.64 | 46.06 | 2023-08-16 08:26:00 |
| SalesDB | 2673.63 | 76.79 | 55.46 | 2023-12-15 15:50:24 |
| SalesDB | 3800.29 | 91.09 | 30.9 | 2023-11-03 08:10:25 |
<end>Convert this Plain text to yaml:
Company: AutoDrive | Sector: Aerospace | Market Cap: Small Cap | Annual Revenue (B): 247.45 | Quarter: Q4
Company: TechCorp | Sector: Aerospace | Market Cap: Mega Cap | Annual Revenue (B): 442.29 | Quarter: Q3
Company: Foodies | Sector: Retail | Market Cap: Small Cap | Annual Revenue (B): 411.06 | Quarter: Q3
Company: BioPharm | Sector: Automotive | Market Cap: Mid Cap | Annual Revenue (B): 233.01 | Quarter: Q2
<start>
- Annual Revenue (B): 247.45
  Company: AutoDrive
  Market Cap: Small Cap
  Quarter: Q4
  Sector: Aerospace
- Annual Revenue (B): 442.29
  Company: TechCorp
  Market Cap: Mega Cap
  Quarter: Q3
  Sector: Aerospace
- Annual Revenue (B): 411.06
  Company: Foodies
  Market Cap: Small Cap
  Quarter: Q3
  Sector: Retail
- Annual Revenue (B): 233.01
  Company: BioPharm
  Market Cap: Mid Cap
  Quarter: Q2
  Sector: Automotive
<end>Please transform the following Json data into MARKDOWN:
[
    {
        "Genre": "Action",
        "Release Year": 1972,
        "Box Office Earnings (M)": 621.48
    },
    {
        "Genre": "Sci-Fi",
        "Release Year": 2011,
        "Box Office Earnings (M)": 661.45
    },
    {
        "Genre": "Adventure",
        "Release Year": 2022,
        "Box Office Earnings (M)": 667.13
    },
    {
        "Genre": "Drama",
        "Release Year": 1983,
        "Box Office Earnings (M)": 942.1
    },
    {
        "Genre": "Adventure",
        "Release Year": 2011,
        "Box Office Earnings (M)": 862.64
    },
    {
        "Genre": "Comedy",
        "Release Year": 1987,
        "Box Office Earnings (M)": 977.34
    }
]<start>
| Genre | Release Year | Box Office Earnings (M) |
| --- | --- | --- |
| Action | 1972 | 621.48 |
| Sci-Fi | 2011 | 661.45 |
| Adventure | 2022 | 667.13 |
| Drama | 1983 | 942.1 |
| Adventure | 2011 | 862.64 |
| Comedy | 1987 | 977.34 |
<end>Can you change this Csv into plain text?
Device ID,Device Type,Location,Battery Level (%),Reading Value
device-0059,Humidity Sensor,Garage,90.2,-36.68
device-0064,Motion Detector,Bedroom,42.8,32.94
device-0089,Motion Detector,Bedroom,97.6,52.75
device-0087,Pressure Sensor,Garage,38.1,-20.68
device-0086,Humidity Sensor,Bedroom,81.6,65.86
<start>
Device ID: device-0059 | Device Type: Humidity Sensor | Location: Garage | Battery Level (%): 90.2 | Reading Value: -36.68
Device ID: device-0064 | Device Type: Motion Detector | Location: Bedroom | Battery Level (%): 42.8 | Reading Value: 32.94
Device ID: device-0089 | Device Type: Motion Detector | Location: Bedroom | Battery Level (%): 97.6 | Reading Value: 52.75
Device ID: device-0087 | Device Type: Pressure Sensor | Location: Garage | Battery Level (%): 38.1 | Reading Value: -20.68
Device ID: device-0086 | Device Type: Humidity Sensor | Location: Bedroom | Battery Level (%): 81.6 | Reading Value: 65.86
<end>Please transform the following Json data into csv:
[
    {
        "Device Type": "Temperature Sensor",
        "Battery Level (%)": 39.3,
        "Timestamp": "2022-10-27 16:57:50"
    },
    {
        "Device Type": "Motion Detector",
        "Battery Level (%)": 25.3,
        "Timestamp": "2022-07-04 00:58:48"
    },
    {
        "Device Type": "Humidity Sensor",
        "Battery Level (%)": 33.5,
        "Timestamp": "2021-02-07 12:53:51"
    },
    {
        "Device Type": "Light Sensor",
        "Battery Level (%)": 23.0,
        "Timestamp": "2023-01-27 02:56:20"
    },
    {
        "Device Type": "Pressure Sensor",
        "Battery Level (%)": 71.1,
        "Timestamp": "2022-06-10 22:06:00"
    },
    {
        "Device Type": "Motion Detector",
        "Battery Level (%)": 16.8,
        "Timestamp": "2022-12-20 15:58:23"
    },
    {
        "Device Type": "Light Sensor",
        "Battery Level (%)": 85.1,
        "Timestamp": "2022-12-26 01:57:21"
    },
    {
        "Device Type": "Temperature Sensor",
        "Battery Level (%)": 89.8,
        "Timestamp": "2022-02-16 02:57:59"
    }
]<start>
Device Type,Battery Level (%),Timestamp
Temperature Sensor,39.3,2022-10-27 16:57:50
Motion Detector,25.3,2022-07-04 00:58:48
Humidity Sensor,33.5,2021-02-07 12:53:51
Light Sensor,23.0,2023-01-27 02:56:20
Pressure Sensor,71.1,2022-06-10 22:06:00
Motion Detector,16.8,2022-12-20 15:58:23
Light Sensor,85.1,2022-12-26 01:57:21
Temperature Sensor,89.8,2022-02-16 02:57:59
<end>Can you change this Csv into plain text?
Trip Name,Start Location,End Location,Duration (hours),Fuel Used (gallons)
Historic Route,Houston,Chicago,58.0,61.0
Canyon Trek,Los Angeles,Houston,32.7,48.7
Valley Voyage,Houston,Chicago,35.9,16.5
Highway Odyssey,Phoenix,Miami,50.6,41.3
Mountain Adventure,San Francisco,Chicago,7.0,27.3
Desert Drive,Denver,San Francisco,33.6,93.8
Desert Drive,Houston,New York,34.2,9.5
Historic Route,Los Angeles,New York,33.0,9.5
City Explorer,Chicago,San Francisco,33.0,16.7
Forest Journey,Denver,Los Angeles,19.4,44.0
<start>
Trip Name: Historic Route | Start Location: Houston | End Location: Chicago | Duration (hours): 58.0 | Fuel Used (gallons): 61.0
Trip Name: Canyon Trek | Start Location: Los Angeles | End Location: Houston | Duration (hours): 32.7 | Fuel Used (gallons): 48.7
Trip Name: Valley Voyage | Start Location: Houston | End Location: Chicago | Duration (hours): 35.9 | Fuel Used (gallons): 16.5
Trip Name: Highway Odyssey | Start Location: Phoenix | End Location: Miami | Duration (hours): 50.6 | Fuel Used (gallons): 41.3
Trip Name: Mountain Adventure | Start Location: San Francisco | End Location: Chicago | Duration (hours): 7.0 | Fuel Used (gallons): 27.3
Trip Name: Desert Drive | Start Location: Denver | End Location: San Francisco | Duration (hours): 33.6 | Fuel Used (gallons): 93.8
Trip Name: Desert Drive | Start Location: Houston | End Location: New York | Duration (hours): 34.2 | Fuel Used (gallons): 9.5
Trip Name: Historic Route | Start Location: Los Angeles | End Location: New York | Duration (hours): 33.0 | Fuel Used (gallons): 9.5
Trip Name: City Explorer | Start Location: Chicago | End Location: San Francisco | Duration (hours): 33.0 | Fuel Used (gallons): 16.7
Trip Name: Forest Journey | Start Location: Denver | End Location: Los Angeles | Duration (hours): 19.4 | Fuel Used (gallons): 44.0
<end>Convert this Markdown to json:
| Sector | Market Cap | Stock Price | Annual Revenue (B) | Quarter |
| --- | --- | --- | --- | --- |
| Automotive | Mid Cap | 530.55 | 389.03 | Q2 |
| Technology | Small Cap | 445.0 | 300.58 | Q1 |
| Technology | Mega Cap | 473.47 | 407.55 | Q1 |
| Retail | Large Cap | 109.49 | 438.27 | Q4 |
| Energy | Mid Cap | 158.61 | 372.19 | Q2 |
| Energy | Large Cap | 445.0 | 398.18 | Q4 |
| Energy | Mid Cap | 875.41 | 79.99 | Q3 |
| Automotive | Large Cap | 834.06 | 460.12 | Q4 |
| Aerospace | Large Cap | 461.57 | 372.19 | Q1 |
| Retail | Large Cap | 70.19 | 421.31 | Q4 |<start>
[
    {
        "Sector": "Automotive",
        "Market Cap": "Mid Cap",
        "Stock Price": 530.55,
        "Annual Revenue (B)": 389.03,
        "Quarter": "Q2"
    },
    {
        "Sector": "Technology",
        "Market Cap": "Small Cap",
        "Stock Price": 445.0,
        "Annual Revenue (B)": 300.58,
        "Quarter": "Q1"
    },
    {
        "Sector": "Technology",
        "Market Cap": "Mega Cap",
        "Stock Price": 473.47,
        "Annual Revenue (B)": 407.55,
        "Quarter": "Q1"
    },
    {
        "Sector": "Retail",
        "Market Cap": "Large Cap",
        "Stock Price": 109.49,
        "Annual Revenue (B)": 438.27,
        "Quarter": "Q4"
    },
    {
        "Sector": "Energy",
        "Market Cap": "Mid Cap",
        "Stock Price": 158.61,
        "Annual Revenue (B)": 372.19,
        "Quarter": "Q2"
    },
    {
        "Sector": "Energy",
        "Market Cap": "Large Cap",
        "Stock Price": 445.0,
        "Annual Revenue (B)": 398.18,
        "Quarter": "Q4"
    },
    {
        "Sector": "Energy",
        "Market Cap": "Mid Cap",
        "Stock Price": 875.41,
        "Annual Revenue (B)": 79.99,
        "Quarter": "Q3"
    },
    {
        "Sector": "Automotive",
        "Market Cap": "Large Cap",
        "Stock Price": 834.06,
        "Annual Revenue (B)": 460.12,
        "Quarter": "Q4"
    },
    {
        "Sector": "Aerospace",
        "Market Cap": "Large Cap",
        "Stock Price": 461.57,
        "Annual Revenue (B)": 372.19,
        "Quarter": "Q1"
    },
    {
        "Sector": "Retail",
        "Market Cap": "Large Cap",
        "Stock Price": 70.19,
        "Annual Revenue (B)": 421.31,
        "Quarter": "Q4"
    }
]
<end>Can you change this MARKDOWN into yaml?
| Device ID | Device Type | Location | Battery Level (%) | Reading Value | Timestamp |
| --- | --- | --- | --- | --- | --- |
| device-0005 | Light Sensor | Living Room | 34.8 | -29.15 | 2022-03-21 19:36:52 |
| device-0083 | Motion Detector | Office | 22.0 | 34.63 | 2021-10-27 14:02:53 |
| device-0066 | Temperature Sensor | Garden | 10.4 | -11.16 | 2023-11-06 15:52:35 |
| device-0020 | Light Sensor | Bathroom | 33.3 | -3.15 | 2023-06-28 23:23:40 |
| device-0050 | Humidity Sensor | Garden | 13.7 | 23.25 | 2023-01-04 15:32:30 |
| device-0018 | Temperature Sensor | Hallway | 91.9 | 51.61 | 2021-02-16 04:16:08 |
| device-0057 | Humidity Sensor | Bedroom | 50.2 | -11.16 | 2023-07-24 23:39:37 |
| device-0070 | Temperature Sensor | Kitchen | 28.8 | -34.31 | 2023-07-11 10:29:13 |
| device-0019 | Motion Detector | Bedroom | 28.8 | 58.4 | 2023-08-05 15:46:08 |
| device-0072 | Humidity Sensor | Garage | 42.8 | 34.74 | 2022-02-02 11:27:38 |<start>
- Battery Level (%): 34.8
  Device ID: device-0005
  Device Type: Light Sensor
  Location: Living Room
  Reading Value: -29.15
  Timestamp: '2022-03-21 19:36:52'
- Battery Level (%): 22.0
  Device ID: device-0083
  Device Type: Motion Detector
  Location: Office
  Reading Value: 34.63
  Timestamp: '2021-10-27 14:02:53'
- Battery Level (%): 10.4
  Device ID: device-0066
  Device Type: Temperature Sensor
  Location: Garden
  Reading Value: -11.16
  Timestamp: '2023-11-06 15:52:35'
- Battery Level (%): 33.3
  Device ID: device-0020
  Device Type: Light Sensor
  Location: Bathroom
  Reading Value: -3.15
  Timestamp: '2023-06-28 23:23:40'
- Battery Level (%): 13.7
  Device ID: device-0050
  Device Type: Humidity Sensor
  Location: Garden
  Reading Value: 23.25
  Timestamp: '2023-01-04 15:32:30'
- Battery Level (%): 91.9
  Device ID: device-0018
  Device Type: Temperature Sensor
  Location: Hallway
  Reading Value: 51.61
  Timestamp: '2021-02-16 04:16:08'
- Battery Level (%): 50.2
  Device ID: device-0057
  Device Type: Humidity Sensor
  Location: Bedroom
  Reading Value: -11.16
  Timestamp: '2023-07-24 23:39:37'
- Battery Level (%): 28.8
  Device ID: device-0070
  Device Type: Temperature Sensor
  Location: Kitchen
  Reading Value: -34.31
  Timestamp: '2023-07-11 10:29:13'
- Battery Level (%): 28.8
  Device ID: device-0019
  Device Type: Motion Detector
  Location: Bedroom
  Reading Value: 58.4
  Timestamp: '2023-08-05 15:46:08'
- Battery Level (%): 42.8
  Device ID: device-0072
  Device Type: Humidity Sensor
  Location: Garage
  Reading Value: 34.74
  Timestamp: '2022-02-02 11:27:38'
<end>Please transform the following csv data into yaml:
Product Name,Stock Quantity,Category
Whatchamacallit,479,Automotive
Apparatus,186,Electronics
Whatchamacallit,274,Household
Gizmo,401,Automotive
Whatchamacallit,353,Sports
Thingamajig,492,Household
Thingamajig,219,Sports
Gadget,48,Automotive
<start>
- Category: Automotive
  Product Name: Whatchamacallit
  Stock Quantity: 479
- Category: Electronics
  Product Name: Apparatus
  Stock Quantity: 186
- Category: Household
  Product Name: Whatchamacallit
  Stock Quantity: 274
- Category: Automotive
  Product Name: Gizmo
  Stock Quantity: 401
- Category: Sports
  Product Name: Whatchamacallit
  Stock Quantity: 353
- Category: Household
  Product Name: Thingamajig
  Stock Quantity: 492
- Category: Sports
  Product Name: Thingamajig
  Stock Quantity: 219
- Category: Automotive
  Product Name: Gadget
  Stock Quantity: 48
<end>Transform this yml structure to a plain text format:
- Condition: Rainy
  Day: Wednesday
  Temperature (C): 31.8
  Wind Speed (km/h): 9.6
- Condition: Rainy
  Day: Wednesday
  Temperature (C): -4.7
  Wind Speed (km/h): 4.4
- Condition: Snowy
  Day: Saturday
  Temperature (C): 0.4
  Wind Speed (km/h): 23.1
- Condition: Stormy
  Day: Monday
  Temperature (C): 34.4
  Wind Speed (km/h): 11.3
- Condition: Stormy
  Day: Thursday
  Temperature (C): 21.2
  Wind Speed (km/h): 23.0
- Condition: Rainy
  Day: Tuesday
  Temperature (C): 23.8
  Wind Speed (km/h): 16.4
- Condition: Sunny
  Day: Sunday
  Temperature (C): -6.1
  Wind Speed (km/h): 20.1
- Condition: Foggy
  Day: Sunday
  Temperature (C): 20.9
  Wind Speed (km/h): 16.4
- Condition: Stormy
  Day: Sunday
  Temperature (C): -9.5
  Wind Speed (km/h): 18.0
<start>
Condition: Rainy | Temperature (C): 31.8 | Wind Speed (km/h): 9.6 | Day: Wednesday
Condition: Rainy | Temperature (C): -4.7 | Wind Speed (km/h): 4.4 | Day: Wednesday
Condition: Snowy | Temperature (C): 0.4 | Wind Speed (km/h): 23.1 | Day: Saturday
Condition: Stormy | Temperature (C): 34.4 | Wind Speed (km/h): 11.3 | Day: Monday
Condition: Stormy | Temperature (C): 21.2 | Wind Speed (km/h): 23.0 | Day: Thursday
Condition: Rainy | Temperature (C): 23.8 | Wind Speed (km/h): 16.4 | Day: Tuesday
Condition: Sunny | Temperature (C): -6.1 | Wind Speed (km/h): 20.1 | Day: Sunday
Condition: Foggy | Temperature (C): 20.9 | Wind Speed (km/h): 16.4 | Day: Sunday
Condition: Stormy | Temperature (C): -9.5 | Wind Speed (km/h): 18.0 | Day: Sunday
<end>Convert this Yml to Markdown:
- Cuisine: Japanese
  Location: New York
  Price Range: $
  Rating: 5
  Restaurant Name: BBQ Barn
- Cuisine: French
  Location: New York
  Price Range: $$
  Rating: 5
  Restaurant Name: Pizza Planet
- Cuisine: Mexican
  Location: Seattle
  Price Range: $$$$
  Rating: 1
  Restaurant Name: Taco Town
- Cuisine: Chinese
  Location: Phoenix
  Price Range: $
  Rating: 2
  Restaurant Name: The Steakhouse
- Cuisine: French
  Location: Los Angeles
  Price Range: $$$$$
  Rating: 4
  Restaurant Name: Sushi World
- Cuisine: French
  Location: Los Angeles
  Price Range: $$$
  Rating: 3
  Restaurant Name: The Golden Spoon
- Cuisine: Italian
  Location: Chicago
  Price Range: $
  Rating: 1
  Restaurant Name: Burger Haven
<start>
| Restaurant Name | Cuisine | Location | Rating | Price Range |
| --- | --- | --- | --- | --- |
| BBQ Barn | Japanese | New York | 5 | $ |
| Pizza Planet | French | New York | 5 | $$ |
| Taco Town | Mexican | Seattle | 1 | $$$$ |
| The Steakhouse | Chinese | Phoenix | 2 | $ |
| Sushi World | French | Los Angeles | 4 | $$$$$ |
| The Golden Spoon | French | Los Angeles | 3 | $$$ |
| Burger Haven | Italian | Chicago | 1 | $ |
<end>Here's some Plain text data, can you convert it to Json?
Cuisine: Mediterranean | Price Range: $$$
Cuisine: Italian | Price Range: $
Cuisine: French | Price Range: $
Cuisine: Indian | Price Range: $$
Cuisine: Italian | Price Range: $$$
Cuisine: Mexican | Price Range: $$$
Cuisine: Chinese | Price Range: $$$$
Cuisine: Indian | Price Range: $$$$$
<start>
[
    {
        "Cuisine": "Mediterranean",
        "Price Range": "$$$"
    },
    {
        "Cuisine": "Italian",
        "Price Range": "$"
    },
    {
        "Cuisine": "French",
        "Price Range": "$"
    },
    {
        "Cuisine": "Indian",
        "Price Range": "$$"
    },
    {
        "Cuisine": "Italian",
        "Price Range": "$$$"
    },
    {
        "Cuisine": "Mexican",
        "Price Range": "$$$"
    },
    {
        "Cuisine": "Chinese",
        "Price Range": "$$$$"
    },
    {
        "Cuisine": "Indian",
        "Price Range": "$$$$$"
    }
]
<end>Here's some PLAIN TEXT data, can you convert it to csv?
Company: HealthGen | Date: 2018-11-12 | Open Price: 358.91 | High Price: 1406.52 | Low Price: 358.91 | Volume: 285502
Company: MediaGroup | Date: 2014-08-24 | Open Price: 330.24 | High Price: 751.69 | Low Price: 330.24 | Volume: 1114209
Company: BioLife | Date: 2012-02-14 | Open Price: 563.95 | High Price: 1159.46 | Low Price: 15.02 | Volume: 3927473
Company: FinanceTrust | Date: 2021-08-26 | Open Price: 517.18 | High Price: 1428.72 | Low Price: 323.14 | Volume: 500846
<start>
Company,Date,Open Price,High Price,Low Price,Volume
HealthGen,2018-11-12,358.91,1406.52,358.91,285502
MediaGroup,2014-08-24,330.24,751.69,330.24,1114209
BioLife,2012-02-14,563.95,1159.46,15.02,3927473
FinanceTrust,2021-08-26,517.18,1428.72,323.14,500846
<end>Can you change this json into CSV?
[
    {
        "Sector": "Automotive",
        "Market Cap": "Small Cap",
        "Stock Price": 151.78,
        "Annual Revenue (B)": 253.19,
        "Quarter": "Q4"
    },
    {
        "Sector": "Energy",
        "Market Cap": "Mega Cap",
        "Stock Price": 456.76,
        "Annual Revenue (B)": 228.65,
        "Quarter": "Q2"
    },
    {
        "Sector": "Healthcare",
        "Market Cap": "Mega Cap",
        "Stock Price": 267.81,
        "Annual Revenue (B)": 118.69,
        "Quarter": "Q4"
    },
    {
        "Sector": "Technology",
        "Market Cap": "Mega Cap",
        "Stock Price": 292.06,
        "Annual Revenue (B)": 207.39,
        "Quarter": "Q3"
    },
    {
        "Sector": "Technology",
        "Market Cap": "Large Cap",
        "Stock Price": 503.73,
        "Annual Revenue (B)": 387.12,
        "Quarter": "Q3"
    },
    {
        "Sector": "Energy",
        "Market Cap": "Small Cap",
        "Stock Price": 970.56,
        "Annual Revenue (B)": 342.52,
        "Quarter": "Q1"
    },
    {
        "Sector": "Finance",
        "Market Cap": "Small Cap",
        "Stock Price": 796.37,
        "Annual Revenue (B)": 426.2,
        "Quarter": "Q2"
    }
]<start>
Sector,Market Cap,Stock Price,Annual Revenue (B),Quarter
Automotive,Small Cap,151.78,253.19,Q4
Energy,Mega Cap,456.76,228.65,Q2
Healthcare,Mega Cap,267.81,118.69,Q4
Technology,Mega Cap,292.06,207.39,Q3
Technology,Large Cap,503.73,387.12,Q3
Energy,Small Cap,970.56,342.52,Q1
Finance,Small Cap,796.37,426.2,Q2
<end>Can you change this json into Markdown?
[
    {
        "Product Name": "Whatchamacallit",
        "Stock Quantity": 346,
        "Supplier Name": "Wayne Enterprises"
    },
    {
        "Product Name": "Device",
        "Stock Quantity": 284,
        "Supplier Name": "Wonka Industries"
    },
    {
        "Product Name": "Instrument",
        "Stock Quantity": 306,
        "Supplier Name": "Wonka Industries"
    },
    {
        "Product Name": "Whatchamacallit",
        "Stock Quantity": 454,
        "Supplier Name": "Umbrella Corp"
    },
    {
        "Product Name": "Contraption",
        "Stock Quantity": 460,
        "Supplier Name": "Umbrella Corp"
    },
    {
        "Product Name": "Device",
        "Stock Quantity": 283,
        "Supplier Name": "Umbrella Corp"
    },
    {
        "Product Name": "Widget",
        "Stock Quantity": 96,
        "Supplier Name": "Wayne Enterprises"
    },
    {
        "Product Name": "Widget",
        "Stock Quantity": 56,
        "Supplier Name": "Wayne Enterprises"
    },
    {
        "Product Name": "Device",
        "Stock Quantity": 179,
        "Supplier Name": "Umbrella Corp"
    }
]<start>
| Product Name | Stock Quantity | Supplier Name |
| --- | --- | --- |
| Whatchamacallit | 346 | Wayne Enterprises |
| Device | 284 | Wonka Industries |
| Instrument | 306 | Wonka Industries |
| Whatchamacallit | 454 | Umbrella Corp |
| Contraption | 460 | Umbrella Corp |
| Device | 283 | Umbrella Corp |
| Widget | 96 | Wayne Enterprises |
| Widget | 56 | Wayne Enterprises |
| Device | 179 | Umbrella Corp |
<end>Convert this yaml to markdown:
- Average Latency (ms): 25.15
  Cache Hit Ratio (%): 79.46
  Connection Count: 206
  Queries per Second: 1342.61
- Average Latency (ms): 51.14
  Cache Hit Ratio (%): 90.54
  Connection Count: 134
  Queries per Second: 4119.27
- Average Latency (ms): 12.24
  Cache Hit Ratio (%): 71.5
  Connection Count: 315
  Queries per Second: 3721.49
<start>
| Queries per Second | Cache Hit Ratio (%) | Connection Count | Average Latency (ms) |
| --- | --- | --- | --- |
| 1342.61 | 79.46 | 206 | 25.15 |
| 4119.27 | 90.54 | 134 | 51.14 |
| 3721.49 | 71.5 | 315 | 12.24 |
<end>Transform this csv structure to a Plain text format:
Title,Author,Genre,Publication Year,Rating
Echoes of Eternity,Thorne Ironwood,Fantasy,1958,2.3
Echoes of Eternity,Draven Blackthorn,Romance,2012,1.8
Echoes of Eternity,Isla Windrider,Historical,2012,2.3
A Journey Through Time,Thorne Ironwood,Horror,2007,1.3
The Crystal Key,Luna Silverleaf,Historical,1961,4.0
Whispers of the Abyss,Isla Windrider,Mystery,1979,2.3
Tales of the Brave,Galen Starfire,Science Fiction,2002,3.7
The Silent Grove,Luna Silverleaf,Mystery,1988,3.1
The Silent Grove,Sylvia Nightshade,Thriller,1973,2.0
<start>
Title: Echoes of Eternity | Author: Thorne Ironwood | Genre: Fantasy | Publication Year: 1958 | Rating: 2.3
Title: Echoes of Eternity | Author: Draven Blackthorn | Genre: Romance | Publication Year: 2012 | Rating: 1.8
Title: Echoes of Eternity | Author: Isla Windrider | Genre: Historical | Publication Year: 2012 | Rating: 2.3
Title: A Journey Through Time | Author: Thorne Ironwood | Genre: Horror | Publication Year: 2007 | Rating: 1.3
Title: The Crystal Key | Author: Luna Silverleaf | Genre: Historical | Publication Year: 1961 | Rating: 4.0
Title: Whispers of the Abyss | Author: Isla Windrider | Genre: Mystery | Publication Year: 1979 | Rating: 2.3
Title: Tales of the Brave | Author: Galen Starfire | Genre: Science Fiction | Publication Year: 2002 | Rating: 3.7
Title: The Silent Grove | Author: Luna Silverleaf | Genre: Mystery | Publication Year: 1988 | Rating: 3.1
Title: The Silent Grove | Author: Sylvia Nightshade | Genre: Thriller | Publication Year: 1973 | Rating: 2.0
<end>Can you change this YAML into CSV?
- Annual Revenue (B): 294.28
  Company: GlobalTrade
  Market Cap: Mid Cap
  Sector: Energy
- Annual Revenue (B): 103.4
  Company: Foodies
  Market Cap: Large Cap
  Sector: Healthcare
- Annual Revenue (B): 122.41
  Company: EcoEnergy
  Market Cap: Large Cap
  Sector: Biotech
- Annual Revenue (B): 63.51
  Company: AutoDrive
  Market Cap: Mega Cap
  Sector: Automotive
- Annual Revenue (B): 353.2
  Company: HealthPlus
  Market Cap: Mega Cap
  Sector: Energy
- Annual Revenue (B): 326.49
  Company: BioPharm
  Market Cap: Mid Cap
  Sector: Energy
- Annual Revenue (B): 465.92
  Company: HealthPlus
  Market Cap: Small Cap
  Sector: Healthcare
<start>
Company,Sector,Market Cap,Annual Revenue (B)
GlobalTrade,Energy,Mid Cap,294.28
Foodies,Healthcare,Large Cap,103.4
EcoEnergy,Biotech,Large Cap,122.41
AutoDrive,Automotive,Mega Cap,63.51
HealthPlus,Energy,Mega Cap,353.2
BioPharm,Energy,Mid Cap,326.49
HealthPlus,Healthcare,Small Cap,465.92
<end>Here's some Json data, can you convert it to yml?
[
    {
        "Database Name": "AnalyticsDB",
        "Cache Hit Ratio (%)": 77.54,
        "Average Latency (ms)": 65.23,
        "Timestamp": "2021-05-07 14:17:23"
    },
    {
        "Database Name": "SalesDB",
        "Cache Hit Ratio (%)": 79.2,
        "Average Latency (ms)": 13.12,
        "Timestamp": "2022-07-19 19:46:22"
    },
    {
        "Database Name": "UserDB",
        "Cache Hit Ratio (%)": 89.32,
        "Average Latency (ms)": 79.43,
        "Timestamp": "2023-11-27 11:46:14"
    },
    {
        "Database Name": "AnalyticsDB",
        "Cache Hit Ratio (%)": 89.91,
        "Average Latency (ms)": 3.88,
        "Timestamp": "2022-02-06 14:27:42"
    },
    {
        "Database Name": "ProductsDB",
        "Cache Hit Ratio (%)": 75.94,
        "Average Latency (ms)": 66.04,
        "Timestamp": "2022-12-03 09:14:42"
    }
]<start>
- Average Latency (ms): 65.23
  Cache Hit Ratio (%): 77.54
  Database Name: AnalyticsDB
  Timestamp: '2021-05-07 14:17:23'
- Average Latency (ms): 13.12
  Cache Hit Ratio (%): 79.2
  Database Name: SalesDB
  Timestamp: '2022-07-19 19:46:22'
- Average Latency (ms): 79.43
  Cache Hit Ratio (%): 89.32
  Database Name: UserDB
  Timestamp: '2023-11-27 11:46:14'
- Average Latency (ms): 3.88
  Cache Hit Ratio (%): 89.91
  Database Name: AnalyticsDB
  Timestamp: '2022-02-06 14:27:42'
- Average Latency (ms): 66.04
  Cache Hit Ratio (%): 75.94
  Database Name: ProductsDB
  Timestamp: '2022-12-03 09:14:42'
<end>Transform this json structure to a Csv format:
[
    {
        "Trip Name": "Valley Voyage",
        "Start Location": "New York",
        "End Location": "Phoenix",
        "Distance (miles)": 1318.6,
        "Fuel Used (gallons)": 91.8
    },
    {
        "Trip Name": "Historic Route",
        "Start Location": "San Francisco",
        "End Location": "Denver",
        "Distance (miles)": 1423.1,
        "Fuel Used (gallons)": 89.9
    },
    {
        "Trip Name": "Forest Journey",
        "Start Location": "Denver",
        "End Location": "Houston",
        "Distance (miles)": 991.4,
        "Fuel Used (gallons)": 98.5
    },
    {
        "Trip Name": "Mountain Adventure",
        "Start Location": "Phoenix",
        "End Location": "Chicago",
        "Distance (miles)": 205.7,
        "Fuel Used (gallons)": 5.6
    },
    {
        "Trip Name": "Canyon Trek",
        "Start Location": "Houston",
        "End Location": "New York",
        "Distance (miles)": 1022.4,
        "Fuel Used (gallons)": 7.0
    },
    {
        "Trip Name": "Mountain Adventure",
        "Start Location": "Houston",
        "End Location": "Los Angeles",
        "Distance (miles)": 847.3,
        "Fuel Used (gallons)": 65.0
    }
]<start>
Trip Name,Start Location,End Location,Distance (miles),Fuel Used (gallons)
Valley Voyage,New York,Phoenix,1318.6,91.8
Historic Route,San Francisco,Denver,1423.1,89.9
Forest Journey,Denver,Houston,991.4,98.5
Mountain Adventure,Phoenix,Chicago,205.7,5.6
Canyon Trek,Houston,New York,1022.4,7.0
Mountain Adventure,Houston,Los Angeles,847.3,65.0
<end>Here's some Json data, can you convert it to MARKDOWN?
[
    {
        "Company": "GreenEnergy",
        "Date": "2017-08-27",
        "Open Price": 74.56,
        "Close Price": 1017.47,
        "High Price": 1045.59,
        "Low Price": 74.56
    },
    {
        "Company": "HealthGen",
        "Date": "2021-09-19",
        "Open Price": 1379.61,
        "Close Price": 963.09,
        "High Price": 1379.61,
        "Low Price": 172.71
    },
    {
        "Company": "MediaGroup",
        "Date": "2014-04-19",
        "Open Price": 74.3,
        "Close Price": 833.34,
        "High Price": 833.34,
        "Low Price": 74.3
    },
    {
        "Company": "MediaGroup",
        "Date": "2013-04-27",
        "Open Price": 785.76,
        "Close Price": 1218.47,
        "High Price": 1218.47,
        "Low Price": 785.76
    },
    {
        "Company": "GreenEnergy",
        "Date": "2016-03-02",
        "Open Price": 984.88,
        "Close Price": 1320.6,
        "High Price": 1320.6,
        "Low Price": 984.88
    },
    {
        "Company": "MediaGroup",
        "Date": "2016-06-07",
        "Open Price": 979.96,
        "Close Price": 172.71,
        "High Price": 979.96,
        "Low Price": 22.59
    },
    {
        "Company": "AeroSystems",
        "Date": "2013-05-06",
        "Open Price": 800.01,
        "Close Price": 27.74,
        "High Price": 1282.07,
        "Low Price": 27.74
    },
    {
        "Company": "AutoMotive",
        "Date": "2012-05-15",
        "Open Price": 436.59,
        "Close Price": 595.08,
        "High Price": 595.08,
        "Low Price": 172.71
    },
    {
        "Company": "GreenEnergy",
        "Date": "2011-01-18",
        "Open Price": 817.38,
        "Close Price": 500.15,
        "High Price": 817.38,
        "Low Price": 500.15
    }
]<start>
| Company | Date | Open Price | Close Price | High Price | Low Price |
| --- | --- | --- | --- | --- | --- |
| GreenEnergy | 2017-08-27 | 74.56 | 1017.47 | 1045.59 | 74.56 |
| HealthGen | 2021-09-19 | 1379.61 | 963.09 | 1379.61 | 172.71 |
| MediaGroup | 2014-04-19 | 74.3 | 833.34 | 833.34 | 74.3 |
| MediaGroup | 2013-04-27 | 785.76 | 1218.47 | 1218.47 | 785.76 |
| GreenEnergy | 2016-03-02 | 984.88 | 1320.6 | 1320.6 | 984.88 |
| MediaGroup | 2016-06-07 | 979.96 | 172.71 | 979.96 | 22.59 |
| AeroSystems | 2013-05-06 | 800.01 | 27.74 | 1282.07 | 27.74 |
| AutoMotive | 2012-05-15 | 436.59 | 595.08 | 595.08 | 172.71 |
| GreenEnergy | 2011-01-18 | 817.38 | 500.15 | 817.38 | 500.15 |
<end>Convert this yaml to Json:
- Close Price: 829.06
  Company: MediaGroup
  Date: '2023-07-28'
  High Price: 1096.18
  Low Price: 169.29
  Open Price: 169.29
  Volume: 3683220
- Close Price: 1287.68
  Company: AutoMotive
  Date: '2013-07-21'
  High Price: 1311.18
  Low Price: 630.71
  Open Price: 630.71
  Volume: 9968907
- Close Price: 1181.29
  Company: HealthGen
  Date: '2010-02-17'
  High Price: 1181.29
  Low Price: 107.05
  Open Price: 517.84
  Volume: 4738371
- Close Price: 786.85
  Company: AeroSystems
  Date: '2015-03-06'
  High Price: 1247.48
  Low Price: 149.38
  Open Price: 1247.48
  Volume: 6745489
- Close Price: 1272.99
  Company: MediaGroup
  Date: '2014-05-28'
  High Price: 1418.36
  Low Price: 907.67
  Open Price: 907.67
  Volume: 7035113
- Close Price: 787.82
  Company: HealthGen
  Date: '2013-04-25'
  High Price: 986.67
  Low Price: 144.03
  Open Price: 986.67
  Volume: 7563455
<start>
[
    {
        "Company": "MediaGroup",
        "Date": "2023-07-28",
        "Open Price": 169.29,
        "Close Price": 829.06,
        "High Price": 1096.18,
        "Low Price": 169.29,
        "Volume": 3683220
    },
    {
        "Company": "AutoMotive",
        "Date": "2013-07-21",
        "Open Price": 630.71,
        "Close Price": 1287.68,
        "High Price": 1311.18,
        "Low Price": 630.71,
        "Volume": 9968907
    },
    {
        "Company": "HealthGen",
        "Date": "2010-02-17",
        "Open Price": 517.84,
        "Close Price": 1181.29,
        "High Price": 1181.29,
        "Low Price": 107.05,
        "Volume": 4738371
    },
    {
        "Company": "AeroSystems",
        "Date": "2015-03-06",
        "Open Price": 1247.48,
        "Close Price": 786.85,
        "High Price": 1247.48,
        "Low Price": 149.38,
        "Volume": 6745489
    },
    {
        "Company": "MediaGroup",
        "Date": "2014-05-28",
        "Open Price": 907.67,
        "Close Price": 1272.99,
        "High Price": 1418.36,
        "Low Price": 907.67,
        "Volume": 7035113
    },
    {
        "Company": "HealthGen",
        "Date": "2013-04-25",
        "Open Price": 986.67,
        "Close Price": 787.82,
        "High Price": 986.67,
        "Low Price": 144.03,
        "Volume": 7563455
    }
]
<end>Please transform the following plain text data into Yaml:
Restaurant Name: Curry Corner | Cuisine: Italian | Location: San Francisco | Rating: 3
Restaurant Name: Vegan Delight | Cuisine: French | Location: Chicago | Rating: 2
Restaurant Name: The Steakhouse | Cuisine: American | Location: Chicago | Rating: 3
Restaurant Name: Sushi World | Cuisine: Indian | Location: Chicago | Rating: 1
Restaurant Name: Pizza Planet | Cuisine: Italian | Location: Los Angeles | Rating: 2
Restaurant Name: Taco Town | Cuisine: Italian | Location: Miami | Rating: 1
Restaurant Name: Sushi World | Cuisine: Indian | Location: Phoenix | Rating: 3
<start>
- Cuisine: Italian
  Location: San Francisco
  Rating: 3
  Restaurant Name: Curry Corner
- Cuisine: French
  Location: Chicago
  Rating: 2
  Restaurant Name: Vegan Delight
- Cuisine: American
  Location: Chicago
  Rating: 3
  Restaurant Name: The Steakhouse
- Cuisine: Indian
  Location: Chicago
  Rating: 1
  Restaurant Name: Sushi World
- Cuisine: Italian
  Location: Los Angeles
  Rating: 2
  Restaurant Name: Pizza Planet
- Cuisine: Italian
  Location: Miami
  Rating: 1
  Restaurant Name: Taco Town
- Cuisine: Indian
  Location: Phoenix
  Rating: 3
  Restaurant Name: Sushi World
<end>Can you change this MARKDOWN into json?
| Start Location | Distance (miles) | Duration (hours) |
| --- | --- | --- |
| Houston | 2442.8 | 6.7 |
| Phoenix | 1018.4 | 50.8 |
| New York | 2732.1 | 11.2 |
| Denver | 1088.9 | 29.7 |<start>
[
    {
        "Start Location": "Houston",
        "Distance (miles)": 2442.8,
        "Duration (hours)": 6.7
    },
    {
        "Start Location": "Phoenix",
        "Distance (miles)": 1018.4,
        "Duration (hours)": 50.8
    },
    {
        "Start Location": "New York",
        "Distance (miles)": 2732.1,
        "Duration (hours)": 11.2
    },
    {
        "Start Location": "Denver",
        "Distance (miles)": 1088.9,
        "Duration (hours)": 29.7
    }
]
<end>Here's some Markdown data, can you convert it to json?
| Trip Name | End Location | Distance (miles) | Duration (hours) | Fuel Used (gallons) |
| --- | --- | --- | --- | --- |
| Canyon Trek | San Francisco | 2445.5 | 17.4 | 43.2 |
| Forest Journey | Chicago | 2750.1 | 33.1 | 96.1 |
| Forest Journey | Miami | 94.6 | 41.5 | 38.9 |
| Lakeside Retreat | Houston | 942.1 | 48.8 | 53.3 |
| Valley Voyage | Los Angeles | 2812.6 | 65.8 | 19.3 |
| Forest Journey | Denver | 371.5 | 63.9 | 9.2 |
| Historic Route | Phoenix | 1591.8 | 25.6 | 69.6 |
| Coast to Coast | Los Angeles | 1021.6 | 62.6 | 93.2 |
| Highway Odyssey | San Francisco | 2421.8 | 40.2 | 11.4 |
| Valley Voyage | Los Angeles | 411.0 | 39.8 | 93.8 |<start>
[
    {
        "Trip Name": "Canyon Trek",
        "End Location": "San Francisco",
        "Distance (miles)": 2445.5,
        "Duration (hours)": 17.4,
        "Fuel Used (gallons)": 43.2
    },
    {
        "Trip Name": "Forest Journey",
        "End Location": "Chicago",
        "Distance (miles)": 2750.1,
        "Duration (hours)": 33.1,
        "Fuel Used (gallons)": 96.1
    },
    {
        "Trip Name": "Forest Journey",
        "End Location": "Miami",
        "Distance (miles)": 94.6,
        "Duration (hours)": 41.5,
        "Fuel Used (gallons)": 38.9
    },
    {
        "Trip Name": "Lakeside Retreat",
        "End Location": "Houston",
        "Distance (miles)": 942.1,
        "Duration (hours)": 48.8,
        "Fuel Used (gallons)": 53.3
    },
    {
        "Trip Name": "Valley Voyage",
        "End Location": "Los Angeles",
        "Distance (miles)": 2812.6,
        "Duration (hours)": 65.8,
        "Fuel Used (gallons)": 19.3
    },
    {
        "Trip Name": "Forest Journey",
        "End Location": "Denver",
        "Distance (miles)": 371.5,
        "Duration (hours)": 63.9,
        "Fuel Used (gallons)": 9.2
    },
    {
        "Trip Name": "Historic Route",
        "End Location": "Phoenix",
        "Distance (miles)": 1591.8,
        "Duration (hours)": 25.6,
        "Fuel Used (gallons)": 69.6
    },
    {
        "Trip Name": "Coast to Coast",
        "End Location": "Los Angeles",
        "Distance (miles)": 1021.6,
        "Duration (hours)": 62.6,
        "Fuel Used (gallons)": 93.2
    },
    {
        "Trip Name": "Highway Odyssey",
        "End Location": "San Francisco",
        "Distance (miles)": 2421.8,
        "Duration (hours)": 40.2,
        "Fuel Used (gallons)": 11.4
    },
    {
        "Trip Name": "Valley Voyage",
        "End Location": "Los Angeles",
        "Distance (miles)": 411.0,
        "Duration (hours)": 39.8,
        "Fuel Used (gallons)": 93.8
    }
]
<end>Can you change this Plain text into Json?
Start Location: Houston | End Location: Chicago | Distance (miles): 329.4 | Duration (hours): 28.6
Start Location: Houston | End Location: Chicago | Distance (miles): 1086.8 | Duration (hours): 28.6
Start Location: Chicago | End Location: Houston | Distance (miles): 2240.2 | Duration (hours): 26.3
<start>
[
    {
        "Start Location": "Houston",
        "End Location": "Chicago",
        "Distance (miles)": 329.4,
        "Duration (hours)": 28.6
    },
    {
        "Start Location": "Houston",
        "End Location": "Chicago",
        "Distance (miles)": 1086.8,
        "Duration (hours)": 28.6
    },
    {
        "Start Location": "Chicago",
        "End Location": "Houston",
        "Distance (miles)": 2240.2,
        "Duration (hours)": 26.3
    }
]
<end>Please transform the following PLAIN TEXT data into MARKDOWN:
Director: Mara Moonshadow | Genre: Adventure | Box Office Earnings (M): 546.67
Director: Talon Blackthorn | Genre: Drama | Box Office Earnings (M): 398.2
Director: Selene Darkwhisper | Genre: Thriller | Box Office Earnings (M): 724.88
Director: Orin Shadowalker | Genre: Drama | Box Office Earnings (M): 659.25
Director: Aria Ravenwood | Genre: Drama | Box Office Earnings (M): 431.08
<start>
| Director | Genre | Box Office Earnings (M) |
| --- | --- | --- |
| Mara Moonshadow | Adventure | 546.67 |
| Talon Blackthorn | Drama | 398.2 |
| Selene Darkwhisper | Thriller | 724.88 |
| Orin Shadowalker | Drama | 659.25 |
| Aria Ravenwood | Drama | 431.08 |
<end>Can you change this Markdown into Json?
| Company | Sector | Market Cap | Stock Price |
| --- | --- | --- | --- |
| AeroSpace | Automotive | Mid Cap | 105.56 |
| EcoEnergy | Finance | Mid Cap | 709.87 |
| AeroSpace | Retail | Small Cap | 788.39 |
| AeroSpace | Aerospace | Mega Cap | 413.38 |
| HealthPlus | Healthcare | Large Cap | 486.15 |
| GlobalTrade | Healthcare | Large Cap | 486.15 |
| HealthPlus | Finance | Mega Cap | 795.0 |<start>
[
    {
        "Company": "AeroSpace",
        "Sector": "Automotive",
        "Market Cap": "Mid Cap",
        "Stock Price": 105.56
    },
    {
        "Company": "EcoEnergy",
        "Sector": "Finance",
        "Market Cap": "Mid Cap",
        "Stock Price": 709.87
    },
    {
        "Company": "AeroSpace",
        "Sector": "Retail",
        "Market Cap": "Small Cap",
        "Stock Price": 788.39
    },
    {
        "Company": "AeroSpace",
        "Sector": "Aerospace",
        "Market Cap": "Mega Cap",
        "Stock Price": 413.38
    },
    {
        "Company": "HealthPlus",
        "Sector": "Healthcare",
        "Market Cap": "Large Cap",
        "Stock Price": 486.15
    },
    {
        "Company": "GlobalTrade",
        "Sector": "Healthcare",
        "Market Cap": "Large Cap",
        "Stock Price": 486.15
    },
    {
        "Company": "HealthPlus",
        "Sector": "Finance",
        "Market Cap": "Mega Cap",
        "Stock Price": 795.0
    }
]
<end>Can you change this Yml into JSON?
- Author: Luna Silverleaf
  Genre: Mystery
  Rating: 2.1
  Title: Legends of the Rift
- Author: Thorne Ironwood
  Genre: Non-Fiction
  Rating: 2.0
  Title: Tales of the Brave
- Author: Kara Firebrand
  Genre: Thriller
  Rating: 4.5
  Title: The Last Sky
<start>
[
    {
        "Title": "Legends of the Rift",
        "Author": "Luna Silverleaf",
        "Genre": "Mystery",
        "Rating": 2.1
    },
    {
        "Title": "Tales of the Brave",
        "Author": "Thorne Ironwood",
        "Genre": "Non-Fiction",
        "Rating": 2.0
    },
    {
        "Title": "The Last Sky",
        "Author": "Kara Firebrand",
        "Genre": "Thriller",
        "Rating": 4.5
    }
]
<end>Convert this markdown to plain text:
| Device ID | Device Type | Location | Battery Level (%) | Reading Value |
| --- | --- | --- | --- | --- |
| device-0026 | Temperature Sensor | Kitchen | 77.1 | 83.89 |
| device-0086 | Temperature Sensor | Bathroom | 77.1 | -27.35 |
| device-0006 | Light Sensor | Bathroom | 14.7 | -22.26 |
| device-0053 | Light Sensor | Garden | 18.6 | 3.11 |
| device-0062 | Pressure Sensor | Kitchen | 12.7 | -22.26 |<start>
Device ID: device-0026 | Device Type: Temperature Sensor | Location: Kitchen | Battery Level (%): 77.1 | Reading Value: 83.89
Device ID: device-0086 | Device Type: Temperature Sensor | Location: Bathroom | Battery Level (%): 77.1 | Reading Value: -27.35
Device ID: device-0006 | Device Type: Light Sensor | Location: Bathroom | Battery Level (%): 14.7 | Reading Value: -22.26
Device ID: device-0053 | Device Type: Light Sensor | Location: Garden | Battery Level (%): 18.6 | Reading Value: 3.11
Device ID: device-0062 | Device Type: Pressure Sensor | Location: Kitchen | Battery Level (%): 12.7 | Reading Value: -22.26
<end>Convert this MARKDOWN to Json:
| Sector | Market Cap | Annual Revenue (B) | Quarter |
| --- | --- | --- | --- |
| Retail | Small Cap | 422.36 | Q1 |
| Healthcare | Small Cap | 254.3 | Q2 |
| Finance | Small Cap | 430.24 | Q2 |
| Aerospace | Large Cap | 401.79 | Q4 |
| Retail | Large Cap | 386.75 | Q3 |
| Retail | Mega Cap | 335.01 | Q2 |
| Retail | Large Cap | 297.82 | Q3 |
| Biotech | Mid Cap | 111.67 | Q3 |<start>
[
    {
        "Sector": "Retail",
        "Market Cap": "Small Cap",
        "Annual Revenue (B)": 422.36,
        "Quarter": "Q1"
    },
    {
        "Sector": "Healthcare",
        "Market Cap": "Small Cap",
        "Annual Revenue (B)": 254.3,
        "Quarter": "Q2"
    },
    {
        "Sector": "Finance",
        "Market Cap": "Small Cap",
        "Annual Revenue (B)": 430.24,
        "Quarter": "Q2"
    },
    {
        "Sector": "Aerospace",
        "Market Cap": "Large Cap",
        "Annual Revenue (B)": 401.79,
        "Quarter": "Q4"
    },
    {
        "Sector": "Retail",
        "Market Cap": "Large Cap",
        "Annual Revenue (B)": 386.75,
        "Quarter": "Q3"
    },
    {
        "Sector": "Retail",
        "Market Cap": "Mega Cap",
        "Annual Revenue (B)": 335.01,
        "Quarter": "Q2"
    },
    {
        "Sector": "Retail",
        "Market Cap": "Large Cap",
        "Annual Revenue (B)": 297.82,
        "Quarter": "Q3"
    },
    {
        "Sector": "Biotech",
        "Market Cap": "Mid Cap",
        "Annual Revenue (B)": 111.67,
        "Quarter": "Q3"
    }
]
<end>Convert this yaml to Plain text:
- Location: San Francisco
  Restaurant Name: Curry Corner
- Location: Los Angeles
  Restaurant Name: Taco Town
- Location: Seattle
  Restaurant Name: Sushi World
- Location: Chicago
  Restaurant Name: Vegan Delight
<start>
Restaurant Name: Curry Corner | Location: San Francisco
Restaurant Name: Taco Town | Location: Los Angeles
Restaurant Name: Sushi World | Location: Seattle
Restaurant Name: Vegan Delight | Location: Chicago
<end>Please transform the following Json data into yml:
[
    {
        "Name": "Caroline",
        "Age": 61,
        "Birth Month": "September",
        "City": "San Diego",
        "Income": 285000
    },
    {
        "Name": "Kenneth",
        "Age": 38,
        "Birth Month": "August",
        "City": "Dallas",
        "Income": 330000
    },
    {
        "Name": "Lulu",
        "Age": 58,
        "Birth Month": "October",
        "City": "Nashville",
        "Income": 220000
    },
    {
        "Name": "Marjorie",
        "Age": 22,
        "Birth Month": "February",
        "City": "Baltimore",
        "Income": 230000
    },
    {
        "Name": "Iva",
        "Age": 42,
        "Birth Month": "February",
        "City": "San Diego",
        "Income": 240000
    },
    {
        "Name": "Jasmin",
        "Age": 60,
        "Birth Month": "July",
        "City": "San Francisco",
        "Income": 335000
    }
]<start>
- Age: 61
  Birth Month: September
  City: San Diego
  Income: 285000
  Name: Caroline
- Age: 38
  Birth Month: August
  City: Dallas
  Income: 330000
  Name: Kenneth
- Age: 58
  Birth Month: October
  City: Nashville
  Income: 220000
  Name: Lulu
- Age: 22
  Birth Month: February
  City: Baltimore
  Income: 230000
  Name: Marjorie
- Age: 42
  Birth Month: February
  City: San Diego
  Income: 240000
  Name: Iva
- Age: 60
  Birth Month: July
  City: San Francisco
  Income: 335000
  Name: Jasmin
<end>Can you change this json into plain text?
[
    {
        "Director": "Talon Blackthorn",
        "Genre": "Thriller"
    },
    {
        "Director": "Rylan Frostblade",
        "Genre": "Comedy"
    },
    {
        "Director": "Aria Ravenwood",
        "Genre": "Adventure"
    }
]<start>
Director: Talon Blackthorn | Genre: Thriller
Director: Rylan Frostblade | Genre: Comedy
Director: Aria Ravenwood | Genre: Adventure
<end>Here's some yaml data, can you convert it to Json?
- Condition: Snowy
  Day: Saturday
  Humidity (%): 28
  Location: Chicago
  Wind Speed (km/h): 28.4
- Condition: Rainy
  Day: Sunday
  Humidity (%): 99
  Location: Houston
  Wind Speed (km/h): 13.3
- Condition: Cloudy
  Day: Thursday
  Humidity (%): 91
  Location: New York
  Wind Speed (km/h): 17.7
- Condition: Snowy
  Day: Tuesday
  Humidity (%): 34
  Location: New York
  Wind Speed (km/h): 17.0
- Condition: Stormy
  Day: Sunday
  Humidity (%): 60
  Location: Miami
  Wind Speed (km/h): 1.0
- Condition: Cloudy
  Day: Monday
  Humidity (%): 59
  Location: Denver
  Wind Speed (km/h): 24.2
- Condition: Cloudy
  Day: Friday
  Humidity (%): 99
  Location: Chicago
  Wind Speed (km/h): 23.8
- Condition: Rainy
  Day: Sunday
  Humidity (%): 33
  Location: Miami
  Wind Speed (km/h): 24.5
<start>
[
    {
        "Location": "Chicago",
        "Condition": "Snowy",
        "Humidity (%)": 28,
        "Wind Speed (km/h)": 28.4,
        "Day": "Saturday"
    },
    {
        "Location": "Houston",
        "Condition": "Rainy",
        "Humidity (%)": 99,
        "Wind Speed (km/h)": 13.3,
        "Day": "Sunday"
    },
    {
        "Location": "New York",
        "Condition": "Cloudy",
        "Humidity (%)": 91,
        "Wind Speed (km/h)": 17.7,
        "Day": "Thursday"
    },
    {
        "Location": "New York",
        "Condition": "Snowy",
        "Humidity (%)": 34,
        "Wind Speed (km/h)": 17.0,
        "Day": "Tuesday"
    },
    {
        "Location": "Miami",
        "Condition": "Stormy",
        "Humidity (%)": 60,
        "Wind Speed (km/h)": 1.0,
        "Day": "Sunday"
    },
    {
        "Location": "Denver",
        "Condition": "Cloudy",
        "Humidity (%)": 59,
        "Wind Speed (km/h)": 24.2,
        "Day": "Monday"
    },
    {
        "Location": "Chicago",
        "Condition": "Cloudy",
        "Humidity (%)": 99,
        "Wind Speed (km/h)": 23.8,
        "Day": "Friday"
    },
    {
        "Location": "Miami",
        "Condition": "Rainy",
        "Humidity (%)": 33,
        "Wind Speed (km/h)": 24.5,
        "Day": "Sunday"
    }
]
<end>Transform this plain text structure to a json format:
Name: Felicia | Age: 40 | Birth Month: June
Name: Anne | Age: 53 | Birth Month: July
Name: Glenn | Age: 26 | Birth Month: August
Name: Bridget | Age: 32 | Birth Month: January
Name: Cassie | Age: 34 | Birth Month: March
Name: Frieda | Age: 49 | Birth Month: January
Name: Johnny | Age: 42 | Birth Month: March
Name: King | Age: 68 | Birth Month: September
Name: Aubrey | Age: 23 | Birth Month: January
<start>
[
    {
        "Name": "Felicia",
        "Age": 40,
        "Birth Month": "June"
    },
    {
        "Name": "Anne",
        "Age": 53,
        "Birth Month": "July"
    },
    {
        "Name": "Glenn",
        "Age": 26,
        "Birth Month": "August"
    },
    {
        "Name": "Bridget",
        "Age": 32,
        "Birth Month": "January"
    },
    {
        "Name": "Cassie",
        "Age": 34,
        "Birth Month": "March"
    },
    {
        "Name": "Frieda",
        "Age": 49,
        "Birth Month": "January"
    },
    {
        "Name": "Johnny",
        "Age": 42,
        "Birth Month": "March"
    },
    {
        "Name": "King",
        "Age": 68,
        "Birth Month": "September"
    },
    {
        "Name": "Aubrey",
        "Age": 23,
        "Birth Month": "January"
    }
]
<end>Here's some PLAIN TEXT data, can you convert it to yml?
Company: AeroSpace | Sector: Aerospace | Market Cap: Small Cap | Stock Price: 824.91 | Quarter: Q2
Company: GlobalTrade | Sector: Technology | Market Cap: Mega Cap | Stock Price: 605.06 | Quarter: Q1
Company: GlobalTrade | Sector: Technology | Market Cap: Small Cap | Stock Price: 475.95 | Quarter: Q1
Company: EcoEnergy | Sector: Aerospace | Market Cap: Large Cap | Stock Price: 870.71 | Quarter: Q1
<start>
- Company: AeroSpace
  Market Cap: Small Cap
  Quarter: Q2
  Sector: Aerospace
  Stock Price: 824.91
- Company: GlobalTrade
  Market Cap: Mega Cap
  Quarter: Q1
  Sector: Technology
  Stock Price: 605.06
- Company: GlobalTrade
  Market Cap: Small Cap
  Quarter: Q1
  Sector: Technology
  Stock Price: 475.95
- Company: EcoEnergy
  Market Cap: Large Cap
  Quarter: Q1
  Sector: Aerospace
  Stock Price: 870.71
<end>Convert this CSV to YML:
Product Name,Price,Stock Quantity,Category,Supplier Name
Device,289.26,252,Automotive,Umbrella Corp
Gadget,108.19,468,Electronics,Globex
Doohickey,286.12,387,Electronics,Wonka Industries
Doohickey,146.51,350,Household,Wonka Industries
Contraption,108.58,451,Sports,Umbrella Corp
Instrument,85.24,236,Sports,Wonka Industries
Thingamajig,176.31,95,Electronics,Wonka Industries
Instrument,367.94,390,Toys,Wonka Industries
<start>
- Category: Automotive
  Price: 289.26
  Product Name: Device
  Stock Quantity: 252
  Supplier Name: Umbrella Corp
- Category: Electronics
  Price: 108.19
  Product Name: Gadget
  Stock Quantity: 468
  Supplier Name: Globex
- Category: Electronics
  Price: 286.12
  Product Name: Doohickey
  Stock Quantity: 387
  Supplier Name: Wonka Industries
- Category: Household
  Price: 146.51
  Product Name: Doohickey
  Stock Quantity: 350
  Supplier Name: Wonka Industries
- Category: Sports
  Price: 108.58
  Product Name: Contraption
  Stock Quantity: 451
  Supplier Name: Umbrella Corp
- Category: Sports
  Price: 85.24
  Product Name: Instrument
  Stock Quantity: 236
  Supplier Name: Wonka Industries
- Category: Electronics
  Price: 176.31
  Product Name: Thingamajig
  Stock Quantity: 95
  Supplier Name: Wonka Industries
- Category: Toys
  Price: 367.94
  Product Name: Instrument
  Stock Quantity: 390
  Supplier Name: Wonka Industries
<end>Can you change this json into PLAIN TEXT?
[
    {
        "Title": "Whispers of the Abyss",
        "Author": "Kara Firebrand",
        "Publication Year": 2006,
        "Rating": 2.2
    },
    {
        "Title": "The Silent Grove",
        "Author": "Elara Moonshadow",
        "Publication Year": 1991,
        "Rating": 1.3
    },
    {
        "Title": "Echoes of Eternity",
        "Author": "Orion Frostblade",
        "Publication Year": 1985,
        "Rating": 1.2
    },
    {
        "Title": "The Crystal Key",
        "Author": "Draven Blackthorn",
        "Publication Year": 1957,
        "Rating": 3.6
    },
    {
        "Title": "Tales of the Brave",
        "Author": "Draven Blackthorn",
        "Publication Year": 1984,
        "Rating": 4.9
    },
    {
        "Title": "A Journey Through Time",
        "Author": "Galen Starfire",
        "Publication Year": 1984,
        "Rating": 1.3
    },
    {
        "Title": "Legends of the Rift",
        "Author": "Thorne Ironwood",
        "Publication Year": 1962,
        "Rating": 4.9
    }
]<start>
Title: Whispers of the Abyss | Author: Kara Firebrand | Publication Year: 2006 | Rating: 2.2
Title: The Silent Grove | Author: Elara Moonshadow | Publication Year: 1991 | Rating: 1.3
Title: Echoes of Eternity | Author: Orion Frostblade | Publication Year: 1985 | Rating: 1.2
Title: The Crystal Key | Author: Draven Blackthorn | Publication Year: 1957 | Rating: 3.6
Title: Tales of the Brave | Author: Draven Blackthorn | Publication Year: 1984 | Rating: 4.9
Title: A Journey Through Time | Author: Galen Starfire | Publication Year: 1984 | Rating: 1.3
Title: Legends of the Rift | Author: Thorne Ironwood | Publication Year: 1962 | Rating: 4.9
<end>Please transform the following Plain text data into json:
Date: 2023-03-05 | Close Price: 616.74 | High Price: 677.06 | Volume: 3292738
Date: 2016-09-05 | Close Price: 292.48 | High Price: 593.71 | Volume: 9916305
Date: 2013-08-02 | Close Price: 593.71 | High Price: 593.71 | Volume: 3508070
Date: 2014-06-25 | Close Price: 1445.37 | High Price: 1445.37 | Volume: 2346279
Date: 2023-05-27 | Close Price: 562.55 | High Price: 860.81 | Volume: 1850665
<start>
[
    {
        "Date": "2023-03-05",
        "Close Price": 616.74,
        "High Price": 677.06,
        "Volume": 3292738
    },
    {
        "Date": "2016-09-05",
        "Close Price": 292.48,
        "High Price": 593.71,
        "Volume": 9916305
    },
    {
        "Date": "2013-08-02",
        "Close Price": 593.71,
        "High Price": 593.71,
        "Volume": 3508070
    },
    {
        "Date": "2014-06-25",
        "Close Price": 1445.37,
        "High Price": 1445.37,
        "Volume": 2346279
    },
    {
        "Date": "2023-05-27",
        "Close Price": 562.55,
        "High Price": 860.81,
        "Volume": 1850665
    }
]
<end>Here's some MARKDOWN data, can you convert it to CSV?
| Product Name | SKU | Price | Stock Quantity | Category | Supplier Name |
| --- | --- | --- | --- | --- | --- |
| Instrument | SKU-1094 | 472.69 | 403 | Toys | Globex |
| Apparatus | SKU-1010 | 85.79 | 60 | Sports | Wayne Enterprises |
| Gizmo | SKU-1025 | 217.59 | 416 | Household | Wonka Industries |
| Thingamajig | SKU-1099 | 97.29 | 383 | Household | Globex |
| Instrument | SKU-1008 | 258.15 | 412 | Household | Umbrella Corp |
| Apparatus | SKU-1072 | 486.24 | 180 | Household | Wonka Industries |
| Gizmo | SKU-1075 | 496.4 | 447 | Household | Wayne Enterprises |
| Thingamajig | SKU-1054 | 446.52 | 473 | Toys | ACME Corp |
| Apparatus | SKU-1020 | 380.59 | 5 | Electronics | Wonka Industries |
| Apparatus | SKU-1027 | 250.13 | 263 | Toys | ACME Corp |<start>
Product Name,SKU,Price,Stock Quantity,Category,Supplier Name
Instrument,SKU-1094,472.69,403,Toys,Globex
Apparatus,SKU-1010,85.79,60,Sports,Wayne Enterprises
Gizmo,SKU-1025,217.59,416,Household,Wonka Industries
Thingamajig,SKU-1099,97.29,383,Household,Globex
Instrument,SKU-1008,258.15,412,Household,Umbrella Corp
Apparatus,SKU-1072,486.24,180,Household,Wonka Industries
Gizmo,SKU-1075,496.4,447,Household,Wayne Enterprises
Thingamajig,SKU-1054,446.52,473,Toys,ACME Corp
Apparatus,SKU-1020,380.59,5,Electronics,Wonka Industries
Apparatus,SKU-1027,250.13,263,Toys,ACME Corp
<end>Convert this markdown to plain text:
| Device ID | Device Type | Battery Level (%) | Reading Value | Timestamp |
| --- | --- | --- | --- | --- |
| device-0072 | Temperature Sensor | 14.3 | 12.4 | 2021-11-25 23:38:25 |
| device-0083 | Light Sensor | 26.7 | -7.83 | 2021-04-02 11:49:02 |
| device-0040 | Humidity Sensor | 71.2 | -15.87 | 2022-04-19 19:26:26 |<start>
Device ID: device-0072 | Device Type: Temperature Sensor | Battery Level (%): 14.3 | Reading Value: 12.4 | Timestamp: 2021-11-25 23:38:25
Device ID: device-0083 | Device Type: Light Sensor | Battery Level (%): 26.7 | Reading Value: -7.83 | Timestamp: 2021-04-02 11:49:02
Device ID: device-0040 | Device Type: Humidity Sensor | Battery Level (%): 71.2 | Reading Value: -15.87 | Timestamp: 2022-04-19 19:26:26
<end>Transform this csv structure to a plain text format:
Age,City
65,Fort Worth
69,El Paso
39,Austin
23,Louisville
30,New York
63,Washington
64,Louisville
30,Louisville
53,Milwaukee
43,Memphis
<start>
Age: 65 | City: Fort Worth
Age: 69 | City: El Paso
Age: 39 | City: Austin
Age: 23 | City: Louisville
Age: 30 | City: New York
Age: 63 | City: Washington
Age: 64 | City: Louisville
Age: 30 | City: Louisville
Age: 53 | City: Milwaukee
Age: 43 | City: Memphis
<end>Can you change this JSON into CSV?
[
    {
        "Birth Month": "May",
        "City": "Seattle"
    },
    {
        "Birth Month": "August",
        "City": "Chicago"
    },
    {
        "Birth Month": "February",
        "City": "Columbus"
    }
]<start>
Birth Month,City
May,Seattle
August,Chicago
February,Columbus
<end>Can you change this markdown into YML?
| Date | Open Price | High Price | Low Price |
| --- | --- | --- | --- |
| 2011-10-27 | 584.8 | 1381.96 | 314.6 |
| 2023-02-20 | 581.94 | 581.94 | 190.01 |
| 2010-03-03 | 210.42 | 1166.08 | 210.42 |
| 2011-08-28 | 314.75 | 898.92 | 314.75 |
| 2022-07-16 | 1198.8 | 1198.8 | 210.42 |
| 2022-08-20 | 136.19 | 632.57 | 136.19 |<start>
- Date: '2011-10-27'
  High Price: 1381.96
  Low Price: 314.6
  Open Price: 584.8
- Date: '2023-02-20'
  High Price: 581.94
  Low Price: 190.01
  Open Price: 581.94
- Date: '2010-03-03'
  High Price: 1166.08
  Low Price: 210.42
  Open Price: 210.42
- Date: '2011-08-28'
  High Price: 898.92
  Low Price: 314.75
  Open Price: 314.75
- Date: '2022-07-16'
  High Price: 1198.8
  Low Price: 210.42
  Open Price: 1198.8
- Date: '2022-08-20'
  High Price: 632.57
  Low Price: 136.19
  Open Price: 136.19
<end>Here's some json data, can you convert it to csv?
[
    {
        "Queries per Second": 3973.2,
        "Cache Hit Ratio (%)": 92.12,
        "Connection Count": 335,
        "Average Latency (ms)": 68.78,
        "Timestamp": "2023-05-20 16:04:10"
    },
    {
        "Queries per Second": 3807.43,
        "Cache Hit Ratio (%)": 70.9,
        "Connection Count": 40,
        "Average Latency (ms)": 99.3,
        "Timestamp": "2021-01-05 04:34:41"
    },
    {
        "Queries per Second": 3407.7,
        "Cache Hit Ratio (%)": 72.29,
        "Connection Count": 477,
        "Average Latency (ms)": 11.18,
        "Timestamp": "2023-04-11 06:33:02"
    },
    {
        "Queries per Second": 53.11,
        "Cache Hit Ratio (%)": 78.95,
        "Connection Count": 277,
        "Average Latency (ms)": 33.5,
        "Timestamp": "2022-12-07 16:53:20"
    }
]<start>
Queries per Second,Cache Hit Ratio (%),Connection Count,Average Latency (ms),Timestamp
3973.2,92.12,335,68.78,2023-05-20 16:04:10
3807.43,70.9,40,99.3,2021-01-05 04:34:41
3407.7,72.29,477,11.18,2023-04-11 06:33:02
53.11,78.95,277,33.5,2022-12-07 16:53:20
<end>Please transform the following JSON data into plain text:
[
    {
        "Database Name": "ProfilesDB",
        "Queries per Second": 1853.89,
        "Connection Count": 495,
        "Average Latency (ms)": 37.23,
        "Timestamp": "2022-02-08 23:12:26"
    },
    {
        "Database Name": "ProductsDB",
        "Queries per Second": 1314.25,
        "Connection Count": 47,
        "Average Latency (ms)": 33.58,
        "Timestamp": "2022-03-14 05:41:48"
    },
    {
        "Database Name": "ProductsDB",
        "Queries per Second": 894.12,
        "Connection Count": 345,
        "Average Latency (ms)": 51.51,
        "Timestamp": "2021-05-27 05:57:44"
    },
    {
        "Database Name": "InventoryDB",
        "Queries per Second": 1216.7,
        "Connection Count": 332,
        "Average Latency (ms)": 59.06,
        "Timestamp": "2022-11-08 15:24:48"
    },
    {
        "Database Name": "ProfilesDB",
        "Queries per Second": 628.61,
        "Connection Count": 365,
        "Average Latency (ms)": 59.06,
        "Timestamp": "2021-02-11 18:39:31"
    },
    {
        "Database Name": "ProfilesDB",
        "Queries per Second": 4306.68,
        "Connection Count": 346,
        "Average Latency (ms)": 57.47,
        "Timestamp": "2021-12-25 19:42:37"
    },
    {
        "Database Name": "InventoryDB",
        "Queries per Second": 1860.02,
        "Connection Count": 342,
        "Average Latency (ms)": 94.35,
        "Timestamp": "2022-04-28 13:08:58"
    }
]<start>
Database Name: ProfilesDB | Queries per Second: 1853.89 | Connection Count: 495 | Average Latency (ms): 37.23 | Timestamp: 2022-02-08 23:12:26
Database Name: ProductsDB | Queries per Second: 1314.25 | Connection Count: 47 | Average Latency (ms): 33.58 | Timestamp: 2022-03-14 05:41:48
Database Name: ProductsDB | Queries per Second: 894.12 | Connection Count: 345 | Average Latency (ms): 51.51 | Timestamp: 2021-05-27 05:57:44
Database Name: InventoryDB | Queries per Second: 1216.7 | Connection Count: 332 | Average Latency (ms): 59.06 | Timestamp: 2022-11-08 15:24:48
Database Name: ProfilesDB | Queries per Second: 628.61 | Connection Count: 365 | Average Latency (ms): 59.06 | Timestamp: 2021-02-11 18:39:31
Database Name: ProfilesDB | Queries per Second: 4306.68 | Connection Count: 346 | Average Latency (ms): 57.47 | Timestamp: 2021-12-25 19:42:37
Database Name: InventoryDB | Queries per Second: 1860.02 | Connection Count: 342 | Average Latency (ms): 94.35 | Timestamp: 2022-04-28 13:08:58
<end>Convert this yaml to markdown:
- Birth Month: July
  City: Baltimore
- Birth Month: January
  City: Portland
- Birth Month: June
  City: New York
- Birth Month: April
  City: Denver
<start>
| Birth Month | City |
| --- | --- |
| July | Baltimore |
| January | Portland |
| June | New York |
| April | Denver |
<end>Convert this YML to json:
- Box Office Earnings (M): 84.71
  Director: Rylan Frostblade
  Genre: Thriller
  Title: Edge of Infinity
- Box Office Earnings (M): 751.69
  Director: Lira Silverleaf
  Genre: Adventure
  Title: Rise of the Titans
- Box Office Earnings (M): 368.53
  Director: Orin Shadowalker
  Genre: Horror
  Title: Starbound Odyssey
- Box Office Earnings (M): 715.84
  Director: Talon Blackthorn
  Genre: Adventure
  Title: Edge of Infinity
<start>
[
    {
        "Title": "Edge of Infinity",
        "Director": "Rylan Frostblade",
        "Genre": "Thriller",
        "Box Office Earnings (M)": 84.71
    },
    {
        "Title": "Rise of the Titans",
        "Director": "Lira Silverleaf",
        "Genre": "Adventure",
        "Box Office Earnings (M)": 751.69
    },
    {
        "Title": "Starbound Odyssey",
        "Director": "Orin Shadowalker",
        "Genre": "Horror",
        "Box Office Earnings (M)": 368.53
    },
    {
        "Title": "Edge of Infinity",
        "Director": "Talon Blackthorn",
        "Genre": "Adventure",
        "Box Office Earnings (M)": 715.84
    }
]
<end>Please transform the following json data into CSV:
[
    {
        "Company": "BioPharm",
        "Sector": "Automotive",
        "Market Cap": "Mega Cap",
        "Stock Price": 875.43,
        "Annual Revenue (B)": 162.09,
        "Quarter": "Q3"
    },
    {
        "Company": "AeroSpace",
        "Sector": "Energy",
        "Market Cap": "Large Cap",
        "Stock Price": 526.45,
        "Annual Revenue (B)": 437.1,
        "Quarter": "Q3"
    },
    {
        "Company": "AutoDrive",
        "Sector": "Retail",
        "Market Cap": "Small Cap",
        "Stock Price": 98.99,
        "Annual Revenue (B)": 451.63,
        "Quarter": "Q3"
    },
    {
        "Company": "AeroSpace",
        "Sector": "Finance",
        "Market Cap": "Mega Cap",
        "Stock Price": 796.91,
        "Annual Revenue (B)": 431.47,
        "Quarter": "Q4"
    },
    {
        "Company": "Foodies",
        "Sector": "Biotech",
        "Market Cap": "Mega Cap",
        "Stock Price": 304.65,
        "Annual Revenue (B)": 260.9,
        "Quarter": "Q4"
    }
]<start>
Company,Sector,Market Cap,Stock Price,Annual Revenue (B),Quarter
BioPharm,Automotive,Mega Cap,875.43,162.09,Q3
AeroSpace,Energy,Large Cap,526.45,437.1,Q3
AutoDrive,Retail,Small Cap,98.99,451.63,Q3
AeroSpace,Finance,Mega Cap,796.91,431.47,Q4
Foodies,Biotech,Mega Cap,304.65,260.9,Q4
<end>Here's some markdown data, can you convert it to yml?
| Location | Condition | Temperature (C) | Humidity (%) | Wind Speed (km/h) | Day |
| --- | --- | --- | --- | --- | --- |
| New York | Stormy | 11.3 | 62 | 29.1 | Sunday |
| Chicago | Snowy | 25.3 | 73 | 6.2 | Wednesday |
| Phoenix | Foggy | 15.6 | 59 | 15.8 | Sunday |
| Phoenix | Stormy | 14.8 | 35 | 18.2 | Saturday |
| Houston | Windy | 36.8 | 61 | 2.0 | Saturday |
| Houston | Foggy | 17.8 | 64 | 18.2 | Thursday |
| Houston | Cloudy | 26.0 | 70 | 7.7 | Tuesday |<start>
- Condition: Stormy
  Day: Sunday
  Humidity (%): 62
  Location: New York
  Temperature (C): 11.3
  Wind Speed (km/h): 29.1
- Condition: Snowy
  Day: Wednesday
  Humidity (%): 73
  Location: Chicago
  Temperature (C): 25.3
  Wind Speed (km/h): 6.2
- Condition: Foggy
  Day: Sunday
  Humidity (%): 59
  Location: Phoenix
  Temperature (C): 15.6
  Wind Speed (km/h): 15.8
- Condition: Stormy
  Day: Saturday
  Humidity (%): 35
  Location: Phoenix
  Temperature (C): 14.8
  Wind Speed (km/h): 18.2
- Condition: Windy
  Day: Saturday
  Humidity (%): 61
  Location: Houston
  Temperature (C): 36.8
  Wind Speed (km/h): 2.0
- Condition: Foggy
  Day: Thursday
  Humidity (%): 64
  Location: Houston
  Temperature (C): 17.8
  Wind Speed (km/h): 18.2
- Condition: Cloudy
  Day: Tuesday
  Humidity (%): 70
  Location: Houston
  Temperature (C): 26.0
  Wind Speed (km/h): 7.7
<end>Here's some yaml data, can you convert it to json?
- Cuisine: Chinese
  Location: Miami
  Price Range: $
  Rating: 1
  Restaurant Name: The Steakhouse
- Cuisine: Mediterranean
  Location: New York
  Price Range: $$
  Rating: 4
  Restaurant Name: The Golden Spoon
- Cuisine: Indian
  Location: Phoenix
  Price Range: $
  Rating: 1
  Restaurant Name: The Steakhouse
- Cuisine: American
  Location: New York
  Price Range: $
  Rating: 3
  Restaurant Name: Taco Town
- Cuisine: Italian
  Location: Miami
  Price Range: $$$
  Rating: 4
  Restaurant Name: Pizza Planet
- Cuisine: Indian
  Location: Los Angeles
  Price Range: $$$$
  Rating: 3
  Restaurant Name: Curry Corner
- Cuisine: Mexican
  Location: Seattle
  Price Range: $
  Rating: 1
  Restaurant Name: The Golden Spoon
<start>
[
    {
        "Restaurant Name": "The Steakhouse",
        "Cuisine": "Chinese",
        "Location": "Miami",
        "Rating": 1,
        "Price Range": "$"
    },
    {
        "Restaurant Name": "The Golden Spoon",
        "Cuisine": "Mediterranean",
        "Location": "New York",
        "Rating": 4,
        "Price Range": "$$"
    },
    {
        "Restaurant Name": "The Steakhouse",
        "Cuisine": "Indian",
        "Location": "Phoenix",
        "Rating": 1,
        "Price Range": "$"
    },
    {
        "Restaurant Name": "Taco Town",
        "Cuisine": "American",
        "Location": "New York",
        "Rating": 3,
        "Price Range": "$"
    },
    {
        "Restaurant Name": "Pizza Planet",
        "Cuisine": "Italian",
        "Location": "Miami",
        "Rating": 4,
        "Price Range": "$$$"
    },
    {
        "Restaurant Name": "Curry Corner",
        "Cuisine": "Indian",
        "Location": "Los Angeles",
        "Rating": 3,
        "Price Range": "$$$$"
    },
    {
        "Restaurant Name": "The Golden Spoon",
        "Cuisine": "Mexican",
        "Location": "Seattle",
        "Rating": 1,
        "Price Range": "$"
    }
]
<end>Please transform the following Plain text data into csv:
Condition: Rainy | Temperature (C): 16.9 | Humidity (%): 78 | Wind Speed (km/h): 12.7 | Day: Monday
Condition: Windy | Temperature (C): -5.6 | Humidity (%): 75 | Wind Speed (km/h): 20.1 | Day: Monday
Condition: Stormy | Temperature (C): 7.0 | Humidity (%): 20 | Wind Speed (km/h): 27.8 | Day: Friday
Condition: Snowy | Temperature (C): 12.5 | Humidity (%): 56 | Wind Speed (km/h): 18.0 | Day: Sunday
Condition: Stormy | Temperature (C): 36.4 | Humidity (%): 68 | Wind Speed (km/h): 22.0 | Day: Thursday
Condition: Stormy | Temperature (C): 30.2 | Humidity (%): 56 | Wind Speed (km/h): 27.8 | Day: Monday
Condition: Foggy | Temperature (C): 25.5 | Humidity (%): 29 | Wind Speed (km/h): 18.6 | Day: Monday
Condition: Snowy | Temperature (C): 19.0 | Humidity (%): 41 | Wind Speed (km/h): 23.6 | Day: Thursday
<start>
Condition,Temperature (C),Humidity (%),Wind Speed (km/h),Day
Rainy,16.9,78,12.7,Monday
Windy,-5.6,75,20.1,Monday
Stormy,7.0,20,27.8,Friday
Snowy,12.5,56,18.0,Sunday
Stormy,36.4,68,22.0,Thursday
Stormy,30.2,56,27.8,Monday
Foggy,25.5,29,18.6,Monday
Snowy,19.0,41,23.6,Thursday
<end>Transform this markdown structure to a csv format:
| Date | Open Price | Close Price | High Price | Low Price | Volume |
| --- | --- | --- | --- | --- | --- |
| 2022-04-09 | 623.7 | 412.49 | 970.13 | 192.42 | 8703942 |
| 2022-08-01 | 1360.83 | 963.77 | 1360.83 | 322.95 | 7210727 |
| 2015-03-28 | 73.87 | 184.72 | 184.72 | 73.87 | 3744492 |
| 2021-10-07 | 230.25 | 1360.83 | 1360.83 | 230.25 | 7168410 |
| 2022-07-12 | 1122.98 | 1325.96 | 1325.96 | 1122.98 | 8076507 |
| 2010-09-26 | 230.25 | 845.85 | 845.85 | 176.91 | 8582277 |<start>
Date,Open Price,Close Price,High Price,Low Price,Volume
2022-04-09,623.7,412.49,970.13,192.42,8703942
2022-08-01,1360.83,963.77,1360.83,322.95,7210727
2015-03-28,73.87,184.72,184.72,73.87,3744492
2021-10-07,230.25,1360.83,1360.83,230.25,7168410
2022-07-12,1122.98,1325.96,1325.96,1122.98,8076507
2010-09-26,230.25,845.85,845.85,176.91,8582277
<end>Transform this Yaml structure to a CSV format:
- Distance (miles): 669.9
  Duration (hours): 50.9
  End Location: Houston
  Fuel Used (gallons): 24.9
  Start Location: San Francisco
  Trip Name: Historic Route
- Distance (miles): 2035.4
  Duration (hours): 11.4
  End Location: Chicago
  Fuel Used (gallons): 5.6
  Start Location: San Francisco
  Trip Name: Forest Journey
- Distance (miles): 1715.8
  Duration (hours): 54.0
  End Location: Los Angeles
  Fuel Used (gallons): 32.3
  Start Location: San Francisco
  Trip Name: Highway Odyssey
- Distance (miles): 1856.9
  Duration (hours): 24.1
  End Location: Phoenix
  Fuel Used (gallons): 72.6
  Start Location: Los Angeles
  Trip Name: Historic Route
- Distance (miles): 2441.0
  Duration (hours): 31.2
  End Location: San Francisco
  Fuel Used (gallons): 9.5
  Start Location: New York
  Trip Name: City Explorer
- Distance (miles): 2314.8
  Duration (hours): 26.7
  End Location: San Francisco
  Fuel Used (gallons): 91.1
  Start Location: New York
  Trip Name: Canyon Trek
- Distance (miles): 2744.6
  Duration (hours): 1.5
  End Location: Chicago
  Fuel Used (gallons): 60.5
  Start Location: Houston
  Trip Name: Forest Journey
- Distance (miles): 2392.3
  Duration (hours): 40.3
  End Location: New York
  Fuel Used (gallons): 77.7
  Start Location: Houston
  Trip Name: Highway Odyssey
<start>
Trip Name,Start Location,End Location,Distance (miles),Duration (hours),Fuel Used (gallons)
Historic Route,San Francisco,Houston,669.9,50.9,24.9
Forest Journey,San Francisco,Chicago,2035.4,11.4,5.6
Highway Odyssey,San Francisco,Los Angeles,1715.8,54.0,32.3
Historic Route,Los Angeles,Phoenix,1856.9,24.1,72.6
City Explorer,New York,San Francisco,2441.0,31.2,9.5
Canyon Trek,New York,San Francisco,2314.8,26.7,91.1
Forest Journey,Houston,Chicago,2744.6,1.5,60.5
Highway Odyssey,Houston,New York,2392.3,40.3,77.7
<end>Please transform the following Markdown data into YML:
| Start Location | End Location | Duration (hours) | Fuel Used (gallons) |
| --- | --- | --- | --- |
| San Francisco | Denver | 9.7 | 44.1 |
| Houston | Phoenix | 15.0 | 44.1 |
| Los Angeles | San Francisco | 56.0 | 79.2 |
| Houston | Miami | 21.8 | 14.5 |
| Chicago | New York | 18.4 | 16.2 |
| Phoenix | San Francisco | 51.2 | 92.7 |
| New York | Phoenix | 47.5 | 58.7 |
| Denver | Miami | 22.0 | 98.2 |<start>
- Duration (hours): 9.7
  End Location: Denver
  Fuel Used (gallons): 44.1
  Start Location: San Francisco
- Duration (hours): 15.0
  End Location: Phoenix
  Fuel Used (gallons): 44.1
  Start Location: Houston
- Duration (hours): 56.0
  End Location: San Francisco
  Fuel Used (gallons): 79.2
  Start Location: Los Angeles
- Duration (hours): 21.8
  End Location: Miami
  Fuel Used (gallons): 14.5
  Start Location: Houston
- Duration (hours): 18.4
  End Location: New York
  Fuel Used (gallons): 16.2
  Start Location: Chicago
- Duration (hours): 51.2
  End Location: San Francisco
  Fuel Used (gallons): 92.7
  Start Location: Phoenix
- Duration (hours): 47.5
  End Location: Phoenix
  Fuel Used (gallons): 58.7
  Start Location: New York
- Duration (hours): 22.0
  End Location: Miami
  Fuel Used (gallons): 98.2
  Start Location: Denver
<end>Can you change this Csv into markdown?
Age,Birth Month
52,November
26,January
66,August
44,July
21,November
30,February
69,August
<start>
| Age | Birth Month |
| --- | --- |
| 52 | November |
| 26 | January |
| 66 | August |
| 44 | July |
| 21 | November |
| 30 | February |
| 69 | August |
<end>Here's some Json data, can you convert it to YAML?
[
    {
        "Trip Name": "Forest Journey",
        "Start Location": "Denver",
        "Distance (miles)": 2049.6,
        "Fuel Used (gallons)": 74.3
    },
    {
        "Trip Name": "Valley Voyage",
        "Start Location": "Denver",
        "Distance (miles)": 420.9,
        "Fuel Used (gallons)": 66.9
    },
    {
        "Trip Name": "Forest Journey",
        "Start Location": "New York",
        "Distance (miles)": 2344.3,
        "Fuel Used (gallons)": 94.8
    },
    {
        "Trip Name": "Valley Voyage",
        "Start Location": "Phoenix",
        "Distance (miles)": 1683.4,
        "Fuel Used (gallons)": 42.8
    },
    {
        "Trip Name": "Desert Drive",
        "Start Location": "Houston",
        "Distance (miles)": 395.9,
        "Fuel Used (gallons)": 99.9
    },
    {
        "Trip Name": "Canyon Trek",
        "Start Location": "New York",
        "Distance (miles)": 2525.2,
        "Fuel Used (gallons)": 57.5
    },
    {
        "Trip Name": "Highway Odyssey",
        "Start Location": "Denver",
        "Distance (miles)": 2534.1,
        "Fuel Used (gallons)": 13.8
    }
]<start>
- Distance (miles): 2049.6
  Fuel Used (gallons): 74.3
  Start Location: Denver
  Trip Name: Forest Journey
- Distance (miles): 420.9
  Fuel Used (gallons): 66.9
  Start Location: Denver
  Trip Name: Valley Voyage
- Distance (miles): 2344.3
  Fuel Used (gallons): 94.8
  Start Location: New York
  Trip Name: Forest Journey
- Distance (miles): 1683.4
  Fuel Used (gallons): 42.8
  Start Location: Phoenix
  Trip Name: Valley Voyage
- Distance (miles): 395.9
  Fuel Used (gallons): 99.9
  Start Location: Houston
  Trip Name: Desert Drive
- Distance (miles): 2525.2
  Fuel Used (gallons): 57.5
  Start Location: New York
  Trip Name: Canyon Trek
- Distance (miles): 2534.1
  Fuel Used (gallons): 13.8
  Start Location: Denver
  Trip Name: Highway Odyssey
<end>Transform this plain text structure to a yml format:
Genre: Science Fiction | Publication Year: 1992
Genre: Mystery | Publication Year: 1985
Genre: Science Fiction | Publication Year: 1992
Genre: Historical | Publication Year: 1987
Genre: Thriller | Publication Year: 1962
Genre: Horror | Publication Year: 1964
Genre: Romance | Publication Year: 1958
Genre: Thriller | Publication Year: 1962
<start>
- Genre: Science Fiction
  Publication Year: 1992
- Genre: Mystery
  Publication Year: 1985
- Genre: Science Fiction
  Publication Year: 1992
- Genre: Historical
  Publication Year: 1987
- Genre: Thriller
  Publication Year: 1962
- Genre: Horror
  Publication Year: 1964
- Genre: Romance
  Publication Year: 1958
- Genre: Thriller
  Publication Year: 1962
<end>Transform this yml structure to a Plain text format:
- Distance (miles): 342.6
  Duration (hours): 66.6
  End Location: Denver
  Fuel Used (gallons): 6.8
  Start Location: New York
  Trip Name: Highway Odyssey
- Distance (miles): 2273.2
  Duration (hours): 54.6
  End Location: Miami
  Fuel Used (gallons): 40.2
  Start Location: Houston
  Trip Name: Historic Route
- Distance (miles): 661.4
  Duration (hours): 20.3
  End Location: San Francisco
  Fuel Used (gallons): 44.8
  Start Location: Los Angeles
  Trip Name: Coast to Coast
- Distance (miles): 1331.1
  Duration (hours): 28.8
  End Location: Chicago
  Fuel Used (gallons): 75.2
  Start Location: Los Angeles
  Trip Name: Historic Route
- Distance (miles): 2017.6
  Duration (hours): 18.6
  End Location: San Francisco
  Fuel Used (gallons): 61.0
  Start Location: New York
  Trip Name: Lakeside Retreat
- Distance (miles): 1352.4
  Duration (hours): 33.9
  End Location: Los Angeles
  Fuel Used (gallons): 43.1
  Start Location: Denver
  Trip Name: Forest Journey
- Distance (miles): 1585.9
  Duration (hours): 65.1
  End Location: Denver
  Fuel Used (gallons): 93.7
  Start Location: San Francisco
  Trip Name: Desert Drive
<start>
Trip Name: Highway Odyssey | Start Location: New York | End Location: Denver | Distance (miles): 342.6 | Duration (hours): 66.6 | Fuel Used (gallons): 6.8
Trip Name: Historic Route | Start Location: Houston | End Location: Miami | Distance (miles): 2273.2 | Duration (hours): 54.6 | Fuel Used (gallons): 40.2
Trip Name: Coast to Coast | Start Location: Los Angeles | End Location: San Francisco | Distance (miles): 661.4 | Duration (hours): 20.3 | Fuel Used (gallons): 44.8
Trip Name: Historic Route | Start Location: Los Angeles | End Location: Chicago | Distance (miles): 1331.1 | Duration (hours): 28.8 | Fuel Used (gallons): 75.2
Trip Name: Lakeside Retreat | Start Location: New York | End Location: San Francisco | Distance (miles): 2017.6 | Duration (hours): 18.6 | Fuel Used (gallons): 61.0
Trip Name: Forest Journey | Start Location: Denver | End Location: Los Angeles | Distance (miles): 1352.4 | Duration (hours): 33.9 | Fuel Used (gallons): 43.1
Trip Name: Desert Drive | Start Location: San Francisco | End Location: Denver | Distance (miles): 1585.9 | Duration (hours): 65.1 | Fuel Used (gallons): 93.7
<end>Convert this PLAIN TEXT to CSV:
Device ID: device-0066 | Device Type: Motion Detector | Location: Living Room | Timestamp: 2022-02-21 22:47:18
Device ID: device-0054 | Device Type: Humidity Sensor | Location: Garden | Timestamp: 2023-10-01 01:43:26
Device ID: device-0036 | Device Type: Light Sensor | Location: Garage | Timestamp: 2023-04-15 08:12:17
Device ID: device-0068 | Device Type: Temperature Sensor | Location: Living Room | Timestamp: 2023-07-22 17:58:29
Device ID: device-0022 | Device Type: Light Sensor | Location: Bathroom | Timestamp: 2022-10-03 17:48:28
Device ID: device-0029 | Device Type: Light Sensor | Location: Office | Timestamp: 2021-06-21 06:36:31
<start>
Device ID,Device Type,Location,Timestamp
device-0066,Motion Detector,Living Room,2022-02-21 22:47:18
device-0054,Humidity Sensor,Garden,2023-10-01 01:43:26
device-0036,Light Sensor,Garage,2023-04-15 08:12:17
device-0068,Temperature Sensor,Living Room,2023-07-22 17:58:29
device-0022,Light Sensor,Bathroom,2022-10-03 17:48:28
device-0029,Light Sensor,Office,2021-06-21 06:36:31
<end>Transform this plain text structure to a CSV format:
Name: Irene | Age: 34 | City: Portland
Name: Deanna | Age: 59 | City: Portland
Name: Harmony | Age: 37 | City: Denver
Name: Susie | Age: 62 | City: Austin
Name: Faye | Age: 19 | City: Memphis
Name: Roberta | Age: 67 | City: Jacksonville
Name: Nolan | Age: 42 | City: Indianapolis
Name: Aubree | Age: 52 | City: Portland
Name: Devin | Age: 18 | City: Indianapolis
Name: Dustin | Age: 31 | City: Nashville
<start>
Name,Age,City
Irene,34,Portland
Deanna,59,Portland
Harmony,37,Denver
Susie,62,Austin
Faye,19,Memphis
Roberta,67,Jacksonville
Nolan,42,Indianapolis
Aubree,52,Portland
Devin,18,Indianapolis
Dustin,31,Nashville
<end>Here's some json data, can you convert it to Plain text?
[
    {
        "Title": "The Great Expedition",
        "Genre": "Action"
    },
    {
        "Title": "The Endless Horizon",
        "Genre": "Thriller"
    },
    {
        "Title": "Mystery of the Depths",
        "Genre": "Fantasy"
    },
    {
        "Title": "Escape from Earth",
        "Genre": "Fantasy"
    },
    {
        "Title": "Beyond the Veil",
        "Genre": "Horror"
    },
    {
        "Title": "Starbound Odyssey",
        "Genre": "Adventure"
    },
    {
        "Title": "The Endless Horizon",
        "Genre": "Fantasy"
    },
    {
        "Title": "Escape from Earth",
        "Genre": "Comedy"
    }
]<start>
Title: The Great Expedition | Genre: Action
Title: The Endless Horizon | Genre: Thriller
Title: Mystery of the Depths | Genre: Fantasy
Title: Escape from Earth | Genre: Fantasy
Title: Beyond the Veil | Genre: Horror
Title: Starbound Odyssey | Genre: Adventure
Title: The Endless Horizon | Genre: Fantasy
Title: Escape from Earth | Genre: Comedy
<end>Convert this json to markdown:
[
    {
        "Database Name": "SalesDB",
        "Queries per Second": 4211.16,
        "Cache Hit Ratio (%)": 75.53,
        "Connection Count": 463,
        "Average Latency (ms)": 65.72,
        "Timestamp": "2023-12-08 06:09:30"
    },
    {
        "Database Name": "AnalyticsDB",
        "Queries per Second": 4196.94,
        "Cache Hit Ratio (%)": 86.26,
        "Connection Count": 244,
        "Average Latency (ms)": 13.74,
        "Timestamp": "2021-03-17 12:11:28"
    },
    {
        "Database Name": "AnalyticsDB",
        "Queries per Second": 2254.22,
        "Cache Hit Ratio (%)": 83.72,
        "Connection Count": 113,
        "Average Latency (ms)": 98.7,
        "Timestamp": "2023-05-02 08:33:59"
    },
    {
        "Database Name": "ProfilesDB",
        "Queries per Second": 1044.74,
        "Cache Hit Ratio (%)": 88.07,
        "Connection Count": 216,
        "Average Latency (ms)": 81.43,
        "Timestamp": "2023-04-08 00:49:50"
    },
    {
        "Database Name": "AnalyticsDB",
        "Queries per Second": 1252.89,
        "Cache Hit Ratio (%)": 76.13,
        "Connection Count": 218,
        "Average Latency (ms)": 57.07,
        "Timestamp": "2023-12-08 16:45:30"
    },
    {
        "Database Name": "LogsDB",
        "Queries per Second": 2523.85,
        "Cache Hit Ratio (%)": 83.77,
        "Connection Count": 303,
        "Average Latency (ms)": 58.4,
        "Timestamp": "2023-09-06 13:27:51"
    },
    {
        "Database Name": "OrdersDB",
        "Queries per Second": 4974.22,
        "Cache Hit Ratio (%)": 87.82,
        "Connection Count": 80,
        "Average Latency (ms)": 28.4,
        "Timestamp": "2022-01-15 20:21:36"
    }
]<start>
| Database Name | Queries per Second | Cache Hit Ratio (%) | Connection Count | Average Latency (ms) | Timestamp |
| --- | --- | --- | --- | --- | --- |
| SalesDB | 4211.16 | 75.53 | 463 | 65.72 | 2023-12-08 06:09:30 |
| AnalyticsDB | 4196.94 | 86.26 | 244 | 13.74 | 2021-03-17 12:11:28 |
| AnalyticsDB | 2254.22 | 83.72 | 113 | 98.7 | 2023-05-02 08:33:59 |
| ProfilesDB | 1044.74 | 88.07 | 216 | 81.43 | 2023-04-08 00:49:50 |
| AnalyticsDB | 1252.89 | 76.13 | 218 | 57.07 | 2023-12-08 16:45:30 |
| LogsDB | 2523.85 | 83.77 | 303 | 58.4 | 2023-09-06 13:27:51 |
| OrdersDB | 4974.22 | 87.82 | 80 | 28.4 | 2022-01-15 20:21:36 |
<end>Can you change this yml into plain text?
- Box Office Earnings (M): 321.78
  Director: Orin Shadowalker
  Genre: Thriller
  Release Year: 2020
  Title: Rise of the Titans
- Box Office Earnings (M): 90.63
  Director: Lira Silverleaf
  Genre: Comedy
  Release Year: 2020
  Title: The Endless Horizon
- Box Office Earnings (M): 65.75
  Director: Orin Shadowalker
  Genre: Adventure
  Release Year: 1979
  Title: Rise of the Titans
- Box Office Earnings (M): 751.09
  Director: Cade Firebrand
  Genre: Action
  Release Year: 1994
  Title: The Final Voyage
- Box Office Earnings (M): 857.67
  Director: Drake Nightshade
  Genre: Drama
  Release Year: 2005
  Title: Escape from Earth
- Box Office Earnings (M): 469.12
  Director: Zara Stormrider
  Genre: Action
  Release Year: 1987
  Title: The Great Expedition
- Box Office Earnings (M): 663.53
  Director: Talon Blackthorn
  Genre: Thriller
  Release Year: 1995
  Title: Starbound Odyssey
- Box Office Earnings (M): 348.79
  Director: Selene Darkwhisper
  Genre: Drama
  Release Year: 1972
  Title: Starbound Odyssey
<start>
Title: Rise of the Titans | Director: Orin Shadowalker | Genre: Thriller | Release Year: 2020 | Box Office Earnings (M): 321.78
Title: The Endless Horizon | Director: Lira Silverleaf | Genre: Comedy | Release Year: 2020 | Box Office Earnings (M): 90.63
Title: Rise of the Titans | Director: Orin Shadowalker | Genre: Adventure | Release Year: 1979 | Box Office Earnings (M): 65.75
Title: The Final Voyage | Director: Cade Firebrand | Genre: Action | Release Year: 1994 | Box Office Earnings (M): 751.09
Title: Escape from Earth | Director: Drake Nightshade | Genre: Drama | Release Year: 2005 | Box Office Earnings (M): 857.67
Title: The Great Expedition | Director: Zara Stormrider | Genre: Action | Release Year: 1987 | Box Office Earnings (M): 469.12
Title: Starbound Odyssey | Director: Talon Blackthorn | Genre: Thriller | Release Year: 1995 | Box Office Earnings (M): 663.53
Title: Starbound Odyssey | Director: Selene Darkwhisper | Genre: Drama | Release Year: 1972 | Box Office Earnings (M): 348.79
<end>Convert this yml to markdown:
- Company: BioLife
  Date: '2010-09-10'
  High Price: 1184.16
  Low Price: 259.85
- Company: GreenEnergy
  Date: '2015-03-24'
  High Price: 777.06
  Low Price: 574.55
- Company: BioLife
  Date: '2013-08-17'
  High Price: 1307.54
  Low Price: 341.71
- Company: MediaGroup
  Date: '2020-03-26'
  High Price: 1321.05
  Low Price: 259.85
- Company: MediaGroup
  Date: '2012-01-06'
  High Price: 937.4
  Low Price: 345.1
- Company: MediaGroup
  Date: '2017-01-17'
  High Price: 1373.76
  Low Price: 462.41
- Company: BioLife
  Date: '2010-07-10'
  High Price: 749.66
  Low Price: 79.54
- Company: AutoMotive
  Date: '2013-01-04'
  High Price: 843.7
  Low Price: 79.54
<start>
| Company | Date | High Price | Low Price |
| --- | --- | --- | --- |
| BioLife | 2010-09-10 | 1184.16 | 259.85 |
| GreenEnergy | 2015-03-24 | 777.06 | 574.55 |
| BioLife | 2013-08-17 | 1307.54 | 341.71 |
| MediaGroup | 2020-03-26 | 1321.05 | 259.85 |
| MediaGroup | 2012-01-06 | 937.4 | 345.1 |
| MediaGroup | 2017-01-17 | 1373.76 | 462.41 |
| BioLife | 2010-07-10 | 749.66 | 79.54 |
| AutoMotive | 2013-01-04 | 843.7 | 79.54 |
<end>Please transform the following markdown data into yaml:
| City | Income |
| --- | --- |
| Louisville | 170000 |
| Indianapolis | 55000 |
| El Paso | 390000 |
| San Antonio | 375000 |
| San Diego | 275000 |
| Jacksonville | 470000 |
| San Francisco | 275000 |
| Detroit | 280000 |
| Detroit | 120000 |
| Louisville | 125000 |<start>
- City: Louisville
  Income: 170000
- City: Indianapolis
  Income: 55000
- City: El Paso
  Income: 390000
- City: San Antonio
  Income: 375000
- City: San Diego
  Income: 275000
- City: Jacksonville
  Income: 470000
- City: San Francisco
  Income: 275000
- City: Detroit
  Income: 280000
- City: Detroit
  Income: 120000
- City: Louisville
  Income: 125000
<end>Convert this plain text to Markdown:
Trip Name: Mountain Adventure | Start Location: New York | End Location: San Francisco | Distance (miles): 1851.3 | Duration (hours): 5.5 | Fuel Used (gallons): 92.7
Trip Name: City Explorer | Start Location: Miami | End Location: Los Angeles | Distance (miles): 929.3 | Duration (hours): 43.2 | Fuel Used (gallons): 62.1
Trip Name: Forest Journey | Start Location: Phoenix | End Location: New York | Distance (miles): 1908.4 | Duration (hours): 29.1 | Fuel Used (gallons): 25.5
Trip Name: Lakeside Retreat | Start Location: Chicago | End Location: New York | Distance (miles): 2022.4 | Duration (hours): 4.0 | Fuel Used (gallons): 31.2
Trip Name: Lakeside Retreat | Start Location: New York | End Location: Denver | Distance (miles): 2262.6 | Duration (hours): 42.1 | Fuel Used (gallons): 26.2
<start>
| Trip Name | Start Location | End Location | Distance (miles) | Duration (hours) | Fuel Used (gallons) |
| --- | --- | --- | --- | --- | --- |
| Mountain Adventure | New York | San Francisco | 1851.3 | 5.5 | 92.7 |
| City Explorer | Miami | Los Angeles | 929.3 | 43.2 | 62.1 |
| Forest Journey | Phoenix | New York | 1908.4 | 29.1 | 25.5 |
| Lakeside Retreat | Chicago | New York | 2022.4 | 4.0 | 31.2 |
| Lakeside Retreat | New York | Denver | 2262.6 | 42.1 | 26.2 |
<end>Please transform the following Csv data into yaml:
Title,Author,Genre,Publication Year
Tales of the Brave,Luna Silverleaf,Mystery,1987
Legends of the Rift,Galen Starfire,Thriller,1990
The Last Sky,Sylvia Nightshade,Historical,1960
A Journey Through Time,Elara Moonshadow,Science Fiction,2021
Legends of the Rift,Draven Blackthorn,Fantasy,1960
Echoes of Eternity,Thorne Ironwood,Romance,1965
The Forgotten World,Sylvia Nightshade,Science Fiction,1987
<start>
- Author: Luna Silverleaf
  Genre: Mystery
  Publication Year: 1987
  Title: Tales of the Brave
- Author: Galen Starfire
  Genre: Thriller
  Publication Year: 1990
  Title: Legends of the Rift
- Author: Sylvia Nightshade
  Genre: Historical
  Publication Year: 1960
  Title: The Last Sky
- Author: Elara Moonshadow
  Genre: Science Fiction
  Publication Year: 2021
  Title: A Journey Through Time
- Author: Draven Blackthorn
  Genre: Fantasy
  Publication Year: 1960
  Title: Legends of the Rift
- Author: Thorne Ironwood
  Genre: Romance
  Publication Year: 1965
  Title: Echoes of Eternity
- Author: Sylvia Nightshade
  Genre: Science Fiction
  Publication Year: 1987
  Title: The Forgotten World
<end>Can you change this CSV into PLAIN TEXT?
Location,Condition,Humidity (%),Wind Speed (km/h),Day
Miami,Cloudy,50,28.9,Sunday
Miami,Foggy,90,13.5,Saturday
Los Angeles,Snowy,63,0.2,Friday
Los Angeles,Rainy,67,15.6,Tuesday
<start>
Location: Miami | Condition: Cloudy | Humidity (%): 50 | Wind Speed (km/h): 28.9 | Day: Sunday
Location: Miami | Condition: Foggy | Humidity (%): 90 | Wind Speed (km/h): 13.5 | Day: Saturday
Location: Los Angeles | Condition: Snowy | Humidity (%): 63 | Wind Speed (km/h): 0.2 | Day: Friday
Location: Los Angeles | Condition: Rainy | Humidity (%): 67 | Wind Speed (km/h): 15.6 | Day: Tuesday
<end>Convert this plain text to Markdown:
Database Name: UserDB | Queries per Second: 233.07 | Connection Count: 120 | Average Latency (ms): 92.29 | Timestamp: 2023-10-15 07:24:47
Database Name: MetricsDB | Queries per Second: 467.82 | Connection Count: 271 | Average Latency (ms): 42.19 | Timestamp: 2021-09-09 05:59:15
Database Name: SessionsDB | Queries per Second: 2777.87 | Connection Count: 262 | Average Latency (ms): 67.19 | Timestamp: 2023-10-21 08:46:18
<start>
| Database Name | Queries per Second | Connection Count | Average Latency (ms) | Timestamp |
| --- | --- | --- | --- | --- |
| UserDB | 233.07 | 120 | 92.29 | 2023-10-15 07:24:47 |
| MetricsDB | 467.82 | 271 | 42.19 | 2021-09-09 05:59:15 |
| SessionsDB | 2777.87 | 262 | 67.19 | 2023-10-21 08:46:18 |
<end>Please transform the following JSON data into MARKDOWN:
[
    {
        "Product Name": "Device",
        "SKU": "SKU-1053",
        "Price": 118.14,
        "Stock Quantity": 182
    },
    {
        "Product Name": "Instrument",
        "SKU": "SKU-1052",
        "Price": 335.4,
        "Stock Quantity": 194
    },
    {
        "Product Name": "Apparatus",
        "SKU": "SKU-1056",
        "Price": 19.87,
        "Stock Quantity": 477
    },
    {
        "Product Name": "Widget",
        "SKU": "SKU-1020",
        "Price": 84.87,
        "Stock Quantity": 282
    },
    {
        "Product Name": "Whatchamacallit",
        "SKU": "SKU-1011",
        "Price": 226.1,
        "Stock Quantity": 125
    },
    {
        "Product Name": "Whatchamacallit",
        "SKU": "SKU-1094",
        "Price": 173.58,
        "Stock Quantity": 464
    },
    {
        "Product Name": "Instrument",
        "SKU": "SKU-1012",
        "Price": 498.08,
        "Stock Quantity": 214
    },
    {
        "Product Name": "Whatchamacallit",
        "SKU": "SKU-1000",
        "Price": 27.65,
        "Stock Quantity": 119
    },
    {
        "Product Name": "Device",
        "SKU": "SKU-1050",
        "Price": 465.47,
        "Stock Quantity": 118
    },
    {
        "Product Name": "Gizmo",
        "SKU": "SKU-1097",
        "Price": 13.21,
        "Stock Quantity": 54
    }
]<start>
| Product Name | SKU | Price | Stock Quantity |
| --- | --- | --- | --- |
| Device | SKU-1053 | 118.14 | 182 |
| Instrument | SKU-1052 | 335.4 | 194 |
| Apparatus | SKU-1056 | 19.87 | 477 |
| Widget | SKU-1020 | 84.87 | 282 |
| Whatchamacallit | SKU-1011 | 226.1 | 125 |
| Whatchamacallit | SKU-1094 | 173.58 | 464 |
| Instrument | SKU-1012 | 498.08 | 214 |
| Whatchamacallit | SKU-1000 | 27.65 | 119 |
| Device | SKU-1050 | 465.47 | 118 |
| Gizmo | SKU-1097 | 13.21 | 54 |
<end>Convert this YAML to json:
- Cuisine: Chinese
  Price Range: $$
  Rating: 5
- Cuisine: American
  Price Range: $$$$$
  Rating: 2
- Cuisine: American
  Price Range: $
  Rating: 1
- Cuisine: Mexican
  Price Range: $
  Rating: 1
- Cuisine: Mediterranean
  Price Range: $$$$
  Rating: 1
- Cuisine: American
  Price Range: $$$$$
  Rating: 5
- Cuisine: Mexican
  Price Range: $
  Rating: 3
- Cuisine: Mediterranean
  Price Range: $
  Rating: 1
<start>
[
    {
        "Cuisine": "Chinese",
        "Rating": 5,
        "Price Range": "$$"
    },
    {
        "Cuisine": "American",
        "Rating": 2,
        "Price Range": "$$$$$"
    },
    {
        "Cuisine": "American",
        "Rating": 1,
        "Price Range": "$"
    },
    {
        "Cuisine": "Mexican",
        "Rating": 1,
        "Price Range": "$"
    },
    {
        "Cuisine": "Mediterranean",
        "Rating": 1,
        "Price Range": "$$$$"
    },
    {
        "Cuisine": "American",
        "Rating": 5,
        "Price Range": "$$$$$"
    },
    {
        "Cuisine": "Mexican",
        "Rating": 3,
        "Price Range": "$"
    },
    {
        "Cuisine": "Mediterranean",
        "Rating": 1,
        "Price Range": "$"
    }
]
<end>Here's some Json data, can you convert it to PLAIN TEXT?
[
    {
        "Start Location": "Miami",
        "End Location": "Denver",
        "Distance (miles)": 684.0,
        "Duration (hours)": 30.4,
        "Fuel Used (gallons)": 55.5
    },
    {
        "Start Location": "Miami",
        "End Location": "Phoenix",
        "Distance (miles)": 1173.1,
        "Duration (hours)": 63.7,
        "Fuel Used (gallons)": 85.6
    },
    {
        "Start Location": "Denver",
        "End Location": "Miami",
        "Distance (miles)": 2361.7,
        "Duration (hours)": 32.9,
        "Fuel Used (gallons)": 88.9
    },
    {
        "Start Location": "Los Angeles",
        "End Location": "Miami",
        "Distance (miles)": 818.2,
        "Duration (hours)": 4.8,
        "Fuel Used (gallons)": 79.7
    },
    {
        "Start Location": "San Francisco",
        "End Location": "New York",
        "Distance (miles)": 1519.0,
        "Duration (hours)": 37.6,
        "Fuel Used (gallons)": 97.7
    },
    {
        "Start Location": "New York",
        "End Location": "Miami",
        "Distance (miles)": 1227.3,
        "Duration (hours)": 49.1,
        "Fuel Used (gallons)": 17.9
    },
    {
        "Start Location": "Los Angeles",
        "End Location": "New York",
        "Distance (miles)": 1754.0,
        "Duration (hours)": 16.5,
        "Fuel Used (gallons)": 18.1
    },
    {
        "Start Location": "San Francisco",
        "End Location": "Miami",
        "Distance (miles)": 580.8,
        "Duration (hours)": 63.0,
        "Fuel Used (gallons)": 55.5
    },
    {
        "Start Location": "New York",
        "End Location": "Houston",
        "Distance (miles)": 2948.4,
        "Duration (hours)": 10.5,
        "Fuel Used (gallons)": 87.6
    }
]<start>
Start Location: Miami | End Location: Denver | Distance (miles): 684.0 | Duration (hours): 30.4 | Fuel Used (gallons): 55.5
Start Location: Miami | End Location: Phoenix | Distance (miles): 1173.1 | Duration (hours): 63.7 | Fuel Used (gallons): 85.6
Start Location: Denver | End Location: Miami | Distance (miles): 2361.7 | Duration (hours): 32.9 | Fuel Used (gallons): 88.9
Start Location: Los Angeles | End Location: Miami | Distance (miles): 818.2 | Duration (hours): 4.8 | Fuel Used (gallons): 79.7
Start Location: San Francisco | End Location: New York | Distance (miles): 1519.0 | Duration (hours): 37.6 | Fuel Used (gallons): 97.7
Start Location: New York | End Location: Miami | Distance (miles): 1227.3 | Duration (hours): 49.1 | Fuel Used (gallons): 17.9
Start Location: Los Angeles | End Location: New York | Distance (miles): 1754.0 | Duration (hours): 16.5 | Fuel Used (gallons): 18.1
Start Location: San Francisco | End Location: Miami | Distance (miles): 580.8 | Duration (hours): 63.0 | Fuel Used (gallons): 55.5
Start Location: New York | End Location: Houston | Distance (miles): 2948.4 | Duration (hours): 10.5 | Fuel Used (gallons): 87.6
<end>Transform this json structure to a csv format:
[
    {
        "Company": "HealthGen",
        "Date": "2012-09-18",
        "Open Price": 43.71,
        "Close Price": 1392.58,
        "Volume": 7853316
    },
    {
        "Company": "RetailWorld",
        "Date": "2018-12-23",
        "Open Price": 265.02,
        "Close Price": 909.59,
        "Volume": 7361861
    },
    {
        "Company": "AutoMotive",
        "Date": "2012-11-17",
        "Open Price": 1144.97,
        "Close Price": 842.45,
        "Volume": 1814065
    },
    {
        "Company": "BioLife",
        "Date": "2019-06-21",
        "Open Price": 1018.52,
        "Close Price": 897.06,
        "Volume": 2008574
    },
    {
        "Company": "AeroSystems",
        "Date": "2011-12-26",
        "Open Price": 160.76,
        "Close Price": 363.73,
        "Volume": 7412826
    },
    {
        "Company": "BioLife",
        "Date": "2023-02-08",
        "Open Price": 196.26,
        "Close Price": 645.82,
        "Volume": 7436867
    },
    {
        "Company": "BioLife",
        "Date": "2016-07-24",
        "Open Price": 313.83,
        "Close Price": 1144.97,
        "Volume": 9980934
    },
    {
        "Company": "FoodChain",
        "Date": "2020-04-12",
        "Open Price": 1009.72,
        "Close Price": 637.57,
        "Volume": 5823765
    },
    {
        "Company": "TechnoCorp",
        "Date": "2010-09-27",
        "Open Price": 1183.13,
        "Close Price": 363.73,
        "Volume": 7361861
    }
]<start>
Company,Date,Open Price,Close Price,Volume
HealthGen,2012-09-18,43.71,1392.58,7853316
RetailWorld,2018-12-23,265.02,909.59,7361861
AutoMotive,2012-11-17,1144.97,842.45,1814065
BioLife,2019-06-21,1018.52,897.06,2008574
AeroSystems,2011-12-26,160.76,363.73,7412826
BioLife,2023-02-08,196.26,645.82,7436867
BioLife,2016-07-24,313.83,1144.97,9980934
FoodChain,2020-04-12,1009.72,637.57,5823765
TechnoCorp,2010-09-27,1183.13,363.73,7361861
<end>Can you change this PLAIN TEXT into Json?
Location: Seattle | Condition: Cloudy | Temperature (C): 28.7 | Humidity (%): 75 | Day: Wednesday
Location: Denver | Condition: Sunny | Temperature (C): 12.3 | Humidity (%): 50 | Day: Sunday
Location: Seattle | Condition: Stormy | Temperature (C): 13.6 | Humidity (%): 59 | Day: Sunday
Location: Chicago | Condition: Stormy | Temperature (C): -8.7 | Humidity (%): 25 | Day: Friday
Location: Los Angeles | Condition: Snowy | Temperature (C): -4.4 | Humidity (%): 62 | Day: Monday
Location: New York | Condition: Snowy | Temperature (C): 20.7 | Humidity (%): 37 | Day: Friday
Location: Denver | Condition: Rainy | Temperature (C): 16.1 | Humidity (%): 96 | Day: Sunday
Location: New York | Condition: Cloudy | Temperature (C): -9.8 | Humidity (%): 22 | Day: Monday
<start>
[
    {
        "Location": "Seattle",
        "Condition": "Cloudy",
        "Temperature (C)": 28.7,
        "Humidity (%)": 75,
        "Day": "Wednesday"
    },
    {
        "Location": "Denver",
        "Condition": "Sunny",
        "Temperature (C)": 12.3,
        "Humidity (%)": 50,
        "Day": "Sunday"
    },
    {
        "Location": "Seattle",
        "Condition": "Stormy",
        "Temperature (C)": 13.6,
        "Humidity (%)": 59,
        "Day": "Sunday"
    },
    {
        "Location": "Chicago",
        "Condition": "Stormy",
        "Temperature (C)": -8.7,
        "Humidity (%)": 25,
        "Day": "Friday"
    },
    {
        "Location": "Los Angeles",
        "Condition": "Snowy",
        "Temperature (C)": -4.4,
        "Humidity (%)": 62,
        "Day": "Monday"
    },
    {
        "Location": "New York",
        "Condition": "Snowy",
        "Temperature (C)": 20.7,
        "Humidity (%)": 37,
        "Day": "Friday"
    },
    {
        "Location": "Denver",
        "Condition": "Rainy",
        "Temperature (C)": 16.1,
        "Humidity (%)": 96,
        "Day": "Sunday"
    },
    {
        "Location": "New York",
        "Condition": "Cloudy",
        "Temperature (C)": -9.8,
        "Humidity (%)": 22,
        "Day": "Monday"
    }
]
<end>Convert this MARKDOWN to Csv:
| Queries per Second | Connection Count | Timestamp |
| --- | --- | --- |
| 2435.5 | 89 | 2021-05-02 12:50:51 |
| 1685.83 | 446 | 2022-08-25 10:51:07 |
| 1744.88 | 142 | 2021-11-14 16:25:14 |
| 1945.01 | 174 | 2022-04-06 08:47:58 |
| 1830.29 | 177 | 2021-11-20 21:54:01 |<start>
Queries per Second,Connection Count,Timestamp
2435.5,89,2021-05-02 12:50:51
1685.83,446,2022-08-25 10:51:07
1744.88,142,2021-11-14 16:25:14
1945.01,174,2022-04-06 08:47:58
1830.29,177,2021-11-20 21:54:01
<end>Convert this yaml to MARKDOWN:
- Box Office Earnings (M): 201.97
  Release Year: 2012
- Box Office Earnings (M): 728.88
  Release Year: 1993
- Box Office Earnings (M): 526.27
  Release Year: 1985
<start>
| Release Year | Box Office Earnings (M) |
| --- | --- |
| 2012 | 201.97 |
| 1993 | 728.88 |
| 1985 | 526.27 |
<end>Convert this Csv to plain text:
Birth Month,Income
June,435000
December,330000
October,320000
June,235000
<start>
Birth Month: June | Income: 435000
Birth Month: December | Income: 330000
Birth Month: October | Income: 320000
Birth Month: June | Income: 235000
<end>Convert this YAML to CSV:
- Average Latency (ms): 48.32
  Cache Hit Ratio (%): 73.69
  Queries per Second: 1529.01
  Timestamp: '2023-10-10 04:15:31'
- Average Latency (ms): 67.46
  Cache Hit Ratio (%): 99.29
  Queries per Second: 3604.75
  Timestamp: '2023-02-15 07:09:14'
- Average Latency (ms): 90.01
  Cache Hit Ratio (%): 80.76
  Queries per Second: 529.17
  Timestamp: '2022-11-20 05:45:27'
- Average Latency (ms): 36.81
  Cache Hit Ratio (%): 71.93
  Queries per Second: 3011.6
  Timestamp: '2022-08-03 13:20:59'
<start>
Queries per Second,Cache Hit Ratio (%),Average Latency (ms),Timestamp
1529.01,73.69,48.32,2023-10-10 04:15:31
3604.75,99.29,67.46,2023-02-15 07:09:14
529.17,80.76,90.01,2022-11-20 05:45:27
3011.6,71.93,36.81,2022-08-03 13:20:59
<end>Here's some PLAIN TEXT data, can you convert it to json?
End Location: Houston | Distance (miles): 277.3 | Duration (hours): 36.6
End Location: Los Angeles | Distance (miles): 201.0 | Duration (hours): 41.2
End Location: Phoenix | Distance (miles): 1598.1 | Duration (hours): 32.9
End Location: San Francisco | Distance (miles): 2214.9 | Duration (hours): 14.5
End Location: San Francisco | Distance (miles): 858.1 | Duration (hours): 20.2
End Location: Phoenix | Distance (miles): 1169.6 | Duration (hours): 34.3
End Location: Phoenix | Distance (miles): 2054.4 | Duration (hours): 64.5
<start>
[
    {
        "End Location": "Houston",
        "Distance (miles)": 277.3,
        "Duration (hours)": 36.6
    },
    {
        "End Location": "Los Angeles",
        "Distance (miles)": 201.0,
        "Duration (hours)": 41.2
    },
    {
        "End Location": "Phoenix",
        "Distance (miles)": 1598.1,
        "Duration (hours)": 32.9
    },
    {
        "End Location": "San Francisco",
        "Distance (miles)": 2214.9,
        "Duration (hours)": 14.5
    },
    {
        "End Location": "San Francisco",
        "Distance (miles)": 858.1,
        "Duration (hours)": 20.2
    },
    {
        "End Location": "Phoenix",
        "Distance (miles)": 1169.6,
        "Duration (hours)": 34.3
    },
    {
        "End Location": "Phoenix",
        "Distance (miles)": 2054.4,
        "Duration (hours)": 64.5
    }
]
<end>Can you change this markdown into yml?
| Restaurant Name | Rating |
| --- | --- |
| Pizza Planet | 2 |
| Burger Haven | 3 |
| The Steakhouse | 4 |
| BBQ Barn | 1 |
| BBQ Barn | 3 |
| BBQ Barn | 1 |
| Taco Town | 3 |
| The Golden Spoon | 1 |
| Burger Haven | 3 |
| Pizza Planet | 1 |<start>
- Rating: 2
  Restaurant Name: Pizza Planet
- Rating: 3
  Restaurant Name: Burger Haven
- Rating: 4
  Restaurant Name: The Steakhouse
- Rating: 1
  Restaurant Name: BBQ Barn
- Rating: 3
  Restaurant Name: BBQ Barn
- Rating: 1
  Restaurant Name: BBQ Barn
- Rating: 3
  Restaurant Name: Taco Town
- Rating: 1
  Restaurant Name: The Golden Spoon
- Rating: 3
  Restaurant Name: Burger Haven
- Rating: 1
  Restaurant Name: Pizza Planet
<end>Here's some markdown data, can you convert it to CSV?
| Trip Name | Start Location | Distance (miles) | Fuel Used (gallons) |
| --- | --- | --- | --- |
| Lakeside Retreat | Los Angeles | 1157.2 | 65.2 |
| Historic Route | New York | 135.2 | 60.7 |
| City Explorer | Los Angeles | 2692.6 | 76.4 |
| Historic Route | Phoenix | 964.1 | 83.6 |<start>
Trip Name,Start Location,Distance (miles),Fuel Used (gallons)
Lakeside Retreat,Los Angeles,1157.2,65.2
Historic Route,New York,135.2,60.7
City Explorer,Los Angeles,2692.6,76.4
Historic Route,Phoenix,964.1,83.6
<end>Here's some Yml data, can you convert it to CSV?
- Day: Sunday
  Humidity (%): 73
  Temperature (C): 15.1
  Wind Speed (km/h): 28.8
- Day: Sunday
  Humidity (%): 29
  Temperature (C): 36.6
  Wind Speed (km/h): 18.8
- Day: Sunday
  Humidity (%): 100
  Temperature (C): 25.6
  Wind Speed (km/h): 3.2
- Day: Tuesday
  Humidity (%): 79
  Temperature (C): 17.8
  Wind Speed (km/h): 10.7
- Day: Saturday
  Humidity (%): 63
  Temperature (C): 7.3
  Wind Speed (km/h): 28.0
- Day: Saturday
  Humidity (%): 95
  Temperature (C): 25.6
  Wind Speed (km/h): 12.4
- Day: Tuesday
  Humidity (%): 33
  Temperature (C): 25.6
  Wind Speed (km/h): 13.0
- Day: Friday
  Humidity (%): 41
  Temperature (C): 0.6
  Wind Speed (km/h): 27.7
- Day: Friday
  Humidity (%): 30
  Temperature (C): 31.0
  Wind Speed (km/h): 15.5
- Day: Monday
  Humidity (%): 31
  Temperature (C): 1.2
  Wind Speed (km/h): 11.9
<start>
Temperature (C),Humidity (%),Wind Speed (km/h),Day
15.1,73,28.8,Sunday
36.6,29,18.8,Sunday
25.6,100,3.2,Sunday
17.8,79,10.7,Tuesday
7.3,63,28.0,Saturday
25.6,95,12.4,Saturday
25.6,33,13.0,Tuesday
0.6,41,27.7,Friday
31.0,30,15.5,Friday
1.2,31,11.9,Monday
<end>Can you change this Yaml into MARKDOWN?
- Category: Electronics
  Price: 188.58
  Product Name: Apparatus
  SKU: SKU-1070
  Stock Quantity: 372
  Supplier Name: Wonka Industries
- Category: Household
  Price: 169.68
  Product Name: Thingamajig
  SKU: SKU-1062
  Stock Quantity: 67
  Supplier Name: Wonka Industries
- Category: Sports
  Price: 300.6
  Product Name: Apparatus
  SKU: SKU-1022
  Stock Quantity: 325
  Supplier Name: Wayne Enterprises
- Category: Toys
  Price: 327.31
  Product Name: Gadget
  SKU: SKU-1006
  Stock Quantity: 248
  Supplier Name: Wonka Industries
- Category: Toys
  Price: 423.9
  Product Name: Thingamajig
  SKU: SKU-1085
  Stock Quantity: 60
  Supplier Name: ACME Corp
<start>
| Product Name | SKU | Price | Stock Quantity | Category | Supplier Name |
| --- | --- | --- | --- | --- | --- |
| Apparatus | SKU-1070 | 188.58 | 372 | Electronics | Wonka Industries |
| Thingamajig | SKU-1062 | 169.68 | 67 | Household | Wonka Industries |
| Apparatus | SKU-1022 | 300.6 | 325 | Sports | Wayne Enterprises |
| Gadget | SKU-1006 | 327.31 | 248 | Toys | Wonka Industries |
| Thingamajig | SKU-1085 | 423.9 | 60 | Toys | ACME Corp |
<end>Here's some Yaml data, can you convert it to csv?
- Battery Level (%): 10.6
  Device ID: device-0088
  Device Type: Light Sensor
  Timestamp: '2023-08-18 03:47:04'
- Battery Level (%): 50.3
  Device ID: device-0094
  Device Type: Temperature Sensor
  Timestamp: '2021-01-16 20:12:32'
- Battery Level (%): 28.8
  Device ID: device-0013
  Device Type: Humidity Sensor
  Timestamp: '2021-01-07 19:38:10'
- Battery Level (%): 57.1
  Device ID: device-0096
  Device Type: Light Sensor
  Timestamp: '2021-06-21 10:28:25'
- Battery Level (%): 22.9
  Device ID: device-0009
  Device Type: Motion Detector
  Timestamp: '2022-02-18 20:36:39'
<start>
Device ID,Device Type,Battery Level (%),Timestamp
device-0088,Light Sensor,10.6,2023-08-18 03:47:04
device-0094,Temperature Sensor,50.3,2021-01-16 20:12:32
device-0013,Humidity Sensor,28.8,2021-01-07 19:38:10
device-0096,Light Sensor,57.1,2021-06-21 10:28:25
device-0009,Motion Detector,22.9,2022-02-18 20:36:39
<end>Convert this yml to csv:
- Condition: Stormy
  Humidity (%): 55
  Temperature (C): 37.5
  Wind Speed (km/h): 27.8
- Condition: Windy
  Humidity (%): 37
  Temperature (C): 0.5
  Wind Speed (km/h): 8.0
- Condition: Rainy
  Humidity (%): 37
  Temperature (C): 15.1
  Wind Speed (km/h): 5.6
- Condition: Sunny
  Humidity (%): 22
  Temperature (C): 31.0
  Wind Speed (km/h): 22.8
- Condition: Windy
  Humidity (%): 90
  Temperature (C): -2.8
  Wind Speed (km/h): 22.6
- Condition: Stormy
  Humidity (%): 37
  Temperature (C): 9.8
  Wind Speed (km/h): 23.5
- Condition: Windy
  Humidity (%): 69
  Temperature (C): 7.4
  Wind Speed (km/h): 15.3
- Condition: Snowy
  Humidity (%): 78
  Temperature (C): 26.9
  Wind Speed (km/h): 6.5
- Condition: Stormy
  Humidity (%): 92
  Temperature (C): -2.7
  Wind Speed (km/h): 7.0
- Condition: Snowy
  Humidity (%): 33
  Temperature (C): -6.5
  Wind Speed (km/h): 13.1
<start>
Condition,Temperature (C),Humidity (%),Wind Speed (km/h)
Stormy,37.5,55,27.8
Windy,0.5,37,8.0
Rainy,15.1,37,5.6
Sunny,31.0,22,22.8
Windy,-2.8,90,22.6
Stormy,9.8,37,23.5
Windy,7.4,69,15.3
Snowy,26.9,78,6.5
Stormy,-2.7,92,7.0
Snowy,-6.5,33,13.1
<end>Please transform the following Csv data into Yaml:
Company,Date,Open Price,Close Price,High Price,Low Price,Volume
FoodChain,2015-10-13,920.02,485.83,1370.79,485.83,1499497
FoodChain,2023-03-13,903.82,228.57,903.82,228.57,2202475
AutoMotive,2018-07-23,1078.63,898.88,1078.63,324.31,9547814
AutoMotive,2019-05-24,1232.96,1100.14,1232.96,36.46,4439035
RetailWorld,2021-04-02,228.57,230.93,1042.76,228.57,3700779
HealthGen,2023-03-25,202.47,752.2,752.2,202.47,4230202
MediaGroup,2020-10-18,1242.59,414.17,1242.59,414.17,2488194
FoodChain,2014-02-24,1311.52,485.83,1311.52,485.83,4352491
<start>
- Close Price: 485.83
  Company: FoodChain
  Date: '2015-10-13'
  High Price: 1370.79
  Low Price: 485.83
  Open Price: 920.02
  Volume: 1499497
- Close Price: 228.57
  Company: FoodChain
  Date: '2023-03-13'
  High Price: 903.82
  Low Price: 228.57
  Open Price: 903.82
  Volume: 2202475
- Close Price: 898.88
  Company: AutoMotive
  Date: '2018-07-23'
  High Price: 1078.63
  Low Price: 324.31
  Open Price: 1078.63
  Volume: 9547814
- Close Price: 1100.14
  Company: AutoMotive
  Date: '2019-05-24'
  High Price: 1232.96
  Low Price: 36.46
  Open Price: 1232.96
  Volume: 4439035
- Close Price: 230.93
  Company: RetailWorld
  Date: '2021-04-02'
  High Price: 1042.76
  Low Price: 228.57
  Open Price: 228.57
  Volume: 3700779
- Close Price: 752.2
  Company: HealthGen
  Date: '2023-03-25'
  High Price: 752.2
  Low Price: 202.47
  Open Price: 202.47
  Volume: 4230202
- Close Price: 414.17
  Company: MediaGroup
  Date: '2020-10-18'
  High Price: 1242.59
  Low Price: 414.17
  Open Price: 1242.59
  Volume: 2488194
- Close Price: 485.83
  Company: FoodChain
  Date: '2014-02-24'
  High Price: 1311.52
  Low Price: 485.83
  Open Price: 1311.52
  Volume: 4352491
<end>Transform this json structure to a Plain text format:
[
    {
        "Name": "Keith",
        "Birth Month": "December",
        "City": "Phoenix",
        "Income": 170000
    },
    {
        "Name": "Cecil",
        "Birth Month": "April",
        "City": "Austin",
        "Income": 360000
    },
    {
        "Name": "Caden",
        "Birth Month": "October",
        "City": "Portland",
        "Income": 470000
    },
    {
        "Name": "Jan",
        "Birth Month": "October",
        "City": "Dallas",
        "Income": 115000
    },
    {
        "Name": "Londyn",
        "Birth Month": "May",
        "City": "San Jose",
        "Income": 405000
    }
]<start>
Name: Keith | Birth Month: December | City: Phoenix | Income: 170000
Name: Cecil | Birth Month: April | City: Austin | Income: 360000
Name: Caden | Birth Month: October | City: Portland | Income: 470000
Name: Jan | Birth Month: October | City: Dallas | Income: 115000
Name: Londyn | Birth Month: May | City: San Jose | Income: 405000
<end>Transform this csv structure to a Json format:
Database Name,Cache Hit Ratio (%),Connection Count,Timestamp
InventoryDB,74.71,225,2023-02-27 15:54:22
SessionsDB,82.89,229,2022-07-04 17:16:31
SessionsDB,96.52,485,2022-02-10 18:33:21
LogsDB,98.67,474,2022-03-24 16:13:00
InventoryDB,98.67,77,2023-02-25 09:05:39
<start>
[
    {
        "Database Name": "InventoryDB",
        "Cache Hit Ratio (%)": 74.71,
        "Connection Count": 225,
        "Timestamp": "2023-02-27 15:54:22"
    },
    {
        "Database Name": "SessionsDB",
        "Cache Hit Ratio (%)": 82.89,
        "Connection Count": 229,
        "Timestamp": "2022-07-04 17:16:31"
    },
    {
        "Database Name": "SessionsDB",
        "Cache Hit Ratio (%)": 96.52,
        "Connection Count": 485,
        "Timestamp": "2022-02-10 18:33:21"
    },
    {
        "Database Name": "LogsDB",
        "Cache Hit Ratio (%)": 98.67,
        "Connection Count": 474,
        "Timestamp": "2022-03-24 16:13:00"
    },
    {
        "Database Name": "InventoryDB",
        "Cache Hit Ratio (%)": 98.67,
        "Connection Count": 77,
        "Timestamp": "2023-02-25 09:05:39"
    }
]
<end>Convert this YAML to Json:
- Price: 359.1
  Product Name: Contraption
  Stock Quantity: 311
  Supplier Name: Globex
- Price: 23.17
  Product Name: Gizmo
  Stock Quantity: 236
  Supplier Name: Umbrella Corp
- Price: 235.96
  Product Name: Instrument
  Stock Quantity: 266
  Supplier Name: Wonka Industries
- Price: 319.38
  Product Name: Whatchamacallit
  Stock Quantity: 267
  Supplier Name: Globex
- Price: 108.31
  Product Name: Device
  Stock Quantity: 265
  Supplier Name: Wonka Industries
- Price: 151.17
  Product Name: Gadget
  Stock Quantity: 223
  Supplier Name: Umbrella Corp
<start>
[
    {
        "Product Name": "Contraption",
        "Price": 359.1,
        "Stock Quantity": 311,
        "Supplier Name": "Globex"
    },
    {
        "Product Name": "Gizmo",
        "Price": 23.17,
        "Stock Quantity": 236,
        "Supplier Name": "Umbrella Corp"
    },
    {
        "Product Name": "Instrument",
        "Price": 235.96,
        "Stock Quantity": 266,
        "Supplier Name": "Wonka Industries"
    },
    {
        "Product Name": "Whatchamacallit",
        "Price": 319.38,
        "Stock Quantity": 267,
        "Supplier Name": "Globex"
    },
    {
        "Product Name": "Device",
        "Price": 108.31,
        "Stock Quantity": 265,
        "Supplier Name": "Wonka Industries"
    },
    {
        "Product Name": "Gadget",
        "Price": 151.17,
        "Stock Quantity": 223,
        "Supplier Name": "Umbrella Corp"
    }
]
<end>Transform this plain text structure to a json format:
Title: Whispers of the Abyss | Author: Luna Silverleaf | Genre: Mystery | Publication Year: 2005 | Rating: 3.2
Title: Shadows of Solitude | Author: Elara Moonshadow | Genre: Mystery | Publication Year: 1964 | Rating: 1.3
Title: Whispers of the Abyss | Author: Luna Silverleaf | Genre: Romance | Publication Year: 1991 | Rating: 2.2
Title: The Forgotten World | Author: Sylvia Nightshade | Genre: Historical | Publication Year: 1980 | Rating: 3.5
Title: Whispers of the Abyss | Author: Orion Frostblade | Genre: Science Fiction | Publication Year: 1981 | Rating: 2.2
Title: Shadows of Solitude | Author: Kara Firebrand | Genre: Science Fiction | Publication Year: 1989 | Rating: 2.7
Title: Tales of the Brave | Author: Isla Windrider | Genre: Horror | Publication Year: 1985 | Rating: 1.4
Title: Tales of the Brave | Author: Elara Moonshadow | Genre: Fantasy | Publication Year: 1959 | Rating: 3.7
Title: The Forgotten World | Author: Galen Starfire | Genre: Non-Fiction | Publication Year: 2007 | Rating: 1.3
<start>
[
    {
        "Title": "Whispers of the Abyss",
        "Author": "Luna Silverleaf",
        "Genre": "Mystery",
        "Publication Year": 2005,
        "Rating": 3.2
    },
    {
        "Title": "Shadows of Solitude",
        "Author": "Elara Moonshadow",
        "Genre": "Mystery",
        "Publication Year": 1964,
        "Rating": 1.3
    },
    {
        "Title": "Whispers of the Abyss",
        "Author": "Luna Silverleaf",
        "Genre": "Romance",
        "Publication Year": 1991,
        "Rating": 2.2
    },
    {
        "Title": "The Forgotten World",
        "Author": "Sylvia Nightshade",
        "Genre": "Historical",
        "Publication Year": 1980,
        "Rating": 3.5
    },
    {
        "Title": "Whispers of the Abyss",
        "Author": "Orion Frostblade",
        "Genre": "Science Fiction",
        "Publication Year": 1981,
        "Rating": 2.2
    },
    {
        "Title": "Shadows of Solitude",
        "Author": "Kara Firebrand",
        "Genre": "Science Fiction",
        "Publication Year": 1989,
        "Rating": 2.7
    },
    {
        "Title": "Tales of the Brave",
        "Author": "Isla Windrider",
        "Genre": "Horror",
        "Publication Year": 1985,
        "Rating": 1.4
    },
    {
        "Title": "Tales of the Brave",
        "Author": "Elara Moonshadow",
        "Genre": "Fantasy",
        "Publication Year": 1959,
        "Rating": 3.7
    },
    {
        "Title": "The Forgotten World",
        "Author": "Galen Starfire",
        "Genre": "Non-Fiction",
        "Publication Year": 2007,
        "Rating": 1.3
    }
]
<end>Convert this Yaml to plain text:
- Distance (miles): 124.5
  Duration (hours): 9.7
  Fuel Used (gallons): 74.2
  Start Location: Chicago
  Trip Name: Mountain Adventure
- Distance (miles): 1812.7
  Duration (hours): 23.4
  Fuel Used (gallons): 62.1
  Start Location: Los Angeles
  Trip Name: Forest Journey
- Distance (miles): 1875.3
  Duration (hours): 30.3
  Fuel Used (gallons): 79.6
  Start Location: New York
  Trip Name: Historic Route
<start>
Trip Name: Mountain Adventure | Start Location: Chicago | Distance (miles): 124.5 | Duration (hours): 9.7 | Fuel Used (gallons): 74.2
Trip Name: Forest Journey | Start Location: Los Angeles | Distance (miles): 1812.7 | Duration (hours): 23.4 | Fuel Used (gallons): 62.1
Trip Name: Historic Route | Start Location: New York | Distance (miles): 1875.3 | Duration (hours): 30.3 | Fuel Used (gallons): 79.6
<end>Can you change this PLAIN TEXT into yaml?
Trip Name: Coast to Coast | End Location: Chicago | Distance (miles): 1867.4 | Duration (hours): 67.2 | Fuel Used (gallons): 70.2
Trip Name: Lakeside Retreat | End Location: Phoenix | Distance (miles): 1630.7 | Duration (hours): 24.8 | Fuel Used (gallons): 92.0
Trip Name: Valley Voyage | End Location: Phoenix | Distance (miles): 1867.4 | Duration (hours): 54.7 | Fuel Used (gallons): 16.4
Trip Name: Desert Drive | End Location: New York | Distance (miles): 2744.3 | Duration (hours): 43.9 | Fuel Used (gallons): 67.0
Trip Name: Mountain Adventure | End Location: Houston | Distance (miles): 1462.0 | Duration (hours): 70.4 | Fuel Used (gallons): 32.1
Trip Name: Historic Route | End Location: Miami | Distance (miles): 759.4 | Duration (hours): 30.0 | Fuel Used (gallons): 25.6
Trip Name: Lakeside Retreat | End Location: San Francisco | Distance (miles): 539.5 | Duration (hours): 53.8 | Fuel Used (gallons): 47.7
Trip Name: Desert Drive | End Location: San Francisco | Distance (miles): 2249.6 | Duration (hours): 55.7 | Fuel Used (gallons): 52.1
Trip Name: Forest Journey | End Location: Denver | Distance (miles): 2854.1 | Duration (hours): 58.8 | Fuel Used (gallons): 76.7
Trip Name: Lakeside Retreat | End Location: Miami | Distance (miles): 1742.3 | Duration (hours): 4.3 | Fuel Used (gallons): 25.3
<start>
- Distance (miles): 1867.4
  Duration (hours): 67.2
  End Location: Chicago
  Fuel Used (gallons): 70.2
  Trip Name: Coast to Coast
- Distance (miles): 1630.7
  Duration (hours): 24.8
  End Location: Phoenix
  Fuel Used (gallons): 92.0
  Trip Name: Lakeside Retreat
- Distance (miles): 1867.4
  Duration (hours): 54.7
  End Location: Phoenix
  Fuel Used (gallons): 16.4
  Trip Name: Valley Voyage
- Distance (miles): 2744.3
  Duration (hours): 43.9
  End Location: New York
  Fuel Used (gallons): 67.0
  Trip Name: Desert Drive
- Distance (miles): 1462.0
  Duration (hours): 70.4
  End Location: Houston
  Fuel Used (gallons): 32.1
  Trip Name: Mountain Adventure
- Distance (miles): 759.4
  Duration (hours): 30.0
  End Location: Miami
  Fuel Used (gallons): 25.6
  Trip Name: Historic Route
- Distance (miles): 539.5
  Duration (hours): 53.8
  End Location: San Francisco
  Fuel Used (gallons): 47.7
  Trip Name: Lakeside Retreat
- Distance (miles): 2249.6
  Duration (hours): 55.7
  End Location: San Francisco
  Fuel Used (gallons): 52.1
  Trip Name: Desert Drive
- Distance (miles): 2854.1
  Duration (hours): 58.8
  End Location: Denver
  Fuel Used (gallons): 76.7
  Trip Name: Forest Journey
- Distance (miles): 1742.3
  Duration (hours): 4.3
  End Location: Miami
  Fuel Used (gallons): 25.3
  Trip Name: Lakeside Retreat
<end>Convert this Csv to json:
Location,Price Range
San Francisco,$$
Seattle,$$$
New York,$$$$$
San Francisco,$
Phoenix,$$$
Seattle,$$
San Francisco,$$$
Phoenix,$$$
Seattle,$$
<start>
[
    {
        "Location": "San Francisco",
        "Price Range": "$$"
    },
    {
        "Location": "Seattle",
        "Price Range": "$$$"
    },
    {
        "Location": "New York",
        "Price Range": "$$$$$"
    },
    {
        "Location": "San Francisco",
        "Price Range": "$"
    },
    {
        "Location": "Phoenix",
        "Price Range": "$$$"
    },
    {
        "Location": "Seattle",
        "Price Range": "$$"
    },
    {
        "Location": "San Francisco",
        "Price Range": "$$$"
    },
    {
        "Location": "Phoenix",
        "Price Range": "$$$"
    },
    {
        "Location": "Seattle",
        "Price Range": "$$"
    }
]
<end>Transform this Json structure to a plain text format:
[
    {
        "Database Name": "SalesDB",
        "Queries per Second": 4899.42,
        "Cache Hit Ratio (%)": 96.73,
        "Connection Count": 387,
        "Average Latency (ms)": 95.31,
        "Timestamp": "2022-09-13 13:50:42"
    },
    {
        "Database Name": "SessionsDB",
        "Queries per Second": 3134.15,
        "Cache Hit Ratio (%)": 99.56,
        "Connection Count": 323,
        "Average Latency (ms)": 83.08,
        "Timestamp": "2022-01-15 07:15:50"
    },
    {
        "Database Name": "ProfilesDB",
        "Queries per Second": 2605.08,
        "Cache Hit Ratio (%)": 87.88,
        "Connection Count": 171,
        "Average Latency (ms)": 69.39,
        "Timestamp": "2023-03-17 11:15:13"
    }
]<start>
Database Name: SalesDB | Queries per Second: 4899.42 | Cache Hit Ratio (%): 96.73 | Connection Count: 387 | Average Latency (ms): 95.31 | Timestamp: 2022-09-13 13:50:42
Database Name: SessionsDB | Queries per Second: 3134.15 | Cache Hit Ratio (%): 99.56 | Connection Count: 323 | Average Latency (ms): 83.08 | Timestamp: 2022-01-15 07:15:50
Database Name: ProfilesDB | Queries per Second: 2605.08 | Cache Hit Ratio (%): 87.88 | Connection Count: 171 | Average Latency (ms): 69.39 | Timestamp: 2023-03-17 11:15:13
<end>Convert this csv to json:
Location,Rating,Price Range
New York,5,$
Phoenix,1,$$$$$
Houston,5,$
Houston,5,$
<start>
[
    {
        "Location": "New York",
        "Rating": 5,
        "Price Range": "$"
    },
    {
        "Location": "Phoenix",
        "Rating": 1,
        "Price Range": "$$$$$"
    },
    {
        "Location": "Houston",
        "Rating": 5,
        "Price Range": "$"
    },
    {
        "Location": "Houston",
        "Rating": 5,
        "Price Range": "$"
    }
]
<end>Please transform the following Csv data into Markdown:
Database Name,Queries per Second,Cache Hit Ratio (%),Average Latency (ms)
MetricsDB,2958.21,87.12,28.33
LogsDB,970.77,75.42,32.16
UserDB,4588.51,71.94,67.39
<start>
| Database Name | Queries per Second | Cache Hit Ratio (%) | Average Latency (ms) |
| --- | --- | --- | --- |
| MetricsDB | 2958.21 | 87.12 | 28.33 |
| LogsDB | 970.77 | 75.42 | 32.16 |
| UserDB | 4588.51 | 71.94 | 67.39 |
<end>Transform this MARKDOWN structure to a json format:
| Company | Date | Open Price | Close Price | High Price | Low Price | Volume |
| --- | --- | --- | --- | --- | --- | --- |
| BioLife | 2011-09-09 | 1297.62 | 1092.88 | 1469.93 | 14.38 | 6191352 |
| TechnoCorp | 2010-11-12 | 1008.74 | 1393.9 | 1393.9 | 1008.74 | 1039793 |
| AutoMotive | 2012-12-15 | 938.41 | 1011.04 | 1011.04 | 938.41 | 4573875 |
| AutoMotive | 2012-10-09 | 1466.93 | 359.74 | 1466.93 | 359.74 | 2718242 |
| HealthGen | 2011-08-17 | 14.38 | 557.6 | 557.6 | 14.38 | 8938494 |
| GreenEnergy | 2017-09-04 | 1239.59 | 52.95 | 1239.59 | 52.95 | 8799969 |
| RetailWorld | 2015-03-18 | 535.58 | 267.09 | 1024.07 | 267.09 | 3094622 |
| RetailWorld | 2015-04-04 | 259.14 | 805.72 | 1059.03 | 259.14 | 3094622 |
| MediaGroup | 2017-02-01 | 1492.02 | 142.4 | 1492.02 | 142.4 | 6414216 |<start>
[
    {
        "Company": "BioLife",
        "Date": "2011-09-09",
        "Open Price": 1297.62,
        "Close Price": 1092.88,
        "High Price": 1469.93,
        "Low Price": 14.38,
        "Volume": 6191352
    },
    {
        "Company": "TechnoCorp",
        "Date": "2010-11-12",
        "Open Price": 1008.74,
        "Close Price": 1393.9,
        "High Price": 1393.9,
        "Low Price": 1008.74,
        "Volume": 1039793
    },
    {
        "Company": "AutoMotive",
        "Date": "2012-12-15",
        "Open Price": 938.41,
        "Close Price": 1011.04,
        "High Price": 1011.04,
        "Low Price": 938.41,
        "Volume": 4573875
    },
    {
        "Company": "AutoMotive",
        "Date": "2012-10-09",
        "Open Price": 1466.93,
        "Close Price": 359.74,
        "High Price": 1466.93,
        "Low Price": 359.74,
        "Volume": 2718242
    },
    {
        "Company": "HealthGen",
        "Date": "2011-08-17",
        "Open Price": 14.38,
        "Close Price": 557.6,
        "High Price": 557.6,
        "Low Price": 14.38,
        "Volume": 8938494
    },
    {
        "Company": "GreenEnergy",
        "Date": "2017-09-04",
        "Open Price": 1239.59,
        "Close Price": 52.95,
        "High Price": 1239.59,
        "Low Price": 52.95,
        "Volume": 8799969
    },
    {
        "Company": "RetailWorld",
        "Date": "2015-03-18",
        "Open Price": 535.58,
        "Close Price": 267.09,
        "High Price": 1024.07,
        "Low Price": 267.09,
        "Volume": 3094622
    },
    {
        "Company": "RetailWorld",
        "Date": "2015-04-04",
        "Open Price": 259.14,
        "Close Price": 805.72,
        "High Price": 1059.03,
        "Low Price": 259.14,
        "Volume": 3094622
    },
    {
        "Company": "MediaGroup",
        "Date": "2017-02-01",
        "Open Price": 1492.02,
        "Close Price": 142.4,
        "High Price": 1492.02,
        "Low Price": 142.4,
        "Volume": 6414216
    }
]
<end>Convert this MARKDOWN to Json:
| Company | Sector | Market Cap | Stock Price | Annual Revenue (B) | Quarter |
| --- | --- | --- | --- | --- | --- |
| EcoEnergy | Retail | Mega Cap | 169.94 | 311.39 | Q2 |
| HealthPlus | Automotive | Mid Cap | 732.14 | 461.35 | Q1 |
| HealthPlus | Retail | Mega Cap | 925.62 | 310.78 | Q4 |
| AutoDrive | Healthcare | Small Cap | 10.84 | 212.5 | Q1 |
| AutoDrive | Technology | Large Cap | 732.14 | 132.9 | Q4 |
| GlobalTrade | Retail | Mid Cap | 899.08 | 311.39 | Q2 |
| RetailHub | Automotive | Mid Cap | 215.17 | 231.38 | Q4 |
| GlobalTrade | Healthcare | Small Cap | 925.62 | 291.86 | Q4 |
| Foodies | Finance | Small Cap | 604.45 | 91.22 | Q3 |
| TechCorp | Aerospace | Small Cap | 795.8 | 102.63 | Q3 |<start>
[
    {
        "Company": "EcoEnergy",
        "Sector": "Retail",
        "Market Cap": "Mega Cap",
        "Stock Price": 169.94,
        "Annual Revenue (B)": 311.39,
        "Quarter": "Q2"
    },
    {
        "Company": "HealthPlus",
        "Sector": "Automotive",
        "Market Cap": "Mid Cap",
        "Stock Price": 732.14,
        "Annual Revenue (B)": 461.35,
        "Quarter": "Q1"
    },
    {
        "Company": "HealthPlus",
        "Sector": "Retail",
        "Market Cap": "Mega Cap",
        "Stock Price": 925.62,
        "Annual Revenue (B)": 310.78,
        "Quarter": "Q4"
    },
    {
        "Company": "AutoDrive",
        "Sector": "Healthcare",
        "Market Cap": "Small Cap",
        "Stock Price": 10.84,
        "Annual Revenue (B)": 212.5,
        "Quarter": "Q1"
    },
    {
        "Company": "AutoDrive",
        "Sector": "Technology",
        "Market Cap": "Large Cap",
        "Stock Price": 732.14,
        "Annual Revenue (B)": 132.9,
        "Quarter": "Q4"
    },
    {
        "Company": "GlobalTrade",
        "Sector": "Retail",
        "Market Cap": "Mid Cap",
        "Stock Price": 899.08,
        "Annual Revenue (B)": 311.39,
        "Quarter": "Q2"
    },
    {
        "Company": "RetailHub",
        "Sector": "Automotive",
        "Market Cap": "Mid Cap",
        "Stock Price": 215.17,
        "Annual Revenue (B)": 231.38,
        "Quarter": "Q4"
    },
    {
        "Company": "GlobalTrade",
        "Sector": "Healthcare",
        "Market Cap": "Small Cap",
        "Stock Price": 925.62,
        "Annual Revenue (B)": 291.86,
        "Quarter": "Q4"
    },
    {
        "Company": "Foodies",
        "Sector": "Finance",
        "Market Cap": "Small Cap",
        "Stock Price": 604.45,
        "Annual Revenue (B)": 91.22,
        "Quarter": "Q3"
    },
    {
        "Company": "TechCorp",
        "Sector": "Aerospace",
        "Market Cap": "Small Cap",
        "Stock Price": 795.8,
        "Annual Revenue (B)": 102.63,
        "Quarter": "Q3"
    }
]
<end>Here's some markdown data, can you convert it to PLAIN TEXT?
| Product Name | Category | Supplier Name |
| --- | --- | --- |
| Apparatus | Household | Umbrella Corp |
| Thingamajig | Sports | Umbrella Corp |
| Whatchamacallit | Automotive | Globex |<start>
Product Name: Apparatus | Category: Household | Supplier Name: Umbrella Corp
Product Name: Thingamajig | Category: Sports | Supplier Name: Umbrella Corp
Product Name: Whatchamacallit | Category: Automotive | Supplier Name: Globex
<end>Please transform the following MARKDOWN data into plain text:
| Device ID | Device Type | Location | Battery Level (%) | Reading Value | Timestamp |
| --- | --- | --- | --- | --- | --- |
| device-0060 | Motion Detector | Bedroom | 24.4 | -0.43 | 2021-05-28 10:47:41 |
| device-0094 | Temperature Sensor | Kitchen | 83.5 | 21.83 | 2021-07-10 02:20:22 |
| device-0100 | Motion Detector | Office | 31.0 | -15.26 | 2022-07-01 22:21:00 |
| device-0083 | Humidity Sensor | Office | 54.4 | 38.54 | 2023-01-13 05:06:11 |<start>
Device ID: device-0060 | Device Type: Motion Detector | Location: Bedroom | Battery Level (%): 24.4 | Reading Value: -0.43 | Timestamp: 2021-05-28 10:47:41
Device ID: device-0094 | Device Type: Temperature Sensor | Location: Kitchen | Battery Level (%): 83.5 | Reading Value: 21.83 | Timestamp: 2021-07-10 02:20:22
Device ID: device-0100 | Device Type: Motion Detector | Location: Office | Battery Level (%): 31.0 | Reading Value: -15.26 | Timestamp: 2022-07-01 22:21:00
Device ID: device-0083 | Device Type: Humidity Sensor | Location: Office | Battery Level (%): 54.4 | Reading Value: 38.54 | Timestamp: 2023-01-13 05:06:11
<end>Transform this Plain text structure to a csv format:
Price: 308.82 | Stock Quantity: 75 | Category: Toys | Supplier Name: Wayne Enterprises
Price: 177.14 | Stock Quantity: 12 | Category: Sports | Supplier Name: ACME Corp
Price: 350.25 | Stock Quantity: 233 | Category: Household | Supplier Name: Wayne Enterprises
Price: 343.3 | Stock Quantity: 70 | Category: Electronics | Supplier Name: Umbrella Corp
<start>
Price,Stock Quantity,Category,Supplier Name
308.82,75,Toys,Wayne Enterprises
177.14,12,Sports,ACME Corp
350.25,233,Household,Wayne Enterprises
343.3,70,Electronics,Umbrella Corp
<end>Can you change this YML into plain text?
- Distance (miles): 1263.4
  Duration (hours): 11.8
  End Location: Chicago
  Fuel Used (gallons): 16.9
  Trip Name: Lakeside Retreat
- Distance (miles): 969.8
  Duration (hours): 42.1
  End Location: Houston
  Fuel Used (gallons): 13.2
  Trip Name: Historic Route
- Distance (miles): 1394.3
  Duration (hours): 44.2
  End Location: New York
  Fuel Used (gallons): 46.4
  Trip Name: Coast to Coast
- Distance (miles): 2523.6
  Duration (hours): 19.1
  End Location: Denver
  Fuel Used (gallons): 91.0
  Trip Name: Historic Route
<start>
Trip Name: Lakeside Retreat | End Location: Chicago | Distance (miles): 1263.4 | Duration (hours): 11.8 | Fuel Used (gallons): 16.9
Trip Name: Historic Route | End Location: Houston | Distance (miles): 969.8 | Duration (hours): 42.1 | Fuel Used (gallons): 13.2
Trip Name: Coast to Coast | End Location: New York | Distance (miles): 1394.3 | Duration (hours): 44.2 | Fuel Used (gallons): 46.4
Trip Name: Historic Route | End Location: Denver | Distance (miles): 2523.6 | Duration (hours): 19.1 | Fuel Used (gallons): 91.0
<end>Transform this CSV structure to a yaml format:
Company,Market Cap,Stock Price,Annual Revenue (B)
AutoDrive,Large Cap,754.89,346.46
FinanceWorks,Mega Cap,252.6,135.72
AeroSpace,Mega Cap,811.78,256.68
EcoEnergy,Small Cap,25.04,364.98
RetailHub,Mid Cap,616.28,413.16
<start>
- Annual Revenue (B): 346.46
  Company: AutoDrive
  Market Cap: Large Cap
  Stock Price: 754.89
- Annual Revenue (B): 135.72
  Company: FinanceWorks
  Market Cap: Mega Cap
  Stock Price: 252.6
- Annual Revenue (B): 256.68
  Company: AeroSpace
  Market Cap: Mega Cap
  Stock Price: 811.78
- Annual Revenue (B): 364.98
  Company: EcoEnergy
  Market Cap: Small Cap
  Stock Price: 25.04
- Annual Revenue (B): 413.16
  Company: RetailHub
  Market Cap: Mid Cap
  Stock Price: 616.28
<end>Convert this PLAIN TEXT to YML:
Company: RetailHub | Sector: Aerospace | Stock Price: 673.55 | Annual Revenue (B): 453.48 | Quarter: Q2
Company: AeroSpace | Sector: Aerospace | Stock Price: 343.17 | Annual Revenue (B): 446.19 | Quarter: Q2
Company: AeroSpace | Sector: Biotech | Stock Price: 71.4 | Annual Revenue (B): 315.65 | Quarter: Q2
Company: AutoDrive | Sector: Retail | Stock Price: 634.33 | Annual Revenue (B): 82.1 | Quarter: Q3
Company: EcoEnergy | Sector: Retail | Stock Price: 316.55 | Annual Revenue (B): 405.31 | Quarter: Q1
Company: RetailHub | Sector: Automotive | Stock Price: 533.89 | Annual Revenue (B): 453.48 | Quarter: Q3
Company: EcoEnergy | Sector: Healthcare | Stock Price: 540.85 | Annual Revenue (B): 377.22 | Quarter: Q2
Company: Foodies | Sector: Energy | Stock Price: 533.89 | Annual Revenue (B): 116.59 | Quarter: Q3
Company: AutoDrive | Sector: Aerospace | Stock Price: 641.11 | Annual Revenue (B): 350.61 | Quarter: Q2
Company: AutoDrive | Sector: Retail | Stock Price: 402.06 | Annual Revenue (B): 344.92 | Quarter: Q3
<start>
- Annual Revenue (B): 453.48
  Company: RetailHub
  Quarter: Q2
  Sector: Aerospace
  Stock Price: 673.55
- Annual Revenue (B): 446.19
  Company: AeroSpace
  Quarter: Q2
  Sector: Aerospace
  Stock Price: 343.17
- Annual Revenue (B): 315.65
  Company: AeroSpace
  Quarter: Q2
  Sector: Biotech
  Stock Price: 71.4
- Annual Revenue (B): 82.1
  Company: AutoDrive
  Quarter: Q3
  Sector: Retail
  Stock Price: 634.33
- Annual Revenue (B): 405.31
  Company: EcoEnergy
  Quarter: Q1
  Sector: Retail
  Stock Price: 316.55
- Annual Revenue (B): 453.48
  Company: RetailHub
  Quarter: Q3
  Sector: Automotive
  Stock Price: 533.89
- Annual Revenue (B): 377.22
  Company: EcoEnergy
  Quarter: Q2
  Sector: Healthcare
  Stock Price: 540.85
- Annual Revenue (B): 116.59
  Company: Foodies
  Quarter: Q3
  Sector: Energy
  Stock Price: 533.89
- Annual Revenue (B): 350.61
  Company: AutoDrive
  Quarter: Q2
  Sector: Aerospace
  Stock Price: 641.11
- Annual Revenue (B): 344.92
  Company: AutoDrive
  Quarter: Q3
  Sector: Retail
  Stock Price: 402.06
<end>Here's some yml data, can you convert it to json?
- Close Price: 941.9
  Company: TechnoCorp
  Date: '2021-04-17'
  High Price: 941.9
  Open Price: 368.92
  Volume: 5322769
- Close Price: 693.76
  Company: AutoMotive
  Date: '2019-07-07'
  High Price: 1438.3
  Open Price: 492.73
  Volume: 4982924
- Close Price: 211.77
  Company: AeroSystems
  Date: '2013-04-27'
  High Price: 880.54
  Open Price: 673.86
  Volume: 7341578
- Close Price: 287.98
  Company: GreenEnergy
  Date: '2017-04-28'
  High Price: 901.56
  Open Price: 167.89
  Volume: 2961805
- Close Price: 351.47
  Company: FinanceTrust
  Date: '2020-06-04'
  High Price: 1365.64
  Open Price: 1365.64
  Volume: 4156672
<start>
[
    {
        "Company": "TechnoCorp",
        "Date": "2021-04-17",
        "Open Price": 368.92,
        "Close Price": 941.9,
        "High Price": 941.9,
        "Volume": 5322769
    },
    {
        "Company": "AutoMotive",
        "Date": "2019-07-07",
        "Open Price": 492.73,
        "Close Price": 693.76,
        "High Price": 1438.3,
        "Volume": 4982924
    },
    {
        "Company": "AeroSystems",
        "Date": "2013-04-27",
        "Open Price": 673.86,
        "Close Price": 211.77,
        "High Price": 880.54,
        "Volume": 7341578
    },
    {
        "Company": "GreenEnergy",
        "Date": "2017-04-28",
        "Open Price": 167.89,
        "Close Price": 287.98,
        "High Price": 901.56,
        "Volume": 2961805
    },
    {
        "Company": "FinanceTrust",
        "Date": "2020-06-04",
        "Open Price": 1365.64,
        "Close Price": 351.47,
        "High Price": 1365.64,
        "Volume": 4156672
    }
]
<end>Convert this CSV to YAML:
Company,Sector,Market Cap,Stock Price,Annual Revenue (B),Quarter
RetailHub,Automotive,Mega Cap,92.72,420.39,Q1
AeroSpace,Biotech,Small Cap,555.04,404.59,Q1
HealthPlus,Biotech,Large Cap,521.46,272.75,Q4
EcoEnergy,Technology,Small Cap,688.15,175.13,Q3
TechCorp,Automotive,Mid Cap,555.04,84.86,Q4
Foodies,Finance,Small Cap,497.52,333.69,Q1
HealthPlus,Energy,Mega Cap,150.97,290.25,Q1
RetailHub,Aerospace,Small Cap,788.05,185.11,Q3
AeroSpace,Energy,Large Cap,339.77,74.41,Q2
<start>
- Annual Revenue (B): 420.39
  Company: RetailHub
  Market Cap: Mega Cap
  Quarter: Q1
  Sector: Automotive
  Stock Price: 92.72
- Annual Revenue (B): 404.59
  Company: AeroSpace
  Market Cap: Small Cap
  Quarter: Q1
  Sector: Biotech
  Stock Price: 555.04
- Annual Revenue (B): 272.75
  Company: HealthPlus
  Market Cap: Large Cap
  Quarter: Q4
  Sector: Biotech
  Stock Price: 521.46
- Annual Revenue (B): 175.13
  Company: EcoEnergy
  Market Cap: Small Cap
  Quarter: Q3
  Sector: Technology
  Stock Price: 688.15
- Annual Revenue (B): 84.86
  Company: TechCorp
  Market Cap: Mid Cap
  Quarter: Q4
  Sector: Automotive
  Stock Price: 555.04
- Annual Revenue (B): 333.69
  Company: Foodies
  Market Cap: Small Cap
  Quarter: Q1
  Sector: Finance
  Stock Price: 497.52
- Annual Revenue (B): 290.25
  Company: HealthPlus
  Market Cap: Mega Cap
  Quarter: Q1
  Sector: Energy
  Stock Price: 150.97
- Annual Revenue (B): 185.11
  Company: RetailHub
  Market Cap: Small Cap
  Quarter: Q3
  Sector: Aerospace
  Stock Price: 788.05
- Annual Revenue (B): 74.41
  Company: AeroSpace
  Market Cap: Large Cap
  Quarter: Q2
  Sector: Energy
  Stock Price: 339.77
<end>Here's some plain text data, can you convert it to markdown?
Title: Mystery of the Depths | Director: Mara Moonshadow | Release Year: 2011 | Box Office Earnings (M): 210.58
Title: Beyond the Veil | Director: Orin Shadowalker | Release Year: 2015 | Box Office Earnings (M): 826.02
Title: Starbound Odyssey | Director: Lira Silverleaf | Release Year: 1989 | Box Office Earnings (M): 699.71
Title: The Endless Horizon | Director: Aria Ravenwood | Release Year: 1990 | Box Office Earnings (M): 496.29
Title: Starbound Odyssey | Director: Zara Stormrider | Release Year: 1996 | Box Office Earnings (M): 269.13
<start>
| Title | Director | Release Year | Box Office Earnings (M) |
| --- | --- | --- | --- |
| Mystery of the Depths | Mara Moonshadow | 2011 | 210.58 |
| Beyond the Veil | Orin Shadowalker | 2015 | 826.02 |
| Starbound Odyssey | Lira Silverleaf | 1989 | 699.71 |
| The Endless Horizon | Aria Ravenwood | 1990 | 496.29 |
| Starbound Odyssey | Zara Stormrider | 1996 | 269.13 |
<end>Transform this yml structure to a Csv format:
- Distance (miles): 1214.5
  Duration (hours): 2.6
  End Location: Los Angeles
  Fuel Used (gallons): 92.6
  Start Location: Denver
- Distance (miles): 1043.6
  Duration (hours): 33.7
  End Location: New York
  Fuel Used (gallons): 73.7
  Start Location: Los Angeles
- Distance (miles): 2418.5
  Duration (hours): 3.4
  End Location: Houston
  Fuel Used (gallons): 12.9
  Start Location: Phoenix
- Distance (miles): 2557.1
  Duration (hours): 68.4
  End Location: Los Angeles
  Fuel Used (gallons): 93.0
  Start Location: Chicago
- Distance (miles): 2933.5
  Duration (hours): 44.5
  End Location: San Francisco
  Fuel Used (gallons): 46.1
  Start Location: Houston
<start>
Start Location,End Location,Distance (miles),Duration (hours),Fuel Used (gallons)
Denver,Los Angeles,1214.5,2.6,92.6
Los Angeles,New York,1043.6,33.7,73.7
Phoenix,Houston,2418.5,3.4,12.9
Chicago,Los Angeles,2557.1,68.4,93.0
Houston,San Francisco,2933.5,44.5,46.1
<end>Can you change this Plain text into Json?
Trip Name: Highway Odyssey | Start Location: Miami | End Location: Denver | Distance (miles): 2268.4 | Duration (hours): 18.0 | Fuel Used (gallons): 81.2
Trip Name: Valley Voyage | Start Location: Houston | End Location: Chicago | Distance (miles): 1838.6 | Duration (hours): 22.1 | Fuel Used (gallons): 92.1
Trip Name: City Explorer | Start Location: Chicago | End Location: Los Angeles | Distance (miles): 2533.7 | Duration (hours): 42.7 | Fuel Used (gallons): 68.6
Trip Name: Forest Journey | Start Location: New York | End Location: Chicago | Distance (miles): 1382.9 | Duration (hours): 20.0 | Fuel Used (gallons): 95.8
<start>
[
    {
        "Trip Name": "Highway Odyssey",
        "Start Location": "Miami",
        "End Location": "Denver",
        "Distance (miles)": 2268.4,
        "Duration (hours)": 18.0,
        "Fuel Used (gallons)": 81.2
    },
    {
        "Trip Name": "Valley Voyage",
        "Start Location": "Houston",
        "End Location": "Chicago",
        "Distance (miles)": 1838.6,
        "Duration (hours)": 22.1,
        "Fuel Used (gallons)": 92.1
    },
    {
        "Trip Name": "City Explorer",
        "Start Location": "Chicago",
        "End Location": "Los Angeles",
        "Distance (miles)": 2533.7,
        "Duration (hours)": 42.7,
        "Fuel Used (gallons)": 68.6
    },
    {
        "Trip Name": "Forest Journey",
        "Start Location": "New York",
        "End Location": "Chicago",
        "Distance (miles)": 1382.9,
        "Duration (hours)": 20.0,
        "Fuel Used (gallons)": 95.8
    }
]
<end>Can you change this plain text into YML?
Location: Seattle | Condition: Sunny | Temperature (C): -2.2 | Wind Speed (km/h): 24.5 | Day: Saturday
Location: Seattle | Condition: Cloudy | Temperature (C): 20.6 | Wind Speed (km/h): 2.8 | Day: Wednesday
Location: Houston | Condition: Cloudy | Temperature (C): 39.5 | Wind Speed (km/h): 28.4 | Day: Friday
Location: Los Angeles | Condition: Sunny | Temperature (C): 25.1 | Wind Speed (km/h): 5.7 | Day: Monday
Location: Denver | Condition: Sunny | Temperature (C): 11.3 | Wind Speed (km/h): 28.3 | Day: Tuesday
Location: New York | Condition: Rainy | Temperature (C): 17.6 | Wind Speed (km/h): 21.8 | Day: Monday
Location: Seattle | Condition: Foggy | Temperature (C): 4.8 | Wind Speed (km/h): 27.3 | Day: Friday
Location: Houston | Condition: Foggy | Temperature (C): -3.5 | Wind Speed (km/h): 24.5 | Day: Friday
Location: Chicago | Condition: Rainy | Temperature (C): 24.3 | Wind Speed (km/h): 18.1 | Day: Friday
Location: Seattle | Condition: Stormy | Temperature (C): 25.8 | Wind Speed (km/h): 17.2 | Day: Sunday
<start>
- Condition: Sunny
  Day: Saturday
  Location: Seattle
  Temperature (C): -2.2
  Wind Speed (km/h): 24.5
- Condition: Cloudy
  Day: Wednesday
  Location: Seattle
  Temperature (C): 20.6
  Wind Speed (km/h): 2.8
- Condition: Cloudy
  Day: Friday
  Location: Houston
  Temperature (C): 39.5
  Wind Speed (km/h): 28.4
- Condition: Sunny
  Day: Monday
  Location: Los Angeles
  Temperature (C): 25.1
  Wind Speed (km/h): 5.7
- Condition: Sunny
  Day: Tuesday
  Location: Denver
  Temperature (C): 11.3
  Wind Speed (km/h): 28.3
- Condition: Rainy
  Day: Monday
  Location: New York
  Temperature (C): 17.6
  Wind Speed (km/h): 21.8
- Condition: Foggy
  Day: Friday
  Location: Seattle
  Temperature (C): 4.8
  Wind Speed (km/h): 27.3
- Condition: Foggy
  Day: Friday
  Location: Houston
  Temperature (C): -3.5
  Wind Speed (km/h): 24.5
- Condition: Rainy
  Day: Friday
  Location: Chicago
  Temperature (C): 24.3
  Wind Speed (km/h): 18.1
- Condition: Stormy
  Day: Sunday
  Location: Seattle
  Temperature (C): 25.8
  Wind Speed (km/h): 17.2
<end>Convert this Json to CSV:
[
    {
        "Device Type": "Temperature Sensor",
        "Location": "Hallway",
        "Battery Level (%)": 23.1
    },
    {
        "Device Type": "Pressure Sensor",
        "Location": "Hallway",
        "Battery Level (%)": 18.7
    },
    {
        "Device Type": "Temperature Sensor",
        "Location": "Bedroom",
        "Battery Level (%)": 87.6
    },
    {
        "Device Type": "Motion Detector",
        "Location": "Living Room",
        "Battery Level (%)": 81.3
    },
    {
        "Device Type": "Light Sensor",
        "Location": "Garden",
        "Battery Level (%)": 33.9
    },
    {
        "Device Type": "Temperature Sensor",
        "Location": "Hallway",
        "Battery Level (%)": 88.0
    },
    {
        "Device Type": "Humidity Sensor",
        "Location": "Bathroom",
        "Battery Level (%)": 83.3
    },
    {
        "Device Type": "Pressure Sensor",
        "Location": "Living Room",
        "Battery Level (%)": 41.8
    },
    {
        "Device Type": "Temperature Sensor",
        "Location": "Garage",
        "Battery Level (%)": 69.8
    },
    {
        "Device Type": "Pressure Sensor",
        "Location": "Kitchen",
        "Battery Level (%)": 44.2
    }
]<start>
Device Type,Location,Battery Level (%)
Temperature Sensor,Hallway,23.1
Pressure Sensor,Hallway,18.7
Temperature Sensor,Bedroom,87.6
Motion Detector,Living Room,81.3
Light Sensor,Garden,33.9
Temperature Sensor,Hallway,88.0
Humidity Sensor,Bathroom,83.3
Pressure Sensor,Living Room,41.8
Temperature Sensor,Garage,69.8
Pressure Sensor,Kitchen,44.2
<end>Please transform the following plain text data into Yaml:
Device ID: device-0100 | Location: Office | Timestamp: 2022-02-24 22:11:35
Device ID: device-0056 | Location: Garage | Timestamp: 2023-09-17 16:55:50
Device ID: device-0044 | Location: Kitchen | Timestamp: 2023-12-03 22:17:29
Device ID: device-0040 | Location: Garden | Timestamp: 2021-01-24 17:31:33
Device ID: device-0036 | Location: Garage | Timestamp: 2022-01-28 23:05:45
Device ID: device-0067 | Location: Office | Timestamp: 2023-11-03 17:47:43
Device ID: device-0074 | Location: Office | Timestamp: 2023-11-08 14:39:51
Device ID: device-0003 | Location: Garden | Timestamp: 2021-02-14 23:30:52
Device ID: device-0016 | Location: Bedroom | Timestamp: 2022-05-23 10:45:10
<start>
- Device ID: device-0100
  Location: Office
  Timestamp: '2022-02-24 22:11:35'
- Device ID: device-0056
  Location: Garage
  Timestamp: '2023-09-17 16:55:50'
- Device ID: device-0044
  Location: Kitchen
  Timestamp: '2023-12-03 22:17:29'
- Device ID: device-0040
  Location: Garden
  Timestamp: '2021-01-24 17:31:33'
- Device ID: device-0036
  Location: Garage
  Timestamp: '2022-01-28 23:05:45'
- Device ID: device-0067
  Location: Office
  Timestamp: '2023-11-03 17:47:43'
- Device ID: device-0074
  Location: Office
  Timestamp: '2023-11-08 14:39:51'
- Device ID: device-0003
  Location: Garden
  Timestamp: '2021-02-14 23:30:52'
- Device ID: device-0016
  Location: Bedroom
  Timestamp: '2022-05-23 10:45:10'
<end>Here's some markdown data, can you convert it to Csv?
| Device Type | Location | Battery Level (%) | Reading Value | Timestamp |
| --- | --- | --- | --- | --- |
| Motion Detector | Bedroom | 81.5 | 52.21 | 2021-06-13 16:50:36 |
| Pressure Sensor | Kitchen | 71.5 | 18.15 | 2022-12-01 13:59:38 |
| Light Sensor | Garden | 46.1 | 76.12 | 2022-08-03 04:13:38 |
| Motion Detector | Garage | 34.8 | 15.73 | 2023-03-07 07:03:38 |
| Motion Detector | Living Room | 59.0 | 60.37 | 2021-07-23 21:59:45 |
| Pressure Sensor | Garage | 29.4 | -28.2 | 2023-09-17 17:38:14 |
| Temperature Sensor | Living Room | 55.2 | 57.95 | 2022-10-23 00:24:50 |
| Pressure Sensor | Kitchen | 57.7 | 6.33 | 2022-08-23 07:17:08 |<start>
Device Type,Location,Battery Level (%),Reading Value,Timestamp
Motion Detector,Bedroom,81.5,52.21,2021-06-13 16:50:36
Pressure Sensor,Kitchen,71.5,18.15,2022-12-01 13:59:38
Light Sensor,Garden,46.1,76.12,2022-08-03 04:13:38
Motion Detector,Garage,34.8,15.73,2023-03-07 07:03:38
Motion Detector,Living Room,59.0,60.37,2021-07-23 21:59:45
Pressure Sensor,Garage,29.4,-28.2,2023-09-17 17:38:14
Temperature Sensor,Living Room,55.2,57.95,2022-10-23 00:24:50
Pressure Sensor,Kitchen,57.7,6.33,2022-08-23 07:17:08
<end>Please transform the following Csv data into json:
Product Name,Stock Quantity,Category
Apparatus,484,Automotive
Gadget,330,Sports
Contraption,264,Household
Instrument,391,Toys
Gadget,144,Household
Instrument,469,Household
Thingamajig,62,Automotive
Apparatus,418,Automotive
<start>
[
    {
        "Product Name": "Apparatus",
        "Stock Quantity": 484,
        "Category": "Automotive"
    },
    {
        "Product Name": "Gadget",
        "Stock Quantity": 330,
        "Category": "Sports"
    },
    {
        "Product Name": "Contraption",
        "Stock Quantity": 264,
        "Category": "Household"
    },
    {
        "Product Name": "Instrument",
        "Stock Quantity": 391,
        "Category": "Toys"
    },
    {
        "Product Name": "Gadget",
        "Stock Quantity": 144,
        "Category": "Household"
    },
    {
        "Product Name": "Instrument",
        "Stock Quantity": 469,
        "Category": "Household"
    },
    {
        "Product Name": "Thingamajig",
        "Stock Quantity": 62,
        "Category": "Automotive"
    },
    {
        "Product Name": "Apparatus",
        "Stock Quantity": 418,
        "Category": "Automotive"
    }
]
<end>Convert this csv to json:
Director,Genre,Release Year
Zara Stormrider,Fantasy,1990
Aria Ravenwood,Sci-Fi,1997
Aria Ravenwood,Drama,1990
Talon Blackthorn,Action,2013
Drake Nightshade,Fantasy,1977
Aria Ravenwood,Comedy,2017
Zara Stormrider,Thriller,2017
Lira Silverleaf,Thriller,1974
Drake Nightshade,Drama,2016
Aria Ravenwood,Fantasy,2017
<start>
[
    {
        "Director": "Zara Stormrider",
        "Genre": "Fantasy",
        "Release Year": 1990
    },
    {
        "Director": "Aria Ravenwood",
        "Genre": "Sci-Fi",
        "Release Year": 1997
    },
    {
        "Director": "Aria Ravenwood",
        "Genre": "Drama",
        "Release Year": 1990
    },
    {
        "Director": "Talon Blackthorn",
        "Genre": "Action",
        "Release Year": 2013
    },
    {
        "Director": "Drake Nightshade",
        "Genre": "Fantasy",
        "Release Year": 1977
    },
    {
        "Director": "Aria Ravenwood",
        "Genre": "Comedy",
        "Release Year": 2017
    },
    {
        "Director": "Zara Stormrider",
        "Genre": "Thriller",
        "Release Year": 2017
    },
    {
        "Director": "Lira Silverleaf",
        "Genre": "Thriller",
        "Release Year": 1974
    },
    {
        "Director": "Drake Nightshade",
        "Genre": "Drama",
        "Release Year": 2016
    },
    {
        "Director": "Aria Ravenwood",
        "Genre": "Fantasy",
        "Release Year": 2017
    }
]
<end>Please transform the following MARKDOWN data into Json:
| Restaurant Name | Location |
| --- | --- |
| BBQ Barn | Los Angeles |
| Pasta Palace | Phoenix |
| Taco Town | San Francisco |
| BBQ Barn | Phoenix |
| Pizza Planet | Seattle |
| Vegan Delight | Seattle |
| Taco Town | New York |
| The Steakhouse | San Francisco |
| Sushi World | Seattle |
| Vegan Delight | Phoenix |<start>
[
    {
        "Restaurant Name": "BBQ Barn",
        "Location": "Los Angeles"
    },
    {
        "Restaurant Name": "Pasta Palace",
        "Location": "Phoenix"
    },
    {
        "Restaurant Name": "Taco Town",
        "Location": "San Francisco"
    },
    {
        "Restaurant Name": "BBQ Barn",
        "Location": "Phoenix"
    },
    {
        "Restaurant Name": "Pizza Planet",
        "Location": "Seattle"
    },
    {
        "Restaurant Name": "Vegan Delight",
        "Location": "Seattle"
    },
    {
        "Restaurant Name": "Taco Town",
        "Location": "New York"
    },
    {
        "Restaurant Name": "The Steakhouse",
        "Location": "San Francisco"
    },
    {
        "Restaurant Name": "Sushi World",
        "Location": "Seattle"
    },
    {
        "Restaurant Name": "Vegan Delight",
        "Location": "Phoenix"
    }
]
<end>Can you change this YML into Csv?
- Close Price: 253.69
  Company: AeroSystems
  Date: '2021-08-28'
  High Price: 1172.74
  Low Price: 253.69
  Open Price: 1172.74
  Volume: 2803407
- Close Price: 1242.78
  Company: AeroSystems
  Date: '2017-08-04'
  High Price: 1450.96
  Low Price: 1242.78
  Open Price: 1450.96
  Volume: 448493
- Close Price: 635.93
  Company: FinanceTrust
  Date: '2021-06-21'
  High Price: 1394.82
  Low Price: 635.93
  Open Price: 1013.24
  Volume: 5666098
- Close Price: 1263.67
  Company: AeroSystems
  Date: '2012-12-09'
  High Price: 1271.3
  Low Price: 1042.76
  Open Price: 1271.3
  Volume: 3014585
- Close Price: 131.8
  Company: AeroSystems
  Date: '2014-02-19'
  High Price: 1242.78
  Low Price: 65.15
  Open Price: 65.15
  Volume: 3098614
- Close Price: 1180.77
  Company: FoodChain
  Date: '2016-05-15'
  High Price: 1180.77
  Low Price: 342.1
  Open Price: 559.22
  Volume: 5255833
<start>
Company,Date,Open Price,Close Price,High Price,Low Price,Volume
AeroSystems,2021-08-28,1172.74,253.69,1172.74,253.69,2803407
AeroSystems,2017-08-04,1450.96,1242.78,1450.96,1242.78,448493
FinanceTrust,2021-06-21,1013.24,635.93,1394.82,635.93,5666098
AeroSystems,2012-12-09,1271.3,1263.67,1271.3,1042.76,3014585
AeroSystems,2014-02-19,65.15,131.8,1242.78,65.15,3098614
FoodChain,2016-05-15,559.22,1180.77,1180.77,342.1,5255833
<end>Here's some json data, can you convert it to MARKDOWN?
[
    {
        "Condition": "Sunny",
        "Temperature (C)": -7.9,
        "Day": "Thursday"
    },
    {
        "Condition": "Windy",
        "Temperature (C)": 2.1,
        "Day": "Wednesday"
    },
    {
        "Condition": "Stormy",
        "Temperature (C)": 31.9,
        "Day": "Thursday"
    },
    {
        "Condition": "Stormy",
        "Temperature (C)": 17.8,
        "Day": "Tuesday"
    },
    {
        "Condition": "Windy",
        "Temperature (C)": 29.1,
        "Day": "Thursday"
    },
    {
        "Condition": "Sunny",
        "Temperature (C)": 28.3,
        "Day": "Wednesday"
    }
]<start>
| Condition | Temperature (C) | Day |
| --- | --- | --- |
| Sunny | -7.9 | Thursday |
| Windy | 2.1 | Wednesday |
| Stormy | 31.9 | Thursday |
| Stormy | 17.8 | Tuesday |
| Windy | 29.1 | Thursday |
| Sunny | 28.3 | Wednesday |
<end>Can you change this CSV into Yaml?
Title,Author,Genre,Publication Year,Rating
Shadows of Solitude,Isla Windrider,Non-Fiction,1997,3.1
Echoes of Eternity,Luna Silverleaf,Non-Fiction,2022,3.2
The Silent Grove,Rowan Ashborne,Science Fiction,1994,2.7
Tales of the Brave,Rowan Ashborne,Mystery,1965,1.5
<start>
- Author: Isla Windrider
  Genre: Non-Fiction
  Publication Year: 1997
  Rating: 3.1
  Title: Shadows of Solitude
- Author: Luna Silverleaf
  Genre: Non-Fiction
  Publication Year: 2022
  Rating: 3.2
  Title: Echoes of Eternity
- Author: Rowan Ashborne
  Genre: Science Fiction
  Publication Year: 1994
  Rating: 2.7
  Title: The Silent Grove
- Author: Rowan Ashborne
  Genre: Mystery
  Publication Year: 1965
  Rating: 1.5
  Title: Tales of the Brave
<end>Here's some Csv data, can you convert it to MARKDOWN?
Title,Director,Genre,Release Year,Box Office Earnings (M)
The Great Expedition,Lira Silverleaf,Action,2015,201.38
Beyond the Veil,Lira Silverleaf,Horror,2019,830.24
Dreamwalker,Drake Nightshade,Horror,2014,628.63
Beyond the Veil,Zara Stormrider,Drama,2021,14.9
Dreamwalker,Aria Ravenwood,Action,2000,666.87
The Endless Horizon,Orin Shadowalker,Adventure,1978,333.65
Mystery of the Depths,Mara Moonshadow,Horror,1973,55.76
Rise of the Titans,Lira Silverleaf,Sci-Fi,2016,881.72
<start>
| Title | Director | Genre | Release Year | Box Office Earnings (M) |
| --- | --- | --- | --- | --- |
| The Great Expedition | Lira Silverleaf | Action | 2015 | 201.38 |
| Beyond the Veil | Lira Silverleaf | Horror | 2019 | 830.24 |
| Dreamwalker | Drake Nightshade | Horror | 2014 | 628.63 |
| Beyond the Veil | Zara Stormrider | Drama | 2021 | 14.9 |
| Dreamwalker | Aria Ravenwood | Action | 2000 | 666.87 |
| The Endless Horizon | Orin Shadowalker | Adventure | 1978 | 333.65 |
| Mystery of the Depths | Mara Moonshadow | Horror | 1973 | 55.76 |
| Rise of the Titans | Lira Silverleaf | Sci-Fi | 2016 | 881.72 |
<end>Convert this csv to Yml:
Age,Birth Month,Income
62,July,250000
21,June,230000
52,April,190000
<start>
- Age: 62
  Birth Month: July
  Income: 250000
- Age: 21
  Birth Month: June
  Income: 230000
- Age: 52
  Birth Month: April
  Income: 190000
<end>Transform this Yaml structure to a CSV format:
- Distance (miles): 2819.6
  End Location: Denver
  Fuel Used (gallons): 61.6
  Start Location: Miami
  Trip Name: Coast to Coast
- Distance (miles): 2251.6
  End Location: Chicago
  Fuel Used (gallons): 9.5
  Start Location: Phoenix
  Trip Name: Highway Odyssey
- Distance (miles): 820.5
  End Location: New York
  Fuel Used (gallons): 41.1
  Start Location: Phoenix
  Trip Name: Historic Route
- Distance (miles): 593.8
  End Location: Houston
  Fuel Used (gallons): 19.8
  Start Location: San Francisco
  Trip Name: Mountain Adventure
- Distance (miles): 2723.2
  End Location: New York
  Fuel Used (gallons): 96.6
  Start Location: San Francisco
  Trip Name: Lakeside Retreat
- Distance (miles): 2542.5
  End Location: Phoenix
  Fuel Used (gallons): 83.8
  Start Location: San Francisco
  Trip Name: City Explorer
- Distance (miles): 738.0
  End Location: Los Angeles
  Fuel Used (gallons): 26.4
  Start Location: Chicago
  Trip Name: Forest Journey
- Distance (miles): 2579.8
  End Location: Chicago
  Fuel Used (gallons): 35.1
  Start Location: Houston
  Trip Name: Forest Journey
<start>
Trip Name,Start Location,End Location,Distance (miles),Fuel Used (gallons)
Coast to Coast,Miami,Denver,2819.6,61.6
Highway Odyssey,Phoenix,Chicago,2251.6,9.5
Historic Route,Phoenix,New York,820.5,41.1
Mountain Adventure,San Francisco,Houston,593.8,19.8
Lakeside Retreat,San Francisco,New York,2723.2,96.6
City Explorer,San Francisco,Phoenix,2542.5,83.8
Forest Journey,Chicago,Los Angeles,738.0,26.4
Forest Journey,Houston,Chicago,2579.8,35.1
<end>Please transform the following Yaml data into MARKDOWN:
- Close Price: 381.82
  Date: '2015-11-18'
  High Price: 1264.53
  Volume: 7544963
- Close Price: 784.61
  Date: '2014-10-03'
  High Price: 996.4
  Volume: 3426992
- Close Price: 574.0
  Date: '2020-08-11'
  High Price: 918.94
  Volume: 8785837
- Close Price: 323.66
  Date: '2022-04-06'
  High Price: 1125.69
  Volume: 5105036
- Close Price: 607.67
  Date: '2019-08-09'
  High Price: 607.67
  Volume: 6045550
- Close Price: 470.45
  Date: '2023-02-22'
  High Price: 1176.73
  Volume: 6673666
<start>
| Date | Close Price | High Price | Volume |
| --- | --- | --- | --- |
| 2015-11-18 | 381.82 | 1264.53 | 7544963 |
| 2014-10-03 | 784.61 | 996.4 | 3426992 |
| 2020-08-11 | 574.0 | 918.94 | 8785837 |
| 2022-04-06 | 323.66 | 1125.69 | 5105036 |
| 2019-08-09 | 607.67 | 607.67 | 6045550 |
| 2023-02-22 | 470.45 | 1176.73 | 6673666 |
<end>Convert this plain text to csv:
Product Name: Gadget | SKU: SKU-1036 | Price: 360.49
Product Name: Doohickey | SKU: SKU-1077 | Price: 308.42
Product Name: Contraption | SKU: SKU-1084 | Price: 181.57
Product Name: Doohickey | SKU: SKU-1088 | Price: 204.71
Product Name: Widget | SKU: SKU-1084 | Price: 61.56
Product Name: Device | SKU: SKU-1016 | Price: 179.85
Product Name: Gadget | SKU: SKU-1077 | Price: 168.31
Product Name: Instrument | SKU: SKU-1078 | Price: 377.93
Product Name: Instrument | SKU: SKU-1013 | Price: 405.92
Product Name: Doohickey | SKU: SKU-1087 | Price: 371.3
<start>
Product Name,SKU,Price
Gadget,SKU-1036,360.49
Doohickey,SKU-1077,308.42
Contraption,SKU-1084,181.57
Doohickey,SKU-1088,204.71
Widget,SKU-1084,61.56
Device,SKU-1016,179.85
Gadget,SKU-1077,168.31
Instrument,SKU-1078,377.93
Instrument,SKU-1013,405.92
Doohickey,SKU-1087,371.3
<end>Transform this PLAIN TEXT structure to a yaml format:
Restaurant Name: Burger Haven | Cuisine: Italian | Location: Seattle | Rating: 1 | Price Range: $$$
Restaurant Name: Vegan Delight | Cuisine: Italian | Location: Phoenix | Rating: 2 | Price Range: $$$
Restaurant Name: Taco Town | Cuisine: Indian | Location: New York | Rating: 3 | Price Range: $$
Restaurant Name: Taco Town | Cuisine: American | Location: San Francisco | Rating: 2 | Price Range: $$$$$
Restaurant Name: Curry Corner | Cuisine: French | Location: San Francisco | Rating: 3 | Price Range: $
<start>
- Cuisine: Italian
  Location: Seattle
  Price Range: $$$
  Rating: 1
  Restaurant Name: Burger Haven
- Cuisine: Italian
  Location: Phoenix
  Price Range: $$$
  Rating: 2
  Restaurant Name: Vegan Delight
- Cuisine: Indian
  Location: New York
  Price Range: $$
  Rating: 3
  Restaurant Name: Taco Town
- Cuisine: American
  Location: San Francisco
  Price Range: $$$$$
  Rating: 2
  Restaurant Name: Taco Town
- Cuisine: French
  Location: San Francisco
  Price Range: $
  Rating: 3
  Restaurant Name: Curry Corner
<end>Please transform the following Yaml data into json:
- Close Price: 423.64
  Company: MediaGroup
  High Price: 1351.82
  Low Price: 214.79
  Volume: 3774189
- Close Price: 1240.15
  Company: TechnoCorp
  High Price: 1240.15
  Low Price: 610.67
  Volume: 3976163
- Close Price: 1472.52
  Company: AutoMotive
  High Price: 1472.52
  Low Price: 768.99
  Volume: 1375415
- Close Price: 49.1
  Company: MediaGroup
  High Price: 921.37
  Low Price: 49.1
  Volume: 7905202
- Close Price: 897.73
  Company: GreenEnergy
  High Price: 1396.88
  Low Price: 257.45
  Volume: 272530
- Close Price: 537.98
  Company: BioLife
  High Price: 1219.73
  Low Price: 537.98
  Volume: 463972
- Close Price: 897.73
  Company: BioLife
  High Price: 1410.94
  Low Price: 858.47
  Volume: 3523717
- Close Price: 1376.45
  Company: GreenEnergy
  High Price: 1376.45
  Low Price: 417.6
  Volume: 819794
- Close Price: 1426.21
  Company: AeroSystems
  High Price: 1426.21
  Low Price: 32.37
  Volume: 708044
<start>
[
    {
        "Company": "MediaGroup",
        "Close Price": 423.64,
        "High Price": 1351.82,
        "Low Price": 214.79,
        "Volume": 3774189
    },
    {
        "Company": "TechnoCorp",
        "Close Price": 1240.15,
        "High Price": 1240.15,
        "Low Price": 610.67,
        "Volume": 3976163
    },
    {
        "Company": "AutoMotive",
        "Close Price": 1472.52,
        "High Price": 1472.52,
        "Low Price": 768.99,
        "Volume": 1375415
    },
    {
        "Company": "MediaGroup",
        "Close Price": 49.1,
        "High Price": 921.37,
        "Low Price": 49.1,
        "Volume": 7905202
    },
    {
        "Company": "GreenEnergy",
        "Close Price": 897.73,
        "High Price": 1396.88,
        "Low Price": 257.45,
        "Volume": 272530
    },
    {
        "Company": "BioLife",
        "Close Price": 537.98,
        "High Price": 1219.73,
        "Low Price": 537.98,
        "Volume": 463972
    },
    {
        "Company": "BioLife",
        "Close Price": 897.73,
        "High Price": 1410.94,
        "Low Price": 858.47,
        "Volume": 3523717
    },
    {
        "Company": "GreenEnergy",
        "Close Price": 1376.45,
        "High Price": 1376.45,
        "Low Price": 417.6,
        "Volume": 819794
    },
    {
        "Company": "AeroSystems",
        "Close Price": 1426.21,
        "High Price": 1426.21,
        "Low Price": 32.37,
        "Volume": 708044
    }
]
<end>Convert this markdown to PLAIN TEXT:
| Company | Open Price | Low Price | Volume |
| --- | --- | --- | --- |
| BioLife | 890.64 | 116.41 | 8961384 |
| RetailWorld | 649.92 | 157.45 | 2047483 |
| FinanceTrust | 1188.48 | 1154.14 | 4435659 |<start>
Company: BioLife | Open Price: 890.64 | Low Price: 116.41 | Volume: 8961384
Company: RetailWorld | Open Price: 649.92 | Low Price: 157.45 | Volume: 2047483
Company: FinanceTrust | Open Price: 1188.48 | Low Price: 1154.14 | Volume: 4435659
<end>Can you change this json into Csv?
[
    {
        "Company": "AutoDrive",
        "Sector": "Biotech",
        "Market Cap": "Small Cap",
        "Annual Revenue (B)": 422.71,
        "Quarter": "Q3"
    },
    {
        "Company": "Foodies",
        "Sector": "Biotech",
        "Market Cap": "Small Cap",
        "Annual Revenue (B)": 312.51,
        "Quarter": "Q1"
    },
    {
        "Company": "RetailHub",
        "Sector": "Biotech",
        "Market Cap": "Small Cap",
        "Annual Revenue (B)": 144.84,
        "Quarter": "Q2"
    },
    {
        "Company": "GlobalTrade",
        "Sector": "Energy",
        "Market Cap": "Mid Cap",
        "Annual Revenue (B)": 462.79,
        "Quarter": "Q3"
    }
]<start>
Company,Sector,Market Cap,Annual Revenue (B),Quarter
AutoDrive,Biotech,Small Cap,422.71,Q3
Foodies,Biotech,Small Cap,312.51,Q1
RetailHub,Biotech,Small Cap,144.84,Q2
GlobalTrade,Energy,Mid Cap,462.79,Q3
<end>Here's some MARKDOWN data, can you convert it to json?
| Location | Condition | Temperature (C) | Day |
| --- | --- | --- | --- |
| New York | Foggy | -6.5 | Thursday |
| New York | Cloudy | 26.8 | Monday |
| Chicago | Stormy | -3.0 | Sunday |<start>
[
    {
        "Location": "New York",
        "Condition": "Foggy",
        "Temperature (C)": -6.5,
        "Day": "Thursday"
    },
    {
        "Location": "New York",
        "Condition": "Cloudy",
        "Temperature (C)": 26.8,
        "Day": "Monday"
    },
    {
        "Location": "Chicago",
        "Condition": "Stormy",
        "Temperature (C)": -3.0,
        "Day": "Sunday"
    }
]
<end>Can you change this MARKDOWN into YML?
| Device ID | Device Type | Battery Level (%) | Timestamp |
| --- | --- | --- | --- |
| device-0096 | Temperature Sensor | 73.2 | 2023-12-05 15:58:59 |
| device-0097 | Motion Detector | 31.8 | 2022-11-23 08:16:41 |
| device-0008 | Light Sensor | 85.8 | 2022-12-16 06:39:58 |
| device-0084 | Light Sensor | 97.5 | 2023-02-22 03:02:17 |
| device-0058 | Light Sensor | 17.1 | 2021-01-13 07:33:24 |
| device-0073 | Motion Detector | 10.7 | 2021-06-20 15:36:52 |
| device-0036 | Humidity Sensor | 12.8 | 2022-10-10 02:48:44 |
| device-0010 | Light Sensor | 26.4 | 2021-04-13 04:30:16 |
| device-0012 | Motion Detector | 15.8 | 2021-02-26 12:29:13 |<start>
- Battery Level (%): 73.2
  Device ID: device-0096
  Device Type: Temperature Sensor
  Timestamp: '2023-12-05 15:58:59'
- Battery Level (%): 31.8
  Device ID: device-0097
  Device Type: Motion Detector
  Timestamp: '2022-11-23 08:16:41'
- Battery Level (%): 85.8
  Device ID: device-0008
  Device Type: Light Sensor
  Timestamp: '2022-12-16 06:39:58'
- Battery Level (%): 97.5
  Device ID: device-0084
  Device Type: Light Sensor
  Timestamp: '2023-02-22 03:02:17'
- Battery Level (%): 17.1
  Device ID: device-0058
  Device Type: Light Sensor
  Timestamp: '2021-01-13 07:33:24'
- Battery Level (%): 10.7
  Device ID: device-0073
  Device Type: Motion Detector
  Timestamp: '2021-06-20 15:36:52'
- Battery Level (%): 12.8
  Device ID: device-0036
  Device Type: Humidity Sensor
  Timestamp: '2022-10-10 02:48:44'
- Battery Level (%): 26.4
  Device ID: device-0010
  Device Type: Light Sensor
  Timestamp: '2021-04-13 04:30:16'
- Battery Level (%): 15.8
  Device ID: device-0012
  Device Type: Motion Detector
  Timestamp: '2021-02-26 12:29:13'
<end>Please transform the following Json data into markdown:
[
    {
        "Company": "GreenEnergy",
        "Date": "2021-07-13",
        "Open Price": 661.16,
        "Close Price": 970.66,
        "Low Price": 661.16,
        "Volume": 2187712
    },
    {
        "Company": "AeroSystems",
        "Date": "2023-05-19",
        "Open Price": 321.36,
        "Close Price": 1418.91,
        "Low Price": 321.36,
        "Volume": 6358517
    },
    {
        "Company": "AeroSystems",
        "Date": "2013-11-01",
        "Open Price": 734.13,
        "Close Price": 332.37,
        "Low Price": 210.7,
        "Volume": 790772
    },
    {
        "Company": "AeroSystems",
        "Date": "2011-10-03",
        "Open Price": 316.82,
        "Close Price": 1258.58,
        "Low Price": 316.82,
        "Volume": 2580652
    },
    {
        "Company": "AutoMotive",
        "Date": "2010-09-20",
        "Open Price": 1021.16,
        "Close Price": 1009.27,
        "Low Price": 1009.27,
        "Volume": 3841340
    }
]<start>
| Company | Date | Open Price | Close Price | Low Price | Volume |
| --- | --- | --- | --- | --- | --- |
| GreenEnergy | 2021-07-13 | 661.16 | 970.66 | 661.16 | 2187712 |
| AeroSystems | 2023-05-19 | 321.36 | 1418.91 | 321.36 | 6358517 |
| AeroSystems | 2013-11-01 | 734.13 | 332.37 | 210.7 | 790772 |
| AeroSystems | 2011-10-03 | 316.82 | 1258.58 | 316.82 | 2580652 |
| AutoMotive | 2010-09-20 | 1021.16 | 1009.27 | 1009.27 | 3841340 |
<end>Can you change this yaml into CSV?
- Close Price: 77.38
  Company: AeroSystems
  High Price: 1309.14
  Low Price: 77.38
  Open Price: 1309.14
- Close Price: 457.5
  Company: FoodChain
  High Price: 663.89
  Low Price: 457.5
  Open Price: 491.92
- Close Price: 1048.71
  Company: AeroSystems
  High Price: 1079.72
  Low Price: 905.82
  Open Price: 1079.72
- Close Price: 834.29
  Company: GreenEnergy
  High Price: 1238.2
  Low Price: 98.42
  Open Price: 747.81
- Close Price: 1241.98
  Company: AeroSystems
  High Price: 1241.98
  Low Price: 261.58
  Open Price: 427.47
- Close Price: 281.72
  Company: FoodChain
  High Price: 1185.5
  Low Price: 281.72
  Open Price: 1185.5
- Close Price: 1364.72
  Company: TechnoCorp
  High Price: 1364.72
  Low Price: 581.52
  Open Price: 581.52
- Close Price: 663.14
  Company: FinanceTrust
  High Price: 1279.1
  Low Price: 235.59
  Open Price: 235.59
<start>
Company,Open Price,Close Price,High Price,Low Price
AeroSystems,1309.14,77.38,1309.14,77.38
FoodChain,491.92,457.5,663.89,457.5
AeroSystems,1079.72,1048.71,1079.72,905.82
GreenEnergy,747.81,834.29,1238.2,98.42
AeroSystems,427.47,1241.98,1241.98,261.58
FoodChain,1185.5,281.72,1185.5,281.72
TechnoCorp,581.52,1364.72,1364.72,581.52
FinanceTrust,235.59,663.14,1279.1,235.59
<end>Transform this csv structure to a Json format:
Device ID,Device Type,Location,Battery Level (%),Reading Value
device-0053,Motion Detector,Kitchen,43.6,-6.47
device-0028,Motion Detector,Garden,92.7,82.05
device-0035,Pressure Sensor,Bathroom,47.6,20.93
device-0072,Light Sensor,Bathroom,78.9,-28.51
<start>
[
    {
        "Device ID": "device-0053",
        "Device Type": "Motion Detector",
        "Location": "Kitchen",
        "Battery Level (%)": 43.6,
        "Reading Value": -6.47
    },
    {
        "Device ID": "device-0028",
        "Device Type": "Motion Detector",
        "Location": "Garden",
        "Battery Level (%)": 92.7,
        "Reading Value": 82.05
    },
    {
        "Device ID": "device-0035",
        "Device Type": "Pressure Sensor",
        "Location": "Bathroom",
        "Battery Level (%)": 47.6,
        "Reading Value": 20.93
    },
    {
        "Device ID": "device-0072",
        "Device Type": "Light Sensor",
        "Location": "Bathroom",
        "Battery Level (%)": 78.9,
        "Reading Value": -28.51
    }
]
<end>Can you change this PLAIN TEXT into YAML?
Age: 29 | Birth Month: July | City: Columbus
Age: 65 | Birth Month: January | City: Memphis
Age: 28 | Birth Month: October | City: Portland
<start>
- Age: 29
  Birth Month: July
  City: Columbus
- Age: 65
  Birth Month: January
  City: Memphis
- Age: 28
  Birth Month: October
  City: Portland
<end>Please transform the following json data into CSV:
[
    {
        "Restaurant Name": "Taco Town",
        "Location": "Miami",
        "Rating": 2,
        "Price Range": "$$$"
    },
    {
        "Restaurant Name": "Pasta Palace",
        "Location": "Seattle",
        "Rating": 3,
        "Price Range": "$$$"
    },
    {
        "Restaurant Name": "Pizza Planet",
        "Location": "Miami",
        "Rating": 4,
        "Price Range": "$$$"
    },
    {
        "Restaurant Name": "The Steakhouse",
        "Location": "Seattle",
        "Rating": 3,
        "Price Range": "$$$$$"
    },
    {
        "Restaurant Name": "Pizza Planet",
        "Location": "Los Angeles",
        "Rating": 5,
        "Price Range": "$$"
    },
    {
        "Restaurant Name": "Sushi World",
        "Location": "San Francisco",
        "Rating": 5,
        "Price Range": "$$$"
    },
    {
        "Restaurant Name": "BBQ Barn",
        "Location": "New York",
        "Rating": 5,
        "Price Range": "$$$$$"
    }
]<start>
Restaurant Name,Location,Rating,Price Range
Taco Town,Miami,2,$$$
Pasta Palace,Seattle,3,$$$
Pizza Planet,Miami,4,$$$
The Steakhouse,Seattle,3,$$$$$
Pizza Planet,Los Angeles,5,$$
Sushi World,San Francisco,5,$$$
BBQ Barn,New York,5,$$$$$
<end>Here's some yaml data, can you convert it to markdown?
- Price Range: $$
  Restaurant Name: Curry Corner
- Price Range: $
  Restaurant Name: The Steakhouse
- Price Range: $$$$$
  Restaurant Name: Pizza Planet
- Price Range: $$
  Restaurant Name: Pizza Planet
- Price Range: $$$
  Restaurant Name: Sushi World
- Price Range: $$
  Restaurant Name: Pasta Palace
- Price Range: $
  Restaurant Name: Curry Corner
- Price Range: $$$$$
  Restaurant Name: Pasta Palace
- Price Range: $$$$
  Restaurant Name: Taco Town
<start>
| Restaurant Name | Price Range |
| --- | --- |
| Curry Corner | $$ |
| The Steakhouse | $ |
| Pizza Planet | $$$$$ |
| Pizza Planet | $$ |
| Sushi World | $$$ |
| Pasta Palace | $$ |
| Curry Corner | $ |
| Pasta Palace | $$$$$ |
| Taco Town | $$$$ |
<end>Transform this plain text structure to a csv format:
Title: Edge of Infinity | Box Office Earnings (M): 580.13
Title: Starbound Odyssey | Box Office Earnings (M): 971.64
Title: Mystery of the Depths | Box Office Earnings (M): 571.7
Title: Edge of Infinity | Box Office Earnings (M): 915.03
Title: The Endless Horizon | Box Office Earnings (M): 606.94
Title: Beyond the Veil | Box Office Earnings (M): 528.99
Title: Dreamwalker | Box Office Earnings (M): 264.52
Title: Dreamwalker | Box Office Earnings (M): 221.16
Title: Dreamwalker | Box Office Earnings (M): 489.63
<start>
Title,Box Office Earnings (M)
Edge of Infinity,580.13
Starbound Odyssey,971.64
Mystery of the Depths,571.7
Edge of Infinity,915.03
The Endless Horizon,606.94
Beyond the Veil,528.99
Dreamwalker,264.52
Dreamwalker,221.16
Dreamwalker,489.63
<end>Please transform the following plain text data into YML:
Market Cap: Mega Cap | Annual Revenue (B): 184.32 | Quarter: Q3
Market Cap: Small Cap | Annual Revenue (B): 64.46 | Quarter: Q4
Market Cap: Small Cap | Annual Revenue (B): 256.73 | Quarter: Q2
Market Cap: Small Cap | Annual Revenue (B): 142.65 | Quarter: Q4
Market Cap: Large Cap | Annual Revenue (B): 287.03 | Quarter: Q2
Market Cap: Small Cap | Annual Revenue (B): 172.73 | Quarter: Q1
Market Cap: Mega Cap | Annual Revenue (B): 293.82 | Quarter: Q1
Market Cap: Mid Cap | Annual Revenue (B): 304.25 | Quarter: Q1
Market Cap: Small Cap | Annual Revenue (B): 313.64 | Quarter: Q2
<start>
- Annual Revenue (B): 184.32
  Market Cap: Mega Cap
  Quarter: Q3
- Annual Revenue (B): 64.46
  Market Cap: Small Cap
  Quarter: Q4
- Annual Revenue (B): 256.73
  Market Cap: Small Cap
  Quarter: Q2
- Annual Revenue (B): 142.65
  Market Cap: Small Cap
  Quarter: Q4
- Annual Revenue (B): 287.03
  Market Cap: Large Cap
  Quarter: Q2
- Annual Revenue (B): 172.73
  Market Cap: Small Cap
  Quarter: Q1
- Annual Revenue (B): 293.82
  Market Cap: Mega Cap
  Quarter: Q1
- Annual Revenue (B): 304.25
  Market Cap: Mid Cap
  Quarter: Q1
- Annual Revenue (B): 313.64
  Market Cap: Small Cap
  Quarter: Q2
<end>Please transform the following CSV data into Plain text:
Company,Sector,Market Cap,Annual Revenue (B),Quarter
RetailHub,Finance,Large Cap,393.78,Q4
GlobalTrade,Aerospace,Mid Cap,393.78,Q4
TechCorp,Healthcare,Mid Cap,304.82,Q2
FinanceWorks,Biotech,Mid Cap,191.58,Q3
AutoDrive,Finance,Small Cap,353.04,Q2
<start>
Company: RetailHub | Sector: Finance | Market Cap: Large Cap | Annual Revenue (B): 393.78 | Quarter: Q4
Company: GlobalTrade | Sector: Aerospace | Market Cap: Mid Cap | Annual Revenue (B): 393.78 | Quarter: Q4
Company: TechCorp | Sector: Healthcare | Market Cap: Mid Cap | Annual Revenue (B): 304.82 | Quarter: Q2
Company: FinanceWorks | Sector: Biotech | Market Cap: Mid Cap | Annual Revenue (B): 191.58 | Quarter: Q3
Company: AutoDrive | Sector: Finance | Market Cap: Small Cap | Annual Revenue (B): 353.04 | Quarter: Q2
<end>Can you change this yaml into markdown?
- Author: Luna Silverleaf
  Genre: Science Fiction
  Publication Year: 1986
  Rating: 4.1
  Title: The Forgotten World
- Author: Orion Frostblade
  Genre: Historical
  Publication Year: 1999
  Rating: 3.6
  Title: The Silent Grove
- Author: Kara Firebrand
  Genre: Science Fiction
  Publication Year: 1974
  Rating: 3.9
  Title: Shadows of Solitude
- Author: Kara Firebrand
  Genre: Fantasy
  Publication Year: 2007
  Rating: 2.4
  Title: Echoes of Eternity
- Author: Sylvia Nightshade
  Genre: Historical
  Publication Year: 1962
  Rating: 1.3
  Title: The Last Sky
- Author: Galen Starfire
  Genre: Science Fiction
  Publication Year: 1992
  Rating: 2.4
  Title: The Silent Grove
- Author: Kara Firebrand
  Genre: Romance
  Publication Year: 1977
  Rating: 1.6
  Title: A Journey Through Time
- Author: Elara Moonshadow
  Genre: Science Fiction
  Publication Year: 1977
  Rating: 1.6
  Title: Shadows of Solitude
<start>
| Title | Author | Genre | Publication Year | Rating |
| --- | --- | --- | --- | --- |
| The Forgotten World | Luna Silverleaf | Science Fiction | 1986 | 4.1 |
| The Silent Grove | Orion Frostblade | Historical | 1999 | 3.6 |
| Shadows of Solitude | Kara Firebrand | Science Fiction | 1974 | 3.9 |
| Echoes of Eternity | Kara Firebrand | Fantasy | 2007 | 2.4 |
| The Last Sky | Sylvia Nightshade | Historical | 1962 | 1.3 |
| The Silent Grove | Galen Starfire | Science Fiction | 1992 | 2.4 |
| A Journey Through Time | Kara Firebrand | Romance | 1977 | 1.6 |
| Shadows of Solitude | Elara Moonshadow | Science Fiction | 1977 | 1.6 |
<end>Here's some Json data, can you convert it to Csv?
[
    {
        "Location": "Miami",
        "Condition": "Sunny",
        "Humidity (%)": 89,
        "Day": "Sunday"
    },
    {
        "Location": "Seattle",
        "Condition": "Foggy",
        "Humidity (%)": 79,
        "Day": "Thursday"
    },
    {
        "Location": "New York",
        "Condition": "Windy",
        "Humidity (%)": 45,
        "Day": "Friday"
    },
    {
        "Location": "Houston",
        "Condition": "Windy",
        "Humidity (%)": 56,
        "Day": "Thursday"
    },
    {
        "Location": "Seattle",
        "Condition": "Stormy",
        "Humidity (%)": 67,
        "Day": "Friday"
    }
]<start>
Location,Condition,Humidity (%),Day
Miami,Sunny,89,Sunday
Seattle,Foggy,79,Thursday
New York,Windy,45,Friday
Houston,Windy,56,Thursday
Seattle,Stormy,67,Friday
<end>Here's some YAML data, can you convert it to csv?
- Condition: Snowy
  Day: Saturday
  Humidity (%): 52
  Location: Denver
  Temperature (C): 28.7
  Wind Speed (km/h): 4.2
- Condition: Stormy
  Day: Tuesday
  Humidity (%): 65
  Location: Chicago
  Temperature (C): 28.4
  Wind Speed (km/h): 13.2
- Condition: Sunny
  Day: Sunday
  Humidity (%): 35
  Location: Phoenix
  Temperature (C): 38.2
  Wind Speed (km/h): 2.2
- Condition: Stormy
  Day: Sunday
  Humidity (%): 96
  Location: Phoenix
  Temperature (C): 32.2
  Wind Speed (km/h): 12.6
- Condition: Sunny
  Day: Wednesday
  Humidity (%): 73
  Location: Chicago
  Temperature (C): -8.3
  Wind Speed (km/h): 4.2
<start>
Location,Condition,Temperature (C),Humidity (%),Wind Speed (km/h),Day
Denver,Snowy,28.7,52,4.2,Saturday
Chicago,Stormy,28.4,65,13.2,Tuesday
Phoenix,Sunny,38.2,35,2.2,Sunday
Phoenix,Stormy,32.2,96,12.6,Sunday
Chicago,Sunny,-8.3,73,4.2,Wednesday
<end>Can you change this Json into plain text?
[
    {
        "Location": "Los Angeles",
        "Condition": "Foggy",
        "Temperature (C)": -7.9,
        "Humidity (%)": 39,
        "Wind Speed (km/h)": 21.8,
        "Day": "Wednesday"
    },
    {
        "Location": "Phoenix",
        "Condition": "Windy",
        "Temperature (C)": 33.7,
        "Humidity (%)": 67,
        "Wind Speed (km/h)": 18.3,
        "Day": "Wednesday"
    },
    {
        "Location": "Denver",
        "Condition": "Stormy",
        "Temperature (C)": 4.7,
        "Humidity (%)": 82,
        "Wind Speed (km/h)": 27.4,
        "Day": "Tuesday"
    },
    {
        "Location": "Miami",
        "Condition": "Sunny",
        "Temperature (C)": 26.3,
        "Humidity (%)": 94,
        "Wind Speed (km/h)": 27.2,
        "Day": "Friday"
    },
    {
        "Location": "Houston",
        "Condition": "Foggy",
        "Temperature (C)": 7.3,
        "Humidity (%)": 64,
        "Wind Speed (km/h)": 12.8,
        "Day": "Thursday"
    },
    {
        "Location": "Miami",
        "Condition": "Snowy",
        "Temperature (C)": 35.5,
        "Humidity (%)": 38,
        "Wind Speed (km/h)": 22.0,
        "Day": "Monday"
    }
]<start>
Location: Los Angeles | Condition: Foggy | Temperature (C): -7.9 | Humidity (%): 39 | Wind Speed (km/h): 21.8 | Day: Wednesday
Location: Phoenix | Condition: Windy | Temperature (C): 33.7 | Humidity (%): 67 | Wind Speed (km/h): 18.3 | Day: Wednesday
Location: Denver | Condition: Stormy | Temperature (C): 4.7 | Humidity (%): 82 | Wind Speed (km/h): 27.4 | Day: Tuesday
Location: Miami | Condition: Sunny | Temperature (C): 26.3 | Humidity (%): 94 | Wind Speed (km/h): 27.2 | Day: Friday
Location: Houston | Condition: Foggy | Temperature (C): 7.3 | Humidity (%): 64 | Wind Speed (km/h): 12.8 | Day: Thursday
Location: Miami | Condition: Snowy | Temperature (C): 35.5 | Humidity (%): 38 | Wind Speed (km/h): 22.0 | Day: Monday
<end>Transform this Yml structure to a plain text format:
- Average Latency (ms): 67.83
  Cache Hit Ratio (%): 70.24
  Connection Count: 154
  Database Name: OrdersDB
  Queries per Second: 465.15
  Timestamp: '2022-10-18 23:16:14'
- Average Latency (ms): 33.12
  Cache Hit Ratio (%): 87.9
  Connection Count: 405
  Database Name: ProductsDB
  Queries per Second: 2109.31
  Timestamp: '2021-01-25 08:42:19'
- Average Latency (ms): 54.05
  Cache Hit Ratio (%): 78.12
  Connection Count: 306
  Database Name: AnalyticsDB
  Queries per Second: 4588.07
  Timestamp: '2023-01-16 07:46:27'
- Average Latency (ms): 7.42
  Cache Hit Ratio (%): 74.48
  Connection Count: 46
  Database Name: SalesDB
  Queries per Second: 1228.25
  Timestamp: '2021-05-11 05:19:58'
- Average Latency (ms): 36.99
  Cache Hit Ratio (%): 98.54
  Connection Count: 154
  Database Name: LogsDB
  Queries per Second: 2982.75
  Timestamp: '2023-10-26 01:24:29'
- Average Latency (ms): 31.37
  Cache Hit Ratio (%): 93.69
  Connection Count: 25
  Database Name: ProductsDB
  Queries per Second: 443.72
  Timestamp: '2023-01-17 18:43:22'
- Average Latency (ms): 68.72
  Cache Hit Ratio (%): 99.46
  Connection Count: 298
  Database Name: LogsDB
  Queries per Second: 3007.74
  Timestamp: '2023-07-21 08:24:56'
- Average Latency (ms): 67.75
  Cache Hit Ratio (%): 92.64
  Connection Count: 396
  Database Name: MetricsDB
  Queries per Second: 2966.87
  Timestamp: '2021-08-17 22:50:54'
<start>
Database Name: OrdersDB | Queries per Second: 465.15 | Cache Hit Ratio (%): 70.24 | Connection Count: 154 | Average Latency (ms): 67.83 | Timestamp: 2022-10-18 23:16:14
Database Name: ProductsDB | Queries per Second: 2109.31 | Cache Hit Ratio (%): 87.9 | Connection Count: 405 | Average Latency (ms): 33.12 | Timestamp: 2021-01-25 08:42:19
Database Name: AnalyticsDB | Queries per Second: 4588.07 | Cache Hit Ratio (%): 78.12 | Connection Count: 306 | Average Latency (ms): 54.05 | Timestamp: 2023-01-16 07:46:27
Database Name: SalesDB | Queries per Second: 1228.25 | Cache Hit Ratio (%): 74.48 | Connection Count: 46 | Average Latency (ms): 7.42 | Timestamp: 2021-05-11 05:19:58
Database Name: LogsDB | Queries per Second: 2982.75 | Cache Hit Ratio (%): 98.54 | Connection Count: 154 | Average Latency (ms): 36.99 | Timestamp: 2023-10-26 01:24:29
Database Name: ProductsDB | Queries per Second: 443.72 | Cache Hit Ratio (%): 93.69 | Connection Count: 25 | Average Latency (ms): 31.37 | Timestamp: 2023-01-17 18:43:22
Database Name: LogsDB | Queries per Second: 3007.74 | Cache Hit Ratio (%): 99.46 | Connection Count: 298 | Average Latency (ms): 68.72 | Timestamp: 2023-07-21 08:24:56
Database Name: MetricsDB | Queries per Second: 2966.87 | Cache Hit Ratio (%): 92.64 | Connection Count: 396 | Average Latency (ms): 67.75 | Timestamp: 2021-08-17 22:50:54
<end>Can you change this json into YAML?
[
    {
        "Date": "2014-11-01",
        "Open Price": 1215.24,
        "Close Price": 1162.23,
        "High Price": 1460.38,
        "Low Price": 644.73
    },
    {
        "Date": "2022-12-17",
        "Open Price": 1391.18,
        "Close Price": 26.94,
        "High Price": 1391.18,
        "Low Price": 26.94
    },
    {
        "Date": "2022-10-07",
        "Open Price": 1104.73,
        "Close Price": 1209.81,
        "High Price": 1494.72,
        "Low Price": 1033.12
    },
    {
        "Date": "2012-03-27",
        "Open Price": 343.86,
        "Close Price": 1238.66,
        "High Price": 1238.66,
        "Low Price": 343.86
    },
    {
        "Date": "2017-09-15",
        "Open Price": 36.06,
        "Close Price": 1127.37,
        "High Price": 1127.37,
        "Low Price": 36.06
    }
]<start>
- Close Price: 1162.23
  Date: '2014-11-01'
  High Price: 1460.38
  Low Price: 644.73
  Open Price: 1215.24
- Close Price: 26.94
  Date: '2022-12-17'
  High Price: 1391.18
  Low Price: 26.94
  Open Price: 1391.18
- Close Price: 1209.81
  Date: '2022-10-07'
  High Price: 1494.72
  Low Price: 1033.12
  Open Price: 1104.73
- Close Price: 1238.66
  Date: '2012-03-27'
  High Price: 1238.66
  Low Price: 343.86
  Open Price: 343.86
- Close Price: 1127.37
  Date: '2017-09-15'
  High Price: 1127.37
  Low Price: 36.06
  Open Price: 36.06
<end>Can you change this json into CSV?
[
    {
        "Title": "The Great Expedition",
        "Director": "Lira Silverleaf",
        "Genre": "Sci-Fi",
        "Release Year": 1984
    },
    {
        "Title": "Rise of the Titans",
        "Director": "Selene Darkwhisper",
        "Genre": "Fantasy",
        "Release Year": 1985
    },
    {
        "Title": "Dreamwalker",
        "Director": "Drake Nightshade",
        "Genre": "Sci-Fi",
        "Release Year": 1985
    }
]<start>
Title,Director,Genre,Release Year
The Great Expedition,Lira Silverleaf,Sci-Fi,1984
Rise of the Titans,Selene Darkwhisper,Fantasy,1985
Dreamwalker,Drake Nightshade,Sci-Fi,1985
<end>Here's some Json data, can you convert it to MARKDOWN?
[
    {
        "Name": "Carlos",
        "Age": 26,
        "Birth Month": "January",
        "City": "Boston",
        "Income": 350000
    },
    {
        "Name": "Candace",
        "Age": 24,
        "Birth Month": "May",
        "City": "Seattle",
        "Income": 345000
    },
    {
        "Name": "Destiny",
        "Age": 69,
        "Birth Month": "September",
        "City": "Austin",
        "Income": 465000
    },
    {
        "Name": "Marshall",
        "Age": 67,
        "Birth Month": "December",
        "City": "Milwaukee",
        "Income": 485000
    },
    {
        "Name": "Ann",
        "Age": 24,
        "Birth Month": "May",
        "City": "Milwaukee",
        "Income": 210000
    },
    {
        "Name": "Nick",
        "Age": 57,
        "Birth Month": "June",
        "City": "Milwaukee",
        "Income": 180000
    },
    {
        "Name": "Gayle",
        "Age": 30,
        "Birth Month": "November",
        "City": "New York",
        "Income": 320000
    },
    {
        "Name": "Genesis",
        "Age": 30,
        "Birth Month": "September",
        "City": "Washington",
        "Income": 455000
    }
]<start>
| Name | Age | Birth Month | City | Income |
| --- | --- | --- | --- | --- |
| Carlos | 26 | January | Boston | 350000 |
| Candace | 24 | May | Seattle | 345000 |
| Destiny | 69 | September | Austin | 465000 |
| Marshall | 67 | December | Milwaukee | 485000 |
| Ann | 24 | May | Milwaukee | 210000 |
| Nick | 57 | June | Milwaukee | 180000 |
| Gayle | 30 | November | New York | 320000 |
| Genesis | 30 | September | Washington | 455000 |
<end>Here's some MARKDOWN data, can you convert it to Csv?
| Company | Sector | Stock Price | Annual Revenue (B) |
| --- | --- | --- | --- |
| BioPharm | Energy | 675.3 | 461.43 |
| HealthPlus | Healthcare | 423.82 | 137.29 |
| GlobalTrade | Aerospace | 79.46 | 94.49 |
| GlobalTrade | Biotech | 365.34 | 79.8 |
| AutoDrive | Aerospace | 623.58 | 189.11 |
| AeroSpace | Aerospace | 859.38 | 137.29 |
| BioPharm | Biotech | 622.27 | 358.23 |
| GlobalTrade | Technology | 902.48 | 272.88 |
| AeroSpace | Finance | 445.42 | 122.63 |<start>
Company,Sector,Stock Price,Annual Revenue (B)
BioPharm,Energy,675.3,461.43
HealthPlus,Healthcare,423.82,137.29
GlobalTrade,Aerospace,79.46,94.49
GlobalTrade,Biotech,365.34,79.8
AutoDrive,Aerospace,623.58,189.11
AeroSpace,Aerospace,859.38,137.29
BioPharm,Biotech,622.27,358.23
GlobalTrade,Technology,902.48,272.88
AeroSpace,Finance,445.42,122.63
<end>Can you change this plain text into json?
Company: BioPharm | Sector: Finance | Stock Price: 652.5 | Annual Revenue (B): 133.75 | Quarter: Q3
Company: RetailHub | Sector: Technology | Stock Price: 787.08 | Annual Revenue (B): 199.28 | Quarter: Q2
Company: EcoEnergy | Sector: Aerospace | Stock Price: 599.39 | Annual Revenue (B): 263.89 | Quarter: Q1
Company: TechCorp | Sector: Technology | Stock Price: 795.42 | Annual Revenue (B): 382.54 | Quarter: Q2
Company: Foodies | Sector: Automotive | Stock Price: 937.93 | Annual Revenue (B): 172.31 | Quarter: Q3
<start>
[
    {
        "Company": "BioPharm",
        "Sector": "Finance",
        "Stock Price": 652.5,
        "Annual Revenue (B)": 133.75,
        "Quarter": "Q3"
    },
    {
        "Company": "RetailHub",
        "Sector": "Technology",
        "Stock Price": 787.08,
        "Annual Revenue (B)": 199.28,
        "Quarter": "Q2"
    },
    {
        "Company": "EcoEnergy",
        "Sector": "Aerospace",
        "Stock Price": 599.39,
        "Annual Revenue (B)": 263.89,
        "Quarter": "Q1"
    },
    {
        "Company": "TechCorp",
        "Sector": "Technology",
        "Stock Price": 795.42,
        "Annual Revenue (B)": 382.54,
        "Quarter": "Q2"
    },
    {
        "Company": "Foodies",
        "Sector": "Automotive",
        "Stock Price": 937.93,
        "Annual Revenue (B)": 172.31,
        "Quarter": "Q3"
    }
]
<end>Convert this PLAIN TEXT to markdown:
Director: Cade Firebrand | Genre: Fantasy | Box Office Earnings (M): 54.45
Director: Aria Ravenwood | Genre: Horror | Box Office Earnings (M): 754.22
Director: Rylan Frostblade | Genre: Drama | Box Office Earnings (M): 565.39
Director: Lira Silverleaf | Genre: Drama | Box Office Earnings (M): 537.64
Director: Zara Stormrider | Genre: Sci-Fi | Box Office Earnings (M): 959.02
Director: Rylan Frostblade | Genre: Comedy | Box Office Earnings (M): 999.64
Director: Lira Silverleaf | Genre: Adventure | Box Office Earnings (M): 384.74
Director: Aria Ravenwood | Genre: Action | Box Office Earnings (M): 182.02
<start>
| Director | Genre | Box Office Earnings (M) |
| --- | --- | --- |
| Cade Firebrand | Fantasy | 54.45 |
| Aria Ravenwood | Horror | 754.22 |
| Rylan Frostblade | Drama | 565.39 |
| Lira Silverleaf | Drama | 537.64 |
| Zara Stormrider | Sci-Fi | 959.02 |
| Rylan Frostblade | Comedy | 999.64 |
| Lira Silverleaf | Adventure | 384.74 |
| Aria Ravenwood | Action | 182.02 |
<end>Please transform the following PLAIN TEXT data into markdown:
Company: AeroSpace | Sector: Automotive | Market Cap: Large Cap | Stock Price: 31.51 | Annual Revenue (B): 59.58 | Quarter: Q2
Company: TechCorp | Sector: Automotive | Market Cap: Mid Cap | Stock Price: 585.34 | Annual Revenue (B): 289.41 | Quarter: Q4
Company: AutoDrive | Sector: Aerospace | Market Cap: Small Cap | Stock Price: 432.51 | Annual Revenue (B): 302.29 | Quarter: Q2
Company: AeroSpace | Sector: Aerospace | Market Cap: Mid Cap | Stock Price: 881.98 | Annual Revenue (B): 81.73 | Quarter: Q2
Company: Foodies | Sector: Healthcare | Market Cap: Small Cap | Stock Price: 863.51 | Annual Revenue (B): 442.54 | Quarter: Q1
Company: BioPharm | Sector: Healthcare | Market Cap: Large Cap | Stock Price: 984.89 | Annual Revenue (B): 313.83 | Quarter: Q1
Company: GlobalTrade | Sector: Energy | Market Cap: Large Cap | Stock Price: 580.71 | Annual Revenue (B): 178.77 | Quarter: Q4
Company: RetailHub | Sector: Aerospace | Market Cap: Large Cap | Stock Price: 291.5 | Annual Revenue (B): 466.36 | Quarter: Q1
Company: FinanceWorks | Sector: Automotive | Market Cap: Large Cap | Stock Price: 50.34 | Annual Revenue (B): 330.96 | Quarter: Q3
Company: AeroSpace | Sector: Technology | Market Cap: Mega Cap | Stock Price: 250.0 | Annual Revenue (B): 389.56 | Quarter: Q2
<start>
| Company | Sector | Market Cap | Stock Price | Annual Revenue (B) | Quarter |
| --- | --- | --- | --- | --- | --- |
| AeroSpace | Automotive | Large Cap | 31.51 | 59.58 | Q2 |
| TechCorp | Automotive | Mid Cap | 585.34 | 289.41 | Q4 |
| AutoDrive | Aerospace | Small Cap | 432.51 | 302.29 | Q2 |
| AeroSpace | Aerospace | Mid Cap | 881.98 | 81.73 | Q2 |
| Foodies | Healthcare | Small Cap | 863.51 | 442.54 | Q1 |
| BioPharm | Healthcare | Large Cap | 984.89 | 313.83 | Q1 |
| GlobalTrade | Energy | Large Cap | 580.71 | 178.77 | Q4 |
| RetailHub | Aerospace | Large Cap | 291.5 | 466.36 | Q1 |
| FinanceWorks | Automotive | Large Cap | 50.34 | 330.96 | Q3 |
| AeroSpace | Technology | Mega Cap | 250.0 | 389.56 | Q2 |
<end>Here's some json data, can you convert it to yaml?
[
    {
        "Device ID": "device-0058",
        "Device Type": "Temperature Sensor",
        "Location": "Garden",
        "Battery Level (%)": 41.3,
        "Reading Value": 79.74,
        "Timestamp": "2022-12-14 22:54:39"
    },
    {
        "Device ID": "device-0098",
        "Device Type": "Motion Detector",
        "Location": "Living Room",
        "Battery Level (%)": 37.0,
        "Reading Value": -12.93,
        "Timestamp": "2023-10-26 11:36:11"
    },
    {
        "Device ID": "device-0090",
        "Device Type": "Motion Detector",
        "Location": "Bedroom",
        "Battery Level (%)": 83.9,
        "Reading Value": -21.74,
        "Timestamp": "2023-09-05 08:36:45"
    },
    {
        "Device ID": "device-0008",
        "Device Type": "Light Sensor",
        "Location": "Bathroom",
        "Battery Level (%)": 47.4,
        "Reading Value": 73.51,
        "Timestamp": "2023-05-22 10:56:59"
    },
    {
        "Device ID": "device-0036",
        "Device Type": "Motion Detector",
        "Location": "Bedroom",
        "Battery Level (%)": 42.1,
        "Reading Value": 27.09,
        "Timestamp": "2021-06-12 23:25:41"
    },
    {
        "Device ID": "device-0037",
        "Device Type": "Light Sensor",
        "Location": "Garage",
        "Battery Level (%)": 15.2,
        "Reading Value": 45.13,
        "Timestamp": "2022-09-26 16:34:55"
    }
]<start>
- Battery Level (%): 41.3
  Device ID: device-0058
  Device Type: Temperature Sensor
  Location: Garden
  Reading Value: 79.74
  Timestamp: '2022-12-14 22:54:39'
- Battery Level (%): 37.0
  Device ID: device-0098
  Device Type: Motion Detector
  Location: Living Room
  Reading Value: -12.93
  Timestamp: '2023-10-26 11:36:11'
- Battery Level (%): 83.9
  Device ID: device-0090
  Device Type: Motion Detector
  Location: Bedroom
  Reading Value: -21.74
  Timestamp: '2023-09-05 08:36:45'
- Battery Level (%): 47.4
  Device ID: device-0008
  Device Type: Light Sensor
  Location: Bathroom
  Reading Value: 73.51
  Timestamp: '2023-05-22 10:56:59'
- Battery Level (%): 42.1
  Device ID: device-0036
  Device Type: Motion Detector
  Location: Bedroom
  Reading Value: 27.09
  Timestamp: '2021-06-12 23:25:41'
- Battery Level (%): 15.2
  Device ID: device-0037
  Device Type: Light Sensor
  Location: Garage
  Reading Value: 45.13
  Timestamp: '2022-09-26 16:34:55'
<end>Can you change this json into csv?
[
    {
        "Name": "Elena",
        "Age": 45,
        "Birth Month": "July",
        "City": "New York",
        "Income": 125000
    },
    {
        "Name": "Holly",
        "Age": 60,
        "Birth Month": "April",
        "City": "Portland",
        "Income": 85000
    },
    {
        "Name": "Janice",
        "Age": 60,
        "Birth Month": "March",
        "City": "Milwaukee",
        "Income": 485000
    },
    {
        "Name": "Josiah",
        "Age": 35,
        "Birth Month": "December",
        "City": "Charlotte",
        "Income": 315000
    },
    {
        "Name": "Heather",
        "Age": 33,
        "Birth Month": "March",
        "City": "Baltimore",
        "Income": 295000
    },
    {
        "Name": "Melissa",
        "Age": 61,
        "Birth Month": "June",
        "City": "Fort Worth",
        "Income": 160000
    },
    {
        "Name": "Erin",
        "Age": 59,
        "Birth Month": "December",
        "City": "San Diego",
        "Income": 435000
    },
    {
        "Name": "Samuel",
        "Age": 68,
        "Birth Month": "January",
        "City": "Portland",
        "Income": 195000
    }
]<start>
Name,Age,Birth Month,City,Income
Elena,45,July,New York,125000
Holly,60,April,Portland,85000
Janice,60,March,Milwaukee,485000
Josiah,35,December,Charlotte,315000
Heather,33,March,Baltimore,295000
Melissa,61,June,Fort Worth,160000
Erin,59,December,San Diego,435000
Samuel,68,January,Portland,195000
<end>Transform this Csv structure to a yml format:
Title,Director,Genre
Starbound Odyssey,Drake Nightshade,Comedy
The Final Voyage,Zara Stormrider,Sci-Fi
The Endless Horizon,Rylan Frostblade,Fantasy
Starbound Odyssey,Aria Ravenwood,Action
The Final Voyage,Aria Ravenwood,Thriller
Mystery of the Depths,Rylan Frostblade,Horror
Beyond the Veil,Orin Shadowalker,Fantasy
Dreamwalker,Lira Silverleaf,Adventure
<start>
- Director: Drake Nightshade
  Genre: Comedy
  Title: Starbound Odyssey
- Director: Zara Stormrider
  Genre: Sci-Fi
  Title: The Final Voyage
- Director: Rylan Frostblade
  Genre: Fantasy
  Title: The Endless Horizon
- Director: Aria Ravenwood
  Genre: Action
  Title: Starbound Odyssey
- Director: Aria Ravenwood
  Genre: Thriller
  Title: The Final Voyage
- Director: Rylan Frostblade
  Genre: Horror
  Title: Mystery of the Depths
- Director: Orin Shadowalker
  Genre: Fantasy
  Title: Beyond the Veil
- Director: Lira Silverleaf
  Genre: Adventure
  Title: Dreamwalker
<end>Here's some markdown data, can you convert it to yaml?
| Title | Director | Genre | Release Year | Box Office Earnings (M) |
| --- | --- | --- | --- | --- |
| The Endless Horizon | Selene Darkwhisper | Horror | 2014 | 646.06 |
| Edge of Infinity | Aria Ravenwood | Fantasy | 1970 | 895.67 |
| The Final Voyage | Drake Nightshade | Sci-Fi | 1994 | 929.28 |
| The Endless Horizon | Zara Stormrider | Sci-Fi | 2002 | 405.2 |<start>
- Box Office Earnings (M): 646.06
  Director: Selene Darkwhisper
  Genre: Horror
  Release Year: 2014
  Title: The Endless Horizon
- Box Office Earnings (M): 895.67
  Director: Aria Ravenwood
  Genre: Fantasy
  Release Year: 1970
  Title: Edge of Infinity
- Box Office Earnings (M): 929.28
  Director: Drake Nightshade
  Genre: Sci-Fi
  Release Year: 1994
  Title: The Final Voyage
- Box Office Earnings (M): 405.2
  Director: Zara Stormrider
  Genre: Sci-Fi
  Release Year: 2002
  Title: The Endless Horizon
<end>Convert this csv to markdown:
Name,Age,Birth Month,City,Income
Roscoe,66,June,Boston,265000
Clarence,45,December,Washington,275000
Damian,65,September,Houston,125000
Fredrick,18,March,Indianapolis,50000
Karla,50,November,Oklahoma City,310000
Kendra,40,September,Milwaukee,100000
Cheryl,65,June,Austin,270000
Lila,56,December,El Paso,265000
Theresa,25,May,Memphis,135000
<start>
| Name | Age | Birth Month | City | Income |
| --- | --- | --- | --- | --- |
| Roscoe | 66 | June | Boston | 265000 |
| Clarence | 45 | December | Washington | 275000 |
| Damian | 65 | September | Houston | 125000 |
| Fredrick | 18 | March | Indianapolis | 50000 |
| Karla | 50 | November | Oklahoma City | 310000 |
| Kendra | 40 | September | Milwaukee | 100000 |
| Cheryl | 65 | June | Austin | 270000 |
| Lila | 56 | December | El Paso | 265000 |
| Theresa | 25 | May | Memphis | 135000 |
<end>