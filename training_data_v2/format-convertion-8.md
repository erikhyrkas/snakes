Transform this markdown structure to a yaml format:
| Condition | Temperature (C) | Humidity (%) |
| --- | --- | --- |
| Cloudy | 18.5 | 94 |
| Windy | -1.2 | 34 |
| Windy | -3.7 | 67 |
| Cloudy | 39.4 | 60 |
| Foggy | 32.4 | 82 |<start>
- Condition: Cloudy
  Humidity (%): 94
  Temperature (C): 18.5
- Condition: Windy
  Humidity (%): 34
  Temperature (C): -1.2
- Condition: Windy
  Humidity (%): 67
  Temperature (C): -3.7
- Condition: Cloudy
  Humidity (%): 60
  Temperature (C): 39.4
- Condition: Foggy
  Humidity (%): 82
  Temperature (C): 32.4
<end>Can you change this YML into MARKDOWN?
- Cuisine: American
  Location: Houston
  Price Range: $$$$
  Rating: 2
- Cuisine: French
  Location: Houston
  Price Range: $$$
  Rating: 4
- Cuisine: Mexican
  Location: Miami
  Price Range: $$
  Rating: 4
- Cuisine: Mexican
  Location: Los Angeles
  Price Range: $$$$
  Rating: 5
- Cuisine: Mexican
  Location: Miami
  Price Range: $$$$
  Rating: 1
- Cuisine: Mexican
  Location: Houston
  Price Range: $$$
  Rating: 3
- Cuisine: French
  Location: Seattle
  Price Range: $$$
  Rating: 5
<start>
| Cuisine | Location | Rating | Price Range |
| --- | --- | --- | --- |
| American | Houston | 2 | $$$$ |
| French | Houston | 4 | $$$ |
| Mexican | Miami | 4 | $$ |
| Mexican | Los Angeles | 5 | $$$$ |
| Mexican | Miami | 1 | $$$$ |
| Mexican | Houston | 3 | $$$ |
| French | Seattle | 5 | $$$ |
<end>Transform this Json structure to a markdown format:
[
    {
        "Device ID": "device-0058",
        "Device Type": "Pressure Sensor",
        "Location": "Hallway",
        "Battery Level (%)": 37.3,
        "Reading Value": -2.14,
        "Timestamp": "2021-05-08 20:17:57"
    },
    {
        "Device ID": "device-0017",
        "Device Type": "Motion Detector",
        "Location": "Garden",
        "Battery Level (%)": 87.4,
        "Reading Value": -8.81,
        "Timestamp": "2022-07-16 22:50:37"
    },
    {
        "Device ID": "device-0056",
        "Device Type": "Temperature Sensor",
        "Location": "Living Room",
        "Battery Level (%)": 11.9,
        "Reading Value": 79.76,
        "Timestamp": "2022-06-19 14:41:54"
    },
    {
        "Device ID": "device-0048",
        "Device Type": "Temperature Sensor",
        "Location": "Garage",
        "Battery Level (%)": 84.8,
        "Reading Value": 81.92,
        "Timestamp": "2023-01-16 17:21:04"
    },
    {
        "Device ID": "device-0041",
        "Device Type": "Pressure Sensor",
        "Location": "Living Room",
        "Battery Level (%)": 58.9,
        "Reading Value": 29.66,
        "Timestamp": "2023-07-13 22:57:05"
    },
    {
        "Device ID": "device-0040",
        "Device Type": "Pressure Sensor",
        "Location": "Office",
        "Battery Level (%)": 61.1,
        "Reading Value": 47.06,
        "Timestamp": "2021-10-01 08:28:01"
    },
    {
        "Device ID": "device-0065",
        "Device Type": "Temperature Sensor",
        "Location": "Bathroom",
        "Battery Level (%)": 41.3,
        "Reading Value": 2.91,
        "Timestamp": "2023-04-09 21:31:39"
    },
    {
        "Device ID": "device-0055",
        "Device Type": "Temperature Sensor",
        "Location": "Bedroom",
        "Battery Level (%)": 95.1,
        "Reading Value": 73.97,
        "Timestamp": "2022-09-13 11:44:57"
    },
    {
        "Device ID": "device-0081",
        "Device Type": "Motion Detector",
        "Location": "Office",
        "Battery Level (%)": 34.3,
        "Reading Value": 29.66,
        "Timestamp": "2022-09-26 07:29:31"
    }
]<start>
| Device ID | Device Type | Location | Battery Level (%) | Reading Value | Timestamp |
| --- | --- | --- | --- | --- | --- |
| device-0058 | Pressure Sensor | Hallway | 37.3 | -2.14 | 2021-05-08 20:17:57 |
| device-0017 | Motion Detector | Garden | 87.4 | -8.81 | 2022-07-16 22:50:37 |
| device-0056 | Temperature Sensor | Living Room | 11.9 | 79.76 | 2022-06-19 14:41:54 |
| device-0048 | Temperature Sensor | Garage | 84.8 | 81.92 | 2023-01-16 17:21:04 |
| device-0041 | Pressure Sensor | Living Room | 58.9 | 29.66 | 2023-07-13 22:57:05 |
| device-0040 | Pressure Sensor | Office | 61.1 | 47.06 | 2021-10-01 08:28:01 |
| device-0065 | Temperature Sensor | Bathroom | 41.3 | 2.91 | 2023-04-09 21:31:39 |
| device-0055 | Temperature Sensor | Bedroom | 95.1 | 73.97 | 2022-09-13 11:44:57 |
| device-0081 | Motion Detector | Office | 34.3 | 29.66 | 2022-09-26 07:29:31 |
<end>Can you change this CSV into markdown?
Database Name,Queries per Second,Cache Hit Ratio (%),Connection Count,Average Latency (ms),Timestamp
MetricsDB,4822.19,88.22,153,95.98,2022-04-21 04:22:12
SalesDB,2387.31,74.1,229,97.53,2023-03-06 10:15:41
LogsDB,463.79,90.82,100,20.51,2022-05-18 07:23:19
<start>
| Database Name | Queries per Second | Cache Hit Ratio (%) | Connection Count | Average Latency (ms) | Timestamp |
| --- | --- | --- | --- | --- | --- |
| MetricsDB | 4822.19 | 88.22 | 153 | 95.98 | 2022-04-21 04:22:12 |
| SalesDB | 2387.31 | 74.1 | 229 | 97.53 | 2023-03-06 10:15:41 |
| LogsDB | 463.79 | 90.82 | 100 | 20.51 | 2022-05-18 07:23:19 |
<end>Transform this YML structure to a Markdown format:
- Company: FinanceTrust
  Date: '2022-02-20'
  Low Price: 306.09
  Open Price: 1165.55
  Volume: 9175510
- Company: GreenEnergy
  Date: '2021-12-16'
  Low Price: 449.48
  Open Price: 695.33
  Volume: 8212028
- Company: RetailWorld
  Date: '2021-12-16'
  Low Price: 430.0
  Open Price: 449.48
  Volume: 3038157
<start>
| Company | Date | Open Price | Low Price | Volume |
| --- | --- | --- | --- | --- |
| FinanceTrust | 2022-02-20 | 1165.55 | 306.09 | 9175510 |
| GreenEnergy | 2021-12-16 | 695.33 | 449.48 | 8212028 |
| RetailWorld | 2021-12-16 | 449.48 | 430.0 | 3038157 |
<end>Convert this Markdown to csv:
| Price | Category | Supplier Name |
| --- | --- | --- |
| 455.56 | Toys | ACME Corp |
| 496.43 | Automotive | Globex |
| 25.18 | Toys | Globex |
| 159.08 | Toys | Wonka Industries |<start>
Price,Category,Supplier Name
455.56,Toys,ACME Corp
496.43,Automotive,Globex
25.18,Toys,Globex
159.08,Toys,Wonka Industries
<end>Here's some markdown data, can you convert it to yaml?
| Restaurant Name | Cuisine | Location | Rating | Price Range |
| --- | --- | --- | --- | --- |
| Curry Corner | Mediterranean | San Francisco | 2 | $$$$ |
| BBQ Barn | Mediterranean | Seattle | 1 | $$$$$ |
| The Golden Spoon | Indian | Houston | 2 | $$$$$ |
| BBQ Barn | Chinese | Miami | 5 | $$ |
| Taco Town | Mexican | Phoenix | 5 | $$ |
| BBQ Barn | Italian | San Francisco | 3 | $ |
| Sushi World | French | San Francisco | 2 | $ |<start>
- Cuisine: Mediterranean
  Location: San Francisco
  Price Range: $$$$
  Rating: 2
  Restaurant Name: Curry Corner
- Cuisine: Mediterranean
  Location: Seattle
  Price Range: $$$$$
  Rating: 1
  Restaurant Name: BBQ Barn
- Cuisine: Indian
  Location: Houston
  Price Range: $$$$$
  Rating: 2
  Restaurant Name: The Golden Spoon
- Cuisine: Chinese
  Location: Miami
  Price Range: $$
  Rating: 5
  Restaurant Name: BBQ Barn
- Cuisine: Mexican
  Location: Phoenix
  Price Range: $$
  Rating: 5
  Restaurant Name: Taco Town
- Cuisine: Italian
  Location: San Francisco
  Price Range: $
  Rating: 3
  Restaurant Name: BBQ Barn
- Cuisine: French
  Location: San Francisco
  Price Range: $
  Rating: 2
  Restaurant Name: Sushi World
<end>Transform this Yml structure to a json format:
- Category: Automotive
  SKU: SKU-1077
  Supplier Name: Umbrella Corp
- Category: Automotive
  SKU: SKU-1043
  Supplier Name: Wayne Enterprises
- Category: Household
  SKU: SKU-1009
  Supplier Name: Wayne Enterprises
<start>
[
    {
        "SKU": "SKU-1077",
        "Category": "Automotive",
        "Supplier Name": "Umbrella Corp"
    },
    {
        "SKU": "SKU-1043",
        "Category": "Automotive",
        "Supplier Name": "Wayne Enterprises"
    },
    {
        "SKU": "SKU-1009",
        "Category": "Household",
        "Supplier Name": "Wayne Enterprises"
    }
]
<end>Transform this markdown structure to a CSV format:
| Database Name | Cache Hit Ratio (%) | Average Latency (ms) | Timestamp |
| --- | --- | --- | --- |
| AnalyticsDB | 93.32 | 98.36 | 2023-09-25 15:54:58 |
| UserDB | 98.46 | 23.03 | 2021-07-04 11:42:34 |
| AnalyticsDB | 73.51 | 8.6 | 2021-09-01 12:43:55 |<start>
Database Name,Cache Hit Ratio (%),Average Latency (ms),Timestamp
AnalyticsDB,93.32,98.36,2023-09-25 15:54:58
UserDB,98.46,23.03,2021-07-04 11:42:34
AnalyticsDB,73.51,8.6,2021-09-01 12:43:55
<end>Please transform the following plain text data into Json:
Location: Seattle | Temperature (C): -7.1 | Humidity (%): 95 | Day: Thursday
Location: Phoenix | Temperature (C): 12.0 | Humidity (%): 80 | Day: Monday
Location: Phoenix | Temperature (C): 9.9 | Humidity (%): 21 | Day: Sunday
<start>
[
    {
        "Location": "Seattle",
        "Temperature (C)": -7.1,
        "Humidity (%)": 95,
        "Day": "Thursday"
    },
    {
        "Location": "Phoenix",
        "Temperature (C)": 12.0,
        "Humidity (%)": 80,
        "Day": "Monday"
    },
    {
        "Location": "Phoenix",
        "Temperature (C)": 9.9,
        "Humidity (%)": 21,
        "Day": "Sunday"
    }
]
<end>Convert this YML to JSON:
- Battery Level (%): 83.3
  Device ID: device-0068
  Device Type: Temperature Sensor
  Location: Garage
  Reading Value: -6.18
  Timestamp: '2022-02-12 02:08:45'
- Battery Level (%): 21.1
  Device ID: device-0066
  Device Type: Light Sensor
  Location: Bedroom
  Reading Value: 45.04
  Timestamp: '2021-09-11 07:38:18'
- Battery Level (%): 57.4
  Device ID: device-0095
  Device Type: Light Sensor
  Location: Garage
  Reading Value: 44.4
  Timestamp: '2022-02-06 16:38:29'
- Battery Level (%): 49.4
  Device ID: device-0088
  Device Type: Humidity Sensor
  Location: Office
  Reading Value: -26.63
  Timestamp: '2023-08-17 12:05:48'
- Battery Level (%): 78.5
  Device ID: device-0075
  Device Type: Motion Detector
  Location: Office
  Reading Value: 34.95
  Timestamp: '2021-12-01 17:10:40'
- Battery Level (%): 61.9
  Device ID: device-0087
  Device Type: Motion Detector
  Location: Office
  Reading Value: -29.34
  Timestamp: '2021-11-16 09:13:35'
- Battery Level (%): 49.5
  Device ID: device-0011
  Device Type: Temperature Sensor
  Location: Garden
  Reading Value: -26.63
  Timestamp: '2023-09-17 22:56:28'
- Battery Level (%): 92.7
  Device ID: device-0049
  Device Type: Humidity Sensor
  Location: Garden
  Reading Value: -16.58
  Timestamp: '2023-11-14 14:09:36'
<start>
[
    {
        "Device ID": "device-0068",
        "Device Type": "Temperature Sensor",
        "Location": "Garage",
        "Battery Level (%)": 83.3,
        "Reading Value": -6.18,
        "Timestamp": "2022-02-12 02:08:45"
    },
    {
        "Device ID": "device-0066",
        "Device Type": "Light Sensor",
        "Location": "Bedroom",
        "Battery Level (%)": 21.1,
        "Reading Value": 45.04,
        "Timestamp": "2021-09-11 07:38:18"
    },
    {
        "Device ID": "device-0095",
        "Device Type": "Light Sensor",
        "Location": "Garage",
        "Battery Level (%)": 57.4,
        "Reading Value": 44.4,
        "Timestamp": "2022-02-06 16:38:29"
    },
    {
        "Device ID": "device-0088",
        "Device Type": "Humidity Sensor",
        "Location": "Office",
        "Battery Level (%)": 49.4,
        "Reading Value": -26.63,
        "Timestamp": "2023-08-17 12:05:48"
    },
    {
        "Device ID": "device-0075",
        "Device Type": "Motion Detector",
        "Location": "Office",
        "Battery Level (%)": 78.5,
        "Reading Value": 34.95,
        "Timestamp": "2021-12-01 17:10:40"
    },
    {
        "Device ID": "device-0087",
        "Device Type": "Motion Detector",
        "Location": "Office",
        "Battery Level (%)": 61.9,
        "Reading Value": -29.34,
        "Timestamp": "2021-11-16 09:13:35"
    },
    {
        "Device ID": "device-0011",
        "Device Type": "Temperature Sensor",
        "Location": "Garden",
        "Battery Level (%)": 49.5,
        "Reading Value": -26.63,
        "Timestamp": "2023-09-17 22:56:28"
    },
    {
        "Device ID": "device-0049",
        "Device Type": "Humidity Sensor",
        "Location": "Garden",
        "Battery Level (%)": 92.7,
        "Reading Value": -16.58,
        "Timestamp": "2023-11-14 14:09:36"
    }
]
<end>Can you change this Csv into json?
Title,Director,Genre,Release Year,Box Office Earnings (M)
Starbound Odyssey,Drake Nightshade,Drama,2019,49.53
Edge of Infinity,Drake Nightshade,Horror,2017,14.36
The Great Expedition,Cade Firebrand,Drama,1991,905.87
<start>
[
    {
        "Title": "Starbound Odyssey",
        "Director": "Drake Nightshade",
        "Genre": "Drama",
        "Release Year": 2019,
        "Box Office Earnings (M)": 49.53
    },
    {
        "Title": "Edge of Infinity",
        "Director": "Drake Nightshade",
        "Genre": "Horror",
        "Release Year": 2017,
        "Box Office Earnings (M)": 14.36
    },
    {
        "Title": "The Great Expedition",
        "Director": "Cade Firebrand",
        "Genre": "Drama",
        "Release Year": 1991,
        "Box Office Earnings (M)": 905.87
    }
]
<end>Can you change this plain text into json?
Device ID: device-0068 | Device Type: Pressure Sensor | Battery Level (%): 17.6 | Reading Value: 10.37 | Timestamp: 2021-06-05 19:44:34
Device ID: device-0083 | Device Type: Light Sensor | Battery Level (%): 78.2 | Reading Value: 10.8 | Timestamp: 2021-03-25 02:39:32
Device ID: device-0007 | Device Type: Pressure Sensor | Battery Level (%): 87.1 | Reading Value: 38.71 | Timestamp: 2021-03-14 07:43:09
Device ID: device-0087 | Device Type: Pressure Sensor | Battery Level (%): 55.8 | Reading Value: 14.89 | Timestamp: 2021-09-20 10:17:31
Device ID: device-0019 | Device Type: Humidity Sensor | Battery Level (%): 85.2 | Reading Value: -0.56 | Timestamp: 2022-12-13 10:22:53
Device ID: device-0017 | Device Type: Pressure Sensor | Battery Level (%): 19.0 | Reading Value: 30.92 | Timestamp: 2021-04-28 08:44:38
Device ID: device-0011 | Device Type: Motion Detector | Battery Level (%): 68.0 | Reading Value: -12.72 | Timestamp: 2022-11-25 22:08:39
Device ID: device-0010 | Device Type: Humidity Sensor | Battery Level (%): 25.4 | Reading Value: 72.0 | Timestamp: 2022-10-28 08:54:17
<start>
[
    {
        "Device ID": "device-0068",
        "Device Type": "Pressure Sensor",
        "Battery Level (%)": 17.6,
        "Reading Value": 10.37,
        "Timestamp": "2021-06-05 19:44:34"
    },
    {
        "Device ID": "device-0083",
        "Device Type": "Light Sensor",
        "Battery Level (%)": 78.2,
        "Reading Value": 10.8,
        "Timestamp": "2021-03-25 02:39:32"
    },
    {
        "Device ID": "device-0007",
        "Device Type": "Pressure Sensor",
        "Battery Level (%)": 87.1,
        "Reading Value": 38.71,
        "Timestamp": "2021-03-14 07:43:09"
    },
    {
        "Device ID": "device-0087",
        "Device Type": "Pressure Sensor",
        "Battery Level (%)": 55.8,
        "Reading Value": 14.89,
        "Timestamp": "2021-09-20 10:17:31"
    },
    {
        "Device ID": "device-0019",
        "Device Type": "Humidity Sensor",
        "Battery Level (%)": 85.2,
        "Reading Value": -0.56,
        "Timestamp": "2022-12-13 10:22:53"
    },
    {
        "Device ID": "device-0017",
        "Device Type": "Pressure Sensor",
        "Battery Level (%)": 19.0,
        "Reading Value": 30.92,
        "Timestamp": "2021-04-28 08:44:38"
    },
    {
        "Device ID": "device-0011",
        "Device Type": "Motion Detector",
        "Battery Level (%)": 68.0,
        "Reading Value": -12.72,
        "Timestamp": "2022-11-25 22:08:39"
    },
    {
        "Device ID": "device-0010",
        "Device Type": "Humidity Sensor",
        "Battery Level (%)": 25.4,
        "Reading Value": 72.0,
        "Timestamp": "2022-10-28 08:54:17"
    }
]
<end>Please transform the following markdown data into JSON:
| Condition | Temperature (C) | Wind Speed (km/h) |
| --- | --- | --- |
| Foggy | -1.0 | 29.1 |
| Rainy | 31.8 | 22.5 |
| Foggy | -5.9 | 7.0 |<start>
[
    {
        "Condition": "Foggy",
        "Temperature (C)": -1.0,
        "Wind Speed (km/h)": 29.1
    },
    {
        "Condition": "Rainy",
        "Temperature (C)": 31.8,
        "Wind Speed (km/h)": 22.5
    },
    {
        "Condition": "Foggy",
        "Temperature (C)": -5.9,
        "Wind Speed (km/h)": 7.0
    }
]
<end>Here's some markdown data, can you convert it to json?
| Title | Author | Genre | Publication Year | Rating |
| --- | --- | --- | --- | --- |
| A Journey Through Time | Isla Windrider | Non-Fiction | 1958 | 2.3 |
| The Last Sky | Luna Silverleaf | Mystery | 2009 | 3.8 |
| Echoes of Eternity | Rowan Ashborne | Horror | 1984 | 1.4 |
| The Silent Grove | Sylvia Nightshade | Thriller | 2006 | 3.4 |
| Legends of the Rift | Luna Silverleaf | Non-Fiction | 2002 | 4.1 |<start>
[
    {
        "Title": "A Journey Through Time",
        "Author": "Isla Windrider",
        "Genre": "Non-Fiction",
        "Publication Year": 1958,
        "Rating": 2.3
    },
    {
        "Title": "The Last Sky",
        "Author": "Luna Silverleaf",
        "Genre": "Mystery",
        "Publication Year": 2009,
        "Rating": 3.8
    },
    {
        "Title": "Echoes of Eternity",
        "Author": "Rowan Ashborne",
        "Genre": "Horror",
        "Publication Year": 1984,
        "Rating": 1.4
    },
    {
        "Title": "The Silent Grove",
        "Author": "Sylvia Nightshade",
        "Genre": "Thriller",
        "Publication Year": 2006,
        "Rating": 3.4
    },
    {
        "Title": "Legends of the Rift",
        "Author": "Luna Silverleaf",
        "Genre": "Non-Fiction",
        "Publication Year": 2002,
        "Rating": 4.1
    }
]
<end>Can you change this markdown into PLAIN TEXT?
| Restaurant Name | Cuisine | Location |
| --- | --- | --- |
| The Golden Spoon | French | Phoenix |
| The Steakhouse | French | Miami |
| Curry Corner | Chinese | Los Angeles |
| BBQ Barn | Mexican | San Francisco |
| The Steakhouse | Mediterranean | Los Angeles |
| Curry Corner | Mediterranean | Seattle |
| The Steakhouse | Italian | Miami |
| Taco Town | French | Chicago |<start>
Restaurant Name: The Golden Spoon | Cuisine: French | Location: Phoenix
Restaurant Name: The Steakhouse | Cuisine: French | Location: Miami
Restaurant Name: Curry Corner | Cuisine: Chinese | Location: Los Angeles
Restaurant Name: BBQ Barn | Cuisine: Mexican | Location: San Francisco
Restaurant Name: The Steakhouse | Cuisine: Mediterranean | Location: Los Angeles
Restaurant Name: Curry Corner | Cuisine: Mediterranean | Location: Seattle
Restaurant Name: The Steakhouse | Cuisine: Italian | Location: Miami
Restaurant Name: Taco Town | Cuisine: French | Location: Chicago
<end>Can you change this yml into MARKDOWN?
- Box Office Earnings (M): 222.59
  Director: Lira Silverleaf
  Genre: Adventure
  Release Year: 2009
- Box Office Earnings (M): 568.82
  Director: Cade Firebrand
  Genre: Sci-Fi
  Release Year: 2007
- Box Office Earnings (M): 708.4
  Director: Aria Ravenwood
  Genre: Thriller
  Release Year: 1976
- Box Office Earnings (M): 876.51
  Director: Aria Ravenwood
  Genre: Fantasy
  Release Year: 1984
- Box Office Earnings (M): 708.4
  Director: Rylan Frostblade
  Genre: Adventure
  Release Year: 2006
<start>
| Director | Genre | Release Year | Box Office Earnings (M) |
| --- | --- | --- | --- |
| Lira Silverleaf | Adventure | 2009 | 222.59 |
| Cade Firebrand | Sci-Fi | 2007 | 568.82 |
| Aria Ravenwood | Thriller | 1976 | 708.4 |
| Aria Ravenwood | Fantasy | 1984 | 876.51 |
| Rylan Frostblade | Adventure | 2006 | 708.4 |
<end>Can you change this json into MARKDOWN?
[
    {
        "Director": "Talon Blackthorn",
        "Genre": "Comedy"
    },
    {
        "Director": "Mara Moonshadow",
        "Genre": "Comedy"
    },
    {
        "Director": "Selene Darkwhisper",
        "Genre": "Comedy"
    },
    {
        "Director": "Aria Ravenwood",
        "Genre": "Drama"
    },
    {
        "Director": "Aria Ravenwood",
        "Genre": "Action"
    },
    {
        "Director": "Aria Ravenwood",
        "Genre": "Action"
    },
    {
        "Director": "Lira Silverleaf",
        "Genre": "Comedy"
    },
    {
        "Director": "Zara Stormrider",
        "Genre": "Horror"
    },
    {
        "Director": "Lira Silverleaf",
        "Genre": "Comedy"
    }
]<start>
| Director | Genre |
| --- | --- |
| Talon Blackthorn | Comedy |
| Mara Moonshadow | Comedy |
| Selene Darkwhisper | Comedy |
| Aria Ravenwood | Drama |
| Aria Ravenwood | Action |
| Aria Ravenwood | Action |
| Lira Silverleaf | Comedy |
| Zara Stormrider | Horror |
| Lira Silverleaf | Comedy |
<end>Please transform the following Csv data into Markdown:
Device Type,Location,Reading Value,Timestamp
Motion Detector,Living Room,23.3,2022-06-13 10:59:58
Temperature Sensor,Bedroom,57.25,2023-11-17 15:07:42
Humidity Sensor,Garage,44.34,2021-12-07 01:24:07
Temperature Sensor,Bedroom,-17.25,2021-06-11 23:56:30
Temperature Sensor,Bathroom,79.8,2023-04-21 08:18:33
Humidity Sensor,Bedroom,45.65,2022-11-21 22:22:33
Motion Detector,Garage,45.65,2022-05-12 15:54:52
Pressure Sensor,Garden,57.25,2021-09-16 20:53:40
Temperature Sensor,Bedroom,-25.18,2023-04-08 14:18:16
Motion Detector,Bedroom,23.72,2021-04-10 10:07:58
<start>
| Device Type | Location | Reading Value | Timestamp |
| --- | --- | --- | --- |
| Motion Detector | Living Room | 23.3 | 2022-06-13 10:59:58 |
| Temperature Sensor | Bedroom | 57.25 | 2023-11-17 15:07:42 |
| Humidity Sensor | Garage | 44.34 | 2021-12-07 01:24:07 |
| Temperature Sensor | Bedroom | -17.25 | 2021-06-11 23:56:30 |
| Temperature Sensor | Bathroom | 79.8 | 2023-04-21 08:18:33 |
| Humidity Sensor | Bedroom | 45.65 | 2022-11-21 22:22:33 |
| Motion Detector | Garage | 45.65 | 2022-05-12 15:54:52 |
| Pressure Sensor | Garden | 57.25 | 2021-09-16 20:53:40 |
| Temperature Sensor | Bedroom | -25.18 | 2023-04-08 14:18:16 |
| Motion Detector | Bedroom | 23.72 | 2021-04-10 10:07:58 |
<end>Can you change this yml into Markdown?
- Category: Automotive
  Product Name: Thingamajig
  SKU: SKU-1015
  Supplier Name: Wonka Industries
- Category: Electronics
  Product Name: Device
  SKU: SKU-1047
  Supplier Name: Globex
- Category: Toys
  Product Name: Instrument
  SKU: SKU-1098
  Supplier Name: Umbrella Corp
<start>
| Product Name | SKU | Category | Supplier Name |
| --- | --- | --- | --- |
| Thingamajig | SKU-1015 | Automotive | Wonka Industries |
| Device | SKU-1047 | Electronics | Globex |
| Instrument | SKU-1098 | Toys | Umbrella Corp |
<end>Transform this json structure to a yml format:
[
    {
        "Trip Name": "Canyon Trek",
        "Distance (miles)": 1688.8,
        "Duration (hours)": 67.4,
        "Fuel Used (gallons)": 39.8
    },
    {
        "Trip Name": "Lakeside Retreat",
        "Distance (miles)": 2526.1,
        "Duration (hours)": 24.0,
        "Fuel Used (gallons)": 36.4
    },
    {
        "Trip Name": "Desert Drive",
        "Distance (miles)": 690.2,
        "Duration (hours)": 4.9,
        "Fuel Used (gallons)": 81.4
    },
    {
        "Trip Name": "Mountain Adventure",
        "Distance (miles)": 1239.9,
        "Duration (hours)": 71.0,
        "Fuel Used (gallons)": 71.7
    },
    {
        "Trip Name": "Historic Route",
        "Distance (miles)": 480.1,
        "Duration (hours)": 17.3,
        "Fuel Used (gallons)": 25.4
    }
]<start>
- Distance (miles): 1688.8
  Duration (hours): 67.4
  Fuel Used (gallons): 39.8
  Trip Name: Canyon Trek
- Distance (miles): 2526.1
  Duration (hours): 24.0
  Fuel Used (gallons): 36.4
  Trip Name: Lakeside Retreat
- Distance (miles): 690.2
  Duration (hours): 4.9
  Fuel Used (gallons): 81.4
  Trip Name: Desert Drive
- Distance (miles): 1239.9
  Duration (hours): 71.0
  Fuel Used (gallons): 71.7
  Trip Name: Mountain Adventure
- Distance (miles): 480.1
  Duration (hours): 17.3
  Fuel Used (gallons): 25.4
  Trip Name: Historic Route
<end>Transform this Csv structure to a Json format:
Author,Rating
Orion Frostblade,1.5
Sylvia Nightshade,2.3
Thorne Ironwood,1.8
Luna Silverleaf,4.3
Sylvia Nightshade,2.4
Isla Windrider,2.8
Sylvia Nightshade,2.7
Elara Moonshadow,4.6
<start>
[
    {
        "Author": "Orion Frostblade",
        "Rating": 1.5
    },
    {
        "Author": "Sylvia Nightshade",
        "Rating": 2.3
    },
    {
        "Author": "Thorne Ironwood",
        "Rating": 1.8
    },
    {
        "Author": "Luna Silverleaf",
        "Rating": 4.3
    },
    {
        "Author": "Sylvia Nightshade",
        "Rating": 2.4
    },
    {
        "Author": "Isla Windrider",
        "Rating": 2.8
    },
    {
        "Author": "Sylvia Nightshade",
        "Rating": 2.7
    },
    {
        "Author": "Elara Moonshadow",
        "Rating": 4.6
    }
]
<end>Transform this CSV structure to a Markdown format:
Location,Temperature (C),Humidity (%),Wind Speed (km/h),Day
Seattle,33.2,61,11.5,Wednesday
Denver,33.1,64,9.7,Monday
Seattle,14.9,32,27.7,Saturday
Chicago,29.0,95,4.0,Thursday
Phoenix,12.4,61,22.9,Wednesday
Denver,17.3,31,1.7,Monday
Houston,-6.1,41,14.7,Sunday
Seattle,15.1,49,16.4,Saturday
<start>
| Location | Temperature (C) | Humidity (%) | Wind Speed (km/h) | Day |
| --- | --- | --- | --- | --- |
| Seattle | 33.2 | 61 | 11.5 | Wednesday |
| Denver | 33.1 | 64 | 9.7 | Monday |
| Seattle | 14.9 | 32 | 27.7 | Saturday |
| Chicago | 29.0 | 95 | 4.0 | Thursday |
| Phoenix | 12.4 | 61 | 22.9 | Wednesday |
| Denver | 17.3 | 31 | 1.7 | Monday |
| Houston | -6.1 | 41 | 14.7 | Sunday |
| Seattle | 15.1 | 49 | 16.4 | Saturday |
<end>Can you change this PLAIN TEXT into MARKDOWN?
Device ID: device-0058 | Location: Garden | Timestamp: 2023-06-02 00:40:57
Device ID: device-0078 | Location: Garden | Timestamp: 2023-07-28 06:19:32
Device ID: device-0037 | Location: Kitchen | Timestamp: 2022-09-06 21:59:02
Device ID: device-0002 | Location: Kitchen | Timestamp: 2021-12-07 14:27:42
<start>
| Device ID | Location | Timestamp |
| --- | --- | --- |
| device-0058 | Garden | 2023-06-02 00:40:57 |
| device-0078 | Garden | 2023-07-28 06:19:32 |
| device-0037 | Kitchen | 2022-09-06 21:59:02 |
| device-0002 | Kitchen | 2021-12-07 14:27:42 |
<end>Convert this plain text to json:
Age: 58 | Birth Month: March | Income: 445000
Age: 20 | Birth Month: March | Income: 30000
Age: 63 | Birth Month: October | Income: 495000
Age: 29 | Birth Month: October | Income: 185000
Age: 51 | Birth Month: June | Income: 260000
Age: 55 | Birth Month: October | Income: 155000
<start>
[
    {
        "Age": 58,
        "Birth Month": "March",
        "Income": 445000
    },
    {
        "Age": 20,
        "Birth Month": "March",
        "Income": 30000
    },
    {
        "Age": 63,
        "Birth Month": "October",
        "Income": 495000
    },
    {
        "Age": 29,
        "Birth Month": "October",
        "Income": 185000
    },
    {
        "Age": 51,
        "Birth Month": "June",
        "Income": 260000
    },
    {
        "Age": 55,
        "Birth Month": "October",
        "Income": 155000
    }
]
<end>Transform this PLAIN TEXT structure to a json format:
Company: GlobalTrade | Sector: Automotive | Market Cap: Small Cap | Stock Price: 186.26 | Annual Revenue (B): 79.92 | Quarter: Q2
Company: BioPharm | Sector: Retail | Market Cap: Large Cap | Stock Price: 452.71 | Annual Revenue (B): 280.7 | Quarter: Q3
Company: EcoEnergy | Sector: Aerospace | Market Cap: Mid Cap | Stock Price: 422.63 | Annual Revenue (B): 296.6 | Quarter: Q3
Company: TechCorp | Sector: Biotech | Market Cap: Small Cap | Stock Price: 317.62 | Annual Revenue (B): 109.47 | Quarter: Q3
Company: Foodies | Sector: Healthcare | Market Cap: Small Cap | Stock Price: 452.71 | Annual Revenue (B): 109.47 | Quarter: Q1
Company: AutoDrive | Sector: Finance | Market Cap: Mid Cap | Stock Price: 658.4 | Annual Revenue (B): 191.53 | Quarter: Q2
Company: RetailHub | Sector: Technology | Market Cap: Mega Cap | Stock Price: 901.05 | Annual Revenue (B): 130.53 | Quarter: Q1
<start>
[
    {
        "Company": "GlobalTrade",
        "Sector": "Automotive",
        "Market Cap": "Small Cap",
        "Stock Price": 186.26,
        "Annual Revenue (B)": 79.92,
        "Quarter": "Q2"
    },
    {
        "Company": "BioPharm",
        "Sector": "Retail",
        "Market Cap": "Large Cap",
        "Stock Price": 452.71,
        "Annual Revenue (B)": 280.7,
        "Quarter": "Q3"
    },
    {
        "Company": "EcoEnergy",
        "Sector": "Aerospace",
        "Market Cap": "Mid Cap",
        "Stock Price": 422.63,
        "Annual Revenue (B)": 296.6,
        "Quarter": "Q3"
    },
    {
        "Company": "TechCorp",
        "Sector": "Biotech",
        "Market Cap": "Small Cap",
        "Stock Price": 317.62,
        "Annual Revenue (B)": 109.47,
        "Quarter": "Q3"
    },
    {
        "Company": "Foodies",
        "Sector": "Healthcare",
        "Market Cap": "Small Cap",
        "Stock Price": 452.71,
        "Annual Revenue (B)": 109.47,
        "Quarter": "Q1"
    },
    {
        "Company": "AutoDrive",
        "Sector": "Finance",
        "Market Cap": "Mid Cap",
        "Stock Price": 658.4,
        "Annual Revenue (B)": 191.53,
        "Quarter": "Q2"
    },
    {
        "Company": "RetailHub",
        "Sector": "Technology",
        "Market Cap": "Mega Cap",
        "Stock Price": 901.05,
        "Annual Revenue (B)": 130.53,
        "Quarter": "Q1"
    }
]
<end>Here's some CSV data, can you convert it to yml?
Queries per Second,Connection Count,Average Latency (ms),Timestamp
3603.23,200,53.9,2023-02-18 05:39:22
4652.77,112,85.12,2021-11-07 00:05:38
3678.35,346,62.94,2021-08-08 19:47:00
<start>
- Average Latency (ms): 53.9
  Connection Count: 200
  Queries per Second: 3603.23
  Timestamp: '2023-02-18 05:39:22'
- Average Latency (ms): 85.12
  Connection Count: 112
  Queries per Second: 4652.77
  Timestamp: '2021-11-07 00:05:38'
- Average Latency (ms): 62.94
  Connection Count: 346
  Queries per Second: 3678.35
  Timestamp: '2021-08-08 19:47:00'
<end>Transform this Yaml structure to a JSON format:
- Distance (miles): 518.2
  Duration (hours): 24.8
  End Location: Denver
  Start Location: Miami
- Distance (miles): 2083.0
  Duration (hours): 57.6
  End Location: Miami
  Start Location: Chicago
- Distance (miles): 1136.7
  Duration (hours): 10.8
  End Location: Phoenix
  Start Location: Houston
- Distance (miles): 1810.9
  Duration (hours): 4.5
  End Location: Houston
  Start Location: Denver
<start>
[
    {
        "Start Location": "Miami",
        "End Location": "Denver",
        "Distance (miles)": 518.2,
        "Duration (hours)": 24.8
    },
    {
        "Start Location": "Chicago",
        "End Location": "Miami",
        "Distance (miles)": 2083.0,
        "Duration (hours)": 57.6
    },
    {
        "Start Location": "Houston",
        "End Location": "Phoenix",
        "Distance (miles)": 1136.7,
        "Duration (hours)": 10.8
    },
    {
        "Start Location": "Denver",
        "End Location": "Houston",
        "Distance (miles)": 1810.9,
        "Duration (hours)": 4.5
    }
]
<end>Convert this YAML to CSV:
- Director: Rylan Frostblade
  Genre: Horror
  Title: Escape from Earth
- Director: Orin Shadowalker
  Genre: Fantasy
  Title: Mystery of the Depths
- Director: Mara Moonshadow
  Genre: Adventure
  Title: Beyond the Veil
<start>
Title,Director,Genre
Escape from Earth,Rylan Frostblade,Horror
Mystery of the Depths,Orin Shadowalker,Fantasy
Beyond the Veil,Mara Moonshadow,Adventure
<end>Please transform the following Yml data into Json:
- Battery Level (%): 85.3
  Location: Bedroom
  Reading Value: 42.35
- Battery Level (%): 36.6
  Location: Garden
  Reading Value: 68.57
- Battery Level (%): 63.5
  Location: Hallway
  Reading Value: 47.95
- Battery Level (%): 57.7
  Location: Kitchen
  Reading Value: -15.91
- Battery Level (%): 55.4
  Location: Living Room
  Reading Value: -10.95
<start>
[
    {
        "Location": "Bedroom",
        "Battery Level (%)": 85.3,
        "Reading Value": 42.35
    },
    {
        "Location": "Garden",
        "Battery Level (%)": 36.6,
        "Reading Value": 68.57
    },
    {
        "Location": "Hallway",
        "Battery Level (%)": 63.5,
        "Reading Value": 47.95
    },
    {
        "Location": "Kitchen",
        "Battery Level (%)": 57.7,
        "Reading Value": -15.91
    },
    {
        "Location": "Living Room",
        "Battery Level (%)": 55.4,
        "Reading Value": -10.95
    }
]
<end>Convert this Plain text to CSV:
Device Type: Pressure Sensor | Location: Garage | Battery Level (%): 20.8 | Reading Value: -13.52 | Timestamp: 2022-12-17 00:00:38
Device Type: Light Sensor | Location: Living Room | Battery Level (%): 48.1 | Reading Value: 70.44 | Timestamp: 2023-08-06 10:41:28
Device Type: Motion Detector | Location: Garage | Battery Level (%): 69.1 | Reading Value: 59.63 | Timestamp: 2021-09-26 17:19:17
Device Type: Temperature Sensor | Location: Living Room | Battery Level (%): 86.5 | Reading Value: 81.82 | Timestamp: 2022-01-04 00:54:27
Device Type: Light Sensor | Location: Garden | Battery Level (%): 69.9 | Reading Value: -25.62 | Timestamp: 2023-03-06 09:28:21
<start>
Device Type,Location,Battery Level (%),Reading Value,Timestamp
Pressure Sensor,Garage,20.8,-13.52,2022-12-17 00:00:38
Light Sensor,Living Room,48.1,70.44,2023-08-06 10:41:28
Motion Detector,Garage,69.1,59.63,2021-09-26 17:19:17
Temperature Sensor,Living Room,86.5,81.82,2022-01-04 00:54:27
Light Sensor,Garden,69.9,-25.62,2023-03-06 09:28:21
<end>Please transform the following Markdown data into csv:
| Author | Genre | Rating |
| --- | --- | --- |
| Elara Moonshadow | Science Fiction | 3.8 |
| Elara Moonshadow | Science Fiction | 3.0 |
| Luna Silverleaf | Horror | 1.3 |
| Galen Starfire | Science Fiction | 3.0 |<start>
Author,Genre,Rating
Elara Moonshadow,Science Fiction,3.8
Elara Moonshadow,Science Fiction,3.0
Luna Silverleaf,Horror,1.3
Galen Starfire,Science Fiction,3.0
<end>Can you change this PLAIN TEXT into MARKDOWN?
Name: Trinity | Age: 21
Name: Damian | Age: 22
Name: Hugh | Age: 40
<start>
| Name | Age |
| --- | --- |
| Trinity | 21 |
| Damian | 22 |
| Hugh | 40 |
<end>Here's some markdown data, can you convert it to Json?
| Author | Genre | Publication Year | Rating |
| --- | --- | --- | --- |
| Luna Silverleaf | Horror | 2018 | 3.2 |
| Draven Blackthorn | Horror | 2021 | 3.6 |
| Elara Moonshadow | Horror | 1970 | 2.3 |
| Isla Windrider | Fantasy | 1978 | 4.8 |
| Rowan Ashborne | Fantasy | 1986 | 1.7 |<start>
[
    {
        "Author": "Luna Silverleaf",
        "Genre": "Horror",
        "Publication Year": 2018,
        "Rating": 3.2
    },
    {
        "Author": "Draven Blackthorn",
        "Genre": "Horror",
        "Publication Year": 2021,
        "Rating": 3.6
    },
    {
        "Author": "Elara Moonshadow",
        "Genre": "Horror",
        "Publication Year": 1970,
        "Rating": 2.3
    },
    {
        "Author": "Isla Windrider",
        "Genre": "Fantasy",
        "Publication Year": 1978,
        "Rating": 4.8
    },
    {
        "Author": "Rowan Ashborne",
        "Genre": "Fantasy",
        "Publication Year": 1986,
        "Rating": 1.7
    }
]
<end>Can you change this Json into csv?
[
    {
        "Company": "RetailWorld",
        "Open Price": 1378.29,
        "Close Price": 1128.55,
        "High Price": 1458.98,
        "Low Price": 1128.55
    },
    {
        "Company": "AutoMotive",
        "Open Price": 87.31,
        "Close Price": 894.98,
        "High Price": 894.98,
        "Low Price": 87.31
    },
    {
        "Company": "MediaGroup",
        "Open Price": 451.09,
        "Close Price": 1220.98,
        "High Price": 1220.98,
        "Low Price": 235.68
    },
    {
        "Company": "FoodChain",
        "Open Price": 540.94,
        "Close Price": 301.73,
        "High Price": 555.48,
        "Low Price": 36.07
    },
    {
        "Company": "MediaGroup",
        "Open Price": 704.78,
        "Close Price": 1222.92,
        "High Price": 1222.92,
        "Low Price": 704.78
    },
    {
        "Company": "BioLife",
        "Open Price": 1442.65,
        "Close Price": 541.98,
        "High Price": 1442.65,
        "Low Price": 541.98
    },
    {
        "Company": "HealthGen",
        "Open Price": 159.35,
        "Close Price": 919.98,
        "High Price": 919.98,
        "Low Price": 159.35
    }
]<start>
Company,Open Price,Close Price,High Price,Low Price
RetailWorld,1378.29,1128.55,1458.98,1128.55
AutoMotive,87.31,894.98,894.98,87.31
MediaGroup,451.09,1220.98,1220.98,235.68
FoodChain,540.94,301.73,555.48,36.07
MediaGroup,704.78,1222.92,1222.92,704.78
BioLife,1442.65,541.98,1442.65,541.98
HealthGen,159.35,919.98,919.98,159.35
<end>Please transform the following YAML data into Markdown:
- Battery Level (%): 97.4
  Device ID: device-0005
  Location: Office
  Reading Value: 41.45
  Timestamp: '2022-11-16 15:04:41'
- Battery Level (%): 66.8
  Device ID: device-0017
  Location: Bedroom
  Reading Value: -24.73
  Timestamp: '2023-12-23 21:08:26'
- Battery Level (%): 12.6
  Device ID: device-0068
  Location: Kitchen
  Reading Value: -18.49
  Timestamp: '2023-05-13 23:15:25'
- Battery Level (%): 97.4
  Device ID: device-0011
  Location: Office
  Reading Value: 58.46
  Timestamp: '2022-09-04 04:54:34'
- Battery Level (%): 41.2
  Device ID: device-0085
  Location: Living Room
  Reading Value: 74.27
  Timestamp: '2023-11-01 22:10:58'
- Battery Level (%): 39.9
  Device ID: device-0082
  Location: Kitchen
  Reading Value: 65.87
  Timestamp: '2023-12-14 19:41:00'
- Battery Level (%): 58.6
  Device ID: device-0004
  Location: Garage
  Reading Value: -35.49
  Timestamp: '2022-04-05 20:33:15'
<start>
| Device ID | Location | Battery Level (%) | Reading Value | Timestamp |
| --- | --- | --- | --- | --- |
| device-0005 | Office | 97.4 | 41.45 | 2022-11-16 15:04:41 |
| device-0017 | Bedroom | 66.8 | -24.73 | 2023-12-23 21:08:26 |
| device-0068 | Kitchen | 12.6 | -18.49 | 2023-05-13 23:15:25 |
| device-0011 | Office | 97.4 | 58.46 | 2022-09-04 04:54:34 |
| device-0085 | Living Room | 41.2 | 74.27 | 2023-11-01 22:10:58 |
| device-0082 | Kitchen | 39.9 | 65.87 | 2023-12-14 19:41:00 |
| device-0004 | Garage | 58.6 | -35.49 | 2022-04-05 20:33:15 |
<end>Transform this Markdown structure to a plain text format:
| Price | Stock Quantity | Category | Supplier Name |
| --- | --- | --- | --- |
| 160.75 | 272 | Toys | ACME Corp |
| 310.66 | 149 | Electronics | Wonka Industries |
| 250.22 | 160 | Household | Wonka Industries |
| 390.25 | 356 | Household | Wonka Industries |
| 47.54 | 426 | Sports | Globex |
| 460.34 | 324 | Electronics | ACME Corp |
| 214.22 | 64 | Automotive | Globex |<start>
Price: 160.75 | Stock Quantity: 272 | Category: Toys | Supplier Name: ACME Corp
Price: 310.66 | Stock Quantity: 149 | Category: Electronics | Supplier Name: Wonka Industries
Price: 250.22 | Stock Quantity: 160 | Category: Household | Supplier Name: Wonka Industries
Price: 390.25 | Stock Quantity: 356 | Category: Household | Supplier Name: Wonka Industries
Price: 47.54 | Stock Quantity: 426 | Category: Sports | Supplier Name: Globex
Price: 460.34 | Stock Quantity: 324 | Category: Electronics | Supplier Name: ACME Corp
Price: 214.22 | Stock Quantity: 64 | Category: Automotive | Supplier Name: Globex
<end>Please transform the following csv data into plain text:
Title,Author,Publication Year,Rating
Legends of the Rift,Thorne Ironwood,1988,3.7
Tales of the Brave,Isla Windrider,2008,1.6
Echoes of Eternity,Draven Blackthorn,2016,2.8
Shadows of Solitude,Rowan Ashborne,2013,3.2
<start>
Title: Legends of the Rift | Author: Thorne Ironwood | Publication Year: 1988 | Rating: 3.7
Title: Tales of the Brave | Author: Isla Windrider | Publication Year: 2008 | Rating: 1.6
Title: Echoes of Eternity | Author: Draven Blackthorn | Publication Year: 2016 | Rating: 2.8
Title: Shadows of Solitude | Author: Rowan Ashborne | Publication Year: 2013 | Rating: 3.2
<end>Transform this markdown structure to a csv format:
| Device ID | Device Type | Location | Battery Level (%) | Reading Value | Timestamp |
| --- | --- | --- | --- | --- | --- |
| device-0011 | Motion Detector | Living Room | 71.7 | 61.78 | 2023-12-05 00:41:48 |
| device-0025 | Pressure Sensor | Garage | 63.8 | -37.06 | 2021-10-07 20:16:59 |
| device-0044 | Light Sensor | Bathroom | 77.0 | 45.98 | 2022-01-09 16:00:47 |
| device-0047 | Temperature Sensor | Hallway | 63.8 | 78.63 | 2021-06-26 10:38:01 |
| device-0065 | Humidity Sensor | Bedroom | 48.7 | -7.61 | 2022-02-19 05:55:09 |
| device-0086 | Motion Detector | Kitchen | 86.2 | 12.78 | 2023-08-08 22:41:53 |<start>
Device ID,Device Type,Location,Battery Level (%),Reading Value,Timestamp
device-0011,Motion Detector,Living Room,71.7,61.78,2023-12-05 00:41:48
device-0025,Pressure Sensor,Garage,63.8,-37.06,2021-10-07 20:16:59
device-0044,Light Sensor,Bathroom,77.0,45.98,2022-01-09 16:00:47
device-0047,Temperature Sensor,Hallway,63.8,78.63,2021-06-26 10:38:01
device-0065,Humidity Sensor,Bedroom,48.7,-7.61,2022-02-19 05:55:09
device-0086,Motion Detector,Kitchen,86.2,12.78,2023-08-08 22:41:53
<end>Can you change this json into Markdown?
[
    {
        "Company": "FoodChain",
        "Open Price": 82.03,
        "High Price": 821.55,
        "Low Price": 82.03,
        "Volume": 3962577
    },
    {
        "Company": "AeroSystems",
        "Open Price": 1359.45,
        "High Price": 1359.45,
        "Low Price": 233.45,
        "Volume": 9528119
    },
    {
        "Company": "AeroSystems",
        "Open Price": 1143.39,
        "High Price": 1480.35,
        "Low Price": 519.49,
        "Volume": 2719477
    },
    {
        "Company": "HealthGen",
        "Open Price": 616.64,
        "High Price": 705.78,
        "Low Price": 616.64,
        "Volume": 8778255
    },
    {
        "Company": "GreenEnergy",
        "Open Price": 270.34,
        "High Price": 985.94,
        "Low Price": 270.34,
        "Volume": 8311582
    },
    {
        "Company": "BioLife",
        "Open Price": 1045.86,
        "High Price": 1390.19,
        "Low Price": 588.42,
        "Volume": 8602687
    }
]<start>
| Company | Open Price | High Price | Low Price | Volume |
| --- | --- | --- | --- | --- |
| FoodChain | 82.03 | 821.55 | 82.03 | 3962577 |
| AeroSystems | 1359.45 | 1359.45 | 233.45 | 9528119 |
| AeroSystems | 1143.39 | 1480.35 | 519.49 | 2719477 |
| HealthGen | 616.64 | 705.78 | 616.64 | 8778255 |
| GreenEnergy | 270.34 | 985.94 | 270.34 | 8311582 |
| BioLife | 1045.86 | 1390.19 | 588.42 | 8602687 |
<end>Please transform the following markdown data into plain text:
| Product Name | Price | Stock Quantity | Supplier Name |
| --- | --- | --- | --- |
| Device | 480.15 | 463 | Wonka Industries |
| Gadget | 216.16 | 292 | ACME Corp |
| Thingamajig | 246.55 | 148 | ACME Corp |
| Gizmo | 259.17 | 376 | Umbrella Corp |
| Device | 293.97 | 51 | ACME Corp |<start>
Product Name: Device | Price: 480.15 | Stock Quantity: 463 | Supplier Name: Wonka Industries
Product Name: Gadget | Price: 216.16 | Stock Quantity: 292 | Supplier Name: ACME Corp
Product Name: Thingamajig | Price: 246.55 | Stock Quantity: 148 | Supplier Name: ACME Corp
Product Name: Gizmo | Price: 259.17 | Stock Quantity: 376 | Supplier Name: Umbrella Corp
Product Name: Device | Price: 293.97 | Stock Quantity: 51 | Supplier Name: ACME Corp
<end>Convert this csv to plain text:
Start Location,End Location,Duration (hours)
Denver,Phoenix,58.5
Denver,San Francisco,59.6
San Francisco,Denver,29.6
Houston,San Francisco,4.6
Denver,Houston,44.2
New York,Phoenix,60.3
<start>
Start Location: Denver | End Location: Phoenix | Duration (hours): 58.5
Start Location: Denver | End Location: San Francisco | Duration (hours): 59.6
Start Location: San Francisco | End Location: Denver | Duration (hours): 29.6
Start Location: Houston | End Location: San Francisco | Duration (hours): 4.6
Start Location: Denver | End Location: Houston | Duration (hours): 44.2
Start Location: New York | End Location: Phoenix | Duration (hours): 60.3
<end>Here's some Plain text data, can you convert it to json?
Restaurant Name: The Golden Spoon | Price Range: $$
Restaurant Name: Burger Haven | Price Range: $
Restaurant Name: Taco Town | Price Range: $$$$
Restaurant Name: Sushi World | Price Range: $
Restaurant Name: The Golden Spoon | Price Range: $
Restaurant Name: Sushi World | Price Range: $$$$$
Restaurant Name: BBQ Barn | Price Range: $$$$
Restaurant Name: Pizza Planet | Price Range: $$$
<start>
[
    {
        "Restaurant Name": "The Golden Spoon",
        "Price Range": "$$"
    },
    {
        "Restaurant Name": "Burger Haven",
        "Price Range": "$"
    },
    {
        "Restaurant Name": "Taco Town",
        "Price Range": "$$$$"
    },
    {
        "Restaurant Name": "Sushi World",
        "Price Range": "$"
    },
    {
        "Restaurant Name": "The Golden Spoon",
        "Price Range": "$"
    },
    {
        "Restaurant Name": "Sushi World",
        "Price Range": "$$$$$"
    },
    {
        "Restaurant Name": "BBQ Barn",
        "Price Range": "$$$$"
    },
    {
        "Restaurant Name": "Pizza Planet",
        "Price Range": "$$$"
    }
]
<end>Here's some markdown data, can you convert it to yml?
| Sector | Market Cap | Stock Price | Annual Revenue (B) |
| --- | --- | --- | --- |
| Finance | Small Cap | 253.46 | 441.0 |
| Finance | Mid Cap | 138.14 | 363.64 |
| Retail | Mega Cap | 264.21 | 113.46 |
| Biotech | Large Cap | 321.41 | 391.3 |
| Technology | Small Cap | 923.21 | 301.4 |
| Finance | Mid Cap | 38.81 | 298.92 |
| Finance | Mega Cap | 643.18 | 159.69 |
| Energy | Small Cap | 204.51 | 210.83 |
| Retail | Mid Cap | 370.46 | 61.72 |<start>
- Annual Revenue (B): 441.0
  Market Cap: Small Cap
  Sector: Finance
  Stock Price: 253.46
- Annual Revenue (B): 363.64
  Market Cap: Mid Cap
  Sector: Finance
  Stock Price: 138.14
- Annual Revenue (B): 113.46
  Market Cap: Mega Cap
  Sector: Retail
  Stock Price: 264.21
- Annual Revenue (B): 391.3
  Market Cap: Large Cap
  Sector: Biotech
  Stock Price: 321.41
- Annual Revenue (B): 301.4
  Market Cap: Small Cap
  Sector: Technology
  Stock Price: 923.21
- Annual Revenue (B): 298.92
  Market Cap: Mid Cap
  Sector: Finance
  Stock Price: 38.81
- Annual Revenue (B): 159.69
  Market Cap: Mega Cap
  Sector: Finance
  Stock Price: 643.18
- Annual Revenue (B): 210.83
  Market Cap: Small Cap
  Sector: Energy
  Stock Price: 204.51
- Annual Revenue (B): 61.72
  Market Cap: Mid Cap
  Sector: Retail
  Stock Price: 370.46
<end>Please transform the following CSV data into plain text:
Company,Date,Open Price,Close Price,High Price,Low Price,Volume
BioLife,2011-09-06,290.02,812.6,1148.82,290.02,7946617
AeroSystems,2019-11-24,1459.32,634.61,1459.32,353.59,1622418
MediaGroup,2016-08-24,118.91,1177.39,1177.39,118.91,7665149
<start>
Company: BioLife | Date: 2011-09-06 | Open Price: 290.02 | Close Price: 812.6 | High Price: 1148.82 | Low Price: 290.02 | Volume: 7946617
Company: AeroSystems | Date: 2019-11-24 | Open Price: 1459.32 | Close Price: 634.61 | High Price: 1459.32 | Low Price: 353.59 | Volume: 1622418
Company: MediaGroup | Date: 2016-08-24 | Open Price: 118.91 | Close Price: 1177.39 | High Price: 1177.39 | Low Price: 118.91 | Volume: 7665149
<end>Please transform the following yml data into json:
- Close Price: 903.34
  Company: FinanceTrust
  High Price: 1281.27
  Low Price: 903.34
  Open Price: 1281.27
  Volume: 2492215
- Close Price: 971.27
  Company: AeroSystems
  High Price: 971.27
  Low Price: 392.44
  Open Price: 392.44
  Volume: 3033415
- Close Price: 45.56
  Company: FoodChain
  High Price: 935.41
  Low Price: 45.56
  Open Price: 935.41
  Volume: 9030936
- Close Price: 968.96
  Company: RetailWorld
  High Price: 968.96
  Low Price: 171.45
  Open Price: 416.63
  Volume: 243201
- Close Price: 1236.6
  Company: BioLife
  High Price: 1236.6
  Low Price: 968.96
  Open Price: 968.96
  Volume: 5066126
- Close Price: 1298.4
  Company: RetailWorld
  High Price: 1298.4
  Low Price: 214.29
  Open Price: 214.29
  Volume: 7050868
- Close Price: 985.19
  Company: BioLife
  High Price: 1467.65
  Low Price: 195.39
  Open Price: 1467.65
  Volume: 4485923
- Close Price: 903.34
  Company: RetailWorld
  High Price: 903.34
  Low Price: 712.53
  Open Price: 712.53
  Volume: 790074
- Close Price: 644.61
  Company: HealthGen
  High Price: 1236.6
  Low Price: 644.61
  Open Price: 1236.6
  Volume: 1384484
- Close Price: 1143.87
  Company: BioLife
  High Price: 1442.56
  Low Price: 622.21
  Open Price: 622.21
  Volume: 243201
<start>
[
    {
        "Company": "FinanceTrust",
        "Open Price": 1281.27,
        "Close Price": 903.34,
        "High Price": 1281.27,
        "Low Price": 903.34,
        "Volume": 2492215
    },
    {
        "Company": "AeroSystems",
        "Open Price": 392.44,
        "Close Price": 971.27,
        "High Price": 971.27,
        "Low Price": 392.44,
        "Volume": 3033415
    },
    {
        "Company": "FoodChain",
        "Open Price": 935.41,
        "Close Price": 45.56,
        "High Price": 935.41,
        "Low Price": 45.56,
        "Volume": 9030936
    },
    {
        "Company": "RetailWorld",
        "Open Price": 416.63,
        "Close Price": 968.96,
        "High Price": 968.96,
        "Low Price": 171.45,
        "Volume": 243201
    },
    {
        "Company": "BioLife",
        "Open Price": 968.96,
        "Close Price": 1236.6,
        "High Price": 1236.6,
        "Low Price": 968.96,
        "Volume": 5066126
    },
    {
        "Company": "RetailWorld",
        "Open Price": 214.29,
        "Close Price": 1298.4,
        "High Price": 1298.4,
        "Low Price": 214.29,
        "Volume": 7050868
    },
    {
        "Company": "BioLife",
        "Open Price": 1467.65,
        "Close Price": 985.19,
        "High Price": 1467.65,
        "Low Price": 195.39,
        "Volume": 4485923
    },
    {
        "Company": "RetailWorld",
        "Open Price": 712.53,
        "Close Price": 903.34,
        "High Price": 903.34,
        "Low Price": 712.53,
        "Volume": 790074
    },
    {
        "Company": "HealthGen",
        "Open Price": 1236.6,
        "Close Price": 644.61,
        "High Price": 1236.6,
        "Low Price": 644.61,
        "Volume": 1384484
    },
    {
        "Company": "BioLife",
        "Open Price": 622.21,
        "Close Price": 1143.87,
        "High Price": 1442.56,
        "Low Price": 622.21,
        "Volume": 243201
    }
]
<end>Convert this csv to Json:
Author,Publication Year,Rating
Elara Moonshadow,1968,2.9
Isla Windrider,2020,2.7
Elara Moonshadow,2008,3.6
Thorne Ironwood,1981,1.4
Draven Blackthorn,1986,2.7
Elara Moonshadow,1974,2.6
Thorne Ironwood,2011,3.7
Isla Windrider,1957,3.6
<start>
[
    {
        "Author": "Elara Moonshadow",
        "Publication Year": 1968,
        "Rating": 2.9
    },
    {
        "Author": "Isla Windrider",
        "Publication Year": 2020,
        "Rating": 2.7
    },
    {
        "Author": "Elara Moonshadow",
        "Publication Year": 2008,
        "Rating": 3.6
    },
    {
        "Author": "Thorne Ironwood",
        "Publication Year": 1981,
        "Rating": 1.4
    },
    {
        "Author": "Draven Blackthorn",
        "Publication Year": 1986,
        "Rating": 2.7
    },
    {
        "Author": "Elara Moonshadow",
        "Publication Year": 1974,
        "Rating": 2.6
    },
    {
        "Author": "Thorne Ironwood",
        "Publication Year": 2011,
        "Rating": 3.7
    },
    {
        "Author": "Isla Windrider",
        "Publication Year": 1957,
        "Rating": 3.6
    }
]
<end>Here's some csv data, can you convert it to yaml?
Cuisine,Location,Rating,Price Range
Italian,Houston,3,$$
Mexican,Miami,1,$$$$
Chinese,Houston,5,$$$$
French,San Francisco,4,$$
Chinese,Miami,4,$
Italian,Seattle,3,$$$$$
Italian,New York,4,$$$$$
American,San Francisco,2,$$
Italian,Chicago,4,$$$
<start>
- Cuisine: Italian
  Location: Houston
  Price Range: $$
  Rating: 3
- Cuisine: Mexican
  Location: Miami
  Price Range: $$$$
  Rating: 1
- Cuisine: Chinese
  Location: Houston
  Price Range: $$$$
  Rating: 5
- Cuisine: French
  Location: San Francisco
  Price Range: $$
  Rating: 4
- Cuisine: Chinese
  Location: Miami
  Price Range: $
  Rating: 4
- Cuisine: Italian
  Location: Seattle
  Price Range: $$$$$
  Rating: 3
- Cuisine: Italian
  Location: New York
  Price Range: $$$$$
  Rating: 4
- Cuisine: American
  Location: San Francisco
  Price Range: $$
  Rating: 2
- Cuisine: Italian
  Location: Chicago
  Price Range: $$$
  Rating: 4
<end>Convert this csv to YML:
Device ID,Location,Timestamp
device-0001,Bedroom,2023-07-03 11:21:49
device-0008,Garage,2021-09-14 19:16:25
device-0069,Garage,2023-03-03 06:00:30
device-0070,Bathroom,2021-10-27 14:12:12
device-0062,Living Room,2022-10-02 22:41:46
device-0011,Hallway,2023-06-02 22:35:41
device-0077,Garden,2021-07-18 09:05:18
<start>
- Device ID: device-0001
  Location: Bedroom
  Timestamp: '2023-07-03 11:21:49'
- Device ID: device-0008
  Location: Garage
  Timestamp: '2021-09-14 19:16:25'
- Device ID: device-0069
  Location: Garage
  Timestamp: '2023-03-03 06:00:30'
- Device ID: device-0070
  Location: Bathroom
  Timestamp: '2021-10-27 14:12:12'
- Device ID: device-0062
  Location: Living Room
  Timestamp: '2022-10-02 22:41:46'
- Device ID: device-0011
  Location: Hallway
  Timestamp: '2023-06-02 22:35:41'
- Device ID: device-0077
  Location: Garden
  Timestamp: '2021-07-18 09:05:18'
<end>Here's some JSON data, can you convert it to plain text?
[
    {
        "Device ID": "device-0017",
        "Device Type": "Pressure Sensor",
        "Battery Level (%)": 49.1
    },
    {
        "Device ID": "device-0007",
        "Device Type": "Temperature Sensor",
        "Battery Level (%)": 58.0
    },
    {
        "Device ID": "device-0009",
        "Device Type": "Humidity Sensor",
        "Battery Level (%)": 66.0
    }
]<start>
Device ID: device-0017 | Device Type: Pressure Sensor | Battery Level (%): 49.1
Device ID: device-0007 | Device Type: Temperature Sensor | Battery Level (%): 58.0
Device ID: device-0009 | Device Type: Humidity Sensor | Battery Level (%): 66.0
<end>Please transform the following yaml data into CSV:
- Publication Year: 1956
  Rating: 4.9
  Title: The Silent Grove
- Publication Year: 1976
  Rating: 2.9
  Title: The Forgotten World
- Publication Year: 1994
  Rating: 3.6
  Title: A Journey Through Time
- Publication Year: 2006
  Rating: 4.9
  Title: The Forgotten World
- Publication Year: 1983
  Rating: 4.7
  Title: The Crystal Key
<start>
Title,Publication Year,Rating
The Silent Grove,1956,4.9
The Forgotten World,1976,2.9
A Journey Through Time,1994,3.6
The Forgotten World,2006,4.9
The Crystal Key,1983,4.7
<end>Convert this yml to CSV:
- Duration (hours): 66.4
  End Location: Phoenix
  Start Location: New York
  Trip Name: Desert Drive
- Duration (hours): 15.8
  End Location: Miami
  Start Location: Houston
  Trip Name: Desert Drive
- Duration (hours): 39.8
  End Location: Denver
  Start Location: Chicago
  Trip Name: City Explorer
- Duration (hours): 26.9
  End Location: Phoenix
  Start Location: San Francisco
  Trip Name: Lakeside Retreat
- Duration (hours): 28.5
  End Location: Houston
  Start Location: New York
  Trip Name: Mountain Adventure
- Duration (hours): 47.1
  End Location: Chicago
  Start Location: San Francisco
  Trip Name: Desert Drive
- Duration (hours): 70.6
  End Location: San Francisco
  Start Location: Chicago
  Trip Name: Lakeside Retreat
<start>
Trip Name,Start Location,End Location,Duration (hours)
Desert Drive,New York,Phoenix,66.4
Desert Drive,Houston,Miami,15.8
City Explorer,Chicago,Denver,39.8
Lakeside Retreat,San Francisco,Phoenix,26.9
Mountain Adventure,New York,Houston,28.5
Desert Drive,San Francisco,Chicago,47.1
Lakeside Retreat,Chicago,San Francisco,70.6
<end>Here's some Yaml data, can you convert it to PLAIN TEXT?
- Author: Luna Silverleaf
  Rating: 4.0
  Title: A Journey Through Time
- Author: Kara Firebrand
  Rating: 4.3
  Title: The Forgotten World
- Author: Kara Firebrand
  Rating: 3.5
  Title: The Forgotten World
- Author: Orion Frostblade
  Rating: 4.3
  Title: Legends of the Rift
- Author: Elara Moonshadow
  Rating: 4.1
  Title: A Journey Through Time
- Author: Thorne Ironwood
  Rating: 3.7
  Title: The Last Sky
<start>
Title: A Journey Through Time | Author: Luna Silverleaf | Rating: 4.0
Title: The Forgotten World | Author: Kara Firebrand | Rating: 4.3
Title: The Forgotten World | Author: Kara Firebrand | Rating: 3.5
Title: Legends of the Rift | Author: Orion Frostblade | Rating: 4.3
Title: A Journey Through Time | Author: Elara Moonshadow | Rating: 4.1
Title: The Last Sky | Author: Thorne Ironwood | Rating: 3.7
<end>Convert this json to CSV:
[
    {
        "Product Name": "Widget",
        "SKU": "SKU-1045",
        "Supplier Name": "Wayne Enterprises"
    },
    {
        "Product Name": "Contraption",
        "SKU": "SKU-1017",
        "Supplier Name": "Wayne Enterprises"
    },
    {
        "Product Name": "Instrument",
        "SKU": "SKU-1085",
        "Supplier Name": "ACME Corp"
    },
    {
        "Product Name": "Contraption",
        "SKU": "SKU-1061",
        "Supplier Name": "ACME Corp"
    },
    {
        "Product Name": "Contraption",
        "SKU": "SKU-1048",
        "Supplier Name": "Wayne Enterprises"
    },
    {
        "Product Name": "Gizmo",
        "SKU": "SKU-1057",
        "Supplier Name": "Umbrella Corp"
    },
    {
        "Product Name": "Whatchamacallit",
        "SKU": "SKU-1026",
        "Supplier Name": "Globex"
    },
    {
        "Product Name": "Whatchamacallit",
        "SKU": "SKU-1039",
        "Supplier Name": "Wonka Industries"
    },
    {
        "Product Name": "Widget",
        "SKU": "SKU-1022",
        "Supplier Name": "Globex"
    },
    {
        "Product Name": "Thingamajig",
        "SKU": "SKU-1098",
        "Supplier Name": "Wayne Enterprises"
    }
]<start>
Product Name,SKU,Supplier Name
Widget,SKU-1045,Wayne Enterprises
Contraption,SKU-1017,Wayne Enterprises
Instrument,SKU-1085,ACME Corp
Contraption,SKU-1061,ACME Corp
Contraption,SKU-1048,Wayne Enterprises
Gizmo,SKU-1057,Umbrella Corp
Whatchamacallit,SKU-1026,Globex
Whatchamacallit,SKU-1039,Wonka Industries
Widget,SKU-1022,Globex
Thingamajig,SKU-1098,Wayne Enterprises
<end>Here's some yml data, can you convert it to json?
- Category: Automotive
  SKU: SKU-1045
  Supplier Name: Wayne Enterprises
- Category: Electronics
  SKU: SKU-1001
  Supplier Name: Globex
- Category: Automotive
  SKU: SKU-1006
  Supplier Name: ACME Corp
- Category: Toys
  SKU: SKU-1075
  Supplier Name: Wayne Enterprises
- Category: Electronics
  SKU: SKU-1025
  Supplier Name: Umbrella Corp
- Category: Household
  SKU: SKU-1003
  Supplier Name: Globex
- Category: Sports
  SKU: SKU-1079
  Supplier Name: Wonka Industries
<start>
[
    {
        "SKU": "SKU-1045",
        "Category": "Automotive",
        "Supplier Name": "Wayne Enterprises"
    },
    {
        "SKU": "SKU-1001",
        "Category": "Electronics",
        "Supplier Name": "Globex"
    },
    {
        "SKU": "SKU-1006",
        "Category": "Automotive",
        "Supplier Name": "ACME Corp"
    },
    {
        "SKU": "SKU-1075",
        "Category": "Toys",
        "Supplier Name": "Wayne Enterprises"
    },
    {
        "SKU": "SKU-1025",
        "Category": "Electronics",
        "Supplier Name": "Umbrella Corp"
    },
    {
        "SKU": "SKU-1003",
        "Category": "Household",
        "Supplier Name": "Globex"
    },
    {
        "SKU": "SKU-1079",
        "Category": "Sports",
        "Supplier Name": "Wonka Industries"
    }
]
<end>Transform this JSON structure to a CSV format:
[
    {
        "Location": "Los Angeles",
        "Condition": "Stormy",
        "Temperature (C)": -8.7,
        "Humidity (%)": 37,
        "Day": "Saturday"
    },
    {
        "Location": "Miami",
        "Condition": "Stormy",
        "Temperature (C)": 9.3,
        "Humidity (%)": 70,
        "Day": "Monday"
    },
    {
        "Location": "New York",
        "Condition": "Windy",
        "Temperature (C)": 3.9,
        "Humidity (%)": 54,
        "Day": "Tuesday"
    }
]<start>
Location,Condition,Temperature (C),Humidity (%),Day
Los Angeles,Stormy,-8.7,37,Saturday
Miami,Stormy,9.3,70,Monday
New York,Windy,3.9,54,Tuesday
<end>Can you change this plain text into Markdown?
Trip Name: Coast to Coast | End Location: Los Angeles | Distance (miles): 859.7 | Duration (hours): 17.3 | Fuel Used (gallons): 73.3
Trip Name: Forest Journey | End Location: San Francisco | Distance (miles): 1531.3 | Duration (hours): 30.7 | Fuel Used (gallons): 35.7
Trip Name: Canyon Trek | End Location: Denver | Distance (miles): 400.0 | Duration (hours): 25.9 | Fuel Used (gallons): 57.7
Trip Name: Lakeside Retreat | End Location: Miami | Distance (miles): 2019.3 | Duration (hours): 24.9 | Fuel Used (gallons): 39.5
<start>
| Trip Name | End Location | Distance (miles) | Duration (hours) | Fuel Used (gallons) |
| --- | --- | --- | --- | --- |
| Coast to Coast | Los Angeles | 859.7 | 17.3 | 73.3 |
| Forest Journey | San Francisco | 1531.3 | 30.7 | 35.7 |
| Canyon Trek | Denver | 400.0 | 25.9 | 57.7 |
| Lakeside Retreat | Miami | 2019.3 | 24.9 | 39.5 |
<end>Here's some yaml data, can you convert it to Markdown?
- Category: Toys
  Price: 149.83
  Product Name: Instrument
  SKU: SKU-1058
  Stock Quantity: 221
  Supplier Name: Umbrella Corp
- Category: Toys
  Price: 416.73
  Product Name: Doohickey
  SKU: SKU-1077
  Stock Quantity: 149
  Supplier Name: Globex
- Category: Electronics
  Price: 273.67
  Product Name: Gadget
  SKU: SKU-1089
  Stock Quantity: 163
  Supplier Name: Wonka Industries
- Category: Electronics
  Price: 378.98
  Product Name: Device
  SKU: SKU-1026
  Stock Quantity: 205
  Supplier Name: Wayne Enterprises
- Category: Toys
  Price: 170.43
  Product Name: Doohickey
  SKU: SKU-1075
  Stock Quantity: 420
  Supplier Name: Globex
- Category: Household
  Price: 369.05
  Product Name: Gadget
  SKU: SKU-1017
  Stock Quantity: 235
  Supplier Name: Wonka Industries
- Category: Automotive
  Price: 249.51
  Product Name: Thingamajig
  SKU: SKU-1059
  Stock Quantity: 378
  Supplier Name: ACME Corp
- Category: Toys
  Price: 465.16
  Product Name: Doohickey
  SKU: SKU-1039
  Stock Quantity: 454
  Supplier Name: Globex
- Category: Sports
  Price: 311.33
  Product Name: Gadget
  SKU: SKU-1035
  Stock Quantity: 270
  Supplier Name: Umbrella Corp
- Category: Household
  Price: 425.77
  Product Name: Instrument
  SKU: SKU-1093
  Stock Quantity: 209
  Supplier Name: Umbrella Corp
<start>
| Product Name | SKU | Price | Stock Quantity | Category | Supplier Name |
| --- | --- | --- | --- | --- | --- |
| Instrument | SKU-1058 | 149.83 | 221 | Toys | Umbrella Corp |
| Doohickey | SKU-1077 | 416.73 | 149 | Toys | Globex |
| Gadget | SKU-1089 | 273.67 | 163 | Electronics | Wonka Industries |
| Device | SKU-1026 | 378.98 | 205 | Electronics | Wayne Enterprises |
| Doohickey | SKU-1075 | 170.43 | 420 | Toys | Globex |
| Gadget | SKU-1017 | 369.05 | 235 | Household | Wonka Industries |
| Thingamajig | SKU-1059 | 249.51 | 378 | Automotive | ACME Corp |
| Doohickey | SKU-1039 | 465.16 | 454 | Toys | Globex |
| Gadget | SKU-1035 | 311.33 | 270 | Sports | Umbrella Corp |
| Instrument | SKU-1093 | 425.77 | 209 | Household | Umbrella Corp |
<end>Can you change this yaml into csv?
- Distance (miles): 1165.8
  Duration (hours): 29.1
  End Location: Houston
  Fuel Used (gallons): 66.0
  Start Location: Denver
  Trip Name: Desert Drive
- Distance (miles): 1276.9
  Duration (hours): 7.7
  End Location: Houston
  Fuel Used (gallons): 76.5
  Start Location: Los Angeles
  Trip Name: Mountain Adventure
- Distance (miles): 2921.6
  Duration (hours): 19.8
  End Location: New York
  Fuel Used (gallons): 15.9
  Start Location: Los Angeles
  Trip Name: Mountain Adventure
- Distance (miles): 2394.9
  Duration (hours): 43.9
  End Location: Los Angeles
  Fuel Used (gallons): 48.9
  Start Location: New York
  Trip Name: Mountain Adventure
- Distance (miles): 2122.5
  Duration (hours): 58.8
  End Location: Miami
  Fuel Used (gallons): 22.8
  Start Location: Houston
  Trip Name: Forest Journey
<start>
Trip Name,Start Location,End Location,Distance (miles),Duration (hours),Fuel Used (gallons)
Desert Drive,Denver,Houston,1165.8,29.1,66.0
Mountain Adventure,Los Angeles,Houston,1276.9,7.7,76.5
Mountain Adventure,Los Angeles,New York,2921.6,19.8,15.9
Mountain Adventure,New York,Los Angeles,2394.9,43.9,48.9
Forest Journey,Houston,Miami,2122.5,58.8,22.8
<end>Here's some Markdown data, can you convert it to plain text?
| Trip Name | Start Location | End Location | Duration (hours) | Fuel Used (gallons) |
| --- | --- | --- | --- | --- |
| Mountain Adventure | Los Angeles | Chicago | 61.6 | 15.3 |
| Lakeside Retreat | Miami | Denver | 12.1 | 64.2 |
| Forest Journey | New York | Los Angeles | 31.6 | 59.9 |
| Forest Journey | Los Angeles | San Francisco | 67.0 | 6.3 |
| Forest Journey | Miami | Denver | 9.9 | 36.5 |
| Canyon Trek | Los Angeles | Miami | 33.1 | 6.6 |
| City Explorer | Chicago | Miami | 11.7 | 62.4 |<start>
Trip Name: Mountain Adventure | Start Location: Los Angeles | End Location: Chicago | Duration (hours): 61.6 | Fuel Used (gallons): 15.3
Trip Name: Lakeside Retreat | Start Location: Miami | End Location: Denver | Duration (hours): 12.1 | Fuel Used (gallons): 64.2
Trip Name: Forest Journey | Start Location: New York | End Location: Los Angeles | Duration (hours): 31.6 | Fuel Used (gallons): 59.9
Trip Name: Forest Journey | Start Location: Los Angeles | End Location: San Francisco | Duration (hours): 67.0 | Fuel Used (gallons): 6.3
Trip Name: Forest Journey | Start Location: Miami | End Location: Denver | Duration (hours): 9.9 | Fuel Used (gallons): 36.5
Trip Name: Canyon Trek | Start Location: Los Angeles | End Location: Miami | Duration (hours): 33.1 | Fuel Used (gallons): 6.6
Trip Name: City Explorer | Start Location: Chicago | End Location: Miami | Duration (hours): 11.7 | Fuel Used (gallons): 62.4
<end>Please transform the following json data into yml:
[
    {
        "Product Name": "Apparatus",
        "SKU": "SKU-1024",
        "Price": 428.15,
        "Stock Quantity": 348,
        "Category": "Sports"
    },
    {
        "Product Name": "Whatchamacallit",
        "SKU": "SKU-1090",
        "Price": 303.62,
        "Stock Quantity": 395,
        "Category": "Electronics"
    },
    {
        "Product Name": "Gadget",
        "SKU": "SKU-1034",
        "Price": 432.18,
        "Stock Quantity": 20,
        "Category": "Toys"
    },
    {
        "Product Name": "Whatchamacallit",
        "SKU": "SKU-1090",
        "Price": 414.43,
        "Stock Quantity": 10,
        "Category": "Sports"
    },
    {
        "Product Name": "Device",
        "SKU": "SKU-1020",
        "Price": 204.66,
        "Stock Quantity": 265,
        "Category": "Electronics"
    }
]<start>
- Category: Sports
  Price: 428.15
  Product Name: Apparatus
  SKU: SKU-1024
  Stock Quantity: 348
- Category: Electronics
  Price: 303.62
  Product Name: Whatchamacallit
  SKU: SKU-1090
  Stock Quantity: 395
- Category: Toys
  Price: 432.18
  Product Name: Gadget
  SKU: SKU-1034
  Stock Quantity: 20
- Category: Sports
  Price: 414.43
  Product Name: Whatchamacallit
  SKU: SKU-1090
  Stock Quantity: 10
- Category: Electronics
  Price: 204.66
  Product Name: Device
  SKU: SKU-1020
  Stock Quantity: 265
<end>Transform this Markdown structure to a PLAIN TEXT format:
| Trip Name | Start Location | End Location | Distance (miles) | Duration (hours) | Fuel Used (gallons) |
| --- | --- | --- | --- | --- | --- |
| Coast to Coast | Houston | Phoenix | 767.4 | 53.4 | 51.0 |
| Coast to Coast | San Francisco | Los Angeles | 422.2 | 16.8 | 91.1 |
| City Explorer | Miami | Los Angeles | 1586.4 | 50.8 | 86.3 |
| Coast to Coast | Miami | San Francisco | 2151.0 | 63.3 | 85.2 |
| Forest Journey | Los Angeles | Miami | 401.5 | 50.8 | 95.2 |
| City Explorer | Miami | New York | 2647.1 | 46.2 | 82.2 |
| Lakeside Retreat | Houston | Phoenix | 1244.4 | 5.8 | 17.9 |
| Desert Drive | New York | Los Angeles | 1224.0 | 43.2 | 83.8 |<start>
Trip Name: Coast to Coast | Start Location: Houston | End Location: Phoenix | Distance (miles): 767.4 | Duration (hours): 53.4 | Fuel Used (gallons): 51.0
Trip Name: Coast to Coast | Start Location: San Francisco | End Location: Los Angeles | Distance (miles): 422.2 | Duration (hours): 16.8 | Fuel Used (gallons): 91.1
Trip Name: City Explorer | Start Location: Miami | End Location: Los Angeles | Distance (miles): 1586.4 | Duration (hours): 50.8 | Fuel Used (gallons): 86.3
Trip Name: Coast to Coast | Start Location: Miami | End Location: San Francisco | Distance (miles): 2151.0 | Duration (hours): 63.3 | Fuel Used (gallons): 85.2
Trip Name: Forest Journey | Start Location: Los Angeles | End Location: Miami | Distance (miles): 401.5 | Duration (hours): 50.8 | Fuel Used (gallons): 95.2
Trip Name: City Explorer | Start Location: Miami | End Location: New York | Distance (miles): 2647.1 | Duration (hours): 46.2 | Fuel Used (gallons): 82.2
Trip Name: Lakeside Retreat | Start Location: Houston | End Location: Phoenix | Distance (miles): 1244.4 | Duration (hours): 5.8 | Fuel Used (gallons): 17.9
Trip Name: Desert Drive | Start Location: New York | End Location: Los Angeles | Distance (miles): 1224.0 | Duration (hours): 43.2 | Fuel Used (gallons): 83.8
<end>Here's some Csv data, can you convert it to markdown?
Condition,Humidity (%),Wind Speed (km/h)
Foggy,52,27.9
Snowy,75,4.5
Snowy,21,17.2
Sunny,87,23.5
Rainy,94,29.5
<start>
| Condition | Humidity (%) | Wind Speed (km/h) |
| --- | --- | --- |
| Foggy | 52 | 27.9 |
| Snowy | 75 | 4.5 |
| Snowy | 21 | 17.2 |
| Sunny | 87 | 23.5 |
| Rainy | 94 | 29.5 |
<end>Convert this json to plain text:
[
    {
        "Title": "The Silent Grove",
        "Author": "Elara Moonshadow",
        "Rating": 2.6
    },
    {
        "Title": "The Silent Grove",
        "Author": "Rowan Ashborne",
        "Rating": 2.6
    },
    {
        "Title": "The Forgotten World",
        "Author": "Draven Blackthorn",
        "Rating": 4.7
    },
    {
        "Title": "The Silent Grove",
        "Author": "Draven Blackthorn",
        "Rating": 3.4
    }
]<start>
Title: The Silent Grove | Author: Elara Moonshadow | Rating: 2.6
Title: The Silent Grove | Author: Rowan Ashborne | Rating: 2.6
Title: The Forgotten World | Author: Draven Blackthorn | Rating: 4.7
Title: The Silent Grove | Author: Draven Blackthorn | Rating: 3.4
<end>Can you change this Plain text into json?
SKU: SKU-1052 | Price: 78.32 | Stock Quantity: 291
SKU: SKU-1035 | Price: 54.32 | Stock Quantity: 179
SKU: SKU-1026 | Price: 230.27 | Stock Quantity: 418
SKU: SKU-1036 | Price: 289.48 | Stock Quantity: 85
SKU: SKU-1073 | Price: 10.28 | Stock Quantity: 175
SKU: SKU-1036 | Price: 194.11 | Stock Quantity: 467
<start>
[
    {
        "SKU": "SKU-1052",
        "Price": 78.32,
        "Stock Quantity": 291
    },
    {
        "SKU": "SKU-1035",
        "Price": 54.32,
        "Stock Quantity": 179
    },
    {
        "SKU": "SKU-1026",
        "Price": 230.27,
        "Stock Quantity": 418
    },
    {
        "SKU": "SKU-1036",
        "Price": 289.48,
        "Stock Quantity": 85
    },
    {
        "SKU": "SKU-1073",
        "Price": 10.28,
        "Stock Quantity": 175
    },
    {
        "SKU": "SKU-1036",
        "Price": 194.11,
        "Stock Quantity": 467
    }
]
<end>Can you change this plain text into JSON?
Device ID: device-0072 | Device Type: Humidity Sensor | Location: Garage | Battery Level (%): 85.3 | Reading Value: -36.01 | Timestamp: 2021-06-01 10:34:44
Device ID: device-0069 | Device Type: Light Sensor | Location: Bedroom | Battery Level (%): 33.0 | Reading Value: 20.91 | Timestamp: 2021-12-13 15:12:44
Device ID: device-0014 | Device Type: Motion Detector | Location: Bedroom | Battery Level (%): 76.3 | Reading Value: 48.04 | Timestamp: 2022-04-09 20:10:15
<start>
[
    {
        "Device ID": "device-0072",
        "Device Type": "Humidity Sensor",
        "Location": "Garage",
        "Battery Level (%)": 85.3,
        "Reading Value": -36.01,
        "Timestamp": "2021-06-01 10:34:44"
    },
    {
        "Device ID": "device-0069",
        "Device Type": "Light Sensor",
        "Location": "Bedroom",
        "Battery Level (%)": 33.0,
        "Reading Value": 20.91,
        "Timestamp": "2021-12-13 15:12:44"
    },
    {
        "Device ID": "device-0014",
        "Device Type": "Motion Detector",
        "Location": "Bedroom",
        "Battery Level (%)": 76.3,
        "Reading Value": 48.04,
        "Timestamp": "2022-04-09 20:10:15"
    }
]
<end>Can you change this CSV into PLAIN TEXT?
Title,Genre,Publication Year,Rating
The Forgotten World,Thriller,1952,4.4
Tales of the Brave,Horror,1992,3.7
Whispers of the Abyss,Mystery,1995,1.0
Whispers of the Abyss,Non-Fiction,2009,4.8
The Last Sky,Science Fiction,1962,3.5
Whispers of the Abyss,Fantasy,1967,3.9
The Crystal Key,Thriller,1983,4.6
Tales of the Brave,Historical,1998,4.3
<start>
Title: The Forgotten World | Genre: Thriller | Publication Year: 1952 | Rating: 4.4
Title: Tales of the Brave | Genre: Horror | Publication Year: 1992 | Rating: 3.7
Title: Whispers of the Abyss | Genre: Mystery | Publication Year: 1995 | Rating: 1.0
Title: Whispers of the Abyss | Genre: Non-Fiction | Publication Year: 2009 | Rating: 4.8
Title: The Last Sky | Genre: Science Fiction | Publication Year: 1962 | Rating: 3.5
Title: Whispers of the Abyss | Genre: Fantasy | Publication Year: 1967 | Rating: 3.9
Title: The Crystal Key | Genre: Thriller | Publication Year: 1983 | Rating: 4.6
Title: Tales of the Brave | Genre: Historical | Publication Year: 1998 | Rating: 4.3
<end>Can you change this PLAIN TEXT into CSV?
Trip Name: Canyon Trek | Start Location: Houston | Duration (hours): 8.5
Trip Name: City Explorer | Start Location: Miami | Duration (hours): 46.2
Trip Name: City Explorer | Start Location: San Francisco | Duration (hours): 11.9
<start>
Trip Name,Start Location,Duration (hours)
Canyon Trek,Houston,8.5
City Explorer,Miami,46.2
City Explorer,San Francisco,11.9
<end>Can you change this yml into csv?
- Category: Household
  Price: 206.31
  Product Name: Gizmo
  SKU: SKU-1032
  Stock Quantity: 7
- Category: Toys
  Price: 77.86
  Product Name: Gadget
  SKU: SKU-1007
  Stock Quantity: 417
- Category: Household
  Price: 121.47
  Product Name: Instrument
  SKU: SKU-1058
  Stock Quantity: 117
- Category: Toys
  Price: 187.05
  Product Name: Instrument
  SKU: SKU-1068
  Stock Quantity: 42
- Category: Sports
  Price: 52.61
  Product Name: Gadget
  SKU: SKU-1056
  Stock Quantity: 315
- Category: Automotive
  Price: 216.98
  Product Name: Gadget
  SKU: SKU-1033
  Stock Quantity: 115
- Category: Electronics
  Price: 280.58
  Product Name: Gadget
  SKU: SKU-1099
  Stock Quantity: 220
- Category: Toys
  Price: 209.49
  Product Name: Thingamajig
  SKU: SKU-1082
  Stock Quantity: 248
- Category: Toys
  Price: 148.44
  Product Name: Gadget
  SKU: SKU-1015
  Stock Quantity: 239
<start>
Product Name,SKU,Price,Stock Quantity,Category
Gizmo,SKU-1032,206.31,7,Household
Gadget,SKU-1007,77.86,417,Toys
Instrument,SKU-1058,121.47,117,Household
Instrument,SKU-1068,187.05,42,Toys
Gadget,SKU-1056,52.61,315,Sports
Gadget,SKU-1033,216.98,115,Automotive
Gadget,SKU-1099,280.58,220,Electronics
Thingamajig,SKU-1082,209.49,248,Toys
Gadget,SKU-1015,148.44,239,Toys
<end>Transform this PLAIN TEXT structure to a json format:
Company: MediaGroup | Date: 2020-05-03 | Open Price: 82.63 | Close Price: 506.55 | High Price: 602.25 | Low Price: 82.63 | Volume: 8233300
Company: AutoMotive | Date: 2022-08-04 | Open Price: 221.73 | Close Price: 1235.94 | High Price: 1235.94 | Low Price: 221.73 | Volume: 8766407
Company: TechnoCorp | Date: 2013-03-21 | Open Price: 149.63 | Close Price: 1250.6 | High Price: 1250.6 | Low Price: 149.63 | Volume: 9028516
Company: RetailWorld | Date: 2018-02-04 | Open Price: 1250.6 | Close Price: 415.82 | High Price: 1250.6 | Low Price: 221.73 | Volume: 3953729
Company: BioLife | Date: 2022-07-26 | Open Price: 753.33 | Close Price: 1487.72 | High Price: 1487.72 | Low Price: 160.16 | Volume: 8864923
Company: FinanceTrust | Date: 2019-02-23 | Open Price: 1265.2 | Close Price: 861.95 | High Price: 1265.2 | Low Price: 369.38 | Volume: 9288435
Company: RetailWorld | Date: 2023-12-19 | Open Price: 160.16 | Close Price: 1476.21 | High Price: 1476.21 | Low Price: 160.16 | Volume: 7103152
Company: TechnoCorp | Date: 2019-06-21 | Open Price: 1318.15 | Close Price: 1449.69 | High Price: 1449.69 | Low Price: 925.32 | Volume: 9155270
Company: MediaGroup | Date: 2020-06-06 | Open Price: 221.73 | Close Price: 1494.67 | High Price: 1494.67 | Low Price: 221.73 | Volume: 7272202
<start>
[
    {
        "Company": "MediaGroup",
        "Date": "2020-05-03",
        "Open Price": 82.63,
        "Close Price": 506.55,
        "High Price": 602.25,
        "Low Price": 82.63,
        "Volume": 8233300
    },
    {
        "Company": "AutoMotive",
        "Date": "2022-08-04",
        "Open Price": 221.73,
        "Close Price": 1235.94,
        "High Price": 1235.94,
        "Low Price": 221.73,
        "Volume": 8766407
    },
    {
        "Company": "TechnoCorp",
        "Date": "2013-03-21",
        "Open Price": 149.63,
        "Close Price": 1250.6,
        "High Price": 1250.6,
        "Low Price": 149.63,
        "Volume": 9028516
    },
    {
        "Company": "RetailWorld",
        "Date": "2018-02-04",
        "Open Price": 1250.6,
        "Close Price": 415.82,
        "High Price": 1250.6,
        "Low Price": 221.73,
        "Volume": 3953729
    },
    {
        "Company": "BioLife",
        "Date": "2022-07-26",
        "Open Price": 753.33,
        "Close Price": 1487.72,
        "High Price": 1487.72,
        "Low Price": 160.16,
        "Volume": 8864923
    },
    {
        "Company": "FinanceTrust",
        "Date": "2019-02-23",
        "Open Price": 1265.2,
        "Close Price": 861.95,
        "High Price": 1265.2,
        "Low Price": 369.38,
        "Volume": 9288435
    },
    {
        "Company": "RetailWorld",
        "Date": "2023-12-19",
        "Open Price": 160.16,
        "Close Price": 1476.21,
        "High Price": 1476.21,
        "Low Price": 160.16,
        "Volume": 7103152
    },
    {
        "Company": "TechnoCorp",
        "Date": "2019-06-21",
        "Open Price": 1318.15,
        "Close Price": 1449.69,
        "High Price": 1449.69,
        "Low Price": 925.32,
        "Volume": 9155270
    },
    {
        "Company": "MediaGroup",
        "Date": "2020-06-06",
        "Open Price": 221.73,
        "Close Price": 1494.67,
        "High Price": 1494.67,
        "Low Price": 221.73,
        "Volume": 7272202
    }
]
<end>Can you change this MARKDOWN into PLAIN TEXT?
| Device ID | Device Type | Location | Battery Level (%) | Reading Value | Timestamp |
| --- | --- | --- | --- | --- | --- |
| device-0030 | Temperature Sensor | Garden | 94.9 | 51.89 | 2023-09-05 01:37:11 |
| device-0013 | Pressure Sensor | Bedroom | 13.9 | -37.96 | 2021-08-22 04:48:50 |
| device-0012 | Motion Detector | Office | 17.0 | -8.73 | 2022-02-27 02:57:16 |<start>
Device ID: device-0030 | Device Type: Temperature Sensor | Location: Garden | Battery Level (%): 94.9 | Reading Value: 51.89 | Timestamp: 2023-09-05 01:37:11
Device ID: device-0013 | Device Type: Pressure Sensor | Location: Bedroom | Battery Level (%): 13.9 | Reading Value: -37.96 | Timestamp: 2021-08-22 04:48:50
Device ID: device-0012 | Device Type: Motion Detector | Location: Office | Battery Level (%): 17.0 | Reading Value: -8.73 | Timestamp: 2022-02-27 02:57:16
<end>Convert this markdown to yml:
| Restaurant Name | Location | Rating | Price Range |
| --- | --- | --- | --- |
| Burger Haven | Phoenix | 1 | $$$ |
| Curry Corner | Houston | 4 | $$$$ |
| Curry Corner | Miami | 1 | $$$$ |
| Burger Haven | New York | 4 | $ |
| Curry Corner | Houston | 5 | $$ |
| Vegan Delight | Chicago | 4 | $ |
| The Golden Spoon | Los Angeles | 4 | $$$$ |
| The Steakhouse | Phoenix | 1 | $ |
| Sushi World | Miami | 4 | $ |
| The Golden Spoon | Miami | 5 | $$$$ |<start>
- Location: Phoenix
  Price Range: $$$
  Rating: 1
  Restaurant Name: Burger Haven
- Location: Houston
  Price Range: $$$$
  Rating: 4
  Restaurant Name: Curry Corner
- Location: Miami
  Price Range: $$$$
  Rating: 1
  Restaurant Name: Curry Corner
- Location: New York
  Price Range: $
  Rating: 4
  Restaurant Name: Burger Haven
- Location: Houston
  Price Range: $$
  Rating: 5
  Restaurant Name: Curry Corner
- Location: Chicago
  Price Range: $
  Rating: 4
  Restaurant Name: Vegan Delight
- Location: Los Angeles
  Price Range: $$$$
  Rating: 4
  Restaurant Name: The Golden Spoon
- Location: Phoenix
  Price Range: $
  Rating: 1
  Restaurant Name: The Steakhouse
- Location: Miami
  Price Range: $
  Rating: 4
  Restaurant Name: Sushi World
- Location: Miami
  Price Range: $$$$
  Rating: 5
  Restaurant Name: The Golden Spoon
<end>Convert this yaml to Json:
- Cache Hit Ratio (%): 72.42
  Connection Count: 313
  Timestamp: '2023-06-16 17:20:53'
- Cache Hit Ratio (%): 98.38
  Connection Count: 473
  Timestamp: '2022-09-14 14:37:19'
- Cache Hit Ratio (%): 85.81
  Connection Count: 206
  Timestamp: '2021-02-05 01:02:29'
- Cache Hit Ratio (%): 87.76
  Connection Count: 454
  Timestamp: '2021-05-21 03:56:24'
<start>
[
    {
        "Cache Hit Ratio (%)": 72.42,
        "Connection Count": 313,
        "Timestamp": "2023-06-16 17:20:53"
    },
    {
        "Cache Hit Ratio (%)": 98.38,
        "Connection Count": 473,
        "Timestamp": "2022-09-14 14:37:19"
    },
    {
        "Cache Hit Ratio (%)": 85.81,
        "Connection Count": 206,
        "Timestamp": "2021-02-05 01:02:29"
    },
    {
        "Cache Hit Ratio (%)": 87.76,
        "Connection Count": 454,
        "Timestamp": "2021-05-21 03:56:24"
    }
]
<end>Please transform the following Markdown data into JSON:
| SKU | Price | Stock Quantity | Category |
| --- | --- | --- | --- |
| SKU-1016 | 239.78 | 423 | Household |
| SKU-1041 | 472.58 | 312 | Sports |
| SKU-1048 | 216.95 | 268 | Household |
| SKU-1090 | 252.41 | 76 | Toys |
| SKU-1049 | 421.06 | 493 | Sports |
| SKU-1062 | 169.14 | 168 | Sports |
| SKU-1059 | 416.41 | 456 | Sports |
| SKU-1019 | 79.06 | 13 | Sports |<start>
[
    {
        "SKU": "SKU-1016",
        "Price": 239.78,
        "Stock Quantity": 423,
        "Category": "Household"
    },
    {
        "SKU": "SKU-1041",
        "Price": 472.58,
        "Stock Quantity": 312,
        "Category": "Sports"
    },
    {
        "SKU": "SKU-1048",
        "Price": 216.95,
        "Stock Quantity": 268,
        "Category": "Household"
    },
    {
        "SKU": "SKU-1090",
        "Price": 252.41,
        "Stock Quantity": 76,
        "Category": "Toys"
    },
    {
        "SKU": "SKU-1049",
        "Price": 421.06,
        "Stock Quantity": 493,
        "Category": "Sports"
    },
    {
        "SKU": "SKU-1062",
        "Price": 169.14,
        "Stock Quantity": 168,
        "Category": "Sports"
    },
    {
        "SKU": "SKU-1059",
        "Price": 416.41,
        "Stock Quantity": 456,
        "Category": "Sports"
    },
    {
        "SKU": "SKU-1019",
        "Price": 79.06,
        "Stock Quantity": 13,
        "Category": "Sports"
    }
]
<end>Transform this PLAIN TEXT structure to a YAML format:
Genre: Fantasy | Release Year: 2007
Genre: Horror | Release Year: 1976
Genre: Adventure | Release Year: 1997
Genre: Drama | Release Year: 1974
Genre: Fantasy | Release Year: 1997
<start>
- Genre: Fantasy
  Release Year: 2007
- Genre: Horror
  Release Year: 1976
- Genre: Adventure
  Release Year: 1997
- Genre: Drama
  Release Year: 1974
- Genre: Fantasy
  Release Year: 1997
<end>Here's some markdown data, can you convert it to csv?
| Title | Director | Release Year | Box Office Earnings (M) |
| --- | --- | --- | --- |
| Dreamwalker | Aria Ravenwood | 1984 | 207.39 |
| Edge of Infinity | Zara Stormrider | 1984 | 446.59 |
| Beyond the Veil | Cade Firebrand | 1988 | 814.16 |
| The Great Expedition | Mara Moonshadow | 1988 | 628.88 |
| Escape from Earth | Lira Silverleaf | 2004 | 777.38 |
| Edge of Infinity | Zara Stormrider | 2013 | 20.42 |
| Rise of the Titans | Lira Silverleaf | 1976 | 710.13 |
| The Endless Horizon | Aria Ravenwood | 1982 | 710.62 |
| The Final Voyage | Cade Firebrand | 1996 | 249.77 |
| The Great Expedition | Talon Blackthorn | 1995 | 79.44 |<start>
Title,Director,Release Year,Box Office Earnings (M)
Dreamwalker,Aria Ravenwood,1984,207.39
Edge of Infinity,Zara Stormrider,1984,446.59
Beyond the Veil,Cade Firebrand,1988,814.16
The Great Expedition,Mara Moonshadow,1988,628.88
Escape from Earth,Lira Silverleaf,2004,777.38
Edge of Infinity,Zara Stormrider,2013,20.42
Rise of the Titans,Lira Silverleaf,1976,710.13
The Endless Horizon,Aria Ravenwood,1982,710.62
The Final Voyage,Cade Firebrand,1996,249.77
The Great Expedition,Talon Blackthorn,1995,79.44
<end>Here's some json data, can you convert it to PLAIN TEXT?
[
    {
        "Location": "Miami",
        "Condition": "Rainy",
        "Humidity (%)": 65,
        "Wind Speed (km/h)": 9.3
    },
    {
        "Location": "Los Angeles",
        "Condition": "Cloudy",
        "Humidity (%)": 44,
        "Wind Speed (km/h)": 23.5
    },
    {
        "Location": "Phoenix",
        "Condition": "Rainy",
        "Humidity (%)": 45,
        "Wind Speed (km/h)": 25.1
    },
    {
        "Location": "Denver",
        "Condition": "Rainy",
        "Humidity (%)": 68,
        "Wind Speed (km/h)": 27.2
    },
    {
        "Location": "Denver",
        "Condition": "Snowy",
        "Humidity (%)": 57,
        "Wind Speed (km/h)": 6.6
    },
    {
        "Location": "Phoenix",
        "Condition": "Sunny",
        "Humidity (%)": 68,
        "Wind Speed (km/h)": 3.6
    },
    {
        "Location": "New York",
        "Condition": "Sunny",
        "Humidity (%)": 75,
        "Wind Speed (km/h)": 1.8
    }
]<start>
Location: Miami | Condition: Rainy | Humidity (%): 65 | Wind Speed (km/h): 9.3
Location: Los Angeles | Condition: Cloudy | Humidity (%): 44 | Wind Speed (km/h): 23.5
Location: Phoenix | Condition: Rainy | Humidity (%): 45 | Wind Speed (km/h): 25.1
Location: Denver | Condition: Rainy | Humidity (%): 68 | Wind Speed (km/h): 27.2
Location: Denver | Condition: Snowy | Humidity (%): 57 | Wind Speed (km/h): 6.6
Location: Phoenix | Condition: Sunny | Humidity (%): 68 | Wind Speed (km/h): 3.6
Location: New York | Condition: Sunny | Humidity (%): 75 | Wind Speed (km/h): 1.8
<end>Transform this plain text structure to a YML format:
Product Name: Apparatus | SKU: SKU-1043 | Price: 383.17 | Stock Quantity: 263 | Category: Household | Supplier Name: Umbrella Corp
Product Name: Gizmo | SKU: SKU-1022 | Price: 399.26 | Stock Quantity: 141 | Category: Household | Supplier Name: ACME Corp
Product Name: Contraption | SKU: SKU-1020 | Price: 83.86 | Stock Quantity: 206 | Category: Toys | Supplier Name: Globex
Product Name: Instrument | SKU: SKU-1024 | Price: 398.42 | Stock Quantity: 167 | Category: Sports | Supplier Name: Wonka Industries
Product Name: Apparatus | SKU: SKU-1065 | Price: 134.9 | Stock Quantity: 39 | Category: Toys | Supplier Name: ACME Corp
<start>
- Category: Household
  Price: 383.17
  Product Name: Apparatus
  SKU: SKU-1043
  Stock Quantity: 263
  Supplier Name: Umbrella Corp
- Category: Household
  Price: 399.26
  Product Name: Gizmo
  SKU: SKU-1022
  Stock Quantity: 141
  Supplier Name: ACME Corp
- Category: Toys
  Price: 83.86
  Product Name: Contraption
  SKU: SKU-1020
  Stock Quantity: 206
  Supplier Name: Globex
- Category: Sports
  Price: 398.42
  Product Name: Instrument
  SKU: SKU-1024
  Stock Quantity: 167
  Supplier Name: Wonka Industries
- Category: Toys
  Price: 134.9
  Product Name: Apparatus
  SKU: SKU-1065
  Stock Quantity: 39
  Supplier Name: ACME Corp
<end>Transform this yaml structure to a PLAIN TEXT format:
- Company: HealthPlus
  Market Cap: Small Cap
  Quarter: Q1
  Sector: Finance
  Stock Price: 892.0
- Company: AeroSpace
  Market Cap: Mega Cap
  Quarter: Q1
  Sector: Finance
  Stock Price: 906.07
- Company: Foodies
  Market Cap: Mega Cap
  Quarter: Q2
  Sector: Energy
  Stock Price: 336.22
- Company: GlobalTrade
  Market Cap: Mid Cap
  Quarter: Q3
  Sector: Technology
  Stock Price: 491.5
- Company: AutoDrive
  Market Cap: Mid Cap
  Quarter: Q4
  Sector: Aerospace
  Stock Price: 95.15
- Company: RetailHub
  Market Cap: Large Cap
  Quarter: Q3
  Sector: Retail
  Stock Price: 252.23
- Company: HealthPlus
  Market Cap: Large Cap
  Quarter: Q3
  Sector: Energy
  Stock Price: 624.56
- Company: RetailHub
  Market Cap: Large Cap
  Quarter: Q2
  Sector: Biotech
  Stock Price: 147.27
<start>
Company: HealthPlus | Sector: Finance | Market Cap: Small Cap | Stock Price: 892.0 | Quarter: Q1
Company: AeroSpace | Sector: Finance | Market Cap: Mega Cap | Stock Price: 906.07 | Quarter: Q1
Company: Foodies | Sector: Energy | Market Cap: Mega Cap | Stock Price: 336.22 | Quarter: Q2
Company: GlobalTrade | Sector: Technology | Market Cap: Mid Cap | Stock Price: 491.5 | Quarter: Q3
Company: AutoDrive | Sector: Aerospace | Market Cap: Mid Cap | Stock Price: 95.15 | Quarter: Q4
Company: RetailHub | Sector: Retail | Market Cap: Large Cap | Stock Price: 252.23 | Quarter: Q3
Company: HealthPlus | Sector: Energy | Market Cap: Large Cap | Stock Price: 624.56 | Quarter: Q3
Company: RetailHub | Sector: Biotech | Market Cap: Large Cap | Stock Price: 147.27 | Quarter: Q2
<end>Convert this Markdown to CSV:
| Trip Name | Start Location | End Location | Distance (miles) | Duration (hours) | Fuel Used (gallons) |
| --- | --- | --- | --- | --- | --- |
| City Explorer | Phoenix | Houston | 1853.0 | 55.0 | 51.9 |
| Forest Journey | San Francisco | Los Angeles | 2850.9 | 63.1 | 41.8 |
| Forest Journey | Denver | San Francisco | 1040.2 | 3.6 | 68.3 |
| Valley Voyage | Miami | Phoenix | 1741.0 | 62.7 | 59.2 |
| Lakeside Retreat | Denver | Phoenix | 1462.2 | 13.9 | 68.3 |
| Historic Route | Phoenix | San Francisco | 204.4 | 26.6 | 23.0 |
| Valley Voyage | San Francisco | Los Angeles | 2476.6 | 68.5 | 43.9 |
| Historic Route | Chicago | Phoenix | 2601.4 | 56.0 | 51.9 |
| Coast to Coast | Los Angeles | Houston | 2496.3 | 56.0 | 22.2 |
| City Explorer | Los Angeles | Phoenix | 2670.0 | 42.4 | 93.9 |<start>
Trip Name,Start Location,End Location,Distance (miles),Duration (hours),Fuel Used (gallons)
City Explorer,Phoenix,Houston,1853.0,55.0,51.9
Forest Journey,San Francisco,Los Angeles,2850.9,63.1,41.8
Forest Journey,Denver,San Francisco,1040.2,3.6,68.3
Valley Voyage,Miami,Phoenix,1741.0,62.7,59.2
Lakeside Retreat,Denver,Phoenix,1462.2,13.9,68.3
Historic Route,Phoenix,San Francisco,204.4,26.6,23.0
Valley Voyage,San Francisco,Los Angeles,2476.6,68.5,43.9
Historic Route,Chicago,Phoenix,2601.4,56.0,51.9
Coast to Coast,Los Angeles,Houston,2496.3,56.0,22.2
City Explorer,Los Angeles,Phoenix,2670.0,42.4,93.9
<end>Convert this PLAIN TEXT to Markdown:
Queries per Second: 3272.13 | Cache Hit Ratio (%): 73.19 | Connection Count: 107
Queries per Second: 4425.54 | Cache Hit Ratio (%): 75.51 | Connection Count: 333
Queries per Second: 4045.01 | Cache Hit Ratio (%): 98.94 | Connection Count: 416
<start>
| Queries per Second | Cache Hit Ratio (%) | Connection Count |
| --- | --- | --- |
| 3272.13 | 73.19 | 107 |
| 4425.54 | 75.51 | 333 |
| 4045.01 | 98.94 | 416 |
<end>Here's some csv data, can you convert it to yml?
Market Cap,Stock Price,Annual Revenue (B)
Large Cap,198.72,114.72
Mega Cap,979.16,324.96
Large Cap,843.06,216.89
Small Cap,708.31,242.62
Mid Cap,552.6,412.24
Large Cap,488.92,487.01
Small Cap,374.76,216.89
Small Cap,960.84,295.56
<start>
- Annual Revenue (B): 114.72
  Market Cap: Large Cap
  Stock Price: 198.72
- Annual Revenue (B): 324.96
  Market Cap: Mega Cap
  Stock Price: 979.16
- Annual Revenue (B): 216.89
  Market Cap: Large Cap
  Stock Price: 843.06
- Annual Revenue (B): 242.62
  Market Cap: Small Cap
  Stock Price: 708.31
- Annual Revenue (B): 412.24
  Market Cap: Mid Cap
  Stock Price: 552.6
- Annual Revenue (B): 487.01
  Market Cap: Large Cap
  Stock Price: 488.92
- Annual Revenue (B): 216.89
  Market Cap: Small Cap
  Stock Price: 374.76
- Annual Revenue (B): 295.56
  Market Cap: Small Cap
  Stock Price: 960.84
<end>Here's some csv data, can you convert it to Yaml?
Title,Director,Box Office Earnings (M)
Starbound Odyssey,Selene Darkwhisper,391.74
Rise of the Titans,Orin Shadowalker,791.48
Edge of Infinity,Talon Blackthorn,87.08
Mystery of the Depths,Zara Stormrider,621.79
Starbound Odyssey,Cade Firebrand,567.12
<start>
- Box Office Earnings (M): 391.74
  Director: Selene Darkwhisper
  Title: Starbound Odyssey
- Box Office Earnings (M): 791.48
  Director: Orin Shadowalker
  Title: Rise of the Titans
- Box Office Earnings (M): 87.08
  Director: Talon Blackthorn
  Title: Edge of Infinity
- Box Office Earnings (M): 621.79
  Director: Zara Stormrider
  Title: Mystery of the Depths
- Box Office Earnings (M): 567.12
  Director: Cade Firebrand
  Title: Starbound Odyssey
<end>Here's some plain text data, can you convert it to Json?
Title: A Journey Through Time | Author: Thorne Ironwood | Publication Year: 2012 | Rating: 4.3
Title: Shadows of Solitude | Author: Kara Firebrand | Publication Year: 2018 | Rating: 4.9
Title: Whispers of the Abyss | Author: Kara Firebrand | Publication Year: 1961 | Rating: 4.6
Title: The Forgotten World | Author: Isla Windrider | Publication Year: 1953 | Rating: 1.6
Title: Tales of the Brave | Author: Kara Firebrand | Publication Year: 1955 | Rating: 4.8
<start>
[
    {
        "Title": "A Journey Through Time",
        "Author": "Thorne Ironwood",
        "Publication Year": 2012,
        "Rating": 4.3
    },
    {
        "Title": "Shadows of Solitude",
        "Author": "Kara Firebrand",
        "Publication Year": 2018,
        "Rating": 4.9
    },
    {
        "Title": "Whispers of the Abyss",
        "Author": "Kara Firebrand",
        "Publication Year": 1961,
        "Rating": 4.6
    },
    {
        "Title": "The Forgotten World",
        "Author": "Isla Windrider",
        "Publication Year": 1953,
        "Rating": 1.6
    },
    {
        "Title": "Tales of the Brave",
        "Author": "Kara Firebrand",
        "Publication Year": 1955,
        "Rating": 4.8
    }
]
<end>Here's some Yml data, can you convert it to markdown?
- Close Price: 831.97
  Company: RetailWorld
  Date: '2022-12-03'
  High Price: 981.93
  Low Price: 326.74
  Open Price: 981.93
  Volume: 1225480
- Close Price: 769.31
  Company: MediaGroup
  Date: '2013-01-04'
  High Price: 769.31
  Low Price: 575.43
  Open Price: 575.43
  Volume: 4975329
- Close Price: 769.31
  Company: BioLife
  Date: '2020-04-16'
  High Price: 769.31
  Low Price: 181.93
  Open Price: 181.93
  Volume: 5584228
<start>
| Company | Date | Open Price | Close Price | High Price | Low Price | Volume |
| --- | --- | --- | --- | --- | --- | --- |
| RetailWorld | 2022-12-03 | 981.93 | 831.97 | 981.93 | 326.74 | 1225480 |
| MediaGroup | 2013-01-04 | 575.43 | 769.31 | 769.31 | 575.43 | 4975329 |
| BioLife | 2020-04-16 | 181.93 | 769.31 | 769.31 | 181.93 | 5584228 |
<end>Convert this yml to MARKDOWN:
- Distance (miles): 1332.6
  Duration (hours): 49.7
  End Location: New York
  Start Location: Denver
  Trip Name: City Explorer
- Distance (miles): 2008.3
  Duration (hours): 6.3
  End Location: Miami
  Start Location: Phoenix
  Trip Name: Historic Route
- Distance (miles): 2852.9
  Duration (hours): 24.4
  End Location: New York
  Start Location: Denver
  Trip Name: Forest Journey
- Distance (miles): 2389.1
  Duration (hours): 18.6
  End Location: Denver
  Start Location: Houston
  Trip Name: Lakeside Retreat
- Distance (miles): 616.9
  Duration (hours): 62.1
  End Location: Chicago
  Start Location: Denver
  Trip Name: Lakeside Retreat
- Distance (miles): 1171.5
  Duration (hours): 14.7
  End Location: Phoenix
  Start Location: Chicago
  Trip Name: Highway Odyssey
- Distance (miles): 870.5
  Duration (hours): 68.7
  End Location: Chicago
  Start Location: New York
  Trip Name: Desert Drive
- Distance (miles): 95.6
  Duration (hours): 18.6
  End Location: Chicago
  Start Location: Phoenix
  Trip Name: Highway Odyssey
<start>
| Trip Name | Start Location | End Location | Distance (miles) | Duration (hours) |
| --- | --- | --- | --- | --- |
| City Explorer | Denver | New York | 1332.6 | 49.7 |
| Historic Route | Phoenix | Miami | 2008.3 | 6.3 |
| Forest Journey | Denver | New York | 2852.9 | 24.4 |
| Lakeside Retreat | Houston | Denver | 2389.1 | 18.6 |
| Lakeside Retreat | Denver | Chicago | 616.9 | 62.1 |
| Highway Odyssey | Chicago | Phoenix | 1171.5 | 14.7 |
| Desert Drive | New York | Chicago | 870.5 | 68.7 |
| Highway Odyssey | Phoenix | Chicago | 95.6 | 18.6 |
<end>Here's some yml data, can you convert it to Plain text?
- Condition: Sunny
  Location: Phoenix
  Temperature (C): 27.3
  Wind Speed (km/h): 10.0
- Condition: Sunny
  Location: Seattle
  Temperature (C): -8.1
  Wind Speed (km/h): 13.8
- Condition: Cloudy
  Location: New York
  Temperature (C): 16.4
  Wind Speed (km/h): 25.3
- Condition: Foggy
  Location: Houston
  Temperature (C): -3.0
  Wind Speed (km/h): 24.6
<start>
Location: Phoenix | Condition: Sunny | Temperature (C): 27.3 | Wind Speed (km/h): 10.0
Location: Seattle | Condition: Sunny | Temperature (C): -8.1 | Wind Speed (km/h): 13.8
Location: New York | Condition: Cloudy | Temperature (C): 16.4 | Wind Speed (km/h): 25.3
Location: Houston | Condition: Foggy | Temperature (C): -3.0 | Wind Speed (km/h): 24.6
<end>Please transform the following Markdown data into json:
| Title | Director | Genre | Release Year |
| --- | --- | --- | --- |
| Escape from Earth | Aria Ravenwood | Comedy | 2007 |
| Beyond the Veil | Zara Stormrider | Sci-Fi | 2005 |
| The Endless Horizon | Lira Silverleaf | Adventure | 1983 |<start>
[
    {
        "Title": "Escape from Earth",
        "Director": "Aria Ravenwood",
        "Genre": "Comedy",
        "Release Year": 2007
    },
    {
        "Title": "Beyond the Veil",
        "Director": "Zara Stormrider",
        "Genre": "Sci-Fi",
        "Release Year": 2005
    },
    {
        "Title": "The Endless Horizon",
        "Director": "Lira Silverleaf",
        "Genre": "Adventure",
        "Release Year": 1983
    }
]
<end>Can you change this Yml into MARKDOWN?
- Device ID: device-0067
  Reading Value: 0.51
  Timestamp: '2021-09-19 03:24:27'
- Device ID: device-0081
  Reading Value: 40.81
  Timestamp: '2021-02-01 03:00:47'
- Device ID: device-0082
  Reading Value: -19.73
  Timestamp: '2023-09-28 17:58:59'
- Device ID: device-0061
  Reading Value: -29.54
  Timestamp: '2022-07-10 19:04:01'
- Device ID: device-0048
  Reading Value: 48.49
  Timestamp: '2023-09-13 19:32:40'
- Device ID: device-0026
  Reading Value: 6.79
  Timestamp: '2021-01-22 08:30:12'
- Device ID: device-0090
  Reading Value: -3.9
  Timestamp: '2022-09-08 02:38:07'
- Device ID: device-0072
  Reading Value: 75.87
  Timestamp: '2022-01-05 22:36:45'
- Device ID: device-0085
  Reading Value: 24.97
  Timestamp: '2021-10-08 05:37:24'
<start>
| Device ID | Reading Value | Timestamp |
| --- | --- | --- |
| device-0067 | 0.51 | 2021-09-19 03:24:27 |
| device-0081 | 40.81 | 2021-02-01 03:00:47 |
| device-0082 | -19.73 | 2023-09-28 17:58:59 |
| device-0061 | -29.54 | 2022-07-10 19:04:01 |
| device-0048 | 48.49 | 2023-09-13 19:32:40 |
| device-0026 | 6.79 | 2021-01-22 08:30:12 |
| device-0090 | -3.9 | 2022-09-08 02:38:07 |
| device-0072 | 75.87 | 2022-01-05 22:36:45 |
| device-0085 | 24.97 | 2021-10-08 05:37:24 |
<end>Here's some plain text data, can you convert it to json?
Device ID: device-0014 | Device Type: Temperature Sensor | Battery Level (%): 35.4 | Reading Value: 47.62 | Timestamp: 2023-05-24 18:09:12
Device ID: device-0013 | Device Type: Temperature Sensor | Battery Level (%): 40.5 | Reading Value: -13.25 | Timestamp: 2023-04-25 02:25:22
Device ID: device-0061 | Device Type: Humidity Sensor | Battery Level (%): 39.8 | Reading Value: 8.58 | Timestamp: 2023-04-26 18:11:36
Device ID: device-0016 | Device Type: Light Sensor | Battery Level (%): 25.6 | Reading Value: -36.47 | Timestamp: 2021-05-19 14:41:35
Device ID: device-0064 | Device Type: Humidity Sensor | Battery Level (%): 16.2 | Reading Value: 31.92 | Timestamp: 2023-06-02 08:02:28
Device ID: device-0069 | Device Type: Humidity Sensor | Battery Level (%): 44.6 | Reading Value: -11.97 | Timestamp: 2022-06-22 16:25:22
Device ID: device-0032 | Device Type: Temperature Sensor | Battery Level (%): 97.5 | Reading Value: 16.88 | Timestamp: 2023-12-12 20:36:49
Device ID: device-0039 | Device Type: Pressure Sensor | Battery Level (%): 25.3 | Reading Value: 76.72 | Timestamp: 2021-12-26 15:58:11
Device ID: device-0091 | Device Type: Pressure Sensor | Battery Level (%): 25.6 | Reading Value: 71.35 | Timestamp: 2021-09-15 20:15:19
<start>
[
    {
        "Device ID": "device-0014",
        "Device Type": "Temperature Sensor",
        "Battery Level (%)": 35.4,
        "Reading Value": 47.62,
        "Timestamp": "2023-05-24 18:09:12"
    },
    {
        "Device ID": "device-0013",
        "Device Type": "Temperature Sensor",
        "Battery Level (%)": 40.5,
        "Reading Value": -13.25,
        "Timestamp": "2023-04-25 02:25:22"
    },
    {
        "Device ID": "device-0061",
        "Device Type": "Humidity Sensor",
        "Battery Level (%)": 39.8,
        "Reading Value": 8.58,
        "Timestamp": "2023-04-26 18:11:36"
    },
    {
        "Device ID": "device-0016",
        "Device Type": "Light Sensor",
        "Battery Level (%)": 25.6,
        "Reading Value": -36.47,
        "Timestamp": "2021-05-19 14:41:35"
    },
    {
        "Device ID": "device-0064",
        "Device Type": "Humidity Sensor",
        "Battery Level (%)": 16.2,
        "Reading Value": 31.92,
        "Timestamp": "2023-06-02 08:02:28"
    },
    {
        "Device ID": "device-0069",
        "Device Type": "Humidity Sensor",
        "Battery Level (%)": 44.6,
        "Reading Value": -11.97,
        "Timestamp": "2022-06-22 16:25:22"
    },
    {
        "Device ID": "device-0032",
        "Device Type": "Temperature Sensor",
        "Battery Level (%)": 97.5,
        "Reading Value": 16.88,
        "Timestamp": "2023-12-12 20:36:49"
    },
    {
        "Device ID": "device-0039",
        "Device Type": "Pressure Sensor",
        "Battery Level (%)": 25.3,
        "Reading Value": 76.72,
        "Timestamp": "2021-12-26 15:58:11"
    },
    {
        "Device ID": "device-0091",
        "Device Type": "Pressure Sensor",
        "Battery Level (%)": 25.6,
        "Reading Value": 71.35,
        "Timestamp": "2021-09-15 20:15:19"
    }
]
<end>Can you change this yml into Markdown?
- Condition: Snowy
  Day: Thursday
  Humidity (%): 46
  Temperature (C): 9.5
  Wind Speed (km/h): 29.3
- Condition: Foggy
  Day: Thursday
  Humidity (%): 53
  Temperature (C): 5.4
  Wind Speed (km/h): 24.9
- Condition: Cloudy
  Day: Monday
  Humidity (%): 78
  Temperature (C): 15.2
  Wind Speed (km/h): 16.3
- Condition: Sunny
  Day: Saturday
  Humidity (%): 96
  Temperature (C): 10.4
  Wind Speed (km/h): 15.5
- Condition: Sunny
  Day: Sunday
  Humidity (%): 31
  Temperature (C): -1.7
  Wind Speed (km/h): 28.7
<start>
| Condition | Temperature (C) | Humidity (%) | Wind Speed (km/h) | Day |
| --- | --- | --- | --- | --- |
| Snowy | 9.5 | 46 | 29.3 | Thursday |
| Foggy | 5.4 | 53 | 24.9 | Thursday |
| Cloudy | 15.2 | 78 | 16.3 | Monday |
| Sunny | 10.4 | 96 | 15.5 | Saturday |
| Sunny | -1.7 | 31 | 28.7 | Sunday |
<end>Please transform the following MARKDOWN data into Json:
| Genre | Release Year | Box Office Earnings (M) |
| --- | --- | --- |
| Action | 1971 | 238.74 |
| Drama | 2001 | 876.72 |
| Fantasy | 1977 | 843.25 |
| Drama | 2007 | 886.29 |
| Comedy | 1992 | 554.52 |
| Horror | 1992 | 876.72 |
| Adventure | 2021 | 262.8 |
| Horror | 1985 | 90.61 |<start>
[
    {
        "Genre": "Action",
        "Release Year": 1971,
        "Box Office Earnings (M)": 238.74
    },
    {
        "Genre": "Drama",
        "Release Year": 2001,
        "Box Office Earnings (M)": 876.72
    },
    {
        "Genre": "Fantasy",
        "Release Year": 1977,
        "Box Office Earnings (M)": 843.25
    },
    {
        "Genre": "Drama",
        "Release Year": 2007,
        "Box Office Earnings (M)": 886.29
    },
    {
        "Genre": "Comedy",
        "Release Year": 1992,
        "Box Office Earnings (M)": 554.52
    },
    {
        "Genre": "Horror",
        "Release Year": 1992,
        "Box Office Earnings (M)": 876.72
    },
    {
        "Genre": "Adventure",
        "Release Year": 2021,
        "Box Office Earnings (M)": 262.8
    },
    {
        "Genre": "Horror",
        "Release Year": 1985,
        "Box Office Earnings (M)": 90.61
    }
]
<end>Convert this plain text to JSON:
Director: Selene Darkwhisper | Release Year: 1979
Director: Cade Firebrand | Release Year: 2007
Director: Aria Ravenwood | Release Year: 1991
Director: Lira Silverleaf | Release Year: 1995
Director: Mara Moonshadow | Release Year: 1977
Director: Rylan Frostblade | Release Year: 1988
<start>
[
    {
        "Director": "Selene Darkwhisper",
        "Release Year": 1979
    },
    {
        "Director": "Cade Firebrand",
        "Release Year": 2007
    },
    {
        "Director": "Aria Ravenwood",
        "Release Year": 1991
    },
    {
        "Director": "Lira Silverleaf",
        "Release Year": 1995
    },
    {
        "Director": "Mara Moonshadow",
        "Release Year": 1977
    },
    {
        "Director": "Rylan Frostblade",
        "Release Year": 1988
    }
]
<end>Here's some JSON data, can you convert it to Yaml?
[
    {
        "Device ID": "device-0043",
        "Device Type": "Humidity Sensor",
        "Location": "Kitchen",
        "Battery Level (%)": 17.0,
        "Reading Value": -37.99,
        "Timestamp": "2023-03-05 03:37:14"
    },
    {
        "Device ID": "device-0041",
        "Device Type": "Light Sensor",
        "Location": "Hallway",
        "Battery Level (%)": 93.8,
        "Reading Value": 50.78,
        "Timestamp": "2021-12-25 07:36:13"
    },
    {
        "Device ID": "device-0075",
        "Device Type": "Temperature Sensor",
        "Location": "Office",
        "Battery Level (%)": 34.1,
        "Reading Value": 69.84,
        "Timestamp": "2023-04-10 09:17:11"
    },
    {
        "Device ID": "device-0042",
        "Device Type": "Light Sensor",
        "Location": "Hallway",
        "Battery Level (%)": 11.1,
        "Reading Value": -37.49,
        "Timestamp": "2021-06-06 01:59:10"
    },
    {
        "Device ID": "device-0009",
        "Device Type": "Motion Detector",
        "Location": "Living Room",
        "Battery Level (%)": 82.1,
        "Reading Value": 35.19,
        "Timestamp": "2023-04-04 03:17:03"
    },
    {
        "Device ID": "device-0059",
        "Device Type": "Light Sensor",
        "Location": "Hallway",
        "Battery Level (%)": 29.7,
        "Reading Value": -33.52,
        "Timestamp": "2021-01-11 17:31:12"
    },
    {
        "Device ID": "device-0060",
        "Device Type": "Temperature Sensor",
        "Location": "Living Room",
        "Battery Level (%)": 35.1,
        "Reading Value": 59.88,
        "Timestamp": "2022-06-19 19:14:24"
    },
    {
        "Device ID": "device-0066",
        "Device Type": "Light Sensor",
        "Location": "Living Room",
        "Battery Level (%)": 51.8,
        "Reading Value": 20.79,
        "Timestamp": "2023-09-18 06:55:56"
    },
    {
        "Device ID": "device-0100",
        "Device Type": "Temperature Sensor",
        "Location": "Garden",
        "Battery Level (%)": 56.8,
        "Reading Value": 74.14,
        "Timestamp": "2021-10-08 23:35:17"
    }
]<start>
- Battery Level (%): 17.0
  Device ID: device-0043
  Device Type: Humidity Sensor
  Location: Kitchen
  Reading Value: -37.99
  Timestamp: '2023-03-05 03:37:14'
- Battery Level (%): 93.8
  Device ID: device-0041
  Device Type: Light Sensor
  Location: Hallway
  Reading Value: 50.78
  Timestamp: '2021-12-25 07:36:13'
- Battery Level (%): 34.1
  Device ID: device-0075
  Device Type: Temperature Sensor
  Location: Office
  Reading Value: 69.84
  Timestamp: '2023-04-10 09:17:11'
- Battery Level (%): 11.1
  Device ID: device-0042
  Device Type: Light Sensor
  Location: Hallway
  Reading Value: -37.49
  Timestamp: '2021-06-06 01:59:10'
- Battery Level (%): 82.1
  Device ID: device-0009
  Device Type: Motion Detector
  Location: Living Room
  Reading Value: 35.19
  Timestamp: '2023-04-04 03:17:03'
- Battery Level (%): 29.7
  Device ID: device-0059
  Device Type: Light Sensor
  Location: Hallway
  Reading Value: -33.52
  Timestamp: '2021-01-11 17:31:12'
- Battery Level (%): 35.1
  Device ID: device-0060
  Device Type: Temperature Sensor
  Location: Living Room
  Reading Value: 59.88
  Timestamp: '2022-06-19 19:14:24'
- Battery Level (%): 51.8
  Device ID: device-0066
  Device Type: Light Sensor
  Location: Living Room
  Reading Value: 20.79
  Timestamp: '2023-09-18 06:55:56'
- Battery Level (%): 56.8
  Device ID: device-0100
  Device Type: Temperature Sensor
  Location: Garden
  Reading Value: 74.14
  Timestamp: '2021-10-08 23:35:17'
<end>Can you change this Csv into yml?
Title,Author,Genre,Publication Year
The Last Sky,Elara Moonshadow,Science Fiction,2014
Whispers of the Abyss,Elara Moonshadow,Fantasy,1998
Legends of the Rift,Draven Blackthorn,Thriller,1950
The Forgotten World,Kara Firebrand,Non-Fiction,1999
Echoes of Eternity,Draven Blackthorn,Mystery,1982
<start>
- Author: Elara Moonshadow
  Genre: Science Fiction
  Publication Year: 2014
  Title: The Last Sky
- Author: Elara Moonshadow
  Genre: Fantasy
  Publication Year: 1998
  Title: Whispers of the Abyss
- Author: Draven Blackthorn
  Genre: Thriller
  Publication Year: 1950
  Title: Legends of the Rift
- Author: Kara Firebrand
  Genre: Non-Fiction
  Publication Year: 1999
  Title: The Forgotten World
- Author: Draven Blackthorn
  Genre: Mystery
  Publication Year: 1982
  Title: Echoes of Eternity
<end>Here's some markdown data, can you convert it to CSV?
| Trip Name | Start Location | End Location | Distance (miles) | Fuel Used (gallons) |
| --- | --- | --- | --- | --- |
| Highway Odyssey | San Francisco | Miami | 2292.3 | 77.2 |
| Canyon Trek | Denver | Miami | 1324.3 | 25.1 |
| Canyon Trek | Houston | Chicago | 1745.4 | 23.7 |
| Highway Odyssey | Houston | Chicago | 2291.8 | 61.3 |
| Canyon Trek | New York | Houston | 445.4 | 19.6 |<start>
Trip Name,Start Location,End Location,Distance (miles),Fuel Used (gallons)
Highway Odyssey,San Francisco,Miami,2292.3,77.2
Canyon Trek,Denver,Miami,1324.3,25.1
Canyon Trek,Houston,Chicago,1745.4,23.7
Highway Odyssey,Houston,Chicago,2291.8,61.3
Canyon Trek,New York,Houston,445.4,19.6
<end>Here's some markdown data, can you convert it to YAML?
| Start Location | End Location | Duration (hours) | Fuel Used (gallons) |
| --- | --- | --- | --- |
| Chicago | Miami | 32.1 | 99.5 |
| Denver | Los Angeles | 23.6 | 64.9 |
| Phoenix | Chicago | 16.3 | 64.9 |
| Phoenix | New York | 39.8 | 87.7 |
| San Francisco | Miami | 20.8 | 36.5 |
| San Francisco | Chicago | 42.1 | 32.0 |
| Chicago | Los Angeles | 2.5 | 12.4 |
| Denver | San Francisco | 20.6 | 26.8 |<start>
- Duration (hours): 32.1
  End Location: Miami
  Fuel Used (gallons): 99.5
  Start Location: Chicago
- Duration (hours): 23.6
  End Location: Los Angeles
  Fuel Used (gallons): 64.9
  Start Location: Denver
- Duration (hours): 16.3
  End Location: Chicago
  Fuel Used (gallons): 64.9
  Start Location: Phoenix
- Duration (hours): 39.8
  End Location: New York
  Fuel Used (gallons): 87.7
  Start Location: Phoenix
- Duration (hours): 20.8
  End Location: Miami
  Fuel Used (gallons): 36.5
  Start Location: San Francisco
- Duration (hours): 42.1
  End Location: Chicago
  Fuel Used (gallons): 32.0
  Start Location: San Francisco
- Duration (hours): 2.5
  End Location: Los Angeles
  Fuel Used (gallons): 12.4
  Start Location: Chicago
- Duration (hours): 20.6
  End Location: San Francisco
  Fuel Used (gallons): 26.8
  Start Location: Denver
<end>Here's some plain text data, can you convert it to JSON?
Device ID: device-0060 | Device Type: Temperature Sensor | Location: Bathroom | Battery Level (%): 34.8 | Reading Value: 9.18 | Timestamp: 2023-01-28 19:53:34
Device ID: device-0030 | Device Type: Temperature Sensor | Location: Kitchen | Battery Level (%): 45.8 | Reading Value: 35.07 | Timestamp: 2021-08-11 20:20:43
Device ID: device-0054 | Device Type: Motion Detector | Location: Living Room | Battery Level (%): 37.5 | Reading Value: -37.19 | Timestamp: 2021-01-15 19:45:51
Device ID: device-0075 | Device Type: Pressure Sensor | Location: Office | Battery Level (%): 15.8 | Reading Value: 78.92 | Timestamp: 2023-09-18 13:47:05
Device ID: device-0064 | Device Type: Temperature Sensor | Location: Garage | Battery Level (%): 35.4 | Reading Value: 42.97 | Timestamp: 2023-07-24 07:34:45
Device ID: device-0027 | Device Type: Motion Detector | Location: Office | Battery Level (%): 96.2 | Reading Value: -4.2 | Timestamp: 2023-10-23 19:30:22
Device ID: device-0094 | Device Type: Pressure Sensor | Location: Bathroom | Battery Level (%): 80.9 | Reading Value: 3.62 | Timestamp: 2023-04-28 22:47:23
<start>
[
    {
        "Device ID": "device-0060",
        "Device Type": "Temperature Sensor",
        "Location": "Bathroom",
        "Battery Level (%)": 34.8,
        "Reading Value": 9.18,
        "Timestamp": "2023-01-28 19:53:34"
    },
    {
        "Device ID": "device-0030",
        "Device Type": "Temperature Sensor",
        "Location": "Kitchen",
        "Battery Level (%)": 45.8,
        "Reading Value": 35.07,
        "Timestamp": "2021-08-11 20:20:43"
    },
    {
        "Device ID": "device-0054",
        "Device Type": "Motion Detector",
        "Location": "Living Room",
        "Battery Level (%)": 37.5,
        "Reading Value": -37.19,
        "Timestamp": "2021-01-15 19:45:51"
    },
    {
        "Device ID": "device-0075",
        "Device Type": "Pressure Sensor",
        "Location": "Office",
        "Battery Level (%)": 15.8,
        "Reading Value": 78.92,
        "Timestamp": "2023-09-18 13:47:05"
    },
    {
        "Device ID": "device-0064",
        "Device Type": "Temperature Sensor",
        "Location": "Garage",
        "Battery Level (%)": 35.4,
        "Reading Value": 42.97,
        "Timestamp": "2023-07-24 07:34:45"
    },
    {
        "Device ID": "device-0027",
        "Device Type": "Motion Detector",
        "Location": "Office",
        "Battery Level (%)": 96.2,
        "Reading Value": -4.2,
        "Timestamp": "2023-10-23 19:30:22"
    },
    {
        "Device ID": "device-0094",
        "Device Type": "Pressure Sensor",
        "Location": "Bathroom",
        "Battery Level (%)": 80.9,
        "Reading Value": 3.62,
        "Timestamp": "2023-04-28 22:47:23"
    }
]
<end>Here's some MARKDOWN data, can you convert it to Yml?
| Title | Director | Genre | Release Year | Box Office Earnings (M) |
| --- | --- | --- | --- | --- |
| Mystery of the Depths | Orin Shadowalker | Action | 1994 | 649.83 |
| The Endless Horizon | Aria Ravenwood | Horror | 2022 | 649.83 |
| The Final Voyage | Cade Firebrand | Fantasy | 1992 | 400.63 |
| Beyond the Veil | Rylan Frostblade | Action | 1994 | 865.81 |<start>
- Box Office Earnings (M): 649.83
  Director: Orin Shadowalker
  Genre: Action
  Release Year: 1994
  Title: Mystery of the Depths
- Box Office Earnings (M): 649.83
  Director: Aria Ravenwood
  Genre: Horror
  Release Year: 2022
  Title: The Endless Horizon
- Box Office Earnings (M): 400.63
  Director: Cade Firebrand
  Genre: Fantasy
  Release Year: 1992
  Title: The Final Voyage
- Box Office Earnings (M): 865.81
  Director: Rylan Frostblade
  Genre: Action
  Release Year: 1994
  Title: Beyond the Veil
<end>Can you change this plain text into yaml?
Trip Name: Mountain Adventure | Start Location: Phoenix | End Location: San Francisco | Distance (miles): 626.0 | Fuel Used (gallons): 94.2
Trip Name: Mountain Adventure | Start Location: Houston | End Location: New York | Distance (miles): 1773.1 | Fuel Used (gallons): 13.8
Trip Name: Mountain Adventure | Start Location: Miami | End Location: Houston | Distance (miles): 1456.8 | Fuel Used (gallons): 20.6
Trip Name: Lakeside Retreat | Start Location: Phoenix | End Location: Denver | Distance (miles): 698.3 | Fuel Used (gallons): 6.0
Trip Name: City Explorer | Start Location: Phoenix | End Location: Miami | Distance (miles): 1543.5 | Fuel Used (gallons): 68.0
Trip Name: Highway Odyssey | Start Location: San Francisco | End Location: New York | Distance (miles): 1581.4 | Fuel Used (gallons): 39.2
<start>
- Distance (miles): 626.0
  End Location: San Francisco
  Fuel Used (gallons): 94.2
  Start Location: Phoenix
  Trip Name: Mountain Adventure
- Distance (miles): 1773.1
  End Location: New York
  Fuel Used (gallons): 13.8
  Start Location: Houston
  Trip Name: Mountain Adventure
- Distance (miles): 1456.8
  End Location: Houston
  Fuel Used (gallons): 20.6
  Start Location: Miami
  Trip Name: Mountain Adventure
- Distance (miles): 698.3
  End Location: Denver
  Fuel Used (gallons): 6.0
  Start Location: Phoenix
  Trip Name: Lakeside Retreat
- Distance (miles): 1543.5
  End Location: Miami
  Fuel Used (gallons): 68.0
  Start Location: Phoenix
  Trip Name: City Explorer
- Distance (miles): 1581.4
  End Location: New York
  Fuel Used (gallons): 39.2
  Start Location: San Francisco
  Trip Name: Highway Odyssey
<end>Please transform the following YML data into MARKDOWN:
- Category: Electronics
  Price: 33.68
  SKU: SKU-1053
  Stock Quantity: 475
  Supplier Name: Wayne Enterprises
- Category: Electronics
  Price: 124.6
  SKU: SKU-1004
  Stock Quantity: 231
  Supplier Name: Umbrella Corp
- Category: Electronics
  Price: 213.07
  SKU: SKU-1030
  Stock Quantity: 126
  Supplier Name: Umbrella Corp
- Category: Automotive
  Price: 183.18
  SKU: SKU-1031
  Stock Quantity: 178
  Supplier Name: Globex
- Category: Sports
  Price: 446.64
  SKU: SKU-1064
  Stock Quantity: 203
  Supplier Name: Umbrella Corp
- Category: Toys
  Price: 43.06
  SKU: SKU-1024
  Stock Quantity: 336
  Supplier Name: Wonka Industries
<start>
| SKU | Price | Stock Quantity | Category | Supplier Name |
| --- | --- | --- | --- | --- |
| SKU-1053 | 33.68 | 475 | Electronics | Wayne Enterprises |
| SKU-1004 | 124.6 | 231 | Electronics | Umbrella Corp |
| SKU-1030 | 213.07 | 126 | Electronics | Umbrella Corp |
| SKU-1031 | 183.18 | 178 | Automotive | Globex |
| SKU-1064 | 446.64 | 203 | Sports | Umbrella Corp |
| SKU-1024 | 43.06 | 336 | Toys | Wonka Industries |
<end>Please transform the following YML data into JSON:
- Annual Revenue (B): 85.88
  Company: HealthPlus
  Market Cap: Small Cap
  Quarter: Q2
  Stock Price: 783.07
- Annual Revenue (B): 274.54
  Company: FinanceWorks
  Market Cap: Large Cap
  Quarter: Q3
  Stock Price: 263.23
- Annual Revenue (B): 208.71
  Company: RetailHub
  Market Cap: Small Cap
  Quarter: Q3
  Stock Price: 793.52
- Annual Revenue (B): 66.09
  Company: TechCorp
  Market Cap: Mid Cap
  Quarter: Q2
  Stock Price: 206.77
- Annual Revenue (B): 82.6
  Company: EcoEnergy
  Market Cap: Large Cap
  Quarter: Q3
  Stock Price: 709.09
- Annual Revenue (B): 399.81
  Company: TechCorp
  Market Cap: Mid Cap
  Quarter: Q4
  Stock Price: 511.38
- Annual Revenue (B): 212.08
  Company: RetailHub
  Market Cap: Mid Cap
  Quarter: Q3
  Stock Price: 164.49
- Annual Revenue (B): 382.34
  Company: BioPharm
  Market Cap: Mega Cap
  Quarter: Q3
  Stock Price: 972.3
- Annual Revenue (B): 404.18
  Company: FinanceWorks
  Market Cap: Small Cap
  Quarter: Q4
  Stock Price: 543.56
<start>
[
    {
        "Company": "HealthPlus",
        "Market Cap": "Small Cap",
        "Stock Price": 783.07,
        "Annual Revenue (B)": 85.88,
        "Quarter": "Q2"
    },
    {
        "Company": "FinanceWorks",
        "Market Cap": "Large Cap",
        "Stock Price": 263.23,
        "Annual Revenue (B)": 274.54,
        "Quarter": "Q3"
    },
    {
        "Company": "RetailHub",
        "Market Cap": "Small Cap",
        "Stock Price": 793.52,
        "Annual Revenue (B)": 208.71,
        "Quarter": "Q3"
    },
    {
        "Company": "TechCorp",
        "Market Cap": "Mid Cap",
        "Stock Price": 206.77,
        "Annual Revenue (B)": 66.09,
        "Quarter": "Q2"
    },
    {
        "Company": "EcoEnergy",
        "Market Cap": "Large Cap",
        "Stock Price": 709.09,
        "Annual Revenue (B)": 82.6,
        "Quarter": "Q3"
    },
    {
        "Company": "TechCorp",
        "Market Cap": "Mid Cap",
        "Stock Price": 511.38,
        "Annual Revenue (B)": 399.81,
        "Quarter": "Q4"
    },
    {
        "Company": "RetailHub",
        "Market Cap": "Mid Cap",
        "Stock Price": 164.49,
        "Annual Revenue (B)": 212.08,
        "Quarter": "Q3"
    },
    {
        "Company": "BioPharm",
        "Market Cap": "Mega Cap",
        "Stock Price": 972.3,
        "Annual Revenue (B)": 382.34,
        "Quarter": "Q3"
    },
    {
        "Company": "FinanceWorks",
        "Market Cap": "Small Cap",
        "Stock Price": 543.56,
        "Annual Revenue (B)": 404.18,
        "Quarter": "Q4"
    }
]
<end>Convert this Csv to MARKDOWN:
Company,Date,Open Price,Close Price,High Price,Low Price,Volume
MediaGroup,2015-05-16,1421.23,1399.06,1421.23,488.25,4257764
BioLife,2022-08-05,976.67,304.8,976.67,304.8,8964203
FinanceTrust,2020-02-23,267.68,1345.27,1345.27,267.68,2570483
AeroSystems,2014-02-07,928.1,558.21,1361.7,267.68,4516070
HealthGen,2019-03-24,1176.32,821.56,1176.32,21.93,6741352
FoodChain,2022-06-24,196.45,214.27,214.27,159.47,9007771
HealthGen,2011-05-23,342.81,839.22,839.22,342.81,2293600
RetailWorld,2015-12-14,500.8,247.42,1176.32,247.42,9116693
<start>
| Company | Date | Open Price | Close Price | High Price | Low Price | Volume |
| --- | --- | --- | --- | --- | --- | --- |
| MediaGroup | 2015-05-16 | 1421.23 | 1399.06 | 1421.23 | 488.25 | 4257764 |
| BioLife | 2022-08-05 | 976.67 | 304.8 | 976.67 | 304.8 | 8964203 |
| FinanceTrust | 2020-02-23 | 267.68 | 1345.27 | 1345.27 | 267.68 | 2570483 |
| AeroSystems | 2014-02-07 | 928.1 | 558.21 | 1361.7 | 267.68 | 4516070 |
| HealthGen | 2019-03-24 | 1176.32 | 821.56 | 1176.32 | 21.93 | 6741352 |
| FoodChain | 2022-06-24 | 196.45 | 214.27 | 214.27 | 159.47 | 9007771 |
| HealthGen | 2011-05-23 | 342.81 | 839.22 | 839.22 | 342.81 | 2293600 |
| RetailWorld | 2015-12-14 | 500.8 | 247.42 | 1176.32 | 247.42 | 9116693 |
<end>Convert this PLAIN TEXT to Yml:
Device ID: device-0077 | Location: Hallway | Battery Level (%): 76.2
Device ID: device-0059 | Location: Garage | Battery Level (%): 44.1
Device ID: device-0062 | Location: Kitchen | Battery Level (%): 88.2
Device ID: device-0024 | Location: Living Room | Battery Level (%): 47.5
Device ID: device-0096 | Location: Bathroom | Battery Level (%): 27.1
Device ID: device-0088 | Location: Bathroom | Battery Level (%): 67.6
Device ID: device-0059 | Location: Garage | Battery Level (%): 49.4
Device ID: device-0032 | Location: Garage | Battery Level (%): 38.4
<start>
- Battery Level (%): 76.2
  Device ID: device-0077
  Location: Hallway
- Battery Level (%): 44.1
  Device ID: device-0059
  Location: Garage
- Battery Level (%): 88.2
  Device ID: device-0062
  Location: Kitchen
- Battery Level (%): 47.5
  Device ID: device-0024
  Location: Living Room
- Battery Level (%): 27.1
  Device ID: device-0096
  Location: Bathroom
- Battery Level (%): 67.6
  Device ID: device-0088
  Location: Bathroom
- Battery Level (%): 49.4
  Device ID: device-0059
  Location: Garage
- Battery Level (%): 38.4
  Device ID: device-0032
  Location: Garage
<end>Transform this Json structure to a yaml format:
[
    {
        "Restaurant Name": "Vegan Delight",
        "Cuisine": "Chinese",
        "Location": "Phoenix",
        "Rating": 3
    },
    {
        "Restaurant Name": "Curry Corner",
        "Cuisine": "Japanese",
        "Location": "Phoenix",
        "Rating": 2
    },
    {
        "Restaurant Name": "Curry Corner",
        "Cuisine": "Japanese",
        "Location": "Los Angeles",
        "Rating": 2
    },
    {
        "Restaurant Name": "Burger Haven",
        "Cuisine": "American",
        "Location": "New York",
        "Rating": 3
    },
    {
        "Restaurant Name": "Vegan Delight",
        "Cuisine": "Chinese",
        "Location": "Seattle",
        "Rating": 4
    },
    {
        "Restaurant Name": "Taco Town",
        "Cuisine": "American",
        "Location": "Houston",
        "Rating": 1
    },
    {
        "Restaurant Name": "The Steakhouse",
        "Cuisine": "Mexican",
        "Location": "Chicago",
        "Rating": 3
    },
    {
        "Restaurant Name": "The Golden Spoon",
        "Cuisine": "Indian",
        "Location": "Miami",
        "Rating": 5
    },
    {
        "Restaurant Name": "Sushi World",
        "Cuisine": "Mexican",
        "Location": "Seattle",
        "Rating": 5
    },
    {
        "Restaurant Name": "The Steakhouse",
        "Cuisine": "Italian",
        "Location": "Seattle",
        "Rating": 2
    }
]<start>
- Cuisine: Chinese
  Location: Phoenix
  Rating: 3
  Restaurant Name: Vegan Delight
- Cuisine: Japanese
  Location: Phoenix
  Rating: 2
  Restaurant Name: Curry Corner
- Cuisine: Japanese
  Location: Los Angeles
  Rating: 2
  Restaurant Name: Curry Corner
- Cuisine: American
  Location: New York
  Rating: 3
  Restaurant Name: Burger Haven
- Cuisine: Chinese
  Location: Seattle
  Rating: 4
  Restaurant Name: Vegan Delight
- Cuisine: American
  Location: Houston
  Rating: 1
  Restaurant Name: Taco Town
- Cuisine: Mexican
  Location: Chicago
  Rating: 3
  Restaurant Name: The Steakhouse
- Cuisine: Indian
  Location: Miami
  Rating: 5
  Restaurant Name: The Golden Spoon
- Cuisine: Mexican
  Location: Seattle
  Rating: 5
  Restaurant Name: Sushi World
- Cuisine: Italian
  Location: Seattle
  Rating: 2
  Restaurant Name: The Steakhouse
<end>Transform this csv structure to a Markdown format:
Device Type,Location,Reading Value,Timestamp
Temperature Sensor,Bedroom,22.78,2023-01-20 00:12:28
Temperature Sensor,Garage,-6.84,2023-11-20 00:09:42
Pressure Sensor,Bathroom,-39.61,2023-10-17 10:58:33
<start>
| Device Type | Location | Reading Value | Timestamp |
| --- | --- | --- | --- |
| Temperature Sensor | Bedroom | 22.78 | 2023-01-20 00:12:28 |
| Temperature Sensor | Garage | -6.84 | 2023-11-20 00:09:42 |
| Pressure Sensor | Bathroom | -39.61 | 2023-10-17 10:58:33 |
<end>Here's some markdown data, can you convert it to CSV?
| Database Name | Queries per Second | Connection Count | Average Latency (ms) | Timestamp |
| --- | --- | --- | --- | --- |
| LogsDB | 4079.2 | 322 | 55.09 | 2023-03-14 02:14:11 |
| MetricsDB | 4823.25 | 19 | 13.75 | 2023-04-19 09:23:24 |
| AnalyticsDB | 3242.34 | 162 | 77.48 | 2021-12-03 08:06:38 |
| SalesDB | 4027.78 | 26 | 67.18 | 2022-06-14 18:10:14 |
| UserDB | 1160.45 | 13 | 55.58 | 2023-11-07 18:51:27 |
| LogsDB | 650.54 | 432 | 74.71 | 2022-02-08 18:30:11 |
| InventoryDB | 2284.5 | 280 | 86.63 | 2023-07-07 15:19:43 |<start>
Database Name,Queries per Second,Connection Count,Average Latency (ms),Timestamp
LogsDB,4079.2,322,55.09,2023-03-14 02:14:11
MetricsDB,4823.25,19,13.75,2023-04-19 09:23:24
AnalyticsDB,3242.34,162,77.48,2021-12-03 08:06:38
SalesDB,4027.78,26,67.18,2022-06-14 18:10:14
UserDB,1160.45,13,55.58,2023-11-07 18:51:27
LogsDB,650.54,432,74.71,2022-02-08 18:30:11
InventoryDB,2284.5,280,86.63,2023-07-07 15:19:43
<end>Please transform the following Csv data into Markdown:
Location,Wind Speed (km/h),Day
Seattle,14.6,Saturday
Houston,19.2,Tuesday
New York,1.9,Monday
Denver,11.4,Thursday
Miami,23.9,Wednesday
Chicago,15.5,Sunday
Seattle,6.0,Monday
New York,26.7,Friday
Denver,10.3,Thursday
Miami,16.4,Friday
<start>
| Location | Wind Speed (km/h) | Day |
| --- | --- | --- |
| Seattle | 14.6 | Saturday |
| Houston | 19.2 | Tuesday |
| New York | 1.9 | Monday |
| Denver | 11.4 | Thursday |
| Miami | 23.9 | Wednesday |
| Chicago | 15.5 | Sunday |
| Seattle | 6.0 | Monday |
| New York | 26.7 | Friday |
| Denver | 10.3 | Thursday |
| Miami | 16.4 | Friday |
<end>Convert this MARKDOWN to Yml:
| Company | Market Cap | Stock Price |
| --- | --- | --- |
| AeroSpace | Small Cap | 185.88 |
| TechCorp | Mid Cap | 708.61 |
| Foodies | Mid Cap | 917.84 |
| BioPharm | Mid Cap | 289.89 |
| BioPharm | Mid Cap | 479.44 |
| GlobalTrade | Mid Cap | 857.07 |
| TechCorp | Mid Cap | 446.21 |
| AutoDrive | Mid Cap | 197.09 |
| AeroSpace | Large Cap | 569.45 |<start>
- Company: AeroSpace
  Market Cap: Small Cap
  Stock Price: 185.88
- Company: TechCorp
  Market Cap: Mid Cap
  Stock Price: 708.61
- Company: Foodies
  Market Cap: Mid Cap
  Stock Price: 917.84
- Company: BioPharm
  Market Cap: Mid Cap
  Stock Price: 289.89
- Company: BioPharm
  Market Cap: Mid Cap
  Stock Price: 479.44
- Company: GlobalTrade
  Market Cap: Mid Cap
  Stock Price: 857.07
- Company: TechCorp
  Market Cap: Mid Cap
  Stock Price: 446.21
- Company: AutoDrive
  Market Cap: Mid Cap
  Stock Price: 197.09
- Company: AeroSpace
  Market Cap: Large Cap
  Stock Price: 569.45
<end>Transform this JSON structure to a yml format:
[
    {
        "Location": "Chicago",
        "Condition": "Rainy",
        "Day": "Friday"
    },
    {
        "Location": "Chicago",
        "Condition": "Foggy",
        "Day": "Wednesday"
    },
    {
        "Location": "Los Angeles",
        "Condition": "Sunny",
        "Day": "Tuesday"
    },
    {
        "Location": "Miami",
        "Condition": "Foggy",
        "Day": "Thursday"
    }
]<start>
- Condition: Rainy
  Day: Friday
  Location: Chicago
- Condition: Foggy
  Day: Wednesday
  Location: Chicago
- Condition: Sunny
  Day: Tuesday
  Location: Los Angeles
- Condition: Foggy
  Day: Thursday
  Location: Miami
<end>Can you change this Yml into json?
- Humidity (%): 68
  Location: Seattle
  Wind Speed (km/h): 22.0
- Humidity (%): 48
  Location: Los Angeles
  Wind Speed (km/h): 22.8
- Humidity (%): 58
  Location: Los Angeles
  Wind Speed (km/h): 1.3
<start>
[
    {
        "Location": "Seattle",
        "Humidity (%)": 68,
        "Wind Speed (km/h)": 22.0
    },
    {
        "Location": "Los Angeles",
        "Humidity (%)": 48,
        "Wind Speed (km/h)": 22.8
    },
    {
        "Location": "Los Angeles",
        "Humidity (%)": 58,
        "Wind Speed (km/h)": 1.3
    }
]
<end>Convert this PLAIN TEXT to YAML:
Title: The Final Voyage | Director: Talon Blackthorn | Genre: Comedy | Release Year: 2020 | Box Office Earnings (M): 958.76
Title: The Great Expedition | Director: Rylan Frostblade | Genre: Horror | Release Year: 2022 | Box Office Earnings (M): 248.58
Title: Beyond the Veil | Director: Talon Blackthorn | Genre: Fantasy | Release Year: 1990 | Box Office Earnings (M): 668.06
Title: Edge of Infinity | Director: Cade Firebrand | Genre: Comedy | Release Year: 2014 | Box Office Earnings (M): 122.91
Title: Rise of the Titans | Director: Rylan Frostblade | Genre: Sci-Fi | Release Year: 1991 | Box Office Earnings (M): 564.72
Title: Starbound Odyssey | Director: Mara Moonshadow | Genre: Sci-Fi | Release Year: 1999 | Box Office Earnings (M): 978.9
Title: Rise of the Titans | Director: Talon Blackthorn | Genre: Horror | Release Year: 1983 | Box Office Earnings (M): 546.31
Title: Dreamwalker | Director: Selene Darkwhisper | Genre: Comedy | Release Year: 1997 | Box Office Earnings (M): 834.12
Title: The Final Voyage | Director: Lira Silverleaf | Genre: Adventure | Release Year: 1997 | Box Office Earnings (M): 125.18
Title: Edge of Infinity | Director: Cade Firebrand | Genre: Action | Release Year: 1970 | Box Office Earnings (M): 785.36
<start>
- Box Office Earnings (M): 958.76
  Director: Talon Blackthorn
  Genre: Comedy
  Release Year: 2020
  Title: The Final Voyage
- Box Office Earnings (M): 248.58
  Director: Rylan Frostblade
  Genre: Horror
  Release Year: 2022
  Title: The Great Expedition
- Box Office Earnings (M): 668.06
  Director: Talon Blackthorn
  Genre: Fantasy
  Release Year: 1990
  Title: Beyond the Veil
- Box Office Earnings (M): 122.91
  Director: Cade Firebrand
  Genre: Comedy
  Release Year: 2014
  Title: Edge of Infinity
- Box Office Earnings (M): 564.72
  Director: Rylan Frostblade
  Genre: Sci-Fi
  Release Year: 1991
  Title: Rise of the Titans
- Box Office Earnings (M): 978.9
  Director: Mara Moonshadow
  Genre: Sci-Fi
  Release Year: 1999
  Title: Starbound Odyssey
- Box Office Earnings (M): 546.31
  Director: Talon Blackthorn
  Genre: Horror
  Release Year: 1983
  Title: Rise of the Titans
- Box Office Earnings (M): 834.12
  Director: Selene Darkwhisper
  Genre: Comedy
  Release Year: 1997
  Title: Dreamwalker
- Box Office Earnings (M): 125.18
  Director: Lira Silverleaf
  Genre: Adventure
  Release Year: 1997
  Title: The Final Voyage
- Box Office Earnings (M): 785.36
  Director: Cade Firebrand
  Genre: Action
  Release Year: 1970
  Title: Edge of Infinity
<end>Can you change this JSON into YML?
[
    {
        "SKU": "SKU-1027",
        "Price": 244.27,
        "Stock Quantity": 484
    },
    {
        "SKU": "SKU-1027",
        "Price": 39.57,
        "Stock Quantity": 183
    },
    {
        "SKU": "SKU-1086",
        "Price": 160.04,
        "Stock Quantity": 181
    },
    {
        "SKU": "SKU-1062",
        "Price": 322.41,
        "Stock Quantity": 187
    },
    {
        "SKU": "SKU-1039",
        "Price": 221.38,
        "Stock Quantity": 99
    },
    {
        "SKU": "SKU-1001",
        "Price": 181.51,
        "Stock Quantity": 238
    },
    {
        "SKU": "SKU-1010",
        "Price": 77.14,
        "Stock Quantity": 205
    },
    {
        "SKU": "SKU-1063",
        "Price": 183.53,
        "Stock Quantity": 266
    }
]<start>
- Price: 244.27
  SKU: SKU-1027
  Stock Quantity: 484
- Price: 39.57
  SKU: SKU-1027
  Stock Quantity: 183
- Price: 160.04
  SKU: SKU-1086
  Stock Quantity: 181
- Price: 322.41
  SKU: SKU-1062
  Stock Quantity: 187
- Price: 221.38
  SKU: SKU-1039
  Stock Quantity: 99
- Price: 181.51
  SKU: SKU-1001
  Stock Quantity: 238
- Price: 77.14
  SKU: SKU-1010
  Stock Quantity: 205
- Price: 183.53
  SKU: SKU-1063
  Stock Quantity: 266
<end>Here's some CSV data, can you convert it to yaml?
Start Location,End Location,Distance (miles),Fuel Used (gallons)
Miami,San Francisco,271.7,60.8
Denver,Chicago,945.2,95.3
Los Angeles,New York,1957.6,27.3
Chicago,Miami,1801.5,41.6
Chicago,Houston,1180.6,58.3
San Francisco,Houston,939.6,46.7
Chicago,Miami,1050.4,76.0
Los Angeles,Denver,68.9,35.2
Los Angeles,Houston,499.3,16.5
<start>
- Distance (miles): 271.7
  End Location: San Francisco
  Fuel Used (gallons): 60.8
  Start Location: Miami
- Distance (miles): 945.2
  End Location: Chicago
  Fuel Used (gallons): 95.3
  Start Location: Denver
- Distance (miles): 1957.6
  End Location: New York
  Fuel Used (gallons): 27.3
  Start Location: Los Angeles
- Distance (miles): 1801.5
  End Location: Miami
  Fuel Used (gallons): 41.6
  Start Location: Chicago
- Distance (miles): 1180.6
  End Location: Houston
  Fuel Used (gallons): 58.3
  Start Location: Chicago
- Distance (miles): 939.6
  End Location: Houston
  Fuel Used (gallons): 46.7
  Start Location: San Francisco
- Distance (miles): 1050.4
  End Location: Miami
  Fuel Used (gallons): 76.0
  Start Location: Chicago
- Distance (miles): 68.9
  End Location: Denver
  Fuel Used (gallons): 35.2
  Start Location: Los Angeles
- Distance (miles): 499.3
  End Location: Houston
  Fuel Used (gallons): 16.5
  Start Location: Los Angeles
<end>Please transform the following Markdown data into json:
| Database Name | Cache Hit Ratio (%) | Connection Count | Average Latency (ms) | Timestamp |
| --- | --- | --- | --- | --- |
| OrdersDB | 84.6 | 186 | 23.7 | 2023-04-22 09:54:59 |
| AnalyticsDB | 99.61 | 132 | 24.7 | 2021-06-24 15:53:56 |
| SessionsDB | 72.86 | 133 | 99.74 | 2023-12-14 17:45:03 |
| MetricsDB | 92.66 | 459 | 79.18 | 2021-04-25 00:32:38 |
| ProfilesDB | 76.2 | 29 | 37.15 | 2021-03-21 15:50:13 |
| MetricsDB | 87.38 | 274 | 24.7 | 2023-02-15 15:38:01 |
| ProfilesDB | 80.99 | 258 | 86.2 | 2022-02-20 02:44:52 |<start>
[
    {
        "Database Name": "OrdersDB",
        "Cache Hit Ratio (%)": 84.6,
        "Connection Count": 186,
        "Average Latency (ms)": 23.7,
        "Timestamp": "2023-04-22 09:54:59"
    },
    {
        "Database Name": "AnalyticsDB",
        "Cache Hit Ratio (%)": 99.61,
        "Connection Count": 132,
        "Average Latency (ms)": 24.7,
        "Timestamp": "2021-06-24 15:53:56"
    },
    {
        "Database Name": "SessionsDB",
        "Cache Hit Ratio (%)": 72.86,
        "Connection Count": 133,
        "Average Latency (ms)": 99.74,
        "Timestamp": "2023-12-14 17:45:03"
    },
    {
        "Database Name": "MetricsDB",
        "Cache Hit Ratio (%)": 92.66,
        "Connection Count": 459,
        "Average Latency (ms)": 79.18,
        "Timestamp": "2021-04-25 00:32:38"
    },
    {
        "Database Name": "ProfilesDB",
        "Cache Hit Ratio (%)": 76.2,
        "Connection Count": 29,
        "Average Latency (ms)": 37.15,
        "Timestamp": "2021-03-21 15:50:13"
    },
    {
        "Database Name": "MetricsDB",
        "Cache Hit Ratio (%)": 87.38,
        "Connection Count": 274,
        "Average Latency (ms)": 24.7,
        "Timestamp": "2023-02-15 15:38:01"
    },
    {
        "Database Name": "ProfilesDB",
        "Cache Hit Ratio (%)": 80.99,
        "Connection Count": 258,
        "Average Latency (ms)": 86.2,
        "Timestamp": "2022-02-20 02:44:52"
    }
]
<end>Please transform the following yml data into JSON:
- Average Latency (ms): 56.36
  Cache Hit Ratio (%): 90.06
  Database Name: SalesDB
- Average Latency (ms): 41.53
  Cache Hit Ratio (%): 85.97
  Database Name: MetricsDB
- Average Latency (ms): 35.5
  Cache Hit Ratio (%): 97.11
  Database Name: UserDB
- Average Latency (ms): 75.32
  Cache Hit Ratio (%): 75.87
  Database Name: InventoryDB
- Average Latency (ms): 37.39
  Cache Hit Ratio (%): 80.06
  Database Name: AnalyticsDB
- Average Latency (ms): 69.0
  Cache Hit Ratio (%): 86.96
  Database Name: OrdersDB
<start>
[
    {
        "Database Name": "SalesDB",
        "Cache Hit Ratio (%)": 90.06,
        "Average Latency (ms)": 56.36
    },
    {
        "Database Name": "MetricsDB",
        "Cache Hit Ratio (%)": 85.97,
        "Average Latency (ms)": 41.53
    },
    {
        "Database Name": "UserDB",
        "Cache Hit Ratio (%)": 97.11,
        "Average Latency (ms)": 35.5
    },
    {
        "Database Name": "InventoryDB",
        "Cache Hit Ratio (%)": 75.87,
        "Average Latency (ms)": 75.32
    },
    {
        "Database Name": "AnalyticsDB",
        "Cache Hit Ratio (%)": 80.06,
        "Average Latency (ms)": 37.39
    },
    {
        "Database Name": "OrdersDB",
        "Cache Hit Ratio (%)": 86.96,
        "Average Latency (ms)": 69.0
    }
]
<end>Please transform the following markdown data into PLAIN TEXT:
| Restaurant Name | Rating |
| --- | --- |
| Pizza Planet | 3 |
| Taco Town | 5 |
| Curry Corner | 4 |
| Pasta Palace | 3 |
| The Golden Spoon | 1 |
| Pasta Palace | 4 |
| Pasta Palace | 2 |
| BBQ Barn | 1 |<start>
Restaurant Name: Pizza Planet | Rating: 3
Restaurant Name: Taco Town | Rating: 5
Restaurant Name: Curry Corner | Rating: 4
Restaurant Name: Pasta Palace | Rating: 3
Restaurant Name: The Golden Spoon | Rating: 1
Restaurant Name: Pasta Palace | Rating: 4
Restaurant Name: Pasta Palace | Rating: 2
Restaurant Name: BBQ Barn | Rating: 1
<end>Here's some Yaml data, can you convert it to csv?
- Close Price: 956.43
  Company: AutoMotive
  Date: '2018-02-16'
  High Price: 1449.37
  Low Price: 956.43
  Open Price: 1449.37
  Volume: 2518942
- Close Price: 1006.97
  Company: MediaGroup
  Date: '2018-11-13'
  High Price: 1006.97
  Low Price: 597.66
  Open Price: 947.6
  Volume: 8398142
- Close Price: 623.1
  Company: FoodChain
  Date: '2012-04-19'
  High Price: 1022.05
  Low Price: 195.04
  Open Price: 195.04
  Volume: 7146276
- Close Price: 947.6
  Company: MediaGroup
  Date: '2021-11-14'
  High Price: 947.6
  Low Price: 364.72
  Open Price: 597.66
  Volume: 1161256
- Close Price: 461.22
  Company: AeroSystems
  Date: '2011-06-15'
  High Price: 485.66
  Low Price: 134.15
  Open Price: 134.15
  Volume: 7146276
- Close Price: 1153.05
  Company: GreenEnergy
  Date: '2023-07-26'
  High Price: 1153.05
  Low Price: 439.93
  Open Price: 439.93
  Volume: 2527112
- Close Price: 725.73
  Company: FinanceTrust
  Date: '2017-06-05'
  High Price: 725.73
  Low Price: 103.6
  Open Price: 103.6
  Volume: 4164168
- Close Price: 439.93
  Company: TechnoCorp
  Date: '2015-10-19'
  High Price: 1442.78
  Low Price: 439.93
  Open Price: 1170.64
  Volume: 8004457
- Close Price: 851.19
  Company: TechnoCorp
  Date: '2019-05-01'
  High Price: 880.93
  Low Price: 565.88
  Open Price: 880.93
  Volume: 3554179
<start>
Company,Date,Open Price,Close Price,High Price,Low Price,Volume
AutoMotive,2018-02-16,1449.37,956.43,1449.37,956.43,2518942
MediaGroup,2018-11-13,947.6,1006.97,1006.97,597.66,8398142
FoodChain,2012-04-19,195.04,623.1,1022.05,195.04,7146276
MediaGroup,2021-11-14,597.66,947.6,947.6,364.72,1161256
AeroSystems,2011-06-15,134.15,461.22,485.66,134.15,7146276
GreenEnergy,2023-07-26,439.93,1153.05,1153.05,439.93,2527112
FinanceTrust,2017-06-05,103.6,725.73,725.73,103.6,4164168
TechnoCorp,2015-10-19,1170.64,439.93,1442.78,439.93,8004457
TechnoCorp,2019-05-01,880.93,851.19,880.93,565.88,3554179
<end>Convert this yml to csv:
- Cuisine: American
  Location: Seattle
- Cuisine: Chinese
  Location: Phoenix
- Cuisine: Italian
  Location: Seattle
- Cuisine: Italian
  Location: New York
- Cuisine: Indian
  Location: Miami
- Cuisine: Mediterranean
  Location: Houston
- Cuisine: Indian
  Location: Miami
<start>
Cuisine,Location
American,Seattle
Chinese,Phoenix
Italian,Seattle
Italian,New York
Indian,Miami
Mediterranean,Houston
Indian,Miami
<end>Here's some csv data, can you convert it to Yml?
Condition,Temperature (C),Humidity (%),Wind Speed (km/h)
Foggy,25.6,56,22.6
Cloudy,34.6,81,23.9
Cloudy,37.7,65,22.8
Foggy,22.3,30,5.2
Stormy,35.4,72,11.7
Windy,20.0,47,0.6
Sunny,17.4,74,23.9
Stormy,37.7,36,25.7
Foggy,3.4,42,4.5
<start>
- Condition: Foggy
  Humidity (%): 56
  Temperature (C): 25.6
  Wind Speed (km/h): 22.6
- Condition: Cloudy
  Humidity (%): 81
  Temperature (C): 34.6
  Wind Speed (km/h): 23.9
- Condition: Cloudy
  Humidity (%): 65
  Temperature (C): 37.7
  Wind Speed (km/h): 22.8
- Condition: Foggy
  Humidity (%): 30
  Temperature (C): 22.3
  Wind Speed (km/h): 5.2
- Condition: Stormy
  Humidity (%): 72
  Temperature (C): 35.4
  Wind Speed (km/h): 11.7
- Condition: Windy
  Humidity (%): 47
  Temperature (C): 20.0
  Wind Speed (km/h): 0.6
- Condition: Sunny
  Humidity (%): 74
  Temperature (C): 17.4
  Wind Speed (km/h): 23.9
- Condition: Stormy
  Humidity (%): 36
  Temperature (C): 37.7
  Wind Speed (km/h): 25.7
- Condition: Foggy
  Humidity (%): 42
  Temperature (C): 3.4
  Wind Speed (km/h): 4.5
<end>Transform this json structure to a MARKDOWN format:
[
    {
        "Company": "TechnoCorp",
        "Date": "2019-09-04",
        "Open Price": 737.87,
        "Close Price": 660.63,
        "High Price": 737.87,
        "Low Price": 499.81
    },
    {
        "Company": "MediaGroup",
        "Date": "2013-06-02",
        "Open Price": 1275.17,
        "Close Price": 285.71,
        "High Price": 1275.17,
        "Low Price": 285.71
    },
    {
        "Company": "BioLife",
        "Date": "2011-03-06",
        "Open Price": 186.48,
        "Close Price": 923.4,
        "High Price": 923.4,
        "Low Price": 186.48
    },
    {
        "Company": "GreenEnergy",
        "Date": "2013-09-27",
        "Open Price": 1323.5,
        "Close Price": 1303.77,
        "High Price": 1323.5,
        "Low Price": 1089.86
    },
    {
        "Company": "GreenEnergy",
        "Date": "2021-09-02",
        "Open Price": 285.71,
        "Close Price": 1041.72,
        "High Price": 1041.72,
        "Low Price": 285.71
    },
    {
        "Company": "HealthGen",
        "Date": "2023-04-09",
        "Open Price": 486.77,
        "Close Price": 1366.2,
        "High Price": 1366.2,
        "Low Price": 486.77
    },
    {
        "Company": "FinanceTrust",
        "Date": "2016-11-09",
        "Open Price": 251.89,
        "Close Price": 548.99,
        "High Price": 1119.65,
        "Low Price": 251.89
    },
    {
        "Company": "AutoMotive",
        "Date": "2015-06-15",
        "Open Price": 900.37,
        "Close Price": 923.4,
        "High Price": 923.4,
        "Low Price": 446.33
    },
    {
        "Company": "GreenEnergy",
        "Date": "2023-12-20",
        "Open Price": 634.47,
        "Close Price": 548.99,
        "High Price": 634.47,
        "Low Price": 548.99
    },
    {
        "Company": "GreenEnergy",
        "Date": "2022-03-12",
        "Open Price": 652.58,
        "Close Price": 952.2,
        "High Price": 952.2,
        "Low Price": 652.58
    }
]<start>
| Company | Date | Open Price | Close Price | High Price | Low Price |
| --- | --- | --- | --- | --- | --- |
| TechnoCorp | 2019-09-04 | 737.87 | 660.63 | 737.87 | 499.81 |
| MediaGroup | 2013-06-02 | 1275.17 | 285.71 | 1275.17 | 285.71 |
| BioLife | 2011-03-06 | 186.48 | 923.4 | 923.4 | 186.48 |
| GreenEnergy | 2013-09-27 | 1323.5 | 1303.77 | 1323.5 | 1089.86 |
| GreenEnergy | 2021-09-02 | 285.71 | 1041.72 | 1041.72 | 285.71 |
| HealthGen | 2023-04-09 | 486.77 | 1366.2 | 1366.2 | 486.77 |
| FinanceTrust | 2016-11-09 | 251.89 | 548.99 | 1119.65 | 251.89 |
| AutoMotive | 2015-06-15 | 900.37 | 923.4 | 923.4 | 446.33 |
| GreenEnergy | 2023-12-20 | 634.47 | 548.99 | 634.47 | 548.99 |
| GreenEnergy | 2022-03-12 | 652.58 | 952.2 | 952.2 | 652.58 |
<end>Transform this Json structure to a Plain text format:
[
    {
        "Device ID": "device-0056",
        "Device Type": "Temperature Sensor",
        "Reading Value": 19.92,
        "Timestamp": "2021-08-04 09:10:29"
    },
    {
        "Device ID": "device-0043",
        "Device Type": "Pressure Sensor",
        "Reading Value": 71.96,
        "Timestamp": "2021-05-18 02:02:46"
    },
    {
        "Device ID": "device-0011",
        "Device Type": "Temperature Sensor",
        "Reading Value": 22.12,
        "Timestamp": "2021-08-08 10:20:08"
    },
    {
        "Device ID": "device-0077",
        "Device Type": "Pressure Sensor",
        "Reading Value": -21.84,
        "Timestamp": "2022-11-11 07:04:21"
    },
    {
        "Device ID": "device-0008",
        "Device Type": "Pressure Sensor",
        "Reading Value": 42.16,
        "Timestamp": "2022-06-03 10:19:06"
    },
    {
        "Device ID": "device-0052",
        "Device Type": "Motion Detector",
        "Reading Value": -22.18,
        "Timestamp": "2023-04-04 04:12:48"
    },
    {
        "Device ID": "device-0099",
        "Device Type": "Temperature Sensor",
        "Reading Value": 66.12,
        "Timestamp": "2021-03-01 17:12:32"
    },
    {
        "Device ID": "device-0008",
        "Device Type": "Temperature Sensor",
        "Reading Value": 50.18,
        "Timestamp": "2022-08-07 06:51:52"
    }
]<start>
Device ID: device-0056 | Device Type: Temperature Sensor | Reading Value: 19.92 | Timestamp: 2021-08-04 09:10:29
Device ID: device-0043 | Device Type: Pressure Sensor | Reading Value: 71.96 | Timestamp: 2021-05-18 02:02:46
Device ID: device-0011 | Device Type: Temperature Sensor | Reading Value: 22.12 | Timestamp: 2021-08-08 10:20:08
Device ID: device-0077 | Device Type: Pressure Sensor | Reading Value: -21.84 | Timestamp: 2022-11-11 07:04:21
Device ID: device-0008 | Device Type: Pressure Sensor | Reading Value: 42.16 | Timestamp: 2022-06-03 10:19:06
Device ID: device-0052 | Device Type: Motion Detector | Reading Value: -22.18 | Timestamp: 2023-04-04 04:12:48
Device ID: device-0099 | Device Type: Temperature Sensor | Reading Value: 66.12 | Timestamp: 2021-03-01 17:12:32
Device ID: device-0008 | Device Type: Temperature Sensor | Reading Value: 50.18 | Timestamp: 2022-08-07 06:51:52
<end>Convert this MARKDOWN to plain text:
| Company | Close Price | High Price | Low Price |
| --- | --- | --- | --- |
| GreenEnergy | 1118.37 | 1118.37 | 332.77 |
| HealthGen | 1388.08 | 1388.08 | 1275.58 |
| MediaGroup | 1368.39 | 1368.39 | 935.74 |
| GreenEnergy | 386.86 | 1210.06 | 386.86 |
| FoodChain | 1275.58 | 1275.58 | 321.14 |
| FoodChain | 892.38 | 892.38 | 35.89 |
| RetailWorld | 1275.58 | 1275.58 | 721.03 |
| FoodChain | 952.24 | 1468.32 | 714.84 |
| FoodChain | 1071.03 | 1071.03 | 961.62 |
| TechnoCorp | 952.24 | 1249.89 | 387.79 |<start>
Company: GreenEnergy | Close Price: 1118.37 | High Price: 1118.37 | Low Price: 332.77
Company: HealthGen | Close Price: 1388.08 | High Price: 1388.08 | Low Price: 1275.58
Company: MediaGroup | Close Price: 1368.39 | High Price: 1368.39 | Low Price: 935.74
Company: GreenEnergy | Close Price: 386.86 | High Price: 1210.06 | Low Price: 386.86
Company: FoodChain | Close Price: 1275.58 | High Price: 1275.58 | Low Price: 321.14
Company: FoodChain | Close Price: 892.38 | High Price: 892.38 | Low Price: 35.89
Company: RetailWorld | Close Price: 1275.58 | High Price: 1275.58 | Low Price: 721.03
Company: FoodChain | Close Price: 952.24 | High Price: 1468.32 | Low Price: 714.84
Company: FoodChain | Close Price: 1071.03 | High Price: 1071.03 | Low Price: 961.62
Company: TechnoCorp | Close Price: 952.24 | High Price: 1249.89 | Low Price: 387.79
<end>Transform this yml structure to a MARKDOWN format:
- Age: 43
  Birth Month: October
  City: San Francisco
  Income: 300000
  Name: Patti
- Age: 34
  Birth Month: November
  City: Charlotte
  Income: 125000
  Name: Estelle
- Age: 43
  Birth Month: September
  City: Phoenix
  Income: 135000
  Name: Gloria
- Age: 40
  Birth Month: December
  City: El Paso
  Income: 90000
  Name: Kiara
- Age: 55
  Birth Month: July
  City: Denver
  Income: 60000
  Name: Gloria
- Age: 36
  Birth Month: May
  City: Austin
  Income: 280000
  Name: Tara
- Age: 55
  Birth Month: May
  City: Indianapolis
  Income: 200000
  Name: Tucker
- Age: 24
  Birth Month: August
  City: Washington
  Income: 435000
  Name: Bobbie
- Age: 42
  Birth Month: March
  City: Nashville
  Income: 355000
  Name: Leila
- Age: 58
  Birth Month: January
  City: Phoenix
  Income: 215000
  Name: Dianne
<start>
| Name | Age | Birth Month | City | Income |
| --- | --- | --- | --- | --- |
| Patti | 43 | October | San Francisco | 300000 |
| Estelle | 34 | November | Charlotte | 125000 |
| Gloria | 43 | September | Phoenix | 135000 |
| Kiara | 40 | December | El Paso | 90000 |
| Gloria | 55 | July | Denver | 60000 |
| Tara | 36 | May | Austin | 280000 |
| Tucker | 55 | May | Indianapolis | 200000 |
| Bobbie | 24 | August | Washington | 435000 |
| Leila | 42 | March | Nashville | 355000 |
| Dianne | 58 | January | Phoenix | 215000 |
<end>Convert this json to Csv:
[
    {
        "Product Name": "Doohickey",
        "SKU": "SKU-1036",
        "Price": 199.13,
        "Category": "Toys"
    },
    {
        "Product Name": "Device",
        "SKU": "SKU-1061",
        "Price": 302.71,
        "Category": "Automotive"
    },
    {
        "Product Name": "Apparatus",
        "SKU": "SKU-1087",
        "Price": 130.99,
        "Category": "Electronics"
    },
    {
        "Product Name": "Widget",
        "SKU": "SKU-1019",
        "Price": 202.42,
        "Category": "Household"
    }
]<start>
Product Name,SKU,Price,Category
Doohickey,SKU-1036,199.13,Toys
Device,SKU-1061,302.71,Automotive
Apparatus,SKU-1087,130.99,Electronics
Widget,SKU-1019,202.42,Household
<end>Can you change this markdown into yml?
| Start Location | Distance (miles) | Duration (hours) |
| --- | --- | --- |
| Miami | 2316.3 | 57.3 |
| Chicago | 1541.3 | 62.1 |
| Denver | 911.0 | 40.2 |<start>
- Distance (miles): 2316.3
  Duration (hours): 57.3
  Start Location: Miami
- Distance (miles): 1541.3
  Duration (hours): 62.1
  Start Location: Chicago
- Distance (miles): 911.0
  Duration (hours): 40.2
  Start Location: Denver
<end>Transform this Yml structure to a json format:
- Genre: Thriller
  Publication Year: 1978
  Rating: 3.4
  Title: Shadows of Solitude
- Genre: Historical
  Publication Year: 1968
  Rating: 1.2
  Title: The Silent Grove
- Genre: Horror
  Publication Year: 2012
  Rating: 3.8
  Title: The Silent Grove
- Genre: Romance
  Publication Year: 1973
  Rating: 4.3
  Title: The Crystal Key
- Genre: Fantasy
  Publication Year: 2011
  Rating: 4.5
  Title: Shadows of Solitude
- Genre: Non-Fiction
  Publication Year: 2017
  Rating: 2.3
  Title: The Forgotten World
<start>
[
    {
        "Title": "Shadows of Solitude",
        "Genre": "Thriller",
        "Publication Year": 1978,
        "Rating": 3.4
    },
    {
        "Title": "The Silent Grove",
        "Genre": "Historical",
        "Publication Year": 1968,
        "Rating": 1.2
    },
    {
        "Title": "The Silent Grove",
        "Genre": "Horror",
        "Publication Year": 2012,
        "Rating": 3.8
    },
    {
        "Title": "The Crystal Key",
        "Genre": "Romance",
        "Publication Year": 1973,
        "Rating": 4.3
    },
    {
        "Title": "Shadows of Solitude",
        "Genre": "Fantasy",
        "Publication Year": 2011,
        "Rating": 4.5
    },
    {
        "Title": "The Forgotten World",
        "Genre": "Non-Fiction",
        "Publication Year": 2017,
        "Rating": 2.3
    }
]
<end>Transform this plain text structure to a YML format:
Database Name: ProfilesDB | Queries per Second: 2993.8 | Cache Hit Ratio (%): 88.4 | Connection Count: 131
Database Name: OrdersDB | Queries per Second: 1153.85 | Cache Hit Ratio (%): 90.59 | Connection Count: 494
Database Name: LogsDB | Queries per Second: 2553.06 | Cache Hit Ratio (%): 70.54 | Connection Count: 389
Database Name: ProfilesDB | Queries per Second: 3874.19 | Cache Hit Ratio (%): 89.52 | Connection Count: 389
Database Name: SessionsDB | Queries per Second: 500.39 | Cache Hit Ratio (%): 97.14 | Connection Count: 63
Database Name: UserDB | Queries per Second: 1252.06 | Cache Hit Ratio (%): 89.06 | Connection Count: 500
Database Name: LogsDB | Queries per Second: 2134.94 | Cache Hit Ratio (%): 97.14 | Connection Count: 16
Database Name: MetricsDB | Queries per Second: 3915.96 | Cache Hit Ratio (%): 72.83 | Connection Count: 226
Database Name: LogsDB | Queries per Second: 3982.64 | Cache Hit Ratio (%): 92.42 | Connection Count: 16
Database Name: LogsDB | Queries per Second: 744.23 | Cache Hit Ratio (%): 83.85 | Connection Count: 21
<start>
- Cache Hit Ratio (%): 88.4
  Connection Count: 131
  Database Name: ProfilesDB
  Queries per Second: 2993.8
- Cache Hit Ratio (%): 90.59
  Connection Count: 494
  Database Name: OrdersDB
  Queries per Second: 1153.85
- Cache Hit Ratio (%): 70.54
  Connection Count: 389
  Database Name: LogsDB
  Queries per Second: 2553.06
- Cache Hit Ratio (%): 89.52
  Connection Count: 389
  Database Name: ProfilesDB
  Queries per Second: 3874.19
- Cache Hit Ratio (%): 97.14
  Connection Count: 63
  Database Name: SessionsDB
  Queries per Second: 500.39
- Cache Hit Ratio (%): 89.06
  Connection Count: 500
  Database Name: UserDB
  Queries per Second: 1252.06
- Cache Hit Ratio (%): 97.14
  Connection Count: 16
  Database Name: LogsDB
  Queries per Second: 2134.94
- Cache Hit Ratio (%): 72.83
  Connection Count: 226
  Database Name: MetricsDB
  Queries per Second: 3915.96
- Cache Hit Ratio (%): 92.42
  Connection Count: 16
  Database Name: LogsDB
  Queries per Second: 3982.64
- Cache Hit Ratio (%): 83.85
  Connection Count: 21
  Database Name: LogsDB
  Queries per Second: 744.23
<end>Please transform the following CSV data into yml:
Title,Release Year,Box Office Earnings (M)
The Great Expedition,1974,379.75
The Endless Horizon,1976,506.05
Starbound Odyssey,1994,606.79
Beyond the Veil,1987,200.12
Dreamwalker,2005,907.49
The Great Expedition,2001,66.22
The Endless Horizon,2009,218.63
Rise of the Titans,2009,60.28
Mystery of the Depths,2020,892.35
Beyond the Veil,1999,288.65
<start>
- Box Office Earnings (M): 379.75
  Release Year: 1974
  Title: The Great Expedition
- Box Office Earnings (M): 506.05
  Release Year: 1976
  Title: The Endless Horizon
- Box Office Earnings (M): 606.79
  Release Year: 1994
  Title: Starbound Odyssey
- Box Office Earnings (M): 200.12
  Release Year: 1987
  Title: Beyond the Veil
- Box Office Earnings (M): 907.49
  Release Year: 2005
  Title: Dreamwalker
- Box Office Earnings (M): 66.22
  Release Year: 2001
  Title: The Great Expedition
- Box Office Earnings (M): 218.63
  Release Year: 2009
  Title: The Endless Horizon
- Box Office Earnings (M): 60.28
  Release Year: 2009
  Title: Rise of the Titans
- Box Office Earnings (M): 892.35
  Release Year: 2020
  Title: Mystery of the Depths
- Box Office Earnings (M): 288.65
  Release Year: 1999
  Title: Beyond the Veil
<end>Here's some Csv data, can you convert it to PLAIN TEXT?
Product Name,SKU,Price,Stock Quantity,Category,Supplier Name
Whatchamacallit,SKU-1086,414.61,494,Electronics,Wonka Industries
Gizmo,SKU-1050,63.43,236,Toys,Wonka Industries
Apparatus,SKU-1000,152.96,454,Automotive,Globex
Instrument,SKU-1026,198.88,276,Electronics,ACME Corp
Thingamajig,SKU-1093,332.92,106,Toys,ACME Corp
Contraption,SKU-1005,116.32,135,Automotive,Wonka Industries
Widget,SKU-1027,489.01,365,Automotive,ACME Corp
<start>
Product Name: Whatchamacallit | SKU: SKU-1086 | Price: 414.61 | Stock Quantity: 494 | Category: Electronics | Supplier Name: Wonka Industries
Product Name: Gizmo | SKU: SKU-1050 | Price: 63.43 | Stock Quantity: 236 | Category: Toys | Supplier Name: Wonka Industries
Product Name: Apparatus | SKU: SKU-1000 | Price: 152.96 | Stock Quantity: 454 | Category: Automotive | Supplier Name: Globex
Product Name: Instrument | SKU: SKU-1026 | Price: 198.88 | Stock Quantity: 276 | Category: Electronics | Supplier Name: ACME Corp
Product Name: Thingamajig | SKU: SKU-1093 | Price: 332.92 | Stock Quantity: 106 | Category: Toys | Supplier Name: ACME Corp
Product Name: Contraption | SKU: SKU-1005 | Price: 116.32 | Stock Quantity: 135 | Category: Automotive | Supplier Name: Wonka Industries
Product Name: Widget | SKU: SKU-1027 | Price: 489.01 | Stock Quantity: 365 | Category: Automotive | Supplier Name: ACME Corp
<end>Can you change this csv into json?
Title,Genre,Publication Year,Rating
The Silent Grove,Romance,2019,2.1
The Last Sky,Science Fiction,2013,3.2
The Last Sky,Science Fiction,1996,1.8
A Journey Through Time,Thriller,1996,1.6
<start>
[
    {
        "Title": "The Silent Grove",
        "Genre": "Romance",
        "Publication Year": 2019,
        "Rating": 2.1
    },
    {
        "Title": "The Last Sky",
        "Genre": "Science Fiction",
        "Publication Year": 2013,
        "Rating": 3.2
    },
    {
        "Title": "The Last Sky",
        "Genre": "Science Fiction",
        "Publication Year": 1996,
        "Rating": 1.8
    },
    {
        "Title": "A Journey Through Time",
        "Genre": "Thriller",
        "Publication Year": 1996,
        "Rating": 1.6
    }
]
<end>Please transform the following markdown data into Yaml:
| Location | Condition | Temperature (C) | Humidity (%) | Wind Speed (km/h) | Day |
| --- | --- | --- | --- | --- | --- |
| Seattle | Stormy | -1.8 | 82 | 4.6 | Monday |
| Chicago | Stormy | 10.0 | 53 | 13.4 | Saturday |
| Denver | Sunny | 35.8 | 31 | 13.4 | Thursday |
| New York | Snowy | 15.3 | 70 | 0.4 | Monday |
| Phoenix | Sunny | 0.5 | 66 | 28.6 | Wednesday |<start>
- Condition: Stormy
  Day: Monday
  Humidity (%): 82
  Location: Seattle
  Temperature (C): -1.8
  Wind Speed (km/h): 4.6
- Condition: Stormy
  Day: Saturday
  Humidity (%): 53
  Location: Chicago
  Temperature (C): 10.0
  Wind Speed (km/h): 13.4
- Condition: Sunny
  Day: Thursday
  Humidity (%): 31
  Location: Denver
  Temperature (C): 35.8
  Wind Speed (km/h): 13.4
- Condition: Snowy
  Day: Monday
  Humidity (%): 70
  Location: New York
  Temperature (C): 15.3
  Wind Speed (km/h): 0.4
- Condition: Sunny
  Day: Wednesday
  Humidity (%): 66
  Location: Phoenix
  Temperature (C): 0.5
  Wind Speed (km/h): 28.6
<end>Transform this markdown structure to a plain text format:
| Device ID | Location | Battery Level (%) | Reading Value |
| --- | --- | --- | --- |
| device-0042 | Bedroom | 27.9 | -10.64 |
| device-0042 | Office | 30.4 | -2.57 |
| device-0005 | Hallway | 41.3 | 75.57 |
| device-0066 | Garden | 86.7 | 43.38 |
| device-0098 | Garden | 14.9 | 16.98 |
| device-0041 | Bathroom | 74.7 | -23.11 |
| device-0025 | Bathroom | 63.2 | 66.82 |
| device-0063 | Garden | 63.2 | -4.98 |
| device-0025 | Bathroom | 47.9 | 74.57 |
| device-0001 | Office | 84.7 | 63.52 |<start>
Device ID: device-0042 | Location: Bedroom | Battery Level (%): 27.9 | Reading Value: -10.64
Device ID: device-0042 | Location: Office | Battery Level (%): 30.4 | Reading Value: -2.57
Device ID: device-0005 | Location: Hallway | Battery Level (%): 41.3 | Reading Value: 75.57
Device ID: device-0066 | Location: Garden | Battery Level (%): 86.7 | Reading Value: 43.38
Device ID: device-0098 | Location: Garden | Battery Level (%): 14.9 | Reading Value: 16.98
Device ID: device-0041 | Location: Bathroom | Battery Level (%): 74.7 | Reading Value: -23.11
Device ID: device-0025 | Location: Bathroom | Battery Level (%): 63.2 | Reading Value: 66.82
Device ID: device-0063 | Location: Garden | Battery Level (%): 63.2 | Reading Value: -4.98
Device ID: device-0025 | Location: Bathroom | Battery Level (%): 47.9 | Reading Value: 74.57
Device ID: device-0001 | Location: Office | Battery Level (%): 84.7 | Reading Value: 63.52
<end>Here's some Csv data, can you convert it to json?
Location,Condition,Temperature (C),Wind Speed (km/h),Day
Chicago,Rainy,22.7,21.7,Thursday
Denver,Rainy,6.4,18.5,Sunday
Denver,Foggy,1.0,18.9,Sunday
<start>
[
    {
        "Location": "Chicago",
        "Condition": "Rainy",
        "Temperature (C)": 22.7,
        "Wind Speed (km/h)": 21.7,
        "Day": "Thursday"
    },
    {
        "Location": "Denver",
        "Condition": "Rainy",
        "Temperature (C)": 6.4,
        "Wind Speed (km/h)": 18.5,
        "Day": "Sunday"
    },
    {
        "Location": "Denver",
        "Condition": "Foggy",
        "Temperature (C)": 1.0,
        "Wind Speed (km/h)": 18.9,
        "Day": "Sunday"
    }
]
<end>Please transform the following markdown data into Yml:
| Name | Age | Birth Month | City | Income |
| --- | --- | --- | --- | --- |
| Sylvia | 40 | July | Austin | 25000 |
| Claudia | 57 | February | Charlotte | 370000 |
| Linda | 29 | October | Washington | 100000 |
| Sharon | 49 | April | Portland | 320000 |
| Birdie | 38 | June | Denver | 275000 |
| Rick | 50 | September | Milwaukee | 295000 |
| Ann | 68 | October | San Francisco | 135000 |
| Donna | 29 | January | Las Vegas | 380000 |<start>
- Age: 40
  Birth Month: July
  City: Austin
  Income: 25000
  Name: Sylvia
- Age: 57
  Birth Month: February
  City: Charlotte
  Income: 370000
  Name: Claudia
- Age: 29
  Birth Month: October
  City: Washington
  Income: 100000
  Name: Linda
- Age: 49
  Birth Month: April
  City: Portland
  Income: 320000
  Name: Sharon
- Age: 38
  Birth Month: June
  City: Denver
  Income: 275000
  Name: Birdie
- Age: 50
  Birth Month: September
  City: Milwaukee
  Income: 295000
  Name: Rick
- Age: 68
  Birth Month: October
  City: San Francisco
  Income: 135000
  Name: Ann
- Age: 29
  Birth Month: January
  City: Las Vegas
  Income: 380000
  Name: Donna
<end>Please transform the following Csv data into plain text:
Author,Genre,Publication Year
Luna Silverleaf,Historical,1986
Galen Starfire,Thriller,1975
Elara Moonshadow,Romance,2006
Luna Silverleaf,Thriller,1975
Rowan Ashborne,Mystery,2010
Orion Frostblade,Science Fiction,1964
Orion Frostblade,Non-Fiction,1975
Luna Silverleaf,Mystery,1977
Kara Firebrand,Science Fiction,2020
Kara Firebrand,Romance,2023
<start>
Author: Luna Silverleaf | Genre: Historical | Publication Year: 1986
Author: Galen Starfire | Genre: Thriller | Publication Year: 1975
Author: Elara Moonshadow | Genre: Romance | Publication Year: 2006
Author: Luna Silverleaf | Genre: Thriller | Publication Year: 1975
Author: Rowan Ashborne | Genre: Mystery | Publication Year: 2010
Author: Orion Frostblade | Genre: Science Fiction | Publication Year: 1964
Author: Orion Frostblade | Genre: Non-Fiction | Publication Year: 1975
Author: Luna Silverleaf | Genre: Mystery | Publication Year: 1977
Author: Kara Firebrand | Genre: Science Fiction | Publication Year: 2020
Author: Kara Firebrand | Genre: Romance | Publication Year: 2023
<end>Please transform the following markdown data into yml:
| Company | Date | Open Price | Close Price | High Price | Low Price | Volume |
| --- | --- | --- | --- | --- | --- | --- |
| AutoMotive | 2021-07-21 | 269.11 | 391.17 | 1018.08 | 269.11 | 9408769 |
| HealthGen | 2013-03-05 | 902.84 | 337.42 | 902.84 | 337.42 | 8000103 |
| AeroSystems | 2017-08-23 | 1018.08 | 472.64 | 1018.08 | 472.64 | 9169946 |<start>
- Close Price: 391.17
  Company: AutoMotive
  Date: '2021-07-21'
  High Price: 1018.08
  Low Price: 269.11
  Open Price: 269.11
  Volume: 9408769
- Close Price: 337.42
  Company: HealthGen
  Date: '2013-03-05'
  High Price: 902.84
  Low Price: 337.42
  Open Price: 902.84
  Volume: 8000103
- Close Price: 472.64
  Company: AeroSystems
  Date: '2017-08-23'
  High Price: 1018.08
  Low Price: 472.64
  Open Price: 1018.08
  Volume: 9169946
<end>Transform this Markdown structure to a Json format:
| Name | Age | Birth Month | City | Income |
| --- | --- | --- | --- | --- |
| Arthur | 56 | January | Portland | 35000 |
| Lloyd | 60 | October | Detroit | 30000 |
| Rosemary | 62 | July | Jacksonville | 435000 |
| Kimberly | 68 | December | Detroit | 485000 |
| Regina | 39 | May | Seattle | 170000 |
| Willow | 19 | May | Charlotte | 365000 |
| Bertie | 69 | January | Charlotte | 150000 |
| Eugene | 36 | August | Fort Worth | 270000 |
| Charlene | 69 | August | San Antonio | 170000 |
| Faith | 42 | October | Jacksonville | 120000 |<start>
[
    {
        "Name": "Arthur",
        "Age": 56,
        "Birth Month": "January",
        "City": "Portland",
        "Income": 35000
    },
    {
        "Name": "Lloyd",
        "Age": 60,
        "Birth Month": "October",
        "City": "Detroit",
        "Income": 30000
    },
    {
        "Name": "Rosemary",
        "Age": 62,
        "Birth Month": "July",
        "City": "Jacksonville",
        "Income": 435000
    },
    {
        "Name": "Kimberly",
        "Age": 68,
        "Birth Month": "December",
        "City": "Detroit",
        "Income": 485000
    },
    {
        "Name": "Regina",
        "Age": 39,
        "Birth Month": "May",
        "City": "Seattle",
        "Income": 170000
    },
    {
        "Name": "Willow",
        "Age": 19,
        "Birth Month": "May",
        "City": "Charlotte",
        "Income": 365000
    },
    {
        "Name": "Bertie",
        "Age": 69,
        "Birth Month": "January",
        "City": "Charlotte",
        "Income": 150000
    },
    {
        "Name": "Eugene",
        "Age": 36,
        "Birth Month": "August",
        "City": "Fort Worth",
        "Income": 270000
    },
    {
        "Name": "Charlene",
        "Age": 69,
        "Birth Month": "August",
        "City": "San Antonio",
        "Income": 170000
    },
    {
        "Name": "Faith",
        "Age": 42,
        "Birth Month": "October",
        "City": "Jacksonville",
        "Income": 120000
    }
]
<end>Please transform the following markdown data into YAML:
| Name | Birth Month | Income |
| --- | --- | --- |
| Craig | December | 370000 |
| Belle | June | 145000 |
| Jill | August | 205000 |
| Giovanni | July | 110000 |
| Emil | May | 225000 |
| Nelson | October | 200000 |
| Henrietta | December | 35000 |
| Hudson | February | 55000 |
| Kaiden | March | 430000 |
| Salvatore | May | 485000 |<start>
- Birth Month: December
  Income: 370000
  Name: Craig
- Birth Month: June
  Income: 145000
  Name: Belle
- Birth Month: August
  Income: 205000
  Name: Jill
- Birth Month: July
  Income: 110000
  Name: Giovanni
- Birth Month: May
  Income: 225000
  Name: Emil
- Birth Month: October
  Income: 200000
  Name: Nelson
- Birth Month: December
  Income: 35000
  Name: Henrietta
- Birth Month: February
  Income: 55000
  Name: Hudson
- Birth Month: March
  Income: 430000
  Name: Kaiden
- Birth Month: May
  Income: 485000
  Name: Salvatore
<end>Here's some Csv data, can you convert it to Markdown?
Device Type,Battery Level (%),Reading Value
Temperature Sensor,13.2,-12.31
Motion Detector,84.3,64.08
Light Sensor,31.2,-5.64
Humidity Sensor,60.1,18.36
Temperature Sensor,41.1,33.14
Light Sensor,79.8,-12.31
Humidity Sensor,83.2,44.55
<start>
| Device Type | Battery Level (%) | Reading Value |
| --- | --- | --- |
| Temperature Sensor | 13.2 | -12.31 |
| Motion Detector | 84.3 | 64.08 |
| Light Sensor | 31.2 | -5.64 |
| Humidity Sensor | 60.1 | 18.36 |
| Temperature Sensor | 41.1 | 33.14 |
| Light Sensor | 79.8 | -12.31 |
| Humidity Sensor | 83.2 | 44.55 |
<end>Please transform the following json data into Plain text:
[
    {
        "Name": "Lizzie",
        "Age": 68,
        "Birth Month": "June",
        "City": "New York",
        "Income": 165000
    },
    {
        "Name": "Joann",
        "Age": 57,
        "Birth Month": "January",
        "City": "Houston",
        "Income": 200000
    },
    {
        "Name": "Kaleb",
        "Age": 61,
        "Birth Month": "March",
        "City": "Memphis",
        "Income": 370000
    },
    {
        "Name": "Julian",
        "Age": 28,
        "Birth Month": "September",
        "City": "Washington",
        "Income": 385000
    },
    {
        "Name": "Monica",
        "Age": 27,
        "Birth Month": "January",
        "City": "San Antonio",
        "Income": 180000
    },
    {
        "Name": "Sheryl",
        "Age": 61,
        "Birth Month": "April",
        "City": "Washington",
        "Income": 160000
    },
    {
        "Name": "June",
        "Age": 51,
        "Birth Month": "August",
        "City": "Boston",
        "Income": 360000
    },
    {
        "Name": "Antoinette",
        "Age": 68,
        "Birth Month": "January",
        "City": "Phoenix",
        "Income": 370000
    }
]<start>
Name: Lizzie | Age: 68 | Birth Month: June | City: New York | Income: 165000
Name: Joann | Age: 57 | Birth Month: January | City: Houston | Income: 200000
Name: Kaleb | Age: 61 | Birth Month: March | City: Memphis | Income: 370000
Name: Julian | Age: 28 | Birth Month: September | City: Washington | Income: 385000
Name: Monica | Age: 27 | Birth Month: January | City: San Antonio | Income: 180000
Name: Sheryl | Age: 61 | Birth Month: April | City: Washington | Income: 160000
Name: June | Age: 51 | Birth Month: August | City: Boston | Income: 360000
Name: Antoinette | Age: 68 | Birth Month: January | City: Phoenix | Income: 370000
<end>Convert this yaml to Markdown:
- Connection Count: 90
  Database Name: MetricsDB
  Timestamp: '2021-09-04 07:02:04'
- Connection Count: 126
  Database Name: SalesDB
  Timestamp: '2022-04-14 21:32:48'
- Connection Count: 24
  Database Name: OrdersDB
  Timestamp: '2022-10-24 01:29:08'
- Connection Count: 493
  Database Name: MetricsDB
  Timestamp: '2022-03-01 07:47:42'
- Connection Count: 320
  Database Name: ProductsDB
  Timestamp: '2021-11-19 15:05:37'
- Connection Count: 122
  Database Name: SessionsDB
  Timestamp: '2022-10-13 02:44:18'
<start>
| Database Name | Connection Count | Timestamp |
| --- | --- | --- |
| MetricsDB | 90 | 2021-09-04 07:02:04 |
| SalesDB | 126 | 2022-04-14 21:32:48 |
| OrdersDB | 24 | 2022-10-24 01:29:08 |
| MetricsDB | 493 | 2022-03-01 07:47:42 |
| ProductsDB | 320 | 2021-11-19 15:05:37 |
| SessionsDB | 122 | 2022-10-13 02:44:18 |
<end>Transform this Csv structure to a MARKDOWN format:
Product Name,SKU,Stock Quantity,Category,Supplier Name
Widget,SKU-1012,258,Sports,Umbrella Corp
Widget,SKU-1026,483,Household,ACME Corp
Instrument,SKU-1091,286,Toys,Umbrella Corp
Contraption,SKU-1017,386,Automotive,ACME Corp
Whatchamacallit,SKU-1078,58,Electronics,Umbrella Corp
Gizmo,SKU-1016,298,Electronics,Wayne Enterprises
Instrument,SKU-1007,314,Household,ACME Corp
<start>
| Product Name | SKU | Stock Quantity | Category | Supplier Name |
| --- | --- | --- | --- | --- |
| Widget | SKU-1012 | 258 | Sports | Umbrella Corp |
| Widget | SKU-1026 | 483 | Household | ACME Corp |
| Instrument | SKU-1091 | 286 | Toys | Umbrella Corp |
| Contraption | SKU-1017 | 386 | Automotive | ACME Corp |
| Whatchamacallit | SKU-1078 | 58 | Electronics | Umbrella Corp |
| Gizmo | SKU-1016 | 298 | Electronics | Wayne Enterprises |
| Instrument | SKU-1007 | 314 | Household | ACME Corp |
<end>Please transform the following CSV data into yml:
Date,Close Price,High Price,Low Price,Volume
2022-01-24,1456.28,1456.28,463.81,3894053
2010-04-10,732.3,1075.02,20.91,3867672
2021-05-19,1043.97,1043.97,267.63,4580859
2016-02-27,904.34,1321.1,693.61,8501816
2020-04-04,1335.48,1335.48,542.79,9007175
<start>
- Close Price: 1456.28
  Date: '2022-01-24'
  High Price: 1456.28
  Low Price: 463.81
  Volume: 3894053
- Close Price: 732.3
  Date: '2010-04-10'
  High Price: 1075.02
  Low Price: 20.91
  Volume: 3867672
- Close Price: 1043.97
  Date: '2021-05-19'
  High Price: 1043.97
  Low Price: 267.63
  Volume: 4580859
- Close Price: 904.34
  Date: '2016-02-27'
  High Price: 1321.1
  Low Price: 693.61
  Volume: 8501816
- Close Price: 1335.48
  Date: '2020-04-04'
  High Price: 1335.48
  Low Price: 542.79
  Volume: 9007175
<end>Can you change this plain text into yaml?
Condition: Windy | Temperature (C): 20.6 | Humidity (%): 39 | Wind Speed (km/h): 4.6
Condition: Foggy | Temperature (C): 25.4 | Humidity (%): 54 | Wind Speed (km/h): 1.1
Condition: Windy | Temperature (C): 20.3 | Humidity (%): 59 | Wind Speed (km/h): 0.9
<start>
- Condition: Windy
  Humidity (%): 39
  Temperature (C): 20.6
  Wind Speed (km/h): 4.6
- Condition: Foggy
  Humidity (%): 54
  Temperature (C): 25.4
  Wind Speed (km/h): 1.1
- Condition: Windy
  Humidity (%): 59
  Temperature (C): 20.3
  Wind Speed (km/h): 0.9
<end>Can you change this CSV into yml?
Database Name,Cache Hit Ratio (%),Average Latency (ms)
LogsDB,82.2,48.67
SessionsDB,90.77,65.14
AnalyticsDB,78.87,34.6
SessionsDB,75.62,2.17
UserDB,81.09,48.67
SalesDB,71.76,99.84
AnalyticsDB,88.79,99.33
<start>
- Average Latency (ms): 48.67
  Cache Hit Ratio (%): 82.2
  Database Name: LogsDB
- Average Latency (ms): 65.14
  Cache Hit Ratio (%): 90.77
  Database Name: SessionsDB
- Average Latency (ms): 34.6
  Cache Hit Ratio (%): 78.87
  Database Name: AnalyticsDB
- Average Latency (ms): 2.17
  Cache Hit Ratio (%): 75.62
  Database Name: SessionsDB
- Average Latency (ms): 48.67
  Cache Hit Ratio (%): 81.09
  Database Name: UserDB
- Average Latency (ms): 99.84
  Cache Hit Ratio (%): 71.76
  Database Name: SalesDB
- Average Latency (ms): 99.33
  Cache Hit Ratio (%): 88.79
  Database Name: AnalyticsDB
<end>Here's some MARKDOWN data, can you convert it to yml?
| Name | Age |
| --- | --- |
| Helen | 34 |
| Isabel | 63 |
| Tonya | 49 |
| Johnnie | 27 |<start>
- Age: 34
  Name: Helen
- Age: 63
  Name: Isabel
- Age: 49
  Name: Tonya
- Age: 27
  Name: Johnnie
<end>Here's some json data, can you convert it to plain text?
[
    {
        "Title": "A Journey Through Time",
        "Author": "Draven Blackthorn",
        "Genre": "Romance",
        "Publication Year": 1987
    },
    {
        "Title": "The Forgotten World",
        "Author": "Elara Moonshadow",
        "Genre": "Science Fiction",
        "Publication Year": 1986
    },
    {
        "Title": "Echoes of Eternity",
        "Author": "Galen Starfire",
        "Genre": "Horror",
        "Publication Year": 1986
    },
    {
        "Title": "Echoes of Eternity",
        "Author": "Orion Frostblade",
        "Genre": "Fantasy",
        "Publication Year": 1956
    },
    {
        "Title": "The Crystal Key",
        "Author": "Galen Starfire",
        "Genre": "Horror",
        "Publication Year": 1984
    },
    {
        "Title": "The Last Sky",
        "Author": "Kara Firebrand",
        "Genre": "Non-Fiction",
        "Publication Year": 2010
    },
    {
        "Title": "Shadows of Solitude",
        "Author": "Rowan Ashborne",
        "Genre": "Historical",
        "Publication Year": 1984
    },
    {
        "Title": "Shadows of Solitude",
        "Author": "Orion Frostblade",
        "Genre": "Horror",
        "Publication Year": 1995
    },
    {
        "Title": "Shadows of Solitude",
        "Author": "Elara Moonshadow",
        "Genre": "Horror",
        "Publication Year": 1977
    },
    {
        "Title": "Whispers of the Abyss",
        "Author": "Rowan Ashborne",
        "Genre": "Mystery",
        "Publication Year": 2007
    }
]<start>
Title: A Journey Through Time | Author: Draven Blackthorn | Genre: Romance | Publication Year: 1987
Title: The Forgotten World | Author: Elara Moonshadow | Genre: Science Fiction | Publication Year: 1986
Title: Echoes of Eternity | Author: Galen Starfire | Genre: Horror | Publication Year: 1986
Title: Echoes of Eternity | Author: Orion Frostblade | Genre: Fantasy | Publication Year: 1956
Title: The Crystal Key | Author: Galen Starfire | Genre: Horror | Publication Year: 1984
Title: The Last Sky | Author: Kara Firebrand | Genre: Non-Fiction | Publication Year: 2010
Title: Shadows of Solitude | Author: Rowan Ashborne | Genre: Historical | Publication Year: 1984
Title: Shadows of Solitude | Author: Orion Frostblade | Genre: Horror | Publication Year: 1995
Title: Shadows of Solitude | Author: Elara Moonshadow | Genre: Horror | Publication Year: 1977
Title: Whispers of the Abyss | Author: Rowan Ashborne | Genre: Mystery | Publication Year: 2007
<end>Can you change this PLAIN TEXT into csv?
Database Name: SalesDB | Queries per Second: 2916.27 | Connection Count: 438 | Average Latency (ms): 94.94 | Timestamp: 2023-08-08 13:05:14
Database Name: ProductsDB | Queries per Second: 52.15 | Connection Count: 183 | Average Latency (ms): 43.54 | Timestamp: 2021-02-12 20:07:30
Database Name: OrdersDB | Queries per Second: 3507.36 | Connection Count: 219 | Average Latency (ms): 83.91 | Timestamp: 2022-01-04 06:58:52
Database Name: LogsDB | Queries per Second: 1257.53 | Connection Count: 93 | Average Latency (ms): 80.9 | Timestamp: 2022-03-24 07:23:32
<start>
Database Name,Queries per Second,Connection Count,Average Latency (ms),Timestamp
SalesDB,2916.27,438,94.94,2023-08-08 13:05:14
ProductsDB,52.15,183,43.54,2021-02-12 20:07:30
OrdersDB,3507.36,219,83.91,2022-01-04 06:58:52
LogsDB,1257.53,93,80.9,2022-03-24 07:23:32
<end>Convert this Markdown to yml:
| Device Type | Location | Battery Level (%) | Timestamp |
| --- | --- | --- | --- |
| Motion Detector | Bedroom | 25.6 | 2023-11-18 00:17:46 |
| Motion Detector | Office | 55.3 | 2022-03-09 17:57:52 |
| Humidity Sensor | Kitchen | 72.1 | 2021-03-01 03:20:45 |
| Pressure Sensor | Hallway | 93.2 | 2022-05-02 23:45:49 |
| Motion Detector | Garden | 75.4 | 2022-09-06 02:53:35 |
| Humidity Sensor | Kitchen | 45.2 | 2022-09-13 04:59:41 |
| Light Sensor | Garden | 33.2 | 2023-11-25 15:50:27 |
| Motion Detector | Garage | 45.2 | 2023-07-09 13:16:13 |
| Pressure Sensor | Bedroom | 98.9 | 2023-04-17 15:37:58 |<start>
- Battery Level (%): 25.6
  Device Type: Motion Detector
  Location: Bedroom
  Timestamp: '2023-11-18 00:17:46'
- Battery Level (%): 55.3
  Device Type: Motion Detector
  Location: Office
  Timestamp: '2022-03-09 17:57:52'
- Battery Level (%): 72.1
  Device Type: Humidity Sensor
  Location: Kitchen
  Timestamp: '2021-03-01 03:20:45'
- Battery Level (%): 93.2
  Device Type: Pressure Sensor
  Location: Hallway
  Timestamp: '2022-05-02 23:45:49'
- Battery Level (%): 75.4
  Device Type: Motion Detector
  Location: Garden
  Timestamp: '2022-09-06 02:53:35'
- Battery Level (%): 45.2
  Device Type: Humidity Sensor
  Location: Kitchen
  Timestamp: '2022-09-13 04:59:41'
- Battery Level (%): 33.2
  Device Type: Light Sensor
  Location: Garden
  Timestamp: '2023-11-25 15:50:27'
- Battery Level (%): 45.2
  Device Type: Motion Detector
  Location: Garage
  Timestamp: '2023-07-09 13:16:13'
- Battery Level (%): 98.9
  Device Type: Pressure Sensor
  Location: Bedroom
  Timestamp: '2023-04-17 15:37:58'
<end>Convert this CSV to Plain text:
Title,Author,Genre,Publication Year
The Forgotten World,Luna Silverleaf,Mystery,1957
The Last Sky,Sylvia Nightshade,Thriller,1965
The Crystal Key,Elara Moonshadow,Fantasy,2017
Shadows of Solitude,Elara Moonshadow,Thriller,1978
Whispers of the Abyss,Draven Blackthorn,Mystery,1978
Tales of the Brave,Elara Moonshadow,Fantasy,2004
Legends of the Rift,Elara Moonshadow,Romance,1960
The Forgotten World,Kara Firebrand,Science Fiction,1981
Echoes of Eternity,Orion Frostblade,Thriller,1962
<start>
Title: The Forgotten World | Author: Luna Silverleaf | Genre: Mystery | Publication Year: 1957
Title: The Last Sky | Author: Sylvia Nightshade | Genre: Thriller | Publication Year: 1965
Title: The Crystal Key | Author: Elara Moonshadow | Genre: Fantasy | Publication Year: 2017
Title: Shadows of Solitude | Author: Elara Moonshadow | Genre: Thriller | Publication Year: 1978
Title: Whispers of the Abyss | Author: Draven Blackthorn | Genre: Mystery | Publication Year: 1978
Title: Tales of the Brave | Author: Elara Moonshadow | Genre: Fantasy | Publication Year: 2004
Title: Legends of the Rift | Author: Elara Moonshadow | Genre: Romance | Publication Year: 1960
Title: The Forgotten World | Author: Kara Firebrand | Genre: Science Fiction | Publication Year: 1981
Title: Echoes of Eternity | Author: Orion Frostblade | Genre: Thriller | Publication Year: 1962
<end>Please transform the following MARKDOWN data into json:
| Company | Stock Price | Annual Revenue (B) | Quarter |
| --- | --- | --- | --- |
| HealthPlus | 57.13 | 122.6 | Q3 |
| EcoEnergy | 328.34 | 203.74 | Q2 |
| FinanceWorks | 476.2 | 134.67 | Q2 |
| FinanceWorks | 417.39 | 203.74 | Q1 |
| HealthPlus | 54.45 | 114.27 | Q3 |<start>
[
    {
        "Company": "HealthPlus",
        "Stock Price": 57.13,
        "Annual Revenue (B)": 122.6,
        "Quarter": "Q3"
    },
    {
        "Company": "EcoEnergy",
        "Stock Price": 328.34,
        "Annual Revenue (B)": 203.74,
        "Quarter": "Q2"
    },
    {
        "Company": "FinanceWorks",
        "Stock Price": 476.2,
        "Annual Revenue (B)": 134.67,
        "Quarter": "Q2"
    },
    {
        "Company": "FinanceWorks",
        "Stock Price": 417.39,
        "Annual Revenue (B)": 203.74,
        "Quarter": "Q1"
    },
    {
        "Company": "HealthPlus",
        "Stock Price": 54.45,
        "Annual Revenue (B)": 114.27,
        "Quarter": "Q3"
    }
]
<end>Please transform the following plain text data into json:
Company: RetailHub | Sector: Retail | Market Cap: Small Cap | Stock Price: 54.58 | Annual Revenue (B): 229.23 | Quarter: Q2
Company: FinanceWorks | Sector: Biotech | Market Cap: Mega Cap | Stock Price: 916.07 | Annual Revenue (B): 168.21 | Quarter: Q3
Company: Foodies | Sector: Retail | Market Cap: Mid Cap | Stock Price: 320.98 | Annual Revenue (B): 168.21 | Quarter: Q2
<start>
[
    {
        "Company": "RetailHub",
        "Sector": "Retail",
        "Market Cap": "Small Cap",
        "Stock Price": 54.58,
        "Annual Revenue (B)": 229.23,
        "Quarter": "Q2"
    },
    {
        "Company": "FinanceWorks",
        "Sector": "Biotech",
        "Market Cap": "Mega Cap",
        "Stock Price": 916.07,
        "Annual Revenue (B)": 168.21,
        "Quarter": "Q3"
    },
    {
        "Company": "Foodies",
        "Sector": "Retail",
        "Market Cap": "Mid Cap",
        "Stock Price": 320.98,
        "Annual Revenue (B)": 168.21,
        "Quarter": "Q2"
    }
]
<end>Please transform the following markdown data into json:
| Name | Age | Income |
| --- | --- | --- |
| Cayden | 63 | 470000 |
| Charlene | 47 | 265000 |
| Fern | 21 | 35000 |
| Cory | 22 | 255000 |
| Regina | 24 | 75000 |
| Courtney | 58 | 65000 |
| Cindy | 42 | 250000 |<start>
[
    {
        "Name": "Cayden",
        "Age": 63,
        "Income": 470000
    },
    {
        "Name": "Charlene",
        "Age": 47,
        "Income": 265000
    },
    {
        "Name": "Fern",
        "Age": 21,
        "Income": 35000
    },
    {
        "Name": "Cory",
        "Age": 22,
        "Income": 255000
    },
    {
        "Name": "Regina",
        "Age": 24,
        "Income": 75000
    },
    {
        "Name": "Courtney",
        "Age": 58,
        "Income": 65000
    },
    {
        "Name": "Cindy",
        "Age": 42,
        "Income": 250000
    }
]
<end>Here's some Yaml data, can you convert it to plain text?
- Cuisine: French
  Location: San Francisco
  Price Range: $$$
  Restaurant Name: The Golden Spoon
- Cuisine: American
  Location: Houston
  Price Range: $
  Restaurant Name: Sushi World
- Cuisine: Indian
  Location: Chicago
  Price Range: $$$$$
  Restaurant Name: BBQ Barn
- Cuisine: Mediterranean
  Location: Miami
  Price Range: $$
  Restaurant Name: BBQ Barn
- Cuisine: Mexican
  Location: Houston
  Price Range: $$
  Restaurant Name: The Steakhouse
- Cuisine: Chinese
  Location: New York
  Price Range: $$
  Restaurant Name: The Steakhouse
- Cuisine: French
  Location: New York
  Price Range: $$$
  Restaurant Name: Vegan Delight
- Cuisine: Indian
  Location: Houston
  Price Range: $$$$$
  Restaurant Name: Curry Corner
- Cuisine: Chinese
  Location: Phoenix
  Price Range: $$
  Restaurant Name: Pasta Palace
<start>
Restaurant Name: The Golden Spoon | Cuisine: French | Location: San Francisco | Price Range: $$$
Restaurant Name: Sushi World | Cuisine: American | Location: Houston | Price Range: $
Restaurant Name: BBQ Barn | Cuisine: Indian | Location: Chicago | Price Range: $$$$$
Restaurant Name: BBQ Barn | Cuisine: Mediterranean | Location: Miami | Price Range: $$
Restaurant Name: The Steakhouse | Cuisine: Mexican | Location: Houston | Price Range: $$
Restaurant Name: The Steakhouse | Cuisine: Chinese | Location: New York | Price Range: $$
Restaurant Name: Vegan Delight | Cuisine: French | Location: New York | Price Range: $$$
Restaurant Name: Curry Corner | Cuisine: Indian | Location: Houston | Price Range: $$$$$
Restaurant Name: Pasta Palace | Cuisine: Chinese | Location: Phoenix | Price Range: $$
<end>Please transform the following Yml data into PLAIN TEXT:
- Box Office Earnings (M): 689.96
  Director: Orin Shadowalker
  Genre: Thriller
  Release Year: 1977
  Title: Beyond the Veil
- Box Office Earnings (M): 499.45
  Director: Lira Silverleaf
  Genre: Action
  Release Year: 1982
  Title: Starbound Odyssey
- Box Office Earnings (M): 704.84
  Director: Mara Moonshadow
  Genre: Adventure
  Release Year: 1989
  Title: Starbound Odyssey
- Box Office Earnings (M): 258.72
  Director: Aria Ravenwood
  Genre: Sci-Fi
  Release Year: 2002
  Title: Mystery of the Depths
<start>
Title: Beyond the Veil | Director: Orin Shadowalker | Genre: Thriller | Release Year: 1977 | Box Office Earnings (M): 689.96
Title: Starbound Odyssey | Director: Lira Silverleaf | Genre: Action | Release Year: 1982 | Box Office Earnings (M): 499.45
Title: Starbound Odyssey | Director: Mara Moonshadow | Genre: Adventure | Release Year: 1989 | Box Office Earnings (M): 704.84
Title: Mystery of the Depths | Director: Aria Ravenwood | Genre: Sci-Fi | Release Year: 2002 | Box Office Earnings (M): 258.72
<end>Convert this plain text to Csv:
Company: FinanceWorks | Sector: Aerospace | Market Cap: Small Cap | Stock Price: 842.95 | Annual Revenue (B): 482.68
Company: EcoEnergy | Sector: Automotive | Market Cap: Mid Cap | Stock Price: 276.23 | Annual Revenue (B): 75.79
Company: HealthPlus | Sector: Retail | Market Cap: Small Cap | Stock Price: 842.95 | Annual Revenue (B): 185.79
Company: BioPharm | Sector: Finance | Market Cap: Small Cap | Stock Price: 828.33 | Annual Revenue (B): 290.7
Company: RetailHub | Sector: Automotive | Market Cap: Large Cap | Stock Price: 104.01 | Annual Revenue (B): 239.92
Company: EcoEnergy | Sector: Automotive | Market Cap: Mega Cap | Stock Price: 41.03 | Annual Revenue (B): 256.01
<start>
Company,Sector,Market Cap,Stock Price,Annual Revenue (B)
FinanceWorks,Aerospace,Small Cap,842.95,482.68
EcoEnergy,Automotive,Mid Cap,276.23,75.79
HealthPlus,Retail,Small Cap,842.95,185.79
BioPharm,Finance,Small Cap,828.33,290.7
RetailHub,Automotive,Large Cap,104.01,239.92
EcoEnergy,Automotive,Mega Cap,41.03,256.01
<end>Can you change this markdown into plain text?
| SKU | Stock Quantity | Supplier Name |
| --- | --- | --- |
| SKU-1053 | 326 | Wonka Industries |
| SKU-1022 | 310 | ACME Corp |
| SKU-1075 | 139 | ACME Corp |
| SKU-1020 | 146 | Wonka Industries |<start>
SKU: SKU-1053 | Stock Quantity: 326 | Supplier Name: Wonka Industries
SKU: SKU-1022 | Stock Quantity: 310 | Supplier Name: ACME Corp
SKU: SKU-1075 | Stock Quantity: 139 | Supplier Name: ACME Corp
SKU: SKU-1020 | Stock Quantity: 146 | Supplier Name: Wonka Industries
<end>Here's some Yml data, can you convert it to csv?
- Rating: 4
  Restaurant Name: Pizza Planet
- Rating: 3
  Restaurant Name: Vegan Delight
- Rating: 5
  Restaurant Name: The Golden Spoon
- Rating: 3
  Restaurant Name: Burger Haven
- Rating: 4
  Restaurant Name: Pizza Planet
- Rating: 3
  Restaurant Name: Curry Corner
- Rating: 2
  Restaurant Name: Sushi World
- Rating: 1
  Restaurant Name: The Golden Spoon
- Rating: 5
  Restaurant Name: Vegan Delight
- Rating: 1
  Restaurant Name: BBQ Barn
<start>
Restaurant Name,Rating
Pizza Planet,4
Vegan Delight,3
The Golden Spoon,5
Burger Haven,3
Pizza Planet,4
Curry Corner,3
Sushi World,2
The Golden Spoon,1
Vegan Delight,5
BBQ Barn,1
<end>Here's some PLAIN TEXT data, can you convert it to Yaml?
Company: GreenEnergy | Date: 2012-11-20 | Open Price: 735.72 | Close Price: 1103.77 | High Price: 1218.04 | Low Price: 656.68 | Volume: 5885610
Company: TechnoCorp | Date: 2013-03-19 | Open Price: 355.6 | Close Price: 860.17 | High Price: 860.17 | Low Price: 355.6 | Volume: 9432645
Company: GreenEnergy | Date: 2015-04-20 | Open Price: 943.73 | Close Price: 1313.24 | High Price: 1313.24 | Low Price: 943.73 | Volume: 5016365
<start>
- Close Price: 1103.77
  Company: GreenEnergy
  Date: '2012-11-20'
  High Price: 1218.04
  Low Price: 656.68
  Open Price: 735.72
  Volume: 5885610
- Close Price: 860.17
  Company: TechnoCorp
  Date: '2013-03-19'
  High Price: 860.17
  Low Price: 355.6
  Open Price: 355.6
  Volume: 9432645
- Close Price: 1313.24
  Company: GreenEnergy
  Date: '2015-04-20'
  High Price: 1313.24
  Low Price: 943.73
  Open Price: 943.73
  Volume: 5016365
<end>Can you change this markdown into PLAIN TEXT?
| Start Location | Distance (miles) | Fuel Used (gallons) |
| --- | --- | --- |
| New York | 2776.3 | 40.8 |
| New York | 1427.4 | 44.4 |
| San Francisco | 1234.6 | 25.3 |
| Houston | 992.8 | 40.8 |
| Chicago | 1234.6 | 95.6 |
| Denver | 1109.9 | 50.3 |
| Denver | 1343.9 | 56.4 |
| Phoenix | 1455.3 | 84.7 |<start>
Start Location: New York | Distance (miles): 2776.3 | Fuel Used (gallons): 40.8
Start Location: New York | Distance (miles): 1427.4 | Fuel Used (gallons): 44.4
Start Location: San Francisco | Distance (miles): 1234.6 | Fuel Used (gallons): 25.3
Start Location: Houston | Distance (miles): 992.8 | Fuel Used (gallons): 40.8
Start Location: Chicago | Distance (miles): 1234.6 | Fuel Used (gallons): 95.6
Start Location: Denver | Distance (miles): 1109.9 | Fuel Used (gallons): 50.3
Start Location: Denver | Distance (miles): 1343.9 | Fuel Used (gallons): 56.4
Start Location: Phoenix | Distance (miles): 1455.3 | Fuel Used (gallons): 84.7
<end>Transform this plain text structure to a Json format:
Device ID: device-0013 | Device Type: Motion Detector | Location: Living Room | Battery Level (%): 15.4 | Timestamp: 2021-12-08 05:10:37
Device ID: device-0094 | Device Type: Humidity Sensor | Location: Bathroom | Battery Level (%): 68.4 | Timestamp: 2021-06-19 05:08:12
Device ID: device-0059 | Device Type: Light Sensor | Location: Office | Battery Level (%): 13.3 | Timestamp: 2023-03-23 06:59:27
Device ID: device-0032 | Device Type: Pressure Sensor | Location: Bathroom | Battery Level (%): 59.4 | Timestamp: 2022-12-28 01:50:09
<start>
[
    {
        "Device ID": "device-0013",
        "Device Type": "Motion Detector",
        "Location": "Living Room",
        "Battery Level (%)": 15.4,
        "Timestamp": "2021-12-08 05:10:37"
    },
    {
        "Device ID": "device-0094",
        "Device Type": "Humidity Sensor",
        "Location": "Bathroom",
        "Battery Level (%)": 68.4,
        "Timestamp": "2021-06-19 05:08:12"
    },
    {
        "Device ID": "device-0059",
        "Device Type": "Light Sensor",
        "Location": "Office",
        "Battery Level (%)": 13.3,
        "Timestamp": "2023-03-23 06:59:27"
    },
    {
        "Device ID": "device-0032",
        "Device Type": "Pressure Sensor",
        "Location": "Bathroom",
        "Battery Level (%)": 59.4,
        "Timestamp": "2022-12-28 01:50:09"
    }
]
<end>Please transform the following json data into YAML:
[
    {
        "Location": "Denver",
        "Temperature (C)": 22.7,
        "Humidity (%)": 32,
        "Wind Speed (km/h)": 17.6
    },
    {
        "Location": "Seattle",
        "Temperature (C)": 10.6,
        "Humidity (%)": 28,
        "Wind Speed (km/h)": 9.3
    },
    {
        "Location": "Denver",
        "Temperature (C)": 20.8,
        "Humidity (%)": 22,
        "Wind Speed (km/h)": 24.0
    },
    {
        "Location": "Los Angeles",
        "Temperature (C)": 2.1,
        "Humidity (%)": 24,
        "Wind Speed (km/h)": 7.0
    },
    {
        "Location": "New York",
        "Temperature (C)": 24.1,
        "Humidity (%)": 24,
        "Wind Speed (km/h)": 5.5
    },
    {
        "Location": "Los Angeles",
        "Temperature (C)": 25.2,
        "Humidity (%)": 73,
        "Wind Speed (km/h)": 22.1
    },
    {
        "Location": "Denver",
        "Temperature (C)": 39.9,
        "Humidity (%)": 49,
        "Wind Speed (km/h)": 14.2
    }
]<start>
- Humidity (%): 32
  Location: Denver
  Temperature (C): 22.7
  Wind Speed (km/h): 17.6
- Humidity (%): 28
  Location: Seattle
  Temperature (C): 10.6
  Wind Speed (km/h): 9.3
- Humidity (%): 22
  Location: Denver
  Temperature (C): 20.8
  Wind Speed (km/h): 24.0
- Humidity (%): 24
  Location: Los Angeles
  Temperature (C): 2.1
  Wind Speed (km/h): 7.0
- Humidity (%): 24
  Location: New York
  Temperature (C): 24.1
  Wind Speed (km/h): 5.5
- Humidity (%): 73
  Location: Los Angeles
  Temperature (C): 25.2
  Wind Speed (km/h): 22.1
- Humidity (%): 49
  Location: Denver
  Temperature (C): 39.9
  Wind Speed (km/h): 14.2
<end>Here's some plain text data, can you convert it to Markdown?
Database Name: ProfilesDB | Queries per Second: 3453.91 | Cache Hit Ratio (%): 78.72 | Average Latency (ms): 72.03
Database Name: LogsDB | Queries per Second: 1081.37 | Cache Hit Ratio (%): 96.89 | Average Latency (ms): 57.11
Database Name: MetricsDB | Queries per Second: 894.69 | Cache Hit Ratio (%): 78.45 | Average Latency (ms): 63.26
Database Name: MetricsDB | Queries per Second: 4129.07 | Cache Hit Ratio (%): 71.53 | Average Latency (ms): 17.44
Database Name: ProfilesDB | Queries per Second: 4251.69 | Cache Hit Ratio (%): 95.64 | Average Latency (ms): 88.34
Database Name: LogsDB | Queries per Second: 4212.63 | Cache Hit Ratio (%): 77.77 | Average Latency (ms): 22.69
Database Name: OrdersDB | Queries per Second: 1056.3 | Cache Hit Ratio (%): 78.39 | Average Latency (ms): 25.63
Database Name: ProfilesDB | Queries per Second: 2470.59 | Cache Hit Ratio (%): 92.0 | Average Latency (ms): 42.81
Database Name: UserDB | Queries per Second: 4262.13 | Cache Hit Ratio (%): 79.42 | Average Latency (ms): 40.94
Database Name: ProfilesDB | Queries per Second: 2544.17 | Cache Hit Ratio (%): 81.53 | Average Latency (ms): 5.16
<start>
| Database Name | Queries per Second | Cache Hit Ratio (%) | Average Latency (ms) |
| --- | --- | --- | --- |
| ProfilesDB | 3453.91 | 78.72 | 72.03 |
| LogsDB | 1081.37 | 96.89 | 57.11 |
| MetricsDB | 894.69 | 78.45 | 63.26 |
| MetricsDB | 4129.07 | 71.53 | 17.44 |
| ProfilesDB | 4251.69 | 95.64 | 88.34 |
| LogsDB | 4212.63 | 77.77 | 22.69 |
| OrdersDB | 1056.3 | 78.39 | 25.63 |
| ProfilesDB | 2470.59 | 92.0 | 42.81 |
| UserDB | 4262.13 | 79.42 | 40.94 |
| ProfilesDB | 2544.17 | 81.53 | 5.16 |
<end>Transform this YML structure to a Markdown format:
- Condition: Rainy
  Day: Friday
  Humidity (%): 64
  Location: Phoenix
  Temperature (C): 8.9
- Condition: Snowy
  Day: Thursday
  Humidity (%): 43
  Location: Chicago
  Temperature (C): 34.1
- Condition: Stormy
  Day: Sunday
  Humidity (%): 53
  Location: Phoenix
  Temperature (C): -8.2
- Condition: Rainy
  Day: Saturday
  Humidity (%): 54
  Location: Chicago
  Temperature (C): 27.6
- Condition: Cloudy
  Day: Thursday
  Humidity (%): 25
  Location: New York
  Temperature (C): -6.2
- Condition: Foggy
  Day: Thursday
  Humidity (%): 30
  Location: Chicago
  Temperature (C): 5.0
- Condition: Foggy
  Day: Tuesday
  Humidity (%): 67
  Location: Los Angeles
  Temperature (C): -3.3
- Condition: Sunny
  Day: Wednesday
  Humidity (%): 72
  Location: Denver
  Temperature (C): 5.8
<start>
| Location | Condition | Temperature (C) | Humidity (%) | Day |
| --- | --- | --- | --- | --- |
| Phoenix | Rainy | 8.9 | 64 | Friday |
| Chicago | Snowy | 34.1 | 43 | Thursday |
| Phoenix | Stormy | -8.2 | 53 | Sunday |
| Chicago | Rainy | 27.6 | 54 | Saturday |
| New York | Cloudy | -6.2 | 25 | Thursday |
| Chicago | Foggy | 5.0 | 30 | Thursday |
| Los Angeles | Foggy | -3.3 | 67 | Tuesday |
| Denver | Sunny | 5.8 | 72 | Wednesday |
<end>Transform this JSON structure to a Csv format:
[
    {
        "Device ID": "device-0056",
        "Device Type": "Light Sensor",
        "Location": "Bedroom",
        "Reading Value": 13.47
    },
    {
        "Device ID": "device-0049",
        "Device Type": "Motion Detector",
        "Location": "Bathroom",
        "Reading Value": -1.53
    },
    {
        "Device ID": "device-0011",
        "Device Type": "Motion Detector",
        "Location": "Office",
        "Reading Value": 81.17
    }
]<start>
Device ID,Device Type,Location,Reading Value
device-0056,Light Sensor,Bedroom,13.47
device-0049,Motion Detector,Bathroom,-1.53
device-0011,Motion Detector,Office,81.17
<end>Here's some plain text data, can you convert it to Csv?
Company: RetailHub | Sector: Aerospace | Market Cap: Small Cap | Stock Price: 423.15 | Annual Revenue (B): 490.24 | Quarter: Q2
Company: Foodies | Sector: Aerospace | Market Cap: Small Cap | Stock Price: 718.62 | Annual Revenue (B): 355.37 | Quarter: Q4
Company: AutoDrive | Sector: Biotech | Market Cap: Mid Cap | Stock Price: 290.49 | Annual Revenue (B): 73.77 | Quarter: Q4
Company: BioPharm | Sector: Automotive | Market Cap: Mid Cap | Stock Price: 277.88 | Annual Revenue (B): 404.24 | Quarter: Q4
Company: Foodies | Sector: Finance | Market Cap: Large Cap | Stock Price: 831.14 | Annual Revenue (B): 477.57 | Quarter: Q1
Company: FinanceWorks | Sector: Retail | Market Cap: Large Cap | Stock Price: 410.82 | Annual Revenue (B): 68.47 | Quarter: Q4
Company: RetailHub | Sector: Retail | Market Cap: Mega Cap | Stock Price: 726.96 | Annual Revenue (B): 106.52 | Quarter: Q3
Company: RetailHub | Sector: Aerospace | Market Cap: Mega Cap | Stock Price: 423.15 | Annual Revenue (B): 56.16 | Quarter: Q3
Company: AutoDrive | Sector: Finance | Market Cap: Large Cap | Stock Price: 138.68 | Annual Revenue (B): 421.56 | Quarter: Q3
<start>
Company,Sector,Market Cap,Stock Price,Annual Revenue (B),Quarter
RetailHub,Aerospace,Small Cap,423.15,490.24,Q2
Foodies,Aerospace,Small Cap,718.62,355.37,Q4
AutoDrive,Biotech,Mid Cap,290.49,73.77,Q4
BioPharm,Automotive,Mid Cap,277.88,404.24,Q4
Foodies,Finance,Large Cap,831.14,477.57,Q1
FinanceWorks,Retail,Large Cap,410.82,68.47,Q4
RetailHub,Retail,Mega Cap,726.96,106.52,Q3
RetailHub,Aerospace,Mega Cap,423.15,56.16,Q3
AutoDrive,Finance,Large Cap,138.68,421.56,Q3
<end>Transform this MARKDOWN structure to a YAML format:
| Title | Director | Release Year | Box Office Earnings (M) |
| --- | --- | --- | --- |
| The Endless Horizon | Talon Blackthorn | 2002 | 920.96 |
| Escape from Earth | Zara Stormrider | 1985 | 363.44 |
| The Endless Horizon | Selene Darkwhisper | 2006 | 825.86 |
| The Great Expedition | Aria Ravenwood | 2001 | 922.65 |<start>
- Box Office Earnings (M): 920.96
  Director: Talon Blackthorn
  Release Year: 2002
  Title: The Endless Horizon
- Box Office Earnings (M): 363.44
  Director: Zara Stormrider
  Release Year: 1985
  Title: Escape from Earth
- Box Office Earnings (M): 825.86
  Director: Selene Darkwhisper
  Release Year: 2006
  Title: The Endless Horizon
- Box Office Earnings (M): 922.65
  Director: Aria Ravenwood
  Release Year: 2001
  Title: The Great Expedition
<end>Here's some Json data, can you convert it to csv?
[
    {
        "Company": "HealthPlus",
        "Sector": "Aerospace",
        "Market Cap": "Large Cap",
        "Stock Price": 949.36,
        "Annual Revenue (B)": 175.9
    },
    {
        "Company": "EcoEnergy",
        "Sector": "Healthcare",
        "Market Cap": "Mega Cap",
        "Stock Price": 615.11,
        "Annual Revenue (B)": 392.5
    },
    {
        "Company": "HealthPlus",
        "Sector": "Aerospace",
        "Market Cap": "Mega Cap",
        "Stock Price": 23.65,
        "Annual Revenue (B)": 339.4
    },
    {
        "Company": "FinanceWorks",
        "Sector": "Technology",
        "Market Cap": "Small Cap",
        "Stock Price": 615.11,
        "Annual Revenue (B)": 202.88
    },
    {
        "Company": "Foodies",
        "Sector": "Energy",
        "Market Cap": "Mega Cap",
        "Stock Price": 715.82,
        "Annual Revenue (B)": 293.12
    }
]<start>
Company,Sector,Market Cap,Stock Price,Annual Revenue (B)
HealthPlus,Aerospace,Large Cap,949.36,175.9
EcoEnergy,Healthcare,Mega Cap,615.11,392.5
HealthPlus,Aerospace,Mega Cap,23.65,339.4
FinanceWorks,Technology,Small Cap,615.11,202.88
Foodies,Energy,Mega Cap,715.82,293.12
<end>Can you change this yaml into csv?
- Duration (hours): 12.0
  End Location: Houston
  Start Location: Phoenix
  Trip Name: Valley Voyage
- Duration (hours): 56.0
  End Location: Houston
  Start Location: Phoenix
  Trip Name: Historic Route
- Duration (hours): 67.0
  End Location: Phoenix
  Start Location: Miami
  Trip Name: Canyon Trek
- Duration (hours): 62.2
  End Location: Denver
  Start Location: Miami
  Trip Name: Highway Odyssey
- Duration (hours): 67.0
  End Location: New York
  Start Location: Phoenix
  Trip Name: Canyon Trek
- Duration (hours): 54.4
  End Location: Chicago
  Start Location: San Francisco
  Trip Name: Valley Voyage
- Duration (hours): 15.1
  End Location: New York
  Start Location: Houston
  Trip Name: Forest Journey
- Duration (hours): 62.2
  End Location: Denver
  Start Location: San Francisco
  Trip Name: Forest Journey
- Duration (hours): 1.8
  End Location: Denver
  Start Location: Miami
  Trip Name: Coast to Coast
<start>
Trip Name,Start Location,End Location,Duration (hours)
Valley Voyage,Phoenix,Houston,12.0
Historic Route,Phoenix,Houston,56.0
Canyon Trek,Miami,Phoenix,67.0
Highway Odyssey,Miami,Denver,62.2
Canyon Trek,Phoenix,New York,67.0
Valley Voyage,San Francisco,Chicago,54.4
Forest Journey,Houston,New York,15.1
Forest Journey,San Francisco,Denver,62.2
Coast to Coast,Miami,Denver,1.8
<end>Can you change this markdown into Json?
| Device ID | Device Type | Location | Reading Value | Timestamp |
| --- | --- | --- | --- | --- |
| device-0042 | Humidity Sensor | Office | 74.71 | 2023-07-11 09:37:47 |
| device-0016 | Humidity Sensor | Garage | -2.37 | 2023-04-18 20:55:58 |
| device-0007 | Humidity Sensor | Office | -12.25 | 2022-11-02 18:24:40 |<start>
[
    {
        "Device ID": "device-0042",
        "Device Type": "Humidity Sensor",
        "Location": "Office",
        "Reading Value": 74.71,
        "Timestamp": "2023-07-11 09:37:47"
    },
    {
        "Device ID": "device-0016",
        "Device Type": "Humidity Sensor",
        "Location": "Garage",
        "Reading Value": -2.37,
        "Timestamp": "2023-04-18 20:55:58"
    },
    {
        "Device ID": "device-0007",
        "Device Type": "Humidity Sensor",
        "Location": "Office",
        "Reading Value": -12.25,
        "Timestamp": "2022-11-02 18:24:40"
    }
]
<end>Please transform the following Plain text data into markdown:
Birth Month: April | Income: 285000
Birth Month: July | Income: 350000
Birth Month: December | Income: 235000
Birth Month: December | Income: 410000
Birth Month: October | Income: 305000
Birth Month: December | Income: 395000
Birth Month: April | Income: 390000
<start>
| Birth Month | Income |
| --- | --- |
| April | 285000 |
| July | 350000 |
| December | 235000 |
| December | 410000 |
| October | 305000 |
| December | 395000 |
| April | 390000 |
<end>Can you change this Plain text into MARKDOWN?
Company: TechnoCorp | Date: 2022-12-25 | High Price: 1454.91 | Low Price: 105.26 | Volume: 130158
Company: RetailWorld | Date: 2016-12-27 | High Price: 966.34 | Low Price: 185.12 | Volume: 6352609
Company: TechnoCorp | Date: 2018-04-04 | High Price: 1438.36 | Low Price: 829.07 | Volume: 7601930
Company: AutoMotive | Date: 2016-08-10 | High Price: 920.81 | Low Price: 865.17 | Volume: 8905602
<start>
| Company | Date | High Price | Low Price | Volume |
| --- | --- | --- | --- | --- |
| TechnoCorp | 2022-12-25 | 1454.91 | 105.26 | 130158 |
| RetailWorld | 2016-12-27 | 966.34 | 185.12 | 6352609 |
| TechnoCorp | 2018-04-04 | 1438.36 | 829.07 | 7601930 |
| AutoMotive | 2016-08-10 | 920.81 | 865.17 | 8905602 |
<end>Convert this yaml to markdown:
- Day: Monday
  Humidity (%): 56
  Location: New York
- Day: Thursday
  Humidity (%): 30
  Location: Houston
- Day: Sunday
  Humidity (%): 74
  Location: Houston
- Day: Tuesday
  Humidity (%): 32
  Location: Denver
- Day: Monday
  Humidity (%): 63
  Location: Los Angeles
<start>
| Location | Humidity (%) | Day |
| --- | --- | --- |
| New York | 56 | Monday |
| Houston | 30 | Thursday |
| Houston | 74 | Sunday |
| Denver | 32 | Tuesday |
| Los Angeles | 63 | Monday |
<end>Can you change this Yaml into plain text?
- Author: Draven Blackthorn
  Publication Year: 1975
  Title: The Last Sky
- Author: Orion Frostblade
  Publication Year: 2019
  Title: The Silent Grove
- Author: Elara Moonshadow
  Publication Year: 1964
  Title: The Crystal Key
- Author: Elara Moonshadow
  Publication Year: 1988
  Title: Echoes of Eternity
- Author: Isla Windrider
  Publication Year: 2020
  Title: Tales of the Brave
<start>
Title: The Last Sky | Author: Draven Blackthorn | Publication Year: 1975
Title: The Silent Grove | Author: Orion Frostblade | Publication Year: 2019
Title: The Crystal Key | Author: Elara Moonshadow | Publication Year: 1964
Title: Echoes of Eternity | Author: Elara Moonshadow | Publication Year: 1988
Title: Tales of the Brave | Author: Isla Windrider | Publication Year: 2020
<end>Please transform the following Json data into Plain text:
[
    {
        "Director": "Selene Darkwhisper",
        "Release Year": 1989,
        "Box Office Earnings (M)": 748.25
    },
    {
        "Director": "Drake Nightshade",
        "Release Year": 1995,
        "Box Office Earnings (M)": 847.63
    },
    {
        "Director": "Lira Silverleaf",
        "Release Year": 1981,
        "Box Office Earnings (M)": 916.76
    },
    {
        "Director": "Rylan Frostblade",
        "Release Year": 1973,
        "Box Office Earnings (M)": 979.47
    },
    {
        "Director": "Rylan Frostblade",
        "Release Year": 1998,
        "Box Office Earnings (M)": 743.73
    },
    {
        "Director": "Cade Firebrand",
        "Release Year": 1976,
        "Box Office Earnings (M)": 354.98
    }
]<start>
Director: Selene Darkwhisper | Release Year: 1989 | Box Office Earnings (M): 748.25
Director: Drake Nightshade | Release Year: 1995 | Box Office Earnings (M): 847.63
Director: Lira Silverleaf | Release Year: 1981 | Box Office Earnings (M): 916.76
Director: Rylan Frostblade | Release Year: 1973 | Box Office Earnings (M): 979.47
Director: Rylan Frostblade | Release Year: 1998 | Box Office Earnings (M): 743.73
Director: Cade Firebrand | Release Year: 1976 | Box Office Earnings (M): 354.98
<end>Transform this markdown structure to a csv format:
| Company | Date | Open Price | Close Price | High Price | Low Price | Volume |
| --- | --- | --- | --- | --- | --- | --- |
| AeroSystems | 2011-08-10 | 1431.37 | 496.52 | 1431.37 | 496.52 | 7396254 |
| HealthGen | 2017-06-17 | 1028.21 | 178.4 | 1028.21 | 178.4 | 1293927 |
| TechnoCorp | 2020-12-20 | 392.82 | 1044.03 | 1044.03 | 392.82 | 7243956 |
| BioLife | 2013-03-19 | 718.28 | 454.22 | 808.74 | 454.22 | 2077620 |
| TechnoCorp | 2017-10-15 | 516.11 | 326.49 | 1346.56 | 326.49 | 2077620 |
| TechnoCorp | 2014-04-05 | 724.2 | 1028.21 | 1028.21 | 269.65 | 7201510 |
| TechnoCorp | 2014-09-13 | 393.37 | 504.6 | 977.05 | 179.33 | 3274869 |<start>
Company,Date,Open Price,Close Price,High Price,Low Price,Volume
AeroSystems,2011-08-10,1431.37,496.52,1431.37,496.52,7396254
HealthGen,2017-06-17,1028.21,178.4,1028.21,178.4,1293927
TechnoCorp,2020-12-20,392.82,1044.03,1044.03,392.82,7243956
BioLife,2013-03-19,718.28,454.22,808.74,454.22,2077620
TechnoCorp,2017-10-15,516.11,326.49,1346.56,326.49,2077620
TechnoCorp,2014-04-05,724.2,1028.21,1028.21,269.65,7201510
TechnoCorp,2014-09-13,393.37,504.6,977.05,179.33,3274869
<end>Here's some markdown data, can you convert it to Yaml?
| Location | Condition | Temperature (C) | Humidity (%) | Day |
| --- | --- | --- | --- | --- |
| Houston | Sunny | 13.9 | 25 | Monday |
| Phoenix | Windy | 33.7 | 94 | Thursday |
| Seattle | Sunny | 34.2 | 80 | Friday |
| Chicago | Snowy | -9.7 | 73 | Tuesday |<start>
- Condition: Sunny
  Day: Monday
  Humidity (%): 25
  Location: Houston
  Temperature (C): 13.9
- Condition: Windy
  Day: Thursday
  Humidity (%): 94
  Location: Phoenix
  Temperature (C): 33.7
- Condition: Sunny
  Day: Friday
  Humidity (%): 80
  Location: Seattle
  Temperature (C): 34.2
- Condition: Snowy
  Day: Tuesday
  Humidity (%): 73
  Location: Chicago
  Temperature (C): -9.7
<end>Please transform the following Markdown data into Plain text:
| Trip Name | Start Location | End Location | Distance (miles) | Fuel Used (gallons) |
| --- | --- | --- | --- | --- |
| Mountain Adventure | Miami | San Francisco | 260.1 | 42.5 |
| Desert Drive | San Francisco | Houston | 2366.7 | 55.3 |
| City Explorer | Denver | Los Angeles | 90.5 | 55.3 |
| Highway Odyssey | Houston | Chicago | 293.8 | 56.3 |
| Mountain Adventure | San Francisco | Houston | 1549.4 | 42.5 |
| Mountain Adventure | San Francisco | Houston | 445.1 | 29.3 |
| City Explorer | Phoenix | San Francisco | 2391.1 | 6.1 |
| Highway Odyssey | Chicago | Miami | 2364.2 | 6.1 |<start>
Trip Name: Mountain Adventure | Start Location: Miami | End Location: San Francisco | Distance (miles): 260.1 | Fuel Used (gallons): 42.5
Trip Name: Desert Drive | Start Location: San Francisco | End Location: Houston | Distance (miles): 2366.7 | Fuel Used (gallons): 55.3
Trip Name: City Explorer | Start Location: Denver | End Location: Los Angeles | Distance (miles): 90.5 | Fuel Used (gallons): 55.3
Trip Name: Highway Odyssey | Start Location: Houston | End Location: Chicago | Distance (miles): 293.8 | Fuel Used (gallons): 56.3
Trip Name: Mountain Adventure | Start Location: San Francisco | End Location: Houston | Distance (miles): 1549.4 | Fuel Used (gallons): 42.5
Trip Name: Mountain Adventure | Start Location: San Francisco | End Location: Houston | Distance (miles): 445.1 | Fuel Used (gallons): 29.3
Trip Name: City Explorer | Start Location: Phoenix | End Location: San Francisco | Distance (miles): 2391.1 | Fuel Used (gallons): 6.1
Trip Name: Highway Odyssey | Start Location: Chicago | End Location: Miami | Distance (miles): 2364.2 | Fuel Used (gallons): 6.1
<end>Here's some CSV data, can you convert it to markdown?
Company,Sector,Market Cap,Quarter
Foodies,Energy,Small Cap,Q2
EcoEnergy,Technology,Large Cap,Q3
FinanceWorks,Automotive,Mid Cap,Q1
<start>
| Company | Sector | Market Cap | Quarter |
| --- | --- | --- | --- |
| Foodies | Energy | Small Cap | Q2 |
| EcoEnergy | Technology | Large Cap | Q3 |
| FinanceWorks | Automotive | Mid Cap | Q1 |
<end>Convert this Json to markdown:
[
    {
        "Title": "A Journey Through Time",
        "Publication Year": 1964,
        "Rating": 2.9
    },
    {
        "Title": "Shadows of Solitude",
        "Publication Year": 2004,
        "Rating": 2.0
    },
    {
        "Title": "The Silent Grove",
        "Publication Year": 2020,
        "Rating": 1.2
    },
    {
        "Title": "A Journey Through Time",
        "Publication Year": 1952,
        "Rating": 3.6
    },
    {
        "Title": "The Silent Grove",
        "Publication Year": 1955,
        "Rating": 3.4
    }
]<start>
| Title | Publication Year | Rating |
| --- | --- | --- |
| A Journey Through Time | 1964 | 2.9 |
| Shadows of Solitude | 2004 | 2.0 |
| The Silent Grove | 2020 | 1.2 |
| A Journey Through Time | 1952 | 3.6 |
| The Silent Grove | 1955 | 3.4 |
<end>Convert this CSV to yaml:
Company,Date,Open Price,High Price,Low Price,Volume
AeroSystems,2023-02-27,308.11,752.95,308.11,6746651
BioLife,2012-12-09,1282.48,1282.48,1064.94,4079072
AeroSystems,2012-03-14,501.87,527.97,146.94,2049906
BioLife,2013-04-06,1282.48,1282.48,958.09,7815699
RetailWorld,2017-03-22,87.43,474.74,87.43,3167374
HealthGen,2015-11-13,66.1,656.88,66.1,1471833
FinanceTrust,2010-01-25,708.36,708.36,338.06,6506099
MediaGroup,2020-06-14,321.83,321.83,223.0,1471833
AutoMotive,2013-05-11,1429.01,1429.01,803.03,9639164
<start>
- Company: AeroSystems
  Date: '2023-02-27'
  High Price: 752.95
  Low Price: 308.11
  Open Price: 308.11
  Volume: 6746651
- Company: BioLife
  Date: '2012-12-09'
  High Price: 1282.48
  Low Price: 1064.94
  Open Price: 1282.48
  Volume: 4079072
- Company: AeroSystems
  Date: '2012-03-14'
  High Price: 527.97
  Low Price: 146.94
  Open Price: 501.87
  Volume: 2049906
- Company: BioLife
  Date: '2013-04-06'
  High Price: 1282.48
  Low Price: 958.09
  Open Price: 1282.48
  Volume: 7815699
- Company: RetailWorld
  Date: '2017-03-22'
  High Price: 474.74
  Low Price: 87.43
  Open Price: 87.43
  Volume: 3167374
- Company: HealthGen
  Date: '2015-11-13'
  High Price: 656.88
  Low Price: 66.1
  Open Price: 66.1
  Volume: 1471833
- Company: FinanceTrust
  Date: '2010-01-25'
  High Price: 708.36
  Low Price: 338.06
  Open Price: 708.36
  Volume: 6506099
- Company: MediaGroup
  Date: '2020-06-14'
  High Price: 321.83
  Low Price: 223.0
  Open Price: 321.83
  Volume: 1471833
- Company: AutoMotive
  Date: '2013-05-11'
  High Price: 1429.01
  Low Price: 803.03
  Open Price: 1429.01
  Volume: 9639164
<end>Please transform the following csv data into Plain text:
Company,Market Cap,Quarter
RetailHub,Small Cap,Q3
BioPharm,Mid Cap,Q1
TechCorp,Mega Cap,Q4
RetailHub,Mid Cap,Q3
<start>
Company: RetailHub | Market Cap: Small Cap | Quarter: Q3
Company: BioPharm | Market Cap: Mid Cap | Quarter: Q1
Company: TechCorp | Market Cap: Mega Cap | Quarter: Q4
Company: RetailHub | Market Cap: Mid Cap | Quarter: Q3
<end>Can you change this YAML into csv?
- Income: 385000
  Name: Brandi
- Income: 25000
  Name: Ola
- Income: 125000
  Name: Leslie
- Income: 75000
  Name: Brantley
- Income: 350000
  Name: Gabrielle
- Income: 285000
  Name: Joann
<start>
Name,Income
Brandi,385000
Ola,25000
Leslie,125000
Brantley,75000
Gabrielle,350000
Joann,285000
<end>Convert this YAML to PLAIN TEXT:
- Birth Month: January
  City: Dallas
  Income: 360000
- Birth Month: February
  City: San Jose
  Income: 480000
- Birth Month: February
  City: Washington
  Income: 195000
- Birth Month: January
  City: Boston
  Income: 210000
- Birth Month: December
  City: Indianapolis
  Income: 230000
- Birth Month: July
  City: Seattle
  Income: 220000
- Birth Month: November
  City: Las Vegas
  Income: 460000
<start>
Birth Month: January | City: Dallas | Income: 360000
Birth Month: February | City: San Jose | Income: 480000
Birth Month: February | City: Washington | Income: 195000
Birth Month: January | City: Boston | Income: 210000
Birth Month: December | City: Indianapolis | Income: 230000
Birth Month: July | City: Seattle | Income: 220000
Birth Month: November | City: Las Vegas | Income: 460000
<end>Can you change this JSON into yaml?
[
    {
        "Condition": "Snowy",
        "Temperature (C)": 18.7,
        "Day": "Saturday"
    },
    {
        "Condition": "Stormy",
        "Temperature (C)": 17.4,
        "Day": "Saturday"
    },
    {
        "Condition": "Sunny",
        "Temperature (C)": 34.5,
        "Day": "Saturday"
    },
    {
        "Condition": "Cloudy",
        "Temperature (C)": 13.5,
        "Day": "Sunday"
    },
    {
        "Condition": "Cloudy",
        "Temperature (C)": 11.6,
        "Day": "Sunday"
    },
    {
        "Condition": "Foggy",
        "Temperature (C)": 7.2,
        "Day": "Saturday"
    }
]<start>
- Condition: Snowy
  Day: Saturday
  Temperature (C): 18.7
- Condition: Stormy
  Day: Saturday
  Temperature (C): 17.4
- Condition: Sunny
  Day: Saturday
  Temperature (C): 34.5
- Condition: Cloudy
  Day: Sunday
  Temperature (C): 13.5
- Condition: Cloudy
  Day: Sunday
  Temperature (C): 11.6
- Condition: Foggy
  Day: Saturday
  Temperature (C): 7.2
<end>Can you change this CSV into json?
Restaurant Name,Cuisine,Location,Price Range
Vegan Delight,Indian,Miami,$$$$
Pizza Planet,Italian,Seattle,$$$$$
Burger Haven,French,San Francisco,$
Pizza Planet,Italian,Phoenix,$$$$$
Burger Haven,Japanese,Seattle,$$$
BBQ Barn,Chinese,Miami,$$$
Burger Haven,Chinese,San Francisco,$$
Curry Corner,Chinese,Phoenix,$$$$
Burger Haven,American,Chicago,$$$
Curry Corner,American,Miami,$$$$$
<start>
[
    {
        "Restaurant Name": "Vegan Delight",
        "Cuisine": "Indian",
        "Location": "Miami",
        "Price Range": "$$$$"
    },
    {
        "Restaurant Name": "Pizza Planet",
        "Cuisine": "Italian",
        "Location": "Seattle",
        "Price Range": "$$$$$"
    },
    {
        "Restaurant Name": "Burger Haven",
        "Cuisine": "French",
        "Location": "San Francisco",
        "Price Range": "$"
    },
    {
        "Restaurant Name": "Pizza Planet",
        "Cuisine": "Italian",
        "Location": "Phoenix",
        "Price Range": "$$$$$"
    },
    {
        "Restaurant Name": "Burger Haven",
        "Cuisine": "Japanese",
        "Location": "Seattle",
        "Price Range": "$$$"
    },
    {
        "Restaurant Name": "BBQ Barn",
        "Cuisine": "Chinese",
        "Location": "Miami",
        "Price Range": "$$$"
    },
    {
        "Restaurant Name": "Burger Haven",
        "Cuisine": "Chinese",
        "Location": "San Francisco",
        "Price Range": "$$"
    },
    {
        "Restaurant Name": "Curry Corner",
        "Cuisine": "Chinese",
        "Location": "Phoenix",
        "Price Range": "$$$$"
    },
    {
        "Restaurant Name": "Burger Haven",
        "Cuisine": "American",
        "Location": "Chicago",
        "Price Range": "$$$"
    },
    {
        "Restaurant Name": "Curry Corner",
        "Cuisine": "American",
        "Location": "Miami",
        "Price Range": "$$$$$"
    }
]
<end>Can you change this markdown into plain text?
| Company | Sector | Market Cap | Stock Price | Quarter |
| --- | --- | --- | --- | --- |
| Foodies | Aerospace | Mega Cap | 86.26 | Q3 |
| HealthPlus | Technology | Mega Cap | 607.48 | Q1 |
| TechCorp | Technology | Mega Cap | 754.08 | Q1 |
| HealthPlus | Finance | Small Cap | 326.07 | Q2 |
| EcoEnergy | Biotech | Small Cap | 222.42 | Q4 |
| BioPharm | Biotech | Small Cap | 754.08 | Q4 |
| Foodies | Retail | Small Cap | 448.31 | Q3 |
| FinanceWorks | Energy | Large Cap | 306.46 | Q4 |
| AutoDrive | Finance | Mid Cap | 673.97 | Q2 |
| Foodies | Energy | Small Cap | 524.04 | Q2 |<start>
Company: Foodies | Sector: Aerospace | Market Cap: Mega Cap | Stock Price: 86.26 | Quarter: Q3
Company: HealthPlus | Sector: Technology | Market Cap: Mega Cap | Stock Price: 607.48 | Quarter: Q1
Company: TechCorp | Sector: Technology | Market Cap: Mega Cap | Stock Price: 754.08 | Quarter: Q1
Company: HealthPlus | Sector: Finance | Market Cap: Small Cap | Stock Price: 326.07 | Quarter: Q2
Company: EcoEnergy | Sector: Biotech | Market Cap: Small Cap | Stock Price: 222.42 | Quarter: Q4
Company: BioPharm | Sector: Biotech | Market Cap: Small Cap | Stock Price: 754.08 | Quarter: Q4
Company: Foodies | Sector: Retail | Market Cap: Small Cap | Stock Price: 448.31 | Quarter: Q3
Company: FinanceWorks | Sector: Energy | Market Cap: Large Cap | Stock Price: 306.46 | Quarter: Q4
Company: AutoDrive | Sector: Finance | Market Cap: Mid Cap | Stock Price: 673.97 | Quarter: Q2
Company: Foodies | Sector: Energy | Market Cap: Small Cap | Stock Price: 524.04 | Quarter: Q2
<end>Can you change this yml into Plain text?
- Day: Saturday
  Temperature (C): 4.8
  Wind Speed (km/h): 28.7
- Day: Saturday
  Temperature (C): 30.8
  Wind Speed (km/h): 27.2
- Day: Sunday
  Temperature (C): 14.9
  Wind Speed (km/h): 27.9
<start>
Temperature (C): 4.8 | Wind Speed (km/h): 28.7 | Day: Saturday
Temperature (C): 30.8 | Wind Speed (km/h): 27.2 | Day: Saturday
Temperature (C): 14.9 | Wind Speed (km/h): 27.9 | Day: Sunday
<end>Transform this Csv structure to a Json format:
Name,Age,Birth Month,City,Income
Gayle,35,January,Dallas,490000
Bryce,39,February,Fort Worth,415000
Martha,50,November,Jacksonville,470000
Estelle,63,March,Louisville,210000
<start>
[
    {
        "Name": "Gayle",
        "Age": 35,
        "Birth Month": "January",
        "City": "Dallas",
        "Income": 490000
    },
    {
        "Name": "Bryce",
        "Age": 39,
        "Birth Month": "February",
        "City": "Fort Worth",
        "Income": 415000
    },
    {
        "Name": "Martha",
        "Age": 50,
        "Birth Month": "November",
        "City": "Jacksonville",
        "Income": 470000
    },
    {
        "Name": "Estelle",
        "Age": 63,
        "Birth Month": "March",
        "City": "Louisville",
        "Income": 210000
    }
]
<end>Transform this CSV structure to a JSON format:
Location,Condition,Temperature (C)
Los Angeles,Snowy,36.5
New York,Foggy,38.0
Seattle,Windy,21.0
Phoenix,Snowy,23.4
<start>
[
    {
        "Location": "Los Angeles",
        "Condition": "Snowy",
        "Temperature (C)": 36.5
    },
    {
        "Location": "New York",
        "Condition": "Foggy",
        "Temperature (C)": 38.0
    },
    {
        "Location": "Seattle",
        "Condition": "Windy",
        "Temperature (C)": 21.0
    },
    {
        "Location": "Phoenix",
        "Condition": "Snowy",
        "Temperature (C)": 23.4
    }
]
<end>Convert this plain text to markdown:
Location: Denver | Condition: Sunny | Temperature (C): -3.4 | Humidity (%): 78 | Wind Speed (km/h): 6.8 | Day: Saturday
Location: Seattle | Condition: Sunny | Temperature (C): -6.4 | Humidity (%): 69 | Wind Speed (km/h): 7.4 | Day: Monday
Location: Phoenix | Condition: Snowy | Temperature (C): -5.6 | Humidity (%): 95 | Wind Speed (km/h): 12.1 | Day: Tuesday
Location: Houston | Condition: Rainy | Temperature (C): 23.9 | Humidity (%): 80 | Wind Speed (km/h): 22.6 | Day: Friday
Location: Miami | Condition: Sunny | Temperature (C): 7.4 | Humidity (%): 34 | Wind Speed (km/h): 24.7 | Day: Friday
Location: Phoenix | Condition: Foggy | Temperature (C): 20.7 | Humidity (%): 78 | Wind Speed (km/h): 12.9 | Day: Saturday
Location: Seattle | Condition: Sunny | Temperature (C): 30.0 | Humidity (%): 38 | Wind Speed (km/h): 8.2 | Day: Thursday
Location: Los Angeles | Condition: Sunny | Temperature (C): 0.9 | Humidity (%): 55 | Wind Speed (km/h): 20.8 | Day: Thursday
Location: New York | Condition: Windy | Temperature (C): 23.9 | Humidity (%): 91 | Wind Speed (km/h): 9.2 | Day: Wednesday
<start>
| Location | Condition | Temperature (C) | Humidity (%) | Wind Speed (km/h) | Day |
| --- | --- | --- | --- | --- | --- |
| Denver | Sunny | -3.4 | 78 | 6.8 | Saturday |
| Seattle | Sunny | -6.4 | 69 | 7.4 | Monday |
| Phoenix | Snowy | -5.6 | 95 | 12.1 | Tuesday |
| Houston | Rainy | 23.9 | 80 | 22.6 | Friday |
| Miami | Sunny | 7.4 | 34 | 24.7 | Friday |
| Phoenix | Foggy | 20.7 | 78 | 12.9 | Saturday |
| Seattle | Sunny | 30.0 | 38 | 8.2 | Thursday |
| Los Angeles | Sunny | 0.9 | 55 | 20.8 | Thursday |
| New York | Windy | 23.9 | 91 | 9.2 | Wednesday |
<end>Here's some plain text data, can you convert it to yml?
Condition: Windy | Temperature (C): 6.0 | Wind Speed (km/h): 7.0
Condition: Rainy | Temperature (C): 35.8 | Wind Speed (km/h): 28.3
Condition: Cloudy | Temperature (C): 19.5 | Wind Speed (km/h): 18.4
Condition: Stormy | Temperature (C): 26.7 | Wind Speed (km/h): 28.6
<start>
- Condition: Windy
  Temperature (C): 6.0
  Wind Speed (km/h): 7.0
- Condition: Rainy
  Temperature (C): 35.8
  Wind Speed (km/h): 28.3
- Condition: Cloudy
  Temperature (C): 19.5
  Wind Speed (km/h): 18.4
- Condition: Stormy
  Temperature (C): 26.7
  Wind Speed (km/h): 28.6
<end>Transform this plain text structure to a Yml format:
Product Name: Instrument | Price: 178.76 | Category: Sports
Product Name: Whatchamacallit | Price: 129.53 | Category: Automotive
Product Name: Thingamajig | Price: 225.4 | Category: Household
Product Name: Gizmo | Price: 361.95 | Category: Automotive
<start>
- Category: Sports
  Price: 178.76
  Product Name: Instrument
- Category: Automotive
  Price: 129.53
  Product Name: Whatchamacallit
- Category: Household
  Price: 225.4
  Product Name: Thingamajig
- Category: Automotive
  Price: 361.95
  Product Name: Gizmo
<end>Here's some csv data, can you convert it to yaml?
Restaurant Name,Cuisine,Price Range
Burger Haven,French,$$$$$
Taco Town,French,$$$$
Curry Corner,Indian,$$$
The Steakhouse,American,$$
Pizza Planet,Italian,$
<start>
- Cuisine: French
  Price Range: $$$$$
  Restaurant Name: Burger Haven
- Cuisine: French
  Price Range: $$$$
  Restaurant Name: Taco Town
- Cuisine: Indian
  Price Range: $$$
  Restaurant Name: Curry Corner
- Cuisine: American
  Price Range: $$
  Restaurant Name: The Steakhouse
- Cuisine: Italian
  Price Range: $
  Restaurant Name: Pizza Planet
<end>Convert this Json to yaml:
[
    {
        "SKU": "SKU-1064",
        "Price": 166.63,
        "Stock Quantity": 53,
        "Category": "Sports",
        "Supplier Name": "ACME Corp"
    },
    {
        "SKU": "SKU-1068",
        "Price": 356.06,
        "Stock Quantity": 250,
        "Category": "Household",
        "Supplier Name": "Wonka Industries"
    },
    {
        "SKU": "SKU-1023",
        "Price": 247.51,
        "Stock Quantity": 424,
        "Category": "Household",
        "Supplier Name": "Umbrella Corp"
    },
    {
        "SKU": "SKU-1026",
        "Price": 310.51,
        "Stock Quantity": 347,
        "Category": "Electronics",
        "Supplier Name": "Wayne Enterprises"
    },
    {
        "SKU": "SKU-1066",
        "Price": 105.93,
        "Stock Quantity": 322,
        "Category": "Sports",
        "Supplier Name": "Wayne Enterprises"
    }
]<start>
- Category: Sports
  Price: 166.63
  SKU: SKU-1064
  Stock Quantity: 53
  Supplier Name: ACME Corp
- Category: Household
  Price: 356.06
  SKU: SKU-1068
  Stock Quantity: 250
  Supplier Name: Wonka Industries
- Category: Household
  Price: 247.51
  SKU: SKU-1023
  Stock Quantity: 424
  Supplier Name: Umbrella Corp
- Category: Electronics
  Price: 310.51
  SKU: SKU-1026
  Stock Quantity: 347
  Supplier Name: Wayne Enterprises
- Category: Sports
  Price: 105.93
  SKU: SKU-1066
  Stock Quantity: 322
  Supplier Name: Wayne Enterprises
<end>Please transform the following csv data into YML:
Restaurant Name,Location,Price Range
Vegan Delight,Los Angeles,$$
Pizza Planet,New York,$
Taco Town,San Francisco,$$$
Pizza Planet,San Francisco,$$$
<start>
- Location: Los Angeles
  Price Range: $$
  Restaurant Name: Vegan Delight
- Location: New York
  Price Range: $
  Restaurant Name: Pizza Planet
- Location: San Francisco
  Price Range: $$$
  Restaurant Name: Taco Town
- Location: San Francisco
  Price Range: $$$
  Restaurant Name: Pizza Planet
<end>Here's some PLAIN TEXT data, can you convert it to Markdown?
Date: 2022-11-05 | Open Price: 512.57 | Close Price: 524.65 | Low Price: 299.59 | Volume: 4728799
Date: 2023-12-19 | Open Price: 1082.24 | Close Price: 1395.59 | Low Price: 435.37 | Volume: 6922283
Date: 2015-12-10 | Open Price: 1490.73 | Close Price: 1084.15 | Low Price: 68.16 | Volume: 4726726
Date: 2014-06-07 | Open Price: 1047.69 | Close Price: 696.73 | Low Price: 696.73 | Volume: 8455883
Date: 2020-07-14 | Open Price: 649.28 | Close Price: 552.46 | Low Price: 552.46 | Volume: 600733
<start>
| Date | Open Price | Close Price | Low Price | Volume |
| --- | --- | --- | --- | --- |
| 2022-11-05 | 512.57 | 524.65 | 299.59 | 4728799 |
| 2023-12-19 | 1082.24 | 1395.59 | 435.37 | 6922283 |
| 2015-12-10 | 1490.73 | 1084.15 | 68.16 | 4726726 |
| 2014-06-07 | 1047.69 | 696.73 | 696.73 | 8455883 |
| 2020-07-14 | 649.28 | 552.46 | 552.46 | 600733 |
<end>Transform this Yaml structure to a plain text format:
- Fuel Used (gallons): 65.0
  Start Location: Miami
  Trip Name: Canyon Trek
- Fuel Used (gallons): 21.4
  Start Location: San Francisco
  Trip Name: Historic Route
- Fuel Used (gallons): 84.4
  Start Location: Chicago
  Trip Name: Historic Route
- Fuel Used (gallons): 40.6
  Start Location: San Francisco
  Trip Name: Highway Odyssey
- Fuel Used (gallons): 61.8
  Start Location: Miami
  Trip Name: Forest Journey
- Fuel Used (gallons): 77.3
  Start Location: New York
  Trip Name: Lakeside Retreat
- Fuel Used (gallons): 49.2
  Start Location: San Francisco
  Trip Name: Mountain Adventure
- Fuel Used (gallons): 55.1
  Start Location: Houston
  Trip Name: Coast to Coast
- Fuel Used (gallons): 63.9
  Start Location: Denver
  Trip Name: Historic Route
<start>
Trip Name: Canyon Trek | Start Location: Miami | Fuel Used (gallons): 65.0
Trip Name: Historic Route | Start Location: San Francisco | Fuel Used (gallons): 21.4
Trip Name: Historic Route | Start Location: Chicago | Fuel Used (gallons): 84.4
Trip Name: Highway Odyssey | Start Location: San Francisco | Fuel Used (gallons): 40.6
Trip Name: Forest Journey | Start Location: Miami | Fuel Used (gallons): 61.8
Trip Name: Lakeside Retreat | Start Location: New York | Fuel Used (gallons): 77.3
Trip Name: Mountain Adventure | Start Location: San Francisco | Fuel Used (gallons): 49.2
Trip Name: Coast to Coast | Start Location: Houston | Fuel Used (gallons): 55.1
Trip Name: Historic Route | Start Location: Denver | Fuel Used (gallons): 63.9
<end>Convert this JSON to Csv:
[
    {
        "Company": "AutoDrive",
        "Sector": "Energy",
        "Market Cap": "Mega Cap",
        "Stock Price": 855.41,
        "Annual Revenue (B)": 130.63,
        "Quarter": "Q2"
    },
    {
        "Company": "Foodies",
        "Sector": "Technology",
        "Market Cap": "Small Cap",
        "Stock Price": 311.22,
        "Annual Revenue (B)": 248.25,
        "Quarter": "Q4"
    },
    {
        "Company": "EcoEnergy",
        "Sector": "Finance",
        "Market Cap": "Mega Cap",
        "Stock Price": 629.45,
        "Annual Revenue (B)": 104.19,
        "Quarter": "Q4"
    },
    {
        "Company": "TechCorp",
        "Sector": "Finance",
        "Market Cap": "Mega Cap",
        "Stock Price": 211.65,
        "Annual Revenue (B)": 141.54,
        "Quarter": "Q1"
    },
    {
        "Company": "TechCorp",
        "Sector": "Automotive",
        "Market Cap": "Small Cap",
        "Stock Price": 16.39,
        "Annual Revenue (B)": 461.71,
        "Quarter": "Q3"
    },
    {
        "Company": "Foodies",
        "Sector": "Energy",
        "Market Cap": "Mid Cap",
        "Stock Price": 647.49,
        "Annual Revenue (B)": 130.63,
        "Quarter": "Q1"
    },
    {
        "Company": "Foodies",
        "Sector": "Biotech",
        "Market Cap": "Large Cap",
        "Stock Price": 294.84,
        "Annual Revenue (B)": 230.74,
        "Quarter": "Q4"
    },
    {
        "Company": "EcoEnergy",
        "Sector": "Technology",
        "Market Cap": "Large Cap",
        "Stock Price": 796.8,
        "Annual Revenue (B)": 485.95,
        "Quarter": "Q1"
    },
    {
        "Company": "AeroSpace",
        "Sector": "Finance",
        "Market Cap": "Large Cap",
        "Stock Price": 511.23,
        "Annual Revenue (B)": 383.8,
        "Quarter": "Q2"
    },
    {
        "Company": "TechCorp",
        "Sector": "Retail",
        "Market Cap": "Mega Cap",
        "Stock Price": 855.41,
        "Annual Revenue (B)": 187.11,
        "Quarter": "Q4"
    }
]<start>
Company,Sector,Market Cap,Stock Price,Annual Revenue (B),Quarter
AutoDrive,Energy,Mega Cap,855.41,130.63,Q2
Foodies,Technology,Small Cap,311.22,248.25,Q4
EcoEnergy,Finance,Mega Cap,629.45,104.19,Q4
TechCorp,Finance,Mega Cap,211.65,141.54,Q1
TechCorp,Automotive,Small Cap,16.39,461.71,Q3
Foodies,Energy,Mid Cap,647.49,130.63,Q1
Foodies,Biotech,Large Cap,294.84,230.74,Q4
EcoEnergy,Technology,Large Cap,796.8,485.95,Q1
AeroSpace,Finance,Large Cap,511.23,383.8,Q2
TechCorp,Retail,Mega Cap,855.41,187.11,Q4
<end>