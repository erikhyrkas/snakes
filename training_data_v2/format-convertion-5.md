Convert this csv to json:
Trip Name,Start Location,End Location,Distance (miles),Duration (hours),Fuel Used (gallons)
Highway Odyssey,Phoenix,Los Angeles,2973.2,61.6,7.8
Canyon Trek,New York,Los Angeles,1801.1,63.0,94.6
Coast to Coast,Los Angeles,Denver,1727.1,61.7,52.5
Desert Drive,Los Angeles,Chicago,607.5,61.6,17.4
<start>
[
    {
        "Trip Name": "Highway Odyssey",
        "Start Location": "Phoenix",
        "End Location": "Los Angeles",
        "Distance (miles)": 2973.2,
        "Duration (hours)": 61.6,
        "Fuel Used (gallons)": 7.8
    },
    {
        "Trip Name": "Canyon Trek",
        "Start Location": "New York",
        "End Location": "Los Angeles",
        "Distance (miles)": 1801.1,
        "Duration (hours)": 63.0,
        "Fuel Used (gallons)": 94.6
    },
    {
        "Trip Name": "Coast to Coast",
        "Start Location": "Los Angeles",
        "End Location": "Denver",
        "Distance (miles)": 1727.1,
        "Duration (hours)": 61.7,
        "Fuel Used (gallons)": 52.5
    },
    {
        "Trip Name": "Desert Drive",
        "Start Location": "Los Angeles",
        "End Location": "Chicago",
        "Distance (miles)": 607.5,
        "Duration (hours)": 61.6,
        "Fuel Used (gallons)": 17.4
    }
]
<end>Here's some Json data, can you convert it to Plain text?
[
    {
        "Genre": "Non-Fiction",
        "Publication Year": 1992,
        "Rating": 1.2
    },
    {
        "Genre": "Horror",
        "Publication Year": 1969,
        "Rating": 3.5
    },
    {
        "Genre": "Thriller",
        "Publication Year": 1953,
        "Rating": 3.9
    },
    {
        "Genre": "Thriller",
        "Publication Year": 2006,
        "Rating": 3.2
    },
    {
        "Genre": "Fantasy",
        "Publication Year": 1969,
        "Rating": 1.2
    }
]<start>
Genre: Non-Fiction | Publication Year: 1992 | Rating: 1.2
Genre: Horror | Publication Year: 1969 | Rating: 3.5
Genre: Thriller | Publication Year: 1953 | Rating: 3.9
Genre: Thriller | Publication Year: 2006 | Rating: 3.2
Genre: Fantasy | Publication Year: 1969 | Rating: 1.2
<end>Can you change this csv into Yml?
Device ID,Device Type,Location,Battery Level (%),Reading Value,Timestamp
device-0041,Pressure Sensor,Office,14.4,10.04,2021-07-19 21:38:31
device-0051,Temperature Sensor,Office,89.5,55.99,2021-07-01 14:34:58
device-0024,Light Sensor,Living Room,38.2,77.81,2023-03-13 03:42:32
device-0003,Humidity Sensor,Garage,91.3,-0.06,2021-09-05 20:46:51
device-0004,Humidity Sensor,Hallway,25.6,76.95,2021-06-20 11:12:32
device-0051,Light Sensor,Bedroom,54.3,58.62,2021-08-16 05:48:14
device-0036,Light Sensor,Bedroom,37.9,-20.91,2022-05-03 10:05:46
device-0034,Pressure Sensor,Kitchen,58.2,78.58,2021-07-27 01:35:54
<start>
- Battery Level (%): 14.4
  Device ID: device-0041
  Device Type: Pressure Sensor
  Location: Office
  Reading Value: 10.04
  Timestamp: '2021-07-19 21:38:31'
- Battery Level (%): 89.5
  Device ID: device-0051
  Device Type: Temperature Sensor
  Location: Office
  Reading Value: 55.99
  Timestamp: '2021-07-01 14:34:58'
- Battery Level (%): 38.2
  Device ID: device-0024
  Device Type: Light Sensor
  Location: Living Room
  Reading Value: 77.81
  Timestamp: '2023-03-13 03:42:32'
- Battery Level (%): 91.3
  Device ID: device-0003
  Device Type: Humidity Sensor
  Location: Garage
  Reading Value: -0.06
  Timestamp: '2021-09-05 20:46:51'
- Battery Level (%): 25.6
  Device ID: device-0004
  Device Type: Humidity Sensor
  Location: Hallway
  Reading Value: 76.95
  Timestamp: '2021-06-20 11:12:32'
- Battery Level (%): 54.3
  Device ID: device-0051
  Device Type: Light Sensor
  Location: Bedroom
  Reading Value: 58.62
  Timestamp: '2021-08-16 05:48:14'
- Battery Level (%): 37.9
  Device ID: device-0036
  Device Type: Light Sensor
  Location: Bedroom
  Reading Value: -20.91
  Timestamp: '2022-05-03 10:05:46'
- Battery Level (%): 58.2
  Device ID: device-0034
  Device Type: Pressure Sensor
  Location: Kitchen
  Reading Value: 78.58
  Timestamp: '2021-07-27 01:35:54'
<end>Transform this csv structure to a yml format:
Restaurant Name,Cuisine,Location,Price Range
Taco Town,Indian,Chicago,$$$
Taco Town,Chinese,San Francisco,$$
Pizza Planet,Italian,Los Angeles,$$$
The Golden Spoon,Italian,Seattle,$$$$$
<start>
- Cuisine: Indian
  Location: Chicago
  Price Range: $$$
  Restaurant Name: Taco Town
- Cuisine: Chinese
  Location: San Francisco
  Price Range: $$
  Restaurant Name: Taco Town
- Cuisine: Italian
  Location: Los Angeles
  Price Range: $$$
  Restaurant Name: Pizza Planet
- Cuisine: Italian
  Location: Seattle
  Price Range: $$$$$
  Restaurant Name: The Golden Spoon
<end>Convert this Json to Yaml:
[
    {
        "Location": "Houston",
        "Condition": "Cloudy",
        "Temperature (C)": 8.6,
        "Humidity (%)": 70,
        "Wind Speed (km/h)": 24.0,
        "Day": "Sunday"
    },
    {
        "Location": "Los Angeles",
        "Condition": "Cloudy",
        "Temperature (C)": 4.3,
        "Humidity (%)": 39,
        "Wind Speed (km/h)": 5.2,
        "Day": "Tuesday"
    },
    {
        "Location": "Seattle",
        "Condition": "Rainy",
        "Temperature (C)": 3.7,
        "Humidity (%)": 41,
        "Wind Speed (km/h)": 24.0,
        "Day": "Friday"
    },
    {
        "Location": "Houston",
        "Condition": "Snowy",
        "Temperature (C)": 16.8,
        "Humidity (%)": 63,
        "Wind Speed (km/h)": 15.1,
        "Day": "Tuesday"
    }
]<start>
- Condition: Cloudy
  Day: Sunday
  Humidity (%): 70
  Location: Houston
  Temperature (C): 8.6
  Wind Speed (km/h): 24.0
- Condition: Cloudy
  Day: Tuesday
  Humidity (%): 39
  Location: Los Angeles
  Temperature (C): 4.3
  Wind Speed (km/h): 5.2
- Condition: Rainy
  Day: Friday
  Humidity (%): 41
  Location: Seattle
  Temperature (C): 3.7
  Wind Speed (km/h): 24.0
- Condition: Snowy
  Day: Tuesday
  Humidity (%): 63
  Location: Houston
  Temperature (C): 16.8
  Wind Speed (km/h): 15.1
<end>Here's some markdown data, can you convert it to csv?
| Condition | Temperature (C) | Day |
| --- | --- | --- |
| Snowy | 7.2 | Sunday |
| Snowy | 2.2 | Sunday |
| Snowy | 23.1 | Tuesday |<start>
Condition,Temperature (C),Day
Snowy,7.2,Sunday
Snowy,2.2,Sunday
Snowy,23.1,Tuesday
<end>Please transform the following CSV data into YML:
Product Name,Price,Stock Quantity,Category
Whatchamacallit,497.38,224,Automotive
Doohickey,311.52,28,Toys
Device,91.11,102,Sports
Contraption,319.09,386,Sports
Device,447.93,44,Automotive
Gizmo,311.52,364,Toys
Thingamajig,71.02,199,Toys
<start>
- Category: Automotive
  Price: 497.38
  Product Name: Whatchamacallit
  Stock Quantity: 224
- Category: Toys
  Price: 311.52
  Product Name: Doohickey
  Stock Quantity: 28
- Category: Sports
  Price: 91.11
  Product Name: Device
  Stock Quantity: 102
- Category: Sports
  Price: 319.09
  Product Name: Contraption
  Stock Quantity: 386
- Category: Automotive
  Price: 447.93
  Product Name: Device
  Stock Quantity: 44
- Category: Toys
  Price: 311.52
  Product Name: Gizmo
  Stock Quantity: 364
- Category: Toys
  Price: 71.02
  Product Name: Thingamajig
  Stock Quantity: 199
<end>Convert this markdown to json:
| Start Location | Distance (miles) | Fuel Used (gallons) |
| --- | --- | --- |
| San Francisco | 2507.7 | 19.2 |
| Miami | 2914.9 | 62.0 |
| San Francisco | 1829.9 | 59.3 |
| Miami | 2989.6 | 68.5 |
| Miami | 2082.3 | 91.0 |
| Miami | 1973.0 | 29.7 |
| San Francisco | 840.5 | 76.1 |
| Los Angeles | 324.5 | 29.7 |<start>
[
    {
        "Start Location": "San Francisco",
        "Distance (miles)": 2507.7,
        "Fuel Used (gallons)": 19.2
    },
    {
        "Start Location": "Miami",
        "Distance (miles)": 2914.9,
        "Fuel Used (gallons)": 62.0
    },
    {
        "Start Location": "San Francisco",
        "Distance (miles)": 1829.9,
        "Fuel Used (gallons)": 59.3
    },
    {
        "Start Location": "Miami",
        "Distance (miles)": 2989.6,
        "Fuel Used (gallons)": 68.5
    },
    {
        "Start Location": "Miami",
        "Distance (miles)": 2082.3,
        "Fuel Used (gallons)": 91.0
    },
    {
        "Start Location": "Miami",
        "Distance (miles)": 1973.0,
        "Fuel Used (gallons)": 29.7
    },
    {
        "Start Location": "San Francisco",
        "Distance (miles)": 840.5,
        "Fuel Used (gallons)": 76.1
    },
    {
        "Start Location": "Los Angeles",
        "Distance (miles)": 324.5,
        "Fuel Used (gallons)": 29.7
    }
]
<end>Convert this csv to json:
Restaurant Name,Location,Rating,Price Range
Curry Corner,Miami,1,$$$$
Curry Corner,Chicago,5,$
Taco Town,Houston,5,$$
Vegan Delight,Los Angeles,4,$$
Pizza Planet,Phoenix,4,$$$$
Sushi World,Miami,4,$$$$
The Golden Spoon,New York,5,$$
The Steakhouse,Phoenix,5,$$
<start>
[
    {
        "Restaurant Name": "Curry Corner",
        "Location": "Miami",
        "Rating": 1,
        "Price Range": "$$$$"
    },
    {
        "Restaurant Name": "Curry Corner",
        "Location": "Chicago",
        "Rating": 5,
        "Price Range": "$"
    },
    {
        "Restaurant Name": "Taco Town",
        "Location": "Houston",
        "Rating": 5,
        "Price Range": "$$"
    },
    {
        "Restaurant Name": "Vegan Delight",
        "Location": "Los Angeles",
        "Rating": 4,
        "Price Range": "$$"
    },
    {
        "Restaurant Name": "Pizza Planet",
        "Location": "Phoenix",
        "Rating": 4,
        "Price Range": "$$$$"
    },
    {
        "Restaurant Name": "Sushi World",
        "Location": "Miami",
        "Rating": 4,
        "Price Range": "$$$$"
    },
    {
        "Restaurant Name": "The Golden Spoon",
        "Location": "New York",
        "Rating": 5,
        "Price Range": "$$"
    },
    {
        "Restaurant Name": "The Steakhouse",
        "Location": "Phoenix",
        "Rating": 5,
        "Price Range": "$$"
    }
]
<end>Can you change this JSON into plain text?
[
    {
        "Start Location": "Chicago",
        "End Location": "New York",
        "Distance (miles)": 679.8
    },
    {
        "Start Location": "Phoenix",
        "End Location": "Houston",
        "Distance (miles)": 2163.2
    },
    {
        "Start Location": "Los Angeles",
        "End Location": "New York",
        "Distance (miles)": 2499.9
    },
    {
        "Start Location": "Miami",
        "End Location": "Houston",
        "Distance (miles)": 259.6
    },
    {
        "Start Location": "San Francisco",
        "End Location": "Houston",
        "Distance (miles)": 584.3
    },
    {
        "Start Location": "Phoenix",
        "End Location": "Chicago",
        "Distance (miles)": 392.4
    }
]<start>
Start Location: Chicago | End Location: New York | Distance (miles): 679.8
Start Location: Phoenix | End Location: Houston | Distance (miles): 2163.2
Start Location: Los Angeles | End Location: New York | Distance (miles): 2499.9
Start Location: Miami | End Location: Houston | Distance (miles): 259.6
Start Location: San Francisco | End Location: Houston | Distance (miles): 584.3
Start Location: Phoenix | End Location: Chicago | Distance (miles): 392.4
<end>Please transform the following CSV data into markdown:
Title,Author,Genre,Publication Year,Rating
The Last Sky,Sylvia Nightshade,Historical,2020,2.3
Whispers of the Abyss,Rowan Ashborne,Non-Fiction,1957,3.8
Echoes of Eternity,Kara Firebrand,Non-Fiction,1996,1.7
Tales of the Brave,Orion Frostblade,Science Fiction,1956,1.2
Legends of the Rift,Thorne Ironwood,Historical,1952,2.0
The Last Sky,Isla Windrider,Fantasy,1957,4.1
The Last Sky,Elara Moonshadow,Historical,2004,4.3
The Last Sky,Kara Firebrand,Horror,2020,4.6
The Crystal Key,Luna Silverleaf,Fantasy,1970,2.7
Tales of the Brave,Isla Windrider,Non-Fiction,2022,3.9
<start>
| Title | Author | Genre | Publication Year | Rating |
| --- | --- | --- | --- | --- |
| The Last Sky | Sylvia Nightshade | Historical | 2020 | 2.3 |
| Whispers of the Abyss | Rowan Ashborne | Non-Fiction | 1957 | 3.8 |
| Echoes of Eternity | Kara Firebrand | Non-Fiction | 1996 | 1.7 |
| Tales of the Brave | Orion Frostblade | Science Fiction | 1956 | 1.2 |
| Legends of the Rift | Thorne Ironwood | Historical | 1952 | 2.0 |
| The Last Sky | Isla Windrider | Fantasy | 1957 | 4.1 |
| The Last Sky | Elara Moonshadow | Historical | 2004 | 4.3 |
| The Last Sky | Kara Firebrand | Horror | 2020 | 4.6 |
| The Crystal Key | Luna Silverleaf | Fantasy | 1970 | 2.7 |
| Tales of the Brave | Isla Windrider | Non-Fiction | 2022 | 3.9 |
<end>Convert this markdown to Json:
| Device ID | Device Type | Location | Battery Level (%) | Timestamp |
| --- | --- | --- | --- | --- |
| device-0020 | Light Sensor | Living Room | 29.3 | 2023-11-12 08:42:10 |
| device-0052 | Temperature Sensor | Bathroom | 22.2 | 2022-12-01 14:51:19 |
| device-0041 | Motion Detector | Garage | 72.8 | 2023-11-03 07:30:45 |
| device-0078 | Light Sensor | Garden | 38.9 | 2021-11-03 09:49:40 |
| device-0028 | Temperature Sensor | Garage | 60.8 | 2022-01-13 23:09:44 |
| device-0059 | Pressure Sensor | Office | 25.6 | 2022-01-18 10:33:50 |
| device-0052 | Humidity Sensor | Living Room | 30.3 | 2021-01-19 03:39:18 |<start>
[
    {
        "Device ID": "device-0020",
        "Device Type": "Light Sensor",
        "Location": "Living Room",
        "Battery Level (%)": 29.3,
        "Timestamp": "2023-11-12 08:42:10"
    },
    {
        "Device ID": "device-0052",
        "Device Type": "Temperature Sensor",
        "Location": "Bathroom",
        "Battery Level (%)": 22.2,
        "Timestamp": "2022-12-01 14:51:19"
    },
    {
        "Device ID": "device-0041",
        "Device Type": "Motion Detector",
        "Location": "Garage",
        "Battery Level (%)": 72.8,
        "Timestamp": "2023-11-03 07:30:45"
    },
    {
        "Device ID": "device-0078",
        "Device Type": "Light Sensor",
        "Location": "Garden",
        "Battery Level (%)": 38.9,
        "Timestamp": "2021-11-03 09:49:40"
    },
    {
        "Device ID": "device-0028",
        "Device Type": "Temperature Sensor",
        "Location": "Garage",
        "Battery Level (%)": 60.8,
        "Timestamp": "2022-01-13 23:09:44"
    },
    {
        "Device ID": "device-0059",
        "Device Type": "Pressure Sensor",
        "Location": "Office",
        "Battery Level (%)": 25.6,
        "Timestamp": "2022-01-18 10:33:50"
    },
    {
        "Device ID": "device-0052",
        "Device Type": "Humidity Sensor",
        "Location": "Living Room",
        "Battery Level (%)": 30.3,
        "Timestamp": "2021-01-19 03:39:18"
    }
]
<end>Transform this yaml structure to a markdown format:
- Cuisine: French
  Restaurant Name: Taco Town
- Cuisine: French
  Restaurant Name: The Golden Spoon
- Cuisine: Mediterranean
  Restaurant Name: Curry Corner
- Cuisine: Mediterranean
  Restaurant Name: Vegan Delight
- Cuisine: French
  Restaurant Name: Burger Haven
- Cuisine: Mediterranean
  Restaurant Name: Pasta Palace
- Cuisine: American
  Restaurant Name: Vegan Delight
<start>
| Restaurant Name | Cuisine |
| --- | --- |
| Taco Town | French |
| The Golden Spoon | French |
| Curry Corner | Mediterranean |
| Vegan Delight | Mediterranean |
| Burger Haven | French |
| Pasta Palace | Mediterranean |
| Vegan Delight | American |
<end>Here's some Yml data, can you convert it to Json?
- Distance (miles): 1511.7
  Duration (hours): 66.3
  End Location: Chicago
  Start Location: Denver
  Trip Name: Mountain Adventure
- Distance (miles): 1573.6
  Duration (hours): 52.1
  End Location: San Francisco
  Start Location: Houston
  Trip Name: Desert Drive
- Distance (miles): 1417.4
  Duration (hours): 20.8
  End Location: Houston
  Start Location: Chicago
  Trip Name: Highway Odyssey
- Distance (miles): 1921.8
  Duration (hours): 70.0
  End Location: Denver
  Start Location: Phoenix
  Trip Name: Mountain Adventure
- Distance (miles): 1097.1
  Duration (hours): 66.8
  End Location: Denver
  Start Location: Miami
  Trip Name: Forest Journey
- Distance (miles): 1059.4
  Duration (hours): 52.1
  End Location: New York
  Start Location: Denver
  Trip Name: Historic Route
<start>
[
    {
        "Trip Name": "Mountain Adventure",
        "Start Location": "Denver",
        "End Location": "Chicago",
        "Distance (miles)": 1511.7,
        "Duration (hours)": 66.3
    },
    {
        "Trip Name": "Desert Drive",
        "Start Location": "Houston",
        "End Location": "San Francisco",
        "Distance (miles)": 1573.6,
        "Duration (hours)": 52.1
    },
    {
        "Trip Name": "Highway Odyssey",
        "Start Location": "Chicago",
        "End Location": "Houston",
        "Distance (miles)": 1417.4,
        "Duration (hours)": 20.8
    },
    {
        "Trip Name": "Mountain Adventure",
        "Start Location": "Phoenix",
        "End Location": "Denver",
        "Distance (miles)": 1921.8,
        "Duration (hours)": 70.0
    },
    {
        "Trip Name": "Forest Journey",
        "Start Location": "Miami",
        "End Location": "Denver",
        "Distance (miles)": 1097.1,
        "Duration (hours)": 66.8
    },
    {
        "Trip Name": "Historic Route",
        "Start Location": "Denver",
        "End Location": "New York",
        "Distance (miles)": 1059.4,
        "Duration (hours)": 52.1
    }
]
<end>Can you change this YAML into csv?
- Condition: Windy
  Day: Wednesday
  Humidity (%): 53
  Location: Seattle
  Temperature (C): 27.6
  Wind Speed (km/h): 20.2
- Condition: Sunny
  Day: Sunday
  Humidity (%): 82
  Location: Denver
  Temperature (C): -1.9
  Wind Speed (km/h): 14.7
- Condition: Stormy
  Day: Thursday
  Humidity (%): 93
  Location: New York
  Temperature (C): -4.2
  Wind Speed (km/h): 12.1
- Condition: Rainy
  Day: Saturday
  Humidity (%): 42
  Location: Houston
  Temperature (C): -5.4
  Wind Speed (km/h): 23.5
- Condition: Sunny
  Day: Saturday
  Humidity (%): 41
  Location: New York
  Temperature (C): 12.7
  Wind Speed (km/h): 27.0
- Condition: Snowy
  Day: Saturday
  Humidity (%): 84
  Location: Seattle
  Temperature (C): 0.1
  Wind Speed (km/h): 10.3
<start>
Location,Condition,Temperature (C),Humidity (%),Wind Speed (km/h),Day
Seattle,Windy,27.6,53,20.2,Wednesday
Denver,Sunny,-1.9,82,14.7,Sunday
New York,Stormy,-4.2,93,12.1,Thursday
Houston,Rainy,-5.4,42,23.5,Saturday
New York,Sunny,12.7,41,27.0,Saturday
Seattle,Snowy,0.1,84,10.3,Saturday
<end>Convert this YML to Csv:
- Close Price: 1150.01
  Company: HealthGen
  Date: '2018-03-10'
  Low Price: 318.58
  Open Price: 1076.56
- Close Price: 1316.41
  Company: BioLife
  Date: '2012-12-28'
  Low Price: 739.22
  Open Price: 1196.55
- Close Price: 159.42
  Company: RetailWorld
  Date: '2012-02-24'
  Low Price: 159.42
  Open Price: 487.7
- Close Price: 601.32
  Company: BioLife
  Date: '2020-04-13'
  Low Price: 599.03
  Open Price: 1495.16
- Close Price: 1215.68
  Company: FinanceTrust
  Date: '2010-07-27'
  Low Price: 238.87
  Open Price: 238.87
- Close Price: 1276.37
  Company: AutoMotive
  Date: '2011-08-12'
  Low Price: 136.53
  Open Price: 1101.19
- Close Price: 950.89
  Company: AutoMotive
  Date: '2011-04-14'
  Low Price: 254.82
  Open Price: 254.82
- Close Price: 599.03
  Company: MediaGroup
  Date: '2019-12-04'
  Low Price: 255.27
  Open Price: 1040.28
<start>
Company,Date,Open Price,Close Price,Low Price
HealthGen,2018-03-10,1076.56,1150.01,318.58
BioLife,2012-12-28,1196.55,1316.41,739.22
RetailWorld,2012-02-24,487.7,159.42,159.42
BioLife,2020-04-13,1495.16,601.32,599.03
FinanceTrust,2010-07-27,238.87,1215.68,238.87
AutoMotive,2011-08-12,1101.19,1276.37,136.53
AutoMotive,2011-04-14,254.82,950.89,254.82
MediaGroup,2019-12-04,1040.28,599.03,255.27
<end>Here's some plain text data, can you convert it to MARKDOWN?
Device ID: device-0056 | Device Type: Light Sensor | Location: Kitchen | Battery Level (%): 84.5 | Reading Value: 80.04 | Timestamp: 2022-02-25 10:22:05
Device ID: device-0055 | Device Type: Motion Detector | Location: Garage | Battery Level (%): 70.1 | Reading Value: 33.39 | Timestamp: 2021-06-09 20:00:38
Device ID: device-0040 | Device Type: Motion Detector | Location: Garden | Battery Level (%): 28.3 | Reading Value: -22.99 | Timestamp: 2021-05-13 04:59:20
Device ID: device-0076 | Device Type: Humidity Sensor | Location: Garage | Battery Level (%): 96.6 | Reading Value: -27.26 | Timestamp: 2022-02-07 04:14:49
Device ID: device-0063 | Device Type: Pressure Sensor | Location: Garden | Battery Level (%): 25.1 | Reading Value: 45.74 | Timestamp: 2022-10-09 02:43:53
Device ID: device-0019 | Device Type: Humidity Sensor | Location: Bedroom | Battery Level (%): 14.3 | Reading Value: -9.0 | Timestamp: 2022-03-01 08:51:22
<start>
| Device ID | Device Type | Location | Battery Level (%) | Reading Value | Timestamp |
| --- | --- | --- | --- | --- | --- |
| device-0056 | Light Sensor | Kitchen | 84.5 | 80.04 | 2022-02-25 10:22:05 |
| device-0055 | Motion Detector | Garage | 70.1 | 33.39 | 2021-06-09 20:00:38 |
| device-0040 | Motion Detector | Garden | 28.3 | -22.99 | 2021-05-13 04:59:20 |
| device-0076 | Humidity Sensor | Garage | 96.6 | -27.26 | 2022-02-07 04:14:49 |
| device-0063 | Pressure Sensor | Garden | 25.1 | 45.74 | 2022-10-09 02:43:53 |
| device-0019 | Humidity Sensor | Bedroom | 14.3 | -9.0 | 2022-03-01 08:51:22 |
<end>Please transform the following CSV data into PLAIN TEXT:
Name,Age,Birth Month,Income
Brad,18,September,30000
Steve,18,January,180000
Kirk,56,January,285000
Melissa,57,July,395000
<start>
Name: Brad | Age: 18 | Birth Month: September | Income: 30000
Name: Steve | Age: 18 | Birth Month: January | Income: 180000
Name: Kirk | Age: 56 | Birth Month: January | Income: 285000
Name: Melissa | Age: 57 | Birth Month: July | Income: 395000
<end>Please transform the following plain text data into JSON:
Title: The Endless Horizon | Release Year: 1983
Title: The Great Expedition | Release Year: 1990
Title: Edge of Infinity | Release Year: 2021
Title: Dreamwalker | Release Year: 1990
Title: Starbound Odyssey | Release Year: 1999
Title: Edge of Infinity | Release Year: 2004
Title: Mystery of the Depths | Release Year: 1972
Title: Escape from Earth | Release Year: 1993
<start>
[
    {
        "Title": "The Endless Horizon",
        "Release Year": 1983
    },
    {
        "Title": "The Great Expedition",
        "Release Year": 1990
    },
    {
        "Title": "Edge of Infinity",
        "Release Year": 2021
    },
    {
        "Title": "Dreamwalker",
        "Release Year": 1990
    },
    {
        "Title": "Starbound Odyssey",
        "Release Year": 1999
    },
    {
        "Title": "Edge of Infinity",
        "Release Year": 2004
    },
    {
        "Title": "Mystery of the Depths",
        "Release Year": 1972
    },
    {
        "Title": "Escape from Earth",
        "Release Year": 1993
    }
]
<end>Here's some yml data, can you convert it to markdown?
- Distance (miles): 2820.7
  Duration (hours): 32.6
  End Location: Denver
  Fuel Used (gallons): 39.8
  Start Location: Phoenix
  Trip Name: Highway Odyssey
- Distance (miles): 1558.8
  Duration (hours): 18.9
  End Location: Phoenix
  Fuel Used (gallons): 23.3
  Start Location: New York
  Trip Name: Lakeside Retreat
- Distance (miles): 471.8
  Duration (hours): 64.7
  End Location: Houston
  Fuel Used (gallons): 70.0
  Start Location: San Francisco
  Trip Name: Lakeside Retreat
<start>
| Trip Name | Start Location | End Location | Distance (miles) | Duration (hours) | Fuel Used (gallons) |
| --- | --- | --- | --- | --- | --- |
| Highway Odyssey | Phoenix | Denver | 2820.7 | 32.6 | 39.8 |
| Lakeside Retreat | New York | Phoenix | 1558.8 | 18.9 | 23.3 |
| Lakeside Retreat | San Francisco | Houston | 471.8 | 64.7 | 70.0 |
<end>Convert this Json to Csv:
[
    {
        "Trip Name": "Historic Route",
        "Start Location": "Denver",
        "End Location": "Phoenix",
        "Distance (miles)": 2061.7,
        "Duration (hours)": 62.9,
        "Fuel Used (gallons)": 65.5
    },
    {
        "Trip Name": "Lakeside Retreat",
        "Start Location": "New York",
        "End Location": "Denver",
        "Distance (miles)": 928.0,
        "Duration (hours)": 9.0,
        "Fuel Used (gallons)": 15.3
    },
    {
        "Trip Name": "Mountain Adventure",
        "Start Location": "Houston",
        "End Location": "New York",
        "Distance (miles)": 1376.9,
        "Duration (hours)": 2.4,
        "Fuel Used (gallons)": 33.3
    },
    {
        "Trip Name": "Historic Route",
        "Start Location": "Los Angeles",
        "End Location": "Chicago",
        "Distance (miles)": 2586.0,
        "Duration (hours)": 51.9,
        "Fuel Used (gallons)": 74.9
    },
    {
        "Trip Name": "Valley Voyage",
        "Start Location": "Miami",
        "End Location": "Denver",
        "Distance (miles)": 225.3,
        "Duration (hours)": 50.3,
        "Fuel Used (gallons)": 50.7
    },
    {
        "Trip Name": "Desert Drive",
        "Start Location": "New York",
        "End Location": "Miami",
        "Distance (miles)": 328.4,
        "Duration (hours)": 62.9,
        "Fuel Used (gallons)": 39.1
    }
]<start>
Trip Name,Start Location,End Location,Distance (miles),Duration (hours),Fuel Used (gallons)
Historic Route,Denver,Phoenix,2061.7,62.9,65.5
Lakeside Retreat,New York,Denver,928.0,9.0,15.3
Mountain Adventure,Houston,New York,1376.9,2.4,33.3
Historic Route,Los Angeles,Chicago,2586.0,51.9,74.9
Valley Voyage,Miami,Denver,225.3,50.3,50.7
Desert Drive,New York,Miami,328.4,62.9,39.1
<end>Transform this Json structure to a markdown format:
[
    {
        "Device ID": "device-0030",
        "Device Type": "Humidity Sensor",
        "Location": "Kitchen",
        "Battery Level (%)": 22.7,
        "Reading Value": -20.94,
        "Timestamp": "2021-07-24 19:55:52"
    },
    {
        "Device ID": "device-0058",
        "Device Type": "Humidity Sensor",
        "Location": "Hallway",
        "Battery Level (%)": 40.6,
        "Reading Value": 21.23,
        "Timestamp": "2023-11-06 19:25:34"
    },
    {
        "Device ID": "device-0069",
        "Device Type": "Motion Detector",
        "Location": "Kitchen",
        "Battery Level (%)": 24.1,
        "Reading Value": 10.88,
        "Timestamp": "2023-04-19 14:32:59"
    },
    {
        "Device ID": "device-0083",
        "Device Type": "Light Sensor",
        "Location": "Kitchen",
        "Battery Level (%)": 62.6,
        "Reading Value": 53.61,
        "Timestamp": "2021-07-02 11:08:16"
    },
    {
        "Device ID": "device-0011",
        "Device Type": "Motion Detector",
        "Location": "Bedroom",
        "Battery Level (%)": 64.2,
        "Reading Value": 1.46,
        "Timestamp": "2023-05-21 04:23:14"
    },
    {
        "Device ID": "device-0037",
        "Device Type": "Motion Detector",
        "Location": "Office",
        "Battery Level (%)": 85.6,
        "Reading Value": 13.2,
        "Timestamp": "2021-08-03 00:08:39"
    },
    {
        "Device ID": "device-0034",
        "Device Type": "Light Sensor",
        "Location": "Bedroom",
        "Battery Level (%)": 79.1,
        "Reading Value": 54.61,
        "Timestamp": "2021-10-27 10:05:21"
    },
    {
        "Device ID": "device-0050",
        "Device Type": "Temperature Sensor",
        "Location": "Bedroom",
        "Battery Level (%)": 58.9,
        "Reading Value": 35.46,
        "Timestamp": "2021-04-28 11:01:42"
    },
    {
        "Device ID": "device-0090",
        "Device Type": "Temperature Sensor",
        "Location": "Garage",
        "Battery Level (%)": 81.4,
        "Reading Value": -1.37,
        "Timestamp": "2022-05-20 17:16:26"
    }
]<start>
| Device ID | Device Type | Location | Battery Level (%) | Reading Value | Timestamp |
| --- | --- | --- | --- | --- | --- |
| device-0030 | Humidity Sensor | Kitchen | 22.7 | -20.94 | 2021-07-24 19:55:52 |
| device-0058 | Humidity Sensor | Hallway | 40.6 | 21.23 | 2023-11-06 19:25:34 |
| device-0069 | Motion Detector | Kitchen | 24.1 | 10.88 | 2023-04-19 14:32:59 |
| device-0083 | Light Sensor | Kitchen | 62.6 | 53.61 | 2021-07-02 11:08:16 |
| device-0011 | Motion Detector | Bedroom | 64.2 | 1.46 | 2023-05-21 04:23:14 |
| device-0037 | Motion Detector | Office | 85.6 | 13.2 | 2021-08-03 00:08:39 |
| device-0034 | Light Sensor | Bedroom | 79.1 | 54.61 | 2021-10-27 10:05:21 |
| device-0050 | Temperature Sensor | Bedroom | 58.9 | 35.46 | 2021-04-28 11:01:42 |
| device-0090 | Temperature Sensor | Garage | 81.4 | -1.37 | 2022-05-20 17:16:26 |
<end>Please transform the following json data into csv:
[
    {
        "Director": "Selene Darkwhisper",
        "Genre": "Adventure"
    },
    {
        "Director": "Cade Firebrand",
        "Genre": "Adventure"
    },
    {
        "Director": "Zara Stormrider",
        "Genre": "Sci-Fi"
    },
    {
        "Director": "Talon Blackthorn",
        "Genre": "Comedy"
    },
    {
        "Director": "Selene Darkwhisper",
        "Genre": "Comedy"
    },
    {
        "Director": "Cade Firebrand",
        "Genre": "Drama"
    },
    {
        "Director": "Mara Moonshadow",
        "Genre": "Sci-Fi"
    },
    {
        "Director": "Drake Nightshade",
        "Genre": "Thriller"
    }
]<start>
Director,Genre
Selene Darkwhisper,Adventure
Cade Firebrand,Adventure
Zara Stormrider,Sci-Fi
Talon Blackthorn,Comedy
Selene Darkwhisper,Comedy
Cade Firebrand,Drama
Mara Moonshadow,Sci-Fi
Drake Nightshade,Thriller
<end>Convert this JSON to markdown:
[
    {
        "Restaurant Name": "Burger Haven",
        "Cuisine": "Mediterranean",
        "Location": "Phoenix",
        "Rating": 3,
        "Price Range": "$$$$"
    },
    {
        "Restaurant Name": "The Golden Spoon",
        "Cuisine": "Italian",
        "Location": "Phoenix",
        "Rating": 4,
        "Price Range": "$$$"
    },
    {
        "Restaurant Name": "Pizza Planet",
        "Cuisine": "Mexican",
        "Location": "Phoenix",
        "Rating": 4,
        "Price Range": "$$"
    },
    {
        "Restaurant Name": "Pasta Palace",
        "Cuisine": "Indian",
        "Location": "San Francisco",
        "Rating": 2,
        "Price Range": "$$$$"
    },
    {
        "Restaurant Name": "Pizza Planet",
        "Cuisine": "Chinese",
        "Location": "Houston",
        "Rating": 2,
        "Price Range": "$$"
    },
    {
        "Restaurant Name": "Vegan Delight",
        "Cuisine": "French",
        "Location": "Houston",
        "Rating": 4,
        "Price Range": "$$$$"
    },
    {
        "Restaurant Name": "Vegan Delight",
        "Cuisine": "Mexican",
        "Location": "Phoenix",
        "Rating": 5,
        "Price Range": "$$$"
    }
]<start>
| Restaurant Name | Cuisine | Location | Rating | Price Range |
| --- | --- | --- | --- | --- |
| Burger Haven | Mediterranean | Phoenix | 3 | $$$$ |
| The Golden Spoon | Italian | Phoenix | 4 | $$$ |
| Pizza Planet | Mexican | Phoenix | 4 | $$ |
| Pasta Palace | Indian | San Francisco | 2 | $$$$ |
| Pizza Planet | Chinese | Houston | 2 | $$ |
| Vegan Delight | French | Houston | 4 | $$$$ |
| Vegan Delight | Mexican | Phoenix | 5 | $$$ |
<end>Please transform the following Yaml data into csv:
- Price Range: $$$$
  Restaurant Name: Vegan Delight
- Price Range: $$$
  Restaurant Name: The Steakhouse
- Price Range: $$$$
  Restaurant Name: Vegan Delight
- Price Range: $
  Restaurant Name: Taco Town
- Price Range: $
  Restaurant Name: The Steakhouse
- Price Range: $$$$$
  Restaurant Name: Burger Haven
- Price Range: $$$
  Restaurant Name: Taco Town
- Price Range: $
  Restaurant Name: Burger Haven
- Price Range: $$$$
  Restaurant Name: Curry Corner
<start>
Restaurant Name,Price Range
Vegan Delight,$$$$
The Steakhouse,$$$
Vegan Delight,$$$$
Taco Town,$
The Steakhouse,$
Burger Haven,$$$$$
Taco Town,$$$
Burger Haven,$
Curry Corner,$$$$
<end>Can you change this json into yaml?
[
    {
        "Company": "HealthGen",
        "Date": "2010-01-26",
        "High Price": 985.75,
        "Volume": 2458235
    },
    {
        "Company": "BioLife",
        "Date": "2015-04-14",
        "High Price": 1423.61,
        "Volume": 5664288
    },
    {
        "Company": "TechnoCorp",
        "Date": "2017-11-18",
        "High Price": 1440.0,
        "Volume": 5982210
    }
]<start>
- Company: HealthGen
  Date: '2010-01-26'
  High Price: 985.75
  Volume: 2458235
- Company: BioLife
  Date: '2015-04-14'
  High Price: 1423.61
  Volume: 5664288
- Company: TechnoCorp
  Date: '2017-11-18'
  High Price: 1440.0
  Volume: 5982210
<end>Transform this Csv structure to a JSON format:
Trip Name,Distance (miles),Duration (hours)
Coast to Coast,1392.0,61.3
Historic Route,177.3,13.2
Mountain Adventure,2946.5,34.7
Mountain Adventure,874.4,66.8
Desert Drive,2891.0,61.1
<start>
[
    {
        "Trip Name": "Coast to Coast",
        "Distance (miles)": 1392.0,
        "Duration (hours)": 61.3
    },
    {
        "Trip Name": "Historic Route",
        "Distance (miles)": 177.3,
        "Duration (hours)": 13.2
    },
    {
        "Trip Name": "Mountain Adventure",
        "Distance (miles)": 2946.5,
        "Duration (hours)": 34.7
    },
    {
        "Trip Name": "Mountain Adventure",
        "Distance (miles)": 874.4,
        "Duration (hours)": 66.8
    },
    {
        "Trip Name": "Desert Drive",
        "Distance (miles)": 2891.0,
        "Duration (hours)": 61.1
    }
]
<end>Please transform the following MARKDOWN data into Yaml:
| Title | Director | Genre | Release Year |
| --- | --- | --- | --- |
| The Great Expedition | Zara Stormrider | Action | 1972 |
| Beyond the Veil | Talon Blackthorn | Horror | 2019 |
| Escape from Earth | Talon Blackthorn | Sci-Fi | 1979 |<start>
- Director: Zara Stormrider
  Genre: Action
  Release Year: 1972
  Title: The Great Expedition
- Director: Talon Blackthorn
  Genre: Horror
  Release Year: 2019
  Title: Beyond the Veil
- Director: Talon Blackthorn
  Genre: Sci-Fi
  Release Year: 1979
  Title: Escape from Earth
<end>Here's some CSV data, can you convert it to yaml?
Company,Sector,Market Cap,Stock Price
BioPharm,Finance,Small Cap,153.47
RetailHub,Retail,Large Cap,929.24
Foodies,Healthcare,Mega Cap,232.27
TechCorp,Retail,Small Cap,493.86
FinanceWorks,Retail,Small Cap,388.76
EcoEnergy,Finance,Mid Cap,748.31
FinanceWorks,Energy,Mega Cap,503.54
RetailHub,Healthcare,Mid Cap,956.91
Foodies,Energy,Large Cap,16.41
<start>
- Company: BioPharm
  Market Cap: Small Cap
  Sector: Finance
  Stock Price: 153.47
- Company: RetailHub
  Market Cap: Large Cap
  Sector: Retail
  Stock Price: 929.24
- Company: Foodies
  Market Cap: Mega Cap
  Sector: Healthcare
  Stock Price: 232.27
- Company: TechCorp
  Market Cap: Small Cap
  Sector: Retail
  Stock Price: 493.86
- Company: FinanceWorks
  Market Cap: Small Cap
  Sector: Retail
  Stock Price: 388.76
- Company: EcoEnergy
  Market Cap: Mid Cap
  Sector: Finance
  Stock Price: 748.31
- Company: FinanceWorks
  Market Cap: Mega Cap
  Sector: Energy
  Stock Price: 503.54
- Company: RetailHub
  Market Cap: Mid Cap
  Sector: Healthcare
  Stock Price: 956.91
- Company: Foodies
  Market Cap: Large Cap
  Sector: Energy
  Stock Price: 16.41
<end>Here's some yaml data, can you convert it to json?
- Distance (miles): 939.1
  End Location: Houston
  Fuel Used (gallons): 93.4
  Start Location: Miami
  Trip Name: Mountain Adventure
- Distance (miles): 1962.0
  End Location: Denver
  Fuel Used (gallons): 68.1
  Start Location: Phoenix
  Trip Name: Coast to Coast
- Distance (miles): 2588.9
  End Location: Los Angeles
  Fuel Used (gallons): 99.8
  Start Location: Denver
  Trip Name: Lakeside Retreat
- Distance (miles): 190.1
  End Location: Houston
  Fuel Used (gallons): 43.4
  Start Location: Chicago
  Trip Name: Highway Odyssey
- Distance (miles): 1751.0
  End Location: Phoenix
  Fuel Used (gallons): 59.2
  Start Location: Denver
  Trip Name: Lakeside Retreat
- Distance (miles): 194.9
  End Location: Chicago
  Fuel Used (gallons): 63.5
  Start Location: Miami
  Trip Name: Forest Journey
<start>
[
    {
        "Trip Name": "Mountain Adventure",
        "Start Location": "Miami",
        "End Location": "Houston",
        "Distance (miles)": 939.1,
        "Fuel Used (gallons)": 93.4
    },
    {
        "Trip Name": "Coast to Coast",
        "Start Location": "Phoenix",
        "End Location": "Denver",
        "Distance (miles)": 1962.0,
        "Fuel Used (gallons)": 68.1
    },
    {
        "Trip Name": "Lakeside Retreat",
        "Start Location": "Denver",
        "End Location": "Los Angeles",
        "Distance (miles)": 2588.9,
        "Fuel Used (gallons)": 99.8
    },
    {
        "Trip Name": "Highway Odyssey",
        "Start Location": "Chicago",
        "End Location": "Houston",
        "Distance (miles)": 190.1,
        "Fuel Used (gallons)": 43.4
    },
    {
        "Trip Name": "Lakeside Retreat",
        "Start Location": "Denver",
        "End Location": "Phoenix",
        "Distance (miles)": 1751.0,
        "Fuel Used (gallons)": 59.2
    },
    {
        "Trip Name": "Forest Journey",
        "Start Location": "Miami",
        "End Location": "Chicago",
        "Distance (miles)": 194.9,
        "Fuel Used (gallons)": 63.5
    }
]
<end>Transform this Json structure to a Csv format:
[
    {
        "Trip Name": "Mountain Adventure",
        "Start Location": "San Francisco",
        "Duration (hours)": 58.6
    },
    {
        "Trip Name": "Lakeside Retreat",
        "Start Location": "Los Angeles",
        "Duration (hours)": 50.6
    },
    {
        "Trip Name": "Historic Route",
        "Start Location": "Miami",
        "Duration (hours)": 4.4
    },
    {
        "Trip Name": "Mountain Adventure",
        "Start Location": "Houston",
        "Duration (hours)": 50.6
    },
    {
        "Trip Name": "City Explorer",
        "Start Location": "New York",
        "Duration (hours)": 23.8
    },
    {
        "Trip Name": "City Explorer",
        "Start Location": "San Francisco",
        "Duration (hours)": 57.0
    },
    {
        "Trip Name": "Valley Voyage",
        "Start Location": "San Francisco",
        "Duration (hours)": 55.7
    },
    {
        "Trip Name": "Historic Route",
        "Start Location": "Denver",
        "Duration (hours)": 70.6
    }
]<start>
Trip Name,Start Location,Duration (hours)
Mountain Adventure,San Francisco,58.6
Lakeside Retreat,Los Angeles,50.6
Historic Route,Miami,4.4
Mountain Adventure,Houston,50.6
City Explorer,New York,23.8
City Explorer,San Francisco,57.0
Valley Voyage,San Francisco,55.7
Historic Route,Denver,70.6
<end>Can you change this csv into json?
Location,Reading Value,Timestamp
Bedroom,41.94,2022-05-06 19:01:50
Garden,-35.24,2022-06-24 15:05:24
Bathroom,10.92,2022-02-21 04:34:49
Garden,17.81,2023-12-02 09:41:46
Kitchen,44.48,2023-10-27 10:12:13
Bathroom,60.32,2021-11-07 21:47:26
<start>
[
    {
        "Location": "Bedroom",
        "Reading Value": 41.94,
        "Timestamp": "2022-05-06 19:01:50"
    },
    {
        "Location": "Garden",
        "Reading Value": -35.24,
        "Timestamp": "2022-06-24 15:05:24"
    },
    {
        "Location": "Bathroom",
        "Reading Value": 10.92,
        "Timestamp": "2022-02-21 04:34:49"
    },
    {
        "Location": "Garden",
        "Reading Value": 17.81,
        "Timestamp": "2023-12-02 09:41:46"
    },
    {
        "Location": "Kitchen",
        "Reading Value": 44.48,
        "Timestamp": "2023-10-27 10:12:13"
    },
    {
        "Location": "Bathroom",
        "Reading Value": 60.32,
        "Timestamp": "2021-11-07 21:47:26"
    }
]
<end>Here's some Json data, can you convert it to YAML?
[
    {
        "Title": "Shadows of Solitude",
        "Author": "Luna Silverleaf",
        "Genre": "Romance",
        "Publication Year": 2014,
        "Rating": 4.2
    },
    {
        "Title": "The Forgotten World",
        "Author": "Rowan Ashborne",
        "Genre": "Romance",
        "Publication Year": 1996,
        "Rating": 2.1
    },
    {
        "Title": "Shadows of Solitude",
        "Author": "Sylvia Nightshade",
        "Genre": "Horror",
        "Publication Year": 2013,
        "Rating": 4.3
    },
    {
        "Title": "A Journey Through Time",
        "Author": "Luna Silverleaf",
        "Genre": "Fantasy",
        "Publication Year": 1969,
        "Rating": 4.4
    },
    {
        "Title": "Whispers of the Abyss",
        "Author": "Elara Moonshadow",
        "Genre": "Mystery",
        "Publication Year": 1986,
        "Rating": 4.3
    }
]<start>
- Author: Luna Silverleaf
  Genre: Romance
  Publication Year: 2014
  Rating: 4.2
  Title: Shadows of Solitude
- Author: Rowan Ashborne
  Genre: Romance
  Publication Year: 1996
  Rating: 2.1
  Title: The Forgotten World
- Author: Sylvia Nightshade
  Genre: Horror
  Publication Year: 2013
  Rating: 4.3
  Title: Shadows of Solitude
- Author: Luna Silverleaf
  Genre: Fantasy
  Publication Year: 1969
  Rating: 4.4
  Title: A Journey Through Time
- Author: Elara Moonshadow
  Genre: Mystery
  Publication Year: 1986
  Rating: 4.3
  Title: Whispers of the Abyss
<end>Convert this csv to yml:
Title,Author,Genre,Publication Year,Rating
The Forgotten World,Kara Firebrand,Historical,1960,2.0
Whispers of the Abyss,Kara Firebrand,Mystery,1989,1.4
The Silent Grove,Rowan Ashborne,Historical,2022,1.1
The Crystal Key,Elara Moonshadow,Horror,1974,1.2
A Journey Through Time,Thorne Ironwood,Horror,1960,3.6
The Crystal Key,Galen Starfire,Mystery,1974,2.6
Whispers of the Abyss,Isla Windrider,Mystery,1954,3.9
The Silent Grove,Sylvia Nightshade,Science Fiction,2023,1.1
<start>
- Author: Kara Firebrand
  Genre: Historical
  Publication Year: 1960
  Rating: 2.0
  Title: The Forgotten World
- Author: Kara Firebrand
  Genre: Mystery
  Publication Year: 1989
  Rating: 1.4
  Title: Whispers of the Abyss
- Author: Rowan Ashborne
  Genre: Historical
  Publication Year: 2022
  Rating: 1.1
  Title: The Silent Grove
- Author: Elara Moonshadow
  Genre: Horror
  Publication Year: 1974
  Rating: 1.2
  Title: The Crystal Key
- Author: Thorne Ironwood
  Genre: Horror
  Publication Year: 1960
  Rating: 3.6
  Title: A Journey Through Time
- Author: Galen Starfire
  Genre: Mystery
  Publication Year: 1974
  Rating: 2.6
  Title: The Crystal Key
- Author: Isla Windrider
  Genre: Mystery
  Publication Year: 1954
  Rating: 3.9
  Title: Whispers of the Abyss
- Author: Sylvia Nightshade
  Genre: Science Fiction
  Publication Year: 2023
  Rating: 1.1
  Title: The Silent Grove
<end>Transform this PLAIN TEXT structure to a csv format:
Title: Tales of the Brave | Author: Luna Silverleaf | Publication Year: 2002 | Rating: 4.4
Title: The Forgotten World | Author: Sylvia Nightshade | Publication Year: 2016 | Rating: 4.2
Title: The Forgotten World | Author: Rowan Ashborne | Publication Year: 1970 | Rating: 2.0
Title: Tales of the Brave | Author: Thorne Ironwood | Publication Year: 1967 | Rating: 4.5
Title: The Silent Grove | Author: Kara Firebrand | Publication Year: 1967 | Rating: 2.1
Title: Shadows of Solitude | Author: Thorne Ironwood | Publication Year: 2002 | Rating: 2.1
Title: The Forgotten World | Author: Galen Starfire | Publication Year: 2017 | Rating: 3.4
Title: Tales of the Brave | Author: Elara Moonshadow | Publication Year: 1967 | Rating: 1.1
<start>
Title,Author,Publication Year,Rating
Tales of the Brave,Luna Silverleaf,2002,4.4
The Forgotten World,Sylvia Nightshade,2016,4.2
The Forgotten World,Rowan Ashborne,1970,2.0
Tales of the Brave,Thorne Ironwood,1967,4.5
The Silent Grove,Kara Firebrand,1967,2.1
Shadows of Solitude,Thorne Ironwood,2002,2.1
The Forgotten World,Galen Starfire,2017,3.4
Tales of the Brave,Elara Moonshadow,1967,1.1
<end>Convert this Json to markdown:
[
    {
        "Age": 65,
        "City": "Los Angeles",
        "Income": 90000
    },
    {
        "Age": 63,
        "City": "Baltimore",
        "Income": 55000
    },
    {
        "Age": 19,
        "City": "Boston",
        "Income": 320000
    },
    {
        "Age": 28,
        "City": "Washington",
        "Income": 70000
    },
    {
        "Age": 24,
        "City": "Portland",
        "Income": 165000
    }
]<start>
| Age | City | Income |
| --- | --- | --- |
| 65 | Los Angeles | 90000 |
| 63 | Baltimore | 55000 |
| 19 | Boston | 320000 |
| 28 | Washington | 70000 |
| 24 | Portland | 165000 |
<end>Convert this Json to PLAIN TEXT:
[
    {
        "Location": "Seattle",
        "Condition": "Snowy",
        "Temperature (C)": 15.6,
        "Humidity (%)": 42,
        "Day": "Wednesday"
    },
    {
        "Location": "New York",
        "Condition": "Foggy",
        "Temperature (C)": 26.4,
        "Humidity (%)": 21,
        "Day": "Monday"
    },
    {
        "Location": "Denver",
        "Condition": "Windy",
        "Temperature (C)": -6.1,
        "Humidity (%)": 41,
        "Day": "Monday"
    }
]<start>
Location: Seattle | Condition: Snowy | Temperature (C): 15.6 | Humidity (%): 42 | Day: Wednesday
Location: New York | Condition: Foggy | Temperature (C): 26.4 | Humidity (%): 21 | Day: Monday
Location: Denver | Condition: Windy | Temperature (C): -6.1 | Humidity (%): 41 | Day: Monday
<end>Here's some Csv data, can you convert it to Markdown?
Database Name,Connection Count,Average Latency (ms),Timestamp
ProductsDB,313,53.29,2023-01-04 20:41:47
MetricsDB,251,10.15,2021-07-06 19:45:13
SessionsDB,78,4.45,2021-02-26 00:17:28
SessionsDB,266,88.24,2022-04-08 18:55:13
AnalyticsDB,102,10.15,2021-01-08 15:35:53
SessionsDB,103,81.64,2023-06-05 13:14:44
<start>
| Database Name | Connection Count | Average Latency (ms) | Timestamp |
| --- | --- | --- | --- |
| ProductsDB | 313 | 53.29 | 2023-01-04 20:41:47 |
| MetricsDB | 251 | 10.15 | 2021-07-06 19:45:13 |
| SessionsDB | 78 | 4.45 | 2021-02-26 00:17:28 |
| SessionsDB | 266 | 88.24 | 2022-04-08 18:55:13 |
| AnalyticsDB | 102 | 10.15 | 2021-01-08 15:35:53 |
| SessionsDB | 103 | 81.64 | 2023-06-05 13:14:44 |
<end>Convert this PLAIN TEXT to Csv:
Name: Edith | Age: 60 | Birth Month: November | Income: 295000
Name: Joanne | Age: 60 | Birth Month: July | Income: 145000
Name: Tiffany | Age: 19 | Birth Month: September | Income: 175000
Name: Dwayne | Age: 63 | Birth Month: November | Income: 185000
<start>
Name,Age,Birth Month,Income
Edith,60,November,295000
Joanne,60,July,145000
Tiffany,19,September,175000
Dwayne,63,November,185000
<end>Please transform the following Csv data into MARKDOWN:
Name,Age,Birth Month,City,Income
Gregory,32,January,San Antonio,95000
Dalton,43,November,Denver,80000
Arlene,18,February,Los Angeles,75000
Lottie,18,April,San Jose,250000
Mckenzie,66,September,Washington,110000
Alex,65,August,Oklahoma City,295000
Alfred,18,February,Detroit,105000
<start>
| Name | Age | Birth Month | City | Income |
| --- | --- | --- | --- | --- |
| Gregory | 32 | January | San Antonio | 95000 |
| Dalton | 43 | November | Denver | 80000 |
| Arlene | 18 | February | Los Angeles | 75000 |
| Lottie | 18 | April | San Jose | 250000 |
| Mckenzie | 66 | September | Washington | 110000 |
| Alex | 65 | August | Oklahoma City | 295000 |
| Alfred | 18 | February | Detroit | 105000 |
<end>Convert this Json to plain text:
[
    {
        "Condition": "Sunny",
        "Temperature (C)": 34.2,
        "Wind Speed (km/h)": 2.9
    },
    {
        "Condition": "Rainy",
        "Temperature (C)": 30.4,
        "Wind Speed (km/h)": 11.6
    },
    {
        "Condition": "Snowy",
        "Temperature (C)": -7.2,
        "Wind Speed (km/h)": 29.5
    },
    {
        "Condition": "Cloudy",
        "Temperature (C)": 11.6,
        "Wind Speed (km/h)": 26.6
    },
    {
        "Condition": "Windy",
        "Temperature (C)": 16.1,
        "Wind Speed (km/h)": 20.4
    },
    {
        "Condition": "Stormy",
        "Temperature (C)": -8.0,
        "Wind Speed (km/h)": 0.6
    }
]<start>
Condition: Sunny | Temperature (C): 34.2 | Wind Speed (km/h): 2.9
Condition: Rainy | Temperature (C): 30.4 | Wind Speed (km/h): 11.6
Condition: Snowy | Temperature (C): -7.2 | Wind Speed (km/h): 29.5
Condition: Cloudy | Temperature (C): 11.6 | Wind Speed (km/h): 26.6
Condition: Windy | Temperature (C): 16.1 | Wind Speed (km/h): 20.4
Condition: Stormy | Temperature (C): -8.0 | Wind Speed (km/h): 0.6
<end>Convert this MARKDOWN to yml:
| Device ID | Device Type | Location | Battery Level (%) | Reading Value | Timestamp |
| --- | --- | --- | --- | --- | --- |
| device-0071 | Temperature Sensor | Garden | 95.8 | -2.84 | 2021-05-11 03:29:00 |
| device-0068 | Pressure Sensor | Garage | 67.6 | -1.71 | 2023-06-04 00:34:51 |
| device-0006 | Temperature Sensor | Hallway | 88.2 | -11.56 | 2023-01-16 06:14:06 |
| device-0027 | Humidity Sensor | Garage | 88.4 | 29.62 | 2022-05-17 07:16:57 |
| device-0071 | Pressure Sensor | Garden | 93.2 | 64.82 | 2022-06-15 14:00:36 |
| device-0095 | Humidity Sensor | Bathroom | 51.3 | 84.01 | 2022-11-25 11:54:10 |<start>
- Battery Level (%): 95.8
  Device ID: device-0071
  Device Type: Temperature Sensor
  Location: Garden
  Reading Value: -2.84
  Timestamp: '2021-05-11 03:29:00'
- Battery Level (%): 67.6
  Device ID: device-0068
  Device Type: Pressure Sensor
  Location: Garage
  Reading Value: -1.71
  Timestamp: '2023-06-04 00:34:51'
- Battery Level (%): 88.2
  Device ID: device-0006
  Device Type: Temperature Sensor
  Location: Hallway
  Reading Value: -11.56
  Timestamp: '2023-01-16 06:14:06'
- Battery Level (%): 88.4
  Device ID: device-0027
  Device Type: Humidity Sensor
  Location: Garage
  Reading Value: 29.62
  Timestamp: '2022-05-17 07:16:57'
- Battery Level (%): 93.2
  Device ID: device-0071
  Device Type: Pressure Sensor
  Location: Garden
  Reading Value: 64.82
  Timestamp: '2022-06-15 14:00:36'
- Battery Level (%): 51.3
  Device ID: device-0095
  Device Type: Humidity Sensor
  Location: Bathroom
  Reading Value: 84.01
  Timestamp: '2022-11-25 11:54:10'
<end>Transform this Plain text structure to a Csv format:
Author: Rowan Ashborne | Publication Year: 2011 | Rating: 3.6
Author: Orion Frostblade | Publication Year: 1970 | Rating: 3.3
Author: Draven Blackthorn | Publication Year: 2017 | Rating: 1.7
Author: Draven Blackthorn | Publication Year: 1993 | Rating: 2.8
Author: Draven Blackthorn | Publication Year: 2008 | Rating: 3.5
Author: Orion Frostblade | Publication Year: 2011 | Rating: 3.5
Author: Thorne Ironwood | Publication Year: 1979 | Rating: 2.2
Author: Kara Firebrand | Publication Year: 1963 | Rating: 3.9
Author: Draven Blackthorn | Publication Year: 2013 | Rating: 4.1
<start>
Author,Publication Year,Rating
Rowan Ashborne,2011,3.6
Orion Frostblade,1970,3.3
Draven Blackthorn,2017,1.7
Draven Blackthorn,1993,2.8
Draven Blackthorn,2008,3.5
Orion Frostblade,2011,3.5
Thorne Ironwood,1979,2.2
Kara Firebrand,1963,3.9
Draven Blackthorn,2013,4.1
<end>Can you change this PLAIN TEXT into markdown?
Company: RetailHub | Sector: Automotive | Annual Revenue (B): 237.39 | Quarter: Q4
Company: Foodies | Sector: Healthcare | Annual Revenue (B): 411.19 | Quarter: Q4
Company: RetailHub | Sector: Healthcare | Annual Revenue (B): 279.42 | Quarter: Q1
Company: GlobalTrade | Sector: Healthcare | Annual Revenue (B): 286.25 | Quarter: Q3
Company: RetailHub | Sector: Automotive | Annual Revenue (B): 331.02 | Quarter: Q1
<start>
| Company | Sector | Annual Revenue (B) | Quarter |
| --- | --- | --- | --- |
| RetailHub | Automotive | 237.39 | Q4 |
| Foodies | Healthcare | 411.19 | Q4 |
| RetailHub | Healthcare | 279.42 | Q1 |
| GlobalTrade | Healthcare | 286.25 | Q3 |
| RetailHub | Automotive | 331.02 | Q1 |
<end>Please transform the following plain text data into json:
Director: Drake Nightshade | Genre: Horror
Director: Aria Ravenwood | Genre: Action
Director: Rylan Frostblade | Genre: Sci-Fi
Director: Talon Blackthorn | Genre: Comedy
<start>
[
    {
        "Director": "Drake Nightshade",
        "Genre": "Horror"
    },
    {
        "Director": "Aria Ravenwood",
        "Genre": "Action"
    },
    {
        "Director": "Rylan Frostblade",
        "Genre": "Sci-Fi"
    },
    {
        "Director": "Talon Blackthorn",
        "Genre": "Comedy"
    }
]
<end>Can you change this json into csv?
[
    {
        "Company": "FinanceWorks",
        "Market Cap": "Mid Cap",
        "Annual Revenue (B)": 403.48
    },
    {
        "Company": "HealthPlus",
        "Market Cap": "Small Cap",
        "Annual Revenue (B)": 113.65
    },
    {
        "Company": "AutoDrive",
        "Market Cap": "Mid Cap",
        "Annual Revenue (B)": 437.77
    }
]<start>
Company,Market Cap,Annual Revenue (B)
FinanceWorks,Mid Cap,403.48
HealthPlus,Small Cap,113.65
AutoDrive,Mid Cap,437.77
<end>Transform this YML structure to a Plain text format:
- Age: 67
  City: Memphis
  Name: Grant
- Age: 40
  City: Jacksonville
  Name: Iva
- Age: 27
  City: Fort Worth
  Name: Luke
- Age: 38
  City: Oklahoma City
  Name: Lacey
- Age: 60
  City: Los Angeles
  Name: Micah
- Age: 57
  City: Jacksonville
  Name: Carmen
- Age: 67
  City: Washington
  Name: Bennett
- Age: 53
  City: Denver
  Name: Frank
<start>
Name: Grant | Age: 67 | City: Memphis
Name: Iva | Age: 40 | City: Jacksonville
Name: Luke | Age: 27 | City: Fort Worth
Name: Lacey | Age: 38 | City: Oklahoma City
Name: Micah | Age: 60 | City: Los Angeles
Name: Carmen | Age: 57 | City: Jacksonville
Name: Bennett | Age: 67 | City: Washington
Name: Frank | Age: 53 | City: Denver
<end>Convert this yml to Plain text:
- Category: Toys
  Price: 452.89
  Product Name: Apparatus
  SKU: SKU-1013
  Stock Quantity: 352
  Supplier Name: Umbrella Corp
- Category: Sports
  Price: 398.97
  Product Name: Widget
  SKU: SKU-1064
  Stock Quantity: 420
  Supplier Name: Globex
- Category: Electronics
  Price: 226.43
  Product Name: Gizmo
  SKU: SKU-1077
  Stock Quantity: 25
  Supplier Name: Wonka Industries
- Category: Electronics
  Price: 147.45
  Product Name: Whatchamacallit
  SKU: SKU-1001
  Stock Quantity: 5
  Supplier Name: ACME Corp
- Category: Household
  Price: 20.42
  Product Name: Widget
  SKU: SKU-1077
  Stock Quantity: 92
  Supplier Name: Wonka Industries
- Category: Household
  Price: 243.41
  Product Name: Gizmo
  SKU: SKU-1097
  Stock Quantity: 423
  Supplier Name: Umbrella Corp
- Category: Sports
  Price: 55.04
  Product Name: Thingamajig
  SKU: SKU-1018
  Stock Quantity: 262
  Supplier Name: Wayne Enterprises
- Category: Household
  Price: 350.08
  Product Name: Gadget
  SKU: SKU-1009
  Stock Quantity: 157
  Supplier Name: Globex
- Category: Automotive
  Price: 173.15
  Product Name: Whatchamacallit
  SKU: SKU-1023
  Stock Quantity: 350
  Supplier Name: Wayne Enterprises
<start>
Product Name: Apparatus | SKU: SKU-1013 | Price: 452.89 | Stock Quantity: 352 | Category: Toys | Supplier Name: Umbrella Corp
Product Name: Widget | SKU: SKU-1064 | Price: 398.97 | Stock Quantity: 420 | Category: Sports | Supplier Name: Globex
Product Name: Gizmo | SKU: SKU-1077 | Price: 226.43 | Stock Quantity: 25 | Category: Electronics | Supplier Name: Wonka Industries
Product Name: Whatchamacallit | SKU: SKU-1001 | Price: 147.45 | Stock Quantity: 5 | Category: Electronics | Supplier Name: ACME Corp
Product Name: Widget | SKU: SKU-1077 | Price: 20.42 | Stock Quantity: 92 | Category: Household | Supplier Name: Wonka Industries
Product Name: Gizmo | SKU: SKU-1097 | Price: 243.41 | Stock Quantity: 423 | Category: Household | Supplier Name: Umbrella Corp
Product Name: Thingamajig | SKU: SKU-1018 | Price: 55.04 | Stock Quantity: 262 | Category: Sports | Supplier Name: Wayne Enterprises
Product Name: Gadget | SKU: SKU-1009 | Price: 350.08 | Stock Quantity: 157 | Category: Household | Supplier Name: Globex
Product Name: Whatchamacallit | SKU: SKU-1023 | Price: 173.15 | Stock Quantity: 350 | Category: Automotive | Supplier Name: Wayne Enterprises
<end>Here's some json data, can you convert it to markdown?
[
    {
        "Cuisine": "French",
        "Rating": 4
    },
    {
        "Cuisine": "Mexican",
        "Rating": 4
    },
    {
        "Cuisine": "Italian",
        "Rating": 2
    },
    {
        "Cuisine": "Chinese",
        "Rating": 1
    },
    {
        "Cuisine": "American",
        "Rating": 3
    },
    {
        "Cuisine": "Japanese",
        "Rating": 2
    },
    {
        "Cuisine": "French",
        "Rating": 4
    },
    {
        "Cuisine": "Japanese",
        "Rating": 2
    }
]<start>
| Cuisine | Rating |
| --- | --- |
| French | 4 |
| Mexican | 4 |
| Italian | 2 |
| Chinese | 1 |
| American | 3 |
| Japanese | 2 |
| French | 4 |
| Japanese | 2 |
<end>Convert this JSON to Markdown:
[
    {
        "Restaurant Name": "BBQ Barn",
        "Cuisine": "American",
        "Rating": 4
    },
    {
        "Restaurant Name": "Pizza Planet",
        "Cuisine": "Mexican",
        "Rating": 3
    },
    {
        "Restaurant Name": "Pizza Planet",
        "Cuisine": "Italian",
        "Rating": 3
    },
    {
        "Restaurant Name": "The Steakhouse",
        "Cuisine": "American",
        "Rating": 1
    },
    {
        "Restaurant Name": "BBQ Barn",
        "Cuisine": "Mexican",
        "Rating": 4
    },
    {
        "Restaurant Name": "Curry Corner",
        "Cuisine": "Mexican",
        "Rating": 5
    },
    {
        "Restaurant Name": "Burger Haven",
        "Cuisine": "Japanese",
        "Rating": 2
    }
]<start>
| Restaurant Name | Cuisine | Rating |
| --- | --- | --- |
| BBQ Barn | American | 4 |
| Pizza Planet | Mexican | 3 |
| Pizza Planet | Italian | 3 |
| The Steakhouse | American | 1 |
| BBQ Barn | Mexican | 4 |
| Curry Corner | Mexican | 5 |
| Burger Haven | Japanese | 2 |
<end>Transform this JSON structure to a CSV format:
[
    {
        "Product Name": "Widget",
        "SKU": "SKU-1058",
        "Stock Quantity": 324,
        "Category": "Automotive",
        "Supplier Name": "Globex"
    },
    {
        "Product Name": "Whatchamacallit",
        "SKU": "SKU-1090",
        "Stock Quantity": 221,
        "Category": "Automotive",
        "Supplier Name": "Wayne Enterprises"
    },
    {
        "Product Name": "Thingamajig",
        "SKU": "SKU-1085",
        "Stock Quantity": 53,
        "Category": "Automotive",
        "Supplier Name": "ACME Corp"
    }
]<start>
Product Name,SKU,Stock Quantity,Category,Supplier Name
Widget,SKU-1058,324,Automotive,Globex
Whatchamacallit,SKU-1090,221,Automotive,Wayne Enterprises
Thingamajig,SKU-1085,53,Automotive,ACME Corp
<end>Convert this yml to JSON:
- Cuisine: Chinese
  Location: Houston
  Price Range: $
  Restaurant Name: Curry Corner
- Cuisine: French
  Location: Houston
  Price Range: $$$$$
  Restaurant Name: BBQ Barn
- Cuisine: Mediterranean
  Location: Miami
  Price Range: $$$$
  Restaurant Name: Burger Haven
- Cuisine: Japanese
  Location: Los Angeles
  Price Range: $$
  Restaurant Name: Taco Town
- Cuisine: Mediterranean
  Location: Miami
  Price Range: $
  Restaurant Name: Pizza Planet
- Cuisine: American
  Location: San Francisco
  Price Range: $$
  Restaurant Name: Pizza Planet
- Cuisine: Mediterranean
  Location: Houston
  Price Range: $$
  Restaurant Name: The Steakhouse
- Cuisine: Italian
  Location: San Francisco
  Price Range: $$
  Restaurant Name: Pasta Palace
- Cuisine: Mexican
  Location: Miami
  Price Range: $$$$$
  Restaurant Name: Burger Haven
<start>
[
    {
        "Restaurant Name": "Curry Corner",
        "Cuisine": "Chinese",
        "Location": "Houston",
        "Price Range": "$"
    },
    {
        "Restaurant Name": "BBQ Barn",
        "Cuisine": "French",
        "Location": "Houston",
        "Price Range": "$$$$$"
    },
    {
        "Restaurant Name": "Burger Haven",
        "Cuisine": "Mediterranean",
        "Location": "Miami",
        "Price Range": "$$$$"
    },
    {
        "Restaurant Name": "Taco Town",
        "Cuisine": "Japanese",
        "Location": "Los Angeles",
        "Price Range": "$$"
    },
    {
        "Restaurant Name": "Pizza Planet",
        "Cuisine": "Mediterranean",
        "Location": "Miami",
        "Price Range": "$"
    },
    {
        "Restaurant Name": "Pizza Planet",
        "Cuisine": "American",
        "Location": "San Francisco",
        "Price Range": "$$"
    },
    {
        "Restaurant Name": "The Steakhouse",
        "Cuisine": "Mediterranean",
        "Location": "Houston",
        "Price Range": "$$"
    },
    {
        "Restaurant Name": "Pasta Palace",
        "Cuisine": "Italian",
        "Location": "San Francisco",
        "Price Range": "$$"
    },
    {
        "Restaurant Name": "Burger Haven",
        "Cuisine": "Mexican",
        "Location": "Miami",
        "Price Range": "$$$$$"
    }
]
<end>Can you change this plain text into csv?
Trip Name: City Explorer | Start Location: San Francisco | End Location: Los Angeles | Distance (miles): 1770.0 | Duration (hours): 33.1
Trip Name: Lakeside Retreat | Start Location: Chicago | End Location: Los Angeles | Distance (miles): 2262.7 | Duration (hours): 50.3
Trip Name: Canyon Trek | Start Location: Los Angeles | End Location: New York | Distance (miles): 738.0 | Duration (hours): 64.2
Trip Name: Desert Drive | Start Location: Phoenix | End Location: Houston | Distance (miles): 286.9 | Duration (hours): 19.9
Trip Name: Lakeside Retreat | Start Location: New York | End Location: Denver | Distance (miles): 952.4 | Duration (hours): 16.7
Trip Name: Valley Voyage | Start Location: Houston | End Location: Denver | Distance (miles): 2227.7 | Duration (hours): 7.6
<start>
Trip Name,Start Location,End Location,Distance (miles),Duration (hours)
City Explorer,San Francisco,Los Angeles,1770.0,33.1
Lakeside Retreat,Chicago,Los Angeles,2262.7,50.3
Canyon Trek,Los Angeles,New York,738.0,64.2
Desert Drive,Phoenix,Houston,286.9,19.9
Lakeside Retreat,New York,Denver,952.4,16.7
Valley Voyage,Houston,Denver,2227.7,7.6
<end>Transform this markdown structure to a Yaml format:
| Title | Author |
| --- | --- |
| The Last Sky | Draven Blackthorn |
| The Forgotten World | Isla Windrider |
| The Last Sky | Sylvia Nightshade |
| Shadows of Solitude | Orion Frostblade |
| The Silent Grove | Orion Frostblade |
| Whispers of the Abyss | Draven Blackthorn |
| Shadows of Solitude | Isla Windrider |
| The Forgotten World | Kara Firebrand |
| Echoes of Eternity | Sylvia Nightshade |
| The Last Sky | Rowan Ashborne |<start>
- Author: Draven Blackthorn
  Title: The Last Sky
- Author: Isla Windrider
  Title: The Forgotten World
- Author: Sylvia Nightshade
  Title: The Last Sky
- Author: Orion Frostblade
  Title: Shadows of Solitude
- Author: Orion Frostblade
  Title: The Silent Grove
- Author: Draven Blackthorn
  Title: Whispers of the Abyss
- Author: Isla Windrider
  Title: Shadows of Solitude
- Author: Kara Firebrand
  Title: The Forgotten World
- Author: Sylvia Nightshade
  Title: Echoes of Eternity
- Author: Rowan Ashborne
  Title: The Last Sky
<end>Transform this json structure to a yaml format:
[
    {
        "Director": "Aria Ravenwood",
        "Box Office Earnings (M)": 76.72
    },
    {
        "Director": "Orin Shadowalker",
        "Box Office Earnings (M)": 734.33
    },
    {
        "Director": "Lira Silverleaf",
        "Box Office Earnings (M)": 428.23
    },
    {
        "Director": "Drake Nightshade",
        "Box Office Earnings (M)": 219.72
    },
    {
        "Director": "Zara Stormrider",
        "Box Office Earnings (M)": 347.62
    },
    {
        "Director": "Lira Silverleaf",
        "Box Office Earnings (M)": 39.65
    },
    {
        "Director": "Cade Firebrand",
        "Box Office Earnings (M)": 775.72
    },
    {
        "Director": "Cade Firebrand",
        "Box Office Earnings (M)": 637.88
    }
]<start>
- Box Office Earnings (M): 76.72
  Director: Aria Ravenwood
- Box Office Earnings (M): 734.33
  Director: Orin Shadowalker
- Box Office Earnings (M): 428.23
  Director: Lira Silverleaf
- Box Office Earnings (M): 219.72
  Director: Drake Nightshade
- Box Office Earnings (M): 347.62
  Director: Zara Stormrider
- Box Office Earnings (M): 39.65
  Director: Lira Silverleaf
- Box Office Earnings (M): 775.72
  Director: Cade Firebrand
- Box Office Earnings (M): 637.88
  Director: Cade Firebrand
<end>Transform this csv structure to a MARKDOWN format:
Title,Director,Genre,Box Office Earnings (M)
The Great Expedition,Orin Shadowalker,Drama,387.26
Rise of the Titans,Cade Firebrand,Action,911.12
The Great Expedition,Selene Darkwhisper,Fantasy,640.11
Mystery of the Depths,Mara Moonshadow,Comedy,623.01
Edge of Infinity,Talon Blackthorn,Adventure,565.44
Beyond the Veil,Mara Moonshadow,Comedy,964.91
<start>
| Title | Director | Genre | Box Office Earnings (M) |
| --- | --- | --- | --- |
| The Great Expedition | Orin Shadowalker | Drama | 387.26 |
| Rise of the Titans | Cade Firebrand | Action | 911.12 |
| The Great Expedition | Selene Darkwhisper | Fantasy | 640.11 |
| Mystery of the Depths | Mara Moonshadow | Comedy | 623.01 |
| Edge of Infinity | Talon Blackthorn | Adventure | 565.44 |
| Beyond the Veil | Mara Moonshadow | Comedy | 964.91 |
<end>Convert this YAML to Plain text:
- Average Latency (ms): 49.18
  Connection Count: 77
  Database Name: LogsDB
  Queries per Second: 69.19
- Average Latency (ms): 52.88
  Connection Count: 64
  Database Name: LogsDB
  Queries per Second: 3258.58
- Average Latency (ms): 85.72
  Connection Count: 39
  Database Name: InventoryDB
  Queries per Second: 2998.01
- Average Latency (ms): 47.97
  Connection Count: 249
  Database Name: MetricsDB
  Queries per Second: 1616.94
- Average Latency (ms): 79.78
  Connection Count: 367
  Database Name: ProductsDB
  Queries per Second: 2143.21
- Average Latency (ms): 85.29
  Connection Count: 275
  Database Name: OrdersDB
  Queries per Second: 3461.04
- Average Latency (ms): 1.6
  Connection Count: 158
  Database Name: ProductsDB
  Queries per Second: 304.63
- Average Latency (ms): 37.63
  Connection Count: 14
  Database Name: SessionsDB
  Queries per Second: 949.89
- Average Latency (ms): 40.77
  Connection Count: 432
  Database Name: AnalyticsDB
  Queries per Second: 3789.44
<start>
Database Name: LogsDB | Queries per Second: 69.19 | Connection Count: 77 | Average Latency (ms): 49.18
Database Name: LogsDB | Queries per Second: 3258.58 | Connection Count: 64 | Average Latency (ms): 52.88
Database Name: InventoryDB | Queries per Second: 2998.01 | Connection Count: 39 | Average Latency (ms): 85.72
Database Name: MetricsDB | Queries per Second: 1616.94 | Connection Count: 249 | Average Latency (ms): 47.97
Database Name: ProductsDB | Queries per Second: 2143.21 | Connection Count: 367 | Average Latency (ms): 79.78
Database Name: OrdersDB | Queries per Second: 3461.04 | Connection Count: 275 | Average Latency (ms): 85.29
Database Name: ProductsDB | Queries per Second: 304.63 | Connection Count: 158 | Average Latency (ms): 1.6
Database Name: SessionsDB | Queries per Second: 949.89 | Connection Count: 14 | Average Latency (ms): 37.63
Database Name: AnalyticsDB | Queries per Second: 3789.44 | Connection Count: 432 | Average Latency (ms): 40.77
<end>Here's some JSON data, can you convert it to Plain text?
[
    {
        "Company": "MediaGroup",
        "Date": "2021-04-06",
        "Open Price": 1187.73,
        "Close Price": 653.91,
        "High Price": 1187.73,
        "Low Price": 236.02,
        "Volume": 3341824
    },
    {
        "Company": "HealthGen",
        "Date": "2021-11-17",
        "Open Price": 1187.73,
        "Close Price": 542.09,
        "High Price": 1187.73,
        "Low Price": 542.09,
        "Volume": 283631
    },
    {
        "Company": "TechnoCorp",
        "Date": "2014-06-19",
        "Open Price": 102.19,
        "Close Price": 667.98,
        "High Price": 1350.99,
        "Low Price": 102.19,
        "Volume": 8263121
    },
    {
        "Company": "GreenEnergy",
        "Date": "2011-11-04",
        "Open Price": 246.21,
        "Close Price": 1427.37,
        "High Price": 1427.37,
        "Low Price": 246.21,
        "Volume": 5134576
    },
    {
        "Company": "AeroSystems",
        "Date": "2010-03-02",
        "Open Price": 629.68,
        "Close Price": 12.84,
        "High Price": 1169.68,
        "Low Price": 12.84,
        "Volume": 9362218
    }
]<start>
Company: MediaGroup | Date: 2021-04-06 | Open Price: 1187.73 | Close Price: 653.91 | High Price: 1187.73 | Low Price: 236.02 | Volume: 3341824
Company: HealthGen | Date: 2021-11-17 | Open Price: 1187.73 | Close Price: 542.09 | High Price: 1187.73 | Low Price: 542.09 | Volume: 283631
Company: TechnoCorp | Date: 2014-06-19 | Open Price: 102.19 | Close Price: 667.98 | High Price: 1350.99 | Low Price: 102.19 | Volume: 8263121
Company: GreenEnergy | Date: 2011-11-04 | Open Price: 246.21 | Close Price: 1427.37 | High Price: 1427.37 | Low Price: 246.21 | Volume: 5134576
Company: AeroSystems | Date: 2010-03-02 | Open Price: 629.68 | Close Price: 12.84 | High Price: 1169.68 | Low Price: 12.84 | Volume: 9362218
<end>Can you change this Json into markdown?
[
    {
        "Trip Name": "Forest Journey",
        "Start Location": "Denver",
        "End Location": "Houston",
        "Distance (miles)": 1003.5,
        "Duration (hours)": 71.0,
        "Fuel Used (gallons)": 19.0
    },
    {
        "Trip Name": "Historic Route",
        "Start Location": "Miami",
        "End Location": "Los Angeles",
        "Distance (miles)": 486.3,
        "Duration (hours)": 54.0,
        "Fuel Used (gallons)": 56.2
    },
    {
        "Trip Name": "Historic Route",
        "Start Location": "San Francisco",
        "End Location": "Houston",
        "Distance (miles)": 382.3,
        "Duration (hours)": 41.7,
        "Fuel Used (gallons)": 33.0
    },
    {
        "Trip Name": "Highway Odyssey",
        "Start Location": "Denver",
        "End Location": "New York",
        "Distance (miles)": 2415.6,
        "Duration (hours)": 35.7,
        "Fuel Used (gallons)": 69.4
    },
    {
        "Trip Name": "Canyon Trek",
        "Start Location": "Chicago",
        "End Location": "San Francisco",
        "Distance (miles)": 2124.3,
        "Duration (hours)": 59.6,
        "Fuel Used (gallons)": 33.0
    },
    {
        "Trip Name": "Highway Odyssey",
        "Start Location": "Los Angeles",
        "End Location": "Houston",
        "Distance (miles)": 2907.2,
        "Duration (hours)": 33.5,
        "Fuel Used (gallons)": 11.5
    },
    {
        "Trip Name": "City Explorer",
        "Start Location": "Miami",
        "End Location": "San Francisco",
        "Distance (miles)": 2529.1,
        "Duration (hours)": 8.1,
        "Fuel Used (gallons)": 23.3
    }
]<start>
| Trip Name | Start Location | End Location | Distance (miles) | Duration (hours) | Fuel Used (gallons) |
| --- | --- | --- | --- | --- | --- |
| Forest Journey | Denver | Houston | 1003.5 | 71.0 | 19.0 |
| Historic Route | Miami | Los Angeles | 486.3 | 54.0 | 56.2 |
| Historic Route | San Francisco | Houston | 382.3 | 41.7 | 33.0 |
| Highway Odyssey | Denver | New York | 2415.6 | 35.7 | 69.4 |
| Canyon Trek | Chicago | San Francisco | 2124.3 | 59.6 | 33.0 |
| Highway Odyssey | Los Angeles | Houston | 2907.2 | 33.5 | 11.5 |
| City Explorer | Miami | San Francisco | 2529.1 | 8.1 | 23.3 |
<end>Please transform the following MARKDOWN data into csv:
| Trip Name | End Location | Distance (miles) |
| --- | --- | --- |
| Coast to Coast | Los Angeles | 2332.9 |
| Forest Journey | Denver | 850.0 |
| Highway Odyssey | Chicago | 732.9 |
| Historic Route | Miami | 1748.1 |
| Mountain Adventure | Phoenix | 1869.5 |
| Canyon Trek | Chicago | 1991.5 |<start>
Trip Name,End Location,Distance (miles)
Coast to Coast,Los Angeles,2332.9
Forest Journey,Denver,850.0
Highway Odyssey,Chicago,732.9
Historic Route,Miami,1748.1
Mountain Adventure,Phoenix,1869.5
Canyon Trek,Chicago,1991.5
<end>Can you change this PLAIN TEXT into YML?
Title: Starbound Odyssey | Director: Mara Moonshadow | Release Year: 2002
Title: Dreamwalker | Director: Mara Moonshadow | Release Year: 1976
Title: Beyond the Veil | Director: Selene Darkwhisper | Release Year: 2015
Title: Mystery of the Depths | Director: Cade Firebrand | Release Year: 2004
Title: The Final Voyage | Director: Talon Blackthorn | Release Year: 2002
Title: Escape from Earth | Director: Zara Stormrider | Release Year: 1992
Title: Escape from Earth | Director: Drake Nightshade | Release Year: 2004
Title: The Great Expedition | Director: Zara Stormrider | Release Year: 2005
<start>
- Director: Mara Moonshadow
  Release Year: 2002
  Title: Starbound Odyssey
- Director: Mara Moonshadow
  Release Year: 1976
  Title: Dreamwalker
- Director: Selene Darkwhisper
  Release Year: 2015
  Title: Beyond the Veil
- Director: Cade Firebrand
  Release Year: 2004
  Title: Mystery of the Depths
- Director: Talon Blackthorn
  Release Year: 2002
  Title: The Final Voyage
- Director: Zara Stormrider
  Release Year: 1992
  Title: Escape from Earth
- Director: Drake Nightshade
  Release Year: 2004
  Title: Escape from Earth
- Director: Zara Stormrider
  Release Year: 2005
  Title: The Great Expedition
<end>Can you change this plain text into csv?
Company: AeroSystems | Date: 2018-10-25 | Open Price: 557.83 | Close Price: 470.13 | High Price: 557.83 | Low Price: 470.13 | Volume: 3098553
Company: HealthGen | Date: 2019-12-25 | Open Price: 959.32 | Close Price: 212.36 | High Price: 959.32 | Low Price: 212.36 | Volume: 4296043
Company: FoodChain | Date: 2022-08-05 | Open Price: 959.32 | Close Price: 697.15 | High Price: 959.32 | Low Price: 129.14 | Volume: 8044187
Company: AutoMotive | Date: 2020-01-04 | Open Price: 82.69 | Close Price: 75.51 | High Price: 667.99 | Low Price: 75.51 | Volume: 2134183
Company: GreenEnergy | Date: 2020-07-26 | Open Price: 882.44 | Close Price: 882.44 | High Price: 1190.5 | Low Price: 717.65 | Volume: 9409896
<start>
Company,Date,Open Price,Close Price,High Price,Low Price,Volume
AeroSystems,2018-10-25,557.83,470.13,557.83,470.13,3098553
HealthGen,2019-12-25,959.32,212.36,959.32,212.36,4296043
FoodChain,2022-08-05,959.32,697.15,959.32,129.14,8044187
AutoMotive,2020-01-04,82.69,75.51,667.99,75.51,2134183
GreenEnergy,2020-07-26,882.44,882.44,1190.5,717.65,9409896
<end>Can you change this CSV into markdown?
Trip Name,Start Location,End Location,Distance (miles),Duration (hours),Fuel Used (gallons)
Coast to Coast,Phoenix,Denver,432.4,49.5,23.9
Coast to Coast,Miami,New York,2299.1,50.3,27.8
Highway Odyssey,Los Angeles,San Francisco,1448.7,60.7,37.8
City Explorer,New York,Chicago,1367.0,50.8,44.4
Highway Odyssey,Phoenix,Chicago,1732.1,46.5,64.9
Mountain Adventure,Houston,Phoenix,1044.4,13.8,75.0
Mountain Adventure,New York,Chicago,1864.6,25.4,75.0
City Explorer,San Francisco,Miami,397.8,43.1,30.4
Desert Drive,Miami,San Francisco,299.5,59.9,50.6
<start>
| Trip Name | Start Location | End Location | Distance (miles) | Duration (hours) | Fuel Used (gallons) |
| --- | --- | --- | --- | --- | --- |
| Coast to Coast | Phoenix | Denver | 432.4 | 49.5 | 23.9 |
| Coast to Coast | Miami | New York | 2299.1 | 50.3 | 27.8 |
| Highway Odyssey | Los Angeles | San Francisco | 1448.7 | 60.7 | 37.8 |
| City Explorer | New York | Chicago | 1367.0 | 50.8 | 44.4 |
| Highway Odyssey | Phoenix | Chicago | 1732.1 | 46.5 | 64.9 |
| Mountain Adventure | Houston | Phoenix | 1044.4 | 13.8 | 75.0 |
| Mountain Adventure | New York | Chicago | 1864.6 | 25.4 | 75.0 |
| City Explorer | San Francisco | Miami | 397.8 | 43.1 | 30.4 |
| Desert Drive | Miami | San Francisco | 299.5 | 59.9 | 50.6 |
<end>Convert this Plain text to markdown:
Cuisine: Japanese | Location: Phoenix | Rating: 4
Cuisine: Chinese | Location: Seattle | Rating: 2
Cuisine: Italian | Location: Phoenix | Rating: 5
<start>
| Cuisine | Location | Rating |
| --- | --- | --- |
| Japanese | Phoenix | 4 |
| Chinese | Seattle | 2 |
| Italian | Phoenix | 5 |
<end>Transform this json structure to a YML format:
[
    {
        "Condition": "Rainy",
        "Temperature (C)": -4.2,
        "Humidity (%)": 52,
        "Wind Speed (km/h)": 20.9
    },
    {
        "Condition": "Cloudy",
        "Temperature (C)": -6.7,
        "Humidity (%)": 91,
        "Wind Speed (km/h)": 27.2
    },
    {
        "Condition": "Foggy",
        "Temperature (C)": 34.8,
        "Humidity (%)": 88,
        "Wind Speed (km/h)": 6.5
    }
]<start>
- Condition: Rainy
  Humidity (%): 52
  Temperature (C): -4.2
  Wind Speed (km/h): 20.9
- Condition: Cloudy
  Humidity (%): 91
  Temperature (C): -6.7
  Wind Speed (km/h): 27.2
- Condition: Foggy
  Humidity (%): 88
  Temperature (C): 34.8
  Wind Speed (km/h): 6.5
<end>Here's some Yaml data, can you convert it to CSV?
- Condition: Foggy
  Day: Saturday
  Humidity (%): 86
  Location: Houston
  Temperature (C): -10.0
  Wind Speed (km/h): 23.7
- Condition: Cloudy
  Day: Thursday
  Humidity (%): 25
  Location: Seattle
  Temperature (C): -4.1
  Wind Speed (km/h): 13.4
- Condition: Rainy
  Day: Wednesday
  Humidity (%): 73
  Location: Phoenix
  Temperature (C): 22.5
  Wind Speed (km/h): 1.9
- Condition: Rainy
  Day: Wednesday
  Humidity (%): 31
  Location: Los Angeles
  Temperature (C): 33.0
  Wind Speed (km/h): 13.1
- Condition: Sunny
  Day: Tuesday
  Humidity (%): 25
  Location: Denver
  Temperature (C): 27.5
  Wind Speed (km/h): 6.0
- Condition: Cloudy
  Day: Saturday
  Humidity (%): 42
  Location: Denver
  Temperature (C): 29.7
  Wind Speed (km/h): 3.4
<start>
Location,Condition,Temperature (C),Humidity (%),Wind Speed (km/h),Day
Houston,Foggy,-10.0,86,23.7,Saturday
Seattle,Cloudy,-4.1,25,13.4,Thursday
Phoenix,Rainy,22.5,73,1.9,Wednesday
Los Angeles,Rainy,33.0,31,13.1,Wednesday
Denver,Sunny,27.5,25,6.0,Tuesday
Denver,Cloudy,29.7,42,3.4,Saturday
<end>Here's some PLAIN TEXT data, can you convert it to CSV?
Title: Rise of the Titans | Director: Lira Silverleaf | Release Year: 2014
Title: The Endless Horizon | Director: Zara Stormrider | Release Year: 1979
Title: The Great Expedition | Director: Selene Darkwhisper | Release Year: 2011
<start>
Title,Director,Release Year
Rise of the Titans,Lira Silverleaf,2014
The Endless Horizon,Zara Stormrider,1979
The Great Expedition,Selene Darkwhisper,2011
<end>Transform this YAML structure to a CSV format:
- Duration (hours): 36.5
  End Location: Miami
  Start Location: Denver
- Duration (hours): 66.8
  End Location: San Francisco
  Start Location: Los Angeles
- Duration (hours): 22.9
  End Location: New York
  Start Location: Chicago
<start>
Start Location,End Location,Duration (hours)
Denver,Miami,36.5
Los Angeles,San Francisco,66.8
Chicago,New York,22.9
<end>Transform this yml structure to a markdown format:
- Battery Level (%): 29.4
  Device ID: device-0084
  Device Type: Pressure Sensor
  Reading Value: 74.69
  Timestamp: '2023-06-15 01:42:29'
- Battery Level (%): 44.1
  Device ID: device-0020
  Device Type: Pressure Sensor
  Reading Value: 39.36
  Timestamp: '2023-09-05 17:06:24'
- Battery Level (%): 81.6
  Device ID: device-0052
  Device Type: Temperature Sensor
  Reading Value: 46.69
  Timestamp: '2021-01-22 11:17:02'
- Battery Level (%): 77.8
  Device ID: device-0050
  Device Type: Motion Detector
  Reading Value: 54.64
  Timestamp: '2023-11-24 05:20:36'
- Battery Level (%): 37.1
  Device ID: device-0047
  Device Type: Temperature Sensor
  Reading Value: 22.36
  Timestamp: '2022-07-25 14:25:27'
<start>
| Device ID | Device Type | Battery Level (%) | Reading Value | Timestamp |
| --- | --- | --- | --- | --- |
| device-0084 | Pressure Sensor | 29.4 | 74.69 | 2023-06-15 01:42:29 |
| device-0020 | Pressure Sensor | 44.1 | 39.36 | 2023-09-05 17:06:24 |
| device-0052 | Temperature Sensor | 81.6 | 46.69 | 2021-01-22 11:17:02 |
| device-0050 | Motion Detector | 77.8 | 54.64 | 2023-11-24 05:20:36 |
| device-0047 | Temperature Sensor | 37.1 | 22.36 | 2022-07-25 14:25:27 |
<end>Convert this yml to PLAIN TEXT:
- Box Office Earnings (M): 286.99
  Director: Zara Stormrider
  Genre: Horror
  Release Year: 1999
  Title: Mystery of the Depths
- Box Office Earnings (M): 869.67
  Director: Lira Silverleaf
  Genre: Horror
  Release Year: 1998
  Title: Dreamwalker
- Box Office Earnings (M): 643.68
  Director: Orin Shadowalker
  Genre: Thriller
  Release Year: 2017
  Title: Escape from Earth
- Box Office Earnings (M): 563.75
  Director: Drake Nightshade
  Genre: Fantasy
  Release Year: 2018
  Title: Starbound Odyssey
- Box Office Earnings (M): 792.85
  Director: Mara Moonshadow
  Genre: Fantasy
  Release Year: 2012
  Title: The Final Voyage
- Box Office Earnings (M): 855.86
  Director: Rylan Frostblade
  Genre: Comedy
  Release Year: 2015
  Title: The Final Voyage
- Box Office Earnings (M): 503.19
  Director: Zara Stormrider
  Genre: Sci-Fi
  Release Year: 2006
  Title: Edge of Infinity
<start>
Title: Mystery of the Depths | Director: Zara Stormrider | Genre: Horror | Release Year: 1999 | Box Office Earnings (M): 286.99
Title: Dreamwalker | Director: Lira Silverleaf | Genre: Horror | Release Year: 1998 | Box Office Earnings (M): 869.67
Title: Escape from Earth | Director: Orin Shadowalker | Genre: Thriller | Release Year: 2017 | Box Office Earnings (M): 643.68
Title: Starbound Odyssey | Director: Drake Nightshade | Genre: Fantasy | Release Year: 2018 | Box Office Earnings (M): 563.75
Title: The Final Voyage | Director: Mara Moonshadow | Genre: Fantasy | Release Year: 2012 | Box Office Earnings (M): 792.85
Title: The Final Voyage | Director: Rylan Frostblade | Genre: Comedy | Release Year: 2015 | Box Office Earnings (M): 855.86
Title: Edge of Infinity | Director: Zara Stormrider | Genre: Sci-Fi | Release Year: 2006 | Box Office Earnings (M): 503.19
<end>Here's some markdown data, can you convert it to PLAIN TEXT?
| Cuisine | Price Range |
| --- | --- |
| American | $$ |
| American | $$ |
| Chinese | $$$$$ |
| Chinese | $$$$ |
| Japanese | $$$$$ |
| Chinese | $ |
| Indian | $$$$$ |
| American | $$ |
| French | $$$$ |<start>
Cuisine: American | Price Range: $$
Cuisine: American | Price Range: $$
Cuisine: Chinese | Price Range: $$$$$
Cuisine: Chinese | Price Range: $$$$
Cuisine: Japanese | Price Range: $$$$$
Cuisine: Chinese | Price Range: $
Cuisine: Indian | Price Range: $$$$$
Cuisine: American | Price Range: $$
Cuisine: French | Price Range: $$$$
<end>Here's some json data, can you convert it to csv?
[
    {
        "Restaurant Name": "The Steakhouse",
        "Cuisine": "Japanese",
        "Location": "Miami",
        "Price Range": "$$"
    },
    {
        "Restaurant Name": "The Golden Spoon",
        "Cuisine": "American",
        "Location": "Seattle",
        "Price Range": "$$$$"
    },
    {
        "Restaurant Name": "Sushi World",
        "Cuisine": "Indian",
        "Location": "San Francisco",
        "Price Range": "$$$$$"
    },
    {
        "Restaurant Name": "Sushi World",
        "Cuisine": "Italian",
        "Location": "Phoenix",
        "Price Range": "$$$"
    },
    {
        "Restaurant Name": "BBQ Barn",
        "Cuisine": "Mediterranean",
        "Location": "Chicago",
        "Price Range": "$"
    },
    {
        "Restaurant Name": "Curry Corner",
        "Cuisine": "American",
        "Location": "New York",
        "Price Range": "$$$"
    }
]<start>
Restaurant Name,Cuisine,Location,Price Range
The Steakhouse,Japanese,Miami,$$
The Golden Spoon,American,Seattle,$$$$
Sushi World,Indian,San Francisco,$$$$$
Sushi World,Italian,Phoenix,$$$
BBQ Barn,Mediterranean,Chicago,$
Curry Corner,American,New York,$$$
<end>Transform this plain text structure to a json format:
Name: Rose | City: Los Angeles
Name: Isaac | City: Austin
Name: Junior | City: Nashville
<start>
[
    {
        "Name": "Rose",
        "City": "Los Angeles"
    },
    {
        "Name": "Isaac",
        "City": "Austin"
    },
    {
        "Name": "Junior",
        "City": "Nashville"
    }
]
<end>Here's some yaml data, can you convert it to PLAIN TEXT?
- Condition: Snowy
  Day: Saturday
  Humidity (%): 80
  Location: Chicago
  Temperature (C): 6.0
  Wind Speed (km/h): 23.3
- Condition: Cloudy
  Day: Thursday
  Humidity (%): 57
  Location: Phoenix
  Temperature (C): -5.5
  Wind Speed (km/h): 10.4
- Condition: Snowy
  Day: Wednesday
  Humidity (%): 24
  Location: Phoenix
  Temperature (C): 36.5
  Wind Speed (km/h): 21.6
- Condition: Windy
  Day: Wednesday
  Humidity (%): 71
  Location: Miami
  Temperature (C): 15.1
  Wind Speed (km/h): 23.8
- Condition: Cloudy
  Day: Sunday
  Humidity (%): 58
  Location: Houston
  Temperature (C): 36.6
  Wind Speed (km/h): 2.9
- Condition: Sunny
  Day: Saturday
  Humidity (%): 45
  Location: Denver
  Temperature (C): 5.5
  Wind Speed (km/h): 4.1
- Condition: Rainy
  Day: Tuesday
  Humidity (%): 75
  Location: Phoenix
  Temperature (C): -5.3
  Wind Speed (km/h): 26.4
- Condition: Cloudy
  Day: Saturday
  Humidity (%): 75
  Location: Phoenix
  Temperature (C): 9.6
  Wind Speed (km/h): 20.9
<start>
Location: Chicago | Condition: Snowy | Temperature (C): 6.0 | Humidity (%): 80 | Wind Speed (km/h): 23.3 | Day: Saturday
Location: Phoenix | Condition: Cloudy | Temperature (C): -5.5 | Humidity (%): 57 | Wind Speed (km/h): 10.4 | Day: Thursday
Location: Phoenix | Condition: Snowy | Temperature (C): 36.5 | Humidity (%): 24 | Wind Speed (km/h): 21.6 | Day: Wednesday
Location: Miami | Condition: Windy | Temperature (C): 15.1 | Humidity (%): 71 | Wind Speed (km/h): 23.8 | Day: Wednesday
Location: Houston | Condition: Cloudy | Temperature (C): 36.6 | Humidity (%): 58 | Wind Speed (km/h): 2.9 | Day: Sunday
Location: Denver | Condition: Sunny | Temperature (C): 5.5 | Humidity (%): 45 | Wind Speed (km/h): 4.1 | Day: Saturday
Location: Phoenix | Condition: Rainy | Temperature (C): -5.3 | Humidity (%): 75 | Wind Speed (km/h): 26.4 | Day: Tuesday
Location: Phoenix | Condition: Cloudy | Temperature (C): 9.6 | Humidity (%): 75 | Wind Speed (km/h): 20.9 | Day: Saturday
<end>Can you change this PLAIN TEXT into csv?
Condition: Stormy | Temperature (C): -0.7 | Humidity (%): 78 | Wind Speed (km/h): 10.8 | Day: Thursday
Condition: Rainy | Temperature (C): 12.2 | Humidity (%): 60 | Wind Speed (km/h): 0.6 | Day: Tuesday
Condition: Sunny | Temperature (C): -3.5 | Humidity (%): 77 | Wind Speed (km/h): 24.4 | Day: Saturday
Condition: Cloudy | Temperature (C): -1.2 | Humidity (%): 82 | Wind Speed (km/h): 18.6 | Day: Tuesday
Condition: Cloudy | Temperature (C): 23.3 | Humidity (%): 60 | Wind Speed (km/h): 2.7 | Day: Friday
<start>
Condition,Temperature (C),Humidity (%),Wind Speed (km/h),Day
Stormy,-0.7,78,10.8,Thursday
Rainy,12.2,60,0.6,Tuesday
Sunny,-3.5,77,24.4,Saturday
Cloudy,-1.2,82,18.6,Tuesday
Cloudy,23.3,60,2.7,Friday
<end>Convert this yml to plain text:
- Cuisine: American
  Location: Los Angeles
  Price Range: $
  Rating: 1
  Restaurant Name: BBQ Barn
- Cuisine: American
  Location: San Francisco
  Price Range: $
  Rating: 2
  Restaurant Name: Curry Corner
- Cuisine: French
  Location: Seattle
  Price Range: $$$$
  Rating: 4
  Restaurant Name: The Golden Spoon
- Cuisine: Mediterranean
  Location: San Francisco
  Price Range: $$
  Rating: 3
  Restaurant Name: The Steakhouse
- Cuisine: Italian
  Location: Houston
  Price Range: $$$
  Rating: 3
  Restaurant Name: Burger Haven
<start>
Restaurant Name: BBQ Barn | Cuisine: American | Location: Los Angeles | Rating: 1 | Price Range: $
Restaurant Name: Curry Corner | Cuisine: American | Location: San Francisco | Rating: 2 | Price Range: $
Restaurant Name: The Golden Spoon | Cuisine: French | Location: Seattle | Rating: 4 | Price Range: $$$$
Restaurant Name: The Steakhouse | Cuisine: Mediterranean | Location: San Francisco | Rating: 3 | Price Range: $$
Restaurant Name: Burger Haven | Cuisine: Italian | Location: Houston | Rating: 3 | Price Range: $$$
<end>Transform this csv structure to a markdown format:
Database Name,Cache Hit Ratio (%),Connection Count,Average Latency (ms)
ProfilesDB,82.53,132,63.27
SalesDB,84.04,269,98.99
OrdersDB,79.24,162,8.05
InventoryDB,99.03,187,17.11
ProfilesDB,93.02,305,17.11
SalesDB,99.03,445,37.74
InventoryDB,72.21,371,18.14
ProfilesDB,78.45,473,8.05
<start>
| Database Name | Cache Hit Ratio (%) | Connection Count | Average Latency (ms) |
| --- | --- | --- | --- |
| ProfilesDB | 82.53 | 132 | 63.27 |
| SalesDB | 84.04 | 269 | 98.99 |
| OrdersDB | 79.24 | 162 | 8.05 |
| InventoryDB | 99.03 | 187 | 17.11 |
| ProfilesDB | 93.02 | 305 | 17.11 |
| SalesDB | 99.03 | 445 | 37.74 |
| InventoryDB | 72.21 | 371 | 18.14 |
| ProfilesDB | 78.45 | 473 | 8.05 |
<end>Transform this yml structure to a plain text format:
- Box Office Earnings (M): 721.01
  Director: Orin Shadowalker
  Genre: Fantasy
  Release Year: 2018
  Title: The Great Expedition
- Box Office Earnings (M): 37.41
  Director: Drake Nightshade
  Genre: Comedy
  Release Year: 1977
  Title: Escape from Earth
- Box Office Earnings (M): 699.85
  Director: Rylan Frostblade
  Genre: Action
  Release Year: 2003
  Title: The Final Voyage
- Box Office Earnings (M): 46.97
  Director: Talon Blackthorn
  Genre: Fantasy
  Release Year: 1976
  Title: The Final Voyage
- Box Office Earnings (M): 875.23
  Director: Cade Firebrand
  Genre: Sci-Fi
  Release Year: 1970
  Title: The Final Voyage
<start>
Title: The Great Expedition | Director: Orin Shadowalker | Genre: Fantasy | Release Year: 2018 | Box Office Earnings (M): 721.01
Title: Escape from Earth | Director: Drake Nightshade | Genre: Comedy | Release Year: 1977 | Box Office Earnings (M): 37.41
Title: The Final Voyage | Director: Rylan Frostblade | Genre: Action | Release Year: 2003 | Box Office Earnings (M): 699.85
Title: The Final Voyage | Director: Talon Blackthorn | Genre: Fantasy | Release Year: 1976 | Box Office Earnings (M): 46.97
Title: The Final Voyage | Director: Cade Firebrand | Genre: Sci-Fi | Release Year: 1970 | Box Office Earnings (M): 875.23
<end>Can you change this plain text into yml?
Queries per Second: 3688.45 | Average Latency (ms): 28.99 | Timestamp: 2021-11-05 23:48:59
Queries per Second: 1267.64 | Average Latency (ms): 25.55 | Timestamp: 2022-03-03 17:00:41
Queries per Second: 2443.95 | Average Latency (ms): 60.08 | Timestamp: 2023-11-01 11:38:00
Queries per Second: 4885.37 | Average Latency (ms): 52.75 | Timestamp: 2021-08-26 11:04:09
Queries per Second: 3806.08 | Average Latency (ms): 7.23 | Timestamp: 2021-04-21 06:34:09
Queries per Second: 1613.16 | Average Latency (ms): 8.62 | Timestamp: 2023-03-25 17:57:59
<start>
- Average Latency (ms): 28.99
  Queries per Second: 3688.45
  Timestamp: '2021-11-05 23:48:59'
- Average Latency (ms): 25.55
  Queries per Second: 1267.64
  Timestamp: '2022-03-03 17:00:41'
- Average Latency (ms): 60.08
  Queries per Second: 2443.95
  Timestamp: '2023-11-01 11:38:00'
- Average Latency (ms): 52.75
  Queries per Second: 4885.37
  Timestamp: '2021-08-26 11:04:09'
- Average Latency (ms): 7.23
  Queries per Second: 3806.08
  Timestamp: '2021-04-21 06:34:09'
- Average Latency (ms): 8.62
  Queries per Second: 1613.16
  Timestamp: '2023-03-25 17:57:59'
<end>Here's some markdown data, can you convert it to Json?
| Trip Name | Start Location | End Location | Distance (miles) | Duration (hours) | Fuel Used (gallons) |
| --- | --- | --- | --- | --- | --- |
| Lakeside Retreat | San Francisco | Phoenix | 766.3 | 18.0 | 5.2 |
| Canyon Trek | Denver | Miami | 725.6 | 32.9 | 17.8 |
| Coast to Coast | New York | Los Angeles | 1866.7 | 69.8 | 36.4 |
| Historic Route | Miami | San Francisco | 1400.8 | 25.3 | 9.1 |
| Valley Voyage | Los Angeles | Chicago | 2518.2 | 24.4 | 94.4 |
| Mountain Adventure | Los Angeles | Miami | 858.9 | 18.5 | 37.1 |
| Coast to Coast | Los Angeles | New York | 659.2 | 60.4 | 46.0 |
| Forest Journey | Chicago | Houston | 766.3 | 29.4 | 38.2 |
| Valley Voyage | Denver | New York | 58.7 | 45.2 | 79.0 |<start>
[
    {
        "Trip Name": "Lakeside Retreat",
        "Start Location": "San Francisco",
        "End Location": "Phoenix",
        "Distance (miles)": 766.3,
        "Duration (hours)": 18.0,
        "Fuel Used (gallons)": 5.2
    },
    {
        "Trip Name": "Canyon Trek",
        "Start Location": "Denver",
        "End Location": "Miami",
        "Distance (miles)": 725.6,
        "Duration (hours)": 32.9,
        "Fuel Used (gallons)": 17.8
    },
    {
        "Trip Name": "Coast to Coast",
        "Start Location": "New York",
        "End Location": "Los Angeles",
        "Distance (miles)": 1866.7,
        "Duration (hours)": 69.8,
        "Fuel Used (gallons)": 36.4
    },
    {
        "Trip Name": "Historic Route",
        "Start Location": "Miami",
        "End Location": "San Francisco",
        "Distance (miles)": 1400.8,
        "Duration (hours)": 25.3,
        "Fuel Used (gallons)": 9.1
    },
    {
        "Trip Name": "Valley Voyage",
        "Start Location": "Los Angeles",
        "End Location": "Chicago",
        "Distance (miles)": 2518.2,
        "Duration (hours)": 24.4,
        "Fuel Used (gallons)": 94.4
    },
    {
        "Trip Name": "Mountain Adventure",
        "Start Location": "Los Angeles",
        "End Location": "Miami",
        "Distance (miles)": 858.9,
        "Duration (hours)": 18.5,
        "Fuel Used (gallons)": 37.1
    },
    {
        "Trip Name": "Coast to Coast",
        "Start Location": "Los Angeles",
        "End Location": "New York",
        "Distance (miles)": 659.2,
        "Duration (hours)": 60.4,
        "Fuel Used (gallons)": 46.0
    },
    {
        "Trip Name": "Forest Journey",
        "Start Location": "Chicago",
        "End Location": "Houston",
        "Distance (miles)": 766.3,
        "Duration (hours)": 29.4,
        "Fuel Used (gallons)": 38.2
    },
    {
        "Trip Name": "Valley Voyage",
        "Start Location": "Denver",
        "End Location": "New York",
        "Distance (miles)": 58.7,
        "Duration (hours)": 45.2,
        "Fuel Used (gallons)": 79.0
    }
]
<end>Here's some Csv data, can you convert it to plain text?
Company,Annual Revenue (B),Quarter
BioPharm,358.65,Q4
EcoEnergy,439.51,Q3
BioPharm,372.08,Q1
AeroSpace,374.89,Q2
GlobalTrade,175.81,Q2
<start>
Company: BioPharm | Annual Revenue (B): 358.65 | Quarter: Q4
Company: EcoEnergy | Annual Revenue (B): 439.51 | Quarter: Q3
Company: BioPharm | Annual Revenue (B): 372.08 | Quarter: Q1
Company: AeroSpace | Annual Revenue (B): 374.89 | Quarter: Q2
Company: GlobalTrade | Annual Revenue (B): 175.81 | Quarter: Q2
<end>Can you change this csv into markdown?
Queries per Second,Cache Hit Ratio (%),Average Latency (ms)
800.06,72.25,37.54
4900.7,94.71,36.92
989.36,82.08,17.01
1954.1,89.06,35.6
2689.3,80.54,29.59
<start>
| Queries per Second | Cache Hit Ratio (%) | Average Latency (ms) |
| --- | --- | --- |
| 800.06 | 72.25 | 37.54 |
| 4900.7 | 94.71 | 36.92 |
| 989.36 | 82.08 | 17.01 |
| 1954.1 | 89.06 | 35.6 |
| 2689.3 | 80.54 | 29.59 |
<end>Convert this YML to plain text:
- Close Price: 156.67
  Company: AutoMotive
  Date: '2012-06-13'
  High Price: 1250.0
  Volume: 4373013
- Close Price: 829.93
  Company: MediaGroup
  Date: '2013-04-24'
  High Price: 1321.64
  Volume: 8840073
- Close Price: 1455.14
  Company: MediaGroup
  Date: '2011-03-28'
  High Price: 1455.14
  Volume: 8622239
- Close Price: 486.96
  Company: GreenEnergy
  Date: '2013-09-04'
  High Price: 1250.0
  Volume: 5287435
- Close Price: 1446.21
  Company: AutoMotive
  Date: '2018-02-18'
  High Price: 1446.21
  Volume: 9256943
- Close Price: 673.89
  Company: MediaGroup
  Date: '2017-01-20'
  High Price: 1453.89
  Volume: 3136130
- Close Price: 807.77
  Company: MediaGroup
  Date: '2023-09-25'
  High Price: 807.77
  Volume: 8491398
- Close Price: 465.36
  Company: FoodChain
  Date: '2013-11-13'
  High Price: 1250.0
  Volume: 7198856
- Close Price: 102.22
  Company: AutoMotive
  Date: '2010-12-08'
  High Price: 970.69
  Volume: 3209191
- Close Price: 829.93
  Company: TechnoCorp
  Date: '2010-07-25'
  High Price: 862.92
  Volume: 9726756
<start>
Company: AutoMotive | Date: 2012-06-13 | Close Price: 156.67 | High Price: 1250.0 | Volume: 4373013
Company: MediaGroup | Date: 2013-04-24 | Close Price: 829.93 | High Price: 1321.64 | Volume: 8840073
Company: MediaGroup | Date: 2011-03-28 | Close Price: 1455.14 | High Price: 1455.14 | Volume: 8622239
Company: GreenEnergy | Date: 2013-09-04 | Close Price: 486.96 | High Price: 1250.0 | Volume: 5287435
Company: AutoMotive | Date: 2018-02-18 | Close Price: 1446.21 | High Price: 1446.21 | Volume: 9256943
Company: MediaGroup | Date: 2017-01-20 | Close Price: 673.89 | High Price: 1453.89 | Volume: 3136130
Company: MediaGroup | Date: 2023-09-25 | Close Price: 807.77 | High Price: 807.77 | Volume: 8491398
Company: FoodChain | Date: 2013-11-13 | Close Price: 465.36 | High Price: 1250.0 | Volume: 7198856
Company: AutoMotive | Date: 2010-12-08 | Close Price: 102.22 | High Price: 970.69 | Volume: 3209191
Company: TechnoCorp | Date: 2010-07-25 | Close Price: 829.93 | High Price: 862.92 | Volume: 9726756
<end>Here's some YML data, can you convert it to csv?
- Distance (miles): 2939.5
  Duration (hours): 2.8
  End Location: Denver
  Fuel Used (gallons): 65.2
  Start Location: Houston
  Trip Name: Highway Odyssey
- Distance (miles): 2511.7
  Duration (hours): 15.3
  End Location: Miami
  Fuel Used (gallons): 21.2
  Start Location: Phoenix
  Trip Name: Lakeside Retreat
- Distance (miles): 1645.2
  Duration (hours): 41.2
  End Location: New York
  Fuel Used (gallons): 75.8
  Start Location: Miami
  Trip Name: Valley Voyage
<start>
Trip Name,Start Location,End Location,Distance (miles),Duration (hours),Fuel Used (gallons)
Highway Odyssey,Houston,Denver,2939.5,2.8,65.2
Lakeside Retreat,Phoenix,Miami,2511.7,15.3,21.2
Valley Voyage,Miami,New York,1645.2,41.2,75.8
<end>Please transform the following json data into CSV:
[
    {
        "Title": "Shadows of Solitude",
        "Genre": "Romance"
    },
    {
        "Title": "The Last Sky",
        "Genre": "Mystery"
    },
    {
        "Title": "Legends of the Rift",
        "Genre": "Mystery"
    },
    {
        "Title": "Whispers of the Abyss",
        "Genre": "Non-Fiction"
    },
    {
        "Title": "The Crystal Key",
        "Genre": "Romance"
    },
    {
        "Title": "The Forgotten World",
        "Genre": "Science Fiction"
    }
]<start>
Title,Genre
Shadows of Solitude,Romance
The Last Sky,Mystery
Legends of the Rift,Mystery
Whispers of the Abyss,Non-Fiction
The Crystal Key,Romance
The Forgotten World,Science Fiction
<end>Here's some Plain text data, can you convert it to MARKDOWN?
Author: Luna Silverleaf | Genre: Science Fiction | Publication Year: 2000 | Rating: 1.2
Author: Rowan Ashborne | Genre: Non-Fiction | Publication Year: 1957 | Rating: 3.7
Author: Draven Blackthorn | Genre: Non-Fiction | Publication Year: 1971 | Rating: 4.3
Author: Sylvia Nightshade | Genre: Fantasy | Publication Year: 2007 | Rating: 4.7
Author: Thorne Ironwood | Genre: Mystery | Publication Year: 1950 | Rating: 1.9
Author: Rowan Ashborne | Genre: Romance | Publication Year: 1968 | Rating: 1.5
<start>
| Author | Genre | Publication Year | Rating |
| --- | --- | --- | --- |
| Luna Silverleaf | Science Fiction | 2000 | 1.2 |
| Rowan Ashborne | Non-Fiction | 1957 | 3.7 |
| Draven Blackthorn | Non-Fiction | 1971 | 4.3 |
| Sylvia Nightshade | Fantasy | 2007 | 4.7 |
| Thorne Ironwood | Mystery | 1950 | 1.9 |
| Rowan Ashborne | Romance | 1968 | 1.5 |
<end>Here's some yml data, can you convert it to Plain text?
- Average Latency (ms): 50.63
  Cache Hit Ratio (%): 71.92
  Connection Count: 360
- Average Latency (ms): 28.02
  Cache Hit Ratio (%): 70.74
  Connection Count: 338
- Average Latency (ms): 28.94
  Cache Hit Ratio (%): 83.98
  Connection Count: 449
- Average Latency (ms): 65.66
  Cache Hit Ratio (%): 84.38
  Connection Count: 297
- Average Latency (ms): 27.85
  Cache Hit Ratio (%): 98.18
  Connection Count: 382
- Average Latency (ms): 57.78
  Cache Hit Ratio (%): 98.59
  Connection Count: 216
- Average Latency (ms): 98.58
  Cache Hit Ratio (%): 95.01
  Connection Count: 351
- Average Latency (ms): 14.79
  Cache Hit Ratio (%): 90.5
  Connection Count: 116
<start>
Cache Hit Ratio (%): 71.92 | Connection Count: 360 | Average Latency (ms): 50.63
Cache Hit Ratio (%): 70.74 | Connection Count: 338 | Average Latency (ms): 28.02
Cache Hit Ratio (%): 83.98 | Connection Count: 449 | Average Latency (ms): 28.94
Cache Hit Ratio (%): 84.38 | Connection Count: 297 | Average Latency (ms): 65.66
Cache Hit Ratio (%): 98.18 | Connection Count: 382 | Average Latency (ms): 27.85
Cache Hit Ratio (%): 98.59 | Connection Count: 216 | Average Latency (ms): 57.78
Cache Hit Ratio (%): 95.01 | Connection Count: 351 | Average Latency (ms): 98.58
Cache Hit Ratio (%): 90.5 | Connection Count: 116 | Average Latency (ms): 14.79
<end>Can you change this yaml into json?
- Director: Mara Moonshadow
  Genre: Fantasy
  Release Year: 2010
- Director: Mara Moonshadow
  Genre: Thriller
  Release Year: 2001
- Director: Mara Moonshadow
  Genre: Drama
  Release Year: 1976
- Director: Cade Firebrand
  Genre: Action
  Release Year: 2020
- Director: Aria Ravenwood
  Genre: Thriller
  Release Year: 1998
- Director: Rylan Frostblade
  Genre: Fantasy
  Release Year: 1991
- Director: Talon Blackthorn
  Genre: Action
  Release Year: 1992
- Director: Selene Darkwhisper
  Genre: Adventure
  Release Year: 1975
- Director: Aria Ravenwood
  Genre: Horror
  Release Year: 1992
<start>
[
    {
        "Director": "Mara Moonshadow",
        "Genre": "Fantasy",
        "Release Year": 2010
    },
    {
        "Director": "Mara Moonshadow",
        "Genre": "Thriller",
        "Release Year": 2001
    },
    {
        "Director": "Mara Moonshadow",
        "Genre": "Drama",
        "Release Year": 1976
    },
    {
        "Director": "Cade Firebrand",
        "Genre": "Action",
        "Release Year": 2020
    },
    {
        "Director": "Aria Ravenwood",
        "Genre": "Thriller",
        "Release Year": 1998
    },
    {
        "Director": "Rylan Frostblade",
        "Genre": "Fantasy",
        "Release Year": 1991
    },
    {
        "Director": "Talon Blackthorn",
        "Genre": "Action",
        "Release Year": 1992
    },
    {
        "Director": "Selene Darkwhisper",
        "Genre": "Adventure",
        "Release Year": 1975
    },
    {
        "Director": "Aria Ravenwood",
        "Genre": "Horror",
        "Release Year": 1992
    }
]
<end>Can you change this JSON into YAML?
[
    {
        "Restaurant Name": "Burger Haven",
        "Cuisine": "Japanese",
        "Location": "Miami",
        "Rating": 4,
        "Price Range": "$$$$"
    },
    {
        "Restaurant Name": "Burger Haven",
        "Cuisine": "American",
        "Location": "Los Angeles",
        "Rating": 2,
        "Price Range": "$$"
    },
    {
        "Restaurant Name": "Curry Corner",
        "Cuisine": "Chinese",
        "Location": "Los Angeles",
        "Rating": 3,
        "Price Range": "$$$"
    },
    {
        "Restaurant Name": "Vegan Delight",
        "Cuisine": "Chinese",
        "Location": "Seattle",
        "Rating": 4,
        "Price Range": "$$"
    },
    {
        "Restaurant Name": "Sushi World",
        "Cuisine": "Mexican",
        "Location": "New York",
        "Rating": 2,
        "Price Range": "$$$$"
    },
    {
        "Restaurant Name": "BBQ Barn",
        "Cuisine": "French",
        "Location": "Los Angeles",
        "Rating": 5,
        "Price Range": "$$$$$"
    },
    {
        "Restaurant Name": "Sushi World",
        "Cuisine": "Italian",
        "Location": "New York",
        "Rating": 4,
        "Price Range": "$$$"
    }
]<start>
- Cuisine: Japanese
  Location: Miami
  Price Range: $$$$
  Rating: 4
  Restaurant Name: Burger Haven
- Cuisine: American
  Location: Los Angeles
  Price Range: $$
  Rating: 2
  Restaurant Name: Burger Haven
- Cuisine: Chinese
  Location: Los Angeles
  Price Range: $$$
  Rating: 3
  Restaurant Name: Curry Corner
- Cuisine: Chinese
  Location: Seattle
  Price Range: $$
  Rating: 4
  Restaurant Name: Vegan Delight
- Cuisine: Mexican
  Location: New York
  Price Range: $$$$
  Rating: 2
  Restaurant Name: Sushi World
- Cuisine: French
  Location: Los Angeles
  Price Range: $$$$$
  Rating: 5
  Restaurant Name: BBQ Barn
- Cuisine: Italian
  Location: New York
  Price Range: $$$
  Rating: 4
  Restaurant Name: Sushi World
<end>Can you change this YML into MARKDOWN?
- Condition: Cloudy
  Day: Monday
  Humidity (%): 85
  Location: Phoenix
  Temperature (C): -8.3
  Wind Speed (km/h): 25.3
- Condition: Stormy
  Day: Monday
  Humidity (%): 51
  Location: New York
  Temperature (C): 14.1
  Wind Speed (km/h): 12.5
- Condition: Sunny
  Day: Wednesday
  Humidity (%): 42
  Location: Chicago
  Temperature (C): 36.6
  Wind Speed (km/h): 12.5
- Condition: Cloudy
  Day: Tuesday
  Humidity (%): 48
  Location: Chicago
  Temperature (C): 35.5
  Wind Speed (km/h): 1.3
- Condition: Cloudy
  Day: Wednesday
  Humidity (%): 36
  Location: Houston
  Temperature (C): -2.8
  Wind Speed (km/h): 13.6
<start>
| Location | Condition | Temperature (C) | Humidity (%) | Wind Speed (km/h) | Day |
| --- | --- | --- | --- | --- | --- |
| Phoenix | Cloudy | -8.3 | 85 | 25.3 | Monday |
| New York | Stormy | 14.1 | 51 | 12.5 | Monday |
| Chicago | Sunny | 36.6 | 42 | 12.5 | Wednesday |
| Chicago | Cloudy | 35.5 | 48 | 1.3 | Tuesday |
| Houston | Cloudy | -2.8 | 36 | 13.6 | Wednesday |
<end>Can you change this yaml into csv?
- Annual Revenue (B): 379.4
  Company: Foodies
  Sector: Healthcare
  Stock Price: 461.87
- Annual Revenue (B): 133.08
  Company: RetailHub
  Sector: Retail
  Stock Price: 140.82
- Annual Revenue (B): 279.96
  Company: AeroSpace
  Sector: Automotive
  Stock Price: 346.04
- Annual Revenue (B): 281.71
  Company: Foodies
  Sector: Finance
  Stock Price: 331.44
- Annual Revenue (B): 356.61
  Company: FinanceWorks
  Sector: Biotech
  Stock Price: 205.61
- Annual Revenue (B): 145.47
  Company: FinanceWorks
  Sector: Biotech
  Stock Price: 623.13
- Annual Revenue (B): 148.05
  Company: HealthPlus
  Sector: Technology
  Stock Price: 464.91
- Annual Revenue (B): 150.41
  Company: GlobalTrade
  Sector: Biotech
  Stock Price: 637.9
- Annual Revenue (B): 428.96
  Company: HealthPlus
  Sector: Retail
  Stock Price: 726.24
- Annual Revenue (B): 253.73
  Company: Foodies
  Sector: Retail
  Stock Price: 770.37
<start>
Company,Sector,Stock Price,Annual Revenue (B)
Foodies,Healthcare,461.87,379.4
RetailHub,Retail,140.82,133.08
AeroSpace,Automotive,346.04,279.96
Foodies,Finance,331.44,281.71
FinanceWorks,Biotech,205.61,356.61
FinanceWorks,Biotech,623.13,145.47
HealthPlus,Technology,464.91,148.05
GlobalTrade,Biotech,637.9,150.41
HealthPlus,Retail,726.24,428.96
Foodies,Retail,770.37,253.73
<end>Convert this markdown to Yml:
| Director | Genre |
| --- | --- |
| Zara Stormrider | Thriller |
| Talon Blackthorn | Thriller |
| Cade Firebrand | Adventure |<start>
- Director: Zara Stormrider
  Genre: Thriller
- Director: Talon Blackthorn
  Genre: Thriller
- Director: Cade Firebrand
  Genre: Adventure
<end>Here's some csv data, can you convert it to Plain text?
Company,Date,Open Price,Close Price,Low Price,Volume
MediaGroup,2010-05-13,835.31,1361.01,835.31,8554721
AeroSystems,2018-10-01,1264.5,1383.05,1264.5,9237840
TechnoCorp,2015-04-19,1437.88,954.11,497.51,1208921
AutoMotive,2021-12-25,1137.76,1456.06,199.87,7617026
GreenEnergy,2020-10-10,1361.01,829.94,829.94,5841941
TechnoCorp,2017-06-18,1219.84,371.94,371.94,6454079
GreenEnergy,2020-08-22,688.91,227.92,227.92,675494
FoodChain,2022-06-05,263.92,723.85,227.92,3403598
<start>
Company: MediaGroup | Date: 2010-05-13 | Open Price: 835.31 | Close Price: 1361.01 | Low Price: 835.31 | Volume: 8554721
Company: AeroSystems | Date: 2018-10-01 | Open Price: 1264.5 | Close Price: 1383.05 | Low Price: 1264.5 | Volume: 9237840
Company: TechnoCorp | Date: 2015-04-19 | Open Price: 1437.88 | Close Price: 954.11 | Low Price: 497.51 | Volume: 1208921
Company: AutoMotive | Date: 2021-12-25 | Open Price: 1137.76 | Close Price: 1456.06 | Low Price: 199.87 | Volume: 7617026
Company: GreenEnergy | Date: 2020-10-10 | Open Price: 1361.01 | Close Price: 829.94 | Low Price: 829.94 | Volume: 5841941
Company: TechnoCorp | Date: 2017-06-18 | Open Price: 1219.84 | Close Price: 371.94 | Low Price: 371.94 | Volume: 6454079
Company: GreenEnergy | Date: 2020-08-22 | Open Price: 688.91 | Close Price: 227.92 | Low Price: 227.92 | Volume: 675494
Company: FoodChain | Date: 2022-06-05 | Open Price: 263.92 | Close Price: 723.85 | Low Price: 227.92 | Volume: 3403598
<end>Convert this JSON to Csv:
[
    {
        "Age": 39,
        "Birth Month": "July"
    },
    {
        "Age": 46,
        "Birth Month": "December"
    },
    {
        "Age": 21,
        "Birth Month": "November"
    },
    {
        "Age": 19,
        "Birth Month": "May"
    },
    {
        "Age": 56,
        "Birth Month": "February"
    },
    {
        "Age": 27,
        "Birth Month": "December"
    },
    {
        "Age": 33,
        "Birth Month": "August"
    },
    {
        "Age": 56,
        "Birth Month": "July"
    },
    {
        "Age": 47,
        "Birth Month": "November"
    }
]<start>
Age,Birth Month
39,July
46,December
21,November
19,May
56,February
27,December
33,August
56,July
47,November
<end>Here's some Plain text data, can you convert it to csv?
Device ID: device-0068 | Device Type: Light Sensor | Reading Value: -35.76 | Timestamp: 2022-08-23 07:25:58
Device ID: device-0051 | Device Type: Light Sensor | Reading Value: -25.81 | Timestamp: 2022-01-25 03:14:52
Device ID: device-0069 | Device Type: Temperature Sensor | Reading Value: -26.14 | Timestamp: 2021-09-11 17:35:16
Device ID: device-0085 | Device Type: Temperature Sensor | Reading Value: -26.89 | Timestamp: 2023-12-23 05:17:36
<start>
Device ID,Device Type,Reading Value,Timestamp
device-0068,Light Sensor,-35.76,2022-08-23 07:25:58
device-0051,Light Sensor,-25.81,2022-01-25 03:14:52
device-0069,Temperature Sensor,-26.14,2021-09-11 17:35:16
device-0085,Temperature Sensor,-26.89,2023-12-23 05:17:36
<end>Convert this csv to yml:
Company,Close Price,High Price,Low Price,Volume
RetailWorld,567.72,1445.42,215.69,4066145
MediaGroup,712.3,923.96,45.2,6468920
AutoMotive,323.41,999.98,121.1,3076876
AeroSystems,1307.43,1307.43,647.83,8403702
AutoMotive,952.3,952.3,485.97,927171
HealthGen,915.34,1351.02,174.79,4487738
RetailWorld,704.39,712.3,704.39,1414639
AeroSystems,954.33,954.33,420.61,7112466
TechnoCorp,1319.25,1319.25,826.57,1804720
<start>
- Close Price: 567.72
  Company: RetailWorld
  High Price: 1445.42
  Low Price: 215.69
  Volume: 4066145
- Close Price: 712.3
  Company: MediaGroup
  High Price: 923.96
  Low Price: 45.2
  Volume: 6468920
- Close Price: 323.41
  Company: AutoMotive
  High Price: 999.98
  Low Price: 121.1
  Volume: 3076876
- Close Price: 1307.43
  Company: AeroSystems
  High Price: 1307.43
  Low Price: 647.83
  Volume: 8403702
- Close Price: 952.3
  Company: AutoMotive
  High Price: 952.3
  Low Price: 485.97
  Volume: 927171
- Close Price: 915.34
  Company: HealthGen
  High Price: 1351.02
  Low Price: 174.79
  Volume: 4487738
- Close Price: 704.39
  Company: RetailWorld
  High Price: 712.3
  Low Price: 704.39
  Volume: 1414639
- Close Price: 954.33
  Company: AeroSystems
  High Price: 954.33
  Low Price: 420.61
  Volume: 7112466
- Close Price: 1319.25
  Company: TechnoCorp
  High Price: 1319.25
  Low Price: 826.57
  Volume: 1804720
<end>Transform this markdown structure to a csv format:
| Device ID | Location | Battery Level (%) | Reading Value | Timestamp |
| --- | --- | --- | --- | --- |
| device-0032 | Hallway | 58.5 | 53.14 | 2023-06-13 20:22:03 |
| device-0075 | Bathroom | 21.4 | 9.28 | 2023-10-01 19:56:52 |
| device-0059 | Garden | 39.9 | 61.11 | 2023-03-04 21:31:41 |
| device-0054 | Bathroom | 33.6 | 11.45 | 2023-07-10 18:53:14 |
| device-0012 | Hallway | 42.5 | 25.42 | 2021-11-15 00:34:27 |
| device-0010 | Kitchen | 61.7 | 10.71 | 2022-05-24 03:32:49 |<start>
Device ID,Location,Battery Level (%),Reading Value,Timestamp
device-0032,Hallway,58.5,53.14,2023-06-13 20:22:03
device-0075,Bathroom,21.4,9.28,2023-10-01 19:56:52
device-0059,Garden,39.9,61.11,2023-03-04 21:31:41
device-0054,Bathroom,33.6,11.45,2023-07-10 18:53:14
device-0012,Hallway,42.5,25.42,2021-11-15 00:34:27
device-0010,Kitchen,61.7,10.71,2022-05-24 03:32:49
<end>Here's some csv data, can you convert it to JSON?
Name,Age,Birth Month,City,Income
Cole,64,July,San Diego,200000
Greyson,57,January,Oklahoma City,140000
Cornelius,47,July,Denver,245000
Victoria,46,March,Dallas,385000
Harrison,60,October,Boston,50000
Harper,39,May,Boston,110000
Keith,18,July,Houston,445000
<start>
[
    {
        "Name": "Cole",
        "Age": 64,
        "Birth Month": "July",
        "City": "San Diego",
        "Income": 200000
    },
    {
        "Name": "Greyson",
        "Age": 57,
        "Birth Month": "January",
        "City": "Oklahoma City",
        "Income": 140000
    },
    {
        "Name": "Cornelius",
        "Age": 47,
        "Birth Month": "July",
        "City": "Denver",
        "Income": 245000
    },
    {
        "Name": "Victoria",
        "Age": 46,
        "Birth Month": "March",
        "City": "Dallas",
        "Income": 385000
    },
    {
        "Name": "Harrison",
        "Age": 60,
        "Birth Month": "October",
        "City": "Boston",
        "Income": 50000
    },
    {
        "Name": "Harper",
        "Age": 39,
        "Birth Month": "May",
        "City": "Boston",
        "Income": 110000
    },
    {
        "Name": "Keith",
        "Age": 18,
        "Birth Month": "July",
        "City": "Houston",
        "Income": 445000
    }
]
<end>Here's some csv data, can you convert it to markdown?
Title,Author,Genre,Publication Year,Rating
A Journey Through Time,Draven Blackthorn,Science Fiction,1968,2.6
Shadows of Solitude,Orion Frostblade,Historical,1967,4.1
Echoes of Eternity,Luna Silverleaf,Thriller,1967,1.4
Tales of the Brave,Rowan Ashborne,Historical,2008,1.2
The Last Sky,Sylvia Nightshade,Thriller,1958,3.9
Legends of the Rift,Draven Blackthorn,Historical,1955,3.9
The Forgotten World,Isla Windrider,Mystery,2007,3.1
Whispers of the Abyss,Elara Moonshadow,Mystery,1978,4.9
The Forgotten World,Kara Firebrand,Fantasy,1980,3.0
<start>
| Title | Author | Genre | Publication Year | Rating |
| --- | --- | --- | --- | --- |
| A Journey Through Time | Draven Blackthorn | Science Fiction | 1968 | 2.6 |
| Shadows of Solitude | Orion Frostblade | Historical | 1967 | 4.1 |
| Echoes of Eternity | Luna Silverleaf | Thriller | 1967 | 1.4 |
| Tales of the Brave | Rowan Ashborne | Historical | 2008 | 1.2 |
| The Last Sky | Sylvia Nightshade | Thriller | 1958 | 3.9 |
| Legends of the Rift | Draven Blackthorn | Historical | 1955 | 3.9 |
| The Forgotten World | Isla Windrider | Mystery | 2007 | 3.1 |
| Whispers of the Abyss | Elara Moonshadow | Mystery | 1978 | 4.9 |
| The Forgotten World | Kara Firebrand | Fantasy | 1980 | 3.0 |
<end>Can you change this Yaml into json?
- Close Price: 313.02
  Company: FinanceTrust
  Date: '2010-12-18'
  High Price: 803.15
  Low Price: 313.02
  Open Price: 525.01
  Volume: 9530969
- Close Price: 758.58
  Company: RetailWorld
  Date: '2023-07-01'
  High Price: 1457.8
  Low Price: 758.58
  Open Price: 1457.8
  Volume: 4739863
- Close Price: 179.83
  Company: GreenEnergy
  Date: '2022-07-26'
  High Price: 494.54
  Low Price: 179.83
  Open Price: 494.54
  Volume: 3395760
<start>
[
    {
        "Company": "FinanceTrust",
        "Date": "2010-12-18",
        "Open Price": 525.01,
        "Close Price": 313.02,
        "High Price": 803.15,
        "Low Price": 313.02,
        "Volume": 9530969
    },
    {
        "Company": "RetailWorld",
        "Date": "2023-07-01",
        "Open Price": 1457.8,
        "Close Price": 758.58,
        "High Price": 1457.8,
        "Low Price": 758.58,
        "Volume": 4739863
    },
    {
        "Company": "GreenEnergy",
        "Date": "2022-07-26",
        "Open Price": 494.54,
        "Close Price": 179.83,
        "High Price": 494.54,
        "Low Price": 179.83,
        "Volume": 3395760
    }
]
<end>Please transform the following csv data into YAML:
Genre,Publication Year,Rating
Thriller,2019,4.2
Thriller,1995,3.1
Romance,1997,3.8
Historical,1995,1.6
Historical,1987,4.7
Historical,1960,2.1
Fantasy,2019,2.4
<start>
- Genre: Thriller
  Publication Year: 2019
  Rating: 4.2
- Genre: Thriller
  Publication Year: 1995
  Rating: 3.1
- Genre: Romance
  Publication Year: 1997
  Rating: 3.8
- Genre: Historical
  Publication Year: 1995
  Rating: 1.6
- Genre: Historical
  Publication Year: 1987
  Rating: 4.7
- Genre: Historical
  Publication Year: 1960
  Rating: 2.1
- Genre: Fantasy
  Publication Year: 2019
  Rating: 2.4
<end>Please transform the following Markdown data into YAML:
| Product Name | Price | Stock Quantity | Category | Supplier Name |
| --- | --- | --- | --- | --- |
| Gizmo | 287.29 | 312 | Household | Wayne Enterprises |
| Contraption | 45.86 | 205 | Household | Umbrella Corp |
| Device | 378.99 | 410 | Electronics | ACME Corp |
| Instrument | 235.18 | 192 | Electronics | ACME Corp |<start>
- Category: Household
  Price: 287.29
  Product Name: Gizmo
  Stock Quantity: 312
  Supplier Name: Wayne Enterprises
- Category: Household
  Price: 45.86
  Product Name: Contraption
  Stock Quantity: 205
  Supplier Name: Umbrella Corp
- Category: Electronics
  Price: 378.99
  Product Name: Device
  Stock Quantity: 410
  Supplier Name: ACME Corp
- Category: Electronics
  Price: 235.18
  Product Name: Instrument
  Stock Quantity: 192
  Supplier Name: ACME Corp
<end>Can you change this json into YML?
[
    {
        "Location": "New York",
        "Condition": "Foggy",
        "Temperature (C)": 19.4,
        "Humidity (%)": 40,
        "Wind Speed (km/h)": 25.1
    },
    {
        "Location": "New York",
        "Condition": "Snowy",
        "Temperature (C)": 20.4,
        "Humidity (%)": 69,
        "Wind Speed (km/h)": 24.7
    },
    {
        "Location": "Denver",
        "Condition": "Stormy",
        "Temperature (C)": 26.5,
        "Humidity (%)": 41,
        "Wind Speed (km/h)": 7.6
    },
    {
        "Location": "New York",
        "Condition": "Rainy",
        "Temperature (C)": 34.5,
        "Humidity (%)": 97,
        "Wind Speed (km/h)": 19.6
    },
    {
        "Location": "Chicago",
        "Condition": "Cloudy",
        "Temperature (C)": 25.2,
        "Humidity (%)": 23,
        "Wind Speed (km/h)": 15.2
    },
    {
        "Location": "Phoenix",
        "Condition": "Foggy",
        "Temperature (C)": 5.1,
        "Humidity (%)": 25,
        "Wind Speed (km/h)": 28.8
    },
    {
        "Location": "Denver",
        "Condition": "Stormy",
        "Temperature (C)": 20.4,
        "Humidity (%)": 31,
        "Wind Speed (km/h)": 5.3
    },
    {
        "Location": "New York",
        "Condition": "Snowy",
        "Temperature (C)": 11.2,
        "Humidity (%)": 47,
        "Wind Speed (km/h)": 14.6
    },
    {
        "Location": "Denver",
        "Condition": "Cloudy",
        "Temperature (C)": 10.4,
        "Humidity (%)": 51,
        "Wind Speed (km/h)": 23.9
    },
    {
        "Location": "Los Angeles",
        "Condition": "Foggy",
        "Temperature (C)": 34.4,
        "Humidity (%)": 76,
        "Wind Speed (km/h)": 16.0
    }
]<start>
- Condition: Foggy
  Humidity (%): 40
  Location: New York
  Temperature (C): 19.4
  Wind Speed (km/h): 25.1
- Condition: Snowy
  Humidity (%): 69
  Location: New York
  Temperature (C): 20.4
  Wind Speed (km/h): 24.7
- Condition: Stormy
  Humidity (%): 41
  Location: Denver
  Temperature (C): 26.5
  Wind Speed (km/h): 7.6
- Condition: Rainy
  Humidity (%): 97
  Location: New York
  Temperature (C): 34.5
  Wind Speed (km/h): 19.6
- Condition: Cloudy
  Humidity (%): 23
  Location: Chicago
  Temperature (C): 25.2
  Wind Speed (km/h): 15.2
- Condition: Foggy
  Humidity (%): 25
  Location: Phoenix
  Temperature (C): 5.1
  Wind Speed (km/h): 28.8
- Condition: Stormy
  Humidity (%): 31
  Location: Denver
  Temperature (C): 20.4
  Wind Speed (km/h): 5.3
- Condition: Snowy
  Humidity (%): 47
  Location: New York
  Temperature (C): 11.2
  Wind Speed (km/h): 14.6
- Condition: Cloudy
  Humidity (%): 51
  Location: Denver
  Temperature (C): 10.4
  Wind Speed (km/h): 23.9
- Condition: Foggy
  Humidity (%): 76
  Location: Los Angeles
  Temperature (C): 34.4
  Wind Speed (km/h): 16.0
<end>Convert this YAML to CSV:
- Price: 129.06
  Stock Quantity: 377
  Supplier Name: ACME Corp
- Price: 121.39
  Stock Quantity: 96
  Supplier Name: Wayne Enterprises
- Price: 434.12
  Stock Quantity: 172
  Supplier Name: Globex
- Price: 58.5
  Stock Quantity: 23
  Supplier Name: Umbrella Corp
- Price: 414.41
  Stock Quantity: 151
  Supplier Name: Wayne Enterprises
- Price: 301.89
  Stock Quantity: 79
  Supplier Name: ACME Corp
- Price: 276.66
  Stock Quantity: 80
  Supplier Name: Wayne Enterprises
- Price: 328.83
  Stock Quantity: 264
  Supplier Name: ACME Corp
<start>
Price,Stock Quantity,Supplier Name
129.06,377,ACME Corp
121.39,96,Wayne Enterprises
434.12,172,Globex
58.5,23,Umbrella Corp
414.41,151,Wayne Enterprises
301.89,79,ACME Corp
276.66,80,Wayne Enterprises
328.83,264,ACME Corp
<end>Please transform the following MARKDOWN data into csv:
| Location | Condition | Temperature (C) | Humidity (%) | Wind Speed (km/h) | Day |
| --- | --- | --- | --- | --- | --- |
| Denver | Sunny | 33.7 | 80 | 21.4 | Friday |
| New York | Sunny | 13.1 | 52 | 17.4 | Saturday |
| Denver | Windy | 8.1 | 89 | 17.7 | Thursday |
| Los Angeles | Snowy | 6.8 | 44 | 29.1 | Saturday |
| Houston | Foggy | 1.2 | 23 | 10.8 | Monday |
| Seattle | Stormy | 7.6 | 96 | 21.5 | Friday |<start>
Location,Condition,Temperature (C),Humidity (%),Wind Speed (km/h),Day
Denver,Sunny,33.7,80,21.4,Friday
New York,Sunny,13.1,52,17.4,Saturday
Denver,Windy,8.1,89,17.7,Thursday
Los Angeles,Snowy,6.8,44,29.1,Saturday
Houston,Foggy,1.2,23,10.8,Monday
Seattle,Stormy,7.6,96,21.5,Friday
<end>Convert this markdown to json:
| Title | Author | Genre | Publication Year | Rating |
| --- | --- | --- | --- | --- |
| Echoes of Eternity | Rowan Ashborne | Romance | 2005 | 3.8 |
| Shadows of Solitude | Rowan Ashborne | Historical | 1950 | 4.5 |
| The Silent Grove | Sylvia Nightshade | Non-Fiction | 1964 | 4.3 |
| Shadows of Solitude | Isla Windrider | Fantasy | 2015 | 2.9 |
| The Silent Grove | Luna Silverleaf | Historical | 2002 | 1.6 |
| A Journey Through Time | Orion Frostblade | Science Fiction | 2003 | 1.8 |
| Legends of the Rift | Orion Frostblade | Romance | 2023 | 2.6 |
| A Journey Through Time | Thorne Ironwood | Historical | 1966 | 3.6 |<start>
[
    {
        "Title": "Echoes of Eternity",
        "Author": "Rowan Ashborne",
        "Genre": "Romance",
        "Publication Year": 2005,
        "Rating": 3.8
    },
    {
        "Title": "Shadows of Solitude",
        "Author": "Rowan Ashborne",
        "Genre": "Historical",
        "Publication Year": 1950,
        "Rating": 4.5
    },
    {
        "Title": "The Silent Grove",
        "Author": "Sylvia Nightshade",
        "Genre": "Non-Fiction",
        "Publication Year": 1964,
        "Rating": 4.3
    },
    {
        "Title": "Shadows of Solitude",
        "Author": "Isla Windrider",
        "Genre": "Fantasy",
        "Publication Year": 2015,
        "Rating": 2.9
    },
    {
        "Title": "The Silent Grove",
        "Author": "Luna Silverleaf",
        "Genre": "Historical",
        "Publication Year": 2002,
        "Rating": 1.6
    },
    {
        "Title": "A Journey Through Time",
        "Author": "Orion Frostblade",
        "Genre": "Science Fiction",
        "Publication Year": 2003,
        "Rating": 1.8
    },
    {
        "Title": "Legends of the Rift",
        "Author": "Orion Frostblade",
        "Genre": "Romance",
        "Publication Year": 2023,
        "Rating": 2.6
    },
    {
        "Title": "A Journey Through Time",
        "Author": "Thorne Ironwood",
        "Genre": "Historical",
        "Publication Year": 1966,
        "Rating": 3.6
    }
]
<end>Here's some yaml data, can you convert it to csv?
- Cuisine: French
  Price Range: $$$
  Restaurant Name: The Golden Spoon
- Cuisine: Japanese
  Price Range: $$$$
  Restaurant Name: The Golden Spoon
- Cuisine: Italian
  Price Range: $$$
  Restaurant Name: The Steakhouse
- Cuisine: Indian
  Price Range: $$$$$
  Restaurant Name: Taco Town
- Cuisine: Indian
  Price Range: $$$$$
  Restaurant Name: The Golden Spoon
- Cuisine: Chinese
  Price Range: $$$$
  Restaurant Name: Burger Haven
- Cuisine: Mediterranean
  Price Range: $
  Restaurant Name: Burger Haven
- Cuisine: Mexican
  Price Range: $$$$
  Restaurant Name: The Steakhouse
- Cuisine: Japanese
  Price Range: $$$
  Restaurant Name: Sushi World
- Cuisine: French
  Price Range: $$$$$
  Restaurant Name: The Steakhouse
<start>
Restaurant Name,Cuisine,Price Range
The Golden Spoon,French,$$$
The Golden Spoon,Japanese,$$$$
The Steakhouse,Italian,$$$
Taco Town,Indian,$$$$$
The Golden Spoon,Indian,$$$$$
Burger Haven,Chinese,$$$$
Burger Haven,Mediterranean,$
The Steakhouse,Mexican,$$$$
Sushi World,Japanese,$$$
The Steakhouse,French,$$$$$
<end>Can you change this json into markdown?
[
    {
        "Title": "Edge of Infinity",
        "Director": "Talon Blackthorn",
        "Genre": "Comedy",
        "Release Year": 2006
    },
    {
        "Title": "The Great Expedition",
        "Director": "Drake Nightshade",
        "Genre": "Sci-Fi",
        "Release Year": 2009
    },
    {
        "Title": "Escape from Earth",
        "Director": "Cade Firebrand",
        "Genre": "Adventure",
        "Release Year": 1992
    },
    {
        "Title": "The Endless Horizon",
        "Director": "Orin Shadowalker",
        "Genre": "Sci-Fi",
        "Release Year": 2021
    },
    {
        "Title": "Starbound Odyssey",
        "Director": "Drake Nightshade",
        "Genre": "Action",
        "Release Year": 1992
    },
    {
        "Title": "Edge of Infinity",
        "Director": "Talon Blackthorn",
        "Genre": "Thriller",
        "Release Year": 1991
    },
    {
        "Title": "Edge of Infinity",
        "Director": "Aria Ravenwood",
        "Genre": "Thriller",
        "Release Year": 2004
    },
    {
        "Title": "Rise of the Titans",
        "Director": "Talon Blackthorn",
        "Genre": "Fantasy",
        "Release Year": 1994
    },
    {
        "Title": "Dreamwalker",
        "Director": "Selene Darkwhisper",
        "Genre": "Adventure",
        "Release Year": 2001
    },
    {
        "Title": "Edge of Infinity",
        "Director": "Orin Shadowalker",
        "Genre": "Action",
        "Release Year": 2021
    }
]<start>
| Title | Director | Genre | Release Year |
| --- | --- | --- | --- |
| Edge of Infinity | Talon Blackthorn | Comedy | 2006 |
| The Great Expedition | Drake Nightshade | Sci-Fi | 2009 |
| Escape from Earth | Cade Firebrand | Adventure | 1992 |
| The Endless Horizon | Orin Shadowalker | Sci-Fi | 2021 |
| Starbound Odyssey | Drake Nightshade | Action | 1992 |
| Edge of Infinity | Talon Blackthorn | Thriller | 1991 |
| Edge of Infinity | Aria Ravenwood | Thriller | 2004 |
| Rise of the Titans | Talon Blackthorn | Fantasy | 1994 |
| Dreamwalker | Selene Darkwhisper | Adventure | 2001 |
| Edge of Infinity | Orin Shadowalker | Action | 2021 |
<end>Can you change this JSON into Plain text?
[
    {
        "Location": "Miami",
        "Condition": "Snowy",
        "Humidity (%)": 81,
        "Wind Speed (km/h)": 24.7,
        "Day": "Thursday"
    },
    {
        "Location": "Phoenix",
        "Condition": "Snowy",
        "Humidity (%)": 50,
        "Wind Speed (km/h)": 26.0,
        "Day": "Tuesday"
    },
    {
        "Location": "Seattle",
        "Condition": "Sunny",
        "Humidity (%)": 50,
        "Wind Speed (km/h)": 26.4,
        "Day": "Friday"
    },
    {
        "Location": "Miami",
        "Condition": "Cloudy",
        "Humidity (%)": 47,
        "Wind Speed (km/h)": 26.2,
        "Day": "Tuesday"
    }
]<start>
Location: Miami | Condition: Snowy | Humidity (%): 81 | Wind Speed (km/h): 24.7 | Day: Thursday
Location: Phoenix | Condition: Snowy | Humidity (%): 50 | Wind Speed (km/h): 26.0 | Day: Tuesday
Location: Seattle | Condition: Sunny | Humidity (%): 50 | Wind Speed (km/h): 26.4 | Day: Friday
Location: Miami | Condition: Cloudy | Humidity (%): 47 | Wind Speed (km/h): 26.2 | Day: Tuesday
<end>Please transform the following JSON data into yaml:
[
    {
        "Cache Hit Ratio (%)": 72.32,
        "Connection Count": 43,
        "Timestamp": "2022-12-13 22:39:05"
    },
    {
        "Cache Hit Ratio (%)": 83.03,
        "Connection Count": 249,
        "Timestamp": "2022-04-05 12:52:30"
    },
    {
        "Cache Hit Ratio (%)": 86.16,
        "Connection Count": 357,
        "Timestamp": "2022-10-13 00:18:53"
    },
    {
        "Cache Hit Ratio (%)": 89.51,
        "Connection Count": 10,
        "Timestamp": "2022-12-03 01:10:52"
    },
    {
        "Cache Hit Ratio (%)": 77.09,
        "Connection Count": 312,
        "Timestamp": "2021-05-23 09:01:42"
    }
]<start>
- Cache Hit Ratio (%): 72.32
  Connection Count: 43
  Timestamp: '2022-12-13 22:39:05'
- Cache Hit Ratio (%): 83.03
  Connection Count: 249
  Timestamp: '2022-04-05 12:52:30'
- Cache Hit Ratio (%): 86.16
  Connection Count: 357
  Timestamp: '2022-10-13 00:18:53'
- Cache Hit Ratio (%): 89.51
  Connection Count: 10
  Timestamp: '2022-12-03 01:10:52'
- Cache Hit Ratio (%): 77.09
  Connection Count: 312
  Timestamp: '2021-05-23 09:01:42'
<end>Can you change this MARKDOWN into plain text?
| Title | Author |
| --- | --- |
| A Journey Through Time | Thorne Ironwood |
| The Crystal Key | Kara Firebrand |
| Legends of the Rift | Orion Frostblade |
| The Crystal Key | Rowan Ashborne |
| The Forgotten World | Kara Firebrand |
| The Silent Grove | Elara Moonshadow |<start>
Title: A Journey Through Time | Author: Thorne Ironwood
Title: The Crystal Key | Author: Kara Firebrand
Title: Legends of the Rift | Author: Orion Frostblade
Title: The Crystal Key | Author: Rowan Ashborne
Title: The Forgotten World | Author: Kara Firebrand
Title: The Silent Grove | Author: Elara Moonshadow
<end>Transform this Json structure to a MARKDOWN format:
[
    {
        "Company": "BioPharm",
        "Market Cap": "Small Cap",
        "Annual Revenue (B)": 297.27,
        "Quarter": "Q2"
    },
    {
        "Company": "Foodies",
        "Market Cap": "Small Cap",
        "Annual Revenue (B)": 247.35,
        "Quarter": "Q2"
    },
    {
        "Company": "TechCorp",
        "Market Cap": "Large Cap",
        "Annual Revenue (B)": 95.39,
        "Quarter": "Q1"
    },
    {
        "Company": "GlobalTrade",
        "Market Cap": "Large Cap",
        "Annual Revenue (B)": 275.52,
        "Quarter": "Q3"
    },
    {
        "Company": "AutoDrive",
        "Market Cap": "Mega Cap",
        "Annual Revenue (B)": 95.39,
        "Quarter": "Q2"
    },
    {
        "Company": "AutoDrive",
        "Market Cap": "Small Cap",
        "Annual Revenue (B)": 330.38,
        "Quarter": "Q3"
    },
    {
        "Company": "BioPharm",
        "Market Cap": "Large Cap",
        "Annual Revenue (B)": 181.69,
        "Quarter": "Q1"
    }
]<start>
| Company | Market Cap | Annual Revenue (B) | Quarter |
| --- | --- | --- | --- |
| BioPharm | Small Cap | 297.27 | Q2 |
| Foodies | Small Cap | 247.35 | Q2 |
| TechCorp | Large Cap | 95.39 | Q1 |
| GlobalTrade | Large Cap | 275.52 | Q3 |
| AutoDrive | Mega Cap | 95.39 | Q2 |
| AutoDrive | Small Cap | 330.38 | Q3 |
| BioPharm | Large Cap | 181.69 | Q1 |
<end>Convert this Plain text to Csv:
Company: GreenEnergy | Date: 2013-03-26 | Open Price: 1316.28 | Close Price: 1406.31 | High Price: 1406.31 | Low Price: 683.26 | Volume: 6840544
Company: FinanceTrust | Date: 2014-04-01 | Open Price: 495.17 | Close Price: 1032.67 | High Price: 1032.67 | Low Price: 495.17 | Volume: 8261424
Company: FoodChain | Date: 2022-10-20 | Open Price: 196.87 | Close Price: 1148.24 | High Price: 1148.24 | Low Price: 196.87 | Volume: 6295203
Company: FinanceTrust | Date: 2020-10-22 | Open Price: 1240.18 | Close Price: 877.34 | High Price: 1240.18 | Low Price: 833.02 | Volume: 6028757
Company: FinanceTrust | Date: 2017-03-27 | Open Price: 1248.84 | Close Price: 1094.93 | High Price: 1248.84 | Low Price: 613.85 | Volume: 3356881
Company: BioLife | Date: 2016-12-27 | Open Price: 957.81 | Close Price: 742.13 | High Price: 1145.65 | Low Price: 464.55 | Volume: 6370946
Company: MediaGroup | Date: 2014-04-21 | Open Price: 85.52 | Close Price: 347.9 | High Price: 936.54 | Low Price: 85.52 | Volume: 6351162
Company: TechnoCorp | Date: 2023-11-03 | Open Price: 234.93 | Close Price: 696.77 | High Price: 1240.18 | Low Price: 234.93 | Volume: 2769128
<start>
Company,Date,Open Price,Close Price,High Price,Low Price,Volume
GreenEnergy,2013-03-26,1316.28,1406.31,1406.31,683.26,6840544
FinanceTrust,2014-04-01,495.17,1032.67,1032.67,495.17,8261424
FoodChain,2022-10-20,196.87,1148.24,1148.24,196.87,6295203
FinanceTrust,2020-10-22,1240.18,877.34,1240.18,833.02,6028757
FinanceTrust,2017-03-27,1248.84,1094.93,1248.84,613.85,3356881
BioLife,2016-12-27,957.81,742.13,1145.65,464.55,6370946
MediaGroup,2014-04-21,85.52,347.9,936.54,85.52,6351162
TechnoCorp,2023-11-03,234.93,696.77,1240.18,234.93,2769128
<end>Here's some PLAIN TEXT data, can you convert it to Markdown?
Restaurant Name: Vegan Delight | Cuisine: American | Location: New York | Price Range: $$$
Restaurant Name: Pasta Palace | Cuisine: Mediterranean | Location: Chicago | Price Range: $$$$$
Restaurant Name: Burger Haven | Cuisine: Japanese | Location: New York | Price Range: $$
Restaurant Name: Vegan Delight | Cuisine: Indian | Location: Seattle | Price Range: $$$$$
Restaurant Name: Pizza Planet | Cuisine: Indian | Location: Los Angeles | Price Range: $$$
Restaurant Name: Vegan Delight | Cuisine: French | Location: Miami | Price Range: $$$$
Restaurant Name: Pasta Palace | Cuisine: Chinese | Location: Chicago | Price Range: $$$$
Restaurant Name: Vegan Delight | Cuisine: Chinese | Location: San Francisco | Price Range: $
Restaurant Name: Curry Corner | Cuisine: Indian | Location: Miami | Price Range: $
Restaurant Name: The Golden Spoon | Cuisine: French | Location: San Francisco | Price Range: $$$$
<start>
| Restaurant Name | Cuisine | Location | Price Range |
| --- | --- | --- | --- |
| Vegan Delight | American | New York | $$$ |
| Pasta Palace | Mediterranean | Chicago | $$$$$ |
| Burger Haven | Japanese | New York | $$ |
| Vegan Delight | Indian | Seattle | $$$$$ |
| Pizza Planet | Indian | Los Angeles | $$$ |
| Vegan Delight | French | Miami | $$$$ |
| Pasta Palace | Chinese | Chicago | $$$$ |
| Vegan Delight | Chinese | San Francisco | $ |
| Curry Corner | Indian | Miami | $ |
| The Golden Spoon | French | San Francisco | $$$$ |
<end>Transform this YAML structure to a PLAIN TEXT format:
- Director: Aria Ravenwood
  Genre: Action
  Release Year: 1987
  Title: Rise of the Titans
- Director: Lira Silverleaf
  Genre: Fantasy
  Release Year: 1986
  Title: Escape from Earth
- Director: Selene Darkwhisper
  Genre: Comedy
  Release Year: 2013
  Title: Rise of the Titans
- Director: Zara Stormrider
  Genre: Horror
  Release Year: 2001
  Title: Starbound Odyssey
- Director: Zara Stormrider
  Genre: Adventure
  Release Year: 2002
  Title: Escape from Earth
- Director: Rylan Frostblade
  Genre: Sci-Fi
  Release Year: 2014
  Title: Rise of the Titans
- Director: Cade Firebrand
  Genre: Drama
  Release Year: 2013
  Title: Beyond the Veil
- Director: Cade Firebrand
  Genre: Adventure
  Release Year: 2016
  Title: The Great Expedition
<start>
Title: Rise of the Titans | Director: Aria Ravenwood | Genre: Action | Release Year: 1987
Title: Escape from Earth | Director: Lira Silverleaf | Genre: Fantasy | Release Year: 1986
Title: Rise of the Titans | Director: Selene Darkwhisper | Genre: Comedy | Release Year: 2013
Title: Starbound Odyssey | Director: Zara Stormrider | Genre: Horror | Release Year: 2001
Title: Escape from Earth | Director: Zara Stormrider | Genre: Adventure | Release Year: 2002
Title: Rise of the Titans | Director: Rylan Frostblade | Genre: Sci-Fi | Release Year: 2014
Title: Beyond the Veil | Director: Cade Firebrand | Genre: Drama | Release Year: 2013
Title: The Great Expedition | Director: Cade Firebrand | Genre: Adventure | Release Year: 2016
<end>Convert this plain text to json:
Database Name: LogsDB | Queries per Second: 3051.55 | Cache Hit Ratio (%): 77.25 | Connection Count: 81 | Average Latency (ms): 96.77
Database Name: AnalyticsDB | Queries per Second: 3406.95 | Cache Hit Ratio (%): 70.14 | Connection Count: 294 | Average Latency (ms): 4.46
Database Name: MetricsDB | Queries per Second: 4035.28 | Cache Hit Ratio (%): 89.17 | Connection Count: 270 | Average Latency (ms): 29.05
Database Name: ProfilesDB | Queries per Second: 4546.0 | Cache Hit Ratio (%): 72.23 | Connection Count: 196 | Average Latency (ms): 75.8
Database Name: SalesDB | Queries per Second: 1208.86 | Cache Hit Ratio (%): 90.7 | Connection Count: 119 | Average Latency (ms): 14.58
Database Name: LogsDB | Queries per Second: 2021.75 | Cache Hit Ratio (%): 93.05 | Connection Count: 397 | Average Latency (ms): 16.96
Database Name: ProductsDB | Queries per Second: 555.75 | Cache Hit Ratio (%): 91.43 | Connection Count: 325 | Average Latency (ms): 7.17
Database Name: OrdersDB | Queries per Second: 879.78 | Cache Hit Ratio (%): 98.25 | Connection Count: 181 | Average Latency (ms): 59.92
Database Name: LogsDB | Queries per Second: 2107.84 | Cache Hit Ratio (%): 87.83 | Connection Count: 135 | Average Latency (ms): 6.38
<start>
[
    {
        "Database Name": "LogsDB",
        "Queries per Second": 3051.55,
        "Cache Hit Ratio (%)": 77.25,
        "Connection Count": 81,
        "Average Latency (ms)": 96.77
    },
    {
        "Database Name": "AnalyticsDB",
        "Queries per Second": 3406.95,
        "Cache Hit Ratio (%)": 70.14,
        "Connection Count": 294,
        "Average Latency (ms)": 4.46
    },
    {
        "Database Name": "MetricsDB",
        "Queries per Second": 4035.28,
        "Cache Hit Ratio (%)": 89.17,
        "Connection Count": 270,
        "Average Latency (ms)": 29.05
    },
    {
        "Database Name": "ProfilesDB",
        "Queries per Second": 4546.0,
        "Cache Hit Ratio (%)": 72.23,
        "Connection Count": 196,
        "Average Latency (ms)": 75.8
    },
    {
        "Database Name": "SalesDB",
        "Queries per Second": 1208.86,
        "Cache Hit Ratio (%)": 90.7,
        "Connection Count": 119,
        "Average Latency (ms)": 14.58
    },
    {
        "Database Name": "LogsDB",
        "Queries per Second": 2021.75,
        "Cache Hit Ratio (%)": 93.05,
        "Connection Count": 397,
        "Average Latency (ms)": 16.96
    },
    {
        "Database Name": "ProductsDB",
        "Queries per Second": 555.75,
        "Cache Hit Ratio (%)": 91.43,
        "Connection Count": 325,
        "Average Latency (ms)": 7.17
    },
    {
        "Database Name": "OrdersDB",
        "Queries per Second": 879.78,
        "Cache Hit Ratio (%)": 98.25,
        "Connection Count": 181,
        "Average Latency (ms)": 59.92
    },
    {
        "Database Name": "LogsDB",
        "Queries per Second": 2107.84,
        "Cache Hit Ratio (%)": 87.83,
        "Connection Count": 135,
        "Average Latency (ms)": 6.38
    }
]
<end>Here's some markdown data, can you convert it to csv?
| Name | Age | Birth Month | City | Income |
| --- | --- | --- | --- | --- |
| Ted | 28 | March | Milwaukee | 375000 |
| Penny | 55 | June | Columbus | 245000 |
| Abbie | 49 | September | New York | 225000 |<start>
Name,Age,Birth Month,City,Income
Ted,28,March,Milwaukee,375000
Penny,55,June,Columbus,245000
Abbie,49,September,New York,225000
<end>Can you change this PLAIN TEXT into yaml?
Company: BioLife | Date: 2019-06-17 | Open Price: 249.52 | Close Price: 1279.96 | High Price: 1279.96 | Low Price: 249.52 | Volume: 9303938
Company: BioLife | Date: 2017-12-27 | Open Price: 814.2 | Close Price: 1498.45 | High Price: 1498.45 | Low Price: 128.1 | Volume: 6694528
Company: HealthGen | Date: 2010-03-06 | Open Price: 1023.89 | Close Price: 369.76 | High Price: 1397.42 | Low Price: 369.76 | Volume: 2225690
Company: TechnoCorp | Date: 2017-02-16 | Open Price: 1174.25 | Close Price: 1200.31 | High Price: 1200.31 | Low Price: 233.82 | Volume: 5742650
Company: AutoMotive | Date: 2013-11-09 | Open Price: 563.94 | Close Price: 239.42 | High Price: 563.94 | Low Price: 239.42 | Volume: 2152467
Company: FinanceTrust | Date: 2010-05-01 | Open Price: 114.26 | Close Price: 1409.73 | High Price: 1409.73 | Low Price: 114.26 | Volume: 1178204
Company: TechnoCorp | Date: 2017-09-18 | Open Price: 450.04 | Close Price: 1409.73 | High Price: 1409.73 | Low Price: 450.04 | Volume: 5005319
<start>
- Close Price: 1279.96
  Company: BioLife
  Date: '2019-06-17'
  High Price: 1279.96
  Low Price: 249.52
  Open Price: 249.52
  Volume: 9303938
- Close Price: 1498.45
  Company: BioLife
  Date: '2017-12-27'
  High Price: 1498.45
  Low Price: 128.1
  Open Price: 814.2
  Volume: 6694528
- Close Price: 369.76
  Company: HealthGen
  Date: '2010-03-06'
  High Price: 1397.42
  Low Price: 369.76
  Open Price: 1023.89
  Volume: 2225690
- Close Price: 1200.31
  Company: TechnoCorp
  Date: '2017-02-16'
  High Price: 1200.31
  Low Price: 233.82
  Open Price: 1174.25
  Volume: 5742650
- Close Price: 239.42
  Company: AutoMotive
  Date: '2013-11-09'
  High Price: 563.94
  Low Price: 239.42
  Open Price: 563.94
  Volume: 2152467
- Close Price: 1409.73
  Company: FinanceTrust
  Date: '2010-05-01'
  High Price: 1409.73
  Low Price: 114.26
  Open Price: 114.26
  Volume: 1178204
- Close Price: 1409.73
  Company: TechnoCorp
  Date: '2017-09-18'
  High Price: 1409.73
  Low Price: 450.04
  Open Price: 450.04
  Volume: 5005319
<end>Convert this yaml to csv:
- Author: Rowan Ashborne
  Rating: 2.2
- Author: Elara Moonshadow
  Rating: 1.0
- Author: Luna Silverleaf
  Rating: 3.0
<start>
Author,Rating
Rowan Ashborne,2.2
Elara Moonshadow,1.0
Luna Silverleaf,3.0
<end>Can you change this yaml into json?
- Age: 69
  Birth Month: July
  City: Dallas
- Age: 69
  Birth Month: July
  City: Indianapolis
- Age: 64
  Birth Month: April
  City: Las Vegas
- Age: 46
  Birth Month: June
  City: Jacksonville
<start>
[
    {
        "Age": 69,
        "Birth Month": "July",
        "City": "Dallas"
    },
    {
        "Age": 69,
        "Birth Month": "July",
        "City": "Indianapolis"
    },
    {
        "Age": 64,
        "Birth Month": "April",
        "City": "Las Vegas"
    },
    {
        "Age": 46,
        "Birth Month": "June",
        "City": "Jacksonville"
    }
]
<end>Transform this csv structure to a Yaml format:
Device ID,Device Type,Battery Level (%),Reading Value,Timestamp
device-0026,Light Sensor,37.3,83.85,2022-07-04 18:06:54
device-0020,Light Sensor,45.0,48.58,2023-07-20 13:56:48
device-0048,Temperature Sensor,80.1,-17.01,2021-09-03 04:22:31
device-0089,Humidity Sensor,53.8,12.32,2022-04-28 01:31:50
device-0096,Temperature Sensor,22.2,79.91,2022-07-27 09:19:23
device-0027,Motion Detector,45.0,-38.82,2022-06-04 16:38:58
device-0055,Temperature Sensor,46.1,26.63,2021-09-11 18:51:10
device-0046,Humidity Sensor,31.1,-6.35,2022-06-14 08:24:43
device-0099,Light Sensor,60.4,-35.12,2022-09-23 10:23:58
device-0037,Light Sensor,17.9,-31.65,2021-11-21 19:53:32
<start>
- Battery Level (%): 37.3
  Device ID: device-0026
  Device Type: Light Sensor
  Reading Value: 83.85
  Timestamp: '2022-07-04 18:06:54'
- Battery Level (%): 45.0
  Device ID: device-0020
  Device Type: Light Sensor
  Reading Value: 48.58
  Timestamp: '2023-07-20 13:56:48'
- Battery Level (%): 80.1
  Device ID: device-0048
  Device Type: Temperature Sensor
  Reading Value: -17.01
  Timestamp: '2021-09-03 04:22:31'
- Battery Level (%): 53.8
  Device ID: device-0089
  Device Type: Humidity Sensor
  Reading Value: 12.32
  Timestamp: '2022-04-28 01:31:50'
- Battery Level (%): 22.2
  Device ID: device-0096
  Device Type: Temperature Sensor
  Reading Value: 79.91
  Timestamp: '2022-07-27 09:19:23'
- Battery Level (%): 45.0
  Device ID: device-0027
  Device Type: Motion Detector
  Reading Value: -38.82
  Timestamp: '2022-06-04 16:38:58'
- Battery Level (%): 46.1
  Device ID: device-0055
  Device Type: Temperature Sensor
  Reading Value: 26.63
  Timestamp: '2021-09-11 18:51:10'
- Battery Level (%): 31.1
  Device ID: device-0046
  Device Type: Humidity Sensor
  Reading Value: -6.35
  Timestamp: '2022-06-14 08:24:43'
- Battery Level (%): 60.4
  Device ID: device-0099
  Device Type: Light Sensor
  Reading Value: -35.12
  Timestamp: '2022-09-23 10:23:58'
- Battery Level (%): 17.9
  Device ID: device-0037
  Device Type: Light Sensor
  Reading Value: -31.65
  Timestamp: '2021-11-21 19:53:32'
<end>Please transform the following markdown data into plain text:
| Cuisine | Rating | Price Range |
| --- | --- | --- |
| French | 2 | $$$$$ |
| Mexican | 2 | $ |
| French | 1 | $$ |
| Mexican | 1 | $$ |
| French | 2 | $ |<start>
Cuisine: French | Rating: 2 | Price Range: $$$$$
Cuisine: Mexican | Rating: 2 | Price Range: $
Cuisine: French | Rating: 1 | Price Range: $$
Cuisine: Mexican | Rating: 1 | Price Range: $$
Cuisine: French | Rating: 2 | Price Range: $
<end>Here's some Plain text data, can you convert it to yml?
SKU: SKU-1022 | Price: 103.89 | Stock Quantity: 260 | Category: Household | Supplier Name: Wayne Enterprises
SKU: SKU-1070 | Price: 55.47 | Stock Quantity: 189 | Category: Household | Supplier Name: Globex
SKU: SKU-1060 | Price: 334.34 | Stock Quantity: 12 | Category: Sports | Supplier Name: Wayne Enterprises
<start>
- Category: Household
  Price: 103.89
  SKU: SKU-1022
  Stock Quantity: 260
  Supplier Name: Wayne Enterprises
- Category: Household
  Price: 55.47
  SKU: SKU-1070
  Stock Quantity: 189
  Supplier Name: Globex
- Category: Sports
  Price: 334.34
  SKU: SKU-1060
  Stock Quantity: 12
  Supplier Name: Wayne Enterprises
<end>Here's some plain text data, can you convert it to MARKDOWN?
Database Name: OrdersDB | Queries per Second: 3794.96 | Cache Hit Ratio (%): 95.92 | Connection Count: 29 | Average Latency (ms): 21.51 | Timestamp: 2023-07-17 13:39:16
Database Name: UserDB | Queries per Second: 3128.89 | Cache Hit Ratio (%): 89.96 | Connection Count: 298 | Average Latency (ms): 81.1 | Timestamp: 2023-01-02 17:09:34
Database Name: OrdersDB | Queries per Second: 4175.38 | Cache Hit Ratio (%): 80.19 | Connection Count: 257 | Average Latency (ms): 37.21 | Timestamp: 2021-03-16 05:21:49
Database Name: AnalyticsDB | Queries per Second: 2992.71 | Cache Hit Ratio (%): 72.06 | Connection Count: 392 | Average Latency (ms): 75.29 | Timestamp: 2021-06-01 12:28:10
Database Name: LogsDB | Queries per Second: 154.35 | Cache Hit Ratio (%): 91.62 | Connection Count: 136 | Average Latency (ms): 97.06 | Timestamp: 2021-11-20 13:02:47
Database Name: AnalyticsDB | Queries per Second: 3842.85 | Cache Hit Ratio (%): 85.15 | Connection Count: 269 | Average Latency (ms): 37.21 | Timestamp: 2023-04-22 21:07:19
<start>
| Database Name | Queries per Second | Cache Hit Ratio (%) | Connection Count | Average Latency (ms) | Timestamp |
| --- | --- | --- | --- | --- | --- |
| OrdersDB | 3794.96 | 95.92 | 29 | 21.51 | 2023-07-17 13:39:16 |
| UserDB | 3128.89 | 89.96 | 298 | 81.1 | 2023-01-02 17:09:34 |
| OrdersDB | 4175.38 | 80.19 | 257 | 37.21 | 2021-03-16 05:21:49 |
| AnalyticsDB | 2992.71 | 72.06 | 392 | 75.29 | 2021-06-01 12:28:10 |
| LogsDB | 154.35 | 91.62 | 136 | 97.06 | 2021-11-20 13:02:47 |
| AnalyticsDB | 3842.85 | 85.15 | 269 | 37.21 | 2023-04-22 21:07:19 |
<end>Please transform the following markdown data into CSV:
| Company | Market Cap | Stock Price | Annual Revenue (B) | Quarter |
| --- | --- | --- | --- | --- |
| Foodies | Small Cap | 650.98 | 220.31 | Q3 |
| HealthPlus | Large Cap | 314.49 | 68.28 | Q2 |
| AeroSpace | Mega Cap | 288.67 | 167.43 | Q3 |
| AutoDrive | Mega Cap | 51.28 | 269.47 | Q3 |
| Foodies | Large Cap | 998.1 | 492.69 | Q2 |
| BioPharm | Small Cap | 76.39 | 372.72 | Q2 |
| AutoDrive | Small Cap | 911.2 | 197.82 | Q2 |
| GlobalTrade | Mega Cap | 639.42 | 59.53 | Q3 |
| AeroSpace | Mid Cap | 317.04 | 220.31 | Q1 |
| FinanceWorks | Mega Cap | 670.06 | 90.54 | Q4 |<start>
Company,Market Cap,Stock Price,Annual Revenue (B),Quarter
Foodies,Small Cap,650.98,220.31,Q3
HealthPlus,Large Cap,314.49,68.28,Q2
AeroSpace,Mega Cap,288.67,167.43,Q3
AutoDrive,Mega Cap,51.28,269.47,Q3
Foodies,Large Cap,998.1,492.69,Q2
BioPharm,Small Cap,76.39,372.72,Q2
AutoDrive,Small Cap,911.2,197.82,Q2
GlobalTrade,Mega Cap,639.42,59.53,Q3
AeroSpace,Mid Cap,317.04,220.31,Q1
FinanceWorks,Mega Cap,670.06,90.54,Q4
<end>Please transform the following Json data into csv:
[
    {
        "Database Name": "ProfilesDB",
        "Queries per Second": 4639.88,
        "Cache Hit Ratio (%)": 70.39,
        "Connection Count": 490,
        "Average Latency (ms)": 73.28,
        "Timestamp": "2023-10-21 14:47:32"
    },
    {
        "Database Name": "SalesDB",
        "Queries per Second": 531.23,
        "Cache Hit Ratio (%)": 97.95,
        "Connection Count": 455,
        "Average Latency (ms)": 3.86,
        "Timestamp": "2022-06-05 09:12:14"
    },
    {
        "Database Name": "SessionsDB",
        "Queries per Second": 2694.81,
        "Cache Hit Ratio (%)": 75.53,
        "Connection Count": 249,
        "Average Latency (ms)": 42.86,
        "Timestamp": "2023-05-07 01:49:58"
    },
    {
        "Database Name": "UserDB",
        "Queries per Second": 1635.93,
        "Cache Hit Ratio (%)": 74.48,
        "Connection Count": 497,
        "Average Latency (ms)": 79.51,
        "Timestamp": "2023-12-15 05:54:29"
    },
    {
        "Database Name": "ProductsDB",
        "Queries per Second": 2518.37,
        "Cache Hit Ratio (%)": 93.27,
        "Connection Count": 455,
        "Average Latency (ms)": 36.1,
        "Timestamp": "2023-09-09 05:40:28"
    },
    {
        "Database Name": "AnalyticsDB",
        "Queries per Second": 2579.84,
        "Cache Hit Ratio (%)": 95.05,
        "Connection Count": 328,
        "Average Latency (ms)": 56.03,
        "Timestamp": "2023-05-14 00:38:14"
    },
    {
        "Database Name": "AnalyticsDB",
        "Queries per Second": 2447.21,
        "Cache Hit Ratio (%)": 96.03,
        "Connection Count": 273,
        "Average Latency (ms)": 81.87,
        "Timestamp": "2021-06-12 21:57:25"
    }
]<start>
Database Name,Queries per Second,Cache Hit Ratio (%),Connection Count,Average Latency (ms),Timestamp
ProfilesDB,4639.88,70.39,490,73.28,2023-10-21 14:47:32
SalesDB,531.23,97.95,455,3.86,2022-06-05 09:12:14
SessionsDB,2694.81,75.53,249,42.86,2023-05-07 01:49:58
UserDB,1635.93,74.48,497,79.51,2023-12-15 05:54:29
ProductsDB,2518.37,93.27,455,36.1,2023-09-09 05:40:28
AnalyticsDB,2579.84,95.05,328,56.03,2023-05-14 00:38:14
AnalyticsDB,2447.21,96.03,273,81.87,2021-06-12 21:57:25
<end>Here's some yml data, can you convert it to MARKDOWN?
- Age: 28
  Name: Sharon
- Age: 47
  Name: Francisco
- Age: 21
  Name: Elena
- Age: 36
  Name: Vivian
- Age: 21
  Name: Valentina
- Age: 64
  Name: Isabelle
<start>
| Name | Age |
| --- | --- |
| Sharon | 28 |
| Francisco | 47 |
| Elena | 21 |
| Vivian | 36 |
| Valentina | 21 |
| Isabelle | 64 |
<end>Convert this markdown to plain text:
| Company | Market Cap | Stock Price | Annual Revenue (B) |
| --- | --- | --- | --- |
| HealthPlus | Large Cap | 651.62 | 483.17 |
| HealthPlus | Mega Cap | 199.08 | 372.52 |
| AeroSpace | Mega Cap | 441.52 | 470.43 |
| GlobalTrade | Mid Cap | 444.61 | 189.44 |
| EcoEnergy | Mid Cap | 647.99 | 189.44 |
| HealthPlus | Mega Cap | 647.99 | 51.87 |
| FinanceWorks | Mega Cap | 716.57 | 479.67 |
| FinanceWorks | Small Cap | 575.61 | 443.49 |<start>
Company: HealthPlus | Market Cap: Large Cap | Stock Price: 651.62 | Annual Revenue (B): 483.17
Company: HealthPlus | Market Cap: Mega Cap | Stock Price: 199.08 | Annual Revenue (B): 372.52
Company: AeroSpace | Market Cap: Mega Cap | Stock Price: 441.52 | Annual Revenue (B): 470.43
Company: GlobalTrade | Market Cap: Mid Cap | Stock Price: 444.61 | Annual Revenue (B): 189.44
Company: EcoEnergy | Market Cap: Mid Cap | Stock Price: 647.99 | Annual Revenue (B): 189.44
Company: HealthPlus | Market Cap: Mega Cap | Stock Price: 647.99 | Annual Revenue (B): 51.87
Company: FinanceWorks | Market Cap: Mega Cap | Stock Price: 716.57 | Annual Revenue (B): 479.67
Company: FinanceWorks | Market Cap: Small Cap | Stock Price: 575.61 | Annual Revenue (B): 443.49
<end>Here's some yml data, can you convert it to Csv?
- Condition: Sunny
  Day: Saturday
  Wind Speed (km/h): 2.9
- Condition: Snowy
  Day: Thursday
  Wind Speed (km/h): 6.4
- Condition: Foggy
  Day: Thursday
  Wind Speed (km/h): 21.6
- Condition: Snowy
  Day: Monday
  Wind Speed (km/h): 21.6
- Condition: Foggy
  Day: Wednesday
  Wind Speed (km/h): 2.8
- Condition: Snowy
  Day: Sunday
  Wind Speed (km/h): 28.4
- Condition: Windy
  Day: Monday
  Wind Speed (km/h): 0.6
- Condition: Windy
  Day: Monday
  Wind Speed (km/h): 18.8
- Condition: Rainy
  Day: Wednesday
  Wind Speed (km/h): 23.5
<start>
Condition,Wind Speed (km/h),Day
Sunny,2.9,Saturday
Snowy,6.4,Thursday
Foggy,21.6,Thursday
Snowy,21.6,Monday
Foggy,2.8,Wednesday
Snowy,28.4,Sunday
Windy,0.6,Monday
Windy,18.8,Monday
Rainy,23.5,Wednesday
<end>Convert this Plain text to markdown:
Director: Zara Stormrider | Box Office Earnings (M): 838.75
Director: Orin Shadowalker | Box Office Earnings (M): 589.12
Director: Mara Moonshadow | Box Office Earnings (M): 91.79
Director: Cade Firebrand | Box Office Earnings (M): 719.65
Director: Cade Firebrand | Box Office Earnings (M): 213.6
Director: Lira Silverleaf | Box Office Earnings (M): 970.64
<start>
| Director | Box Office Earnings (M) |
| --- | --- |
| Zara Stormrider | 838.75 |
| Orin Shadowalker | 589.12 |
| Mara Moonshadow | 91.79 |
| Cade Firebrand | 719.65 |
| Cade Firebrand | 213.6 |
| Lira Silverleaf | 970.64 |
<end>Please transform the following PLAIN TEXT data into csv:
Company: BioPharm | Sector: Automotive | Market Cap: Small Cap | Stock Price: 382.53 | Annual Revenue (B): 245.65 | Quarter: Q1
Company: TechCorp | Sector: Automotive | Market Cap: Small Cap | Stock Price: 122.98 | Annual Revenue (B): 375.74 | Quarter: Q1
Company: RetailHub | Sector: Healthcare | Market Cap: Mega Cap | Stock Price: 274.47 | Annual Revenue (B): 167.67 | Quarter: Q3
Company: BioPharm | Sector: Energy | Market Cap: Large Cap | Stock Price: 263.79 | Annual Revenue (B): 335.37 | Quarter: Q2
Company: Foodies | Sector: Healthcare | Market Cap: Small Cap | Stock Price: 599.5 | Annual Revenue (B): 364.56 | Quarter: Q2
Company: BioPharm | Sector: Retail | Market Cap: Large Cap | Stock Price: 869.24 | Annual Revenue (B): 230.52 | Quarter: Q3
Company: AutoDrive | Sector: Finance | Market Cap: Large Cap | Stock Price: 51.44 | Annual Revenue (B): 450.3 | Quarter: Q4
Company: RetailHub | Sector: Automotive | Market Cap: Small Cap | Stock Price: 962.95 | Annual Revenue (B): 271.18 | Quarter: Q3
Company: EcoEnergy | Sector: Retail | Market Cap: Large Cap | Stock Price: 145.48 | Annual Revenue (B): 274.03 | Quarter: Q2
<start>
Company,Sector,Market Cap,Stock Price,Annual Revenue (B),Quarter
BioPharm,Automotive,Small Cap,382.53,245.65,Q1
TechCorp,Automotive,Small Cap,122.98,375.74,Q1
RetailHub,Healthcare,Mega Cap,274.47,167.67,Q3
BioPharm,Energy,Large Cap,263.79,335.37,Q2
Foodies,Healthcare,Small Cap,599.5,364.56,Q2
BioPharm,Retail,Large Cap,869.24,230.52,Q3
AutoDrive,Finance,Large Cap,51.44,450.3,Q4
RetailHub,Automotive,Small Cap,962.95,271.18,Q3
EcoEnergy,Retail,Large Cap,145.48,274.03,Q2
<end>Here's some json data, can you convert it to YML?
[
    {
        "Condition": "Snowy",
        "Humidity (%)": 50,
        "Day": "Sunday"
    },
    {
        "Condition": "Snowy",
        "Humidity (%)": 46,
        "Day": "Thursday"
    },
    {
        "Condition": "Rainy",
        "Humidity (%)": 25,
        "Day": "Sunday"
    },
    {
        "Condition": "Rainy",
        "Humidity (%)": 35,
        "Day": "Saturday"
    }
]<start>
- Condition: Snowy
  Day: Sunday
  Humidity (%): 50
- Condition: Snowy
  Day: Thursday
  Humidity (%): 46
- Condition: Rainy
  Day: Sunday
  Humidity (%): 25
- Condition: Rainy
  Day: Saturday
  Humidity (%): 35
<end>Please transform the following PLAIN TEXT data into markdown:
Queries per Second: 1597.86 | Connection Count: 289 | Average Latency (ms): 15.96 | Timestamp: 2021-04-07 04:08:53
Queries per Second: 2537.61 | Connection Count: 54 | Average Latency (ms): 40.16 | Timestamp: 2022-11-24 16:15:06
Queries per Second: 1226.2 | Connection Count: 416 | Average Latency (ms): 6.73 | Timestamp: 2023-01-07 09:37:49
Queries per Second: 4542.07 | Connection Count: 198 | Average Latency (ms): 48.87 | Timestamp: 2021-02-09 20:34:57
Queries per Second: 1823.87 | Connection Count: 188 | Average Latency (ms): 9.53 | Timestamp: 2022-12-22 03:02:49
Queries per Second: 4542.07 | Connection Count: 179 | Average Latency (ms): 69.15 | Timestamp: 2023-08-10 21:16:20
Queries per Second: 2537.61 | Connection Count: 54 | Average Latency (ms): 80.74 | Timestamp: 2021-07-16 16:02:54
<start>
| Queries per Second | Connection Count | Average Latency (ms) | Timestamp |
| --- | --- | --- | --- |
| 1597.86 | 289 | 15.96 | 2021-04-07 04:08:53 |
| 2537.61 | 54 | 40.16 | 2022-11-24 16:15:06 |
| 1226.2 | 416 | 6.73 | 2023-01-07 09:37:49 |
| 4542.07 | 198 | 48.87 | 2021-02-09 20:34:57 |
| 1823.87 | 188 | 9.53 | 2022-12-22 03:02:49 |
| 4542.07 | 179 | 69.15 | 2023-08-10 21:16:20 |
| 2537.61 | 54 | 80.74 | 2021-07-16 16:02:54 |
<end>Here's some PLAIN TEXT data, can you convert it to csv?
Name: Summer | Age: 26 | City: Portland | Income: 225000
Name: Elmer | Age: 45 | City: Portland | Income: 110000
Name: Alta | Age: 37 | City: Chicago | Income: 205000
Name: Paisley | Age: 34 | City: Las Vegas | Income: 40000
Name: Yvette | Age: 31 | City: El Paso | Income: 185000
Name: George | Age: 51 | City: Washington | Income: 385000
Name: Tanner | Age: 39 | City: Las Vegas | Income: 190000
Name: Claire | Age: 52 | City: San Diego | Income: 25000
Name: Ariana | Age: 61 | City: Milwaukee | Income: 105000
Name: Jade | Age: 18 | City: Columbus | Income: 325000
<start>
Name,Age,City,Income
Summer,26,Portland,225000
Elmer,45,Portland,110000
Alta,37,Chicago,205000
Paisley,34,Las Vegas,40000
Yvette,31,El Paso,185000
George,51,Washington,385000
Tanner,39,Las Vegas,190000
Claire,52,San Diego,25000
Ariana,61,Milwaukee,105000
Jade,18,Columbus,325000
<end>Here's some MARKDOWN data, can you convert it to yml?
| Device ID | Location | Battery Level (%) |
| --- | --- | --- |
| device-0043 | Office | 86.3 |
| device-0031 | Bedroom | 39.0 |
| device-0085 | Kitchen | 86.6 |
| device-0018 | Living Room | 71.9 |
| device-0043 | Bedroom | 17.7 |
| device-0046 | Kitchen | 22.8 |
| device-0012 | Garage | 58.2 |
| device-0035 | Bedroom | 48.9 |<start>
- Battery Level (%): 86.3
  Device ID: device-0043
  Location: Office
- Battery Level (%): 39.0
  Device ID: device-0031
  Location: Bedroom
- Battery Level (%): 86.6
  Device ID: device-0085
  Location: Kitchen
- Battery Level (%): 71.9
  Device ID: device-0018
  Location: Living Room
- Battery Level (%): 17.7
  Device ID: device-0043
  Location: Bedroom
- Battery Level (%): 22.8
  Device ID: device-0046
  Location: Kitchen
- Battery Level (%): 58.2
  Device ID: device-0012
  Location: Garage
- Battery Level (%): 48.9
  Device ID: device-0035
  Location: Bedroom
<end>Can you change this markdown into CSV?
| Location | Condition | Humidity (%) | Wind Speed (km/h) | Day |
| --- | --- | --- | --- | --- |
| Seattle | Windy | 80 | 21.1 | Tuesday |
| Chicago | Snowy | 83 | 13.5 | Saturday |
| Phoenix | Windy | 89 | 17.9 | Tuesday |
| Denver | Rainy | 82 | 11.9 | Monday |
| Phoenix | Foggy | 29 | 19.7 | Thursday |
| Houston | Sunny | 100 | 21.1 | Monday |
| Chicago | Rainy | 49 | 22.8 | Monday |<start>
Location,Condition,Humidity (%),Wind Speed (km/h),Day
Seattle,Windy,80,21.1,Tuesday
Chicago,Snowy,83,13.5,Saturday
Phoenix,Windy,89,17.9,Tuesday
Denver,Rainy,82,11.9,Monday
Phoenix,Foggy,29,19.7,Thursday
Houston,Sunny,100,21.1,Monday
Chicago,Rainy,49,22.8,Monday
<end>Convert this PLAIN TEXT to Json:
Cuisine: Japanese | Rating: 2 | Price Range: $
Cuisine: American | Rating: 5 | Price Range: $$
Cuisine: American | Rating: 5 | Price Range: $$$$$
Cuisine: Italian | Rating: 1 | Price Range: $$$$
Cuisine: Mediterranean | Rating: 1 | Price Range: $$$$$
Cuisine: Japanese | Rating: 4 | Price Range: $$$$$
Cuisine: Mediterranean | Rating: 4 | Price Range: $
Cuisine: Mexican | Rating: 2 | Price Range: $
<start>
[
    {
        "Cuisine": "Japanese",
        "Rating": 2,
        "Price Range": "$"
    },
    {
        "Cuisine": "American",
        "Rating": 5,
        "Price Range": "$$"
    },
    {
        "Cuisine": "American",
        "Rating": 5,
        "Price Range": "$$$$$"
    },
    {
        "Cuisine": "Italian",
        "Rating": 1,
        "Price Range": "$$$$"
    },
    {
        "Cuisine": "Mediterranean",
        "Rating": 1,
        "Price Range": "$$$$$"
    },
    {
        "Cuisine": "Japanese",
        "Rating": 4,
        "Price Range": "$$$$$"
    },
    {
        "Cuisine": "Mediterranean",
        "Rating": 4,
        "Price Range": "$"
    },
    {
        "Cuisine": "Mexican",
        "Rating": 2,
        "Price Range": "$"
    }
]
<end>Convert this PLAIN TEXT to json:
Genre: Drama | Release Year: 2019 | Box Office Earnings (M): 11.02
Genre: Fantasy | Release Year: 2005 | Box Office Earnings (M): 602.38
Genre: Adventure | Release Year: 1975 | Box Office Earnings (M): 853.07
Genre: Horror | Release Year: 2008 | Box Office Earnings (M): 306.64
Genre: Horror | Release Year: 2017 | Box Office Earnings (M): 425.79
Genre: Horror | Release Year: 1977 | Box Office Earnings (M): 18.91
<start>
[
    {
        "Genre": "Drama",
        "Release Year": 2019,
        "Box Office Earnings (M)": 11.02
    },
    {
        "Genre": "Fantasy",
        "Release Year": 2005,
        "Box Office Earnings (M)": 602.38
    },
    {
        "Genre": "Adventure",
        "Release Year": 1975,
        "Box Office Earnings (M)": 853.07
    },
    {
        "Genre": "Horror",
        "Release Year": 2008,
        "Box Office Earnings (M)": 306.64
    },
    {
        "Genre": "Horror",
        "Release Year": 2017,
        "Box Office Earnings (M)": 425.79
    },
    {
        "Genre": "Horror",
        "Release Year": 1977,
        "Box Office Earnings (M)": 18.91
    }
]
<end>Transform this markdown structure to a YAML format:
| Genre | Release Year |
| --- | --- |
| Drama | 2018 |
| Drama | 2003 |
| Comedy | 1990 |
| Drama | 1997 |
| Thriller | 1978 |
| Fantasy | 1978 |<start>
- Genre: Drama
  Release Year: 2018
- Genre: Drama
  Release Year: 2003
- Genre: Comedy
  Release Year: 1990
- Genre: Drama
  Release Year: 1997
- Genre: Thriller
  Release Year: 1978
- Genre: Fantasy
  Release Year: 1978
<end>Here's some Csv data, can you convert it to plain text?
Condition,Temperature (C),Humidity (%),Wind Speed (km/h)
Windy,1.2,48,28.5
Stormy,-8.5,31,25.2
Rainy,-9.9,66,5.0
Rainy,-2.6,23,0.7
Stormy,27.3,23,16.5
Stormy,6.1,44,8.2
Stormy,12.8,48,29.2
Snowy,-7.9,97,5.7
Rainy,27.1,94,29.1
<start>
Condition: Windy | Temperature (C): 1.2 | Humidity (%): 48 | Wind Speed (km/h): 28.5
Condition: Stormy | Temperature (C): -8.5 | Humidity (%): 31 | Wind Speed (km/h): 25.2
Condition: Rainy | Temperature (C): -9.9 | Humidity (%): 66 | Wind Speed (km/h): 5.0
Condition: Rainy | Temperature (C): -2.6 | Humidity (%): 23 | Wind Speed (km/h): 0.7
Condition: Stormy | Temperature (C): 27.3 | Humidity (%): 23 | Wind Speed (km/h): 16.5
Condition: Stormy | Temperature (C): 6.1 | Humidity (%): 44 | Wind Speed (km/h): 8.2
Condition: Stormy | Temperature (C): 12.8 | Humidity (%): 48 | Wind Speed (km/h): 29.2
Condition: Snowy | Temperature (C): -7.9 | Humidity (%): 97 | Wind Speed (km/h): 5.7
Condition: Rainy | Temperature (C): 27.1 | Humidity (%): 94 | Wind Speed (km/h): 29.1
<end>Transform this markdown structure to a Csv format:
| Title | Genre | Release Year | Box Office Earnings (M) |
| --- | --- | --- | --- |
| The Endless Horizon | Fantasy | 1991 | 624.62 |
| Rise of the Titans | Adventure | 1995 | 975.01 |
| The Great Expedition | Sci-Fi | 1996 | 925.93 |
| Dreamwalker | Sci-Fi | 1999 | 810.63 |
| Starbound Odyssey | Thriller | 2023 | 76.43 |
| Dreamwalker | Thriller | 1995 | 663.27 |<start>
Title,Genre,Release Year,Box Office Earnings (M)
The Endless Horizon,Fantasy,1991,624.62
Rise of the Titans,Adventure,1995,975.01
The Great Expedition,Sci-Fi,1996,925.93
Dreamwalker,Sci-Fi,1999,810.63
Starbound Odyssey,Thriller,2023,76.43
Dreamwalker,Thriller,1995,663.27
<end>Please transform the following Csv data into plain text:
Company,Open Price,High Price,Low Price
FoodChain,48.49,1300.36,48.49
AeroSystems,502.85,918.49,502.85
RetailWorld,236.51,664.41,236.51
RetailWorld,181.15,1452.93,181.15
AeroSystems,560.77,1347.39,294.41
<start>
Company: FoodChain | Open Price: 48.49 | High Price: 1300.36 | Low Price: 48.49
Company: AeroSystems | Open Price: 502.85 | High Price: 918.49 | Low Price: 502.85
Company: RetailWorld | Open Price: 236.51 | High Price: 664.41 | Low Price: 236.51
Company: RetailWorld | Open Price: 181.15 | High Price: 1452.93 | Low Price: 181.15
Company: AeroSystems | Open Price: 560.77 | High Price: 1347.39 | Low Price: 294.41
<end>Please transform the following MARKDOWN data into Csv:
| Database Name | Queries per Second | Cache Hit Ratio (%) | Timestamp |
| --- | --- | --- | --- |
| InventoryDB | 1929.27 | 75.54 | 2023-11-03 16:28:28 |
| OrdersDB | 4141.26 | 93.45 | 2023-06-19 13:42:21 |
| OrdersDB | 4730.84 | 95.75 | 2021-08-28 02:08:23 |<start>
Database Name,Queries per Second,Cache Hit Ratio (%),Timestamp
InventoryDB,1929.27,75.54,2023-11-03 16:28:28
OrdersDB,4141.26,93.45,2023-06-19 13:42:21
OrdersDB,4730.84,95.75,2021-08-28 02:08:23
<end>Convert this markdown to YAML:
| Product Name | SKU | Stock Quantity |
| --- | --- | --- |
| Apparatus | SKU-1060 | 298 |
| Device | SKU-1059 | 371 |
| Instrument | SKU-1084 | 471 |
| Contraption | SKU-1009 | 92 |
| Apparatus | SKU-1070 | 179 |
| Whatchamacallit | SKU-1056 | 440 |
| Widget | SKU-1049 | 85 |<start>
- Product Name: Apparatus
  SKU: SKU-1060
  Stock Quantity: 298
- Product Name: Device
  SKU: SKU-1059
  Stock Quantity: 371
- Product Name: Instrument
  SKU: SKU-1084
  Stock Quantity: 471
- Product Name: Contraption
  SKU: SKU-1009
  Stock Quantity: 92
- Product Name: Apparatus
  SKU: SKU-1070
  Stock Quantity: 179
- Product Name: Whatchamacallit
  SKU: SKU-1056
  Stock Quantity: 440
- Product Name: Widget
  SKU: SKU-1049
  Stock Quantity: 85
<end>Transform this JSON structure to a csv format:
[
    {
        "Cache Hit Ratio (%)": 84.35,
        "Connection Count": 183,
        "Average Latency (ms)": 82.98
    },
    {
        "Cache Hit Ratio (%)": 74.08,
        "Connection Count": 263,
        "Average Latency (ms)": 18.53
    },
    {
        "Cache Hit Ratio (%)": 90.48,
        "Connection Count": 337,
        "Average Latency (ms)": 79.73
    },
    {
        "Cache Hit Ratio (%)": 96.24,
        "Connection Count": 222,
        "Average Latency (ms)": 68.05
    },
    {
        "Cache Hit Ratio (%)": 99.77,
        "Connection Count": 446,
        "Average Latency (ms)": 25.29
    },
    {
        "Cache Hit Ratio (%)": 71.9,
        "Connection Count": 160,
        "Average Latency (ms)": 20.38
    },
    {
        "Cache Hit Ratio (%)": 77.22,
        "Connection Count": 284,
        "Average Latency (ms)": 33.4
    },
    {
        "Cache Hit Ratio (%)": 71.43,
        "Connection Count": 314,
        "Average Latency (ms)": 32.88
    },
    {
        "Cache Hit Ratio (%)": 92.64,
        "Connection Count": 164,
        "Average Latency (ms)": 89.44
    }
]<start>
Cache Hit Ratio (%),Connection Count,Average Latency (ms)
84.35,183,82.98
74.08,263,18.53
90.48,337,79.73
96.24,222,68.05
99.77,446,25.29
71.9,160,20.38
77.22,284,33.4
71.43,314,32.88
92.64,164,89.44
<end>Please transform the following Csv data into JSON:
Location,Condition,Temperature (C),Humidity (%),Wind Speed (km/h)
Miami,Snowy,-8.5,45,6.9
Miami,Snowy,7.3,35,6.9
Denver,Foggy,33.2,56,4.3
Miami,Cloudy,30.7,78,23.2
<start>
[
    {
        "Location": "Miami",
        "Condition": "Snowy",
        "Temperature (C)": -8.5,
        "Humidity (%)": 45,
        "Wind Speed (km/h)": 6.9
    },
    {
        "Location": "Miami",
        "Condition": "Snowy",
        "Temperature (C)": 7.3,
        "Humidity (%)": 35,
        "Wind Speed (km/h)": 6.9
    },
    {
        "Location": "Denver",
        "Condition": "Foggy",
        "Temperature (C)": 33.2,
        "Humidity (%)": 56,
        "Wind Speed (km/h)": 4.3
    },
    {
        "Location": "Miami",
        "Condition": "Cloudy",
        "Temperature (C)": 30.7,
        "Humidity (%)": 78,
        "Wind Speed (km/h)": 23.2
    }
]
<end>Can you change this Csv into markdown?
Restaurant Name,Cuisine,Location,Rating,Price Range
Pasta Palace,Japanese,Chicago,5,$$
Curry Corner,French,Seattle,5,$$$$$
Burger Haven,French,Chicago,5,$$
Taco Town,French,Houston,3,$$$$$
BBQ Barn,Mediterranean,Houston,4,$
<start>
| Restaurant Name | Cuisine | Location | Rating | Price Range |
| --- | --- | --- | --- | --- |
| Pasta Palace | Japanese | Chicago | 5 | $$ |
| Curry Corner | French | Seattle | 5 | $$$$$ |
| Burger Haven | French | Chicago | 5 | $$ |
| Taco Town | French | Houston | 3 | $$$$$ |
| BBQ Barn | Mediterranean | Houston | 4 | $ |
<end>Here's some Json data, can you convert it to Plain text?
[
    {
        "Location": "Seattle",
        "Condition": "Sunny",
        "Temperature (C)": 10.1,
        "Humidity (%)": 20,
        "Wind Speed (km/h)": 13.8,
        "Day": "Tuesday"
    },
    {
        "Location": "Denver",
        "Condition": "Windy",
        "Temperature (C)": 15.8,
        "Humidity (%)": 52,
        "Wind Speed (km/h)": 17.1,
        "Day": "Monday"
    },
    {
        "Location": "Phoenix",
        "Condition": "Sunny",
        "Temperature (C)": -5.0,
        "Humidity (%)": 42,
        "Wind Speed (km/h)": 13.8,
        "Day": "Saturday"
    },
    {
        "Location": "Los Angeles",
        "Condition": "Rainy",
        "Temperature (C)": 15.4,
        "Humidity (%)": 95,
        "Wind Speed (km/h)": 19.4,
        "Day": "Wednesday"
    },
    {
        "Location": "Los Angeles",
        "Condition": "Windy",
        "Temperature (C)": -5.0,
        "Humidity (%)": 75,
        "Wind Speed (km/h)": 13.7,
        "Day": "Friday"
    },
    {
        "Location": "Denver",
        "Condition": "Snowy",
        "Temperature (C)": 32.4,
        "Humidity (%)": 39,
        "Wind Speed (km/h)": 28.7,
        "Day": "Friday"
    },
    {
        "Location": "Denver",
        "Condition": "Cloudy",
        "Temperature (C)": 24.5,
        "Humidity (%)": 44,
        "Wind Speed (km/h)": 24.5,
        "Day": "Thursday"
    },
    {
        "Location": "Houston",
        "Condition": "Windy",
        "Temperature (C)": 12.4,
        "Humidity (%)": 69,
        "Wind Speed (km/h)": 5.0,
        "Day": "Monday"
    },
    {
        "Location": "Seattle",
        "Condition": "Snowy",
        "Temperature (C)": -7.6,
        "Humidity (%)": 39,
        "Wind Speed (km/h)": 21.0,
        "Day": "Wednesday"
    },
    {
        "Location": "Chicago",
        "Condition": "Windy",
        "Temperature (C)": -2.3,
        "Humidity (%)": 23,
        "Wind Speed (km/h)": 17.1,
        "Day": "Saturday"
    }
]<start>
Location: Seattle | Condition: Sunny | Temperature (C): 10.1 | Humidity (%): 20 | Wind Speed (km/h): 13.8 | Day: Tuesday
Location: Denver | Condition: Windy | Temperature (C): 15.8 | Humidity (%): 52 | Wind Speed (km/h): 17.1 | Day: Monday
Location: Phoenix | Condition: Sunny | Temperature (C): -5.0 | Humidity (%): 42 | Wind Speed (km/h): 13.8 | Day: Saturday
Location: Los Angeles | Condition: Rainy | Temperature (C): 15.4 | Humidity (%): 95 | Wind Speed (km/h): 19.4 | Day: Wednesday
Location: Los Angeles | Condition: Windy | Temperature (C): -5.0 | Humidity (%): 75 | Wind Speed (km/h): 13.7 | Day: Friday
Location: Denver | Condition: Snowy | Temperature (C): 32.4 | Humidity (%): 39 | Wind Speed (km/h): 28.7 | Day: Friday
Location: Denver | Condition: Cloudy | Temperature (C): 24.5 | Humidity (%): 44 | Wind Speed (km/h): 24.5 | Day: Thursday
Location: Houston | Condition: Windy | Temperature (C): 12.4 | Humidity (%): 69 | Wind Speed (km/h): 5.0 | Day: Monday
Location: Seattle | Condition: Snowy | Temperature (C): -7.6 | Humidity (%): 39 | Wind Speed (km/h): 21.0 | Day: Wednesday
Location: Chicago | Condition: Windy | Temperature (C): -2.3 | Humidity (%): 23 | Wind Speed (km/h): 17.1 | Day: Saturday
<end>Convert this yml to Markdown:
- Box Office Earnings (M): 639.56
  Director: Aria Ravenwood
  Release Year: 1974
  Title: Rise of the Titans
- Box Office Earnings (M): 509.0
  Director: Drake Nightshade
  Release Year: 1990
  Title: Rise of the Titans
- Box Office Earnings (M): 341.75
  Director: Drake Nightshade
  Release Year: 2015
  Title: Starbound Odyssey
<start>
| Title | Director | Release Year | Box Office Earnings (M) |
| --- | --- | --- | --- |
| Rise of the Titans | Aria Ravenwood | 1974 | 639.56 |
| Rise of the Titans | Drake Nightshade | 1990 | 509.0 |
| Starbound Odyssey | Drake Nightshade | 2015 | 341.75 |
<end>Transform this markdown structure to a Json format:
| Restaurant Name | Price Range |
| --- | --- |
| Burger Haven | $$$ |
| The Golden Spoon | $$$$$ |
| The Golden Spoon | $$$ |
| The Golden Spoon | $$$$ |
| BBQ Barn | $$ |<start>
[
    {
        "Restaurant Name": "Burger Haven",
        "Price Range": "$$$"
    },
    {
        "Restaurant Name": "The Golden Spoon",
        "Price Range": "$$$$$"
    },
    {
        "Restaurant Name": "The Golden Spoon",
        "Price Range": "$$$"
    },
    {
        "Restaurant Name": "The Golden Spoon",
        "Price Range": "$$$$"
    },
    {
        "Restaurant Name": "BBQ Barn",
        "Price Range": "$$"
    }
]
<end>Transform this PLAIN TEXT structure to a MARKDOWN format:
Restaurant Name: Sushi World | Cuisine: Mediterranean | Location: Houston | Rating: 3
Restaurant Name: The Golden Spoon | Cuisine: Chinese | Location: Phoenix | Rating: 2
Restaurant Name: Curry Corner | Cuisine: Indian | Location: Miami | Rating: 2
Restaurant Name: Curry Corner | Cuisine: Italian | Location: Seattle | Rating: 2
Restaurant Name: The Steakhouse | Cuisine: Mediterranean | Location: Los Angeles | Rating: 4
Restaurant Name: Burger Haven | Cuisine: Mexican | Location: Seattle | Rating: 5
Restaurant Name: The Steakhouse | Cuisine: Mediterranean | Location: Los Angeles | Rating: 3
Restaurant Name: Curry Corner | Cuisine: Chinese | Location: Miami | Rating: 3
Restaurant Name: Pasta Palace | Cuisine: Indian | Location: Phoenix | Rating: 5
<start>
| Restaurant Name | Cuisine | Location | Rating |
| --- | --- | --- | --- |
| Sushi World | Mediterranean | Houston | 3 |
| The Golden Spoon | Chinese | Phoenix | 2 |
| Curry Corner | Indian | Miami | 2 |
| Curry Corner | Italian | Seattle | 2 |
| The Steakhouse | Mediterranean | Los Angeles | 4 |
| Burger Haven | Mexican | Seattle | 5 |
| The Steakhouse | Mediterranean | Los Angeles | 3 |
| Curry Corner | Chinese | Miami | 3 |
| Pasta Palace | Indian | Phoenix | 5 |
<end>Here's some json data, can you convert it to csv?
[
    {
        "Database Name": "InventoryDB",
        "Queries per Second": 2186.52,
        "Cache Hit Ratio (%)": 74.37,
        "Connection Count": 219,
        "Timestamp": "2023-11-26 23:58:00"
    },
    {
        "Database Name": "SalesDB",
        "Queries per Second": 2476.0,
        "Cache Hit Ratio (%)": 80.44,
        "Connection Count": 432,
        "Timestamp": "2022-08-25 22:36:58"
    },
    {
        "Database Name": "SalesDB",
        "Queries per Second": 3466.71,
        "Cache Hit Ratio (%)": 89.86,
        "Connection Count": 122,
        "Timestamp": "2023-04-10 04:46:28"
    }
]<start>
Database Name,Queries per Second,Cache Hit Ratio (%),Connection Count,Timestamp
InventoryDB,2186.52,74.37,219,2023-11-26 23:58:00
SalesDB,2476.0,80.44,432,2022-08-25 22:36:58
SalesDB,3466.71,89.86,122,2023-04-10 04:46:28
<end>Here's some MARKDOWN data, can you convert it to Csv?
| Trip Name | Start Location | End Location | Distance (miles) | Duration (hours) |
| --- | --- | --- | --- | --- |
| Coast to Coast | Chicago | Phoenix | 2399.0 | 34.6 |
| Forest Journey | New York | Miami | 2937.2 | 48.9 |
| Coast to Coast | Denver | Phoenix | 1826.4 | 10.8 |
| Mountain Adventure | San Francisco | Phoenix | 2676.3 | 17.3 |
| Mountain Adventure | Houston | Denver | 2415.7 | 49.7 |
| Canyon Trek | New York | Denver | 844.5 | 38.6 |
| Lakeside Retreat | Chicago | Houston | 2265.4 | 12.9 |
| Highway Odyssey | Los Angeles | Houston | 1960.7 | 39.5 |<start>
Trip Name,Start Location,End Location,Distance (miles),Duration (hours)
Coast to Coast,Chicago,Phoenix,2399.0,34.6
Forest Journey,New York,Miami,2937.2,48.9
Coast to Coast,Denver,Phoenix,1826.4,10.8
Mountain Adventure,San Francisco,Phoenix,2676.3,17.3
Mountain Adventure,Houston,Denver,2415.7,49.7
Canyon Trek,New York,Denver,844.5,38.6
Lakeside Retreat,Chicago,Houston,2265.4,12.9
Highway Odyssey,Los Angeles,Houston,1960.7,39.5
<end>Can you change this json into markdown?
[
    {
        "Title": "The Forgotten World",
        "Author": "Rowan Ashborne",
        "Genre": "Romance",
        "Publication Year": 2001,
        "Rating": 4.9
    },
    {
        "Title": "Tales of the Brave",
        "Author": "Draven Blackthorn",
        "Genre": "Horror",
        "Publication Year": 1977,
        "Rating": 4.1
    },
    {
        "Title": "A Journey Through Time",
        "Author": "Kara Firebrand",
        "Genre": "Romance",
        "Publication Year": 1981,
        "Rating": 4.9
    },
    {
        "Title": "Whispers of the Abyss",
        "Author": "Thorne Ironwood",
        "Genre": "Fantasy",
        "Publication Year": 1958,
        "Rating": 1.6
    },
    {
        "Title": "Shadows of Solitude",
        "Author": "Luna Silverleaf",
        "Genre": "Romance",
        "Publication Year": 1995,
        "Rating": 4.0
    },
    {
        "Title": "Echoes of Eternity",
        "Author": "Rowan Ashborne",
        "Genre": "Horror",
        "Publication Year": 1991,
        "Rating": 2.9
    }
]<start>
| Title | Author | Genre | Publication Year | Rating |
| --- | --- | --- | --- | --- |
| The Forgotten World | Rowan Ashborne | Romance | 2001 | 4.9 |
| Tales of the Brave | Draven Blackthorn | Horror | 1977 | 4.1 |
| A Journey Through Time | Kara Firebrand | Romance | 1981 | 4.9 |
| Whispers of the Abyss | Thorne Ironwood | Fantasy | 1958 | 1.6 |
| Shadows of Solitude | Luna Silverleaf | Romance | 1995 | 4.0 |
| Echoes of Eternity | Rowan Ashborne | Horror | 1991 | 2.9 |
<end>Here's some Csv data, can you convert it to JSON?
Device ID,Battery Level (%),Reading Value,Timestamp
device-0088,31.1,-35.3,2023-04-22 19:01:35
device-0048,39.7,31.56,2023-11-02 12:00:12
device-0031,13.3,76.72,2021-08-19 04:18:42
device-0021,80.9,73.9,2021-08-13 19:07:40
device-0078,83.9,69.81,2021-08-23 05:21:25
device-0092,84.5,41.03,2021-07-22 23:14:40
<start>
[
    {
        "Device ID": "device-0088",
        "Battery Level (%)": 31.1,
        "Reading Value": -35.3,
        "Timestamp": "2023-04-22 19:01:35"
    },
    {
        "Device ID": "device-0048",
        "Battery Level (%)": 39.7,
        "Reading Value": 31.56,
        "Timestamp": "2023-11-02 12:00:12"
    },
    {
        "Device ID": "device-0031",
        "Battery Level (%)": 13.3,
        "Reading Value": 76.72,
        "Timestamp": "2021-08-19 04:18:42"
    },
    {
        "Device ID": "device-0021",
        "Battery Level (%)": 80.9,
        "Reading Value": 73.9,
        "Timestamp": "2021-08-13 19:07:40"
    },
    {
        "Device ID": "device-0078",
        "Battery Level (%)": 83.9,
        "Reading Value": 69.81,
        "Timestamp": "2021-08-23 05:21:25"
    },
    {
        "Device ID": "device-0092",
        "Battery Level (%)": 84.5,
        "Reading Value": 41.03,
        "Timestamp": "2021-07-22 23:14:40"
    }
]
<end>Here's some JSON data, can you convert it to markdown?
[
    {
        "Author": "Sylvia Nightshade",
        "Genre": "Thriller",
        "Publication Year": 2018
    },
    {
        "Author": "Draven Blackthorn",
        "Genre": "Mystery",
        "Publication Year": 2006
    },
    {
        "Author": "Thorne Ironwood",
        "Genre": "Mystery",
        "Publication Year": 2010
    },
    {
        "Author": "Rowan Ashborne",
        "Genre": "Horror",
        "Publication Year": 1973
    },
    {
        "Author": "Isla Windrider",
        "Genre": "Science Fiction",
        "Publication Year": 2006
    },
    {
        "Author": "Galen Starfire",
        "Genre": "Fantasy",
        "Publication Year": 1996
    },
    {
        "Author": "Sylvia Nightshade",
        "Genre": "Fantasy",
        "Publication Year": 1977
    },
    {
        "Author": "Draven Blackthorn",
        "Genre": "Thriller",
        "Publication Year": 1989
    }
]<start>
| Author | Genre | Publication Year |
| --- | --- | --- |
| Sylvia Nightshade | Thriller | 2018 |
| Draven Blackthorn | Mystery | 2006 |
| Thorne Ironwood | Mystery | 2010 |
| Rowan Ashborne | Horror | 1973 |
| Isla Windrider | Science Fiction | 2006 |
| Galen Starfire | Fantasy | 1996 |
| Sylvia Nightshade | Fantasy | 1977 |
| Draven Blackthorn | Thriller | 1989 |
<end>Please transform the following MARKDOWN data into yaml:
| Rating | Price Range |
| --- | --- |
| 5 | $$$$$ |
| 3 | $$ |
| 4 | $$ |<start>
- Price Range: $$$$$
  Rating: 5
- Price Range: $$
  Rating: 3
- Price Range: $$
  Rating: 4
<end>Transform this Csv structure to a YML format:
Title,Author,Genre,Publication Year
The Forgotten World,Galen Starfire,Horror,2009
A Journey Through Time,Elara Moonshadow,Romance,2013
The Last Sky,Isla Windrider,Thriller,1962
A Journey Through Time,Thorne Ironwood,Fantasy,1950
The Last Sky,Isla Windrider,Fantasy,2000
Legends of the Rift,Thorne Ironwood,Historical,1991
The Forgotten World,Rowan Ashborne,Romance,2009
Whispers of the Abyss,Luna Silverleaf,Fantasy,1995
The Silent Grove,Sylvia Nightshade,Horror,1992
The Forgotten World,Orion Frostblade,Historical,2013
<start>
- Author: Galen Starfire
  Genre: Horror
  Publication Year: 2009
  Title: The Forgotten World
- Author: Elara Moonshadow
  Genre: Romance
  Publication Year: 2013
  Title: A Journey Through Time
- Author: Isla Windrider
  Genre: Thriller
  Publication Year: 1962
  Title: The Last Sky
- Author: Thorne Ironwood
  Genre: Fantasy
  Publication Year: 1950
  Title: A Journey Through Time
- Author: Isla Windrider
  Genre: Fantasy
  Publication Year: 2000
  Title: The Last Sky
- Author: Thorne Ironwood
  Genre: Historical
  Publication Year: 1991
  Title: Legends of the Rift
- Author: Rowan Ashborne
  Genre: Romance
  Publication Year: 2009
  Title: The Forgotten World
- Author: Luna Silverleaf
  Genre: Fantasy
  Publication Year: 1995
  Title: Whispers of the Abyss
- Author: Sylvia Nightshade
  Genre: Horror
  Publication Year: 1992
  Title: The Silent Grove
- Author: Orion Frostblade
  Genre: Historical
  Publication Year: 2013
  Title: The Forgotten World
<end>Here's some csv data, can you convert it to json?
SKU,Price,Supplier Name
SKU-1075,303.67,Wonka Industries
SKU-1031,452.46,Globex
SKU-1088,279.85,Wayne Enterprises
SKU-1076,109.7,Wonka Industries
<start>
[
    {
        "SKU": "SKU-1075",
        "Price": 303.67,
        "Supplier Name": "Wonka Industries"
    },
    {
        "SKU": "SKU-1031",
        "Price": 452.46,
        "Supplier Name": "Globex"
    },
    {
        "SKU": "SKU-1088",
        "Price": 279.85,
        "Supplier Name": "Wayne Enterprises"
    },
    {
        "SKU": "SKU-1076",
        "Price": 109.7,
        "Supplier Name": "Wonka Industries"
    }
]
<end>Please transform the following Markdown data into plain text:
| Title | Director | Release Year | Box Office Earnings (M) |
| --- | --- | --- | --- |
| Beyond the Veil | Rylan Frostblade | 2023 | 703.15 |
| Rise of the Titans | Mara Moonshadow | 1981 | 794.96 |
| Beyond the Veil | Mara Moonshadow | 1992 | 794.96 |
| The Final Voyage | Selene Darkwhisper | 2011 | 30.96 |
| The Endless Horizon | Orin Shadowalker | 2016 | 163.17 |
| Starbound Odyssey | Aria Ravenwood | 2013 | 601.65 |
| Dreamwalker | Drake Nightshade | 2017 | 878.4 |
| Rise of the Titans | Cade Firebrand | 2016 | 548.74 |
| The Final Voyage | Mara Moonshadow | 1974 | 805.1 |<start>
Title: Beyond the Veil | Director: Rylan Frostblade | Release Year: 2023 | Box Office Earnings (M): 703.15
Title: Rise of the Titans | Director: Mara Moonshadow | Release Year: 1981 | Box Office Earnings (M): 794.96
Title: Beyond the Veil | Director: Mara Moonshadow | Release Year: 1992 | Box Office Earnings (M): 794.96
Title: The Final Voyage | Director: Selene Darkwhisper | Release Year: 2011 | Box Office Earnings (M): 30.96
Title: The Endless Horizon | Director: Orin Shadowalker | Release Year: 2016 | Box Office Earnings (M): 163.17
Title: Starbound Odyssey | Director: Aria Ravenwood | Release Year: 2013 | Box Office Earnings (M): 601.65
Title: Dreamwalker | Director: Drake Nightshade | Release Year: 2017 | Box Office Earnings (M): 878.4
Title: Rise of the Titans | Director: Cade Firebrand | Release Year: 2016 | Box Office Earnings (M): 548.74
Title: The Final Voyage | Director: Mara Moonshadow | Release Year: 1974 | Box Office Earnings (M): 805.1
<end>Transform this Markdown structure to a PLAIN TEXT format:
| Product Name | SKU | Stock Quantity | Category | Supplier Name |
| --- | --- | --- | --- | --- |
| Apparatus | SKU-1042 | 266 | Electronics | Wonka Industries |
| Doohickey | SKU-1074 | 403 | Electronics | Umbrella Corp |
| Thingamajig | SKU-1010 | 105 | Electronics | ACME Corp |
| Contraption | SKU-1089 | 446 | Automotive | Wonka Industries |<start>
Product Name: Apparatus | SKU: SKU-1042 | Stock Quantity: 266 | Category: Electronics | Supplier Name: Wonka Industries
Product Name: Doohickey | SKU: SKU-1074 | Stock Quantity: 403 | Category: Electronics | Supplier Name: Umbrella Corp
Product Name: Thingamajig | SKU: SKU-1010 | Stock Quantity: 105 | Category: Electronics | Supplier Name: ACME Corp
Product Name: Contraption | SKU: SKU-1089 | Stock Quantity: 446 | Category: Automotive | Supplier Name: Wonka Industries
<end>Please transform the following PLAIN TEXT data into YAML:
Restaurant Name: The Golden Spoon | Cuisine: American | Location: Chicago | Rating: 5
Restaurant Name: Pasta Palace | Cuisine: American | Location: New York | Rating: 4
Restaurant Name: Sushi World | Cuisine: American | Location: Seattle | Rating: 3
Restaurant Name: Vegan Delight | Cuisine: American | Location: Phoenix | Rating: 1
Restaurant Name: BBQ Barn | Cuisine: Chinese | Location: Miami | Rating: 4
Restaurant Name: Vegan Delight | Cuisine: French | Location: Miami | Rating: 3
Restaurant Name: The Golden Spoon | Cuisine: Mediterranean | Location: Chicago | Rating: 2
<start>
- Cuisine: American
  Location: Chicago
  Rating: 5
  Restaurant Name: The Golden Spoon
- Cuisine: American
  Location: New York
  Rating: 4
  Restaurant Name: Pasta Palace
- Cuisine: American
  Location: Seattle
  Rating: 3
  Restaurant Name: Sushi World
- Cuisine: American
  Location: Phoenix
  Rating: 1
  Restaurant Name: Vegan Delight
- Cuisine: Chinese
  Location: Miami
  Rating: 4
  Restaurant Name: BBQ Barn
- Cuisine: French
  Location: Miami
  Rating: 3
  Restaurant Name: Vegan Delight
- Cuisine: Mediterranean
  Location: Chicago
  Rating: 2
  Restaurant Name: The Golden Spoon
<end>Transform this markdown structure to a plain text format:
| Title | Director | Genre |
| --- | --- | --- |
| Mystery of the Depths | Talon Blackthorn | Fantasy |
| Starbound Odyssey | Rylan Frostblade | Comedy |
| Beyond the Veil | Cade Firebrand | Sci-Fi |
| Rise of the Titans | Rylan Frostblade | Action |
| Edge of Infinity | Zara Stormrider | Action |
| The Final Voyage | Aria Ravenwood | Thriller |<start>
Title: Mystery of the Depths | Director: Talon Blackthorn | Genre: Fantasy
Title: Starbound Odyssey | Director: Rylan Frostblade | Genre: Comedy
Title: Beyond the Veil | Director: Cade Firebrand | Genre: Sci-Fi
Title: Rise of the Titans | Director: Rylan Frostblade | Genre: Action
Title: Edge of Infinity | Director: Zara Stormrider | Genre: Action
Title: The Final Voyage | Director: Aria Ravenwood | Genre: Thriller
<end>Convert this Markdown to JSON:
| Device ID | Location | Battery Level (%) | Reading Value |
| --- | --- | --- | --- |
| device-0066 | Garage | 80.5 | 23.6 |
| device-0037 | Garage | 54.1 | 36.45 |
| device-0055 | Garden | 70.9 | 12.09 |<start>
[
    {
        "Device ID": "device-0066",
        "Location": "Garage",
        "Battery Level (%)": 80.5,
        "Reading Value": 23.6
    },
    {
        "Device ID": "device-0037",
        "Location": "Garage",
        "Battery Level (%)": 54.1,
        "Reading Value": 36.45
    },
    {
        "Device ID": "device-0055",
        "Location": "Garden",
        "Battery Level (%)": 70.9,
        "Reading Value": 12.09
    }
]
<end>Can you change this PLAIN TEXT into Csv?
Database Name: ProductsDB | Queries per Second: 4059.87 | Connection Count: 55 | Average Latency (ms): 12.21
Database Name: ProfilesDB | Queries per Second: 174.98 | Connection Count: 427 | Average Latency (ms): 42.33
Database Name: MetricsDB | Queries per Second: 1947.02 | Connection Count: 11 | Average Latency (ms): 43.28
Database Name: LogsDB | Queries per Second: 3130.49 | Connection Count: 482 | Average Latency (ms): 71.45
Database Name: LogsDB | Queries per Second: 2641.11 | Connection Count: 171 | Average Latency (ms): 93.7
Database Name: LogsDB | Queries per Second: 3534.73 | Connection Count: 145 | Average Latency (ms): 31.63
Database Name: LogsDB | Queries per Second: 4901.67 | Connection Count: 221 | Average Latency (ms): 44.86
<start>
Database Name,Queries per Second,Connection Count,Average Latency (ms)
ProductsDB,4059.87,55,12.21
ProfilesDB,174.98,427,42.33
MetricsDB,1947.02,11,43.28
LogsDB,3130.49,482,71.45
LogsDB,2641.11,171,93.7
LogsDB,3534.73,145,31.63
LogsDB,4901.67,221,44.86
<end>Please transform the following yml data into markdown:
- Condition: Rainy
  Day: Thursday
  Humidity (%): 48
  Location: Houston
  Temperature (C): 16.9
  Wind Speed (km/h): 10.1
- Condition: Snowy
  Day: Wednesday
  Humidity (%): 93
  Location: Seattle
  Temperature (C): 9.1
  Wind Speed (km/h): 2.1
- Condition: Snowy
  Day: Monday
  Humidity (%): 77
  Location: Denver
  Temperature (C): 27.5
  Wind Speed (km/h): 8.0
- Condition: Snowy
  Day: Wednesday
  Humidity (%): 73
  Location: Seattle
  Temperature (C): -8.5
  Wind Speed (km/h): 0.9
- Condition: Rainy
  Day: Thursday
  Humidity (%): 56
  Location: Seattle
  Temperature (C): 2.3
  Wind Speed (km/h): 3.3
- Condition: Rainy
  Day: Sunday
  Humidity (%): 80
  Location: Seattle
  Temperature (C): 32.4
  Wind Speed (km/h): 20.0
- Condition: Stormy
  Day: Monday
  Humidity (%): 62
  Location: Seattle
  Temperature (C): 34.4
  Wind Speed (km/h): 20.7
- Condition: Cloudy
  Day: Wednesday
  Humidity (%): 23
  Location: Chicago
  Temperature (C): 29.7
  Wind Speed (km/h): 22.5
<start>
| Location | Condition | Temperature (C) | Humidity (%) | Wind Speed (km/h) | Day |
| --- | --- | --- | --- | --- | --- |
| Houston | Rainy | 16.9 | 48 | 10.1 | Thursday |
| Seattle | Snowy | 9.1 | 93 | 2.1 | Wednesday |
| Denver | Snowy | 27.5 | 77 | 8.0 | Monday |
| Seattle | Snowy | -8.5 | 73 | 0.9 | Wednesday |
| Seattle | Rainy | 2.3 | 56 | 3.3 | Thursday |
| Seattle | Rainy | 32.4 | 80 | 20.0 | Sunday |
| Seattle | Stormy | 34.4 | 62 | 20.7 | Monday |
| Chicago | Cloudy | 29.7 | 23 | 22.5 | Wednesday |
<end>Please transform the following Json data into Markdown:
[
    {
        "Company": "FinanceWorks",
        "Sector": "Biotech",
        "Quarter": "Q1"
    },
    {
        "Company": "EcoEnergy",
        "Sector": "Technology",
        "Quarter": "Q4"
    },
    {
        "Company": "AeroSpace",
        "Sector": "Energy",
        "Quarter": "Q2"
    },
    {
        "Company": "FinanceWorks",
        "Sector": "Aerospace",
        "Quarter": "Q1"
    },
    {
        "Company": "AutoDrive",
        "Sector": "Technology",
        "Quarter": "Q3"
    },
    {
        "Company": "AutoDrive",
        "Sector": "Biotech",
        "Quarter": "Q2"
    },
    {
        "Company": "FinanceWorks",
        "Sector": "Aerospace",
        "Quarter": "Q1"
    }
]<start>
| Company | Sector | Quarter |
| --- | --- | --- |
| FinanceWorks | Biotech | Q1 |
| EcoEnergy | Technology | Q4 |
| AeroSpace | Energy | Q2 |
| FinanceWorks | Aerospace | Q1 |
| AutoDrive | Technology | Q3 |
| AutoDrive | Biotech | Q2 |
| FinanceWorks | Aerospace | Q1 |
<end>Can you change this csv into markdown?
Company,Date,High Price,Low Price
HealthGen,2017-02-17,1267.57,756.82
BioLife,2012-09-07,1448.09,478.62
BioLife,2022-10-15,1056.45,730.34
TechnoCorp,2018-03-09,1311.5,452.95
GreenEnergy,2017-02-24,1295.7,869.09
GreenEnergy,2014-04-18,730.34,134.26
AutoMotive,2023-12-11,1383.3,474.52
RetailWorld,2017-06-10,740.5,134.26
FoodChain,2012-09-14,1241.98,804.93
AeroSystems,2014-08-02,1443.69,833.51
<start>
| Company | Date | High Price | Low Price |
| --- | --- | --- | --- |
| HealthGen | 2017-02-17 | 1267.57 | 756.82 |
| BioLife | 2012-09-07 | 1448.09 | 478.62 |
| BioLife | 2022-10-15 | 1056.45 | 730.34 |
| TechnoCorp | 2018-03-09 | 1311.5 | 452.95 |
| GreenEnergy | 2017-02-24 | 1295.7 | 869.09 |
| GreenEnergy | 2014-04-18 | 730.34 | 134.26 |
| AutoMotive | 2023-12-11 | 1383.3 | 474.52 |
| RetailWorld | 2017-06-10 | 740.5 | 134.26 |
| FoodChain | 2012-09-14 | 1241.98 | 804.93 |
| AeroSystems | 2014-08-02 | 1443.69 | 833.51 |
<end>Here's some PLAIN TEXT data, can you convert it to MARKDOWN?
Trip Name: Lakeside Retreat | End Location: Miami | Distance (miles): 915.8 | Duration (hours): 62.7 | Fuel Used (gallons): 49.4
Trip Name: Coast to Coast | End Location: Denver | Distance (miles): 1148.5 | Duration (hours): 27.7 | Fuel Used (gallons): 82.2
Trip Name: Forest Journey | End Location: Chicago | Distance (miles): 2731.5 | Duration (hours): 33.7 | Fuel Used (gallons): 11.6
Trip Name: Desert Drive | End Location: Miami | Distance (miles): 1148.5 | Duration (hours): 7.3 | Fuel Used (gallons): 12.1
Trip Name: Desert Drive | End Location: New York | Distance (miles): 2810.4 | Duration (hours): 46.0 | Fuel Used (gallons): 25.7
Trip Name: Canyon Trek | End Location: Houston | Distance (miles): 549.5 | Duration (hours): 3.4 | Fuel Used (gallons): 19.9
Trip Name: City Explorer | End Location: Phoenix | Distance (miles): 791.2 | Duration (hours): 58.8 | Fuel Used (gallons): 35.0
Trip Name: City Explorer | End Location: New York | Distance (miles): 1431.6 | Duration (hours): 18.5 | Fuel Used (gallons): 10.9
Trip Name: Canyon Trek | End Location: Phoenix | Distance (miles): 2403.2 | Duration (hours): 8.3 | Fuel Used (gallons): 82.5
Trip Name: Mountain Adventure | End Location: Chicago | Distance (miles): 587.2 | Duration (hours): 19.8 | Fuel Used (gallons): 82.5
<start>
| Trip Name | End Location | Distance (miles) | Duration (hours) | Fuel Used (gallons) |
| --- | --- | --- | --- | --- |
| Lakeside Retreat | Miami | 915.8 | 62.7 | 49.4 |
| Coast to Coast | Denver | 1148.5 | 27.7 | 82.2 |
| Forest Journey | Chicago | 2731.5 | 33.7 | 11.6 |
| Desert Drive | Miami | 1148.5 | 7.3 | 12.1 |
| Desert Drive | New York | 2810.4 | 46.0 | 25.7 |
| Canyon Trek | Houston | 549.5 | 3.4 | 19.9 |
| City Explorer | Phoenix | 791.2 | 58.8 | 35.0 |
| City Explorer | New York | 1431.6 | 18.5 | 10.9 |
| Canyon Trek | Phoenix | 2403.2 | 8.3 | 82.5 |
| Mountain Adventure | Chicago | 587.2 | 19.8 | 82.5 |
<end>Please transform the following Csv data into YAML:
Genre,Publication Year,Rating
Historical,1988,4.3
Non-Fiction,2016,3.1
Romance,2017,2.5
Romance,1996,3.4
Fantasy,2014,1.7
Science Fiction,1989,3.9
Science Fiction,1974,3.2
Science Fiction,1971,3.1
Mystery,1977,5.0
<start>
- Genre: Historical
  Publication Year: 1988
  Rating: 4.3
- Genre: Non-Fiction
  Publication Year: 2016
  Rating: 3.1
- Genre: Romance
  Publication Year: 2017
  Rating: 2.5
- Genre: Romance
  Publication Year: 1996
  Rating: 3.4
- Genre: Fantasy
  Publication Year: 2014
  Rating: 1.7
- Genre: Science Fiction
  Publication Year: 1989
  Rating: 3.9
- Genre: Science Fiction
  Publication Year: 1974
  Rating: 3.2
- Genre: Science Fiction
  Publication Year: 1971
  Rating: 3.1
- Genre: Mystery
  Publication Year: 1977
  Rating: 5.0
<end>Transform this Markdown structure to a yaml format:
| Company | Sector | Market Cap | Stock Price | Annual Revenue (B) | Quarter |
| --- | --- | --- | --- | --- | --- |
| FinanceWorks | Energy | Mega Cap | 581.61 | 487.88 | Q1 |
| FinanceWorks | Healthcare | Small Cap | 11.07 | 322.15 | Q2 |
| Foodies | Healthcare | Small Cap | 815.27 | 470.03 | Q3 |
| AutoDrive | Healthcare | Large Cap | 507.06 | 496.59 | Q3 |
| RetailHub | Automotive | Small Cap | 456.5 | 59.53 | Q2 |
| HealthPlus | Aerospace | Mega Cap | 133.99 | 110.41 | Q1 |
| FinanceWorks | Retail | Large Cap | 356.94 | 470.03 | Q3 |
| Foodies | Automotive | Large Cap | 267.26 | 200.78 | Q2 |<start>
- Annual Revenue (B): 487.88
  Company: FinanceWorks
  Market Cap: Mega Cap
  Quarter: Q1
  Sector: Energy
  Stock Price: 581.61
- Annual Revenue (B): 322.15
  Company: FinanceWorks
  Market Cap: Small Cap
  Quarter: Q2
  Sector: Healthcare
  Stock Price: 11.07
- Annual Revenue (B): 470.03
  Company: Foodies
  Market Cap: Small Cap
  Quarter: Q3
  Sector: Healthcare
  Stock Price: 815.27
- Annual Revenue (B): 496.59
  Company: AutoDrive
  Market Cap: Large Cap
  Quarter: Q3
  Sector: Healthcare
  Stock Price: 507.06
- Annual Revenue (B): 59.53
  Company: RetailHub
  Market Cap: Small Cap
  Quarter: Q2
  Sector: Automotive
  Stock Price: 456.5
- Annual Revenue (B): 110.41
  Company: HealthPlus
  Market Cap: Mega Cap
  Quarter: Q1
  Sector: Aerospace
  Stock Price: 133.99
- Annual Revenue (B): 470.03
  Company: FinanceWorks
  Market Cap: Large Cap
  Quarter: Q3
  Sector: Retail
  Stock Price: 356.94
- Annual Revenue (B): 200.78
  Company: Foodies
  Market Cap: Large Cap
  Quarter: Q2
  Sector: Automotive
  Stock Price: 267.26
<end>Please transform the following plain text data into markdown:
Release Year: 1994 | Box Office Earnings (M): 396.39
Release Year: 2022 | Box Office Earnings (M): 845.9
Release Year: 2006 | Box Office Earnings (M): 244.6
Release Year: 2022 | Box Office Earnings (M): 119.7
Release Year: 2014 | Box Office Earnings (M): 833.88
Release Year: 1971 | Box Office Earnings (M): 928.79
Release Year: 1994 | Box Office Earnings (M): 216.64
Release Year: 2021 | Box Office Earnings (M): 833.88
<start>
| Release Year | Box Office Earnings (M) |
| --- | --- |
| 1994 | 396.39 |
| 2022 | 845.9 |
| 2006 | 244.6 |
| 2022 | 119.7 |
| 2014 | 833.88 |
| 1971 | 928.79 |
| 1994 | 216.64 |
| 2021 | 833.88 |
<end>Can you change this markdown into csv?
| Title | Genre | Release Year |
| --- | --- | --- |
| The Great Expedition | Thriller | 1998 |
| The Final Voyage | Drama | 1995 |
| Mystery of the Depths | Comedy | 2022 |
| Edge of Infinity | Sci-Fi | 2000 |
| The Great Expedition | Action | 1982 |<start>
Title,Genre,Release Year
The Great Expedition,Thriller,1998
The Final Voyage,Drama,1995
Mystery of the Depths,Comedy,2022
Edge of Infinity,Sci-Fi,2000
The Great Expedition,Action,1982
<end>Transform this Markdown structure to a YML format:
| Company | Sector | Market Cap | Stock Price | Annual Revenue (B) | Quarter |
| --- | --- | --- | --- | --- | --- |
| EcoEnergy | Energy | Large Cap | 407.7 | 289.06 | Q3 |
| EcoEnergy | Finance | Small Cap | 435.31 | 467.12 | Q2 |
| FinanceWorks | Energy | Large Cap | 255.82 | 445.22 | Q4 |
| FinanceWorks | Biotech | Large Cap | 854.41 | 210.33 | Q4 |
| AeroSpace | Healthcare | Mid Cap | 174.81 | 445.22 | Q2 |
| AeroSpace | Finance | Large Cap | 637.57 | 249.59 | Q2 |<start>
- Annual Revenue (B): 289.06
  Company: EcoEnergy
  Market Cap: Large Cap
  Quarter: Q3
  Sector: Energy
  Stock Price: 407.7
- Annual Revenue (B): 467.12
  Company: EcoEnergy
  Market Cap: Small Cap
  Quarter: Q2
  Sector: Finance
  Stock Price: 435.31
- Annual Revenue (B): 445.22
  Company: FinanceWorks
  Market Cap: Large Cap
  Quarter: Q4
  Sector: Energy
  Stock Price: 255.82
- Annual Revenue (B): 210.33
  Company: FinanceWorks
  Market Cap: Large Cap
  Quarter: Q4
  Sector: Biotech
  Stock Price: 854.41
- Annual Revenue (B): 445.22
  Company: AeroSpace
  Market Cap: Mid Cap
  Quarter: Q2
  Sector: Healthcare
  Stock Price: 174.81
- Annual Revenue (B): 249.59
  Company: AeroSpace
  Market Cap: Large Cap
  Quarter: Q2
  Sector: Finance
  Stock Price: 637.57
<end>Here's some Markdown data, can you convert it to PLAIN TEXT?
| Condition | Temperature (C) | Day |
| --- | --- | --- |
| Snowy | 29.7 | Monday |
| Sunny | 39.5 | Wednesday |
| Windy | 5.8 | Wednesday |
| Snowy | 22.5 | Tuesday |
| Stormy | -2.3 | Friday |
| Snowy | -5.1 | Monday |
| Snowy | 23.7 | Friday |
| Cloudy | 22.2 | Friday |<start>
Condition: Snowy | Temperature (C): 29.7 | Day: Monday
Condition: Sunny | Temperature (C): 39.5 | Day: Wednesday
Condition: Windy | Temperature (C): 5.8 | Day: Wednesday
Condition: Snowy | Temperature (C): 22.5 | Day: Tuesday
Condition: Stormy | Temperature (C): -2.3 | Day: Friday
Condition: Snowy | Temperature (C): -5.1 | Day: Monday
Condition: Snowy | Temperature (C): 23.7 | Day: Friday
Condition: Cloudy | Temperature (C): 22.2 | Day: Friday
<end>Please transform the following MARKDOWN data into PLAIN TEXT:
| Database Name | Queries per Second | Cache Hit Ratio (%) | Average Latency (ms) | Timestamp |
| --- | --- | --- | --- | --- |
| MetricsDB | 3074.9 | 80.97 | 45.24 | 2023-06-04 01:51:22 |
| ProductsDB | 1132.76 | 87.62 | 41.6 | 2022-12-13 20:03:45 |
| OrdersDB | 4272.48 | 89.71 | 9.76 | 2021-09-26 13:30:40 |<start>
Database Name: MetricsDB | Queries per Second: 3074.9 | Cache Hit Ratio (%): 80.97 | Average Latency (ms): 45.24 | Timestamp: 2023-06-04 01:51:22
Database Name: ProductsDB | Queries per Second: 1132.76 | Cache Hit Ratio (%): 87.62 | Average Latency (ms): 41.6 | Timestamp: 2022-12-13 20:03:45
Database Name: OrdersDB | Queries per Second: 4272.48 | Cache Hit Ratio (%): 89.71 | Average Latency (ms): 9.76 | Timestamp: 2021-09-26 13:30:40
<end>Please transform the following json data into csv:
[
    {
        "Name": "Tracy",
        "City": "San Antonio",
        "Income": 340000
    },
    {
        "Name": "Ruben",
        "City": "Nashville",
        "Income": 220000
    },
    {
        "Name": "Suzanne",
        "City": "Memphis",
        "Income": 405000
    },
    {
        "Name": "Julia",
        "City": "Columbus",
        "Income": 60000
    },
    {
        "Name": "Cassie",
        "City": "Oklahoma City",
        "Income": 470000
    },
    {
        "Name": "Lauren",
        "City": "Columbus",
        "Income": 295000
    }
]<start>
Name,City,Income
Tracy,San Antonio,340000
Ruben,Nashville,220000
Suzanne,Memphis,405000
Julia,Columbus,60000
Cassie,Oklahoma City,470000
Lauren,Columbus,295000
<end>Can you change this csv into yaml?
Date,Open Price,High Price,Volume
2019-01-23,1307.98,1307.98,3170067
2021-05-22,534.96,780.97,4438779
2019-02-27,133.99,1397.82,3533293
2023-01-26,210.19,858.76,9408266
2023-10-17,1258.62,1358.74,7845935
2018-11-26,227.79,774.3,9750226
<start>
- Date: '2019-01-23'
  High Price: 1307.98
  Open Price: 1307.98
  Volume: 3170067
- Date: '2021-05-22'
  High Price: 780.97
  Open Price: 534.96
  Volume: 4438779
- Date: '2019-02-27'
  High Price: 1397.82
  Open Price: 133.99
  Volume: 3533293
- Date: '2023-01-26'
  High Price: 858.76
  Open Price: 210.19
  Volume: 9408266
- Date: '2023-10-17'
  High Price: 1358.74
  Open Price: 1258.62
  Volume: 7845935
- Date: '2018-11-26'
  High Price: 774.3
  Open Price: 227.79
  Volume: 9750226
<end>Here's some plain text data, can you convert it to Yaml?
Device ID: device-0100 | Device Type: Light Sensor | Reading Value: 18.3 | Timestamp: 2021-02-01 08:24:30
Device ID: device-0095 | Device Type: Temperature Sensor | Reading Value: -19.8 | Timestamp: 2023-09-03 07:11:06
Device ID: device-0067 | Device Type: Temperature Sensor | Reading Value: 1.71 | Timestamp: 2022-09-23 18:52:30
Device ID: device-0006 | Device Type: Humidity Sensor | Reading Value: 20.16 | Timestamp: 2021-07-28 06:15:17
Device ID: device-0021 | Device Type: Pressure Sensor | Reading Value: 5.07 | Timestamp: 2023-04-04 22:01:34
<start>
- Device ID: device-0100
  Device Type: Light Sensor
  Reading Value: 18.3
  Timestamp: '2021-02-01 08:24:30'
- Device ID: device-0095
  Device Type: Temperature Sensor
  Reading Value: -19.8
  Timestamp: '2023-09-03 07:11:06'
- Device ID: device-0067
  Device Type: Temperature Sensor
  Reading Value: 1.71
  Timestamp: '2022-09-23 18:52:30'
- Device ID: device-0006
  Device Type: Humidity Sensor
  Reading Value: 20.16
  Timestamp: '2021-07-28 06:15:17'
- Device ID: device-0021
  Device Type: Pressure Sensor
  Reading Value: 5.07
  Timestamp: '2023-04-04 22:01:34'
<end>Convert this markdown to json:
| Title | Genre | Rating |
| --- | --- | --- |
| The Silent Grove | Mystery | 1.6 |
| The Silent Grove | Science Fiction | 4.0 |
| The Crystal Key | Science Fiction | 4.7 |
| The Last Sky | Romance | 4.1 |
| The Last Sky | Fantasy | 1.8 |
| The Forgotten World | Thriller | 1.6 |
| The Crystal Key | Romance | 3.8 |
| Whispers of the Abyss | Science Fiction | 1.1 |<start>
[
    {
        "Title": "The Silent Grove",
        "Genre": "Mystery",
        "Rating": 1.6
    },
    {
        "Title": "The Silent Grove",
        "Genre": "Science Fiction",
        "Rating": 4.0
    },
    {
        "Title": "The Crystal Key",
        "Genre": "Science Fiction",
        "Rating": 4.7
    },
    {
        "Title": "The Last Sky",
        "Genre": "Romance",
        "Rating": 4.1
    },
    {
        "Title": "The Last Sky",
        "Genre": "Fantasy",
        "Rating": 1.8
    },
    {
        "Title": "The Forgotten World",
        "Genre": "Thriller",
        "Rating": 1.6
    },
    {
        "Title": "The Crystal Key",
        "Genre": "Romance",
        "Rating": 3.8
    },
    {
        "Title": "Whispers of the Abyss",
        "Genre": "Science Fiction",
        "Rating": 1.1
    }
]
<end>Convert this Markdown to plain text:
| Name | Age |
| --- | --- |
| Lillian | 23 |
| Ina | 42 |
| Willie | 36 |
| Isaac | 32 |
| Zachary | 30 |
| Mason | 42 |
| Katrina | 52 |<start>
Name: Lillian | Age: 23
Name: Ina | Age: 42
Name: Willie | Age: 36
Name: Isaac | Age: 32
Name: Zachary | Age: 30
Name: Mason | Age: 42
Name: Katrina | Age: 52
<end>Here's some yml data, can you convert it to markdown?
- Distance (miles): 2316.0
  Duration (hours): 71.4
  End Location: Denver
- Distance (miles): 2418.7
  Duration (hours): 70.8
  End Location: Chicago
- Distance (miles): 1613.6
  Duration (hours): 41.9
  End Location: Houston
- Distance (miles): 2636.8
  Duration (hours): 52.8
  End Location: Denver
- Distance (miles): 2418.7
  Duration (hours): 59.2
  End Location: Chicago
- Distance (miles): 1289.9
  Duration (hours): 26.5
  End Location: Phoenix
- Distance (miles): 1417.4
  Duration (hours): 10.1
  End Location: Los Angeles
- Distance (miles): 1215.1
  Duration (hours): 10.1
  End Location: Houston
- Distance (miles): 1729.3
  Duration (hours): 31.4
  End Location: Los Angeles
<start>
| End Location | Distance (miles) | Duration (hours) |
| --- | --- | --- |
| Denver | 2316.0 | 71.4 |
| Chicago | 2418.7 | 70.8 |
| Houston | 1613.6 | 41.9 |
| Denver | 2636.8 | 52.8 |
| Chicago | 2418.7 | 59.2 |
| Phoenix | 1289.9 | 26.5 |
| Los Angeles | 1417.4 | 10.1 |
| Houston | 1215.1 | 10.1 |
| Los Angeles | 1729.3 | 31.4 |
<end>Here's some json data, can you convert it to plain text?
[
    {
        "Device ID": "device-0017",
        "Device Type": "Humidity Sensor",
        "Battery Level (%)": 52.7,
        "Reading Value": 76.34
    },
    {
        "Device ID": "device-0002",
        "Device Type": "Pressure Sensor",
        "Battery Level (%)": 77.7,
        "Reading Value": -3.24
    },
    {
        "Device ID": "device-0007",
        "Device Type": "Pressure Sensor",
        "Battery Level (%)": 20.7,
        "Reading Value": 16.16
    },
    {
        "Device ID": "device-0005",
        "Device Type": "Temperature Sensor",
        "Battery Level (%)": 25.0,
        "Reading Value": 40.98
    },
    {
        "Device ID": "device-0053",
        "Device Type": "Pressure Sensor",
        "Battery Level (%)": 67.9,
        "Reading Value": 40.46
    }
]<start>
Device ID: device-0017 | Device Type: Humidity Sensor | Battery Level (%): 52.7 | Reading Value: 76.34
Device ID: device-0002 | Device Type: Pressure Sensor | Battery Level (%): 77.7 | Reading Value: -3.24
Device ID: device-0007 | Device Type: Pressure Sensor | Battery Level (%): 20.7 | Reading Value: 16.16
Device ID: device-0005 | Device Type: Temperature Sensor | Battery Level (%): 25.0 | Reading Value: 40.98
Device ID: device-0053 | Device Type: Pressure Sensor | Battery Level (%): 67.9 | Reading Value: 40.46
<end>Transform this CSV structure to a MARKDOWN format:
Company,Sector,Market Cap,Stock Price,Annual Revenue (B),Quarter
TechCorp,Healthcare,Mega Cap,844.98,162.8,Q2
AeroSpace,Biotech,Mid Cap,314.07,208.91,Q4
AutoDrive,Aerospace,Mid Cap,335.93,487.29,Q4
FinanceWorks,Automotive,Small Cap,443.88,101.64,Q2
TechCorp,Finance,Mid Cap,69.02,286.15,Q2
RetailHub,Technology,Mega Cap,993.48,166.24,Q1
RetailHub,Finance,Mid Cap,953.75,218.12,Q2
<start>
| Company | Sector | Market Cap | Stock Price | Annual Revenue (B) | Quarter |
| --- | --- | --- | --- | --- | --- |
| TechCorp | Healthcare | Mega Cap | 844.98 | 162.8 | Q2 |
| AeroSpace | Biotech | Mid Cap | 314.07 | 208.91 | Q4 |
| AutoDrive | Aerospace | Mid Cap | 335.93 | 487.29 | Q4 |
| FinanceWorks | Automotive | Small Cap | 443.88 | 101.64 | Q2 |
| TechCorp | Finance | Mid Cap | 69.02 | 286.15 | Q2 |
| RetailHub | Technology | Mega Cap | 993.48 | 166.24 | Q1 |
| RetailHub | Finance | Mid Cap | 953.75 | 218.12 | Q2 |
<end>Convert this YML to markdown:
- Average Latency (ms): 9.43
  Cache Hit Ratio (%): 88.4
  Connection Count: 193
  Queries per Second: 2052.33
  Timestamp: '2022-12-23 08:52:41'
- Average Latency (ms): 95.12
  Cache Hit Ratio (%): 85.14
  Connection Count: 15
  Queries per Second: 3558.82
  Timestamp: '2021-01-18 23:07:17'
- Average Latency (ms): 88.21
  Cache Hit Ratio (%): 70.29
  Connection Count: 375
  Queries per Second: 4995.65
  Timestamp: '2022-10-01 14:24:02'
- Average Latency (ms): 85.48
  Cache Hit Ratio (%): 78.78
  Connection Count: 194
  Queries per Second: 4075.45
  Timestamp: '2021-07-23 10:10:18'
- Average Latency (ms): 27.39
  Cache Hit Ratio (%): 87.06
  Connection Count: 418
  Queries per Second: 2421.22
  Timestamp: '2022-06-02 11:13:52'
- Average Latency (ms): 88.21
  Cache Hit Ratio (%): 72.32
  Connection Count: 471
  Queries per Second: 4850.97
  Timestamp: '2021-10-06 08:27:10'
- Average Latency (ms): 21.6
  Cache Hit Ratio (%): 79.24
  Connection Count: 488
  Queries per Second: 4669.01
  Timestamp: '2023-01-03 03:32:04'
- Average Latency (ms): 77.14
  Cache Hit Ratio (%): 78.42
  Connection Count: 318
  Queries per Second: 1777.45
  Timestamp: '2022-10-03 11:13:02'
<start>
| Queries per Second | Cache Hit Ratio (%) | Connection Count | Average Latency (ms) | Timestamp |
| --- | --- | --- | --- | --- |
| 2052.33 | 88.4 | 193 | 9.43 | 2022-12-23 08:52:41 |
| 3558.82 | 85.14 | 15 | 95.12 | 2021-01-18 23:07:17 |
| 4995.65 | 70.29 | 375 | 88.21 | 2022-10-01 14:24:02 |
| 4075.45 | 78.78 | 194 | 85.48 | 2021-07-23 10:10:18 |
| 2421.22 | 87.06 | 418 | 27.39 | 2022-06-02 11:13:52 |
| 4850.97 | 72.32 | 471 | 88.21 | 2021-10-06 08:27:10 |
| 4669.01 | 79.24 | 488 | 21.6 | 2023-01-03 03:32:04 |
| 1777.45 | 78.42 | 318 | 77.14 | 2022-10-03 11:13:02 |
<end>Transform this markdown structure to a csv format:
| End Location | Distance (miles) | Duration (hours) |
| --- | --- | --- |
| Houston | 611.9 | 6.6 |
| San Francisco | 1670.3 | 19.0 |
| San Francisco | 1190.6 | 51.6 |<start>
End Location,Distance (miles),Duration (hours)
Houston,611.9,6.6
San Francisco,1670.3,19.0
San Francisco,1190.6,51.6
<end>Here's some yaml data, can you convert it to CSV?
- Average Latency (ms): 6.25
  Cache Hit Ratio (%): 82.05
  Connection Count: 380
  Database Name: AnalyticsDB
  Queries per Second: 1813.75
- Average Latency (ms): 43.08
  Cache Hit Ratio (%): 73.98
  Connection Count: 156
  Database Name: LogsDB
  Queries per Second: 3752.78
- Average Latency (ms): 87.45
  Cache Hit Ratio (%): 76.12
  Connection Count: 190
  Database Name: OrdersDB
  Queries per Second: 3259.83
- Average Latency (ms): 91.44
  Cache Hit Ratio (%): 95.01
  Connection Count: 452
  Database Name: AnalyticsDB
  Queries per Second: 2459.7
- Average Latency (ms): 2.16
  Cache Hit Ratio (%): 88.75
  Connection Count: 318
  Database Name: LogsDB
  Queries per Second: 4976.26
- Average Latency (ms): 48.33
  Cache Hit Ratio (%): 94.42
  Connection Count: 305
  Database Name: MetricsDB
  Queries per Second: 312.76
- Average Latency (ms): 56.92
  Cache Hit Ratio (%): 78.12
  Connection Count: 417
  Database Name: AnalyticsDB
  Queries per Second: 804.27
- Average Latency (ms): 99.2
  Cache Hit Ratio (%): 89.16
  Connection Count: 498
  Database Name: UserDB
  Queries per Second: 880.7
- Average Latency (ms): 32.96
  Cache Hit Ratio (%): 87.75
  Connection Count: 309
  Database Name: ProfilesDB
  Queries per Second: 4942.62
- Average Latency (ms): 79.88
  Cache Hit Ratio (%): 80.49
  Connection Count: 430
  Database Name: ProfilesDB
  Queries per Second: 4595.65
<start>
Database Name,Queries per Second,Cache Hit Ratio (%),Connection Count,Average Latency (ms)
AnalyticsDB,1813.75,82.05,380,6.25
LogsDB,3752.78,73.98,156,43.08
OrdersDB,3259.83,76.12,190,87.45
AnalyticsDB,2459.7,95.01,452,91.44
LogsDB,4976.26,88.75,318,2.16
MetricsDB,312.76,94.42,305,48.33
AnalyticsDB,804.27,78.12,417,56.92
UserDB,880.7,89.16,498,99.2
ProfilesDB,4942.62,87.75,309,32.96
ProfilesDB,4595.65,80.49,430,79.88
<end>Here's some yml data, can you convert it to plain text?
- Battery Level (%): 27.1
  Device ID: device-0090
  Device Type: Temperature Sensor
  Location: Garage
  Reading Value: 2.25
  Timestamp: '2021-09-06 16:14:23'
- Battery Level (%): 11.2
  Device ID: device-0042
  Device Type: Temperature Sensor
  Location: Living Room
  Reading Value: 4.16
  Timestamp: '2022-11-12 01:45:02'
- Battery Level (%): 97.5
  Device ID: device-0054
  Device Type: Light Sensor
  Location: Kitchen
  Reading Value: 64.03
  Timestamp: '2023-07-01 20:41:29'
<start>
Device ID: device-0090 | Device Type: Temperature Sensor | Location: Garage | Battery Level (%): 27.1 | Reading Value: 2.25 | Timestamp: 2021-09-06 16:14:23
Device ID: device-0042 | Device Type: Temperature Sensor | Location: Living Room | Battery Level (%): 11.2 | Reading Value: 4.16 | Timestamp: 2022-11-12 01:45:02
Device ID: device-0054 | Device Type: Light Sensor | Location: Kitchen | Battery Level (%): 97.5 | Reading Value: 64.03 | Timestamp: 2023-07-01 20:41:29
<end>Convert this plain text to JSON:
Name: Virgie | Age: 33 | City: San Jose | Income: 435000
Name: Bryan | Age: 60 | City: Milwaukee | Income: 85000
Name: Luis | Age: 48 | City: Jacksonville | Income: 180000
Name: Marjorie | Age: 54 | City: Las Vegas | Income: 255000
Name: Silas | Age: 31 | City: Charlotte | Income: 340000
Name: Katelyn | Age: 34 | City: Nashville | Income: 165000
<start>
[
    {
        "Name": "Virgie",
        "Age": 33,
        "City": "San Jose",
        "Income": 435000
    },
    {
        "Name": "Bryan",
        "Age": 60,
        "City": "Milwaukee",
        "Income": 85000
    },
    {
        "Name": "Luis",
        "Age": 48,
        "City": "Jacksonville",
        "Income": 180000
    },
    {
        "Name": "Marjorie",
        "Age": 54,
        "City": "Las Vegas",
        "Income": 255000
    },
    {
        "Name": "Silas",
        "Age": 31,
        "City": "Charlotte",
        "Income": 340000
    },
    {
        "Name": "Katelyn",
        "Age": 34,
        "City": "Nashville",
        "Income": 165000
    }
]
<end>Convert this csv to Yml:
Database Name,Cache Hit Ratio (%),Connection Count,Average Latency (ms),Timestamp
UserDB,70.54,474,78.49,2021-07-19 07:04:13
MetricsDB,80.43,435,35.67,2023-02-07 18:06:05
LogsDB,75.95,262,25.57,2021-05-08 20:49:27
LogsDB,94.71,112,87.76,2022-08-08 08:28:12
<start>
- Average Latency (ms): 78.49
  Cache Hit Ratio (%): 70.54
  Connection Count: 474
  Database Name: UserDB
  Timestamp: '2021-07-19 07:04:13'
- Average Latency (ms): 35.67
  Cache Hit Ratio (%): 80.43
  Connection Count: 435
  Database Name: MetricsDB
  Timestamp: '2023-02-07 18:06:05'
- Average Latency (ms): 25.57
  Cache Hit Ratio (%): 75.95
  Connection Count: 262
  Database Name: LogsDB
  Timestamp: '2021-05-08 20:49:27'
- Average Latency (ms): 87.76
  Cache Hit Ratio (%): 94.71
  Connection Count: 112
  Database Name: LogsDB
  Timestamp: '2022-08-08 08:28:12'
<end>Convert this Json to PLAIN TEXT:
[
    {
        "Company": "HealthPlus",
        "Sector": "Biotech",
        "Stock Price": 981.64,
        "Annual Revenue (B)": 232.54,
        "Quarter": "Q4"
    },
    {
        "Company": "TechCorp",
        "Sector": "Finance",
        "Stock Price": 549.08,
        "Annual Revenue (B)": 334.83,
        "Quarter": "Q1"
    },
    {
        "Company": "RetailHub",
        "Sector": "Finance",
        "Stock Price": 720.97,
        "Annual Revenue (B)": 272.09,
        "Quarter": "Q1"
    },
    {
        "Company": "Foodies",
        "Sector": "Healthcare",
        "Stock Price": 435.64,
        "Annual Revenue (B)": 459.76,
        "Quarter": "Q3"
    },
    {
        "Company": "EcoEnergy",
        "Sector": "Finance",
        "Stock Price": 658.06,
        "Annual Revenue (B)": 87.07,
        "Quarter": "Q3"
    },
    {
        "Company": "RetailHub",
        "Sector": "Automotive",
        "Stock Price": 843.75,
        "Annual Revenue (B)": 473.37,
        "Quarter": "Q2"
    },
    {
        "Company": "HealthPlus",
        "Sector": "Technology",
        "Stock Price": 251.41,
        "Annual Revenue (B)": 333.65,
        "Quarter": "Q3"
    }
]<start>
Company: HealthPlus | Sector: Biotech | Stock Price: 981.64 | Annual Revenue (B): 232.54 | Quarter: Q4
Company: TechCorp | Sector: Finance | Stock Price: 549.08 | Annual Revenue (B): 334.83 | Quarter: Q1
Company: RetailHub | Sector: Finance | Stock Price: 720.97 | Annual Revenue (B): 272.09 | Quarter: Q1
Company: Foodies | Sector: Healthcare | Stock Price: 435.64 | Annual Revenue (B): 459.76 | Quarter: Q3
Company: EcoEnergy | Sector: Finance | Stock Price: 658.06 | Annual Revenue (B): 87.07 | Quarter: Q3
Company: RetailHub | Sector: Automotive | Stock Price: 843.75 | Annual Revenue (B): 473.37 | Quarter: Q2
Company: HealthPlus | Sector: Technology | Stock Price: 251.41 | Annual Revenue (B): 333.65 | Quarter: Q3
<end>Please transform the following YML data into PLAIN TEXT:
- Device ID: device-0071
  Device Type: Motion Detector
  Reading Value: -2.91
- Device ID: device-0001
  Device Type: Humidity Sensor
  Reading Value: -6.59
- Device ID: device-0023
  Device Type: Light Sensor
  Reading Value: 42.64
- Device ID: device-0061
  Device Type: Pressure Sensor
  Reading Value: -22.72
- Device ID: device-0079
  Device Type: Temperature Sensor
  Reading Value: -10.6
<start>
Device ID: device-0071 | Device Type: Motion Detector | Reading Value: -2.91
Device ID: device-0001 | Device Type: Humidity Sensor | Reading Value: -6.59
Device ID: device-0023 | Device Type: Light Sensor | Reading Value: 42.64
Device ID: device-0061 | Device Type: Pressure Sensor | Reading Value: -22.72
Device ID: device-0079 | Device Type: Temperature Sensor | Reading Value: -10.6
<end>Can you change this Csv into JSON?
Name,Age
Athena,56
Bette,26
Bridget,66
Bob,29
Harriett,32
<start>
[
    {
        "Name": "Athena",
        "Age": 56
    },
    {
        "Name": "Bette",
        "Age": 26
    },
    {
        "Name": "Bridget",
        "Age": 66
    },
    {
        "Name": "Bob",
        "Age": 29
    },
    {
        "Name": "Harriett",
        "Age": 32
    }
]
<end>Can you change this PLAIN TEXT into yaml?
Sector: Energy | Market Cap: Mid Cap | Stock Price: 774.09 | Annual Revenue (B): 100.1 | Quarter: Q3
Sector: Retail | Market Cap: Large Cap | Stock Price: 720.31 | Annual Revenue (B): 95.22 | Quarter: Q2
Sector: Finance | Market Cap: Large Cap | Stock Price: 89.1 | Annual Revenue (B): 153.01 | Quarter: Q3
<start>
- Annual Revenue (B): 100.1
  Market Cap: Mid Cap
  Quarter: Q3
  Sector: Energy
  Stock Price: 774.09
- Annual Revenue (B): 95.22
  Market Cap: Large Cap
  Quarter: Q2
  Sector: Retail
  Stock Price: 720.31
- Annual Revenue (B): 153.01
  Market Cap: Large Cap
  Quarter: Q3
  Sector: Finance
  Stock Price: 89.1
<end>Convert this plain text to CSV:
Trip Name: City Explorer | Start Location: Chicago | End Location: New York | Distance (miles): 2660.2 | Duration (hours): 6.0 | Fuel Used (gallons): 66.0
Trip Name: Forest Journey | Start Location: Los Angeles | End Location: Chicago | Distance (miles): 586.8 | Duration (hours): 60.3 | Fuel Used (gallons): 66.6
Trip Name: Valley Voyage | Start Location: Houston | End Location: Chicago | Distance (miles): 2311.7 | Duration (hours): 40.4 | Fuel Used (gallons): 52.1
Trip Name: Highway Odyssey | Start Location: Los Angeles | End Location: Phoenix | Distance (miles): 2401.9 | Duration (hours): 40.1 | Fuel Used (gallons): 9.6
Trip Name: Mountain Adventure | Start Location: New York | End Location: Miami | Distance (miles): 732.9 | Duration (hours): 59.4 | Fuel Used (gallons): 64.0
<start>
Trip Name,Start Location,End Location,Distance (miles),Duration (hours),Fuel Used (gallons)
City Explorer,Chicago,New York,2660.2,6.0,66.0
Forest Journey,Los Angeles,Chicago,586.8,60.3,66.6
Valley Voyage,Houston,Chicago,2311.7,40.4,52.1
Highway Odyssey,Los Angeles,Phoenix,2401.9,40.1,9.6
Mountain Adventure,New York,Miami,732.9,59.4,64.0
<end>Here's some Json data, can you convert it to csv?
[
    {
        "Title": "Beyond the Veil",
        "Director": "Talon Blackthorn",
        "Genre": "Sci-Fi",
        "Release Year": 2013,
        "Box Office Earnings (M)": 748.22
    },
    {
        "Title": "Mystery of the Depths",
        "Director": "Drake Nightshade",
        "Genre": "Adventure",
        "Release Year": 1996,
        "Box Office Earnings (M)": 385.27
    },
    {
        "Title": "The Great Expedition",
        "Director": "Aria Ravenwood",
        "Genre": "Comedy",
        "Release Year": 2013,
        "Box Office Earnings (M)": 551.94
    }
]<start>
Title,Director,Genre,Release Year,Box Office Earnings (M)
Beyond the Veil,Talon Blackthorn,Sci-Fi,2013,748.22
Mystery of the Depths,Drake Nightshade,Adventure,1996,385.27
The Great Expedition,Aria Ravenwood,Comedy,2013,551.94
<end>Please transform the following PLAIN TEXT data into csv:
Trip Name: Lakeside Retreat | End Location: Houston | Distance (miles): 1420.7 | Duration (hours): 53.2 | Fuel Used (gallons): 79.4
Trip Name: Canyon Trek | End Location: Chicago | Distance (miles): 2408.3 | Duration (hours): 28.4 | Fuel Used (gallons): 61.5
Trip Name: Mountain Adventure | End Location: San Francisco | Distance (miles): 1423.5 | Duration (hours): 13.3 | Fuel Used (gallons): 73.9
Trip Name: Highway Odyssey | End Location: Houston | Distance (miles): 1680.8 | Duration (hours): 38.4 | Fuel Used (gallons): 5.6
<start>
Trip Name,End Location,Distance (miles),Duration (hours),Fuel Used (gallons)
Lakeside Retreat,Houston,1420.7,53.2,79.4
Canyon Trek,Chicago,2408.3,28.4,61.5
Mountain Adventure,San Francisco,1423.5,13.3,73.9
Highway Odyssey,Houston,1680.8,38.4,5.6
<end>Can you change this Json into Markdown?
[
    {
        "Location": "Kitchen",
        "Battery Level (%)": 68.5,
        "Timestamp": "2021-11-03 17:35:58"
    },
    {
        "Location": "Hallway",
        "Battery Level (%)": 22.4,
        "Timestamp": "2023-03-04 15:57:41"
    },
    {
        "Location": "Office",
        "Battery Level (%)": 44.4,
        "Timestamp": "2022-05-19 12:13:48"
    },
    {
        "Location": "Hallway",
        "Battery Level (%)": 83.6,
        "Timestamp": "2021-12-27 21:30:44"
    },
    {
        "Location": "Bathroom",
        "Battery Level (%)": 69.0,
        "Timestamp": "2022-11-26 20:18:18"
    },
    {
        "Location": "Hallway",
        "Battery Level (%)": 66.4,
        "Timestamp": "2021-06-21 09:08:46"
    },
    {
        "Location": "Hallway",
        "Battery Level (%)": 81.6,
        "Timestamp": "2021-04-18 02:22:37"
    }
]<start>
| Location | Battery Level (%) | Timestamp |
| --- | --- | --- |
| Kitchen | 68.5 | 2021-11-03 17:35:58 |
| Hallway | 22.4 | 2023-03-04 15:57:41 |
| Office | 44.4 | 2022-05-19 12:13:48 |
| Hallway | 83.6 | 2021-12-27 21:30:44 |
| Bathroom | 69.0 | 2022-11-26 20:18:18 |
| Hallway | 66.4 | 2021-06-21 09:08:46 |
| Hallway | 81.6 | 2021-04-18 02:22:37 |
<end>Transform this markdown structure to a csv format:
| Location | Condition | Temperature (C) | Wind Speed (km/h) |
| --- | --- | --- | --- |
| Denver | Stormy | 35.1 | 23.6 |
| Houston | Rainy | 28.8 | 24.8 |
| Houston | Sunny | 25.1 | 25.0 |<start>
Location,Condition,Temperature (C),Wind Speed (km/h)
Denver,Stormy,35.1,23.6
Houston,Rainy,28.8,24.8
Houston,Sunny,25.1,25.0
<end>Transform this Csv structure to a json format:
Device ID,Device Type,Location,Battery Level (%),Reading Value,Timestamp
device-0079,Pressure Sensor,Hallway,99.3,-10.57,2023-03-12 03:58:32
device-0030,Motion Detector,Garden,16.8,53.52,2021-12-13 00:15:53
device-0015,Motion Detector,Garage,73.3,16.47,2022-04-27 10:25:54
device-0099,Pressure Sensor,Bathroom,16.2,-36.93,2021-05-13 21:18:04
<start>
[
    {
        "Device ID": "device-0079",
        "Device Type": "Pressure Sensor",
        "Location": "Hallway",
        "Battery Level (%)": 99.3,
        "Reading Value": -10.57,
        "Timestamp": "2023-03-12 03:58:32"
    },
    {
        "Device ID": "device-0030",
        "Device Type": "Motion Detector",
        "Location": "Garden",
        "Battery Level (%)": 16.8,
        "Reading Value": 53.52,
        "Timestamp": "2021-12-13 00:15:53"
    },
    {
        "Device ID": "device-0015",
        "Device Type": "Motion Detector",
        "Location": "Garage",
        "Battery Level (%)": 73.3,
        "Reading Value": 16.47,
        "Timestamp": "2022-04-27 10:25:54"
    },
    {
        "Device ID": "device-0099",
        "Device Type": "Pressure Sensor",
        "Location": "Bathroom",
        "Battery Level (%)": 16.2,
        "Reading Value": -36.93,
        "Timestamp": "2021-05-13 21:18:04"
    }
]
<end>