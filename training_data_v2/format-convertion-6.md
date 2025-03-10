Transform this Csv structure to a yml format:
Name,Birth Month
Brody,September
Delores,May
Arianna,April
Hudson,July
Terrence,May
<start>
- Birth Month: September
  Name: Brody
- Birth Month: May
  Name: Delores
- Birth Month: April
  Name: Arianna
- Birth Month: July
  Name: Hudson
- Birth Month: May
  Name: Terrence
<end>Transform this json structure to a Markdown format:
[
    {
        "Trip Name": "Lakeside Retreat",
        "Start Location": "Miami",
        "Distance (miles)": 2090.4,
        "Fuel Used (gallons)": 7.6
    },
    {
        "Trip Name": "Valley Voyage",
        "Start Location": "San Francisco",
        "Distance (miles)": 2834.1,
        "Fuel Used (gallons)": 7.2
    },
    {
        "Trip Name": "Lakeside Retreat",
        "Start Location": "Denver",
        "Distance (miles)": 2796.4,
        "Fuel Used (gallons)": 82.1
    }
]<start>
| Trip Name | Start Location | Distance (miles) | Fuel Used (gallons) |
| --- | --- | --- | --- |
| Lakeside Retreat | Miami | 2090.4 | 7.6 |
| Valley Voyage | San Francisco | 2834.1 | 7.2 |
| Lakeside Retreat | Denver | 2796.4 | 82.1 |
<end>Convert this plain text to YAML:
Company: AeroSpace | Market Cap: Mid Cap | Stock Price: 720.75
Company: EcoEnergy | Market Cap: Small Cap | Stock Price: 250.03
Company: EcoEnergy | Market Cap: Large Cap | Stock Price: 417.74
Company: EcoEnergy | Market Cap: Mid Cap | Stock Price: 951.77
Company: AutoDrive | Market Cap: Mega Cap | Stock Price: 869.31
Company: Foodies | Market Cap: Mid Cap | Stock Price: 866.29
Company: GlobalTrade | Market Cap: Small Cap | Stock Price: 388.09
Company: AutoDrive | Market Cap: Mega Cap | Stock Price: 710.48
<start>
- Company: AeroSpace
  Market Cap: Mid Cap
  Stock Price: 720.75
- Company: EcoEnergy
  Market Cap: Small Cap
  Stock Price: 250.03
- Company: EcoEnergy
  Market Cap: Large Cap
  Stock Price: 417.74
- Company: EcoEnergy
  Market Cap: Mid Cap
  Stock Price: 951.77
- Company: AutoDrive
  Market Cap: Mega Cap
  Stock Price: 869.31
- Company: Foodies
  Market Cap: Mid Cap
  Stock Price: 866.29
- Company: GlobalTrade
  Market Cap: Small Cap
  Stock Price: 388.09
- Company: AutoDrive
  Market Cap: Mega Cap
  Stock Price: 710.48
<end>Can you change this Markdown into PLAIN TEXT?
| Company | Open Price | High Price | Volume |
| --- | --- | --- | --- |
| HealthGen | 482.26 | 1192.06 | 6608168 |
| AutoMotive | 486.72 | 486.72 | 8265543 |
| AeroSystems | 105.43 | 105.43 | 1873520 |
| RetailWorld | 793.83 | 1455.94 | 4491285 |
| AutoMotive | 370.02 | 1438.51 | 8735844 |
| MediaGroup | 708.47 | 799.49 | 7766917 |
| HealthGen | 163.56 | 1022.76 | 2784939 |<start>
Company: HealthGen | Open Price: 482.26 | High Price: 1192.06 | Volume: 6608168
Company: AutoMotive | Open Price: 486.72 | High Price: 486.72 | Volume: 8265543
Company: AeroSystems | Open Price: 105.43 | High Price: 105.43 | Volume: 1873520
Company: RetailWorld | Open Price: 793.83 | High Price: 1455.94 | Volume: 4491285
Company: AutoMotive | Open Price: 370.02 | High Price: 1438.51 | Volume: 8735844
Company: MediaGroup | Open Price: 708.47 | High Price: 799.49 | Volume: 7766917
Company: HealthGen | Open Price: 163.56 | High Price: 1022.76 | Volume: 2784939
<end>Here's some csv data, can you convert it to PLAIN TEXT?
Company,Date,Open Price,Close Price,High Price
BioLife,2015-07-09,658.59,1421.96,1421.96
FinanceTrust,2021-02-28,31.81,795.02,795.02
TechnoCorp,2020-03-08,173.16,830.47,830.47
AeroSystems,2011-12-18,864.85,1004.41,1004.41
<start>
Company: BioLife | Date: 2015-07-09 | Open Price: 658.59 | Close Price: 1421.96 | High Price: 1421.96
Company: FinanceTrust | Date: 2021-02-28 | Open Price: 31.81 | Close Price: 795.02 | High Price: 795.02
Company: TechnoCorp | Date: 2020-03-08 | Open Price: 173.16 | Close Price: 830.47 | High Price: 830.47
Company: AeroSystems | Date: 2011-12-18 | Open Price: 864.85 | Close Price: 1004.41 | High Price: 1004.41
<end>Transform this json structure to a Csv format:
[
    {
        "Product Name": "Doohickey",
        "SKU": "SKU-1045",
        "Price": 172.06,
        "Stock Quantity": 476,
        "Category": "Electronics",
        "Supplier Name": "ACME Corp"
    },
    {
        "Product Name": "Gizmo",
        "SKU": "SKU-1091",
        "Price": 122.47,
        "Stock Quantity": 156,
        "Category": "Automotive",
        "Supplier Name": "ACME Corp"
    },
    {
        "Product Name": "Widget",
        "SKU": "SKU-1090",
        "Price": 342.81,
        "Stock Quantity": 431,
        "Category": "Toys",
        "Supplier Name": "Wonka Industries"
    },
    {
        "Product Name": "Apparatus",
        "SKU": "SKU-1039",
        "Price": 244.54,
        "Stock Quantity": 225,
        "Category": "Toys",
        "Supplier Name": "Wayne Enterprises"
    },
    {
        "Product Name": "Instrument",
        "SKU": "SKU-1032",
        "Price": 45.15,
        "Stock Quantity": 385,
        "Category": "Electronics",
        "Supplier Name": "Wonka Industries"
    },
    {
        "Product Name": "Device",
        "SKU": "SKU-1040",
        "Price": 451.26,
        "Stock Quantity": 159,
        "Category": "Automotive",
        "Supplier Name": "ACME Corp"
    },
    {
        "Product Name": "Whatchamacallit",
        "SKU": "SKU-1048",
        "Price": 162.17,
        "Stock Quantity": 393,
        "Category": "Household",
        "Supplier Name": "Wonka Industries"
    },
    {
        "Product Name": "Contraption",
        "SKU": "SKU-1007",
        "Price": 351.7,
        "Stock Quantity": 154,
        "Category": "Toys",
        "Supplier Name": "Globex"
    }
]<start>
Product Name,SKU,Price,Stock Quantity,Category,Supplier Name
Doohickey,SKU-1045,172.06,476,Electronics,ACME Corp
Gizmo,SKU-1091,122.47,156,Automotive,ACME Corp
Widget,SKU-1090,342.81,431,Toys,Wonka Industries
Apparatus,SKU-1039,244.54,225,Toys,Wayne Enterprises
Instrument,SKU-1032,45.15,385,Electronics,Wonka Industries
Device,SKU-1040,451.26,159,Automotive,ACME Corp
Whatchamacallit,SKU-1048,162.17,393,Household,Wonka Industries
Contraption,SKU-1007,351.7,154,Toys,Globex
<end>Transform this plain text structure to a yaml format:
Device ID: device-0100 | Device Type: Temperature Sensor | Battery Level (%): 49.2 | Reading Value: -13.66 | Timestamp: 2023-02-19 16:53:56
Device ID: device-0055 | Device Type: Humidity Sensor | Battery Level (%): 28.3 | Reading Value: -19.31 | Timestamp: 2021-11-25 17:30:19
Device ID: device-0063 | Device Type: Light Sensor | Battery Level (%): 46.3 | Reading Value: 5.44 | Timestamp: 2022-07-05 18:16:02
Device ID: device-0078 | Device Type: Pressure Sensor | Battery Level (%): 56.4 | Reading Value: -1.98 | Timestamp: 2022-07-08 19:24:06
<start>
- Battery Level (%): 49.2
  Device ID: device-0100
  Device Type: Temperature Sensor
  Reading Value: -13.66
  Timestamp: '2023-02-19 16:53:56'
- Battery Level (%): 28.3
  Device ID: device-0055
  Device Type: Humidity Sensor
  Reading Value: -19.31
  Timestamp: '2021-11-25 17:30:19'
- Battery Level (%): 46.3
  Device ID: device-0063
  Device Type: Light Sensor
  Reading Value: 5.44
  Timestamp: '2022-07-05 18:16:02'
- Battery Level (%): 56.4
  Device ID: device-0078
  Device Type: Pressure Sensor
  Reading Value: -1.98
  Timestamp: '2022-07-08 19:24:06'
<end>Please transform the following json data into markdown:
[
    {
        "Database Name": "InventoryDB",
        "Queries per Second": 866.1,
        "Cache Hit Ratio (%)": 90.59,
        "Connection Count": 119,
        "Average Latency (ms)": 15.57,
        "Timestamp": "2021-05-22 01:54:50"
    },
    {
        "Database Name": "SessionsDB",
        "Queries per Second": 271.89,
        "Cache Hit Ratio (%)": 77.92,
        "Connection Count": 465,
        "Average Latency (ms)": 44.76,
        "Timestamp": "2023-01-03 18:15:51"
    },
    {
        "Database Name": "OrdersDB",
        "Queries per Second": 3948.14,
        "Cache Hit Ratio (%)": 83.55,
        "Connection Count": 188,
        "Average Latency (ms)": 29.88,
        "Timestamp": "2021-11-28 12:09:14"
    },
    {
        "Database Name": "SessionsDB",
        "Queries per Second": 1434.63,
        "Cache Hit Ratio (%)": 99.58,
        "Connection Count": 386,
        "Average Latency (ms)": 38.2,
        "Timestamp": "2021-05-15 00:17:40"
    },
    {
        "Database Name": "SessionsDB",
        "Queries per Second": 4902.54,
        "Cache Hit Ratio (%)": 91.18,
        "Connection Count": 237,
        "Average Latency (ms)": 20.12,
        "Timestamp": "2021-11-27 11:19:52"
    }
]<start>
| Database Name | Queries per Second | Cache Hit Ratio (%) | Connection Count | Average Latency (ms) | Timestamp |
| --- | --- | --- | --- | --- | --- |
| InventoryDB | 866.1 | 90.59 | 119 | 15.57 | 2021-05-22 01:54:50 |
| SessionsDB | 271.89 | 77.92 | 465 | 44.76 | 2023-01-03 18:15:51 |
| OrdersDB | 3948.14 | 83.55 | 188 | 29.88 | 2021-11-28 12:09:14 |
| SessionsDB | 1434.63 | 99.58 | 386 | 38.2 | 2021-05-15 00:17:40 |
| SessionsDB | 4902.54 | 91.18 | 237 | 20.12 | 2021-11-27 11:19:52 |
<end>Convert this markdown to json:
| Location | Condition | Temperature (C) | Day |
| --- | --- | --- | --- |
| Houston | Sunny | 12.5 | Monday |
| Chicago | Rainy | -3.3 | Monday |
| Chicago | Stormy | 34.7 | Friday |
| Houston | Foggy | 4.4 | Thursday |
| Denver | Foggy | 28.6 | Sunday |
| Seattle | Cloudy | 25.4 | Sunday |<start>
[
    {
        "Location": "Houston",
        "Condition": "Sunny",
        "Temperature (C)": 12.5,
        "Day": "Monday"
    },
    {
        "Location": "Chicago",
        "Condition": "Rainy",
        "Temperature (C)": -3.3,
        "Day": "Monday"
    },
    {
        "Location": "Chicago",
        "Condition": "Stormy",
        "Temperature (C)": 34.7,
        "Day": "Friday"
    },
    {
        "Location": "Houston",
        "Condition": "Foggy",
        "Temperature (C)": 4.4,
        "Day": "Thursday"
    },
    {
        "Location": "Denver",
        "Condition": "Foggy",
        "Temperature (C)": 28.6,
        "Day": "Sunday"
    },
    {
        "Location": "Seattle",
        "Condition": "Cloudy",
        "Temperature (C)": 25.4,
        "Day": "Sunday"
    }
]
<end>Can you change this yml into markdown?
- Close Price: 1021.23
  Date: '2020-01-16'
  High Price: 1021.23
  Low Price: 399.34
  Open Price: 399.34
  Volume: 9794627
- Close Price: 71.8
  Date: '2010-11-10'
  High Price: 1413.53
  Low Price: 71.8
  Open Price: 1413.53
  Volume: 2046962
- Close Price: 996.26
  Date: '2021-03-28'
  High Price: 1133.94
  Low Price: 349.75
  Open Price: 349.75
  Volume: 8464040
- Close Price: 147.93
  Date: '2022-06-09'
  High Price: 682.48
  Low Price: 147.93
  Open Price: 682.48
  Volume: 8523084
- Close Price: 733.61
  Date: '2012-11-09'
  High Price: 733.61
  Low Price: 147.93
  Open Price: 403.94
  Volume: 4111765
- Close Price: 878.21
  Date: '2012-01-16'
  High Price: 878.21
  Low Price: 294.83
  Open Price: 294.83
  Volume: 2046962
- Close Price: 1413.53
  Date: '2020-02-14'
  High Price: 1413.53
  Low Price: 1016.74
  Open Price: 1016.74
  Volume: 1724338
<start>
| Date | Open Price | Close Price | High Price | Low Price | Volume |
| --- | --- | --- | --- | --- | --- |
| 2020-01-16 | 399.34 | 1021.23 | 1021.23 | 399.34 | 9794627 |
| 2010-11-10 | 1413.53 | 71.8 | 1413.53 | 71.8 | 2046962 |
| 2021-03-28 | 349.75 | 996.26 | 1133.94 | 349.75 | 8464040 |
| 2022-06-09 | 682.48 | 147.93 | 682.48 | 147.93 | 8523084 |
| 2012-11-09 | 403.94 | 733.61 | 733.61 | 147.93 | 4111765 |
| 2012-01-16 | 294.83 | 878.21 | 878.21 | 294.83 | 2046962 |
| 2020-02-14 | 1016.74 | 1413.53 | 1413.53 | 1016.74 | 1724338 |
<end>Here's some csv data, can you convert it to Plain text?
Database Name,Queries per Second,Cache Hit Ratio (%),Connection Count
ProfilesDB,3162.89,96.21,485
UserDB,2580.4,72.81,227
SessionsDB,3452.06,72.12,413
SalesDB,4785.47,88.01,451
<start>
Database Name: ProfilesDB | Queries per Second: 3162.89 | Cache Hit Ratio (%): 96.21 | Connection Count: 485
Database Name: UserDB | Queries per Second: 2580.4 | Cache Hit Ratio (%): 72.81 | Connection Count: 227
Database Name: SessionsDB | Queries per Second: 3452.06 | Cache Hit Ratio (%): 72.12 | Connection Count: 413
Database Name: SalesDB | Queries per Second: 4785.47 | Cache Hit Ratio (%): 88.01 | Connection Count: 451
<end>Transform this Csv structure to a plain text format:
Restaurant Name,Cuisine,Location
Curry Corner,Italian,Miami
The Steakhouse,American,San Francisco
The Golden Spoon,Italian,San Francisco
Pizza Planet,French,Chicago
Vegan Delight,American,Miami
<start>
Restaurant Name: Curry Corner | Cuisine: Italian | Location: Miami
Restaurant Name: The Steakhouse | Cuisine: American | Location: San Francisco
Restaurant Name: The Golden Spoon | Cuisine: Italian | Location: San Francisco
Restaurant Name: Pizza Planet | Cuisine: French | Location: Chicago
Restaurant Name: Vegan Delight | Cuisine: American | Location: Miami
<end>Can you change this YML into csv?
- Annual Revenue (B): 434.36
  Company: EcoEnergy
  Market Cap: Mega Cap
  Quarter: Q2
  Sector: Aerospace
  Stock Price: 276.22
- Annual Revenue (B): 60.03
  Company: FinanceWorks
  Market Cap: Small Cap
  Quarter: Q4
  Sector: Biotech
  Stock Price: 267.5
- Annual Revenue (B): 318.57
  Company: BioPharm
  Market Cap: Mega Cap
  Quarter: Q1
  Sector: Automotive
  Stock Price: 914.96
- Annual Revenue (B): 111.83
  Company: HealthPlus
  Market Cap: Small Cap
  Quarter: Q2
  Sector: Automotive
  Stock Price: 135.86
- Annual Revenue (B): 412.58
  Company: AutoDrive
  Market Cap: Mid Cap
  Quarter: Q4
  Sector: Biotech
  Stock Price: 327.5
- Annual Revenue (B): 113.1
  Company: Foodies
  Market Cap: Mega Cap
  Quarter: Q1
  Sector: Biotech
  Stock Price: 32.76
- Annual Revenue (B): 405.1
  Company: EcoEnergy
  Market Cap: Mega Cap
  Quarter: Q2
  Sector: Aerospace
  Stock Price: 641.71
<start>
Company,Sector,Market Cap,Stock Price,Annual Revenue (B),Quarter
EcoEnergy,Aerospace,Mega Cap,276.22,434.36,Q2
FinanceWorks,Biotech,Small Cap,267.5,60.03,Q4
BioPharm,Automotive,Mega Cap,914.96,318.57,Q1
HealthPlus,Automotive,Small Cap,135.86,111.83,Q2
AutoDrive,Biotech,Mid Cap,327.5,412.58,Q4
Foodies,Biotech,Mega Cap,32.76,113.1,Q1
EcoEnergy,Aerospace,Mega Cap,641.71,405.1,Q2
<end>Can you change this plain text into MARKDOWN?
Product Name: Gadget | SKU: SKU-1086 | Price: 301.27 | Stock Quantity: 77 | Category: Household | Supplier Name: Wayne Enterprises
Product Name: Whatchamacallit | SKU: SKU-1093 | Price: 220.75 | Stock Quantity: 278 | Category: Toys | Supplier Name: Globex
Product Name: Apparatus | SKU: SKU-1047 | Price: 277.62 | Stock Quantity: 269 | Category: Sports | Supplier Name: Wayne Enterprises
Product Name: Contraption | SKU: SKU-1005 | Price: 419.3 | Stock Quantity: 488 | Category: Toys | Supplier Name: Wayne Enterprises
Product Name: Apparatus | SKU: SKU-1075 | Price: 298.16 | Stock Quantity: 345 | Category: Electronics | Supplier Name: Wonka Industries
Product Name: Doohickey | SKU: SKU-1060 | Price: 473.36 | Stock Quantity: 334 | Category: Sports | Supplier Name: Globex
<start>
| Product Name | SKU | Price | Stock Quantity | Category | Supplier Name |
| --- | --- | --- | --- | --- | --- |
| Gadget | SKU-1086 | 301.27 | 77 | Household | Wayne Enterprises |
| Whatchamacallit | SKU-1093 | 220.75 | 278 | Toys | Globex |
| Apparatus | SKU-1047 | 277.62 | 269 | Sports | Wayne Enterprises |
| Contraption | SKU-1005 | 419.3 | 488 | Toys | Wayne Enterprises |
| Apparatus | SKU-1075 | 298.16 | 345 | Electronics | Wonka Industries |
| Doohickey | SKU-1060 | 473.36 | 334 | Sports | Globex |
<end>Transform this csv structure to a markdown format:
Device Type,Battery Level (%),Reading Value,Timestamp
Temperature Sensor,79.4,70.49,2023-01-07 14:02:31
Motion Detector,20.4,41.87,2021-05-06 20:26:11
Humidity Sensor,61.6,-35.33,2022-04-21 05:04:52
Temperature Sensor,85.5,55.89,2023-11-04 09:47:43
<start>
| Device Type | Battery Level (%) | Reading Value | Timestamp |
| --- | --- | --- | --- |
| Temperature Sensor | 79.4 | 70.49 | 2023-01-07 14:02:31 |
| Motion Detector | 20.4 | 41.87 | 2021-05-06 20:26:11 |
| Humidity Sensor | 61.6 | -35.33 | 2022-04-21 05:04:52 |
| Temperature Sensor | 85.5 | 55.89 | 2023-11-04 09:47:43 |
<end>Transform this CSV structure to a json format:
Company,Sector,Annual Revenue (B),Quarter
HealthPlus,Technology,427.34,Q1
AutoDrive,Retail,113.01,Q3
BioPharm,Aerospace,126.06,Q3
TechCorp,Retail,477.56,Q4
FinanceWorks,Automotive,286.44,Q4
AeroSpace,Energy,435.0,Q3
RetailHub,Healthcare,228.25,Q1
GlobalTrade,Retail,359.03,Q1
<start>
[
    {
        "Company": "HealthPlus",
        "Sector": "Technology",
        "Annual Revenue (B)": 427.34,
        "Quarter": "Q1"
    },
    {
        "Company": "AutoDrive",
        "Sector": "Retail",
        "Annual Revenue (B)": 113.01,
        "Quarter": "Q3"
    },
    {
        "Company": "BioPharm",
        "Sector": "Aerospace",
        "Annual Revenue (B)": 126.06,
        "Quarter": "Q3"
    },
    {
        "Company": "TechCorp",
        "Sector": "Retail",
        "Annual Revenue (B)": 477.56,
        "Quarter": "Q4"
    },
    {
        "Company": "FinanceWorks",
        "Sector": "Automotive",
        "Annual Revenue (B)": 286.44,
        "Quarter": "Q4"
    },
    {
        "Company": "AeroSpace",
        "Sector": "Energy",
        "Annual Revenue (B)": 435.0,
        "Quarter": "Q3"
    },
    {
        "Company": "RetailHub",
        "Sector": "Healthcare",
        "Annual Revenue (B)": 228.25,
        "Quarter": "Q1"
    },
    {
        "Company": "GlobalTrade",
        "Sector": "Retail",
        "Annual Revenue (B)": 359.03,
        "Quarter": "Q1"
    }
]
<end>Transform this csv structure to a markdown format:
Queries per Second,Cache Hit Ratio (%),Connection Count,Average Latency (ms),Timestamp
856.75,78.94,29,21.55,2022-03-25 12:51:48
934.82,82.49,186,65.07,2021-06-26 03:25:37
4450.3,89.88,78,17.51,2021-02-22 15:29:10
3665.05,86.15,14,16.42,2023-06-10 08:58:58
1324.62,76.42,31,17.51,2022-09-01 07:41:32
2946.07,96.11,441,3.46,2023-02-27 01:19:43
1266.3,92.69,114,15.57,2021-10-10 03:05:34
<start>
| Queries per Second | Cache Hit Ratio (%) | Connection Count | Average Latency (ms) | Timestamp |
| --- | --- | --- | --- | --- |
| 856.75 | 78.94 | 29 | 21.55 | 2022-03-25 12:51:48 |
| 934.82 | 82.49 | 186 | 65.07 | 2021-06-26 03:25:37 |
| 4450.3 | 89.88 | 78 | 17.51 | 2021-02-22 15:29:10 |
| 3665.05 | 86.15 | 14 | 16.42 | 2023-06-10 08:58:58 |
| 1324.62 | 76.42 | 31 | 17.51 | 2022-09-01 07:41:32 |
| 2946.07 | 96.11 | 441 | 3.46 | 2023-02-27 01:19:43 |
| 1266.3 | 92.69 | 114 | 15.57 | 2021-10-10 03:05:34 |
<end>Transform this CSV structure to a markdown format:
Title,Genre,Publication Year,Rating
The Crystal Key,Science Fiction,1993,4.8
The Last Sky,Romance,2008,2.3
Whispers of the Abyss,Mystery,1967,2.0
Shadows of Solitude,Science Fiction,2015,2.3
<start>
| Title | Genre | Publication Year | Rating |
| --- | --- | --- | --- |
| The Crystal Key | Science Fiction | 1993 | 4.8 |
| The Last Sky | Romance | 2008 | 2.3 |
| Whispers of the Abyss | Mystery | 1967 | 2.0 |
| Shadows of Solitude | Science Fiction | 2015 | 2.3 |
<end>Please transform the following Json data into Yaml:
[
    {
        "Location": "Los Angeles",
        "Condition": "Snowy",
        "Temperature (C)": 27.6,
        "Humidity (%)": 45,
        "Wind Speed (km/h)": 6.1,
        "Day": "Thursday"
    },
    {
        "Location": "Chicago",
        "Condition": "Rainy",
        "Temperature (C)": 24.9,
        "Humidity (%)": 71,
        "Wind Speed (km/h)": 24.0,
        "Day": "Tuesday"
    },
    {
        "Location": "Houston",
        "Condition": "Sunny",
        "Temperature (C)": 17.6,
        "Humidity (%)": 49,
        "Wind Speed (km/h)": 17.8,
        "Day": "Friday"
    },
    {
        "Location": "Denver",
        "Condition": "Cloudy",
        "Temperature (C)": 26.6,
        "Humidity (%)": 20,
        "Wind Speed (km/h)": 14.8,
        "Day": "Friday"
    },
    {
        "Location": "Phoenix",
        "Condition": "Sunny",
        "Temperature (C)": 0.6,
        "Humidity (%)": 39,
        "Wind Speed (km/h)": 4.7,
        "Day": "Monday"
    },
    {
        "Location": "Seattle",
        "Condition": "Foggy",
        "Temperature (C)": 28.1,
        "Humidity (%)": 55,
        "Wind Speed (km/h)": 20.7,
        "Day": "Saturday"
    },
    {
        "Location": "Miami",
        "Condition": "Sunny",
        "Temperature (C)": 19.2,
        "Humidity (%)": 27,
        "Wind Speed (km/h)": 11.0,
        "Day": "Saturday"
    }
]<start>
- Condition: Snowy
  Day: Thursday
  Humidity (%): 45
  Location: Los Angeles
  Temperature (C): 27.6
  Wind Speed (km/h): 6.1
- Condition: Rainy
  Day: Tuesday
  Humidity (%): 71
  Location: Chicago
  Temperature (C): 24.9
  Wind Speed (km/h): 24.0
- Condition: Sunny
  Day: Friday
  Humidity (%): 49
  Location: Houston
  Temperature (C): 17.6
  Wind Speed (km/h): 17.8
- Condition: Cloudy
  Day: Friday
  Humidity (%): 20
  Location: Denver
  Temperature (C): 26.6
  Wind Speed (km/h): 14.8
- Condition: Sunny
  Day: Monday
  Humidity (%): 39
  Location: Phoenix
  Temperature (C): 0.6
  Wind Speed (km/h): 4.7
- Condition: Foggy
  Day: Saturday
  Humidity (%): 55
  Location: Seattle
  Temperature (C): 28.1
  Wind Speed (km/h): 20.7
- Condition: Sunny
  Day: Saturday
  Humidity (%): 27
  Location: Miami
  Temperature (C): 19.2
  Wind Speed (km/h): 11.0
<end>Please transform the following markdown data into Yml:
| Start Location | End Location | Fuel Used (gallons) |
| --- | --- | --- |
| New York | Los Angeles | 50.6 |
| Denver | San Francisco | 28.1 |
| Chicago | Los Angeles | 59.6 |<start>
- End Location: Los Angeles
  Fuel Used (gallons): 50.6
  Start Location: New York
- End Location: San Francisco
  Fuel Used (gallons): 28.1
  Start Location: Denver
- End Location: Los Angeles
  Fuel Used (gallons): 59.6
  Start Location: Chicago
<end>Transform this PLAIN TEXT structure to a Yml format:
Device Type: Pressure Sensor | Location: Kitchen | Battery Level (%): 74.6 | Reading Value: -37.12 | Timestamp: 2021-06-05 10:20:58
Device Type: Pressure Sensor | Location: Kitchen | Battery Level (%): 69.6 | Reading Value: 33.7 | Timestamp: 2023-03-01 07:08:18
Device Type: Motion Detector | Location: Hallway | Battery Level (%): 39.5 | Reading Value: 73.11 | Timestamp: 2022-07-27 11:02:47
Device Type: Humidity Sensor | Location: Bathroom | Battery Level (%): 71.5 | Reading Value: -25.91 | Timestamp: 2022-10-02 20:27:02
Device Type: Pressure Sensor | Location: Garden | Battery Level (%): 74.6 | Reading Value: 69.52 | Timestamp: 2021-01-23 00:45:53
Device Type: Pressure Sensor | Location: Kitchen | Battery Level (%): 21.0 | Reading Value: 18.11 | Timestamp: 2022-07-01 01:52:16
<start>
- Battery Level (%): 74.6
  Device Type: Pressure Sensor
  Location: Kitchen
  Reading Value: -37.12
  Timestamp: '2021-06-05 10:20:58'
- Battery Level (%): 69.6
  Device Type: Pressure Sensor
  Location: Kitchen
  Reading Value: 33.7
  Timestamp: '2023-03-01 07:08:18'
- Battery Level (%): 39.5
  Device Type: Motion Detector
  Location: Hallway
  Reading Value: 73.11
  Timestamp: '2022-07-27 11:02:47'
- Battery Level (%): 71.5
  Device Type: Humidity Sensor
  Location: Bathroom
  Reading Value: -25.91
  Timestamp: '2022-10-02 20:27:02'
- Battery Level (%): 74.6
  Device Type: Pressure Sensor
  Location: Garden
  Reading Value: 69.52
  Timestamp: '2021-01-23 00:45:53'
- Battery Level (%): 21.0
  Device Type: Pressure Sensor
  Location: Kitchen
  Reading Value: 18.11
  Timestamp: '2022-07-01 01:52:16'
<end>Here's some markdown data, can you convert it to plain text?
| Device ID | Device Type | Battery Level (%) | Reading Value | Timestamp |
| --- | --- | --- | --- | --- |
| device-0096 | Motion Detector | 36.2 | 79.24 | 2021-04-23 10:21:54 |
| device-0093 | Temperature Sensor | 20.7 | 72.9 | 2021-06-04 23:22:28 |
| device-0023 | Pressure Sensor | 68.1 | -18.05 | 2021-03-19 00:07:33 |
| device-0071 | Light Sensor | 34.5 | -1.62 | 2021-05-07 17:48:35 |<start>
Device ID: device-0096 | Device Type: Motion Detector | Battery Level (%): 36.2 | Reading Value: 79.24 | Timestamp: 2021-04-23 10:21:54
Device ID: device-0093 | Device Type: Temperature Sensor | Battery Level (%): 20.7 | Reading Value: 72.9 | Timestamp: 2021-06-04 23:22:28
Device ID: device-0023 | Device Type: Pressure Sensor | Battery Level (%): 68.1 | Reading Value: -18.05 | Timestamp: 2021-03-19 00:07:33
Device ID: device-0071 | Device Type: Light Sensor | Battery Level (%): 34.5 | Reading Value: -1.62 | Timestamp: 2021-05-07 17:48:35
<end>Transform this Yaml structure to a Csv format:
- Day: Monday
  Temperature (C): -1.7
  Wind Speed (km/h): 13.8
- Day: Monday
  Temperature (C): -8.3
  Wind Speed (km/h): 12.0
- Day: Thursday
  Temperature (C): 26.8
  Wind Speed (km/h): 18.0
<start>
Temperature (C),Wind Speed (km/h),Day
-1.7,13.8,Monday
-8.3,12.0,Monday
26.8,18.0,Thursday
<end>Transform this Plain text structure to a MARKDOWN format:
Title: Legends of the Rift | Author: Kara Firebrand | Genre: Historical | Rating: 1.1
Title: Tales of the Brave | Author: Orion Frostblade | Genre: Historical | Rating: 2.3
Title: Shadows of Solitude | Author: Orion Frostblade | Genre: Non-Fiction | Rating: 1.2
Title: Echoes of Eternity | Author: Elara Moonshadow | Genre: Non-Fiction | Rating: 1.9
Title: Shadows of Solitude | Author: Rowan Ashborne | Genre: Science Fiction | Rating: 3.7
Title: Tales of the Brave | Author: Draven Blackthorn | Genre: Mystery | Rating: 3.0
Title: The Silent Grove | Author: Sylvia Nightshade | Genre: Horror | Rating: 4.4
Title: A Journey Through Time | Author: Thorne Ironwood | Genre: Romance | Rating: 4.2
Title: The Last Sky | Author: Sylvia Nightshade | Genre: Thriller | Rating: 4.9
<start>
| Title | Author | Genre | Rating |
| --- | --- | --- | --- |
| Legends of the Rift | Kara Firebrand | Historical | 1.1 |
| Tales of the Brave | Orion Frostblade | Historical | 2.3 |
| Shadows of Solitude | Orion Frostblade | Non-Fiction | 1.2 |
| Echoes of Eternity | Elara Moonshadow | Non-Fiction | 1.9 |
| Shadows of Solitude | Rowan Ashborne | Science Fiction | 3.7 |
| Tales of the Brave | Draven Blackthorn | Mystery | 3.0 |
| The Silent Grove | Sylvia Nightshade | Horror | 4.4 |
| A Journey Through Time | Thorne Ironwood | Romance | 4.2 |
| The Last Sky | Sylvia Nightshade | Thriller | 4.9 |
<end>Please transform the following CSV data into markdown:
Restaurant Name,Cuisine,Rating
Taco Town,Indian,5
The Steakhouse,Italian,3
The Steakhouse,American,5
<start>
| Restaurant Name | Cuisine | Rating |
| --- | --- | --- |
| Taco Town | Indian | 5 |
| The Steakhouse | Italian | 3 |
| The Steakhouse | American | 5 |
<end>Please transform the following Markdown data into Plain text:
| Product Name | SKU | Stock Quantity | Category | Supplier Name |
| --- | --- | --- | --- | --- |
| Instrument | SKU-1016 | 230 | Automotive | Wonka Industries |
| Gadget | SKU-1045 | 7 | Automotive | ACME Corp |
| Apparatus | SKU-1033 | 340 | Household | Wonka Industries |
| Thingamajig | SKU-1073 | 138 | Toys | ACME Corp |
| Apparatus | SKU-1094 | 452 | Sports | Umbrella Corp |
| Doohickey | SKU-1089 | 228 | Household | Wayne Enterprises |<start>
Product Name: Instrument | SKU: SKU-1016 | Stock Quantity: 230 | Category: Automotive | Supplier Name: Wonka Industries
Product Name: Gadget | SKU: SKU-1045 | Stock Quantity: 7 | Category: Automotive | Supplier Name: ACME Corp
Product Name: Apparatus | SKU: SKU-1033 | Stock Quantity: 340 | Category: Household | Supplier Name: Wonka Industries
Product Name: Thingamajig | SKU: SKU-1073 | Stock Quantity: 138 | Category: Toys | Supplier Name: ACME Corp
Product Name: Apparatus | SKU: SKU-1094 | Stock Quantity: 452 | Category: Sports | Supplier Name: Umbrella Corp
Product Name: Doohickey | SKU: SKU-1089 | Stock Quantity: 228 | Category: Household | Supplier Name: Wayne Enterprises
<end>Here's some json data, can you convert it to MARKDOWN?
[
    {
        "Device Type": "Light Sensor",
        "Location": "Kitchen",
        "Battery Level (%)": 41.2
    },
    {
        "Device Type": "Pressure Sensor",
        "Location": "Garden",
        "Battery Level (%)": 54.4
    },
    {
        "Device Type": "Pressure Sensor",
        "Location": "Bedroom",
        "Battery Level (%)": 40.3
    },
    {
        "Device Type": "Temperature Sensor",
        "Location": "Garden",
        "Battery Level (%)": 66.5
    },
    {
        "Device Type": "Temperature Sensor",
        "Location": "Garden",
        "Battery Level (%)": 39.8
    }
]<start>
| Device Type | Location | Battery Level (%) |
| --- | --- | --- |
| Light Sensor | Kitchen | 41.2 |
| Pressure Sensor | Garden | 54.4 |
| Pressure Sensor | Bedroom | 40.3 |
| Temperature Sensor | Garden | 66.5 |
| Temperature Sensor | Garden | 39.8 |
<end>Please transform the following json data into PLAIN TEXT:
[
    {
        "Location": "Miami",
        "Condition": "Cloudy",
        "Temperature (C)": 20.7,
        "Humidity (%)": 100,
        "Wind Speed (km/h)": 18.2,
        "Day": "Saturday"
    },
    {
        "Location": "New York",
        "Condition": "Stormy",
        "Temperature (C)": 8.4,
        "Humidity (%)": 42,
        "Wind Speed (km/h)": 25.0,
        "Day": "Sunday"
    },
    {
        "Location": "Houston",
        "Condition": "Stormy",
        "Temperature (C)": -9.6,
        "Humidity (%)": 33,
        "Wind Speed (km/h)": 9.2,
        "Day": "Thursday"
    },
    {
        "Location": "Los Angeles",
        "Condition": "Sunny",
        "Temperature (C)": -9.6,
        "Humidity (%)": 20,
        "Wind Speed (km/h)": 25.0,
        "Day": "Friday"
    },
    {
        "Location": "Chicago",
        "Condition": "Stormy",
        "Temperature (C)": -3.8,
        "Humidity (%)": 98,
        "Wind Speed (km/h)": 4.6,
        "Day": "Wednesday"
    },
    {
        "Location": "Seattle",
        "Condition": "Snowy",
        "Temperature (C)": 25.6,
        "Humidity (%)": 43,
        "Wind Speed (km/h)": 16.5,
        "Day": "Friday"
    },
    {
        "Location": "Houston",
        "Condition": "Foggy",
        "Temperature (C)": 3.5,
        "Humidity (%)": 42,
        "Wind Speed (km/h)": 0.6,
        "Day": "Sunday"
    },
    {
        "Location": "Miami",
        "Condition": "Cloudy",
        "Temperature (C)": -1.6,
        "Humidity (%)": 77,
        "Wind Speed (km/h)": 1.3,
        "Day": "Tuesday"
    },
    {
        "Location": "Chicago",
        "Condition": "Foggy",
        "Temperature (C)": 17.1,
        "Humidity (%)": 54,
        "Wind Speed (km/h)": 0.4,
        "Day": "Friday"
    }
]<start>
Location: Miami | Condition: Cloudy | Temperature (C): 20.7 | Humidity (%): 100 | Wind Speed (km/h): 18.2 | Day: Saturday
Location: New York | Condition: Stormy | Temperature (C): 8.4 | Humidity (%): 42 | Wind Speed (km/h): 25.0 | Day: Sunday
Location: Houston | Condition: Stormy | Temperature (C): -9.6 | Humidity (%): 33 | Wind Speed (km/h): 9.2 | Day: Thursday
Location: Los Angeles | Condition: Sunny | Temperature (C): -9.6 | Humidity (%): 20 | Wind Speed (km/h): 25.0 | Day: Friday
Location: Chicago | Condition: Stormy | Temperature (C): -3.8 | Humidity (%): 98 | Wind Speed (km/h): 4.6 | Day: Wednesday
Location: Seattle | Condition: Snowy | Temperature (C): 25.6 | Humidity (%): 43 | Wind Speed (km/h): 16.5 | Day: Friday
Location: Houston | Condition: Foggy | Temperature (C): 3.5 | Humidity (%): 42 | Wind Speed (km/h): 0.6 | Day: Sunday
Location: Miami | Condition: Cloudy | Temperature (C): -1.6 | Humidity (%): 77 | Wind Speed (km/h): 1.3 | Day: Tuesday
Location: Chicago | Condition: Foggy | Temperature (C): 17.1 | Humidity (%): 54 | Wind Speed (km/h): 0.4 | Day: Friday
<end>Can you change this YAML into Plain text?
- Battery Level (%): 93.2
  Device ID: device-0035
  Device Type: Motion Detector
  Location: Hallway
  Reading Value: 80.43
  Timestamp: '2021-11-04 15:23:15'
- Battery Level (%): 60.7
  Device ID: device-0073
  Device Type: Motion Detector
  Location: Garage
  Reading Value: 75.1
  Timestamp: '2023-12-04 02:38:19'
- Battery Level (%): 14.3
  Device ID: device-0039
  Device Type: Motion Detector
  Location: Garden
  Reading Value: 67.92
  Timestamp: '2022-10-24 14:08:11'
- Battery Level (%): 36.5
  Device ID: device-0065
  Device Type: Motion Detector
  Location: Bedroom
  Reading Value: 74.35
  Timestamp: '2022-09-18 04:55:21'
- Battery Level (%): 45.0
  Device ID: device-0064
  Device Type: Temperature Sensor
  Location: Bedroom
  Reading Value: 40.72
  Timestamp: '2022-05-13 06:49:03'
- Battery Level (%): 14.3
  Device ID: device-0016
  Device Type: Light Sensor
  Location: Living Room
  Reading Value: 2.88
  Timestamp: '2021-05-24 15:16:12'
<start>
Device ID: device-0035 | Device Type: Motion Detector | Location: Hallway | Battery Level (%): 93.2 | Reading Value: 80.43 | Timestamp: 2021-11-04 15:23:15
Device ID: device-0073 | Device Type: Motion Detector | Location: Garage | Battery Level (%): 60.7 | Reading Value: 75.1 | Timestamp: 2023-12-04 02:38:19
Device ID: device-0039 | Device Type: Motion Detector | Location: Garden | Battery Level (%): 14.3 | Reading Value: 67.92 | Timestamp: 2022-10-24 14:08:11
Device ID: device-0065 | Device Type: Motion Detector | Location: Bedroom | Battery Level (%): 36.5 | Reading Value: 74.35 | Timestamp: 2022-09-18 04:55:21
Device ID: device-0064 | Device Type: Temperature Sensor | Location: Bedroom | Battery Level (%): 45.0 | Reading Value: 40.72 | Timestamp: 2022-05-13 06:49:03
Device ID: device-0016 | Device Type: Light Sensor | Location: Living Room | Battery Level (%): 14.3 | Reading Value: 2.88 | Timestamp: 2021-05-24 15:16:12
<end>Can you change this markdown into json?
| Title | Genre |
| --- | --- |
| The Endless Horizon | Horror |
| The Great Expedition | Sci-Fi |
| The Great Expedition | Adventure |
| Edge of Infinity | Action |
| Beyond the Veil | Sci-Fi |
| Mystery of the Depths | Drama |<start>
[
    {
        "Title": "The Endless Horizon",
        "Genre": "Horror"
    },
    {
        "Title": "The Great Expedition",
        "Genre": "Sci-Fi"
    },
    {
        "Title": "The Great Expedition",
        "Genre": "Adventure"
    },
    {
        "Title": "Edge of Infinity",
        "Genre": "Action"
    },
    {
        "Title": "Beyond the Veil",
        "Genre": "Sci-Fi"
    },
    {
        "Title": "Mystery of the Depths",
        "Genre": "Drama"
    }
]
<end>Transform this csv structure to a json format:
Genre,Rating
Historical,1.1
Thriller,3.5
Mystery,2.0
Romance,3.6
Mystery,2.7
Fantasy,2.4
Historical,4.1
Non-Fiction,4.5
<start>
[
    {
        "Genre": "Historical",
        "Rating": 1.1
    },
    {
        "Genre": "Thriller",
        "Rating": 3.5
    },
    {
        "Genre": "Mystery",
        "Rating": 2.0
    },
    {
        "Genre": "Romance",
        "Rating": 3.6
    },
    {
        "Genre": "Mystery",
        "Rating": 2.7
    },
    {
        "Genre": "Fantasy",
        "Rating": 2.4
    },
    {
        "Genre": "Historical",
        "Rating": 4.1
    },
    {
        "Genre": "Non-Fiction",
        "Rating": 4.5
    }
]
<end>Please transform the following Markdown data into json:
| Company | Sector | Market Cap | Stock Price | Annual Revenue (B) | Quarter |
| --- | --- | --- | --- | --- | --- |
| BioPharm | Energy | Small Cap | 777.9 | 120.3 | Q3 |
| AeroSpace | Biotech | Small Cap | 104.19 | 192.83 | Q2 |
| TechCorp | Energy | Small Cap | 948.63 | 187.22 | Q2 |
| RetailHub | Biotech | Mega Cap | 484.76 | 372.7 | Q1 |
| FinanceWorks | Technology | Small Cap | 210.95 | 136.55 | Q1 |
| EcoEnergy | Technology | Mega Cap | 543.09 | 415.73 | Q4 |<start>
[
    {
        "Company": "BioPharm",
        "Sector": "Energy",
        "Market Cap": "Small Cap",
        "Stock Price": 777.9,
        "Annual Revenue (B)": 120.3,
        "Quarter": "Q3"
    },
    {
        "Company": "AeroSpace",
        "Sector": "Biotech",
        "Market Cap": "Small Cap",
        "Stock Price": 104.19,
        "Annual Revenue (B)": 192.83,
        "Quarter": "Q2"
    },
    {
        "Company": "TechCorp",
        "Sector": "Energy",
        "Market Cap": "Small Cap",
        "Stock Price": 948.63,
        "Annual Revenue (B)": 187.22,
        "Quarter": "Q2"
    },
    {
        "Company": "RetailHub",
        "Sector": "Biotech",
        "Market Cap": "Mega Cap",
        "Stock Price": 484.76,
        "Annual Revenue (B)": 372.7,
        "Quarter": "Q1"
    },
    {
        "Company": "FinanceWorks",
        "Sector": "Technology",
        "Market Cap": "Small Cap",
        "Stock Price": 210.95,
        "Annual Revenue (B)": 136.55,
        "Quarter": "Q1"
    },
    {
        "Company": "EcoEnergy",
        "Sector": "Technology",
        "Market Cap": "Mega Cap",
        "Stock Price": 543.09,
        "Annual Revenue (B)": 415.73,
        "Quarter": "Q4"
    }
]
<end>Transform this CSV structure to a PLAIN TEXT format:
Title,Author,Genre,Publication Year,Rating
Echoes of Eternity,Isla Windrider,Historical,2022,2.8
Shadows of Solitude,Sylvia Nightshade,Science Fiction,1973,2.7
Whispers of the Abyss,Draven Blackthorn,Historical,1972,4.8
Shadows of Solitude,Luna Silverleaf,Science Fiction,1978,1.4
Echoes of Eternity,Draven Blackthorn,Non-Fiction,1988,4.4
Echoes of Eternity,Isla Windrider,Mystery,2016,1.8
The Crystal Key,Thorne Ironwood,Non-Fiction,1977,3.5
<start>
Title: Echoes of Eternity | Author: Isla Windrider | Genre: Historical | Publication Year: 2022 | Rating: 2.8
Title: Shadows of Solitude | Author: Sylvia Nightshade | Genre: Science Fiction | Publication Year: 1973 | Rating: 2.7
Title: Whispers of the Abyss | Author: Draven Blackthorn | Genre: Historical | Publication Year: 1972 | Rating: 4.8
Title: Shadows of Solitude | Author: Luna Silverleaf | Genre: Science Fiction | Publication Year: 1978 | Rating: 1.4
Title: Echoes of Eternity | Author: Draven Blackthorn | Genre: Non-Fiction | Publication Year: 1988 | Rating: 4.4
Title: Echoes of Eternity | Author: Isla Windrider | Genre: Mystery | Publication Year: 2016 | Rating: 1.8
Title: The Crystal Key | Author: Thorne Ironwood | Genre: Non-Fiction | Publication Year: 1977 | Rating: 3.5
<end>Here's some json data, can you convert it to plain text?
[
    {
        "SKU": "SKU-1018",
        "Stock Quantity": 377,
        "Category": "Automotive",
        "Supplier Name": "Globex"
    },
    {
        "SKU": "SKU-1038",
        "Stock Quantity": 114,
        "Category": "Sports",
        "Supplier Name": "Wayne Enterprises"
    },
    {
        "SKU": "SKU-1025",
        "Stock Quantity": 139,
        "Category": "Automotive",
        "Supplier Name": "Globex"
    }
]<start>
SKU: SKU-1018 | Stock Quantity: 377 | Category: Automotive | Supplier Name: Globex
SKU: SKU-1038 | Stock Quantity: 114 | Category: Sports | Supplier Name: Wayne Enterprises
SKU: SKU-1025 | Stock Quantity: 139 | Category: Automotive | Supplier Name: Globex
<end>Convert this Markdown to yml:
| Title | Director | Genre | Release Year | Box Office Earnings (M) |
| --- | --- | --- | --- | --- |
| Starbound Odyssey | Selene Darkwhisper | Comedy | 1976 | 594.33 |
| Rise of the Titans | Zara Stormrider | Drama | 1970 | 187.21 |
| The Final Voyage | Talon Blackthorn | Comedy | 1974 | 277.84 |
| Beyond the Veil | Selene Darkwhisper | Comedy | 1975 | 715.28 |<start>
- Box Office Earnings (M): 594.33
  Director: Selene Darkwhisper
  Genre: Comedy
  Release Year: 1976
  Title: Starbound Odyssey
- Box Office Earnings (M): 187.21
  Director: Zara Stormrider
  Genre: Drama
  Release Year: 1970
  Title: Rise of the Titans
- Box Office Earnings (M): 277.84
  Director: Talon Blackthorn
  Genre: Comedy
  Release Year: 1974
  Title: The Final Voyage
- Box Office Earnings (M): 715.28
  Director: Selene Darkwhisper
  Genre: Comedy
  Release Year: 1975
  Title: Beyond the Veil
<end>Convert this markdown to plain text:
| Device Type | Location | Reading Value | Timestamp |
| --- | --- | --- | --- |
| Pressure Sensor | Bedroom | 6.75 | 2023-02-08 20:21:19 |
| Temperature Sensor | Garage | 75.46 | 2022-03-21 02:21:38 |
| Humidity Sensor | Bathroom | 45.68 | 2022-02-19 14:52:43 |
| Pressure Sensor | Kitchen | 40.0 | 2021-04-02 02:22:37 |
| Pressure Sensor | Kitchen | 66.79 | 2023-11-21 21:56:00 |
| Light Sensor | Living Room | 60.09 | 2023-01-07 03:24:25 |
| Pressure Sensor | Garage | -1.23 | 2021-01-09 14:57:59 |
| Motion Detector | Garage | 20.49 | 2021-11-08 08:46:00 |
| Temperature Sensor | Kitchen | -9.01 | 2023-04-20 23:45:19 |
| Light Sensor | Bathroom | 6.75 | 2022-07-15 03:40:22 |<start>
Device Type: Pressure Sensor | Location: Bedroom | Reading Value: 6.75 | Timestamp: 2023-02-08 20:21:19
Device Type: Temperature Sensor | Location: Garage | Reading Value: 75.46 | Timestamp: 2022-03-21 02:21:38
Device Type: Humidity Sensor | Location: Bathroom | Reading Value: 45.68 | Timestamp: 2022-02-19 14:52:43
Device Type: Pressure Sensor | Location: Kitchen | Reading Value: 40.0 | Timestamp: 2021-04-02 02:22:37
Device Type: Pressure Sensor | Location: Kitchen | Reading Value: 66.79 | Timestamp: 2023-11-21 21:56:00
Device Type: Light Sensor | Location: Living Room | Reading Value: 60.09 | Timestamp: 2023-01-07 03:24:25
Device Type: Pressure Sensor | Location: Garage | Reading Value: -1.23 | Timestamp: 2021-01-09 14:57:59
Device Type: Motion Detector | Location: Garage | Reading Value: 20.49 | Timestamp: 2021-11-08 08:46:00
Device Type: Temperature Sensor | Location: Kitchen | Reading Value: -9.01 | Timestamp: 2023-04-20 23:45:19
Device Type: Light Sensor | Location: Bathroom | Reading Value: 6.75 | Timestamp: 2022-07-15 03:40:22
<end>Convert this PLAIN TEXT to csv:
Product Name: Device | SKU: SKU-1011 | Price: 10.54 | Stock Quantity: 280 | Category: Electronics
Product Name: Contraption | SKU: SKU-1043 | Price: 344.39 | Stock Quantity: 490 | Category: Electronics
Product Name: Gizmo | SKU: SKU-1018 | Price: 20.88 | Stock Quantity: 77 | Category: Electronics
Product Name: Thingamajig | SKU: SKU-1016 | Price: 422.52 | Stock Quantity: 60 | Category: Toys
Product Name: Widget | SKU: SKU-1078 | Price: 469.57 | Stock Quantity: 497 | Category: Electronics
<start>
Product Name,SKU,Price,Stock Quantity,Category
Device,SKU-1011,10.54,280,Electronics
Contraption,SKU-1043,344.39,490,Electronics
Gizmo,SKU-1018,20.88,77,Electronics
Thingamajig,SKU-1016,422.52,60,Toys
Widget,SKU-1078,469.57,497,Electronics
<end>Please transform the following YAML data into plain text:
- Cuisine: Italian
  Price Range: $$
  Rating: 4
  Restaurant Name: Pasta Palace
- Cuisine: Japanese
  Price Range: $$$$$
  Rating: 4
  Restaurant Name: Sushi World
- Cuisine: Japanese
  Price Range: $$
  Rating: 3
  Restaurant Name: Curry Corner
- Cuisine: Chinese
  Price Range: $$$$$
  Rating: 5
  Restaurant Name: Curry Corner
<start>
Restaurant Name: Pasta Palace | Cuisine: Italian | Rating: 4 | Price Range: $$
Restaurant Name: Sushi World | Cuisine: Japanese | Rating: 4 | Price Range: $$$$$
Restaurant Name: Curry Corner | Cuisine: Japanese | Rating: 3 | Price Range: $$
Restaurant Name: Curry Corner | Cuisine: Chinese | Rating: 5 | Price Range: $$$$$
<end>Can you change this MARKDOWN into json?
| Title | Author | Genre | Publication Year |
| --- | --- | --- | --- |
| Shadows of Solitude | Draven Blackthorn | Fantasy | 1989 |
| Whispers of the Abyss | Isla Windrider | Fantasy | 1973 |
| The Forgotten World | Galen Starfire | Fantasy | 2011 |
| Whispers of the Abyss | Kara Firebrand | Historical | 2014 |
| Echoes of Eternity | Orion Frostblade | Mystery | 1990 |
| Whispers of the Abyss | Draven Blackthorn | Science Fiction | 1976 |
| Legends of the Rift | Elara Moonshadow | Science Fiction | 2000 |
| The Last Sky | Rowan Ashborne | Fantasy | 2003 |
| Tales of the Brave | Draven Blackthorn | Historical | 1972 |
| Shadows of Solitude | Kara Firebrand | Romance | 1951 |<start>
[
    {
        "Title": "Shadows of Solitude",
        "Author": "Draven Blackthorn",
        "Genre": "Fantasy",
        "Publication Year": 1989
    },
    {
        "Title": "Whispers of the Abyss",
        "Author": "Isla Windrider",
        "Genre": "Fantasy",
        "Publication Year": 1973
    },
    {
        "Title": "The Forgotten World",
        "Author": "Galen Starfire",
        "Genre": "Fantasy",
        "Publication Year": 2011
    },
    {
        "Title": "Whispers of the Abyss",
        "Author": "Kara Firebrand",
        "Genre": "Historical",
        "Publication Year": 2014
    },
    {
        "Title": "Echoes of Eternity",
        "Author": "Orion Frostblade",
        "Genre": "Mystery",
        "Publication Year": 1990
    },
    {
        "Title": "Whispers of the Abyss",
        "Author": "Draven Blackthorn",
        "Genre": "Science Fiction",
        "Publication Year": 1976
    },
    {
        "Title": "Legends of the Rift",
        "Author": "Elara Moonshadow",
        "Genre": "Science Fiction",
        "Publication Year": 2000
    },
    {
        "Title": "The Last Sky",
        "Author": "Rowan Ashborne",
        "Genre": "Fantasy",
        "Publication Year": 2003
    },
    {
        "Title": "Tales of the Brave",
        "Author": "Draven Blackthorn",
        "Genre": "Historical",
        "Publication Year": 1972
    },
    {
        "Title": "Shadows of Solitude",
        "Author": "Kara Firebrand",
        "Genre": "Romance",
        "Publication Year": 1951
    }
]
<end>Convert this csv to Plain text:
Product Name,SKU,Price,Stock Quantity,Supplier Name
Apparatus,SKU-1051,455.7,415,Umbrella Corp
Contraption,SKU-1055,160.1,254,Wayne Enterprises
Widget,SKU-1044,263.46,152,Globex
Gadget,SKU-1042,413.79,191,ACME Corp
Gizmo,SKU-1051,280.14,255,Globex
Apparatus,SKU-1072,496.0,486,Globex
Instrument,SKU-1089,9.18,176,Umbrella Corp
Gizmo,SKU-1078,472.3,181,Wonka Industries
<start>
Product Name: Apparatus | SKU: SKU-1051 | Price: 455.7 | Stock Quantity: 415 | Supplier Name: Umbrella Corp
Product Name: Contraption | SKU: SKU-1055 | Price: 160.1 | Stock Quantity: 254 | Supplier Name: Wayne Enterprises
Product Name: Widget | SKU: SKU-1044 | Price: 263.46 | Stock Quantity: 152 | Supplier Name: Globex
Product Name: Gadget | SKU: SKU-1042 | Price: 413.79 | Stock Quantity: 191 | Supplier Name: ACME Corp
Product Name: Gizmo | SKU: SKU-1051 | Price: 280.14 | Stock Quantity: 255 | Supplier Name: Globex
Product Name: Apparatus | SKU: SKU-1072 | Price: 496.0 | Stock Quantity: 486 | Supplier Name: Globex
Product Name: Instrument | SKU: SKU-1089 | Price: 9.18 | Stock Quantity: 176 | Supplier Name: Umbrella Corp
Product Name: Gizmo | SKU: SKU-1078 | Price: 472.3 | Stock Quantity: 181 | Supplier Name: Wonka Industries
<end>Convert this plain text to Csv:
Start Location: Miami | End Location: San Francisco | Fuel Used (gallons): 33.6
Start Location: San Francisco | End Location: New York | Fuel Used (gallons): 52.6
Start Location: Phoenix | End Location: Denver | Fuel Used (gallons): 63.3
Start Location: Chicago | End Location: Houston | Fuel Used (gallons): 16.4
Start Location: San Francisco | End Location: Houston | Fuel Used (gallons): 60.9
<start>
Start Location,End Location,Fuel Used (gallons)
Miami,San Francisco,33.6
San Francisco,New York,52.6
Phoenix,Denver,63.3
Chicago,Houston,16.4
San Francisco,Houston,60.9
<end>Convert this markdown to JSON:
| Restaurant Name | Cuisine | Location |
| --- | --- | --- |
| Taco Town | Italian | Seattle |
| Vegan Delight | Indian | Miami |
| Pizza Planet | Mediterranean | Los Angeles |
| Pasta Palace | Italian | Phoenix |
| Curry Corner | Indian | Seattle |
| The Steakhouse | Mexican | Seattle |
| Curry Corner | Japanese | Los Angeles |
| The Golden Spoon | French | Miami |
| Taco Town | Italian | Houston |
| Taco Town | Italian | Miami |<start>
[
    {
        "Restaurant Name": "Taco Town",
        "Cuisine": "Italian",
        "Location": "Seattle"
    },
    {
        "Restaurant Name": "Vegan Delight",
        "Cuisine": "Indian",
        "Location": "Miami"
    },
    {
        "Restaurant Name": "Pizza Planet",
        "Cuisine": "Mediterranean",
        "Location": "Los Angeles"
    },
    {
        "Restaurant Name": "Pasta Palace",
        "Cuisine": "Italian",
        "Location": "Phoenix"
    },
    {
        "Restaurant Name": "Curry Corner",
        "Cuisine": "Indian",
        "Location": "Seattle"
    },
    {
        "Restaurant Name": "The Steakhouse",
        "Cuisine": "Mexican",
        "Location": "Seattle"
    },
    {
        "Restaurant Name": "Curry Corner",
        "Cuisine": "Japanese",
        "Location": "Los Angeles"
    },
    {
        "Restaurant Name": "The Golden Spoon",
        "Cuisine": "French",
        "Location": "Miami"
    },
    {
        "Restaurant Name": "Taco Town",
        "Cuisine": "Italian",
        "Location": "Houston"
    },
    {
        "Restaurant Name": "Taco Town",
        "Cuisine": "Italian",
        "Location": "Miami"
    }
]
<end>Transform this json structure to a PLAIN TEXT format:
[
    {
        "Company": "AutoDrive",
        "Market Cap": "Large Cap",
        "Stock Price": 131.63,
        "Annual Revenue (B)": 261.3,
        "Quarter": "Q4"
    },
    {
        "Company": "GlobalTrade",
        "Market Cap": "Mid Cap",
        "Stock Price": 872.38,
        "Annual Revenue (B)": 403.43,
        "Quarter": "Q1"
    },
    {
        "Company": "AutoDrive",
        "Market Cap": "Small Cap",
        "Stock Price": 732.71,
        "Annual Revenue (B)": 213.06,
        "Quarter": "Q4"
    },
    {
        "Company": "TechCorp",
        "Market Cap": "Small Cap",
        "Stock Price": 121.68,
        "Annual Revenue (B)": 128.98,
        "Quarter": "Q1"
    }
]<start>
Company: AutoDrive | Market Cap: Large Cap | Stock Price: 131.63 | Annual Revenue (B): 261.3 | Quarter: Q4
Company: GlobalTrade | Market Cap: Mid Cap | Stock Price: 872.38 | Annual Revenue (B): 403.43 | Quarter: Q1
Company: AutoDrive | Market Cap: Small Cap | Stock Price: 732.71 | Annual Revenue (B): 213.06 | Quarter: Q4
Company: TechCorp | Market Cap: Small Cap | Stock Price: 121.68 | Annual Revenue (B): 128.98 | Quarter: Q1
<end>Can you change this MARKDOWN into CSV?
| Publication Year | Rating |
| --- | --- |
| 1993 | 4.6 |
| 1971 | 2.9 |
| 2008 | 3.0 |
| 1962 | 2.7 |
| 1956 | 1.2 |
| 1980 | 1.8 |
| 2022 | 4.1 |
| 2017 | 4.3 |
| 1981 | 3.7 |<start>
Publication Year,Rating
1993,4.6
1971,2.9
2008,3.0
1962,2.7
1956,1.2
1980,1.8
2022,4.1
2017,4.3
1981,3.7
<end>Can you change this Yml into csv?
- Age: 38
  City: Denver
- Age: 31
  City: Charlotte
- Age: 32
  City: Charlotte
- Age: 28
  City: Denver
- Age: 58
  City: New York
<start>
Age,City
38,Denver
31,Charlotte
32,Charlotte
28,Denver
58,New York
<end>Please transform the following YAML data into PLAIN TEXT:
- Close Price: 588.51
  Company: FoodChain
  High Price: 588.51
  Low Price: 259.45
  Open Price: 259.45
  Volume: 7869327
- Close Price: 784.55
  Company: HealthGen
  High Price: 1066.62
  Low Price: 100.78
  Open Price: 384.37
  Volume: 6452671
- Close Price: 1444.11
  Company: GreenEnergy
  High Price: 1444.11
  Low Price: 19.65
  Open Price: 19.65
  Volume: 2205345
- Close Price: 389.76
  Company: FinanceTrust
  High Price: 1357.17
  Low Price: 389.76
  Open Price: 656.1
  Volume: 8913253
- Close Price: 984.18
  Company: AeroSystems
  High Price: 1034.63
  Low Price: 221.91
  Open Price: 1034.63
  Volume: 3863573
- Close Price: 221.91
  Company: MediaGroup
  High Price: 322.78
  Low Price: 221.91
  Open Price: 322.78
  Volume: 2677087
- Close Price: 378.35
  Company: MediaGroup
  High Price: 542.67
  Low Price: 378.35
  Open Price: 461.4
  Volume: 6137537
- Close Price: 1098.73
  Company: AutoMotive
  High Price: 1098.73
  Low Price: 487.48
  Open Price: 1007.13
  Volume: 7869327
<start>
Company: FoodChain | Open Price: 259.45 | Close Price: 588.51 | High Price: 588.51 | Low Price: 259.45 | Volume: 7869327
Company: HealthGen | Open Price: 384.37 | Close Price: 784.55 | High Price: 1066.62 | Low Price: 100.78 | Volume: 6452671
Company: GreenEnergy | Open Price: 19.65 | Close Price: 1444.11 | High Price: 1444.11 | Low Price: 19.65 | Volume: 2205345
Company: FinanceTrust | Open Price: 656.1 | Close Price: 389.76 | High Price: 1357.17 | Low Price: 389.76 | Volume: 8913253
Company: AeroSystems | Open Price: 1034.63 | Close Price: 984.18 | High Price: 1034.63 | Low Price: 221.91 | Volume: 3863573
Company: MediaGroup | Open Price: 322.78 | Close Price: 221.91 | High Price: 322.78 | Low Price: 221.91 | Volume: 2677087
Company: MediaGroup | Open Price: 461.4 | Close Price: 378.35 | High Price: 542.67 | Low Price: 378.35 | Volume: 6137537
Company: AutoMotive | Open Price: 1007.13 | Close Price: 1098.73 | High Price: 1098.73 | Low Price: 487.48 | Volume: 7869327
<end>Can you change this json into PLAIN TEXT?
[
    {
        "Date": "2018-04-16",
        "Open Price": 967.69,
        "Low Price": 45.96,
        "Volume": 9688626
    },
    {
        "Date": "2010-05-03",
        "Open Price": 1356.47,
        "Low Price": 1201.34,
        "Volume": 253926
    },
    {
        "Date": "2012-07-06",
        "Open Price": 1467.06,
        "Low Price": 211.45,
        "Volume": 1455993
    }
]<start>
Date: 2018-04-16 | Open Price: 967.69 | Low Price: 45.96 | Volume: 9688626
Date: 2010-05-03 | Open Price: 1356.47 | Low Price: 1201.34 | Volume: 253926
Date: 2012-07-06 | Open Price: 1467.06 | Low Price: 211.45 | Volume: 1455993
<end>Convert this Yaml to plain text:
- Box Office Earnings (M): 596.22
  Director: Mara Moonshadow
  Genre: Sci-Fi
  Release Year: 1985
  Title: The Final Voyage
- Box Office Earnings (M): 991.08
  Director: Talon Blackthorn
  Genre: Drama
  Release Year: 2018
  Title: The Great Expedition
- Box Office Earnings (M): 574.58
  Director: Rylan Frostblade
  Genre: Action
  Release Year: 2008
  Title: Dreamwalker
- Box Office Earnings (M): 454.91
  Director: Mara Moonshadow
  Genre: Drama
  Release Year: 1973
  Title: Beyond the Veil
- Box Office Earnings (M): 671.68
  Director: Zara Stormrider
  Genre: Adventure
  Release Year: 2022
  Title: Rise of the Titans
- Box Office Earnings (M): 818.04
  Director: Talon Blackthorn
  Genre: Drama
  Release Year: 1996
  Title: Starbound Odyssey
- Box Office Earnings (M): 455.83
  Director: Rylan Frostblade
  Genre: Thriller
  Release Year: 1976
  Title: Dreamwalker
- Box Office Earnings (M): 580.79
  Director: Talon Blackthorn
  Genre: Fantasy
  Release Year: 2021
  Title: The Final Voyage
- Box Office Earnings (M): 580.6
  Director: Talon Blackthorn
  Genre: Fantasy
  Release Year: 1996
  Title: Escape from Earth
- Box Office Earnings (M): 133.6
  Director: Mara Moonshadow
  Genre: Fantasy
  Release Year: 2009
  Title: Starbound Odyssey
<start>
Title: The Final Voyage | Director: Mara Moonshadow | Genre: Sci-Fi | Release Year: 1985 | Box Office Earnings (M): 596.22
Title: The Great Expedition | Director: Talon Blackthorn | Genre: Drama | Release Year: 2018 | Box Office Earnings (M): 991.08
Title: Dreamwalker | Director: Rylan Frostblade | Genre: Action | Release Year: 2008 | Box Office Earnings (M): 574.58
Title: Beyond the Veil | Director: Mara Moonshadow | Genre: Drama | Release Year: 1973 | Box Office Earnings (M): 454.91
Title: Rise of the Titans | Director: Zara Stormrider | Genre: Adventure | Release Year: 2022 | Box Office Earnings (M): 671.68
Title: Starbound Odyssey | Director: Talon Blackthorn | Genre: Drama | Release Year: 1996 | Box Office Earnings (M): 818.04
Title: Dreamwalker | Director: Rylan Frostblade | Genre: Thriller | Release Year: 1976 | Box Office Earnings (M): 455.83
Title: The Final Voyage | Director: Talon Blackthorn | Genre: Fantasy | Release Year: 2021 | Box Office Earnings (M): 580.79
Title: Escape from Earth | Director: Talon Blackthorn | Genre: Fantasy | Release Year: 1996 | Box Office Earnings (M): 580.6
Title: Starbound Odyssey | Director: Mara Moonshadow | Genre: Fantasy | Release Year: 2009 | Box Office Earnings (M): 133.6
<end>Convert this json to Csv:
[
    {
        "Restaurant Name": "Curry Corner",
        "Cuisine": "Italian",
        "Location": "Miami",
        "Rating": 1
    },
    {
        "Restaurant Name": "Pizza Planet",
        "Cuisine": "Chinese",
        "Location": "Miami",
        "Rating": 3
    },
    {
        "Restaurant Name": "Vegan Delight",
        "Cuisine": "Japanese",
        "Location": "Miami",
        "Rating": 2
    },
    {
        "Restaurant Name": "Pizza Planet",
        "Cuisine": "American",
        "Location": "Phoenix",
        "Rating": 4
    },
    {
        "Restaurant Name": "Pizza Planet",
        "Cuisine": "French",
        "Location": "San Francisco",
        "Rating": 5
    },
    {
        "Restaurant Name": "The Golden Spoon",
        "Cuisine": "Italian",
        "Location": "New York",
        "Rating": 5
    }
]<start>
Restaurant Name,Cuisine,Location,Rating
Curry Corner,Italian,Miami,1
Pizza Planet,Chinese,Miami,3
Vegan Delight,Japanese,Miami,2
Pizza Planet,American,Phoenix,4
Pizza Planet,French,San Francisco,5
The Golden Spoon,Italian,New York,5
<end>Here's some Json data, can you convert it to Yml?
[
    {
        "Name": "Louisa",
        "Age": 37,
        "Birth Month": "May",
        "City": "Washington"
    },
    {
        "Name": "Mae",
        "Age": 18,
        "Birth Month": "July",
        "City": "Milwaukee"
    },
    {
        "Name": "Harriet",
        "Age": 45,
        "Birth Month": "July",
        "City": "Austin"
    },
    {
        "Name": "Dick",
        "Age": 43,
        "Birth Month": "August",
        "City": "Charlotte"
    },
    {
        "Name": "James",
        "Age": 39,
        "Birth Month": "January",
        "City": "Seattle"
    },
    {
        "Name": "Gene",
        "Age": 53,
        "Birth Month": "June",
        "City": "San Francisco"
    },
    {
        "Name": "Jack",
        "Age": 33,
        "Birth Month": "November",
        "City": "Memphis"
    },
    {
        "Name": "Paige",
        "Age": 28,
        "Birth Month": "July",
        "City": "Los Angeles"
    }
]<start>
- Age: 37
  Birth Month: May
  City: Washington
  Name: Louisa
- Age: 18
  Birth Month: July
  City: Milwaukee
  Name: Mae
- Age: 45
  Birth Month: July
  City: Austin
  Name: Harriet
- Age: 43
  Birth Month: August
  City: Charlotte
  Name: Dick
- Age: 39
  Birth Month: January
  City: Seattle
  Name: James
- Age: 53
  Birth Month: June
  City: San Francisco
  Name: Gene
- Age: 33
  Birth Month: November
  City: Memphis
  Name: Jack
- Age: 28
  Birth Month: July
  City: Los Angeles
  Name: Paige
<end>Please transform the following markdown data into Json:
| Start Location | Distance (miles) | Duration (hours) |
| --- | --- | --- |
| Los Angeles | 1234.9 | 29.8 |
| Houston | 2213.3 | 67.9 |
| Los Angeles | 259.6 | 37.9 |
| Los Angeles | 1933.0 | 4.3 |<start>
[
    {
        "Start Location": "Los Angeles",
        "Distance (miles)": 1234.9,
        "Duration (hours)": 29.8
    },
    {
        "Start Location": "Houston",
        "Distance (miles)": 2213.3,
        "Duration (hours)": 67.9
    },
    {
        "Start Location": "Los Angeles",
        "Distance (miles)": 259.6,
        "Duration (hours)": 37.9
    },
    {
        "Start Location": "Los Angeles",
        "Distance (miles)": 1933.0,
        "Duration (hours)": 4.3
    }
]
<end>Convert this json to plain text:
[
    {
        "Release Year": 2020,
        "Box Office Earnings (M)": 568.8
    },
    {
        "Release Year": 1980,
        "Box Office Earnings (M)": 99.64
    },
    {
        "Release Year": 2008,
        "Box Office Earnings (M)": 566.67
    }
]<start>
Release Year: 2020 | Box Office Earnings (M): 568.8
Release Year: 1980 | Box Office Earnings (M): 99.64
Release Year: 2008 | Box Office Earnings (M): 566.67
<end>Transform this CSV structure to a Yaml format:
Date,Open Price,Close Price,High Price,Volume
2017-03-12,1455.32,466.72,1455.32,7319722
2011-02-02,1164.78,1430.66,1430.66,1592059
2022-10-19,500.55,12.91,1152.36,3731468
2012-10-21,1433.56,846.26,1433.56,473543
2014-09-03,1017.31,402.92,1017.31,6072428
2011-08-26,706.21,377.0,706.21,3731468
<start>
- Close Price: 466.72
  Date: '2017-03-12'
  High Price: 1455.32
  Open Price: 1455.32
  Volume: 7319722
- Close Price: 1430.66
  Date: '2011-02-02'
  High Price: 1430.66
  Open Price: 1164.78
  Volume: 1592059
- Close Price: 12.91
  Date: '2022-10-19'
  High Price: 1152.36
  Open Price: 500.55
  Volume: 3731468
- Close Price: 846.26
  Date: '2012-10-21'
  High Price: 1433.56
  Open Price: 1433.56
  Volume: 473543
- Close Price: 402.92
  Date: '2014-09-03'
  High Price: 1017.31
  Open Price: 1017.31
  Volume: 6072428
- Close Price: 377.0
  Date: '2011-08-26'
  High Price: 706.21
  Open Price: 706.21
  Volume: 3731468
<end>Convert this yml to CSV:
- Distance (miles): 1611.2
  End Location: Denver
  Start Location: New York
- Distance (miles): 1801.2
  End Location: Phoenix
  Start Location: New York
- Distance (miles): 1291.6
  End Location: Los Angeles
  Start Location: Denver
- Distance (miles): 2198.8
  End Location: Los Angeles
  Start Location: Miami
- Distance (miles): 947.4
  End Location: Denver
  Start Location: Houston
- Distance (miles): 859.5
  End Location: Phoenix
  Start Location: San Francisco
<start>
Start Location,End Location,Distance (miles)
New York,Denver,1611.2
New York,Phoenix,1801.2
Denver,Los Angeles,1291.6
Miami,Los Angeles,2198.8
Houston,Denver,947.4
San Francisco,Phoenix,859.5
<end>Please transform the following markdown data into CSV:
| Cuisine | Location | Rating | Price Range |
| --- | --- | --- | --- |
| Mediterranean | Miami | 3 | $$ |
| Mexican | Chicago | 4 | $$ |
| Japanese | Phoenix | 4 | $ |
| Chinese | Los Angeles | 2 | $ |
| American | Los Angeles | 4 | $$$$$ |
| Mediterranean | Chicago | 3 | $$$$ |
| Mexican | Houston | 5 | $$$$$ |
| Mexican | New York | 4 | $$$ |
| French | New York | 3 | $$$ |<start>
Cuisine,Location,Rating,Price Range
Mediterranean,Miami,3,$$
Mexican,Chicago,4,$$
Japanese,Phoenix,4,$
Chinese,Los Angeles,2,$
American,Los Angeles,4,$$$$$
Mediterranean,Chicago,3,$$$$
Mexican,Houston,5,$$$$$
Mexican,New York,4,$$$
French,New York,3,$$$
<end>Transform this PLAIN TEXT structure to a MARKDOWN format:
Birth Month: December | Income: 65000
Birth Month: February | Income: 370000
Birth Month: March | Income: 465000
<start>
| Birth Month | Income |
| --- | --- |
| December | 65000 |
| February | 370000 |
| March | 465000 |
<end>Transform this csv structure to a markdown format:
Cuisine,Rating,Price Range
Mexican,5,$
Japanese,5,$
Japanese,3,$$$$$
<start>
| Cuisine | Rating | Price Range |
| --- | --- | --- |
| Mexican | 5 | $ |
| Japanese | 5 | $ |
| Japanese | 3 | $$$$$ |
<end>Here's some markdown data, can you convert it to yaml?
| Product Name | SKU | Price | Stock Quantity | Category | Supplier Name |
| --- | --- | --- | --- | --- | --- |
| Apparatus | SKU-1003 | 66.11 | 168 | Electronics | ACME Corp |
| Contraption | SKU-1089 | 464.17 | 88 | Sports | Globex |
| Contraption | SKU-1084 | 118.38 | 321 | Toys | Globex |
| Gadget | SKU-1002 | 349.91 | 410 | Automotive | Globex |
| Instrument | SKU-1097 | 341.34 | 19 | Automotive | Umbrella Corp |
| Doohickey | SKU-1039 | 468.63 | 175 | Household | Globex |
| Doohickey | SKU-1097 | 121.57 | 250 | Sports | Wonka Industries |
| Gizmo | SKU-1071 | 242.51 | 310 | Household | Globex |
| Widget | SKU-1005 | 462.42 | 388 | Electronics | Umbrella Corp |<start>
- Category: Electronics
  Price: 66.11
  Product Name: Apparatus
  SKU: SKU-1003
  Stock Quantity: 168
  Supplier Name: ACME Corp
- Category: Sports
  Price: 464.17
  Product Name: Contraption
  SKU: SKU-1089
  Stock Quantity: 88
  Supplier Name: Globex
- Category: Toys
  Price: 118.38
  Product Name: Contraption
  SKU: SKU-1084
  Stock Quantity: 321
  Supplier Name: Globex
- Category: Automotive
  Price: 349.91
  Product Name: Gadget
  SKU: SKU-1002
  Stock Quantity: 410
  Supplier Name: Globex
- Category: Automotive
  Price: 341.34
  Product Name: Instrument
  SKU: SKU-1097
  Stock Quantity: 19
  Supplier Name: Umbrella Corp
- Category: Household
  Price: 468.63
  Product Name: Doohickey
  SKU: SKU-1039
  Stock Quantity: 175
  Supplier Name: Globex
- Category: Sports
  Price: 121.57
  Product Name: Doohickey
  SKU: SKU-1097
  Stock Quantity: 250
  Supplier Name: Wonka Industries
- Category: Household
  Price: 242.51
  Product Name: Gizmo
  SKU: SKU-1071
  Stock Quantity: 310
  Supplier Name: Globex
- Category: Electronics
  Price: 462.42
  Product Name: Widget
  SKU: SKU-1005
  Stock Quantity: 388
  Supplier Name: Umbrella Corp
<end>Transform this YAML structure to a Markdown format:
- Close Price: 428.55
  Company: AutoMotive
  Date: '2022-10-09'
  High Price: 1432.15
  Low Price: 182.46
  Open Price: 1432.15
  Volume: 5707592
- Close Price: 205.34
  Company: FoodChain
  Date: '2012-07-18'
  High Price: 1066.06
  Low Price: 205.34
  Open Price: 1066.06
  Volume: 3434917
- Close Price: 1070.13
  Company: HealthGen
  Date: '2022-04-19'
  High Price: 1490.18
  Low Price: 1070.13
  Open Price: 1205.4
  Volume: 6636963
- Close Price: 482.62
  Company: FoodChain
  Date: '2019-11-02'
  High Price: 1315.87
  Low Price: 434.08
  Open Price: 1315.87
  Volume: 8794421
- Close Price: 669.37
  Company: FinanceTrust
  Date: '2017-08-11'
  High Price: 669.37
  Low Price: 205.34
  Open Price: 337.22
  Volume: 8899214
- Close Price: 1323.47
  Company: RetailWorld
  Date: '2011-05-22'
  High Price: 1323.47
  Low Price: 721.86
  Open Price: 721.86
  Volume: 2526026
- Close Price: 1459.64
  Company: TechnoCorp
  Date: '2013-09-15'
  High Price: 1459.64
  Low Price: 378.08
  Open Price: 378.08
  Volume: 6873124
- Close Price: 389.59
  Company: MediaGroup
  Date: '2019-11-08'
  High Price: 608.77
  Low Price: 279.89
  Open Price: 279.89
  Volume: 3548242
- Close Price: 586.89
  Company: AeroSystems
  Date: '2019-11-15'
  High Price: 586.89
  Low Price: 274.84
  Open Price: 274.84
  Volume: 3316737
- Close Price: 1072.66
  Company: FoodChain
  Date: '2015-10-06'
  High Price: 1268.4
  Low Price: 571.27
  Open Price: 571.27
  Volume: 3278798
<start>
| Company | Date | Open Price | Close Price | High Price | Low Price | Volume |
| --- | --- | --- | --- | --- | --- | --- |
| AutoMotive | 2022-10-09 | 1432.15 | 428.55 | 1432.15 | 182.46 | 5707592 |
| FoodChain | 2012-07-18 | 1066.06 | 205.34 | 1066.06 | 205.34 | 3434917 |
| HealthGen | 2022-04-19 | 1205.4 | 1070.13 | 1490.18 | 1070.13 | 6636963 |
| FoodChain | 2019-11-02 | 1315.87 | 482.62 | 1315.87 | 434.08 | 8794421 |
| FinanceTrust | 2017-08-11 | 337.22 | 669.37 | 669.37 | 205.34 | 8899214 |
| RetailWorld | 2011-05-22 | 721.86 | 1323.47 | 1323.47 | 721.86 | 2526026 |
| TechnoCorp | 2013-09-15 | 378.08 | 1459.64 | 1459.64 | 378.08 | 6873124 |
| MediaGroup | 2019-11-08 | 279.89 | 389.59 | 608.77 | 279.89 | 3548242 |
| AeroSystems | 2019-11-15 | 274.84 | 586.89 | 586.89 | 274.84 | 3316737 |
| FoodChain | 2015-10-06 | 571.27 | 1072.66 | 1268.4 | 571.27 | 3278798 |
<end>Convert this Markdown to JSON:
| Company | Market Cap | Stock Price | Annual Revenue (B) | Quarter |
| --- | --- | --- | --- | --- |
| Foodies | Mega Cap | 818.13 | 323.66 | Q1 |
| HealthPlus | Mid Cap | 837.03 | 345.92 | Q3 |
| EcoEnergy | Large Cap | 407.0 | 479.55 | Q3 |
| RetailHub | Small Cap | 464.02 | 246.57 | Q2 |
| HealthPlus | Small Cap | 647.87 | 174.74 | Q1 |<start>
[
    {
        "Company": "Foodies",
        "Market Cap": "Mega Cap",
        "Stock Price": 818.13,
        "Annual Revenue (B)": 323.66,
        "Quarter": "Q1"
    },
    {
        "Company": "HealthPlus",
        "Market Cap": "Mid Cap",
        "Stock Price": 837.03,
        "Annual Revenue (B)": 345.92,
        "Quarter": "Q3"
    },
    {
        "Company": "EcoEnergy",
        "Market Cap": "Large Cap",
        "Stock Price": 407.0,
        "Annual Revenue (B)": 479.55,
        "Quarter": "Q3"
    },
    {
        "Company": "RetailHub",
        "Market Cap": "Small Cap",
        "Stock Price": 464.02,
        "Annual Revenue (B)": 246.57,
        "Quarter": "Q2"
    },
    {
        "Company": "HealthPlus",
        "Market Cap": "Small Cap",
        "Stock Price": 647.87,
        "Annual Revenue (B)": 174.74,
        "Quarter": "Q1"
    }
]
<end>Convert this json to plain text:
[
    {
        "Restaurant Name": "Pasta Palace",
        "Cuisine": "Italian",
        "Location": "Houston",
        "Price Range": "$$$$"
    },
    {
        "Restaurant Name": "Pasta Palace",
        "Cuisine": "Mexican",
        "Location": "Phoenix",
        "Price Range": "$$"
    },
    {
        "Restaurant Name": "Curry Corner",
        "Cuisine": "Japanese",
        "Location": "Los Angeles",
        "Price Range": "$$$"
    },
    {
        "Restaurant Name": "The Golden Spoon",
        "Cuisine": "Indian",
        "Location": "San Francisco",
        "Price Range": "$$$$$"
    }
]<start>
Restaurant Name: Pasta Palace | Cuisine: Italian | Location: Houston | Price Range: $$$$
Restaurant Name: Pasta Palace | Cuisine: Mexican | Location: Phoenix | Price Range: $$
Restaurant Name: Curry Corner | Cuisine: Japanese | Location: Los Angeles | Price Range: $$$
Restaurant Name: The Golden Spoon | Cuisine: Indian | Location: San Francisco | Price Range: $$$$$
<end>Here's some plain text data, can you convert it to YML?
Company: FoodChain | Date: 2016-07-03 | Open Price: 1456.69 | Close Price: 674.64 | Volume: 7606806
Company: BioLife | Date: 2021-10-16 | Open Price: 1426.03 | Close Price: 1064.41 | Volume: 4651993
Company: RetailWorld | Date: 2022-11-03 | Open Price: 1064.41 | Close Price: 848.91 | Volume: 1661448
Company: AutoMotive | Date: 2019-12-27 | Open Price: 27.99 | Close Price: 1245.71 | Volume: 4440662
Company: RetailWorld | Date: 2023-11-03 | Open Price: 288.85 | Close Price: 547.33 | Volume: 9009723
<start>
- Close Price: 674.64
  Company: FoodChain
  Date: '2016-07-03'
  Open Price: 1456.69
  Volume: 7606806
- Close Price: 1064.41
  Company: BioLife
  Date: '2021-10-16'
  Open Price: 1426.03
  Volume: 4651993
- Close Price: 848.91
  Company: RetailWorld
  Date: '2022-11-03'
  Open Price: 1064.41
  Volume: 1661448
- Close Price: 1245.71
  Company: AutoMotive
  Date: '2019-12-27'
  Open Price: 27.99
  Volume: 4440662
- Close Price: 547.33
  Company: RetailWorld
  Date: '2023-11-03'
  Open Price: 288.85
  Volume: 9009723
<end>Convert this markdown to plain text:
| Temperature (C) | Humidity (%) | Wind Speed (km/h) |
| --- | --- | --- |
| 7.3 | 86 | 23.4 |
| 37.9 | 52 | 18.7 |
| 36.7 | 99 | 24.1 |
| 38.9 | 50 | 26.6 |<start>
Temperature (C): 7.3 | Humidity (%): 86 | Wind Speed (km/h): 23.4
Temperature (C): 37.9 | Humidity (%): 52 | Wind Speed (km/h): 18.7
Temperature (C): 36.7 | Humidity (%): 99 | Wind Speed (km/h): 24.1
Temperature (C): 38.9 | Humidity (%): 50 | Wind Speed (km/h): 26.6
<end>Can you change this csv into plain text?
Restaurant Name,Location,Price Range
Pasta Palace,Los Angeles,$$$$$
Burger Haven,Houston,$
Burger Haven,New York,$$
The Golden Spoon,Seattle,$
The Steakhouse,Miami,$
Taco Town,New York,$$$$
Pasta Palace,Seattle,$$$$$
BBQ Barn,New York,$$$
Pizza Planet,Miami,$$$
The Golden Spoon,Houston,$$$
<start>
Restaurant Name: Pasta Palace | Location: Los Angeles | Price Range: $$$$$
Restaurant Name: Burger Haven | Location: Houston | Price Range: $
Restaurant Name: Burger Haven | Location: New York | Price Range: $$
Restaurant Name: The Golden Spoon | Location: Seattle | Price Range: $
Restaurant Name: The Steakhouse | Location: Miami | Price Range: $
Restaurant Name: Taco Town | Location: New York | Price Range: $$$$
Restaurant Name: Pasta Palace | Location: Seattle | Price Range: $$$$$
Restaurant Name: BBQ Barn | Location: New York | Price Range: $$$
Restaurant Name: Pizza Planet | Location: Miami | Price Range: $$$
Restaurant Name: The Golden Spoon | Location: Houston | Price Range: $$$
<end>Please transform the following json data into csv:
[
    {
        "Title": "Legends of the Rift",
        "Author": "Thorne Ironwood"
    },
    {
        "Title": "The Forgotten World",
        "Author": "Rowan Ashborne"
    },
    {
        "Title": "Legends of the Rift",
        "Author": "Draven Blackthorn"
    },
    {
        "Title": "A Journey Through Time",
        "Author": "Orion Frostblade"
    },
    {
        "Title": "Legends of the Rift",
        "Author": "Luna Silverleaf"
    }
]<start>
Title,Author
Legends of the Rift,Thorne Ironwood
The Forgotten World,Rowan Ashborne
Legends of the Rift,Draven Blackthorn
A Journey Through Time,Orion Frostblade
Legends of the Rift,Luna Silverleaf
<end>Please transform the following markdown data into plain text:
| Company | Sector | Market Cap | Stock Price | Quarter |
| --- | --- | --- | --- | --- |
| AeroSpace | Aerospace | Mid Cap | 972.87 | Q1 |
| BioPharm | Healthcare | Large Cap | 137.86 | Q1 |
| AeroSpace | Automotive | Small Cap | 137.86 | Q2 |
| AeroSpace | Energy | Mega Cap | 953.22 | Q4 |
| HealthPlus | Automotive | Mega Cap | 163.91 | Q4 |
| AutoDrive | Biotech | Mega Cap | 945.95 | Q3 |<start>
Company: AeroSpace | Sector: Aerospace | Market Cap: Mid Cap | Stock Price: 972.87 | Quarter: Q1
Company: BioPharm | Sector: Healthcare | Market Cap: Large Cap | Stock Price: 137.86 | Quarter: Q1
Company: AeroSpace | Sector: Automotive | Market Cap: Small Cap | Stock Price: 137.86 | Quarter: Q2
Company: AeroSpace | Sector: Energy | Market Cap: Mega Cap | Stock Price: 953.22 | Quarter: Q4
Company: HealthPlus | Sector: Automotive | Market Cap: Mega Cap | Stock Price: 163.91 | Quarter: Q4
Company: AutoDrive | Sector: Biotech | Market Cap: Mega Cap | Stock Price: 945.95 | Quarter: Q3
<end>Please transform the following markdown data into json:
| Start Location | Distance (miles) | Duration (hours) | Fuel Used (gallons) |
| --- | --- | --- | --- |
| Chicago | 367.4 | 14.4 | 6.2 |
| Chicago | 1389.1 | 62.5 | 55.5 |
| Los Angeles | 859.2 | 35.0 | 49.6 |
| San Francisco | 2898.5 | 57.3 | 66.9 |
| Miami | 2905.0 | 58.1 | 67.6 |<start>
[
    {
        "Start Location": "Chicago",
        "Distance (miles)": 367.4,
        "Duration (hours)": 14.4,
        "Fuel Used (gallons)": 6.2
    },
    {
        "Start Location": "Chicago",
        "Distance (miles)": 1389.1,
        "Duration (hours)": 62.5,
        "Fuel Used (gallons)": 55.5
    },
    {
        "Start Location": "Los Angeles",
        "Distance (miles)": 859.2,
        "Duration (hours)": 35.0,
        "Fuel Used (gallons)": 49.6
    },
    {
        "Start Location": "San Francisco",
        "Distance (miles)": 2898.5,
        "Duration (hours)": 57.3,
        "Fuel Used (gallons)": 66.9
    },
    {
        "Start Location": "Miami",
        "Distance (miles)": 2905.0,
        "Duration (hours)": 58.1,
        "Fuel Used (gallons)": 67.6
    }
]
<end>Transform this Json structure to a yml format:
[
    {
        "Date": "2018-01-20",
        "Open Price": 996.43,
        "High Price": 1285.09,
        "Low Price": 84.83
    },
    {
        "Date": "2012-01-23",
        "Open Price": 873.48,
        "High Price": 934.01,
        "Low Price": 247.58
    },
    {
        "Date": "2021-02-19",
        "Open Price": 1253.63,
        "High Price": 1350.08,
        "Low Price": 1003.55
    },
    {
        "Date": "2020-02-08",
        "Open Price": 23.26,
        "High Price": 850.03,
        "Low Price": 23.26
    },
    {
        "Date": "2011-04-05",
        "Open Price": 1420.08,
        "High Price": 1420.08,
        "Low Price": 98.36
    },
    {
        "Date": "2013-08-08",
        "Open Price": 1332.51,
        "High Price": 1332.51,
        "Low Price": 23.26
    },
    {
        "Date": "2014-01-03",
        "Open Price": 392.85,
        "High Price": 1263.12,
        "Low Price": 392.85
    }
]<start>
- Date: '2018-01-20'
  High Price: 1285.09
  Low Price: 84.83
  Open Price: 996.43
- Date: '2012-01-23'
  High Price: 934.01
  Low Price: 247.58
  Open Price: 873.48
- Date: '2021-02-19'
  High Price: 1350.08
  Low Price: 1003.55
  Open Price: 1253.63
- Date: '2020-02-08'
  High Price: 850.03
  Low Price: 23.26
  Open Price: 23.26
- Date: '2011-04-05'
  High Price: 1420.08
  Low Price: 98.36
  Open Price: 1420.08
- Date: '2013-08-08'
  High Price: 1332.51
  Low Price: 23.26
  Open Price: 1332.51
- Date: '2014-01-03'
  High Price: 1263.12
  Low Price: 392.85
  Open Price: 392.85
<end>Can you change this json into markdown?
[
    {
        "Location": "Phoenix",
        "Condition": "Stormy",
        "Temperature (C)": 20.5,
        "Humidity (%)": 90,
        "Day": "Saturday"
    },
    {
        "Location": "Chicago",
        "Condition": "Windy",
        "Temperature (C)": 37.0,
        "Humidity (%)": 96,
        "Day": "Saturday"
    },
    {
        "Location": "Miami",
        "Condition": "Windy",
        "Temperature (C)": 28.1,
        "Humidity (%)": 70,
        "Day": "Monday"
    },
    {
        "Location": "Phoenix",
        "Condition": "Cloudy",
        "Temperature (C)": 11.4,
        "Humidity (%)": 33,
        "Day": "Friday"
    },
    {
        "Location": "Seattle",
        "Condition": "Windy",
        "Temperature (C)": 2.2,
        "Humidity (%)": 88,
        "Day": "Saturday"
    },
    {
        "Location": "Chicago",
        "Condition": "Rainy",
        "Temperature (C)": 29.0,
        "Humidity (%)": 71,
        "Day": "Saturday"
    },
    {
        "Location": "Seattle",
        "Condition": "Snowy",
        "Temperature (C)": 15.3,
        "Humidity (%)": 95,
        "Day": "Thursday"
    },
    {
        "Location": "Seattle",
        "Condition": "Snowy",
        "Temperature (C)": 36.4,
        "Humidity (%)": 67,
        "Day": "Thursday"
    },
    {
        "Location": "Seattle",
        "Condition": "Snowy",
        "Temperature (C)": 17.2,
        "Humidity (%)": 30,
        "Day": "Tuesday"
    }
]<start>
| Location | Condition | Temperature (C) | Humidity (%) | Day |
| --- | --- | --- | --- | --- |
| Phoenix | Stormy | 20.5 | 90 | Saturday |
| Chicago | Windy | 37.0 | 96 | Saturday |
| Miami | Windy | 28.1 | 70 | Monday |
| Phoenix | Cloudy | 11.4 | 33 | Friday |
| Seattle | Windy | 2.2 | 88 | Saturday |
| Chicago | Rainy | 29.0 | 71 | Saturday |
| Seattle | Snowy | 15.3 | 95 | Thursday |
| Seattle | Snowy | 36.4 | 67 | Thursday |
| Seattle | Snowy | 17.2 | 30 | Tuesday |
<end>Can you change this markdown into CSV?
| Trip Name | Start Location | Duration (hours) | Fuel Used (gallons) |
| --- | --- | --- | --- |
| Valley Voyage | San Francisco | 61.4 | 26.9 |
| Canyon Trek | Los Angeles | 53.2 | 84.1 |
| Canyon Trek | Miami | 34.1 | 58.6 |
| Highway Odyssey | Miami | 35.2 | 44.2 |
| Valley Voyage | Phoenix | 47.2 | 42.4 |
| Highway Odyssey | Houston | 62.9 | 21.4 |
| Coast to Coast | New York | 61.0 | 27.0 |
| Coast to Coast | Los Angeles | 20.4 | 84.1 |
| City Explorer | Miami | 18.6 | 31.1 |
| Canyon Trek | Los Angeles | 32.9 | 81.8 |<start>
Trip Name,Start Location,Duration (hours),Fuel Used (gallons)
Valley Voyage,San Francisco,61.4,26.9
Canyon Trek,Los Angeles,53.2,84.1
Canyon Trek,Miami,34.1,58.6
Highway Odyssey,Miami,35.2,44.2
Valley Voyage,Phoenix,47.2,42.4
Highway Odyssey,Houston,62.9,21.4
Coast to Coast,New York,61.0,27.0
Coast to Coast,Los Angeles,20.4,84.1
City Explorer,Miami,18.6,31.1
Canyon Trek,Los Angeles,32.9,81.8
<end>Can you change this Markdown into YML?
| Product Name | SKU | Price | Category | Supplier Name |
| --- | --- | --- | --- | --- |
| Whatchamacallit | SKU-1003 | 44.77 | Household | ACME Corp |
| Gadget | SKU-1014 | 47.13 | Electronics | ACME Corp |
| Whatchamacallit | SKU-1015 | 184.15 | Toys | ACME Corp |
| Thingamajig | SKU-1001 | 363.05 | Sports | Umbrella Corp |
| Device | SKU-1010 | 125.73 | Toys | Wonka Industries |
| Gadget | SKU-1077 | 57.84 | Electronics | Globex |
| Apparatus | SKU-1067 | 493.6 | Electronics | Wonka Industries |<start>
- Category: Household
  Price: 44.77
  Product Name: Whatchamacallit
  SKU: SKU-1003
  Supplier Name: ACME Corp
- Category: Electronics
  Price: 47.13
  Product Name: Gadget
  SKU: SKU-1014
  Supplier Name: ACME Corp
- Category: Toys
  Price: 184.15
  Product Name: Whatchamacallit
  SKU: SKU-1015
  Supplier Name: ACME Corp
- Category: Sports
  Price: 363.05
  Product Name: Thingamajig
  SKU: SKU-1001
  Supplier Name: Umbrella Corp
- Category: Toys
  Price: 125.73
  Product Name: Device
  SKU: SKU-1010
  Supplier Name: Wonka Industries
- Category: Electronics
  Price: 57.84
  Product Name: Gadget
  SKU: SKU-1077
  Supplier Name: Globex
- Category: Electronics
  Price: 493.6
  Product Name: Apparatus
  SKU: SKU-1067
  Supplier Name: Wonka Industries
<end>Here's some markdown data, can you convert it to Yml?
| Location | Condition | Temperature (C) | Humidity (%) | Wind Speed (km/h) | Day |
| --- | --- | --- | --- | --- | --- |
| Miami | Sunny | 19.2 | 26 | 17.8 | Wednesday |
| Phoenix | Snowy | 12.8 | 26 | 3.3 | Saturday |
| Seattle | Windy | 37.2 | 56 | 16.4 | Monday |
| Seattle | Stormy | -5.6 | 70 | 6.2 | Thursday |
| Chicago | Stormy | -3.3 | 32 | 4.1 | Saturday |
| Seattle | Windy | 16.9 | 84 | 9.4 | Saturday |
| Houston | Cloudy | 32.9 | 92 | 22.2 | Tuesday |
| New York | Windy | -6.9 | 41 | 4.1 | Saturday |
| Los Angeles | Foggy | 16.9 | 78 | 8.2 | Tuesday |<start>
- Condition: Sunny
  Day: Wednesday
  Humidity (%): 26
  Location: Miami
  Temperature (C): 19.2
  Wind Speed (km/h): 17.8
- Condition: Snowy
  Day: Saturday
  Humidity (%): 26
  Location: Phoenix
  Temperature (C): 12.8
  Wind Speed (km/h): 3.3
- Condition: Windy
  Day: Monday
  Humidity (%): 56
  Location: Seattle
  Temperature (C): 37.2
  Wind Speed (km/h): 16.4
- Condition: Stormy
  Day: Thursday
  Humidity (%): 70
  Location: Seattle
  Temperature (C): -5.6
  Wind Speed (km/h): 6.2
- Condition: Stormy
  Day: Saturday
  Humidity (%): 32
  Location: Chicago
  Temperature (C): -3.3
  Wind Speed (km/h): 4.1
- Condition: Windy
  Day: Saturday
  Humidity (%): 84
  Location: Seattle
  Temperature (C): 16.9
  Wind Speed (km/h): 9.4
- Condition: Cloudy
  Day: Tuesday
  Humidity (%): 92
  Location: Houston
  Temperature (C): 32.9
  Wind Speed (km/h): 22.2
- Condition: Windy
  Day: Saturday
  Humidity (%): 41
  Location: New York
  Temperature (C): -6.9
  Wind Speed (km/h): 4.1
- Condition: Foggy
  Day: Tuesday
  Humidity (%): 78
  Location: Los Angeles
  Temperature (C): 16.9
  Wind Speed (km/h): 8.2
<end>Here's some csv data, can you convert it to PLAIN TEXT?
Restaurant Name,Rating,Price Range
Vegan Delight,4,$$$$
BBQ Barn,3,$$$$
Curry Corner,1,$$$$$
BBQ Barn,5,$
The Golden Spoon,5,$$
Pasta Palace,4,$$$$
Vegan Delight,4,$$$$
Sushi World,4,$
Pizza Planet,1,$
Sushi World,5,$$
<start>
Restaurant Name: Vegan Delight | Rating: 4 | Price Range: $$$$
Restaurant Name: BBQ Barn | Rating: 3 | Price Range: $$$$
Restaurant Name: Curry Corner | Rating: 1 | Price Range: $$$$$
Restaurant Name: BBQ Barn | Rating: 5 | Price Range: $
Restaurant Name: The Golden Spoon | Rating: 5 | Price Range: $$
Restaurant Name: Pasta Palace | Rating: 4 | Price Range: $$$$
Restaurant Name: Vegan Delight | Rating: 4 | Price Range: $$$$
Restaurant Name: Sushi World | Rating: 4 | Price Range: $
Restaurant Name: Pizza Planet | Rating: 1 | Price Range: $
Restaurant Name: Sushi World | Rating: 5 | Price Range: $$
<end>Convert this plain text to markdown:
SKU: SKU-1079 | Price: 327.31 | Stock Quantity: 277 | Category: Toys | Supplier Name: Wonka Industries
SKU: SKU-1092 | Price: 165.88 | Stock Quantity: 225 | Category: Household | Supplier Name: Globex
SKU: SKU-1090 | Price: 52.74 | Stock Quantity: 32 | Category: Household | Supplier Name: Wonka Industries
SKU: SKU-1067 | Price: 188.99 | Stock Quantity: 171 | Category: Electronics | Supplier Name: Globex
<start>
| SKU | Price | Stock Quantity | Category | Supplier Name |
| --- | --- | --- | --- | --- |
| SKU-1079 | 327.31 | 277 | Toys | Wonka Industries |
| SKU-1092 | 165.88 | 225 | Household | Globex |
| SKU-1090 | 52.74 | 32 | Household | Wonka Industries |
| SKU-1067 | 188.99 | 171 | Electronics | Globex |
<end>Transform this json structure to a CSV format:
[
    {
        "Company": "BioPharm",
        "Sector": "Automotive",
        "Market Cap": "Mega Cap",
        "Stock Price": 274.04,
        "Annual Revenue (B)": 196.56,
        "Quarter": "Q3"
    },
    {
        "Company": "TechCorp",
        "Sector": "Technology",
        "Market Cap": "Small Cap",
        "Stock Price": 562.1,
        "Annual Revenue (B)": 364.47,
        "Quarter": "Q2"
    },
    {
        "Company": "AeroSpace",
        "Sector": "Biotech",
        "Market Cap": "Mega Cap",
        "Stock Price": 347.29,
        "Annual Revenue (B)": 158.17,
        "Quarter": "Q4"
    },
    {
        "Company": "RetailHub",
        "Sector": "Healthcare",
        "Market Cap": "Small Cap",
        "Stock Price": 94.5,
        "Annual Revenue (B)": 261.19,
        "Quarter": "Q4"
    },
    {
        "Company": "EcoEnergy",
        "Sector": "Retail",
        "Market Cap": "Large Cap",
        "Stock Price": 42.17,
        "Annual Revenue (B)": 201.93,
        "Quarter": "Q4"
    },
    {
        "Company": "GlobalTrade",
        "Sector": "Finance",
        "Market Cap": "Small Cap",
        "Stock Price": 751.35,
        "Annual Revenue (B)": 498.86,
        "Quarter": "Q4"
    },
    {
        "Company": "BioPharm",
        "Sector": "Automotive",
        "Market Cap": "Mid Cap",
        "Stock Price": 139.59,
        "Annual Revenue (B)": 110.92,
        "Quarter": "Q4"
    },
    {
        "Company": "TechCorp",
        "Sector": "Aerospace",
        "Market Cap": "Small Cap",
        "Stock Price": 853.37,
        "Annual Revenue (B)": 423.57,
        "Quarter": "Q4"
    },
    {
        "Company": "RetailHub",
        "Sector": "Technology",
        "Market Cap": "Small Cap",
        "Stock Price": 518.47,
        "Annual Revenue (B)": 367.78,
        "Quarter": "Q3"
    },
    {
        "Company": "HealthPlus",
        "Sector": "Aerospace",
        "Market Cap": "Mid Cap",
        "Stock Price": 137.44,
        "Annual Revenue (B)": 209.97,
        "Quarter": "Q2"
    }
]<start>
Company,Sector,Market Cap,Stock Price,Annual Revenue (B),Quarter
BioPharm,Automotive,Mega Cap,274.04,196.56,Q3
TechCorp,Technology,Small Cap,562.1,364.47,Q2
AeroSpace,Biotech,Mega Cap,347.29,158.17,Q4
RetailHub,Healthcare,Small Cap,94.5,261.19,Q4
EcoEnergy,Retail,Large Cap,42.17,201.93,Q4
GlobalTrade,Finance,Small Cap,751.35,498.86,Q4
BioPharm,Automotive,Mid Cap,139.59,110.92,Q4
TechCorp,Aerospace,Small Cap,853.37,423.57,Q4
RetailHub,Technology,Small Cap,518.47,367.78,Q3
HealthPlus,Aerospace,Mid Cap,137.44,209.97,Q2
<end>Convert this MARKDOWN to JSON:
| Location | Condition | Temperature (C) | Humidity (%) | Wind Speed (km/h) | Day |
| --- | --- | --- | --- | --- | --- |
| Seattle | Rainy | 35.0 | 39 | 6.2 | Wednesday |
| Chicago | Sunny | 36.4 | 61 | 10.8 | Friday |
| Denver | Cloudy | 21.6 | 20 | 9.0 | Wednesday |
| Seattle | Snowy | 12.5 | 31 | 2.6 | Sunday |
| Seattle | Windy | 36.4 | 39 | 5.6 | Monday |
| New York | Snowy | 37.3 | 91 | 9.1 | Friday |
| Seattle | Rainy | 36.1 | 37 | 10.9 | Thursday |
| Denver | Rainy | 33.5 | 98 | 24.7 | Thursday |
| Phoenix | Snowy | 28.5 | 81 | 29.2 | Friday |
| Phoenix | Snowy | 6.6 | 84 | 3.0 | Friday |<start>
[
    {
        "Location": "Seattle",
        "Condition": "Rainy",
        "Temperature (C)": 35.0,
        "Humidity (%)": 39,
        "Wind Speed (km/h)": 6.2,
        "Day": "Wednesday"
    },
    {
        "Location": "Chicago",
        "Condition": "Sunny",
        "Temperature (C)": 36.4,
        "Humidity (%)": 61,
        "Wind Speed (km/h)": 10.8,
        "Day": "Friday"
    },
    {
        "Location": "Denver",
        "Condition": "Cloudy",
        "Temperature (C)": 21.6,
        "Humidity (%)": 20,
        "Wind Speed (km/h)": 9.0,
        "Day": "Wednesday"
    },
    {
        "Location": "Seattle",
        "Condition": "Snowy",
        "Temperature (C)": 12.5,
        "Humidity (%)": 31,
        "Wind Speed (km/h)": 2.6,
        "Day": "Sunday"
    },
    {
        "Location": "Seattle",
        "Condition": "Windy",
        "Temperature (C)": 36.4,
        "Humidity (%)": 39,
        "Wind Speed (km/h)": 5.6,
        "Day": "Monday"
    },
    {
        "Location": "New York",
        "Condition": "Snowy",
        "Temperature (C)": 37.3,
        "Humidity (%)": 91,
        "Wind Speed (km/h)": 9.1,
        "Day": "Friday"
    },
    {
        "Location": "Seattle",
        "Condition": "Rainy",
        "Temperature (C)": 36.1,
        "Humidity (%)": 37,
        "Wind Speed (km/h)": 10.9,
        "Day": "Thursday"
    },
    {
        "Location": "Denver",
        "Condition": "Rainy",
        "Temperature (C)": 33.5,
        "Humidity (%)": 98,
        "Wind Speed (km/h)": 24.7,
        "Day": "Thursday"
    },
    {
        "Location": "Phoenix",
        "Condition": "Snowy",
        "Temperature (C)": 28.5,
        "Humidity (%)": 81,
        "Wind Speed (km/h)": 29.2,
        "Day": "Friday"
    },
    {
        "Location": "Phoenix",
        "Condition": "Snowy",
        "Temperature (C)": 6.6,
        "Humidity (%)": 84,
        "Wind Speed (km/h)": 3.0,
        "Day": "Friday"
    }
]
<end>Transform this JSON structure to a YML format:
[
    {
        "Title": "The Forgotten World",
        "Author": "Orion Frostblade",
        "Genre": "Non-Fiction",
        "Publication Year": 1974,
        "Rating": 5.0
    },
    {
        "Title": "The Silent Grove",
        "Author": "Rowan Ashborne",
        "Genre": "Fantasy",
        "Publication Year": 2001,
        "Rating": 1.0
    },
    {
        "Title": "The Silent Grove",
        "Author": "Kara Firebrand",
        "Genre": "Fantasy",
        "Publication Year": 1953,
        "Rating": 1.4
    },
    {
        "Title": "The Last Sky",
        "Author": "Rowan Ashborne",
        "Genre": "Thriller",
        "Publication Year": 1987,
        "Rating": 1.2
    }
]<start>
- Author: Orion Frostblade
  Genre: Non-Fiction
  Publication Year: 1974
  Rating: 5.0
  Title: The Forgotten World
- Author: Rowan Ashborne
  Genre: Fantasy
  Publication Year: 2001
  Rating: 1.0
  Title: The Silent Grove
- Author: Kara Firebrand
  Genre: Fantasy
  Publication Year: 1953
  Rating: 1.4
  Title: The Silent Grove
- Author: Rowan Ashborne
  Genre: Thriller
  Publication Year: 1987
  Rating: 1.2
  Title: The Last Sky
<end>Can you change this markdown into YAML?
| Trip Name | Start Location | End Location | Distance (miles) | Duration (hours) | Fuel Used (gallons) |
| --- | --- | --- | --- | --- | --- |
| Historic Route | Miami | San Francisco | 1421.3 | 12.5 | 64.1 |
| Canyon Trek | Houston | Chicago | 76.5 | 70.8 | 43.5 |
| Forest Journey | Denver | San Francisco | 2828.3 | 11.8 | 51.8 |
| Historic Route | Phoenix | New York | 2581.5 | 22.5 | 69.6 |
| City Explorer | San Francisco | Denver | 269.0 | 59.0 | 71.5 |
| Forest Journey | Houston | Denver | 2574.4 | 55.0 | 19.5 |
| Valley Voyage | San Francisco | Chicago | 71.9 | 22.8 | 87.5 |
| Forest Journey | Houston | New York | 1393.7 | 12.5 | 70.3 |<start>
- Distance (miles): 1421.3
  Duration (hours): 12.5
  End Location: San Francisco
  Fuel Used (gallons): 64.1
  Start Location: Miami
  Trip Name: Historic Route
- Distance (miles): 76.5
  Duration (hours): 70.8
  End Location: Chicago
  Fuel Used (gallons): 43.5
  Start Location: Houston
  Trip Name: Canyon Trek
- Distance (miles): 2828.3
  Duration (hours): 11.8
  End Location: San Francisco
  Fuel Used (gallons): 51.8
  Start Location: Denver
  Trip Name: Forest Journey
- Distance (miles): 2581.5
  Duration (hours): 22.5
  End Location: New York
  Fuel Used (gallons): 69.6
  Start Location: Phoenix
  Trip Name: Historic Route
- Distance (miles): 269.0
  Duration (hours): 59.0
  End Location: Denver
  Fuel Used (gallons): 71.5
  Start Location: San Francisco
  Trip Name: City Explorer
- Distance (miles): 2574.4
  Duration (hours): 55.0
  End Location: Denver
  Fuel Used (gallons): 19.5
  Start Location: Houston
  Trip Name: Forest Journey
- Distance (miles): 71.9
  Duration (hours): 22.8
  End Location: Chicago
  Fuel Used (gallons): 87.5
  Start Location: San Francisco
  Trip Name: Valley Voyage
- Distance (miles): 1393.7
  Duration (hours): 12.5
  End Location: New York
  Fuel Used (gallons): 70.3
  Start Location: Houston
  Trip Name: Forest Journey
<end>Transform this plain text structure to a markdown format:
Title: A Journey Through Time | Author: Elara Moonshadow | Genre: Thriller | Publication Year: 1956 | Rating: 1.4
Title: A Journey Through Time | Author: Isla Windrider | Genre: Thriller | Publication Year: 2005 | Rating: 3.1
Title: The Silent Grove | Author: Elara Moonshadow | Genre: Thriller | Publication Year: 1952 | Rating: 4.5
Title: Tales of the Brave | Author: Kara Firebrand | Genre: Mystery | Publication Year: 1980 | Rating: 1.6
Title: The Crystal Key | Author: Thorne Ironwood | Genre: Historical | Publication Year: 1994 | Rating: 1.8
Title: Shadows of Solitude | Author: Thorne Ironwood | Genre: Historical | Publication Year: 2010 | Rating: 4.4
<start>
| Title | Author | Genre | Publication Year | Rating |
| --- | --- | --- | --- | --- |
| A Journey Through Time | Elara Moonshadow | Thriller | 1956 | 1.4 |
| A Journey Through Time | Isla Windrider | Thriller | 2005 | 3.1 |
| The Silent Grove | Elara Moonshadow | Thriller | 1952 | 4.5 |
| Tales of the Brave | Kara Firebrand | Mystery | 1980 | 1.6 |
| The Crystal Key | Thorne Ironwood | Historical | 1994 | 1.8 |
| Shadows of Solitude | Thorne Ironwood | Historical | 2010 | 4.4 |
<end>Can you change this MARKDOWN into csv?
| Title | Genre | Release Year | Box Office Earnings (M) |
| --- | --- | --- | --- |
| Escape from Earth | Action | 2007 | 315.18 |
| Edge of Infinity | Fantasy | 2011 | 293.98 |
| Dreamwalker | Comedy | 1975 | 386.21 |
| The Endless Horizon | Action | 2019 | 350.24 |
| Mystery of the Depths | Action | 2019 | 293.98 |
| The Final Voyage | Fantasy | 1999 | 18.09 |
| Mystery of the Depths | Adventure | 1997 | 313.16 |
| The Endless Horizon | Sci-Fi | 2017 | 399.6 |
| The Great Expedition | Adventure | 2015 | 831.61 |
| Edge of Infinity | Action | 2005 | 603.37 |<start>
Title,Genre,Release Year,Box Office Earnings (M)
Escape from Earth,Action,2007,315.18
Edge of Infinity,Fantasy,2011,293.98
Dreamwalker,Comedy,1975,386.21
The Endless Horizon,Action,2019,350.24
Mystery of the Depths,Action,2019,293.98
The Final Voyage,Fantasy,1999,18.09
Mystery of the Depths,Adventure,1997,313.16
The Endless Horizon,Sci-Fi,2017,399.6
The Great Expedition,Adventure,2015,831.61
Edge of Infinity,Action,2005,603.37
<end>Convert this yml to csv:
- Market Cap: Mega Cap
  Quarter: Q4
  Sector: Finance
  Stock Price: 103.75
- Market Cap: Mid Cap
  Quarter: Q4
  Sector: Technology
  Stock Price: 338.7
- Market Cap: Small Cap
  Quarter: Q2
  Sector: Aerospace
  Stock Price: 717.88
- Market Cap: Large Cap
  Quarter: Q3
  Sector: Technology
  Stock Price: 877.47
- Market Cap: Small Cap
  Quarter: Q4
  Sector: Automotive
  Stock Price: 335.42
<start>
Sector,Market Cap,Stock Price,Quarter
Finance,Mega Cap,103.75,Q4
Technology,Mid Cap,338.7,Q4
Aerospace,Small Cap,717.88,Q2
Technology,Large Cap,877.47,Q3
Automotive,Small Cap,335.42,Q4
<end>Can you change this JSON into plain text?
[
    {
        "Name": "Tammy",
        "Age": 41,
        "Birth Month": "June",
        "Income": 310000
    },
    {
        "Name": "Tony",
        "Age": 29,
        "Birth Month": "January",
        "Income": 340000
    },
    {
        "Name": "Susie",
        "Age": 24,
        "Birth Month": "March",
        "Income": 125000
    },
    {
        "Name": "Hadley",
        "Age": 56,
        "Birth Month": "February",
        "Income": 105000
    },
    {
        "Name": "Walter",
        "Age": 36,
        "Birth Month": "May",
        "Income": 245000
    },
    {
        "Name": "Delores",
        "Age": 30,
        "Birth Month": "November",
        "Income": 205000
    },
    {
        "Name": "Sandy",
        "Age": 52,
        "Birth Month": "November",
        "Income": 405000
    },
    {
        "Name": "Jimmy",
        "Age": 53,
        "Birth Month": "September",
        "Income": 50000
    }
]<start>
Name: Tammy | Age: 41 | Birth Month: June | Income: 310000
Name: Tony | Age: 29 | Birth Month: January | Income: 340000
Name: Susie | Age: 24 | Birth Month: March | Income: 125000
Name: Hadley | Age: 56 | Birth Month: February | Income: 105000
Name: Walter | Age: 36 | Birth Month: May | Income: 245000
Name: Delores | Age: 30 | Birth Month: November | Income: 205000
Name: Sandy | Age: 52 | Birth Month: November | Income: 405000
Name: Jimmy | Age: 53 | Birth Month: September | Income: 50000
<end>Transform this markdown structure to a YML format:
| Trip Name | End Location | Distance (miles) |
| --- | --- | --- |
| Historic Route | San Francisco | 793.3 |
| Forest Journey | Los Angeles | 466.5 |
| Valley Voyage | New York | 2753.2 |
| City Explorer | New York | 354.8 |
| Valley Voyage | Denver | 558.1 |
| Valley Voyage | Phoenix | 2954.2 |
| Forest Journey | New York | 2121.2 |
| Highway Odyssey | Los Angeles | 2036.4 |
| Desert Drive | Phoenix | 51.0 |<start>
- Distance (miles): 793.3
  End Location: San Francisco
  Trip Name: Historic Route
- Distance (miles): 466.5
  End Location: Los Angeles
  Trip Name: Forest Journey
- Distance (miles): 2753.2
  End Location: New York
  Trip Name: Valley Voyage
- Distance (miles): 354.8
  End Location: New York
  Trip Name: City Explorer
- Distance (miles): 558.1
  End Location: Denver
  Trip Name: Valley Voyage
- Distance (miles): 2954.2
  End Location: Phoenix
  Trip Name: Valley Voyage
- Distance (miles): 2121.2
  End Location: New York
  Trip Name: Forest Journey
- Distance (miles): 2036.4
  End Location: Los Angeles
  Trip Name: Highway Odyssey
- Distance (miles): 51.0
  End Location: Phoenix
  Trip Name: Desert Drive
<end>Convert this Csv to MARKDOWN:
Database Name,Cache Hit Ratio (%),Connection Count,Average Latency (ms),Timestamp
ProfilesDB,75.05,497,3.29,2021-08-10 09:02:05
ProductsDB,77.5,365,26.78,2022-12-04 21:16:50
SalesDB,90.47,497,53.2,2022-01-15 14:51:57
<start>
| Database Name | Cache Hit Ratio (%) | Connection Count | Average Latency (ms) | Timestamp |
| --- | --- | --- | --- | --- |
| ProfilesDB | 75.05 | 497 | 3.29 | 2021-08-10 09:02:05 |
| ProductsDB | 77.5 | 365 | 26.78 | 2022-12-04 21:16:50 |
| SalesDB | 90.47 | 497 | 53.2 | 2022-01-15 14:51:57 |
<end>Transform this MARKDOWN structure to a plain text format:
| SKU | Price | Stock Quantity |
| --- | --- | --- |
| SKU-1064 | 67.17 | 114 |
| SKU-1061 | 240.34 | 277 |
| SKU-1017 | 230.13 | 33 |
| SKU-1029 | 134.39 | 382 |
| SKU-1027 | 337.46 | 292 |<start>
SKU: SKU-1064 | Price: 67.17 | Stock Quantity: 114
SKU: SKU-1061 | Price: 240.34 | Stock Quantity: 277
SKU: SKU-1017 | Price: 230.13 | Stock Quantity: 33
SKU: SKU-1029 | Price: 134.39 | Stock Quantity: 382
SKU: SKU-1027 | Price: 337.46 | Stock Quantity: 292
<end>Convert this PLAIN TEXT to Yml:
Queries per Second: 3110.75 | Cache Hit Ratio (%): 98.91 | Connection Count: 64 | Average Latency (ms): 66.2
Queries per Second: 3785.36 | Cache Hit Ratio (%): 83.76 | Connection Count: 36 | Average Latency (ms): 38.57
Queries per Second: 2039.43 | Cache Hit Ratio (%): 75.17 | Connection Count: 378 | Average Latency (ms): 63.96
<start>
- Average Latency (ms): 66.2
  Cache Hit Ratio (%): 98.91
  Connection Count: 64
  Queries per Second: 3110.75
- Average Latency (ms): 38.57
  Cache Hit Ratio (%): 83.76
  Connection Count: 36
  Queries per Second: 3785.36
- Average Latency (ms): 63.96
  Cache Hit Ratio (%): 75.17
  Connection Count: 378
  Queries per Second: 2039.43
<end>Can you change this Csv into Yml?
Title,Genre,Publication Year,Rating
Tales of the Brave,Non-Fiction,1983,1.4
Shadows of Solitude,Science Fiction,2005,3.7
Shadows of Solitude,Mystery,2016,2.4
A Journey Through Time,Fantasy,1961,1.4
<start>
- Genre: Non-Fiction
  Publication Year: 1983
  Rating: 1.4
  Title: Tales of the Brave
- Genre: Science Fiction
  Publication Year: 2005
  Rating: 3.7
  Title: Shadows of Solitude
- Genre: Mystery
  Publication Year: 2016
  Rating: 2.4
  Title: Shadows of Solitude
- Genre: Fantasy
  Publication Year: 1961
  Rating: 1.4
  Title: A Journey Through Time
<end>Here's some csv data, can you convert it to json?
Queries per Second,Cache Hit Ratio (%),Connection Count,Average Latency (ms)
3130.82,74.46,387,15.75
536.18,90.38,380,3.51
174.89,77.31,399,34.07
3472.09,89.15,495,81.46
3717.88,76.98,183,12.28
2270.79,92.32,186,97.42
2740.06,82.88,179,18.7
1014.58,81.28,277,71.14
775.12,91.74,380,69.55
2031.88,78.47,455,74.84
<start>
[
    {
        "Queries per Second": 3130.82,
        "Cache Hit Ratio (%)": 74.46,
        "Connection Count": 387,
        "Average Latency (ms)": 15.75
    },
    {
        "Queries per Second": 536.18,
        "Cache Hit Ratio (%)": 90.38,
        "Connection Count": 380,
        "Average Latency (ms)": 3.51
    },
    {
        "Queries per Second": 174.89,
        "Cache Hit Ratio (%)": 77.31,
        "Connection Count": 399,
        "Average Latency (ms)": 34.07
    },
    {
        "Queries per Second": 3472.09,
        "Cache Hit Ratio (%)": 89.15,
        "Connection Count": 495,
        "Average Latency (ms)": 81.46
    },
    {
        "Queries per Second": 3717.88,
        "Cache Hit Ratio (%)": 76.98,
        "Connection Count": 183,
        "Average Latency (ms)": 12.28
    },
    {
        "Queries per Second": 2270.79,
        "Cache Hit Ratio (%)": 92.32,
        "Connection Count": 186,
        "Average Latency (ms)": 97.42
    },
    {
        "Queries per Second": 2740.06,
        "Cache Hit Ratio (%)": 82.88,
        "Connection Count": 179,
        "Average Latency (ms)": 18.7
    },
    {
        "Queries per Second": 1014.58,
        "Cache Hit Ratio (%)": 81.28,
        "Connection Count": 277,
        "Average Latency (ms)": 71.14
    },
    {
        "Queries per Second": 775.12,
        "Cache Hit Ratio (%)": 91.74,
        "Connection Count": 380,
        "Average Latency (ms)": 69.55
    },
    {
        "Queries per Second": 2031.88,
        "Cache Hit Ratio (%)": 78.47,
        "Connection Count": 455,
        "Average Latency (ms)": 74.84
    }
]
<end>Please transform the following plain text data into Yaml:
Trip Name: Lakeside Retreat | Start Location: New York | End Location: Miami | Duration (hours): 12.5 | Fuel Used (gallons): 24.7
Trip Name: Mountain Adventure | Start Location: New York | End Location: Denver | Duration (hours): 56.2 | Fuel Used (gallons): 83.9
Trip Name: Desert Drive | Start Location: Chicago | End Location: Denver | Duration (hours): 14.6 | Fuel Used (gallons): 78.9
Trip Name: Mountain Adventure | Start Location: New York | End Location: Denver | Duration (hours): 11.2 | Fuel Used (gallons): 52.8
Trip Name: Lakeside Retreat | Start Location: Los Angeles | End Location: Chicago | Duration (hours): 33.3 | Fuel Used (gallons): 21.0
Trip Name: Mountain Adventure | Start Location: Los Angeles | End Location: Miami | Duration (hours): 27.9 | Fuel Used (gallons): 79.7
Trip Name: Canyon Trek | Start Location: Denver | End Location: Miami | Duration (hours): 51.6 | Fuel Used (gallons): 17.2
<start>
- Duration (hours): 12.5
  End Location: Miami
  Fuel Used (gallons): 24.7
  Start Location: New York
  Trip Name: Lakeside Retreat
- Duration (hours): 56.2
  End Location: Denver
  Fuel Used (gallons): 83.9
  Start Location: New York
  Trip Name: Mountain Adventure
- Duration (hours): 14.6
  End Location: Denver
  Fuel Used (gallons): 78.9
  Start Location: Chicago
  Trip Name: Desert Drive
- Duration (hours): 11.2
  End Location: Denver
  Fuel Used (gallons): 52.8
  Start Location: New York
  Trip Name: Mountain Adventure
- Duration (hours): 33.3
  End Location: Chicago
  Fuel Used (gallons): 21.0
  Start Location: Los Angeles
  Trip Name: Lakeside Retreat
- Duration (hours): 27.9
  End Location: Miami
  Fuel Used (gallons): 79.7
  Start Location: Los Angeles
  Trip Name: Mountain Adventure
- Duration (hours): 51.6
  End Location: Miami
  Fuel Used (gallons): 17.2
  Start Location: Denver
  Trip Name: Canyon Trek
<end>Here's some plain text data, can you convert it to YAML?
Cuisine: Mexican | Rating: 5 | Price Range: $$
Cuisine: French | Rating: 5 | Price Range: $$$$$
Cuisine: French | Rating: 2 | Price Range: $$$
Cuisine: Mexican | Rating: 3 | Price Range: $$
<start>
- Cuisine: Mexican
  Price Range: $$
  Rating: 5
- Cuisine: French
  Price Range: $$$$$
  Rating: 5
- Cuisine: French
  Price Range: $$$
  Rating: 2
- Cuisine: Mexican
  Price Range: $$
  Rating: 3
<end>Can you change this csv into Plain text?
Product Name,SKU,Price,Category,Supplier Name
Device,SKU-1029,474.47,Sports,Wonka Industries
Device,SKU-1098,187.62,Household,Umbrella Corp
Widget,SKU-1076,273.26,Household,Globex
<start>
Product Name: Device | SKU: SKU-1029 | Price: 474.47 | Category: Sports | Supplier Name: Wonka Industries
Product Name: Device | SKU: SKU-1098 | Price: 187.62 | Category: Household | Supplier Name: Umbrella Corp
Product Name: Widget | SKU: SKU-1076 | Price: 273.26 | Category: Household | Supplier Name: Globex
<end>Please transform the following Json data into markdown:
[
    {
        "Trip Name": "Canyon Trek",
        "End Location": "New York",
        "Distance (miles)": 962.5
    },
    {
        "Trip Name": "Desert Drive",
        "End Location": "Miami",
        "Distance (miles)": 2144.7
    },
    {
        "Trip Name": "Forest Journey",
        "End Location": "Phoenix",
        "Distance (miles)": 781.1
    },
    {
        "Trip Name": "Historic Route",
        "End Location": "Chicago",
        "Distance (miles)": 1435.5
    },
    {
        "Trip Name": "Desert Drive",
        "End Location": "Phoenix",
        "Distance (miles)": 1196.5
    }
]<start>
| Trip Name | End Location | Distance (miles) |
| --- | --- | --- |
| Canyon Trek | New York | 962.5 |
| Desert Drive | Miami | 2144.7 |
| Forest Journey | Phoenix | 781.1 |
| Historic Route | Chicago | 1435.5 |
| Desert Drive | Phoenix | 1196.5 |
<end>Please transform the following JSON data into Csv:
[
    {
        "Database Name": "OrdersDB",
        "Queries per Second": 3784.57,
        "Connection Count": 351,
        "Average Latency (ms)": 76.22,
        "Timestamp": "2023-10-14 05:58:53"
    },
    {
        "Database Name": "OrdersDB",
        "Queries per Second": 1094.84,
        "Connection Count": 456,
        "Average Latency (ms)": 25.74,
        "Timestamp": "2021-09-15 20:34:52"
    },
    {
        "Database Name": "SalesDB",
        "Queries per Second": 3749.62,
        "Connection Count": 261,
        "Average Latency (ms)": 53.11,
        "Timestamp": "2021-11-12 15:33:25"
    }
]<start>
Database Name,Queries per Second,Connection Count,Average Latency (ms),Timestamp
OrdersDB,3784.57,351,76.22,2023-10-14 05:58:53
OrdersDB,1094.84,456,25.74,2021-09-15 20:34:52
SalesDB,3749.62,261,53.11,2021-11-12 15:33:25
<end>Please transform the following json data into yaml:
[
    {
        "Location": "Miami",
        "Condition": "Windy",
        "Temperature (C)": -6.1,
        "Humidity (%)": 42,
        "Wind Speed (km/h)": 0.7,
        "Day": "Monday"
    },
    {
        "Location": "Seattle",
        "Condition": "Rainy",
        "Temperature (C)": -7.0,
        "Humidity (%)": 79,
        "Wind Speed (km/h)": 27.2,
        "Day": "Sunday"
    },
    {
        "Location": "Seattle",
        "Condition": "Cloudy",
        "Temperature (C)": 33.1,
        "Humidity (%)": 57,
        "Wind Speed (km/h)": 26.3,
        "Day": "Saturday"
    },
    {
        "Location": "New York",
        "Condition": "Stormy",
        "Temperature (C)": 34.3,
        "Humidity (%)": 64,
        "Wind Speed (km/h)": 15.0,
        "Day": "Friday"
    }
]<start>
- Condition: Windy
  Day: Monday
  Humidity (%): 42
  Location: Miami
  Temperature (C): -6.1
  Wind Speed (km/h): 0.7
- Condition: Rainy
  Day: Sunday
  Humidity (%): 79
  Location: Seattle
  Temperature (C): -7.0
  Wind Speed (km/h): 27.2
- Condition: Cloudy
  Day: Saturday
  Humidity (%): 57
  Location: Seattle
  Temperature (C): 33.1
  Wind Speed (km/h): 26.3
- Condition: Stormy
  Day: Friday
  Humidity (%): 64
  Location: New York
  Temperature (C): 34.3
  Wind Speed (km/h): 15.0
<end>Please transform the following CSV data into plain text:
Title,Author,Publication Year,Rating
Whispers of the Abyss,Kara Firebrand,1980,3.2
The Forgotten World,Kara Firebrand,1990,2.2
Whispers of the Abyss,Draven Blackthorn,2002,2.5
The Forgotten World,Isla Windrider,1966,1.5
The Silent Grove,Rowan Ashborne,1982,3.8
<start>
Title: Whispers of the Abyss | Author: Kara Firebrand | Publication Year: 1980 | Rating: 3.2
Title: The Forgotten World | Author: Kara Firebrand | Publication Year: 1990 | Rating: 2.2
Title: Whispers of the Abyss | Author: Draven Blackthorn | Publication Year: 2002 | Rating: 2.5
Title: The Forgotten World | Author: Isla Windrider | Publication Year: 1966 | Rating: 1.5
Title: The Silent Grove | Author: Rowan Ashborne | Publication Year: 1982 | Rating: 3.8
<end>Can you change this Yaml into csv?
- Genre: Adventure
  Release Year: 1998
  Title: The Final Voyage
- Genre: Thriller
  Release Year: 2002
  Title: Rise of the Titans
- Genre: Adventure
  Release Year: 1978
  Title: Escape from Earth
<start>
Title,Genre,Release Year
The Final Voyage,Adventure,1998
Rise of the Titans,Thriller,2002
Escape from Earth,Adventure,1978
<end>Can you change this csv into MARKDOWN?
Director,Release Year,Box Office Earnings (M)
Rylan Frostblade,2017,978.86
Selene Darkwhisper,1971,599.84
Lira Silverleaf,2007,267.78
Cade Firebrand,2022,189.47
Zara Stormrider,2004,650.04
Rylan Frostblade,1992,618.9
Talon Blackthorn,2022,406.85
Mara Moonshadow,1996,335.55
Selene Darkwhisper,1981,540.64
<start>
| Director | Release Year | Box Office Earnings (M) |
| --- | --- | --- |
| Rylan Frostblade | 2017 | 978.86 |
| Selene Darkwhisper | 1971 | 599.84 |
| Lira Silverleaf | 2007 | 267.78 |
| Cade Firebrand | 2022 | 189.47 |
| Zara Stormrider | 2004 | 650.04 |
| Rylan Frostblade | 1992 | 618.9 |
| Talon Blackthorn | 2022 | 406.85 |
| Mara Moonshadow | 1996 | 335.55 |
| Selene Darkwhisper | 1981 | 540.64 |
<end>Can you change this yaml into json?
- Category: Toys
  Price: 96.89
  SKU: SKU-1071
- Category: Automotive
  Price: 143.76
  SKU: SKU-1029
- Category: Household
  Price: 398.24
  SKU: SKU-1065
- Category: Toys
  Price: 475.25
  SKU: SKU-1074
<start>
[
    {
        "SKU": "SKU-1071",
        "Price": 96.89,
        "Category": "Toys"
    },
    {
        "SKU": "SKU-1029",
        "Price": 143.76,
        "Category": "Automotive"
    },
    {
        "SKU": "SKU-1065",
        "Price": 398.24,
        "Category": "Household"
    },
    {
        "SKU": "SKU-1074",
        "Price": 475.25,
        "Category": "Toys"
    }
]
<end>Here's some plain text data, can you convert it to Csv?
Title: Whispers of the Abyss | Author: Kara Firebrand | Genre: Horror | Publication Year: 2018 | Rating: 4.2
Title: The Last Sky | Author: Isla Windrider | Genre: Horror | Publication Year: 1990 | Rating: 1.7
Title: A Journey Through Time | Author: Thorne Ironwood | Genre: Non-Fiction | Publication Year: 2023 | Rating: 4.4
Title: The Last Sky | Author: Sylvia Nightshade | Genre: Historical | Publication Year: 2008 | Rating: 2.4
Title: Echoes of Eternity | Author: Orion Frostblade | Genre: Fantasy | Publication Year: 2007 | Rating: 2.8
Title: The Last Sky | Author: Thorne Ironwood | Genre: Mystery | Publication Year: 1961 | Rating: 2.0
Title: The Silent Grove | Author: Sylvia Nightshade | Genre: Romance | Publication Year: 1991 | Rating: 3.8
Title: Whispers of the Abyss | Author: Galen Starfire | Genre: Romance | Publication Year: 2005 | Rating: 5.0
Title: Legends of the Rift | Author: Orion Frostblade | Genre: Mystery | Publication Year: 2002 | Rating: 1.6
Title: The Silent Grove | Author: Isla Windrider | Genre: Fantasy | Publication Year: 1968 | Rating: 1.8
<start>
Title,Author,Genre,Publication Year,Rating
Whispers of the Abyss,Kara Firebrand,Horror,2018,4.2
The Last Sky,Isla Windrider,Horror,1990,1.7
A Journey Through Time,Thorne Ironwood,Non-Fiction,2023,4.4
The Last Sky,Sylvia Nightshade,Historical,2008,2.4
Echoes of Eternity,Orion Frostblade,Fantasy,2007,2.8
The Last Sky,Thorne Ironwood,Mystery,1961,2.0
The Silent Grove,Sylvia Nightshade,Romance,1991,3.8
Whispers of the Abyss,Galen Starfire,Romance,2005,5.0
Legends of the Rift,Orion Frostblade,Mystery,2002,1.6
The Silent Grove,Isla Windrider,Fantasy,1968,1.8
<end>Convert this Plain text to markdown:
Date: 2011-03-04 | Open Price: 628.74 | Close Price: 183.89 | High Price: 1320.14 | Low Price: 183.89 | Volume: 3965093
Date: 2013-07-26 | Open Price: 1320.14 | Close Price: 867.17 | High Price: 1320.14 | Low Price: 262.73 | Volume: 5916424
Date: 2017-05-21 | Open Price: 174.24 | Close Price: 443.19 | High Price: 1159.48 | Low Price: 174.24 | Volume: 8864213
Date: 2018-11-23 | Open Price: 891.95 | Close Price: 250.95 | High Price: 891.95 | Low Price: 250.95 | Volume: 695889
Date: 2023-10-21 | Open Price: 617.72 | Close Price: 1296.37 | High Price: 1296.37 | Low Price: 617.72 | Volume: 5693367
Date: 2012-10-19 | Open Price: 1100.78 | Close Price: 26.69 | High Price: 1100.78 | Low Price: 26.69 | Volume: 2847871
Date: 2017-11-18 | Open Price: 1443.02 | Close Price: 174.24 | High Price: 1443.02 | Low Price: 174.24 | Volume: 9060443
Date: 2012-08-07 | Open Price: 1116.46 | Close Price: 1209.97 | High Price: 1209.97 | Low Price: 1116.46 | Volume: 1707720
Date: 2020-04-25 | Open Price: 1392.9 | Close Price: 607.06 | High Price: 1473.35 | Low Price: 119.8 | Volume: 8393220
<start>
| Date | Open Price | Close Price | High Price | Low Price | Volume |
| --- | --- | --- | --- | --- | --- |
| 2011-03-04 | 628.74 | 183.89 | 1320.14 | 183.89 | 3965093 |
| 2013-07-26 | 1320.14 | 867.17 | 1320.14 | 262.73 | 5916424 |
| 2017-05-21 | 174.24 | 443.19 | 1159.48 | 174.24 | 8864213 |
| 2018-11-23 | 891.95 | 250.95 | 891.95 | 250.95 | 695889 |
| 2023-10-21 | 617.72 | 1296.37 | 1296.37 | 617.72 | 5693367 |
| 2012-10-19 | 1100.78 | 26.69 | 1100.78 | 26.69 | 2847871 |
| 2017-11-18 | 1443.02 | 174.24 | 1443.02 | 174.24 | 9060443 |
| 2012-08-07 | 1116.46 | 1209.97 | 1209.97 | 1116.46 | 1707720 |
| 2020-04-25 | 1392.9 | 607.06 | 1473.35 | 119.8 | 8393220 |
<end>Here's some yml data, can you convert it to Csv?
- Distance (miles): 2080.7
  Fuel Used (gallons): 7.4
  Start Location: San Francisco
  Trip Name: Highway Odyssey
- Distance (miles): 1000.2
  Fuel Used (gallons): 75.3
  Start Location: Houston
  Trip Name: Historic Route
- Distance (miles): 2072.1
  Fuel Used (gallons): 62.4
  Start Location: San Francisco
  Trip Name: Forest Journey
- Distance (miles): 839.8
  Fuel Used (gallons): 62.8
  Start Location: Chicago
  Trip Name: Highway Odyssey
- Distance (miles): 550.0
  Fuel Used (gallons): 17.6
  Start Location: Los Angeles
  Trip Name: City Explorer
- Distance (miles): 2845.3
  Fuel Used (gallons): 60.6
  Start Location: Denver
  Trip Name: Highway Odyssey
<start>
Trip Name,Start Location,Distance (miles),Fuel Used (gallons)
Highway Odyssey,San Francisco,2080.7,7.4
Historic Route,Houston,1000.2,75.3
Forest Journey,San Francisco,2072.1,62.4
Highway Odyssey,Chicago,839.8,62.8
City Explorer,Los Angeles,550.0,17.6
Highway Odyssey,Denver,2845.3,60.6
<end>Here's some yaml data, can you convert it to JSON?
- Cuisine: French
  Location: Los Angeles
  Price Range: $$$$
  Rating: 5
  Restaurant Name: Curry Corner
- Cuisine: French
  Location: San Francisco
  Price Range: $
  Rating: 3
  Restaurant Name: Burger Haven
- Cuisine: Mediterranean
  Location: Miami
  Price Range: $$$
  Rating: 3
  Restaurant Name: Taco Town
- Cuisine: Indian
  Location: Chicago
  Price Range: $
  Rating: 3
  Restaurant Name: The Golden Spoon
- Cuisine: Italian
  Location: New York
  Price Range: $$
  Rating: 4
  Restaurant Name: Pasta Palace
<start>
[
    {
        "Restaurant Name": "Curry Corner",
        "Cuisine": "French",
        "Location": "Los Angeles",
        "Rating": 5,
        "Price Range": "$$$$"
    },
    {
        "Restaurant Name": "Burger Haven",
        "Cuisine": "French",
        "Location": "San Francisco",
        "Rating": 3,
        "Price Range": "$"
    },
    {
        "Restaurant Name": "Taco Town",
        "Cuisine": "Mediterranean",
        "Location": "Miami",
        "Rating": 3,
        "Price Range": "$$$"
    },
    {
        "Restaurant Name": "The Golden Spoon",
        "Cuisine": "Indian",
        "Location": "Chicago",
        "Rating": 3,
        "Price Range": "$"
    },
    {
        "Restaurant Name": "Pasta Palace",
        "Cuisine": "Italian",
        "Location": "New York",
        "Rating": 4,
        "Price Range": "$$"
    }
]
<end>Can you change this csv into JSON?
Name,Age,Birth Month,City,Income
Todd,38,November,Washington,190000
Katrina,53,May,Los Angeles,135000
Mila,64,September,Memphis,245000
<start>
[
    {
        "Name": "Todd",
        "Age": 38,
        "Birth Month": "November",
        "City": "Washington",
        "Income": 190000
    },
    {
        "Name": "Katrina",
        "Age": 53,
        "Birth Month": "May",
        "City": "Los Angeles",
        "Income": 135000
    },
    {
        "Name": "Mila",
        "Age": 64,
        "Birth Month": "September",
        "City": "Memphis",
        "Income": 245000
    }
]
<end>Can you change this json into yaml?
[
    {
        "Company": "BioPharm",
        "Sector": "Healthcare",
        "Market Cap": "Large Cap",
        "Stock Price": 409.52,
        "Annual Revenue (B)": 291.18,
        "Quarter": "Q2"
    },
    {
        "Company": "TechCorp",
        "Sector": "Aerospace",
        "Market Cap": "Mega Cap",
        "Stock Price": 367.0,
        "Annual Revenue (B)": 437.3,
        "Quarter": "Q4"
    },
    {
        "Company": "GlobalTrade",
        "Sector": "Biotech",
        "Market Cap": "Mid Cap",
        "Stock Price": 772.36,
        "Annual Revenue (B)": 310.93,
        "Quarter": "Q3"
    },
    {
        "Company": "BioPharm",
        "Sector": "Biotech",
        "Market Cap": "Large Cap",
        "Stock Price": 728.24,
        "Annual Revenue (B)": 494.05,
        "Quarter": "Q4"
    },
    {
        "Company": "AutoDrive",
        "Sector": "Automotive",
        "Market Cap": "Mid Cap",
        "Stock Price": 368.4,
        "Annual Revenue (B)": 310.93,
        "Quarter": "Q2"
    },
    {
        "Company": "AutoDrive",
        "Sector": "Technology",
        "Market Cap": "Large Cap",
        "Stock Price": 894.35,
        "Annual Revenue (B)": 180.19,
        "Quarter": "Q2"
    },
    {
        "Company": "FinanceWorks",
        "Sector": "Technology",
        "Market Cap": "Small Cap",
        "Stock Price": 229.91,
        "Annual Revenue (B)": 109.66,
        "Quarter": "Q3"
    },
    {
        "Company": "AutoDrive",
        "Sector": "Biotech",
        "Market Cap": "Small Cap",
        "Stock Price": 321.0,
        "Annual Revenue (B)": 265.58,
        "Quarter": "Q3"
    },
    {
        "Company": "HealthPlus",
        "Sector": "Automotive",
        "Market Cap": "Mega Cap",
        "Stock Price": 890.04,
        "Annual Revenue (B)": 218.56,
        "Quarter": "Q2"
    },
    {
        "Company": "RetailHub",
        "Sector": "Retail",
        "Market Cap": "Large Cap",
        "Stock Price": 404.92,
        "Annual Revenue (B)": 55.7,
        "Quarter": "Q2"
    }
]<start>
- Annual Revenue (B): 291.18
  Company: BioPharm
  Market Cap: Large Cap
  Quarter: Q2
  Sector: Healthcare
  Stock Price: 409.52
- Annual Revenue (B): 437.3
  Company: TechCorp
  Market Cap: Mega Cap
  Quarter: Q4
  Sector: Aerospace
  Stock Price: 367.0
- Annual Revenue (B): 310.93
  Company: GlobalTrade
  Market Cap: Mid Cap
  Quarter: Q3
  Sector: Biotech
  Stock Price: 772.36
- Annual Revenue (B): 494.05
  Company: BioPharm
  Market Cap: Large Cap
  Quarter: Q4
  Sector: Biotech
  Stock Price: 728.24
- Annual Revenue (B): 310.93
  Company: AutoDrive
  Market Cap: Mid Cap
  Quarter: Q2
  Sector: Automotive
  Stock Price: 368.4
- Annual Revenue (B): 180.19
  Company: AutoDrive
  Market Cap: Large Cap
  Quarter: Q2
  Sector: Technology
  Stock Price: 894.35
- Annual Revenue (B): 109.66
  Company: FinanceWorks
  Market Cap: Small Cap
  Quarter: Q3
  Sector: Technology
  Stock Price: 229.91
- Annual Revenue (B): 265.58
  Company: AutoDrive
  Market Cap: Small Cap
  Quarter: Q3
  Sector: Biotech
  Stock Price: 321.0
- Annual Revenue (B): 218.56
  Company: HealthPlus
  Market Cap: Mega Cap
  Quarter: Q2
  Sector: Automotive
  Stock Price: 890.04
- Annual Revenue (B): 55.7
  Company: RetailHub
  Market Cap: Large Cap
  Quarter: Q2
  Sector: Retail
  Stock Price: 404.92
<end>Please transform the following markdown data into plain text:
| Restaurant Name | Cuisine |
| --- | --- |
| Pizza Planet | French |
| The Golden Spoon | American |
| Curry Corner | Indian |
| Vegan Delight | Mediterranean |
| The Golden Spoon | Mediterranean |
| BBQ Barn | Mediterranean |
| Taco Town | Mediterranean |
| Burger Haven | Indian |<start>
Restaurant Name: Pizza Planet | Cuisine: French
Restaurant Name: The Golden Spoon | Cuisine: American
Restaurant Name: Curry Corner | Cuisine: Indian
Restaurant Name: Vegan Delight | Cuisine: Mediterranean
Restaurant Name: The Golden Spoon | Cuisine: Mediterranean
Restaurant Name: BBQ Barn | Cuisine: Mediterranean
Restaurant Name: Taco Town | Cuisine: Mediterranean
Restaurant Name: Burger Haven | Cuisine: Indian
<end>Convert this YAML to Plain text:
- Cuisine: Mexican
  Location: New York
  Price Range: $
  Rating: 5
  Restaurant Name: BBQ Barn
- Cuisine: American
  Location: New York
  Price Range: $$$$
  Rating: 4
  Restaurant Name: The Golden Spoon
- Cuisine: Chinese
  Location: New York
  Price Range: $
  Rating: 2
  Restaurant Name: The Golden Spoon
- Cuisine: Italian
  Location: Phoenix
  Price Range: $$$
  Rating: 2
  Restaurant Name: The Steakhouse
- Cuisine: Mediterranean
  Location: Seattle
  Price Range: $$
  Rating: 1
  Restaurant Name: Curry Corner
- Cuisine: Chinese
  Location: Phoenix
  Price Range: $$$$$
  Rating: 1
  Restaurant Name: Curry Corner
- Cuisine: American
  Location: Seattle
  Price Range: $$$$
  Rating: 2
  Restaurant Name: The Steakhouse
- Cuisine: Japanese
  Location: New York
  Price Range: $
  Rating: 4
  Restaurant Name: Vegan Delight
- Cuisine: Chinese
  Location: Chicago
  Price Range: $$$
  Rating: 1
  Restaurant Name: Pizza Planet
<start>
Restaurant Name: BBQ Barn | Cuisine: Mexican | Location: New York | Rating: 5 | Price Range: $
Restaurant Name: The Golden Spoon | Cuisine: American | Location: New York | Rating: 4 | Price Range: $$$$
Restaurant Name: The Golden Spoon | Cuisine: Chinese | Location: New York | Rating: 2 | Price Range: $
Restaurant Name: The Steakhouse | Cuisine: Italian | Location: Phoenix | Rating: 2 | Price Range: $$$
Restaurant Name: Curry Corner | Cuisine: Mediterranean | Location: Seattle | Rating: 1 | Price Range: $$
Restaurant Name: Curry Corner | Cuisine: Chinese | Location: Phoenix | Rating: 1 | Price Range: $$$$$
Restaurant Name: The Steakhouse | Cuisine: American | Location: Seattle | Rating: 2 | Price Range: $$$$
Restaurant Name: Vegan Delight | Cuisine: Japanese | Location: New York | Rating: 4 | Price Range: $
Restaurant Name: Pizza Planet | Cuisine: Chinese | Location: Chicago | Rating: 1 | Price Range: $$$
<end>Please transform the following CSV data into YML:
Device ID,Device Type,Location,Battery Level (%),Reading Value,Timestamp
device-0088,Pressure Sensor,Kitchen,10.5,-3.01,2021-08-28 06:28:04
device-0004,Pressure Sensor,Kitchen,12.3,-15.36,2023-06-19 04:31:17
device-0061,Temperature Sensor,Kitchen,59.7,4.57,2023-03-26 12:59:22
device-0037,Light Sensor,Bathroom,15.1,-15.36,2023-12-09 02:17:54
device-0072,Light Sensor,Bedroom,27.8,-37.73,2022-12-17 14:23:23
device-0032,Light Sensor,Garage,59.7,25.19,2021-07-07 08:32:35
device-0095,Humidity Sensor,Bathroom,76.0,83.9,2021-11-11 00:42:35
<start>
- Battery Level (%): 10.5
  Device ID: device-0088
  Device Type: Pressure Sensor
  Location: Kitchen
  Reading Value: -3.01
  Timestamp: '2021-08-28 06:28:04'
- Battery Level (%): 12.3
  Device ID: device-0004
  Device Type: Pressure Sensor
  Location: Kitchen
  Reading Value: -15.36
  Timestamp: '2023-06-19 04:31:17'
- Battery Level (%): 59.7
  Device ID: device-0061
  Device Type: Temperature Sensor
  Location: Kitchen
  Reading Value: 4.57
  Timestamp: '2023-03-26 12:59:22'
- Battery Level (%): 15.1
  Device ID: device-0037
  Device Type: Light Sensor
  Location: Bathroom
  Reading Value: -15.36
  Timestamp: '2023-12-09 02:17:54'
- Battery Level (%): 27.8
  Device ID: device-0072
  Device Type: Light Sensor
  Location: Bedroom
  Reading Value: -37.73
  Timestamp: '2022-12-17 14:23:23'
- Battery Level (%): 59.7
  Device ID: device-0032
  Device Type: Light Sensor
  Location: Garage
  Reading Value: 25.19
  Timestamp: '2021-07-07 08:32:35'
- Battery Level (%): 76.0
  Device ID: device-0095
  Device Type: Humidity Sensor
  Location: Bathroom
  Reading Value: 83.9
  Timestamp: '2021-11-11 00:42:35'
<end>Can you change this markdown into csv?
| SKU | Price | Stock Quantity | Supplier Name |
| --- | --- | --- | --- |
| SKU-1065 | 477.96 | 202 | Globex |
| SKU-1031 | 281.44 | 432 | Wayne Enterprises |
| SKU-1007 | 201.14 | 204 | Wayne Enterprises |<start>
SKU,Price,Stock Quantity,Supplier Name
SKU-1065,477.96,202,Globex
SKU-1031,281.44,432,Wayne Enterprises
SKU-1007,201.14,204,Wayne Enterprises
<end>Can you change this JSON into yaml?
[
    {
        "Location": "Phoenix",
        "Temperature (C)": 29.1,
        "Humidity (%)": 40,
        "Wind Speed (km/h)": 15.2
    },
    {
        "Location": "Seattle",
        "Temperature (C)": 28.7,
        "Humidity (%)": 27,
        "Wind Speed (km/h)": 0.4
    },
    {
        "Location": "Houston",
        "Temperature (C)": -2.1,
        "Humidity (%)": 93,
        "Wind Speed (km/h)": 15.9
    },
    {
        "Location": "Miami",
        "Temperature (C)": 34.8,
        "Humidity (%)": 70,
        "Wind Speed (km/h)": 28.7
    },
    {
        "Location": "Seattle",
        "Temperature (C)": 32.3,
        "Humidity (%)": 84,
        "Wind Speed (km/h)": 9.9
    },
    {
        "Location": "Phoenix",
        "Temperature (C)": 5.3,
        "Humidity (%)": 30,
        "Wind Speed (km/h)": 8.6
    },
    {
        "Location": "Seattle",
        "Temperature (C)": 23.9,
        "Humidity (%)": 86,
        "Wind Speed (km/h)": 24.2
    }
]<start>
- Humidity (%): 40
  Location: Phoenix
  Temperature (C): 29.1
  Wind Speed (km/h): 15.2
- Humidity (%): 27
  Location: Seattle
  Temperature (C): 28.7
  Wind Speed (km/h): 0.4
- Humidity (%): 93
  Location: Houston
  Temperature (C): -2.1
  Wind Speed (km/h): 15.9
- Humidity (%): 70
  Location: Miami
  Temperature (C): 34.8
  Wind Speed (km/h): 28.7
- Humidity (%): 84
  Location: Seattle
  Temperature (C): 32.3
  Wind Speed (km/h): 9.9
- Humidity (%): 30
  Location: Phoenix
  Temperature (C): 5.3
  Wind Speed (km/h): 8.6
- Humidity (%): 86
  Location: Seattle
  Temperature (C): 23.9
  Wind Speed (km/h): 24.2
<end>Can you change this Csv into Plain text?
Restaurant Name,Cuisine,Rating,Price Range
Burger Haven,American,5,$
Taco Town,American,4,$$$$
Sushi World,Mediterranean,3,$
Sushi World,Italian,5,$$$$
Taco Town,Mediterranean,3,$$
The Golden Spoon,French,4,$$$
Burger Haven,Mediterranean,4,$$$$
<start>
Restaurant Name: Burger Haven | Cuisine: American | Rating: 5 | Price Range: $
Restaurant Name: Taco Town | Cuisine: American | Rating: 4 | Price Range: $$$$
Restaurant Name: Sushi World | Cuisine: Mediterranean | Rating: 3 | Price Range: $
Restaurant Name: Sushi World | Cuisine: Italian | Rating: 5 | Price Range: $$$$
Restaurant Name: Taco Town | Cuisine: Mediterranean | Rating: 3 | Price Range: $$
Restaurant Name: The Golden Spoon | Cuisine: French | Rating: 4 | Price Range: $$$
Restaurant Name: Burger Haven | Cuisine: Mediterranean | Rating: 4 | Price Range: $$$$
<end>Here's some MARKDOWN data, can you convert it to yml?
| Location | Rating | Price Range |
| --- | --- | --- |
| Houston | 3 | $$ |
| Houston | 1 | $$$$$ |
| San Francisco | 5 | $ |
| Houston | 3 | $ |<start>
- Location: Houston
  Price Range: $$
  Rating: 3
- Location: Houston
  Price Range: $$$$$
  Rating: 1
- Location: San Francisco
  Price Range: $
  Rating: 5
- Location: Houston
  Price Range: $
  Rating: 3
<end>Transform this Csv structure to a plain text format:
Product Name,Price,Stock Quantity,Supplier Name
Widget,68.22,234,Umbrella Corp
Gizmo,436.51,142,Wonka Industries
Gizmo,334.12,314,Umbrella Corp
Contraption,330.74,138,Globex
Device,213.36,19,ACME Corp
Instrument,183.33,64,Umbrella Corp
Device,321.06,402,ACME Corp
<start>
Product Name: Widget | Price: 68.22 | Stock Quantity: 234 | Supplier Name: Umbrella Corp
Product Name: Gizmo | Price: 436.51 | Stock Quantity: 142 | Supplier Name: Wonka Industries
Product Name: Gizmo | Price: 334.12 | Stock Quantity: 314 | Supplier Name: Umbrella Corp
Product Name: Contraption | Price: 330.74 | Stock Quantity: 138 | Supplier Name: Globex
Product Name: Device | Price: 213.36 | Stock Quantity: 19 | Supplier Name: ACME Corp
Product Name: Instrument | Price: 183.33 | Stock Quantity: 64 | Supplier Name: Umbrella Corp
Product Name: Device | Price: 321.06 | Stock Quantity: 402 | Supplier Name: ACME Corp
<end>Here's some csv data, can you convert it to plain text?
Device ID,Device Type,Location,Battery Level (%)
device-0013,Humidity Sensor,Garage,16.6
device-0061,Light Sensor,Living Room,17.0
device-0090,Light Sensor,Living Room,25.7
device-0029,Light Sensor,Hallway,96.5
device-0099,Temperature Sensor,Bathroom,60.5
device-0093,Motion Detector,Garden,94.2
device-0021,Light Sensor,Hallway,65.0
device-0026,Light Sensor,Hallway,94.2
device-0083,Pressure Sensor,Office,40.7
<start>
Device ID: device-0013 | Device Type: Humidity Sensor | Location: Garage | Battery Level (%): 16.6
Device ID: device-0061 | Device Type: Light Sensor | Location: Living Room | Battery Level (%): 17.0
Device ID: device-0090 | Device Type: Light Sensor | Location: Living Room | Battery Level (%): 25.7
Device ID: device-0029 | Device Type: Light Sensor | Location: Hallway | Battery Level (%): 96.5
Device ID: device-0099 | Device Type: Temperature Sensor | Location: Bathroom | Battery Level (%): 60.5
Device ID: device-0093 | Device Type: Motion Detector | Location: Garden | Battery Level (%): 94.2
Device ID: device-0021 | Device Type: Light Sensor | Location: Hallway | Battery Level (%): 65.0
Device ID: device-0026 | Device Type: Light Sensor | Location: Hallway | Battery Level (%): 94.2
Device ID: device-0083 | Device Type: Pressure Sensor | Location: Office | Battery Level (%): 40.7
<end>Please transform the following yaml data into Markdown:
- Average Latency (ms): 32.0
  Cache Hit Ratio (%): 77.29
  Connection Count: 168
  Queries per Second: 673.34
- Average Latency (ms): 28.76
  Cache Hit Ratio (%): 99.53
  Connection Count: 178
  Queries per Second: 2876.98
- Average Latency (ms): 32.66
  Cache Hit Ratio (%): 91.26
  Connection Count: 103
  Queries per Second: 627.53
- Average Latency (ms): 88.63
  Cache Hit Ratio (%): 81.89
  Connection Count: 417
  Queries per Second: 2013.53
<start>
| Queries per Second | Cache Hit Ratio (%) | Connection Count | Average Latency (ms) |
| --- | --- | --- | --- |
| 673.34 | 77.29 | 168 | 32.0 |
| 2876.98 | 99.53 | 178 | 28.76 |
| 627.53 | 91.26 | 103 | 32.66 |
| 2013.53 | 81.89 | 417 | 88.63 |
<end>Please transform the following csv data into PLAIN TEXT:
Device ID,Battery Level (%),Reading Value,Timestamp
device-0100,14.8,8.72,2022-11-11 06:28:30
device-0069,35.5,-35.25,2021-12-19 16:20:05
device-0023,20.6,-13.98,2021-02-27 01:24:27
device-0042,26.2,-7.66,2023-11-15 04:37:02
device-0098,94.2,70.23,2022-07-11 19:30:01
device-0057,89.9,47.17,2022-09-09 02:41:50
device-0050,49.0,1.0,2022-08-03 09:26:26
device-0035,63.8,-13.27,2023-05-17 04:55:53
<start>
Device ID: device-0100 | Battery Level (%): 14.8 | Reading Value: 8.72 | Timestamp: 2022-11-11 06:28:30
Device ID: device-0069 | Battery Level (%): 35.5 | Reading Value: -35.25 | Timestamp: 2021-12-19 16:20:05
Device ID: device-0023 | Battery Level (%): 20.6 | Reading Value: -13.98 | Timestamp: 2021-02-27 01:24:27
Device ID: device-0042 | Battery Level (%): 26.2 | Reading Value: -7.66 | Timestamp: 2023-11-15 04:37:02
Device ID: device-0098 | Battery Level (%): 94.2 | Reading Value: 70.23 | Timestamp: 2022-07-11 19:30:01
Device ID: device-0057 | Battery Level (%): 89.9 | Reading Value: 47.17 | Timestamp: 2022-09-09 02:41:50
Device ID: device-0050 | Battery Level (%): 49.0 | Reading Value: 1.0 | Timestamp: 2022-08-03 09:26:26
Device ID: device-0035 | Battery Level (%): 63.8 | Reading Value: -13.27 | Timestamp: 2023-05-17 04:55:53
<end>Please transform the following json data into csv:
[
    {
        "Company": "RetailWorld",
        "Date": "2021-05-19",
        "Open Price": 128.19,
        "Close Price": 1498.86,
        "High Price": 1498.86,
        "Low Price": 105.4,
        "Volume": 6765677
    },
    {
        "Company": "AeroSystems",
        "Date": "2010-06-05",
        "Open Price": 1015.43,
        "Close Price": 1423.6,
        "High Price": 1423.6,
        "Low Price": 1015.43,
        "Volume": 3789796
    },
    {
        "Company": "HealthGen",
        "Date": "2018-04-09",
        "Open Price": 1365.31,
        "Close Price": 874.57,
        "High Price": 1403.4,
        "Low Price": 621.46,
        "Volume": 7289945
    },
    {
        "Company": "MediaGroup",
        "Date": "2013-02-23",
        "Open Price": 1288.31,
        "Close Price": 481.31,
        "High Price": 1288.31,
        "Low Price": 444.61,
        "Volume": 2494621
    }
]<start>
Company,Date,Open Price,Close Price,High Price,Low Price,Volume
RetailWorld,2021-05-19,128.19,1498.86,1498.86,105.4,6765677
AeroSystems,2010-06-05,1015.43,1423.6,1423.6,1015.43,3789796
HealthGen,2018-04-09,1365.31,874.57,1403.4,621.46,7289945
MediaGroup,2013-02-23,1288.31,481.31,1288.31,444.61,2494621
<end>Here's some YML data, can you convert it to csv?
- Condition: Stormy
  Day: Sunday
  Humidity (%): 36
  Location: Los Angeles
  Wind Speed (km/h): 20.9
- Condition: Snowy
  Day: Monday
  Humidity (%): 30
  Location: Denver
  Wind Speed (km/h): 12.0
- Condition: Stormy
  Day: Tuesday
  Humidity (%): 93
  Location: Los Angeles
  Wind Speed (km/h): 10.0
<start>
Location,Condition,Humidity (%),Wind Speed (km/h),Day
Los Angeles,Stormy,36,20.9,Sunday
Denver,Snowy,30,12.0,Monday
Los Angeles,Stormy,93,10.0,Tuesday
<end>Convert this json to csv:
[
    {
        "Company": "FoodChain",
        "Open Price": 883.5,
        "Close Price": 1021.86,
        "High Price": 1021.86,
        "Low Price": 883.5,
        "Volume": 7285310
    },
    {
        "Company": "FoodChain",
        "Open Price": 1345.97,
        "Close Price": 127.52,
        "High Price": 1345.97,
        "Low Price": 127.52,
        "Volume": 457160
    },
    {
        "Company": "HealthGen",
        "Open Price": 68.4,
        "Close Price": 139.98,
        "High Price": 1109.67,
        "Low Price": 68.4,
        "Volume": 4644692
    }
]<start>
Company,Open Price,Close Price,High Price,Low Price,Volume
FoodChain,883.5,1021.86,1021.86,883.5,7285310
FoodChain,1345.97,127.52,1345.97,127.52,457160
HealthGen,68.4,139.98,1109.67,68.4,4644692
<end>Transform this Markdown structure to a JSON format:
| Birth Month | Income |
| --- | --- |
| June | 295000 |
| September | 265000 |
| March | 145000 |
| October | 300000 |
| November | 30000 |
| December | 245000 |
| October | 240000 |
| June | 410000 |<start>
[
    {
        "Birth Month": "June",
        "Income": 295000
    },
    {
        "Birth Month": "September",
        "Income": 265000
    },
    {
        "Birth Month": "March",
        "Income": 145000
    },
    {
        "Birth Month": "October",
        "Income": 300000
    },
    {
        "Birth Month": "November",
        "Income": 30000
    },
    {
        "Birth Month": "December",
        "Income": 245000
    },
    {
        "Birth Month": "October",
        "Income": 240000
    },
    {
        "Birth Month": "June",
        "Income": 410000
    }
]
<end>Can you change this MARKDOWN into JSON?
| Restaurant Name | Cuisine | Location |
| --- | --- | --- |
| Taco Town | Japanese | Phoenix |
| Sushi World | Mediterranean | Chicago |
| Burger Haven | Indian | San Francisco |
| The Golden Spoon | Japanese | Seattle |<start>
[
    {
        "Restaurant Name": "Taco Town",
        "Cuisine": "Japanese",
        "Location": "Phoenix"
    },
    {
        "Restaurant Name": "Sushi World",
        "Cuisine": "Mediterranean",
        "Location": "Chicago"
    },
    {
        "Restaurant Name": "Burger Haven",
        "Cuisine": "Indian",
        "Location": "San Francisco"
    },
    {
        "Restaurant Name": "The Golden Spoon",
        "Cuisine": "Japanese",
        "Location": "Seattle"
    }
]
<end>Can you change this markdown into json?
| Location | Rating | Price Range |
| --- | --- | --- |
| San Francisco | 4 | $$ |
| Miami | 4 | $$$$ |
| New York | 4 | $ |<start>
[
    {
        "Location": "San Francisco",
        "Rating": 4,
        "Price Range": "$$"
    },
    {
        "Location": "Miami",
        "Rating": 4,
        "Price Range": "$$$$"
    },
    {
        "Location": "New York",
        "Rating": 4,
        "Price Range": "$"
    }
]
<end>Convert this yaml to plain text:
- Average Latency (ms): 35.61
  Cache Hit Ratio (%): 81.97
  Database Name: SessionsDB
  Queries per Second: 3680.72
  Timestamp: '2023-05-28 21:49:46'
- Average Latency (ms): 18.04
  Cache Hit Ratio (%): 77.92
  Database Name: ProfilesDB
  Queries per Second: 2130.0
  Timestamp: '2022-12-15 13:17:51'
- Average Latency (ms): 68.65
  Cache Hit Ratio (%): 89.96
  Database Name: SalesDB
  Queries per Second: 4142.34
  Timestamp: '2022-09-26 19:10:09'
- Average Latency (ms): 49.29
  Cache Hit Ratio (%): 77.92
  Database Name: MetricsDB
  Queries per Second: 2825.0
  Timestamp: '2021-03-02 06:06:17'
- Average Latency (ms): 25.0
  Cache Hit Ratio (%): 86.54
  Database Name: SalesDB
  Queries per Second: 662.05
  Timestamp: '2023-03-03 16:00:20'
- Average Latency (ms): 92.15
  Cache Hit Ratio (%): 77.92
  Database Name: InventoryDB
  Queries per Second: 3160.86
  Timestamp: '2021-05-10 17:57:18'
- Average Latency (ms): 18.04
  Cache Hit Ratio (%): 84.98
  Database Name: SalesDB
  Queries per Second: 1097.45
  Timestamp: '2023-12-14 19:08:09'
- Average Latency (ms): 49.29
  Cache Hit Ratio (%): 77.98
  Database Name: SessionsDB
  Queries per Second: 4541.73
  Timestamp: '2023-09-08 08:25:55'
- Average Latency (ms): 42.36
  Cache Hit Ratio (%): 92.1
  Database Name: AnalyticsDB
  Queries per Second: 3794.98
  Timestamp: '2023-10-20 19:47:07'
- Average Latency (ms): 41.09
  Cache Hit Ratio (%): 76.21
  Database Name: AnalyticsDB
  Queries per Second: 2792.68
  Timestamp: '2021-07-25 17:04:00'
<start>
Database Name: SessionsDB | Queries per Second: 3680.72 | Cache Hit Ratio (%): 81.97 | Average Latency (ms): 35.61 | Timestamp: 2023-05-28 21:49:46
Database Name: ProfilesDB | Queries per Second: 2130.0 | Cache Hit Ratio (%): 77.92 | Average Latency (ms): 18.04 | Timestamp: 2022-12-15 13:17:51
Database Name: SalesDB | Queries per Second: 4142.34 | Cache Hit Ratio (%): 89.96 | Average Latency (ms): 68.65 | Timestamp: 2022-09-26 19:10:09
Database Name: MetricsDB | Queries per Second: 2825.0 | Cache Hit Ratio (%): 77.92 | Average Latency (ms): 49.29 | Timestamp: 2021-03-02 06:06:17
Database Name: SalesDB | Queries per Second: 662.05 | Cache Hit Ratio (%): 86.54 | Average Latency (ms): 25.0 | Timestamp: 2023-03-03 16:00:20
Database Name: InventoryDB | Queries per Second: 3160.86 | Cache Hit Ratio (%): 77.92 | Average Latency (ms): 92.15 | Timestamp: 2021-05-10 17:57:18
Database Name: SalesDB | Queries per Second: 1097.45 | Cache Hit Ratio (%): 84.98 | Average Latency (ms): 18.04 | Timestamp: 2023-12-14 19:08:09
Database Name: SessionsDB | Queries per Second: 4541.73 | Cache Hit Ratio (%): 77.98 | Average Latency (ms): 49.29 | Timestamp: 2023-09-08 08:25:55
Database Name: AnalyticsDB | Queries per Second: 3794.98 | Cache Hit Ratio (%): 92.1 | Average Latency (ms): 42.36 | Timestamp: 2023-10-20 19:47:07
Database Name: AnalyticsDB | Queries per Second: 2792.68 | Cache Hit Ratio (%): 76.21 | Average Latency (ms): 41.09 | Timestamp: 2021-07-25 17:04:00
<end>Transform this Markdown structure to a Json format:
| Condition | Temperature (C) | Humidity (%) | Wind Speed (km/h) | Day |
| --- | --- | --- | --- | --- |
| Sunny | 29.8 | 46 | 9.8 | Friday |
| Windy | 13.8 | 88 | 26.8 | Monday |
| Windy | 15.4 | 62 | 10.9 | Saturday |<start>
[
    {
        "Condition": "Sunny",
        "Temperature (C)": 29.8,
        "Humidity (%)": 46,
        "Wind Speed (km/h)": 9.8,
        "Day": "Friday"
    },
    {
        "Condition": "Windy",
        "Temperature (C)": 13.8,
        "Humidity (%)": 88,
        "Wind Speed (km/h)": 26.8,
        "Day": "Monday"
    },
    {
        "Condition": "Windy",
        "Temperature (C)": 15.4,
        "Humidity (%)": 62,
        "Wind Speed (km/h)": 10.9,
        "Day": "Saturday"
    }
]
<end>Can you change this json into plain text?
[
    {
        "Title": "Legends of the Rift",
        "Genre": "Fantasy",
        "Rating": 1.3
    },
    {
        "Title": "Echoes of Eternity",
        "Genre": "Fantasy",
        "Rating": 4.4
    },
    {
        "Title": "Whispers of the Abyss",
        "Genre": "Horror",
        "Rating": 1.3
    },
    {
        "Title": "Echoes of Eternity",
        "Genre": "Science Fiction",
        "Rating": 4.5
    },
    {
        "Title": "Tales of the Brave",
        "Genre": "Non-Fiction",
        "Rating": 4.4
    },
    {
        "Title": "Tales of the Brave",
        "Genre": "Mystery",
        "Rating": 3.6
    },
    {
        "Title": "The Crystal Key",
        "Genre": "Thriller",
        "Rating": 3.2
    }
]<start>
Title: Legends of the Rift | Genre: Fantasy | Rating: 1.3
Title: Echoes of Eternity | Genre: Fantasy | Rating: 4.4
Title: Whispers of the Abyss | Genre: Horror | Rating: 1.3
Title: Echoes of Eternity | Genre: Science Fiction | Rating: 4.5
Title: Tales of the Brave | Genre: Non-Fiction | Rating: 4.4
Title: Tales of the Brave | Genre: Mystery | Rating: 3.6
Title: The Crystal Key | Genre: Thriller | Rating: 3.2
<end>Transform this json structure to a MARKDOWN format:
[
    {
        "Cuisine": "Mexican",
        "Location": "San Francisco",
        "Rating": 3
    },
    {
        "Cuisine": "Mexican",
        "Location": "Houston",
        "Rating": 2
    },
    {
        "Cuisine": "Chinese",
        "Location": "Los Angeles",
        "Rating": 1
    },
    {
        "Cuisine": "Mediterranean",
        "Location": "Phoenix",
        "Rating": 3
    },
    {
        "Cuisine": "Japanese",
        "Location": "Chicago",
        "Rating": 3
    },
    {
        "Cuisine": "French",
        "Location": "San Francisco",
        "Rating": 2
    },
    {
        "Cuisine": "Japanese",
        "Location": "New York",
        "Rating": 3
    }
]<start>
| Cuisine | Location | Rating |
| --- | --- | --- |
| Mexican | San Francisco | 3 |
| Mexican | Houston | 2 |
| Chinese | Los Angeles | 1 |
| Mediterranean | Phoenix | 3 |
| Japanese | Chicago | 3 |
| French | San Francisco | 2 |
| Japanese | New York | 3 |
<end>Can you change this csv into PLAIN TEXT?
Company,Sector,Stock Price
AutoDrive,Healthcare,832.35
FinanceWorks,Aerospace,947.12
BioPharm,Aerospace,733.96
HealthPlus,Biotech,107.55
HealthPlus,Technology,881.6
<start>
Company: AutoDrive | Sector: Healthcare | Stock Price: 832.35
Company: FinanceWorks | Sector: Aerospace | Stock Price: 947.12
Company: BioPharm | Sector: Aerospace | Stock Price: 733.96
Company: HealthPlus | Sector: Biotech | Stock Price: 107.55
Company: HealthPlus | Sector: Technology | Stock Price: 881.6
<end>Here's some PLAIN TEXT data, can you convert it to yaml?
Cache Hit Ratio (%): 97.69 | Average Latency (ms): 14.38 | Timestamp: 2021-06-01 10:53:45
Cache Hit Ratio (%): 79.99 | Average Latency (ms): 38.88 | Timestamp: 2022-06-24 08:41:39
Cache Hit Ratio (%): 99.62 | Average Latency (ms): 41.79 | Timestamp: 2021-09-28 04:21:58
Cache Hit Ratio (%): 89.85 | Average Latency (ms): 87.37 | Timestamp: 2023-02-07 22:34:05
Cache Hit Ratio (%): 81.37 | Average Latency (ms): 42.58 | Timestamp: 2021-10-13 23:37:41
Cache Hit Ratio (%): 85.16 | Average Latency (ms): 32.73 | Timestamp: 2023-07-27 08:34:42
Cache Hit Ratio (%): 92.73 | Average Latency (ms): 34.38 | Timestamp: 2022-10-07 10:35:38
Cache Hit Ratio (%): 87.38 | Average Latency (ms): 79.67 | Timestamp: 2022-01-22 18:44:00
Cache Hit Ratio (%): 73.55 | Average Latency (ms): 70.86 | Timestamp: 2022-03-03 08:37:19
Cache Hit Ratio (%): 79.65 | Average Latency (ms): 93.35 | Timestamp: 2023-05-08 05:46:18
<start>
- Average Latency (ms): 14.38
  Cache Hit Ratio (%): 97.69
  Timestamp: '2021-06-01 10:53:45'
- Average Latency (ms): 38.88
  Cache Hit Ratio (%): 79.99
  Timestamp: '2022-06-24 08:41:39'
- Average Latency (ms): 41.79
  Cache Hit Ratio (%): 99.62
  Timestamp: '2021-09-28 04:21:58'
- Average Latency (ms): 87.37
  Cache Hit Ratio (%): 89.85
  Timestamp: '2023-02-07 22:34:05'
- Average Latency (ms): 42.58
  Cache Hit Ratio (%): 81.37
  Timestamp: '2021-10-13 23:37:41'
- Average Latency (ms): 32.73
  Cache Hit Ratio (%): 85.16
  Timestamp: '2023-07-27 08:34:42'
- Average Latency (ms): 34.38
  Cache Hit Ratio (%): 92.73
  Timestamp: '2022-10-07 10:35:38'
- Average Latency (ms): 79.67
  Cache Hit Ratio (%): 87.38
  Timestamp: '2022-01-22 18:44:00'
- Average Latency (ms): 70.86
  Cache Hit Ratio (%): 73.55
  Timestamp: '2022-03-03 08:37:19'
- Average Latency (ms): 93.35
  Cache Hit Ratio (%): 79.65
  Timestamp: '2023-05-08 05:46:18'
<end>Please transform the following JSON data into Csv:
[
    {
        "Temperature (C)": 39.2,
        "Humidity (%)": 29,
        "Wind Speed (km/h)": 27.3,
        "Day": "Friday"
    },
    {
        "Temperature (C)": 36.1,
        "Humidity (%)": 64,
        "Wind Speed (km/h)": 0.8,
        "Day": "Saturday"
    },
    {
        "Temperature (C)": 27.9,
        "Humidity (%)": 53,
        "Wind Speed (km/h)": 8.2,
        "Day": "Tuesday"
    },
    {
        "Temperature (C)": -9.4,
        "Humidity (%)": 60,
        "Wind Speed (km/h)": 5.7,
        "Day": "Wednesday"
    },
    {
        "Temperature (C)": 17.9,
        "Humidity (%)": 59,
        "Wind Speed (km/h)": 16.9,
        "Day": "Saturday"
    }
]<start>
Temperature (C),Humidity (%),Wind Speed (km/h),Day
39.2,29,27.3,Friday
36.1,64,0.8,Saturday
27.9,53,8.2,Tuesday
-9.4,60,5.7,Wednesday
17.9,59,16.9,Saturday
<end>Transform this MARKDOWN structure to a csv format:
| Title | Release Year | Box Office Earnings (M) |
| --- | --- | --- |
| Beyond the Veil | 1977 | 787.1 |
| The Great Expedition | 1976 | 349.08 |
| Escape from Earth | 1986 | 567.7 |
| Edge of Infinity | 1982 | 615.39 |
| Beyond the Veil | 2006 | 990.08 |
| Edge of Infinity | 2000 | 503.28 |
| Escape from Earth | 2010 | 257.92 |<start>
Title,Release Year,Box Office Earnings (M)
Beyond the Veil,1977,787.1
The Great Expedition,1976,349.08
Escape from Earth,1986,567.7
Edge of Infinity,1982,615.39
Beyond the Veil,2006,990.08
Edge of Infinity,2000,503.28
Escape from Earth,2010,257.92
<end>Please transform the following yaml data into json:
- Battery Level (%): 14.6
  Device ID: device-0045
  Device Type: Pressure Sensor
  Location: Garage
  Reading Value: 25.44
  Timestamp: '2021-08-18 11:56:46'
- Battery Level (%): 42.3
  Device ID: device-0075
  Device Type: Light Sensor
  Location: Living Room
  Reading Value: 39.23
  Timestamp: '2022-06-23 14:08:03'
- Battery Level (%): 77.1
  Device ID: device-0020
  Device Type: Temperature Sensor
  Location: Garage
  Reading Value: 16.04
  Timestamp: '2021-05-03 16:53:34'
- Battery Level (%): 32.6
  Device ID: device-0064
  Device Type: Humidity Sensor
  Location: Garage
  Reading Value: 21.33
  Timestamp: '2021-06-08 03:37:21'
- Battery Level (%): 64.0
  Device ID: device-0078
  Device Type: Humidity Sensor
  Location: Bathroom
  Reading Value: 69.41
  Timestamp: '2021-11-23 20:39:50'
<start>
[
    {
        "Device ID": "device-0045",
        "Device Type": "Pressure Sensor",
        "Location": "Garage",
        "Battery Level (%)": 14.6,
        "Reading Value": 25.44,
        "Timestamp": "2021-08-18 11:56:46"
    },
    {
        "Device ID": "device-0075",
        "Device Type": "Light Sensor",
        "Location": "Living Room",
        "Battery Level (%)": 42.3,
        "Reading Value": 39.23,
        "Timestamp": "2022-06-23 14:08:03"
    },
    {
        "Device ID": "device-0020",
        "Device Type": "Temperature Sensor",
        "Location": "Garage",
        "Battery Level (%)": 77.1,
        "Reading Value": 16.04,
        "Timestamp": "2021-05-03 16:53:34"
    },
    {
        "Device ID": "device-0064",
        "Device Type": "Humidity Sensor",
        "Location": "Garage",
        "Battery Level (%)": 32.6,
        "Reading Value": 21.33,
        "Timestamp": "2021-06-08 03:37:21"
    },
    {
        "Device ID": "device-0078",
        "Device Type": "Humidity Sensor",
        "Location": "Bathroom",
        "Battery Level (%)": 64.0,
        "Reading Value": 69.41,
        "Timestamp": "2021-11-23 20:39:50"
    }
]
<end>Can you change this markdown into Plain text?
| Title | Release Year |
| --- | --- |
| Starbound Odyssey | 2000 |
| Escape from Earth | 2010 |
| Starbound Odyssey | 2015 |
| The Final Voyage | 1980 |
| Escape from Earth | 2015 |
| Rise of the Titans | 1988 |
| Beyond the Veil | 1975 |
| Dreamwalker | 1992 |<start>
Title: Starbound Odyssey | Release Year: 2000
Title: Escape from Earth | Release Year: 2010
Title: Starbound Odyssey | Release Year: 2015
Title: The Final Voyage | Release Year: 1980
Title: Escape from Earth | Release Year: 2015
Title: Rise of the Titans | Release Year: 1988
Title: Beyond the Veil | Release Year: 1975
Title: Dreamwalker | Release Year: 1992
<end>Here's some csv data, can you convert it to Plain text?
Title,Director,Genre,Release Year,Box Office Earnings (M)
Mystery of the Depths,Orin Shadowalker,Horror,2023,982.77
The Great Expedition,Lira Silverleaf,Horror,2017,391.95
Mystery of the Depths,Orin Shadowalker,Comedy,2020,157.23
Rise of the Titans,Orin Shadowalker,Drama,1999,363.3
Mystery of the Depths,Mara Moonshadow,Comedy,2011,777.65
Starbound Odyssey,Lira Silverleaf,Adventure,1995,433.29
Edge of Infinity,Selene Darkwhisper,Drama,1996,922.56
The Great Expedition,Rylan Frostblade,Fantasy,1972,127.79
Starbound Odyssey,Lira Silverleaf,Fantasy,1985,417.91
<start>
Title: Mystery of the Depths | Director: Orin Shadowalker | Genre: Horror | Release Year: 2023 | Box Office Earnings (M): 982.77
Title: The Great Expedition | Director: Lira Silverleaf | Genre: Horror | Release Year: 2017 | Box Office Earnings (M): 391.95
Title: Mystery of the Depths | Director: Orin Shadowalker | Genre: Comedy | Release Year: 2020 | Box Office Earnings (M): 157.23
Title: Rise of the Titans | Director: Orin Shadowalker | Genre: Drama | Release Year: 1999 | Box Office Earnings (M): 363.3
Title: Mystery of the Depths | Director: Mara Moonshadow | Genre: Comedy | Release Year: 2011 | Box Office Earnings (M): 777.65
Title: Starbound Odyssey | Director: Lira Silverleaf | Genre: Adventure | Release Year: 1995 | Box Office Earnings (M): 433.29
Title: Edge of Infinity | Director: Selene Darkwhisper | Genre: Drama | Release Year: 1996 | Box Office Earnings (M): 922.56
Title: The Great Expedition | Director: Rylan Frostblade | Genre: Fantasy | Release Year: 1972 | Box Office Earnings (M): 127.79
Title: Starbound Odyssey | Director: Lira Silverleaf | Genre: Fantasy | Release Year: 1985 | Box Office Earnings (M): 417.91
<end>Here's some plain text data, can you convert it to csv?
Title: The Silent Grove | Genre: Horror
Title: A Journey Through Time | Genre: Horror
Title: The Crystal Key | Genre: Thriller
Title: Whispers of the Abyss | Genre: Fantasy
<start>
Title,Genre
The Silent Grove,Horror
A Journey Through Time,Horror
The Crystal Key,Thriller
Whispers of the Abyss,Fantasy
<end>Please transform the following PLAIN TEXT data into Markdown:
Device ID: device-0072 | Device Type: Motion Detector | Location: Kitchen | Reading Value: 16.53 | Timestamp: 2021-10-09 14:15:56
Device ID: device-0038 | Device Type: Humidity Sensor | Location: Garden | Reading Value: 59.32 | Timestamp: 2021-07-17 06:32:04
Device ID: device-0061 | Device Type: Humidity Sensor | Location: Garage | Reading Value: 41.05 | Timestamp: 2021-08-28 03:41:07
Device ID: device-0032 | Device Type: Humidity Sensor | Location: Kitchen | Reading Value: 23.1 | Timestamp: 2022-06-15 15:10:39
Device ID: device-0032 | Device Type: Light Sensor | Location: Bathroom | Reading Value: 81.48 | Timestamp: 2022-10-08 16:29:43
Device ID: device-0056 | Device Type: Temperature Sensor | Location: Office | Reading Value: -7.36 | Timestamp: 2023-06-27 08:27:19
Device ID: device-0022 | Device Type: Motion Detector | Location: Office | Reading Value: 47.25 | Timestamp: 2021-02-04 04:47:26
<start>
| Device ID | Device Type | Location | Reading Value | Timestamp |
| --- | --- | --- | --- | --- |
| device-0072 | Motion Detector | Kitchen | 16.53 | 2021-10-09 14:15:56 |
| device-0038 | Humidity Sensor | Garden | 59.32 | 2021-07-17 06:32:04 |
| device-0061 | Humidity Sensor | Garage | 41.05 | 2021-08-28 03:41:07 |
| device-0032 | Humidity Sensor | Kitchen | 23.1 | 2022-06-15 15:10:39 |
| device-0032 | Light Sensor | Bathroom | 81.48 | 2022-10-08 16:29:43 |
| device-0056 | Temperature Sensor | Office | -7.36 | 2023-06-27 08:27:19 |
| device-0022 | Motion Detector | Office | 47.25 | 2021-02-04 04:47:26 |
<end>Transform this yml structure to a csv format:
- Humidity (%): 96
  Temperature (C): 25.1
  Wind Speed (km/h): 8.5
- Humidity (%): 54
  Temperature (C): 4.7
  Wind Speed (km/h): 10.6
- Humidity (%): 54
  Temperature (C): -5.9
  Wind Speed (km/h): 9.1
- Humidity (%): 79
  Temperature (C): 12.9
  Wind Speed (km/h): 15.9
- Humidity (%): 40
  Temperature (C): -4.3
  Wind Speed (km/h): 10.6
- Humidity (%): 92
  Temperature (C): 6.4
  Wind Speed (km/h): 15.5
- Humidity (%): 90
  Temperature (C): 28.4
  Wind Speed (km/h): 9.4
- Humidity (%): 96
  Temperature (C): -8.3
  Wind Speed (km/h): 12.1
- Humidity (%): 39
  Temperature (C): 4.7
  Wind Speed (km/h): 24.9
<start>
Temperature (C),Humidity (%),Wind Speed (km/h)
25.1,96,8.5
4.7,54,10.6
-5.9,54,9.1
12.9,79,15.9
-4.3,40,10.6
6.4,92,15.5
28.4,90,9.4
-8.3,96,12.1
4.7,39,24.9
<end>Transform this json structure to a csv format:
[
    {
        "Company": "TechnoCorp",
        "Date": "2023-08-03",
        "Open Price": 41.23,
        "High Price": 879.21,
        "Volume": 8120814
    },
    {
        "Company": "MediaGroup",
        "Date": "2012-08-13",
        "Open Price": 879.21,
        "High Price": 1429.72,
        "Volume": 4362646
    },
    {
        "Company": "GreenEnergy",
        "Date": "2017-09-07",
        "Open Price": 418.43,
        "High Price": 1119.56,
        "Volume": 5239708
    },
    {
        "Company": "AeroSystems",
        "Date": "2015-09-28",
        "Open Price": 1237.88,
        "High Price": 1237.88,
        "Volume": 8054871
    },
    {
        "Company": "BioLife",
        "Date": "2020-01-25",
        "Open Price": 1428.74,
        "High Price": 1470.9,
        "Volume": 3522269
    },
    {
        "Company": "RetailWorld",
        "Date": "2015-06-17",
        "Open Price": 1252.28,
        "High Price": 1252.28,
        "Volume": 3102942
    }
]<start>
Company,Date,Open Price,High Price,Volume
TechnoCorp,2023-08-03,41.23,879.21,8120814
MediaGroup,2012-08-13,879.21,1429.72,4362646
GreenEnergy,2017-09-07,418.43,1119.56,5239708
AeroSystems,2015-09-28,1237.88,1237.88,8054871
BioLife,2020-01-25,1428.74,1470.9,3522269
RetailWorld,2015-06-17,1252.28,1252.28,3102942
<end>Please transform the following PLAIN TEXT data into yaml:
Company: RetailWorld | Close Price: 511.7 | Low Price: 511.7 | Volume: 4234801
Company: RetailWorld | Close Price: 550.09 | Low Price: 550.09 | Volume: 7489371
Company: FinanceTrust | Close Price: 710.4 | Low Price: 710.4 | Volume: 2773233
Company: RetailWorld | Close Price: 1248.83 | Low Price: 1071.08 | Volume: 2629648
Company: HealthGen | Close Price: 1295.42 | Low Price: 581.73 | Volume: 9430816
Company: BioLife | Close Price: 710.4 | Low Price: 710.4 | Volume: 8184175
Company: AutoMotive | Close Price: 1335.47 | Low Price: 120.19 | Volume: 5586666
<start>
- Close Price: 511.7
  Company: RetailWorld
  Low Price: 511.7
  Volume: 4234801
- Close Price: 550.09
  Company: RetailWorld
  Low Price: 550.09
  Volume: 7489371
- Close Price: 710.4
  Company: FinanceTrust
  Low Price: 710.4
  Volume: 2773233
- Close Price: 1248.83
  Company: RetailWorld
  Low Price: 1071.08
  Volume: 2629648
- Close Price: 1295.42
  Company: HealthGen
  Low Price: 581.73
  Volume: 9430816
- Close Price: 710.4
  Company: BioLife
  Low Price: 710.4
  Volume: 8184175
- Close Price: 1335.47
  Company: AutoMotive
  Low Price: 120.19
  Volume: 5586666
<end>Transform this markdown structure to a YAML format:
| Company | Close Price | High Price | Low Price | Volume |
| --- | --- | --- | --- | --- |
| GreenEnergy | 1142.08 | 1142.08 | 30.14 | 3442719 |
| BioLife | 683.29 | 998.07 | 370.91 | 1531018 |
| GreenEnergy | 242.55 | 673.04 | 20.56 | 7489015 |
| GreenEnergy | 1401.31 | 1401.31 | 552.19 | 5363948 |
| AutoMotive | 685.15 | 1241.44 | 685.15 | 5018541 |<start>
- Close Price: 1142.08
  Company: GreenEnergy
  High Price: 1142.08
  Low Price: 30.14
  Volume: 3442719
- Close Price: 683.29
  Company: BioLife
  High Price: 998.07
  Low Price: 370.91
  Volume: 1531018
- Close Price: 242.55
  Company: GreenEnergy
  High Price: 673.04
  Low Price: 20.56
  Volume: 7489015
- Close Price: 1401.31
  Company: GreenEnergy
  High Price: 1401.31
  Low Price: 552.19
  Volume: 5363948
- Close Price: 685.15
  Company: AutoMotive
  High Price: 1241.44
  Low Price: 685.15
  Volume: 5018541
<end>Convert this csv to plain text:
Company,Date,Open Price,Close Price,High Price,Low Price,Volume
AutoMotive,2012-06-27,1198.53,854.44,1198.53,311.27,5022623
HealthGen,2018-05-22,311.27,1223.95,1223.95,311.27,3195484
GreenEnergy,2010-07-07,486.76,1383.97,1383.97,486.76,286088
AutoMotive,2022-08-04,13.26,1496.14,1496.14,13.26,9976706
FinanceTrust,2010-02-01,1331.05,776.79,1465.64,776.79,166495
<start>
Company: AutoMotive | Date: 2012-06-27 | Open Price: 1198.53 | Close Price: 854.44 | High Price: 1198.53 | Low Price: 311.27 | Volume: 5022623
Company: HealthGen | Date: 2018-05-22 | Open Price: 311.27 | Close Price: 1223.95 | High Price: 1223.95 | Low Price: 311.27 | Volume: 3195484
Company: GreenEnergy | Date: 2010-07-07 | Open Price: 486.76 | Close Price: 1383.97 | High Price: 1383.97 | Low Price: 486.76 | Volume: 286088
Company: AutoMotive | Date: 2022-08-04 | Open Price: 13.26 | Close Price: 1496.14 | High Price: 1496.14 | Low Price: 13.26 | Volume: 9976706
Company: FinanceTrust | Date: 2010-02-01 | Open Price: 1331.05 | Close Price: 776.79 | High Price: 1465.64 | Low Price: 776.79 | Volume: 166495
<end>Can you change this plain text into json?
Trip Name: Coast to Coast | Start Location: Los Angeles | End Location: Phoenix | Distance (miles): 308.6 | Duration (hours): 59.0 | Fuel Used (gallons): 47.6
Trip Name: Desert Drive | Start Location: Phoenix | End Location: Denver | Distance (miles): 2181.4 | Duration (hours): 68.4 | Fuel Used (gallons): 29.1
Trip Name: City Explorer | Start Location: Houston | End Location: Chicago | Distance (miles): 262.1 | Duration (hours): 69.8 | Fuel Used (gallons): 93.6
<start>
[
    {
        "Trip Name": "Coast to Coast",
        "Start Location": "Los Angeles",
        "End Location": "Phoenix",
        "Distance (miles)": 308.6,
        "Duration (hours)": 59.0,
        "Fuel Used (gallons)": 47.6
    },
    {
        "Trip Name": "Desert Drive",
        "Start Location": "Phoenix",
        "End Location": "Denver",
        "Distance (miles)": 2181.4,
        "Duration (hours)": 68.4,
        "Fuel Used (gallons)": 29.1
    },
    {
        "Trip Name": "City Explorer",
        "Start Location": "Houston",
        "End Location": "Chicago",
        "Distance (miles)": 262.1,
        "Duration (hours)": 69.8,
        "Fuel Used (gallons)": 93.6
    }
]
<end>Can you change this json into yml?
[
    {
        "Start Location": "Denver",
        "End Location": "Houston",
        "Distance (miles)": 1857.6,
        "Duration (hours)": 56.5,
        "Fuel Used (gallons)": 37.4
    },
    {
        "Start Location": "San Francisco",
        "End Location": "Houston",
        "Distance (miles)": 593.1,
        "Duration (hours)": 19.8,
        "Fuel Used (gallons)": 83.3
    },
    {
        "Start Location": "New York",
        "End Location": "San Francisco",
        "Distance (miles)": 837.5,
        "Duration (hours)": 4.6,
        "Fuel Used (gallons)": 84.0
    },
    {
        "Start Location": "Houston",
        "End Location": "Chicago",
        "Distance (miles)": 695.7,
        "Duration (hours)": 56.6,
        "Fuel Used (gallons)": 35.2
    },
    {
        "Start Location": "Miami",
        "End Location": "Los Angeles",
        "Distance (miles)": 988.1,
        "Duration (hours)": 24.8,
        "Fuel Used (gallons)": 10.3
    },
    {
        "Start Location": "Chicago",
        "End Location": "Los Angeles",
        "Distance (miles)": 1681.6,
        "Duration (hours)": 20.4,
        "Fuel Used (gallons)": 87.4
    }
]<start>
- Distance (miles): 1857.6
  Duration (hours): 56.5
  End Location: Houston
  Fuel Used (gallons): 37.4
  Start Location: Denver
- Distance (miles): 593.1
  Duration (hours): 19.8
  End Location: Houston
  Fuel Used (gallons): 83.3
  Start Location: San Francisco
- Distance (miles): 837.5
  Duration (hours): 4.6
  End Location: San Francisco
  Fuel Used (gallons): 84.0
  Start Location: New York
- Distance (miles): 695.7
  Duration (hours): 56.6
  End Location: Chicago
  Fuel Used (gallons): 35.2
  Start Location: Houston
- Distance (miles): 988.1
  Duration (hours): 24.8
  End Location: Los Angeles
  Fuel Used (gallons): 10.3
  Start Location: Miami
- Distance (miles): 1681.6
  Duration (hours): 20.4
  End Location: Los Angeles
  Fuel Used (gallons): 87.4
  Start Location: Chicago
<end>Please transform the following csv data into YAML:
Date,Open Price,High Price,Volume
2012-12-06,63.09,1327.8,4297633
2016-03-02,384.03,599.37,3412974
2022-09-06,1000.33,1073.08,4197356
2011-09-16,764.54,764.54,6417640
2016-02-08,823.29,823.29,5001872
2014-06-09,1181.94,1181.94,2416433
2015-05-28,1016.84,1016.84,1130903
2015-08-27,178.61,964.15,2384446
2016-05-22,1357.08,1357.08,2358836
<start>
- Date: '2012-12-06'
  High Price: 1327.8
  Open Price: 63.09
  Volume: 4297633
- Date: '2016-03-02'
  High Price: 599.37
  Open Price: 384.03
  Volume: 3412974
- Date: '2022-09-06'
  High Price: 1073.08
  Open Price: 1000.33
  Volume: 4197356
- Date: '2011-09-16'
  High Price: 764.54
  Open Price: 764.54
  Volume: 6417640
- Date: '2016-02-08'
  High Price: 823.29
  Open Price: 823.29
  Volume: 5001872
- Date: '2014-06-09'
  High Price: 1181.94
  Open Price: 1181.94
  Volume: 2416433
- Date: '2015-05-28'
  High Price: 1016.84
  Open Price: 1016.84
  Volume: 1130903
- Date: '2015-08-27'
  High Price: 964.15
  Open Price: 178.61
  Volume: 2384446
- Date: '2016-05-22'
  High Price: 1357.08
  Open Price: 1357.08
  Volume: 2358836
<end>Convert this csv to MARKDOWN:
Cuisine,Location,Price Range
Italian,Los Angeles,$
Mediterranean,San Francisco,$$$$
American,Seattle,$$$$$
Indian,Chicago,$$$
Japanese,Los Angeles,$$$$
Chinese,Seattle,$$$$$
Mexican,New York,$$$
Italian,Houston,$$$$
<start>
| Cuisine | Location | Price Range |
| --- | --- | --- |
| Italian | Los Angeles | $ |
| Mediterranean | San Francisco | $$$$ |
| American | Seattle | $$$$$ |
| Indian | Chicago | $$$ |
| Japanese | Los Angeles | $$$$ |
| Chinese | Seattle | $$$$$ |
| Mexican | New York | $$$ |
| Italian | Houston | $$$$ |
<end>Can you change this markdown into yaml?
| Product Name | Price | Stock Quantity | Category |
| --- | --- | --- | --- |
| Gadget | 407.9 | 452 | Sports |
| Contraption | 367.8 | 414 | Household |
| Whatchamacallit | 452.67 | 208 | Electronics |
| Whatchamacallit | 157.14 | 178 | Sports |
| Widget | 82.21 | 317 | Electronics |
| Contraption | 487.6 | 272 | Household |
| Widget | 412.69 | 43 | Automotive |
| Apparatus | 400.84 | 50 | Sports |
| Gizmo | 144.35 | 430 | Toys |
| Gadget | 219.72 | 186 | Sports |<start>
- Category: Sports
  Price: 407.9
  Product Name: Gadget
  Stock Quantity: 452
- Category: Household
  Price: 367.8
  Product Name: Contraption
  Stock Quantity: 414
- Category: Electronics
  Price: 452.67
  Product Name: Whatchamacallit
  Stock Quantity: 208
- Category: Sports
  Price: 157.14
  Product Name: Whatchamacallit
  Stock Quantity: 178
- Category: Electronics
  Price: 82.21
  Product Name: Widget
  Stock Quantity: 317
- Category: Household
  Price: 487.6
  Product Name: Contraption
  Stock Quantity: 272
- Category: Automotive
  Price: 412.69
  Product Name: Widget
  Stock Quantity: 43
- Category: Sports
  Price: 400.84
  Product Name: Apparatus
  Stock Quantity: 50
- Category: Toys
  Price: 144.35
  Product Name: Gizmo
  Stock Quantity: 430
- Category: Sports
  Price: 219.72
  Product Name: Gadget
  Stock Quantity: 186
<end>Convert this csv to Json:
Company,Open Price,Close Price,High Price,Low Price,Volume
RetailWorld,820.6,896.74,1482.74,194.55,2986348
AutoMotive,844.88,1003.19,1003.19,306.93,9704788
AeroSystems,1173.61,913.6,1173.61,913.6,2011309
BioLife,306.93,1108.6,1108.6,306.93,6430273
FinanceTrust,820.6,31.63,1305.72,31.63,7737083
GreenEnergy,603.76,463.05,1339.3,463.05,541016
<start>
[
    {
        "Company": "RetailWorld",
        "Open Price": 820.6,
        "Close Price": 896.74,
        "High Price": 1482.74,
        "Low Price": 194.55,
        "Volume": 2986348
    },
    {
        "Company": "AutoMotive",
        "Open Price": 844.88,
        "Close Price": 1003.19,
        "High Price": 1003.19,
        "Low Price": 306.93,
        "Volume": 9704788
    },
    {
        "Company": "AeroSystems",
        "Open Price": 1173.61,
        "Close Price": 913.6,
        "High Price": 1173.61,
        "Low Price": 913.6,
        "Volume": 2011309
    },
    {
        "Company": "BioLife",
        "Open Price": 306.93,
        "Close Price": 1108.6,
        "High Price": 1108.6,
        "Low Price": 306.93,
        "Volume": 6430273
    },
    {
        "Company": "FinanceTrust",
        "Open Price": 820.6,
        "Close Price": 31.63,
        "High Price": 1305.72,
        "Low Price": 31.63,
        "Volume": 7737083
    },
    {
        "Company": "GreenEnergy",
        "Open Price": 603.76,
        "Close Price": 463.05,
        "High Price": 1339.3,
        "Low Price": 463.05,
        "Volume": 541016
    }
]
<end>Transform this plain text structure to a Markdown format:
Author: Thorne Ironwood | Genre: Fantasy | Publication Year: 1960 | Rating: 4.3
Author: Isla Windrider | Genre: Mystery | Publication Year: 1992 | Rating: 1.4
Author: Thorne Ironwood | Genre: Romance | Publication Year: 1992 | Rating: 2.3
Author: Draven Blackthorn | Genre: Science Fiction | Publication Year: 2016 | Rating: 2.5
Author: Orion Frostblade | Genre: Science Fiction | Publication Year: 1998 | Rating: 2.5
Author: Sylvia Nightshade | Genre: Historical | Publication Year: 1978 | Rating: 3.8
<start>
| Author | Genre | Publication Year | Rating |
| --- | --- | --- | --- |
| Thorne Ironwood | Fantasy | 1960 | 4.3 |
| Isla Windrider | Mystery | 1992 | 1.4 |
| Thorne Ironwood | Romance | 1992 | 2.3 |
| Draven Blackthorn | Science Fiction | 2016 | 2.5 |
| Orion Frostblade | Science Fiction | 1998 | 2.5 |
| Sylvia Nightshade | Historical | 1978 | 3.8 |
<end>Can you change this Yml into json?
- Average Latency (ms): 60.77
  Cache Hit Ratio (%): 70.87
  Connection Count: 233
  Database Name: MetricsDB
  Queries per Second: 1809.52
  Timestamp: '2023-05-28 09:46:23'
- Average Latency (ms): 49.63
  Cache Hit Ratio (%): 73.79
  Connection Count: 360
  Database Name: ProfilesDB
  Queries per Second: 4895.11
  Timestamp: '2023-02-01 09:40:56'
- Average Latency (ms): 76.48
  Cache Hit Ratio (%): 98.76
  Connection Count: 453
  Database Name: LogsDB
  Queries per Second: 216.6
  Timestamp: '2022-06-07 15:02:45'
- Average Latency (ms): 74.59
  Cache Hit Ratio (%): 85.7
  Connection Count: 127
  Database Name: OrdersDB
  Queries per Second: 4702.88
  Timestamp: '2023-09-04 11:32:41'
- Average Latency (ms): 91.66
  Cache Hit Ratio (%): 80.69
  Connection Count: 390
  Database Name: LogsDB
  Queries per Second: 2948.58
  Timestamp: '2021-12-16 18:57:52'
- Average Latency (ms): 91.66
  Cache Hit Ratio (%): 77.17
  Connection Count: 88
  Database Name: MetricsDB
  Queries per Second: 1346.12
  Timestamp: '2023-10-17 00:04:54'
<start>
[
    {
        "Database Name": "MetricsDB",
        "Queries per Second": 1809.52,
        "Cache Hit Ratio (%)": 70.87,
        "Connection Count": 233,
        "Average Latency (ms)": 60.77,
        "Timestamp": "2023-05-28 09:46:23"
    },
    {
        "Database Name": "ProfilesDB",
        "Queries per Second": 4895.11,
        "Cache Hit Ratio (%)": 73.79,
        "Connection Count": 360,
        "Average Latency (ms)": 49.63,
        "Timestamp": "2023-02-01 09:40:56"
    },
    {
        "Database Name": "LogsDB",
        "Queries per Second": 216.6,
        "Cache Hit Ratio (%)": 98.76,
        "Connection Count": 453,
        "Average Latency (ms)": 76.48,
        "Timestamp": "2022-06-07 15:02:45"
    },
    {
        "Database Name": "OrdersDB",
        "Queries per Second": 4702.88,
        "Cache Hit Ratio (%)": 85.7,
        "Connection Count": 127,
        "Average Latency (ms)": 74.59,
        "Timestamp": "2023-09-04 11:32:41"
    },
    {
        "Database Name": "LogsDB",
        "Queries per Second": 2948.58,
        "Cache Hit Ratio (%)": 80.69,
        "Connection Count": 390,
        "Average Latency (ms)": 91.66,
        "Timestamp": "2021-12-16 18:57:52"
    },
    {
        "Database Name": "MetricsDB",
        "Queries per Second": 1346.12,
        "Cache Hit Ratio (%)": 77.17,
        "Connection Count": 88,
        "Average Latency (ms)": 91.66,
        "Timestamp": "2023-10-17 00:04:54"
    }
]
<end>Convert this plain text to yaml:
Company: Foodies | Market Cap: Mid Cap | Annual Revenue (B): 327.53
Company: EcoEnergy | Market Cap: Small Cap | Annual Revenue (B): 65.72
Company: FinanceWorks | Market Cap: Mega Cap | Annual Revenue (B): 352.75
Company: RetailHub | Market Cap: Large Cap | Annual Revenue (B): 408.03
Company: BioPharm | Market Cap: Small Cap | Annual Revenue (B): 193.56
<start>
- Annual Revenue (B): 327.53
  Company: Foodies
  Market Cap: Mid Cap
- Annual Revenue (B): 65.72
  Company: EcoEnergy
  Market Cap: Small Cap
- Annual Revenue (B): 352.75
  Company: FinanceWorks
  Market Cap: Mega Cap
- Annual Revenue (B): 408.03
  Company: RetailHub
  Market Cap: Large Cap
- Annual Revenue (B): 193.56
  Company: BioPharm
  Market Cap: Small Cap
<end>Here's some csv data, can you convert it to Json?
Birth Month,City,Income
September,Fort Worth,85000
May,San Jose,270000
January,Baltimore,160000
November,Memphis,70000
December,Boston,295000
March,Washington,410000
<start>
[
    {
        "Birth Month": "September",
        "City": "Fort Worth",
        "Income": 85000
    },
    {
        "Birth Month": "May",
        "City": "San Jose",
        "Income": 270000
    },
    {
        "Birth Month": "January",
        "City": "Baltimore",
        "Income": 160000
    },
    {
        "Birth Month": "November",
        "City": "Memphis",
        "Income": 70000
    },
    {
        "Birth Month": "December",
        "City": "Boston",
        "Income": 295000
    },
    {
        "Birth Month": "March",
        "City": "Washington",
        "Income": 410000
    }
]
<end>Transform this plain text structure to a CSV format:
Device ID: device-0031 | Device Type: Pressure Sensor | Location: Living Room | Battery Level (%): 90.3 | Reading Value: 0.39 | Timestamp: 2023-07-27 09:11:31
Device ID: device-0031 | Device Type: Pressure Sensor | Location: Office | Battery Level (%): 82.3 | Reading Value: 11.51 | Timestamp: 2023-10-06 00:51:29
Device ID: device-0022 | Device Type: Motion Detector | Location: Bedroom | Battery Level (%): 64.5 | Reading Value: 75.93 | Timestamp: 2023-10-03 01:03:10
Device ID: device-0026 | Device Type: Light Sensor | Location: Garden | Battery Level (%): 82.6 | Reading Value: 32.47 | Timestamp: 2023-06-28 00:31:04
<start>
Device ID,Device Type,Location,Battery Level (%),Reading Value,Timestamp
device-0031,Pressure Sensor,Living Room,90.3,0.39,2023-07-27 09:11:31
device-0031,Pressure Sensor,Office,82.3,11.51,2023-10-06 00:51:29
device-0022,Motion Detector,Bedroom,64.5,75.93,2023-10-03 01:03:10
device-0026,Light Sensor,Garden,82.6,32.47,2023-06-28 00:31:04
<end>Please transform the following csv data into yaml:
Age,Birth Month,City,Income
48,November,Portland,340000
65,October,Detroit,115000
22,April,Charlotte,385000
43,June,Indianapolis,50000
40,August,New York,110000
28,December,Detroit,345000
38,June,El Paso,260000
27,October,Seattle,170000
30,April,Los Angeles,475000
32,October,San Jose,365000
<start>
- Age: 48
  Birth Month: November
  City: Portland
  Income: 340000
- Age: 65
  Birth Month: October
  City: Detroit
  Income: 115000
- Age: 22
  Birth Month: April
  City: Charlotte
  Income: 385000
- Age: 43
  Birth Month: June
  City: Indianapolis
  Income: 50000
- Age: 40
  Birth Month: August
  City: New York
  Income: 110000
- Age: 28
  Birth Month: December
  City: Detroit
  Income: 345000
- Age: 38
  Birth Month: June
  City: El Paso
  Income: 260000
- Age: 27
  Birth Month: October
  City: Seattle
  Income: 170000
- Age: 30
  Birth Month: April
  City: Los Angeles
  Income: 475000
- Age: 32
  Birth Month: October
  City: San Jose
  Income: 365000
<end>Transform this Json structure to a plain text format:
[
    {
        "SKU": "SKU-1034",
        "Stock Quantity": 472,
        "Category": "Sports",
        "Supplier Name": "Globex"
    },
    {
        "SKU": "SKU-1091",
        "Stock Quantity": 26,
        "Category": "Household",
        "Supplier Name": "Umbrella Corp"
    },
    {
        "SKU": "SKU-1096",
        "Stock Quantity": 111,
        "Category": "Sports",
        "Supplier Name": "Wonka Industries"
    },
    {
        "SKU": "SKU-1072",
        "Stock Quantity": 136,
        "Category": "Household",
        "Supplier Name": "Umbrella Corp"
    },
    {
        "SKU": "SKU-1072",
        "Stock Quantity": 442,
        "Category": "Electronics",
        "Supplier Name": "ACME Corp"
    },
    {
        "SKU": "SKU-1071",
        "Stock Quantity": 280,
        "Category": "Automotive",
        "Supplier Name": "Wonka Industries"
    },
    {
        "SKU": "SKU-1014",
        "Stock Quantity": 38,
        "Category": "Automotive",
        "Supplier Name": "Umbrella Corp"
    },
    {
        "SKU": "SKU-1075",
        "Stock Quantity": 190,
        "Category": "Electronics",
        "Supplier Name": "Umbrella Corp"
    },
    {
        "SKU": "SKU-1020",
        "Stock Quantity": 415,
        "Category": "Electronics",
        "Supplier Name": "Wayne Enterprises"
    },
    {
        "SKU": "SKU-1064",
        "Stock Quantity": 51,
        "Category": "Household",
        "Supplier Name": "Umbrella Corp"
    }
]<start>
SKU: SKU-1034 | Stock Quantity: 472 | Category: Sports | Supplier Name: Globex
SKU: SKU-1091 | Stock Quantity: 26 | Category: Household | Supplier Name: Umbrella Corp
SKU: SKU-1096 | Stock Quantity: 111 | Category: Sports | Supplier Name: Wonka Industries
SKU: SKU-1072 | Stock Quantity: 136 | Category: Household | Supplier Name: Umbrella Corp
SKU: SKU-1072 | Stock Quantity: 442 | Category: Electronics | Supplier Name: ACME Corp
SKU: SKU-1071 | Stock Quantity: 280 | Category: Automotive | Supplier Name: Wonka Industries
SKU: SKU-1014 | Stock Quantity: 38 | Category: Automotive | Supplier Name: Umbrella Corp
SKU: SKU-1075 | Stock Quantity: 190 | Category: Electronics | Supplier Name: Umbrella Corp
SKU: SKU-1020 | Stock Quantity: 415 | Category: Electronics | Supplier Name: Wayne Enterprises
SKU: SKU-1064 | Stock Quantity: 51 | Category: Household | Supplier Name: Umbrella Corp
<end>Transform this plain text structure to a Csv format:
Company: BioPharm | Sector: Healthcare | Market Cap: Mid Cap | Stock Price: 211.64 | Annual Revenue (B): 331.77 | Quarter: Q4
Company: EcoEnergy | Sector: Energy | Market Cap: Mega Cap | Stock Price: 950.47 | Annual Revenue (B): 246.28 | Quarter: Q2
Company: TechCorp | Sector: Retail | Market Cap: Mega Cap | Stock Price: 225.86 | Annual Revenue (B): 407.47 | Quarter: Q3
<start>
Company,Sector,Market Cap,Stock Price,Annual Revenue (B),Quarter
BioPharm,Healthcare,Mid Cap,211.64,331.77,Q4
EcoEnergy,Energy,Mega Cap,950.47,246.28,Q2
TechCorp,Retail,Mega Cap,225.86,407.47,Q3
<end>Convert this Markdown to Yml:
| Database Name | Queries per Second | Cache Hit Ratio (%) | Connection Count | Average Latency (ms) | Timestamp |
| --- | --- | --- | --- | --- | --- |
| ProductsDB | 1949.85 | 93.51 | 354 | 93.35 | 2023-09-04 18:19:30 |
| InventoryDB | 2130.69 | 95.57 | 72 | 3.79 | 2021-04-20 19:49:39 |
| AnalyticsDB | 1807.09 | 73.86 | 241 | 65.93 | 2021-04-25 04:48:51 |
| UserDB | 3058.68 | 90.81 | 227 | 84.22 | 2022-04-05 11:32:01 |
| LogsDB | 2071.92 | 82.14 | 245 | 67.76 | 2022-11-13 08:47:18 |
| LogsDB | 2486.12 | 74.87 | 241 | 47.84 | 2022-02-25 23:28:52 |
| AnalyticsDB | 54.69 | 71.54 | 275 | 84.53 | 2023-10-28 17:08:47 |
| LogsDB | 2488.06 | 90.81 | 198 | 52.36 | 2022-05-07 12:04:25 |<start>
- Average Latency (ms): 93.35
  Cache Hit Ratio (%): 93.51
  Connection Count: 354
  Database Name: ProductsDB
  Queries per Second: 1949.85
  Timestamp: '2023-09-04 18:19:30'
- Average Latency (ms): 3.79
  Cache Hit Ratio (%): 95.57
  Connection Count: 72
  Database Name: InventoryDB
  Queries per Second: 2130.69
  Timestamp: '2021-04-20 19:49:39'
- Average Latency (ms): 65.93
  Cache Hit Ratio (%): 73.86
  Connection Count: 241
  Database Name: AnalyticsDB
  Queries per Second: 1807.09
  Timestamp: '2021-04-25 04:48:51'
- Average Latency (ms): 84.22
  Cache Hit Ratio (%): 90.81
  Connection Count: 227
  Database Name: UserDB
  Queries per Second: 3058.68
  Timestamp: '2022-04-05 11:32:01'
- Average Latency (ms): 67.76
  Cache Hit Ratio (%): 82.14
  Connection Count: 245
  Database Name: LogsDB
  Queries per Second: 2071.92
  Timestamp: '2022-11-13 08:47:18'
- Average Latency (ms): 47.84
  Cache Hit Ratio (%): 74.87
  Connection Count: 241
  Database Name: LogsDB
  Queries per Second: 2486.12
  Timestamp: '2022-02-25 23:28:52'
- Average Latency (ms): 84.53
  Cache Hit Ratio (%): 71.54
  Connection Count: 275
  Database Name: AnalyticsDB
  Queries per Second: 54.69
  Timestamp: '2023-10-28 17:08:47'
- Average Latency (ms): 52.36
  Cache Hit Ratio (%): 90.81
  Connection Count: 198
  Database Name: LogsDB
  Queries per Second: 2488.06
  Timestamp: '2022-05-07 12:04:25'
<end>Here's some yml data, can you convert it to markdown?
- Average Latency (ms): 86.2
  Cache Hit Ratio (%): 76.64
  Connection Count: 452
  Database Name: ProfilesDB
  Queries per Second: 2283.11
  Timestamp: '2021-08-27 14:55:35'
- Average Latency (ms): 12.0
  Cache Hit Ratio (%): 84.63
  Connection Count: 479
  Database Name: ProfilesDB
  Queries per Second: 3045.59
  Timestamp: '2021-01-02 12:10:51'
- Average Latency (ms): 40.0
  Cache Hit Ratio (%): 82.75
  Connection Count: 142
  Database Name: UserDB
  Queries per Second: 4441.82
  Timestamp: '2021-12-09 00:48:10'
- Average Latency (ms): 65.35
  Cache Hit Ratio (%): 99.38
  Connection Count: 20
  Database Name: OrdersDB
  Queries per Second: 1490.48
  Timestamp: '2022-01-21 08:34:26'
- Average Latency (ms): 1.15
  Cache Hit Ratio (%): 82.27
  Connection Count: 34
  Database Name: SalesDB
  Queries per Second: 1945.19
  Timestamp: '2023-06-07 04:59:18'
- Average Latency (ms): 29.69
  Cache Hit Ratio (%): 94.83
  Connection Count: 481
  Database Name: LogsDB
  Queries per Second: 4333.16
  Timestamp: '2023-02-09 07:45:58'
- Average Latency (ms): 49.75
  Cache Hit Ratio (%): 94.52
  Connection Count: 127
  Database Name: ProfilesDB
  Queries per Second: 1703.78
  Timestamp: '2023-10-06 22:02:51'
- Average Latency (ms): 99.37
  Cache Hit Ratio (%): 82.27
  Connection Count: 235
  Database Name: SalesDB
  Queries per Second: 1898.87
  Timestamp: '2023-08-04 07:27:55'
- Average Latency (ms): 62.35
  Cache Hit Ratio (%): 76.64
  Connection Count: 496
  Database Name: UserDB
  Queries per Second: 1100.1
  Timestamp: '2022-03-03 14:57:32'
<start>
| Database Name | Queries per Second | Cache Hit Ratio (%) | Connection Count | Average Latency (ms) | Timestamp |
| --- | --- | --- | --- | --- | --- |
| ProfilesDB | 2283.11 | 76.64 | 452 | 86.2 | 2021-08-27 14:55:35 |
| ProfilesDB | 3045.59 | 84.63 | 479 | 12.0 | 2021-01-02 12:10:51 |
| UserDB | 4441.82 | 82.75 | 142 | 40.0 | 2021-12-09 00:48:10 |
| OrdersDB | 1490.48 | 99.38 | 20 | 65.35 | 2022-01-21 08:34:26 |
| SalesDB | 1945.19 | 82.27 | 34 | 1.15 | 2023-06-07 04:59:18 |
| LogsDB | 4333.16 | 94.83 | 481 | 29.69 | 2023-02-09 07:45:58 |
| ProfilesDB | 1703.78 | 94.52 | 127 | 49.75 | 2023-10-06 22:02:51 |
| SalesDB | 1898.87 | 82.27 | 235 | 99.37 | 2023-08-04 07:27:55 |
| UserDB | 1100.1 | 76.64 | 496 | 62.35 | 2022-03-03 14:57:32 |
<end>Can you change this PLAIN TEXT into MARKDOWN?
Name: Lincoln | Age: 41
Name: Cecelia | Age: 44
Name: Juan | Age: 68
Name: Hubert | Age: 59
Name: Laura | Age: 58
Name: Nelson | Age: 40
<start>
| Name | Age |
| --- | --- |
| Lincoln | 41 |
| Cecelia | 44 |
| Juan | 68 |
| Hubert | 59 |
| Laura | 58 |
| Nelson | 40 |
<end>Can you change this MARKDOWN into Plain text?
| Device ID | Device Type | Location | Battery Level (%) | Reading Value | Timestamp |
| --- | --- | --- | --- | --- | --- |
| device-0018 | Temperature Sensor | Bedroom | 18.8 | -11.15 | 2023-06-04 23:14:18 |
| device-0054 | Humidity Sensor | Garage | 58.4 | 8.52 | 2021-08-06 17:06:42 |
| device-0085 | Motion Detector | Garden | 16.7 | 15.83 | 2022-09-21 06:29:35 |
| device-0043 | Motion Detector | Office | 33.9 | 69.48 | 2023-11-07 08:16:28 |
| device-0078 | Light Sensor | Kitchen | 44.4 | 80.48 | 2023-01-11 17:24:36 |<start>
Device ID: device-0018 | Device Type: Temperature Sensor | Location: Bedroom | Battery Level (%): 18.8 | Reading Value: -11.15 | Timestamp: 2023-06-04 23:14:18
Device ID: device-0054 | Device Type: Humidity Sensor | Location: Garage | Battery Level (%): 58.4 | Reading Value: 8.52 | Timestamp: 2021-08-06 17:06:42
Device ID: device-0085 | Device Type: Motion Detector | Location: Garden | Battery Level (%): 16.7 | Reading Value: 15.83 | Timestamp: 2022-09-21 06:29:35
Device ID: device-0043 | Device Type: Motion Detector | Location: Office | Battery Level (%): 33.9 | Reading Value: 69.48 | Timestamp: 2023-11-07 08:16:28
Device ID: device-0078 | Device Type: Light Sensor | Location: Kitchen | Battery Level (%): 44.4 | Reading Value: 80.48 | Timestamp: 2023-01-11 17:24:36
<end>Here's some markdown data, can you convert it to JSON?
| Queries per Second | Cache Hit Ratio (%) | Average Latency (ms) | Timestamp |
| --- | --- | --- | --- |
| 1551.02 | 95.83 | 87.41 | 2022-09-17 09:38:45 |
| 3801.6 | 72.31 | 8.54 | 2023-01-07 04:46:47 |
| 4684.73 | 95.47 | 30.45 | 2023-12-23 02:29:20 |
| 3516.75 | 96.81 | 98.48 | 2022-01-08 15:35:01 |
| 4200.68 | 96.68 | 29.1 | 2021-06-16 04:49:30 |
| 2697.1 | 80.05 | 24.02 | 2022-04-27 12:54:47 |
| 1551.02 | 81.06 | 99.34 | 2023-01-01 06:19:36 |
| 830.0 | 89.88 | 89.07 | 2021-11-18 20:56:03 |<start>
[
    {
        "Queries per Second": 1551.02,
        "Cache Hit Ratio (%)": 95.83,
        "Average Latency (ms)": 87.41,
        "Timestamp": "2022-09-17 09:38:45"
    },
    {
        "Queries per Second": 3801.6,
        "Cache Hit Ratio (%)": 72.31,
        "Average Latency (ms)": 8.54,
        "Timestamp": "2023-01-07 04:46:47"
    },
    {
        "Queries per Second": 4684.73,
        "Cache Hit Ratio (%)": 95.47,
        "Average Latency (ms)": 30.45,
        "Timestamp": "2023-12-23 02:29:20"
    },
    {
        "Queries per Second": 3516.75,
        "Cache Hit Ratio (%)": 96.81,
        "Average Latency (ms)": 98.48,
        "Timestamp": "2022-01-08 15:35:01"
    },
    {
        "Queries per Second": 4200.68,
        "Cache Hit Ratio (%)": 96.68,
        "Average Latency (ms)": 29.1,
        "Timestamp": "2021-06-16 04:49:30"
    },
    {
        "Queries per Second": 2697.1,
        "Cache Hit Ratio (%)": 80.05,
        "Average Latency (ms)": 24.02,
        "Timestamp": "2022-04-27 12:54:47"
    },
    {
        "Queries per Second": 1551.02,
        "Cache Hit Ratio (%)": 81.06,
        "Average Latency (ms)": 99.34,
        "Timestamp": "2023-01-01 06:19:36"
    },
    {
        "Queries per Second": 830.0,
        "Cache Hit Ratio (%)": 89.88,
        "Average Latency (ms)": 89.07,
        "Timestamp": "2021-11-18 20:56:03"
    }
]
<end>Here's some Plain text data, can you convert it to json?
Restaurant Name: Curry Corner | Cuisine: French | Location: Miami | Rating: 1
Restaurant Name: The Steakhouse | Cuisine: Indian | Location: San Francisco | Rating: 4
Restaurant Name: Sushi World | Cuisine: Indian | Location: Los Angeles | Rating: 5
<start>
[
    {
        "Restaurant Name": "Curry Corner",
        "Cuisine": "French",
        "Location": "Miami",
        "Rating": 1
    },
    {
        "Restaurant Name": "The Steakhouse",
        "Cuisine": "Indian",
        "Location": "San Francisco",
        "Rating": 4
    },
    {
        "Restaurant Name": "Sushi World",
        "Cuisine": "Indian",
        "Location": "Los Angeles",
        "Rating": 5
    }
]
<end>Here's some JSON data, can you convert it to csv?
[
    {
        "Start Location": "Houston",
        "End Location": "Los Angeles",
        "Fuel Used (gallons)": 93.0
    },
    {
        "Start Location": "Chicago",
        "End Location": "Phoenix",
        "Fuel Used (gallons)": 45.5
    },
    {
        "Start Location": "Chicago",
        "End Location": "Denver",
        "Fuel Used (gallons)": 71.4
    },
    {
        "Start Location": "New York",
        "End Location": "Houston",
        "Fuel Used (gallons)": 45.7
    },
    {
        "Start Location": "Chicago",
        "End Location": "Phoenix",
        "Fuel Used (gallons)": 34.8
    },
    {
        "Start Location": "Houston",
        "End Location": "New York",
        "Fuel Used (gallons)": 24.4
    },
    {
        "Start Location": "Los Angeles",
        "End Location": "San Francisco",
        "Fuel Used (gallons)": 37.4
    },
    {
        "Start Location": "Chicago",
        "End Location": "New York",
        "Fuel Used (gallons)": 24.8
    },
    {
        "Start Location": "Miami",
        "End Location": "San Francisco",
        "Fuel Used (gallons)": 35.0
    }
]<start>
Start Location,End Location,Fuel Used (gallons)
Houston,Los Angeles,93.0
Chicago,Phoenix,45.5
Chicago,Denver,71.4
New York,Houston,45.7
Chicago,Phoenix,34.8
Houston,New York,24.4
Los Angeles,San Francisco,37.4
Chicago,New York,24.8
Miami,San Francisco,35.0
<end>Please transform the following yaml data into plain text:
- Author: Draven Blackthorn
  Publication Year: 1953
- Author: Elara Moonshadow
  Publication Year: 1996
- Author: Luna Silverleaf
  Publication Year: 2013
- Author: Rowan Ashborne
  Publication Year: 2008
- Author: Galen Starfire
  Publication Year: 1971
- Author: Kara Firebrand
  Publication Year: 1983
<start>
Author: Draven Blackthorn | Publication Year: 1953
Author: Elara Moonshadow | Publication Year: 1996
Author: Luna Silverleaf | Publication Year: 2013
Author: Rowan Ashborne | Publication Year: 2008
Author: Galen Starfire | Publication Year: 1971
Author: Kara Firebrand | Publication Year: 1983
<end>Here's some yaml data, can you convert it to json?
- Age: 60
  Birth Month: September
  Name: Genevieve
- Age: 66
  Birth Month: January
  Name: Sawyer
- Age: 25
  Birth Month: November
  Name: Nellie
<start>
[
    {
        "Name": "Genevieve",
        "Age": 60,
        "Birth Month": "September"
    },
    {
        "Name": "Sawyer",
        "Age": 66,
        "Birth Month": "January"
    },
    {
        "Name": "Nellie",
        "Age": 25,
        "Birth Month": "November"
    }
]
<end>Here's some csv data, can you convert it to markdown?
Age,Birth Month
66,June
32,November
51,July
37,July
39,September
32,August
<start>
| Age | Birth Month |
| --- | --- |
| 66 | June |
| 32 | November |
| 51 | July |
| 37 | July |
| 39 | September |
| 32 | August |
<end>Here's some JSON data, can you convert it to PLAIN TEXT?
[
    {
        "Product Name": "Gizmo",
        "SKU": "SKU-1050",
        "Price": 302.63,
        "Supplier Name": "Globex"
    },
    {
        "Product Name": "Widget",
        "SKU": "SKU-1035",
        "Price": 61.93,
        "Supplier Name": "Umbrella Corp"
    },
    {
        "Product Name": "Device",
        "SKU": "SKU-1079",
        "Price": 205.28,
        "Supplier Name": "Wayne Enterprises"
    },
    {
        "Product Name": "Whatchamacallit",
        "SKU": "SKU-1049",
        "Price": 323.94,
        "Supplier Name": "Wayne Enterprises"
    },
    {
        "Product Name": "Instrument",
        "SKU": "SKU-1056",
        "Price": 139.93,
        "Supplier Name": "Globex"
    },
    {
        "Product Name": "Widget",
        "SKU": "SKU-1066",
        "Price": 100.02,
        "Supplier Name": "Umbrella Corp"
    },
    {
        "Product Name": "Whatchamacallit",
        "SKU": "SKU-1082",
        "Price": 174.68,
        "Supplier Name": "ACME Corp"
    },
    {
        "Product Name": "Apparatus",
        "SKU": "SKU-1085",
        "Price": 117.42,
        "Supplier Name": "ACME Corp"
    }
]<start>
Product Name: Gizmo | SKU: SKU-1050 | Price: 302.63 | Supplier Name: Globex
Product Name: Widget | SKU: SKU-1035 | Price: 61.93 | Supplier Name: Umbrella Corp
Product Name: Device | SKU: SKU-1079 | Price: 205.28 | Supplier Name: Wayne Enterprises
Product Name: Whatchamacallit | SKU: SKU-1049 | Price: 323.94 | Supplier Name: Wayne Enterprises
Product Name: Instrument | SKU: SKU-1056 | Price: 139.93 | Supplier Name: Globex
Product Name: Widget | SKU: SKU-1066 | Price: 100.02 | Supplier Name: Umbrella Corp
Product Name: Whatchamacallit | SKU: SKU-1082 | Price: 174.68 | Supplier Name: ACME Corp
Product Name: Apparatus | SKU: SKU-1085 | Price: 117.42 | Supplier Name: ACME Corp
<end>Convert this csv to markdown:
Device ID,Device Type,Location,Battery Level (%),Reading Value,Timestamp
device-0012,Pressure Sensor,Garden,16.6,-39.74,2021-01-04 14:10:02
device-0075,Humidity Sensor,Living Room,91.2,-31.36,2022-10-12 12:10:20
device-0052,Light Sensor,Office,55.4,-24.7,2023-01-02 12:26:23
<start>
| Device ID | Device Type | Location | Battery Level (%) | Reading Value | Timestamp |
| --- | --- | --- | --- | --- | --- |
| device-0012 | Pressure Sensor | Garden | 16.6 | -39.74 | 2021-01-04 14:10:02 |
| device-0075 | Humidity Sensor | Living Room | 91.2 | -31.36 | 2022-10-12 12:10:20 |
| device-0052 | Light Sensor | Office | 55.4 | -24.7 | 2023-01-02 12:26:23 |
<end>Transform this PLAIN TEXT structure to a Markdown format:
Company: RetailHub | Sector: Automotive | Stock Price: 524.45 | Annual Revenue (B): 323.29
Company: EcoEnergy | Sector: Energy | Stock Price: 148.03 | Annual Revenue (B): 115.42
Company: EcoEnergy | Sector: Retail | Stock Price: 254.34 | Annual Revenue (B): 224.4
Company: HealthPlus | Sector: Aerospace | Stock Price: 874.35 | Annual Revenue (B): 286.63
Company: TechCorp | Sector: Healthcare | Stock Price: 371.1 | Annual Revenue (B): 306.2
Company: BioPharm | Sector: Aerospace | Stock Price: 309.23 | Annual Revenue (B): 278.46
Company: GlobalTrade | Sector: Retail | Stock Price: 356.77 | Annual Revenue (B): 334.5
<start>
| Company | Sector | Stock Price | Annual Revenue (B) |
| --- | --- | --- | --- |
| RetailHub | Automotive | 524.45 | 323.29 |
| EcoEnergy | Energy | 148.03 | 115.42 |
| EcoEnergy | Retail | 254.34 | 224.4 |
| HealthPlus | Aerospace | 874.35 | 286.63 |
| TechCorp | Healthcare | 371.1 | 306.2 |
| BioPharm | Aerospace | 309.23 | 278.46 |
| GlobalTrade | Retail | 356.77 | 334.5 |
<end>Convert this yml to Markdown:
- Close Price: 273.16
  Company: MediaGroup
  Date: '2021-06-27'
  High Price: 1043.33
  Low Price: 273.16
  Open Price: 1043.33
  Volume: 5028817
- Close Price: 97.35
  Company: FinanceTrust
  Date: '2010-09-19'
  High Price: 1227.82
  Low Price: 97.35
  Open Price: 844.89
  Volume: 9878377
- Close Price: 1179.84
  Company: AeroSystems
  Date: '2023-08-16'
  High Price: 1498.8
  Low Price: 68.07
  Open Price: 68.07
  Volume: 751305
<start>
| Company | Date | Open Price | Close Price | High Price | Low Price | Volume |
| --- | --- | --- | --- | --- | --- | --- |
| MediaGroup | 2021-06-27 | 1043.33 | 273.16 | 1043.33 | 273.16 | 5028817 |
| FinanceTrust | 2010-09-19 | 844.89 | 97.35 | 1227.82 | 97.35 | 9878377 |
| AeroSystems | 2023-08-16 | 68.07 | 1179.84 | 1498.8 | 68.07 | 751305 |
<end>Here's some Json data, can you convert it to PLAIN TEXT?
[
    {
        "Device ID": "device-0045",
        "Device Type": "Motion Detector",
        "Location": "Kitchen",
        "Battery Level (%)": 10.5,
        "Reading Value": 47.6,
        "Timestamp": "2023-07-01 00:27:01"
    },
    {
        "Device ID": "device-0056",
        "Device Type": "Pressure Sensor",
        "Location": "Bathroom",
        "Battery Level (%)": 89.8,
        "Reading Value": 56.71,
        "Timestamp": "2023-07-02 06:18:46"
    },
    {
        "Device ID": "device-0098",
        "Device Type": "Motion Detector",
        "Location": "Kitchen",
        "Battery Level (%)": 76.8,
        "Reading Value": 72.56,
        "Timestamp": "2021-03-08 19:41:39"
    },
    {
        "Device ID": "device-0095",
        "Device Type": "Temperature Sensor",
        "Location": "Bathroom",
        "Battery Level (%)": 29.9,
        "Reading Value": 60.05,
        "Timestamp": "2023-11-13 05:31:28"
    }
]<start>
Device ID: device-0045 | Device Type: Motion Detector | Location: Kitchen | Battery Level (%): 10.5 | Reading Value: 47.6 | Timestamp: 2023-07-01 00:27:01
Device ID: device-0056 | Device Type: Pressure Sensor | Location: Bathroom | Battery Level (%): 89.8 | Reading Value: 56.71 | Timestamp: 2023-07-02 06:18:46
Device ID: device-0098 | Device Type: Motion Detector | Location: Kitchen | Battery Level (%): 76.8 | Reading Value: 72.56 | Timestamp: 2021-03-08 19:41:39
Device ID: device-0095 | Device Type: Temperature Sensor | Location: Bathroom | Battery Level (%): 29.9 | Reading Value: 60.05 | Timestamp: 2023-11-13 05:31:28
<end>Can you change this csv into markdown?
Device ID,Device Type,Reading Value,Timestamp
device-0034,Temperature Sensor,22.7,2023-01-03 10:15:24
device-0086,Humidity Sensor,83.78,2022-07-06 01:54:51
device-0098,Motion Detector,33.25,2022-11-16 13:27:04
<start>
| Device ID | Device Type | Reading Value | Timestamp |
| --- | --- | --- | --- |
| device-0034 | Temperature Sensor | 22.7 | 2023-01-03 10:15:24 |
| device-0086 | Humidity Sensor | 83.78 | 2022-07-06 01:54:51 |
| device-0098 | Motion Detector | 33.25 | 2022-11-16 13:27:04 |
<end>Convert this plain text to markdown:
Age: 52 | City: Chicago | Income: 215000
Age: 43 | City: Milwaukee | Income: 320000
Age: 40 | City: San Antonio | Income: 480000
Age: 55 | City: Louisville | Income: 35000
Age: 46 | City: Columbus | Income: 160000
Age: 21 | City: Detroit | Income: 365000
Age: 35 | City: Seattle | Income: 85000
Age: 28 | City: Boston | Income: 65000
Age: 62 | City: Seattle | Income: 275000
<start>
| Age | City | Income |
| --- | --- | --- |
| 52 | Chicago | 215000 |
| 43 | Milwaukee | 320000 |
| 40 | San Antonio | 480000 |
| 55 | Louisville | 35000 |
| 46 | Columbus | 160000 |
| 21 | Detroit | 365000 |
| 35 | Seattle | 85000 |
| 28 | Boston | 65000 |
| 62 | Seattle | 275000 |
<end>Here's some csv data, can you convert it to yml?
Location,Condition,Wind Speed (km/h)
Miami,Sunny,30.0
Miami,Rainy,30.0
Phoenix,Foggy,18.5
Houston,Snowy,10.0
Phoenix,Foggy,24.1
New York,Rainy,19.6
<start>
- Condition: Sunny
  Location: Miami
  Wind Speed (km/h): 30.0
- Condition: Rainy
  Location: Miami
  Wind Speed (km/h): 30.0
- Condition: Foggy
  Location: Phoenix
  Wind Speed (km/h): 18.5
- Condition: Snowy
  Location: Houston
  Wind Speed (km/h): 10.0
- Condition: Foggy
  Location: Phoenix
  Wind Speed (km/h): 24.1
- Condition: Rainy
  Location: New York
  Wind Speed (km/h): 19.6
<end>Here's some JSON data, can you convert it to Yaml?
[
    {
        "SKU": "SKU-1070",
        "Stock Quantity": 380,
        "Category": "Automotive"
    },
    {
        "SKU": "SKU-1038",
        "Stock Quantity": 188,
        "Category": "Sports"
    },
    {
        "SKU": "SKU-1078",
        "Stock Quantity": 421,
        "Category": "Electronics"
    },
    {
        "SKU": "SKU-1064",
        "Stock Quantity": 212,
        "Category": "Household"
    },
    {
        "SKU": "SKU-1068",
        "Stock Quantity": 394,
        "Category": "Electronics"
    },
    {
        "SKU": "SKU-1020",
        "Stock Quantity": 148,
        "Category": "Sports"
    },
    {
        "SKU": "SKU-1097",
        "Stock Quantity": 375,
        "Category": "Electronics"
    },
    {
        "SKU": "SKU-1018",
        "Stock Quantity": 355,
        "Category": "Automotive"
    },
    {
        "SKU": "SKU-1084",
        "Stock Quantity": 46,
        "Category": "Electronics"
    }
]<start>
- Category: Automotive
  SKU: SKU-1070
  Stock Quantity: 380
- Category: Sports
  SKU: SKU-1038
  Stock Quantity: 188
- Category: Electronics
  SKU: SKU-1078
  Stock Quantity: 421
- Category: Household
  SKU: SKU-1064
  Stock Quantity: 212
- Category: Electronics
  SKU: SKU-1068
  Stock Quantity: 394
- Category: Sports
  SKU: SKU-1020
  Stock Quantity: 148
- Category: Electronics
  SKU: SKU-1097
  Stock Quantity: 375
- Category: Automotive
  SKU: SKU-1018
  Stock Quantity: 355
- Category: Electronics
  SKU: SKU-1084
  Stock Quantity: 46
<end>Here's some markdown data, can you convert it to plain text?
| Name | Age |
| --- | --- |
| Luke | 51 |
| Mable | 54 |
| Johnnie | 40 |
| Joel | 33 |
| Felicia | 67 |
| Robert | 18 |<start>
Name: Luke | Age: 51
Name: Mable | Age: 54
Name: Johnnie | Age: 40
Name: Joel | Age: 33
Name: Felicia | Age: 67
Name: Robert | Age: 18
<end>Transform this Markdown structure to a yaml format:
| Title | Author | Rating |
| --- | --- | --- |
| Tales of the Brave | Isla Windrider | 2.4 |
| Shadows of Solitude | Kara Firebrand | 4.7 |
| A Journey Through Time | Elara Moonshadow | 4.3 |
| Tales of the Brave | Draven Blackthorn | 3.8 |
| The Crystal Key | Draven Blackthorn | 3.2 |
| The Forgotten World | Thorne Ironwood | 2.4 |
| The Last Sky | Kara Firebrand | 1.6 |
| Whispers of the Abyss | Orion Frostblade | 1.1 |
| A Journey Through Time | Luna Silverleaf | 3.9 |<start>
- Author: Isla Windrider
  Rating: 2.4
  Title: Tales of the Brave
- Author: Kara Firebrand
  Rating: 4.7
  Title: Shadows of Solitude
- Author: Elara Moonshadow
  Rating: 4.3
  Title: A Journey Through Time
- Author: Draven Blackthorn
  Rating: 3.8
  Title: Tales of the Brave
- Author: Draven Blackthorn
  Rating: 3.2
  Title: The Crystal Key
- Author: Thorne Ironwood
  Rating: 2.4
  Title: The Forgotten World
- Author: Kara Firebrand
  Rating: 1.6
  Title: The Last Sky
- Author: Orion Frostblade
  Rating: 1.1
  Title: Whispers of the Abyss
- Author: Luna Silverleaf
  Rating: 3.9
  Title: A Journey Through Time
<end>Can you change this PLAIN TEXT into Markdown?
Date: 2014-03-04 | Open Price: 1090.66 | Close Price: 910.09 | Volume: 9901112
Date: 2013-09-24 | Open Price: 702.03 | Close Price: 1314.7 | Volume: 9650117
Date: 2012-12-15 | Open Price: 581.58 | Close Price: 1061.98 | Volume: 233944
Date: 2011-07-05 | Open Price: 1271.15 | Close Price: 1214.22 | Volume: 2975021
<start>
| Date | Open Price | Close Price | Volume |
| --- | --- | --- | --- |
| 2014-03-04 | 1090.66 | 910.09 | 9901112 |
| 2013-09-24 | 702.03 | 1314.7 | 9650117 |
| 2012-12-15 | 581.58 | 1061.98 | 233944 |
| 2011-07-05 | 1271.15 | 1214.22 | 2975021 |
<end>Here's some Yml data, can you convert it to Csv?
- Company: TechnoCorp
  High Price: 1075.95
  Open Price: 782.79
  Volume: 2738537
- Company: FoodChain
  High Price: 1040.0
  Open Price: 650.23
  Volume: 3427158
- Company: HealthGen
  High Price: 1123.93
  Open Price: 985.89
  Volume: 4434408
- Company: FinanceTrust
  High Price: 985.89
  Open Price: 985.89
  Volume: 4402870
- Company: AutoMotive
  High Price: 1078.65
  Open Price: 268.46
  Volume: 8567205
- Company: GreenEnergy
  High Price: 1370.9
  Open Price: 541.75
  Volume: 4100267
<start>
Company,Open Price,High Price,Volume
TechnoCorp,782.79,1075.95,2738537
FoodChain,650.23,1040.0,3427158
HealthGen,985.89,1123.93,4434408
FinanceTrust,985.89,985.89,4402870
AutoMotive,268.46,1078.65,8567205
GreenEnergy,541.75,1370.9,4100267
<end>Can you change this yaml into MARKDOWN?
- Product Name: Whatchamacallit
  SKU: SKU-1084
  Stock Quantity: 239
- Product Name: Doohickey
  SKU: SKU-1043
  Stock Quantity: 222
- Product Name: Thingamajig
  SKU: SKU-1062
  Stock Quantity: 200
- Product Name: Device
  SKU: SKU-1001
  Stock Quantity: 403
- Product Name: Thingamajig
  SKU: SKU-1035
  Stock Quantity: 291
- Product Name: Whatchamacallit
  SKU: SKU-1090
  Stock Quantity: 115
- Product Name: Gadget
  SKU: SKU-1081
  Stock Quantity: 274
- Product Name: Gizmo
  SKU: SKU-1095
  Stock Quantity: 177
<start>
| Product Name | SKU | Stock Quantity |
| --- | --- | --- |
| Whatchamacallit | SKU-1084 | 239 |
| Doohickey | SKU-1043 | 222 |
| Thingamajig | SKU-1062 | 200 |
| Device | SKU-1001 | 403 |
| Thingamajig | SKU-1035 | 291 |
| Whatchamacallit | SKU-1090 | 115 |
| Gadget | SKU-1081 | 274 |
| Gizmo | SKU-1095 | 177 |
<end>Transform this yaml structure to a json format:
- Close Price: 422.57
  Company: AutoMotive
  Date: '2014-05-24'
  Low Price: 422.57
  Open Price: 1451.64
  Volume: 6962263
- Close Price: 1361.09
  Company: GreenEnergy
  Date: '2023-05-06'
  Low Price: 11.28
  Open Price: 11.28
  Volume: 9903420
- Close Price: 1435.1
  Company: RetailWorld
  Date: '2022-10-24'
  Low Price: 222.48
  Open Price: 222.48
  Volume: 1384558
<start>
[
    {
        "Company": "AutoMotive",
        "Date": "2014-05-24",
        "Open Price": 1451.64,
        "Close Price": 422.57,
        "Low Price": 422.57,
        "Volume": 6962263
    },
    {
        "Company": "GreenEnergy",
        "Date": "2023-05-06",
        "Open Price": 11.28,
        "Close Price": 1361.09,
        "Low Price": 11.28,
        "Volume": 9903420
    },
    {
        "Company": "RetailWorld",
        "Date": "2022-10-24",
        "Open Price": 222.48,
        "Close Price": 1435.1,
        "Low Price": 222.48,
        "Volume": 1384558
    }
]
<end>Transform this YAML structure to a MARKDOWN format:
- Annual Revenue (B): 356.27
  Market Cap: Mega Cap
  Quarter: Q4
  Sector: Aerospace
- Annual Revenue (B): 287.69
  Market Cap: Mid Cap
  Quarter: Q2
  Sector: Healthcare
- Annual Revenue (B): 190.76
  Market Cap: Large Cap
  Quarter: Q3
  Sector: Finance
<start>
| Sector | Market Cap | Annual Revenue (B) | Quarter |
| --- | --- | --- | --- |
| Aerospace | Mega Cap | 356.27 | Q4 |
| Healthcare | Mid Cap | 287.69 | Q2 |
| Finance | Large Cap | 190.76 | Q3 |
<end>Here's some yaml data, can you convert it to markdown?
- Category: Electronics
  SKU: SKU-1090
  Supplier Name: Globex
- Category: Household
  SKU: SKU-1092
  Supplier Name: Umbrella Corp
- Category: Sports
  SKU: SKU-1095
  Supplier Name: Globex
- Category: Toys
  SKU: SKU-1022
  Supplier Name: ACME Corp
- Category: Electronics
  SKU: SKU-1033
  Supplier Name: Wayne Enterprises
- Category: Automotive
  SKU: SKU-1020
  Supplier Name: Globex
- Category: Toys
  SKU: SKU-1009
  Supplier Name: Wayne Enterprises
- Category: Automotive
  SKU: SKU-1065
  Supplier Name: Umbrella Corp
<start>
| SKU | Category | Supplier Name |
| --- | --- | --- |
| SKU-1090 | Electronics | Globex |
| SKU-1092 | Household | Umbrella Corp |
| SKU-1095 | Sports | Globex |
| SKU-1022 | Toys | ACME Corp |
| SKU-1033 | Electronics | Wayne Enterprises |
| SKU-1020 | Automotive | Globex |
| SKU-1009 | Toys | Wayne Enterprises |
| SKU-1065 | Automotive | Umbrella Corp |
<end>Convert this CSV to markdown:
Age,Birth Month
66,January
31,January
61,June
<start>
| Age | Birth Month |
| --- | --- |
| 66 | January |
| 31 | January |
| 61 | June |
<end>Please transform the following MARKDOWN data into JSON:
| Start Location | End Location | Distance (miles) | Fuel Used (gallons) |
| --- | --- | --- | --- |
| New York | San Francisco | 2923.9 | 46.7 |
| Phoenix | New York | 959.8 | 40.3 |
| Chicago | Houston | 2923.9 | 30.0 |<start>
[
    {
        "Start Location": "New York",
        "End Location": "San Francisco",
        "Distance (miles)": 2923.9,
        "Fuel Used (gallons)": 46.7
    },
    {
        "Start Location": "Phoenix",
        "End Location": "New York",
        "Distance (miles)": 959.8,
        "Fuel Used (gallons)": 40.3
    },
    {
        "Start Location": "Chicago",
        "End Location": "Houston",
        "Distance (miles)": 2923.9,
        "Fuel Used (gallons)": 30.0
    }
]
<end>Can you change this YML into Plain text?
- Age: 57
  Birth Month: July
  Name: Sandy
- Age: 42
  Birth Month: February
  Name: Everett
- Age: 22
  Birth Month: August
  Name: Carl
- Age: 64
  Birth Month: November
  Name: Eileen
- Age: 38
  Birth Month: February
  Name: Jason
- Age: 45
  Birth Month: August
  Name: Julie
- Age: 58
  Birth Month: December
  Name: Stephanie
- Age: 57
  Birth Month: October
  Name: Theodore
- Age: 66
  Birth Month: February
  Name: Luella
<start>
Name: Sandy | Age: 57 | Birth Month: July
Name: Everett | Age: 42 | Birth Month: February
Name: Carl | Age: 22 | Birth Month: August
Name: Eileen | Age: 64 | Birth Month: November
Name: Jason | Age: 38 | Birth Month: February
Name: Julie | Age: 45 | Birth Month: August
Name: Stephanie | Age: 58 | Birth Month: December
Name: Theodore | Age: 57 | Birth Month: October
Name: Luella | Age: 66 | Birth Month: February
<end>Can you change this CSV into markdown?
Market Cap,Stock Price,Quarter
Mega Cap,235.25,Q4
Mid Cap,86.68,Q2
Mega Cap,413.11,Q4
Mega Cap,724.97,Q4
Mid Cap,285.55,Q2
<start>
| Market Cap | Stock Price | Quarter |
| --- | --- | --- |
| Mega Cap | 235.25 | Q4 |
| Mid Cap | 86.68 | Q2 |
| Mega Cap | 413.11 | Q4 |
| Mega Cap | 724.97 | Q4 |
| Mid Cap | 285.55 | Q2 |
<end>Convert this markdown to plain text:
| Title | Author | Genre | Rating |
| --- | --- | --- | --- |
| A Journey Through Time | Kara Firebrand | Horror | 3.8 |
| Shadows of Solitude | Luna Silverleaf | Science Fiction | 1.0 |
| The Forgotten World | Luna Silverleaf | Mystery | 3.8 |
| Echoes of Eternity | Thorne Ironwood | Fantasy | 4.5 |<start>
Title: A Journey Through Time | Author: Kara Firebrand | Genre: Horror | Rating: 3.8
Title: Shadows of Solitude | Author: Luna Silverleaf | Genre: Science Fiction | Rating: 1.0
Title: The Forgotten World | Author: Luna Silverleaf | Genre: Mystery | Rating: 3.8
Title: Echoes of Eternity | Author: Thorne Ironwood | Genre: Fantasy | Rating: 4.5
<end>Transform this YML structure to a json format:
- Battery Level (%): 20.2
  Device ID: device-0070
  Device Type: Temperature Sensor
  Location: Garage
  Reading Value: -19.75
  Timestamp: '2021-06-22 22:04:14'
- Battery Level (%): 32.0
  Device ID: device-0088
  Device Type: Temperature Sensor
  Location: Kitchen
  Reading Value: -20.47
  Timestamp: '2023-09-03 04:26:56'
- Battery Level (%): 78.0
  Device ID: device-0090
  Device Type: Temperature Sensor
  Location: Bedroom
  Reading Value: 68.83
  Timestamp: '2023-04-09 11:43:41'
- Battery Level (%): 91.7
  Device ID: device-0044
  Device Type: Light Sensor
  Location: Living Room
  Reading Value: 6.98
  Timestamp: '2023-12-04 09:53:35'
- Battery Level (%): 78.0
  Device ID: device-0078
  Device Type: Light Sensor
  Location: Hallway
  Reading Value: 6.33
  Timestamp: '2023-10-28 13:30:39'
<start>
[
    {
        "Device ID": "device-0070",
        "Device Type": "Temperature Sensor",
        "Location": "Garage",
        "Battery Level (%)": 20.2,
        "Reading Value": -19.75,
        "Timestamp": "2021-06-22 22:04:14"
    },
    {
        "Device ID": "device-0088",
        "Device Type": "Temperature Sensor",
        "Location": "Kitchen",
        "Battery Level (%)": 32.0,
        "Reading Value": -20.47,
        "Timestamp": "2023-09-03 04:26:56"
    },
    {
        "Device ID": "device-0090",
        "Device Type": "Temperature Sensor",
        "Location": "Bedroom",
        "Battery Level (%)": 78.0,
        "Reading Value": 68.83,
        "Timestamp": "2023-04-09 11:43:41"
    },
    {
        "Device ID": "device-0044",
        "Device Type": "Light Sensor",
        "Location": "Living Room",
        "Battery Level (%)": 91.7,
        "Reading Value": 6.98,
        "Timestamp": "2023-12-04 09:53:35"
    },
    {
        "Device ID": "device-0078",
        "Device Type": "Light Sensor",
        "Location": "Hallway",
        "Battery Level (%)": 78.0,
        "Reading Value": 6.33,
        "Timestamp": "2023-10-28 13:30:39"
    }
]
<end>Convert this json to plain text:
[
    {
        "Restaurant Name": "BBQ Barn",
        "Cuisine": "Mexican",
        "Location": "Seattle",
        "Rating": 1,
        "Price Range": "$$$$$"
    },
    {
        "Restaurant Name": "The Golden Spoon",
        "Cuisine": "Japanese",
        "Location": "Houston",
        "Rating": 4,
        "Price Range": "$$$"
    },
    {
        "Restaurant Name": "Pizza Planet",
        "Cuisine": "American",
        "Location": "Phoenix",
        "Rating": 3,
        "Price Range": "$$"
    },
    {
        "Restaurant Name": "The Steakhouse",
        "Cuisine": "Mexican",
        "Location": "San Francisco",
        "Rating": 4,
        "Price Range": "$$$$"
    },
    {
        "Restaurant Name": "Taco Town",
        "Cuisine": "Mexican",
        "Location": "Phoenix",
        "Rating": 5,
        "Price Range": "$$"
    },
    {
        "Restaurant Name": "The Golden Spoon",
        "Cuisine": "American",
        "Location": "Seattle",
        "Rating": 2,
        "Price Range": "$$"
    },
    {
        "Restaurant Name": "BBQ Barn",
        "Cuisine": "Mediterranean",
        "Location": "New York",
        "Rating": 2,
        "Price Range": "$"
    },
    {
        "Restaurant Name": "The Golden Spoon",
        "Cuisine": "Japanese",
        "Location": "Miami",
        "Rating": 3,
        "Price Range": "$$$$$"
    }
]<start>
Restaurant Name: BBQ Barn | Cuisine: Mexican | Location: Seattle | Rating: 1 | Price Range: $$$$$
Restaurant Name: The Golden Spoon | Cuisine: Japanese | Location: Houston | Rating: 4 | Price Range: $$$
Restaurant Name: Pizza Planet | Cuisine: American | Location: Phoenix | Rating: 3 | Price Range: $$
Restaurant Name: The Steakhouse | Cuisine: Mexican | Location: San Francisco | Rating: 4 | Price Range: $$$$
Restaurant Name: Taco Town | Cuisine: Mexican | Location: Phoenix | Rating: 5 | Price Range: $$
Restaurant Name: The Golden Spoon | Cuisine: American | Location: Seattle | Rating: 2 | Price Range: $$
Restaurant Name: BBQ Barn | Cuisine: Mediterranean | Location: New York | Rating: 2 | Price Range: $
Restaurant Name: The Golden Spoon | Cuisine: Japanese | Location: Miami | Rating: 3 | Price Range: $$$$$
<end>Please transform the following yml data into Markdown:
- Annual Revenue (B): 478.54
  Company: RetailHub
  Market Cap: Mega Cap
  Quarter: Q3
  Sector: Automotive
  Stock Price: 378.73
- Annual Revenue (B): 339.43
  Company: GlobalTrade
  Market Cap: Small Cap
  Quarter: Q3
  Sector: Finance
  Stock Price: 445.91
- Annual Revenue (B): 239.16
  Company: GlobalTrade
  Market Cap: Small Cap
  Quarter: Q3
  Sector: Retail
  Stock Price: 223.17
- Annual Revenue (B): 226.93
  Company: RetailHub
  Market Cap: Mega Cap
  Quarter: Q1
  Sector: Technology
  Stock Price: 790.77
- Annual Revenue (B): 247.0
  Company: Foodies
  Market Cap: Mid Cap
  Quarter: Q1
  Sector: Healthcare
  Stock Price: 764.7
- Annual Revenue (B): 425.92
  Company: TechCorp
  Market Cap: Mega Cap
  Quarter: Q3
  Sector: Biotech
  Stock Price: 113.98
- Annual Revenue (B): 54.09
  Company: BioPharm
  Market Cap: Mega Cap
  Quarter: Q2
  Sector: Aerospace
  Stock Price: 527.61
- Annual Revenue (B): 53.89
  Company: FinanceWorks
  Market Cap: Large Cap
  Quarter: Q1
  Sector: Technology
  Stock Price: 90.69
<start>
| Company | Sector | Market Cap | Stock Price | Annual Revenue (B) | Quarter |
| --- | --- | --- | --- | --- | --- |
| RetailHub | Automotive | Mega Cap | 378.73 | 478.54 | Q3 |
| GlobalTrade | Finance | Small Cap | 445.91 | 339.43 | Q3 |
| GlobalTrade | Retail | Small Cap | 223.17 | 239.16 | Q3 |
| RetailHub | Technology | Mega Cap | 790.77 | 226.93 | Q1 |
| Foodies | Healthcare | Mid Cap | 764.7 | 247.0 | Q1 |
| TechCorp | Biotech | Mega Cap | 113.98 | 425.92 | Q3 |
| BioPharm | Aerospace | Mega Cap | 527.61 | 54.09 | Q2 |
| FinanceWorks | Technology | Large Cap | 90.69 | 53.89 | Q1 |
<end>Convert this MARKDOWN to csv:
| Title | Director | Genre | Release Year | Box Office Earnings (M) |
| --- | --- | --- | --- | --- |
| Dreamwalker | Talon Blackthorn | Action | 2023 | 93.16 |
| Dreamwalker | Lira Silverleaf | Sci-Fi | 1989 | 420.47 |
| Edge of Infinity | Zara Stormrider | Horror | 2013 | 824.67 |<start>
Title,Director,Genre,Release Year,Box Office Earnings (M)
Dreamwalker,Talon Blackthorn,Action,2023,93.16
Dreamwalker,Lira Silverleaf,Sci-Fi,1989,420.47
Edge of Infinity,Zara Stormrider,Horror,2013,824.67
<end>Transform this yml structure to a plain text format:
- Distance (miles): 983.4
  Duration (hours): 52.1
  End Location: San Francisco
  Start Location: Miami
  Trip Name: Historic Route
- Distance (miles): 2864.5
  Duration (hours): 17.6
  End Location: Miami
  Start Location: New York
  Trip Name: Desert Drive
- Distance (miles): 2776.7
  Duration (hours): 51.2
  End Location: San Francisco
  Start Location: Houston
  Trip Name: Coast to Coast
- Distance (miles): 2295.5
  Duration (hours): 67.9
  End Location: Houston
  Start Location: Phoenix
  Trip Name: Highway Odyssey
- Distance (miles): 2235.6
  Duration (hours): 25.5
  End Location: Phoenix
  Start Location: Denver
  Trip Name: Canyon Trek
- Distance (miles): 2194.9
  Duration (hours): 38.8
  End Location: Miami
  Start Location: New York
  Trip Name: Historic Route
- Distance (miles): 1436.4
  Duration (hours): 21.5
  End Location: New York
  Start Location: Denver
  Trip Name: Forest Journey
- Distance (miles): 2730.0
  Duration (hours): 47.7
  End Location: Los Angeles
  Start Location: New York
  Trip Name: Valley Voyage
- Distance (miles): 2845.9
  Duration (hours): 55.6
  End Location: Houston
  Start Location: Denver
  Trip Name: Historic Route
<start>
Trip Name: Historic Route | Start Location: Miami | End Location: San Francisco | Distance (miles): 983.4 | Duration (hours): 52.1
Trip Name: Desert Drive | Start Location: New York | End Location: Miami | Distance (miles): 2864.5 | Duration (hours): 17.6
Trip Name: Coast to Coast | Start Location: Houston | End Location: San Francisco | Distance (miles): 2776.7 | Duration (hours): 51.2
Trip Name: Highway Odyssey | Start Location: Phoenix | End Location: Houston | Distance (miles): 2295.5 | Duration (hours): 67.9
Trip Name: Canyon Trek | Start Location: Denver | End Location: Phoenix | Distance (miles): 2235.6 | Duration (hours): 25.5
Trip Name: Historic Route | Start Location: New York | End Location: Miami | Distance (miles): 2194.9 | Duration (hours): 38.8
Trip Name: Forest Journey | Start Location: Denver | End Location: New York | Distance (miles): 1436.4 | Duration (hours): 21.5
Trip Name: Valley Voyage | Start Location: New York | End Location: Los Angeles | Distance (miles): 2730.0 | Duration (hours): 47.7
Trip Name: Historic Route | Start Location: Denver | End Location: Houston | Distance (miles): 2845.9 | Duration (hours): 55.6
<end>Transform this markdown structure to a json format:
| Trip Name | Start Location | End Location | Distance (miles) | Duration (hours) |
| --- | --- | --- | --- | --- |
| Valley Voyage | New York | Phoenix | 2608.1 | 19.4 |
| Mountain Adventure | Miami | Los Angeles | 2106.8 | 27.9 |
| Desert Drive | Houston | Phoenix | 2906.0 | 62.6 |<start>
[
    {
        "Trip Name": "Valley Voyage",
        "Start Location": "New York",
        "End Location": "Phoenix",
        "Distance (miles)": 2608.1,
        "Duration (hours)": 19.4
    },
    {
        "Trip Name": "Mountain Adventure",
        "Start Location": "Miami",
        "End Location": "Los Angeles",
        "Distance (miles)": 2106.8,
        "Duration (hours)": 27.9
    },
    {
        "Trip Name": "Desert Drive",
        "Start Location": "Houston",
        "End Location": "Phoenix",
        "Distance (miles)": 2906.0,
        "Duration (hours)": 62.6
    }
]
<end>Can you change this JSON into csv?
[
    {
        "Company": "AeroSystems",
        "Date": "2015-05-03",
        "Open Price": 453.42,
        "Low Price": 321.78,
        "Volume": 9277850
    },
    {
        "Company": "TechnoCorp",
        "Date": "2021-12-25",
        "Open Price": 351.98,
        "Low Price": 351.98,
        "Volume": 9671516
    },
    {
        "Company": "FoodChain",
        "Date": "2020-03-11",
        "Open Price": 1449.32,
        "Low Price": 355.56,
        "Volume": 5709580
    },
    {
        "Company": "BioLife",
        "Date": "2021-07-07",
        "Open Price": 721.18,
        "Low Price": 70.96,
        "Volume": 1957948
    },
    {
        "Company": "MediaGroup",
        "Date": "2010-01-28",
        "Open Price": 1302.36,
        "Low Price": 951.5,
        "Volume": 6851356
    }
]<start>
Company,Date,Open Price,Low Price,Volume
AeroSystems,2015-05-03,453.42,321.78,9277850
TechnoCorp,2021-12-25,351.98,351.98,9671516
FoodChain,2020-03-11,1449.32,355.56,5709580
BioLife,2021-07-07,721.18,70.96,1957948
MediaGroup,2010-01-28,1302.36,951.5,6851356
<end>Can you change this Plain text into YAML?
Sector: Automotive | Market Cap: Large Cap | Annual Revenue (B): 235.83
Sector: Energy | Market Cap: Mid Cap | Annual Revenue (B): 325.42
Sector: Aerospace | Market Cap: Large Cap | Annual Revenue (B): 354.69
<start>
- Annual Revenue (B): 235.83
  Market Cap: Large Cap
  Sector: Automotive
- Annual Revenue (B): 325.42
  Market Cap: Mid Cap
  Sector: Energy
- Annual Revenue (B): 354.69
  Market Cap: Large Cap
  Sector: Aerospace
<end>Can you change this markdown into Plain text?
| Product Name | SKU | Price | Category | Supplier Name |
| --- | --- | --- | --- | --- |
| Contraption | SKU-1050 | 465.41 | Household | Globex |
| Device | SKU-1044 | 307.97 | Automotive | Globex |
| Widget | SKU-1013 | 300.19 | Household | Globex |<start>
Product Name: Contraption | SKU: SKU-1050 | Price: 465.41 | Category: Household | Supplier Name: Globex
Product Name: Device | SKU: SKU-1044 | Price: 307.97 | Category: Automotive | Supplier Name: Globex
Product Name: Widget | SKU: SKU-1013 | Price: 300.19 | Category: Household | Supplier Name: Globex
<end>Here's some json data, can you convert it to Yml?
[
    {
        "Trip Name": "Coast to Coast",
        "Start Location": "New York",
        "End Location": "Houston",
        "Distance (miles)": 105.2,
        "Duration (hours)": 36.3
    },
    {
        "Trip Name": "Highway Odyssey",
        "Start Location": "New York",
        "End Location": "Denver",
        "Distance (miles)": 1204.1,
        "Duration (hours)": 5.9
    },
    {
        "Trip Name": "Historic Route",
        "Start Location": "Houston",
        "End Location": "San Francisco",
        "Distance (miles)": 497.4,
        "Duration (hours)": 52.6
    },
    {
        "Trip Name": "Historic Route",
        "Start Location": "Houston",
        "End Location": "Miami",
        "Distance (miles)": 1640.3,
        "Duration (hours)": 41.6
    },
    {
        "Trip Name": "Lakeside Retreat",
        "Start Location": "Miami",
        "End Location": "Phoenix",
        "Distance (miles)": 2328.5,
        "Duration (hours)": 16.9
    },
    {
        "Trip Name": "Coast to Coast",
        "Start Location": "New York",
        "End Location": "Denver",
        "Distance (miles)": 1210.1,
        "Duration (hours)": 34.0
    },
    {
        "Trip Name": "Lakeside Retreat",
        "Start Location": "Los Angeles",
        "End Location": "Denver",
        "Distance (miles)": 1789.6,
        "Duration (hours)": 61.3
    }
]<start>
- Distance (miles): 105.2
  Duration (hours): 36.3
  End Location: Houston
  Start Location: New York
  Trip Name: Coast to Coast
- Distance (miles): 1204.1
  Duration (hours): 5.9
  End Location: Denver
  Start Location: New York
  Trip Name: Highway Odyssey
- Distance (miles): 497.4
  Duration (hours): 52.6
  End Location: San Francisco
  Start Location: Houston
  Trip Name: Historic Route
- Distance (miles): 1640.3
  Duration (hours): 41.6
  End Location: Miami
  Start Location: Houston
  Trip Name: Historic Route
- Distance (miles): 2328.5
  Duration (hours): 16.9
  End Location: Phoenix
  Start Location: Miami
  Trip Name: Lakeside Retreat
- Distance (miles): 1210.1
  Duration (hours): 34.0
  End Location: Denver
  Start Location: New York
  Trip Name: Coast to Coast
- Distance (miles): 1789.6
  Duration (hours): 61.3
  End Location: Denver
  Start Location: Los Angeles
  Trip Name: Lakeside Retreat
<end>Can you change this json into csv?
[
    {
        "Company": "TechnoCorp",
        "Date": "2019-10-06",
        "Open Price": 371.53,
        "Close Price": 902.43,
        "High Price": 1489.01,
        "Low Price": 371.53
    },
    {
        "Company": "RetailWorld",
        "Date": "2021-10-09",
        "Open Price": 1427.37,
        "Close Price": 418.94,
        "High Price": 1427.37,
        "Low Price": 418.94
    },
    {
        "Company": "FoodChain",
        "Date": "2015-05-27",
        "Open Price": 409.9,
        "Close Price": 1227.7,
        "High Price": 1227.7,
        "Low Price": 171.26
    },
    {
        "Company": "TechnoCorp",
        "Date": "2021-05-01",
        "Open Price": 421.22,
        "Close Price": 732.38,
        "High Price": 1314.91,
        "Low Price": 421.22
    },
    {
        "Company": "AeroSystems",
        "Date": "2020-12-03",
        "Open Price": 1072.14,
        "Close Price": 1088.17,
        "High Price": 1088.17,
        "Low Price": 1072.14
    },
    {
        "Company": "GreenEnergy",
        "Date": "2022-07-10",
        "Open Price": 1078.59,
        "Close Price": 126.75,
        "High Price": 1411.92,
        "Low Price": 126.75
    },
    {
        "Company": "BioLife",
        "Date": "2019-07-02",
        "Open Price": 627.33,
        "Close Price": 1070.92,
        "High Price": 1070.92,
        "Low Price": 627.33
    }
]<start>
Company,Date,Open Price,Close Price,High Price,Low Price
TechnoCorp,2019-10-06,371.53,902.43,1489.01,371.53
RetailWorld,2021-10-09,1427.37,418.94,1427.37,418.94
FoodChain,2015-05-27,409.9,1227.7,1227.7,171.26
TechnoCorp,2021-05-01,421.22,732.38,1314.91,421.22
AeroSystems,2020-12-03,1072.14,1088.17,1088.17,1072.14
GreenEnergy,2022-07-10,1078.59,126.75,1411.92,126.75
BioLife,2019-07-02,627.33,1070.92,1070.92,627.33
<end>Convert this Json to Plain text:
[
    {
        "Product Name": "Whatchamacallit",
        "SKU": "SKU-1060",
        "Price": 22.4,
        "Stock Quantity": 476,
        "Category": "Automotive",
        "Supplier Name": "Wayne Enterprises"
    },
    {
        "Product Name": "Whatchamacallit",
        "SKU": "SKU-1003",
        "Price": 497.68,
        "Stock Quantity": 257,
        "Category": "Household",
        "Supplier Name": "Wonka Industries"
    },
    {
        "Product Name": "Whatchamacallit",
        "SKU": "SKU-1062",
        "Price": 467.15,
        "Stock Quantity": 265,
        "Category": "Sports",
        "Supplier Name": "Wonka Industries"
    },
    {
        "Product Name": "Whatchamacallit",
        "SKU": "SKU-1078",
        "Price": 195.95,
        "Stock Quantity": 198,
        "Category": "Household",
        "Supplier Name": "ACME Corp"
    },
    {
        "Product Name": "Instrument",
        "SKU": "SKU-1084",
        "Price": 247.44,
        "Stock Quantity": 10,
        "Category": "Toys",
        "Supplier Name": "Umbrella Corp"
    },
    {
        "Product Name": "Gizmo",
        "SKU": "SKU-1024",
        "Price": 331.83,
        "Stock Quantity": 371,
        "Category": "Automotive",
        "Supplier Name": "Wonka Industries"
    }
]<start>
Product Name: Whatchamacallit | SKU: SKU-1060 | Price: 22.4 | Stock Quantity: 476 | Category: Automotive | Supplier Name: Wayne Enterprises
Product Name: Whatchamacallit | SKU: SKU-1003 | Price: 497.68 | Stock Quantity: 257 | Category: Household | Supplier Name: Wonka Industries
Product Name: Whatchamacallit | SKU: SKU-1062 | Price: 467.15 | Stock Quantity: 265 | Category: Sports | Supplier Name: Wonka Industries
Product Name: Whatchamacallit | SKU: SKU-1078 | Price: 195.95 | Stock Quantity: 198 | Category: Household | Supplier Name: ACME Corp
Product Name: Instrument | SKU: SKU-1084 | Price: 247.44 | Stock Quantity: 10 | Category: Toys | Supplier Name: Umbrella Corp
Product Name: Gizmo | SKU: SKU-1024 | Price: 331.83 | Stock Quantity: 371 | Category: Automotive | Supplier Name: Wonka Industries
<end>Transform this plain text structure to a Yml format:
Name: Ryder | Age: 68 | Income: 70000
Name: Keith | Age: 21 | Income: 335000
Name: Jada | Age: 20 | Income: 385000
Name: Eloise | Age: 51 | Income: 245000
Name: Arnold | Age: 51 | Income: 35000
Name: Meghan | Age: 38 | Income: 130000
Name: Jamie | Age: 23 | Income: 95000
<start>
- Age: 68
  Income: 70000
  Name: Ryder
- Age: 21
  Income: 335000
  Name: Keith
- Age: 20
  Income: 385000
  Name: Jada
- Age: 51
  Income: 245000
  Name: Eloise
- Age: 51
  Income: 35000
  Name: Arnold
- Age: 38
  Income: 130000
  Name: Meghan
- Age: 23
  Income: 95000
  Name: Jamie
<end>Please transform the following CSV data into Json:
Location,Condition,Temperature (C),Humidity (%),Wind Speed (km/h),Day
Los Angeles,Windy,-2.5,86,13.8,Thursday
Houston,Stormy,-7.6,56,26.7,Friday
Miami,Windy,10.0,37,6.1,Thursday
Miami,Cloudy,36.4,39,13.2,Thursday
<start>
[
    {
        "Location": "Los Angeles",
        "Condition": "Windy",
        "Temperature (C)": -2.5,
        "Humidity (%)": 86,
        "Wind Speed (km/h)": 13.8,
        "Day": "Thursday"
    },
    {
        "Location": "Houston",
        "Condition": "Stormy",
        "Temperature (C)": -7.6,
        "Humidity (%)": 56,
        "Wind Speed (km/h)": 26.7,
        "Day": "Friday"
    },
    {
        "Location": "Miami",
        "Condition": "Windy",
        "Temperature (C)": 10.0,
        "Humidity (%)": 37,
        "Wind Speed (km/h)": 6.1,
        "Day": "Thursday"
    },
    {
        "Location": "Miami",
        "Condition": "Cloudy",
        "Temperature (C)": 36.4,
        "Humidity (%)": 39,
        "Wind Speed (km/h)": 13.2,
        "Day": "Thursday"
    }
]
<end>Transform this Plain text structure to a yaml format:
Database Name: InventoryDB | Queries per Second: 2855.48 | Cache Hit Ratio (%): 86.43 | Connection Count: 79 | Average Latency (ms): 34.58 | Timestamp: 2022-12-08 20:45:56
Database Name: ProfilesDB | Queries per Second: 4699.02 | Cache Hit Ratio (%): 97.5 | Connection Count: 235 | Average Latency (ms): 36.9 | Timestamp: 2022-11-25 07:32:07
Database Name: OrdersDB | Queries per Second: 3752.68 | Cache Hit Ratio (%): 98.81 | Connection Count: 395 | Average Latency (ms): 34.58 | Timestamp: 2021-02-14 15:51:52
Database Name: OrdersDB | Queries per Second: 4639.55 | Cache Hit Ratio (%): 76.05 | Connection Count: 175 | Average Latency (ms): 90.43 | Timestamp: 2022-04-08 11:41:12
Database Name: MetricsDB | Queries per Second: 4613.11 | Cache Hit Ratio (%): 77.18 | Connection Count: 260 | Average Latency (ms): 16.95 | Timestamp: 2022-05-25 00:59:21
Database Name: ProductsDB | Queries per Second: 1581.14 | Cache Hit Ratio (%): 77.66 | Connection Count: 201 | Average Latency (ms): 10.25 | Timestamp: 2023-11-10 10:14:54
Database Name: UserDB | Queries per Second: 2300.26 | Cache Hit Ratio (%): 70.04 | Connection Count: 455 | Average Latency (ms): 91.59 | Timestamp: 2022-04-05 05:35:22
Database Name: OrdersDB | Queries per Second: 892.74 | Cache Hit Ratio (%): 79.74 | Connection Count: 271 | Average Latency (ms): 85.18 | Timestamp: 2021-07-13 01:25:57
Database Name: MetricsDB | Queries per Second: 634.3 | Cache Hit Ratio (%): 72.35 | Connection Count: 360 | Average Latency (ms): 30.31 | Timestamp: 2023-01-01 18:32:49
<start>
- Average Latency (ms): 34.58
  Cache Hit Ratio (%): 86.43
  Connection Count: 79
  Database Name: InventoryDB
  Queries per Second: 2855.48
  Timestamp: '2022-12-08 20:45:56'
- Average Latency (ms): 36.9
  Cache Hit Ratio (%): 97.5
  Connection Count: 235
  Database Name: ProfilesDB
  Queries per Second: 4699.02
  Timestamp: '2022-11-25 07:32:07'
- Average Latency (ms): 34.58
  Cache Hit Ratio (%): 98.81
  Connection Count: 395
  Database Name: OrdersDB
  Queries per Second: 3752.68
  Timestamp: '2021-02-14 15:51:52'
- Average Latency (ms): 90.43
  Cache Hit Ratio (%): 76.05
  Connection Count: 175
  Database Name: OrdersDB
  Queries per Second: 4639.55
  Timestamp: '2022-04-08 11:41:12'
- Average Latency (ms): 16.95
  Cache Hit Ratio (%): 77.18
  Connection Count: 260
  Database Name: MetricsDB
  Queries per Second: 4613.11
  Timestamp: '2022-05-25 00:59:21'
- Average Latency (ms): 10.25
  Cache Hit Ratio (%): 77.66
  Connection Count: 201
  Database Name: ProductsDB
  Queries per Second: 1581.14
  Timestamp: '2023-11-10 10:14:54'
- Average Latency (ms): 91.59
  Cache Hit Ratio (%): 70.04
  Connection Count: 455
  Database Name: UserDB
  Queries per Second: 2300.26
  Timestamp: '2022-04-05 05:35:22'
- Average Latency (ms): 85.18
  Cache Hit Ratio (%): 79.74
  Connection Count: 271
  Database Name: OrdersDB
  Queries per Second: 892.74
  Timestamp: '2021-07-13 01:25:57'
- Average Latency (ms): 30.31
  Cache Hit Ratio (%): 72.35
  Connection Count: 360
  Database Name: MetricsDB
  Queries per Second: 634.3
  Timestamp: '2023-01-01 18:32:49'
<end>