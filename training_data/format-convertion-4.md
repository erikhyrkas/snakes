Please transform the following markdown data into json:
| Battery Level (%) | Reading Value | Timestamp |
| --- | --- | --- |
| 85.2 | 32.76 | 2022-09-13 07:42:38 |
| 20.4 | -14.11 | 2023-01-18 18:54:10 |
| 19.5 | 67.31 | 2021-12-23 15:15:13 |
| 14.5 | -35.85 | 2023-07-26 22:12:18 |
| 44.7 | 40.18 | 2022-11-22 10:17:08 |<start>
[
    {
        "Battery Level (%)": 85.2,
        "Reading Value": 32.76,
        "Timestamp": "2022-09-13 07:42:38"
    },
    {
        "Battery Level (%)": 20.4,
        "Reading Value": -14.11,
        "Timestamp": "2023-01-18 18:54:10"
    },
    {
        "Battery Level (%)": 19.5,
        "Reading Value": 67.31,
        "Timestamp": "2021-12-23 15:15:13"
    },
    {
        "Battery Level (%)": 14.5,
        "Reading Value": -35.85,
        "Timestamp": "2023-07-26 22:12:18"
    },
    {
        "Battery Level (%)": 44.7,
        "Reading Value": 40.18,
        "Timestamp": "2022-11-22 10:17:08"
    }
]
<end>Please transform the following yaml data into plain text:
- Price Range: $$$$$
  Restaurant Name: Vegan Delight
- Price Range: $$$
  Restaurant Name: The Golden Spoon
- Price Range: $$$
  Restaurant Name: Curry Corner
<start>
Restaurant Name: Vegan Delight | Price Range: $$$$$
Restaurant Name: The Golden Spoon | Price Range: $$$
Restaurant Name: Curry Corner | Price Range: $$$
<end>Here's some JSON data, can you convert it to MARKDOWN?
[
    {
        "Company": "FinanceTrust",
        "Date": "2019-08-14",
        "Open Price": 981.78,
        "Close Price": 760.59,
        "Low Price": 353.52
    },
    {
        "Company": "TechnoCorp",
        "Date": "2014-12-17",
        "Open Price": 1116.06,
        "Close Price": 1493.8,
        "Low Price": 661.92
    },
    {
        "Company": "GreenEnergy",
        "Date": "2022-01-04",
        "Open Price": 634.14,
        "Close Price": 905.84,
        "Low Price": 634.14
    },
    {
        "Company": "AeroSystems",
        "Date": "2021-02-04",
        "Open Price": 161.1,
        "Close Price": 1028.25,
        "Low Price": 161.1
    },
    {
        "Company": "TechnoCorp",
        "Date": "2014-03-18",
        "Open Price": 263.51,
        "Close Price": 613.02,
        "Low Price": 263.51
    },
    {
        "Company": "AeroSystems",
        "Date": "2023-02-03",
        "Open Price": 855.08,
        "Close Price": 1118.3,
        "Low Price": 855.08
    }
]<start>
| Company | Date | Open Price | Close Price | Low Price |
| --- | --- | --- | --- | --- |
| FinanceTrust | 2019-08-14 | 981.78 | 760.59 | 353.52 |
| TechnoCorp | 2014-12-17 | 1116.06 | 1493.8 | 661.92 |
| GreenEnergy | 2022-01-04 | 634.14 | 905.84 | 634.14 |
| AeroSystems | 2021-02-04 | 161.1 | 1028.25 | 161.1 |
| TechnoCorp | 2014-03-18 | 263.51 | 613.02 | 263.51 |
| AeroSystems | 2023-02-03 | 855.08 | 1118.3 | 855.08 |
<end>Please transform the following csv data into yaml:
Name,Age,Birth Month,City,Income
Crystal,45,October,Boston,210000
Merle,47,July,Columbus,195000
Jennie,38,October,Oklahoma City,60000
Brendan,28,December,Austin,475000
Alexis,68,January,San Jose,250000
Harper,57,April,Houston,220000
Dorothy,49,March,Boston,215000
Rosalie,43,September,Denver,215000
Dale,36,December,Louisville,330000
Bryce,53,August,Denver,235000
<start>
- Age: 45
  Birth Month: October
  City: Boston
  Income: 210000
  Name: Crystal
- Age: 47
  Birth Month: July
  City: Columbus
  Income: 195000
  Name: Merle
- Age: 38
  Birth Month: October
  City: Oklahoma City
  Income: 60000
  Name: Jennie
- Age: 28
  Birth Month: December
  City: Austin
  Income: 475000
  Name: Brendan
- Age: 68
  Birth Month: January
  City: San Jose
  Income: 250000
  Name: Alexis
- Age: 57
  Birth Month: April
  City: Houston
  Income: 220000
  Name: Harper
- Age: 49
  Birth Month: March
  City: Boston
  Income: 215000
  Name: Dorothy
- Age: 43
  Birth Month: September
  City: Denver
  Income: 215000
  Name: Rosalie
- Age: 36
  Birth Month: December
  City: Louisville
  Income: 330000
  Name: Dale
- Age: 53
  Birth Month: August
  City: Denver
  Income: 235000
  Name: Bryce
<end>Convert this json to plain text:
[
    {
        "Title": "Legends of the Rift",
        "Author": "Kara Firebrand",
        "Rating": 3.8
    },
    {
        "Title": "Echoes of Eternity",
        "Author": "Luna Silverleaf",
        "Rating": 4.8
    },
    {
        "Title": "Legends of the Rift",
        "Author": "Luna Silverleaf",
        "Rating": 3.1
    }
]<start>
Title: Legends of the Rift | Author: Kara Firebrand | Rating: 3.8
Title: Echoes of Eternity | Author: Luna Silverleaf | Rating: 4.8
Title: Legends of the Rift | Author: Luna Silverleaf | Rating: 3.1
<end>Here's some csv data, can you convert it to YAML?
Database Name,Queries per Second,Cache Hit Ratio (%),Timestamp
ProfilesDB,3683.81,74.15,2022-10-24 12:39:31
AnalyticsDB,2576.17,87.44,2021-04-12 14:03:33
InventoryDB,2576.17,88.88,2023-03-11 11:03:35
ProductsDB,1388.39,90.6,2022-02-19 21:12:23
OrdersDB,4022.56,98.43,2021-08-20 02:55:51
UserDB,2957.47,83.79,2023-04-25 19:03:06
LogsDB,351.82,93.43,2021-09-27 06:07:51
AnalyticsDB,1990.26,98.74,2022-11-14 04:22:37
SalesDB,209.93,80.67,2023-04-26 12:40:55
<start>
- Cache Hit Ratio (%): 74.15
  Database Name: ProfilesDB
  Queries per Second: 3683.81
  Timestamp: '2022-10-24 12:39:31'
- Cache Hit Ratio (%): 87.44
  Database Name: AnalyticsDB
  Queries per Second: 2576.17
  Timestamp: '2021-04-12 14:03:33'
- Cache Hit Ratio (%): 88.88
  Database Name: InventoryDB
  Queries per Second: 2576.17
  Timestamp: '2023-03-11 11:03:35'
- Cache Hit Ratio (%): 90.6
  Database Name: ProductsDB
  Queries per Second: 1388.39
  Timestamp: '2022-02-19 21:12:23'
- Cache Hit Ratio (%): 98.43
  Database Name: OrdersDB
  Queries per Second: 4022.56
  Timestamp: '2021-08-20 02:55:51'
- Cache Hit Ratio (%): 83.79
  Database Name: UserDB
  Queries per Second: 2957.47
  Timestamp: '2023-04-25 19:03:06'
- Cache Hit Ratio (%): 93.43
  Database Name: LogsDB
  Queries per Second: 351.82
  Timestamp: '2021-09-27 06:07:51'
- Cache Hit Ratio (%): 98.74
  Database Name: AnalyticsDB
  Queries per Second: 1990.26
  Timestamp: '2022-11-14 04:22:37'
- Cache Hit Ratio (%): 80.67
  Database Name: SalesDB
  Queries per Second: 209.93
  Timestamp: '2023-04-26 12:40:55'
<end>Here's some markdown data, can you convert it to csv?
| Company | High Price | Low Price | Volume |
| --- | --- | --- | --- |
| HealthGen | 1223.49 | 455.42 | 5629666 |
| FoodChain | 1165.07 | 149.96 | 1702195 |
| RetailWorld | 482.96 | 35.48 | 336211 |
| TechnoCorp | 1376.57 | 849.32 | 5865647 |
| RetailWorld | 1373.46 | 422.14 | 5341009 |
| GreenEnergy | 923.66 | 35.48 | 9550898 |<start>
Company,High Price,Low Price,Volume
HealthGen,1223.49,455.42,5629666
FoodChain,1165.07,149.96,1702195
RetailWorld,482.96,35.48,336211
TechnoCorp,1376.57,849.32,5865647
RetailWorld,1373.46,422.14,5341009
GreenEnergy,923.66,35.48,9550898
<end>Transform this PLAIN TEXT structure to a markdown format:
Database Name: SalesDB | Queries per Second: 2317.58 | Connection Count: 357 | Timestamp: 2021-05-14 05:48:21
Database Name: MetricsDB | Queries per Second: 2591.78 | Connection Count: 386 | Timestamp: 2021-07-26 21:28:29
Database Name: ProductsDB | Queries per Second: 1789.92 | Connection Count: 363 | Timestamp: 2022-06-24 19:54:17
Database Name: AnalyticsDB | Queries per Second: 4685.93 | Connection Count: 186 | Timestamp: 2023-07-20 16:03:53
Database Name: ProductsDB | Queries per Second: 1284.32 | Connection Count: 362 | Timestamp: 2023-01-07 19:22:29
<start>
| Database Name | Queries per Second | Connection Count | Timestamp |
| --- | --- | --- | --- |
| SalesDB | 2317.58 | 357 | 2021-05-14 05:48:21 |
| MetricsDB | 2591.78 | 386 | 2021-07-26 21:28:29 |
| ProductsDB | 1789.92 | 363 | 2022-06-24 19:54:17 |
| AnalyticsDB | 4685.93 | 186 | 2023-07-20 16:03:53 |
| ProductsDB | 1284.32 | 362 | 2023-01-07 19:22:29 |
<end>Please transform the following markdown data into Yaml:
| Device ID | Device Type | Location | Battery Level (%) | Reading Value | Timestamp |
| --- | --- | --- | --- | --- | --- |
| device-0064 | Motion Detector | Bathroom | 44.7 | 38.24 | 2023-03-23 19:56:27 |
| device-0062 | Pressure Sensor | Bedroom | 67.8 | 21.48 | 2022-10-11 03:12:14 |
| device-0026 | Light Sensor | Kitchen | 53.3 | 84.45 | 2021-06-01 15:23:30 |
| device-0077 | Light Sensor | Bathroom | 47.6 | 29.3 | 2021-02-01 18:48:19 |
| device-0087 | Light Sensor | Bathroom | 70.0 | 25.83 | 2023-08-04 22:43:56 |
| device-0005 | Temperature Sensor | Bathroom | 56.6 | 74.29 | 2022-08-26 09:10:29 |
| device-0074 | Pressure Sensor | Kitchen | 10.7 | 3.31 | 2023-11-12 09:14:24 |<start>
- Battery Level (%): 44.7
  Device ID: device-0064
  Device Type: Motion Detector
  Location: Bathroom
  Reading Value: 38.24
  Timestamp: '2023-03-23 19:56:27'
- Battery Level (%): 67.8
  Device ID: device-0062
  Device Type: Pressure Sensor
  Location: Bedroom
  Reading Value: 21.48
  Timestamp: '2022-10-11 03:12:14'
- Battery Level (%): 53.3
  Device ID: device-0026
  Device Type: Light Sensor
  Location: Kitchen
  Reading Value: 84.45
  Timestamp: '2021-06-01 15:23:30'
- Battery Level (%): 47.6
  Device ID: device-0077
  Device Type: Light Sensor
  Location: Bathroom
  Reading Value: 29.3
  Timestamp: '2021-02-01 18:48:19'
- Battery Level (%): 70.0
  Device ID: device-0087
  Device Type: Light Sensor
  Location: Bathroom
  Reading Value: 25.83
  Timestamp: '2023-08-04 22:43:56'
- Battery Level (%): 56.6
  Device ID: device-0005
  Device Type: Temperature Sensor
  Location: Bathroom
  Reading Value: 74.29
  Timestamp: '2022-08-26 09:10:29'
- Battery Level (%): 10.7
  Device ID: device-0074
  Device Type: Pressure Sensor
  Location: Kitchen
  Reading Value: 3.31
  Timestamp: '2023-11-12 09:14:24'
<end>Transform this JSON structure to a Csv format:
[
    {
        "Database Name": "MetricsDB",
        "Queries per Second": 3637.95,
        "Average Latency (ms)": 37.12,
        "Timestamp": "2023-12-10 02:24:17"
    },
    {
        "Database Name": "LogsDB",
        "Queries per Second": 783.42,
        "Average Latency (ms)": 16.08,
        "Timestamp": "2023-03-13 18:16:14"
    },
    {
        "Database Name": "LogsDB",
        "Queries per Second": 2196.57,
        "Average Latency (ms)": 41.68,
        "Timestamp": "2023-04-11 20:53:42"
    },
    {
        "Database Name": "LogsDB",
        "Queries per Second": 4263.88,
        "Average Latency (ms)": 94.4,
        "Timestamp": "2021-09-25 05:29:22"
    },
    {
        "Database Name": "ProductsDB",
        "Queries per Second": 3261.93,
        "Average Latency (ms)": 48.5,
        "Timestamp": "2022-05-12 12:33:48"
    }
]<start>
Database Name,Queries per Second,Average Latency (ms),Timestamp
MetricsDB,3637.95,37.12,2023-12-10 02:24:17
LogsDB,783.42,16.08,2023-03-13 18:16:14
LogsDB,2196.57,41.68,2023-04-11 20:53:42
LogsDB,4263.88,94.4,2021-09-25 05:29:22
ProductsDB,3261.93,48.5,2022-05-12 12:33:48
<end>Transform this Csv structure to a Plain text format:
Title,Genre,Release Year
Starbound Odyssey,Fantasy,1996
Starbound Odyssey,Action,2011
Mystery of the Depths,Horror,2003
Dreamwalker,Action,1992
Mystery of the Depths,Thriller,1978
Escape from Earth,Horror,1979
<start>
Title: Starbound Odyssey | Genre: Fantasy | Release Year: 1996
Title: Starbound Odyssey | Genre: Action | Release Year: 2011
Title: Mystery of the Depths | Genre: Horror | Release Year: 2003
Title: Dreamwalker | Genre: Action | Release Year: 1992
Title: Mystery of the Depths | Genre: Thriller | Release Year: 1978
Title: Escape from Earth | Genre: Horror | Release Year: 1979
<end>Convert this Markdown to CSV:
| Name | Age | Birth Month | City |
| --- | --- | --- | --- |
| Lucile | 35 | July | Fort Worth |
| Tina | 66 | January | Las Vegas |
| Alondra | 19 | February | Washington |
| Caroline | 40 | March | Seattle |<start>
Name,Age,Birth Month,City
Lucile,35,July,Fort Worth
Tina,66,January,Las Vegas
Alondra,19,February,Washington
Caroline,40,March,Seattle
<end>Convert this JSON to Csv:
[
    {
        "Location": "Phoenix",
        "Condition": "Stormy",
        "Temperature (C)": 16.3,
        "Humidity (%)": 77,
        "Wind Speed (km/h)": 21.3
    },
    {
        "Location": "Houston",
        "Condition": "Stormy",
        "Temperature (C)": 39.1,
        "Humidity (%)": 33,
        "Wind Speed (km/h)": 10.6
    },
    {
        "Location": "Denver",
        "Condition": "Sunny",
        "Temperature (C)": 38.1,
        "Humidity (%)": 45,
        "Wind Speed (km/h)": 27.8
    },
    {
        "Location": "Miami",
        "Condition": "Cloudy",
        "Temperature (C)": 23.6,
        "Humidity (%)": 60,
        "Wind Speed (km/h)": 27.0
    },
    {
        "Location": "Los Angeles",
        "Condition": "Cloudy",
        "Temperature (C)": 18.4,
        "Humidity (%)": 50,
        "Wind Speed (km/h)": 10.6
    }
]<start>
Location,Condition,Temperature (C),Humidity (%),Wind Speed (km/h)
Phoenix,Stormy,16.3,77,21.3
Houston,Stormy,39.1,33,10.6
Denver,Sunny,38.1,45,27.8
Miami,Cloudy,23.6,60,27.0
Los Angeles,Cloudy,18.4,50,10.6
<end>Please transform the following Csv data into YAML:
Genre,Release Year,Box Office Earnings (M)
Fantasy,1985,401.77
Horror,2016,178.03
Fantasy,1984,448.26
Action,2016,401.34
<start>
- Box Office Earnings (M): 401.77
  Genre: Fantasy
  Release Year: 1985
- Box Office Earnings (M): 178.03
  Genre: Horror
  Release Year: 2016
- Box Office Earnings (M): 448.26
  Genre: Fantasy
  Release Year: 1984
- Box Office Earnings (M): 401.34
  Genre: Action
  Release Year: 2016
<end>Convert this CSV to plain text:
Age,Birth Month,Income
18,April,20000
60,November,60000
55,August,195000
35,April,150000
34,July,240000
47,April,135000
28,November,105000
20,August,275000
40,July,495000
<start>
Age: 18 | Birth Month: April | Income: 20000
Age: 60 | Birth Month: November | Income: 60000
Age: 55 | Birth Month: August | Income: 195000
Age: 35 | Birth Month: April | Income: 150000
Age: 34 | Birth Month: July | Income: 240000
Age: 47 | Birth Month: April | Income: 135000
Age: 28 | Birth Month: November | Income: 105000
Age: 20 | Birth Month: August | Income: 275000
Age: 40 | Birth Month: July | Income: 495000
<end>Here's some Markdown data, can you convert it to csv?
| Title | Director | Release Year | Box Office Earnings (M) |
| --- | --- | --- | --- |
| Escape from Earth | Aria Ravenwood | 1988 | 231.92 |
| Edge of Infinity | Talon Blackthorn | 2020 | 633.81 |
| The Final Voyage | Aria Ravenwood | 2011 | 328.77 |
| Beyond the Veil | Cade Firebrand | 1987 | 837.33 |<start>
Title,Director,Release Year,Box Office Earnings (M)
Escape from Earth,Aria Ravenwood,1988,231.92
Edge of Infinity,Talon Blackthorn,2020,633.81
The Final Voyage,Aria Ravenwood,2011,328.77
Beyond the Veil,Cade Firebrand,1987,837.33
<end>Please transform the following csv data into json:
Location,Condition,Temperature (C),Wind Speed (km/h)
New York,Windy,-9.0,2.1
Miami,Foggy,28.5,18.7
Phoenix,Cloudy,14.5,0.2
Miami,Snowy,-4.6,16.8
Miami,Sunny,-1.1,5.8
Seattle,Sunny,21.7,2.4
New York,Snowy,33.6,4.1
Los Angeles,Sunny,38.2,3.6
Chicago,Foggy,17.1,21.9
<start>
[
    {
        "Location": "New York",
        "Condition": "Windy",
        "Temperature (C)": -9.0,
        "Wind Speed (km/h)": 2.1
    },
    {
        "Location": "Miami",
        "Condition": "Foggy",
        "Temperature (C)": 28.5,
        "Wind Speed (km/h)": 18.7
    },
    {
        "Location": "Phoenix",
        "Condition": "Cloudy",
        "Temperature (C)": 14.5,
        "Wind Speed (km/h)": 0.2
    },
    {
        "Location": "Miami",
        "Condition": "Snowy",
        "Temperature (C)": -4.6,
        "Wind Speed (km/h)": 16.8
    },
    {
        "Location": "Miami",
        "Condition": "Sunny",
        "Temperature (C)": -1.1,
        "Wind Speed (km/h)": 5.8
    },
    {
        "Location": "Seattle",
        "Condition": "Sunny",
        "Temperature (C)": 21.7,
        "Wind Speed (km/h)": 2.4
    },
    {
        "Location": "New York",
        "Condition": "Snowy",
        "Temperature (C)": 33.6,
        "Wind Speed (km/h)": 4.1
    },
    {
        "Location": "Los Angeles",
        "Condition": "Sunny",
        "Temperature (C)": 38.2,
        "Wind Speed (km/h)": 3.6
    },
    {
        "Location": "Chicago",
        "Condition": "Foggy",
        "Temperature (C)": 17.1,
        "Wind Speed (km/h)": 21.9
    }
]
<end>Please transform the following Csv data into PLAIN TEXT:
Name,Age,Birth Month,City,Income
Alaina,49,September,Seattle,475000
Brandon,22,January,Portland,325000
Reginald,58,July,Louisville,155000
Carmen,23,March,Phoenix,45000
Margaret,35,December,Charlotte,275000
Rosemarie,29,July,Portland,325000
Virgie,30,January,Jacksonville,405000
Cesar,37,February,Houston,440000
Dana,37,April,Detroit,475000
<start>
Name: Alaina | Age: 49 | Birth Month: September | City: Seattle | Income: 475000
Name: Brandon | Age: 22 | Birth Month: January | City: Portland | Income: 325000
Name: Reginald | Age: 58 | Birth Month: July | City: Louisville | Income: 155000
Name: Carmen | Age: 23 | Birth Month: March | City: Phoenix | Income: 45000
Name: Margaret | Age: 35 | Birth Month: December | City: Charlotte | Income: 275000
Name: Rosemarie | Age: 29 | Birth Month: July | City: Portland | Income: 325000
Name: Virgie | Age: 30 | Birth Month: January | City: Jacksonville | Income: 405000
Name: Cesar | Age: 37 | Birth Month: February | City: Houston | Income: 440000
Name: Dana | Age: 37 | Birth Month: April | City: Detroit | Income: 475000
<end>Here's some json data, can you convert it to markdown?
[
    {
        "Restaurant Name": "Sushi World",
        "Cuisine": "Italian",
        "Location": "Chicago",
        "Rating": 4,
        "Price Range": "$$$$"
    },
    {
        "Restaurant Name": "Pasta Palace",
        "Cuisine": "Japanese",
        "Location": "Houston",
        "Rating": 4,
        "Price Range": "$"
    },
    {
        "Restaurant Name": "Curry Corner",
        "Cuisine": "Indian",
        "Location": "Miami",
        "Rating": 4,
        "Price Range": "$$$"
    },
    {
        "Restaurant Name": "Sushi World",
        "Cuisine": "Chinese",
        "Location": "San Francisco",
        "Rating": 4,
        "Price Range": "$"
    },
    {
        "Restaurant Name": "Vegan Delight",
        "Cuisine": "American",
        "Location": "Los Angeles",
        "Rating": 4,
        "Price Range": "$$"
    },
    {
        "Restaurant Name": "Taco Town",
        "Cuisine": "Japanese",
        "Location": "Chicago",
        "Rating": 5,
        "Price Range": "$$$$$"
    },
    {
        "Restaurant Name": "Taco Town",
        "Cuisine": "Italian",
        "Location": "Miami",
        "Rating": 5,
        "Price Range": "$$$$$"
    }
]<start>
| Restaurant Name | Cuisine | Location | Rating | Price Range |
| --- | --- | --- | --- | --- |
| Sushi World | Italian | Chicago | 4 | $$$$ |
| Pasta Palace | Japanese | Houston | 4 | $ |
| Curry Corner | Indian | Miami | 4 | $$$ |
| Sushi World | Chinese | San Francisco | 4 | $ |
| Vegan Delight | American | Los Angeles | 4 | $$ |
| Taco Town | Japanese | Chicago | 5 | $$$$$ |
| Taco Town | Italian | Miami | 5 | $$$$$ |
<end>Convert this csv to plain text:
Title,Release Year
The Great Expedition,1973
Edge of Infinity,2007
Rise of the Titans,1981
Rise of the Titans,2022
Mystery of the Depths,1997
The Great Expedition,1989
The Great Expedition,1996
The Final Voyage,2014
The Great Expedition,2015
<start>
Title: The Great Expedition | Release Year: 1973
Title: Edge of Infinity | Release Year: 2007
Title: Rise of the Titans | Release Year: 1981
Title: Rise of the Titans | Release Year: 2022
Title: Mystery of the Depths | Release Year: 1997
Title: The Great Expedition | Release Year: 1989
Title: The Great Expedition | Release Year: 1996
Title: The Final Voyage | Release Year: 2014
Title: The Great Expedition | Release Year: 2015
<end>Transform this markdown structure to a Yaml format:
| Start Location | End Location | Duration (hours) | Fuel Used (gallons) |
| --- | --- | --- | --- |
| Chicago | Houston | 31.5 | 34.7 |
| Phoenix | Chicago | 51.9 | 46.9 |
| Chicago | Phoenix | 15.6 | 72.8 |
| New York | San Francisco | 31.0 | 48.4 |
| New York | Chicago | 39.5 | 26.8 |
| Los Angeles | Houston | 43.1 | 22.2 |<start>
- Duration (hours): 31.5
  End Location: Houston
  Fuel Used (gallons): 34.7
  Start Location: Chicago
- Duration (hours): 51.9
  End Location: Chicago
  Fuel Used (gallons): 46.9
  Start Location: Phoenix
- Duration (hours): 15.6
  End Location: Phoenix
  Fuel Used (gallons): 72.8
  Start Location: Chicago
- Duration (hours): 31.0
  End Location: San Francisco
  Fuel Used (gallons): 48.4
  Start Location: New York
- Duration (hours): 39.5
  End Location: Chicago
  Fuel Used (gallons): 26.8
  Start Location: New York
- Duration (hours): 43.1
  End Location: Houston
  Fuel Used (gallons): 22.2
  Start Location: Los Angeles
<end>Here's some csv data, can you convert it to json?
Device ID,Device Type,Location,Battery Level (%),Reading Value,Timestamp
device-0030,Light Sensor,Garden,37.5,-7.44,2022-12-10 11:02:50
device-0087,Motion Detector,Hallway,39.1,74.04,2022-04-25 23:02:29
device-0022,Humidity Sensor,Kitchen,66.5,7.04,2023-11-21 17:02:19
device-0036,Motion Detector,Hallway,23.7,-0.84,2023-12-04 12:36:54
device-0006,Humidity Sensor,Garage,56.8,-1.66,2023-05-16 08:08:36
device-0029,Pressure Sensor,Bathroom,38.2,-7.44,2021-02-10 18:56:33
<start>
[
    {
        "Device ID": "device-0030",
        "Device Type": "Light Sensor",
        "Location": "Garden",
        "Battery Level (%)": 37.5,
        "Reading Value": -7.44,
        "Timestamp": "2022-12-10 11:02:50"
    },
    {
        "Device ID": "device-0087",
        "Device Type": "Motion Detector",
        "Location": "Hallway",
        "Battery Level (%)": 39.1,
        "Reading Value": 74.04,
        "Timestamp": "2022-04-25 23:02:29"
    },
    {
        "Device ID": "device-0022",
        "Device Type": "Humidity Sensor",
        "Location": "Kitchen",
        "Battery Level (%)": 66.5,
        "Reading Value": 7.04,
        "Timestamp": "2023-11-21 17:02:19"
    },
    {
        "Device ID": "device-0036",
        "Device Type": "Motion Detector",
        "Location": "Hallway",
        "Battery Level (%)": 23.7,
        "Reading Value": -0.84,
        "Timestamp": "2023-12-04 12:36:54"
    },
    {
        "Device ID": "device-0006",
        "Device Type": "Humidity Sensor",
        "Location": "Garage",
        "Battery Level (%)": 56.8,
        "Reading Value": -1.66,
        "Timestamp": "2023-05-16 08:08:36"
    },
    {
        "Device ID": "device-0029",
        "Device Type": "Pressure Sensor",
        "Location": "Bathroom",
        "Battery Level (%)": 38.2,
        "Reading Value": -7.44,
        "Timestamp": "2021-02-10 18:56:33"
    }
]
<end>Transform this Markdown structure to a Json format:
| Company | Sector | Market Cap | Stock Price | Annual Revenue (B) | Quarter |
| --- | --- | --- | --- | --- | --- |
| Foodies | Energy | Small Cap | 572.37 | 188.82 | Q4 |
| AutoDrive | Energy | Mega Cap | 917.25 | 346.48 | Q3 |
| EcoEnergy | Automotive | Mid Cap | 637.8 | 333.52 | Q3 |
| BioPharm | Energy | Large Cap | 403.17 | 492.19 | Q2 |<start>
[
    {
        "Company": "Foodies",
        "Sector": "Energy",
        "Market Cap": "Small Cap",
        "Stock Price": 572.37,
        "Annual Revenue (B)": 188.82,
        "Quarter": "Q4"
    },
    {
        "Company": "AutoDrive",
        "Sector": "Energy",
        "Market Cap": "Mega Cap",
        "Stock Price": 917.25,
        "Annual Revenue (B)": 346.48,
        "Quarter": "Q3"
    },
    {
        "Company": "EcoEnergy",
        "Sector": "Automotive",
        "Market Cap": "Mid Cap",
        "Stock Price": 637.8,
        "Annual Revenue (B)": 333.52,
        "Quarter": "Q3"
    },
    {
        "Company": "BioPharm",
        "Sector": "Energy",
        "Market Cap": "Large Cap",
        "Stock Price": 403.17,
        "Annual Revenue (B)": 492.19,
        "Quarter": "Q2"
    }
]
<end>Please transform the following markdown data into PLAIN TEXT:
| Location | Condition | Temperature (C) | Humidity (%) | Wind Speed (km/h) | Day |
| --- | --- | --- | --- | --- | --- |
| Miami | Cloudy | 21.3 | 63 | 18.6 | Thursday |
| Houston | Windy | -2.6 | 29 | 2.3 | Sunday |
| Miami | Sunny | -9.2 | 98 | 26.3 | Monday |
| New York | Cloudy | 1.1 | 92 | 16.8 | Sunday |<start>
Location: Miami | Condition: Cloudy | Temperature (C): 21.3 | Humidity (%): 63 | Wind Speed (km/h): 18.6 | Day: Thursday
Location: Houston | Condition: Windy | Temperature (C): -2.6 | Humidity (%): 29 | Wind Speed (km/h): 2.3 | Day: Sunday
Location: Miami | Condition: Sunny | Temperature (C): -9.2 | Humidity (%): 98 | Wind Speed (km/h): 26.3 | Day: Monday
Location: New York | Condition: Cloudy | Temperature (C): 1.1 | Humidity (%): 92 | Wind Speed (km/h): 16.8 | Day: Sunday
<end>Please transform the following PLAIN TEXT data into Json:
Product Name: Whatchamacallit | SKU: SKU-1004 | Price: 255.56 | Category: Household | Supplier Name: ACME Corp
Product Name: Doohickey | SKU: SKU-1074 | Price: 454.66 | Category: Toys | Supplier Name: Wonka Industries
Product Name: Thingamajig | SKU: SKU-1090 | Price: 29.03 | Category: Electronics | Supplier Name: Umbrella Corp
Product Name: Gizmo | SKU: SKU-1018 | Price: 31.76 | Category: Automotive | Supplier Name: Wonka Industries
Product Name: Widget | SKU: SKU-1054 | Price: 391.51 | Category: Household | Supplier Name: Wayne Enterprises
Product Name: Device | SKU: SKU-1094 | Price: 356.65 | Category: Sports | Supplier Name: Wonka Industries
Product Name: Thingamajig | SKU: SKU-1097 | Price: 329.94 | Category: Sports | Supplier Name: Umbrella Corp
Product Name: Gizmo | SKU: SKU-1062 | Price: 206.86 | Category: Toys | Supplier Name: ACME Corp
Product Name: Thingamajig | SKU: SKU-1017 | Price: 194.09 | Category: Sports | Supplier Name: Wayne Enterprises
Product Name: Doohickey | SKU: SKU-1030 | Price: 98.59 | Category: Toys | Supplier Name: Wonka Industries
<start>
[
    {
        "Product Name": "Whatchamacallit",
        "SKU": "SKU-1004",
        "Price": 255.56,
        "Category": "Household",
        "Supplier Name": "ACME Corp"
    },
    {
        "Product Name": "Doohickey",
        "SKU": "SKU-1074",
        "Price": 454.66,
        "Category": "Toys",
        "Supplier Name": "Wonka Industries"
    },
    {
        "Product Name": "Thingamajig",
        "SKU": "SKU-1090",
        "Price": 29.03,
        "Category": "Electronics",
        "Supplier Name": "Umbrella Corp"
    },
    {
        "Product Name": "Gizmo",
        "SKU": "SKU-1018",
        "Price": 31.76,
        "Category": "Automotive",
        "Supplier Name": "Wonka Industries"
    },
    {
        "Product Name": "Widget",
        "SKU": "SKU-1054",
        "Price": 391.51,
        "Category": "Household",
        "Supplier Name": "Wayne Enterprises"
    },
    {
        "Product Name": "Device",
        "SKU": "SKU-1094",
        "Price": 356.65,
        "Category": "Sports",
        "Supplier Name": "Wonka Industries"
    },
    {
        "Product Name": "Thingamajig",
        "SKU": "SKU-1097",
        "Price": 329.94,
        "Category": "Sports",
        "Supplier Name": "Umbrella Corp"
    },
    {
        "Product Name": "Gizmo",
        "SKU": "SKU-1062",
        "Price": 206.86,
        "Category": "Toys",
        "Supplier Name": "ACME Corp"
    },
    {
        "Product Name": "Thingamajig",
        "SKU": "SKU-1017",
        "Price": 194.09,
        "Category": "Sports",
        "Supplier Name": "Wayne Enterprises"
    },
    {
        "Product Name": "Doohickey",
        "SKU": "SKU-1030",
        "Price": 98.59,
        "Category": "Toys",
        "Supplier Name": "Wonka Industries"
    }
]
<end>Can you change this Markdown into plain text?
| Company | Date | Open Price | High Price | Volume |
| --- | --- | --- | --- | --- |
| TechnoCorp | 2016-05-05 | 371.26 | 765.05 | 7746927 |
| FoodChain | 2013-04-13 | 933.01 | 933.01 | 5645089 |
| MediaGroup | 2010-12-11 | 890.62 | 1188.94 | 5995704 |
| MediaGroup | 2017-08-23 | 425.86 | 1027.07 | 3744357 |
| GreenEnergy | 2014-03-04 | 310.94 | 1007.55 | 1625247 |
| MediaGroup | 2023-08-19 | 185.32 | 1417.61 | 4782383 |
| AutoMotive | 2017-08-17 | 1070.3 | 1070.3 | 2018855 |
| AeroSystems | 2017-04-21 | 628.85 | 857.19 | 3087458 |<start>
Company: TechnoCorp | Date: 2016-05-05 | Open Price: 371.26 | High Price: 765.05 | Volume: 7746927
Company: FoodChain | Date: 2013-04-13 | Open Price: 933.01 | High Price: 933.01 | Volume: 5645089
Company: MediaGroup | Date: 2010-12-11 | Open Price: 890.62 | High Price: 1188.94 | Volume: 5995704
Company: MediaGroup | Date: 2017-08-23 | Open Price: 425.86 | High Price: 1027.07 | Volume: 3744357
Company: GreenEnergy | Date: 2014-03-04 | Open Price: 310.94 | High Price: 1007.55 | Volume: 1625247
Company: MediaGroup | Date: 2023-08-19 | Open Price: 185.32 | High Price: 1417.61 | Volume: 4782383
Company: AutoMotive | Date: 2017-08-17 | Open Price: 1070.3 | High Price: 1070.3 | Volume: 2018855
Company: AeroSystems | Date: 2017-04-21 | Open Price: 628.85 | High Price: 857.19 | Volume: 3087458
<end>Transform this Json structure to a csv format:
[
    {
        "Database Name": "InventoryDB",
        "Queries per Second": 510.36,
        "Cache Hit Ratio (%)": 80.35,
        "Connection Count": 374,
        "Average Latency (ms)": 43.52,
        "Timestamp": "2022-10-06 01:30:25"
    },
    {
        "Database Name": "LogsDB",
        "Queries per Second": 4256.5,
        "Cache Hit Ratio (%)": 73.56,
        "Connection Count": 45,
        "Average Latency (ms)": 30.12,
        "Timestamp": "2023-08-01 17:37:46"
    },
    {
        "Database Name": "ProductsDB",
        "Queries per Second": 4256.5,
        "Cache Hit Ratio (%)": 76.12,
        "Connection Count": 339,
        "Average Latency (ms)": 34.92,
        "Timestamp": "2023-01-17 04:31:40"
    }
]<start>
Database Name,Queries per Second,Cache Hit Ratio (%),Connection Count,Average Latency (ms),Timestamp
InventoryDB,510.36,80.35,374,43.52,2022-10-06 01:30:25
LogsDB,4256.5,73.56,45,30.12,2023-08-01 17:37:46
ProductsDB,4256.5,76.12,339,34.92,2023-01-17 04:31:40
<end>Can you change this markdown into csv?
| Restaurant Name | Cuisine | Location | Rating | Price Range |
| --- | --- | --- | --- | --- |
| Taco Town | Chinese | Phoenix | 3 | $$$$$ |
| The Golden Spoon | American | Chicago | 4 | $$$ |
| BBQ Barn | American | Chicago | 2 | $$$$ |
| Vegan Delight | Japanese | New York | 4 | $$$ |
| Pasta Palace | Indian | Chicago | 4 | $$$ |
| BBQ Barn | Japanese | Phoenix | 4 | $$$ |
| BBQ Barn | Italian | Miami | 4 | $$$ |
| The Golden Spoon | Indian | New York | 3 | $$ |
| The Golden Spoon | French | Houston | 2 | $ |
| Burger Haven | Italian | Seattle | 3 | $$ |<start>
Restaurant Name,Cuisine,Location,Rating,Price Range
Taco Town,Chinese,Phoenix,3,$$$$$
The Golden Spoon,American,Chicago,4,$$$
BBQ Barn,American,Chicago,2,$$$$
Vegan Delight,Japanese,New York,4,$$$
Pasta Palace,Indian,Chicago,4,$$$
BBQ Barn,Japanese,Phoenix,4,$$$
BBQ Barn,Italian,Miami,4,$$$
The Golden Spoon,Indian,New York,3,$$
The Golden Spoon,French,Houston,2,$
Burger Haven,Italian,Seattle,3,$$
<end>Convert this json to yml:
[
    {
        "Database Name": "ProfilesDB",
        "Queries per Second": 2189.36,
        "Cache Hit Ratio (%)": 88.14,
        "Connection Count": 261,
        "Average Latency (ms)": 86.36,
        "Timestamp": "2022-09-21 03:25:58"
    },
    {
        "Database Name": "InventoryDB",
        "Queries per Second": 2776.86,
        "Cache Hit Ratio (%)": 94.15,
        "Connection Count": 485,
        "Average Latency (ms)": 51.7,
        "Timestamp": "2022-09-12 18:43:19"
    },
    {
        "Database Name": "OrdersDB",
        "Queries per Second": 4268.22,
        "Cache Hit Ratio (%)": 86.72,
        "Connection Count": 337,
        "Average Latency (ms)": 18.96,
        "Timestamp": "2023-07-06 09:54:39"
    },
    {
        "Database Name": "ProductsDB",
        "Queries per Second": 4331.15,
        "Cache Hit Ratio (%)": 72.39,
        "Connection Count": 46,
        "Average Latency (ms)": 16.12,
        "Timestamp": "2022-06-12 17:01:31"
    }
]<start>
- Average Latency (ms): 86.36
  Cache Hit Ratio (%): 88.14
  Connection Count: 261
  Database Name: ProfilesDB
  Queries per Second: 2189.36
  Timestamp: '2022-09-21 03:25:58'
- Average Latency (ms): 51.7
  Cache Hit Ratio (%): 94.15
  Connection Count: 485
  Database Name: InventoryDB
  Queries per Second: 2776.86
  Timestamp: '2022-09-12 18:43:19'
- Average Latency (ms): 18.96
  Cache Hit Ratio (%): 86.72
  Connection Count: 337
  Database Name: OrdersDB
  Queries per Second: 4268.22
  Timestamp: '2023-07-06 09:54:39'
- Average Latency (ms): 16.12
  Cache Hit Ratio (%): 72.39
  Connection Count: 46
  Database Name: ProductsDB
  Queries per Second: 4331.15
  Timestamp: '2022-06-12 17:01:31'
<end>Convert this Markdown to Plain text:
| Distance (miles) | Duration (hours) | Fuel Used (gallons) |
| --- | --- | --- |
| 2644.2 | 43.8 | 13.1 |
| 268.5 | 31.6 | 79.6 |
| 2768.9 | 16.6 | 69.8 |
| 101.1 | 48.3 | 89.3 |
| 2907.6 | 53.1 | 82.3 |<start>
Distance (miles): 2644.2 | Duration (hours): 43.8 | Fuel Used (gallons): 13.1
Distance (miles): 268.5 | Duration (hours): 31.6 | Fuel Used (gallons): 79.6
Distance (miles): 2768.9 | Duration (hours): 16.6 | Fuel Used (gallons): 69.8
Distance (miles): 101.1 | Duration (hours): 48.3 | Fuel Used (gallons): 89.3
Distance (miles): 2907.6 | Duration (hours): 53.1 | Fuel Used (gallons): 82.3
<end>Convert this JSON to yml:
[
    {
        "Name": "Marlene",
        "City": "Indianapolis",
        "Income": 455000
    },
    {
        "Name": "Morris",
        "City": "Los Angeles",
        "Income": 285000
    },
    {
        "Name": "Erica",
        "City": "Portland",
        "Income": 195000
    },
    {
        "Name": "Daniel",
        "City": "Boston",
        "Income": 320000
    },
    {
        "Name": "Micheal",
        "City": "Memphis",
        "Income": 240000
    },
    {
        "Name": "Aaliyah",
        "City": "Fort Worth",
        "Income": 435000
    },
    {
        "Name": "Angel",
        "City": "Columbus",
        "Income": 150000
    },
    {
        "Name": "Julian",
        "City": "Nashville",
        "Income": 155000
    },
    {
        "Name": "Ida",
        "City": "Milwaukee",
        "Income": 335000
    },
    {
        "Name": "Esther",
        "City": "Nashville",
        "Income": 350000
    }
]<start>
- City: Indianapolis
  Income: 455000
  Name: Marlene
- City: Los Angeles
  Income: 285000
  Name: Morris
- City: Portland
  Income: 195000
  Name: Erica
- City: Boston
  Income: 320000
  Name: Daniel
- City: Memphis
  Income: 240000
  Name: Micheal
- City: Fort Worth
  Income: 435000
  Name: Aaliyah
- City: Columbus
  Income: 150000
  Name: Angel
- City: Nashville
  Income: 155000
  Name: Julian
- City: Milwaukee
  Income: 335000
  Name: Ida
- City: Nashville
  Income: 350000
  Name: Esther
<end>Please transform the following Json data into yml:
[
    {
        "Company": "TechnoCorp",
        "Date": "2016-12-25",
        "Open Price": 530.03,
        "High Price": 1283.71,
        "Low Price": 423.79,
        "Volume": 5191627
    },
    {
        "Company": "HealthGen",
        "Date": "2013-05-21",
        "Open Price": 209.32,
        "High Price": 595.06,
        "Low Price": 209.32,
        "Volume": 1440412
    },
    {
        "Company": "BioLife",
        "Date": "2018-08-06",
        "Open Price": 659.9,
        "High Price": 1283.84,
        "Low Price": 449.09,
        "Volume": 7386083
    },
    {
        "Company": "AutoMotive",
        "Date": "2014-04-13",
        "Open Price": 1470.5,
        "High Price": 1470.5,
        "Low Price": 156.22,
        "Volume": 5789759
    },
    {
        "Company": "TechnoCorp",
        "Date": "2011-10-08",
        "Open Price": 77.43,
        "High Price": 765.65,
        "Low Price": 77.43,
        "Volume": 9606080
    },
    {
        "Company": "FoodChain",
        "Date": "2011-01-17",
        "Open Price": 1470.5,
        "High Price": 1470.5,
        "Low Price": 1104.89,
        "Volume": 8173958
    },
    {
        "Company": "MediaGroup",
        "Date": "2023-04-07",
        "Open Price": 1104.89,
        "High Price": 1324.51,
        "Low Price": 150.25,
        "Volume": 7324648
    },
    {
        "Company": "TechnoCorp",
        "Date": "2010-12-27",
        "Open Price": 1104.89,
        "High Price": 1104.89,
        "Low Price": 147.39,
        "Volume": 8395969
    }
]<start>
- Company: TechnoCorp
  Date: '2016-12-25'
  High Price: 1283.71
  Low Price: 423.79
  Open Price: 530.03
  Volume: 5191627
- Company: HealthGen
  Date: '2013-05-21'
  High Price: 595.06
  Low Price: 209.32
  Open Price: 209.32
  Volume: 1440412
- Company: BioLife
  Date: '2018-08-06'
  High Price: 1283.84
  Low Price: 449.09
  Open Price: 659.9
  Volume: 7386083
- Company: AutoMotive
  Date: '2014-04-13'
  High Price: 1470.5
  Low Price: 156.22
  Open Price: 1470.5
  Volume: 5789759
- Company: TechnoCorp
  Date: '2011-10-08'
  High Price: 765.65
  Low Price: 77.43
  Open Price: 77.43
  Volume: 9606080
- Company: FoodChain
  Date: '2011-01-17'
  High Price: 1470.5
  Low Price: 1104.89
  Open Price: 1470.5
  Volume: 8173958
- Company: MediaGroup
  Date: '2023-04-07'
  High Price: 1324.51
  Low Price: 150.25
  Open Price: 1104.89
  Volume: 7324648
- Company: TechnoCorp
  Date: '2010-12-27'
  High Price: 1104.89
  Low Price: 147.39
  Open Price: 1104.89
  Volume: 8395969
<end>Please transform the following Csv data into plain text:
SKU,Price,Stock Quantity,Category
SKU-1024,449.25,112,Toys
SKU-1017,123.5,23,Electronics
SKU-1062,207.75,468,Electronics
SKU-1095,60.68,275,Electronics
SKU-1096,16.89,470,Electronics
SKU-1033,127.35,181,Sports
<start>
SKU: SKU-1024 | Price: 449.25 | Stock Quantity: 112 | Category: Toys
SKU: SKU-1017 | Price: 123.5 | Stock Quantity: 23 | Category: Electronics
SKU: SKU-1062 | Price: 207.75 | Stock Quantity: 468 | Category: Electronics
SKU: SKU-1095 | Price: 60.68 | Stock Quantity: 275 | Category: Electronics
SKU: SKU-1096 | Price: 16.89 | Stock Quantity: 470 | Category: Electronics
SKU: SKU-1033 | Price: 127.35 | Stock Quantity: 181 | Category: Sports
<end>Here's some plain text data, can you convert it to Yml?
Location: Seattle | Condition: Rainy | Temperature (C): 24.0 | Humidity (%): 52 | Wind Speed (km/h): 7.7 | Day: Monday
Location: Seattle | Condition: Foggy | Temperature (C): 14.6 | Humidity (%): 98 | Wind Speed (km/h): 6.2 | Day: Friday
Location: Phoenix | Condition: Foggy | Temperature (C): 10.4 | Humidity (%): 92 | Wind Speed (km/h): 0.4 | Day: Monday
Location: Chicago | Condition: Stormy | Temperature (C): 32.1 | Humidity (%): 33 | Wind Speed (km/h): 22.5 | Day: Wednesday
Location: Miami | Condition: Sunny | Temperature (C): 34.2 | Humidity (%): 74 | Wind Speed (km/h): 7.9 | Day: Wednesday
Location: Houston | Condition: Stormy | Temperature (C): 14.6 | Humidity (%): 89 | Wind Speed (km/h): 29.3 | Day: Sunday
Location: Houston | Condition: Cloudy | Temperature (C): 9.6 | Humidity (%): 39 | Wind Speed (km/h): 24.3 | Day: Friday
Location: Seattle | Condition: Rainy | Temperature (C): 21.6 | Humidity (%): 89 | Wind Speed (km/h): 24.3 | Day: Tuesday
Location: Los Angeles | Condition: Foggy | Temperature (C): 25.0 | Humidity (%): 48 | Wind Speed (km/h): 4.5 | Day: Wednesday
Location: Phoenix | Condition: Windy | Temperature (C): -3.8 | Humidity (%): 63 | Wind Speed (km/h): 6.2 | Day: Sunday
<start>
- Condition: Rainy
  Day: Monday
  Humidity (%): 52
  Location: Seattle
  Temperature (C): 24.0
  Wind Speed (km/h): 7.7
- Condition: Foggy
  Day: Friday
  Humidity (%): 98
  Location: Seattle
  Temperature (C): 14.6
  Wind Speed (km/h): 6.2
- Condition: Foggy
  Day: Monday
  Humidity (%): 92
  Location: Phoenix
  Temperature (C): 10.4
  Wind Speed (km/h): 0.4
- Condition: Stormy
  Day: Wednesday
  Humidity (%): 33
  Location: Chicago
  Temperature (C): 32.1
  Wind Speed (km/h): 22.5
- Condition: Sunny
  Day: Wednesday
  Humidity (%): 74
  Location: Miami
  Temperature (C): 34.2
  Wind Speed (km/h): 7.9
- Condition: Stormy
  Day: Sunday
  Humidity (%): 89
  Location: Houston
  Temperature (C): 14.6
  Wind Speed (km/h): 29.3
- Condition: Cloudy
  Day: Friday
  Humidity (%): 39
  Location: Houston
  Temperature (C): 9.6
  Wind Speed (km/h): 24.3
- Condition: Rainy
  Day: Tuesday
  Humidity (%): 89
  Location: Seattle
  Temperature (C): 21.6
  Wind Speed (km/h): 24.3
- Condition: Foggy
  Day: Wednesday
  Humidity (%): 48
  Location: Los Angeles
  Temperature (C): 25.0
  Wind Speed (km/h): 4.5
- Condition: Windy
  Day: Sunday
  Humidity (%): 63
  Location: Phoenix
  Temperature (C): -3.8
  Wind Speed (km/h): 6.2
<end>Can you change this YAML into Plain text?
- Condition: Sunny
  Day: Sunday
  Location: New York
  Wind Speed (km/h): 19.2
- Condition: Windy
  Day: Sunday
  Location: Miami
  Wind Speed (km/h): 4.0
- Condition: Snowy
  Day: Monday
  Location: Chicago
  Wind Speed (km/h): 29.0
- Condition: Rainy
  Day: Sunday
  Location: Los Angeles
  Wind Speed (km/h): 12.4
- Condition: Stormy
  Day: Thursday
  Location: Miami
  Wind Speed (km/h): 1.8
- Condition: Cloudy
  Day: Monday
  Location: Miami
  Wind Speed (km/h): 3.7
- Condition: Rainy
  Day: Saturday
  Location: New York
  Wind Speed (km/h): 12.4
- Condition: Rainy
  Day: Monday
  Location: Los Angeles
  Wind Speed (km/h): 16.7
<start>
Location: New York | Condition: Sunny | Wind Speed (km/h): 19.2 | Day: Sunday
Location: Miami | Condition: Windy | Wind Speed (km/h): 4.0 | Day: Sunday
Location: Chicago | Condition: Snowy | Wind Speed (km/h): 29.0 | Day: Monday
Location: Los Angeles | Condition: Rainy | Wind Speed (km/h): 12.4 | Day: Sunday
Location: Miami | Condition: Stormy | Wind Speed (km/h): 1.8 | Day: Thursday
Location: Miami | Condition: Cloudy | Wind Speed (km/h): 3.7 | Day: Monday
Location: New York | Condition: Rainy | Wind Speed (km/h): 12.4 | Day: Saturday
Location: Los Angeles | Condition: Rainy | Wind Speed (km/h): 16.7 | Day: Monday
<end>Can you change this csv into MARKDOWN?
Distance (miles),Duration (hours),Fuel Used (gallons)
2846.0,64.3,81.8
2538.8,21.0,77.2
2610.4,33.5,18.1
2286.3,11.4,56.3
445.0,32.2,78.2
<start>
| Distance (miles) | Duration (hours) | Fuel Used (gallons) |
| --- | --- | --- |
| 2846.0 | 64.3 | 81.8 |
| 2538.8 | 21.0 | 77.2 |
| 2610.4 | 33.5 | 18.1 |
| 2286.3 | 11.4 | 56.3 |
| 445.0 | 32.2 | 78.2 |
<end>Can you change this Csv into Plain text?
Trip Name,Start Location,End Location,Distance (miles),Duration (hours),Fuel Used (gallons)
Canyon Trek,Denver,Chicago,2654.5,36.9,77.0
Mountain Adventure,Los Angeles,Phoenix,2249.1,70.3,32.8
Lakeside Retreat,Phoenix,Houston,720.8,20.0,23.0
Coast to Coast,San Francisco,Miami,1947.9,40.6,32.8
Canyon Trek,Phoenix,Chicago,2826.3,32.5,85.9
Canyon Trek,Chicago,New York,81.8,8.4,95.5
<start>
Trip Name: Canyon Trek | Start Location: Denver | End Location: Chicago | Distance (miles): 2654.5 | Duration (hours): 36.9 | Fuel Used (gallons): 77.0
Trip Name: Mountain Adventure | Start Location: Los Angeles | End Location: Phoenix | Distance (miles): 2249.1 | Duration (hours): 70.3 | Fuel Used (gallons): 32.8
Trip Name: Lakeside Retreat | Start Location: Phoenix | End Location: Houston | Distance (miles): 720.8 | Duration (hours): 20.0 | Fuel Used (gallons): 23.0
Trip Name: Coast to Coast | Start Location: San Francisco | End Location: Miami | Distance (miles): 1947.9 | Duration (hours): 40.6 | Fuel Used (gallons): 32.8
Trip Name: Canyon Trek | Start Location: Phoenix | End Location: Chicago | Distance (miles): 2826.3 | Duration (hours): 32.5 | Fuel Used (gallons): 85.9
Trip Name: Canyon Trek | Start Location: Chicago | End Location: New York | Distance (miles): 81.8 | Duration (hours): 8.4 | Fuel Used (gallons): 95.5
<end>Here's some yaml data, can you convert it to markdown?
- Duration (hours): 32.4
  End Location: Los Angeles
  Fuel Used (gallons): 10.9
  Start Location: San Francisco
  Trip Name: Desert Drive
- Duration (hours): 12.8
  End Location: Los Angeles
  Fuel Used (gallons): 82.4
  Start Location: New York
  Trip Name: Coast to Coast
- Duration (hours): 28.3
  End Location: Denver
  Fuel Used (gallons): 87.0
  Start Location: Miami
  Trip Name: Coast to Coast
<start>
| Trip Name | Start Location | End Location | Duration (hours) | Fuel Used (gallons) |
| --- | --- | --- | --- | --- |
| Desert Drive | San Francisco | Los Angeles | 32.4 | 10.9 |
| Coast to Coast | New York | Los Angeles | 12.8 | 82.4 |
| Coast to Coast | Miami | Denver | 28.3 | 87.0 |
<end>Convert this CSV to yml:
Device ID,Device Type,Location,Battery Level (%),Reading Value,Timestamp
device-0022,Humidity Sensor,Bedroom,62.7,11.46,2023-03-07 10:23:22
device-0004,Temperature Sensor,Garage,93.1,-1.7,2022-07-06 08:28:28
device-0014,Motion Detector,Bedroom,21.3,-21.23,2022-09-19 07:38:21
device-0064,Temperature Sensor,Kitchen,96.6,23.58,2021-05-02 15:26:46
device-0021,Temperature Sensor,Garage,42.4,-37.72,2021-02-17 15:46:19
device-0024,Motion Detector,Kitchen,84.1,-22.86,2022-09-17 11:37:13
device-0083,Humidity Sensor,Garden,19.0,35.35,2021-10-12 04:31:54
device-0003,Motion Detector,Kitchen,83.7,-17.03,2023-04-01 16:26:55
device-0062,Pressure Sensor,Garage,14.9,32.2,2022-03-06 20:57:12
device-0013,Temperature Sensor,Office,43.5,-19.52,2022-02-13 07:18:05
<start>
- Battery Level (%): 62.7
  Device ID: device-0022
  Device Type: Humidity Sensor
  Location: Bedroom
  Reading Value: 11.46
  Timestamp: '2023-03-07 10:23:22'
- Battery Level (%): 93.1
  Device ID: device-0004
  Device Type: Temperature Sensor
  Location: Garage
  Reading Value: -1.7
  Timestamp: '2022-07-06 08:28:28'
- Battery Level (%): 21.3
  Device ID: device-0014
  Device Type: Motion Detector
  Location: Bedroom
  Reading Value: -21.23
  Timestamp: '2022-09-19 07:38:21'
- Battery Level (%): 96.6
  Device ID: device-0064
  Device Type: Temperature Sensor
  Location: Kitchen
  Reading Value: 23.58
  Timestamp: '2021-05-02 15:26:46'
- Battery Level (%): 42.4
  Device ID: device-0021
  Device Type: Temperature Sensor
  Location: Garage
  Reading Value: -37.72
  Timestamp: '2021-02-17 15:46:19'
- Battery Level (%): 84.1
  Device ID: device-0024
  Device Type: Motion Detector
  Location: Kitchen
  Reading Value: -22.86
  Timestamp: '2022-09-17 11:37:13'
- Battery Level (%): 19.0
  Device ID: device-0083
  Device Type: Humidity Sensor
  Location: Garden
  Reading Value: 35.35
  Timestamp: '2021-10-12 04:31:54'
- Battery Level (%): 83.7
  Device ID: device-0003
  Device Type: Motion Detector
  Location: Kitchen
  Reading Value: -17.03
  Timestamp: '2023-04-01 16:26:55'
- Battery Level (%): 14.9
  Device ID: device-0062
  Device Type: Pressure Sensor
  Location: Garage
  Reading Value: 32.2
  Timestamp: '2022-03-06 20:57:12'
- Battery Level (%): 43.5
  Device ID: device-0013
  Device Type: Temperature Sensor
  Location: Office
  Reading Value: -19.52
  Timestamp: '2022-02-13 07:18:05'
<end>Convert this YML to json:
- Condition: Cloudy
  Day: Saturday
  Humidity (%): 79
  Temperature (C): 9.4
  Wind Speed (km/h): 22.2
- Condition: Cloudy
  Day: Tuesday
  Humidity (%): 72
  Temperature (C): 20.2
  Wind Speed (km/h): 27.4
- Condition: Sunny
  Day: Wednesday
  Humidity (%): 94
  Temperature (C): 35.0
  Wind Speed (km/h): 17.4
- Condition: Sunny
  Day: Wednesday
  Humidity (%): 80
  Temperature (C): 23.6
  Wind Speed (km/h): 19.1
- Condition: Windy
  Day: Thursday
  Humidity (%): 41
  Temperature (C): 18.7
  Wind Speed (km/h): 16.4
- Condition: Windy
  Day: Monday
  Humidity (%): 41
  Temperature (C): -9.4
  Wind Speed (km/h): 16.2
- Condition: Sunny
  Day: Friday
  Humidity (%): 98
  Temperature (C): 9.8
  Wind Speed (km/h): 2.0
- Condition: Rainy
  Day: Sunday
  Humidity (%): 36
  Temperature (C): 37.3
  Wind Speed (km/h): 24.7
<start>
[
    {
        "Condition": "Cloudy",
        "Temperature (C)": 9.4,
        "Humidity (%)": 79,
        "Wind Speed (km/h)": 22.2,
        "Day": "Saturday"
    },
    {
        "Condition": "Cloudy",
        "Temperature (C)": 20.2,
        "Humidity (%)": 72,
        "Wind Speed (km/h)": 27.4,
        "Day": "Tuesday"
    },
    {
        "Condition": "Sunny",
        "Temperature (C)": 35.0,
        "Humidity (%)": 94,
        "Wind Speed (km/h)": 17.4,
        "Day": "Wednesday"
    },
    {
        "Condition": "Sunny",
        "Temperature (C)": 23.6,
        "Humidity (%)": 80,
        "Wind Speed (km/h)": 19.1,
        "Day": "Wednesday"
    },
    {
        "Condition": "Windy",
        "Temperature (C)": 18.7,
        "Humidity (%)": 41,
        "Wind Speed (km/h)": 16.4,
        "Day": "Thursday"
    },
    {
        "Condition": "Windy",
        "Temperature (C)": -9.4,
        "Humidity (%)": 41,
        "Wind Speed (km/h)": 16.2,
        "Day": "Monday"
    },
    {
        "Condition": "Sunny",
        "Temperature (C)": 9.8,
        "Humidity (%)": 98,
        "Wind Speed (km/h)": 2.0,
        "Day": "Friday"
    },
    {
        "Condition": "Rainy",
        "Temperature (C)": 37.3,
        "Humidity (%)": 36,
        "Wind Speed (km/h)": 24.7,
        "Day": "Sunday"
    }
]
<end>Please transform the following json data into csv:
[
    {
        "Company": "GlobalTrade",
        "Market Cap": "Mid Cap",
        "Stock Price": 921.53
    },
    {
        "Company": "AeroSpace",
        "Market Cap": "Small Cap",
        "Stock Price": 317.62
    },
    {
        "Company": "AutoDrive",
        "Market Cap": "Large Cap",
        "Stock Price": 784.34
    },
    {
        "Company": "BioPharm",
        "Market Cap": "Mid Cap",
        "Stock Price": 586.03
    },
    {
        "Company": "AeroSpace",
        "Market Cap": "Mega Cap",
        "Stock Price": 966.19
    },
    {
        "Company": "GlobalTrade",
        "Market Cap": "Mega Cap",
        "Stock Price": 687.59
    },
    {
        "Company": "TechCorp",
        "Market Cap": "Mega Cap",
        "Stock Price": 467.04
    },
    {
        "Company": "Foodies",
        "Market Cap": "Mega Cap",
        "Stock Price": 268.92
    }
]<start>
Company,Market Cap,Stock Price
GlobalTrade,Mid Cap,921.53
AeroSpace,Small Cap,317.62
AutoDrive,Large Cap,784.34
BioPharm,Mid Cap,586.03
AeroSpace,Mega Cap,966.19
GlobalTrade,Mega Cap,687.59
TechCorp,Mega Cap,467.04
Foodies,Mega Cap,268.92
<end>Here's some json data, can you convert it to csv?
[
    {
        "Company": "AeroSystems",
        "Date": "2018-12-08",
        "Open Price": 1311.78,
        "Close Price": 1425.67,
        "High Price": 1425.67,
        "Low Price": 971.8,
        "Volume": 7620412
    },
    {
        "Company": "MediaGroup",
        "Date": "2019-08-05",
        "Open Price": 1319.57,
        "Close Price": 205.7,
        "High Price": 1319.57,
        "Low Price": 205.7,
        "Volume": 5495258
    },
    {
        "Company": "MediaGroup",
        "Date": "2023-07-02",
        "Open Price": 426.38,
        "Close Price": 13.47,
        "High Price": 1294.63,
        "Low Price": 13.47,
        "Volume": 5501997
    },
    {
        "Company": "FinanceTrust",
        "Date": "2020-05-21",
        "Open Price": 234.04,
        "Close Price": 41.94,
        "High Price": 234.04,
        "Low Price": 41.94,
        "Volume": 2541793
    },
    {
        "Company": "BioLife",
        "Date": "2015-04-03",
        "Open Price": 979.17,
        "Close Price": 1425.67,
        "High Price": 1425.67,
        "Low Price": 202.95,
        "Volume": 1202462
    },
    {
        "Company": "RetailWorld",
        "Date": "2020-07-02",
        "Open Price": 234.04,
        "Close Price": 102.89,
        "High Price": 899.79,
        "Low Price": 102.89,
        "Volume": 9666634
    },
    {
        "Company": "FoodChain",
        "Date": "2022-02-07",
        "Open Price": 724.2,
        "Close Price": 870.47,
        "High Price": 912.91,
        "Low Price": 724.2,
        "Volume": 6406752
    },
    {
        "Company": "BioLife",
        "Date": "2022-12-23",
        "Open Price": 1348.23,
        "Close Price": 376.06,
        "High Price": 1348.23,
        "Low Price": 345.79,
        "Volume": 7061078
    },
    {
        "Company": "AeroSystems",
        "Date": "2022-05-22",
        "Open Price": 1348.23,
        "Close Price": 722.38,
        "High Price": 1348.23,
        "Low Price": 722.38,
        "Volume": 3481905
    },
    {
        "Company": "HealthGen",
        "Date": "2021-05-16",
        "Open Price": 971.8,
        "Close Price": 112.43,
        "High Price": 1128.71,
        "Low Price": 112.43,
        "Volume": 8615821
    }
]<start>
Company,Date,Open Price,Close Price,High Price,Low Price,Volume
AeroSystems,2018-12-08,1311.78,1425.67,1425.67,971.8,7620412
MediaGroup,2019-08-05,1319.57,205.7,1319.57,205.7,5495258
MediaGroup,2023-07-02,426.38,13.47,1294.63,13.47,5501997
FinanceTrust,2020-05-21,234.04,41.94,234.04,41.94,2541793
BioLife,2015-04-03,979.17,1425.67,1425.67,202.95,1202462
RetailWorld,2020-07-02,234.04,102.89,899.79,102.89,9666634
FoodChain,2022-02-07,724.2,870.47,912.91,724.2,6406752
BioLife,2022-12-23,1348.23,376.06,1348.23,345.79,7061078
AeroSystems,2022-05-22,1348.23,722.38,1348.23,722.38,3481905
HealthGen,2021-05-16,971.8,112.43,1128.71,112.43,8615821
<end>Can you change this CSV into Json?
Release Year,Box Office Earnings (M)
1988,220.55
1982,786.03
2016,890.43
1983,38.8
1998,446.67
2015,702.32
1990,355.75
2010,583.1
<start>
[
    {
        "Release Year": 1988,
        "Box Office Earnings (M)": 220.55
    },
    {
        "Release Year": 1982,
        "Box Office Earnings (M)": 786.03
    },
    {
        "Release Year": 2016,
        "Box Office Earnings (M)": 890.43
    },
    {
        "Release Year": 1983,
        "Box Office Earnings (M)": 38.8
    },
    {
        "Release Year": 1998,
        "Box Office Earnings (M)": 446.67
    },
    {
        "Release Year": 2015,
        "Box Office Earnings (M)": 702.32
    },
    {
        "Release Year": 1990,
        "Box Office Earnings (M)": 355.75
    },
    {
        "Release Year": 2010,
        "Box Office Earnings (M)": 583.1
    }
]
<end>Convert this csv to json:
Trip Name,Start Location,End Location,Distance (miles),Duration (hours),Fuel Used (gallons)
Highway Odyssey,San Francisco,Denver,2661.5,10.7,60.2
Historic Route,Los Angeles,San Francisco,2423.3,71.4,22.6
Forest Journey,Phoenix,New York,1703.9,38.2,88.9
Highway Odyssey,Los Angeles,Denver,1489.3,22.3,80.2
Canyon Trek,Chicago,Los Angeles,488.6,16.6,97.0
Desert Drive,Denver,New York,2547.3,35.7,24.7
Canyon Trek,Denver,Houston,362.0,38.2,88.9
Coast to Coast,Los Angeles,Phoenix,79.3,26.9,84.6
<start>
[
    {
        "Trip Name": "Highway Odyssey",
        "Start Location": "San Francisco",
        "End Location": "Denver",
        "Distance (miles)": 2661.5,
        "Duration (hours)": 10.7,
        "Fuel Used (gallons)": 60.2
    },
    {
        "Trip Name": "Historic Route",
        "Start Location": "Los Angeles",
        "End Location": "San Francisco",
        "Distance (miles)": 2423.3,
        "Duration (hours)": 71.4,
        "Fuel Used (gallons)": 22.6
    },
    {
        "Trip Name": "Forest Journey",
        "Start Location": "Phoenix",
        "End Location": "New York",
        "Distance (miles)": 1703.9,
        "Duration (hours)": 38.2,
        "Fuel Used (gallons)": 88.9
    },
    {
        "Trip Name": "Highway Odyssey",
        "Start Location": "Los Angeles",
        "End Location": "Denver",
        "Distance (miles)": 1489.3,
        "Duration (hours)": 22.3,
        "Fuel Used (gallons)": 80.2
    },
    {
        "Trip Name": "Canyon Trek",
        "Start Location": "Chicago",
        "End Location": "Los Angeles",
        "Distance (miles)": 488.6,
        "Duration (hours)": 16.6,
        "Fuel Used (gallons)": 97.0
    },
    {
        "Trip Name": "Desert Drive",
        "Start Location": "Denver",
        "End Location": "New York",
        "Distance (miles)": 2547.3,
        "Duration (hours)": 35.7,
        "Fuel Used (gallons)": 24.7
    },
    {
        "Trip Name": "Canyon Trek",
        "Start Location": "Denver",
        "End Location": "Houston",
        "Distance (miles)": 362.0,
        "Duration (hours)": 38.2,
        "Fuel Used (gallons)": 88.9
    },
    {
        "Trip Name": "Coast to Coast",
        "Start Location": "Los Angeles",
        "End Location": "Phoenix",
        "Distance (miles)": 79.3,
        "Duration (hours)": 26.9,
        "Fuel Used (gallons)": 84.6
    }
]
<end>Can you change this JSON into yml?
[
    {
        "Director": "Aria Ravenwood",
        "Release Year": 1970,
        "Box Office Earnings (M)": 43.97
    },
    {
        "Director": "Lira Silverleaf",
        "Release Year": 2003,
        "Box Office Earnings (M)": 542.31
    },
    {
        "Director": "Lira Silverleaf",
        "Release Year": 2002,
        "Box Office Earnings (M)": 43.82
    },
    {
        "Director": "Zara Stormrider",
        "Release Year": 1996,
        "Box Office Earnings (M)": 870.49
    },
    {
        "Director": "Zara Stormrider",
        "Release Year": 2004,
        "Box Office Earnings (M)": 821.79
    }
]<start>
- Box Office Earnings (M): 43.97
  Director: Aria Ravenwood
  Release Year: 1970
- Box Office Earnings (M): 542.31
  Director: Lira Silverleaf
  Release Year: 2003
- Box Office Earnings (M): 43.82
  Director: Lira Silverleaf
  Release Year: 2002
- Box Office Earnings (M): 870.49
  Director: Zara Stormrider
  Release Year: 1996
- Box Office Earnings (M): 821.79
  Director: Zara Stormrider
  Release Year: 2004
<end>Here's some JSON data, can you convert it to markdown?
[
    {
        "Location": "Seattle",
        "Condition": "Stormy",
        "Humidity (%)": 70,
        "Wind Speed (km/h)": 4.0
    },
    {
        "Location": "Los Angeles",
        "Condition": "Snowy",
        "Humidity (%)": 79,
        "Wind Speed (km/h)": 2.3
    },
    {
        "Location": "Los Angeles",
        "Condition": "Cloudy",
        "Humidity (%)": 67,
        "Wind Speed (km/h)": 27.6
    },
    {
        "Location": "Seattle",
        "Condition": "Foggy",
        "Humidity (%)": 90,
        "Wind Speed (km/h)": 10.3
    },
    {
        "Location": "Denver",
        "Condition": "Snowy",
        "Humidity (%)": 80,
        "Wind Speed (km/h)": 18.5
    },
    {
        "Location": "Seattle",
        "Condition": "Cloudy",
        "Humidity (%)": 62,
        "Wind Speed (km/h)": 19.6
    },
    {
        "Location": "New York",
        "Condition": "Foggy",
        "Humidity (%)": 20,
        "Wind Speed (km/h)": 8.5
    }
]<start>
| Location | Condition | Humidity (%) | Wind Speed (km/h) |
| --- | --- | --- | --- |
| Seattle | Stormy | 70 | 4.0 |
| Los Angeles | Snowy | 79 | 2.3 |
| Los Angeles | Cloudy | 67 | 27.6 |
| Seattle | Foggy | 90 | 10.3 |
| Denver | Snowy | 80 | 18.5 |
| Seattle | Cloudy | 62 | 19.6 |
| New York | Foggy | 20 | 8.5 |
<end>Convert this PLAIN TEXT to csv:
Title: Starbound Odyssey | Director: Cade Firebrand | Genre: Fantasy
Title: Edge of Infinity | Director: Orin Shadowalker | Genre: Horror
Title: The Final Voyage | Director: Cade Firebrand | Genre: Drama
<start>
Title,Director,Genre
Starbound Odyssey,Cade Firebrand,Fantasy
Edge of Infinity,Orin Shadowalker,Horror
The Final Voyage,Cade Firebrand,Drama
<end>Here's some yaml data, can you convert it to plain text?
- Annual Revenue (B): 458.44
  Company: AeroSpace
  Market Cap: Small Cap
  Quarter: Q2
  Sector: Biotech
  Stock Price: 258.95
- Annual Revenue (B): 89.19
  Company: AeroSpace
  Market Cap: Large Cap
  Quarter: Q4
  Sector: Healthcare
  Stock Price: 783.09
- Annual Revenue (B): 423.68
  Company: BioPharm
  Market Cap: Small Cap
  Quarter: Q2
  Sector: Retail
  Stock Price: 992.05
- Annual Revenue (B): 323.66
  Company: GlobalTrade
  Market Cap: Mid Cap
  Quarter: Q4
  Sector: Aerospace
  Stock Price: 886.17
- Annual Revenue (B): 409.64
  Company: AeroSpace
  Market Cap: Small Cap
  Quarter: Q3
  Sector: Technology
  Stock Price: 763.86
- Annual Revenue (B): 181.49
  Company: FinanceWorks
  Market Cap: Mid Cap
  Quarter: Q3
  Sector: Energy
  Stock Price: 920.83
- Annual Revenue (B): 142.39
  Company: GlobalTrade
  Market Cap: Mega Cap
  Quarter: Q4
  Sector: Automotive
  Stock Price: 625.71
- Annual Revenue (B): 472.81
  Company: AutoDrive
  Market Cap: Mega Cap
  Quarter: Q3
  Sector: Energy
  Stock Price: 268.59
- Annual Revenue (B): 174.34
  Company: AutoDrive
  Market Cap: Large Cap
  Quarter: Q4
  Sector: Healthcare
  Stock Price: 570.46
- Annual Revenue (B): 163.6
  Company: BioPharm
  Market Cap: Mega Cap
  Quarter: Q4
  Sector: Retail
  Stock Price: 152.98
<start>
Company: AeroSpace | Sector: Biotech | Market Cap: Small Cap | Stock Price: 258.95 | Annual Revenue (B): 458.44 | Quarter: Q2
Company: AeroSpace | Sector: Healthcare | Market Cap: Large Cap | Stock Price: 783.09 | Annual Revenue (B): 89.19 | Quarter: Q4
Company: BioPharm | Sector: Retail | Market Cap: Small Cap | Stock Price: 992.05 | Annual Revenue (B): 423.68 | Quarter: Q2
Company: GlobalTrade | Sector: Aerospace | Market Cap: Mid Cap | Stock Price: 886.17 | Annual Revenue (B): 323.66 | Quarter: Q4
Company: AeroSpace | Sector: Technology | Market Cap: Small Cap | Stock Price: 763.86 | Annual Revenue (B): 409.64 | Quarter: Q3
Company: FinanceWorks | Sector: Energy | Market Cap: Mid Cap | Stock Price: 920.83 | Annual Revenue (B): 181.49 | Quarter: Q3
Company: GlobalTrade | Sector: Automotive | Market Cap: Mega Cap | Stock Price: 625.71 | Annual Revenue (B): 142.39 | Quarter: Q4
Company: AutoDrive | Sector: Energy | Market Cap: Mega Cap | Stock Price: 268.59 | Annual Revenue (B): 472.81 | Quarter: Q3
Company: AutoDrive | Sector: Healthcare | Market Cap: Large Cap | Stock Price: 570.46 | Annual Revenue (B): 174.34 | Quarter: Q4
Company: BioPharm | Sector: Retail | Market Cap: Mega Cap | Stock Price: 152.98 | Annual Revenue (B): 163.6 | Quarter: Q4
<end>Transform this plain text structure to a json format:
Trip Name: Forest Journey | Start Location: San Francisco | End Location: Phoenix | Distance (miles): 1250.5 | Fuel Used (gallons): 16.4
Trip Name: Lakeside Retreat | Start Location: San Francisco | End Location: Chicago | Distance (miles): 1651.3 | Fuel Used (gallons): 68.2
Trip Name: City Explorer | Start Location: San Francisco | End Location: Chicago | Distance (miles): 1651.3 | Fuel Used (gallons): 48.4
Trip Name: Lakeside Retreat | Start Location: San Francisco | End Location: Los Angeles | Distance (miles): 66.1 | Fuel Used (gallons): 38.4
Trip Name: City Explorer | Start Location: Miami | End Location: Denver | Distance (miles): 608.0 | Fuel Used (gallons): 19.1
<start>
[
    {
        "Trip Name": "Forest Journey",
        "Start Location": "San Francisco",
        "End Location": "Phoenix",
        "Distance (miles)": 1250.5,
        "Fuel Used (gallons)": 16.4
    },
    {
        "Trip Name": "Lakeside Retreat",
        "Start Location": "San Francisco",
        "End Location": "Chicago",
        "Distance (miles)": 1651.3,
        "Fuel Used (gallons)": 68.2
    },
    {
        "Trip Name": "City Explorer",
        "Start Location": "San Francisco",
        "End Location": "Chicago",
        "Distance (miles)": 1651.3,
        "Fuel Used (gallons)": 48.4
    },
    {
        "Trip Name": "Lakeside Retreat",
        "Start Location": "San Francisco",
        "End Location": "Los Angeles",
        "Distance (miles)": 66.1,
        "Fuel Used (gallons)": 38.4
    },
    {
        "Trip Name": "City Explorer",
        "Start Location": "Miami",
        "End Location": "Denver",
        "Distance (miles)": 608.0,
        "Fuel Used (gallons)": 19.1
    }
]
<end>Here's some PLAIN TEXT data, can you convert it to yaml?
Title: The Great Expedition | Box Office Earnings (M): 160.12
Title: Edge of Infinity | Box Office Earnings (M): 798.7
Title: The Endless Horizon | Box Office Earnings (M): 206.02
Title: The Great Expedition | Box Office Earnings (M): 954.27
Title: Escape from Earth | Box Office Earnings (M): 325.17
Title: The Final Voyage | Box Office Earnings (M): 608.06
Title: Rise of the Titans | Box Office Earnings (M): 620.99
<start>
- Box Office Earnings (M): 160.12
  Title: The Great Expedition
- Box Office Earnings (M): 798.7
  Title: Edge of Infinity
- Box Office Earnings (M): 206.02
  Title: The Endless Horizon
- Box Office Earnings (M): 954.27
  Title: The Great Expedition
- Box Office Earnings (M): 325.17
  Title: Escape from Earth
- Box Office Earnings (M): 608.06
  Title: The Final Voyage
- Box Office Earnings (M): 620.99
  Title: Rise of the Titans
<end>Transform this csv structure to a YAML format:
Device ID,Device Type,Location,Battery Level (%),Reading Value,Timestamp
device-0019,Humidity Sensor,Office,89.7,20.16,2021-02-10 06:56:28
device-0061,Temperature Sensor,Kitchen,17.7,-3.0,2023-11-19 01:37:02
device-0045,Light Sensor,Hallway,19.9,52.22,2021-08-13 08:30:35
device-0038,Humidity Sensor,Kitchen,49.6,41.27,2022-06-04 23:18:54
device-0083,Temperature Sensor,Living Room,71.4,-18.07,2021-05-19 21:01:52
device-0057,Temperature Sensor,Hallway,66.7,35.22,2023-06-16 10:36:15
device-0092,Humidity Sensor,Garage,73.1,53.01,2023-10-09 00:22:43
device-0021,Temperature Sensor,Hallway,33.9,60.55,2021-04-28 10:40:05
device-0090,Light Sensor,Bathroom,70.5,65.67,2021-02-03 19:58:42
device-0002,Temperature Sensor,Hallway,21.6,32.32,2022-10-17 20:09:28
<start>
- Battery Level (%): 89.7
  Device ID: device-0019
  Device Type: Humidity Sensor
  Location: Office
  Reading Value: 20.16
  Timestamp: '2021-02-10 06:56:28'
- Battery Level (%): 17.7
  Device ID: device-0061
  Device Type: Temperature Sensor
  Location: Kitchen
  Reading Value: -3.0
  Timestamp: '2023-11-19 01:37:02'
- Battery Level (%): 19.9
  Device ID: device-0045
  Device Type: Light Sensor
  Location: Hallway
  Reading Value: 52.22
  Timestamp: '2021-08-13 08:30:35'
- Battery Level (%): 49.6
  Device ID: device-0038
  Device Type: Humidity Sensor
  Location: Kitchen
  Reading Value: 41.27
  Timestamp: '2022-06-04 23:18:54'
- Battery Level (%): 71.4
  Device ID: device-0083
  Device Type: Temperature Sensor
  Location: Living Room
  Reading Value: -18.07
  Timestamp: '2021-05-19 21:01:52'
- Battery Level (%): 66.7
  Device ID: device-0057
  Device Type: Temperature Sensor
  Location: Hallway
  Reading Value: 35.22
  Timestamp: '2023-06-16 10:36:15'
- Battery Level (%): 73.1
  Device ID: device-0092
  Device Type: Humidity Sensor
  Location: Garage
  Reading Value: 53.01
  Timestamp: '2023-10-09 00:22:43'
- Battery Level (%): 33.9
  Device ID: device-0021
  Device Type: Temperature Sensor
  Location: Hallway
  Reading Value: 60.55
  Timestamp: '2021-04-28 10:40:05'
- Battery Level (%): 70.5
  Device ID: device-0090
  Device Type: Light Sensor
  Location: Bathroom
  Reading Value: 65.67
  Timestamp: '2021-02-03 19:58:42'
- Battery Level (%): 21.6
  Device ID: device-0002
  Device Type: Temperature Sensor
  Location: Hallway
  Reading Value: 32.32
  Timestamp: '2022-10-17 20:09:28'
<end>Convert this YAML to Json:
- Cuisine: Chinese
  Location: Phoenix
  Price Range: $$
  Rating: 2
  Restaurant Name: Pasta Palace
- Cuisine: Indian
  Location: New York
  Price Range: $$
  Rating: 4
  Restaurant Name: Curry Corner
- Cuisine: Chinese
  Location: Phoenix
  Price Range: $$
  Rating: 2
  Restaurant Name: BBQ Barn
- Cuisine: Chinese
  Location: Phoenix
  Price Range: $$$$
  Rating: 2
  Restaurant Name: Pizza Planet
- Cuisine: Mediterranean
  Location: Phoenix
  Price Range: $
  Rating: 3
  Restaurant Name: The Steakhouse
<start>
[
    {
        "Restaurant Name": "Pasta Palace",
        "Cuisine": "Chinese",
        "Location": "Phoenix",
        "Rating": 2,
        "Price Range": "$$"
    },
    {
        "Restaurant Name": "Curry Corner",
        "Cuisine": "Indian",
        "Location": "New York",
        "Rating": 4,
        "Price Range": "$$"
    },
    {
        "Restaurant Name": "BBQ Barn",
        "Cuisine": "Chinese",
        "Location": "Phoenix",
        "Rating": 2,
        "Price Range": "$$"
    },
    {
        "Restaurant Name": "Pizza Planet",
        "Cuisine": "Chinese",
        "Location": "Phoenix",
        "Rating": 2,
        "Price Range": "$$$$"
    },
    {
        "Restaurant Name": "The Steakhouse",
        "Cuisine": "Mediterranean",
        "Location": "Phoenix",
        "Rating": 3,
        "Price Range": "$"
    }
]
<end>Here's some Yaml data, can you convert it to Csv?
- Company: HealthPlus
  Market Cap: Small Cap
  Stock Price: 375.37
- Company: GlobalTrade
  Market Cap: Mega Cap
  Stock Price: 933.85
- Company: GlobalTrade
  Market Cap: Mid Cap
  Stock Price: 440.18
- Company: EcoEnergy
  Market Cap: Mid Cap
  Stock Price: 989.54
- Company: Foodies
  Market Cap: Mid Cap
  Stock Price: 552.33
- Company: RetailHub
  Market Cap: Mega Cap
  Stock Price: 28.94
- Company: RetailHub
  Market Cap: Mega Cap
  Stock Price: 601.47
- Company: AutoDrive
  Market Cap: Mid Cap
  Stock Price: 989.54
- Company: HealthPlus
  Market Cap: Mega Cap
  Stock Price: 991.22
- Company: AutoDrive
  Market Cap: Mid Cap
  Stock Price: 262.45
<start>
Company,Market Cap,Stock Price
HealthPlus,Small Cap,375.37
GlobalTrade,Mega Cap,933.85
GlobalTrade,Mid Cap,440.18
EcoEnergy,Mid Cap,989.54
Foodies,Mid Cap,552.33
RetailHub,Mega Cap,28.94
RetailHub,Mega Cap,601.47
AutoDrive,Mid Cap,989.54
HealthPlus,Mega Cap,991.22
AutoDrive,Mid Cap,262.45
<end>Convert this json to csv:
[
    {
        "Trip Name": "Historic Route",
        "Start Location": "Miami",
        "End Location": "New York",
        "Distance (miles)": 1500.1,
        "Duration (hours)": 44.6,
        "Fuel Used (gallons)": 47.7
    },
    {
        "Trip Name": "Mountain Adventure",
        "Start Location": "Miami",
        "End Location": "Phoenix",
        "Distance (miles)": 1298.1,
        "Duration (hours)": 46.1,
        "Fuel Used (gallons)": 49.2
    },
    {
        "Trip Name": "Coast to Coast",
        "Start Location": "Miami",
        "End Location": "Chicago",
        "Distance (miles)": 1318.8,
        "Duration (hours)": 55.7,
        "Fuel Used (gallons)": 90.5
    },
    {
        "Trip Name": "Lakeside Retreat",
        "Start Location": "Chicago",
        "End Location": "Houston",
        "Distance (miles)": 2390.3,
        "Duration (hours)": 44.6,
        "Fuel Used (gallons)": 19.4
    },
    {
        "Trip Name": "Mountain Adventure",
        "Start Location": "Denver",
        "End Location": "Chicago",
        "Distance (miles)": 944.0,
        "Duration (hours)": 31.1,
        "Fuel Used (gallons)": 56.6
    },
    {
        "Trip Name": "Desert Drive",
        "Start Location": "Miami",
        "End Location": "Los Angeles",
        "Distance (miles)": 1148.4,
        "Duration (hours)": 34.7,
        "Fuel Used (gallons)": 58.6
    }
]<start>
Trip Name,Start Location,End Location,Distance (miles),Duration (hours),Fuel Used (gallons)
Historic Route,Miami,New York,1500.1,44.6,47.7
Mountain Adventure,Miami,Phoenix,1298.1,46.1,49.2
Coast to Coast,Miami,Chicago,1318.8,55.7,90.5
Lakeside Retreat,Chicago,Houston,2390.3,44.6,19.4
Mountain Adventure,Denver,Chicago,944.0,31.1,56.6
Desert Drive,Miami,Los Angeles,1148.4,34.7,58.6
<end>Convert this markdown to Csv:
| Title | Author | Rating |
| --- | --- | --- |
| Whispers of the Abyss | Rowan Ashborne | 4.7 |
| Shadows of Solitude | Orion Frostblade | 1.9 |
| The Crystal Key | Luna Silverleaf | 1.9 |
| Shadows of Solitude | Elara Moonshadow | 3.3 |
| Echoes of Eternity | Elara Moonshadow | 4.0 |
| The Crystal Key | Galen Starfire | 2.4 |
| Legends of the Rift | Thorne Ironwood | 1.8 |
| Whispers of the Abyss | Luna Silverleaf | 4.2 |<start>
Title,Author,Rating
Whispers of the Abyss,Rowan Ashborne,4.7
Shadows of Solitude,Orion Frostblade,1.9
The Crystal Key,Luna Silverleaf,1.9
Shadows of Solitude,Elara Moonshadow,3.3
Echoes of Eternity,Elara Moonshadow,4.0
The Crystal Key,Galen Starfire,2.4
Legends of the Rift,Thorne Ironwood,1.8
Whispers of the Abyss,Luna Silverleaf,4.2
<end>Here's some markdown data, can you convert it to plain text?
| Title | Author | Genre | Publication Year | Rating |
| --- | --- | --- | --- | --- |
| Shadows of Solitude | Luna Silverleaf | Thriller | 1952 | 2.7 |
| The Last Sky | Thorne Ironwood | Mystery | 1960 | 1.3 |
| Shadows of Solitude | Isla Windrider | Mystery | 2021 | 2.5 |
| Echoes of Eternity | Thorne Ironwood | Thriller | 2005 | 3.2 |
| Shadows of Solitude | Galen Starfire | Non-Fiction | 1953 | 2.3 |
| Shadows of Solitude | Galen Starfire | Fantasy | 1967 | 1.6 |
| A Journey Through Time | Thorne Ironwood | Fantasy | 1951 | 1.0 |
| The Last Sky | Luna Silverleaf | Thriller | 2012 | 2.5 |<start>
Title: Shadows of Solitude | Author: Luna Silverleaf | Genre: Thriller | Publication Year: 1952 | Rating: 2.7
Title: The Last Sky | Author: Thorne Ironwood | Genre: Mystery | Publication Year: 1960 | Rating: 1.3
Title: Shadows of Solitude | Author: Isla Windrider | Genre: Mystery | Publication Year: 2021 | Rating: 2.5
Title: Echoes of Eternity | Author: Thorne Ironwood | Genre: Thriller | Publication Year: 2005 | Rating: 3.2
Title: Shadows of Solitude | Author: Galen Starfire | Genre: Non-Fiction | Publication Year: 1953 | Rating: 2.3
Title: Shadows of Solitude | Author: Galen Starfire | Genre: Fantasy | Publication Year: 1967 | Rating: 1.6
Title: A Journey Through Time | Author: Thorne Ironwood | Genre: Fantasy | Publication Year: 1951 | Rating: 1.0
Title: The Last Sky | Author: Luna Silverleaf | Genre: Thriller | Publication Year: 2012 | Rating: 2.5
<end>Can you change this YML into MARKDOWN?
- Birth Month: February
  City: Denver
- Birth Month: March
  City: Detroit
- Birth Month: March
  City: Denver
- Birth Month: November
  City: Memphis
- Birth Month: February
  City: Oklahoma City
- Birth Month: August
  City: Charlotte
- Birth Month: July
  City: Jacksonville
- Birth Month: March
  City: Houston
- Birth Month: February
  City: San Jose
<start>
| Birth Month | City |
| --- | --- |
| February | Denver |
| March | Detroit |
| March | Denver |
| November | Memphis |
| February | Oklahoma City |
| August | Charlotte |
| July | Jacksonville |
| March | Houston |
| February | San Jose |
<end>Can you change this PLAIN TEXT into MARKDOWN?
Location: Phoenix | Rating: 1
Location: New York | Rating: 2
Location: Los Angeles | Rating: 5
Location: Miami | Rating: 1
Location: Miami | Rating: 5
Location: Los Angeles | Rating: 2
Location: New York | Rating: 2
<start>
| Location | Rating |
| --- | --- |
| Phoenix | 1 |
| New York | 2 |
| Los Angeles | 5 |
| Miami | 1 |
| Miami | 5 |
| Los Angeles | 2 |
| New York | 2 |
<end>Please transform the following Yml data into json:
- Director: Lira Silverleaf
  Release Year: 2008
- Director: Aria Ravenwood
  Release Year: 2016
- Director: Lira Silverleaf
  Release Year: 2018
<start>
[
    {
        "Director": "Lira Silverleaf",
        "Release Year": 2008
    },
    {
        "Director": "Aria Ravenwood",
        "Release Year": 2016
    },
    {
        "Director": "Lira Silverleaf",
        "Release Year": 2018
    }
]
<end>Can you change this Csv into yml?
Database Name,Queries per Second,Cache Hit Ratio (%)
ProfilesDB,3990.64,71.93
MetricsDB,4510.21,80.2
InventoryDB,2169.97,77.78
ProfilesDB,1814.76,89.87
ProductsDB,3294.54,75.25
UserDB,4510.21,77.34
SalesDB,3107.73,93.11
OrdersDB,4142.33,80.2
<start>
- Cache Hit Ratio (%): 71.93
  Database Name: ProfilesDB
  Queries per Second: 3990.64
- Cache Hit Ratio (%): 80.2
  Database Name: MetricsDB
  Queries per Second: 4510.21
- Cache Hit Ratio (%): 77.78
  Database Name: InventoryDB
  Queries per Second: 2169.97
- Cache Hit Ratio (%): 89.87
  Database Name: ProfilesDB
  Queries per Second: 1814.76
- Cache Hit Ratio (%): 75.25
  Database Name: ProductsDB
  Queries per Second: 3294.54
- Cache Hit Ratio (%): 77.34
  Database Name: UserDB
  Queries per Second: 4510.21
- Cache Hit Ratio (%): 93.11
  Database Name: SalesDB
  Queries per Second: 3107.73
- Cache Hit Ratio (%): 80.2
  Database Name: OrdersDB
  Queries per Second: 4142.33
<end>Here's some Yml data, can you convert it to markdown?
- Release Year: 2001
  Title: Edge of Infinity
- Release Year: 1985
  Title: Beyond the Veil
- Release Year: 1982
  Title: Escape from Earth
- Release Year: 2015
  Title: The Endless Horizon
- Release Year: 2000
  Title: The Final Voyage
- Release Year: 1979
  Title: The Great Expedition
- Release Year: 1978
  Title: Starbound Odyssey
- Release Year: 1986
  Title: Starbound Odyssey
- Release Year: 1994
  Title: Edge of Infinity
- Release Year: 2009
  Title: Dreamwalker
<start>
| Title | Release Year |
| --- | --- |
| Edge of Infinity | 2001 |
| Beyond the Veil | 1985 |
| Escape from Earth | 1982 |
| The Endless Horizon | 2015 |
| The Final Voyage | 2000 |
| The Great Expedition | 1979 |
| Starbound Odyssey | 1978 |
| Starbound Odyssey | 1986 |
| Edge of Infinity | 1994 |
| Dreamwalker | 2009 |
<end>Transform this csv structure to a Yaml format:
Product Name,SKU,Price,Stock Quantity,Supplier Name
Device,SKU-1010,387.18,126,Wonka Industries
Device,SKU-1028,255.92,424,Wayne Enterprises
Gadget,SKU-1038,163.66,479,ACME Corp
Gizmo,SKU-1094,459.0,131,Umbrella Corp
Contraption,SKU-1067,344.65,269,Umbrella Corp
Contraption,SKU-1027,316.64,199,Umbrella Corp
Widget,SKU-1084,473.29,175,Wayne Enterprises
<start>
- Price: 387.18
  Product Name: Device
  SKU: SKU-1010
  Stock Quantity: 126
  Supplier Name: Wonka Industries
- Price: 255.92
  Product Name: Device
  SKU: SKU-1028
  Stock Quantity: 424
  Supplier Name: Wayne Enterprises
- Price: 163.66
  Product Name: Gadget
  SKU: SKU-1038
  Stock Quantity: 479
  Supplier Name: ACME Corp
- Price: 459.0
  Product Name: Gizmo
  SKU: SKU-1094
  Stock Quantity: 131
  Supplier Name: Umbrella Corp
- Price: 344.65
  Product Name: Contraption
  SKU: SKU-1067
  Stock Quantity: 269
  Supplier Name: Umbrella Corp
- Price: 316.64
  Product Name: Contraption
  SKU: SKU-1027
  Stock Quantity: 199
  Supplier Name: Umbrella Corp
- Price: 473.29
  Product Name: Widget
  SKU: SKU-1084
  Stock Quantity: 175
  Supplier Name: Wayne Enterprises
<end>Convert this json to Plain text:
[
    {
        "Product Name": "Doohickey",
        "SKU": "SKU-1017",
        "Price": 108.99,
        "Stock Quantity": 60,
        "Category": "Automotive",
        "Supplier Name": "Umbrella Corp"
    },
    {
        "Product Name": "Thingamajig",
        "SKU": "SKU-1086",
        "Price": 431.97,
        "Stock Quantity": 259,
        "Category": "Sports",
        "Supplier Name": "Wayne Enterprises"
    },
    {
        "Product Name": "Gadget",
        "SKU": "SKU-1053",
        "Price": 402.74,
        "Stock Quantity": 145,
        "Category": "Electronics",
        "Supplier Name": "Wonka Industries"
    },
    {
        "Product Name": "Whatchamacallit",
        "SKU": "SKU-1090",
        "Price": 290.15,
        "Stock Quantity": 335,
        "Category": "Automotive",
        "Supplier Name": "Wayne Enterprises"
    },
    {
        "Product Name": "Whatchamacallit",
        "SKU": "SKU-1006",
        "Price": 365.05,
        "Stock Quantity": 160,
        "Category": "Electronics",
        "Supplier Name": "ACME Corp"
    },
    {
        "Product Name": "Device",
        "SKU": "SKU-1035",
        "Price": 315.31,
        "Stock Quantity": 370,
        "Category": "Sports",
        "Supplier Name": "Wayne Enterprises"
    },
    {
        "Product Name": "Device",
        "SKU": "SKU-1096",
        "Price": 448.88,
        "Stock Quantity": 450,
        "Category": "Electronics",
        "Supplier Name": "Wayne Enterprises"
    }
]<start>
Product Name: Doohickey | SKU: SKU-1017 | Price: 108.99 | Stock Quantity: 60 | Category: Automotive | Supplier Name: Umbrella Corp
Product Name: Thingamajig | SKU: SKU-1086 | Price: 431.97 | Stock Quantity: 259 | Category: Sports | Supplier Name: Wayne Enterprises
Product Name: Gadget | SKU: SKU-1053 | Price: 402.74 | Stock Quantity: 145 | Category: Electronics | Supplier Name: Wonka Industries
Product Name: Whatchamacallit | SKU: SKU-1090 | Price: 290.15 | Stock Quantity: 335 | Category: Automotive | Supplier Name: Wayne Enterprises
Product Name: Whatchamacallit | SKU: SKU-1006 | Price: 365.05 | Stock Quantity: 160 | Category: Electronics | Supplier Name: ACME Corp
Product Name: Device | SKU: SKU-1035 | Price: 315.31 | Stock Quantity: 370 | Category: Sports | Supplier Name: Wayne Enterprises
Product Name: Device | SKU: SKU-1096 | Price: 448.88 | Stock Quantity: 450 | Category: Electronics | Supplier Name: Wayne Enterprises
<end>Can you change this YML into markdown?
- Box Office Earnings (M): 581.87
  Genre: Thriller
  Release Year: 1982
  Title: Rise of the Titans
- Box Office Earnings (M): 665.57
  Genre: Horror
  Release Year: 1984
  Title: The Endless Horizon
- Box Office Earnings (M): 665.57
  Genre: Comedy
  Release Year: 1981
  Title: Edge of Infinity
- Box Office Earnings (M): 452.68
  Genre: Drama
  Release Year: 2003
  Title: Dreamwalker
- Box Office Earnings (M): 903.0
  Genre: Sci-Fi
  Release Year: 2009
  Title: Dreamwalker
- Box Office Earnings (M): 509.67
  Genre: Drama
  Release Year: 1973
  Title: Mystery of the Depths
- Box Office Earnings (M): 726.72
  Genre: Drama
  Release Year: 2006
  Title: The Final Voyage
- Box Office Earnings (M): 779.02
  Genre: Fantasy
  Release Year: 2020
  Title: Starbound Odyssey
<start>
| Title | Genre | Release Year | Box Office Earnings (M) |
| --- | --- | --- | --- |
| Rise of the Titans | Thriller | 1982 | 581.87 |
| The Endless Horizon | Horror | 1984 | 665.57 |
| Edge of Infinity | Comedy | 1981 | 665.57 |
| Dreamwalker | Drama | 2003 | 452.68 |
| Dreamwalker | Sci-Fi | 2009 | 903.0 |
| Mystery of the Depths | Drama | 1973 | 509.67 |
| The Final Voyage | Drama | 2006 | 726.72 |
| Starbound Odyssey | Fantasy | 2020 | 779.02 |
<end>Can you change this yaml into markdown?
- Cuisine: Italian
  Price Range: $$
  Restaurant Name: Taco Town
- Cuisine: Mediterranean
  Price Range: $$
  Restaurant Name: Sushi World
- Cuisine: Japanese
  Price Range: $
  Restaurant Name: BBQ Barn
- Cuisine: Mexican
  Price Range: $$$
  Restaurant Name: Curry Corner
- Cuisine: Mediterranean
  Price Range: $$$$
  Restaurant Name: The Steakhouse
- Cuisine: American
  Price Range: $$$
  Restaurant Name: Sushi World
- Cuisine: American
  Price Range: $$$$$
  Restaurant Name: Vegan Delight
- Cuisine: Chinese
  Price Range: $$
  Restaurant Name: Burger Haven
- Cuisine: Mediterranean
  Price Range: $$$$$
  Restaurant Name: Vegan Delight
<start>
| Restaurant Name | Cuisine | Price Range |
| --- | --- | --- |
| Taco Town | Italian | $$ |
| Sushi World | Mediterranean | $$ |
| BBQ Barn | Japanese | $ |
| Curry Corner | Mexican | $$$ |
| The Steakhouse | Mediterranean | $$$$ |
| Sushi World | American | $$$ |
| Vegan Delight | American | $$$$$ |
| Burger Haven | Chinese | $$ |
| Vegan Delight | Mediterranean | $$$$$ |
<end>Can you change this markdown into Plain text?
| Location | Temperature (C) | Humidity (%) | Day |
| --- | --- | --- | --- |
| Seattle | 11.1 | 36 | Saturday |
| Phoenix | 38.1 | 78 | Thursday |
| Miami | 33.0 | 77 | Monday |
| Houston | 33.2 | 78 | Sunday |
| Seattle | 9.7 | 78 | Friday |
| Houston | 31.7 | 69 | Friday |
| Miami | 38.4 | 79 | Monday |<start>
Location: Seattle | Temperature (C): 11.1 | Humidity (%): 36 | Day: Saturday
Location: Phoenix | Temperature (C): 38.1 | Humidity (%): 78 | Day: Thursday
Location: Miami | Temperature (C): 33.0 | Humidity (%): 77 | Day: Monday
Location: Houston | Temperature (C): 33.2 | Humidity (%): 78 | Day: Sunday
Location: Seattle | Temperature (C): 9.7 | Humidity (%): 78 | Day: Friday
Location: Houston | Temperature (C): 31.7 | Humidity (%): 69 | Day: Friday
Location: Miami | Temperature (C): 38.4 | Humidity (%): 79 | Day: Monday
<end>Please transform the following Json data into csv:
[
    {
        "Title": "Echoes of Eternity",
        "Genre": "Horror",
        "Publication Year": 2006,
        "Rating": 2.7
    },
    {
        "Title": "Legends of the Rift",
        "Genre": "Non-Fiction",
        "Publication Year": 1977,
        "Rating": 3.1
    },
    {
        "Title": "Legends of the Rift",
        "Genre": "Mystery",
        "Publication Year": 1957,
        "Rating": 2.0
    },
    {
        "Title": "Echoes of Eternity",
        "Genre": "Non-Fiction",
        "Publication Year": 2011,
        "Rating": 1.5
    },
    {
        "Title": "Tales of the Brave",
        "Genre": "Science Fiction",
        "Publication Year": 1967,
        "Rating": 1.9
    },
    {
        "Title": "The Crystal Key",
        "Genre": "Science Fiction",
        "Publication Year": 1975,
        "Rating": 1.8
    },
    {
        "Title": "The Last Sky",
        "Genre": "Mystery",
        "Publication Year": 1950,
        "Rating": 2.9
    }
]<start>
Title,Genre,Publication Year,Rating
Echoes of Eternity,Horror,2006,2.7
Legends of the Rift,Non-Fiction,1977,3.1
Legends of the Rift,Mystery,1957,2.0
Echoes of Eternity,Non-Fiction,2011,1.5
Tales of the Brave,Science Fiction,1967,1.9
The Crystal Key,Science Fiction,1975,1.8
The Last Sky,Mystery,1950,2.9
<end>Transform this Csv structure to a YML format:
Location,Condition,Temperature (C),Humidity (%),Wind Speed (km/h),Day
Houston,Cloudy,21.6,56,22.6,Wednesday
Miami,Cloudy,12.1,50,16.4,Tuesday
Denver,Windy,23.3,83,1.4,Tuesday
Miami,Stormy,9.5,24,8.5,Tuesday
Houston,Snowy,21.6,92,16.0,Wednesday
New York,Snowy,18.8,66,3.8,Tuesday
New York,Snowy,-8.9,40,28.5,Tuesday
Phoenix,Windy,26.9,61,16.3,Sunday
<start>
- Condition: Cloudy
  Day: Wednesday
  Humidity (%): 56
  Location: Houston
  Temperature (C): 21.6
  Wind Speed (km/h): 22.6
- Condition: Cloudy
  Day: Tuesday
  Humidity (%): 50
  Location: Miami
  Temperature (C): 12.1
  Wind Speed (km/h): 16.4
- Condition: Windy
  Day: Tuesday
  Humidity (%): 83
  Location: Denver
  Temperature (C): 23.3
  Wind Speed (km/h): 1.4
- Condition: Stormy
  Day: Tuesday
  Humidity (%): 24
  Location: Miami
  Temperature (C): 9.5
  Wind Speed (km/h): 8.5
- Condition: Snowy
  Day: Wednesday
  Humidity (%): 92
  Location: Houston
  Temperature (C): 21.6
  Wind Speed (km/h): 16.0
- Condition: Snowy
  Day: Tuesday
  Humidity (%): 66
  Location: New York
  Temperature (C): 18.8
  Wind Speed (km/h): 3.8
- Condition: Snowy
  Day: Tuesday
  Humidity (%): 40
  Location: New York
  Temperature (C): -8.9
  Wind Speed (km/h): 28.5
- Condition: Windy
  Day: Sunday
  Humidity (%): 61
  Location: Phoenix
  Temperature (C): 26.9
  Wind Speed (km/h): 16.3
<end>Can you change this JSON into plain text?
[
    {
        "Location": "Los Angeles",
        "Condition": "Sunny",
        "Humidity (%)": 56
    },
    {
        "Location": "Denver",
        "Condition": "Windy",
        "Humidity (%)": 70
    },
    {
        "Location": "Phoenix",
        "Condition": "Windy",
        "Humidity (%)": 66
    },
    {
        "Location": "Seattle",
        "Condition": "Stormy",
        "Humidity (%)": 22
    },
    {
        "Location": "Miami",
        "Condition": "Cloudy",
        "Humidity (%)": 78
    },
    {
        "Location": "New York",
        "Condition": "Foggy",
        "Humidity (%)": 73
    },
    {
        "Location": "Phoenix",
        "Condition": "Rainy",
        "Humidity (%)": 32
    },
    {
        "Location": "Seattle",
        "Condition": "Rainy",
        "Humidity (%)": 33
    },
    {
        "Location": "Los Angeles",
        "Condition": "Sunny",
        "Humidity (%)": 69
    }
]<start>
Location: Los Angeles | Condition: Sunny | Humidity (%): 56
Location: Denver | Condition: Windy | Humidity (%): 70
Location: Phoenix | Condition: Windy | Humidity (%): 66
Location: Seattle | Condition: Stormy | Humidity (%): 22
Location: Miami | Condition: Cloudy | Humidity (%): 78
Location: New York | Condition: Foggy | Humidity (%): 73
Location: Phoenix | Condition: Rainy | Humidity (%): 32
Location: Seattle | Condition: Rainy | Humidity (%): 33
Location: Los Angeles | Condition: Sunny | Humidity (%): 69
<end>Can you change this Json into csv?
[
    {
        "Cache Hit Ratio (%)": 91.23,
        "Average Latency (ms)": 37.27,
        "Timestamp": "2022-08-27 04:39:53"
    },
    {
        "Cache Hit Ratio (%)": 86.86,
        "Average Latency (ms)": 43.04,
        "Timestamp": "2023-02-24 15:08:21"
    },
    {
        "Cache Hit Ratio (%)": 78.56,
        "Average Latency (ms)": 75.53,
        "Timestamp": "2023-03-01 19:44:47"
    },
    {
        "Cache Hit Ratio (%)": 81.86,
        "Average Latency (ms)": 43.42,
        "Timestamp": "2021-02-09 00:46:30"
    },
    {
        "Cache Hit Ratio (%)": 95.41,
        "Average Latency (ms)": 2.54,
        "Timestamp": "2021-08-25 21:54:01"
    },
    {
        "Cache Hit Ratio (%)": 74.34,
        "Average Latency (ms)": 40.12,
        "Timestamp": "2021-12-13 23:19:31"
    },
    {
        "Cache Hit Ratio (%)": 79.79,
        "Average Latency (ms)": 5.66,
        "Timestamp": "2022-01-05 04:01:04"
    },
    {
        "Cache Hit Ratio (%)": 88.39,
        "Average Latency (ms)": 86.9,
        "Timestamp": "2023-07-19 16:00:38"
    }
]<start>
Cache Hit Ratio (%),Average Latency (ms),Timestamp
91.23,37.27,2022-08-27 04:39:53
86.86,43.04,2023-02-24 15:08:21
78.56,75.53,2023-03-01 19:44:47
81.86,43.42,2021-02-09 00:46:30
95.41,2.54,2021-08-25 21:54:01
74.34,40.12,2021-12-13 23:19:31
79.79,5.66,2022-01-05 04:01:04
88.39,86.9,2023-07-19 16:00:38
<end>Here's some csv data, can you convert it to JSON?
Trip Name,Start Location,End Location,Distance (miles),Duration (hours),Fuel Used (gallons)
Canyon Trek,Los Angeles,Miami,2716.0,25.1,61.4
Mountain Adventure,Houston,Miami,2206.6,1.4,36.3
Forest Journey,Houston,Chicago,2919.4,60.9,64.0
Coast to Coast,San Francisco,Los Angeles,2250.0,38.3,69.5
<start>
[
    {
        "Trip Name": "Canyon Trek",
        "Start Location": "Los Angeles",
        "End Location": "Miami",
        "Distance (miles)": 2716.0,
        "Duration (hours)": 25.1,
        "Fuel Used (gallons)": 61.4
    },
    {
        "Trip Name": "Mountain Adventure",
        "Start Location": "Houston",
        "End Location": "Miami",
        "Distance (miles)": 2206.6,
        "Duration (hours)": 1.4,
        "Fuel Used (gallons)": 36.3
    },
    {
        "Trip Name": "Forest Journey",
        "Start Location": "Houston",
        "End Location": "Chicago",
        "Distance (miles)": 2919.4,
        "Duration (hours)": 60.9,
        "Fuel Used (gallons)": 64.0
    },
    {
        "Trip Name": "Coast to Coast",
        "Start Location": "San Francisco",
        "End Location": "Los Angeles",
        "Distance (miles)": 2250.0,
        "Duration (hours)": 38.3,
        "Fuel Used (gallons)": 69.5
    }
]
<end>Please transform the following json data into markdown:
[
    {
        "Location": "Denver",
        "Condition": "Stormy",
        "Temperature (C)": 15.8,
        "Day": "Tuesday"
    },
    {
        "Location": "Miami",
        "Condition": "Windy",
        "Temperature (C)": 17.6,
        "Day": "Tuesday"
    },
    {
        "Location": "Los Angeles",
        "Condition": "Cloudy",
        "Temperature (C)": 0.9,
        "Day": "Tuesday"
    },
    {
        "Location": "Los Angeles",
        "Condition": "Rainy",
        "Temperature (C)": 16.7,
        "Day": "Sunday"
    },
    {
        "Location": "Denver",
        "Condition": "Windy",
        "Temperature (C)": 3.1,
        "Day": "Saturday"
    },
    {
        "Location": "Chicago",
        "Condition": "Stormy",
        "Temperature (C)": -2.7,
        "Day": "Tuesday"
    }
]<start>
| Location | Condition | Temperature (C) | Day |
| --- | --- | --- | --- |
| Denver | Stormy | 15.8 | Tuesday |
| Miami | Windy | 17.6 | Tuesday |
| Los Angeles | Cloudy | 0.9 | Tuesday |
| Los Angeles | Rainy | 16.7 | Sunday |
| Denver | Windy | 3.1 | Saturday |
| Chicago | Stormy | -2.7 | Tuesday |
<end>Can you change this markdown into CSV?
| Age | City | Income |
| --- | --- | --- |
| 37 | Chicago | 490000 |
| 53 | Jacksonville | 240000 |
| 67 | Detroit | 160000 |
| 38 | El Paso | 410000 |
| 43 | Indianapolis | 285000 |
| 28 | Fort Worth | 490000 |
| 31 | Detroit | 440000 |<start>
Age,City,Income
37,Chicago,490000
53,Jacksonville,240000
67,Detroit,160000
38,El Paso,410000
43,Indianapolis,285000
28,Fort Worth,490000
31,Detroit,440000
<end>Here's some yaml data, can you convert it to plain text?
- Distance (miles): 182.8
  Duration (hours): 11.5
  End Location: Phoenix
  Fuel Used (gallons): 17.4
  Trip Name: Valley Voyage
- Distance (miles): 2208.2
  Duration (hours): 66.1
  End Location: Denver
  Fuel Used (gallons): 35.5
  Trip Name: City Explorer
- Distance (miles): 197.4
  Duration (hours): 20.1
  End Location: Denver
  Fuel Used (gallons): 90.2
  Trip Name: Mountain Adventure
- Distance (miles): 942.9
  Duration (hours): 26.8
  End Location: San Francisco
  Fuel Used (gallons): 28.6
  Trip Name: Canyon Trek
- Distance (miles): 846.4
  Duration (hours): 53.4
  End Location: Phoenix
  Fuel Used (gallons): 97.9
  Trip Name: Lakeside Retreat
<start>
Trip Name: Valley Voyage | End Location: Phoenix | Distance (miles): 182.8 | Duration (hours): 11.5 | Fuel Used (gallons): 17.4
Trip Name: City Explorer | End Location: Denver | Distance (miles): 2208.2 | Duration (hours): 66.1 | Fuel Used (gallons): 35.5
Trip Name: Mountain Adventure | End Location: Denver | Distance (miles): 197.4 | Duration (hours): 20.1 | Fuel Used (gallons): 90.2
Trip Name: Canyon Trek | End Location: San Francisco | Distance (miles): 942.9 | Duration (hours): 26.8 | Fuel Used (gallons): 28.6
Trip Name: Lakeside Retreat | End Location: Phoenix | Distance (miles): 846.4 | Duration (hours): 53.4 | Fuel Used (gallons): 97.9
<end>Convert this Json to csv:
[
    {
        "Author": "Kara Firebrand",
        "Publication Year": 1997,
        "Rating": 2.1
    },
    {
        "Author": "Isla Windrider",
        "Publication Year": 1986,
        "Rating": 4.3
    },
    {
        "Author": "Rowan Ashborne",
        "Publication Year": 2011,
        "Rating": 4.3
    },
    {
        "Author": "Elara Moonshadow",
        "Publication Year": 1973,
        "Rating": 4.8
    },
    {
        "Author": "Rowan Ashborne",
        "Publication Year": 2008,
        "Rating": 2.4
    },
    {
        "Author": "Isla Windrider",
        "Publication Year": 1956,
        "Rating": 3.9
    },
    {
        "Author": "Draven Blackthorn",
        "Publication Year": 1953,
        "Rating": 2.9
    },
    {
        "Author": "Luna Silverleaf",
        "Publication Year": 1987,
        "Rating": 2.5
    },
    {
        "Author": "Thorne Ironwood",
        "Publication Year": 1989,
        "Rating": 3.9
    }
]<start>
Author,Publication Year,Rating
Kara Firebrand,1997,2.1
Isla Windrider,1986,4.3
Rowan Ashborne,2011,4.3
Elara Moonshadow,1973,4.8
Rowan Ashborne,2008,2.4
Isla Windrider,1956,3.9
Draven Blackthorn,1953,2.9
Luna Silverleaf,1987,2.5
Thorne Ironwood,1989,3.9
<end>Transform this MARKDOWN structure to a yaml format:
| Age | City | Income |
| --- | --- | --- |
| 63 | San Jose | 365000 |
| 23 | Louisville | 185000 |
| 32 | El Paso | 265000 |
| 39 | Milwaukee | 205000 |
| 56 | Austin | 70000 |
| 61 | San Antonio | 140000 |<start>
- Age: 63
  City: San Jose
  Income: 365000
- Age: 23
  City: Louisville
  Income: 185000
- Age: 32
  City: El Paso
  Income: 265000
- Age: 39
  City: Milwaukee
  Income: 205000
- Age: 56
  City: Austin
  Income: 70000
- Age: 61
  City: San Antonio
  Income: 140000
<end>Convert this Yaml to csv:
- Company: FoodChain
  High Price: 1480.94
  Low Price: 814.89
  Open Price: 1480.94
- Company: AutoMotive
  High Price: 1022.1
  Low Price: 178.83
  Open Price: 178.83
- Company: AutoMotive
  High Price: 1246.87
  Low Price: 350.52
  Open Price: 1246.87
- Company: TechnoCorp
  High Price: 1102.81
  Low Price: 698.38
  Open Price: 1102.81
- Company: FoodChain
  High Price: 1421.56
  Low Price: 560.1
  Open Price: 1406.81
- Company: TechnoCorp
  High Price: 1463.23
  Low Price: 133.81
  Open Price: 1463.23
- Company: BioLife
  High Price: 1367.89
  Low Price: 704.06
  Open Price: 1003.18
- Company: AutoMotive
  High Price: 576.01
  Low Price: 531.4
  Open Price: 531.4
<start>
Company,Open Price,High Price,Low Price
FoodChain,1480.94,1480.94,814.89
AutoMotive,178.83,1022.1,178.83
AutoMotive,1246.87,1246.87,350.52
TechnoCorp,1102.81,1102.81,698.38
FoodChain,1406.81,1421.56,560.1
TechnoCorp,1463.23,1463.23,133.81
BioLife,1003.18,1367.89,704.06
AutoMotive,531.4,576.01,531.4
<end>Can you change this markdown into Json?
| Restaurant Name | Cuisine | Location | Rating | Price Range |
| --- | --- | --- | --- | --- |
| Curry Corner | American | Houston | 3 | $$ |
| The Steakhouse | Japanese | San Francisco | 1 | $ |
| Pasta Palace | Indian | Phoenix | 3 | $$ |
| Sushi World | Italian | Houston | 4 | $$$ |<start>
[
    {
        "Restaurant Name": "Curry Corner",
        "Cuisine": "American",
        "Location": "Houston",
        "Rating": 3,
        "Price Range": "$$"
    },
    {
        "Restaurant Name": "The Steakhouse",
        "Cuisine": "Japanese",
        "Location": "San Francisco",
        "Rating": 1,
        "Price Range": "$"
    },
    {
        "Restaurant Name": "Pasta Palace",
        "Cuisine": "Indian",
        "Location": "Phoenix",
        "Rating": 3,
        "Price Range": "$$"
    },
    {
        "Restaurant Name": "Sushi World",
        "Cuisine": "Italian",
        "Location": "Houston",
        "Rating": 4,
        "Price Range": "$$$"
    }
]
<end>Convert this yml to CSV:
- Birth Month: December
  Name: Kate
- Birth Month: February
  Name: Ruby
- Birth Month: February
  Name: Cecil
- Birth Month: October
  Name: Tracie
<start>
Name,Birth Month
Kate,December
Ruby,February
Cecil,February
Tracie,October
<end>Please transform the following Yaml data into CSV:
- Category: Electronics
  Price: 238.1
  Product Name: Contraption
  SKU: SKU-1083
  Stock Quantity: 225
  Supplier Name: ACME Corp
- Category: Household
  Price: 370.35
  Product Name: Gizmo
  SKU: SKU-1065
  Stock Quantity: 383
  Supplier Name: ACME Corp
- Category: Household
  Price: 360.05
  Product Name: Device
  SKU: SKU-1080
  Stock Quantity: 430
  Supplier Name: Umbrella Corp
- Category: Toys
  Price: 6.19
  Product Name: Instrument
  SKU: SKU-1097
  Stock Quantity: 387
  Supplier Name: Umbrella Corp
- Category: Household
  Price: 174.98
  Product Name: Gadget
  SKU: SKU-1053
  Stock Quantity: 465
  Supplier Name: Globex
- Category: Electronics
  Price: 155.36
  Product Name: Gizmo
  SKU: SKU-1069
  Stock Quantity: 301
  Supplier Name: Wayne Enterprises
- Category: Sports
  Price: 141.94
  Product Name: Device
  SKU: SKU-1029
  Stock Quantity: 187
  Supplier Name: ACME Corp
- Category: Automotive
  Price: 19.77
  Product Name: Device
  SKU: SKU-1086
  Stock Quantity: 29
  Supplier Name: Wayne Enterprises
<start>
Product Name,SKU,Price,Stock Quantity,Category,Supplier Name
Contraption,SKU-1083,238.1,225,Electronics,ACME Corp
Gizmo,SKU-1065,370.35,383,Household,ACME Corp
Device,SKU-1080,360.05,430,Household,Umbrella Corp
Instrument,SKU-1097,6.19,387,Toys,Umbrella Corp
Gadget,SKU-1053,174.98,465,Household,Globex
Gizmo,SKU-1069,155.36,301,Electronics,Wayne Enterprises
Device,SKU-1029,141.94,187,Sports,ACME Corp
Device,SKU-1086,19.77,29,Automotive,Wayne Enterprises
<end>Here's some Plain text data, can you convert it to yml?
Company: AutoDrive | Sector: Finance | Market Cap: Large Cap | Stock Price: 963.8 | Annual Revenue (B): 89.41 | Quarter: Q2
Company: RetailHub | Sector: Finance | Market Cap: Small Cap | Stock Price: 542.2 | Annual Revenue (B): 277.22 | Quarter: Q4
Company: AutoDrive | Sector: Energy | Market Cap: Mega Cap | Stock Price: 513.42 | Annual Revenue (B): 257.3 | Quarter: Q3
Company: GlobalTrade | Sector: Energy | Market Cap: Mid Cap | Stock Price: 542.2 | Annual Revenue (B): 159.62 | Quarter: Q4
Company: Foodies | Sector: Biotech | Market Cap: Large Cap | Stock Price: 963.8 | Annual Revenue (B): 156.69 | Quarter: Q2
<start>
- Annual Revenue (B): 89.41
  Company: AutoDrive
  Market Cap: Large Cap
  Quarter: Q2
  Sector: Finance
  Stock Price: 963.8
- Annual Revenue (B): 277.22
  Company: RetailHub
  Market Cap: Small Cap
  Quarter: Q4
  Sector: Finance
  Stock Price: 542.2
- Annual Revenue (B): 257.3
  Company: AutoDrive
  Market Cap: Mega Cap
  Quarter: Q3
  Sector: Energy
  Stock Price: 513.42
- Annual Revenue (B): 159.62
  Company: GlobalTrade
  Market Cap: Mid Cap
  Quarter: Q4
  Sector: Energy
  Stock Price: 542.2
- Annual Revenue (B): 156.69
  Company: Foodies
  Market Cap: Large Cap
  Quarter: Q2
  Sector: Biotech
  Stock Price: 963.8
<end>Can you change this Markdown into PLAIN TEXT?
| Company | Open Price | Close Price | High Price | Low Price | Volume |
| --- | --- | --- | --- | --- | --- |
| AutoMotive | 209.71 | 986.63 | 986.63 | 209.71 | 4796442 |
| FoodChain | 358.83 | 1254.05 | 1254.05 | 358.83 | 9659741 |
| MediaGroup | 1438.37 | 319.41 | 1438.37 | 319.41 | 4629011 |
| GreenEnergy | 1095.01 | 966.37 | 1095.01 | 923.56 | 5929064 |
| HealthGen | 23.22 | 1107.12 | 1184.94 | 23.22 | 7752297 |<start>
Company: AutoMotive | Open Price: 209.71 | Close Price: 986.63 | High Price: 986.63 | Low Price: 209.71 | Volume: 4796442
Company: FoodChain | Open Price: 358.83 | Close Price: 1254.05 | High Price: 1254.05 | Low Price: 358.83 | Volume: 9659741
Company: MediaGroup | Open Price: 1438.37 | Close Price: 319.41 | High Price: 1438.37 | Low Price: 319.41 | Volume: 4629011
Company: GreenEnergy | Open Price: 1095.01 | Close Price: 966.37 | High Price: 1095.01 | Low Price: 923.56 | Volume: 5929064
Company: HealthGen | Open Price: 23.22 | Close Price: 1107.12 | High Price: 1184.94 | Low Price: 23.22 | Volume: 7752297
<end>Convert this MARKDOWN to json:
| Device Type | Battery Level (%) | Reading Value | Timestamp |
| --- | --- | --- | --- |
| Temperature Sensor | 69.1 | 6.37 | 2021-06-19 03:37:17 |
| Motion Detector | 34.1 | -12.02 | 2022-08-02 17:07:32 |
| Pressure Sensor | 54.1 | 2.55 | 2023-09-07 05:26:53 |<start>
[
    {
        "Device Type": "Temperature Sensor",
        "Battery Level (%)": 69.1,
        "Reading Value": 6.37,
        "Timestamp": "2021-06-19 03:37:17"
    },
    {
        "Device Type": "Motion Detector",
        "Battery Level (%)": 34.1,
        "Reading Value": -12.02,
        "Timestamp": "2022-08-02 17:07:32"
    },
    {
        "Device Type": "Pressure Sensor",
        "Battery Level (%)": 54.1,
        "Reading Value": 2.55,
        "Timestamp": "2023-09-07 05:26:53"
    }
]
<end>Please transform the following Yml data into plain text:
- Box Office Earnings (M): 190.52
  Director: Selene Darkwhisper
  Genre: Thriller
  Release Year: 2009
  Title: Mystery of the Depths
- Box Office Earnings (M): 479.95
  Director: Aria Ravenwood
  Genre: Fantasy
  Release Year: 1973
  Title: Mystery of the Depths
- Box Office Earnings (M): 166.46
  Director: Talon Blackthorn
  Genre: Horror
  Release Year: 2010
  Title: Dreamwalker
- Box Office Earnings (M): 166.46
  Director: Aria Ravenwood
  Genre: Adventure
  Release Year: 1980
  Title: Rise of the Titans
<start>
Title: Mystery of the Depths | Director: Selene Darkwhisper | Genre: Thriller | Release Year: 2009 | Box Office Earnings (M): 190.52
Title: Mystery of the Depths | Director: Aria Ravenwood | Genre: Fantasy | Release Year: 1973 | Box Office Earnings (M): 479.95
Title: Dreamwalker | Director: Talon Blackthorn | Genre: Horror | Release Year: 2010 | Box Office Earnings (M): 166.46
Title: Rise of the Titans | Director: Aria Ravenwood | Genre: Adventure | Release Year: 1980 | Box Office Earnings (M): 166.46
<end>Please transform the following markdown data into Json:
| Start Location | Distance (miles) | Duration (hours) | Fuel Used (gallons) |
| --- | --- | --- | --- |
| Houston | 2270.8 | 34.0 | 8.9 |
| New York | 1845.6 | 15.8 | 53.0 |
| Chicago | 794.7 | 39.3 | 94.6 |
| Houston | 2506.4 | 4.1 | 53.5 |<start>
[
    {
        "Start Location": "Houston",
        "Distance (miles)": 2270.8,
        "Duration (hours)": 34.0,
        "Fuel Used (gallons)": 8.9
    },
    {
        "Start Location": "New York",
        "Distance (miles)": 1845.6,
        "Duration (hours)": 15.8,
        "Fuel Used (gallons)": 53.0
    },
    {
        "Start Location": "Chicago",
        "Distance (miles)": 794.7,
        "Duration (hours)": 39.3,
        "Fuel Used (gallons)": 94.6
    },
    {
        "Start Location": "Houston",
        "Distance (miles)": 2506.4,
        "Duration (hours)": 4.1,
        "Fuel Used (gallons)": 53.5
    }
]
<end>Convert this yml to json:
- Price: 468.58
  Product Name: Widget
  Supplier Name: Wayne Enterprises
- Price: 499.68
  Product Name: Thingamajig
  Supplier Name: Wonka Industries
- Price: 129.85
  Product Name: Device
  Supplier Name: Wonka Industries
- Price: 269.44
  Product Name: Device
  Supplier Name: Wayne Enterprises
- Price: 201.26
  Product Name: Instrument
  Supplier Name: Wonka Industries
- Price: 331.7
  Product Name: Instrument
  Supplier Name: ACME Corp
<start>
[
    {
        "Product Name": "Widget",
        "Price": 468.58,
        "Supplier Name": "Wayne Enterprises"
    },
    {
        "Product Name": "Thingamajig",
        "Price": 499.68,
        "Supplier Name": "Wonka Industries"
    },
    {
        "Product Name": "Device",
        "Price": 129.85,
        "Supplier Name": "Wonka Industries"
    },
    {
        "Product Name": "Device",
        "Price": 269.44,
        "Supplier Name": "Wayne Enterprises"
    },
    {
        "Product Name": "Instrument",
        "Price": 201.26,
        "Supplier Name": "Wonka Industries"
    },
    {
        "Product Name": "Instrument",
        "Price": 331.7,
        "Supplier Name": "ACME Corp"
    }
]
<end>Convert this Yml to Json:
- Company: Foodies
  Market Cap: Mega Cap
  Sector: Energy
  Stock Price: 116.39
- Company: HealthPlus
  Market Cap: Large Cap
  Sector: Automotive
  Stock Price: 877.96
- Company: GlobalTrade
  Market Cap: Large Cap
  Sector: Aerospace
  Stock Price: 979.31
- Company: RetailHub
  Market Cap: Mega Cap
  Sector: Aerospace
  Stock Price: 510.55
<start>
[
    {
        "Company": "Foodies",
        "Sector": "Energy",
        "Market Cap": "Mega Cap",
        "Stock Price": 116.39
    },
    {
        "Company": "HealthPlus",
        "Sector": "Automotive",
        "Market Cap": "Large Cap",
        "Stock Price": 877.96
    },
    {
        "Company": "GlobalTrade",
        "Sector": "Aerospace",
        "Market Cap": "Large Cap",
        "Stock Price": 979.31
    },
    {
        "Company": "RetailHub",
        "Sector": "Aerospace",
        "Market Cap": "Mega Cap",
        "Stock Price": 510.55
    }
]
<end>Can you change this yaml into markdown?
- Cuisine: Mediterranean
  Location: Miami
  Price Range: $$$$
- Cuisine: Chinese
  Location: Miami
  Price Range: $$$$
- Cuisine: Japanese
  Location: San Francisco
  Price Range: $$$$$
- Cuisine: American
  Location: Houston
  Price Range: $$$
- Cuisine: Mediterranean
  Location: Miami
  Price Range: $$$
- Cuisine: Mexican
  Location: Los Angeles
  Price Range: $$$
<start>
| Cuisine | Location | Price Range |
| --- | --- | --- |
| Mediterranean | Miami | $$$$ |
| Chinese | Miami | $$$$ |
| Japanese | San Francisco | $$$$$ |
| American | Houston | $$$ |
| Mediterranean | Miami | $$$ |
| Mexican | Los Angeles | $$$ |
<end>Can you change this MARKDOWN into Plain text?
| Restaurant Name | Location | Rating |
| --- | --- | --- |
| Pizza Planet | New York | 5 |
| Pizza Planet | Los Angeles | 2 |
| Curry Corner | Phoenix | 4 |
| The Steakhouse | Houston | 4 |<start>
Restaurant Name: Pizza Planet | Location: New York | Rating: 5
Restaurant Name: Pizza Planet | Location: Los Angeles | Rating: 2
Restaurant Name: Curry Corner | Location: Phoenix | Rating: 4
Restaurant Name: The Steakhouse | Location: Houston | Rating: 4
<end>Here's some csv data, can you convert it to json?
Device ID,Device Type,Location,Battery Level (%),Reading Value,Timestamp
device-0019,Humidity Sensor,Hallway,87.2,21.52,2022-05-21 14:01:11
device-0061,Motion Detector,Bedroom,51.1,-37.74,2022-04-12 03:51:35
device-0080,Light Sensor,Hallway,17.3,60.4,2021-07-23 23:07:38
device-0010,Motion Detector,Office,23.9,49.02,2022-02-24 19:26:02
device-0046,Humidity Sensor,Bathroom,52.1,1.5,2021-03-15 21:02:11
<start>
[
    {
        "Device ID": "device-0019",
        "Device Type": "Humidity Sensor",
        "Location": "Hallway",
        "Battery Level (%)": 87.2,
        "Reading Value": 21.52,
        "Timestamp": "2022-05-21 14:01:11"
    },
    {
        "Device ID": "device-0061",
        "Device Type": "Motion Detector",
        "Location": "Bedroom",
        "Battery Level (%)": 51.1,
        "Reading Value": -37.74,
        "Timestamp": "2022-04-12 03:51:35"
    },
    {
        "Device ID": "device-0080",
        "Device Type": "Light Sensor",
        "Location": "Hallway",
        "Battery Level (%)": 17.3,
        "Reading Value": 60.4,
        "Timestamp": "2021-07-23 23:07:38"
    },
    {
        "Device ID": "device-0010",
        "Device Type": "Motion Detector",
        "Location": "Office",
        "Battery Level (%)": 23.9,
        "Reading Value": 49.02,
        "Timestamp": "2022-02-24 19:26:02"
    },
    {
        "Device ID": "device-0046",
        "Device Type": "Humidity Sensor",
        "Location": "Bathroom",
        "Battery Level (%)": 52.1,
        "Reading Value": 1.5,
        "Timestamp": "2021-03-15 21:02:11"
    }
]
<end>Please transform the following Markdown data into JSON:
| Title | Author |
| --- | --- |
| Echoes of Eternity | Rowan Ashborne |
| Whispers of the Abyss | Kara Firebrand |
| Echoes of Eternity | Elara Moonshadow |
| The Last Sky | Kara Firebrand |
| The Crystal Key | Luna Silverleaf |
| The Crystal Key | Elara Moonshadow |
| The Last Sky | Draven Blackthorn |<start>
[
    {
        "Title": "Echoes of Eternity",
        "Author": "Rowan Ashborne"
    },
    {
        "Title": "Whispers of the Abyss",
        "Author": "Kara Firebrand"
    },
    {
        "Title": "Echoes of Eternity",
        "Author": "Elara Moonshadow"
    },
    {
        "Title": "The Last Sky",
        "Author": "Kara Firebrand"
    },
    {
        "Title": "The Crystal Key",
        "Author": "Luna Silverleaf"
    },
    {
        "Title": "The Crystal Key",
        "Author": "Elara Moonshadow"
    },
    {
        "Title": "The Last Sky",
        "Author": "Draven Blackthorn"
    }
]
<end>Convert this markdown to Json:
| Title | Director | Genre | Release Year | Box Office Earnings (M) |
| --- | --- | --- | --- | --- |
| The Final Voyage | Drake Nightshade | Sci-Fi | 1983 | 29.38 |
| Mystery of the Depths | Talon Blackthorn | Adventure | 1989 | 621.11 |
| Escape from Earth | Aria Ravenwood | Comedy | 1994 | 695.44 |
| Mystery of the Depths | Rylan Frostblade | Horror | 1987 | 578.26 |
| The Great Expedition | Orin Shadowalker | Action | 1977 | 239.41 |
| Edge of Infinity | Lira Silverleaf | Sci-Fi | 1988 | 352.56 |
| Dreamwalker | Drake Nightshade | Sci-Fi | 1982 | 834.45 |
| Mystery of the Depths | Mara Moonshadow | Sci-Fi | 1975 | 950.65 |
| The Final Voyage | Mara Moonshadow | Sci-Fi | 2007 | 576.92 |<start>
[
    {
        "Title": "The Final Voyage",
        "Director": "Drake Nightshade",
        "Genre": "Sci-Fi",
        "Release Year": 1983,
        "Box Office Earnings (M)": 29.38
    },
    {
        "Title": "Mystery of the Depths",
        "Director": "Talon Blackthorn",
        "Genre": "Adventure",
        "Release Year": 1989,
        "Box Office Earnings (M)": 621.11
    },
    {
        "Title": "Escape from Earth",
        "Director": "Aria Ravenwood",
        "Genre": "Comedy",
        "Release Year": 1994,
        "Box Office Earnings (M)": 695.44
    },
    {
        "Title": "Mystery of the Depths",
        "Director": "Rylan Frostblade",
        "Genre": "Horror",
        "Release Year": 1987,
        "Box Office Earnings (M)": 578.26
    },
    {
        "Title": "The Great Expedition",
        "Director": "Orin Shadowalker",
        "Genre": "Action",
        "Release Year": 1977,
        "Box Office Earnings (M)": 239.41
    },
    {
        "Title": "Edge of Infinity",
        "Director": "Lira Silverleaf",
        "Genre": "Sci-Fi",
        "Release Year": 1988,
        "Box Office Earnings (M)": 352.56
    },
    {
        "Title": "Dreamwalker",
        "Director": "Drake Nightshade",
        "Genre": "Sci-Fi",
        "Release Year": 1982,
        "Box Office Earnings (M)": 834.45
    },
    {
        "Title": "Mystery of the Depths",
        "Director": "Mara Moonshadow",
        "Genre": "Sci-Fi",
        "Release Year": 1975,
        "Box Office Earnings (M)": 950.65
    },
    {
        "Title": "The Final Voyage",
        "Director": "Mara Moonshadow",
        "Genre": "Sci-Fi",
        "Release Year": 2007,
        "Box Office Earnings (M)": 576.92
    }
]
<end>Can you change this MARKDOWN into yml?
| Trip Name | End Location | Distance (miles) |
| --- | --- | --- |
| Mountain Adventure | Phoenix | 1116.6 |
| Highway Odyssey | New York | 2066.7 |
| Forest Journey | Miami | 1300.4 |
| Coast to Coast | Los Angeles | 2906.2 |
| Coast to Coast | Houston | 1250.2 |
| Forest Journey | Houston | 2932.1 |
| Mountain Adventure | Denver | 236.6 |
| Coast to Coast | New York | 1879.1 |<start>
- Distance (miles): 1116.6
  End Location: Phoenix
  Trip Name: Mountain Adventure
- Distance (miles): 2066.7
  End Location: New York
  Trip Name: Highway Odyssey
- Distance (miles): 1300.4
  End Location: Miami
  Trip Name: Forest Journey
- Distance (miles): 2906.2
  End Location: Los Angeles
  Trip Name: Coast to Coast
- Distance (miles): 1250.2
  End Location: Houston
  Trip Name: Coast to Coast
- Distance (miles): 2932.1
  End Location: Houston
  Trip Name: Forest Journey
- Distance (miles): 236.6
  End Location: Denver
  Trip Name: Mountain Adventure
- Distance (miles): 1879.1
  End Location: New York
  Trip Name: Coast to Coast
<end>Convert this Csv to Yaml:
Product Name,Price,Stock Quantity,Category,Supplier Name
Thingamajig,78.09,320,Automotive,Wayne Enterprises
Gizmo,58.24,4,Electronics,Wonka Industries
Apparatus,14.06,448,Electronics,Wayne Enterprises
Contraption,487.51,276,Toys,ACME Corp
Widget,132.05,498,Household,Wonka Industries
Thingamajig,395.65,405,Electronics,Wayne Enterprises
Apparatus,32.98,274,Automotive,ACME Corp
Instrument,347.14,276,Household,Wayne Enterprises
Whatchamacallit,200.7,32,Electronics,Wayne Enterprises
<start>
- Category: Automotive
  Price: 78.09
  Product Name: Thingamajig
  Stock Quantity: 320
  Supplier Name: Wayne Enterprises
- Category: Electronics
  Price: 58.24
  Product Name: Gizmo
  Stock Quantity: 4
  Supplier Name: Wonka Industries
- Category: Electronics
  Price: 14.06
  Product Name: Apparatus
  Stock Quantity: 448
  Supplier Name: Wayne Enterprises
- Category: Toys
  Price: 487.51
  Product Name: Contraption
  Stock Quantity: 276
  Supplier Name: ACME Corp
- Category: Household
  Price: 132.05
  Product Name: Widget
  Stock Quantity: 498
  Supplier Name: Wonka Industries
- Category: Electronics
  Price: 395.65
  Product Name: Thingamajig
  Stock Quantity: 405
  Supplier Name: Wayne Enterprises
- Category: Automotive
  Price: 32.98
  Product Name: Apparatus
  Stock Quantity: 274
  Supplier Name: ACME Corp
- Category: Household
  Price: 347.14
  Product Name: Instrument
  Stock Quantity: 276
  Supplier Name: Wayne Enterprises
- Category: Electronics
  Price: 200.7
  Product Name: Whatchamacallit
  Stock Quantity: 32
  Supplier Name: Wayne Enterprises
<end>Here's some markdown data, can you convert it to plain text?
| Product Name | SKU | Category | Supplier Name |
| --- | --- | --- | --- |
| Gizmo | SKU-1090 | Household | Wayne Enterprises |
| Contraption | SKU-1012 | Automotive | Wayne Enterprises |
| Apparatus | SKU-1052 | Automotive | Globex |
| Device | SKU-1057 | Automotive | Wonka Industries |
| Instrument | SKU-1088 | Sports | Umbrella Corp |
| Whatchamacallit | SKU-1048 | Electronics | Wonka Industries |
| Gadget | SKU-1000 | Household | Wayne Enterprises |
| Thingamajig | SKU-1085 | Household | Umbrella Corp |
| Contraption | SKU-1039 | Automotive | Globex |<start>
Product Name: Gizmo | SKU: SKU-1090 | Category: Household | Supplier Name: Wayne Enterprises
Product Name: Contraption | SKU: SKU-1012 | Category: Automotive | Supplier Name: Wayne Enterprises
Product Name: Apparatus | SKU: SKU-1052 | Category: Automotive | Supplier Name: Globex
Product Name: Device | SKU: SKU-1057 | Category: Automotive | Supplier Name: Wonka Industries
Product Name: Instrument | SKU: SKU-1088 | Category: Sports | Supplier Name: Umbrella Corp
Product Name: Whatchamacallit | SKU: SKU-1048 | Category: Electronics | Supplier Name: Wonka Industries
Product Name: Gadget | SKU: SKU-1000 | Category: Household | Supplier Name: Wayne Enterprises
Product Name: Thingamajig | SKU: SKU-1085 | Category: Household | Supplier Name: Umbrella Corp
Product Name: Contraption | SKU: SKU-1039 | Category: Automotive | Supplier Name: Globex
<end>Here's some csv data, can you convert it to Plain text?
Database Name,Queries per Second,Average Latency (ms),Timestamp
ProfilesDB,3066.27,54.08,2022-05-28 02:21:47
ProfilesDB,4596.57,29.51,2021-06-16 23:55:29
UserDB,3553.9,42.63,2022-03-13 19:29:16
SalesDB,1791.5,64.66,2023-11-10 18:56:25
LogsDB,2148.34,42.63,2023-12-28 23:30:19
SalesDB,3173.45,26.77,2023-01-07 07:14:36
SessionsDB,4216.64,88.24,2022-03-04 23:23:06
SalesDB,2368.78,40.37,2022-09-12 04:14:49
<start>
Database Name: ProfilesDB | Queries per Second: 3066.27 | Average Latency (ms): 54.08 | Timestamp: 2022-05-28 02:21:47
Database Name: ProfilesDB | Queries per Second: 4596.57 | Average Latency (ms): 29.51 | Timestamp: 2021-06-16 23:55:29
Database Name: UserDB | Queries per Second: 3553.9 | Average Latency (ms): 42.63 | Timestamp: 2022-03-13 19:29:16
Database Name: SalesDB | Queries per Second: 1791.5 | Average Latency (ms): 64.66 | Timestamp: 2023-11-10 18:56:25
Database Name: LogsDB | Queries per Second: 2148.34 | Average Latency (ms): 42.63 | Timestamp: 2023-12-28 23:30:19
Database Name: SalesDB | Queries per Second: 3173.45 | Average Latency (ms): 26.77 | Timestamp: 2023-01-07 07:14:36
Database Name: SessionsDB | Queries per Second: 4216.64 | Average Latency (ms): 88.24 | Timestamp: 2022-03-04 23:23:06
Database Name: SalesDB | Queries per Second: 2368.78 | Average Latency (ms): 40.37 | Timestamp: 2022-09-12 04:14:49
<end>Here's some csv data, can you convert it to yml?
Trip Name,Start Location,End Location,Distance (miles),Duration (hours)
Canyon Trek,Denver,San Francisco,2755.9,28.7
Desert Drive,New York,Houston,895.3,28.1
Historic Route,Denver,Miami,735.4,30.5
City Explorer,Houston,San Francisco,1130.9,29.9
City Explorer,Chicago,San Francisco,2093.7,25.3
Desert Drive,Chicago,San Francisco,2589.8,2.0
Canyon Trek,San Francisco,Houston,1698.2,55.1
Valley Voyage,Miami,San Francisco,1997.6,39.3
Desert Drive,Houston,San Francisco,214.1,39.4
Mountain Adventure,Los Angeles,San Francisco,2361.8,49.7
<start>
- Distance (miles): 2755.9
  Duration (hours): 28.7
  End Location: San Francisco
  Start Location: Denver
  Trip Name: Canyon Trek
- Distance (miles): 895.3
  Duration (hours): 28.1
  End Location: Houston
  Start Location: New York
  Trip Name: Desert Drive
- Distance (miles): 735.4
  Duration (hours): 30.5
  End Location: Miami
  Start Location: Denver
  Trip Name: Historic Route
- Distance (miles): 1130.9
  Duration (hours): 29.9
  End Location: San Francisco
  Start Location: Houston
  Trip Name: City Explorer
- Distance (miles): 2093.7
  Duration (hours): 25.3
  End Location: San Francisco
  Start Location: Chicago
  Trip Name: City Explorer
- Distance (miles): 2589.8
  Duration (hours): 2.0
  End Location: San Francisco
  Start Location: Chicago
  Trip Name: Desert Drive
- Distance (miles): 1698.2
  Duration (hours): 55.1
  End Location: Houston
  Start Location: San Francisco
  Trip Name: Canyon Trek
- Distance (miles): 1997.6
  Duration (hours): 39.3
  End Location: San Francisco
  Start Location: Miami
  Trip Name: Valley Voyage
- Distance (miles): 214.1
  Duration (hours): 39.4
  End Location: San Francisco
  Start Location: Houston
  Trip Name: Desert Drive
- Distance (miles): 2361.8
  Duration (hours): 49.7
  End Location: San Francisco
  Start Location: Los Angeles
  Trip Name: Mountain Adventure
<end>Please transform the following PLAIN TEXT data into Yml:
SKU: SKU-1034 | Stock Quantity: 314 | Category: Sports
SKU: SKU-1043 | Stock Quantity: 301 | Category: Sports
SKU: SKU-1037 | Stock Quantity: 409 | Category: Electronics
<start>
- Category: Sports
  SKU: SKU-1034
  Stock Quantity: 314
- Category: Sports
  SKU: SKU-1043
  Stock Quantity: 301
- Category: Electronics
  SKU: SKU-1037
  Stock Quantity: 409
<end>Convert this yml to plain text:
- Duration (hours): 68.8
  End Location: Phoenix
  Start Location: Denver
- Duration (hours): 38.1
  End Location: Miami
  Start Location: Phoenix
- Duration (hours): 31.2
  End Location: Denver
  Start Location: New York
- Duration (hours): 16.4
  End Location: New York
  Start Location: Phoenix
- Duration (hours): 67.8
  End Location: Houston
  Start Location: Chicago
- Duration (hours): 33.6
  End Location: Miami
  Start Location: Phoenix
- Duration (hours): 54.0
  End Location: Miami
  Start Location: Los Angeles
- Duration (hours): 71.7
  End Location: Chicago
  Start Location: Los Angeles
<start>
Start Location: Denver | End Location: Phoenix | Duration (hours): 68.8
Start Location: Phoenix | End Location: Miami | Duration (hours): 38.1
Start Location: New York | End Location: Denver | Duration (hours): 31.2
Start Location: Phoenix | End Location: New York | Duration (hours): 16.4
Start Location: Chicago | End Location: Houston | Duration (hours): 67.8
Start Location: Phoenix | End Location: Miami | Duration (hours): 33.6
Start Location: Los Angeles | End Location: Miami | Duration (hours): 54.0
Start Location: Los Angeles | End Location: Chicago | Duration (hours): 71.7
<end>Transform this json structure to a MARKDOWN format:
[
    {
        "Product Name": "Contraption",
        "SKU": "SKU-1011",
        "Price": 62.76,
        "Category": "Toys",
        "Supplier Name": "Wonka Industries"
    },
    {
        "Product Name": "Contraption",
        "SKU": "SKU-1041",
        "Price": 303.21,
        "Category": "Automotive",
        "Supplier Name": "Umbrella Corp"
    },
    {
        "Product Name": "Gadget",
        "SKU": "SKU-1042",
        "Price": 145.37,
        "Category": "Automotive",
        "Supplier Name": "Wayne Enterprises"
    },
    {
        "Product Name": "Doohickey",
        "SKU": "SKU-1034",
        "Price": 8.17,
        "Category": "Sports",
        "Supplier Name": "Umbrella Corp"
    },
    {
        "Product Name": "Contraption",
        "SKU": "SKU-1010",
        "Price": 64.7,
        "Category": "Toys",
        "Supplier Name": "Wayne Enterprises"
    },
    {
        "Product Name": "Gizmo",
        "SKU": "SKU-1016",
        "Price": 56.19,
        "Category": "Electronics",
        "Supplier Name": "Wonka Industries"
    }
]<start>
| Product Name | SKU | Price | Category | Supplier Name |
| --- | --- | --- | --- | --- |
| Contraption | SKU-1011 | 62.76 | Toys | Wonka Industries |
| Contraption | SKU-1041 | 303.21 | Automotive | Umbrella Corp |
| Gadget | SKU-1042 | 145.37 | Automotive | Wayne Enterprises |
| Doohickey | SKU-1034 | 8.17 | Sports | Umbrella Corp |
| Contraption | SKU-1010 | 64.7 | Toys | Wayne Enterprises |
| Gizmo | SKU-1016 | 56.19 | Electronics | Wonka Industries |
<end>Can you change this YML into CSV?
- Age: 27
  Birth Month: September
  City: Milwaukee
- Age: 18
  Birth Month: January
  City: Milwaukee
- Age: 55
  Birth Month: July
  City: Detroit
- Age: 41
  Birth Month: February
  City: El Paso
- Age: 43
  Birth Month: August
  City: Louisville
- Age: 42
  Birth Month: October
  City: Charlotte
- Age: 49
  Birth Month: June
  City: Los Angeles
- Age: 63
  Birth Month: May
  City: San Francisco
<start>
Age,Birth Month,City
27,September,Milwaukee
18,January,Milwaukee
55,July,Detroit
41,February,El Paso
43,August,Louisville
42,October,Charlotte
49,June,Los Angeles
63,May,San Francisco
<end>Can you change this JSON into yaml?
[
    {
        "Name": "Lucy",
        "Birth Month": "January",
        "City": "Boston"
    },
    {
        "Name": "Rufus",
        "Birth Month": "November",
        "City": "Columbus"
    },
    {
        "Name": "Rex",
        "Birth Month": "September",
        "City": "San Jose"
    },
    {
        "Name": "Monique",
        "Birth Month": "February",
        "City": "Dallas"
    },
    {
        "Name": "Bonnie",
        "Birth Month": "February",
        "City": "Indianapolis"
    },
    {
        "Name": "Virgie",
        "Birth Month": "October",
        "City": "Austin"
    },
    {
        "Name": "Cecilia",
        "Birth Month": "January",
        "City": "Chicago"
    }
]<start>
- Birth Month: January
  City: Boston
  Name: Lucy
- Birth Month: November
  City: Columbus
  Name: Rufus
- Birth Month: September
  City: San Jose
  Name: Rex
- Birth Month: February
  City: Dallas
  Name: Monique
- Birth Month: February
  City: Indianapolis
  Name: Bonnie
- Birth Month: October
  City: Austin
  Name: Virgie
- Birth Month: January
  City: Chicago
  Name: Cecilia
<end>Here's some Csv data, can you convert it to YML?
Product Name,SKU,Stock Quantity,Category,Supplier Name
Apparatus,SKU-1036,109,Electronics,Umbrella Corp
Instrument,SKU-1056,319,Automotive,ACME Corp
Whatchamacallit,SKU-1030,230,Automotive,Globex
<start>
- Category: Electronics
  Product Name: Apparatus
  SKU: SKU-1036
  Stock Quantity: 109
  Supplier Name: Umbrella Corp
- Category: Automotive
  Product Name: Instrument
  SKU: SKU-1056
  Stock Quantity: 319
  Supplier Name: ACME Corp
- Category: Automotive
  Product Name: Whatchamacallit
  SKU: SKU-1030
  Stock Quantity: 230
  Supplier Name: Globex
<end>Here's some markdown data, can you convert it to yaml?
| Date | Open Price | Close Price | High Price |
| --- | --- | --- | --- |
| 2014-09-08 | 282.9 | 1446.96 | 1446.96 |
| 2023-06-05 | 1043.25 | 1111.96 | 1117.06 |
| 2017-06-21 | 745.39 | 755.5 | 755.5 |
| 2014-07-10 | 639.34 | 628.68 | 790.85 |
| 2017-10-19 | 1281.89 | 1111.12 | 1281.89 |
| 2011-11-09 | 1055.94 | 959.87 | 1337.06 |
| 2010-07-09 | 1384.32 | 495.4 | 1384.32 |
| 2012-04-13 | 322.58 | 755.18 | 755.18 |<start>
- Close Price: 1446.96
  Date: '2014-09-08'
  High Price: 1446.96
  Open Price: 282.9
- Close Price: 1111.96
  Date: '2023-06-05'
  High Price: 1117.06
  Open Price: 1043.25
- Close Price: 755.5
  Date: '2017-06-21'
  High Price: 755.5
  Open Price: 745.39
- Close Price: 628.68
  Date: '2014-07-10'
  High Price: 790.85
  Open Price: 639.34
- Close Price: 1111.12
  Date: '2017-10-19'
  High Price: 1281.89
  Open Price: 1281.89
- Close Price: 959.87
  Date: '2011-11-09'
  High Price: 1337.06
  Open Price: 1055.94
- Close Price: 495.4
  Date: '2010-07-09'
  High Price: 1384.32
  Open Price: 1384.32
- Close Price: 755.18
  Date: '2012-04-13'
  High Price: 755.18
  Open Price: 322.58
<end>Please transform the following JSON data into Plain text:
[
    {
        "Database Name": "ProductsDB",
        "Queries per Second": 4953.6,
        "Connection Count": 478,
        "Average Latency (ms)": 61.67
    },
    {
        "Database Name": "SessionsDB",
        "Queries per Second": 3072.03,
        "Connection Count": 471,
        "Average Latency (ms)": 20.88
    },
    {
        "Database Name": "UserDB",
        "Queries per Second": 3363.82,
        "Connection Count": 386,
        "Average Latency (ms)": 6.03
    },
    {
        "Database Name": "ProfilesDB",
        "Queries per Second": 4119.82,
        "Connection Count": 371,
        "Average Latency (ms)": 52.16
    },
    {
        "Database Name": "LogsDB",
        "Queries per Second": 2540.15,
        "Connection Count": 73,
        "Average Latency (ms)": 57.32
    },
    {
        "Database Name": "OrdersDB",
        "Queries per Second": 4049.28,
        "Connection Count": 486,
        "Average Latency (ms)": 68.36
    }
]<start>
Database Name: ProductsDB | Queries per Second: 4953.6 | Connection Count: 478 | Average Latency (ms): 61.67
Database Name: SessionsDB | Queries per Second: 3072.03 | Connection Count: 471 | Average Latency (ms): 20.88
Database Name: UserDB | Queries per Second: 3363.82 | Connection Count: 386 | Average Latency (ms): 6.03
Database Name: ProfilesDB | Queries per Second: 4119.82 | Connection Count: 371 | Average Latency (ms): 52.16
Database Name: LogsDB | Queries per Second: 2540.15 | Connection Count: 73 | Average Latency (ms): 57.32
Database Name: OrdersDB | Queries per Second: 4049.28 | Connection Count: 486 | Average Latency (ms): 68.36
<end>Here's some csv data, can you convert it to plain text?
Title,Director,Release Year
Edge of Infinity,Orin Shadowalker,2007
The Final Voyage,Talon Blackthorn,2019
Rise of the Titans,Lira Silverleaf,2016
<start>
Title: Edge of Infinity | Director: Orin Shadowalker | Release Year: 2007
Title: The Final Voyage | Director: Talon Blackthorn | Release Year: 2019
Title: Rise of the Titans | Director: Lira Silverleaf | Release Year: 2016
<end>Convert this csv to Yaml:
Location,Rating,Price Range
San Francisco,2,$
Miami,3,$$$
Chicago,2,$$$$$
San Francisco,4,$$
Miami,2,$$$
<start>
- Location: San Francisco
  Price Range: $
  Rating: 2
- Location: Miami
  Price Range: $$$
  Rating: 3
- Location: Chicago
  Price Range: $$$$$
  Rating: 2
- Location: San Francisco
  Price Range: $$
  Rating: 4
- Location: Miami
  Price Range: $$$
  Rating: 2
<end>Convert this Json to yaml:
[
    {
        "Device ID": "device-0042",
        "Device Type": "Pressure Sensor",
        "Location": "Bedroom",
        "Battery Level (%)": 19.8
    },
    {
        "Device ID": "device-0005",
        "Device Type": "Temperature Sensor",
        "Location": "Living Room",
        "Battery Level (%)": 60.9
    },
    {
        "Device ID": "device-0061",
        "Device Type": "Pressure Sensor",
        "Location": "Bathroom",
        "Battery Level (%)": 65.9
    },
    {
        "Device ID": "device-0034",
        "Device Type": "Humidity Sensor",
        "Location": "Office",
        "Battery Level (%)": 37.3
    },
    {
        "Device ID": "device-0084",
        "Device Type": "Light Sensor",
        "Location": "Living Room",
        "Battery Level (%)": 83.5
    },
    {
        "Device ID": "device-0062",
        "Device Type": "Pressure Sensor",
        "Location": "Living Room",
        "Battery Level (%)": 66.7
    }
]<start>
- Battery Level (%): 19.8
  Device ID: device-0042
  Device Type: Pressure Sensor
  Location: Bedroom
- Battery Level (%): 60.9
  Device ID: device-0005
  Device Type: Temperature Sensor
  Location: Living Room
- Battery Level (%): 65.9
  Device ID: device-0061
  Device Type: Pressure Sensor
  Location: Bathroom
- Battery Level (%): 37.3
  Device ID: device-0034
  Device Type: Humidity Sensor
  Location: Office
- Battery Level (%): 83.5
  Device ID: device-0084
  Device Type: Light Sensor
  Location: Living Room
- Battery Level (%): 66.7
  Device ID: device-0062
  Device Type: Pressure Sensor
  Location: Living Room
<end>Transform this yml structure to a CSV format:
- Company: BioPharm
  Quarter: Q3
  Sector: Biotech
- Company: BioPharm
  Quarter: Q2
  Sector: Aerospace
- Company: TechCorp
  Quarter: Q3
  Sector: Aerospace
- Company: BioPharm
  Quarter: Q4
  Sector: Biotech
- Company: RetailHub
  Quarter: Q2
  Sector: Automotive
- Company: AutoDrive
  Quarter: Q1
  Sector: Automotive
- Company: TechCorp
  Quarter: Q2
  Sector: Automotive
- Company: HealthPlus
  Quarter: Q3
  Sector: Technology
- Company: BioPharm
  Quarter: Q1
  Sector: Aerospace
<start>
Company,Sector,Quarter
BioPharm,Biotech,Q3
BioPharm,Aerospace,Q2
TechCorp,Aerospace,Q3
BioPharm,Biotech,Q4
RetailHub,Automotive,Q2
AutoDrive,Automotive,Q1
TechCorp,Automotive,Q2
HealthPlus,Technology,Q3
BioPharm,Aerospace,Q1
<end>Here's some plain text data, can you convert it to YAML?
Company: TechCorp | Sector: Aerospace | Market Cap: Small Cap | Stock Price: 756.27 | Annual Revenue (B): 86.53 | Quarter: Q3
Company: AeroSpace | Sector: Biotech | Market Cap: Mid Cap | Stock Price: 205.28 | Annual Revenue (B): 321.76 | Quarter: Q2
Company: Foodies | Sector: Automotive | Market Cap: Large Cap | Stock Price: 208.67 | Annual Revenue (B): 463.58 | Quarter: Q4
Company: AutoDrive | Sector: Healthcare | Market Cap: Mid Cap | Stock Price: 208.67 | Annual Revenue (B): 284.34 | Quarter: Q4
Company: AutoDrive | Sector: Technology | Market Cap: Mega Cap | Stock Price: 317.39 | Annual Revenue (B): 195.42 | Quarter: Q2
Company: Foodies | Sector: Healthcare | Market Cap: Mega Cap | Stock Price: 35.38 | Annual Revenue (B): 236.52 | Quarter: Q1
Company: TechCorp | Sector: Automotive | Market Cap: Mid Cap | Stock Price: 764.12 | Annual Revenue (B): 486.1 | Quarter: Q2
<start>
- Annual Revenue (B): 86.53
  Company: TechCorp
  Market Cap: Small Cap
  Quarter: Q3
  Sector: Aerospace
  Stock Price: 756.27
- Annual Revenue (B): 321.76
  Company: AeroSpace
  Market Cap: Mid Cap
  Quarter: Q2
  Sector: Biotech
  Stock Price: 205.28
- Annual Revenue (B): 463.58
  Company: Foodies
  Market Cap: Large Cap
  Quarter: Q4
  Sector: Automotive
  Stock Price: 208.67
- Annual Revenue (B): 284.34
  Company: AutoDrive
  Market Cap: Mid Cap
  Quarter: Q4
  Sector: Healthcare
  Stock Price: 208.67
- Annual Revenue (B): 195.42
  Company: AutoDrive
  Market Cap: Mega Cap
  Quarter: Q2
  Sector: Technology
  Stock Price: 317.39
- Annual Revenue (B): 236.52
  Company: Foodies
  Market Cap: Mega Cap
  Quarter: Q1
  Sector: Healthcare
  Stock Price: 35.38
- Annual Revenue (B): 486.1
  Company: TechCorp
  Market Cap: Mid Cap
  Quarter: Q2
  Sector: Automotive
  Stock Price: 764.12
<end>Transform this csv structure to a Plain text format:
Device ID,Device Type,Location,Battery Level (%),Reading Value,Timestamp
device-0038,Motion Detector,Bedroom,45.2,54.06,2023-08-22 16:34:45
device-0050,Light Sensor,Garden,52.2,22.53,2023-02-10 03:52:43
device-0022,Pressure Sensor,Kitchen,34.2,22.53,2023-01-13 10:03:37
device-0055,Humidity Sensor,Office,33.6,-2.31,2022-08-11 11:18:46
device-0078,Humidity Sensor,Garage,20.2,-18.58,2023-12-03 01:59:24
device-0056,Humidity Sensor,Office,51.0,-2.12,2023-10-01 19:38:12
<start>
Device ID: device-0038 | Device Type: Motion Detector | Location: Bedroom | Battery Level (%): 45.2 | Reading Value: 54.06 | Timestamp: 2023-08-22 16:34:45
Device ID: device-0050 | Device Type: Light Sensor | Location: Garden | Battery Level (%): 52.2 | Reading Value: 22.53 | Timestamp: 2023-02-10 03:52:43
Device ID: device-0022 | Device Type: Pressure Sensor | Location: Kitchen | Battery Level (%): 34.2 | Reading Value: 22.53 | Timestamp: 2023-01-13 10:03:37
Device ID: device-0055 | Device Type: Humidity Sensor | Location: Office | Battery Level (%): 33.6 | Reading Value: -2.31 | Timestamp: 2022-08-11 11:18:46
Device ID: device-0078 | Device Type: Humidity Sensor | Location: Garage | Battery Level (%): 20.2 | Reading Value: -18.58 | Timestamp: 2023-12-03 01:59:24
Device ID: device-0056 | Device Type: Humidity Sensor | Location: Office | Battery Level (%): 51.0 | Reading Value: -2.12 | Timestamp: 2023-10-01 19:38:12
<end>Can you change this csv into json?
Database Name,Queries per Second,Cache Hit Ratio (%),Average Latency (ms),Timestamp
InventoryDB,2570.47,77.59,24.63,2021-09-01 23:05:07
SessionsDB,1720.69,78.15,63.89,2023-02-03 20:14:04
SessionsDB,1336.04,78.06,49.46,2023-07-02 11:58:36
ProfilesDB,2974.47,86.06,63.52,2023-07-23 13:59:29
SalesDB,3204.61,70.29,47.99,2021-02-21 01:36:07
SessionsDB,4549.66,97.58,58.04,2021-12-23 13:01:23
ProfilesDB,4513.89,71.26,45.3,2021-09-19 12:11:16
LogsDB,437.53,80.18,83.16,2022-06-11 21:20:19
<start>
[
    {
        "Database Name": "InventoryDB",
        "Queries per Second": 2570.47,
        "Cache Hit Ratio (%)": 77.59,
        "Average Latency (ms)": 24.63,
        "Timestamp": "2021-09-01 23:05:07"
    },
    {
        "Database Name": "SessionsDB",
        "Queries per Second": 1720.69,
        "Cache Hit Ratio (%)": 78.15,
        "Average Latency (ms)": 63.89,
        "Timestamp": "2023-02-03 20:14:04"
    },
    {
        "Database Name": "SessionsDB",
        "Queries per Second": 1336.04,
        "Cache Hit Ratio (%)": 78.06,
        "Average Latency (ms)": 49.46,
        "Timestamp": "2023-07-02 11:58:36"
    },
    {
        "Database Name": "ProfilesDB",
        "Queries per Second": 2974.47,
        "Cache Hit Ratio (%)": 86.06,
        "Average Latency (ms)": 63.52,
        "Timestamp": "2023-07-23 13:59:29"
    },
    {
        "Database Name": "SalesDB",
        "Queries per Second": 3204.61,
        "Cache Hit Ratio (%)": 70.29,
        "Average Latency (ms)": 47.99,
        "Timestamp": "2021-02-21 01:36:07"
    },
    {
        "Database Name": "SessionsDB",
        "Queries per Second": 4549.66,
        "Cache Hit Ratio (%)": 97.58,
        "Average Latency (ms)": 58.04,
        "Timestamp": "2021-12-23 13:01:23"
    },
    {
        "Database Name": "ProfilesDB",
        "Queries per Second": 4513.89,
        "Cache Hit Ratio (%)": 71.26,
        "Average Latency (ms)": 45.3,
        "Timestamp": "2021-09-19 12:11:16"
    },
    {
        "Database Name": "LogsDB",
        "Queries per Second": 437.53,
        "Cache Hit Ratio (%)": 80.18,
        "Average Latency (ms)": 83.16,
        "Timestamp": "2022-06-11 21:20:19"
    }
]
<end>Can you change this csv into JSON?
Condition,Wind Speed (km/h),Day
Cloudy,8.8,Friday
Rainy,21.0,Sunday
Stormy,21.8,Tuesday
Sunny,18.3,Wednesday
Stormy,6.6,Sunday
Rainy,20.5,Thursday
Stormy,29.4,Wednesday
<start>
[
    {
        "Condition": "Cloudy",
        "Wind Speed (km/h)": 8.8,
        "Day": "Friday"
    },
    {
        "Condition": "Rainy",
        "Wind Speed (km/h)": 21.0,
        "Day": "Sunday"
    },
    {
        "Condition": "Stormy",
        "Wind Speed (km/h)": 21.8,
        "Day": "Tuesday"
    },
    {
        "Condition": "Sunny",
        "Wind Speed (km/h)": 18.3,
        "Day": "Wednesday"
    },
    {
        "Condition": "Stormy",
        "Wind Speed (km/h)": 6.6,
        "Day": "Sunday"
    },
    {
        "Condition": "Rainy",
        "Wind Speed (km/h)": 20.5,
        "Day": "Thursday"
    },
    {
        "Condition": "Stormy",
        "Wind Speed (km/h)": 29.4,
        "Day": "Wednesday"
    }
]
<end>Can you change this csv into json?
Company,Sector,Stock Price,Annual Revenue (B),Quarter
FinanceWorks,Technology,104.93,80.21,Q1
HealthPlus,Energy,711.45,420.68,Q2
HealthPlus,Energy,395.88,329.41,Q3
TechCorp,Healthcare,930.07,340.8,Q3
Foodies,Finance,658.33,484.68,Q2
BioPharm,Finance,850.48,488.22,Q2
Foodies,Aerospace,608.33,70.74,Q4
<start>
[
    {
        "Company": "FinanceWorks",
        "Sector": "Technology",
        "Stock Price": 104.93,
        "Annual Revenue (B)": 80.21,
        "Quarter": "Q1"
    },
    {
        "Company": "HealthPlus",
        "Sector": "Energy",
        "Stock Price": 711.45,
        "Annual Revenue (B)": 420.68,
        "Quarter": "Q2"
    },
    {
        "Company": "HealthPlus",
        "Sector": "Energy",
        "Stock Price": 395.88,
        "Annual Revenue (B)": 329.41,
        "Quarter": "Q3"
    },
    {
        "Company": "TechCorp",
        "Sector": "Healthcare",
        "Stock Price": 930.07,
        "Annual Revenue (B)": 340.8,
        "Quarter": "Q3"
    },
    {
        "Company": "Foodies",
        "Sector": "Finance",
        "Stock Price": 658.33,
        "Annual Revenue (B)": 484.68,
        "Quarter": "Q2"
    },
    {
        "Company": "BioPharm",
        "Sector": "Finance",
        "Stock Price": 850.48,
        "Annual Revenue (B)": 488.22,
        "Quarter": "Q2"
    },
    {
        "Company": "Foodies",
        "Sector": "Aerospace",
        "Stock Price": 608.33,
        "Annual Revenue (B)": 70.74,
        "Quarter": "Q4"
    }
]
<end>Transform this CSV structure to a plain text format:
Date,Close Price,High Price,Volume
2021-11-17,321.81,1494.07,7514394
2023-01-26,284.1,1322.04,8369396
2018-02-03,483.59,1085.95,1263050
<start>
Date: 2021-11-17 | Close Price: 321.81 | High Price: 1494.07 | Volume: 7514394
Date: 2023-01-26 | Close Price: 284.1 | High Price: 1322.04 | Volume: 8369396
Date: 2018-02-03 | Close Price: 483.59 | High Price: 1085.95 | Volume: 1263050
<end>Please transform the following yml data into Markdown:
- Distance (miles): 109.1
  End Location: Chicago
  Fuel Used (gallons): 22.3
  Start Location: San Francisco
  Trip Name: Mountain Adventure
- Distance (miles): 363.8
  End Location: Denver
  Fuel Used (gallons): 64.8
  Start Location: New York
  Trip Name: Canyon Trek
- Distance (miles): 100.9
  End Location: Miami
  Fuel Used (gallons): 11.7
  Start Location: Houston
  Trip Name: Canyon Trek
- Distance (miles): 2674.5
  End Location: Phoenix
  Fuel Used (gallons): 64.8
  Start Location: Denver
  Trip Name: Historic Route
- Distance (miles): 1444.7
  End Location: San Francisco
  Fuel Used (gallons): 97.4
  Start Location: Chicago
  Trip Name: Canyon Trek
- Distance (miles): 2196.4
  End Location: Houston
  Fuel Used (gallons): 54.8
  Start Location: New York
  Trip Name: Valley Voyage
- Distance (miles): 109.1
  End Location: San Francisco
  Fuel Used (gallons): 56.9
  Start Location: New York
  Trip Name: Historic Route
<start>
| Trip Name | Start Location | End Location | Distance (miles) | Fuel Used (gallons) |
| --- | --- | --- | --- | --- |
| Mountain Adventure | San Francisco | Chicago | 109.1 | 22.3 |
| Canyon Trek | New York | Denver | 363.8 | 64.8 |
| Canyon Trek | Houston | Miami | 100.9 | 11.7 |
| Historic Route | Denver | Phoenix | 2674.5 | 64.8 |
| Canyon Trek | Chicago | San Francisco | 1444.7 | 97.4 |
| Valley Voyage | New York | Houston | 2196.4 | 54.8 |
| Historic Route | New York | San Francisco | 109.1 | 56.9 |
<end>Transform this yaml structure to a json format:
- Category: Household
  Price: 223.0
  Product Name: Widget
  SKU: SKU-1073
  Supplier Name: Wayne Enterprises
- Category: Household
  Price: 225.92
  Product Name: Contraption
  SKU: SKU-1000
  Supplier Name: Umbrella Corp
- Category: Sports
  Price: 104.33
  Product Name: Contraption
  SKU: SKU-1020
  Supplier Name: Wayne Enterprises
<start>
[
    {
        "Product Name": "Widget",
        "SKU": "SKU-1073",
        "Price": 223.0,
        "Category": "Household",
        "Supplier Name": "Wayne Enterprises"
    },
    {
        "Product Name": "Contraption",
        "SKU": "SKU-1000",
        "Price": 225.92,
        "Category": "Household",
        "Supplier Name": "Umbrella Corp"
    },
    {
        "Product Name": "Contraption",
        "SKU": "SKU-1020",
        "Price": 104.33,
        "Category": "Sports",
        "Supplier Name": "Wayne Enterprises"
    }
]
<end>Here's some Plain text data, can you convert it to Csv?
Location: Seattle | Condition: Foggy | Temperature (C): -4.8 | Humidity (%): 87 | Wind Speed (km/h): 2.3 | Day: Wednesday
Location: Phoenix | Condition: Rainy | Temperature (C): 36.2 | Humidity (%): 38 | Wind Speed (km/h): 22.0 | Day: Friday
Location: Miami | Condition: Cloudy | Temperature (C): 18.5 | Humidity (%): 33 | Wind Speed (km/h): 26.1 | Day: Friday
Location: Seattle | Condition: Rainy | Temperature (C): 6.3 | Humidity (%): 55 | Wind Speed (km/h): 18.8 | Day: Tuesday
Location: Denver | Condition: Stormy | Temperature (C): 32.4 | Humidity (%): 50 | Wind Speed (km/h): 11.5 | Day: Friday
Location: Chicago | Condition: Sunny | Temperature (C): 34.8 | Humidity (%): 38 | Wind Speed (km/h): 18.8 | Day: Thursday
Location: New York | Condition: Stormy | Temperature (C): 32.9 | Humidity (%): 43 | Wind Speed (km/h): 22.1 | Day: Monday
Location: Denver | Condition: Rainy | Temperature (C): 29.4 | Humidity (%): 96 | Wind Speed (km/h): 17.9 | Day: Sunday
Location: Miami | Condition: Windy | Temperature (C): 35.8 | Humidity (%): 88 | Wind Speed (km/h): 0.7 | Day: Wednesday
<start>
Location,Condition,Temperature (C),Humidity (%),Wind Speed (km/h),Day
Seattle,Foggy,-4.8,87,2.3,Wednesday
Phoenix,Rainy,36.2,38,22.0,Friday
Miami,Cloudy,18.5,33,26.1,Friday
Seattle,Rainy,6.3,55,18.8,Tuesday
Denver,Stormy,32.4,50,11.5,Friday
Chicago,Sunny,34.8,38,18.8,Thursday
New York,Stormy,32.9,43,22.1,Monday
Denver,Rainy,29.4,96,17.9,Sunday
Miami,Windy,35.8,88,0.7,Wednesday
<end>Here's some csv data, can you convert it to YAML?
SKU,Price,Stock Quantity
SKU-1088,234.29,385
SKU-1030,89.03,469
SKU-1099,489.43,464
SKU-1017,323.78,238
SKU-1083,404.37,328
SKU-1022,250.36,390
SKU-1007,41.11,26
<start>
- Price: 234.29
  SKU: SKU-1088
  Stock Quantity: 385
- Price: 89.03
  SKU: SKU-1030
  Stock Quantity: 469
- Price: 489.43
  SKU: SKU-1099
  Stock Quantity: 464
- Price: 323.78
  SKU: SKU-1017
  Stock Quantity: 238
- Price: 404.37
  SKU: SKU-1083
  Stock Quantity: 328
- Price: 250.36
  SKU: SKU-1022
  Stock Quantity: 390
- Price: 41.11
  SKU: SKU-1007
  Stock Quantity: 26
<end>Please transform the following PLAIN TEXT data into Yaml:
End Location: Houston | Distance (miles): 2852.6 | Duration (hours): 10.9 | Fuel Used (gallons): 89.4
End Location: Chicago | Distance (miles): 1272.2 | Duration (hours): 26.5 | Fuel Used (gallons): 8.6
End Location: Los Angeles | Distance (miles): 913.5 | Duration (hours): 17.1 | Fuel Used (gallons): 67.9
End Location: Chicago | Distance (miles): 758.5 | Duration (hours): 41.8 | Fuel Used (gallons): 15.8
End Location: San Francisco | Distance (miles): 791.9 | Duration (hours): 63.3 | Fuel Used (gallons): 8.4
End Location: New York | Distance (miles): 589.4 | Duration (hours): 43.0 | Fuel Used (gallons): 52.4
End Location: Chicago | Distance (miles): 805.9 | Duration (hours): 63.2 | Fuel Used (gallons): 30.7
End Location: Chicago | Distance (miles): 805.9 | Duration (hours): 45.2 | Fuel Used (gallons): 99.1
End Location: Denver | Distance (miles): 1967.9 | Duration (hours): 11.2 | Fuel Used (gallons): 68.8
<start>
- Distance (miles): 2852.6
  Duration (hours): 10.9
  End Location: Houston
  Fuel Used (gallons): 89.4
- Distance (miles): 1272.2
  Duration (hours): 26.5
  End Location: Chicago
  Fuel Used (gallons): 8.6
- Distance (miles): 913.5
  Duration (hours): 17.1
  End Location: Los Angeles
  Fuel Used (gallons): 67.9
- Distance (miles): 758.5
  Duration (hours): 41.8
  End Location: Chicago
  Fuel Used (gallons): 15.8
- Distance (miles): 791.9
  Duration (hours): 63.3
  End Location: San Francisco
  Fuel Used (gallons): 8.4
- Distance (miles): 589.4
  Duration (hours): 43.0
  End Location: New York
  Fuel Used (gallons): 52.4
- Distance (miles): 805.9
  Duration (hours): 63.2
  End Location: Chicago
  Fuel Used (gallons): 30.7
- Distance (miles): 805.9
  Duration (hours): 45.2
  End Location: Chicago
  Fuel Used (gallons): 99.1
- Distance (miles): 1967.9
  Duration (hours): 11.2
  End Location: Denver
  Fuel Used (gallons): 68.8
<end>Convert this markdown to json:
| Device ID | Device Type | Location | Battery Level (%) | Timestamp |
| --- | --- | --- | --- | --- |
| device-0002 | Temperature Sensor | Bathroom | 27.4 | 2021-04-10 07:07:11 |
| device-0088 | Motion Detector | Bathroom | 50.5 | 2021-06-23 12:59:14 |
| device-0053 | Light Sensor | Hallway | 27.4 | 2022-06-22 15:25:55 |
| device-0045 | Motion Detector | Living Room | 14.7 | 2021-03-27 13:28:53 |
| device-0025 | Humidity Sensor | Kitchen | 97.6 | 2021-01-08 18:07:34 |
| device-0081 | Temperature Sensor | Bathroom | 46.8 | 2022-08-06 03:51:54 |<start>
[
    {
        "Device ID": "device-0002",
        "Device Type": "Temperature Sensor",
        "Location": "Bathroom",
        "Battery Level (%)": 27.4,
        "Timestamp": "2021-04-10 07:07:11"
    },
    {
        "Device ID": "device-0088",
        "Device Type": "Motion Detector",
        "Location": "Bathroom",
        "Battery Level (%)": 50.5,
        "Timestamp": "2021-06-23 12:59:14"
    },
    {
        "Device ID": "device-0053",
        "Device Type": "Light Sensor",
        "Location": "Hallway",
        "Battery Level (%)": 27.4,
        "Timestamp": "2022-06-22 15:25:55"
    },
    {
        "Device ID": "device-0045",
        "Device Type": "Motion Detector",
        "Location": "Living Room",
        "Battery Level (%)": 14.7,
        "Timestamp": "2021-03-27 13:28:53"
    },
    {
        "Device ID": "device-0025",
        "Device Type": "Humidity Sensor",
        "Location": "Kitchen",
        "Battery Level (%)": 97.6,
        "Timestamp": "2021-01-08 18:07:34"
    },
    {
        "Device ID": "device-0081",
        "Device Type": "Temperature Sensor",
        "Location": "Bathroom",
        "Battery Level (%)": 46.8,
        "Timestamp": "2022-08-06 03:51:54"
    }
]
<end>Here's some yaml data, can you convert it to plain text?
- Birth Month: December
  Income: 110000
  Name: Cheryl
- Birth Month: December
  Income: 430000
  Name: Kylee
- Birth Month: March
  Income: 475000
  Name: Jeffrey
- Birth Month: September
  Income: 350000
  Name: Richard
<start>
Name: Cheryl | Birth Month: December | Income: 110000
Name: Kylee | Birth Month: December | Income: 430000
Name: Jeffrey | Birth Month: March | Income: 475000
Name: Richard | Birth Month: September | Income: 350000
<end>Please transform the following yml data into CSV:
- Birth Month: February
  City: Jacksonville
  Income: 100000
  Name: Spencer
- Birth Month: March
  City: Phoenix
  Income: 375000
  Name: Alvin
- Birth Month: April
  City: San Antonio
  Income: 440000
  Name: Claud
<start>
Name,Birth Month,City,Income
Spencer,February,Jacksonville,100000
Alvin,March,Phoenix,375000
Claud,April,San Antonio,440000
<end>Here's some JSON data, can you convert it to csv?
[
    {
        "Title": "The Forgotten World",
        "Genre": "Science Fiction",
        "Publication Year": 2016
    },
    {
        "Title": "Tales of the Brave",
        "Genre": "Historical",
        "Publication Year": 2003
    },
    {
        "Title": "Echoes of Eternity",
        "Genre": "Romance",
        "Publication Year": 1991
    }
]<start>
Title,Genre,Publication Year
The Forgotten World,Science Fiction,2016
Tales of the Brave,Historical,2003
Echoes of Eternity,Romance,1991
<end>Can you change this markdown into Plain text?
| Trip Name | Start Location | Duration (hours) |
| --- | --- | --- |
| City Explorer | Chicago | 51.0 |
| City Explorer | Houston | 57.0 |
| Historic Route | Los Angeles | 65.3 |
| Valley Voyage | New York | 48.4 |
| Valley Voyage | Los Angeles | 11.7 |
| City Explorer | Phoenix | 5.9 |
| Valley Voyage | Houston | 37.6 |
| Valley Voyage | San Francisco | 53.5 |
| Historic Route | Houston | 19.4 |
| Desert Drive | New York | 50.2 |<start>
Trip Name: City Explorer | Start Location: Chicago | Duration (hours): 51.0
Trip Name: City Explorer | Start Location: Houston | Duration (hours): 57.0
Trip Name: Historic Route | Start Location: Los Angeles | Duration (hours): 65.3
Trip Name: Valley Voyage | Start Location: New York | Duration (hours): 48.4
Trip Name: Valley Voyage | Start Location: Los Angeles | Duration (hours): 11.7
Trip Name: City Explorer | Start Location: Phoenix | Duration (hours): 5.9
Trip Name: Valley Voyage | Start Location: Houston | Duration (hours): 37.6
Trip Name: Valley Voyage | Start Location: San Francisco | Duration (hours): 53.5
Trip Name: Historic Route | Start Location: Houston | Duration (hours): 19.4
Trip Name: Desert Drive | Start Location: New York | Duration (hours): 50.2
<end>Here's some CSV data, can you convert it to json?
Device ID,Battery Level (%),Reading Value,Timestamp
device-0017,78.8,32.64,2021-08-11 09:22:02
device-0042,55.6,68.61,2022-02-09 17:04:48
device-0095,82.8,-27.95,2021-11-07 17:27:30
device-0040,23.1,66.04,2021-03-24 14:32:10
<start>
[
    {
        "Device ID": "device-0017",
        "Battery Level (%)": 78.8,
        "Reading Value": 32.64,
        "Timestamp": "2021-08-11 09:22:02"
    },
    {
        "Device ID": "device-0042",
        "Battery Level (%)": 55.6,
        "Reading Value": 68.61,
        "Timestamp": "2022-02-09 17:04:48"
    },
    {
        "Device ID": "device-0095",
        "Battery Level (%)": 82.8,
        "Reading Value": -27.95,
        "Timestamp": "2021-11-07 17:27:30"
    },
    {
        "Device ID": "device-0040",
        "Battery Level (%)": 23.1,
        "Reading Value": 66.04,
        "Timestamp": "2021-03-24 14:32:10"
    }
]
<end>Please transform the following csv data into YAML:
Company,Sector,Market Cap,Quarter
AutoDrive,Healthcare,Large Cap,Q4
AutoDrive,Technology,Mega Cap,Q1
TechCorp,Technology,Mega Cap,Q4
TechCorp,Biotech,Small Cap,Q1
AutoDrive,Energy,Small Cap,Q2
FinanceWorks,Automotive,Mid Cap,Q3
AeroSpace,Aerospace,Mega Cap,Q2
<start>
- Company: AutoDrive
  Market Cap: Large Cap
  Quarter: Q4
  Sector: Healthcare
- Company: AutoDrive
  Market Cap: Mega Cap
  Quarter: Q1
  Sector: Technology
- Company: TechCorp
  Market Cap: Mega Cap
  Quarter: Q4
  Sector: Technology
- Company: TechCorp
  Market Cap: Small Cap
  Quarter: Q1
  Sector: Biotech
- Company: AutoDrive
  Market Cap: Small Cap
  Quarter: Q2
  Sector: Energy
- Company: FinanceWorks
  Market Cap: Mid Cap
  Quarter: Q3
  Sector: Automotive
- Company: AeroSpace
  Market Cap: Mega Cap
  Quarter: Q2
  Sector: Aerospace
<end>Please transform the following yml data into Json:
- Distance (miles): 1078.9
  Duration (hours): 40.1
  End Location: Los Angeles
  Fuel Used (gallons): 86.9
  Trip Name: Lakeside Retreat
- Distance (miles): 587.7
  Duration (hours): 53.8
  End Location: Houston
  Fuel Used (gallons): 22.5
  Trip Name: Mountain Adventure
- Distance (miles): 376.5
  Duration (hours): 35.1
  End Location: Miami
  Fuel Used (gallons): 24.3
  Trip Name: Valley Voyage
- Distance (miles): 1466.1
  Duration (hours): 67.2
  End Location: Denver
  Fuel Used (gallons): 49.0
  Trip Name: Forest Journey
- Distance (miles): 2535.6
  Duration (hours): 27.5
  End Location: San Francisco
  Fuel Used (gallons): 60.8
  Trip Name: Valley Voyage
<start>
[
    {
        "Trip Name": "Lakeside Retreat",
        "End Location": "Los Angeles",
        "Distance (miles)": 1078.9,
        "Duration (hours)": 40.1,
        "Fuel Used (gallons)": 86.9
    },
    {
        "Trip Name": "Mountain Adventure",
        "End Location": "Houston",
        "Distance (miles)": 587.7,
        "Duration (hours)": 53.8,
        "Fuel Used (gallons)": 22.5
    },
    {
        "Trip Name": "Valley Voyage",
        "End Location": "Miami",
        "Distance (miles)": 376.5,
        "Duration (hours)": 35.1,
        "Fuel Used (gallons)": 24.3
    },
    {
        "Trip Name": "Forest Journey",
        "End Location": "Denver",
        "Distance (miles)": 1466.1,
        "Duration (hours)": 67.2,
        "Fuel Used (gallons)": 49.0
    },
    {
        "Trip Name": "Valley Voyage",
        "End Location": "San Francisco",
        "Distance (miles)": 2535.6,
        "Duration (hours)": 27.5,
        "Fuel Used (gallons)": 60.8
    }
]
<end>Here's some markdown data, can you convert it to Plain text?
| Date | Open Price | Close Price | High Price | Volume |
| --- | --- | --- | --- | --- |
| 2018-06-12 | 82.92 | 469.59 | 469.59 | 3494247 |
| 2016-12-12 | 548.33 | 203.83 | 1352.81 | 1556637 |
| 2015-11-05 | 1041.89 | 60.07 | 1041.89 | 6751375 |
| 2022-03-28 | 1419.37 | 642.44 | 1419.37 | 329152 |
| 2020-10-13 | 1151.14 | 855.64 | 1151.14 | 1764425 |<start>
Date: 2018-06-12 | Open Price: 82.92 | Close Price: 469.59 | High Price: 469.59 | Volume: 3494247
Date: 2016-12-12 | Open Price: 548.33 | Close Price: 203.83 | High Price: 1352.81 | Volume: 1556637
Date: 2015-11-05 | Open Price: 1041.89 | Close Price: 60.07 | High Price: 1041.89 | Volume: 6751375
Date: 2022-03-28 | Open Price: 1419.37 | Close Price: 642.44 | High Price: 1419.37 | Volume: 329152
Date: 2020-10-13 | Open Price: 1151.14 | Close Price: 855.64 | High Price: 1151.14 | Volume: 1764425
<end>Can you change this MARKDOWN into Plain text?
| Name | City |
| --- | --- |
| Austin | Louisville |
| Diego | Chicago |
| Randolph | Los Angeles |
| Santiago | Washington |<start>
Name: Austin | City: Louisville
Name: Diego | City: Chicago
Name: Randolph | City: Los Angeles
Name: Santiago | City: Washington
<end>Convert this yml to plain text:
- Price: 49.16
  SKU: SKU-1061
  Supplier Name: Globex
- Price: 287.9
  SKU: SKU-1035
  Supplier Name: ACME Corp
- Price: 341.52
  SKU: SKU-1056
  Supplier Name: Wonka Industries
- Price: 458.55
  SKU: SKU-1050
  Supplier Name: ACME Corp
- Price: 11.58
  SKU: SKU-1076
  Supplier Name: Wayne Enterprises
- Price: 284.74
  SKU: SKU-1020
  Supplier Name: Wonka Industries
<start>
SKU: SKU-1061 | Price: 49.16 | Supplier Name: Globex
SKU: SKU-1035 | Price: 287.9 | Supplier Name: ACME Corp
SKU: SKU-1056 | Price: 341.52 | Supplier Name: Wonka Industries
SKU: SKU-1050 | Price: 458.55 | Supplier Name: ACME Corp
SKU: SKU-1076 | Price: 11.58 | Supplier Name: Wayne Enterprises
SKU: SKU-1020 | Price: 284.74 | Supplier Name: Wonka Industries
<end>Can you change this JSON into markdown?
[
    {
        "Database Name": "InventoryDB",
        "Queries per Second": 4643.65,
        "Cache Hit Ratio (%)": 82.32,
        "Connection Count": 254,
        "Average Latency (ms)": 96.47
    },
    {
        "Database Name": "SalesDB",
        "Queries per Second": 3773.12,
        "Cache Hit Ratio (%)": 99.21,
        "Connection Count": 138,
        "Average Latency (ms)": 7.99
    },
    {
        "Database Name": "MetricsDB",
        "Queries per Second": 4037.17,
        "Cache Hit Ratio (%)": 88.3,
        "Connection Count": 142,
        "Average Latency (ms)": 47.1
    }
]<start>
| Database Name | Queries per Second | Cache Hit Ratio (%) | Connection Count | Average Latency (ms) |
| --- | --- | --- | --- | --- |
| InventoryDB | 4643.65 | 82.32 | 254 | 96.47 |
| SalesDB | 3773.12 | 99.21 | 138 | 7.99 |
| MetricsDB | 4037.17 | 88.3 | 142 | 47.1 |
<end>Can you change this json into MARKDOWN?
[
    {
        "Location": "Denver",
        "Condition": "Stormy",
        "Temperature (C)": 21.0,
        "Humidity (%)": 27,
        "Wind Speed (km/h)": 5.8,
        "Day": "Monday"
    },
    {
        "Location": "Denver",
        "Condition": "Cloudy",
        "Temperature (C)": 34.5,
        "Humidity (%)": 54,
        "Wind Speed (km/h)": 2.2,
        "Day": "Wednesday"
    },
    {
        "Location": "New York",
        "Condition": "Cloudy",
        "Temperature (C)": 14.0,
        "Humidity (%)": 75,
        "Wind Speed (km/h)": 12.7,
        "Day": "Saturday"
    },
    {
        "Location": "Phoenix",
        "Condition": "Sunny",
        "Temperature (C)": 21.2,
        "Humidity (%)": 54,
        "Wind Speed (km/h)": 28.1,
        "Day": "Saturday"
    },
    {
        "Location": "Phoenix",
        "Condition": "Sunny",
        "Temperature (C)": 13.2,
        "Humidity (%)": 63,
        "Wind Speed (km/h)": 9.8,
        "Day": "Tuesday"
    },
    {
        "Location": "Los Angeles",
        "Condition": "Foggy",
        "Temperature (C)": 10.9,
        "Humidity (%)": 88,
        "Wind Speed (km/h)": 22.4,
        "Day": "Saturday"
    },
    {
        "Location": "Phoenix",
        "Condition": "Windy",
        "Temperature (C)": 30.3,
        "Humidity (%)": 87,
        "Wind Speed (km/h)": 28.2,
        "Day": "Sunday"
    },
    {
        "Location": "Seattle",
        "Condition": "Sunny",
        "Temperature (C)": 2.9,
        "Humidity (%)": 92,
        "Wind Speed (km/h)": 4.1,
        "Day": "Saturday"
    },
    {
        "Location": "Denver",
        "Condition": "Sunny",
        "Temperature (C)": 34.5,
        "Humidity (%)": 84,
        "Wind Speed (km/h)": 10.7,
        "Day": "Thursday"
    },
    {
        "Location": "New York",
        "Condition": "Rainy",
        "Temperature (C)": -7.7,
        "Humidity (%)": 67,
        "Wind Speed (km/h)": 7.8,
        "Day": "Wednesday"
    }
]<start>
| Location | Condition | Temperature (C) | Humidity (%) | Wind Speed (km/h) | Day |
| --- | --- | --- | --- | --- | --- |
| Denver | Stormy | 21.0 | 27 | 5.8 | Monday |
| Denver | Cloudy | 34.5 | 54 | 2.2 | Wednesday |
| New York | Cloudy | 14.0 | 75 | 12.7 | Saturday |
| Phoenix | Sunny | 21.2 | 54 | 28.1 | Saturday |
| Phoenix | Sunny | 13.2 | 63 | 9.8 | Tuesday |
| Los Angeles | Foggy | 10.9 | 88 | 22.4 | Saturday |
| Phoenix | Windy | 30.3 | 87 | 28.2 | Sunday |
| Seattle | Sunny | 2.9 | 92 | 4.1 | Saturday |
| Denver | Sunny | 34.5 | 84 | 10.7 | Thursday |
| New York | Rainy | -7.7 | 67 | 7.8 | Wednesday |
<end>Can you change this Csv into markdown?
Trip Name,Start Location,Distance (miles),Duration (hours),Fuel Used (gallons)
Canyon Trek,Chicago,2883.1,4.1,28.8
Historic Route,Houston,2083.5,6.4,65.8
Lakeside Retreat,Miami,2414.0,66.5,67.5
Coast to Coast,New York,2399.8,31.3,46.9
Desert Drive,Miami,533.3,34.2,26.9
<start>
| Trip Name | Start Location | Distance (miles) | Duration (hours) | Fuel Used (gallons) |
| --- | --- | --- | --- | --- |
| Canyon Trek | Chicago | 2883.1 | 4.1 | 28.8 |
| Historic Route | Houston | 2083.5 | 6.4 | 65.8 |
| Lakeside Retreat | Miami | 2414.0 | 66.5 | 67.5 |
| Coast to Coast | New York | 2399.8 | 31.3 | 46.9 |
| Desert Drive | Miami | 533.3 | 34.2 | 26.9 |
<end>Here's some yml data, can you convert it to plain text?
- Category: Electronics
  Price: 123.68
  SKU: SKU-1009
  Stock Quantity: 208
  Supplier Name: Wonka Industries
- Category: Toys
  Price: 361.17
  SKU: SKU-1090
  Stock Quantity: 267
  Supplier Name: Umbrella Corp
- Category: Electronics
  Price: 25.74
  SKU: SKU-1034
  Stock Quantity: 347
  Supplier Name: ACME Corp
- Category: Household
  Price: 78.58
  SKU: SKU-1005
  Stock Quantity: 397
  Supplier Name: Wayne Enterprises
- Category: Automotive
  Price: 471.03
  SKU: SKU-1084
  Stock Quantity: 290
  Supplier Name: ACME Corp
<start>
SKU: SKU-1009 | Price: 123.68 | Stock Quantity: 208 | Category: Electronics | Supplier Name: Wonka Industries
SKU: SKU-1090 | Price: 361.17 | Stock Quantity: 267 | Category: Toys | Supplier Name: Umbrella Corp
SKU: SKU-1034 | Price: 25.74 | Stock Quantity: 347 | Category: Electronics | Supplier Name: ACME Corp
SKU: SKU-1005 | Price: 78.58 | Stock Quantity: 397 | Category: Household | Supplier Name: Wayne Enterprises
SKU: SKU-1084 | Price: 471.03 | Stock Quantity: 290 | Category: Automotive | Supplier Name: ACME Corp
<end>Here's some JSON data, can you convert it to PLAIN TEXT?
[
    {
        "Title": "Dreamwalker",
        "Genre": "Sci-Fi"
    },
    {
        "Title": "The Endless Horizon",
        "Genre": "Drama"
    },
    {
        "Title": "Beyond the Veil",
        "Genre": "Comedy"
    },
    {
        "Title": "Escape from Earth",
        "Genre": "Adventure"
    },
    {
        "Title": "The Great Expedition",
        "Genre": "Fantasy"
    },
    {
        "Title": "Edge of Infinity",
        "Genre": "Comedy"
    }
]<start>
Title: Dreamwalker | Genre: Sci-Fi
Title: The Endless Horizon | Genre: Drama
Title: Beyond the Veil | Genre: Comedy
Title: Escape from Earth | Genre: Adventure
Title: The Great Expedition | Genre: Fantasy
Title: Edge of Infinity | Genre: Comedy
<end>Transform this Markdown structure to a Plain text format:
| Device Type | Location | Battery Level (%) | Reading Value | Timestamp |
| --- | --- | --- | --- | --- |
| Humidity Sensor | Garage | 19.6 | 58.55 | 2022-05-14 20:47:20 |
| Temperature Sensor | Living Room | 32.7 | -7.63 | 2022-10-25 08:40:05 |
| Light Sensor | Bedroom | 72.9 | -14.9 | 2022-08-25 06:36:46 |
| Motion Detector | Garage | 80.4 | 40.51 | 2022-01-17 19:55:52 |
| Motion Detector | Garden | 83.6 | 73.81 | 2023-08-18 11:42:44 |
| Temperature Sensor | Living Room | 56.4 | 3.93 | 2022-05-23 01:46:45 |
| Light Sensor | Office | 45.8 | 0.27 | 2023-12-19 21:50:27 |
| Humidity Sensor | Bathroom | 52.2 | 4.59 | 2023-10-17 12:12:11 |
| Motion Detector | Garden | 95.2 | 24.72 | 2021-09-01 14:07:08 |
| Humidity Sensor | Bathroom | 11.9 | 3.73 | 2023-11-19 01:41:26 |<start>
Device Type: Humidity Sensor | Location: Garage | Battery Level (%): 19.6 | Reading Value: 58.55 | Timestamp: 2022-05-14 20:47:20
Device Type: Temperature Sensor | Location: Living Room | Battery Level (%): 32.7 | Reading Value: -7.63 | Timestamp: 2022-10-25 08:40:05
Device Type: Light Sensor | Location: Bedroom | Battery Level (%): 72.9 | Reading Value: -14.9 | Timestamp: 2022-08-25 06:36:46
Device Type: Motion Detector | Location: Garage | Battery Level (%): 80.4 | Reading Value: 40.51 | Timestamp: 2022-01-17 19:55:52
Device Type: Motion Detector | Location: Garden | Battery Level (%): 83.6 | Reading Value: 73.81 | Timestamp: 2023-08-18 11:42:44
Device Type: Temperature Sensor | Location: Living Room | Battery Level (%): 56.4 | Reading Value: 3.93 | Timestamp: 2022-05-23 01:46:45
Device Type: Light Sensor | Location: Office | Battery Level (%): 45.8 | Reading Value: 0.27 | Timestamp: 2023-12-19 21:50:27
Device Type: Humidity Sensor | Location: Bathroom | Battery Level (%): 52.2 | Reading Value: 4.59 | Timestamp: 2023-10-17 12:12:11
Device Type: Motion Detector | Location: Garden | Battery Level (%): 95.2 | Reading Value: 24.72 | Timestamp: 2021-09-01 14:07:08
Device Type: Humidity Sensor | Location: Bathroom | Battery Level (%): 11.9 | Reading Value: 3.73 | Timestamp: 2023-11-19 01:41:26
<end>Please transform the following json data into MARKDOWN:
[
    {
        "Database Name": "SessionsDB",
        "Queries per Second": 1800.25,
        "Cache Hit Ratio (%)": 89.2,
        "Connection Count": 287,
        "Timestamp": "2022-04-27 22:30:20"
    },
    {
        "Database Name": "SalesDB",
        "Queries per Second": 604.83,
        "Cache Hit Ratio (%)": 93.78,
        "Connection Count": 175,
        "Timestamp": "2022-09-09 02:44:44"
    },
    {
        "Database Name": "SessionsDB",
        "Queries per Second": 4541.78,
        "Cache Hit Ratio (%)": 75.51,
        "Connection Count": 420,
        "Timestamp": "2021-02-19 01:28:25"
    },
    {
        "Database Name": "SessionsDB",
        "Queries per Second": 836.75,
        "Cache Hit Ratio (%)": 98.6,
        "Connection Count": 201,
        "Timestamp": "2023-01-03 14:55:49"
    },
    {
        "Database Name": "ProductsDB",
        "Queries per Second": 4834.88,
        "Cache Hit Ratio (%)": 73.96,
        "Connection Count": 256,
        "Timestamp": "2022-11-22 01:28:14"
    },
    {
        "Database Name": "AnalyticsDB",
        "Queries per Second": 1716.66,
        "Cache Hit Ratio (%)": 96.53,
        "Connection Count": 399,
        "Timestamp": "2021-04-21 03:34:25"
    },
    {
        "Database Name": "MetricsDB",
        "Queries per Second": 4683.98,
        "Cache Hit Ratio (%)": 83.77,
        "Connection Count": 323,
        "Timestamp": "2021-03-16 10:39:19"
    },
    {
        "Database Name": "OrdersDB",
        "Queries per Second": 97.16,
        "Cache Hit Ratio (%)": 76.32,
        "Connection Count": 342,
        "Timestamp": "2022-06-26 09:26:10"
    }
]<start>
| Database Name | Queries per Second | Cache Hit Ratio (%) | Connection Count | Timestamp |
| --- | --- | --- | --- | --- |
| SessionsDB | 1800.25 | 89.2 | 287 | 2022-04-27 22:30:20 |
| SalesDB | 604.83 | 93.78 | 175 | 2022-09-09 02:44:44 |
| SessionsDB | 4541.78 | 75.51 | 420 | 2021-02-19 01:28:25 |
| SessionsDB | 836.75 | 98.6 | 201 | 2023-01-03 14:55:49 |
| ProductsDB | 4834.88 | 73.96 | 256 | 2022-11-22 01:28:14 |
| AnalyticsDB | 1716.66 | 96.53 | 399 | 2021-04-21 03:34:25 |
| MetricsDB | 4683.98 | 83.77 | 323 | 2021-03-16 10:39:19 |
| OrdersDB | 97.16 | 76.32 | 342 | 2022-06-26 09:26:10 |
<end>Transform this yml structure to a CSV format:
- Author: Draven Blackthorn
  Publication Year: 1971
  Rating: 1.6
  Title: Tales of the Brave
- Author: Elara Moonshadow
  Publication Year: 1963
  Rating: 1.8
  Title: The Silent Grove
- Author: Draven Blackthorn
  Publication Year: 1958
  Rating: 2.2
  Title: Shadows of Solitude
- Author: Draven Blackthorn
  Publication Year: 1991
  Rating: 5.0
  Title: The Crystal Key
- Author: Draven Blackthorn
  Publication Year: 2023
  Rating: 1.6
  Title: A Journey Through Time
- Author: Isla Windrider
  Publication Year: 1964
  Rating: 2.1
  Title: The Forgotten World
- Author: Galen Starfire
  Publication Year: 1950
  Rating: 2.9
  Title: Tales of the Brave
- Author: Isla Windrider
  Publication Year: 1961
  Rating: 2.3
  Title: A Journey Through Time
<start>
Title,Author,Publication Year,Rating
Tales of the Brave,Draven Blackthorn,1971,1.6
The Silent Grove,Elara Moonshadow,1963,1.8
Shadows of Solitude,Draven Blackthorn,1958,2.2
The Crystal Key,Draven Blackthorn,1991,5.0
A Journey Through Time,Draven Blackthorn,2023,1.6
The Forgotten World,Isla Windrider,1964,2.1
Tales of the Brave,Galen Starfire,1950,2.9
A Journey Through Time,Isla Windrider,1961,2.3
<end>Please transform the following YML data into CSV:
- Battery Level (%): 50.3
  Device ID: device-0026
  Device Type: Motion Detector
  Reading Value: 80.84
  Timestamp: '2021-03-02 10:26:19'
- Battery Level (%): 16.5
  Device ID: device-0083
  Device Type: Pressure Sensor
  Reading Value: 49.09
  Timestamp: '2022-08-03 18:17:24'
- Battery Level (%): 32.9
  Device ID: device-0060
  Device Type: Pressure Sensor
  Reading Value: 4.41
  Timestamp: '2021-03-23 15:13:44'
- Battery Level (%): 57.2
  Device ID: device-0085
  Device Type: Motion Detector
  Reading Value: 8.43
  Timestamp: '2023-02-04 23:39:47'
- Battery Level (%): 50.3
  Device ID: device-0068
  Device Type: Humidity Sensor
  Reading Value: 8.43
  Timestamp: '2023-01-07 09:41:48'
- Battery Level (%): 67.1
  Device ID: device-0032
  Device Type: Humidity Sensor
  Reading Value: 71.28
  Timestamp: '2021-02-13 01:50:16'
- Battery Level (%): 31.1
  Device ID: device-0036
  Device Type: Motion Detector
  Reading Value: 25.37
  Timestamp: '2021-10-28 14:16:57'
- Battery Level (%): 81.0
  Device ID: device-0042
  Device Type: Light Sensor
  Reading Value: 28.12
  Timestamp: '2023-05-27 02:43:26'
- Battery Level (%): 91.9
  Device ID: device-0047
  Device Type: Temperature Sensor
  Reading Value: -24.17
  Timestamp: '2022-10-27 02:31:41'
- Battery Level (%): 31.1
  Device ID: device-0099
  Device Type: Humidity Sensor
  Reading Value: 37.99
  Timestamp: '2023-02-27 07:43:44'
<start>
Device ID,Device Type,Battery Level (%),Reading Value,Timestamp
device-0026,Motion Detector,50.3,80.84,2021-03-02 10:26:19
device-0083,Pressure Sensor,16.5,49.09,2022-08-03 18:17:24
device-0060,Pressure Sensor,32.9,4.41,2021-03-23 15:13:44
device-0085,Motion Detector,57.2,8.43,2023-02-04 23:39:47
device-0068,Humidity Sensor,50.3,8.43,2023-01-07 09:41:48
device-0032,Humidity Sensor,67.1,71.28,2021-02-13 01:50:16
device-0036,Motion Detector,31.1,25.37,2021-10-28 14:16:57
device-0042,Light Sensor,81.0,28.12,2023-05-27 02:43:26
device-0047,Temperature Sensor,91.9,-24.17,2022-10-27 02:31:41
device-0099,Humidity Sensor,31.1,37.99,2023-02-27 07:43:44
<end>Transform this json structure to a plain text format:
[
    {
        "Restaurant Name": "The Steakhouse",
        "Cuisine": "American",
        "Location": "New York",
        "Rating": 2,
        "Price Range": "$$"
    },
    {
        "Restaurant Name": "Vegan Delight",
        "Cuisine": "Indian",
        "Location": "San Francisco",
        "Rating": 5,
        "Price Range": "$$"
    },
    {
        "Restaurant Name": "Pizza Planet",
        "Cuisine": "Mediterranean",
        "Location": "San Francisco",
        "Rating": 2,
        "Price Range": "$$$"
    },
    {
        "Restaurant Name": "Pasta Palace",
        "Cuisine": "American",
        "Location": "Miami",
        "Rating": 2,
        "Price Range": "$$$"
    },
    {
        "Restaurant Name": "Burger Haven",
        "Cuisine": "American",
        "Location": "Phoenix",
        "Rating": 4,
        "Price Range": "$$$"
    },
    {
        "Restaurant Name": "Burger Haven",
        "Cuisine": "Italian",
        "Location": "New York",
        "Rating": 5,
        "Price Range": "$$"
    },
    {
        "Restaurant Name": "Taco Town",
        "Cuisine": "Japanese",
        "Location": "Los Angeles",
        "Rating": 4,
        "Price Range": "$$"
    },
    {
        "Restaurant Name": "Curry Corner",
        "Cuisine": "Mediterranean",
        "Location": "Miami",
        "Rating": 4,
        "Price Range": "$$"
    },
    {
        "Restaurant Name": "Pizza Planet",
        "Cuisine": "Indian",
        "Location": "Phoenix",
        "Rating": 1,
        "Price Range": "$$$"
    }
]<start>
Restaurant Name: The Steakhouse | Cuisine: American | Location: New York | Rating: 2 | Price Range: $$
Restaurant Name: Vegan Delight | Cuisine: Indian | Location: San Francisco | Rating: 5 | Price Range: $$
Restaurant Name: Pizza Planet | Cuisine: Mediterranean | Location: San Francisco | Rating: 2 | Price Range: $$$
Restaurant Name: Pasta Palace | Cuisine: American | Location: Miami | Rating: 2 | Price Range: $$$
Restaurant Name: Burger Haven | Cuisine: American | Location: Phoenix | Rating: 4 | Price Range: $$$
Restaurant Name: Burger Haven | Cuisine: Italian | Location: New York | Rating: 5 | Price Range: $$
Restaurant Name: Taco Town | Cuisine: Japanese | Location: Los Angeles | Rating: 4 | Price Range: $$
Restaurant Name: Curry Corner | Cuisine: Mediterranean | Location: Miami | Rating: 4 | Price Range: $$
Restaurant Name: Pizza Planet | Cuisine: Indian | Location: Phoenix | Rating: 1 | Price Range: $$$
<end>Here's some json data, can you convert it to yml?
[
    {
        "Director": "Talon Blackthorn",
        "Genre": "Comedy"
    },
    {
        "Director": "Mara Moonshadow",
        "Genre": "Drama"
    },
    {
        "Director": "Mara Moonshadow",
        "Genre": "Action"
    },
    {
        "Director": "Drake Nightshade",
        "Genre": "Sci-Fi"
    },
    {
        "Director": "Lira Silverleaf",
        "Genre": "Action"
    },
    {
        "Director": "Cade Firebrand",
        "Genre": "Drama"
    },
    {
        "Director": "Aria Ravenwood",
        "Genre": "Action"
    },
    {
        "Director": "Mara Moonshadow",
        "Genre": "Horror"
    },
    {
        "Director": "Lira Silverleaf",
        "Genre": "Action"
    }
]<start>
- Director: Talon Blackthorn
  Genre: Comedy
- Director: Mara Moonshadow
  Genre: Drama
- Director: Mara Moonshadow
  Genre: Action
- Director: Drake Nightshade
  Genre: Sci-Fi
- Director: Lira Silverleaf
  Genre: Action
- Director: Cade Firebrand
  Genre: Drama
- Director: Aria Ravenwood
  Genre: Action
- Director: Mara Moonshadow
  Genre: Horror
- Director: Lira Silverleaf
  Genre: Action
<end>Can you change this PLAIN TEXT into Yml?
Date: 2014-06-24 | Open Price: 1094.51 | Close Price: 1217.02 | High Price: 1217.02 | Low Price: 828.37 | Volume: 5897585
Date: 2023-03-06 | Open Price: 1120.86 | Close Price: 945.23 | High Price: 1412.03 | Low Price: 945.23 | Volume: 2393178
Date: 2011-07-22 | Open Price: 1094.51 | Close Price: 1094.51 | High Price: 1094.51 | Low Price: 646.62 | Volume: 7776069
Date: 2013-11-04 | Open Price: 1120.86 | Close Price: 286.11 | High Price: 1120.86 | Low Price: 109.9 | Volume: 694294
Date: 2021-09-21 | Open Price: 883.26 | Close Price: 1390.18 | High Price: 1390.18 | Low Price: 60.9 | Volume: 7653034
Date: 2022-01-26 | Open Price: 396.28 | Close Price: 521.95 | High Price: 1176.92 | Low Price: 396.28 | Volume: 5150180
Date: 2021-08-09 | Open Price: 1330.14 | Close Price: 258.88 | High Price: 1330.14 | Low Price: 258.88 | Volume: 7117010
Date: 2014-08-26 | Open Price: 258.88 | Close Price: 1270.03 | High Price: 1270.03 | Low Price: 258.88 | Volume: 7776069
Date: 2023-01-23 | Open Price: 883.26 | Close Price: 286.11 | High Price: 883.26 | Low Price: 267.3 | Volume: 9626404
Date: 2023-04-26 | Open Price: 709.9 | Close Price: 74.75 | High Price: 709.9 | Low Price: 74.75 | Volume: 9032283
<start>
- Close Price: 1217.02
  Date: '2014-06-24'
  High Price: 1217.02
  Low Price: 828.37
  Open Price: 1094.51
  Volume: 5897585
- Close Price: 945.23
  Date: '2023-03-06'
  High Price: 1412.03
  Low Price: 945.23
  Open Price: 1120.86
  Volume: 2393178
- Close Price: 1094.51
  Date: '2011-07-22'
  High Price: 1094.51
  Low Price: 646.62
  Open Price: 1094.51
  Volume: 7776069
- Close Price: 286.11
  Date: '2013-11-04'
  High Price: 1120.86
  Low Price: 109.9
  Open Price: 1120.86
  Volume: 694294
- Close Price: 1390.18
  Date: '2021-09-21'
  High Price: 1390.18
  Low Price: 60.9
  Open Price: 883.26
  Volume: 7653034
- Close Price: 521.95
  Date: '2022-01-26'
  High Price: 1176.92
  Low Price: 396.28
  Open Price: 396.28
  Volume: 5150180
- Close Price: 258.88
  Date: '2021-08-09'
  High Price: 1330.14
  Low Price: 258.88
  Open Price: 1330.14
  Volume: 7117010
- Close Price: 1270.03
  Date: '2014-08-26'
  High Price: 1270.03
  Low Price: 258.88
  Open Price: 258.88
  Volume: 7776069
- Close Price: 286.11
  Date: '2023-01-23'
  High Price: 883.26
  Low Price: 267.3
  Open Price: 883.26
  Volume: 9626404
- Close Price: 74.75
  Date: '2023-04-26'
  High Price: 709.9
  Low Price: 74.75
  Open Price: 709.9
  Volume: 9032283
<end>Here's some plain text data, can you convert it to JSON?
Database Name: SessionsDB | Queries per Second: 1557.76 | Cache Hit Ratio (%): 92.15 | Connection Count: 189 | Average Latency (ms): 98.47 | Timestamp: 2023-05-04 06:47:06
Database Name: OrdersDB | Queries per Second: 4934.23 | Cache Hit Ratio (%): 87.99 | Connection Count: 465 | Average Latency (ms): 63.3 | Timestamp: 2021-03-18 21:30:42
Database Name: UserDB | Queries per Second: 144.16 | Cache Hit Ratio (%): 95.96 | Connection Count: 158 | Average Latency (ms): 55.42 | Timestamp: 2022-09-24 08:36:37
Database Name: ProductsDB | Queries per Second: 1286.86 | Cache Hit Ratio (%): 84.15 | Connection Count: 458 | Average Latency (ms): 41.93 | Timestamp: 2023-03-10 01:39:18
<start>
[
    {
        "Database Name": "SessionsDB",
        "Queries per Second": 1557.76,
        "Cache Hit Ratio (%)": 92.15,
        "Connection Count": 189,
        "Average Latency (ms)": 98.47,
        "Timestamp": "2023-05-04 06:47:06"
    },
    {
        "Database Name": "OrdersDB",
        "Queries per Second": 4934.23,
        "Cache Hit Ratio (%)": 87.99,
        "Connection Count": 465,
        "Average Latency (ms)": 63.3,
        "Timestamp": "2021-03-18 21:30:42"
    },
    {
        "Database Name": "UserDB",
        "Queries per Second": 144.16,
        "Cache Hit Ratio (%)": 95.96,
        "Connection Count": 158,
        "Average Latency (ms)": 55.42,
        "Timestamp": "2022-09-24 08:36:37"
    },
    {
        "Database Name": "ProductsDB",
        "Queries per Second": 1286.86,
        "Cache Hit Ratio (%)": 84.15,
        "Connection Count": 458,
        "Average Latency (ms)": 41.93,
        "Timestamp": "2023-03-10 01:39:18"
    }
]
<end>Can you change this csv into Yaml?
Database Name,Queries per Second,Cache Hit Ratio (%),Average Latency (ms),Timestamp
LogsDB,2527.67,97.19,94.35,2022-12-26 00:53:25
SessionsDB,4471.05,83.37,40.02,2023-02-24 22:18:14
ProfilesDB,2527.67,98.05,91.53,2023-10-02 08:03:46
SessionsDB,2037.99,75.86,1.89,2021-11-19 17:08:58
SessionsDB,533.08,99.19,70.36,2021-10-08 09:47:29
ProductsDB,2076.6,77.14,24.05,2022-10-26 05:46:16
ProfilesDB,2202.71,75.4,86.48,2022-11-26 21:30:39
ProductsDB,2007.89,95.34,23.71,2022-09-11 19:34:19
MetricsDB,558.05,72.6,44.48,2021-03-08 07:04:28
OrdersDB,3741.16,79.82,91.53,2023-09-03 01:33:23
<start>
- Average Latency (ms): 94.35
  Cache Hit Ratio (%): 97.19
  Database Name: LogsDB
  Queries per Second: 2527.67
  Timestamp: '2022-12-26 00:53:25'
- Average Latency (ms): 40.02
  Cache Hit Ratio (%): 83.37
  Database Name: SessionsDB
  Queries per Second: 4471.05
  Timestamp: '2023-02-24 22:18:14'
- Average Latency (ms): 91.53
  Cache Hit Ratio (%): 98.05
  Database Name: ProfilesDB
  Queries per Second: 2527.67
  Timestamp: '2023-10-02 08:03:46'
- Average Latency (ms): 1.89
  Cache Hit Ratio (%): 75.86
  Database Name: SessionsDB
  Queries per Second: 2037.99
  Timestamp: '2021-11-19 17:08:58'
- Average Latency (ms): 70.36
  Cache Hit Ratio (%): 99.19
  Database Name: SessionsDB
  Queries per Second: 533.08
  Timestamp: '2021-10-08 09:47:29'
- Average Latency (ms): 24.05
  Cache Hit Ratio (%): 77.14
  Database Name: ProductsDB
  Queries per Second: 2076.6
  Timestamp: '2022-10-26 05:46:16'
- Average Latency (ms): 86.48
  Cache Hit Ratio (%): 75.4
  Database Name: ProfilesDB
  Queries per Second: 2202.71
  Timestamp: '2022-11-26 21:30:39'
- Average Latency (ms): 23.71
  Cache Hit Ratio (%): 95.34
  Database Name: ProductsDB
  Queries per Second: 2007.89
  Timestamp: '2022-09-11 19:34:19'
- Average Latency (ms): 44.48
  Cache Hit Ratio (%): 72.6
  Database Name: MetricsDB
  Queries per Second: 558.05
  Timestamp: '2021-03-08 07:04:28'
- Average Latency (ms): 91.53
  Cache Hit Ratio (%): 79.82
  Database Name: OrdersDB
  Queries per Second: 3741.16
  Timestamp: '2023-09-03 01:33:23'
<end>Transform this CSV structure to a json format:
Company,Date,Close Price,High Price,Volume
GreenEnergy,2011-07-22,315.44,1448.61,4914323
AutoMotive,2015-09-25,646.9,866.32,4208754
FinanceTrust,2019-10-18,886.8,1464.22,2831378
FoodChain,2022-09-04,1482.38,1482.38,6842701
AeroSystems,2015-12-10,178.29,1307.14,432538
MediaGroup,2021-01-21,507.93,507.93,1733047
AutoMotive,2015-12-23,1496.6,1496.6,1935018
<start>
[
    {
        "Company": "GreenEnergy",
        "Date": "2011-07-22",
        "Close Price": 315.44,
        "High Price": 1448.61,
        "Volume": 4914323
    },
    {
        "Company": "AutoMotive",
        "Date": "2015-09-25",
        "Close Price": 646.9,
        "High Price": 866.32,
        "Volume": 4208754
    },
    {
        "Company": "FinanceTrust",
        "Date": "2019-10-18",
        "Close Price": 886.8,
        "High Price": 1464.22,
        "Volume": 2831378
    },
    {
        "Company": "FoodChain",
        "Date": "2022-09-04",
        "Close Price": 1482.38,
        "High Price": 1482.38,
        "Volume": 6842701
    },
    {
        "Company": "AeroSystems",
        "Date": "2015-12-10",
        "Close Price": 178.29,
        "High Price": 1307.14,
        "Volume": 432538
    },
    {
        "Company": "MediaGroup",
        "Date": "2021-01-21",
        "Close Price": 507.93,
        "High Price": 507.93,
        "Volume": 1733047
    },
    {
        "Company": "AutoMotive",
        "Date": "2015-12-23",
        "Close Price": 1496.6,
        "High Price": 1496.6,
        "Volume": 1935018
    }
]
<end>Transform this json structure to a yml format:
[
    {
        "Restaurant Name": "The Golden Spoon",
        "Cuisine": "Indian"
    },
    {
        "Restaurant Name": "The Steakhouse",
        "Cuisine": "Japanese"
    },
    {
        "Restaurant Name": "Taco Town",
        "Cuisine": "American"
    },
    {
        "Restaurant Name": "Pasta Palace",
        "Cuisine": "Mexican"
    },
    {
        "Restaurant Name": "Vegan Delight",
        "Cuisine": "Indian"
    },
    {
        "Restaurant Name": "BBQ Barn",
        "Cuisine": "Chinese"
    }
]<start>
- Cuisine: Indian
  Restaurant Name: The Golden Spoon
- Cuisine: Japanese
  Restaurant Name: The Steakhouse
- Cuisine: American
  Restaurant Name: Taco Town
- Cuisine: Mexican
  Restaurant Name: Pasta Palace
- Cuisine: Indian
  Restaurant Name: Vegan Delight
- Cuisine: Chinese
  Restaurant Name: BBQ Barn
<end>Here's some Csv data, can you convert it to json?
Name,Age,Birth Month,Income
Juanita,43,September,235000
Myrtle,65,January,375000
Kevin,35,December,485000
Miles,27,June,90000
Martin,26,October,190000
Aliyah,65,August,235000
Brody,35,December,400000
<start>
[
    {
        "Name": "Juanita",
        "Age": 43,
        "Birth Month": "September",
        "Income": 235000
    },
    {
        "Name": "Myrtle",
        "Age": 65,
        "Birth Month": "January",
        "Income": 375000
    },
    {
        "Name": "Kevin",
        "Age": 35,
        "Birth Month": "December",
        "Income": 485000
    },
    {
        "Name": "Miles",
        "Age": 27,
        "Birth Month": "June",
        "Income": 90000
    },
    {
        "Name": "Martin",
        "Age": 26,
        "Birth Month": "October",
        "Income": 190000
    },
    {
        "Name": "Aliyah",
        "Age": 65,
        "Birth Month": "August",
        "Income": 235000
    },
    {
        "Name": "Brody",
        "Age": 35,
        "Birth Month": "December",
        "Income": 400000
    }
]
<end>Please transform the following Markdown data into Json:
| Company | Date | Close Price | High Price | Low Price | Volume |
| --- | --- | --- | --- | --- | --- |
| FinanceTrust | 2015-12-23 | 149.07 | 822.49 | 149.07 | 5402361 |
| TechnoCorp | 2021-07-22 | 898.45 | 910.95 | 655.64 | 1130976 |
| HealthGen | 2013-11-12 | 109.01 | 1308.7 | 109.01 | 9050586 |<start>
[
    {
        "Company": "FinanceTrust",
        "Date": "2015-12-23",
        "Close Price": 149.07,
        "High Price": 822.49,
        "Low Price": 149.07,
        "Volume": 5402361
    },
    {
        "Company": "TechnoCorp",
        "Date": "2021-07-22",
        "Close Price": 898.45,
        "High Price": 910.95,
        "Low Price": 655.64,
        "Volume": 1130976
    },
    {
        "Company": "HealthGen",
        "Date": "2013-11-12",
        "Close Price": 109.01,
        "High Price": 1308.7,
        "Low Price": 109.01,
        "Volume": 9050586
    }
]
<end>Here's some markdown data, can you convert it to YAML?
| Product Name | SKU | Price | Stock Quantity | Category | Supplier Name |
| --- | --- | --- | --- | --- | --- |
| Gadget | SKU-1059 | 72.18 | 134 | Household | Umbrella Corp |
| Gizmo | SKU-1022 | 289.0 | 436 | Sports | Umbrella Corp |
| Device | SKU-1096 | 118.72 | 66 | Automotive | Wonka Industries |
| Gadget | SKU-1030 | 267.28 | 432 | Automotive | Wonka Industries |
| Widget | SKU-1002 | 200.45 | 397 | Automotive | Umbrella Corp |
| Thingamajig | SKU-1095 | 394.16 | 341 | Electronics | Umbrella Corp |
| Apparatus | SKU-1049 | 257.28 | 1 | Household | Wayne Enterprises |<start>
- Category: Household
  Price: 72.18
  Product Name: Gadget
  SKU: SKU-1059
  Stock Quantity: 134
  Supplier Name: Umbrella Corp
- Category: Sports
  Price: 289.0
  Product Name: Gizmo
  SKU: SKU-1022
  Stock Quantity: 436
  Supplier Name: Umbrella Corp
- Category: Automotive
  Price: 118.72
  Product Name: Device
  SKU: SKU-1096
  Stock Quantity: 66
  Supplier Name: Wonka Industries
- Category: Automotive
  Price: 267.28
  Product Name: Gadget
  SKU: SKU-1030
  Stock Quantity: 432
  Supplier Name: Wonka Industries
- Category: Automotive
  Price: 200.45
  Product Name: Widget
  SKU: SKU-1002
  Stock Quantity: 397
  Supplier Name: Umbrella Corp
- Category: Electronics
  Price: 394.16
  Product Name: Thingamajig
  SKU: SKU-1095
  Stock Quantity: 341
  Supplier Name: Umbrella Corp
- Category: Household
  Price: 257.28
  Product Name: Apparatus
  SKU: SKU-1049
  Stock Quantity: 1
  Supplier Name: Wayne Enterprises
<end>Transform this markdown structure to a PLAIN TEXT format:
| Title | Genre |
| --- | --- |
| Legends of the Rift | Fantasy |
| Tales of the Brave | Historical |
| Echoes of Eternity | Science Fiction |
| Tales of the Brave | Non-Fiction |
| The Crystal Key | Thriller |
| The Silent Grove | Historical |
| The Last Sky | Non-Fiction |
| The Crystal Key | Mystery |<start>
Title: Legends of the Rift | Genre: Fantasy
Title: Tales of the Brave | Genre: Historical
Title: Echoes of Eternity | Genre: Science Fiction
Title: Tales of the Brave | Genre: Non-Fiction
Title: The Crystal Key | Genre: Thriller
Title: The Silent Grove | Genre: Historical
Title: The Last Sky | Genre: Non-Fiction
Title: The Crystal Key | Genre: Mystery
<end>Here's some json data, can you convert it to plain text?
[
    {
        "Company": "AutoDrive",
        "Stock Price": 556.55,
        "Quarter": "Q3"
    },
    {
        "Company": "FinanceWorks",
        "Stock Price": 286.51,
        "Quarter": "Q3"
    },
    {
        "Company": "AutoDrive",
        "Stock Price": 797.2,
        "Quarter": "Q4"
    },
    {
        "Company": "TechCorp",
        "Stock Price": 830.28,
        "Quarter": "Q1"
    },
    {
        "Company": "RetailHub",
        "Stock Price": 913.94,
        "Quarter": "Q4"
    }
]<start>
Company: AutoDrive | Stock Price: 556.55 | Quarter: Q3
Company: FinanceWorks | Stock Price: 286.51 | Quarter: Q3
Company: AutoDrive | Stock Price: 797.2 | Quarter: Q4
Company: TechCorp | Stock Price: 830.28 | Quarter: Q1
Company: RetailHub | Stock Price: 913.94 | Quarter: Q4
<end>Transform this Plain text structure to a yml format:
Company: TechnoCorp | Date: 2013-09-13 | Open Price: 1485.16 | Close Price: 184.3 | High Price: 1485.16 | Low Price: 184.3 | Volume: 1333558
Company: MediaGroup | Date: 2015-10-14 | Open Price: 977.14 | Close Price: 583.77 | High Price: 1485.16 | Low Price: 343.21 | Volume: 7277856
Company: GreenEnergy | Date: 2023-02-18 | Open Price: 587.3 | Close Price: 1481.79 | High Price: 1481.79 | Low Price: 587.3 | Volume: 726893
Company: FinanceTrust | Date: 2021-10-16 | Open Price: 1392.93 | Close Price: 252.71 | High Price: 1392.93 | Low Price: 252.71 | Volume: 1687688
Company: FoodChain | Date: 2018-11-05 | Open Price: 574.52 | Close Price: 1461.23 | High Price: 1461.23 | Low Price: 574.52 | Volume: 4484627
<start>
- Close Price: 184.3
  Company: TechnoCorp
  Date: '2013-09-13'
  High Price: 1485.16
  Low Price: 184.3
  Open Price: 1485.16
  Volume: 1333558
- Close Price: 583.77
  Company: MediaGroup
  Date: '2015-10-14'
  High Price: 1485.16
  Low Price: 343.21
  Open Price: 977.14
  Volume: 7277856
- Close Price: 1481.79
  Company: GreenEnergy
  Date: '2023-02-18'
  High Price: 1481.79
  Low Price: 587.3
  Open Price: 587.3
  Volume: 726893
- Close Price: 252.71
  Company: FinanceTrust
  Date: '2021-10-16'
  High Price: 1392.93
  Low Price: 252.71
  Open Price: 1392.93
  Volume: 1687688
- Close Price: 1461.23
  Company: FoodChain
  Date: '2018-11-05'
  High Price: 1461.23
  Low Price: 574.52
  Open Price: 574.52
  Volume: 4484627
<end>Can you change this PLAIN TEXT into markdown?
Cuisine: Chinese | Price Range: $$$$
Cuisine: Indian | Price Range: $
Cuisine: Chinese | Price Range: $$$
Cuisine: Italian | Price Range: $
Cuisine: Japanese | Price Range: $$$
Cuisine: Mexican | Price Range: $$$$$
Cuisine: American | Price Range: $$$$
<start>
| Cuisine | Price Range |
| --- | --- |
| Chinese | $$$$ |
| Indian | $ |
| Chinese | $$$ |
| Italian | $ |
| Japanese | $$$ |
| Mexican | $$$$$ |
| American | $$$$ |
<end>Please transform the following csv data into json:
Title,Genre,Rating
The Forgotten World,Mystery,2.0
The Forgotten World,Non-Fiction,1.2
A Journey Through Time,Thriller,1.8
Tales of the Brave,Thriller,3.5
A Journey Through Time,Historical,1.8
Legends of the Rift,Historical,4.0
A Journey Through Time,Fantasy,4.8
Echoes of Eternity,Mystery,2.0
<start>
[
    {
        "Title": "The Forgotten World",
        "Genre": "Mystery",
        "Rating": 2.0
    },
    {
        "Title": "The Forgotten World",
        "Genre": "Non-Fiction",
        "Rating": 1.2
    },
    {
        "Title": "A Journey Through Time",
        "Genre": "Thriller",
        "Rating": 1.8
    },
    {
        "Title": "Tales of the Brave",
        "Genre": "Thriller",
        "Rating": 3.5
    },
    {
        "Title": "A Journey Through Time",
        "Genre": "Historical",
        "Rating": 1.8
    },
    {
        "Title": "Legends of the Rift",
        "Genre": "Historical",
        "Rating": 4.0
    },
    {
        "Title": "A Journey Through Time",
        "Genre": "Fantasy",
        "Rating": 4.8
    },
    {
        "Title": "Echoes of Eternity",
        "Genre": "Mystery",
        "Rating": 2.0
    }
]
<end>Here's some yml data, can you convert it to MARKDOWN?
- Cuisine: French
  Location: Los Angeles
  Restaurant Name: Sushi World
- Cuisine: Indian
  Location: San Francisco
  Restaurant Name: The Golden Spoon
- Cuisine: Indian
  Location: Houston
  Restaurant Name: Vegan Delight
- Cuisine: Japanese
  Location: New York
  Restaurant Name: Burger Haven
<start>
| Restaurant Name | Cuisine | Location |
| --- | --- | --- |
| Sushi World | French | Los Angeles |
| The Golden Spoon | Indian | San Francisco |
| Vegan Delight | Indian | Houston |
| Burger Haven | Japanese | New York |
<end>Here's some Markdown data, can you convert it to CSV?
| Device ID | Device Type | Battery Level (%) | Timestamp |
| --- | --- | --- | --- |
| device-0013 | Light Sensor | 87.8 | 2021-01-08 17:08:22 |
| device-0026 | Light Sensor | 22.1 | 2021-03-21 18:16:14 |
| device-0035 | Humidity Sensor | 52.0 | 2022-06-02 03:49:00 |
| device-0022 | Temperature Sensor | 55.1 | 2022-02-18 03:05:34 |
| device-0097 | Temperature Sensor | 21.6 | 2023-04-16 21:07:43 |<start>
Device ID,Device Type,Battery Level (%),Timestamp
device-0013,Light Sensor,87.8,2021-01-08 17:08:22
device-0026,Light Sensor,22.1,2021-03-21 18:16:14
device-0035,Humidity Sensor,52.0,2022-06-02 03:49:00
device-0022,Temperature Sensor,55.1,2022-02-18 03:05:34
device-0097,Temperature Sensor,21.6,2023-04-16 21:07:43
<end>Can you change this plain text into markdown?
Trip Name: Lakeside Retreat | Start Location: Phoenix | End Location: New York | Distance (miles): 1462.9 | Duration (hours): 12.9 | Fuel Used (gallons): 15.0
Trip Name: Coast to Coast | Start Location: Los Angeles | End Location: Phoenix | Distance (miles): 2036.2 | Duration (hours): 31.4 | Fuel Used (gallons): 71.1
Trip Name: Valley Voyage | Start Location: Chicago | End Location: New York | Distance (miles): 1970.0 | Duration (hours): 19.7 | Fuel Used (gallons): 9.6
Trip Name: Desert Drive | Start Location: New York | End Location: Miami | Distance (miles): 1003.9 | Duration (hours): 29.3 | Fuel Used (gallons): 71.1
<start>
| Trip Name | Start Location | End Location | Distance (miles) | Duration (hours) | Fuel Used (gallons) |
| --- | --- | --- | --- | --- | --- |
| Lakeside Retreat | Phoenix | New York | 1462.9 | 12.9 | 15.0 |
| Coast to Coast | Los Angeles | Phoenix | 2036.2 | 31.4 | 71.1 |
| Valley Voyage | Chicago | New York | 1970.0 | 19.7 | 9.6 |
| Desert Drive | New York | Miami | 1003.9 | 29.3 | 71.1 |
<end>Please transform the following YML data into PLAIN TEXT:
- Box Office Earnings (M): 197.07
  Director: Zara Stormrider
  Genre: Horror
  Release Year: 1970
  Title: Beyond the Veil
- Box Office Earnings (M): 45.74
  Director: Lira Silverleaf
  Genre: Sci-Fi
  Release Year: 2021
  Title: The Endless Horizon
- Box Office Earnings (M): 784.89
  Director: Lira Silverleaf
  Genre: Adventure
  Release Year: 2009
  Title: The Endless Horizon
- Box Office Earnings (M): 627.6
  Director: Mara Moonshadow
  Genre: Action
  Release Year: 2022
  Title: Dreamwalker
- Box Office Earnings (M): 526.14
  Director: Zara Stormrider
  Genre: Thriller
  Release Year: 1986
  Title: Starbound Odyssey
- Box Office Earnings (M): 615.8
  Director: Zara Stormrider
  Genre: Comedy
  Release Year: 2019
  Title: The Final Voyage
- Box Office Earnings (M): 45.74
  Director: Cade Firebrand
  Genre: Horror
  Release Year: 1978
  Title: Edge of Infinity
<start>
Title: Beyond the Veil | Director: Zara Stormrider | Genre: Horror | Release Year: 1970 | Box Office Earnings (M): 197.07
Title: The Endless Horizon | Director: Lira Silverleaf | Genre: Sci-Fi | Release Year: 2021 | Box Office Earnings (M): 45.74
Title: The Endless Horizon | Director: Lira Silverleaf | Genre: Adventure | Release Year: 2009 | Box Office Earnings (M): 784.89
Title: Dreamwalker | Director: Mara Moonshadow | Genre: Action | Release Year: 2022 | Box Office Earnings (M): 627.6
Title: Starbound Odyssey | Director: Zara Stormrider | Genre: Thriller | Release Year: 1986 | Box Office Earnings (M): 526.14
Title: The Final Voyage | Director: Zara Stormrider | Genre: Comedy | Release Year: 2019 | Box Office Earnings (M): 615.8
Title: Edge of Infinity | Director: Cade Firebrand | Genre: Horror | Release Year: 1978 | Box Office Earnings (M): 45.74
<end>Convert this plain text to Json:
Product Name: Gizmo | Price: 320.04 | Category: Sports | Supplier Name: Umbrella Corp
Product Name: Gizmo | Price: 463.17 | Category: Household | Supplier Name: Globex
Product Name: Gizmo | Price: 90.38 | Category: Household | Supplier Name: ACME Corp
Product Name: Gizmo | Price: 383.5 | Category: Electronics | Supplier Name: Globex
Product Name: Gadget | Price: 49.93 | Category: Automotive | Supplier Name: Wonka Industries
Product Name: Contraption | Price: 11.71 | Category: Toys | Supplier Name: ACME Corp
Product Name: Widget | Price: 95.67 | Category: Automotive | Supplier Name: ACME Corp
Product Name: Widget | Price: 24.45 | Category: Automotive | Supplier Name: ACME Corp
Product Name: Gadget | Price: 322.65 | Category: Household | Supplier Name: Wayne Enterprises
Product Name: Apparatus | Price: 270.02 | Category: Household | Supplier Name: Globex
<start>
[
    {
        "Product Name": "Gizmo",
        "Price": 320.04,
        "Category": "Sports",
        "Supplier Name": "Umbrella Corp"
    },
    {
        "Product Name": "Gizmo",
        "Price": 463.17,
        "Category": "Household",
        "Supplier Name": "Globex"
    },
    {
        "Product Name": "Gizmo",
        "Price": 90.38,
        "Category": "Household",
        "Supplier Name": "ACME Corp"
    },
    {
        "Product Name": "Gizmo",
        "Price": 383.5,
        "Category": "Electronics",
        "Supplier Name": "Globex"
    },
    {
        "Product Name": "Gadget",
        "Price": 49.93,
        "Category": "Automotive",
        "Supplier Name": "Wonka Industries"
    },
    {
        "Product Name": "Contraption",
        "Price": 11.71,
        "Category": "Toys",
        "Supplier Name": "ACME Corp"
    },
    {
        "Product Name": "Widget",
        "Price": 95.67,
        "Category": "Automotive",
        "Supplier Name": "ACME Corp"
    },
    {
        "Product Name": "Widget",
        "Price": 24.45,
        "Category": "Automotive",
        "Supplier Name": "ACME Corp"
    },
    {
        "Product Name": "Gadget",
        "Price": 322.65,
        "Category": "Household",
        "Supplier Name": "Wayne Enterprises"
    },
    {
        "Product Name": "Apparatus",
        "Price": 270.02,
        "Category": "Household",
        "Supplier Name": "Globex"
    }
]
<end>Convert this Markdown to yml:
| Location | Temperature (C) | Humidity (%) |
| --- | --- | --- |
| New York | -3.8 | 79 |
| New York | -3.3 | 86 |
| Los Angeles | 16.9 | 59 |
| Chicago | 4.8 | 33 |
| Seattle | 24.2 | 50 |
| Houston | 2.6 | 92 |
| Seattle | -1.7 | 42 |
| Los Angeles | -8.9 | 24 |<start>
- Humidity (%): 79
  Location: New York
  Temperature (C): -3.8
- Humidity (%): 86
  Location: New York
  Temperature (C): -3.3
- Humidity (%): 59
  Location: Los Angeles
  Temperature (C): 16.9
- Humidity (%): 33
  Location: Chicago
  Temperature (C): 4.8
- Humidity (%): 50
  Location: Seattle
  Temperature (C): 24.2
- Humidity (%): 92
  Location: Houston
  Temperature (C): 2.6
- Humidity (%): 42
  Location: Seattle
  Temperature (C): -1.7
- Humidity (%): 24
  Location: Los Angeles
  Temperature (C): -8.9
<end>Can you change this YML into markdown?
- Annual Revenue (B): 411.87
  Sector: Healthcare
  Stock Price: 972.0
- Annual Revenue (B): 411.87
  Sector: Healthcare
  Stock Price: 494.09
- Annual Revenue (B): 55.75
  Sector: Energy
  Stock Price: 396.0
- Annual Revenue (B): 169.04
  Sector: Technology
  Stock Price: 458.44
- Annual Revenue (B): 332.64
  Sector: Healthcare
  Stock Price: 681.68
- Annual Revenue (B): 128.25
  Sector: Technology
  Stock Price: 796.23
- Annual Revenue (B): 449.45
  Sector: Healthcare
  Stock Price: 971.93
<start>
| Sector | Stock Price | Annual Revenue (B) |
| --- | --- | --- |
| Healthcare | 972.0 | 411.87 |
| Healthcare | 494.09 | 411.87 |
| Energy | 396.0 | 55.75 |
| Technology | 458.44 | 169.04 |
| Healthcare | 681.68 | 332.64 |
| Technology | 796.23 | 128.25 |
| Healthcare | 971.93 | 449.45 |
<end>Can you change this plain text into yaml?
Restaurant Name: Curry Corner | Location: Phoenix | Rating: 5 | Price Range: $
Restaurant Name: Pizza Planet | Location: Houston | Rating: 1 | Price Range: $$$$
Restaurant Name: BBQ Barn | Location: Miami | Rating: 2 | Price Range: $$$
Restaurant Name: The Golden Spoon | Location: Houston | Rating: 2 | Price Range: $$
Restaurant Name: Taco Town | Location: Los Angeles | Rating: 3 | Price Range: $$$$$
Restaurant Name: Pizza Planet | Location: Los Angeles | Rating: 1 | Price Range: $
Restaurant Name: The Golden Spoon | Location: New York | Rating: 4 | Price Range: $
<start>
- Location: Phoenix
  Price Range: $
  Rating: 5
  Restaurant Name: Curry Corner
- Location: Houston
  Price Range: $$$$
  Rating: 1
  Restaurant Name: Pizza Planet
- Location: Miami
  Price Range: $$$
  Rating: 2
  Restaurant Name: BBQ Barn
- Location: Houston
  Price Range: $$
  Rating: 2
  Restaurant Name: The Golden Spoon
- Location: Los Angeles
  Price Range: $$$$$
  Rating: 3
  Restaurant Name: Taco Town
- Location: Los Angeles
  Price Range: $
  Rating: 1
  Restaurant Name: Pizza Planet
- Location: New York
  Price Range: $
  Rating: 4
  Restaurant Name: The Golden Spoon
<end>Transform this markdown structure to a CSV format:
| Location | Price Range |
| --- | --- |
| San Francisco | $$$$$ |
| Houston | $$$$ |
| Houston | $$$$$ |
| Miami | $$$$$ |<start>
Location,Price Range
San Francisco,$$$$$
Houston,$$$$
Houston,$$$$$
Miami,$$$$$
<end>Please transform the following json data into Yml:
[
    {
        "Trip Name": "Forest Journey",
        "Start Location": "Los Angeles",
        "End Location": "Houston",
        "Distance (miles)": 2814.7,
        "Duration (hours)": 4.7,
        "Fuel Used (gallons)": 75.1
    },
    {
        "Trip Name": "Valley Voyage",
        "Start Location": "Los Angeles",
        "End Location": "Denver",
        "Distance (miles)": 156.7,
        "Duration (hours)": 14.4,
        "Fuel Used (gallons)": 63.8
    },
    {
        "Trip Name": "Valley Voyage",
        "Start Location": "Denver",
        "End Location": "New York",
        "Distance (miles)": 2416.2,
        "Duration (hours)": 61.3,
        "Fuel Used (gallons)": 5.8
    },
    {
        "Trip Name": "Mountain Adventure",
        "Start Location": "Chicago",
        "End Location": "Miami",
        "Distance (miles)": 645.0,
        "Duration (hours)": 53.0,
        "Fuel Used (gallons)": 18.9
    }
]<start>
- Distance (miles): 2814.7
  Duration (hours): 4.7
  End Location: Houston
  Fuel Used (gallons): 75.1
  Start Location: Los Angeles
  Trip Name: Forest Journey
- Distance (miles): 156.7
  Duration (hours): 14.4
  End Location: Denver
  Fuel Used (gallons): 63.8
  Start Location: Los Angeles
  Trip Name: Valley Voyage
- Distance (miles): 2416.2
  Duration (hours): 61.3
  End Location: New York
  Fuel Used (gallons): 5.8
  Start Location: Denver
  Trip Name: Valley Voyage
- Distance (miles): 645.0
  Duration (hours): 53.0
  End Location: Miami
  Fuel Used (gallons): 18.9
  Start Location: Chicago
  Trip Name: Mountain Adventure
<end>Here's some markdown data, can you convert it to Plain text?
| Name | City | Income |
| --- | --- | --- |
| Jayla | Louisville | 25000 |
| Christian | Chicago | 390000 |
| Antoinette | Nashville | 200000 |
| Mya | Houston | 105000 |
| Lucille | San Jose | 110000 |
| Angelina | Washington | 355000 |
| Preston | San Antonio | 340000 |
| Leland | San Diego | 150000 |<start>
Name: Jayla | City: Louisville | Income: 25000
Name: Christian | City: Chicago | Income: 390000
Name: Antoinette | City: Nashville | Income: 200000
Name: Mya | City: Houston | Income: 105000
Name: Lucille | City: San Jose | Income: 110000
Name: Angelina | City: Washington | Income: 355000
Name: Preston | City: San Antonio | Income: 340000
Name: Leland | City: San Diego | Income: 150000
<end>Can you change this Csv into yaml?
Title,Author,Genre,Publication Year
Shadows of Solitude,Isla Windrider,Fantasy,1992
Shadows of Solitude,Draven Blackthorn,Romance,2020
Legends of the Rift,Galen Starfire,Historical,2007
Whispers of the Abyss,Thorne Ironwood,Science Fiction,1996
Tales of the Brave,Orion Frostblade,Fantasy,2006
<start>
- Author: Isla Windrider
  Genre: Fantasy
  Publication Year: 1992
  Title: Shadows of Solitude
- Author: Draven Blackthorn
  Genre: Romance
  Publication Year: 2020
  Title: Shadows of Solitude
- Author: Galen Starfire
  Genre: Historical
  Publication Year: 2007
  Title: Legends of the Rift
- Author: Thorne Ironwood
  Genre: Science Fiction
  Publication Year: 1996
  Title: Whispers of the Abyss
- Author: Orion Frostblade
  Genre: Fantasy
  Publication Year: 2006
  Title: Tales of the Brave
<end>Can you change this Yaml into CSV?
- Condition: Foggy
  Day: Tuesday
  Humidity (%): 26
  Location: Miami
  Temperature (C): -6.2
  Wind Speed (km/h): 20.5
- Condition: Rainy
  Day: Monday
  Humidity (%): 55
  Location: Seattle
  Temperature (C): -2.2
  Wind Speed (km/h): 3.7
- Condition: Sunny
  Day: Monday
  Humidity (%): 48
  Location: Houston
  Temperature (C): -3.9
  Wind Speed (km/h): 18.3
- Condition: Rainy
  Day: Tuesday
  Humidity (%): 70
  Location: Chicago
  Temperature (C): 6.9
  Wind Speed (km/h): 25.0
- Condition: Snowy
  Day: Wednesday
  Humidity (%): 43
  Location: New York
  Temperature (C): 15.8
  Wind Speed (km/h): 3.3
- Condition: Stormy
  Day: Monday
  Humidity (%): 54
  Location: Phoenix
  Temperature (C): 31.1
  Wind Speed (km/h): 10.0
<start>
Location,Condition,Temperature (C),Humidity (%),Wind Speed (km/h),Day
Miami,Foggy,-6.2,26,20.5,Tuesday
Seattle,Rainy,-2.2,55,3.7,Monday
Houston,Sunny,-3.9,48,18.3,Monday
Chicago,Rainy,6.9,70,25.0,Tuesday
New York,Snowy,15.8,43,3.3,Wednesday
Phoenix,Stormy,31.1,54,10.0,Monday
<end>Convert this yaml to Csv:
- Distance (miles): 2300.4
  End Location: Chicago
  Start Location: San Francisco
  Trip Name: Coast to Coast
- Distance (miles): 1052.9
  End Location: San Francisco
  Start Location: Chicago
  Trip Name: Valley Voyage
- Distance (miles): 585.4
  End Location: Houston
  Start Location: Miami
  Trip Name: Desert Drive
- Distance (miles): 525.6
  End Location: Denver
  Start Location: Chicago
  Trip Name: Highway Odyssey
- Distance (miles): 1919.0
  End Location: Miami
  Start Location: New York
  Trip Name: Coast to Coast
- Distance (miles): 95.3
  End Location: Los Angeles
  Start Location: Denver
  Trip Name: Lakeside Retreat
- Distance (miles): 1919.0
  End Location: Miami
  Start Location: Phoenix
  Trip Name: Lakeside Retreat
- Distance (miles): 247.0
  End Location: Miami
  Start Location: New York
  Trip Name: Mountain Adventure
<start>
Trip Name,Start Location,End Location,Distance (miles)
Coast to Coast,San Francisco,Chicago,2300.4
Valley Voyage,Chicago,San Francisco,1052.9
Desert Drive,Miami,Houston,585.4
Highway Odyssey,Chicago,Denver,525.6
Coast to Coast,New York,Miami,1919.0
Lakeside Retreat,Denver,Los Angeles,95.3
Lakeside Retreat,Phoenix,Miami,1919.0
Mountain Adventure,New York,Miami,247.0
<end>Transform this Csv structure to a MARKDOWN format:
Restaurant Name,Cuisine,Location,Rating
Pizza Planet,Mexican,Houston,3
Pizza Planet,French,San Francisco,5
Pasta Palace,Chinese,Houston,3
The Golden Spoon,Chinese,San Francisco,3
Curry Corner,Japanese,Seattle,2
Sushi World,Italian,Chicago,1
Pizza Planet,Mexican,Chicago,1
Sushi World,Mediterranean,Miami,1
The Golden Spoon,Indian,Seattle,3
Taco Town,Mediterranean,Miami,1
<start>
| Restaurant Name | Cuisine | Location | Rating |
| --- | --- | --- | --- |
| Pizza Planet | Mexican | Houston | 3 |
| Pizza Planet | French | San Francisco | 5 |
| Pasta Palace | Chinese | Houston | 3 |
| The Golden Spoon | Chinese | San Francisco | 3 |
| Curry Corner | Japanese | Seattle | 2 |
| Sushi World | Italian | Chicago | 1 |
| Pizza Planet | Mexican | Chicago | 1 |
| Sushi World | Mediterranean | Miami | 1 |
| The Golden Spoon | Indian | Seattle | 3 |
| Taco Town | Mediterranean | Miami | 1 |
<end>Convert this PLAIN TEXT to JSON:
Company: HealthPlus | Market Cap: Small Cap | Stock Price: 411.51
Company: BioPharm | Market Cap: Large Cap | Stock Price: 504.27
Company: EcoEnergy | Market Cap: Large Cap | Stock Price: 908.56
Company: AeroSpace | Market Cap: Mega Cap | Stock Price: 469.31
Company: AeroSpace | Market Cap: Mid Cap | Stock Price: 655.02
Company: HealthPlus | Market Cap: Large Cap | Stock Price: 437.17
Company: Foodies | Market Cap: Mid Cap | Stock Price: 655.02
Company: EcoEnergy | Market Cap: Mega Cap | Stock Price: 504.27
<start>
[
    {
        "Company": "HealthPlus",
        "Market Cap": "Small Cap",
        "Stock Price": 411.51
    },
    {
        "Company": "BioPharm",
        "Market Cap": "Large Cap",
        "Stock Price": 504.27
    },
    {
        "Company": "EcoEnergy",
        "Market Cap": "Large Cap",
        "Stock Price": 908.56
    },
    {
        "Company": "AeroSpace",
        "Market Cap": "Mega Cap",
        "Stock Price": 469.31
    },
    {
        "Company": "AeroSpace",
        "Market Cap": "Mid Cap",
        "Stock Price": 655.02
    },
    {
        "Company": "HealthPlus",
        "Market Cap": "Large Cap",
        "Stock Price": 437.17
    },
    {
        "Company": "Foodies",
        "Market Cap": "Mid Cap",
        "Stock Price": 655.02
    },
    {
        "Company": "EcoEnergy",
        "Market Cap": "Mega Cap",
        "Stock Price": 504.27
    }
]
<end>Transform this yml structure to a JSON format:
- Cuisine: French
  Rating: 2
- Cuisine: Chinese
  Rating: 3
- Cuisine: Japanese
  Rating: 1
<start>
[
    {
        "Cuisine": "French",
        "Rating": 2
    },
    {
        "Cuisine": "Chinese",
        "Rating": 3
    },
    {
        "Cuisine": "Japanese",
        "Rating": 1
    }
]
<end>Here's some json data, can you convert it to csv?
[
    {
        "Name": "Amelia",
        "Age": 34,
        "Birth Month": "December",
        "City": "Austin",
        "Income": 285000
    },
    {
        "Name": "Jody",
        "Age": 23,
        "Birth Month": "May",
        "City": "Columbus",
        "Income": 225000
    },
    {
        "Name": "Fern",
        "Age": 49,
        "Birth Month": "February",
        "City": "Denver",
        "Income": 100000
    },
    {
        "Name": "Deborah",
        "Age": 63,
        "Birth Month": "December",
        "City": "Jacksonville",
        "Income": 130000
    }
]<start>
Name,Age,Birth Month,City,Income
Amelia,34,December,Austin,285000
Jody,23,May,Columbus,225000
Fern,49,February,Denver,100000
Deborah,63,December,Jacksonville,130000
<end>Can you change this plain text into CSV?
Author: Luna Silverleaf | Publication Year: 2008 | Rating: 4.6
Author: Thorne Ironwood | Publication Year: 2023 | Rating: 1.7
Author: Luna Silverleaf | Publication Year: 2014 | Rating: 3.9
Author: Orion Frostblade | Publication Year: 2015 | Rating: 1.8
<start>
Author,Publication Year,Rating
Luna Silverleaf,2008,4.6
Thorne Ironwood,2023,1.7
Luna Silverleaf,2014,3.9
Orion Frostblade,2015,1.8
<end>Transform this markdown structure to a PLAIN TEXT format:
| Device ID | Device Type | Location | Battery Level (%) | Reading Value | Timestamp |
| --- | --- | --- | --- | --- | --- |
| device-0058 | Light Sensor | Living Room | 56.9 | 44.72 | 2021-07-10 02:57:02 |
| device-0044 | Motion Detector | Office | 23.6 | -2.44 | 2022-04-02 16:37:20 |
| device-0040 | Light Sensor | Bedroom | 69.5 | -20.67 | 2021-10-17 17:43:09 |
| device-0063 | Motion Detector | Living Room | 18.7 | 23.11 | 2023-07-05 08:36:25 |
| device-0005 | Temperature Sensor | Bathroom | 75.3 | 23.11 | 2022-12-24 15:37:06 |
| device-0061 | Light Sensor | Garage | 88.4 | 23.11 | 2021-06-05 14:12:16 |<start>
Device ID: device-0058 | Device Type: Light Sensor | Location: Living Room | Battery Level (%): 56.9 | Reading Value: 44.72 | Timestamp: 2021-07-10 02:57:02
Device ID: device-0044 | Device Type: Motion Detector | Location: Office | Battery Level (%): 23.6 | Reading Value: -2.44 | Timestamp: 2022-04-02 16:37:20
Device ID: device-0040 | Device Type: Light Sensor | Location: Bedroom | Battery Level (%): 69.5 | Reading Value: -20.67 | Timestamp: 2021-10-17 17:43:09
Device ID: device-0063 | Device Type: Motion Detector | Location: Living Room | Battery Level (%): 18.7 | Reading Value: 23.11 | Timestamp: 2023-07-05 08:36:25
Device ID: device-0005 | Device Type: Temperature Sensor | Location: Bathroom | Battery Level (%): 75.3 | Reading Value: 23.11 | Timestamp: 2022-12-24 15:37:06
Device ID: device-0061 | Device Type: Light Sensor | Location: Garage | Battery Level (%): 88.4 | Reading Value: 23.11 | Timestamp: 2021-06-05 14:12:16
<end>Can you change this yml into Markdown?
- Condition: Sunny
  Humidity (%): 76
  Temperature (C): 20.0
  Wind Speed (km/h): 26.0
- Condition: Cloudy
  Humidity (%): 39
  Temperature (C): -8.6
  Wind Speed (km/h): 5.9
- Condition: Cloudy
  Humidity (%): 86
  Temperature (C): 3.5
  Wind Speed (km/h): 5.0
- Condition: Snowy
  Humidity (%): 96
  Temperature (C): 31.4
  Wind Speed (km/h): 15.9
- Condition: Cloudy
  Humidity (%): 35
  Temperature (C): 30.6
  Wind Speed (km/h): 3.7
- Condition: Stormy
  Humidity (%): 77
  Temperature (C): 39.0
  Wind Speed (km/h): 20.2
- Condition: Cloudy
  Humidity (%): 48
  Temperature (C): -5.5
  Wind Speed (km/h): 2.8
- Condition: Rainy
  Humidity (%): 49
  Temperature (C): 31.4
  Wind Speed (km/h): 13.7
<start>
| Condition | Temperature (C) | Humidity (%) | Wind Speed (km/h) |
| --- | --- | --- | --- |
| Sunny | 20.0 | 76 | 26.0 |
| Cloudy | -8.6 | 39 | 5.9 |
| Cloudy | 3.5 | 86 | 5.0 |
| Snowy | 31.4 | 96 | 15.9 |
| Cloudy | 30.6 | 35 | 3.7 |
| Stormy | 39.0 | 77 | 20.2 |
| Cloudy | -5.5 | 48 | 2.8 |
| Rainy | 31.4 | 49 | 13.7 |
<end>Transform this plain text structure to a yaml format:
Humidity (%): 27 | Wind Speed (km/h): 16.6 | Day: Saturday
Humidity (%): 28 | Wind Speed (km/h): 5.7 | Day: Saturday
Humidity (%): 27 | Wind Speed (km/h): 15.7 | Day: Wednesday
Humidity (%): 45 | Wind Speed (km/h): 17.0 | Day: Sunday
Humidity (%): 22 | Wind Speed (km/h): 22.7 | Day: Sunday
Humidity (%): 58 | Wind Speed (km/h): 9.2 | Day: Thursday
Humidity (%): 100 | Wind Speed (km/h): 22.7 | Day: Friday
Humidity (%): 26 | Wind Speed (km/h): 16.6 | Day: Tuesday
Humidity (%): 27 | Wind Speed (km/h): 22.7 | Day: Monday
<start>
- Day: Saturday
  Humidity (%): 27
  Wind Speed (km/h): 16.6
- Day: Saturday
  Humidity (%): 28
  Wind Speed (km/h): 5.7
- Day: Wednesday
  Humidity (%): 27
  Wind Speed (km/h): 15.7
- Day: Sunday
  Humidity (%): 45
  Wind Speed (km/h): 17.0
- Day: Sunday
  Humidity (%): 22
  Wind Speed (km/h): 22.7
- Day: Thursday
  Humidity (%): 58
  Wind Speed (km/h): 9.2
- Day: Friday
  Humidity (%): 100
  Wind Speed (km/h): 22.7
- Day: Tuesday
  Humidity (%): 26
  Wind Speed (km/h): 16.6
- Day: Monday
  Humidity (%): 27
  Wind Speed (km/h): 22.7
<end>Please transform the following markdown data into json:
| Device ID | Device Type | Location | Timestamp |
| --- | --- | --- | --- |
| device-0025 | Temperature Sensor | Living Room | 2022-04-25 07:56:56 |
| device-0024 | Motion Detector | Kitchen | 2021-10-15 01:17:00 |
| device-0081 | Light Sensor | Bathroom | 2023-06-27 04:50:23 |
| device-0030 | Humidity Sensor | Garden | 2023-01-24 18:26:57 |<start>
[
    {
        "Device ID": "device-0025",
        "Device Type": "Temperature Sensor",
        "Location": "Living Room",
        "Timestamp": "2022-04-25 07:56:56"
    },
    {
        "Device ID": "device-0024",
        "Device Type": "Motion Detector",
        "Location": "Kitchen",
        "Timestamp": "2021-10-15 01:17:00"
    },
    {
        "Device ID": "device-0081",
        "Device Type": "Light Sensor",
        "Location": "Bathroom",
        "Timestamp": "2023-06-27 04:50:23"
    },
    {
        "Device ID": "device-0030",
        "Device Type": "Humidity Sensor",
        "Location": "Garden",
        "Timestamp": "2023-01-24 18:26:57"
    }
]
<end>Transform this Markdown structure to a plain text format:
| Condition | Humidity (%) | Wind Speed (km/h) |
| --- | --- | --- |
| Foggy | 45 | 13.8 |
| Snowy | 24 | 28.0 |
| Stormy | 79 | 26.0 |
| Sunny | 45 | 7.4 |
| Windy | 29 | 6.8 |
| Foggy | 68 | 6.5 |
| Foggy | 34 | 14.9 |
| Cloudy | 20 | 18.6 |
| Foggy | 66 | 23.6 |<start>
Condition: Foggy | Humidity (%): 45 | Wind Speed (km/h): 13.8
Condition: Snowy | Humidity (%): 24 | Wind Speed (km/h): 28.0
Condition: Stormy | Humidity (%): 79 | Wind Speed (km/h): 26.0
Condition: Sunny | Humidity (%): 45 | Wind Speed (km/h): 7.4
Condition: Windy | Humidity (%): 29 | Wind Speed (km/h): 6.8
Condition: Foggy | Humidity (%): 68 | Wind Speed (km/h): 6.5
Condition: Foggy | Humidity (%): 34 | Wind Speed (km/h): 14.9
Condition: Cloudy | Humidity (%): 20 | Wind Speed (km/h): 18.6
Condition: Foggy | Humidity (%): 66 | Wind Speed (km/h): 23.6
<end>Can you change this Csv into json?
Product Name,SKU,Price,Stock Quantity,Category,Supplier Name
Device,SKU-1069,106.72,182,Toys,Umbrella Corp
Thingamajig,SKU-1015,192.72,46,Automotive,Umbrella Corp
Apparatus,SKU-1098,439.7,229,Sports,Globex
Gadget,SKU-1055,399.48,354,Sports,Wonka Industries
Thingamajig,SKU-1065,233.69,303,Toys,Globex
Gizmo,SKU-1074,463.37,162,Automotive,ACME Corp
Gizmo,SKU-1048,227.48,458,Household,Globex
Instrument,SKU-1089,210.66,395,Toys,Wayne Enterprises
Device,SKU-1023,387.96,177,Sports,Globex
<start>
[
    {
        "Product Name": "Device",
        "SKU": "SKU-1069",
        "Price": 106.72,
        "Stock Quantity": 182,
        "Category": "Toys",
        "Supplier Name": "Umbrella Corp"
    },
    {
        "Product Name": "Thingamajig",
        "SKU": "SKU-1015",
        "Price": 192.72,
        "Stock Quantity": 46,
        "Category": "Automotive",
        "Supplier Name": "Umbrella Corp"
    },
    {
        "Product Name": "Apparatus",
        "SKU": "SKU-1098",
        "Price": 439.7,
        "Stock Quantity": 229,
        "Category": "Sports",
        "Supplier Name": "Globex"
    },
    {
        "Product Name": "Gadget",
        "SKU": "SKU-1055",
        "Price": 399.48,
        "Stock Quantity": 354,
        "Category": "Sports",
        "Supplier Name": "Wonka Industries"
    },
    {
        "Product Name": "Thingamajig",
        "SKU": "SKU-1065",
        "Price": 233.69,
        "Stock Quantity": 303,
        "Category": "Toys",
        "Supplier Name": "Globex"
    },
    {
        "Product Name": "Gizmo",
        "SKU": "SKU-1074",
        "Price": 463.37,
        "Stock Quantity": 162,
        "Category": "Automotive",
        "Supplier Name": "ACME Corp"
    },
    {
        "Product Name": "Gizmo",
        "SKU": "SKU-1048",
        "Price": 227.48,
        "Stock Quantity": 458,
        "Category": "Household",
        "Supplier Name": "Globex"
    },
    {
        "Product Name": "Instrument",
        "SKU": "SKU-1089",
        "Price": 210.66,
        "Stock Quantity": 395,
        "Category": "Toys",
        "Supplier Name": "Wayne Enterprises"
    },
    {
        "Product Name": "Device",
        "SKU": "SKU-1023",
        "Price": 387.96,
        "Stock Quantity": 177,
        "Category": "Sports",
        "Supplier Name": "Globex"
    }
]
<end>Can you change this YML into MARKDOWN?
- Day: Tuesday
  Humidity (%): 23
  Location: Denver
  Temperature (C): -0.6
- Day: Monday
  Humidity (%): 74
  Location: Seattle
  Temperature (C): 18.5
- Day: Monday
  Humidity (%): 56
  Location: New York
  Temperature (C): 19.6
- Day: Saturday
  Humidity (%): 91
  Location: Phoenix
  Temperature (C): 17.2
- Day: Thursday
  Humidity (%): 100
  Location: New York
  Temperature (C): 16.5
- Day: Monday
  Humidity (%): 98
  Location: Houston
  Temperature (C): 11.0
- Day: Sunday
  Humidity (%): 90
  Location: Houston
  Temperature (C): -4.9
- Day: Thursday
  Humidity (%): 20
  Location: Los Angeles
  Temperature (C): 27.5
- Day: Thursday
  Humidity (%): 89
  Location: Chicago
  Temperature (C): 31.3
- Day: Tuesday
  Humidity (%): 33
  Location: Miami
  Temperature (C): 3.0
<start>
| Location | Temperature (C) | Humidity (%) | Day |
| --- | --- | --- | --- |
| Denver | -0.6 | 23 | Tuesday |
| Seattle | 18.5 | 74 | Monday |
| New York | 19.6 | 56 | Monday |
| Phoenix | 17.2 | 91 | Saturday |
| New York | 16.5 | 100 | Thursday |
| Houston | 11.0 | 98 | Monday |
| Houston | -4.9 | 90 | Sunday |
| Los Angeles | 27.5 | 20 | Thursday |
| Chicago | 31.3 | 89 | Thursday |
| Miami | 3.0 | 33 | Tuesday |
<end>Transform this JSON structure to a Csv format:
[
    {
        "Trip Name": "Lakeside Retreat",
        "Start Location": "Houston",
        "End Location": "New York",
        "Fuel Used (gallons)": 50.6
    },
    {
        "Trip Name": "Highway Odyssey",
        "Start Location": "Houston",
        "End Location": "Los Angeles",
        "Fuel Used (gallons)": 72.6
    },
    {
        "Trip Name": "Lakeside Retreat",
        "Start Location": "Houston",
        "End Location": "Chicago",
        "Fuel Used (gallons)": 62.1
    },
    {
        "Trip Name": "Forest Journey",
        "Start Location": "Denver",
        "End Location": "Houston",
        "Fuel Used (gallons)": 56.7
    },
    {
        "Trip Name": "Highway Odyssey",
        "Start Location": "Houston",
        "End Location": "New York",
        "Fuel Used (gallons)": 64.4
    },
    {
        "Trip Name": "Historic Route",
        "Start Location": "Houston",
        "End Location": "San Francisco",
        "Fuel Used (gallons)": 88.8
    },
    {
        "Trip Name": "Highway Odyssey",
        "Start Location": "New York",
        "End Location": "Houston",
        "Fuel Used (gallons)": 46.2
    },
    {
        "Trip Name": "Coast to Coast",
        "Start Location": "Phoenix",
        "End Location": "San Francisco",
        "Fuel Used (gallons)": 11.8
    }
]<start>
Trip Name,Start Location,End Location,Fuel Used (gallons)
Lakeside Retreat,Houston,New York,50.6
Highway Odyssey,Houston,Los Angeles,72.6
Lakeside Retreat,Houston,Chicago,62.1
Forest Journey,Denver,Houston,56.7
Highway Odyssey,Houston,New York,64.4
Historic Route,Houston,San Francisco,88.8
Highway Odyssey,New York,Houston,46.2
Coast to Coast,Phoenix,San Francisco,11.8
<end>Here's some markdown data, can you convert it to json?
| Author | Genre | Publication Year |
| --- | --- | --- |
| Elara Moonshadow | Fantasy | 1973 |
| Rowan Ashborne | Thriller | 1988 |
| Kara Firebrand | Thriller | 1956 |<start>
[
    {
        "Author": "Elara Moonshadow",
        "Genre": "Fantasy",
        "Publication Year": 1973
    },
    {
        "Author": "Rowan Ashborne",
        "Genre": "Thriller",
        "Publication Year": 1988
    },
    {
        "Author": "Kara Firebrand",
        "Genre": "Thriller",
        "Publication Year": 1956
    }
]
<end>Here's some CSV data, can you convert it to json?
Cache Hit Ratio (%),Average Latency (ms),Timestamp
82.04,76.53,2022-01-19 23:37:53
98.57,6.88,2023-11-10 02:03:05
96.18,47.8,2022-11-20 20:38:48
80.3,91.67,2021-11-15 19:02:42
85.28,97.05,2022-01-06 08:23:29
77.53,97.05,2023-05-25 13:31:58
<start>
[
    {
        "Cache Hit Ratio (%)": 82.04,
        "Average Latency (ms)": 76.53,
        "Timestamp": "2022-01-19 23:37:53"
    },
    {
        "Cache Hit Ratio (%)": 98.57,
        "Average Latency (ms)": 6.88,
        "Timestamp": "2023-11-10 02:03:05"
    },
    {
        "Cache Hit Ratio (%)": 96.18,
        "Average Latency (ms)": 47.8,
        "Timestamp": "2022-11-20 20:38:48"
    },
    {
        "Cache Hit Ratio (%)": 80.3,
        "Average Latency (ms)": 91.67,
        "Timestamp": "2021-11-15 19:02:42"
    },
    {
        "Cache Hit Ratio (%)": 85.28,
        "Average Latency (ms)": 97.05,
        "Timestamp": "2022-01-06 08:23:29"
    },
    {
        "Cache Hit Ratio (%)": 77.53,
        "Average Latency (ms)": 97.05,
        "Timestamp": "2023-05-25 13:31:58"
    }
]
<end>Here's some markdown data, can you convert it to csv?
| Age | Birth Month | City | Income |
| --- | --- | --- | --- |
| 42 | June | Austin | 235000 |
| 64 | June | San Diego | 140000 |
| 25 | October | Jacksonville | 60000 |
| 35 | September | Louisville | 175000 |
| 44 | October | Jacksonville | 395000 |<start>
Age,Birth Month,City,Income
42,June,Austin,235000
64,June,San Diego,140000
25,October,Jacksonville,60000
35,September,Louisville,175000
44,October,Jacksonville,395000
<end>Can you change this PLAIN TEXT into csv?
Open Price: 265.27 | Close Price: 201.38 | High Price: 870.34 | Low Price: 201.38 | Volume: 2002362
Open Price: 975.21 | Close Price: 64.9 | High Price: 1071.04 | Low Price: 64.9 | Volume: 5338013
Open Price: 222.02 | Close Price: 589.31 | High Price: 589.31 | Low Price: 222.02 | Volume: 2732758
<start>
Open Price,Close Price,High Price,Low Price,Volume
265.27,201.38,870.34,201.38,2002362
975.21,64.9,1071.04,64.9,5338013
222.02,589.31,589.31,222.02,2732758
<end>Can you change this YAML into csv?
- Battery Level (%): 14.3
  Device ID: device-0090
  Reading Value: -25.57
  Timestamp: '2022-10-03 07:51:07'
- Battery Level (%): 60.8
  Device ID: device-0006
  Reading Value: -22.51
  Timestamp: '2023-10-21 23:46:08'
- Battery Level (%): 84.4
  Device ID: device-0089
  Reading Value: 63.05
  Timestamp: '2022-02-27 11:19:56'
- Battery Level (%): 48.1
  Device ID: device-0020
  Reading Value: 79.66
  Timestamp: '2021-09-24 11:15:52'
- Battery Level (%): 64.0
  Device ID: device-0059
  Reading Value: 83.66
  Timestamp: '2022-10-17 15:15:25'
- Battery Level (%): 35.7
  Device ID: device-0075
  Reading Value: -24.38
  Timestamp: '2021-06-21 11:10:59'
- Battery Level (%): 35.7
  Device ID: device-0064
  Reading Value: 30.81
  Timestamp: '2021-01-17 22:27:21'
<start>
Device ID,Battery Level (%),Reading Value,Timestamp
device-0090,14.3,-25.57,2022-10-03 07:51:07
device-0006,60.8,-22.51,2023-10-21 23:46:08
device-0089,84.4,63.05,2022-02-27 11:19:56
device-0020,48.1,79.66,2021-09-24 11:15:52
device-0059,64.0,83.66,2022-10-17 15:15:25
device-0075,35.7,-24.38,2021-06-21 11:10:59
device-0064,35.7,30.81,2021-01-17 22:27:21
<end>Convert this plain text to markdown:
Database Name: OrdersDB | Connection Count: 469 | Timestamp: 2023-09-09 03:40:51
Database Name: ProfilesDB | Connection Count: 128 | Timestamp: 2021-09-02 13:20:58
Database Name: SalesDB | Connection Count: 51 | Timestamp: 2021-12-16 12:10:46
Database Name: LogsDB | Connection Count: 270 | Timestamp: 2023-04-24 21:18:36
Database Name: SessionsDB | Connection Count: 447 | Timestamp: 2022-12-16 22:04:07
Database Name: ProfilesDB | Connection Count: 198 | Timestamp: 2021-04-07 04:28:48
Database Name: AnalyticsDB | Connection Count: 340 | Timestamp: 2021-07-21 10:19:28
Database Name: LogsDB | Connection Count: 294 | Timestamp: 2021-08-02 03:06:39
Database Name: LogsDB | Connection Count: 15 | Timestamp: 2023-05-05 03:27:27
Database Name: LogsDB | Connection Count: 22 | Timestamp: 2023-03-27 20:38:31
<start>
| Database Name | Connection Count | Timestamp |
| --- | --- | --- |
| OrdersDB | 469 | 2023-09-09 03:40:51 |
| ProfilesDB | 128 | 2021-09-02 13:20:58 |
| SalesDB | 51 | 2021-12-16 12:10:46 |
| LogsDB | 270 | 2023-04-24 21:18:36 |
| SessionsDB | 447 | 2022-12-16 22:04:07 |
| ProfilesDB | 198 | 2021-04-07 04:28:48 |
| AnalyticsDB | 340 | 2021-07-21 10:19:28 |
| LogsDB | 294 | 2021-08-02 03:06:39 |
| LogsDB | 15 | 2023-05-05 03:27:27 |
| LogsDB | 22 | 2023-03-27 20:38:31 |
<end>Please transform the following markdown data into json:
| Company | Date | Close Price | High Price | Low Price | Volume |
| --- | --- | --- | --- | --- | --- |
| RetailWorld | 2017-06-09 | 221.93 | 879.9 | 221.93 | 2674819 |
| GreenEnergy | 2021-03-22 | 1053.63 | 1235.77 | 1053.63 | 3629548 |
| RetailWorld | 2022-11-09 | 660.82 | 660.82 | 500.35 | 8677202 |
| TechnoCorp | 2021-06-28 | 1413.15 | 1413.15 | 687.29 | 109520 |
| TechnoCorp | 2019-03-06 | 1251.57 | 1251.57 | 370.87 | 5360153 |
| BioLife | 2020-11-11 | 431.5 | 1386.38 | 431.5 | 4261641 |<start>
[
    {
        "Company": "RetailWorld",
        "Date": "2017-06-09",
        "Close Price": 221.93,
        "High Price": 879.9,
        "Low Price": 221.93,
        "Volume": 2674819
    },
    {
        "Company": "GreenEnergy",
        "Date": "2021-03-22",
        "Close Price": 1053.63,
        "High Price": 1235.77,
        "Low Price": 1053.63,
        "Volume": 3629548
    },
    {
        "Company": "RetailWorld",
        "Date": "2022-11-09",
        "Close Price": 660.82,
        "High Price": 660.82,
        "Low Price": 500.35,
        "Volume": 8677202
    },
    {
        "Company": "TechnoCorp",
        "Date": "2021-06-28",
        "Close Price": 1413.15,
        "High Price": 1413.15,
        "Low Price": 687.29,
        "Volume": 109520
    },
    {
        "Company": "TechnoCorp",
        "Date": "2019-03-06",
        "Close Price": 1251.57,
        "High Price": 1251.57,
        "Low Price": 370.87,
        "Volume": 5360153
    },
    {
        "Company": "BioLife",
        "Date": "2020-11-11",
        "Close Price": 431.5,
        "High Price": 1386.38,
        "Low Price": 431.5,
        "Volume": 4261641
    }
]
<end>Can you change this yml into CSV?
- Annual Revenue (B): 337.7
  Company: AeroSpace
  Market Cap: Large Cap
  Quarter: Q4
  Stock Price: 225.58
- Annual Revenue (B): 246.63
  Company: Foodies
  Market Cap: Mega Cap
  Quarter: Q2
  Stock Price: 153.19
- Annual Revenue (B): 399.42
  Company: AutoDrive
  Market Cap: Small Cap
  Quarter: Q1
  Stock Price: 283.27
- Annual Revenue (B): 155.45
  Company: EcoEnergy
  Market Cap: Mega Cap
  Quarter: Q4
  Stock Price: 936.1
- Annual Revenue (B): 208.8
  Company: TechCorp
  Market Cap: Small Cap
  Quarter: Q3
  Stock Price: 975.98
- Annual Revenue (B): 65.5
  Company: AutoDrive
  Market Cap: Mega Cap
  Quarter: Q2
  Stock Price: 443.76
- Annual Revenue (B): 65.95
  Company: HealthPlus
  Market Cap: Large Cap
  Quarter: Q3
  Stock Price: 450.79
- Annual Revenue (B): 260.28
  Company: EcoEnergy
  Market Cap: Small Cap
  Quarter: Q3
  Stock Price: 684.73
- Annual Revenue (B): 70.11
  Company: EcoEnergy
  Market Cap: Large Cap
  Quarter: Q4
  Stock Price: 176.25
- Annual Revenue (B): 472.74
  Company: AutoDrive
  Market Cap: Small Cap
  Quarter: Q2
  Stock Price: 340.4
<start>
Company,Market Cap,Stock Price,Annual Revenue (B),Quarter
AeroSpace,Large Cap,225.58,337.7,Q4
Foodies,Mega Cap,153.19,246.63,Q2
AutoDrive,Small Cap,283.27,399.42,Q1
EcoEnergy,Mega Cap,936.1,155.45,Q4
TechCorp,Small Cap,975.98,208.8,Q3
AutoDrive,Mega Cap,443.76,65.5,Q2
HealthPlus,Large Cap,450.79,65.95,Q3
EcoEnergy,Small Cap,684.73,260.28,Q3
EcoEnergy,Large Cap,176.25,70.11,Q4
AutoDrive,Small Cap,340.4,472.74,Q2
<end>Transform this csv structure to a Plain text format:
Company,Market Cap,Stock Price,Annual Revenue (B),Quarter
AeroSpace,Small Cap,272.13,126.59,Q2
FinanceWorks,Mega Cap,142.59,212.22,Q1
Foodies,Mid Cap,871.28,478.85,Q3
<start>
Company: AeroSpace | Market Cap: Small Cap | Stock Price: 272.13 | Annual Revenue (B): 126.59 | Quarter: Q2
Company: FinanceWorks | Market Cap: Mega Cap | Stock Price: 142.59 | Annual Revenue (B): 212.22 | Quarter: Q1
Company: Foodies | Market Cap: Mid Cap | Stock Price: 871.28 | Annual Revenue (B): 478.85 | Quarter: Q3
<end>Can you change this Markdown into Csv?
| Trip Name | End Location | Duration (hours) |
| --- | --- | --- |
| Coast to Coast | Houston | 69.0 |
| Desert Drive | Los Angeles | 57.2 |
| Coast to Coast | Chicago | 4.5 |
| Valley Voyage | Chicago | 49.1 |
| Mountain Adventure | Houston | 21.3 |
| Valley Voyage | Los Angeles | 27.9 |
| Valley Voyage | Chicago | 27.9 |
| Coast to Coast | Phoenix | 10.2 |
| Historic Route | Los Angeles | 50.0 |<start>
Trip Name,End Location,Duration (hours)
Coast to Coast,Houston,69.0
Desert Drive,Los Angeles,57.2
Coast to Coast,Chicago,4.5
Valley Voyage,Chicago,49.1
Mountain Adventure,Houston,21.3
Valley Voyage,Los Angeles,27.9
Valley Voyage,Chicago,27.9
Coast to Coast,Phoenix,10.2
Historic Route,Los Angeles,50.0
<end>Convert this Yaml to markdown:
- Category: Household
  Price: 385.68
  Product Name: Apparatus
  SKU: SKU-1040
  Stock Quantity: 225
  Supplier Name: Umbrella Corp
- Category: Electronics
  Price: 45.73
  Product Name: Gadget
  SKU: SKU-1017
  Stock Quantity: 256
  Supplier Name: Wayne Enterprises
- Category: Automotive
  Price: 79.01
  Product Name: Doohickey
  SKU: SKU-1081
  Stock Quantity: 372
  Supplier Name: Globex
<start>
| Product Name | SKU | Price | Stock Quantity | Category | Supplier Name |
| --- | --- | --- | --- | --- | --- |
| Apparatus | SKU-1040 | 385.68 | 225 | Household | Umbrella Corp |
| Gadget | SKU-1017 | 45.73 | 256 | Electronics | Wayne Enterprises |
| Doohickey | SKU-1081 | 79.01 | 372 | Automotive | Globex |
<end>Here's some csv data, can you convert it to Plain text?
Title,Genre,Release Year
Starbound Odyssey,Fantasy,1974
The Final Voyage,Drama,1993
Dreamwalker,Drama,2018
The Great Expedition,Horror,2015
Dreamwalker,Comedy,2012
Escape from Earth,Fantasy,1983
Mystery of the Depths,Fantasy,1977
<start>
Title: Starbound Odyssey | Genre: Fantasy | Release Year: 1974
Title: The Final Voyage | Genre: Drama | Release Year: 1993
Title: Dreamwalker | Genre: Drama | Release Year: 2018
Title: The Great Expedition | Genre: Horror | Release Year: 2015
Title: Dreamwalker | Genre: Comedy | Release Year: 2012
Title: Escape from Earth | Genre: Fantasy | Release Year: 1983
Title: Mystery of the Depths | Genre: Fantasy | Release Year: 1977
<end>Please transform the following Yml data into plain text:
- Category: Household
  Price: 197.29
  SKU: SKU-1075
  Stock Quantity: 465
  Supplier Name: ACME Corp
- Category: Automotive
  Price: 314.05
  SKU: SKU-1015
  Stock Quantity: 42
  Supplier Name: Globex
- Category: Household
  Price: 130.95
  SKU: SKU-1042
  Stock Quantity: 85
  Supplier Name: Wonka Industries
<start>
SKU: SKU-1075 | Price: 197.29 | Stock Quantity: 465 | Category: Household | Supplier Name: ACME Corp
SKU: SKU-1015 | Price: 314.05 | Stock Quantity: 42 | Category: Automotive | Supplier Name: Globex
SKU: SKU-1042 | Price: 130.95 | Stock Quantity: 85 | Category: Household | Supplier Name: Wonka Industries
<end>Transform this MARKDOWN structure to a json format:
| Company | Sector | Stock Price | Annual Revenue (B) |
| --- | --- | --- | --- |
| AutoDrive | Aerospace | 294.89 | 285.81 |
| GlobalTrade | Finance | 680.93 | 225.95 |
| BioPharm | Retail | 591.15 | 65.61 |
| RetailHub | Automotive | 121.42 | 426.61 |
| BioPharm | Technology | 457.03 | 257.24 |
| AeroSpace | Finance | 256.26 | 344.26 |<start>
[
    {
        "Company": "AutoDrive",
        "Sector": "Aerospace",
        "Stock Price": 294.89,
        "Annual Revenue (B)": 285.81
    },
    {
        "Company": "GlobalTrade",
        "Sector": "Finance",
        "Stock Price": 680.93,
        "Annual Revenue (B)": 225.95
    },
    {
        "Company": "BioPharm",
        "Sector": "Retail",
        "Stock Price": 591.15,
        "Annual Revenue (B)": 65.61
    },
    {
        "Company": "RetailHub",
        "Sector": "Automotive",
        "Stock Price": 121.42,
        "Annual Revenue (B)": 426.61
    },
    {
        "Company": "BioPharm",
        "Sector": "Technology",
        "Stock Price": 457.03,
        "Annual Revenue (B)": 257.24
    },
    {
        "Company": "AeroSpace",
        "Sector": "Finance",
        "Stock Price": 256.26,
        "Annual Revenue (B)": 344.26
    }
]
<end>Please transform the following YAML data into markdown:
- Close Price: 1426.06
  Company: AeroSystems
  Date: '2012-09-01'
  High Price: 1426.06
  Low Price: 54.95
  Open Price: 54.95
  Volume: 5346614
- Close Price: 147.9
  Company: AutoMotive
  Date: '2018-11-05'
  High Price: 1095.48
  Low Price: 147.9
  Open Price: 1095.48
  Volume: 2947058
- Close Price: 500.56
  Company: FinanceTrust
  Date: '2010-08-18'
  High Price: 666.0
  Low Price: 500.56
  Open Price: 658.17
  Volume: 7579766
<start>
| Company | Date | Open Price | Close Price | High Price | Low Price | Volume |
| --- | --- | --- | --- | --- | --- | --- |
| AeroSystems | 2012-09-01 | 54.95 | 1426.06 | 1426.06 | 54.95 | 5346614 |
| AutoMotive | 2018-11-05 | 1095.48 | 147.9 | 1095.48 | 147.9 | 2947058 |
| FinanceTrust | 2010-08-18 | 658.17 | 500.56 | 666.0 | 500.56 | 7579766 |
<end>Here's some plain text data, can you convert it to csv?
Name: Danny | Age: 31 | Birth Month: January | City: New York
Name: Morgan | Age: 51 | Birth Month: August | City: Jacksonville
Name: Cody | Age: 21 | Birth Month: October | City: Columbus
Name: Mindy | Age: 52 | Birth Month: October | City: Jacksonville
Name: Celia | Age: 67 | Birth Month: December | City: Indianapolis
Name: Johnie | Age: 61 | Birth Month: November | City: Boston
<start>
Name,Age,Birth Month,City
Danny,31,January,New York
Morgan,51,August,Jacksonville
Cody,21,October,Columbus
Mindy,52,October,Jacksonville
Celia,67,December,Indianapolis
Johnie,61,November,Boston
<end>Here's some CSV data, can you convert it to json?
Age,Birth Month,City,Income
61,October,Milwaukee,165000
68,April,San Diego,370000
60,March,Detroit,115000
36,February,New York,35000
37,November,Denver,465000
48,May,Charlotte,25000
<start>
[
    {
        "Age": 61,
        "Birth Month": "October",
        "City": "Milwaukee",
        "Income": 165000
    },
    {
        "Age": 68,
        "Birth Month": "April",
        "City": "San Diego",
        "Income": 370000
    },
    {
        "Age": 60,
        "Birth Month": "March",
        "City": "Detroit",
        "Income": 115000
    },
    {
        "Age": 36,
        "Birth Month": "February",
        "City": "New York",
        "Income": 35000
    },
    {
        "Age": 37,
        "Birth Month": "November",
        "City": "Denver",
        "Income": 465000
    },
    {
        "Age": 48,
        "Birth Month": "May",
        "City": "Charlotte",
        "Income": 25000
    }
]
<end>Convert this JSON to csv:
[
    {
        "Company": "TechCorp",
        "Sector": "Retail",
        "Market Cap": "Mid Cap",
        "Stock Price": 590.78,
        "Annual Revenue (B)": 81.78,
        "Quarter": "Q4"
    },
    {
        "Company": "Foodies",
        "Sector": "Finance",
        "Market Cap": "Small Cap",
        "Stock Price": 590.78,
        "Annual Revenue (B)": 298.17,
        "Quarter": "Q3"
    },
    {
        "Company": "AeroSpace",
        "Sector": "Energy",
        "Market Cap": "Mega Cap",
        "Stock Price": 973.0,
        "Annual Revenue (B)": 221.91,
        "Quarter": "Q4"
    }
]<start>
Company,Sector,Market Cap,Stock Price,Annual Revenue (B),Quarter
TechCorp,Retail,Mid Cap,590.78,81.78,Q4
Foodies,Finance,Small Cap,590.78,298.17,Q3
AeroSpace,Energy,Mega Cap,973.0,221.91,Q4
<end>