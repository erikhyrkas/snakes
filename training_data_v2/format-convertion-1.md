Here's some yml data, can you convert it to plain text?
- Annual Revenue (B): 259.32
  Company: HealthPlus
  Market Cap: Mega Cap
  Quarter: Q4
- Annual Revenue (B): 73.18
  Company: Foodies
  Market Cap: Mega Cap
  Quarter: Q3
- Annual Revenue (B): 119.33
  Company: TechCorp
  Market Cap: Mega Cap
  Quarter: Q2
- Annual Revenue (B): 125.42
  Company: FinanceWorks
  Market Cap: Large Cap
  Quarter: Q3
- Annual Revenue (B): 471.69
  Company: RetailHub
  Market Cap: Mid Cap
  Quarter: Q1
<start>
Company: HealthPlus | Market Cap: Mega Cap | Annual Revenue (B): 259.32 | Quarter: Q4
Company: Foodies | Market Cap: Mega Cap | Annual Revenue (B): 73.18 | Quarter: Q3
Company: TechCorp | Market Cap: Mega Cap | Annual Revenue (B): 119.33 | Quarter: Q2
Company: FinanceWorks | Market Cap: Large Cap | Annual Revenue (B): 125.42 | Quarter: Q3
Company: RetailHub | Market Cap: Mid Cap | Annual Revenue (B): 471.69 | Quarter: Q1
<end>Here's some yaml data, can you convert it to Markdown?
- Device ID: device-0058
  Device Type: Light Sensor
  Location: Garage
  Timestamp: '2022-07-18 12:35:16'
- Device ID: device-0031
  Device Type: Pressure Sensor
  Location: Garage
  Timestamp: '2022-02-25 03:19:07'
- Device ID: device-0040
  Device Type: Pressure Sensor
  Location: Bedroom
  Timestamp: '2023-06-08 15:54:43'
- Device ID: device-0087
  Device Type: Motion Detector
  Location: Garage
  Timestamp: '2021-07-19 09:12:54'
<start>
| Device ID | Device Type | Location | Timestamp |
| --- | --- | --- | --- |
| device-0058 | Light Sensor | Garage | 2022-07-18 12:35:16 |
| device-0031 | Pressure Sensor | Garage | 2022-02-25 03:19:07 |
| device-0040 | Pressure Sensor | Bedroom | 2023-06-08 15:54:43 |
| device-0087 | Motion Detector | Garage | 2021-07-19 09:12:54 |
<end>Transform this Csv structure to a yaml format:
Birth Month,City,Income
April,Phoenix,480000
August,Nashville,105000
December,Chicago,485000
March,Washington,375000
December,Indianapolis,430000
March,Chicago,45000
February,Boston,75000
April,San Antonio,355000
<start>
- Birth Month: April
  City: Phoenix
  Income: 480000
- Birth Month: August
  City: Nashville
  Income: 105000
- Birth Month: December
  City: Chicago
  Income: 485000
- Birth Month: March
  City: Washington
  Income: 375000
- Birth Month: December
  City: Indianapolis
  Income: 430000
- Birth Month: March
  City: Chicago
  Income: 45000
- Birth Month: February
  City: Boston
  Income: 75000
- Birth Month: April
  City: San Antonio
  Income: 355000
<end>Convert this markdown to csv:
| Open Price | Close Price | High Price | Volume |
| --- | --- | --- | --- |
| 165.25 | 1198.76 | 1422.58 | 2767696 |
| 911.2 | 396.18 | 1171.24 | 1549864 |
| 501.83 | 502.05 | 502.05 | 8085956 |
| 366.97 | 1106.79 | 1106.79 | 511635 |
| 911.2 | 373.92 | 911.2 | 9044982 |
| 937.65 | 1344.06 | 1396.39 | 1688106 |<start>
Open Price,Close Price,High Price,Volume
165.25,1198.76,1422.58,2767696
911.2,396.18,1171.24,1549864
501.83,502.05,502.05,8085956
366.97,1106.79,1106.79,511635
911.2,373.92,911.2,9044982
937.65,1344.06,1396.39,1688106
<end>Convert this Json to csv:
[
    {
        "Location": "Chicago",
        "Humidity (%)": 24,
        "Wind Speed (km/h)": 1.8,
        "Day": "Sunday"
    },
    {
        "Location": "Phoenix",
        "Humidity (%)": 68,
        "Wind Speed (km/h)": 18.1,
        "Day": "Wednesday"
    },
    {
        "Location": "Los Angeles",
        "Humidity (%)": 87,
        "Wind Speed (km/h)": 22.5,
        "Day": "Friday"
    }
]<start>
Location,Humidity (%),Wind Speed (km/h),Day
Chicago,24,1.8,Sunday
Phoenix,68,18.1,Wednesday
Los Angeles,87,22.5,Friday
<end>Convert this csv to yaml:
SKU,Price,Supplier Name
SKU-1026,236.51,Wayne Enterprises
SKU-1016,363.37,Umbrella Corp
SKU-1094,308.07,Umbrella Corp
<start>
- Price: 236.51
  SKU: SKU-1026
  Supplier Name: Wayne Enterprises
- Price: 363.37
  SKU: SKU-1016
  Supplier Name: Umbrella Corp
- Price: 308.07
  SKU: SKU-1094
  Supplier Name: Umbrella Corp
<end>Please transform the following PLAIN TEXT data into markdown:
Company: HealthGen | Date: 2021-11-01 | Open Price: 246.91 | Close Price: 75.38 | High Price: 1294.3 | Low Price: 75.38 | Volume: 7026891
Company: TechnoCorp | Date: 2010-08-26 | Open Price: 348.3 | Close Price: 49.61 | High Price: 1225.93 | Low Price: 49.61 | Volume: 7553923
Company: HealthGen | Date: 2014-07-10 | Open Price: 259.05 | Close Price: 277.97 | High Price: 440.05 | Low Price: 259.05 | Volume: 9984327
Company: FinanceTrust | Date: 2012-08-22 | Open Price: 775.37 | Close Price: 515.74 | High Price: 775.37 | Low Price: 496.5 | Volume: 2680433
Company: BioLife | Date: 2016-03-22 | Open Price: 911.23 | Close Price: 1074.9 | High Price: 1077.7 | Low Price: 88.71 | Volume: 5380098
Company: HealthGen | Date: 2018-11-27 | Open Price: 1084.27 | Close Price: 472.45 | High Price: 1488.47 | Low Price: 472.45 | Volume: 9036490
Company: TechnoCorp | Date: 2020-03-01 | Open Price: 1153.29 | Close Price: 412.47 | High Price: 1153.29 | Low Price: 412.47 | Volume: 7013306
<start>
| Company | Date | Open Price | Close Price | High Price | Low Price | Volume |
| --- | --- | --- | --- | --- | --- | --- |
| HealthGen | 2021-11-01 | 246.91 | 75.38 | 1294.3 | 75.38 | 7026891 |
| TechnoCorp | 2010-08-26 | 348.3 | 49.61 | 1225.93 | 49.61 | 7553923 |
| HealthGen | 2014-07-10 | 259.05 | 277.97 | 440.05 | 259.05 | 9984327 |
| FinanceTrust | 2012-08-22 | 775.37 | 515.74 | 775.37 | 496.5 | 2680433 |
| BioLife | 2016-03-22 | 911.23 | 1074.9 | 1077.7 | 88.71 | 5380098 |
| HealthGen | 2018-11-27 | 1084.27 | 472.45 | 1488.47 | 472.45 | 9036490 |
| TechnoCorp | 2020-03-01 | 1153.29 | 412.47 | 1153.29 | 412.47 | 7013306 |
<end>Please transform the following YML data into Plain text:
- Company: TechnoCorp
  High Price: 1376.55
  Low Price: 797.76
  Open Price: 981.69
  Volume: 8063798
- Company: GreenEnergy
  High Price: 1345.37
  Low Price: 390.65
  Open Price: 1345.37
  Volume: 9841747
- Company: MediaGroup
  High Price: 1135.27
  Low Price: 157.13
  Open Price: 1135.27
  Volume: 7148605
- Company: HealthGen
  High Price: 1344.47
  Low Price: 21.19
  Open Price: 1026.76
  Volume: 2247246
- Company: BioLife
  High Price: 813.79
  Low Price: 381.06
  Open Price: 425.41
  Volume: 149784
- Company: AeroSystems
  High Price: 1344.47
  Low Price: 345.22
  Open Price: 1344.47
  Volume: 4741057
<start>
Company: TechnoCorp | Open Price: 981.69 | High Price: 1376.55 | Low Price: 797.76 | Volume: 8063798
Company: GreenEnergy | Open Price: 1345.37 | High Price: 1345.37 | Low Price: 390.65 | Volume: 9841747
Company: MediaGroup | Open Price: 1135.27 | High Price: 1135.27 | Low Price: 157.13 | Volume: 7148605
Company: HealthGen | Open Price: 1026.76 | High Price: 1344.47 | Low Price: 21.19 | Volume: 2247246
Company: BioLife | Open Price: 425.41 | High Price: 813.79 | Low Price: 381.06 | Volume: 149784
Company: AeroSystems | Open Price: 1344.47 | High Price: 1344.47 | Low Price: 345.22 | Volume: 4741057
<end>Can you change this yaml into csv?
- Battery Level (%): 15.1
  Device ID: device-0026
  Reading Value: 33.39
  Timestamp: '2022-02-12 22:11:02'
- Battery Level (%): 99.2
  Device ID: device-0003
  Reading Value: 34.36
  Timestamp: '2023-07-01 15:42:36'
- Battery Level (%): 58.3
  Device ID: device-0020
  Reading Value: 81.33
  Timestamp: '2022-07-13 14:44:04'
- Battery Level (%): 37.9
  Device ID: device-0009
  Reading Value: 29.02
  Timestamp: '2022-03-16 14:32:37'
- Battery Level (%): 82.6
  Device ID: device-0045
  Reading Value: 17.86
  Timestamp: '2022-10-12 21:29:01'
- Battery Level (%): 52.2
  Device ID: device-0030
  Reading Value: 77.73
  Timestamp: '2021-01-16 15:58:19'
- Battery Level (%): 79.8
  Device ID: device-0090
  Reading Value: 52.23
  Timestamp: '2022-11-27 17:39:22'
- Battery Level (%): 34.0
  Device ID: device-0098
  Reading Value: 64.16
  Timestamp: '2023-12-05 22:24:45'
<start>
Device ID,Battery Level (%),Reading Value,Timestamp
device-0026,15.1,33.39,2022-02-12 22:11:02
device-0003,99.2,34.36,2023-07-01 15:42:36
device-0020,58.3,81.33,2022-07-13 14:44:04
device-0009,37.9,29.02,2022-03-16 14:32:37
device-0045,82.6,17.86,2022-10-12 21:29:01
device-0030,52.2,77.73,2021-01-16 15:58:19
device-0090,79.8,52.23,2022-11-27 17:39:22
device-0098,34.0,64.16,2023-12-05 22:24:45
<end>Here's some CSV data, can you convert it to YML?
Company,Date,Open Price,Close Price,High Price,Low Price,Volume
GreenEnergy,2011-04-19,133.46,713.9,713.9,133.46,5186447
HealthGen,2017-04-07,1144.91,539.17,1144.91,539.17,560117
RetailWorld,2023-05-11,44.49,1484.3,1491.47,44.49,6801757
<start>
- Close Price: 713.9
  Company: GreenEnergy
  Date: '2011-04-19'
  High Price: 713.9
  Low Price: 133.46
  Open Price: 133.46
  Volume: 5186447
- Close Price: 539.17
  Company: HealthGen
  Date: '2017-04-07'
  High Price: 1144.91
  Low Price: 539.17
  Open Price: 1144.91
  Volume: 560117
- Close Price: 1484.3
  Company: RetailWorld
  Date: '2023-05-11'
  High Price: 1491.47
  Low Price: 44.49
  Open Price: 44.49
  Volume: 6801757
<end>Can you change this csv into markdown?
Company,Sector,Annual Revenue (B)
AeroSpace,Healthcare,152.85
GlobalTrade,Biotech,312.53
BioPharm,Biotech,90.28
GlobalTrade,Energy,56.86
AutoDrive,Healthcare,61.1
TechCorp,Automotive,90.28
EcoEnergy,Healthcare,286.39
TechCorp,Technology,272.13
TechCorp,Healthcare,351.67
<start>
| Company | Sector | Annual Revenue (B) |
| --- | --- | --- |
| AeroSpace | Healthcare | 152.85 |
| GlobalTrade | Biotech | 312.53 |
| BioPharm | Biotech | 90.28 |
| GlobalTrade | Energy | 56.86 |
| AutoDrive | Healthcare | 61.1 |
| TechCorp | Automotive | 90.28 |
| EcoEnergy | Healthcare | 286.39 |
| TechCorp | Technology | 272.13 |
| TechCorp | Healthcare | 351.67 |
<end>Can you change this json into PLAIN TEXT?
[
    {
        "Trip Name": "Forest Journey",
        "End Location": "Los Angeles",
        "Distance (miles)": 63.1,
        "Duration (hours)": 17.1,
        "Fuel Used (gallons)": 62.2
    },
    {
        "Trip Name": "Forest Journey",
        "End Location": "Los Angeles",
        "Distance (miles)": 2379.0,
        "Duration (hours)": 17.6,
        "Fuel Used (gallons)": 47.3
    },
    {
        "Trip Name": "City Explorer",
        "End Location": "Chicago",
        "Distance (miles)": 1164.7,
        "Duration (hours)": 11.4,
        "Fuel Used (gallons)": 79.8
    },
    {
        "Trip Name": "City Explorer",
        "End Location": "Chicago",
        "Distance (miles)": 1869.4,
        "Duration (hours)": 41.0,
        "Fuel Used (gallons)": 29.1
    },
    {
        "Trip Name": "Canyon Trek",
        "End Location": "Phoenix",
        "Distance (miles)": 2801.5,
        "Duration (hours)": 65.2,
        "Fuel Used (gallons)": 27.1
    },
    {
        "Trip Name": "Canyon Trek",
        "End Location": "Chicago",
        "Distance (miles)": 1509.8,
        "Duration (hours)": 35.2,
        "Fuel Used (gallons)": 14.0
    }
]<start>
Trip Name: Forest Journey | End Location: Los Angeles | Distance (miles): 63.1 | Duration (hours): 17.1 | Fuel Used (gallons): 62.2
Trip Name: Forest Journey | End Location: Los Angeles | Distance (miles): 2379.0 | Duration (hours): 17.6 | Fuel Used (gallons): 47.3
Trip Name: City Explorer | End Location: Chicago | Distance (miles): 1164.7 | Duration (hours): 11.4 | Fuel Used (gallons): 79.8
Trip Name: City Explorer | End Location: Chicago | Distance (miles): 1869.4 | Duration (hours): 41.0 | Fuel Used (gallons): 29.1
Trip Name: Canyon Trek | End Location: Phoenix | Distance (miles): 2801.5 | Duration (hours): 65.2 | Fuel Used (gallons): 27.1
Trip Name: Canyon Trek | End Location: Chicago | Distance (miles): 1509.8 | Duration (hours): 35.2 | Fuel Used (gallons): 14.0
<end>Here's some csv data, can you convert it to yml?
End Location,Distance (miles),Fuel Used (gallons)
Miami,1268.9,97.0
San Francisco,2595.5,38.5
San Francisco,1564.5,31.6
Chicago,2768.4,18.5
New York,2768.4,69.4
Los Angeles,101.8,35.6
Phoenix,2801.5,64.0
New York,2408.6,77.0
<start>
- Distance (miles): 1268.9
  End Location: Miami
  Fuel Used (gallons): 97.0
- Distance (miles): 2595.5
  End Location: San Francisco
  Fuel Used (gallons): 38.5
- Distance (miles): 1564.5
  End Location: San Francisco
  Fuel Used (gallons): 31.6
- Distance (miles): 2768.4
  End Location: Chicago
  Fuel Used (gallons): 18.5
- Distance (miles): 2768.4
  End Location: New York
  Fuel Used (gallons): 69.4
- Distance (miles): 101.8
  End Location: Los Angeles
  Fuel Used (gallons): 35.6
- Distance (miles): 2801.5
  End Location: Phoenix
  Fuel Used (gallons): 64.0
- Distance (miles): 2408.6
  End Location: New York
  Fuel Used (gallons): 77.0
<end>Transform this MARKDOWN structure to a json format:
| Company | Sector | Market Cap | Stock Price | Annual Revenue (B) | Quarter |
| --- | --- | --- | --- | --- | --- |
| HealthPlus | Finance | Mega Cap | 49.02 | 279.5 | Q1 |
| Foodies | Biotech | Small Cap | 991.83 | 184.85 | Q3 |
| GlobalTrade | Finance | Small Cap | 310.43 | 392.34 | Q3 |
| TechCorp | Finance | Small Cap | 839.85 | 192.43 | Q2 |
| EcoEnergy | Technology | Small Cap | 135.94 | 336.29 | Q4 |
| AutoDrive | Retail | Large Cap | 729.36 | 224.57 | Q3 |
| HealthPlus | Biotech | Small Cap | 533.41 | 209.56 | Q2 |
| GlobalTrade | Automotive | Mid Cap | 522.17 | 296.07 | Q3 |<start>
[
    {
        "Company": "HealthPlus",
        "Sector": "Finance",
        "Market Cap": "Mega Cap",
        "Stock Price": 49.02,
        "Annual Revenue (B)": 279.5,
        "Quarter": "Q1"
    },
    {
        "Company": "Foodies",
        "Sector": "Biotech",
        "Market Cap": "Small Cap",
        "Stock Price": 991.83,
        "Annual Revenue (B)": 184.85,
        "Quarter": "Q3"
    },
    {
        "Company": "GlobalTrade",
        "Sector": "Finance",
        "Market Cap": "Small Cap",
        "Stock Price": 310.43,
        "Annual Revenue (B)": 392.34,
        "Quarter": "Q3"
    },
    {
        "Company": "TechCorp",
        "Sector": "Finance",
        "Market Cap": "Small Cap",
        "Stock Price": 839.85,
        "Annual Revenue (B)": 192.43,
        "Quarter": "Q2"
    },
    {
        "Company": "EcoEnergy",
        "Sector": "Technology",
        "Market Cap": "Small Cap",
        "Stock Price": 135.94,
        "Annual Revenue (B)": 336.29,
        "Quarter": "Q4"
    },
    {
        "Company": "AutoDrive",
        "Sector": "Retail",
        "Market Cap": "Large Cap",
        "Stock Price": 729.36,
        "Annual Revenue (B)": 224.57,
        "Quarter": "Q3"
    },
    {
        "Company": "HealthPlus",
        "Sector": "Biotech",
        "Market Cap": "Small Cap",
        "Stock Price": 533.41,
        "Annual Revenue (B)": 209.56,
        "Quarter": "Q2"
    },
    {
        "Company": "GlobalTrade",
        "Sector": "Automotive",
        "Market Cap": "Mid Cap",
        "Stock Price": 522.17,
        "Annual Revenue (B)": 296.07,
        "Quarter": "Q3"
    }
]
<end>Please transform the following json data into CSV:
[
    {
        "Location": "Houston",
        "Condition": "Stormy",
        "Temperature (C)": -3.5,
        "Humidity (%)": 98,
        "Wind Speed (km/h)": 6.1,
        "Day": "Monday"
    },
    {
        "Location": "Phoenix",
        "Condition": "Snowy",
        "Temperature (C)": 15.3,
        "Humidity (%)": 62,
        "Wind Speed (km/h)": 16.2,
        "Day": "Tuesday"
    },
    {
        "Location": "Phoenix",
        "Condition": "Rainy",
        "Temperature (C)": 2.4,
        "Humidity (%)": 61,
        "Wind Speed (km/h)": 11.9,
        "Day": "Saturday"
    }
]<start>
Location,Condition,Temperature (C),Humidity (%),Wind Speed (km/h),Day
Houston,Stormy,-3.5,98,6.1,Monday
Phoenix,Snowy,15.3,62,16.2,Tuesday
Phoenix,Rainy,2.4,61,11.9,Saturday
<end>Transform this yml structure to a Json format:
- Device Type: Light Sensor
  Location: Living Room
  Reading Value: -32.4
- Device Type: Humidity Sensor
  Location: Garage
  Reading Value: 78.14
- Device Type: Light Sensor
  Location: Garage
  Reading Value: -15.88
- Device Type: Humidity Sensor
  Location: Office
  Reading Value: 16.77
- Device Type: Light Sensor
  Location: Bedroom
  Reading Value: 72.14
<start>
[
    {
        "Device Type": "Light Sensor",
        "Location": "Living Room",
        "Reading Value": -32.4
    },
    {
        "Device Type": "Humidity Sensor",
        "Location": "Garage",
        "Reading Value": 78.14
    },
    {
        "Device Type": "Light Sensor",
        "Location": "Garage",
        "Reading Value": -15.88
    },
    {
        "Device Type": "Humidity Sensor",
        "Location": "Office",
        "Reading Value": 16.77
    },
    {
        "Device Type": "Light Sensor",
        "Location": "Bedroom",
        "Reading Value": 72.14
    }
]
<end>Transform this json structure to a PLAIN TEXT format:
[
    {
        "Start Location": "Phoenix",
        "Distance (miles)": 2172.4,
        "Duration (hours)": 40.9,
        "Fuel Used (gallons)": 60.8
    },
    {
        "Start Location": "Chicago",
        "Distance (miles)": 2985.8,
        "Duration (hours)": 23.1,
        "Fuel Used (gallons)": 42.5
    },
    {
        "Start Location": "Los Angeles",
        "Distance (miles)": 2787.5,
        "Duration (hours)": 49.3,
        "Fuel Used (gallons)": 44.3
    },
    {
        "Start Location": "Los Angeles",
        "Distance (miles)": 2148.1,
        "Duration (hours)": 65.2,
        "Fuel Used (gallons)": 46.8
    },
    {
        "Start Location": "Chicago",
        "Distance (miles)": 860.2,
        "Duration (hours)": 8.7,
        "Fuel Used (gallons)": 14.6
    },
    {
        "Start Location": "Los Angeles",
        "Distance (miles)": 2029.1,
        "Duration (hours)": 17.1,
        "Fuel Used (gallons)": 19.6
    },
    {
        "Start Location": "Los Angeles",
        "Distance (miles)": 296.1,
        "Duration (hours)": 65.2,
        "Fuel Used (gallons)": 21.4
    }
]<start>
Start Location: Phoenix | Distance (miles): 2172.4 | Duration (hours): 40.9 | Fuel Used (gallons): 60.8
Start Location: Chicago | Distance (miles): 2985.8 | Duration (hours): 23.1 | Fuel Used (gallons): 42.5
Start Location: Los Angeles | Distance (miles): 2787.5 | Duration (hours): 49.3 | Fuel Used (gallons): 44.3
Start Location: Los Angeles | Distance (miles): 2148.1 | Duration (hours): 65.2 | Fuel Used (gallons): 46.8
Start Location: Chicago | Distance (miles): 860.2 | Duration (hours): 8.7 | Fuel Used (gallons): 14.6
Start Location: Los Angeles | Distance (miles): 2029.1 | Duration (hours): 17.1 | Fuel Used (gallons): 19.6
Start Location: Los Angeles | Distance (miles): 296.1 | Duration (hours): 65.2 | Fuel Used (gallons): 21.4
<end>Convert this MARKDOWN to Plain text:
| Restaurant Name | Cuisine | Rating | Price Range |
| --- | --- | --- | --- |
| Curry Corner | French | 4 | $$$$$ |
| The Golden Spoon | Indian | 2 | $ |
| The Golden Spoon | Mexican | 3 | $$$$$ |
| The Golden Spoon | Japanese | 3 | $$ |
| Taco Town | Chinese | 1 | $$$$$ |
| Taco Town | American | 1 | $$$ |
| Sushi World | French | 1 | $ |
| The Steakhouse | Indian | 4 | $$ |<start>
Restaurant Name: Curry Corner | Cuisine: French | Rating: 4 | Price Range: $$$$$
Restaurant Name: The Golden Spoon | Cuisine: Indian | Rating: 2 | Price Range: $
Restaurant Name: The Golden Spoon | Cuisine: Mexican | Rating: 3 | Price Range: $$$$$
Restaurant Name: The Golden Spoon | Cuisine: Japanese | Rating: 3 | Price Range: $$
Restaurant Name: Taco Town | Cuisine: Chinese | Rating: 1 | Price Range: $$$$$
Restaurant Name: Taco Town | Cuisine: American | Rating: 1 | Price Range: $$$
Restaurant Name: Sushi World | Cuisine: French | Rating: 1 | Price Range: $
Restaurant Name: The Steakhouse | Cuisine: Indian | Rating: 4 | Price Range: $$
<end>Can you change this Plain text into json?
Trip Name: Historic Route | Start Location: Miami | End Location: Chicago | Distance (miles): 698.4 | Duration (hours): 61.6 | Fuel Used (gallons): 68.4
Trip Name: Desert Drive | Start Location: New York | End Location: Denver | Distance (miles): 1596.9 | Duration (hours): 59.5 | Fuel Used (gallons): 53.0
Trip Name: City Explorer | Start Location: Los Angeles | End Location: Denver | Distance (miles): 1279.3 | Duration (hours): 48.9 | Fuel Used (gallons): 30.0
<start>
[
    {
        "Trip Name": "Historic Route",
        "Start Location": "Miami",
        "End Location": "Chicago",
        "Distance (miles)": 698.4,
        "Duration (hours)": 61.6,
        "Fuel Used (gallons)": 68.4
    },
    {
        "Trip Name": "Desert Drive",
        "Start Location": "New York",
        "End Location": "Denver",
        "Distance (miles)": 1596.9,
        "Duration (hours)": 59.5,
        "Fuel Used (gallons)": 53.0
    },
    {
        "Trip Name": "City Explorer",
        "Start Location": "Los Angeles",
        "End Location": "Denver",
        "Distance (miles)": 1279.3,
        "Duration (hours)": 48.9,
        "Fuel Used (gallons)": 30.0
    }
]
<end>Can you change this Json into plain text?
[
    {
        "Cuisine": "Italian",
        "Rating": 5
    },
    {
        "Cuisine": "Mediterranean",
        "Rating": 2
    },
    {
        "Cuisine": "Japanese",
        "Rating": 3
    },
    {
        "Cuisine": "Japanese",
        "Rating": 4
    }
]<start>
Cuisine: Italian | Rating: 5
Cuisine: Mediterranean | Rating: 2
Cuisine: Japanese | Rating: 3
Cuisine: Japanese | Rating: 4
<end>Can you change this plain text into CSV?
Company: RetailHub | Stock Price: 533.91 | Annual Revenue (B): 256.85 | Quarter: Q3
Company: BioPharm | Stock Price: 498.92 | Annual Revenue (B): 101.65 | Quarter: Q3
Company: FinanceWorks | Stock Price: 556.82 | Annual Revenue (B): 346.22 | Quarter: Q3
Company: Foodies | Stock Price: 383.75 | Annual Revenue (B): 162.78 | Quarter: Q3
Company: FinanceWorks | Stock Price: 454.26 | Annual Revenue (B): 121.91 | Quarter: Q1
Company: Foodies | Stock Price: 273.91 | Annual Revenue (B): 115.67 | Quarter: Q3
Company: BioPharm | Stock Price: 703.11 | Annual Revenue (B): 418.5 | Quarter: Q2
Company: RetailHub | Stock Price: 31.93 | Annual Revenue (B): 346.22 | Quarter: Q2
Company: EcoEnergy | Stock Price: 862.41 | Annual Revenue (B): 86.28 | Quarter: Q2
<start>
Company,Stock Price,Annual Revenue (B),Quarter
RetailHub,533.91,256.85,Q3
BioPharm,498.92,101.65,Q3
FinanceWorks,556.82,346.22,Q3
Foodies,383.75,162.78,Q3
FinanceWorks,454.26,121.91,Q1
Foodies,273.91,115.67,Q3
BioPharm,703.11,418.5,Q2
RetailHub,31.93,346.22,Q2
EcoEnergy,862.41,86.28,Q2
<end>Here's some plain text data, can you convert it to Csv?
Name: Adrienne | Age: 32 | Birth Month: March | City: Nashville | Income: 255000
Name: Tracy | Age: 29 | Birth Month: February | City: El Paso | Income: 480000
Name: Owen | Age: 42 | Birth Month: July | City: Detroit | Income: 85000
Name: Diana | Age: 36 | Birth Month: August | City: Fort Worth | Income: 490000
Name: Miguel | Age: 36 | Birth Month: November | City: San Diego | Income: 220000
Name: Silas | Age: 34 | Birth Month: August | City: Phoenix | Income: 100000
Name: Edwin | Age: 50 | Birth Month: January | City: Houston | Income: 470000
<start>
Name,Age,Birth Month,City,Income
Adrienne,32,March,Nashville,255000
Tracy,29,February,El Paso,480000
Owen,42,July,Detroit,85000
Diana,36,August,Fort Worth,490000
Miguel,36,November,San Diego,220000
Silas,34,August,Phoenix,100000
Edwin,50,January,Houston,470000
<end>Convert this markdown to plain text:
| Author | Publication Year | Rating |
| --- | --- | --- |
| Elara Moonshadow | 1994 | 2.6 |
| Orion Frostblade | 2020 | 3.5 |
| Luna Silverleaf | 1967 | 3.6 |
| Elara Moonshadow | 2013 | 2.5 |
| Orion Frostblade | 1981 | 2.2 |
| Draven Blackthorn | 2007 | 3.6 |
| Orion Frostblade | 1965 | 2.8 |
| Sylvia Nightshade | 2007 | 4.5 |
| Orion Frostblade | 1967 | 4.5 |
| Draven Blackthorn | 1978 | 1.2 |<start>
Author: Elara Moonshadow | Publication Year: 1994 | Rating: 2.6
Author: Orion Frostblade | Publication Year: 2020 | Rating: 3.5
Author: Luna Silverleaf | Publication Year: 1967 | Rating: 3.6
Author: Elara Moonshadow | Publication Year: 2013 | Rating: 2.5
Author: Orion Frostblade | Publication Year: 1981 | Rating: 2.2
Author: Draven Blackthorn | Publication Year: 2007 | Rating: 3.6
Author: Orion Frostblade | Publication Year: 1965 | Rating: 2.8
Author: Sylvia Nightshade | Publication Year: 2007 | Rating: 4.5
Author: Orion Frostblade | Publication Year: 1967 | Rating: 4.5
Author: Draven Blackthorn | Publication Year: 1978 | Rating: 1.2
<end>Can you change this MARKDOWN into csv?
| Name | Age |
| --- | --- |
| Joyce | 65 |
| Liam | 50 |
| Walter | 35 |
| Sidney | 19 |<start>
Name,Age
Joyce,65
Liam,50
Walter,35
Sidney,19
<end>Convert this Yaml to plain text:
- Company: FinanceTrust
  Date: '2021-05-15'
  Low Price: 563.8
  Open Price: 563.8
  Volume: 7160108
- Company: TechnoCorp
  Date: '2016-06-08'
  Low Price: 1000.73
  Open Price: 1456.94
  Volume: 3396129
- Company: AutoMotive
  Date: '2010-06-01'
  Low Price: 654.9
  Open Price: 758.81
  Volume: 1626974
- Company: BioLife
  Date: '2015-08-27'
  Low Price: 132.45
  Open Price: 654.9
  Volume: 9456532
<start>
Company: FinanceTrust | Date: 2021-05-15 | Open Price: 563.8 | Low Price: 563.8 | Volume: 7160108
Company: TechnoCorp | Date: 2016-06-08 | Open Price: 1456.94 | Low Price: 1000.73 | Volume: 3396129
Company: AutoMotive | Date: 2010-06-01 | Open Price: 758.81 | Low Price: 654.9 | Volume: 1626974
Company: BioLife | Date: 2015-08-27 | Open Price: 654.9 | Low Price: 132.45 | Volume: 9456532
<end>Transform this Csv structure to a Markdown format:
Release Year,Box Office Earnings (M)
2009,45.33
2006,993.8
2004,306.23
<start>
| Release Year | Box Office Earnings (M) |
| --- | --- |
| 2009 | 45.33 |
| 2006 | 993.8 |
| 2004 | 306.23 |
<end>Please transform the following Plain text data into json:
End Location: Miami | Duration (hours): 4.2 | Fuel Used (gallons): 24.9
End Location: Los Angeles | Duration (hours): 71.1 | Fuel Used (gallons): 57.0
End Location: Chicago | Duration (hours): 23.4 | Fuel Used (gallons): 80.6
End Location: Chicago | Duration (hours): 16.7 | Fuel Used (gallons): 37.3
End Location: Phoenix | Duration (hours): 33.4 | Fuel Used (gallons): 32.1
End Location: Los Angeles | Duration (hours): 38.5 | Fuel Used (gallons): 21.4
End Location: Houston | Duration (hours): 72.0 | Fuel Used (gallons): 77.2
<start>
[
    {
        "End Location": "Miami",
        "Duration (hours)": 4.2,
        "Fuel Used (gallons)": 24.9
    },
    {
        "End Location": "Los Angeles",
        "Duration (hours)": 71.1,
        "Fuel Used (gallons)": 57.0
    },
    {
        "End Location": "Chicago",
        "Duration (hours)": 23.4,
        "Fuel Used (gallons)": 80.6
    },
    {
        "End Location": "Chicago",
        "Duration (hours)": 16.7,
        "Fuel Used (gallons)": 37.3
    },
    {
        "End Location": "Phoenix",
        "Duration (hours)": 33.4,
        "Fuel Used (gallons)": 32.1
    },
    {
        "End Location": "Los Angeles",
        "Duration (hours)": 38.5,
        "Fuel Used (gallons)": 21.4
    },
    {
        "End Location": "Houston",
        "Duration (hours)": 72.0,
        "Fuel Used (gallons)": 77.2
    }
]
<end>Please transform the following YAML data into markdown:
- Cuisine: Mediterranean
  Location: Phoenix
  Price Range: $$$$
  Rating: 4
  Restaurant Name: The Steakhouse
- Cuisine: Chinese
  Location: Seattle
  Price Range: $
  Rating: 1
  Restaurant Name: The Steakhouse
- Cuisine: Italian
  Location: Chicago
  Price Range: $
  Rating: 3
  Restaurant Name: Vegan Delight
- Cuisine: Italian
  Location: Miami
  Price Range: $
  Rating: 2
  Restaurant Name: Pizza Planet
- Cuisine: Chinese
  Location: Chicago
  Price Range: $$
  Rating: 2
  Restaurant Name: The Steakhouse
- Cuisine: Mediterranean
  Location: Phoenix
  Price Range: $
  Rating: 5
  Restaurant Name: The Steakhouse
- Cuisine: Indian
  Location: New York
  Price Range: $$$$$
  Rating: 3
  Restaurant Name: Burger Haven
<start>
| Restaurant Name | Cuisine | Location | Rating | Price Range |
| --- | --- | --- | --- | --- |
| The Steakhouse | Mediterranean | Phoenix | 4 | $$$$ |
| The Steakhouse | Chinese | Seattle | 1 | $ |
| Vegan Delight | Italian | Chicago | 3 | $ |
| Pizza Planet | Italian | Miami | 2 | $ |
| The Steakhouse | Chinese | Chicago | 2 | $$ |
| The Steakhouse | Mediterranean | Phoenix | 5 | $ |
| Burger Haven | Indian | New York | 3 | $$$$$ |
<end>Transform this CSV structure to a Markdown format:
Location,Condition,Temperature (C),Humidity (%),Wind Speed (km/h),Day
Seattle,Windy,-9.2,20,2.5,Thursday
Seattle,Foggy,2.7,97,7.6,Saturday
Houston,Rainy,-1.6,64,24.1,Thursday
<start>
| Location | Condition | Temperature (C) | Humidity (%) | Wind Speed (km/h) | Day |
| --- | --- | --- | --- | --- | --- |
| Seattle | Windy | -9.2 | 20 | 2.5 | Thursday |
| Seattle | Foggy | 2.7 | 97 | 7.6 | Saturday |
| Houston | Rainy | -1.6 | 64 | 24.1 | Thursday |
<end>Convert this PLAIN TEXT to Json:
Title: Starbound Odyssey | Release Year: 2015 | Box Office Earnings (M): 310.6
Title: Mystery of the Depths | Release Year: 1970 | Box Office Earnings (M): 162.85
Title: Starbound Odyssey | Release Year: 2019 | Box Office Earnings (M): 214.18
<start>
[
    {
        "Title": "Starbound Odyssey",
        "Release Year": 2015,
        "Box Office Earnings (M)": 310.6
    },
    {
        "Title": "Mystery of the Depths",
        "Release Year": 1970,
        "Box Office Earnings (M)": 162.85
    },
    {
        "Title": "Starbound Odyssey",
        "Release Year": 2019,
        "Box Office Earnings (M)": 214.18
    }
]
<end>Transform this markdown structure to a plain text format:
| Company | Sector | Market Cap | Stock Price | Annual Revenue (B) |
| --- | --- | --- | --- | --- |
| Foodies | Retail | Mega Cap | 57.48 | 403.03 |
| RetailHub | Aerospace | Large Cap | 254.29 | 211.84 |
| FinanceWorks | Aerospace | Large Cap | 795.27 | 90.93 |
| GlobalTrade | Biotech | Mid Cap | 715.54 | 117.9 |
| EcoEnergy | Retail | Large Cap | 229.67 | 52.19 |
| EcoEnergy | Technology | Mega Cap | 261.83 | 225.22 |<start>
Company: Foodies | Sector: Retail | Market Cap: Mega Cap | Stock Price: 57.48 | Annual Revenue (B): 403.03
Company: RetailHub | Sector: Aerospace | Market Cap: Large Cap | Stock Price: 254.29 | Annual Revenue (B): 211.84
Company: FinanceWorks | Sector: Aerospace | Market Cap: Large Cap | Stock Price: 795.27 | Annual Revenue (B): 90.93
Company: GlobalTrade | Sector: Biotech | Market Cap: Mid Cap | Stock Price: 715.54 | Annual Revenue (B): 117.9
Company: EcoEnergy | Sector: Retail | Market Cap: Large Cap | Stock Price: 229.67 | Annual Revenue (B): 52.19
Company: EcoEnergy | Sector: Technology | Market Cap: Mega Cap | Stock Price: 261.83 | Annual Revenue (B): 225.22
<end>Here's some plain text data, can you convert it to MARKDOWN?
Company: RetailWorld | Date: 2013-02-14 | Close Price: 214.22 | High Price: 1342.46 | Low Price: 214.22 | Volume: 3410353
Company: BioLife | Date: 2016-12-20 | Close Price: 1064.45 | High Price: 1064.45 | Low Price: 592.94 | Volume: 9939217
Company: FinanceTrust | Date: 2011-03-05 | Close Price: 602.67 | High Price: 1021.33 | Low Price: 99.33 | Volume: 4028084
Company: TechnoCorp | Date: 2015-02-14 | Close Price: 1087.01 | High Price: 1087.01 | Low Price: 112.51 | Volume: 2835703
Company: BioLife | Date: 2019-01-19 | Close Price: 1039.77 | High Price: 1039.77 | Low Price: 584.55 | Volume: 7116650
Company: FoodChain | Date: 2013-01-03 | Close Price: 1066.93 | High Price: 1066.93 | Low Price: 584.55 | Volume: 1261194
Company: GreenEnergy | Date: 2019-10-05 | Close Price: 1117.82 | High Price: 1117.82 | Low Price: 313.66 | Volume: 858335
Company: MediaGroup | Date: 2022-10-28 | Close Price: 802.29 | High Price: 1287.19 | Low Price: 791.63 | Volume: 8493530
Company: RetailWorld | Date: 2015-01-06 | Close Price: 1045.26 | High Price: 1045.26 | Low Price: 301.72 | Volume: 4009050
<start>
| Company | Date | Close Price | High Price | Low Price | Volume |
| --- | --- | --- | --- | --- | --- |
| RetailWorld | 2013-02-14 | 214.22 | 1342.46 | 214.22 | 3410353 |
| BioLife | 2016-12-20 | 1064.45 | 1064.45 | 592.94 | 9939217 |
| FinanceTrust | 2011-03-05 | 602.67 | 1021.33 | 99.33 | 4028084 |
| TechnoCorp | 2015-02-14 | 1087.01 | 1087.01 | 112.51 | 2835703 |
| BioLife | 2019-01-19 | 1039.77 | 1039.77 | 584.55 | 7116650 |
| FoodChain | 2013-01-03 | 1066.93 | 1066.93 | 584.55 | 1261194 |
| GreenEnergy | 2019-10-05 | 1117.82 | 1117.82 | 313.66 | 858335 |
| MediaGroup | 2022-10-28 | 802.29 | 1287.19 | 791.63 | 8493530 |
| RetailWorld | 2015-01-06 | 1045.26 | 1045.26 | 301.72 | 4009050 |
<end>Please transform the following PLAIN TEXT data into YML:
Company: EcoEnergy | Sector: Energy | Market Cap: Mid Cap | Stock Price: 336.26 | Annual Revenue (B): 63.05
Company: RetailHub | Sector: Retail | Market Cap: Mid Cap | Stock Price: 505.55 | Annual Revenue (B): 450.46
Company: BioPharm | Sector: Automotive | Market Cap: Small Cap | Stock Price: 984.89 | Annual Revenue (B): 250.92
Company: Foodies | Sector: Healthcare | Market Cap: Mid Cap | Stock Price: 35.55 | Annual Revenue (B): 109.6
Company: GlobalTrade | Sector: Biotech | Market Cap: Small Cap | Stock Price: 986.78 | Annual Revenue (B): 339.62
Company: AutoDrive | Sector: Finance | Market Cap: Mid Cap | Stock Price: 661.99 | Annual Revenue (B): 351.97
Company: EcoEnergy | Sector: Biotech | Market Cap: Large Cap | Stock Price: 846.54 | Annual Revenue (B): 342.19
<start>
- Annual Revenue (B): 63.05
  Company: EcoEnergy
  Market Cap: Mid Cap
  Sector: Energy
  Stock Price: 336.26
- Annual Revenue (B): 450.46
  Company: RetailHub
  Market Cap: Mid Cap
  Sector: Retail
  Stock Price: 505.55
- Annual Revenue (B): 250.92
  Company: BioPharm
  Market Cap: Small Cap
  Sector: Automotive
  Stock Price: 984.89
- Annual Revenue (B): 109.6
  Company: Foodies
  Market Cap: Mid Cap
  Sector: Healthcare
  Stock Price: 35.55
- Annual Revenue (B): 339.62
  Company: GlobalTrade
  Market Cap: Small Cap
  Sector: Biotech
  Stock Price: 986.78
- Annual Revenue (B): 351.97
  Company: AutoDrive
  Market Cap: Mid Cap
  Sector: Finance
  Stock Price: 661.99
- Annual Revenue (B): 342.19
  Company: EcoEnergy
  Market Cap: Large Cap
  Sector: Biotech
  Stock Price: 846.54
<end>Please transform the following yml data into PLAIN TEXT:
- Box Office Earnings (M): 986.8
  Genre: Sci-Fi
  Release Year: 2008
  Title: Rise of the Titans
- Box Office Earnings (M): 207.38
  Genre: Comedy
  Release Year: 2000
  Title: Starbound Odyssey
- Box Office Earnings (M): 986.8
  Genre: Horror
  Release Year: 2007
  Title: The Great Expedition
- Box Office Earnings (M): 887.26
  Genre: Comedy
  Release Year: 2013
  Title: The Endless Horizon
- Box Office Earnings (M): 284.48
  Genre: Action
  Release Year: 1991
  Title: Escape from Earth
<start>
Title: Rise of the Titans | Genre: Sci-Fi | Release Year: 2008 | Box Office Earnings (M): 986.8
Title: Starbound Odyssey | Genre: Comedy | Release Year: 2000 | Box Office Earnings (M): 207.38
Title: The Great Expedition | Genre: Horror | Release Year: 2007 | Box Office Earnings (M): 986.8
Title: The Endless Horizon | Genre: Comedy | Release Year: 2013 | Box Office Earnings (M): 887.26
Title: Escape from Earth | Genre: Action | Release Year: 1991 | Box Office Earnings (M): 284.48
<end>Convert this json to YML:
[
    {
        "Database Name": "SessionsDB",
        "Queries per Second": 3391.84,
        "Average Latency (ms)": 54.73,
        "Timestamp": "2023-08-07 12:34:01"
    },
    {
        "Database Name": "MetricsDB",
        "Queries per Second": 2861.25,
        "Average Latency (ms)": 92.99,
        "Timestamp": "2021-10-11 00:29:12"
    },
    {
        "Database Name": "SalesDB",
        "Queries per Second": 4465.38,
        "Average Latency (ms)": 5.99,
        "Timestamp": "2022-04-15 04:40:52"
    }
]<start>
- Average Latency (ms): 54.73
  Database Name: SessionsDB
  Queries per Second: 3391.84
  Timestamp: '2023-08-07 12:34:01'
- Average Latency (ms): 92.99
  Database Name: MetricsDB
  Queries per Second: 2861.25
  Timestamp: '2021-10-11 00:29:12'
- Average Latency (ms): 5.99
  Database Name: SalesDB
  Queries per Second: 4465.38
  Timestamp: '2022-04-15 04:40:52'
<end>Please transform the following Plain text data into json:
Name: Rena | Age: 54 | Income: 195000
Name: Kendall | Age: 20 | Income: 155000
Name: Hugh | Age: 48 | Income: 220000
Name: Bertie | Age: 45 | Income: 210000
Name: Bertie | Age: 43 | Income: 280000
Name: Ashton | Age: 46 | Income: 285000
<start>
[
    {
        "Name": "Rena",
        "Age": 54,
        "Income": 195000
    },
    {
        "Name": "Kendall",
        "Age": 20,
        "Income": 155000
    },
    {
        "Name": "Hugh",
        "Age": 48,
        "Income": 220000
    },
    {
        "Name": "Bertie",
        "Age": 45,
        "Income": 210000
    },
    {
        "Name": "Bertie",
        "Age": 43,
        "Income": 280000
    },
    {
        "Name": "Ashton",
        "Age": 46,
        "Income": 285000
    }
]
<end>Transform this MARKDOWN structure to a json format:
| Trip Name | Start Location | End Location | Duration (hours) | Fuel Used (gallons) |
| --- | --- | --- | --- | --- |
| Coast to Coast | San Francisco | New York | 38.4 | 8.9 |
| Lakeside Retreat | Denver | Phoenix | 12.7 | 67.2 |
| Historic Route | Denver | Chicago | 61.4 | 20.6 |
| Mountain Adventure | Chicago | Los Angeles | 70.3 | 82.4 |
| Valley Voyage | Denver | Chicago | 68.3 | 84.2 |
| Lakeside Retreat | New York | San Francisco | 5.4 | 63.4 |
| Lakeside Retreat | Chicago | Denver | 5.1 | 25.2 |
| Canyon Trek | New York | Los Angeles | 48.2 | 90.6 |
| Canyon Trek | Phoenix | San Francisco | 29.6 | 82.8 |<start>
[
    {
        "Trip Name": "Coast to Coast",
        "Start Location": "San Francisco",
        "End Location": "New York",
        "Duration (hours)": 38.4,
        "Fuel Used (gallons)": 8.9
    },
    {
        "Trip Name": "Lakeside Retreat",
        "Start Location": "Denver",
        "End Location": "Phoenix",
        "Duration (hours)": 12.7,
        "Fuel Used (gallons)": 67.2
    },
    {
        "Trip Name": "Historic Route",
        "Start Location": "Denver",
        "End Location": "Chicago",
        "Duration (hours)": 61.4,
        "Fuel Used (gallons)": 20.6
    },
    {
        "Trip Name": "Mountain Adventure",
        "Start Location": "Chicago",
        "End Location": "Los Angeles",
        "Duration (hours)": 70.3,
        "Fuel Used (gallons)": 82.4
    },
    {
        "Trip Name": "Valley Voyage",
        "Start Location": "Denver",
        "End Location": "Chicago",
        "Duration (hours)": 68.3,
        "Fuel Used (gallons)": 84.2
    },
    {
        "Trip Name": "Lakeside Retreat",
        "Start Location": "New York",
        "End Location": "San Francisco",
        "Duration (hours)": 5.4,
        "Fuel Used (gallons)": 63.4
    },
    {
        "Trip Name": "Lakeside Retreat",
        "Start Location": "Chicago",
        "End Location": "Denver",
        "Duration (hours)": 5.1,
        "Fuel Used (gallons)": 25.2
    },
    {
        "Trip Name": "Canyon Trek",
        "Start Location": "New York",
        "End Location": "Los Angeles",
        "Duration (hours)": 48.2,
        "Fuel Used (gallons)": 90.6
    },
    {
        "Trip Name": "Canyon Trek",
        "Start Location": "Phoenix",
        "End Location": "San Francisco",
        "Duration (hours)": 29.6,
        "Fuel Used (gallons)": 82.8
    }
]
<end>Can you change this Yml into markdown?
- Battery Level (%): 25.2
  Device ID: device-0036
  Device Type: Humidity Sensor
  Location: Garage
  Reading Value: 55.34
  Timestamp: '2022-05-06 07:02:21'
- Battery Level (%): 66.7
  Device ID: device-0057
  Device Type: Pressure Sensor
  Location: Garden
  Reading Value: 47.04
  Timestamp: '2022-11-22 04:57:06'
- Battery Level (%): 37.9
  Device ID: device-0044
  Device Type: Humidity Sensor
  Location: Hallway
  Reading Value: -20.02
  Timestamp: '2023-12-25 03:48:13'
- Battery Level (%): 75.5
  Device ID: device-0009
  Device Type: Pressure Sensor
  Location: Bedroom
  Reading Value: 25.14
  Timestamp: '2022-05-01 08:35:49'
- Battery Level (%): 24.3
  Device ID: device-0041
  Device Type: Pressure Sensor
  Location: Garden
  Reading Value: 78.77
  Timestamp: '2021-12-03 17:02:41'
<start>
| Device ID | Device Type | Location | Battery Level (%) | Reading Value | Timestamp |
| --- | --- | --- | --- | --- | --- |
| device-0036 | Humidity Sensor | Garage | 25.2 | 55.34 | 2022-05-06 07:02:21 |
| device-0057 | Pressure Sensor | Garden | 66.7 | 47.04 | 2022-11-22 04:57:06 |
| device-0044 | Humidity Sensor | Hallway | 37.9 | -20.02 | 2023-12-25 03:48:13 |
| device-0009 | Pressure Sensor | Bedroom | 75.5 | 25.14 | 2022-05-01 08:35:49 |
| device-0041 | Pressure Sensor | Garden | 24.3 | 78.77 | 2021-12-03 17:02:41 |
<end>Please transform the following yaml data into json:
- Author: Rowan Ashborne
  Genre: Non-Fiction
  Publication Year: 2000
  Rating: 3.6
  Title: Echoes of Eternity
- Author: Orion Frostblade
  Genre: Fantasy
  Publication Year: 2008
  Rating: 3.3
  Title: The Crystal Key
- Author: Sylvia Nightshade
  Genre: Non-Fiction
  Publication Year: 1992
  Rating: 1.6
  Title: Echoes of Eternity
- Author: Sylvia Nightshade
  Genre: Historical
  Publication Year: 2011
  Rating: 1.4
  Title: The Last Sky
- Author: Orion Frostblade
  Genre: Non-Fiction
  Publication Year: 2015
  Rating: 4.2
  Title: Echoes of Eternity
- Author: Rowan Ashborne
  Genre: Horror
  Publication Year: 1990
  Rating: 1.3
  Title: Shadows of Solitude
- Author: Orion Frostblade
  Genre: Romance
  Publication Year: 1997
  Rating: 3.3
  Title: The Forgotten World
- Author: Rowan Ashborne
  Genre: Historical
  Publication Year: 1981
  Rating: 1.1
  Title: Legends of the Rift
<start>
[
    {
        "Title": "Echoes of Eternity",
        "Author": "Rowan Ashborne",
        "Genre": "Non-Fiction",
        "Publication Year": 2000,
        "Rating": 3.6
    },
    {
        "Title": "The Crystal Key",
        "Author": "Orion Frostblade",
        "Genre": "Fantasy",
        "Publication Year": 2008,
        "Rating": 3.3
    },
    {
        "Title": "Echoes of Eternity",
        "Author": "Sylvia Nightshade",
        "Genre": "Non-Fiction",
        "Publication Year": 1992,
        "Rating": 1.6
    },
    {
        "Title": "The Last Sky",
        "Author": "Sylvia Nightshade",
        "Genre": "Historical",
        "Publication Year": 2011,
        "Rating": 1.4
    },
    {
        "Title": "Echoes of Eternity",
        "Author": "Orion Frostblade",
        "Genre": "Non-Fiction",
        "Publication Year": 2015,
        "Rating": 4.2
    },
    {
        "Title": "Shadows of Solitude",
        "Author": "Rowan Ashborne",
        "Genre": "Horror",
        "Publication Year": 1990,
        "Rating": 1.3
    },
    {
        "Title": "The Forgotten World",
        "Author": "Orion Frostblade",
        "Genre": "Romance",
        "Publication Year": 1997,
        "Rating": 3.3
    },
    {
        "Title": "Legends of the Rift",
        "Author": "Rowan Ashborne",
        "Genre": "Historical",
        "Publication Year": 1981,
        "Rating": 1.1
    }
]
<end>Transform this markdown structure to a yml format:
| Title | Director | Genre | Box Office Earnings (M) |
| --- | --- | --- | --- |
| Starbound Odyssey | Drake Nightshade | Sci-Fi | 187.42 |
| The Great Expedition | Aria Ravenwood | Drama | 150.84 |
| Edge of Infinity | Talon Blackthorn | Drama | 618.78 |
| Edge of Infinity | Zara Stormrider | Sci-Fi | 593.35 |
| Mystery of the Depths | Rylan Frostblade | Action | 206.01 |
| Rise of the Titans | Selene Darkwhisper | Action | 650.22 |
| Rise of the Titans | Lira Silverleaf | Horror | 46.02 |
| Edge of Infinity | Orin Shadowalker | Comedy | 32.76 |
| The Final Voyage | Mara Moonshadow | Drama | 17.1 |<start>
- Box Office Earnings (M): 187.42
  Director: Drake Nightshade
  Genre: Sci-Fi
  Title: Starbound Odyssey
- Box Office Earnings (M): 150.84
  Director: Aria Ravenwood
  Genre: Drama
  Title: The Great Expedition
- Box Office Earnings (M): 618.78
  Director: Talon Blackthorn
  Genre: Drama
  Title: Edge of Infinity
- Box Office Earnings (M): 593.35
  Director: Zara Stormrider
  Genre: Sci-Fi
  Title: Edge of Infinity
- Box Office Earnings (M): 206.01
  Director: Rylan Frostblade
  Genre: Action
  Title: Mystery of the Depths
- Box Office Earnings (M): 650.22
  Director: Selene Darkwhisper
  Genre: Action
  Title: Rise of the Titans
- Box Office Earnings (M): 46.02
  Director: Lira Silverleaf
  Genre: Horror
  Title: Rise of the Titans
- Box Office Earnings (M): 32.76
  Director: Orin Shadowalker
  Genre: Comedy
  Title: Edge of Infinity
- Box Office Earnings (M): 17.1
  Director: Mara Moonshadow
  Genre: Drama
  Title: The Final Voyage
<end>Please transform the following json data into CSV:
[
    {
        "Title": "The Forgotten World",
        "Genre": "Horror"
    },
    {
        "Title": "Echoes of Eternity",
        "Genre": "Historical"
    },
    {
        "Title": "Legends of the Rift",
        "Genre": "Fantasy"
    },
    {
        "Title": "Legends of the Rift",
        "Genre": "Science Fiction"
    },
    {
        "Title": "The Last Sky",
        "Genre": "Thriller"
    },
    {
        "Title": "Whispers of the Abyss",
        "Genre": "Non-Fiction"
    },
    {
        "Title": "The Crystal Key",
        "Genre": "Fantasy"
    },
    {
        "Title": "The Forgotten World",
        "Genre": "Mystery"
    },
    {
        "Title": "The Last Sky",
        "Genre": "Horror"
    },
    {
        "Title": "The Last Sky",
        "Genre": "Historical"
    }
]<start>
Title,Genre
The Forgotten World,Horror
Echoes of Eternity,Historical
Legends of the Rift,Fantasy
Legends of the Rift,Science Fiction
The Last Sky,Thriller
Whispers of the Abyss,Non-Fiction
The Crystal Key,Fantasy
The Forgotten World,Mystery
The Last Sky,Horror
The Last Sky,Historical
<end>Please transform the following CSV data into JSON:
Company,Sector,Market Cap,Stock Price,Annual Revenue (B),Quarter
AeroSpace,Technology,Small Cap,317.12,108.4,Q2
EcoEnergy,Aerospace,Small Cap,555.55,346.47,Q1
GlobalTrade,Biotech,Mid Cap,936.75,161.2,Q4
<start>
[
    {
        "Company": "AeroSpace",
        "Sector": "Technology",
        "Market Cap": "Small Cap",
        "Stock Price": 317.12,
        "Annual Revenue (B)": 108.4,
        "Quarter": "Q2"
    },
    {
        "Company": "EcoEnergy",
        "Sector": "Aerospace",
        "Market Cap": "Small Cap",
        "Stock Price": 555.55,
        "Annual Revenue (B)": 346.47,
        "Quarter": "Q1"
    },
    {
        "Company": "GlobalTrade",
        "Sector": "Biotech",
        "Market Cap": "Mid Cap",
        "Stock Price": 936.75,
        "Annual Revenue (B)": 161.2,
        "Quarter": "Q4"
    }
]
<end>Can you change this markdown into CSV?
| Company | Market Cap | Stock Price | Quarter |
| --- | --- | --- | --- |
| Foodies | Small Cap | 685.62 | Q4 |
| AeroSpace | Small Cap | 378.58 | Q4 |
| Foodies | Large Cap | 516.07 | Q3 |
| RetailHub | Mega Cap | 584.32 | Q4 |
| HealthPlus | Mega Cap | 988.28 | Q2 |
| EcoEnergy | Mid Cap | 787.73 | Q2 |<start>
Company,Market Cap,Stock Price,Quarter
Foodies,Small Cap,685.62,Q4
AeroSpace,Small Cap,378.58,Q4
Foodies,Large Cap,516.07,Q3
RetailHub,Mega Cap,584.32,Q4
HealthPlus,Mega Cap,988.28,Q2
EcoEnergy,Mid Cap,787.73,Q2
<end>Please transform the following MARKDOWN data into JSON:
| Company | Sector | Market Cap | Stock Price | Annual Revenue (B) | Quarter |
| --- | --- | --- | --- | --- | --- |
| AeroSpace | Healthcare | Mid Cap | 502.0 | 152.25 | Q1 |
| RetailHub | Biotech | Small Cap | 645.7 | 292.1 | Q3 |
| AeroSpace | Biotech | Large Cap | 448.12 | 246.22 | Q3 |
| EcoEnergy | Aerospace | Large Cap | 176.68 | 309.21 | Q2 |
| FinanceWorks | Finance | Mega Cap | 156.96 | 238.25 | Q2 |
| RetailHub | Energy | Small Cap | 127.15 | 250.5 | Q3 |<start>
[
    {
        "Company": "AeroSpace",
        "Sector": "Healthcare",
        "Market Cap": "Mid Cap",
        "Stock Price": 502.0,
        "Annual Revenue (B)": 152.25,
        "Quarter": "Q1"
    },
    {
        "Company": "RetailHub",
        "Sector": "Biotech",
        "Market Cap": "Small Cap",
        "Stock Price": 645.7,
        "Annual Revenue (B)": 292.1,
        "Quarter": "Q3"
    },
    {
        "Company": "AeroSpace",
        "Sector": "Biotech",
        "Market Cap": "Large Cap",
        "Stock Price": 448.12,
        "Annual Revenue (B)": 246.22,
        "Quarter": "Q3"
    },
    {
        "Company": "EcoEnergy",
        "Sector": "Aerospace",
        "Market Cap": "Large Cap",
        "Stock Price": 176.68,
        "Annual Revenue (B)": 309.21,
        "Quarter": "Q2"
    },
    {
        "Company": "FinanceWorks",
        "Sector": "Finance",
        "Market Cap": "Mega Cap",
        "Stock Price": 156.96,
        "Annual Revenue (B)": 238.25,
        "Quarter": "Q2"
    },
    {
        "Company": "RetailHub",
        "Sector": "Energy",
        "Market Cap": "Small Cap",
        "Stock Price": 127.15,
        "Annual Revenue (B)": 250.5,
        "Quarter": "Q3"
    }
]
<end>Here's some YML data, can you convert it to Json?
- Average Latency (ms): 81.63
  Cache Hit Ratio (%): 76.08
  Connection Count: 177
  Database Name: AnalyticsDB
  Queries per Second: 1578.54
- Average Latency (ms): 20.88
  Cache Hit Ratio (%): 72.97
  Connection Count: 158
  Database Name: UserDB
  Queries per Second: 329.09
- Average Latency (ms): 54.57
  Cache Hit Ratio (%): 87.11
  Connection Count: 190
  Database Name: ProductsDB
  Queries per Second: 4678.97
- Average Latency (ms): 31.04
  Cache Hit Ratio (%): 81.55
  Connection Count: 124
  Database Name: AnalyticsDB
  Queries per Second: 2610.96
- Average Latency (ms): 66.96
  Cache Hit Ratio (%): 87.11
  Connection Count: 359
  Database Name: InventoryDB
  Queries per Second: 4042.11
- Average Latency (ms): 8.71
  Cache Hit Ratio (%): 72.9
  Connection Count: 277
  Database Name: OrdersDB
  Queries per Second: 4678.97
- Average Latency (ms): 36.54
  Cache Hit Ratio (%): 70.39
  Connection Count: 355
  Database Name: AnalyticsDB
  Queries per Second: 2534.46
- Average Latency (ms): 56.69
  Cache Hit Ratio (%): 88.08
  Connection Count: 234
  Database Name: ProfilesDB
  Queries per Second: 1851.28
- Average Latency (ms): 4.96
  Cache Hit Ratio (%): 76.46
  Connection Count: 489
  Database Name: OrdersDB
  Queries per Second: 2274.72
<start>
[
    {
        "Database Name": "AnalyticsDB",
        "Queries per Second": 1578.54,
        "Cache Hit Ratio (%)": 76.08,
        "Connection Count": 177,
        "Average Latency (ms)": 81.63
    },
    {
        "Database Name": "UserDB",
        "Queries per Second": 329.09,
        "Cache Hit Ratio (%)": 72.97,
        "Connection Count": 158,
        "Average Latency (ms)": 20.88
    },
    {
        "Database Name": "ProductsDB",
        "Queries per Second": 4678.97,
        "Cache Hit Ratio (%)": 87.11,
        "Connection Count": 190,
        "Average Latency (ms)": 54.57
    },
    {
        "Database Name": "AnalyticsDB",
        "Queries per Second": 2610.96,
        "Cache Hit Ratio (%)": 81.55,
        "Connection Count": 124,
        "Average Latency (ms)": 31.04
    },
    {
        "Database Name": "InventoryDB",
        "Queries per Second": 4042.11,
        "Cache Hit Ratio (%)": 87.11,
        "Connection Count": 359,
        "Average Latency (ms)": 66.96
    },
    {
        "Database Name": "OrdersDB",
        "Queries per Second": 4678.97,
        "Cache Hit Ratio (%)": 72.9,
        "Connection Count": 277,
        "Average Latency (ms)": 8.71
    },
    {
        "Database Name": "AnalyticsDB",
        "Queries per Second": 2534.46,
        "Cache Hit Ratio (%)": 70.39,
        "Connection Count": 355,
        "Average Latency (ms)": 36.54
    },
    {
        "Database Name": "ProfilesDB",
        "Queries per Second": 1851.28,
        "Cache Hit Ratio (%)": 88.08,
        "Connection Count": 234,
        "Average Latency (ms)": 56.69
    },
    {
        "Database Name": "OrdersDB",
        "Queries per Second": 2274.72,
        "Cache Hit Ratio (%)": 76.46,
        "Connection Count": 489,
        "Average Latency (ms)": 4.96
    }
]
<end>Here's some markdown data, can you convert it to Json?
| Company | Date | Close Price | Volume |
| --- | --- | --- | --- |
| FoodChain | 2021-12-20 | 69.9 | 8101273 |
| RetailWorld | 2020-05-22 | 289.79 | 9013150 |
| BioLife | 2010-03-25 | 1474.73 | 4442049 |
| MediaGroup | 2022-10-02 | 1114.89 | 5274137 |
| FoodChain | 2014-02-13 | 631.72 | 9442763 |
| FinanceTrust | 2011-05-25 | 858.34 | 2307100 |
| RetailWorld | 2017-02-15 | 310.42 | 8036392 |
| FoodChain | 2014-07-05 | 681.17 | 8668689 |
| AutoMotive | 2010-03-04 | 915.6 | 1706054 |
| AeroSystems | 2021-11-17 | 795.4 | 5575664 |<start>
[
    {
        "Company": "FoodChain",
        "Date": "2021-12-20",
        "Close Price": 69.9,
        "Volume": 8101273
    },
    {
        "Company": "RetailWorld",
        "Date": "2020-05-22",
        "Close Price": 289.79,
        "Volume": 9013150
    },
    {
        "Company": "BioLife",
        "Date": "2010-03-25",
        "Close Price": 1474.73,
        "Volume": 4442049
    },
    {
        "Company": "MediaGroup",
        "Date": "2022-10-02",
        "Close Price": 1114.89,
        "Volume": 5274137
    },
    {
        "Company": "FoodChain",
        "Date": "2014-02-13",
        "Close Price": 631.72,
        "Volume": 9442763
    },
    {
        "Company": "FinanceTrust",
        "Date": "2011-05-25",
        "Close Price": 858.34,
        "Volume": 2307100
    },
    {
        "Company": "RetailWorld",
        "Date": "2017-02-15",
        "Close Price": 310.42,
        "Volume": 8036392
    },
    {
        "Company": "FoodChain",
        "Date": "2014-07-05",
        "Close Price": 681.17,
        "Volume": 8668689
    },
    {
        "Company": "AutoMotive",
        "Date": "2010-03-04",
        "Close Price": 915.6,
        "Volume": 1706054
    },
    {
        "Company": "AeroSystems",
        "Date": "2021-11-17",
        "Close Price": 795.4,
        "Volume": 5575664
    }
]
<end>Transform this json structure to a Plain text format:
[
    {
        "Product Name": "Widget",
        "SKU": "SKU-1053",
        "Stock Quantity": 464,
        "Supplier Name": "Wayne Enterprises"
    },
    {
        "Product Name": "Instrument",
        "SKU": "SKU-1037",
        "Stock Quantity": 8,
        "Supplier Name": "ACME Corp"
    },
    {
        "Product Name": "Apparatus",
        "SKU": "SKU-1037",
        "Stock Quantity": 284,
        "Supplier Name": "Umbrella Corp"
    },
    {
        "Product Name": "Device",
        "SKU": "SKU-1002",
        "Stock Quantity": 318,
        "Supplier Name": "Wayne Enterprises"
    },
    {
        "Product Name": "Gadget",
        "SKU": "SKU-1041",
        "Stock Quantity": 226,
        "Supplier Name": "ACME Corp"
    },
    {
        "Product Name": "Widget",
        "SKU": "SKU-1095",
        "Stock Quantity": 314,
        "Supplier Name": "Wayne Enterprises"
    },
    {
        "Product Name": "Gizmo",
        "SKU": "SKU-1056",
        "Stock Quantity": 331,
        "Supplier Name": "Globex"
    },
    {
        "Product Name": "Contraption",
        "SKU": "SKU-1062",
        "Stock Quantity": 389,
        "Supplier Name": "Globex"
    }
]<start>
Product Name: Widget | SKU: SKU-1053 | Stock Quantity: 464 | Supplier Name: Wayne Enterprises
Product Name: Instrument | SKU: SKU-1037 | Stock Quantity: 8 | Supplier Name: ACME Corp
Product Name: Apparatus | SKU: SKU-1037 | Stock Quantity: 284 | Supplier Name: Umbrella Corp
Product Name: Device | SKU: SKU-1002 | Stock Quantity: 318 | Supplier Name: Wayne Enterprises
Product Name: Gadget | SKU: SKU-1041 | Stock Quantity: 226 | Supplier Name: ACME Corp
Product Name: Widget | SKU: SKU-1095 | Stock Quantity: 314 | Supplier Name: Wayne Enterprises
Product Name: Gizmo | SKU: SKU-1056 | Stock Quantity: 331 | Supplier Name: Globex
Product Name: Contraption | SKU: SKU-1062 | Stock Quantity: 389 | Supplier Name: Globex
<end>Transform this Json structure to a Csv format:
[
    {
        "Name": "Francis",
        "Age": 54,
        "Birth Month": "February",
        "City": "San Antonio",
        "Income": 480000
    },
    {
        "Name": "Avery",
        "Age": 56,
        "Birth Month": "May",
        "City": "Baltimore",
        "Income": 285000
    },
    {
        "Name": "Nathan",
        "Age": 44,
        "Birth Month": "January",
        "City": "Columbus",
        "Income": 220000
    },
    {
        "Name": "Sean",
        "Age": 55,
        "Birth Month": "December",
        "City": "Houston",
        "Income": 90000
    },
    {
        "Name": "Maryann",
        "Age": 48,
        "Birth Month": "October",
        "City": "Fort Worth",
        "Income": 495000
    },
    {
        "Name": "Justin",
        "Age": 68,
        "Birth Month": "April",
        "City": "Portland",
        "Income": 405000
    },
    {
        "Name": "Arianna",
        "Age": 69,
        "Birth Month": "January",
        "City": "San Diego",
        "Income": 20000
    },
    {
        "Name": "Julia",
        "Age": 56,
        "Birth Month": "September",
        "City": "Seattle",
        "Income": 305000
    }
]<start>
Name,Age,Birth Month,City,Income
Francis,54,February,San Antonio,480000
Avery,56,May,Baltimore,285000
Nathan,44,January,Columbus,220000
Sean,55,December,Houston,90000
Maryann,48,October,Fort Worth,495000
Justin,68,April,Portland,405000
Arianna,69,January,San Diego,20000
Julia,56,September,Seattle,305000
<end>Here's some csv data, can you convert it to Markdown?
Device ID,Device Type,Location,Battery Level (%)
device-0053,Temperature Sensor,Office,14.2
device-0058,Humidity Sensor,Hallway,35.1
device-0035,Temperature Sensor,Bathroom,28.8
device-0042,Pressure Sensor,Hallway,92.0
device-0022,Temperature Sensor,Bathroom,83.1
device-0096,Temperature Sensor,Bathroom,92.7
device-0099,Temperature Sensor,Bathroom,19.5
device-0006,Temperature Sensor,Hallway,48.9
<start>
| Device ID | Device Type | Location | Battery Level (%) |
| --- | --- | --- | --- |
| device-0053 | Temperature Sensor | Office | 14.2 |
| device-0058 | Humidity Sensor | Hallway | 35.1 |
| device-0035 | Temperature Sensor | Bathroom | 28.8 |
| device-0042 | Pressure Sensor | Hallway | 92.0 |
| device-0022 | Temperature Sensor | Bathroom | 83.1 |
| device-0096 | Temperature Sensor | Bathroom | 92.7 |
| device-0099 | Temperature Sensor | Bathroom | 19.5 |
| device-0006 | Temperature Sensor | Hallway | 48.9 |
<end>Here's some yaml data, can you convert it to Csv?
- Cuisine: Mediterranean
  Price Range: $$
  Restaurant Name: Pizza Planet
- Cuisine: Mexican
  Price Range: $$$$$
  Restaurant Name: BBQ Barn
- Cuisine: French
  Price Range: $$
  Restaurant Name: Pasta Palace
- Cuisine: Indian
  Price Range: $$
  Restaurant Name: Burger Haven
- Cuisine: Mexican
  Price Range: $$$$$
  Restaurant Name: Pizza Planet
- Cuisine: Mediterranean
  Price Range: $$$$$
  Restaurant Name: BBQ Barn
<start>
Restaurant Name,Cuisine,Price Range
Pizza Planet,Mediterranean,$$
BBQ Barn,Mexican,$$$$$
Pasta Palace,French,$$
Burger Haven,Indian,$$
Pizza Planet,Mexican,$$$$$
BBQ Barn,Mediterranean,$$$$$
<end>Transform this Plain text structure to a Markdown format:
Start Location: San Francisco | End Location: New York | Distance (miles): 2688.5
Start Location: New York | End Location: San Francisco | Distance (miles): 644.1
Start Location: Phoenix | End Location: Chicago | Distance (miles): 782.9
Start Location: Chicago | End Location: Phoenix | Distance (miles): 2214.5
<start>
| Start Location | End Location | Distance (miles) |
| --- | --- | --- |
| San Francisco | New York | 2688.5 |
| New York | San Francisco | 644.1 |
| Phoenix | Chicago | 782.9 |
| Chicago | Phoenix | 2214.5 |
<end>Can you change this yml into Markdown?
- Battery Level (%): 87.4
  Device ID: device-0026
  Device Type: Humidity Sensor
  Location: Garage
  Timestamp: '2021-06-15 05:44:03'
- Battery Level (%): 54.8
  Device ID: device-0028
  Device Type: Motion Detector
  Location: Hallway
  Timestamp: '2021-10-20 06:21:48'
- Battery Level (%): 83.4
  Device ID: device-0016
  Device Type: Temperature Sensor
  Location: Office
  Timestamp: '2023-11-25 12:26:43'
- Battery Level (%): 19.2
  Device ID: device-0022
  Device Type: Temperature Sensor
  Location: Bathroom
  Timestamp: '2023-04-22 19:36:57'
- Battery Level (%): 36.8
  Device ID: device-0004
  Device Type: Pressure Sensor
  Location: Living Room
  Timestamp: '2023-06-15 14:58:07'
- Battery Level (%): 39.6
  Device ID: device-0024
  Device Type: Light Sensor
  Location: Living Room
  Timestamp: '2022-12-26 16:29:51'
<start>
| Device ID | Device Type | Location | Battery Level (%) | Timestamp |
| --- | --- | --- | --- | --- |
| device-0026 | Humidity Sensor | Garage | 87.4 | 2021-06-15 05:44:03 |
| device-0028 | Motion Detector | Hallway | 54.8 | 2021-10-20 06:21:48 |
| device-0016 | Temperature Sensor | Office | 83.4 | 2023-11-25 12:26:43 |
| device-0022 | Temperature Sensor | Bathroom | 19.2 | 2023-04-22 19:36:57 |
| device-0004 | Pressure Sensor | Living Room | 36.8 | 2023-06-15 14:58:07 |
| device-0024 | Light Sensor | Living Room | 39.6 | 2022-12-26 16:29:51 |
<end>Transform this markdown structure to a yml format:
| Trip Name | Start Location | Distance (miles) | Duration (hours) |
| --- | --- | --- | --- |
| Valley Voyage | Phoenix | 2101.4 | 5.7 |
| Canyon Trek | New York | 1848.7 | 24.3 |
| Canyon Trek | Houston | 2195.2 | 32.6 |
| Desert Drive | New York | 2779.1 | 15.4 |
| Coast to Coast | New York | 2507.1 | 19.5 |
| Lakeside Retreat | New York | 2989.1 | 5.0 |<start>
- Distance (miles): 2101.4
  Duration (hours): 5.7
  Start Location: Phoenix
  Trip Name: Valley Voyage
- Distance (miles): 1848.7
  Duration (hours): 24.3
  Start Location: New York
  Trip Name: Canyon Trek
- Distance (miles): 2195.2
  Duration (hours): 32.6
  Start Location: Houston
  Trip Name: Canyon Trek
- Distance (miles): 2779.1
  Duration (hours): 15.4
  Start Location: New York
  Trip Name: Desert Drive
- Distance (miles): 2507.1
  Duration (hours): 19.5
  Start Location: New York
  Trip Name: Coast to Coast
- Distance (miles): 2989.1
  Duration (hours): 5.0
  Start Location: New York
  Trip Name: Lakeside Retreat
<end>Can you change this plain text into MARKDOWN?
Database Name: UserDB | Queries per Second: 539.7 | Cache Hit Ratio (%): 81.98 | Connection Count: 27
Database Name: UserDB | Queries per Second: 186.64 | Cache Hit Ratio (%): 90.93 | Connection Count: 451
Database Name: ProfilesDB | Queries per Second: 3931.08 | Cache Hit Ratio (%): 80.73 | Connection Count: 256
<start>
| Database Name | Queries per Second | Cache Hit Ratio (%) | Connection Count |
| --- | --- | --- | --- |
| UserDB | 539.7 | 81.98 | 27 |
| UserDB | 186.64 | 90.93 | 451 |
| ProfilesDB | 3931.08 | 80.73 | 256 |
<end>Transform this json structure to a Csv format:
[
    {
        "Database Name": "OrdersDB",
        "Queries per Second": 4694.79,
        "Cache Hit Ratio (%)": 70.34,
        "Connection Count": 132,
        "Average Latency (ms)": 66.79,
        "Timestamp": "2022-07-12 22:55:51"
    },
    {
        "Database Name": "AnalyticsDB",
        "Queries per Second": 4885.85,
        "Cache Hit Ratio (%)": 78.34,
        "Connection Count": 372,
        "Average Latency (ms)": 80.85,
        "Timestamp": "2023-02-20 07:24:24"
    },
    {
        "Database Name": "OrdersDB",
        "Queries per Second": 3584.34,
        "Cache Hit Ratio (%)": 86.14,
        "Connection Count": 82,
        "Average Latency (ms)": 48.85,
        "Timestamp": "2021-02-26 15:01:44"
    },
    {
        "Database Name": "OrdersDB",
        "Queries per Second": 2237.08,
        "Cache Hit Ratio (%)": 83.4,
        "Connection Count": 92,
        "Average Latency (ms)": 47.07,
        "Timestamp": "2021-11-04 03:04:25"
    },
    {
        "Database Name": "ProfilesDB",
        "Queries per Second": 2783.22,
        "Cache Hit Ratio (%)": 70.62,
        "Connection Count": 132,
        "Average Latency (ms)": 28.28,
        "Timestamp": "2022-02-20 07:44:40"
    },
    {
        "Database Name": "LogsDB",
        "Queries per Second": 1885.06,
        "Cache Hit Ratio (%)": 95.64,
        "Connection Count": 105,
        "Average Latency (ms)": 40.65,
        "Timestamp": "2023-10-16 05:47:43"
    }
]<start>
Database Name,Queries per Second,Cache Hit Ratio (%),Connection Count,Average Latency (ms),Timestamp
OrdersDB,4694.79,70.34,132,66.79,2022-07-12 22:55:51
AnalyticsDB,4885.85,78.34,372,80.85,2023-02-20 07:24:24
OrdersDB,3584.34,86.14,82,48.85,2021-02-26 15:01:44
OrdersDB,2237.08,83.4,92,47.07,2021-11-04 03:04:25
ProfilesDB,2783.22,70.62,132,28.28,2022-02-20 07:44:40
LogsDB,1885.06,95.64,105,40.65,2023-10-16 05:47:43
<end>Convert this plain text to yaml:
Location: Phoenix | Rating: 3 | Price Range: $
Location: Los Angeles | Rating: 5 | Price Range: $
Location: San Francisco | Rating: 2 | Price Range: $$$$
Location: Phoenix | Rating: 5 | Price Range: $$$$$
Location: Miami | Rating: 2 | Price Range: $$
Location: Phoenix | Rating: 1 | Price Range: $$$
Location: Seattle | Rating: 1 | Price Range: $$$$
Location: New York | Rating: 1 | Price Range: $
Location: Seattle | Rating: 2 | Price Range: $$
<start>
- Location: Phoenix
  Price Range: $
  Rating: 3
- Location: Los Angeles
  Price Range: $
  Rating: 5
- Location: San Francisco
  Price Range: $$$$
  Rating: 2
- Location: Phoenix
  Price Range: $$$$$
  Rating: 5
- Location: Miami
  Price Range: $$
  Rating: 2
- Location: Phoenix
  Price Range: $$$
  Rating: 1
- Location: Seattle
  Price Range: $$$$
  Rating: 1
- Location: New York
  Price Range: $
  Rating: 1
- Location: Seattle
  Price Range: $$
  Rating: 2
<end>Please transform the following Plain text data into json:
Name: Randall | Age: 47 | Birth Month: February | Income: 315000
Name: Fred | Age: 20 | Birth Month: April | Income: 460000
Name: Forrest | Age: 52 | Birth Month: May | Income: 30000
Name: Christie | Age: 45 | Birth Month: September | Income: 485000
Name: Otis | Age: 34 | Birth Month: September | Income: 420000
Name: Amelia | Age: 56 | Birth Month: April | Income: 190000
Name: Jayden | Age: 44 | Birth Month: October | Income: 210000
<start>
[
    {
        "Name": "Randall",
        "Age": 47,
        "Birth Month": "February",
        "Income": 315000
    },
    {
        "Name": "Fred",
        "Age": 20,
        "Birth Month": "April",
        "Income": 460000
    },
    {
        "Name": "Forrest",
        "Age": 52,
        "Birth Month": "May",
        "Income": 30000
    },
    {
        "Name": "Christie",
        "Age": 45,
        "Birth Month": "September",
        "Income": 485000
    },
    {
        "Name": "Otis",
        "Age": 34,
        "Birth Month": "September",
        "Income": 420000
    },
    {
        "Name": "Amelia",
        "Age": 56,
        "Birth Month": "April",
        "Income": 190000
    },
    {
        "Name": "Jayden",
        "Age": 44,
        "Birth Month": "October",
        "Income": 210000
    }
]
<end>Here's some json data, can you convert it to Plain text?
[
    {
        "Restaurant Name": "Vegan Delight",
        "Cuisine": "Japanese",
        "Location": "Chicago",
        "Rating": 4
    },
    {
        "Restaurant Name": "Sushi World",
        "Cuisine": "Italian",
        "Location": "Houston",
        "Rating": 4
    },
    {
        "Restaurant Name": "Curry Corner",
        "Cuisine": "Italian",
        "Location": "New York",
        "Rating": 2
    },
    {
        "Restaurant Name": "The Steakhouse",
        "Cuisine": "Italian",
        "Location": "Houston",
        "Rating": 4
    },
    {
        "Restaurant Name": "The Steakhouse",
        "Cuisine": "Japanese",
        "Location": "New York",
        "Rating": 3
    },
    {
        "Restaurant Name": "The Steakhouse",
        "Cuisine": "French",
        "Location": "Los Angeles",
        "Rating": 5
    },
    {
        "Restaurant Name": "Sushi World",
        "Cuisine": "Japanese",
        "Location": "Seattle",
        "Rating": 2
    },
    {
        "Restaurant Name": "BBQ Barn",
        "Cuisine": "Japanese",
        "Location": "Houston",
        "Rating": 5
    }
]<start>
Restaurant Name: Vegan Delight | Cuisine: Japanese | Location: Chicago | Rating: 4
Restaurant Name: Sushi World | Cuisine: Italian | Location: Houston | Rating: 4
Restaurant Name: Curry Corner | Cuisine: Italian | Location: New York | Rating: 2
Restaurant Name: The Steakhouse | Cuisine: Italian | Location: Houston | Rating: 4
Restaurant Name: The Steakhouse | Cuisine: Japanese | Location: New York | Rating: 3
Restaurant Name: The Steakhouse | Cuisine: French | Location: Los Angeles | Rating: 5
Restaurant Name: Sushi World | Cuisine: Japanese | Location: Seattle | Rating: 2
Restaurant Name: BBQ Barn | Cuisine: Japanese | Location: Houston | Rating: 5
<end>Here's some CSV data, can you convert it to PLAIN TEXT?
Director,Genre
Aria Ravenwood,Drama
Zara Stormrider,Thriller
Lira Silverleaf,Thriller
Cade Firebrand,Adventure
Lira Silverleaf,Sci-Fi
Lira Silverleaf,Adventure
<start>
Director: Aria Ravenwood | Genre: Drama
Director: Zara Stormrider | Genre: Thriller
Director: Lira Silverleaf | Genre: Thriller
Director: Cade Firebrand | Genre: Adventure
Director: Lira Silverleaf | Genre: Sci-Fi
Director: Lira Silverleaf | Genre: Adventure
<end>Transform this Markdown structure to a plain text format:
| Trip Name | Start Location | End Location | Distance (miles) | Duration (hours) | Fuel Used (gallons) |
| --- | --- | --- | --- | --- | --- |
| City Explorer | San Francisco | Phoenix | 1143.4 | 9.9 | 21.1 |
| Forest Journey | Los Angeles | New York | 1734.5 | 9.2 | 46.6 |
| Canyon Trek | Denver | Chicago | 2520.1 | 31.8 | 74.4 |
| Forest Journey | Miami | Chicago | 2930.3 | 12.3 | 92.6 |
| City Explorer | New York | Houston | 373.1 | 24.5 | 11.7 |
| Forest Journey | Los Angeles | Phoenix | 1728.6 | 63.8 | 80.9 |
| Desert Drive | Chicago | Los Angeles | 364.1 | 57.0 | 13.8 |
| Canyon Trek | New York | Phoenix | 924.1 | 47.5 | 49.7 |
| City Explorer | Chicago | Phoenix | 2932.6 | 33.9 | 41.3 |<start>
Trip Name: City Explorer | Start Location: San Francisco | End Location: Phoenix | Distance (miles): 1143.4 | Duration (hours): 9.9 | Fuel Used (gallons): 21.1
Trip Name: Forest Journey | Start Location: Los Angeles | End Location: New York | Distance (miles): 1734.5 | Duration (hours): 9.2 | Fuel Used (gallons): 46.6
Trip Name: Canyon Trek | Start Location: Denver | End Location: Chicago | Distance (miles): 2520.1 | Duration (hours): 31.8 | Fuel Used (gallons): 74.4
Trip Name: Forest Journey | Start Location: Miami | End Location: Chicago | Distance (miles): 2930.3 | Duration (hours): 12.3 | Fuel Used (gallons): 92.6
Trip Name: City Explorer | Start Location: New York | End Location: Houston | Distance (miles): 373.1 | Duration (hours): 24.5 | Fuel Used (gallons): 11.7
Trip Name: Forest Journey | Start Location: Los Angeles | End Location: Phoenix | Distance (miles): 1728.6 | Duration (hours): 63.8 | Fuel Used (gallons): 80.9
Trip Name: Desert Drive | Start Location: Chicago | End Location: Los Angeles | Distance (miles): 364.1 | Duration (hours): 57.0 | Fuel Used (gallons): 13.8
Trip Name: Canyon Trek | Start Location: New York | End Location: Phoenix | Distance (miles): 924.1 | Duration (hours): 47.5 | Fuel Used (gallons): 49.7
Trip Name: City Explorer | Start Location: Chicago | End Location: Phoenix | Distance (miles): 2932.6 | Duration (hours): 33.9 | Fuel Used (gallons): 41.3
<end>Convert this Yaml to CSV:
- Battery Level (%): 16.4
  Device Type: Pressure Sensor
  Location: Office
  Timestamp: '2022-11-25 20:03:54'
- Battery Level (%): 92.9
  Device Type: Pressure Sensor
  Location: Office
  Timestamp: '2023-04-04 18:53:20'
- Battery Level (%): 26.7
  Device Type: Temperature Sensor
  Location: Living Room
  Timestamp: '2022-08-17 01:25:08'
- Battery Level (%): 26.7
  Device Type: Light Sensor
  Location: Garden
  Timestamp: '2023-09-01 04:34:37'
<start>
Device Type,Location,Battery Level (%),Timestamp
Pressure Sensor,Office,16.4,2022-11-25 20:03:54
Pressure Sensor,Office,92.9,2023-04-04 18:53:20
Temperature Sensor,Living Room,26.7,2022-08-17 01:25:08
Light Sensor,Garden,26.7,2023-09-01 04:34:37
<end>Convert this plain text to markdown:
Title: The Endless Horizon | Director: Lira Silverleaf | Genre: Fantasy | Box Office Earnings (M): 800.46
Title: Beyond the Veil | Director: Mara Moonshadow | Genre: Fantasy | Box Office Earnings (M): 84.36
Title: Escape from Earth | Director: Zara Stormrider | Genre: Action | Box Office Earnings (M): 840.43
Title: Escape from Earth | Director: Cade Firebrand | Genre: Horror | Box Office Earnings (M): 857.39
Title: Dreamwalker | Director: Aria Ravenwood | Genre: Thriller | Box Office Earnings (M): 74.96
Title: Dreamwalker | Director: Cade Firebrand | Genre: Fantasy | Box Office Earnings (M): 742.56
Title: Rise of the Titans | Director: Lira Silverleaf | Genre: Drama | Box Office Earnings (M): 921.6
Title: Starbound Odyssey | Director: Cade Firebrand | Genre: Adventure | Box Office Earnings (M): 986.44
Title: Rise of the Titans | Director: Drake Nightshade | Genre: Horror | Box Office Earnings (M): 559.79
<start>
| Title | Director | Genre | Box Office Earnings (M) |
| --- | --- | --- | --- |
| The Endless Horizon | Lira Silverleaf | Fantasy | 800.46 |
| Beyond the Veil | Mara Moonshadow | Fantasy | 84.36 |
| Escape from Earth | Zara Stormrider | Action | 840.43 |
| Escape from Earth | Cade Firebrand | Horror | 857.39 |
| Dreamwalker | Aria Ravenwood | Thriller | 74.96 |
| Dreamwalker | Cade Firebrand | Fantasy | 742.56 |
| Rise of the Titans | Lira Silverleaf | Drama | 921.6 |
| Starbound Odyssey | Cade Firebrand | Adventure | 986.44 |
| Rise of the Titans | Drake Nightshade | Horror | 559.79 |
<end>Here's some csv data, can you convert it to PLAIN TEXT?
Database Name,Queries per Second,Cache Hit Ratio (%),Connection Count,Timestamp
ProfilesDB,1209.86,92.28,175,2023-01-14 22:33:11
SessionsDB,4202.33,86.3,38,2022-05-01 23:52:06
InventoryDB,3763.65,94.28,205,2022-10-04 17:03:06
SessionsDB,516.1,79.44,356,2022-09-12 22:20:33
SessionsDB,2569.55,90.48,75,2021-05-22 01:46:32
UserDB,584.57,73.42,478,2021-12-08 02:10:08
InventoryDB,3670.82,97.51,175,2022-07-08 11:25:37
AnalyticsDB,1374.38,87.12,167,2022-07-15 09:56:28
<start>
Database Name: ProfilesDB | Queries per Second: 1209.86 | Cache Hit Ratio (%): 92.28 | Connection Count: 175 | Timestamp: 2023-01-14 22:33:11
Database Name: SessionsDB | Queries per Second: 4202.33 | Cache Hit Ratio (%): 86.3 | Connection Count: 38 | Timestamp: 2022-05-01 23:52:06
Database Name: InventoryDB | Queries per Second: 3763.65 | Cache Hit Ratio (%): 94.28 | Connection Count: 205 | Timestamp: 2022-10-04 17:03:06
Database Name: SessionsDB | Queries per Second: 516.1 | Cache Hit Ratio (%): 79.44 | Connection Count: 356 | Timestamp: 2022-09-12 22:20:33
Database Name: SessionsDB | Queries per Second: 2569.55 | Cache Hit Ratio (%): 90.48 | Connection Count: 75 | Timestamp: 2021-05-22 01:46:32
Database Name: UserDB | Queries per Second: 584.57 | Cache Hit Ratio (%): 73.42 | Connection Count: 478 | Timestamp: 2021-12-08 02:10:08
Database Name: InventoryDB | Queries per Second: 3670.82 | Cache Hit Ratio (%): 97.51 | Connection Count: 175 | Timestamp: 2022-07-08 11:25:37
Database Name: AnalyticsDB | Queries per Second: 1374.38 | Cache Hit Ratio (%): 87.12 | Connection Count: 167 | Timestamp: 2022-07-15 09:56:28
<end>Transform this plain text structure to a yaml format:
Close Price: 1479.81 | High Price: 1479.81 | Low Price: 169.55 | Volume: 3182621
Close Price: 1229.27 | High Price: 1229.27 | Low Price: 267.24 | Volume: 8144921
Close Price: 559.16 | High Price: 559.16 | Low Price: 62.79 | Volume: 3456877
<start>
- Close Price: 1479.81
  High Price: 1479.81
  Low Price: 169.55
  Volume: 3182621
- Close Price: 1229.27
  High Price: 1229.27
  Low Price: 267.24
  Volume: 8144921
- Close Price: 559.16
  High Price: 559.16
  Low Price: 62.79
  Volume: 3456877
<end>Convert this Json to plain text:
[
    {
        "Age": 69,
        "Birth Month": "February",
        "City": "Seattle",
        "Income": 330000
    },
    {
        "Age": 59,
        "Birth Month": "August",
        "City": "Denver",
        "Income": 285000
    },
    {
        "Age": 18,
        "Birth Month": "January",
        "City": "San Diego",
        "Income": 110000
    },
    {
        "Age": 56,
        "Birth Month": "January",
        "City": "New York",
        "Income": 140000
    },
    {
        "Age": 48,
        "Birth Month": "December",
        "City": "Indianapolis",
        "Income": 265000
    },
    {
        "Age": 41,
        "Birth Month": "August",
        "City": "New York",
        "Income": 150000
    },
    {
        "Age": 47,
        "Birth Month": "March",
        "City": "Chicago",
        "Income": 115000
    },
    {
        "Age": 68,
        "Birth Month": "December",
        "City": "Fort Worth",
        "Income": 220000
    }
]<start>
Age: 69 | Birth Month: February | City: Seattle | Income: 330000
Age: 59 | Birth Month: August | City: Denver | Income: 285000
Age: 18 | Birth Month: January | City: San Diego | Income: 110000
Age: 56 | Birth Month: January | City: New York | Income: 140000
Age: 48 | Birth Month: December | City: Indianapolis | Income: 265000
Age: 41 | Birth Month: August | City: New York | Income: 150000
Age: 47 | Birth Month: March | City: Chicago | Income: 115000
Age: 68 | Birth Month: December | City: Fort Worth | Income: 220000
<end>Please transform the following markdown data into JSON:
| Rating | Price Range |
| --- | --- |
| 5 | $ |
| 1 | $$$$$ |
| 3 | $$ |
| 3 | $$$ |<start>
[
    {
        "Rating": 5,
        "Price Range": "$"
    },
    {
        "Rating": 1,
        "Price Range": "$$$$$"
    },
    {
        "Rating": 3,
        "Price Range": "$$"
    },
    {
        "Rating": 3,
        "Price Range": "$$$"
    }
]
<end>Can you change this CSV into plain text?
Name,Age,City
Ethan,68,Denver
Gina,64,Baltimore
Monica,50,Indianapolis
Mabel,42,Houston
Christie,21,New York
Khloe,28,Milwaukee
Aubree,61,Chicago
<start>
Name: Ethan | Age: 68 | City: Denver
Name: Gina | Age: 64 | City: Baltimore
Name: Monica | Age: 50 | City: Indianapolis
Name: Mabel | Age: 42 | City: Houston
Name: Christie | Age: 21 | City: New York
Name: Khloe | Age: 28 | City: Milwaukee
Name: Aubree | Age: 61 | City: Chicago
<end>Here's some json data, can you convert it to plain text?
[
    {
        "Product Name": "Gizmo",
        "SKU": "SKU-1037",
        "Price": 497.54,
        "Stock Quantity": 261,
        "Category": "Household",
        "Supplier Name": "Umbrella Corp"
    },
    {
        "Product Name": "Device",
        "SKU": "SKU-1075",
        "Price": 165.09,
        "Stock Quantity": 228,
        "Category": "Electronics",
        "Supplier Name": "Wonka Industries"
    },
    {
        "Product Name": "Contraption",
        "SKU": "SKU-1041",
        "Price": 39.57,
        "Stock Quantity": 24,
        "Category": "Toys",
        "Supplier Name": "Globex"
    },
    {
        "Product Name": "Whatchamacallit",
        "SKU": "SKU-1037",
        "Price": 87.2,
        "Stock Quantity": 385,
        "Category": "Toys",
        "Supplier Name": "Umbrella Corp"
    }
]<start>
Product Name: Gizmo | SKU: SKU-1037 | Price: 497.54 | Stock Quantity: 261 | Category: Household | Supplier Name: Umbrella Corp
Product Name: Device | SKU: SKU-1075 | Price: 165.09 | Stock Quantity: 228 | Category: Electronics | Supplier Name: Wonka Industries
Product Name: Contraption | SKU: SKU-1041 | Price: 39.57 | Stock Quantity: 24 | Category: Toys | Supplier Name: Globex
Product Name: Whatchamacallit | SKU: SKU-1037 | Price: 87.2 | Stock Quantity: 385 | Category: Toys | Supplier Name: Umbrella Corp
<end>Transform this markdown structure to a plain text format:
| Title | Director | Genre | Release Year | Box Office Earnings (M) |
| --- | --- | --- | --- | --- |
| Edge of Infinity | Orin Shadowalker | Action | 2012 | 93.32 |
| The Great Expedition | Rylan Frostblade | Sci-Fi | 2004 | 324.81 |
| Dreamwalker | Zara Stormrider | Drama | 1996 | 817.88 |
| Rise of the Titans | Selene Darkwhisper | Fantasy | 1992 | 797.53 |
| Edge of Infinity | Lira Silverleaf | Drama | 1980 | 998.34 |
| The Final Voyage | Drake Nightshade | Comedy | 1989 | 506.26 |
| The Final Voyage | Rylan Frostblade | Horror | 1995 | 809.3 |
| Beyond the Veil | Mara Moonshadow | Drama | 1981 | 674.55 |
| The Great Expedition | Orin Shadowalker | Comedy | 1996 | 195.26 |
| Edge of Infinity | Zara Stormrider | Comedy | 1983 | 462.1 |<start>
Title: Edge of Infinity | Director: Orin Shadowalker | Genre: Action | Release Year: 2012 | Box Office Earnings (M): 93.32
Title: The Great Expedition | Director: Rylan Frostblade | Genre: Sci-Fi | Release Year: 2004 | Box Office Earnings (M): 324.81
Title: Dreamwalker | Director: Zara Stormrider | Genre: Drama | Release Year: 1996 | Box Office Earnings (M): 817.88
Title: Rise of the Titans | Director: Selene Darkwhisper | Genre: Fantasy | Release Year: 1992 | Box Office Earnings (M): 797.53
Title: Edge of Infinity | Director: Lira Silverleaf | Genre: Drama | Release Year: 1980 | Box Office Earnings (M): 998.34
Title: The Final Voyage | Director: Drake Nightshade | Genre: Comedy | Release Year: 1989 | Box Office Earnings (M): 506.26
Title: The Final Voyage | Director: Rylan Frostblade | Genre: Horror | Release Year: 1995 | Box Office Earnings (M): 809.3
Title: Beyond the Veil | Director: Mara Moonshadow | Genre: Drama | Release Year: 1981 | Box Office Earnings (M): 674.55
Title: The Great Expedition | Director: Orin Shadowalker | Genre: Comedy | Release Year: 1996 | Box Office Earnings (M): 195.26
Title: Edge of Infinity | Director: Zara Stormrider | Genre: Comedy | Release Year: 1983 | Box Office Earnings (M): 462.1
<end>Please transform the following Yml data into JSON:
- Category: Electronics
  Price: 126.88
  SKU: SKU-1049
  Stock Quantity: 98
  Supplier Name: Wonka Industries
- Category: Toys
  Price: 29.0
  SKU: SKU-1041
  Stock Quantity: 298
  Supplier Name: Wonka Industries
- Category: Household
  Price: 281.6
  SKU: SKU-1024
  Stock Quantity: 56
  Supplier Name: ACME Corp
- Category: Sports
  Price: 327.6
  SKU: SKU-1094
  Stock Quantity: 393
  Supplier Name: Wonka Industries
- Category: Automotive
  Price: 235.86
  SKU: SKU-1059
  Stock Quantity: 242
  Supplier Name: Globex
- Category: Household
  Price: 69.94
  SKU: SKU-1026
  Stock Quantity: 390
  Supplier Name: ACME Corp
<start>
[
    {
        "SKU": "SKU-1049",
        "Price": 126.88,
        "Stock Quantity": 98,
        "Category": "Electronics",
        "Supplier Name": "Wonka Industries"
    },
    {
        "SKU": "SKU-1041",
        "Price": 29.0,
        "Stock Quantity": 298,
        "Category": "Toys",
        "Supplier Name": "Wonka Industries"
    },
    {
        "SKU": "SKU-1024",
        "Price": 281.6,
        "Stock Quantity": 56,
        "Category": "Household",
        "Supplier Name": "ACME Corp"
    },
    {
        "SKU": "SKU-1094",
        "Price": 327.6,
        "Stock Quantity": 393,
        "Category": "Sports",
        "Supplier Name": "Wonka Industries"
    },
    {
        "SKU": "SKU-1059",
        "Price": 235.86,
        "Stock Quantity": 242,
        "Category": "Automotive",
        "Supplier Name": "Globex"
    },
    {
        "SKU": "SKU-1026",
        "Price": 69.94,
        "Stock Quantity": 390,
        "Category": "Household",
        "Supplier Name": "ACME Corp"
    }
]
<end>Here's some Yml data, can you convert it to MARKDOWN?
- Battery Level (%): 50.5
  Device ID: device-0044
  Device Type: Humidity Sensor
  Location: Garage
  Reading Value: 38.81
  Timestamp: '2021-05-22 13:31:16'
- Battery Level (%): 44.0
  Device ID: device-0098
  Device Type: Pressure Sensor
  Location: Hallway
  Reading Value: 22.33
  Timestamp: '2023-05-19 12:01:17'
- Battery Level (%): 88.8
  Device ID: device-0077
  Device Type: Motion Detector
  Location: Garden
  Reading Value: 34.06
  Timestamp: '2022-01-08 06:29:30'
- Battery Level (%): 42.9
  Device ID: device-0075
  Device Type: Light Sensor
  Location: Garden
  Reading Value: 77.14
  Timestamp: '2022-04-26 19:49:47'
- Battery Level (%): 89.3
  Device ID: device-0035
  Device Type: Pressure Sensor
  Location: Garden
  Reading Value: -20.77
  Timestamp: '2023-05-18 15:50:34'
- Battery Level (%): 94.3
  Device ID: device-0022
  Device Type: Humidity Sensor
  Location: Bedroom
  Reading Value: -13.63
  Timestamp: '2021-07-02 22:49:38'
- Battery Level (%): 23.8
  Device ID: device-0034
  Device Type: Pressure Sensor
  Location: Living Room
  Reading Value: -16.05
  Timestamp: '2021-09-14 14:30:55'
- Battery Level (%): 12.2
  Device ID: device-0069
  Device Type: Motion Detector
  Location: Kitchen
  Reading Value: -36.03
  Timestamp: '2021-12-22 15:28:08'
- Battery Level (%): 13.3
  Device ID: device-0075
  Device Type: Light Sensor
  Location: Living Room
  Reading Value: -36.03
  Timestamp: '2021-09-09 17:16:04'
- Battery Level (%): 47.9
  Device ID: device-0100
  Device Type: Light Sensor
  Location: Living Room
  Reading Value: 37.69
  Timestamp: '2023-12-20 08:10:44'
<start>
| Device ID | Device Type | Location | Battery Level (%) | Reading Value | Timestamp |
| --- | --- | --- | --- | --- | --- |
| device-0044 | Humidity Sensor | Garage | 50.5 | 38.81 | 2021-05-22 13:31:16 |
| device-0098 | Pressure Sensor | Hallway | 44.0 | 22.33 | 2023-05-19 12:01:17 |
| device-0077 | Motion Detector | Garden | 88.8 | 34.06 | 2022-01-08 06:29:30 |
| device-0075 | Light Sensor | Garden | 42.9 | 77.14 | 2022-04-26 19:49:47 |
| device-0035 | Pressure Sensor | Garden | 89.3 | -20.77 | 2023-05-18 15:50:34 |
| device-0022 | Humidity Sensor | Bedroom | 94.3 | -13.63 | 2021-07-02 22:49:38 |
| device-0034 | Pressure Sensor | Living Room | 23.8 | -16.05 | 2021-09-14 14:30:55 |
| device-0069 | Motion Detector | Kitchen | 12.2 | -36.03 | 2021-12-22 15:28:08 |
| device-0075 | Light Sensor | Living Room | 13.3 | -36.03 | 2021-09-09 17:16:04 |
| device-0100 | Light Sensor | Living Room | 47.9 | 37.69 | 2023-12-20 08:10:44 |
<end>Transform this csv structure to a Yaml format:
Genre,Publication Year
Science Fiction,1954
Mystery,2019
Mystery,1992
Mystery,1981
Horror,1991
Science Fiction,2016
Mystery,2021
Fantasy,1967
Non-Fiction,1958
Non-Fiction,1976
<start>
- Genre: Science Fiction
  Publication Year: 1954
- Genre: Mystery
  Publication Year: 2019
- Genre: Mystery
  Publication Year: 1992
- Genre: Mystery
  Publication Year: 1981
- Genre: Horror
  Publication Year: 1991
- Genre: Science Fiction
  Publication Year: 2016
- Genre: Mystery
  Publication Year: 2021
- Genre: Fantasy
  Publication Year: 1967
- Genre: Non-Fiction
  Publication Year: 1958
- Genre: Non-Fiction
  Publication Year: 1976
<end>Here's some Markdown data, can you convert it to csv?
| Director | Genre | Release Year | Box Office Earnings (M) |
| --- | --- | --- | --- |
| Talon Blackthorn | Sci-Fi | 2001 | 439.1 |
| Zara Stormrider | Comedy | 2003 | 252.47 |
| Zara Stormrider | Horror | 2012 | 564.28 |
| Talon Blackthorn | Adventure | 2010 | 841.06 |
| Aria Ravenwood | Adventure | 1970 | 444.99 |
| Aria Ravenwood | Horror | 2004 | 137.88 |
| Lira Silverleaf | Sci-Fi | 2004 | 576.14 |
| Aria Ravenwood | Horror | 1970 | 776.43 |
| Lira Silverleaf | Comedy | 2000 | 302.8 |<start>
Director,Genre,Release Year,Box Office Earnings (M)
Talon Blackthorn,Sci-Fi,2001,439.1
Zara Stormrider,Comedy,2003,252.47
Zara Stormrider,Horror,2012,564.28
Talon Blackthorn,Adventure,2010,841.06
Aria Ravenwood,Adventure,1970,444.99
Aria Ravenwood,Horror,2004,137.88
Lira Silverleaf,Sci-Fi,2004,576.14
Aria Ravenwood,Horror,1970,776.43
Lira Silverleaf,Comedy,2000,302.8
<end>Please transform the following YML data into csv:
- Genre: Action
  Title: Rise of the Titans
- Genre: Horror
  Title: Edge of Infinity
- Genre: Sci-Fi
  Title: Dreamwalker
- Genre: Drama
  Title: Starbound Odyssey
- Genre: Drama
  Title: The Final Voyage
- Genre: Drama
  Title: Starbound Odyssey
- Genre: Action
  Title: Rise of the Titans
- Genre: Horror
  Title: Mystery of the Depths
<start>
Title,Genre
Rise of the Titans,Action
Edge of Infinity,Horror
Dreamwalker,Sci-Fi
Starbound Odyssey,Drama
The Final Voyage,Drama
Starbound Odyssey,Drama
Rise of the Titans,Action
Mystery of the Depths,Horror
<end>Transform this markdown structure to a plain text format:
| Date | Open Price | Close Price | High Price | Low Price | Volume |
| --- | --- | --- | --- | --- | --- |
| 2011-02-23 | 467.91 | 367.23 | 1434.48 | 367.23 | 4484150 |
| 2014-05-22 | 367.23 | 815.38 | 887.66 | 367.23 | 7136198 |
| 2019-04-12 | 535.56 | 1010.81 | 1165.77 | 535.56 | 8734617 |
| 2013-12-10 | 987.12 | 1192.22 | 1192.22 | 940.76 | 2323135 |
| 2016-12-20 | 626.25 | 1197.44 | 1339.99 | 209.13 | 9966602 |
| 2013-04-04 | 255.48 | 1192.22 | 1192.22 | 255.48 | 3176545 |
| 2014-04-25 | 255.48 | 279.96 | 1396.22 | 255.48 | 7794744 |<start>
Date: 2011-02-23 | Open Price: 467.91 | Close Price: 367.23 | High Price: 1434.48 | Low Price: 367.23 | Volume: 4484150
Date: 2014-05-22 | Open Price: 367.23 | Close Price: 815.38 | High Price: 887.66 | Low Price: 367.23 | Volume: 7136198
Date: 2019-04-12 | Open Price: 535.56 | Close Price: 1010.81 | High Price: 1165.77 | Low Price: 535.56 | Volume: 8734617
Date: 2013-12-10 | Open Price: 987.12 | Close Price: 1192.22 | High Price: 1192.22 | Low Price: 940.76 | Volume: 2323135
Date: 2016-12-20 | Open Price: 626.25 | Close Price: 1197.44 | High Price: 1339.99 | Low Price: 209.13 | Volume: 9966602
Date: 2013-04-04 | Open Price: 255.48 | Close Price: 1192.22 | High Price: 1192.22 | Low Price: 255.48 | Volume: 3176545
Date: 2014-04-25 | Open Price: 255.48 | Close Price: 279.96 | High Price: 1396.22 | Low Price: 255.48 | Volume: 7794744
<end>Here's some csv data, can you convert it to markdown?
Company,Sector,Market Cap,Stock Price,Annual Revenue (B),Quarter
HealthPlus,Finance,Small Cap,546.92,373.02,Q1
FinanceWorks,Automotive,Large Cap,204.75,303.25,Q4
RetailHub,Aerospace,Small Cap,305.55,446.68,Q1
Foodies,Biotech,Large Cap,513.47,445.94,Q1
TechCorp,Aerospace,Mid Cap,859.41,349.63,Q2
<start>
| Company | Sector | Market Cap | Stock Price | Annual Revenue (B) | Quarter |
| --- | --- | --- | --- | --- | --- |
| HealthPlus | Finance | Small Cap | 546.92 | 373.02 | Q1 |
| FinanceWorks | Automotive | Large Cap | 204.75 | 303.25 | Q4 |
| RetailHub | Aerospace | Small Cap | 305.55 | 446.68 | Q1 |
| Foodies | Biotech | Large Cap | 513.47 | 445.94 | Q1 |
| TechCorp | Aerospace | Mid Cap | 859.41 | 349.63 | Q2 |
<end>Please transform the following yaml data into JSON:
- Birth Month: June
  City: Washington
  Income: 490000
  Name: Paisley
- Birth Month: August
  City: Boston
  Income: 225000
  Name: Don
- Birth Month: August
  City: Louisville
  Income: 320000
  Name: Dave
- Birth Month: January
  City: Baltimore
  Income: 370000
  Name: Marcella
- Birth Month: August
  City: Boston
  Income: 115000
  Name: Tracey
- Birth Month: July
  City: El Paso
  Income: 210000
  Name: Ollie
- Birth Month: October
  City: San Jose
  Income: 155000
  Name: Edgar
- Birth Month: May
  City: Jacksonville
  Income: 70000
  Name: Randy
<start>
[
    {
        "Name": "Paisley",
        "Birth Month": "June",
        "City": "Washington",
        "Income": 490000
    },
    {
        "Name": "Don",
        "Birth Month": "August",
        "City": "Boston",
        "Income": 225000
    },
    {
        "Name": "Dave",
        "Birth Month": "August",
        "City": "Louisville",
        "Income": 320000
    },
    {
        "Name": "Marcella",
        "Birth Month": "January",
        "City": "Baltimore",
        "Income": 370000
    },
    {
        "Name": "Tracey",
        "Birth Month": "August",
        "City": "Boston",
        "Income": 115000
    },
    {
        "Name": "Ollie",
        "Birth Month": "July",
        "City": "El Paso",
        "Income": 210000
    },
    {
        "Name": "Edgar",
        "Birth Month": "October",
        "City": "San Jose",
        "Income": 155000
    },
    {
        "Name": "Randy",
        "Birth Month": "May",
        "City": "Jacksonville",
        "Income": 70000
    }
]
<end>Transform this yml structure to a Plain text format:
- Location: Phoenix
  Price Range: $$$$$
- Location: San Francisco
  Price Range: $$
- Location: Phoenix
  Price Range: $$$$
<start>
Location: Phoenix | Price Range: $$$$$
Location: San Francisco | Price Range: $$
Location: Phoenix | Price Range: $$$$
<end>Transform this CSV structure to a plain text format:
Birth Month,City,Income
March,Las Vegas,340000
May,Detroit,495000
December,San Francisco,230000
January,San Francisco,45000
October,Seattle,305000
<start>
Birth Month: March | City: Las Vegas | Income: 340000
Birth Month: May | City: Detroit | Income: 495000
Birth Month: December | City: San Francisco | Income: 230000
Birth Month: January | City: San Francisco | Income: 45000
Birth Month: October | City: Seattle | Income: 305000
<end>Can you change this Markdown into Yaml?
| End Location | Distance (miles) | Fuel Used (gallons) |
| --- | --- | --- |
| Denver | 474.0 | 98.5 |
| Los Angeles | 1250.9 | 60.7 |
| Miami | 1250.9 | 6.5 |
| Miami | 932.6 | 24.8 |<start>
- Distance (miles): 474.0
  End Location: Denver
  Fuel Used (gallons): 98.5
- Distance (miles): 1250.9
  End Location: Los Angeles
  Fuel Used (gallons): 60.7
- Distance (miles): 1250.9
  End Location: Miami
  Fuel Used (gallons): 6.5
- Distance (miles): 932.6
  End Location: Miami
  Fuel Used (gallons): 24.8
<end>Please transform the following Plain text data into Markdown:
Age: 38 | Birth Month: April | City: Nashville
Age: 64 | Birth Month: July | City: Oklahoma City
Age: 31 | Birth Month: October | City: Las Vegas
Age: 58 | Birth Month: January | City: Memphis
Age: 68 | Birth Month: August | City: Detroit
Age: 29 | Birth Month: June | City: Phoenix
Age: 54 | Birth Month: September | City: Denver
<start>
| Age | Birth Month | City |
| --- | --- | --- |
| 38 | April | Nashville |
| 64 | July | Oklahoma City |
| 31 | October | Las Vegas |
| 58 | January | Memphis |
| 68 | August | Detroit |
| 29 | June | Phoenix |
| 54 | September | Denver |
<end>Please transform the following yaml data into markdown:
- Product Name: Gadget
  SKU: SKU-1034
  Stock Quantity: 21
  Supplier Name: Wayne Enterprises
- Product Name: Instrument
  SKU: SKU-1047
  Stock Quantity: 59
  Supplier Name: Wonka Industries
- Product Name: Contraption
  SKU: SKU-1054
  Stock Quantity: 384
  Supplier Name: Wonka Industries
- Product Name: Apparatus
  SKU: SKU-1062
  Stock Quantity: 135
  Supplier Name: Umbrella Corp
- Product Name: Instrument
  SKU: SKU-1098
  Stock Quantity: 181
  Supplier Name: Umbrella Corp
<start>
| Product Name | SKU | Stock Quantity | Supplier Name |
| --- | --- | --- | --- |
| Gadget | SKU-1034 | 21 | Wayne Enterprises |
| Instrument | SKU-1047 | 59 | Wonka Industries |
| Contraption | SKU-1054 | 384 | Wonka Industries |
| Apparatus | SKU-1062 | 135 | Umbrella Corp |
| Instrument | SKU-1098 | 181 | Umbrella Corp |
<end>Here's some Plain text data, can you convert it to Yaml?
SKU: SKU-1072 | Price: 51.68 | Stock Quantity: 170 | Category: Automotive | Supplier Name: Umbrella Corp
SKU: SKU-1014 | Price: 116.69 | Stock Quantity: 147 | Category: Household | Supplier Name: Umbrella Corp
SKU: SKU-1069 | Price: 69.85 | Stock Quantity: 493 | Category: Household | Supplier Name: Wonka Industries
SKU: SKU-1007 | Price: 259.81 | Stock Quantity: 469 | Category: Sports | Supplier Name: Wonka Industries
SKU: SKU-1067 | Price: 454.9 | Stock Quantity: 320 | Category: Sports | Supplier Name: ACME Corp
SKU: SKU-1017 | Price: 36.21 | Stock Quantity: 290 | Category: Sports | Supplier Name: ACME Corp
SKU: SKU-1057 | Price: 371.27 | Stock Quantity: 16 | Category: Electronics | Supplier Name: Umbrella Corp
SKU: SKU-1031 | Price: 105.62 | Stock Quantity: 392 | Category: Sports | Supplier Name: Wonka Industries
SKU: SKU-1008 | Price: 30.45 | Stock Quantity: 186 | Category: Electronics | Supplier Name: Wayne Enterprises
<start>
- Category: Automotive
  Price: 51.68
  SKU: SKU-1072
  Stock Quantity: 170
  Supplier Name: Umbrella Corp
- Category: Household
  Price: 116.69
  SKU: SKU-1014
  Stock Quantity: 147
  Supplier Name: Umbrella Corp
- Category: Household
  Price: 69.85
  SKU: SKU-1069
  Stock Quantity: 493
  Supplier Name: Wonka Industries
- Category: Sports
  Price: 259.81
  SKU: SKU-1007
  Stock Quantity: 469
  Supplier Name: Wonka Industries
- Category: Sports
  Price: 454.9
  SKU: SKU-1067
  Stock Quantity: 320
  Supplier Name: ACME Corp
- Category: Sports
  Price: 36.21
  SKU: SKU-1017
  Stock Quantity: 290
  Supplier Name: ACME Corp
- Category: Electronics
  Price: 371.27
  SKU: SKU-1057
  Stock Quantity: 16
  Supplier Name: Umbrella Corp
- Category: Sports
  Price: 105.62
  SKU: SKU-1031
  Stock Quantity: 392
  Supplier Name: Wonka Industries
- Category: Electronics
  Price: 30.45
  SKU: SKU-1008
  Stock Quantity: 186
  Supplier Name: Wayne Enterprises
<end>Please transform the following PLAIN TEXT data into Yml:
Company: GlobalTrade | Sector: Finance | Market Cap: Large Cap | Stock Price: 892.14 | Annual Revenue (B): 150.7
Company: AutoDrive | Sector: Automotive | Market Cap: Small Cap | Stock Price: 743.4 | Annual Revenue (B): 136.14
Company: EcoEnergy | Sector: Biotech | Market Cap: Large Cap | Stock Price: 291.9 | Annual Revenue (B): 330.66
Company: GlobalTrade | Sector: Automotive | Market Cap: Large Cap | Stock Price: 285.22 | Annual Revenue (B): 117.45
<start>
- Annual Revenue (B): 150.7
  Company: GlobalTrade
  Market Cap: Large Cap
  Sector: Finance
  Stock Price: 892.14
- Annual Revenue (B): 136.14
  Company: AutoDrive
  Market Cap: Small Cap
  Sector: Automotive
  Stock Price: 743.4
- Annual Revenue (B): 330.66
  Company: EcoEnergy
  Market Cap: Large Cap
  Sector: Biotech
  Stock Price: 291.9
- Annual Revenue (B): 117.45
  Company: GlobalTrade
  Market Cap: Large Cap
  Sector: Automotive
  Stock Price: 285.22
<end>Here's some csv data, can you convert it to plain text?
Location,Condition,Temperature (C),Humidity (%),Wind Speed (km/h),Day
Miami,Cloudy,4.0,65,28.7,Saturday
Phoenix,Foggy,8.7,65,24.8,Thursday
Phoenix,Windy,10.3,74,20.3,Monday
<start>
Location: Miami | Condition: Cloudy | Temperature (C): 4.0 | Humidity (%): 65 | Wind Speed (km/h): 28.7 | Day: Saturday
Location: Phoenix | Condition: Foggy | Temperature (C): 8.7 | Humidity (%): 65 | Wind Speed (km/h): 24.8 | Day: Thursday
Location: Phoenix | Condition: Windy | Temperature (C): 10.3 | Humidity (%): 74 | Wind Speed (km/h): 20.3 | Day: Monday
<end>Can you change this json into Csv?
[
    {
        "Restaurant Name": "The Golden Spoon",
        "Cuisine": "Italian"
    },
    {
        "Restaurant Name": "Pizza Planet",
        "Cuisine": "Italian"
    },
    {
        "Restaurant Name": "The Golden Spoon",
        "Cuisine": "American"
    },
    {
        "Restaurant Name": "The Golden Spoon",
        "Cuisine": "French"
    },
    {
        "Restaurant Name": "BBQ Barn",
        "Cuisine": "Japanese"
    }
]<start>
Restaurant Name,Cuisine
The Golden Spoon,Italian
Pizza Planet,Italian
The Golden Spoon,American
The Golden Spoon,French
BBQ Barn,Japanese
<end>Transform this plain text structure to a Markdown format:
Title: The Crystal Key | Genre: Romance
Title: The Silent Grove | Genre: Romance
Title: The Last Sky | Genre: Historical
Title: The Last Sky | Genre: Non-Fiction
Title: The Silent Grove | Genre: Science Fiction
Title: Echoes of Eternity | Genre: Non-Fiction
Title: Whispers of the Abyss | Genre: Fantasy
Title: Whispers of the Abyss | Genre: Horror
Title: Shadows of Solitude | Genre: Romance
Title: The Crystal Key | Genre: Fantasy
<start>
| Title | Genre |
| --- | --- |
| The Crystal Key | Romance |
| The Silent Grove | Romance |
| The Last Sky | Historical |
| The Last Sky | Non-Fiction |
| The Silent Grove | Science Fiction |
| Echoes of Eternity | Non-Fiction |
| Whispers of the Abyss | Fantasy |
| Whispers of the Abyss | Horror |
| Shadows of Solitude | Romance |
| The Crystal Key | Fantasy |
<end>Here's some JSON data, can you convert it to CSV?
[
    {
        "Birth Month": "February",
        "City": "Louisville",
        "Income": 205000
    },
    {
        "Birth Month": "December",
        "City": "San Jose",
        "Income": 135000
    },
    {
        "Birth Month": "September",
        "City": "Portland",
        "Income": 360000
    },
    {
        "Birth Month": "August",
        "City": "Fort Worth",
        "Income": 200000
    },
    {
        "Birth Month": "September",
        "City": "Phoenix",
        "Income": 320000
    },
    {
        "Birth Month": "August",
        "City": "Oklahoma City",
        "Income": 460000
    },
    {
        "Birth Month": "September",
        "City": "Seattle",
        "Income": 440000
    }
]<start>
Birth Month,City,Income
February,Louisville,205000
December,San Jose,135000
September,Portland,360000
August,Fort Worth,200000
September,Phoenix,320000
August,Oklahoma City,460000
September,Seattle,440000
<end>Can you change this csv into Json?
Device ID,Device Type,Location,Reading Value,Timestamp
device-0063,Light Sensor,Living Room,-16.88,2021-03-02 05:51:56
device-0019,Humidity Sensor,Garden,-24.08,2022-12-20 00:50:21
device-0082,Motion Detector,Bedroom,-24.08,2022-09-19 17:33:12
<start>
[
    {
        "Device ID": "device-0063",
        "Device Type": "Light Sensor",
        "Location": "Living Room",
        "Reading Value": -16.88,
        "Timestamp": "2021-03-02 05:51:56"
    },
    {
        "Device ID": "device-0019",
        "Device Type": "Humidity Sensor",
        "Location": "Garden",
        "Reading Value": -24.08,
        "Timestamp": "2022-12-20 00:50:21"
    },
    {
        "Device ID": "device-0082",
        "Device Type": "Motion Detector",
        "Location": "Bedroom",
        "Reading Value": -24.08,
        "Timestamp": "2022-09-19 17:33:12"
    }
]
<end>Please transform the following JSON data into CSV:
[
    {
        "Device ID": "device-0016",
        "Device Type": "Pressure Sensor",
        "Location": "Bathroom",
        "Battery Level (%)": 59.4,
        "Reading Value": 63.85,
        "Timestamp": "2021-05-05 01:49:19"
    },
    {
        "Device ID": "device-0053",
        "Device Type": "Motion Detector",
        "Location": "Garden",
        "Battery Level (%)": 68.0,
        "Reading Value": 71.21,
        "Timestamp": "2022-09-16 17:15:05"
    },
    {
        "Device ID": "device-0008",
        "Device Type": "Humidity Sensor",
        "Location": "Living Room",
        "Battery Level (%)": 47.2,
        "Reading Value": 31.51,
        "Timestamp": "2023-05-02 15:48:09"
    },
    {
        "Device ID": "device-0056",
        "Device Type": "Temperature Sensor",
        "Location": "Kitchen",
        "Battery Level (%)": 40.4,
        "Reading Value": 29.37,
        "Timestamp": "2021-01-18 23:01:12"
    },
    {
        "Device ID": "device-0002",
        "Device Type": "Motion Detector",
        "Location": "Bedroom",
        "Battery Level (%)": 66.1,
        "Reading Value": 57.6,
        "Timestamp": "2023-09-17 21:11:29"
    },
    {
        "Device ID": "device-0092",
        "Device Type": "Light Sensor",
        "Location": "Bedroom",
        "Battery Level (%)": 85.3,
        "Reading Value": -10.55,
        "Timestamp": "2021-02-06 08:52:40"
    },
    {
        "Device ID": "device-0087",
        "Device Type": "Motion Detector",
        "Location": "Hallway",
        "Battery Level (%)": 53.1,
        "Reading Value": -31.6,
        "Timestamp": "2023-10-08 17:03:50"
    }
]<start>
Device ID,Device Type,Location,Battery Level (%),Reading Value,Timestamp
device-0016,Pressure Sensor,Bathroom,59.4,63.85,2021-05-05 01:49:19
device-0053,Motion Detector,Garden,68.0,71.21,2022-09-16 17:15:05
device-0008,Humidity Sensor,Living Room,47.2,31.51,2023-05-02 15:48:09
device-0056,Temperature Sensor,Kitchen,40.4,29.37,2021-01-18 23:01:12
device-0002,Motion Detector,Bedroom,66.1,57.6,2023-09-17 21:11:29
device-0092,Light Sensor,Bedroom,85.3,-10.55,2021-02-06 08:52:40
device-0087,Motion Detector,Hallway,53.1,-31.6,2023-10-08 17:03:50
<end>Can you change this plain text into CSV?
Database Name: MetricsDB | Connection Count: 382 | Timestamp: 2023-04-18 23:07:00
Database Name: AnalyticsDB | Connection Count: 187 | Timestamp: 2021-04-08 21:14:27
Database Name: UserDB | Connection Count: 37 | Timestamp: 2023-08-11 06:14:55
Database Name: LogsDB | Connection Count: 360 | Timestamp: 2021-03-15 21:40:37
Database Name: ProductsDB | Connection Count: 202 | Timestamp: 2021-05-25 08:22:26
Database Name: MetricsDB | Connection Count: 438 | Timestamp: 2021-01-17 08:15:33
Database Name: SessionsDB | Connection Count: 489 | Timestamp: 2023-03-20 08:55:14
Database Name: ProductsDB | Connection Count: 264 | Timestamp: 2023-04-21 13:53:34
Database Name: LogsDB | Connection Count: 113 | Timestamp: 2022-04-24 12:17:03
<start>
Database Name,Connection Count,Timestamp
MetricsDB,382,2023-04-18 23:07:00
AnalyticsDB,187,2021-04-08 21:14:27
UserDB,37,2023-08-11 06:14:55
LogsDB,360,2021-03-15 21:40:37
ProductsDB,202,2021-05-25 08:22:26
MetricsDB,438,2021-01-17 08:15:33
SessionsDB,489,2023-03-20 08:55:14
ProductsDB,264,2023-04-21 13:53:34
LogsDB,113,2022-04-24 12:17:03
<end>Can you change this CSV into Yaml?
Restaurant Name,Cuisine,Location,Rating,Price Range
The Golden Spoon,Italian,Seattle,5,$$
Pasta Palace,Mediterranean,Seattle,4,$$$
Pasta Palace,French,Phoenix,5,$
Sushi World,Italian,Houston,5,$$$$
Burger Haven,Mediterranean,Chicago,4,$$
The Steakhouse,Italian,Chicago,4,$$$
<start>
- Cuisine: Italian
  Location: Seattle
  Price Range: $$
  Rating: 5
  Restaurant Name: The Golden Spoon
- Cuisine: Mediterranean
  Location: Seattle
  Price Range: $$$
  Rating: 4
  Restaurant Name: Pasta Palace
- Cuisine: French
  Location: Phoenix
  Price Range: $
  Rating: 5
  Restaurant Name: Pasta Palace
- Cuisine: Italian
  Location: Houston
  Price Range: $$$$
  Rating: 5
  Restaurant Name: Sushi World
- Cuisine: Mediterranean
  Location: Chicago
  Price Range: $$
  Rating: 4
  Restaurant Name: Burger Haven
- Cuisine: Italian
  Location: Chicago
  Price Range: $$$
  Rating: 4
  Restaurant Name: The Steakhouse
<end>Here's some PLAIN TEXT data, can you convert it to Markdown?
Name: Cleveland | Income: 395000
Name: Dawn | Income: 90000
Name: Isabelle | Income: 50000
Name: Taylor | Income: 150000
Name: Bennett | Income: 205000
Name: Eloise | Income: 40000
Name: Marian | Income: 495000
Name: Patricia | Income: 300000
Name: Ryan | Income: 390000
<start>
| Name | Income |
| --- | --- |
| Cleveland | 395000 |
| Dawn | 90000 |
| Isabelle | 50000 |
| Taylor | 150000 |
| Bennett | 205000 |
| Eloise | 40000 |
| Marian | 495000 |
| Patricia | 300000 |
| Ryan | 390000 |
<end>Transform this Markdown structure to a PLAIN TEXT format:
| Database Name | Connection Count | Average Latency (ms) | Timestamp |
| --- | --- | --- | --- |
| InventoryDB | 299 | 18.37 | 2023-02-08 20:18:04 |
| InventoryDB | 379 | 5.85 | 2021-02-17 01:04:49 |
| AnalyticsDB | 252 | 45.59 | 2023-11-17 02:01:05 |
| SessionsDB | 439 | 47.98 | 2023-01-16 19:57:14 |
| OrdersDB | 376 | 2.02 | 2022-05-20 14:56:49 |
| AnalyticsDB | 207 | 11.84 | 2022-08-22 03:42:32 |
| OrdersDB | 99 | 7.85 | 2023-10-06 12:24:53 |<start>
Database Name: InventoryDB | Connection Count: 299 | Average Latency (ms): 18.37 | Timestamp: 2023-02-08 20:18:04
Database Name: InventoryDB | Connection Count: 379 | Average Latency (ms): 5.85 | Timestamp: 2021-02-17 01:04:49
Database Name: AnalyticsDB | Connection Count: 252 | Average Latency (ms): 45.59 | Timestamp: 2023-11-17 02:01:05
Database Name: SessionsDB | Connection Count: 439 | Average Latency (ms): 47.98 | Timestamp: 2023-01-16 19:57:14
Database Name: OrdersDB | Connection Count: 376 | Average Latency (ms): 2.02 | Timestamp: 2022-05-20 14:56:49
Database Name: AnalyticsDB | Connection Count: 207 | Average Latency (ms): 11.84 | Timestamp: 2022-08-22 03:42:32
Database Name: OrdersDB | Connection Count: 99 | Average Latency (ms): 7.85 | Timestamp: 2023-10-06 12:24:53
<end>Transform this Markdown structure to a csv format:
| Location | Condition | Temperature (C) | Humidity (%) | Day |
| --- | --- | --- | --- | --- |
| Miami | Rainy | 0.9 | 83 | Wednesday |
| Miami | Rainy | 20.0 | 71 | Thursday |
| Chicago | Windy | 15.6 | 43 | Friday |
| Los Angeles | Stormy | 5.6 | 71 | Monday |<start>
Location,Condition,Temperature (C),Humidity (%),Day
Miami,Rainy,0.9,83,Wednesday
Miami,Rainy,20.0,71,Thursday
Chicago,Windy,15.6,43,Friday
Los Angeles,Stormy,5.6,71,Monday
<end>Please transform the following plain text data into Json:
Database Name: ProfilesDB | Queries per Second: 1801.46 | Cache Hit Ratio (%): 70.7 | Connection Count: 357 | Timestamp: 2021-10-17 02:41:00
Database Name: ProfilesDB | Queries per Second: 550.72 | Cache Hit Ratio (%): 82.64 | Connection Count: 137 | Timestamp: 2021-02-06 22:33:01
Database Name: LogsDB | Queries per Second: 3626.39 | Cache Hit Ratio (%): 81.85 | Connection Count: 243 | Timestamp: 2023-09-12 22:45:04
Database Name: SalesDB | Queries per Second: 4325.6 | Cache Hit Ratio (%): 82.93 | Connection Count: 289 | Timestamp: 2022-05-22 12:29:36
Database Name: AnalyticsDB | Queries per Second: 3765.33 | Cache Hit Ratio (%): 96.05 | Connection Count: 25 | Timestamp: 2023-11-21 21:42:40
<start>
[
    {
        "Database Name": "ProfilesDB",
        "Queries per Second": 1801.46,
        "Cache Hit Ratio (%)": 70.7,
        "Connection Count": 357,
        "Timestamp": "2021-10-17 02:41:00"
    },
    {
        "Database Name": "ProfilesDB",
        "Queries per Second": 550.72,
        "Cache Hit Ratio (%)": 82.64,
        "Connection Count": 137,
        "Timestamp": "2021-02-06 22:33:01"
    },
    {
        "Database Name": "LogsDB",
        "Queries per Second": 3626.39,
        "Cache Hit Ratio (%)": 81.85,
        "Connection Count": 243,
        "Timestamp": "2023-09-12 22:45:04"
    },
    {
        "Database Name": "SalesDB",
        "Queries per Second": 4325.6,
        "Cache Hit Ratio (%)": 82.93,
        "Connection Count": 289,
        "Timestamp": "2022-05-22 12:29:36"
    },
    {
        "Database Name": "AnalyticsDB",
        "Queries per Second": 3765.33,
        "Cache Hit Ratio (%)": 96.05,
        "Connection Count": 25,
        "Timestamp": "2023-11-21 21:42:40"
    }
]
<end>Convert this json to Markdown:
[
    {
        "Company": "MediaGroup",
        "Date": "2015-06-22",
        "Open Price": 1100.01,
        "Close Price": 432.3,
        "High Price": 1100.01,
        "Low Price": 432.3,
        "Volume": 4899976
    },
    {
        "Company": "GreenEnergy",
        "Date": "2019-04-22",
        "Open Price": 1092.4,
        "Close Price": 1217.22,
        "High Price": 1217.22,
        "Low Price": 39.61,
        "Volume": 3215012
    },
    {
        "Company": "HealthGen",
        "Date": "2020-08-12",
        "Open Price": 289.59,
        "Close Price": 892.36,
        "High Price": 1100.01,
        "Low Price": 289.59,
        "Volume": 6398510
    },
    {
        "Company": "GreenEnergy",
        "Date": "2014-02-09",
        "Open Price": 432.3,
        "Close Price": 154.63,
        "High Price": 432.3,
        "Low Price": 154.63,
        "Volume": 5880510
    }
]<start>
| Company | Date | Open Price | Close Price | High Price | Low Price | Volume |
| --- | --- | --- | --- | --- | --- | --- |
| MediaGroup | 2015-06-22 | 1100.01 | 432.3 | 1100.01 | 432.3 | 4899976 |
| GreenEnergy | 2019-04-22 | 1092.4 | 1217.22 | 1217.22 | 39.61 | 3215012 |
| HealthGen | 2020-08-12 | 289.59 | 892.36 | 1100.01 | 289.59 | 6398510 |
| GreenEnergy | 2014-02-09 | 432.3 | 154.63 | 432.3 | 154.63 | 5880510 |
<end>Here's some Markdown data, can you convert it to CSV?
| Company | Sector | Market Cap | Stock Price | Annual Revenue (B) |
| --- | --- | --- | --- | --- |
| RetailHub | Finance | Small Cap | 154.2 | 325.63 |
| EcoEnergy | Aerospace | Small Cap | 901.82 | 65.53 |
| GlobalTrade | Energy | Small Cap | 865.08 | 399.86 |
| EcoEnergy | Automotive | Mega Cap | 226.6 | 357.68 |
| Foodies | Aerospace | Mid Cap | 182.14 | 357.5 |<start>
Company,Sector,Market Cap,Stock Price,Annual Revenue (B)
RetailHub,Finance,Small Cap,154.2,325.63
EcoEnergy,Aerospace,Small Cap,901.82,65.53
GlobalTrade,Energy,Small Cap,865.08,399.86
EcoEnergy,Automotive,Mega Cap,226.6,357.68
Foodies,Aerospace,Mid Cap,182.14,357.5
<end>Please transform the following plain text data into csv:
Age: 19 | Birth Month: June | City: Louisville | Income: 165000
Age: 60 | Birth Month: May | City: San Diego | Income: 260000
Age: 43 | Birth Month: January | City: Austin | Income: 160000
Age: 38 | Birth Month: August | City: San Jose | Income: 410000
Age: 66 | Birth Month: November | City: Oklahoma City | Income: 475000
Age: 29 | Birth Month: March | City: San Diego | Income: 60000
Age: 18 | Birth Month: January | City: Indianapolis | Income: 400000
Age: 24 | Birth Month: January | City: Seattle | Income: 420000
Age: 58 | Birth Month: August | City: Dallas | Income: 185000
<start>
Age,Birth Month,City,Income
19,June,Louisville,165000
60,May,San Diego,260000
43,January,Austin,160000
38,August,San Jose,410000
66,November,Oklahoma City,475000
29,March,San Diego,60000
18,January,Indianapolis,400000
24,January,Seattle,420000
58,August,Dallas,185000
<end>Transform this MARKDOWN structure to a plain text format:
| Trip Name | Start Location | End Location | Distance (miles) | Duration (hours) | Fuel Used (gallons) |
| --- | --- | --- | --- | --- | --- |
| Mountain Adventure | Denver | San Francisco | 1272.1 | 45.2 | 57.8 |
| Valley Voyage | Los Angeles | Houston | 2857.1 | 11.9 | 8.5 |
| Historic Route | Chicago | San Francisco | 2485.3 | 3.6 | 54.2 |<start>
Trip Name: Mountain Adventure | Start Location: Denver | End Location: San Francisco | Distance (miles): 1272.1 | Duration (hours): 45.2 | Fuel Used (gallons): 57.8
Trip Name: Valley Voyage | Start Location: Los Angeles | End Location: Houston | Distance (miles): 2857.1 | Duration (hours): 11.9 | Fuel Used (gallons): 8.5
Trip Name: Historic Route | Start Location: Chicago | End Location: San Francisco | Distance (miles): 2485.3 | Duration (hours): 3.6 | Fuel Used (gallons): 54.2
<end>Convert this json to yml:
[
    {
        "Location": "Houston",
        "Condition": "Sunny",
        "Temperature (C)": 30.5,
        "Wind Speed (km/h)": 15.1,
        "Day": "Monday"
    },
    {
        "Location": "New York",
        "Condition": "Sunny",
        "Temperature (C)": 16.2,
        "Wind Speed (km/h)": 3.7,
        "Day": "Tuesday"
    },
    {
        "Location": "New York",
        "Condition": "Rainy",
        "Temperature (C)": 6.4,
        "Wind Speed (km/h)": 0.7,
        "Day": "Friday"
    },
    {
        "Location": "Phoenix",
        "Condition": "Stormy",
        "Temperature (C)": -6.5,
        "Wind Speed (km/h)": 14.2,
        "Day": "Friday"
    },
    {
        "Location": "New York",
        "Condition": "Stormy",
        "Temperature (C)": 30.6,
        "Wind Speed (km/h)": 6.4,
        "Day": "Sunday"
    },
    {
        "Location": "Phoenix",
        "Condition": "Rainy",
        "Temperature (C)": 39.3,
        "Wind Speed (km/h)": 2.2,
        "Day": "Sunday"
    },
    {
        "Location": "Denver",
        "Condition": "Snowy",
        "Temperature (C)": 32.7,
        "Wind Speed (km/h)": 9.9,
        "Day": "Wednesday"
    },
    {
        "Location": "Phoenix",
        "Condition": "Sunny",
        "Temperature (C)": 39.1,
        "Wind Speed (km/h)": 18.6,
        "Day": "Friday"
    },
    {
        "Location": "Phoenix",
        "Condition": "Foggy",
        "Temperature (C)": 29.3,
        "Wind Speed (km/h)": 6.4,
        "Day": "Friday"
    },
    {
        "Location": "Los Angeles",
        "Condition": "Foggy",
        "Temperature (C)": 11.5,
        "Wind Speed (km/h)": 25.1,
        "Day": "Friday"
    }
]<start>
- Condition: Sunny
  Day: Monday
  Location: Houston
  Temperature (C): 30.5
  Wind Speed (km/h): 15.1
- Condition: Sunny
  Day: Tuesday
  Location: New York
  Temperature (C): 16.2
  Wind Speed (km/h): 3.7
- Condition: Rainy
  Day: Friday
  Location: New York
  Temperature (C): 6.4
  Wind Speed (km/h): 0.7
- Condition: Stormy
  Day: Friday
  Location: Phoenix
  Temperature (C): -6.5
  Wind Speed (km/h): 14.2
- Condition: Stormy
  Day: Sunday
  Location: New York
  Temperature (C): 30.6
  Wind Speed (km/h): 6.4
- Condition: Rainy
  Day: Sunday
  Location: Phoenix
  Temperature (C): 39.3
  Wind Speed (km/h): 2.2
- Condition: Snowy
  Day: Wednesday
  Location: Denver
  Temperature (C): 32.7
  Wind Speed (km/h): 9.9
- Condition: Sunny
  Day: Friday
  Location: Phoenix
  Temperature (C): 39.1
  Wind Speed (km/h): 18.6
- Condition: Foggy
  Day: Friday
  Location: Phoenix
  Temperature (C): 29.3
  Wind Speed (km/h): 6.4
- Condition: Foggy
  Day: Friday
  Location: Los Angeles
  Temperature (C): 11.5
  Wind Speed (km/h): 25.1
<end>Convert this markdown to JSON:
| Title | Genre | Rating |
| --- | --- | --- |
| The Last Sky | Science Fiction | 1.7 |
| Tales of the Brave | Horror | 3.7 |
| Whispers of the Abyss | Horror | 4.2 |
| The Last Sky | Thriller | 1.2 |
| The Forgotten World | Fantasy | 2.9 |<start>
[
    {
        "Title": "The Last Sky",
        "Genre": "Science Fiction",
        "Rating": 1.7
    },
    {
        "Title": "Tales of the Brave",
        "Genre": "Horror",
        "Rating": 3.7
    },
    {
        "Title": "Whispers of the Abyss",
        "Genre": "Horror",
        "Rating": 4.2
    },
    {
        "Title": "The Last Sky",
        "Genre": "Thriller",
        "Rating": 1.2
    },
    {
        "Title": "The Forgotten World",
        "Genre": "Fantasy",
        "Rating": 2.9
    }
]
<end>Can you change this yml into JSON?
- Company: AutoMotive
  Date: '2022-06-12'
  High Price: 569.36
  Low Price: 83.89
- Company: AutoMotive
  Date: '2018-08-11'
  High Price: 1138.69
  Low Price: 361.76
- Company: RetailWorld
  Date: '2012-04-11'
  High Price: 1414.18
  Low Price: 648.65
- Company: GreenEnergy
  Date: '2015-05-05'
  High Price: 1324.18
  Low Price: 41.36
<start>
[
    {
        "Company": "AutoMotive",
        "Date": "2022-06-12",
        "High Price": 569.36,
        "Low Price": 83.89
    },
    {
        "Company": "AutoMotive",
        "Date": "2018-08-11",
        "High Price": 1138.69,
        "Low Price": 361.76
    },
    {
        "Company": "RetailWorld",
        "Date": "2012-04-11",
        "High Price": 1414.18,
        "Low Price": 648.65
    },
    {
        "Company": "GreenEnergy",
        "Date": "2015-05-05",
        "High Price": 1324.18,
        "Low Price": 41.36
    }
]
<end>Please transform the following MARKDOWN data into Plain text:
| Name | Age |
| --- | --- |
| Lloyd | 54 |
| Eva | 59 |
| Bernice | 41 |
| Douglas | 20 |
| Stefanie | 26 |
| Lucille | 53 |
| Virginia | 41 |
| Flora | 52 |
| Belle | 31 |<start>
Name: Lloyd | Age: 54
Name: Eva | Age: 59
Name: Bernice | Age: 41
Name: Douglas | Age: 20
Name: Stefanie | Age: 26
Name: Lucille | Age: 53
Name: Virginia | Age: 41
Name: Flora | Age: 52
Name: Belle | Age: 31
<end>Can you change this Markdown into CSV?
| Trip Name | Start Location | End Location | Distance (miles) | Duration (hours) |
| --- | --- | --- | --- | --- |
| Historic Route | Miami | San Francisco | 1177.0 | 46.5 |
| Valley Voyage | Houston | Denver | 987.6 | 50.4 |
| Forest Journey | Phoenix | New York | 914.3 | 66.1 |
| Mountain Adventure | Los Angeles | Houston | 1619.2 | 14.3 |<start>
Trip Name,Start Location,End Location,Distance (miles),Duration (hours)
Historic Route,Miami,San Francisco,1177.0,46.5
Valley Voyage,Houston,Denver,987.6,50.4
Forest Journey,Phoenix,New York,914.3,66.1
Mountain Adventure,Los Angeles,Houston,1619.2,14.3
<end>Convert this Markdown to csv:
| Company | Open Price | Close Price | Low Price | Volume |
| --- | --- | --- | --- | --- |
| HealthGen | 790.83 | 1167.79 | 368.42 | 7371462 |
| GreenEnergy | 660.35 | 156.72 | 156.72 | 6049042 |
| RetailWorld | 429.11 | 1047.41 | 429.11 | 9240684 |
| MediaGroup | 920.58 | 118.07 | 118.07 | 3969924 |
| FinanceTrust | 91.85 | 517.3 | 91.85 | 5273337 |
| RetailWorld | 1460.7 | 663.35 | 663.35 | 7010939 |<start>
Company,Open Price,Close Price,Low Price,Volume
HealthGen,790.83,1167.79,368.42,7371462
GreenEnergy,660.35,156.72,156.72,6049042
RetailWorld,429.11,1047.41,429.11,9240684
MediaGroup,920.58,118.07,118.07,3969924
FinanceTrust,91.85,517.3,91.85,5273337
RetailWorld,1460.7,663.35,663.35,7010939
<end>Transform this markdown structure to a Plain text format:
| Rating | Price Range |
| --- | --- |
| 1 | $$$ |
| 3 | $$$$ |
| 5 | $$$ |
| 1 | $ |<start>
Rating: 1 | Price Range: $$$
Rating: 3 | Price Range: $$$$
Rating: 5 | Price Range: $$$
Rating: 1 | Price Range: $
<end>Here's some json data, can you convert it to yml?
[
    {
        "Device ID": "device-0080",
        "Device Type": "Temperature Sensor",
        "Location": "Hallway",
        "Battery Level (%)": 47.8,
        "Reading Value": -35.82,
        "Timestamp": "2023-02-03 03:26:31"
    },
    {
        "Device ID": "device-0068",
        "Device Type": "Humidity Sensor",
        "Location": "Hallway",
        "Battery Level (%)": 27.1,
        "Reading Value": 7.77,
        "Timestamp": "2022-02-22 17:38:26"
    },
    {
        "Device ID": "device-0051",
        "Device Type": "Pressure Sensor",
        "Location": "Office",
        "Battery Level (%)": 72.6,
        "Reading Value": 26.12,
        "Timestamp": "2023-05-11 01:23:13"
    }
]<start>
- Battery Level (%): 47.8
  Device ID: device-0080
  Device Type: Temperature Sensor
  Location: Hallway
  Reading Value: -35.82
  Timestamp: '2023-02-03 03:26:31'
- Battery Level (%): 27.1
  Device ID: device-0068
  Device Type: Humidity Sensor
  Location: Hallway
  Reading Value: 7.77
  Timestamp: '2022-02-22 17:38:26'
- Battery Level (%): 72.6
  Device ID: device-0051
  Device Type: Pressure Sensor
  Location: Office
  Reading Value: 26.12
  Timestamp: '2023-05-11 01:23:13'
<end>Can you change this plain text into markdown?
Sector: Biotech | Stock Price: 568.64 | Annual Revenue (B): 284.99 | Quarter: Q1
Sector: Technology | Stock Price: 650.57 | Annual Revenue (B): 239.31 | Quarter: Q1
Sector: Energy | Stock Price: 923.9 | Annual Revenue (B): 384.36 | Quarter: Q2
Sector: Biotech | Stock Price: 795.25 | Annual Revenue (B): 417.09 | Quarter: Q1
Sector: Retail | Stock Price: 240.93 | Annual Revenue (B): 174.62 | Quarter: Q3
Sector: Finance | Stock Price: 158.34 | Annual Revenue (B): 177.92 | Quarter: Q1
Sector: Automotive | Stock Price: 568.64 | Annual Revenue (B): 149.33 | Quarter: Q2
Sector: Retail | Stock Price: 368.4 | Annual Revenue (B): 301.14 | Quarter: Q1
<start>
| Sector | Stock Price | Annual Revenue (B) | Quarter |
| --- | --- | --- | --- |
| Biotech | 568.64 | 284.99 | Q1 |
| Technology | 650.57 | 239.31 | Q1 |
| Energy | 923.9 | 384.36 | Q2 |
| Biotech | 795.25 | 417.09 | Q1 |
| Retail | 240.93 | 174.62 | Q3 |
| Finance | 158.34 | 177.92 | Q1 |
| Automotive | 568.64 | 149.33 | Q2 |
| Retail | 368.4 | 301.14 | Q1 |
<end>Convert this markdown to csv:
| SKU | Price | Category | Supplier Name |
| --- | --- | --- | --- |
| SKU-1077 | 69.62 | Electronics | Wonka Industries |
| SKU-1025 | 40.37 | Sports | Globex |
| SKU-1080 | 178.72 | Electronics | Umbrella Corp |
| SKU-1014 | 411.43 | Toys | Globex |<start>
SKU,Price,Category,Supplier Name
SKU-1077,69.62,Electronics,Wonka Industries
SKU-1025,40.37,Sports,Globex
SKU-1080,178.72,Electronics,Umbrella Corp
SKU-1014,411.43,Toys,Globex
<end>Here's some plain text data, can you convert it to YML?
Device Type: Light Sensor | Battery Level (%): 29.2 | Timestamp: 2021-10-24 18:20:30
Device Type: Pressure Sensor | Battery Level (%): 73.1 | Timestamp: 2022-04-12 22:14:13
Device Type: Light Sensor | Battery Level (%): 96.5 | Timestamp: 2021-08-19 08:40:46
Device Type: Humidity Sensor | Battery Level (%): 50.4 | Timestamp: 2021-09-09 04:43:11
<start>
- Battery Level (%): 29.2
  Device Type: Light Sensor
  Timestamp: '2021-10-24 18:20:30'
- Battery Level (%): 73.1
  Device Type: Pressure Sensor
  Timestamp: '2022-04-12 22:14:13'
- Battery Level (%): 96.5
  Device Type: Light Sensor
  Timestamp: '2021-08-19 08:40:46'
- Battery Level (%): 50.4
  Device Type: Humidity Sensor
  Timestamp: '2021-09-09 04:43:11'
<end>Can you change this Markdown into plain text?
| End Location | Distance (miles) | Fuel Used (gallons) |
| --- | --- | --- |
| Phoenix | 570.3 | 35.4 |
| Chicago | 1224.9 | 14.9 |
| Los Angeles | 388.3 | 93.1 |
| Los Angeles | 1251.6 | 35.2 |
| Houston | 379.3 | 88.1 |
| Miami | 904.9 | 70.3 |
| Chicago | 741.2 | 30.5 |
| Houston | 1969.5 | 8.9 |<start>
End Location: Phoenix | Distance (miles): 570.3 | Fuel Used (gallons): 35.4
End Location: Chicago | Distance (miles): 1224.9 | Fuel Used (gallons): 14.9
End Location: Los Angeles | Distance (miles): 388.3 | Fuel Used (gallons): 93.1
End Location: Los Angeles | Distance (miles): 1251.6 | Fuel Used (gallons): 35.2
End Location: Houston | Distance (miles): 379.3 | Fuel Used (gallons): 88.1
End Location: Miami | Distance (miles): 904.9 | Fuel Used (gallons): 70.3
End Location: Chicago | Distance (miles): 741.2 | Fuel Used (gallons): 30.5
End Location: Houston | Distance (miles): 1969.5 | Fuel Used (gallons): 8.9
<end>Can you change this markdown into plain text?
| Market Cap | Stock Price | Annual Revenue (B) |
| --- | --- | --- |
| Small Cap | 648.57 | 380.83 |
| Small Cap | 247.46 | 247.31 |
| Mega Cap | 79.56 | 370.47 |
| Mega Cap | 349.84 | 338.06 |
| Small Cap | 281.36 | 457.02 |<start>
Market Cap: Small Cap | Stock Price: 648.57 | Annual Revenue (B): 380.83
Market Cap: Small Cap | Stock Price: 247.46 | Annual Revenue (B): 247.31
Market Cap: Mega Cap | Stock Price: 79.56 | Annual Revenue (B): 370.47
Market Cap: Mega Cap | Stock Price: 349.84 | Annual Revenue (B): 338.06
Market Cap: Small Cap | Stock Price: 281.36 | Annual Revenue (B): 457.02
<end>Please transform the following csv data into yml:
Database Name,Queries per Second,Cache Hit Ratio (%),Connection Count,Timestamp
MetricsDB,4290.38,70.32,429,2022-09-14 15:44:36
ProductsDB,3783.62,83.84,382,2022-04-19 01:38:51
MetricsDB,2109.34,88.47,139,2023-03-08 23:13:31
SalesDB,1452.71,81.54,430,2022-08-04 02:59:31
LogsDB,1548.85,79.1,14,2023-07-15 01:51:33
InventoryDB,462.5,99.82,139,2022-07-28 05:07:09
OrdersDB,4378.77,96.37,429,2021-06-07 13:33:13
SessionsDB,4290.38,70.32,139,2021-01-23 02:10:36
<start>
- Cache Hit Ratio (%): 70.32
  Connection Count: 429
  Database Name: MetricsDB
  Queries per Second: 4290.38
  Timestamp: '2022-09-14 15:44:36'
- Cache Hit Ratio (%): 83.84
  Connection Count: 382
  Database Name: ProductsDB
  Queries per Second: 3783.62
  Timestamp: '2022-04-19 01:38:51'
- Cache Hit Ratio (%): 88.47
  Connection Count: 139
  Database Name: MetricsDB
  Queries per Second: 2109.34
  Timestamp: '2023-03-08 23:13:31'
- Cache Hit Ratio (%): 81.54
  Connection Count: 430
  Database Name: SalesDB
  Queries per Second: 1452.71
  Timestamp: '2022-08-04 02:59:31'
- Cache Hit Ratio (%): 79.1
  Connection Count: 14
  Database Name: LogsDB
  Queries per Second: 1548.85
  Timestamp: '2023-07-15 01:51:33'
- Cache Hit Ratio (%): 99.82
  Connection Count: 139
  Database Name: InventoryDB
  Queries per Second: 462.5
  Timestamp: '2022-07-28 05:07:09'
- Cache Hit Ratio (%): 96.37
  Connection Count: 429
  Database Name: OrdersDB
  Queries per Second: 4378.77
  Timestamp: '2021-06-07 13:33:13'
- Cache Hit Ratio (%): 70.32
  Connection Count: 139
  Database Name: SessionsDB
  Queries per Second: 4290.38
  Timestamp: '2021-01-23 02:10:36'
<end>Please transform the following csv data into Plain text:
Title,Author,Genre,Publication Year
Whispers of the Abyss,Kara Firebrand,Mystery,1971
Legends of the Rift,Draven Blackthorn,Romance,2003
A Journey Through Time,Rowan Ashborne,Romance,1991
<start>
Title: Whispers of the Abyss | Author: Kara Firebrand | Genre: Mystery | Publication Year: 1971
Title: Legends of the Rift | Author: Draven Blackthorn | Genre: Romance | Publication Year: 2003
Title: A Journey Through Time | Author: Rowan Ashborne | Genre: Romance | Publication Year: 1991
<end>Can you change this json into Plain text?
[
    {
        "Author": "Draven Blackthorn",
        "Genre": "Horror",
        "Rating": 2.4
    },
    {
        "Author": "Luna Silverleaf",
        "Genre": "Science Fiction",
        "Rating": 4.6
    },
    {
        "Author": "Isla Windrider",
        "Genre": "Non-Fiction",
        "Rating": 4.4
    },
    {
        "Author": "Galen Starfire",
        "Genre": "Science Fiction",
        "Rating": 4.9
    }
]<start>
Author: Draven Blackthorn | Genre: Horror | Rating: 2.4
Author: Luna Silverleaf | Genre: Science Fiction | Rating: 4.6
Author: Isla Windrider | Genre: Non-Fiction | Rating: 4.4
Author: Galen Starfire | Genre: Science Fiction | Rating: 4.9
<end>Transform this csv structure to a json format:
Company,Date,Open Price,Close Price,High Price,Low Price,Volume
GreenEnergy,2013-01-03,876.73,446.87,876.73,360.27,3326967
HealthGen,2022-05-13,124.33,311.81,311.81,124.33,6876985
FoodChain,2010-02-19,405.13,80.92,405.13,80.92,5142964
FinanceTrust,2021-09-16,1363.4,291.34,1363.4,291.34,9889025
FinanceTrust,2012-05-16,1341.39,784.2,1341.39,784.2,8138389
AutoMotive,2014-02-11,1107.35,1330.42,1330.42,1107.35,2010422
HealthGen,2014-03-23,357.73,420.4,420.4,357.73,5983120
<start>
[
    {
        "Company": "GreenEnergy",
        "Date": "2013-01-03",
        "Open Price": 876.73,
        "Close Price": 446.87,
        "High Price": 876.73,
        "Low Price": 360.27,
        "Volume": 3326967
    },
    {
        "Company": "HealthGen",
        "Date": "2022-05-13",
        "Open Price": 124.33,
        "Close Price": 311.81,
        "High Price": 311.81,
        "Low Price": 124.33,
        "Volume": 6876985
    },
    {
        "Company": "FoodChain",
        "Date": "2010-02-19",
        "Open Price": 405.13,
        "Close Price": 80.92,
        "High Price": 405.13,
        "Low Price": 80.92,
        "Volume": 5142964
    },
    {
        "Company": "FinanceTrust",
        "Date": "2021-09-16",
        "Open Price": 1363.4,
        "Close Price": 291.34,
        "High Price": 1363.4,
        "Low Price": 291.34,
        "Volume": 9889025
    },
    {
        "Company": "FinanceTrust",
        "Date": "2012-05-16",
        "Open Price": 1341.39,
        "Close Price": 784.2,
        "High Price": 1341.39,
        "Low Price": 784.2,
        "Volume": 8138389
    },
    {
        "Company": "AutoMotive",
        "Date": "2014-02-11",
        "Open Price": 1107.35,
        "Close Price": 1330.42,
        "High Price": 1330.42,
        "Low Price": 1107.35,
        "Volume": 2010422
    },
    {
        "Company": "HealthGen",
        "Date": "2014-03-23",
        "Open Price": 357.73,
        "Close Price": 420.4,
        "High Price": 420.4,
        "Low Price": 357.73,
        "Volume": 5983120
    }
]
<end>Please transform the following yml data into JSON:
- Distance (miles): 1754.1
  Duration (hours): 45.8
  End Location: Los Angeles
  Trip Name: Highway Odyssey
- Distance (miles): 2216.3
  Duration (hours): 17.4
  End Location: New York
  Trip Name: Forest Journey
- Distance (miles): 2604.6
  Duration (hours): 20.0
  End Location: Los Angeles
  Trip Name: Forest Journey
- Distance (miles): 626.9
  Duration (hours): 5.8
  End Location: Chicago
  Trip Name: Canyon Trek
- Distance (miles): 537.0
  Duration (hours): 69.0
  End Location: San Francisco
  Trip Name: Coast to Coast
<start>
[
    {
        "Trip Name": "Highway Odyssey",
        "End Location": "Los Angeles",
        "Distance (miles)": 1754.1,
        "Duration (hours)": 45.8
    },
    {
        "Trip Name": "Forest Journey",
        "End Location": "New York",
        "Distance (miles)": 2216.3,
        "Duration (hours)": 17.4
    },
    {
        "Trip Name": "Forest Journey",
        "End Location": "Los Angeles",
        "Distance (miles)": 2604.6,
        "Duration (hours)": 20.0
    },
    {
        "Trip Name": "Canyon Trek",
        "End Location": "Chicago",
        "Distance (miles)": 626.9,
        "Duration (hours)": 5.8
    },
    {
        "Trip Name": "Coast to Coast",
        "End Location": "San Francisco",
        "Distance (miles)": 537.0,
        "Duration (hours)": 69.0
    }
]
<end>Here's some yml data, can you convert it to JSON?
- Publication Year: 1962
  Rating: 2.3
  Title: The Last Sky
- Publication Year: 2020
  Rating: 2.0
  Title: Echoes of Eternity
- Publication Year: 1968
  Rating: 1.3
  Title: Whispers of the Abyss
- Publication Year: 2009
  Rating: 2.7
  Title: The Crystal Key
<start>
[
    {
        "Title": "The Last Sky",
        "Publication Year": 1962,
        "Rating": 2.3
    },
    {
        "Title": "Echoes of Eternity",
        "Publication Year": 2020,
        "Rating": 2.0
    },
    {
        "Title": "Whispers of the Abyss",
        "Publication Year": 1968,
        "Rating": 1.3
    },
    {
        "Title": "The Crystal Key",
        "Publication Year": 2009,
        "Rating": 2.7
    }
]
<end>Can you change this csv into plain text?
Name,Age,Birth Month,City,Income
Krystal,22,December,Las Vegas,375000
Kylie,50,March,Portland,275000
Adalyn,52,February,Las Vegas,450000
Heidi,46,July,Austin,490000
Robin,41,November,Houston,175000
Arianna,20,May,San Francisco,205000
<start>
Name: Krystal | Age: 22 | Birth Month: December | City: Las Vegas | Income: 375000
Name: Kylie | Age: 50 | Birth Month: March | City: Portland | Income: 275000
Name: Adalyn | Age: 52 | Birth Month: February | City: Las Vegas | Income: 450000
Name: Heidi | Age: 46 | Birth Month: July | City: Austin | Income: 490000
Name: Robin | Age: 41 | Birth Month: November | City: Houston | Income: 175000
Name: Arianna | Age: 20 | Birth Month: May | City: San Francisco | Income: 205000
<end>Please transform the following YML data into JSON:
- Box Office Earnings (M): 581.61
  Director: Rylan Frostblade
  Genre: Drama
  Release Year: 1971
- Box Office Earnings (M): 300.74
  Director: Mara Moonshadow
  Genre: Drama
  Release Year: 2022
- Box Office Earnings (M): 974.69
  Director: Aria Ravenwood
  Genre: Drama
  Release Year: 2005
- Box Office Earnings (M): 73.05
  Director: Lira Silverleaf
  Genre: Action
  Release Year: 2017
- Box Office Earnings (M): 773.06
  Director: Cade Firebrand
  Genre: Thriller
  Release Year: 2022
- Box Office Earnings (M): 988.53
  Director: Zara Stormrider
  Genre: Thriller
  Release Year: 2000
- Box Office Earnings (M): 825.93
  Director: Drake Nightshade
  Genre: Adventure
  Release Year: 2009
- Box Office Earnings (M): 15.14
  Director: Drake Nightshade
  Genre: Thriller
  Release Year: 2011
- Box Office Earnings (M): 605.46
  Director: Cade Firebrand
  Genre: Drama
  Release Year: 2019
- Box Office Earnings (M): 581.61
  Director: Rylan Frostblade
  Genre: Comedy
  Release Year: 1971
<start>
[
    {
        "Director": "Rylan Frostblade",
        "Genre": "Drama",
        "Release Year": 1971,
        "Box Office Earnings (M)": 581.61
    },
    {
        "Director": "Mara Moonshadow",
        "Genre": "Drama",
        "Release Year": 2022,
        "Box Office Earnings (M)": 300.74
    },
    {
        "Director": "Aria Ravenwood",
        "Genre": "Drama",
        "Release Year": 2005,
        "Box Office Earnings (M)": 974.69
    },
    {
        "Director": "Lira Silverleaf",
        "Genre": "Action",
        "Release Year": 2017,
        "Box Office Earnings (M)": 73.05
    },
    {
        "Director": "Cade Firebrand",
        "Genre": "Thriller",
        "Release Year": 2022,
        "Box Office Earnings (M)": 773.06
    },
    {
        "Director": "Zara Stormrider",
        "Genre": "Thriller",
        "Release Year": 2000,
        "Box Office Earnings (M)": 988.53
    },
    {
        "Director": "Drake Nightshade",
        "Genre": "Adventure",
        "Release Year": 2009,
        "Box Office Earnings (M)": 825.93
    },
    {
        "Director": "Drake Nightshade",
        "Genre": "Thriller",
        "Release Year": 2011,
        "Box Office Earnings (M)": 15.14
    },
    {
        "Director": "Cade Firebrand",
        "Genre": "Drama",
        "Release Year": 2019,
        "Box Office Earnings (M)": 605.46
    },
    {
        "Director": "Rylan Frostblade",
        "Genre": "Comedy",
        "Release Year": 1971,
        "Box Office Earnings (M)": 581.61
    }
]
<end>Can you change this Json into YAML?
[
    {
        "Database Name": "MetricsDB",
        "Queries per Second": 3410.89,
        "Cache Hit Ratio (%)": 73.37,
        "Connection Count": 137,
        "Average Latency (ms)": 17.08,
        "Timestamp": "2023-05-13 05:05:25"
    },
    {
        "Database Name": "OrdersDB",
        "Queries per Second": 3435.78,
        "Cache Hit Ratio (%)": 83.63,
        "Connection Count": 69,
        "Average Latency (ms)": 64.93,
        "Timestamp": "2021-01-17 16:13:48"
    },
    {
        "Database Name": "SalesDB",
        "Queries per Second": 2275.16,
        "Cache Hit Ratio (%)": 95.95,
        "Connection Count": 285,
        "Average Latency (ms)": 43.78,
        "Timestamp": "2022-07-23 15:34:16"
    },
    {
        "Database Name": "SalesDB",
        "Queries per Second": 1750.39,
        "Cache Hit Ratio (%)": 96.05,
        "Connection Count": 223,
        "Average Latency (ms)": 97.09,
        "Timestamp": "2023-02-14 18:12:55"
    },
    {
        "Database Name": "InventoryDB",
        "Queries per Second": 3918.7,
        "Cache Hit Ratio (%)": 85.3,
        "Connection Count": 27,
        "Average Latency (ms)": 17.08,
        "Timestamp": "2022-05-12 00:49:54"
    },
    {
        "Database Name": "UserDB",
        "Queries per Second": 3918.7,
        "Cache Hit Ratio (%)": 94.09,
        "Connection Count": 105,
        "Average Latency (ms)": 42.88,
        "Timestamp": "2022-01-21 15:22:10"
    },
    {
        "Database Name": "UserDB",
        "Queries per Second": 610.88,
        "Cache Hit Ratio (%)": 95.95,
        "Connection Count": 27,
        "Average Latency (ms)": 10.85,
        "Timestamp": "2023-03-13 11:00:14"
    },
    {
        "Database Name": "ProductsDB",
        "Queries per Second": 3001.36,
        "Cache Hit Ratio (%)": 95.95,
        "Connection Count": 300,
        "Average Latency (ms)": 75.08,
        "Timestamp": "2021-10-06 05:43:10"
    },
    {
        "Database Name": "MetricsDB",
        "Queries per Second": 4754.49,
        "Cache Hit Ratio (%)": 88.25,
        "Connection Count": 137,
        "Average Latency (ms)": 2.37,
        "Timestamp": "2023-11-11 01:27:01"
    }
]<start>
- Average Latency (ms): 17.08
  Cache Hit Ratio (%): 73.37
  Connection Count: 137
  Database Name: MetricsDB
  Queries per Second: 3410.89
  Timestamp: '2023-05-13 05:05:25'
- Average Latency (ms): 64.93
  Cache Hit Ratio (%): 83.63
  Connection Count: 69
  Database Name: OrdersDB
  Queries per Second: 3435.78
  Timestamp: '2021-01-17 16:13:48'
- Average Latency (ms): 43.78
  Cache Hit Ratio (%): 95.95
  Connection Count: 285
  Database Name: SalesDB
  Queries per Second: 2275.16
  Timestamp: '2022-07-23 15:34:16'
- Average Latency (ms): 97.09
  Cache Hit Ratio (%): 96.05
  Connection Count: 223
  Database Name: SalesDB
  Queries per Second: 1750.39
  Timestamp: '2023-02-14 18:12:55'
- Average Latency (ms): 17.08
  Cache Hit Ratio (%): 85.3
  Connection Count: 27
  Database Name: InventoryDB
  Queries per Second: 3918.7
  Timestamp: '2022-05-12 00:49:54'
- Average Latency (ms): 42.88
  Cache Hit Ratio (%): 94.09
  Connection Count: 105
  Database Name: UserDB
  Queries per Second: 3918.7
  Timestamp: '2022-01-21 15:22:10'
- Average Latency (ms): 10.85
  Cache Hit Ratio (%): 95.95
  Connection Count: 27
  Database Name: UserDB
  Queries per Second: 610.88
  Timestamp: '2023-03-13 11:00:14'
- Average Latency (ms): 75.08
  Cache Hit Ratio (%): 95.95
  Connection Count: 300
  Database Name: ProductsDB
  Queries per Second: 3001.36
  Timestamp: '2021-10-06 05:43:10'
- Average Latency (ms): 2.37
  Cache Hit Ratio (%): 88.25
  Connection Count: 137
  Database Name: MetricsDB
  Queries per Second: 4754.49
  Timestamp: '2023-11-11 01:27:01'
<end>Please transform the following Yaml data into markdown:
- Cuisine: Mediterranean
  Price Range: $$$
  Restaurant Name: BBQ Barn
- Cuisine: French
  Price Range: $$$$
  Restaurant Name: BBQ Barn
- Cuisine: American
  Price Range: $$$$$
  Restaurant Name: Pasta Palace
- Cuisine: French
  Price Range: $$
  Restaurant Name: The Steakhouse
<start>
| Restaurant Name | Cuisine | Price Range |
| --- | --- | --- |
| BBQ Barn | Mediterranean | $$$ |
| BBQ Barn | French | $$$$ |
| Pasta Palace | American | $$$$$ |
| The Steakhouse | French | $$ |
<end>Convert this yml to markdown:
- Close Price: 750.97
  Company: HealthGen
  Date: '2018-07-22'
  High Price: 750.97
  Low Price: 743.91
  Open Price: 743.91
  Volume: 8005886
- Close Price: 550.04
  Company: HealthGen
  Date: '2021-04-11'
  High Price: 550.04
  Low Price: 46.71
  Open Price: 46.71
  Volume: 2161362
- Close Price: 169.38
  Company: BioLife
  Date: '2022-02-19'
  High Price: 1203.49
  Low Price: 155.73
  Open Price: 750.97
  Volume: 4400583
<start>
| Company | Date | Open Price | Close Price | High Price | Low Price | Volume |
| --- | --- | --- | --- | --- | --- | --- |
| HealthGen | 2018-07-22 | 743.91 | 750.97 | 750.97 | 743.91 | 8005886 |
| HealthGen | 2021-04-11 | 46.71 | 550.04 | 550.04 | 46.71 | 2161362 |
| BioLife | 2022-02-19 | 750.97 | 169.38 | 1203.49 | 155.73 | 4400583 |
<end>Here's some markdown data, can you convert it to json?
| Product Name | Stock Quantity | Category |
| --- | --- | --- |
| Contraption | 45 | Electronics |
| Thingamajig | 118 | Sports |
| Device | 439 | Toys |<start>
[
    {
        "Product Name": "Contraption",
        "Stock Quantity": 45,
        "Category": "Electronics"
    },
    {
        "Product Name": "Thingamajig",
        "Stock Quantity": 118,
        "Category": "Sports"
    },
    {
        "Product Name": "Device",
        "Stock Quantity": 439,
        "Category": "Toys"
    }
]
<end>Transform this YML structure to a JSON format:
- Director: Drake Nightshade
  Genre: Fantasy
  Release Year: 1983
  Title: The Great Expedition
- Director: Mara Moonshadow
  Genre: Drama
  Release Year: 1983
  Title: Starbound Odyssey
- Director: Selene Darkwhisper
  Genre: Comedy
  Release Year: 1971
  Title: Starbound Odyssey
- Director: Aria Ravenwood
  Genre: Sci-Fi
  Release Year: 2011
  Title: Starbound Odyssey
<start>
[
    {
        "Title": "The Great Expedition",
        "Director": "Drake Nightshade",
        "Genre": "Fantasy",
        "Release Year": 1983
    },
    {
        "Title": "Starbound Odyssey",
        "Director": "Mara Moonshadow",
        "Genre": "Drama",
        "Release Year": 1983
    },
    {
        "Title": "Starbound Odyssey",
        "Director": "Selene Darkwhisper",
        "Genre": "Comedy",
        "Release Year": 1971
    },
    {
        "Title": "Starbound Odyssey",
        "Director": "Aria Ravenwood",
        "Genre": "Sci-Fi",
        "Release Year": 2011
    }
]
<end>Can you change this yaml into csv?
- Category: Electronics
  Price: 290.18
  Product Name: Doohickey
  SKU: SKU-1062
  Stock Quantity: 270
  Supplier Name: Umbrella Corp
- Category: Household
  Price: 438.87
  Product Name: Whatchamacallit
  SKU: SKU-1038
  Stock Quantity: 23
  Supplier Name: Wonka Industries
- Category: Electronics
  Price: 253.21
  Product Name: Instrument
  SKU: SKU-1073
  Stock Quantity: 295
  Supplier Name: Wonka Industries
- Category: Electronics
  Price: 272.07
  Product Name: Gadget
  SKU: SKU-1018
  Stock Quantity: 209
  Supplier Name: ACME Corp
- Category: Automotive
  Price: 235.21
  Product Name: Doohickey
  SKU: SKU-1087
  Stock Quantity: 50
  Supplier Name: Wonka Industries
- Category: Sports
  Price: 113.18
  Product Name: Apparatus
  SKU: SKU-1027
  Stock Quantity: 219
  Supplier Name: Wonka Industries
<start>
Product Name,SKU,Price,Stock Quantity,Category,Supplier Name
Doohickey,SKU-1062,290.18,270,Electronics,Umbrella Corp
Whatchamacallit,SKU-1038,438.87,23,Household,Wonka Industries
Instrument,SKU-1073,253.21,295,Electronics,Wonka Industries
Gadget,SKU-1018,272.07,209,Electronics,ACME Corp
Doohickey,SKU-1087,235.21,50,Automotive,Wonka Industries
Apparatus,SKU-1027,113.18,219,Sports,Wonka Industries
<end>Convert this json to plain text:
[
    {
        "Database Name": "UserDB",
        "Queries per Second": 1404.6,
        "Cache Hit Ratio (%)": 81.11,
        "Connection Count": 445,
        "Average Latency (ms)": 1.72,
        "Timestamp": "2022-06-17 17:05:46"
    },
    {
        "Database Name": "ProductsDB",
        "Queries per Second": 1198.89,
        "Cache Hit Ratio (%)": 94.59,
        "Connection Count": 40,
        "Average Latency (ms)": 58.19,
        "Timestamp": "2022-05-16 00:59:16"
    },
    {
        "Database Name": "OrdersDB",
        "Queries per Second": 423.35,
        "Cache Hit Ratio (%)": 90.16,
        "Connection Count": 398,
        "Average Latency (ms)": 5.23,
        "Timestamp": "2023-08-15 17:48:13"
    },
    {
        "Database Name": "InventoryDB",
        "Queries per Second": 2180.98,
        "Cache Hit Ratio (%)": 81.96,
        "Connection Count": 62,
        "Average Latency (ms)": 78.09,
        "Timestamp": "2022-05-26 10:21:31"
    },
    {
        "Database Name": "InventoryDB",
        "Queries per Second": 2870.97,
        "Cache Hit Ratio (%)": 80.17,
        "Connection Count": 76,
        "Average Latency (ms)": 96.5,
        "Timestamp": "2023-02-05 16:15:49"
    },
    {
        "Database Name": "SessionsDB",
        "Queries per Second": 3423.34,
        "Cache Hit Ratio (%)": 98.19,
        "Connection Count": 353,
        "Average Latency (ms)": 56.6,
        "Timestamp": "2021-08-02 17:46:28"
    },
    {
        "Database Name": "SessionsDB",
        "Queries per Second": 3059.02,
        "Cache Hit Ratio (%)": 73.42,
        "Connection Count": 151,
        "Average Latency (ms)": 82.64,
        "Timestamp": "2021-01-15 14:35:49"
    },
    {
        "Database Name": "ProfilesDB",
        "Queries per Second": 875.19,
        "Cache Hit Ratio (%)": 82.32,
        "Connection Count": 173,
        "Average Latency (ms)": 25.14,
        "Timestamp": "2023-02-02 07:57:54"
    },
    {
        "Database Name": "LogsDB",
        "Queries per Second": 608.49,
        "Cache Hit Ratio (%)": 93.44,
        "Connection Count": 445,
        "Average Latency (ms)": 2.98,
        "Timestamp": "2022-02-19 10:13:37"
    }
]<start>
Database Name: UserDB | Queries per Second: 1404.6 | Cache Hit Ratio (%): 81.11 | Connection Count: 445 | Average Latency (ms): 1.72 | Timestamp: 2022-06-17 17:05:46
Database Name: ProductsDB | Queries per Second: 1198.89 | Cache Hit Ratio (%): 94.59 | Connection Count: 40 | Average Latency (ms): 58.19 | Timestamp: 2022-05-16 00:59:16
Database Name: OrdersDB | Queries per Second: 423.35 | Cache Hit Ratio (%): 90.16 | Connection Count: 398 | Average Latency (ms): 5.23 | Timestamp: 2023-08-15 17:48:13
Database Name: InventoryDB | Queries per Second: 2180.98 | Cache Hit Ratio (%): 81.96 | Connection Count: 62 | Average Latency (ms): 78.09 | Timestamp: 2022-05-26 10:21:31
Database Name: InventoryDB | Queries per Second: 2870.97 | Cache Hit Ratio (%): 80.17 | Connection Count: 76 | Average Latency (ms): 96.5 | Timestamp: 2023-02-05 16:15:49
Database Name: SessionsDB | Queries per Second: 3423.34 | Cache Hit Ratio (%): 98.19 | Connection Count: 353 | Average Latency (ms): 56.6 | Timestamp: 2021-08-02 17:46:28
Database Name: SessionsDB | Queries per Second: 3059.02 | Cache Hit Ratio (%): 73.42 | Connection Count: 151 | Average Latency (ms): 82.64 | Timestamp: 2021-01-15 14:35:49
Database Name: ProfilesDB | Queries per Second: 875.19 | Cache Hit Ratio (%): 82.32 | Connection Count: 173 | Average Latency (ms): 25.14 | Timestamp: 2023-02-02 07:57:54
Database Name: LogsDB | Queries per Second: 608.49 | Cache Hit Ratio (%): 93.44 | Connection Count: 445 | Average Latency (ms): 2.98 | Timestamp: 2022-02-19 10:13:37
<end>Convert this Csv to yaml:
Product Name,SKU,Price,Stock Quantity,Category,Supplier Name
Whatchamacallit,SKU-1074,498.62,460,Sports,Wonka Industries
Whatchamacallit,SKU-1044,86.77,291,Toys,Wonka Industries
Gadget,SKU-1032,106.38,462,Automotive,Umbrella Corp
Doohickey,SKU-1078,409.36,397,Sports,Umbrella Corp
Thingamajig,SKU-1032,25.45,124,Sports,Wonka Industries
Apparatus,SKU-1070,499.91,233,Toys,Wonka Industries
Gizmo,SKU-1067,107.39,483,Sports,Umbrella Corp
Gizmo,SKU-1002,217.19,381,Automotive,Globex
<start>
- Category: Sports
  Price: 498.62
  Product Name: Whatchamacallit
  SKU: SKU-1074
  Stock Quantity: 460
  Supplier Name: Wonka Industries
- Category: Toys
  Price: 86.77
  Product Name: Whatchamacallit
  SKU: SKU-1044
  Stock Quantity: 291
  Supplier Name: Wonka Industries
- Category: Automotive
  Price: 106.38
  Product Name: Gadget
  SKU: SKU-1032
  Stock Quantity: 462
  Supplier Name: Umbrella Corp
- Category: Sports
  Price: 409.36
  Product Name: Doohickey
  SKU: SKU-1078
  Stock Quantity: 397
  Supplier Name: Umbrella Corp
- Category: Sports
  Price: 25.45
  Product Name: Thingamajig
  SKU: SKU-1032
  Stock Quantity: 124
  Supplier Name: Wonka Industries
- Category: Toys
  Price: 499.91
  Product Name: Apparatus
  SKU: SKU-1070
  Stock Quantity: 233
  Supplier Name: Wonka Industries
- Category: Sports
  Price: 107.39
  Product Name: Gizmo
  SKU: SKU-1067
  Stock Quantity: 483
  Supplier Name: Umbrella Corp
- Category: Automotive
  Price: 217.19
  Product Name: Gizmo
  SKU: SKU-1002
  Stock Quantity: 381
  Supplier Name: Globex
<end>Transform this JSON structure to a yaml format:
[
    {
        "Stock Price": 881.3,
        "Annual Revenue (B)": 150.94,
        "Quarter": "Q2"
    },
    {
        "Stock Price": 722.73,
        "Annual Revenue (B)": 105.62,
        "Quarter": "Q2"
    },
    {
        "Stock Price": 556.93,
        "Annual Revenue (B)": 126.92,
        "Quarter": "Q1"
    }
]<start>
- Annual Revenue (B): 150.94
  Quarter: Q2
  Stock Price: 881.3
- Annual Revenue (B): 105.62
  Quarter: Q2
  Stock Price: 722.73
- Annual Revenue (B): 126.92
  Quarter: Q1
  Stock Price: 556.93
<end>Here's some csv data, can you convert it to Yaml?
Restaurant Name,Rating
Taco Town,1
BBQ Barn,4
The Golden Spoon,5
Burger Haven,2
Pasta Palace,4
The Golden Spoon,5
Pasta Palace,2
<start>
- Rating: 1
  Restaurant Name: Taco Town
- Rating: 4
  Restaurant Name: BBQ Barn
- Rating: 5
  Restaurant Name: The Golden Spoon
- Rating: 2
  Restaurant Name: Burger Haven
- Rating: 4
  Restaurant Name: Pasta Palace
- Rating: 5
  Restaurant Name: The Golden Spoon
- Rating: 2
  Restaurant Name: Pasta Palace
<end>Here's some markdown data, can you convert it to PLAIN TEXT?
| Restaurant Name | Location | Rating | Price Range |
| --- | --- | --- | --- |
| Curry Corner | Miami | 1 | $$$$$ |
| Sushi World | Miami | 1 | $ |
| Pizza Planet | Chicago | 5 | $$$ |
| Curry Corner | Seattle | 2 | $$$ |
| Sushi World | Seattle | 2 | $$$ |
| Curry Corner | Houston | 4 | $$$$ |
| Burger Haven | New York | 2 | $$ |
| Burger Haven | Los Angeles | 2 | $$$ |<start>
Restaurant Name: Curry Corner | Location: Miami | Rating: 1 | Price Range: $$$$$
Restaurant Name: Sushi World | Location: Miami | Rating: 1 | Price Range: $
Restaurant Name: Pizza Planet | Location: Chicago | Rating: 5 | Price Range: $$$
Restaurant Name: Curry Corner | Location: Seattle | Rating: 2 | Price Range: $$$
Restaurant Name: Sushi World | Location: Seattle | Rating: 2 | Price Range: $$$
Restaurant Name: Curry Corner | Location: Houston | Rating: 4 | Price Range: $$$$
Restaurant Name: Burger Haven | Location: New York | Rating: 2 | Price Range: $$
Restaurant Name: Burger Haven | Location: Los Angeles | Rating: 2 | Price Range: $$$
<end>Here's some markdown data, can you convert it to Yml?
| Title | Author |
| --- | --- |
| Shadows of Solitude | Draven Blackthorn |
| Legends of the Rift | Draven Blackthorn |
| Echoes of Eternity | Luna Silverleaf |
| The Last Sky | Orion Frostblade |
| The Crystal Key | Luna Silverleaf |
| The Silent Grove | Galen Starfire |
| Shadows of Solitude | Orion Frostblade |
| The Last Sky | Orion Frostblade |<start>
- Author: Draven Blackthorn
  Title: Shadows of Solitude
- Author: Draven Blackthorn
  Title: Legends of the Rift
- Author: Luna Silverleaf
  Title: Echoes of Eternity
- Author: Orion Frostblade
  Title: The Last Sky
- Author: Luna Silverleaf
  Title: The Crystal Key
- Author: Galen Starfire
  Title: The Silent Grove
- Author: Orion Frostblade
  Title: Shadows of Solitude
- Author: Orion Frostblade
  Title: The Last Sky
<end>Here's some PLAIN TEXT data, can you convert it to Markdown?
Company: FinanceWorks | Sector: Technology | Stock Price: 94.28 | Annual Revenue (B): 301.26 | Quarter: Q3
Company: Foodies | Sector: Aerospace | Stock Price: 26.27 | Annual Revenue (B): 209.88 | Quarter: Q2
Company: AeroSpace | Sector: Biotech | Stock Price: 29.5 | Annual Revenue (B): 378.56 | Quarter: Q1
Company: Foodies | Sector: Retail | Stock Price: 128.1 | Annual Revenue (B): 351.64 | Quarter: Q1
Company: TechCorp | Sector: Retail | Stock Price: 39.49 | Annual Revenue (B): 142.06 | Quarter: Q2
Company: HealthPlus | Sector: Aerospace | Stock Price: 459.54 | Annual Revenue (B): 419.22 | Quarter: Q2
Company: RetailHub | Sector: Technology | Stock Price: 39.49 | Annual Revenue (B): 142.06 | Quarter: Q3
Company: BioPharm | Sector: Retail | Stock Price: 929.94 | Annual Revenue (B): 213.17 | Quarter: Q4
<start>
| Company | Sector | Stock Price | Annual Revenue (B) | Quarter |
| --- | --- | --- | --- | --- |
| FinanceWorks | Technology | 94.28 | 301.26 | Q3 |
| Foodies | Aerospace | 26.27 | 209.88 | Q2 |
| AeroSpace | Biotech | 29.5 | 378.56 | Q1 |
| Foodies | Retail | 128.1 | 351.64 | Q1 |
| TechCorp | Retail | 39.49 | 142.06 | Q2 |
| HealthPlus | Aerospace | 459.54 | 419.22 | Q2 |
| RetailHub | Technology | 39.49 | 142.06 | Q3 |
| BioPharm | Retail | 929.94 | 213.17 | Q4 |
<end>Convert this yaml to plain text:
- Genre: Sci-Fi
  Release Year: 2001
- Genre: Horror
  Release Year: 2003
- Genre: Comedy
  Release Year: 1973
- Genre: Thriller
  Release Year: 2013
<start>
Genre: Sci-Fi | Release Year: 2001
Genre: Horror | Release Year: 2003
Genre: Comedy | Release Year: 1973
Genre: Thriller | Release Year: 2013
<end>Transform this json structure to a markdown format:
[
    {
        "Trip Name": "Desert Drive",
        "Start Location": "Phoenix",
        "End Location": "Miami",
        "Distance (miles)": 2970.4,
        "Duration (hours)": 31.1,
        "Fuel Used (gallons)": 48.0
    },
    {
        "Trip Name": "Historic Route",
        "Start Location": "San Francisco",
        "End Location": "Phoenix",
        "Distance (miles)": 447.5,
        "Duration (hours)": 61.4,
        "Fuel Used (gallons)": 50.6
    },
    {
        "Trip Name": "Coast to Coast",
        "Start Location": "New York",
        "End Location": "Chicago",
        "Distance (miles)": 1975.7,
        "Duration (hours)": 54.5,
        "Fuel Used (gallons)": 81.0
    },
    {
        "Trip Name": "Coast to Coast",
        "Start Location": "Miami",
        "End Location": "Los Angeles",
        "Distance (miles)": 2191.1,
        "Duration (hours)": 55.4,
        "Fuel Used (gallons)": 57.2
    },
    {
        "Trip Name": "City Explorer",
        "Start Location": "New York",
        "End Location": "Miami",
        "Distance (miles)": 1517.3,
        "Duration (hours)": 28.6,
        "Fuel Used (gallons)": 13.5
    }
]<start>
| Trip Name | Start Location | End Location | Distance (miles) | Duration (hours) | Fuel Used (gallons) |
| --- | --- | --- | --- | --- | --- |
| Desert Drive | Phoenix | Miami | 2970.4 | 31.1 | 48.0 |
| Historic Route | San Francisco | Phoenix | 447.5 | 61.4 | 50.6 |
| Coast to Coast | New York | Chicago | 1975.7 | 54.5 | 81.0 |
| Coast to Coast | Miami | Los Angeles | 2191.1 | 55.4 | 57.2 |
| City Explorer | New York | Miami | 1517.3 | 28.6 | 13.5 |
<end>Can you change this json into csv?
[
    {
        "Location": "Chicago",
        "Condition": "Sunny",
        "Temperature (C)": 39.3,
        "Humidity (%)": 88,
        "Wind Speed (km/h)": 18.7,
        "Day": "Wednesday"
    },
    {
        "Location": "Los Angeles",
        "Condition": "Rainy",
        "Temperature (C)": -0.6,
        "Humidity (%)": 47,
        "Wind Speed (km/h)": 18.7,
        "Day": "Thursday"
    },
    {
        "Location": "Miami",
        "Condition": "Foggy",
        "Temperature (C)": 28.5,
        "Humidity (%)": 93,
        "Wind Speed (km/h)": 14.0,
        "Day": "Sunday"
    },
    {
        "Location": "Los Angeles",
        "Condition": "Windy",
        "Temperature (C)": 16.6,
        "Humidity (%)": 51,
        "Wind Speed (km/h)": 4.6,
        "Day": "Saturday"
    },
    {
        "Location": "Houston",
        "Condition": "Snowy",
        "Temperature (C)": 10.2,
        "Humidity (%)": 75,
        "Wind Speed (km/h)": 20.8,
        "Day": "Wednesday"
    },
    {
        "Location": "Chicago",
        "Condition": "Cloudy",
        "Temperature (C)": -9.7,
        "Humidity (%)": 20,
        "Wind Speed (km/h)": 14.8,
        "Day": "Friday"
    },
    {
        "Location": "Seattle",
        "Condition": "Sunny",
        "Temperature (C)": 39.3,
        "Humidity (%)": 73,
        "Wind Speed (km/h)": 4.3,
        "Day": "Tuesday"
    }
]<start>
Location,Condition,Temperature (C),Humidity (%),Wind Speed (km/h),Day
Chicago,Sunny,39.3,88,18.7,Wednesday
Los Angeles,Rainy,-0.6,47,18.7,Thursday
Miami,Foggy,28.5,93,14.0,Sunday
Los Angeles,Windy,16.6,51,4.6,Saturday
Houston,Snowy,10.2,75,20.8,Wednesday
Chicago,Cloudy,-9.7,20,14.8,Friday
Seattle,Sunny,39.3,73,4.3,Tuesday
<end>Convert this Markdown to plain text:
| Product Name | SKU | Price | Stock Quantity | Category | Supplier Name |
| --- | --- | --- | --- | --- | --- |
| Doohickey | SKU-1084 | 62.69 | 249 | Automotive | Globex |
| Contraption | SKU-1080 | 17.7 | 325 | Electronics | ACME Corp |
| Contraption | SKU-1037 | 42.86 | 429 | Household | Wayne Enterprises |
| Gizmo | SKU-1073 | 378.02 | 305 | Sports | ACME Corp |
| Device | SKU-1031 | 415.33 | 392 | Automotive | Umbrella Corp |
| Device | SKU-1027 | 84.38 | 302 | Household | Umbrella Corp |
| Contraption | SKU-1036 | 412.58 | 118 | Sports | ACME Corp |
| Widget | SKU-1045 | 448.49 | 266 | Toys | Globex |
| Contraption | SKU-1086 | 125.25 | 50 | Toys | Wonka Industries |
| Widget | SKU-1086 | 112.28 | 100 | Household | Wayne Enterprises |<start>
Product Name: Doohickey | SKU: SKU-1084 | Price: 62.69 | Stock Quantity: 249 | Category: Automotive | Supplier Name: Globex
Product Name: Contraption | SKU: SKU-1080 | Price: 17.7 | Stock Quantity: 325 | Category: Electronics | Supplier Name: ACME Corp
Product Name: Contraption | SKU: SKU-1037 | Price: 42.86 | Stock Quantity: 429 | Category: Household | Supplier Name: Wayne Enterprises
Product Name: Gizmo | SKU: SKU-1073 | Price: 378.02 | Stock Quantity: 305 | Category: Sports | Supplier Name: ACME Corp
Product Name: Device | SKU: SKU-1031 | Price: 415.33 | Stock Quantity: 392 | Category: Automotive | Supplier Name: Umbrella Corp
Product Name: Device | SKU: SKU-1027 | Price: 84.38 | Stock Quantity: 302 | Category: Household | Supplier Name: Umbrella Corp
Product Name: Contraption | SKU: SKU-1036 | Price: 412.58 | Stock Quantity: 118 | Category: Sports | Supplier Name: ACME Corp
Product Name: Widget | SKU: SKU-1045 | Price: 448.49 | Stock Quantity: 266 | Category: Toys | Supplier Name: Globex
Product Name: Contraption | SKU: SKU-1086 | Price: 125.25 | Stock Quantity: 50 | Category: Toys | Supplier Name: Wonka Industries
Product Name: Widget | SKU: SKU-1086 | Price: 112.28 | Stock Quantity: 100 | Category: Household | Supplier Name: Wayne Enterprises
<end>Please transform the following YML data into Plain text:
- Annual Revenue (B): 85.96
  Market Cap: Mid Cap
  Quarter: Q2
  Sector: Energy
  Stock Price: 793.26
- Annual Revenue (B): 259.94
  Market Cap: Small Cap
  Quarter: Q3
  Sector: Healthcare
  Stock Price: 483.29
- Annual Revenue (B): 274.16
  Market Cap: Large Cap
  Quarter: Q3
  Sector: Aerospace
  Stock Price: 564.96
- Annual Revenue (B): 240.36
  Market Cap: Large Cap
  Quarter: Q3
  Sector: Aerospace
  Stock Price: 256.57
- Annual Revenue (B): 127.57
  Market Cap: Mid Cap
  Quarter: Q1
  Sector: Automotive
  Stock Price: 90.63
- Annual Revenue (B): 174.93
  Market Cap: Mid Cap
  Quarter: Q3
  Sector: Aerospace
  Stock Price: 520.98
- Annual Revenue (B): 127.57
  Market Cap: Small Cap
  Quarter: Q3
  Sector: Aerospace
  Stock Price: 197.92
- Annual Revenue (B): 76.64
  Market Cap: Large Cap
  Quarter: Q1
  Sector: Technology
  Stock Price: 599.14
<start>
Sector: Energy | Market Cap: Mid Cap | Stock Price: 793.26 | Annual Revenue (B): 85.96 | Quarter: Q2
Sector: Healthcare | Market Cap: Small Cap | Stock Price: 483.29 | Annual Revenue (B): 259.94 | Quarter: Q3
Sector: Aerospace | Market Cap: Large Cap | Stock Price: 564.96 | Annual Revenue (B): 274.16 | Quarter: Q3
Sector: Aerospace | Market Cap: Large Cap | Stock Price: 256.57 | Annual Revenue (B): 240.36 | Quarter: Q3
Sector: Automotive | Market Cap: Mid Cap | Stock Price: 90.63 | Annual Revenue (B): 127.57 | Quarter: Q1
Sector: Aerospace | Market Cap: Mid Cap | Stock Price: 520.98 | Annual Revenue (B): 174.93 | Quarter: Q3
Sector: Aerospace | Market Cap: Small Cap | Stock Price: 197.92 | Annual Revenue (B): 127.57 | Quarter: Q3
Sector: Technology | Market Cap: Large Cap | Stock Price: 599.14 | Annual Revenue (B): 76.64 | Quarter: Q1
<end>Can you change this CSV into Yaml?
Location,Condition,Temperature (C),Humidity (%),Wind Speed (km/h),Day
Miami,Stormy,26.3,99,19.6,Friday
Houston,Snowy,8.2,60,11.7,Wednesday
Los Angeles,Sunny,38.2,73,4.0,Friday
Denver,Snowy,15.9,65,5.6,Saturday
Los Angeles,Snowy,13.5,95,10.9,Saturday
Los Angeles,Rainy,27.6,65,18.0,Thursday
<start>
- Condition: Stormy
  Day: Friday
  Humidity (%): 99
  Location: Miami
  Temperature (C): 26.3
  Wind Speed (km/h): 19.6
- Condition: Snowy
  Day: Wednesday
  Humidity (%): 60
  Location: Houston
  Temperature (C): 8.2
  Wind Speed (km/h): 11.7
- Condition: Sunny
  Day: Friday
  Humidity (%): 73
  Location: Los Angeles
  Temperature (C): 38.2
  Wind Speed (km/h): 4.0
- Condition: Snowy
  Day: Saturday
  Humidity (%): 65
  Location: Denver
  Temperature (C): 15.9
  Wind Speed (km/h): 5.6
- Condition: Snowy
  Day: Saturday
  Humidity (%): 95
  Location: Los Angeles
  Temperature (C): 13.5
  Wind Speed (km/h): 10.9
- Condition: Rainy
  Day: Thursday
  Humidity (%): 65
  Location: Los Angeles
  Temperature (C): 27.6
  Wind Speed (km/h): 18.0
<end>Convert this plain text to yml:
Location: Miami | Condition: Snowy | Temperature (C): 22.2 | Humidity (%): 42 | Wind Speed (km/h): 14.2
Location: New York | Condition: Cloudy | Temperature (C): 2.4 | Humidity (%): 65 | Wind Speed (km/h): 20.8
Location: Seattle | Condition: Foggy | Temperature (C): -9.0 | Humidity (%): 30 | Wind Speed (km/h): 6.4
<start>
- Condition: Snowy
  Humidity (%): 42
  Location: Miami
  Temperature (C): 22.2
  Wind Speed (km/h): 14.2
- Condition: Cloudy
  Humidity (%): 65
  Location: New York
  Temperature (C): 2.4
  Wind Speed (km/h): 20.8
- Condition: Foggy
  Humidity (%): 30
  Location: Seattle
  Temperature (C): -9.0
  Wind Speed (km/h): 6.4
<end>Please transform the following json data into Plain text:
[
    {
        "Location": "Chicago",
        "Temperature (C)": 25.4,
        "Humidity (%)": 55,
        "Wind Speed (km/h)": 23.3,
        "Day": "Friday"
    },
    {
        "Location": "Los Angeles",
        "Temperature (C)": -3.6,
        "Humidity (%)": 32,
        "Wind Speed (km/h)": 5.6,
        "Day": "Wednesday"
    },
    {
        "Location": "Denver",
        "Temperature (C)": 31.9,
        "Humidity (%)": 39,
        "Wind Speed (km/h)": 15.1,
        "Day": "Sunday"
    },
    {
        "Location": "Seattle",
        "Temperature (C)": 28.5,
        "Humidity (%)": 100,
        "Wind Speed (km/h)": 12.5,
        "Day": "Friday"
    },
    {
        "Location": "Phoenix",
        "Temperature (C)": 1.8,
        "Humidity (%)": 72,
        "Wind Speed (km/h)": 13.8,
        "Day": "Monday"
    }
]<start>
Location: Chicago | Temperature (C): 25.4 | Humidity (%): 55 | Wind Speed (km/h): 23.3 | Day: Friday
Location: Los Angeles | Temperature (C): -3.6 | Humidity (%): 32 | Wind Speed (km/h): 5.6 | Day: Wednesday
Location: Denver | Temperature (C): 31.9 | Humidity (%): 39 | Wind Speed (km/h): 15.1 | Day: Sunday
Location: Seattle | Temperature (C): 28.5 | Humidity (%): 100 | Wind Speed (km/h): 12.5 | Day: Friday
Location: Phoenix | Temperature (C): 1.8 | Humidity (%): 72 | Wind Speed (km/h): 13.8 | Day: Monday
<end>Can you change this Json into markdown?
[
    {
        "Product Name": "Widget",
        "SKU": "SKU-1003",
        "Price": 243.08,
        "Stock Quantity": 31,
        "Category": "Electronics"
    },
    {
        "Product Name": "Widget",
        "SKU": "SKU-1072",
        "Price": 465.54,
        "Stock Quantity": 422,
        "Category": "Sports"
    },
    {
        "Product Name": "Device",
        "SKU": "SKU-1064",
        "Price": 349.19,
        "Stock Quantity": 336,
        "Category": "Household"
    },
    {
        "Product Name": "Doohickey",
        "SKU": "SKU-1023",
        "Price": 179.93,
        "Stock Quantity": 267,
        "Category": "Sports"
    }
]<start>
| Product Name | SKU | Price | Stock Quantity | Category |
| --- | --- | --- | --- | --- |
| Widget | SKU-1003 | 243.08 | 31 | Electronics |
| Widget | SKU-1072 | 465.54 | 422 | Sports |
| Device | SKU-1064 | 349.19 | 336 | Household |
| Doohickey | SKU-1023 | 179.93 | 267 | Sports |
<end>Convert this csv to Yml:
SKU,Category,Supplier Name
SKU-1066,Household,Wonka Industries
SKU-1052,Sports,Globex
SKU-1001,Sports,Wayne Enterprises
SKU-1024,Toys,Wayne Enterprises
SKU-1070,Toys,Wayne Enterprises
<start>
- Category: Household
  SKU: SKU-1066
  Supplier Name: Wonka Industries
- Category: Sports
  SKU: SKU-1052
  Supplier Name: Globex
- Category: Sports
  SKU: SKU-1001
  Supplier Name: Wayne Enterprises
- Category: Toys
  SKU: SKU-1024
  Supplier Name: Wayne Enterprises
- Category: Toys
  SKU: SKU-1070
  Supplier Name: Wayne Enterprises
<end>Can you change this Json into plain text?
[
    {
        "Device ID": "device-0014",
        "Device Type": "Temperature Sensor",
        "Location": "Hallway",
        "Reading Value": 84.6,
        "Timestamp": "2023-11-18 11:26:18"
    },
    {
        "Device ID": "device-0024",
        "Device Type": "Pressure Sensor",
        "Location": "Garden",
        "Reading Value": -13.63,
        "Timestamp": "2022-07-13 10:45:33"
    },
    {
        "Device ID": "device-0088",
        "Device Type": "Light Sensor",
        "Location": "Garage",
        "Reading Value": 47.71,
        "Timestamp": "2021-10-11 01:13:24"
    },
    {
        "Device ID": "device-0022",
        "Device Type": "Light Sensor",
        "Location": "Garden",
        "Reading Value": 52.05,
        "Timestamp": "2022-05-18 00:22:56"
    },
    {
        "Device ID": "device-0051",
        "Device Type": "Humidity Sensor",
        "Location": "Bathroom",
        "Reading Value": -27.92,
        "Timestamp": "2021-01-14 11:46:27"
    },
    {
        "Device ID": "device-0040",
        "Device Type": "Pressure Sensor",
        "Location": "Office",
        "Reading Value": 9.32,
        "Timestamp": "2021-11-22 17:39:23"
    },
    {
        "Device ID": "device-0050",
        "Device Type": "Light Sensor",
        "Location": "Kitchen",
        "Reading Value": 61.5,
        "Timestamp": "2021-07-21 11:05:21"
    },
    {
        "Device ID": "device-0027",
        "Device Type": "Humidity Sensor",
        "Location": "Bedroom",
        "Reading Value": 61.61,
        "Timestamp": "2021-12-28 19:07:05"
    },
    {
        "Device ID": "device-0008",
        "Device Type": "Humidity Sensor",
        "Location": "Bedroom",
        "Reading Value": 73.25,
        "Timestamp": "2021-01-08 11:44:07"
    }
]<start>
Device ID: device-0014 | Device Type: Temperature Sensor | Location: Hallway | Reading Value: 84.6 | Timestamp: 2023-11-18 11:26:18
Device ID: device-0024 | Device Type: Pressure Sensor | Location: Garden | Reading Value: -13.63 | Timestamp: 2022-07-13 10:45:33
Device ID: device-0088 | Device Type: Light Sensor | Location: Garage | Reading Value: 47.71 | Timestamp: 2021-10-11 01:13:24
Device ID: device-0022 | Device Type: Light Sensor | Location: Garden | Reading Value: 52.05 | Timestamp: 2022-05-18 00:22:56
Device ID: device-0051 | Device Type: Humidity Sensor | Location: Bathroom | Reading Value: -27.92 | Timestamp: 2021-01-14 11:46:27
Device ID: device-0040 | Device Type: Pressure Sensor | Location: Office | Reading Value: 9.32 | Timestamp: 2021-11-22 17:39:23
Device ID: device-0050 | Device Type: Light Sensor | Location: Kitchen | Reading Value: 61.5 | Timestamp: 2021-07-21 11:05:21
Device ID: device-0027 | Device Type: Humidity Sensor | Location: Bedroom | Reading Value: 61.61 | Timestamp: 2021-12-28 19:07:05
Device ID: device-0008 | Device Type: Humidity Sensor | Location: Bedroom | Reading Value: 73.25 | Timestamp: 2021-01-08 11:44:07
<end>Transform this Plain text structure to a Csv format:
Cache Hit Ratio (%): 78.15 | Connection Count: 153 | Timestamp: 2022-08-02 09:53:53
Cache Hit Ratio (%): 70.01 | Connection Count: 410 | Timestamp: 2022-08-20 05:56:29
Cache Hit Ratio (%): 98.88 | Connection Count: 56 | Timestamp: 2021-08-02 10:38:46
<start>
Cache Hit Ratio (%),Connection Count,Timestamp
78.15,153,2022-08-02 09:53:53
70.01,410,2022-08-20 05:56:29
98.88,56,2021-08-02 10:38:46
<end>Here's some json data, can you convert it to markdown?
[
    {
        "Trip Name": "Lakeside Retreat",
        "Start Location": "New York",
        "End Location": "Houston",
        "Distance (miles)": 2455.1,
        "Duration (hours)": 15.1,
        "Fuel Used (gallons)": 8.9
    },
    {
        "Trip Name": "Valley Voyage",
        "Start Location": "Phoenix",
        "End Location": "San Francisco",
        "Distance (miles)": 1529.4,
        "Duration (hours)": 59.7,
        "Fuel Used (gallons)": 70.4
    },
    {
        "Trip Name": "Highway Odyssey",
        "Start Location": "Chicago",
        "End Location": "Denver",
        "Distance (miles)": 2744.4,
        "Duration (hours)": 54.4,
        "Fuel Used (gallons)": 37.5
    },
    {
        "Trip Name": "Valley Voyage",
        "Start Location": "Houston",
        "End Location": "Chicago",
        "Distance (miles)": 176.4,
        "Duration (hours)": 9.5,
        "Fuel Used (gallons)": 34.7
    },
    {
        "Trip Name": "Canyon Trek",
        "Start Location": "Los Angeles",
        "End Location": "New York",
        "Distance (miles)": 156.4,
        "Duration (hours)": 27.5,
        "Fuel Used (gallons)": 37.5
    }
]<start>
| Trip Name | Start Location | End Location | Distance (miles) | Duration (hours) | Fuel Used (gallons) |
| --- | --- | --- | --- | --- | --- |
| Lakeside Retreat | New York | Houston | 2455.1 | 15.1 | 8.9 |
| Valley Voyage | Phoenix | San Francisco | 1529.4 | 59.7 | 70.4 |
| Highway Odyssey | Chicago | Denver | 2744.4 | 54.4 | 37.5 |
| Valley Voyage | Houston | Chicago | 176.4 | 9.5 | 34.7 |
| Canyon Trek | Los Angeles | New York | 156.4 | 27.5 | 37.5 |
<end>Here's some PLAIN TEXT data, can you convert it to markdown?
Cache Hit Ratio (%): 99.34 | Connection Count: 262 | Timestamp: 2023-07-06 15:47:35
Cache Hit Ratio (%): 79.11 | Connection Count: 282 | Timestamp: 2021-12-14 20:36:03
Cache Hit Ratio (%): 97.2 | Connection Count: 116 | Timestamp: 2021-08-13 08:24:43
<start>
| Cache Hit Ratio (%) | Connection Count | Timestamp |
| --- | --- | --- |
| 99.34 | 262 | 2023-07-06 15:47:35 |
| 79.11 | 282 | 2021-12-14 20:36:03 |
| 97.2 | 116 | 2021-08-13 08:24:43 |
<end>Transform this MARKDOWN structure to a yaml format:
| Trip Name | Distance (miles) | Duration (hours) |
| --- | --- | --- |
| Historic Route | 1873.8 | 68.5 |
| Canyon Trek | 1527.3 | 44.7 |
| Lakeside Retreat | 1663.6 | 21.7 |
| Coast to Coast | 1351.1 | 11.8 |
| Historic Route | 453.9 | 71.8 |
| Coast to Coast | 150.3 | 52.8 |
| Forest Journey | 1951.7 | 19.6 |<start>
- Distance (miles): 1873.8
  Duration (hours): 68.5
  Trip Name: Historic Route
- Distance (miles): 1527.3
  Duration (hours): 44.7
  Trip Name: Canyon Trek
- Distance (miles): 1663.6
  Duration (hours): 21.7
  Trip Name: Lakeside Retreat
- Distance (miles): 1351.1
  Duration (hours): 11.8
  Trip Name: Coast to Coast
- Distance (miles): 453.9
  Duration (hours): 71.8
  Trip Name: Historic Route
- Distance (miles): 150.3
  Duration (hours): 52.8
  Trip Name: Coast to Coast
- Distance (miles): 1951.7
  Duration (hours): 19.6
  Trip Name: Forest Journey
<end>Transform this CSV structure to a json format:
Company,Sector,Market Cap,Stock Price,Annual Revenue (B),Quarter
FinanceWorks,Aerospace,Mega Cap,514.95,158.42,Q1
GlobalTrade,Retail,Mid Cap,871.21,198.63,Q4
RetailHub,Technology,Mega Cap,47.6,255.69,Q4
<start>
[
    {
        "Company": "FinanceWorks",
        "Sector": "Aerospace",
        "Market Cap": "Mega Cap",
        "Stock Price": 514.95,
        "Annual Revenue (B)": 158.42,
        "Quarter": "Q1"
    },
    {
        "Company": "GlobalTrade",
        "Sector": "Retail",
        "Market Cap": "Mid Cap",
        "Stock Price": 871.21,
        "Annual Revenue (B)": 198.63,
        "Quarter": "Q4"
    },
    {
        "Company": "RetailHub",
        "Sector": "Technology",
        "Market Cap": "Mega Cap",
        "Stock Price": 47.6,
        "Annual Revenue (B)": 255.69,
        "Quarter": "Q4"
    }
]
<end>Can you change this plain text into json?
Location: Miami | Wind Speed (km/h): 8.3 | Day: Monday
Location: Seattle | Wind Speed (km/h): 28.0 | Day: Wednesday
Location: Los Angeles | Wind Speed (km/h): 25.4 | Day: Wednesday
Location: Denver | Wind Speed (km/h): 4.1 | Day: Wednesday
<start>
[
    {
        "Location": "Miami",
        "Wind Speed (km/h)": 8.3,
        "Day": "Monday"
    },
    {
        "Location": "Seattle",
        "Wind Speed (km/h)": 28.0,
        "Day": "Wednesday"
    },
    {
        "Location": "Los Angeles",
        "Wind Speed (km/h)": 25.4,
        "Day": "Wednesday"
    },
    {
        "Location": "Denver",
        "Wind Speed (km/h)": 4.1,
        "Day": "Wednesday"
    }
]
<end>Can you change this Markdown into Json?
| Queries per Second | Cache Hit Ratio (%) | Average Latency (ms) | Timestamp |
| --- | --- | --- | --- |
| 1948.68 | 81.4 | 23.36 | 2023-02-01 23:06:07 |
| 1756.65 | 81.4 | 31.77 | 2021-04-18 00:41:33 |
| 3197.71 | 72.53 | 13.12 | 2023-06-01 16:29:48 |
| 720.87 | 94.69 | 9.7 | 2021-07-28 18:55:47 |
| 1457.41 | 92.54 | 62.34 | 2021-06-17 17:38:24 |<start>
[
    {
        "Queries per Second": 1948.68,
        "Cache Hit Ratio (%)": 81.4,
        "Average Latency (ms)": 23.36,
        "Timestamp": "2023-02-01 23:06:07"
    },
    {
        "Queries per Second": 1756.65,
        "Cache Hit Ratio (%)": 81.4,
        "Average Latency (ms)": 31.77,
        "Timestamp": "2021-04-18 00:41:33"
    },
    {
        "Queries per Second": 3197.71,
        "Cache Hit Ratio (%)": 72.53,
        "Average Latency (ms)": 13.12,
        "Timestamp": "2023-06-01 16:29:48"
    },
    {
        "Queries per Second": 720.87,
        "Cache Hit Ratio (%)": 94.69,
        "Average Latency (ms)": 9.7,
        "Timestamp": "2021-07-28 18:55:47"
    },
    {
        "Queries per Second": 1457.41,
        "Cache Hit Ratio (%)": 92.54,
        "Average Latency (ms)": 62.34,
        "Timestamp": "2021-06-17 17:38:24"
    }
]
<end>Can you change this Plain text into markdown?
Director: Mara Moonshadow | Genre: Horror | Release Year: 1988 | Box Office Earnings (M): 960.18
Director: Aria Ravenwood | Genre: Drama | Release Year: 2016 | Box Office Earnings (M): 943.3
Director: Rylan Frostblade | Genre: Fantasy | Release Year: 1979 | Box Office Earnings (M): 960.18
Director: Cade Firebrand | Genre: Action | Release Year: 1977 | Box Office Earnings (M): 850.13
Director: Talon Blackthorn | Genre: Horror | Release Year: 1970 | Box Office Earnings (M): 850.13
<start>
| Director | Genre | Release Year | Box Office Earnings (M) |
| --- | --- | --- | --- |
| Mara Moonshadow | Horror | 1988 | 960.18 |
| Aria Ravenwood | Drama | 2016 | 943.3 |
| Rylan Frostblade | Fantasy | 1979 | 960.18 |
| Cade Firebrand | Action | 1977 | 850.13 |
| Talon Blackthorn | Horror | 1970 | 850.13 |
<end>Please transform the following Json data into Plain text:
[
    {
        "Name": "Clifton",
        "Age": 69,
        "Birth Month": "June",
        "Income": 450000
    },
    {
        "Name": "Edwin",
        "Age": 65,
        "Birth Month": "December",
        "Income": 265000
    },
    {
        "Name": "Micheal",
        "Age": 43,
        "Birth Month": "November",
        "Income": 460000
    },
    {
        "Name": "Adalynn",
        "Age": 58,
        "Birth Month": "April",
        "Income": 150000
    },
    {
        "Name": "Briana",
        "Age": 63,
        "Birth Month": "April",
        "Income": 310000
    },
    {
        "Name": "Archie",
        "Age": 66,
        "Birth Month": "February",
        "Income": 230000
    },
    {
        "Name": "Ryan",
        "Age": 55,
        "Birth Month": "April",
        "Income": 375000
    },
    {
        "Name": "Maude",
        "Age": 59,
        "Birth Month": "December",
        "Income": 175000
    }
]<start>
Name: Clifton | Age: 69 | Birth Month: June | Income: 450000
Name: Edwin | Age: 65 | Birth Month: December | Income: 265000
Name: Micheal | Age: 43 | Birth Month: November | Income: 460000
Name: Adalynn | Age: 58 | Birth Month: April | Income: 150000
Name: Briana | Age: 63 | Birth Month: April | Income: 310000
Name: Archie | Age: 66 | Birth Month: February | Income: 230000
Name: Ryan | Age: 55 | Birth Month: April | Income: 375000
Name: Maude | Age: 59 | Birth Month: December | Income: 175000
<end>Transform this CSV structure to a json format:
Restaurant Name,Location,Rating
Sushi World,Seattle,5
Taco Town,Seattle,1
Pizza Planet,Los Angeles,3
Taco Town,Chicago,1
Vegan Delight,San Francisco,4
Taco Town,Chicago,4
The Steakhouse,Seattle,5
<start>
[
    {
        "Restaurant Name": "Sushi World",
        "Location": "Seattle",
        "Rating": 5
    },
    {
        "Restaurant Name": "Taco Town",
        "Location": "Seattle",
        "Rating": 1
    },
    {
        "Restaurant Name": "Pizza Planet",
        "Location": "Los Angeles",
        "Rating": 3
    },
    {
        "Restaurant Name": "Taco Town",
        "Location": "Chicago",
        "Rating": 1
    },
    {
        "Restaurant Name": "Vegan Delight",
        "Location": "San Francisco",
        "Rating": 4
    },
    {
        "Restaurant Name": "Taco Town",
        "Location": "Chicago",
        "Rating": 4
    },
    {
        "Restaurant Name": "The Steakhouse",
        "Location": "Seattle",
        "Rating": 5
    }
]
<end>Here's some markdown data, can you convert it to plain text?
| Temperature (C) | Humidity (%) | Wind Speed (km/h) |
| --- | --- | --- |
| 24.1 | 22 | 19.5 |
| 32.8 | 35 | 24.8 |
| 22.6 | 28 | 11.0 |
| -5.5 | 24 | 24.6 |
| -4.9 | 35 | 13.5 |
| 12.6 | 58 | 21.9 |
| 5.0 | 31 | 29.8 |
| 32.8 | 45 | 14.3 |
| 30.3 | 29 | 13.6 |
| -2.6 | 77 | 15.0 |<start>
Temperature (C): 24.1 | Humidity (%): 22 | Wind Speed (km/h): 19.5
Temperature (C): 32.8 | Humidity (%): 35 | Wind Speed (km/h): 24.8
Temperature (C): 22.6 | Humidity (%): 28 | Wind Speed (km/h): 11.0
Temperature (C): -5.5 | Humidity (%): 24 | Wind Speed (km/h): 24.6
Temperature (C): -4.9 | Humidity (%): 35 | Wind Speed (km/h): 13.5
Temperature (C): 12.6 | Humidity (%): 58 | Wind Speed (km/h): 21.9
Temperature (C): 5.0 | Humidity (%): 31 | Wind Speed (km/h): 29.8
Temperature (C): 32.8 | Humidity (%): 45 | Wind Speed (km/h): 14.3
Temperature (C): 30.3 | Humidity (%): 29 | Wind Speed (km/h): 13.6
Temperature (C): -2.6 | Humidity (%): 77 | Wind Speed (km/h): 15.0
<end>Please transform the following json data into csv:
[
    {
        "Company": "TechnoCorp",
        "Date": "2020-05-24",
        "Open Price": 1490.42,
        "High Price": 1490.42
    },
    {
        "Company": "BioLife",
        "Date": "2021-12-25",
        "Open Price": 1303.89,
        "High Price": 1303.89
    },
    {
        "Company": "GreenEnergy",
        "Date": "2021-04-23",
        "Open Price": 565.59,
        "High Price": 1128.77
    },
    {
        "Company": "RetailWorld",
        "Date": "2022-11-09",
        "Open Price": 877.38,
        "High Price": 1025.79
    }
]<start>
Company,Date,Open Price,High Price
TechnoCorp,2020-05-24,1490.42,1490.42
BioLife,2021-12-25,1303.89,1303.89
GreenEnergy,2021-04-23,565.59,1128.77
RetailWorld,2022-11-09,877.38,1025.79
<end>Can you change this csv into JSON?
Trip Name,Start Location,End Location,Distance (miles),Duration (hours),Fuel Used (gallons)
City Explorer,San Francisco,New York,1725.9,16.0,85.3
Desert Drive,Los Angeles,Phoenix,2056.0,59.0,78.0
Canyon Trek,Denver,Los Angeles,541.9,31.5,85.0
<start>
[
    {
        "Trip Name": "City Explorer",
        "Start Location": "San Francisco",
        "End Location": "New York",
        "Distance (miles)": 1725.9,
        "Duration (hours)": 16.0,
        "Fuel Used (gallons)": 85.3
    },
    {
        "Trip Name": "Desert Drive",
        "Start Location": "Los Angeles",
        "End Location": "Phoenix",
        "Distance (miles)": 2056.0,
        "Duration (hours)": 59.0,
        "Fuel Used (gallons)": 78.0
    },
    {
        "Trip Name": "Canyon Trek",
        "Start Location": "Denver",
        "End Location": "Los Angeles",
        "Distance (miles)": 541.9,
        "Duration (hours)": 31.5,
        "Fuel Used (gallons)": 85.0
    }
]
<end>Convert this Markdown to Json:
| Restaurant Name | Cuisine | Location | Rating | Price Range |
| --- | --- | --- | --- | --- |
| Sushi World | American | Phoenix | 5 | $$ |
| Vegan Delight | Mexican | Los Angeles | 4 | $$ |
| Sushi World | Italian | Phoenix | 4 | $$$$$ |
| The Steakhouse | French | Phoenix | 4 | $$$$$ |
| Taco Town | Mediterranean | San Francisco | 2 | $$$$ |
| The Steakhouse | Chinese | Los Angeles | 1 | $$$$$ |
| Sushi World | French | Seattle | 4 | $$ |<start>
[
    {
        "Restaurant Name": "Sushi World",
        "Cuisine": "American",
        "Location": "Phoenix",
        "Rating": 5,
        "Price Range": "$$"
    },
    {
        "Restaurant Name": "Vegan Delight",
        "Cuisine": "Mexican",
        "Location": "Los Angeles",
        "Rating": 4,
        "Price Range": "$$"
    },
    {
        "Restaurant Name": "Sushi World",
        "Cuisine": "Italian",
        "Location": "Phoenix",
        "Rating": 4,
        "Price Range": "$$$$$"
    },
    {
        "Restaurant Name": "The Steakhouse",
        "Cuisine": "French",
        "Location": "Phoenix",
        "Rating": 4,
        "Price Range": "$$$$$"
    },
    {
        "Restaurant Name": "Taco Town",
        "Cuisine": "Mediterranean",
        "Location": "San Francisco",
        "Rating": 2,
        "Price Range": "$$$$"
    },
    {
        "Restaurant Name": "The Steakhouse",
        "Cuisine": "Chinese",
        "Location": "Los Angeles",
        "Rating": 1,
        "Price Range": "$$$$$"
    },
    {
        "Restaurant Name": "Sushi World",
        "Cuisine": "French",
        "Location": "Seattle",
        "Rating": 4,
        "Price Range": "$$"
    }
]
<end>Can you change this Yml into MARKDOWN?
- Distance (miles): 2075.7
  End Location: Phoenix
  Fuel Used (gallons): 55.1
  Start Location: San Francisco
  Trip Name: Forest Journey
- Distance (miles): 1453.6
  End Location: Phoenix
  Fuel Used (gallons): 81.3
  Start Location: San Francisco
  Trip Name: Lakeside Retreat
- Distance (miles): 424.0
  End Location: Denver
  Fuel Used (gallons): 64.7
  Start Location: Houston
  Trip Name: Valley Voyage
- Distance (miles): 2500.7
  End Location: New York
  Fuel Used (gallons): 12.6
  Start Location: Los Angeles
  Trip Name: Forest Journey
- Distance (miles): 1199.4
  End Location: Miami
  Fuel Used (gallons): 19.1
  Start Location: San Francisco
  Trip Name: Lakeside Retreat
- Distance (miles): 424.0
  End Location: Los Angeles
  Fuel Used (gallons): 53.8
  Start Location: New York
  Trip Name: Canyon Trek
- Distance (miles): 1851.0
  End Location: Phoenix
  Fuel Used (gallons): 86.5
  Start Location: Denver
  Trip Name: Forest Journey
- Distance (miles): 424.0
  End Location: San Francisco
  Fuel Used (gallons): 81.7
  Start Location: Houston
  Trip Name: Coast to Coast
- Distance (miles): 674.8
  End Location: New York
  Fuel Used (gallons): 15.6
  Start Location: San Francisco
  Trip Name: Lakeside Retreat
- Distance (miles): 1679.1
  End Location: Chicago
  Fuel Used (gallons): 96.0
  Start Location: San Francisco
  Trip Name: Canyon Trek
<start>
| Trip Name | Start Location | End Location | Distance (miles) | Fuel Used (gallons) |
| --- | --- | --- | --- | --- |
| Forest Journey | San Francisco | Phoenix | 2075.7 | 55.1 |
| Lakeside Retreat | San Francisco | Phoenix | 1453.6 | 81.3 |
| Valley Voyage | Houston | Denver | 424.0 | 64.7 |
| Forest Journey | Los Angeles | New York | 2500.7 | 12.6 |
| Lakeside Retreat | San Francisco | Miami | 1199.4 | 19.1 |
| Canyon Trek | New York | Los Angeles | 424.0 | 53.8 |
| Forest Journey | Denver | Phoenix | 1851.0 | 86.5 |
| Coast to Coast | Houston | San Francisco | 424.0 | 81.7 |
| Lakeside Retreat | San Francisco | New York | 674.8 | 15.6 |
| Canyon Trek | San Francisco | Chicago | 1679.1 | 96.0 |
<end>Can you change this MARKDOWN into yaml?
| Queries per Second | Connection Count | Average Latency (ms) | Timestamp |
| --- | --- | --- | --- |
| 2924.62 | 148 | 74.51 | 2021-07-08 05:05:26 |
| 3054.13 | 180 | 14.81 | 2023-09-17 08:10:25 |
| 3184.55 | 408 | 16.09 | 2022-04-04 17:42:22 |
| 111.01 | 60 | 47.12 | 2021-12-06 04:39:22 |
| 512.23 | 281 | 13.19 | 2023-04-07 00:31:39 |
| 589.14 | 40 | 63.54 | 2023-01-15 06:59:52 |
| 2944.69 | 378 | 31.52 | 2023-03-02 21:35:40 |<start>
- Average Latency (ms): 74.51
  Connection Count: 148
  Queries per Second: 2924.62
  Timestamp: '2021-07-08 05:05:26'
- Average Latency (ms): 14.81
  Connection Count: 180
  Queries per Second: 3054.13
  Timestamp: '2023-09-17 08:10:25'
- Average Latency (ms): 16.09
  Connection Count: 408
  Queries per Second: 3184.55
  Timestamp: '2022-04-04 17:42:22'
- Average Latency (ms): 47.12
  Connection Count: 60
  Queries per Second: 111.01
  Timestamp: '2021-12-06 04:39:22'
- Average Latency (ms): 13.19
  Connection Count: 281
  Queries per Second: 512.23
  Timestamp: '2023-04-07 00:31:39'
- Average Latency (ms): 63.54
  Connection Count: 40
  Queries per Second: 589.14
  Timestamp: '2023-01-15 06:59:52'
- Average Latency (ms): 31.52
  Connection Count: 378
  Queries per Second: 2944.69
  Timestamp: '2023-03-02 21:35:40'
<end>Please transform the following Yml data into plain text:
- Battery Level (%): 41.8
  Device Type: Light Sensor
  Location: Garden
  Timestamp: '2022-03-18 20:44:54'
- Battery Level (%): 79.5
  Device Type: Temperature Sensor
  Location: Garage
  Timestamp: '2022-07-15 06:50:16'
- Battery Level (%): 12.0
  Device Type: Temperature Sensor
  Location: Office
  Timestamp: '2022-10-07 12:26:00'
- Battery Level (%): 18.0
  Device Type: Humidity Sensor
  Location: Hallway
  Timestamp: '2021-01-12 12:29:04'
- Battery Level (%): 31.9
  Device Type: Temperature Sensor
  Location: Office
  Timestamp: '2023-08-04 10:00:47'
- Battery Level (%): 89.0
  Device Type: Motion Detector
  Location: Garden
  Timestamp: '2022-04-15 22:04:16'
- Battery Level (%): 77.7
  Device Type: Pressure Sensor
  Location: Bedroom
  Timestamp: '2021-02-16 12:09:13'
- Battery Level (%): 74.6
  Device Type: Light Sensor
  Location: Office
  Timestamp: '2022-09-21 15:05:05'
- Battery Level (%): 89.6
  Device Type: Motion Detector
  Location: Living Room
  Timestamp: '2022-11-10 09:25:57'
<start>
Device Type: Light Sensor | Location: Garden | Battery Level (%): 41.8 | Timestamp: 2022-03-18 20:44:54
Device Type: Temperature Sensor | Location: Garage | Battery Level (%): 79.5 | Timestamp: 2022-07-15 06:50:16
Device Type: Temperature Sensor | Location: Office | Battery Level (%): 12.0 | Timestamp: 2022-10-07 12:26:00
Device Type: Humidity Sensor | Location: Hallway | Battery Level (%): 18.0 | Timestamp: 2021-01-12 12:29:04
Device Type: Temperature Sensor | Location: Office | Battery Level (%): 31.9 | Timestamp: 2023-08-04 10:00:47
Device Type: Motion Detector | Location: Garden | Battery Level (%): 89.0 | Timestamp: 2022-04-15 22:04:16
Device Type: Pressure Sensor | Location: Bedroom | Battery Level (%): 77.7 | Timestamp: 2021-02-16 12:09:13
Device Type: Light Sensor | Location: Office | Battery Level (%): 74.6 | Timestamp: 2022-09-21 15:05:05
Device Type: Motion Detector | Location: Living Room | Battery Level (%): 89.6 | Timestamp: 2022-11-10 09:25:57
<end>Here's some plain text data, can you convert it to JSON?
Name: Kaden | Age: 53 | Birth Month: December | City: Phoenix | Income: 470000
Name: Kinsley | Age: 47 | Birth Month: January | City: San Diego | Income: 25000
Name: Vernon | Age: 52 | Birth Month: September | City: San Francisco | Income: 145000
Name: Kristopher | Age: 64 | Birth Month: February | City: San Antonio | Income: 115000
Name: Quinn | Age: 29 | Birth Month: April | City: Phoenix | Income: 20000
Name: Miguel | Age: 62 | Birth Month: June | City: Portland | Income: 330000
Name: Rosalie | Age: 55 | Birth Month: December | City: Louisville | Income: 140000
<start>
[
    {
        "Name": "Kaden",
        "Age": 53,
        "Birth Month": "December",
        "City": "Phoenix",
        "Income": 470000
    },
    {
        "Name": "Kinsley",
        "Age": 47,
        "Birth Month": "January",
        "City": "San Diego",
        "Income": 25000
    },
    {
        "Name": "Vernon",
        "Age": 52,
        "Birth Month": "September",
        "City": "San Francisco",
        "Income": 145000
    },
    {
        "Name": "Kristopher",
        "Age": 64,
        "Birth Month": "February",
        "City": "San Antonio",
        "Income": 115000
    },
    {
        "Name": "Quinn",
        "Age": 29,
        "Birth Month": "April",
        "City": "Phoenix",
        "Income": 20000
    },
    {
        "Name": "Miguel",
        "Age": 62,
        "Birth Month": "June",
        "City": "Portland",
        "Income": 330000
    },
    {
        "Name": "Rosalie",
        "Age": 55,
        "Birth Month": "December",
        "City": "Louisville",
        "Income": 140000
    }
]
<end>Transform this CSV structure to a PLAIN TEXT format:
Title,Director,Genre,Release Year,Box Office Earnings (M)
Dreamwalker,Aria Ravenwood,Horror,1976,306.63
The Final Voyage,Cade Firebrand,Adventure,1973,314.54
Dreamwalker,Cade Firebrand,Sci-Fi,1987,391.47
The Great Expedition,Zara Stormrider,Adventure,2008,314.54
The Final Voyage,Lira Silverleaf,Fantasy,2005,534.82
The Endless Horizon,Selene Darkwhisper,Drama,1978,682.43
Starbound Odyssey,Aria Ravenwood,Action,1985,293.53
<start>
Title: Dreamwalker | Director: Aria Ravenwood | Genre: Horror | Release Year: 1976 | Box Office Earnings (M): 306.63
Title: The Final Voyage | Director: Cade Firebrand | Genre: Adventure | Release Year: 1973 | Box Office Earnings (M): 314.54
Title: Dreamwalker | Director: Cade Firebrand | Genre: Sci-Fi | Release Year: 1987 | Box Office Earnings (M): 391.47
Title: The Great Expedition | Director: Zara Stormrider | Genre: Adventure | Release Year: 2008 | Box Office Earnings (M): 314.54
Title: The Final Voyage | Director: Lira Silverleaf | Genre: Fantasy | Release Year: 2005 | Box Office Earnings (M): 534.82
Title: The Endless Horizon | Director: Selene Darkwhisper | Genre: Drama | Release Year: 1978 | Box Office Earnings (M): 682.43
Title: Starbound Odyssey | Director: Aria Ravenwood | Genre: Action | Release Year: 1985 | Box Office Earnings (M): 293.53
<end>Convert this YML to csv:
- Battery Level (%): 90.6
  Reading Value: -19.04
  Timestamp: '2023-12-11 19:29:34'
- Battery Level (%): 69.2
  Reading Value: 54.59
  Timestamp: '2022-07-18 04:14:51'
- Battery Level (%): 68.8
  Reading Value: 81.93
  Timestamp: '2023-02-13 19:44:35'
<start>
Battery Level (%),Reading Value,Timestamp
90.6,-19.04,2023-12-11 19:29:34
69.2,54.59,2022-07-18 04:14:51
68.8,81.93,2023-02-13 19:44:35
<end>Can you change this CSV into markdown?
Restaurant Name,Cuisine,Location,Rating,Price Range
Taco Town,French,Houston,4,$
Sushi World,Japanese,Los Angeles,2,$
Burger Haven,Mexican,Chicago,5,$
Pasta Palace,Chinese,Los Angeles,5,$$$$
Pizza Planet,American,Houston,2,$$$$$
<start>
| Restaurant Name | Cuisine | Location | Rating | Price Range |
| --- | --- | --- | --- | --- |
| Taco Town | French | Houston | 4 | $ |
| Sushi World | Japanese | Los Angeles | 2 | $ |
| Burger Haven | Mexican | Chicago | 5 | $ |
| Pasta Palace | Chinese | Los Angeles | 5 | $$$$ |
| Pizza Planet | American | Houston | 2 | $$$$$ |
<end>Transform this CSV structure to a plain text format:
Title,Author,Publication Year,Rating
A Journey Through Time,Thorne Ironwood,1976,2.2
The Silent Grove,Isla Windrider,1982,4.1
The Last Sky,Orion Frostblade,1976,2.8
Whispers of the Abyss,Thorne Ironwood,2000,1.7
The Silent Grove,Kara Firebrand,1985,3.9
<start>
Title: A Journey Through Time | Author: Thorne Ironwood | Publication Year: 1976 | Rating: 2.2
Title: The Silent Grove | Author: Isla Windrider | Publication Year: 1982 | Rating: 4.1
Title: The Last Sky | Author: Orion Frostblade | Publication Year: 1976 | Rating: 2.8
Title: Whispers of the Abyss | Author: Thorne Ironwood | Publication Year: 2000 | Rating: 1.7
Title: The Silent Grove | Author: Kara Firebrand | Publication Year: 1985 | Rating: 3.9
<end>Convert this Csv to JSON:
Director,Release Year
Aria Ravenwood,1974
Zara Stormrider,1973
Orin Shadowalker,1990
Orin Shadowalker,1975
Rylan Frostblade,1974
Lira Silverleaf,2001
Cade Firebrand,1983
Selene Darkwhisper,1997
Talon Blackthorn,2016
Lira Silverleaf,2007
<start>
[
    {
        "Director": "Aria Ravenwood",
        "Release Year": 1974
    },
    {
        "Director": "Zara Stormrider",
        "Release Year": 1973
    },
    {
        "Director": "Orin Shadowalker",
        "Release Year": 1990
    },
    {
        "Director": "Orin Shadowalker",
        "Release Year": 1975
    },
    {
        "Director": "Rylan Frostblade",
        "Release Year": 1974
    },
    {
        "Director": "Lira Silverleaf",
        "Release Year": 2001
    },
    {
        "Director": "Cade Firebrand",
        "Release Year": 1983
    },
    {
        "Director": "Selene Darkwhisper",
        "Release Year": 1997
    },
    {
        "Director": "Talon Blackthorn",
        "Release Year": 2016
    },
    {
        "Director": "Lira Silverleaf",
        "Release Year": 2007
    }
]
<end>Here's some PLAIN TEXT data, can you convert it to markdown?
Queries per Second: 2697.14 | Cache Hit Ratio (%): 77.43 | Average Latency (ms): 30.56 | Timestamp: 2021-07-10 11:25:54
Queries per Second: 171.88 | Cache Hit Ratio (%): 78.66 | Average Latency (ms): 21.67 | Timestamp: 2022-09-26 15:51:50
Queries per Second: 968.15 | Cache Hit Ratio (%): 95.62 | Average Latency (ms): 31.17 | Timestamp: 2023-04-05 04:22:11
<start>
| Queries per Second | Cache Hit Ratio (%) | Average Latency (ms) | Timestamp |
| --- | --- | --- | --- |
| 2697.14 | 77.43 | 30.56 | 2021-07-10 11:25:54 |
| 171.88 | 78.66 | 21.67 | 2022-09-26 15:51:50 |
| 968.15 | 95.62 | 31.17 | 2023-04-05 04:22:11 |
<end>Please transform the following Yaml data into PLAIN TEXT:
- Author: Thorne Ironwood
  Genre: Science Fiction
  Publication Year: 1958
  Title: A Journey Through Time
- Author: Thorne Ironwood
  Genre: Thriller
  Publication Year: 2009
  Title: The Last Sky
- Author: Thorne Ironwood
  Genre: Romance
  Publication Year: 2017
  Title: The Forgotten World
<start>
Title: A Journey Through Time | Author: Thorne Ironwood | Genre: Science Fiction | Publication Year: 1958
Title: The Last Sky | Author: Thorne Ironwood | Genre: Thriller | Publication Year: 2009
Title: The Forgotten World | Author: Thorne Ironwood | Genre: Romance | Publication Year: 2017
<end>Convert this csv to Yml:
Name,Age,Birth Month,City,Income
Travis,28,August,Denver,345000
Leah,34,June,Denver,25000
Miranda,35,November,Indianapolis,295000
Tami,61,June,Portland,115000
Karl,60,September,San Antonio,420000
Charlotte,35,March,New York,330000
Katrina,59,February,San Jose,175000
<start>
- Age: 28
  Birth Month: August
  City: Denver
  Income: 345000
  Name: Travis
- Age: 34
  Birth Month: June
  City: Denver
  Income: 25000
  Name: Leah
- Age: 35
  Birth Month: November
  City: Indianapolis
  Income: 295000
  Name: Miranda
- Age: 61
  Birth Month: June
  City: Portland
  Income: 115000
  Name: Tami
- Age: 60
  Birth Month: September
  City: San Antonio
  Income: 420000
  Name: Karl
- Age: 35
  Birth Month: March
  City: New York
  Income: 330000
  Name: Charlotte
- Age: 59
  Birth Month: February
  City: San Jose
  Income: 175000
  Name: Katrina
<end>Please transform the following Plain text data into json:
Genre: Drama | Release Year: 1994
Genre: Sci-Fi | Release Year: 2005
Genre: Drama | Release Year: 1981
Genre: Drama | Release Year: 1985
Genre: Horror | Release Year: 1999
Genre: Sci-Fi | Release Year: 1994
Genre: Sci-Fi | Release Year: 1978
Genre: Horror | Release Year: 1982
<start>
[
    {
        "Genre": "Drama",
        "Release Year": 1994
    },
    {
        "Genre": "Sci-Fi",
        "Release Year": 2005
    },
    {
        "Genre": "Drama",
        "Release Year": 1981
    },
    {
        "Genre": "Drama",
        "Release Year": 1985
    },
    {
        "Genre": "Horror",
        "Release Year": 1999
    },
    {
        "Genre": "Sci-Fi",
        "Release Year": 1994
    },
    {
        "Genre": "Sci-Fi",
        "Release Year": 1978
    },
    {
        "Genre": "Horror",
        "Release Year": 1982
    }
]
<end>Transform this yml structure to a plain text format:
- Location: Living Room
  Reading Value: 7.2
  Timestamp: '2021-12-22 05:01:46'
- Location: Kitchen
  Reading Value: 38.64
  Timestamp: '2022-01-05 12:31:55'
- Location: Kitchen
  Reading Value: -25.36
  Timestamp: '2021-02-09 19:29:16'
- Location: Living Room
  Reading Value: 42.1
  Timestamp: '2023-05-12 23:51:51'
- Location: Hallway
  Reading Value: 66.84
  Timestamp: '2021-07-26 16:37:43'
- Location: Garden
  Reading Value: 67.38
  Timestamp: '2021-08-05 00:53:15'
<start>
Location: Living Room | Reading Value: 7.2 | Timestamp: 2021-12-22 05:01:46
Location: Kitchen | Reading Value: 38.64 | Timestamp: 2022-01-05 12:31:55
Location: Kitchen | Reading Value: -25.36 | Timestamp: 2021-02-09 19:29:16
Location: Living Room | Reading Value: 42.1 | Timestamp: 2023-05-12 23:51:51
Location: Hallway | Reading Value: 66.84 | Timestamp: 2021-07-26 16:37:43
Location: Garden | Reading Value: 67.38 | Timestamp: 2021-08-05 00:53:15
<end>Transform this Plain text structure to a yaml format:
Device ID: device-0034 | Device Type: Light Sensor | Location: Bathroom | Battery Level (%): 68.2 | Timestamp: 2021-06-08 06:27:20
Device ID: device-0027 | Device Type: Motion Detector | Location: Bathroom | Battery Level (%): 27.6 | Timestamp: 2021-04-03 18:38:32
Device ID: device-0008 | Device Type: Humidity Sensor | Location: Hallway | Battery Level (%): 34.0 | Timestamp: 2023-04-15 21:17:38
Device ID: device-0004 | Device Type: Light Sensor | Location: Bathroom | Battery Level (%): 45.5 | Timestamp: 2022-12-08 13:37:20
<start>
- Battery Level (%): 68.2
  Device ID: device-0034
  Device Type: Light Sensor
  Location: Bathroom
  Timestamp: '2021-06-08 06:27:20'
- Battery Level (%): 27.6
  Device ID: device-0027
  Device Type: Motion Detector
  Location: Bathroom
  Timestamp: '2021-04-03 18:38:32'
- Battery Level (%): 34.0
  Device ID: device-0008
  Device Type: Humidity Sensor
  Location: Hallway
  Timestamp: '2023-04-15 21:17:38'
- Battery Level (%): 45.5
  Device ID: device-0004
  Device Type: Light Sensor
  Location: Bathroom
  Timestamp: '2022-12-08 13:37:20'
<end>Please transform the following PLAIN TEXT data into YAML:
Restaurant Name: Vegan Delight | Cuisine: Mediterranean | Location: Houston | Rating: 3 | Price Range: $$$$$
Restaurant Name: BBQ Barn | Cuisine: French | Location: San Francisco | Rating: 4 | Price Range: $$$$
Restaurant Name: Pizza Planet | Cuisine: Mediterranean | Location: Miami | Rating: 1 | Price Range: $$$$$
Restaurant Name: BBQ Barn | Cuisine: Mediterranean | Location: Phoenix | Rating: 4 | Price Range: $$$
Restaurant Name: Curry Corner | Cuisine: French | Location: Phoenix | Rating: 2 | Price Range: $$$$$
Restaurant Name: The Golden Spoon | Cuisine: Italian | Location: San Francisco | Rating: 4 | Price Range: $$$$
Restaurant Name: Curry Corner | Cuisine: Japanese | Location: New York | Rating: 5 | Price Range: $$$$
Restaurant Name: Curry Corner | Cuisine: Indian | Location: Phoenix | Rating: 3 | Price Range: $$$$$
<start>
- Cuisine: Mediterranean
  Location: Houston
  Price Range: $$$$$
  Rating: 3
  Restaurant Name: Vegan Delight
- Cuisine: French
  Location: San Francisco
  Price Range: $$$$
  Rating: 4
  Restaurant Name: BBQ Barn
- Cuisine: Mediterranean
  Location: Miami
  Price Range: $$$$$
  Rating: 1
  Restaurant Name: Pizza Planet
- Cuisine: Mediterranean
  Location: Phoenix
  Price Range: $$$
  Rating: 4
  Restaurant Name: BBQ Barn
- Cuisine: French
  Location: Phoenix
  Price Range: $$$$$
  Rating: 2
  Restaurant Name: Curry Corner
- Cuisine: Italian
  Location: San Francisco
  Price Range: $$$$
  Rating: 4
  Restaurant Name: The Golden Spoon
- Cuisine: Japanese
  Location: New York
  Price Range: $$$$
  Rating: 5
  Restaurant Name: Curry Corner
- Cuisine: Indian
  Location: Phoenix
  Price Range: $$$$$
  Rating: 3
  Restaurant Name: Curry Corner
<end>Here's some yml data, can you convert it to json?
- Battery Level (%): 18.8
  Device Type: Motion Detector
  Location: Living Room
  Reading Value: 31.68
  Timestamp: '2022-01-26 10:20:47'
- Battery Level (%): 25.7
  Device Type: Light Sensor
  Location: Bathroom
  Reading Value: 68.12
  Timestamp: '2022-09-06 23:50:21'
- Battery Level (%): 22.8
  Device Type: Pressure Sensor
  Location: Hallway
  Reading Value: 22.06
  Timestamp: '2022-05-02 20:22:03'
- Battery Level (%): 60.2
  Device Type: Humidity Sensor
  Location: Bathroom
  Reading Value: -15.36
  Timestamp: '2022-06-25 01:12:33'
<start>
[
    {
        "Device Type": "Motion Detector",
        "Location": "Living Room",
        "Battery Level (%)": 18.8,
        "Reading Value": 31.68,
        "Timestamp": "2022-01-26 10:20:47"
    },
    {
        "Device Type": "Light Sensor",
        "Location": "Bathroom",
        "Battery Level (%)": 25.7,
        "Reading Value": 68.12,
        "Timestamp": "2022-09-06 23:50:21"
    },
    {
        "Device Type": "Pressure Sensor",
        "Location": "Hallway",
        "Battery Level (%)": 22.8,
        "Reading Value": 22.06,
        "Timestamp": "2022-05-02 20:22:03"
    },
    {
        "Device Type": "Humidity Sensor",
        "Location": "Bathroom",
        "Battery Level (%)": 60.2,
        "Reading Value": -15.36,
        "Timestamp": "2022-06-25 01:12:33"
    }
]
<end>Convert this Yaml to csv:
- Annual Revenue (B): 255.54
  Company: RetailHub
  Market Cap: Mega Cap
  Quarter: Q3
  Sector: Healthcare
  Stock Price: 850.95
- Annual Revenue (B): 474.04
  Company: AeroSpace
  Market Cap: Mega Cap
  Quarter: Q2
  Sector: Aerospace
  Stock Price: 757.98
- Annual Revenue (B): 117.48
  Company: HealthPlus
  Market Cap: Mega Cap
  Quarter: Q1
  Sector: Finance
  Stock Price: 143.87
- Annual Revenue (B): 154.08
  Company: BioPharm
  Market Cap: Mid Cap
  Quarter: Q2
  Sector: Energy
  Stock Price: 349.47
- Annual Revenue (B): 351.64
  Company: Foodies
  Market Cap: Mid Cap
  Quarter: Q2
  Sector: Healthcare
  Stock Price: 655.84
- Annual Revenue (B): 262.08
  Company: TechCorp
  Market Cap: Mid Cap
  Quarter: Q3
  Sector: Technology
  Stock Price: 367.73
- Annual Revenue (B): 371.46
  Company: BioPharm
  Market Cap: Small Cap
  Quarter: Q2
  Sector: Retail
  Stock Price: 367.73
- Annual Revenue (B): 340.83
  Company: AutoDrive
  Market Cap: Large Cap
  Quarter: Q3
  Sector: Aerospace
  Stock Price: 569.07
- Annual Revenue (B): 121.25
  Company: AutoDrive
  Market Cap: Small Cap
  Quarter: Q1
  Sector: Technology
  Stock Price: 596.71
<start>
Company,Sector,Market Cap,Stock Price,Annual Revenue (B),Quarter
RetailHub,Healthcare,Mega Cap,850.95,255.54,Q3
AeroSpace,Aerospace,Mega Cap,757.98,474.04,Q2
HealthPlus,Finance,Mega Cap,143.87,117.48,Q1
BioPharm,Energy,Mid Cap,349.47,154.08,Q2
Foodies,Healthcare,Mid Cap,655.84,351.64,Q2
TechCorp,Technology,Mid Cap,367.73,262.08,Q3
BioPharm,Retail,Small Cap,367.73,371.46,Q2
AutoDrive,Aerospace,Large Cap,569.07,340.83,Q3
AutoDrive,Technology,Small Cap,596.71,121.25,Q1
<end>Convert this CSV to markdown:
Location,Condition,Temperature (C),Humidity (%),Wind Speed (km/h),Day
Phoenix,Rainy,18.6,43,17.4,Tuesday
Los Angeles,Foggy,0.6,61,22.7,Tuesday
Chicago,Foggy,3.4,46,20.4,Thursday
Los Angeles,Cloudy,31.4,27,14.0,Friday
Chicago,Rainy,39.9,94,17.4,Sunday
<start>
| Location | Condition | Temperature (C) | Humidity (%) | Wind Speed (km/h) | Day |
| --- | --- | --- | --- | --- | --- |
| Phoenix | Rainy | 18.6 | 43 | 17.4 | Tuesday |
| Los Angeles | Foggy | 0.6 | 61 | 22.7 | Tuesday |
| Chicago | Foggy | 3.4 | 46 | 20.4 | Thursday |
| Los Angeles | Cloudy | 31.4 | 27 | 14.0 | Friday |
| Chicago | Rainy | 39.9 | 94 | 17.4 | Sunday |
<end>Here's some csv data, can you convert it to json?
Restaurant Name,Cuisine,Rating
The Steakhouse,Japanese,5
The Steakhouse,Indian,5
The Steakhouse,American,4
The Steakhouse,Chinese,1
<start>
[
    {
        "Restaurant Name": "The Steakhouse",
        "Cuisine": "Japanese",
        "Rating": 5
    },
    {
        "Restaurant Name": "The Steakhouse",
        "Cuisine": "Indian",
        "Rating": 5
    },
    {
        "Restaurant Name": "The Steakhouse",
        "Cuisine": "American",
        "Rating": 4
    },
    {
        "Restaurant Name": "The Steakhouse",
        "Cuisine": "Chinese",
        "Rating": 1
    }
]
<end>Can you change this Yaml into json?
- Average Latency (ms): 68.56
  Cache Hit Ratio (%): 91.31
  Connection Count: 272
  Queries per Second: 288.92
  Timestamp: '2021-07-01 10:07:45'
- Average Latency (ms): 78.51
  Cache Hit Ratio (%): 79.05
  Connection Count: 351
  Queries per Second: 1625.28
  Timestamp: '2023-03-09 00:48:19'
- Average Latency (ms): 91.23
  Cache Hit Ratio (%): 73.13
  Connection Count: 91
  Queries per Second: 3048.14
  Timestamp: '2023-08-08 01:29:22'
- Average Latency (ms): 9.39
  Cache Hit Ratio (%): 98.56
  Connection Count: 354
  Queries per Second: 1239.11
  Timestamp: '2023-06-26 09:21:13'
- Average Latency (ms): 9.69
  Cache Hit Ratio (%): 99.11
  Connection Count: 134
  Queries per Second: 4160.5
  Timestamp: '2021-05-17 06:05:10'
- Average Latency (ms): 20.74
  Cache Hit Ratio (%): 81.41
  Connection Count: 335
  Queries per Second: 4218.48
  Timestamp: '2023-12-19 06:03:27'
- Average Latency (ms): 8.33
  Cache Hit Ratio (%): 96.17
  Connection Count: 78
  Queries per Second: 865.21
  Timestamp: '2022-11-25 12:44:25'
- Average Latency (ms): 20.74
  Cache Hit Ratio (%): 78.53
  Connection Count: 138
  Queries per Second: 1074.95
  Timestamp: '2021-10-05 16:45:32'
- Average Latency (ms): 47.16
  Cache Hit Ratio (%): 95.76
  Connection Count: 352
  Queries per Second: 3679.31
  Timestamp: '2021-04-14 18:52:11'
<start>
[
    {
        "Queries per Second": 288.92,
        "Cache Hit Ratio (%)": 91.31,
        "Connection Count": 272,
        "Average Latency (ms)": 68.56,
        "Timestamp": "2021-07-01 10:07:45"
    },
    {
        "Queries per Second": 1625.28,
        "Cache Hit Ratio (%)": 79.05,
        "Connection Count": 351,
        "Average Latency (ms)": 78.51,
        "Timestamp": "2023-03-09 00:48:19"
    },
    {
        "Queries per Second": 3048.14,
        "Cache Hit Ratio (%)": 73.13,
        "Connection Count": 91,
        "Average Latency (ms)": 91.23,
        "Timestamp": "2023-08-08 01:29:22"
    },
    {
        "Queries per Second": 1239.11,
        "Cache Hit Ratio (%)": 98.56,
        "Connection Count": 354,
        "Average Latency (ms)": 9.39,
        "Timestamp": "2023-06-26 09:21:13"
    },
    {
        "Queries per Second": 4160.5,
        "Cache Hit Ratio (%)": 99.11,
        "Connection Count": 134,
        "Average Latency (ms)": 9.69,
        "Timestamp": "2021-05-17 06:05:10"
    },
    {
        "Queries per Second": 4218.48,
        "Cache Hit Ratio (%)": 81.41,
        "Connection Count": 335,
        "Average Latency (ms)": 20.74,
        "Timestamp": "2023-12-19 06:03:27"
    },
    {
        "Queries per Second": 865.21,
        "Cache Hit Ratio (%)": 96.17,
        "Connection Count": 78,
        "Average Latency (ms)": 8.33,
        "Timestamp": "2022-11-25 12:44:25"
    },
    {
        "Queries per Second": 1074.95,
        "Cache Hit Ratio (%)": 78.53,
        "Connection Count": 138,
        "Average Latency (ms)": 20.74,
        "Timestamp": "2021-10-05 16:45:32"
    },
    {
        "Queries per Second": 3679.31,
        "Cache Hit Ratio (%)": 95.76,
        "Connection Count": 352,
        "Average Latency (ms)": 47.16,
        "Timestamp": "2021-04-14 18:52:11"
    }
]
<end>Transform this YAML structure to a json format:
- Box Office Earnings (M): 783.41
  Director: Selene Darkwhisper
- Box Office Earnings (M): 340.32
  Director: Rylan Frostblade
- Box Office Earnings (M): 296.59
  Director: Drake Nightshade
- Box Office Earnings (M): 986.78
  Director: Selene Darkwhisper
<start>
[
    {
        "Director": "Selene Darkwhisper",
        "Box Office Earnings (M)": 783.41
    },
    {
        "Director": "Rylan Frostblade",
        "Box Office Earnings (M)": 340.32
    },
    {
        "Director": "Drake Nightshade",
        "Box Office Earnings (M)": 296.59
    },
    {
        "Director": "Selene Darkwhisper",
        "Box Office Earnings (M)": 986.78
    }
]
<end>Transform this yml structure to a MARKDOWN format:
- Battery Level (%): 45.6
  Device ID: device-0065
  Device Type: Pressure Sensor
  Location: Bedroom
  Reading Value: 47.03
  Timestamp: '2023-12-22 19:46:33'
- Battery Level (%): 61.5
  Device ID: device-0100
  Device Type: Light Sensor
  Location: Office
  Reading Value: -31.11
  Timestamp: '2023-06-03 10:56:40'
- Battery Level (%): 31.7
  Device ID: device-0076
  Device Type: Temperature Sensor
  Location: Garden
  Reading Value: 49.92
  Timestamp: '2021-12-21 12:39:44'
- Battery Level (%): 56.8
  Device ID: device-0029
  Device Type: Temperature Sensor
  Location: Bathroom
  Reading Value: 7.08
  Timestamp: '2023-01-23 21:20:15'
<start>
| Device ID | Device Type | Location | Battery Level (%) | Reading Value | Timestamp |
| --- | --- | --- | --- | --- | --- |
| device-0065 | Pressure Sensor | Bedroom | 45.6 | 47.03 | 2023-12-22 19:46:33 |
| device-0100 | Light Sensor | Office | 61.5 | -31.11 | 2023-06-03 10:56:40 |
| device-0076 | Temperature Sensor | Garden | 31.7 | 49.92 | 2021-12-21 12:39:44 |
| device-0029 | Temperature Sensor | Bathroom | 56.8 | 7.08 | 2023-01-23 21:20:15 |
<end>Convert this Csv to markdown:
Location,Condition,Temperature (C),Humidity (%),Wind Speed (km/h)
Denver,Snowy,36.7,99,2.0
Miami,Cloudy,-3.8,48,1.1
Denver,Cloudy,32.5,81,8.9
Miami,Snowy,2.6,78,22.3
Phoenix,Cloudy,6.2,81,23.3
New York,Windy,16.3,21,28.6
Phoenix,Cloudy,-6.6,30,21.3
<start>
| Location | Condition | Temperature (C) | Humidity (%) | Wind Speed (km/h) |
| --- | --- | --- | --- | --- |
| Denver | Snowy | 36.7 | 99 | 2.0 |
| Miami | Cloudy | -3.8 | 48 | 1.1 |
| Denver | Cloudy | 32.5 | 81 | 8.9 |
| Miami | Snowy | 2.6 | 78 | 22.3 |
| Phoenix | Cloudy | 6.2 | 81 | 23.3 |
| New York | Windy | 16.3 | 21 | 28.6 |
| Phoenix | Cloudy | -6.6 | 30 | 21.3 |
<end>Here's some YAML data, can you convert it to Json?
- Box Office Earnings (M): 815.64
  Director: Aria Ravenwood
  Genre: Thriller
  Release Year: 2014
  Title: The Endless Horizon
- Box Office Earnings (M): 878.8
  Director: Rylan Frostblade
  Genre: Comedy
  Release Year: 1978
  Title: The Endless Horizon
- Box Office Earnings (M): 311.95
  Director: Selene Darkwhisper
  Genre: Adventure
  Release Year: 2008
  Title: Beyond the Veil
- Box Office Earnings (M): 212.49
  Director: Rylan Frostblade
  Genre: Adventure
  Release Year: 1976
  Title: Beyond the Veil
<start>
[
    {
        "Title": "The Endless Horizon",
        "Director": "Aria Ravenwood",
        "Genre": "Thriller",
        "Release Year": 2014,
        "Box Office Earnings (M)": 815.64
    },
    {
        "Title": "The Endless Horizon",
        "Director": "Rylan Frostblade",
        "Genre": "Comedy",
        "Release Year": 1978,
        "Box Office Earnings (M)": 878.8
    },
    {
        "Title": "Beyond the Veil",
        "Director": "Selene Darkwhisper",
        "Genre": "Adventure",
        "Release Year": 2008,
        "Box Office Earnings (M)": 311.95
    },
    {
        "Title": "Beyond the Veil",
        "Director": "Rylan Frostblade",
        "Genre": "Adventure",
        "Release Year": 1976,
        "Box Office Earnings (M)": 212.49
    }
]
<end>Convert this csv to PLAIN TEXT:
Title,Release Year,Box Office Earnings (M)
The Final Voyage,2007,516.34
Mystery of the Depths,1970,716.93
Edge of Infinity,2001,384.03
Dreamwalker,2011,743.06
Mystery of the Depths,1990,443.26
The Great Expedition,2011,987.87
Dreamwalker,1985,576.93
Rise of the Titans,1973,303.15
Mystery of the Depths,2020,574.92
<start>
Title: The Final Voyage | Release Year: 2007 | Box Office Earnings (M): 516.34
Title: Mystery of the Depths | Release Year: 1970 | Box Office Earnings (M): 716.93
Title: Edge of Infinity | Release Year: 2001 | Box Office Earnings (M): 384.03
Title: Dreamwalker | Release Year: 2011 | Box Office Earnings (M): 743.06
Title: Mystery of the Depths | Release Year: 1990 | Box Office Earnings (M): 443.26
Title: The Great Expedition | Release Year: 2011 | Box Office Earnings (M): 987.87
Title: Dreamwalker | Release Year: 1985 | Box Office Earnings (M): 576.93
Title: Rise of the Titans | Release Year: 1973 | Box Office Earnings (M): 303.15
Title: Mystery of the Depths | Release Year: 2020 | Box Office Earnings (M): 574.92
<end>Convert this Markdown to plain text:
| Company | Date | Open Price | Close Price | High Price | Low Price | Volume |
| --- | --- | --- | --- | --- | --- | --- |
| BioLife | 2013-08-05 | 881.23 | 880.86 | 1115.66 | 824.18 | 3337156 |
| BioLife | 2013-09-03 | 542.65 | 341.32 | 702.59 | 131.79 | 406141 |
| FinanceTrust | 2020-08-06 | 152.58 | 911.1 | 1383.63 | 152.58 | 459741 |
| FoodChain | 2013-02-21 | 824.18 | 266.89 | 824.18 | 266.89 | 9144043 |
| FinanceTrust | 2021-03-02 | 883.83 | 763.98 | 883.83 | 763.98 | 4671775 |
| FinanceTrust | 2016-06-17 | 346.26 | 1048.5 | 1048.5 | 346.26 | 4671775 |
| FinanceTrust | 2011-03-13 | 131.79 | 813.6 | 813.6 | 131.79 | 5746156 |<start>
Company: BioLife | Date: 2013-08-05 | Open Price: 881.23 | Close Price: 880.86 | High Price: 1115.66 | Low Price: 824.18 | Volume: 3337156
Company: BioLife | Date: 2013-09-03 | Open Price: 542.65 | Close Price: 341.32 | High Price: 702.59 | Low Price: 131.79 | Volume: 406141
Company: FinanceTrust | Date: 2020-08-06 | Open Price: 152.58 | Close Price: 911.1 | High Price: 1383.63 | Low Price: 152.58 | Volume: 459741
Company: FoodChain | Date: 2013-02-21 | Open Price: 824.18 | Close Price: 266.89 | High Price: 824.18 | Low Price: 266.89 | Volume: 9144043
Company: FinanceTrust | Date: 2021-03-02 | Open Price: 883.83 | Close Price: 763.98 | High Price: 883.83 | Low Price: 763.98 | Volume: 4671775
Company: FinanceTrust | Date: 2016-06-17 | Open Price: 346.26 | Close Price: 1048.5 | High Price: 1048.5 | Low Price: 346.26 | Volume: 4671775
Company: FinanceTrust | Date: 2011-03-13 | Open Price: 131.79 | Close Price: 813.6 | High Price: 813.6 | Low Price: 131.79 | Volume: 5746156
<end>Here's some json data, can you convert it to Markdown?
[
    {
        "Restaurant Name": "Sushi World",
        "Cuisine": "French",
        "Location": "Phoenix",
        "Rating": 2,
        "Price Range": "$$$"
    },
    {
        "Restaurant Name": "Vegan Delight",
        "Cuisine": "Japanese",
        "Location": "Miami",
        "Rating": 4,
        "Price Range": "$$"
    },
    {
        "Restaurant Name": "Curry Corner",
        "Cuisine": "French",
        "Location": "Seattle",
        "Rating": 4,
        "Price Range": "$$"
    }
]<start>
| Restaurant Name | Cuisine | Location | Rating | Price Range |
| --- | --- | --- | --- | --- |
| Sushi World | French | Phoenix | 2 | $$$ |
| Vegan Delight | Japanese | Miami | 4 | $$ |
| Curry Corner | French | Seattle | 4 | $$ |
<end>Transform this Json structure to a yml format:
[
    {
        "Name": "Vanessa",
        "Age": 49,
        "City": "Memphis",
        "Income": 425000
    },
    {
        "Name": "Makenzie",
        "Age": 50,
        "City": "Dallas",
        "Income": 85000
    },
    {
        "Name": "Juanita",
        "Age": 36,
        "City": "San Antonio",
        "Income": 445000
    },
    {
        "Name": "Edmund",
        "Age": 40,
        "City": "Las Vegas",
        "Income": 485000
    },
    {
        "Name": "Jodi",
        "Age": 37,
        "City": "Baltimore",
        "Income": 110000
    },
    {
        "Name": "Nicholas",
        "Age": 46,
        "City": "Nashville",
        "Income": 275000
    },
    {
        "Name": "Natalia",
        "Age": 19,
        "City": "Washington",
        "Income": 495000
    },
    {
        "Name": "Mathilda",
        "Age": 52,
        "City": "Milwaukee",
        "Income": 355000
    }
]<start>
- Age: 49
  City: Memphis
  Income: 425000
  Name: Vanessa
- Age: 50
  City: Dallas
  Income: 85000
  Name: Makenzie
- Age: 36
  City: San Antonio
  Income: 445000
  Name: Juanita
- Age: 40
  City: Las Vegas
  Income: 485000
  Name: Edmund
- Age: 37
  City: Baltimore
  Income: 110000
  Name: Jodi
- Age: 46
  City: Nashville
  Income: 275000
  Name: Nicholas
- Age: 19
  City: Washington
  Income: 495000
  Name: Natalia
- Age: 52
  City: Milwaukee
  Income: 355000
  Name: Mathilda
<end>Convert this json to csv:
[
    {
        "Company": "AutoDrive",
        "Sector": "Aerospace",
        "Market Cap": "Small Cap",
        "Stock Price": 729.13,
        "Annual Revenue (B)": 391.8,
        "Quarter": "Q1"
    },
    {
        "Company": "HealthPlus",
        "Sector": "Retail",
        "Market Cap": "Mega Cap",
        "Stock Price": 750.28,
        "Annual Revenue (B)": 336.12,
        "Quarter": "Q2"
    },
    {
        "Company": "Foodies",
        "Sector": "Technology",
        "Market Cap": "Mega Cap",
        "Stock Price": 614.67,
        "Annual Revenue (B)": 258.63,
        "Quarter": "Q1"
    },
    {
        "Company": "BioPharm",
        "Sector": "Finance",
        "Market Cap": "Mid Cap",
        "Stock Price": 190.09,
        "Annual Revenue (B)": 470.21,
        "Quarter": "Q3"
    },
    {
        "Company": "Foodies",
        "Sector": "Retail",
        "Market Cap": "Large Cap",
        "Stock Price": 775.42,
        "Annual Revenue (B)": 61.72,
        "Quarter": "Q3"
    },
    {
        "Company": "Foodies",
        "Sector": "Automotive",
        "Market Cap": "Large Cap",
        "Stock Price": 987.22,
        "Annual Revenue (B)": 245.65,
        "Quarter": "Q1"
    },
    {
        "Company": "TechCorp",
        "Sector": "Aerospace",
        "Market Cap": "Large Cap",
        "Stock Price": 614.67,
        "Annual Revenue (B)": 318.7,
        "Quarter": "Q4"
    },
    {
        "Company": "RetailHub",
        "Sector": "Energy",
        "Market Cap": "Small Cap",
        "Stock Price": 795.91,
        "Annual Revenue (B)": 104.71,
        "Quarter": "Q4"
    },
    {
        "Company": "AeroSpace",
        "Sector": "Energy",
        "Market Cap": "Mega Cap",
        "Stock Price": 316.26,
        "Annual Revenue (B)": 323.2,
        "Quarter": "Q2"
    }
]<start>
Company,Sector,Market Cap,Stock Price,Annual Revenue (B),Quarter
AutoDrive,Aerospace,Small Cap,729.13,391.8,Q1
HealthPlus,Retail,Mega Cap,750.28,336.12,Q2
Foodies,Technology,Mega Cap,614.67,258.63,Q1
BioPharm,Finance,Mid Cap,190.09,470.21,Q3
Foodies,Retail,Large Cap,775.42,61.72,Q3
Foodies,Automotive,Large Cap,987.22,245.65,Q1
TechCorp,Aerospace,Large Cap,614.67,318.7,Q4
RetailHub,Energy,Small Cap,795.91,104.71,Q4
AeroSpace,Energy,Mega Cap,316.26,323.2,Q2
<end>Here's some Markdown data, can you convert it to CSV?
| Product Name | SKU | Price | Stock Quantity | Category | Supplier Name |
| --- | --- | --- | --- | --- | --- |
| Instrument | SKU-1067 | 310.45 | 440 | Sports | Wayne Enterprises |
| Contraption | SKU-1055 | 194.73 | 194 | Automotive | Wayne Enterprises |
| Device | SKU-1007 | 249.42 | 394 | Sports | Globex |
| Doohickey | SKU-1014 | 460.87 | 285 | Electronics | Wonka Industries |
| Apparatus | SKU-1073 | 31.56 | 191 | Electronics | Globex |
| Apparatus | SKU-1060 | 453.25 | 116 | Electronics | ACME Corp |
| Device | SKU-1085 | 470.63 | 370 | Electronics | Wonka Industries |
| Instrument | SKU-1057 | 232.85 | 314 | Toys | Wonka Industries |<start>
Product Name,SKU,Price,Stock Quantity,Category,Supplier Name
Instrument,SKU-1067,310.45,440,Sports,Wayne Enterprises
Contraption,SKU-1055,194.73,194,Automotive,Wayne Enterprises
Device,SKU-1007,249.42,394,Sports,Globex
Doohickey,SKU-1014,460.87,285,Electronics,Wonka Industries
Apparatus,SKU-1073,31.56,191,Electronics,Globex
Apparatus,SKU-1060,453.25,116,Electronics,ACME Corp
Device,SKU-1085,470.63,370,Electronics,Wonka Industries
Instrument,SKU-1057,232.85,314,Toys,Wonka Industries
<end>Here's some json data, can you convert it to Csv?
[
    {
        "Title": "Dreamwalker",
        "Director": "Selene Darkwhisper",
        "Genre": "Fantasy",
        "Release Year": 1995,
        "Box Office Earnings (M)": 425.18
    },
    {
        "Title": "Starbound Odyssey",
        "Director": "Selene Darkwhisper",
        "Genre": "Drama",
        "Release Year": 2005,
        "Box Office Earnings (M)": 405.49
    },
    {
        "Title": "The Final Voyage",
        "Director": "Zara Stormrider",
        "Genre": "Fantasy",
        "Release Year": 2017,
        "Box Office Earnings (M)": 300.29
    },
    {
        "Title": "The Great Expedition",
        "Director": "Mara Moonshadow",
        "Genre": "Thriller",
        "Release Year": 1988,
        "Box Office Earnings (M)": 106.51
    }
]<start>
Title,Director,Genre,Release Year,Box Office Earnings (M)
Dreamwalker,Selene Darkwhisper,Fantasy,1995,425.18
Starbound Odyssey,Selene Darkwhisper,Drama,2005,405.49
The Final Voyage,Zara Stormrider,Fantasy,2017,300.29
The Great Expedition,Mara Moonshadow,Thriller,1988,106.51
<end>Convert this yaml to markdown:
- Average Latency (ms): 10.75
  Cache Hit Ratio (%): 85.96
  Connection Count: 114
  Database Name: AnalyticsDB
  Queries per Second: 4792.25
  Timestamp: '2022-03-14 01:12:01'
- Average Latency (ms): 8.61
  Cache Hit Ratio (%): 97.78
  Connection Count: 471
  Database Name: InventoryDB
  Queries per Second: 2974.71
  Timestamp: '2023-01-22 11:25:32'
- Average Latency (ms): 42.34
  Cache Hit Ratio (%): 80.56
  Connection Count: 448
  Database Name: LogsDB
  Queries per Second: 574.06
  Timestamp: '2022-03-23 12:03:31'
<start>
| Database Name | Queries per Second | Cache Hit Ratio (%) | Connection Count | Average Latency (ms) | Timestamp |
| --- | --- | --- | --- | --- | --- |
| AnalyticsDB | 4792.25 | 85.96 | 114 | 10.75 | 2022-03-14 01:12:01 |
| InventoryDB | 2974.71 | 97.78 | 471 | 8.61 | 2023-01-22 11:25:32 |
| LogsDB | 574.06 | 80.56 | 448 | 42.34 | 2022-03-23 12:03:31 |
<end>Transform this Plain text structure to a json format:
Name: Gertrude | Age: 19 | Birth Month: July | City: Chicago | Income: 155000
Name: Caitlin | Age: 43 | Birth Month: September | City: Baltimore | Income: 270000
Name: Luke | Age: 41 | Birth Month: March | City: Boston | Income: 305000
Name: Fred | Age: 30 | Birth Month: December | City: Milwaukee | Income: 120000
Name: Sonia | Age: 63 | Birth Month: November | City: Columbus | Income: 35000
Name: Kayden | Age: 51 | Birth Month: July | City: San Francisco | Income: 140000
<start>
[
    {
        "Name": "Gertrude",
        "Age": 19,
        "Birth Month": "July",
        "City": "Chicago",
        "Income": 155000
    },
    {
        "Name": "Caitlin",
        "Age": 43,
        "Birth Month": "September",
        "City": "Baltimore",
        "Income": 270000
    },
    {
        "Name": "Luke",
        "Age": 41,
        "Birth Month": "March",
        "City": "Boston",
        "Income": 305000
    },
    {
        "Name": "Fred",
        "Age": 30,
        "Birth Month": "December",
        "City": "Milwaukee",
        "Income": 120000
    },
    {
        "Name": "Sonia",
        "Age": 63,
        "Birth Month": "November",
        "City": "Columbus",
        "Income": 35000
    },
    {
        "Name": "Kayden",
        "Age": 51,
        "Birth Month": "July",
        "City": "San Francisco",
        "Income": 140000
    }
]
<end>Can you change this PLAIN TEXT into MARKDOWN?
Product Name: Apparatus | Price: 28.03 | Stock Quantity: 440
Product Name: Contraption | Price: 319.84 | Stock Quantity: 460
Product Name: Instrument | Price: 84.52 | Stock Quantity: 422
Product Name: Contraption | Price: 233.22 | Stock Quantity: 339
Product Name: Apparatus | Price: 262.57 | Stock Quantity: 484
Product Name: Whatchamacallit | Price: 247.73 | Stock Quantity: 39
Product Name: Gizmo | Price: 357.87 | Stock Quantity: 172
Product Name: Device | Price: 472.07 | Stock Quantity: 152
<start>
| Product Name | Price | Stock Quantity |
| --- | --- | --- |
| Apparatus | 28.03 | 440 |
| Contraption | 319.84 | 460 |
| Instrument | 84.52 | 422 |
| Contraption | 233.22 | 339 |
| Apparatus | 262.57 | 484 |
| Whatchamacallit | 247.73 | 39 |
| Gizmo | 357.87 | 172 |
| Device | 472.07 | 152 |
<end>Convert this markdown to YAML:
| Cuisine | Rating |
| --- | --- |
| Italian | 4 |
| American | 4 |
| Japanese | 4 |<start>
- Cuisine: Italian
  Rating: 4
- Cuisine: American
  Rating: 4
- Cuisine: Japanese
  Rating: 4
<end>Convert this markdown to Csv:
| Database Name | Queries per Second | Cache Hit Ratio (%) | Connection Count | Average Latency (ms) | Timestamp |
| --- | --- | --- | --- | --- | --- |
| SalesDB | 1784.29 | 90.03 | 99 | 70.03 | 2021-05-28 11:45:10 |
| ProductsDB | 3048.61 | 78.59 | 225 | 68.54 | 2021-09-25 01:22:17 |
| UserDB | 434.45 | 88.75 | 121 | 66.94 | 2022-08-04 04:34:15 |
| MetricsDB | 4354.32 | 79.46 | 20 | 1.73 | 2021-12-07 20:13:35 |
| AnalyticsDB | 1231.72 | 72.98 | 468 | 21.81 | 2023-04-03 03:26:43 |<start>
Database Name,Queries per Second,Cache Hit Ratio (%),Connection Count,Average Latency (ms),Timestamp
SalesDB,1784.29,90.03,99,70.03,2021-05-28 11:45:10
ProductsDB,3048.61,78.59,225,68.54,2021-09-25 01:22:17
UserDB,434.45,88.75,121,66.94,2022-08-04 04:34:15
MetricsDB,4354.32,79.46,20,1.73,2021-12-07 20:13:35
AnalyticsDB,1231.72,72.98,468,21.81,2023-04-03 03:26:43
<end>Can you change this plain text into markdown?
Trip Name: Lakeside Retreat | Start Location: Denver | End Location: Los Angeles | Distance (miles): 777.8 | Duration (hours): 18.6 | Fuel Used (gallons): 71.9
Trip Name: Canyon Trek | Start Location: Miami | End Location: Los Angeles | Distance (miles): 996.7 | Duration (hours): 58.0 | Fuel Used (gallons): 87.0
Trip Name: Historic Route | Start Location: Houston | End Location: Los Angeles | Distance (miles): 2551.5 | Duration (hours): 67.1 | Fuel Used (gallons): 62.7
Trip Name: Lakeside Retreat | Start Location: San Francisco | End Location: Los Angeles | Distance (miles): 2028.9 | Duration (hours): 9.2 | Fuel Used (gallons): 77.1
Trip Name: Lakeside Retreat | Start Location: New York | End Location: Chicago | Distance (miles): 2983.5 | Duration (hours): 44.1 | Fuel Used (gallons): 66.7
Trip Name: Mountain Adventure | Start Location: New York | End Location: Los Angeles | Distance (miles): 784.9 | Duration (hours): 70.7 | Fuel Used (gallons): 28.7
<start>
| Trip Name | Start Location | End Location | Distance (miles) | Duration (hours) | Fuel Used (gallons) |
| --- | --- | --- | --- | --- | --- |
| Lakeside Retreat | Denver | Los Angeles | 777.8 | 18.6 | 71.9 |
| Canyon Trek | Miami | Los Angeles | 996.7 | 58.0 | 87.0 |
| Historic Route | Houston | Los Angeles | 2551.5 | 67.1 | 62.7 |
| Lakeside Retreat | San Francisco | Los Angeles | 2028.9 | 9.2 | 77.1 |
| Lakeside Retreat | New York | Chicago | 2983.5 | 44.1 | 66.7 |
| Mountain Adventure | New York | Los Angeles | 784.9 | 70.7 | 28.7 |
<end>Here's some Markdown data, can you convert it to yaml?
| Database Name | Queries per Second | Cache Hit Ratio (%) | Connection Count |
| --- | --- | --- | --- |
| InventoryDB | 2768.42 | 71.3 | 326 |
| SessionsDB | 939.73 | 95.29 | 350 |
| InventoryDB | 480.01 | 75.52 | 36 |<start>
- Cache Hit Ratio (%): 71.3
  Connection Count: 326
  Database Name: InventoryDB
  Queries per Second: 2768.42
- Cache Hit Ratio (%): 95.29
  Connection Count: 350
  Database Name: SessionsDB
  Queries per Second: 939.73
- Cache Hit Ratio (%): 75.52
  Connection Count: 36
  Database Name: InventoryDB
  Queries per Second: 480.01
<end>Can you change this plain text into CSV?
Company: GlobalTrade | Market Cap: Small Cap | Stock Price: 666.38 | Annual Revenue (B): 209.97
Company: EcoEnergy | Market Cap: Mega Cap | Stock Price: 375.82 | Annual Revenue (B): 486.42
Company: EcoEnergy | Market Cap: Small Cap | Stock Price: 413.75 | Annual Revenue (B): 153.12
Company: AutoDrive | Market Cap: Mid Cap | Stock Price: 212.96 | Annual Revenue (B): 70.58
<start>
Company,Market Cap,Stock Price,Annual Revenue (B)
GlobalTrade,Small Cap,666.38,209.97
EcoEnergy,Mega Cap,375.82,486.42
EcoEnergy,Small Cap,413.75,153.12
AutoDrive,Mid Cap,212.96,70.58
<end>Transform this Markdown structure to a YML format:
| Cache Hit Ratio (%) | Connection Count | Timestamp |
| --- | --- | --- |
| 72.78 | 193 | 2023-08-03 15:33:07 |
| 79.17 | 275 | 2022-09-25 13:41:08 |
| 95.73 | 476 | 2023-01-15 02:44:45 |
| 79.83 | 343 | 2023-09-09 08:57:41 |
| 87.34 | 73 | 2023-09-19 17:16:18 |
| 86.66 | 446 | 2021-12-20 03:53:47 |<start>
- Cache Hit Ratio (%): 72.78
  Connection Count: 193
  Timestamp: '2023-08-03 15:33:07'
- Cache Hit Ratio (%): 79.17
  Connection Count: 275
  Timestamp: '2022-09-25 13:41:08'
- Cache Hit Ratio (%): 95.73
  Connection Count: 476
  Timestamp: '2023-01-15 02:44:45'
- Cache Hit Ratio (%): 79.83
  Connection Count: 343
  Timestamp: '2023-09-09 08:57:41'
- Cache Hit Ratio (%): 87.34
  Connection Count: 73
  Timestamp: '2023-09-19 17:16:18'
- Cache Hit Ratio (%): 86.66
  Connection Count: 446
  Timestamp: '2021-12-20 03:53:47'
<end>