Transform this Yml structure to a Markdown format:
- Box Office Earnings (M): 739.42
  Director: Drake Nightshade
  Genre: Drama
  Release Year: 2001
  Title: Beyond the Veil
- Box Office Earnings (M): 796.85
  Director: Rylan Frostblade
  Genre: Horror
  Release Year: 2012
  Title: Beyond the Veil
- Box Office Earnings (M): 756.06
  Director: Orin Shadowalker
  Genre: Fantasy
  Release Year: 1980
  Title: Beyond the Veil
- Box Office Earnings (M): 346.16
  Director: Drake Nightshade
  Genre: Horror
  Release Year: 1988
  Title: Rise of the Titans
- Box Office Earnings (M): 999.52
  Director: Drake Nightshade
  Genre: Drama
  Release Year: 2006
  Title: Beyond the Veil
<start>
| Title | Director | Genre | Release Year | Box Office Earnings (M) |
| --- | --- | --- | --- | --- |
| Beyond the Veil | Drake Nightshade | Drama | 2001 | 739.42 |
| Beyond the Veil | Rylan Frostblade | Horror | 2012 | 796.85 |
| Beyond the Veil | Orin Shadowalker | Fantasy | 1980 | 756.06 |
| Rise of the Titans | Drake Nightshade | Horror | 1988 | 346.16 |
| Beyond the Veil | Drake Nightshade | Drama | 2006 | 999.52 |
<end>Convert this Plain text to CSV:
Author: Rowan Ashborne | Publication Year: 1994
Author: Sylvia Nightshade | Publication Year: 1965
Author: Kara Firebrand | Publication Year: 1953
Author: Kara Firebrand | Publication Year: 1965
Author: Isla Windrider | Publication Year: 1975
Author: Orion Frostblade | Publication Year: 1972
Author: Rowan Ashborne | Publication Year: 1982
Author: Elara Moonshadow | Publication Year: 1958
Author: Sylvia Nightshade | Publication Year: 1960
Author: Galen Starfire | Publication Year: 2005
<start>
Author,Publication Year
Rowan Ashborne,1994
Sylvia Nightshade,1965
Kara Firebrand,1953
Kara Firebrand,1965
Isla Windrider,1975
Orion Frostblade,1972
Rowan Ashborne,1982
Elara Moonshadow,1958
Sylvia Nightshade,1960
Galen Starfire,2005
<end>Here's some Markdown data, can you convert it to JSON?
| Database Name | Queries per Second | Cache Hit Ratio (%) | Connection Count | Timestamp |
| --- | --- | --- | --- | --- |
| LogsDB | 2392.05 | 99.48 | 371 | 2021-08-10 05:11:44 |
| OrdersDB | 3033.17 | 91.52 | 448 | 2021-04-06 04:29:02 |
| LogsDB | 1170.45 | 71.87 | 448 | 2021-02-27 20:36:44 |
| ProductsDB | 1170.45 | 74.9 | 280 | 2021-08-09 05:07:52 |
| OrdersDB | 3751.97 | 81.57 | 409 | 2023-05-04 05:42:43 |
| InventoryDB | 2793.75 | 99.48 | 400 | 2023-02-10 04:28:58 |
| AnalyticsDB | 3755.49 | 78.14 | 374 | 2022-01-21 15:23:23 |
| InventoryDB | 723.14 | 80.82 | 215 | 2022-06-04 18:35:02 |
| ProfilesDB | 2597.56 | 74.99 | 287 | 2022-09-16 11:51:32 |<start>
[
    {
        "Database Name": "LogsDB",
        "Queries per Second": 2392.05,
        "Cache Hit Ratio (%)": 99.48,
        "Connection Count": 371,
        "Timestamp": "2021-08-10 05:11:44"
    },
    {
        "Database Name": "OrdersDB",
        "Queries per Second": 3033.17,
        "Cache Hit Ratio (%)": 91.52,
        "Connection Count": 448,
        "Timestamp": "2021-04-06 04:29:02"
    },
    {
        "Database Name": "LogsDB",
        "Queries per Second": 1170.45,
        "Cache Hit Ratio (%)": 71.87,
        "Connection Count": 448,
        "Timestamp": "2021-02-27 20:36:44"
    },
    {
        "Database Name": "ProductsDB",
        "Queries per Second": 1170.45,
        "Cache Hit Ratio (%)": 74.9,
        "Connection Count": 280,
        "Timestamp": "2021-08-09 05:07:52"
    },
    {
        "Database Name": "OrdersDB",
        "Queries per Second": 3751.97,
        "Cache Hit Ratio (%)": 81.57,
        "Connection Count": 409,
        "Timestamp": "2023-05-04 05:42:43"
    },
    {
        "Database Name": "InventoryDB",
        "Queries per Second": 2793.75,
        "Cache Hit Ratio (%)": 99.48,
        "Connection Count": 400,
        "Timestamp": "2023-02-10 04:28:58"
    },
    {
        "Database Name": "AnalyticsDB",
        "Queries per Second": 3755.49,
        "Cache Hit Ratio (%)": 78.14,
        "Connection Count": 374,
        "Timestamp": "2022-01-21 15:23:23"
    },
    {
        "Database Name": "InventoryDB",
        "Queries per Second": 723.14,
        "Cache Hit Ratio (%)": 80.82,
        "Connection Count": 215,
        "Timestamp": "2022-06-04 18:35:02"
    },
    {
        "Database Name": "ProfilesDB",
        "Queries per Second": 2597.56,
        "Cache Hit Ratio (%)": 74.99,
        "Connection Count": 287,
        "Timestamp": "2022-09-16 11:51:32"
    }
]
<end>Please transform the following MARKDOWN data into Json:
| Company | Sector | Market Cap | Stock Price | Quarter |
| --- | --- | --- | --- | --- |
| EcoEnergy | Biotech | Large Cap | 854.51 | Q2 |
| FinanceWorks | Aerospace | Mega Cap | 411.35 | Q4 |
| TechCorp | Biotech | Mid Cap | 899.82 | Q4 |
| GlobalTrade | Automotive | Small Cap | 126.09 | Q3 |
| AeroSpace | Automotive | Large Cap | 167.32 | Q4 |<start>
[
    {
        "Company": "EcoEnergy",
        "Sector": "Biotech",
        "Market Cap": "Large Cap",
        "Stock Price": 854.51,
        "Quarter": "Q2"
    },
    {
        "Company": "FinanceWorks",
        "Sector": "Aerospace",
        "Market Cap": "Mega Cap",
        "Stock Price": 411.35,
        "Quarter": "Q4"
    },
    {
        "Company": "TechCorp",
        "Sector": "Biotech",
        "Market Cap": "Mid Cap",
        "Stock Price": 899.82,
        "Quarter": "Q4"
    },
    {
        "Company": "GlobalTrade",
        "Sector": "Automotive",
        "Market Cap": "Small Cap",
        "Stock Price": 126.09,
        "Quarter": "Q3"
    },
    {
        "Company": "AeroSpace",
        "Sector": "Automotive",
        "Market Cap": "Large Cap",
        "Stock Price": 167.32,
        "Quarter": "Q4"
    }
]
<end>Please transform the following json data into markdown:
[
    {
        "Database Name": "SalesDB",
        "Cache Hit Ratio (%)": 83.35,
        "Timestamp": "2023-12-19 00:27:50"
    },
    {
        "Database Name": "InventoryDB",
        "Cache Hit Ratio (%)": 71.08,
        "Timestamp": "2022-04-24 07:27:17"
    },
    {
        "Database Name": "LogsDB",
        "Cache Hit Ratio (%)": 77.55,
        "Timestamp": "2023-03-10 22:03:16"
    },
    {
        "Database Name": "InventoryDB",
        "Cache Hit Ratio (%)": 70.06,
        "Timestamp": "2023-10-16 16:52:44"
    },
    {
        "Database Name": "LogsDB",
        "Cache Hit Ratio (%)": 98.84,
        "Timestamp": "2022-04-06 23:18:24"
    }
]<start>
| Database Name | Cache Hit Ratio (%) | Timestamp |
| --- | --- | --- |
| SalesDB | 83.35 | 2023-12-19 00:27:50 |
| InventoryDB | 71.08 | 2022-04-24 07:27:17 |
| LogsDB | 77.55 | 2023-03-10 22:03:16 |
| InventoryDB | 70.06 | 2023-10-16 16:52:44 |
| LogsDB | 98.84 | 2022-04-06 23:18:24 |
<end>Convert this json to markdown:
[
    {
        "Age": 28,
        "City": "Detroit"
    },
    {
        "Age": 26,
        "City": "Las Vegas"
    },
    {
        "Age": 58,
        "City": "New York"
    },
    {
        "Age": 34,
        "City": "Oklahoma City"
    },
    {
        "Age": 35,
        "City": "Portland"
    },
    {
        "Age": 25,
        "City": "Oklahoma City"
    },
    {
        "Age": 52,
        "City": "Detroit"
    }
]<start>
| Age | City |
| --- | --- |
| 28 | Detroit |
| 26 | Las Vegas |
| 58 | New York |
| 34 | Oklahoma City |
| 35 | Portland |
| 25 | Oklahoma City |
| 52 | Detroit |
<end>Convert this yml to csv:
- Category: Toys
  Product Name: Apparatus
  Supplier Name: Wayne Enterprises
- Category: Electronics
  Product Name: Widget
  Supplier Name: Wonka Industries
- Category: Household
  Product Name: Apparatus
  Supplier Name: Umbrella Corp
- Category: Toys
  Product Name: Device
  Supplier Name: Wonka Industries
- Category: Automotive
  Product Name: Gadget
  Supplier Name: Umbrella Corp
<start>
Product Name,Category,Supplier Name
Apparatus,Toys,Wayne Enterprises
Widget,Electronics,Wonka Industries
Apparatus,Household,Umbrella Corp
Device,Toys,Wonka Industries
Gadget,Automotive,Umbrella Corp
<end>Please transform the following markdown data into YAML:
| Product Name | SKU | Price | Stock Quantity | Category |
| --- | --- | --- | --- | --- |
| Whatchamacallit | SKU-1005 | 453.64 | 161 | Electronics |
| Apparatus | SKU-1043 | 15.1 | 399 | Household |
| Device | SKU-1081 | 364.61 | 148 | Household |
| Gizmo | SKU-1022 | 390.91 | 398 | Sports |
| Doohickey | SKU-1004 | 379.88 | 383 | Toys |
| Widget | SKU-1046 | 90.42 | 322 | Sports |
| Apparatus | SKU-1018 | 379.56 | 379 | Sports |
| Contraption | SKU-1048 | 50.43 | 32 | Electronics |
| Instrument | SKU-1000 | 65.51 | 469 | Household |<start>
- Category: Electronics
  Price: 453.64
  Product Name: Whatchamacallit
  SKU: SKU-1005
  Stock Quantity: 161
- Category: Household
  Price: 15.1
  Product Name: Apparatus
  SKU: SKU-1043
  Stock Quantity: 399
- Category: Household
  Price: 364.61
  Product Name: Device
  SKU: SKU-1081
  Stock Quantity: 148
- Category: Sports
  Price: 390.91
  Product Name: Gizmo
  SKU: SKU-1022
  Stock Quantity: 398
- Category: Toys
  Price: 379.88
  Product Name: Doohickey
  SKU: SKU-1004
  Stock Quantity: 383
- Category: Sports
  Price: 90.42
  Product Name: Widget
  SKU: SKU-1046
  Stock Quantity: 322
- Category: Sports
  Price: 379.56
  Product Name: Apparatus
  SKU: SKU-1018
  Stock Quantity: 379
- Category: Electronics
  Price: 50.43
  Product Name: Contraption
  SKU: SKU-1048
  Stock Quantity: 32
- Category: Household
  Price: 65.51
  Product Name: Instrument
  SKU: SKU-1000
  Stock Quantity: 469
<end>Please transform the following plain text data into json:
Cache Hit Ratio (%): 81.85 | Connection Count: 427 | Average Latency (ms): 13.32 | Timestamp: 2023-11-03 10:06:08
Cache Hit Ratio (%): 75.23 | Connection Count: 422 | Average Latency (ms): 72.48 | Timestamp: 2021-08-15 22:07:54
Cache Hit Ratio (%): 89.16 | Connection Count: 190 | Average Latency (ms): 78.64 | Timestamp: 2021-07-18 14:08:32
<start>
[
    {
        "Cache Hit Ratio (%)": 81.85,
        "Connection Count": 427,
        "Average Latency (ms)": 13.32,
        "Timestamp": "2023-11-03 10:06:08"
    },
    {
        "Cache Hit Ratio (%)": 75.23,
        "Connection Count": 422,
        "Average Latency (ms)": 72.48,
        "Timestamp": "2021-08-15 22:07:54"
    },
    {
        "Cache Hit Ratio (%)": 89.16,
        "Connection Count": 190,
        "Average Latency (ms)": 78.64,
        "Timestamp": "2021-07-18 14:08:32"
    }
]
<end>Please transform the following plain text data into csv:
Product Name: Apparatus | SKU: SKU-1012 | Category: Sports | Supplier Name: ACME Corp
Product Name: Gadget | SKU: SKU-1092 | Category: Household | Supplier Name: Umbrella Corp
Product Name: Whatchamacallit | SKU: SKU-1066 | Category: Automotive | Supplier Name: Wonka Industries
<start>
Product Name,SKU,Category,Supplier Name
Apparatus,SKU-1012,Sports,ACME Corp
Gadget,SKU-1092,Household,Umbrella Corp
Whatchamacallit,SKU-1066,Automotive,Wonka Industries
<end>Transform this plain text structure to a Json format:
Location: Denver | Condition: Windy | Wind Speed (km/h): 25.4
Location: Seattle | Condition: Rainy | Wind Speed (km/h): 25.5
Location: Phoenix | Condition: Sunny | Wind Speed (km/h): 14.4
Location: Denver | Condition: Snowy | Wind Speed (km/h): 27.6
Location: Denver | Condition: Stormy | Wind Speed (km/h): 9.1
Location: Denver | Condition: Rainy | Wind Speed (km/h): 9.1
Location: Los Angeles | Condition: Rainy | Wind Speed (km/h): 14.2
Location: Denver | Condition: Foggy | Wind Speed (km/h): 0.2
Location: New York | Condition: Foggy | Wind Speed (km/h): 0.7
Location: Miami | Condition: Snowy | Wind Speed (km/h): 11.6
<start>
[
    {
        "Location": "Denver",
        "Condition": "Windy",
        "Wind Speed (km/h)": 25.4
    },
    {
        "Location": "Seattle",
        "Condition": "Rainy",
        "Wind Speed (km/h)": 25.5
    },
    {
        "Location": "Phoenix",
        "Condition": "Sunny",
        "Wind Speed (km/h)": 14.4
    },
    {
        "Location": "Denver",
        "Condition": "Snowy",
        "Wind Speed (km/h)": 27.6
    },
    {
        "Location": "Denver",
        "Condition": "Stormy",
        "Wind Speed (km/h)": 9.1
    },
    {
        "Location": "Denver",
        "Condition": "Rainy",
        "Wind Speed (km/h)": 9.1
    },
    {
        "Location": "Los Angeles",
        "Condition": "Rainy",
        "Wind Speed (km/h)": 14.2
    },
    {
        "Location": "Denver",
        "Condition": "Foggy",
        "Wind Speed (km/h)": 0.2
    },
    {
        "Location": "New York",
        "Condition": "Foggy",
        "Wind Speed (km/h)": 0.7
    },
    {
        "Location": "Miami",
        "Condition": "Snowy",
        "Wind Speed (km/h)": 11.6
    }
]
<end>Please transform the following YML data into CSV:
- Annual Revenue (B): 73.26
  Company: EcoEnergy
  Market Cap: Small Cap
  Sector: Technology
- Annual Revenue (B): 362.36
  Company: AutoDrive
  Market Cap: Large Cap
  Sector: Biotech
- Annual Revenue (B): 494.78
  Company: FinanceWorks
  Market Cap: Small Cap
  Sector: Automotive
- Annual Revenue (B): 323.49
  Company: BioPharm
  Market Cap: Mid Cap
  Sector: Retail
- Annual Revenue (B): 494.78
  Company: AutoDrive
  Market Cap: Small Cap
  Sector: Aerospace
- Annual Revenue (B): 62.51
  Company: AutoDrive
  Market Cap: Mega Cap
  Sector: Healthcare
- Annual Revenue (B): 107.35
  Company: AutoDrive
  Market Cap: Mega Cap
  Sector: Technology
- Annual Revenue (B): 212.98
  Company: TechCorp
  Market Cap: Mid Cap
  Sector: Energy
- Annual Revenue (B): 212.98
  Company: TechCorp
  Market Cap: Small Cap
  Sector: Healthcare
- Annual Revenue (B): 73.26
  Company: GlobalTrade
  Market Cap: Small Cap
  Sector: Retail
<start>
Company,Sector,Market Cap,Annual Revenue (B)
EcoEnergy,Technology,Small Cap,73.26
AutoDrive,Biotech,Large Cap,362.36
FinanceWorks,Automotive,Small Cap,494.78
BioPharm,Retail,Mid Cap,323.49
AutoDrive,Aerospace,Small Cap,494.78
AutoDrive,Healthcare,Mega Cap,62.51
AutoDrive,Technology,Mega Cap,107.35
TechCorp,Energy,Mid Cap,212.98
TechCorp,Healthcare,Small Cap,212.98
GlobalTrade,Retail,Small Cap,73.26
<end>Transform this Csv structure to a yaml format:
Restaurant Name,Cuisine,Location
Sushi World,Italian,Chicago
BBQ Barn,Mexican,Phoenix
Pasta Palace,Italian,Seattle
Burger Haven,Chinese,Seattle
Vegan Delight,Indian,San Francisco
<start>
- Cuisine: Italian
  Location: Chicago
  Restaurant Name: Sushi World
- Cuisine: Mexican
  Location: Phoenix
  Restaurant Name: BBQ Barn
- Cuisine: Italian
  Location: Seattle
  Restaurant Name: Pasta Palace
- Cuisine: Chinese
  Location: Seattle
  Restaurant Name: Burger Haven
- Cuisine: Indian
  Location: San Francisco
  Restaurant Name: Vegan Delight
<end>Convert this Plain text to Markdown:
Company: AeroSystems | Date: 2011-05-23 | Open Price: 34.39 | Close Price: 893.93 | High Price: 1250.63 | Low Price: 34.39
Company: GreenEnergy | Date: 2010-12-09 | Open Price: 149.63 | Close Price: 538.21 | High Price: 538.21 | Low Price: 149.63
Company: FinanceTrust | Date: 2021-07-07 | Open Price: 154.6 | Close Price: 487.59 | High Price: 487.59 | Low Price: 154.6
Company: MediaGroup | Date: 2015-04-01 | Open Price: 816.8 | Close Price: 149.63 | High Price: 816.8 | Low Price: 149.63
<start>
| Company | Date | Open Price | Close Price | High Price | Low Price |
| --- | --- | --- | --- | --- | --- |
| AeroSystems | 2011-05-23 | 34.39 | 893.93 | 1250.63 | 34.39 |
| GreenEnergy | 2010-12-09 | 149.63 | 538.21 | 538.21 | 149.63 |
| FinanceTrust | 2021-07-07 | 154.6 | 487.59 | 487.59 | 154.6 |
| MediaGroup | 2015-04-01 | 816.8 | 149.63 | 816.8 | 149.63 |
<end>Convert this CSV to JSON:
Title,Box Office Earnings (M)
The Great Expedition,434.33
Rise of the Titans,432.63
Beyond the Veil,50.78
The Great Expedition,951.94
The Final Voyage,184.17
Rise of the Titans,236.01
<start>
[
    {
        "Title": "The Great Expedition",
        "Box Office Earnings (M)": 434.33
    },
    {
        "Title": "Rise of the Titans",
        "Box Office Earnings (M)": 432.63
    },
    {
        "Title": "Beyond the Veil",
        "Box Office Earnings (M)": 50.78
    },
    {
        "Title": "The Great Expedition",
        "Box Office Earnings (M)": 951.94
    },
    {
        "Title": "The Final Voyage",
        "Box Office Earnings (M)": 184.17
    },
    {
        "Title": "Rise of the Titans",
        "Box Office Earnings (M)": 236.01
    }
]
<end>Please transform the following plain text data into Csv:
Name: Phyllis | Birth Month: July | City: Boston | Income: 75000
Name: Junior | Birth Month: July | City: Phoenix | Income: 330000
Name: Constance | Birth Month: October | City: Charlotte | Income: 320000
Name: Giselle | Birth Month: November | City: Seattle | Income: 225000
Name: Geneva | Birth Month: October | City: San Diego | Income: 75000
Name: Mariah | Birth Month: January | City: Nashville | Income: 130000
Name: Robert | Birth Month: June | City: Boston | Income: 435000
Name: Estella | Birth Month: December | City: Charlotte | Income: 390000
Name: Eric | Birth Month: August | City: San Antonio | Income: 315000
Name: Antonio | Birth Month: August | City: Seattle | Income: 460000
<start>
Name,Birth Month,City,Income
Phyllis,July,Boston,75000
Junior,July,Phoenix,330000
Constance,October,Charlotte,320000
Giselle,November,Seattle,225000
Geneva,October,San Diego,75000
Mariah,January,Nashville,130000
Robert,June,Boston,435000
Estella,December,Charlotte,390000
Eric,August,San Antonio,315000
Antonio,August,Seattle,460000
<end>Here's some json data, can you convert it to YAML?
[
    {
        "Temperature (C)": -5.8,
        "Humidity (%)": 63,
        "Wind Speed (km/h)": 4.5
    },
    {
        "Temperature (C)": 26.6,
        "Humidity (%)": 72,
        "Wind Speed (km/h)": 17.4
    },
    {
        "Temperature (C)": 26.6,
        "Humidity (%)": 28,
        "Wind Speed (km/h)": 8.2
    },
    {
        "Temperature (C)": 28.2,
        "Humidity (%)": 79,
        "Wind Speed (km/h)": 28.3
    },
    {
        "Temperature (C)": 21.5,
        "Humidity (%)": 63,
        "Wind Speed (km/h)": 2.4
    },
    {
        "Temperature (C)": 36.5,
        "Humidity (%)": 66,
        "Wind Speed (km/h)": 11.7
    },
    {
        "Temperature (C)": 28.6,
        "Humidity (%)": 90,
        "Wind Speed (km/h)": 8.8
    },
    {
        "Temperature (C)": 21.8,
        "Humidity (%)": 54,
        "Wind Speed (km/h)": 20.6
    },
    {
        "Temperature (C)": 31.0,
        "Humidity (%)": 37,
        "Wind Speed (km/h)": 12.7
    },
    {
        "Temperature (C)": 9.2,
        "Humidity (%)": 79,
        "Wind Speed (km/h)": 8.8
    }
]<start>
- Humidity (%): 63
  Temperature (C): -5.8
  Wind Speed (km/h): 4.5
- Humidity (%): 72
  Temperature (C): 26.6
  Wind Speed (km/h): 17.4
- Humidity (%): 28
  Temperature (C): 26.6
  Wind Speed (km/h): 8.2
- Humidity (%): 79
  Temperature (C): 28.2
  Wind Speed (km/h): 28.3
- Humidity (%): 63
  Temperature (C): 21.5
  Wind Speed (km/h): 2.4
- Humidity (%): 66
  Temperature (C): 36.5
  Wind Speed (km/h): 11.7
- Humidity (%): 90
  Temperature (C): 28.6
  Wind Speed (km/h): 8.8
- Humidity (%): 54
  Temperature (C): 21.8
  Wind Speed (km/h): 20.6
- Humidity (%): 37
  Temperature (C): 31.0
  Wind Speed (km/h): 12.7
- Humidity (%): 79
  Temperature (C): 9.2
  Wind Speed (km/h): 8.8
<end>Convert this YML to Markdown:
- Condition: Foggy
  Day: Saturday
  Humidity (%): 51
  Wind Speed (km/h): 12.1
- Condition: Windy
  Day: Sunday
  Humidity (%): 23
  Wind Speed (km/h): 19.9
- Condition: Snowy
  Day: Saturday
  Humidity (%): 46
  Wind Speed (km/h): 11.9
- Condition: Cloudy
  Day: Sunday
  Humidity (%): 91
  Wind Speed (km/h): 2.6
- Condition: Stormy
  Day: Friday
  Humidity (%): 54
  Wind Speed (km/h): 23.2
- Condition: Cloudy
  Day: Saturday
  Humidity (%): 79
  Wind Speed (km/h): 17.9
- Condition: Rainy
  Day: Tuesday
  Humidity (%): 22
  Wind Speed (km/h): 24.4
- Condition: Snowy
  Day: Monday
  Humidity (%): 62
  Wind Speed (km/h): 13.4
- Condition: Foggy
  Day: Tuesday
  Humidity (%): 45
  Wind Speed (km/h): 16.9
- Condition: Sunny
  Day: Sunday
  Humidity (%): 58
  Wind Speed (km/h): 14.9
<start>
| Condition | Humidity (%) | Wind Speed (km/h) | Day |
| --- | --- | --- | --- |
| Foggy | 51 | 12.1 | Saturday |
| Windy | 23 | 19.9 | Sunday |
| Snowy | 46 | 11.9 | Saturday |
| Cloudy | 91 | 2.6 | Sunday |
| Stormy | 54 | 23.2 | Friday |
| Cloudy | 79 | 17.9 | Saturday |
| Rainy | 22 | 24.4 | Tuesday |
| Snowy | 62 | 13.4 | Monday |
| Foggy | 45 | 16.9 | Tuesday |
| Sunny | 58 | 14.9 | Sunday |
<end>Please transform the following csv data into plain text:
Cuisine,Location,Rating
Italian,Los Angeles,2
French,Phoenix,5
Mexican,Phoenix,4
Mexican,Miami,4
<start>
Cuisine: Italian | Location: Los Angeles | Rating: 2
Cuisine: French | Location: Phoenix | Rating: 5
Cuisine: Mexican | Location: Phoenix | Rating: 4
Cuisine: Mexican | Location: Miami | Rating: 4
<end>Here's some MARKDOWN data, can you convert it to Yml?
| Company | Sector | Market Cap | Stock Price | Annual Revenue (B) | Quarter |
| --- | --- | --- | --- | --- | --- |
| TechCorp | Energy | Large Cap | 362.05 | 307.61 | Q1 |
| HealthPlus | Technology | Large Cap | 486.03 | 390.41 | Q1 |
| GlobalTrade | Finance | Mid Cap | 33.43 | 370.24 | Q2 |
| EcoEnergy | Automotive | Large Cap | 365.16 | 385.68 | Q1 |
| Foodies | Technology | Large Cap | 968.28 | 492.63 | Q4 |<start>
- Annual Revenue (B): 307.61
  Company: TechCorp
  Market Cap: Large Cap
  Quarter: Q1
  Sector: Energy
  Stock Price: 362.05
- Annual Revenue (B): 390.41
  Company: HealthPlus
  Market Cap: Large Cap
  Quarter: Q1
  Sector: Technology
  Stock Price: 486.03
- Annual Revenue (B): 370.24
  Company: GlobalTrade
  Market Cap: Mid Cap
  Quarter: Q2
  Sector: Finance
  Stock Price: 33.43
- Annual Revenue (B): 385.68
  Company: EcoEnergy
  Market Cap: Large Cap
  Quarter: Q1
  Sector: Automotive
  Stock Price: 365.16
- Annual Revenue (B): 492.63
  Company: Foodies
  Market Cap: Large Cap
  Quarter: Q4
  Sector: Technology
  Stock Price: 968.28
<end>Can you change this json into CSV?
[
    {
        "Title": "Rise of the Titans",
        "Director": "Mara Moonshadow",
        "Genre": "Action",
        "Release Year": 2022,
        "Box Office Earnings (M)": 474.84
    },
    {
        "Title": "The Endless Horizon",
        "Director": "Orin Shadowalker",
        "Genre": "Thriller",
        "Release Year": 1997,
        "Box Office Earnings (M)": 183.09
    },
    {
        "Title": "Rise of the Titans",
        "Director": "Selene Darkwhisper",
        "Genre": "Adventure",
        "Release Year": 1990,
        "Box Office Earnings (M)": 882.87
    },
    {
        "Title": "Dreamwalker",
        "Director": "Selene Darkwhisper",
        "Genre": "Horror",
        "Release Year": 2011,
        "Box Office Earnings (M)": 632.15
    }
]<start>
Title,Director,Genre,Release Year,Box Office Earnings (M)
Rise of the Titans,Mara Moonshadow,Action,2022,474.84
The Endless Horizon,Orin Shadowalker,Thriller,1997,183.09
Rise of the Titans,Selene Darkwhisper,Adventure,1990,882.87
Dreamwalker,Selene Darkwhisper,Horror,2011,632.15
<end>Convert this plain text to Markdown:
Title: Mystery of the Depths | Director: Rylan Frostblade | Genre: Sci-Fi | Release Year: 1980 | Box Office Earnings (M): 123.66
Title: Dreamwalker | Director: Orin Shadowalker | Genre: Drama | Release Year: 1988 | Box Office Earnings (M): 612.41
Title: The Great Expedition | Director: Cade Firebrand | Genre: Sci-Fi | Release Year: 1980 | Box Office Earnings (M): 548.57
Title: Mystery of the Depths | Director: Zara Stormrider | Genre: Fantasy | Release Year: 1984 | Box Office Earnings (M): 179.54
Title: The Great Expedition | Director: Zara Stormrider | Genre: Action | Release Year: 1981 | Box Office Earnings (M): 531.58
Title: The Endless Horizon | Director: Rylan Frostblade | Genre: Fantasy | Release Year: 1995 | Box Office Earnings (M): 123.66
<start>
| Title | Director | Genre | Release Year | Box Office Earnings (M) |
| --- | --- | --- | --- | --- |
| Mystery of the Depths | Rylan Frostblade | Sci-Fi | 1980 | 123.66 |
| Dreamwalker | Orin Shadowalker | Drama | 1988 | 612.41 |
| The Great Expedition | Cade Firebrand | Sci-Fi | 1980 | 548.57 |
| Mystery of the Depths | Zara Stormrider | Fantasy | 1984 | 179.54 |
| The Great Expedition | Zara Stormrider | Action | 1981 | 531.58 |
| The Endless Horizon | Rylan Frostblade | Fantasy | 1995 | 123.66 |
<end>Please transform the following Yaml data into markdown:
- Category: Household
  Price: 143.99
  SKU: SKU-1006
  Stock Quantity: 27
  Supplier Name: Wayne Enterprises
- Category: Electronics
  Price: 392.05
  SKU: SKU-1033
  Stock Quantity: 431
  Supplier Name: Globex
- Category: Household
  Price: 113.32
  SKU: SKU-1005
  Stock Quantity: 295
  Supplier Name: Wayne Enterprises
- Category: Toys
  Price: 405.28
  SKU: SKU-1083
  Stock Quantity: 444
  Supplier Name: Wonka Industries
- Category: Toys
  Price: 392.57
  SKU: SKU-1044
  Stock Quantity: 393
  Supplier Name: Wayne Enterprises
<start>
| SKU | Price | Stock Quantity | Category | Supplier Name |
| --- | --- | --- | --- | --- |
| SKU-1006 | 143.99 | 27 | Household | Wayne Enterprises |
| SKU-1033 | 392.05 | 431 | Electronics | Globex |
| SKU-1005 | 113.32 | 295 | Household | Wayne Enterprises |
| SKU-1083 | 405.28 | 444 | Toys | Wonka Industries |
| SKU-1044 | 392.57 | 393 | Toys | Wayne Enterprises |
<end>Here's some Markdown data, can you convert it to JSON?
| Database Name | Queries per Second | Connection Count | Average Latency (ms) |
| --- | --- | --- | --- |
| ProfilesDB | 4150.9 | 14 | 18.45 |
| OrdersDB | 3094.1 | 456 | 35.01 |
| UserDB | 346.53 | 78 | 74.98 |
| MetricsDB | 2280.96 | 357 | 91.77 |
| MetricsDB | 1038.73 | 348 | 58.52 |
| ProductsDB | 4159.62 | 315 | 41.87 |<start>
[
    {
        "Database Name": "ProfilesDB",
        "Queries per Second": 4150.9,
        "Connection Count": 14,
        "Average Latency (ms)": 18.45
    },
    {
        "Database Name": "OrdersDB",
        "Queries per Second": 3094.1,
        "Connection Count": 456,
        "Average Latency (ms)": 35.01
    },
    {
        "Database Name": "UserDB",
        "Queries per Second": 346.53,
        "Connection Count": 78,
        "Average Latency (ms)": 74.98
    },
    {
        "Database Name": "MetricsDB",
        "Queries per Second": 2280.96,
        "Connection Count": 357,
        "Average Latency (ms)": 91.77
    },
    {
        "Database Name": "MetricsDB",
        "Queries per Second": 1038.73,
        "Connection Count": 348,
        "Average Latency (ms)": 58.52
    },
    {
        "Database Name": "ProductsDB",
        "Queries per Second": 4159.62,
        "Connection Count": 315,
        "Average Latency (ms)": 41.87
    }
]
<end>Can you change this json into csv?
[
    {
        "Title": "Tales of the Brave",
        "Author": "Draven Blackthorn",
        "Genre": "Horror",
        "Publication Year": 2016,
        "Rating": 1.8
    },
    {
        "Title": "Whispers of the Abyss",
        "Author": "Sylvia Nightshade",
        "Genre": "Horror",
        "Publication Year": 2010,
        "Rating": 1.5
    },
    {
        "Title": "Echoes of Eternity",
        "Author": "Draven Blackthorn",
        "Genre": "Science Fiction",
        "Publication Year": 1993,
        "Rating": 1.6
    },
    {
        "Title": "Echoes of Eternity",
        "Author": "Rowan Ashborne",
        "Genre": "Science Fiction",
        "Publication Year": 1968,
        "Rating": 1.5
    }
]<start>
Title,Author,Genre,Publication Year,Rating
Tales of the Brave,Draven Blackthorn,Horror,2016,1.8
Whispers of the Abyss,Sylvia Nightshade,Horror,2010,1.5
Echoes of Eternity,Draven Blackthorn,Science Fiction,1993,1.6
Echoes of Eternity,Rowan Ashborne,Science Fiction,1968,1.5
<end>Please transform the following Yaml data into MARKDOWN:
- Distance (miles): 1913.5
  Start Location: Chicago
  Trip Name: Canyon Trek
- Distance (miles): 1222.4
  Start Location: Phoenix
  Trip Name: Historic Route
- Distance (miles): 1966.5
  Start Location: Phoenix
  Trip Name: Desert Drive
- Distance (miles): 909.2
  Start Location: Phoenix
  Trip Name: Highway Odyssey
- Distance (miles): 84.8
  Start Location: Chicago
  Trip Name: Coast to Coast
- Distance (miles): 1479.8
  Start Location: New York
  Trip Name: Canyon Trek
- Distance (miles): 886.2
  Start Location: Chicago
  Trip Name: Canyon Trek
- Distance (miles): 2340.6
  Start Location: New York
  Trip Name: Historic Route
- Distance (miles): 1920.0
  Start Location: Chicago
  Trip Name: Valley Voyage
- Distance (miles): 1331.5
  Start Location: Los Angeles
  Trip Name: Forest Journey
<start>
| Trip Name | Start Location | Distance (miles) |
| --- | --- | --- |
| Canyon Trek | Chicago | 1913.5 |
| Historic Route | Phoenix | 1222.4 |
| Desert Drive | Phoenix | 1966.5 |
| Highway Odyssey | Phoenix | 909.2 |
| Coast to Coast | Chicago | 84.8 |
| Canyon Trek | New York | 1479.8 |
| Canyon Trek | Chicago | 886.2 |
| Historic Route | New York | 2340.6 |
| Valley Voyage | Chicago | 1920.0 |
| Forest Journey | Los Angeles | 1331.5 |
<end>Convert this yml to csv:
- Price: 241.06
  Product Name: Device
  SKU: SKU-1045
  Stock Quantity: 346
  Supplier Name: ACME Corp
- Price: 361.42
  Product Name: Contraption
  SKU: SKU-1009
  Stock Quantity: 268
  Supplier Name: Wayne Enterprises
- Price: 156.54
  Product Name: Whatchamacallit
  SKU: SKU-1015
  Stock Quantity: 18
  Supplier Name: Wonka Industries
- Price: 300.43
  Product Name: Apparatus
  SKU: SKU-1015
  Stock Quantity: 168
  Supplier Name: ACME Corp
- Price: 147.2
  Product Name: Contraption
  SKU: SKU-1034
  Stock Quantity: 342
  Supplier Name: Wonka Industries
- Price: 463.45
  Product Name: Thingamajig
  SKU: SKU-1092
  Stock Quantity: 466
  Supplier Name: Wonka Industries
- Price: 319.11
  Product Name: Gizmo
  SKU: SKU-1032
  Stock Quantity: 103
  Supplier Name: Wayne Enterprises
<start>
Product Name,SKU,Price,Stock Quantity,Supplier Name
Device,SKU-1045,241.06,346,ACME Corp
Contraption,SKU-1009,361.42,268,Wayne Enterprises
Whatchamacallit,SKU-1015,156.54,18,Wonka Industries
Apparatus,SKU-1015,300.43,168,ACME Corp
Contraption,SKU-1034,147.2,342,Wonka Industries
Thingamajig,SKU-1092,463.45,466,Wonka Industries
Gizmo,SKU-1032,319.11,103,Wayne Enterprises
<end>Can you change this JSON into YML?
[
    {
        "Name": "Victoria",
        "Age": 25,
        "City": "Denver",
        "Income": 100000
    },
    {
        "Name": "William",
        "Age": 58,
        "City": "Memphis",
        "Income": 70000
    },
    {
        "Name": "Jim",
        "Age": 68,
        "City": "San Jose",
        "Income": 320000
    },
    {
        "Name": "Ollie",
        "Age": 53,
        "City": "Los Angeles",
        "Income": 215000
    },
    {
        "Name": "Santiago",
        "Age": 20,
        "City": "Las Vegas",
        "Income": 170000
    },
    {
        "Name": "Johnathan",
        "Age": 38,
        "City": "Memphis",
        "Income": 360000
    }
]<start>
- Age: 25
  City: Denver
  Income: 100000
  Name: Victoria
- Age: 58
  City: Memphis
  Income: 70000
  Name: William
- Age: 68
  City: San Jose
  Income: 320000
  Name: Jim
- Age: 53
  City: Los Angeles
  Income: 215000
  Name: Ollie
- Age: 20
  City: Las Vegas
  Income: 170000
  Name: Santiago
- Age: 38
  City: Memphis
  Income: 360000
  Name: Johnathan
<end>Convert this Markdown to YML:
| Cache Hit Ratio (%) | Connection Count | Average Latency (ms) | Timestamp |
| --- | --- | --- | --- |
| 74.44 | 488 | 45.94 | 2023-05-03 19:08:28 |
| 92.92 | 18 | 18.67 | 2023-04-24 00:44:40 |
| 80.76 | 28 | 60.11 | 2022-10-24 05:10:33 |
| 79.33 | 22 | 46.34 | 2021-02-01 10:19:58 |
| 75.52 | 214 | 15.57 | 2023-09-24 03:39:39 |
| 92.19 | 357 | 23.84 | 2022-09-28 01:05:17 |
| 85.3 | 45 | 69.49 | 2023-02-10 22:51:30 |
| 88.17 | 28 | 49.88 | 2023-03-18 07:19:32 |
| 97.43 | 172 | 44.28 | 2021-01-21 04:56:00 |<start>
- Average Latency (ms): 45.94
  Cache Hit Ratio (%): 74.44
  Connection Count: 488
  Timestamp: '2023-05-03 19:08:28'
- Average Latency (ms): 18.67
  Cache Hit Ratio (%): 92.92
  Connection Count: 18
  Timestamp: '2023-04-24 00:44:40'
- Average Latency (ms): 60.11
  Cache Hit Ratio (%): 80.76
  Connection Count: 28
  Timestamp: '2022-10-24 05:10:33'
- Average Latency (ms): 46.34
  Cache Hit Ratio (%): 79.33
  Connection Count: 22
  Timestamp: '2021-02-01 10:19:58'
- Average Latency (ms): 15.57
  Cache Hit Ratio (%): 75.52
  Connection Count: 214
  Timestamp: '2023-09-24 03:39:39'
- Average Latency (ms): 23.84
  Cache Hit Ratio (%): 92.19
  Connection Count: 357
  Timestamp: '2022-09-28 01:05:17'
- Average Latency (ms): 69.49
  Cache Hit Ratio (%): 85.3
  Connection Count: 45
  Timestamp: '2023-02-10 22:51:30'
- Average Latency (ms): 49.88
  Cache Hit Ratio (%): 88.17
  Connection Count: 28
  Timestamp: '2023-03-18 07:19:32'
- Average Latency (ms): 44.28
  Cache Hit Ratio (%): 97.43
  Connection Count: 172
  Timestamp: '2021-01-21 04:56:00'
<end>Transform this csv structure to a Yml format:
Database Name,Queries per Second,Cache Hit Ratio (%),Connection Count,Average Latency (ms),Timestamp
AnalyticsDB,3840.4,83.37,238,62.68,2023-07-19 05:33:15
AnalyticsDB,1387.3,92.56,54,13.4,2023-11-23 18:22:25
SalesDB,1694.08,87.58,440,23.09,2021-12-02 03:41:23
<start>
- Average Latency (ms): 62.68
  Cache Hit Ratio (%): 83.37
  Connection Count: 238
  Database Name: AnalyticsDB
  Queries per Second: 3840.4
  Timestamp: '2023-07-19 05:33:15'
- Average Latency (ms): 13.4
  Cache Hit Ratio (%): 92.56
  Connection Count: 54
  Database Name: AnalyticsDB
  Queries per Second: 1387.3
  Timestamp: '2023-11-23 18:22:25'
- Average Latency (ms): 23.09
  Cache Hit Ratio (%): 87.58
  Connection Count: 440
  Database Name: SalesDB
  Queries per Second: 1694.08
  Timestamp: '2021-12-02 03:41:23'
<end>Please transform the following Json data into yaml:
[
    {
        "Trip Name": "Mountain Adventure",
        "Start Location": "New York",
        "Fuel Used (gallons)": 97.7
    },
    {
        "Trip Name": "Desert Drive",
        "Start Location": "Chicago",
        "Fuel Used (gallons)": 97.3
    },
    {
        "Trip Name": "Coast to Coast",
        "Start Location": "San Francisco",
        "Fuel Used (gallons)": 76.4
    },
    {
        "Trip Name": "Desert Drive",
        "Start Location": "Phoenix",
        "Fuel Used (gallons)": 98.9
    },
    {
        "Trip Name": "Canyon Trek",
        "Start Location": "Denver",
        "Fuel Used (gallons)": 61.7
    },
    {
        "Trip Name": "City Explorer",
        "Start Location": "New York",
        "Fuel Used (gallons)": 72.2
    },
    {
        "Trip Name": "Lakeside Retreat",
        "Start Location": "Houston",
        "Fuel Used (gallons)": 93.9
    },
    {
        "Trip Name": "Forest Journey",
        "Start Location": "New York",
        "Fuel Used (gallons)": 61.7
    },
    {
        "Trip Name": "Lakeside Retreat",
        "Start Location": "Phoenix",
        "Fuel Used (gallons)": 42.2
    },
    {
        "Trip Name": "Desert Drive",
        "Start Location": "San Francisco",
        "Fuel Used (gallons)": 48.8
    }
]<start>
- Fuel Used (gallons): 97.7
  Start Location: New York
  Trip Name: Mountain Adventure
- Fuel Used (gallons): 97.3
  Start Location: Chicago
  Trip Name: Desert Drive
- Fuel Used (gallons): 76.4
  Start Location: San Francisco
  Trip Name: Coast to Coast
- Fuel Used (gallons): 98.9
  Start Location: Phoenix
  Trip Name: Desert Drive
- Fuel Used (gallons): 61.7
  Start Location: Denver
  Trip Name: Canyon Trek
- Fuel Used (gallons): 72.2
  Start Location: New York
  Trip Name: City Explorer
- Fuel Used (gallons): 93.9
  Start Location: Houston
  Trip Name: Lakeside Retreat
- Fuel Used (gallons): 61.7
  Start Location: New York
  Trip Name: Forest Journey
- Fuel Used (gallons): 42.2
  Start Location: Phoenix
  Trip Name: Lakeside Retreat
- Fuel Used (gallons): 48.8
  Start Location: San Francisco
  Trip Name: Desert Drive
<end>Convert this yaml to plain text:
- Close Price: 1246.03
  Company: TechnoCorp
  Date: '2014-11-05'
  High Price: 1246.03
  Low Price: 557.54
  Open Price: 685.87
- Close Price: 335.26
  Company: AutoMotive
  Date: '2019-09-12'
  High Price: 530.06
  Low Price: 244.34
  Open Price: 244.34
- Close Price: 1485.41
  Company: TechnoCorp
  Date: '2023-02-01'
  High Price: 1485.41
  Low Price: 13.69
  Open Price: 13.69
- Close Price: 107.59
  Company: RetailWorld
  Date: '2020-02-22'
  High Price: 920.05
  Low Price: 107.59
  Open Price: 291.95
- Close Price: 173.87
  Company: AeroSystems
  Date: '2015-10-28'
  High Price: 1489.44
  Low Price: 173.87
  Open Price: 1489.44
<start>
Company: TechnoCorp | Date: 2014-11-05 | Open Price: 685.87 | Close Price: 1246.03 | High Price: 1246.03 | Low Price: 557.54
Company: AutoMotive | Date: 2019-09-12 | Open Price: 244.34 | Close Price: 335.26 | High Price: 530.06 | Low Price: 244.34
Company: TechnoCorp | Date: 2023-02-01 | Open Price: 13.69 | Close Price: 1485.41 | High Price: 1485.41 | Low Price: 13.69
Company: RetailWorld | Date: 2020-02-22 | Open Price: 291.95 | Close Price: 107.59 | High Price: 920.05 | Low Price: 107.59
Company: AeroSystems | Date: 2015-10-28 | Open Price: 1489.44 | Close Price: 173.87 | High Price: 1489.44 | Low Price: 173.87
<end>Convert this Plain text to yaml:
Location: Miami | Condition: Snowy | Humidity (%): 71 | Wind Speed (km/h): 3.9 | Day: Wednesday
Location: Chicago | Condition: Rainy | Humidity (%): 35 | Wind Speed (km/h): 27.7 | Day: Monday
Location: Denver | Condition: Cloudy | Humidity (%): 70 | Wind Speed (km/h): 15.1 | Day: Saturday
Location: Phoenix | Condition: Stormy | Humidity (%): 57 | Wind Speed (km/h): 21.7 | Day: Thursday
Location: Houston | Condition: Cloudy | Humidity (%): 57 | Wind Speed (km/h): 12.5 | Day: Tuesday
Location: Los Angeles | Condition: Sunny | Humidity (%): 86 | Wind Speed (km/h): 3.9 | Day: Sunday
Location: New York | Condition: Windy | Humidity (%): 47 | Wind Speed (km/h): 24.6 | Day: Monday
Location: Chicago | Condition: Snowy | Humidity (%): 31 | Wind Speed (km/h): 21.7 | Day: Thursday
<start>
- Condition: Snowy
  Day: Wednesday
  Humidity (%): 71
  Location: Miami
  Wind Speed (km/h): 3.9
- Condition: Rainy
  Day: Monday
  Humidity (%): 35
  Location: Chicago
  Wind Speed (km/h): 27.7
- Condition: Cloudy
  Day: Saturday
  Humidity (%): 70
  Location: Denver
  Wind Speed (km/h): 15.1
- Condition: Stormy
  Day: Thursday
  Humidity (%): 57
  Location: Phoenix
  Wind Speed (km/h): 21.7
- Condition: Cloudy
  Day: Tuesday
  Humidity (%): 57
  Location: Houston
  Wind Speed (km/h): 12.5
- Condition: Sunny
  Day: Sunday
  Humidity (%): 86
  Location: Los Angeles
  Wind Speed (km/h): 3.9
- Condition: Windy
  Day: Monday
  Humidity (%): 47
  Location: New York
  Wind Speed (km/h): 24.6
- Condition: Snowy
  Day: Thursday
  Humidity (%): 31
  Location: Chicago
  Wind Speed (km/h): 21.7
<end>Can you change this Markdown into plain text?
| Restaurant Name | Cuisine | Price Range |
| --- | --- | --- |
| Pasta Palace | Italian | $$$$ |
| Pasta Palace | Indian | $$$$$ |
| Curry Corner | Mediterranean | $$$ |
| Vegan Delight | Mediterranean | $$$ |<start>
Restaurant Name: Pasta Palace | Cuisine: Italian | Price Range: $$$$
Restaurant Name: Pasta Palace | Cuisine: Indian | Price Range: $$$$$
Restaurant Name: Curry Corner | Cuisine: Mediterranean | Price Range: $$$
Restaurant Name: Vegan Delight | Cuisine: Mediterranean | Price Range: $$$
<end>Convert this JSON to Plain text:
[
    {
        "Location": "Phoenix",
        "Condition": "Cloudy",
        "Temperature (C)": 26.0,
        "Wind Speed (km/h)": 6.1,
        "Day": "Wednesday"
    },
    {
        "Location": "New York",
        "Condition": "Foggy",
        "Temperature (C)": 26.5,
        "Wind Speed (km/h)": 27.7,
        "Day": "Saturday"
    },
    {
        "Location": "Phoenix",
        "Condition": "Rainy",
        "Temperature (C)": 24.6,
        "Wind Speed (km/h)": 3.4,
        "Day": "Sunday"
    },
    {
        "Location": "Denver",
        "Condition": "Sunny",
        "Temperature (C)": -4.1,
        "Wind Speed (km/h)": 5.1,
        "Day": "Wednesday"
    },
    {
        "Location": "Seattle",
        "Condition": "Snowy",
        "Temperature (C)": 4.4,
        "Wind Speed (km/h)": 22.4,
        "Day": "Wednesday"
    },
    {
        "Location": "Los Angeles",
        "Condition": "Cloudy",
        "Temperature (C)": 2.8,
        "Wind Speed (km/h)": 8.9,
        "Day": "Thursday"
    },
    {
        "Location": "Phoenix",
        "Condition": "Rainy",
        "Temperature (C)": 30.1,
        "Wind Speed (km/h)": 22.7,
        "Day": "Saturday"
    },
    {
        "Location": "Seattle",
        "Condition": "Cloudy",
        "Temperature (C)": 7.7,
        "Wind Speed (km/h)": 19.2,
        "Day": "Sunday"
    },
    {
        "Location": "Chicago",
        "Condition": "Stormy",
        "Temperature (C)": 27.3,
        "Wind Speed (km/h)": 6.6,
        "Day": "Saturday"
    },
    {
        "Location": "Phoenix",
        "Condition": "Windy",
        "Temperature (C)": 24.0,
        "Wind Speed (km/h)": 14.0,
        "Day": "Friday"
    }
]<start>
Location: Phoenix | Condition: Cloudy | Temperature (C): 26.0 | Wind Speed (km/h): 6.1 | Day: Wednesday
Location: New York | Condition: Foggy | Temperature (C): 26.5 | Wind Speed (km/h): 27.7 | Day: Saturday
Location: Phoenix | Condition: Rainy | Temperature (C): 24.6 | Wind Speed (km/h): 3.4 | Day: Sunday
Location: Denver | Condition: Sunny | Temperature (C): -4.1 | Wind Speed (km/h): 5.1 | Day: Wednesday
Location: Seattle | Condition: Snowy | Temperature (C): 4.4 | Wind Speed (km/h): 22.4 | Day: Wednesday
Location: Los Angeles | Condition: Cloudy | Temperature (C): 2.8 | Wind Speed (km/h): 8.9 | Day: Thursday
Location: Phoenix | Condition: Rainy | Temperature (C): 30.1 | Wind Speed (km/h): 22.7 | Day: Saturday
Location: Seattle | Condition: Cloudy | Temperature (C): 7.7 | Wind Speed (km/h): 19.2 | Day: Sunday
Location: Chicago | Condition: Stormy | Temperature (C): 27.3 | Wind Speed (km/h): 6.6 | Day: Saturday
Location: Phoenix | Condition: Windy | Temperature (C): 24.0 | Wind Speed (km/h): 14.0 | Day: Friday
<end>Transform this json structure to a Markdown format:
[
    {
        "Age": 57,
        "Income": 70000
    },
    {
        "Age": 43,
        "Income": 60000
    },
    {
        "Age": 58,
        "Income": 265000
    },
    {
        "Age": 32,
        "Income": 50000
    },
    {
        "Age": 36,
        "Income": 350000
    },
    {
        "Age": 41,
        "Income": 490000
    },
    {
        "Age": 48,
        "Income": 80000
    },
    {
        "Age": 25,
        "Income": 400000
    }
]<start>
| Age | Income |
| --- | --- |
| 57 | 70000 |
| 43 | 60000 |
| 58 | 265000 |
| 32 | 50000 |
| 36 | 350000 |
| 41 | 490000 |
| 48 | 80000 |
| 25 | 400000 |
<end>Transform this YML structure to a plain text format:
- Annual Revenue (B): 426.64
  Company: HealthPlus
  Market Cap: Large Cap
  Quarter: Q2
  Sector: Biotech
  Stock Price: 478.27
- Annual Revenue (B): 115.71
  Company: AeroSpace
  Market Cap: Mega Cap
  Quarter: Q4
  Sector: Finance
  Stock Price: 517.3
- Annual Revenue (B): 100.07
  Company: Foodies
  Market Cap: Mega Cap
  Quarter: Q4
  Sector: Energy
  Stock Price: 285.85
- Annual Revenue (B): 123.82
  Company: FinanceWorks
  Market Cap: Mid Cap
  Quarter: Q1
  Sector: Aerospace
  Stock Price: 160.74
- Annual Revenue (B): 492.23
  Company: TechCorp
  Market Cap: Large Cap
  Quarter: Q2
  Sector: Healthcare
  Stock Price: 717.68
- Annual Revenue (B): 115.71
  Company: BioPharm
  Market Cap: Small Cap
  Quarter: Q3
  Sector: Energy
  Stock Price: 831.46
- Annual Revenue (B): 488.24
  Company: GlobalTrade
  Market Cap: Large Cap
  Quarter: Q3
  Sector: Finance
  Stock Price: 731.24
- Annual Revenue (B): 498.42
  Company: AutoDrive
  Market Cap: Mid Cap
  Quarter: Q4
  Sector: Energy
  Stock Price: 462.76
- Annual Revenue (B): 103.89
  Company: RetailHub
  Market Cap: Mid Cap
  Quarter: Q4
  Sector: Retail
  Stock Price: 900.94
<start>
Company: HealthPlus | Sector: Biotech | Market Cap: Large Cap | Stock Price: 478.27 | Annual Revenue (B): 426.64 | Quarter: Q2
Company: AeroSpace | Sector: Finance | Market Cap: Mega Cap | Stock Price: 517.3 | Annual Revenue (B): 115.71 | Quarter: Q4
Company: Foodies | Sector: Energy | Market Cap: Mega Cap | Stock Price: 285.85 | Annual Revenue (B): 100.07 | Quarter: Q4
Company: FinanceWorks | Sector: Aerospace | Market Cap: Mid Cap | Stock Price: 160.74 | Annual Revenue (B): 123.82 | Quarter: Q1
Company: TechCorp | Sector: Healthcare | Market Cap: Large Cap | Stock Price: 717.68 | Annual Revenue (B): 492.23 | Quarter: Q2
Company: BioPharm | Sector: Energy | Market Cap: Small Cap | Stock Price: 831.46 | Annual Revenue (B): 115.71 | Quarter: Q3
Company: GlobalTrade | Sector: Finance | Market Cap: Large Cap | Stock Price: 731.24 | Annual Revenue (B): 488.24 | Quarter: Q3
Company: AutoDrive | Sector: Energy | Market Cap: Mid Cap | Stock Price: 462.76 | Annual Revenue (B): 498.42 | Quarter: Q4
Company: RetailHub | Sector: Retail | Market Cap: Mid Cap | Stock Price: 900.94 | Annual Revenue (B): 103.89 | Quarter: Q4
<end>Please transform the following plain text data into JSON:
Temperature (C): 8.9 | Humidity (%): 81 | Day: Friday
Temperature (C): -6.8 | Humidity (%): 86 | Day: Saturday
Temperature (C): -7.7 | Humidity (%): 52 | Day: Saturday
Temperature (C): 17.5 | Humidity (%): 49 | Day: Saturday
Temperature (C): 33.1 | Humidity (%): 100 | Day: Wednesday
Temperature (C): -1.5 | Humidity (%): 84 | Day: Friday
Temperature (C): 37.4 | Humidity (%): 57 | Day: Tuesday
<start>
[
    {
        "Temperature (C)": 8.9,
        "Humidity (%)": 81,
        "Day": "Friday"
    },
    {
        "Temperature (C)": -6.8,
        "Humidity (%)": 86,
        "Day": "Saturday"
    },
    {
        "Temperature (C)": -7.7,
        "Humidity (%)": 52,
        "Day": "Saturday"
    },
    {
        "Temperature (C)": 17.5,
        "Humidity (%)": 49,
        "Day": "Saturday"
    },
    {
        "Temperature (C)": 33.1,
        "Humidity (%)": 100,
        "Day": "Wednesday"
    },
    {
        "Temperature (C)": -1.5,
        "Humidity (%)": 84,
        "Day": "Friday"
    },
    {
        "Temperature (C)": 37.4,
        "Humidity (%)": 57,
        "Day": "Tuesday"
    }
]
<end>Here's some yaml data, can you convert it to csv?
- Device ID: device-0061
  Location: Bedroom
  Reading Value: 12.23
  Timestamp: '2023-10-20 22:57:51'
- Device ID: device-0066
  Location: Garage
  Reading Value: 9.29
  Timestamp: '2021-01-08 05:32:10'
- Device ID: device-0081
  Location: Office
  Reading Value: 21.82
  Timestamp: '2022-09-21 04:40:39'
- Device ID: device-0069
  Location: Garden
  Reading Value: 18.84
  Timestamp: '2021-11-22 13:32:39'
- Device ID: device-0070
  Location: Hallway
  Reading Value: -13.85
  Timestamp: '2023-06-03 16:47:31'
- Device ID: device-0082
  Location: Living Room
  Reading Value: -0.88
  Timestamp: '2021-11-13 21:52:52'
- Device ID: device-0092
  Location: Living Room
  Reading Value: 34.89
  Timestamp: '2022-12-08 07:19:17'
- Device ID: device-0010
  Location: Living Room
  Reading Value: 4.33
  Timestamp: '2022-10-12 08:20:33'
- Device ID: device-0050
  Location: Kitchen
  Reading Value: 11.32
  Timestamp: '2022-07-05 21:06:15'
<start>
Device ID,Location,Reading Value,Timestamp
device-0061,Bedroom,12.23,2023-10-20 22:57:51
device-0066,Garage,9.29,2021-01-08 05:32:10
device-0081,Office,21.82,2022-09-21 04:40:39
device-0069,Garden,18.84,2021-11-22 13:32:39
device-0070,Hallway,-13.85,2023-06-03 16:47:31
device-0082,Living Room,-0.88,2021-11-13 21:52:52
device-0092,Living Room,34.89,2022-12-08 07:19:17
device-0010,Living Room,4.33,2022-10-12 08:20:33
device-0050,Kitchen,11.32,2022-07-05 21:06:15
<end>Please transform the following json data into csv:
[
    {
        "Company": "BioPharm",
        "Sector": "Biotech",
        "Market Cap": "Mega Cap",
        "Stock Price": 643.84,
        "Annual Revenue (B)": 267.84,
        "Quarter": "Q4"
    },
    {
        "Company": "FinanceWorks",
        "Sector": "Technology",
        "Market Cap": "Large Cap",
        "Stock Price": 829.15,
        "Annual Revenue (B)": 451.19,
        "Quarter": "Q3"
    },
    {
        "Company": "BioPharm",
        "Sector": "Finance",
        "Market Cap": "Small Cap",
        "Stock Price": 570.05,
        "Annual Revenue (B)": 267.84,
        "Quarter": "Q2"
    },
    {
        "Company": "AeroSpace",
        "Sector": "Healthcare",
        "Market Cap": "Mega Cap",
        "Stock Price": 686.81,
        "Annual Revenue (B)": 480.84,
        "Quarter": "Q4"
    }
]<start>
Company,Sector,Market Cap,Stock Price,Annual Revenue (B),Quarter
BioPharm,Biotech,Mega Cap,643.84,267.84,Q4
FinanceWorks,Technology,Large Cap,829.15,451.19,Q3
BioPharm,Finance,Small Cap,570.05,267.84,Q2
AeroSpace,Healthcare,Mega Cap,686.81,480.84,Q4
<end>Here's some CSV data, can you convert it to Plain text?
Company,Sector,Market Cap,Annual Revenue (B),Quarter
GlobalTrade,Biotech,Mid Cap,411.17,Q2
AutoDrive,Technology,Large Cap,73.11,Q4
GlobalTrade,Retail,Mid Cap,60.43,Q4
GlobalTrade,Aerospace,Small Cap,173.62,Q1
BioPharm,Healthcare,Mega Cap,376.52,Q1
Foodies,Biotech,Small Cap,166.35,Q1
EcoEnergy,Technology,Large Cap,485.13,Q4
<start>
Company: GlobalTrade | Sector: Biotech | Market Cap: Mid Cap | Annual Revenue (B): 411.17 | Quarter: Q2
Company: AutoDrive | Sector: Technology | Market Cap: Large Cap | Annual Revenue (B): 73.11 | Quarter: Q4
Company: GlobalTrade | Sector: Retail | Market Cap: Mid Cap | Annual Revenue (B): 60.43 | Quarter: Q4
Company: GlobalTrade | Sector: Aerospace | Market Cap: Small Cap | Annual Revenue (B): 173.62 | Quarter: Q1
Company: BioPharm | Sector: Healthcare | Market Cap: Mega Cap | Annual Revenue (B): 376.52 | Quarter: Q1
Company: Foodies | Sector: Biotech | Market Cap: Small Cap | Annual Revenue (B): 166.35 | Quarter: Q1
Company: EcoEnergy | Sector: Technology | Market Cap: Large Cap | Annual Revenue (B): 485.13 | Quarter: Q4
<end>Convert this YML to plain text:
- Cuisine: Mexican
  Location: Phoenix
  Rating: 5
  Restaurant Name: BBQ Barn
- Cuisine: Italian
  Location: Chicago
  Rating: 5
  Restaurant Name: The Steakhouse
- Cuisine: Mexican
  Location: San Francisco
  Rating: 4
  Restaurant Name: Vegan Delight
- Cuisine: French
  Location: Houston
  Rating: 4
  Restaurant Name: Pasta Palace
- Cuisine: French
  Location: San Francisco
  Rating: 3
  Restaurant Name: Burger Haven
- Cuisine: French
  Location: Seattle
  Rating: 3
  Restaurant Name: Taco Town
- Cuisine: Mediterranean
  Location: San Francisco
  Rating: 1
  Restaurant Name: Pizza Planet
- Cuisine: Chinese
  Location: New York
  Rating: 5
  Restaurant Name: Burger Haven
<start>
Restaurant Name: BBQ Barn | Cuisine: Mexican | Location: Phoenix | Rating: 5
Restaurant Name: The Steakhouse | Cuisine: Italian | Location: Chicago | Rating: 5
Restaurant Name: Vegan Delight | Cuisine: Mexican | Location: San Francisco | Rating: 4
Restaurant Name: Pasta Palace | Cuisine: French | Location: Houston | Rating: 4
Restaurant Name: Burger Haven | Cuisine: French | Location: San Francisco | Rating: 3
Restaurant Name: Taco Town | Cuisine: French | Location: Seattle | Rating: 3
Restaurant Name: Pizza Planet | Cuisine: Mediterranean | Location: San Francisco | Rating: 1
Restaurant Name: Burger Haven | Cuisine: Chinese | Location: New York | Rating: 5
<end>Here's some Csv data, can you convert it to markdown?
Temperature (C),Humidity (%),Wind Speed (km/h),Day
33.9,71,6.3,Tuesday
32.8,54,17.2,Tuesday
-6.9,99,15.8,Monday
0.1,99,15.8,Thursday
33.3,35,15.8,Friday
12.1,75,17.2,Sunday
6.4,42,28.3,Tuesday
9.5,28,19.8,Thursday
<start>
| Temperature (C) | Humidity (%) | Wind Speed (km/h) | Day |
| --- | --- | --- | --- |
| 33.9 | 71 | 6.3 | Tuesday |
| 32.8 | 54 | 17.2 | Tuesday |
| -6.9 | 99 | 15.8 | Monday |
| 0.1 | 99 | 15.8 | Thursday |
| 33.3 | 35 | 15.8 | Friday |
| 12.1 | 75 | 17.2 | Sunday |
| 6.4 | 42 | 28.3 | Tuesday |
| 9.5 | 28 | 19.8 | Thursday |
<end>Here's some csv data, can you convert it to Plain text?
Location,Rating,Price Range
New York,5,$
San Francisco,2,$
Seattle,4,$$$$$
Miami,4,$$$$$
Seattle,4,$$$
Chicago,5,$$$$$
Chicago,3,$$$
Los Angeles,1,$
New York,5,$$$$
Phoenix,4,$$$
<start>
Location: New York | Rating: 5 | Price Range: $
Location: San Francisco | Rating: 2 | Price Range: $
Location: Seattle | Rating: 4 | Price Range: $$$$$
Location: Miami | Rating: 4 | Price Range: $$$$$
Location: Seattle | Rating: 4 | Price Range: $$$
Location: Chicago | Rating: 5 | Price Range: $$$$$
Location: Chicago | Rating: 3 | Price Range: $$$
Location: Los Angeles | Rating: 1 | Price Range: $
Location: New York | Rating: 5 | Price Range: $$$$
Location: Phoenix | Rating: 4 | Price Range: $$$
<end>Can you change this CSV into json?
Restaurant Name,Cuisine,Location,Price Range
Sushi World,Japanese,Miami,$$$$$
The Steakhouse,Mediterranean,Houston,$$$$$
Vegan Delight,Mediterranean,Chicago,$$
Burger Haven,Italian,Phoenix,$$$
Burger Haven,Mediterranean,Phoenix,$$$
Taco Town,Chinese,San Francisco,$$$
Pizza Planet,French,Phoenix,$$
Burger Haven,Chinese,Seattle,$$
Sushi World,Mediterranean,Houston,$$
The Golden Spoon,Japanese,New York,$$
<start>
[
    {
        "Restaurant Name": "Sushi World",
        "Cuisine": "Japanese",
        "Location": "Miami",
        "Price Range": "$$$$$"
    },
    {
        "Restaurant Name": "The Steakhouse",
        "Cuisine": "Mediterranean",
        "Location": "Houston",
        "Price Range": "$$$$$"
    },
    {
        "Restaurant Name": "Vegan Delight",
        "Cuisine": "Mediterranean",
        "Location": "Chicago",
        "Price Range": "$$"
    },
    {
        "Restaurant Name": "Burger Haven",
        "Cuisine": "Italian",
        "Location": "Phoenix",
        "Price Range": "$$$"
    },
    {
        "Restaurant Name": "Burger Haven",
        "Cuisine": "Mediterranean",
        "Location": "Phoenix",
        "Price Range": "$$$"
    },
    {
        "Restaurant Name": "Taco Town",
        "Cuisine": "Chinese",
        "Location": "San Francisco",
        "Price Range": "$$$"
    },
    {
        "Restaurant Name": "Pizza Planet",
        "Cuisine": "French",
        "Location": "Phoenix",
        "Price Range": "$$"
    },
    {
        "Restaurant Name": "Burger Haven",
        "Cuisine": "Chinese",
        "Location": "Seattle",
        "Price Range": "$$"
    },
    {
        "Restaurant Name": "Sushi World",
        "Cuisine": "Mediterranean",
        "Location": "Houston",
        "Price Range": "$$"
    },
    {
        "Restaurant Name": "The Golden Spoon",
        "Cuisine": "Japanese",
        "Location": "New York",
        "Price Range": "$$"
    }
]
<end>Can you change this markdown into json?
| Title | Genre | Rating |
| --- | --- | --- |
| The Forgotten World | Non-Fiction | 4.9 |
| The Crystal Key | Science Fiction | 4.3 |
| Legends of the Rift | Historical | 1.4 |<start>
[
    {
        "Title": "The Forgotten World",
        "Genre": "Non-Fiction",
        "Rating": 4.9
    },
    {
        "Title": "The Crystal Key",
        "Genre": "Science Fiction",
        "Rating": 4.3
    },
    {
        "Title": "Legends of the Rift",
        "Genre": "Historical",
        "Rating": 1.4
    }
]
<end>Here's some CSV data, can you convert it to yml?
Title,Author
A Journey Through Time,Kara Firebrand
A Journey Through Time,Rowan Ashborne
Echoes of Eternity,Isla Windrider
Echoes of Eternity,Isla Windrider
Tales of the Brave,Elara Moonshadow
The Last Sky,Luna Silverleaf
Legends of the Rift,Galen Starfire
The Crystal Key,Sylvia Nightshade
The Crystal Key,Sylvia Nightshade
<start>
- Author: Kara Firebrand
  Title: A Journey Through Time
- Author: Rowan Ashborne
  Title: A Journey Through Time
- Author: Isla Windrider
  Title: Echoes of Eternity
- Author: Isla Windrider
  Title: Echoes of Eternity
- Author: Elara Moonshadow
  Title: Tales of the Brave
- Author: Luna Silverleaf
  Title: The Last Sky
- Author: Galen Starfire
  Title: Legends of the Rift
- Author: Sylvia Nightshade
  Title: The Crystal Key
- Author: Sylvia Nightshade
  Title: The Crystal Key
<end>Can you change this plain text into yml?
Open Price: 1067.5 | Close Price: 181.02 | High Price: 1067.5 | Low Price: 181.02 | Volume: 3795618
Open Price: 979.95 | Close Price: 242.1 | High Price: 979.95 | Low Price: 242.1 | Volume: 9750033
Open Price: 79.66 | Close Price: 317.02 | High Price: 559.62 | Low Price: 79.66 | Volume: 4182283
Open Price: 79.66 | Close Price: 979.95 | High Price: 979.95 | Low Price: 79.66 | Volume: 5583304
Open Price: 624.95 | Close Price: 818.14 | High Price: 818.14 | Low Price: 181.02 | Volume: 2886850
Open Price: 818.29 | Close Price: 1095.12 | High Price: 1314.38 | Low Price: 818.29 | Volume: 855038
Open Price: 691.05 | Close Price: 241.4 | High Price: 691.05 | Low Price: 241.4 | Volume: 9420188
<start>
- Close Price: 181.02
  High Price: 1067.5
  Low Price: 181.02
  Open Price: 1067.5
  Volume: 3795618
- Close Price: 242.1
  High Price: 979.95
  Low Price: 242.1
  Open Price: 979.95
  Volume: 9750033
- Close Price: 317.02
  High Price: 559.62
  Low Price: 79.66
  Open Price: 79.66
  Volume: 4182283
- Close Price: 979.95
  High Price: 979.95
  Low Price: 79.66
  Open Price: 79.66
  Volume: 5583304
- Close Price: 818.14
  High Price: 818.14
  Low Price: 181.02
  Open Price: 624.95
  Volume: 2886850
- Close Price: 1095.12
  High Price: 1314.38
  Low Price: 818.29
  Open Price: 818.29
  Volume: 855038
- Close Price: 241.4
  High Price: 691.05
  Low Price: 241.4
  Open Price: 691.05
  Volume: 9420188
<end>Please transform the following Markdown data into JSON:
| Name | Age | City |
| --- | --- | --- |
| Bethany | 30 | Charlotte |
| Ezra | 41 | Washington |
| Steven | 22 | Nashville |
| Anthony | 22 | San Antonio |
| Emily | 30 | Detroit |
| Leon | 41 | Portland |<start>
[
    {
        "Name": "Bethany",
        "Age": 30,
        "City": "Charlotte"
    },
    {
        "Name": "Ezra",
        "Age": 41,
        "City": "Washington"
    },
    {
        "Name": "Steven",
        "Age": 22,
        "City": "Nashville"
    },
    {
        "Name": "Anthony",
        "Age": 22,
        "City": "San Antonio"
    },
    {
        "Name": "Emily",
        "Age": 30,
        "City": "Detroit"
    },
    {
        "Name": "Leon",
        "Age": 41,
        "City": "Portland"
    }
]
<end>Transform this plain text structure to a yml format:
Restaurant Name: Curry Corner | Cuisine: American | Price Range: $$$$$
Restaurant Name: Burger Haven | Cuisine: Chinese | Price Range: $$$$$
Restaurant Name: Curry Corner | Cuisine: American | Price Range: $$$$$
Restaurant Name: BBQ Barn | Cuisine: Italian | Price Range: $$$$$
Restaurant Name: Vegan Delight | Cuisine: Japanese | Price Range: $$$$$
<start>
- Cuisine: American
  Price Range: $$$$$
  Restaurant Name: Curry Corner
- Cuisine: Chinese
  Price Range: $$$$$
  Restaurant Name: Burger Haven
- Cuisine: American
  Price Range: $$$$$
  Restaurant Name: Curry Corner
- Cuisine: Italian
  Price Range: $$$$$
  Restaurant Name: BBQ Barn
- Cuisine: Japanese
  Price Range: $$$$$
  Restaurant Name: Vegan Delight
<end>Convert this Csv to MARKDOWN:
Cuisine,Location,Rating,Price Range
Indian,New York,3,$
Japanese,Chicago,3,$$$$
Chinese,Chicago,3,$$
Mediterranean,Miami,4,$$
American,Miami,3,$$
American,Phoenix,1,$$$$
<start>
| Cuisine | Location | Rating | Price Range |
| --- | --- | --- | --- |
| Indian | New York | 3 | $ |
| Japanese | Chicago | 3 | $$$$ |
| Chinese | Chicago | 3 | $$ |
| Mediterranean | Miami | 4 | $$ |
| American | Miami | 3 | $$ |
| American | Phoenix | 1 | $$$$ |
<end>Can you change this plain text into csv?
Genre: Science Fiction | Publication Year: 1982
Genre: Romance | Publication Year: 1952
Genre: Romance | Publication Year: 1952
<start>
Genre,Publication Year
Science Fiction,1982
Romance,1952
Romance,1952
<end>Here's some JSON data, can you convert it to Yml?
[
    {
        "Trip Name": "Desert Drive",
        "End Location": "Denver",
        "Distance (miles)": 385.1,
        "Duration (hours)": 31.5,
        "Fuel Used (gallons)": 20.4
    },
    {
        "Trip Name": "Historic Route",
        "End Location": "Denver",
        "Distance (miles)": 2608.5,
        "Duration (hours)": 68.0,
        "Fuel Used (gallons)": 70.2
    },
    {
        "Trip Name": "Forest Journey",
        "End Location": "Phoenix",
        "Distance (miles)": 2886.8,
        "Duration (hours)": 7.2,
        "Fuel Used (gallons)": 91.1
    },
    {
        "Trip Name": "Mountain Adventure",
        "End Location": "Miami",
        "Distance (miles)": 1225.3,
        "Duration (hours)": 31.0,
        "Fuel Used (gallons)": 20.4
    }
]<start>
- Distance (miles): 385.1
  Duration (hours): 31.5
  End Location: Denver
  Fuel Used (gallons): 20.4
  Trip Name: Desert Drive
- Distance (miles): 2608.5
  Duration (hours): 68.0
  End Location: Denver
  Fuel Used (gallons): 70.2
  Trip Name: Historic Route
- Distance (miles): 2886.8
  Duration (hours): 7.2
  End Location: Phoenix
  Fuel Used (gallons): 91.1
  Trip Name: Forest Journey
- Distance (miles): 1225.3
  Duration (hours): 31.0
  End Location: Miami
  Fuel Used (gallons): 20.4
  Trip Name: Mountain Adventure
<end>Transform this Json structure to a MARKDOWN format:
[
    {
        "Company": "TechnoCorp",
        "Date": "2013-02-25",
        "Open Price": 1199.82,
        "Close Price": 774.32,
        "High Price": 1469.71,
        "Low Price": 511.06,
        "Volume": 6547899
    },
    {
        "Company": "AutoMotive",
        "Date": "2012-05-14",
        "Open Price": 1369.73,
        "Close Price": 488.94,
        "High Price": 1369.73,
        "Low Price": 488.94,
        "Volume": 702999
    },
    {
        "Company": "RetailWorld",
        "Date": "2010-07-24",
        "Open Price": 1304.01,
        "Close Price": 1201.26,
        "High Price": 1304.01,
        "Low Price": 600.23,
        "Volume": 5125597
    },
    {
        "Company": "BioLife",
        "Date": "2012-01-03",
        "Open Price": 374.99,
        "Close Price": 80.65,
        "High Price": 639.95,
        "Low Price": 80.65,
        "Volume": 644808
    },
    {
        "Company": "FoodChain",
        "Date": "2018-05-25",
        "Open Price": 460.97,
        "Close Price": 39.57,
        "High Price": 460.97,
        "Low Price": 39.57,
        "Volume": 7325479
    },
    {
        "Company": "AeroSystems",
        "Date": "2014-12-17",
        "Open Price": 1304.01,
        "Close Price": 807.64,
        "High Price": 1304.01,
        "Low Price": 601.45,
        "Volume": 8598883
    },
    {
        "Company": "AutoMotive",
        "Date": "2014-01-23",
        "Open Price": 398.84,
        "Close Price": 675.35,
        "High Price": 675.35,
        "Low Price": 398.84,
        "Volume": 8713550
    },
    {
        "Company": "MediaGroup",
        "Date": "2022-02-04",
        "Open Price": 984.48,
        "Close Price": 1306.63,
        "High Price": 1306.63,
        "Low Price": 984.48,
        "Volume": 2354672
    },
    {
        "Company": "AeroSystems",
        "Date": "2012-08-07",
        "Open Price": 994.89,
        "Close Price": 1054.49,
        "High Price": 1054.49,
        "Low Price": 994.89,
        "Volume": 5160618
    },
    {
        "Company": "RetailWorld",
        "Date": "2018-12-01",
        "Open Price": 601.45,
        "Close Price": 80.65,
        "High Price": 749.91,
        "Low Price": 80.65,
        "Volume": 1900812
    }
]<start>
| Company | Date | Open Price | Close Price | High Price | Low Price | Volume |
| --- | --- | --- | --- | --- | --- | --- |
| TechnoCorp | 2013-02-25 | 1199.82 | 774.32 | 1469.71 | 511.06 | 6547899 |
| AutoMotive | 2012-05-14 | 1369.73 | 488.94 | 1369.73 | 488.94 | 702999 |
| RetailWorld | 2010-07-24 | 1304.01 | 1201.26 | 1304.01 | 600.23 | 5125597 |
| BioLife | 2012-01-03 | 374.99 | 80.65 | 639.95 | 80.65 | 644808 |
| FoodChain | 2018-05-25 | 460.97 | 39.57 | 460.97 | 39.57 | 7325479 |
| AeroSystems | 2014-12-17 | 1304.01 | 807.64 | 1304.01 | 601.45 | 8598883 |
| AutoMotive | 2014-01-23 | 398.84 | 675.35 | 675.35 | 398.84 | 8713550 |
| MediaGroup | 2022-02-04 | 984.48 | 1306.63 | 1306.63 | 984.48 | 2354672 |
| AeroSystems | 2012-08-07 | 994.89 | 1054.49 | 1054.49 | 994.89 | 5160618 |
| RetailWorld | 2018-12-01 | 601.45 | 80.65 | 749.91 | 80.65 | 1900812 |
<end>Transform this PLAIN TEXT structure to a yaml format:
Age: 61 | City: El Paso
Age: 38 | City: Nashville
Age: 43 | City: Baltimore
Age: 25 | City: San Francisco
<start>
- Age: 61
  City: El Paso
- Age: 38
  City: Nashville
- Age: 43
  City: Baltimore
- Age: 25
  City: San Francisco
<end>Please transform the following Csv data into plain text:
Product Name,SKU,Price,Stock Quantity,Category,Supplier Name
Contraption,SKU-1079,139.82,36,Sports,ACME Corp
Gadget,SKU-1093,305.29,216,Toys,Wayne Enterprises
Whatchamacallit,SKU-1044,160.94,119,Sports,ACME Corp
Gizmo,SKU-1027,219.07,342,Household,ACME Corp
Doohickey,SKU-1075,302.54,322,Automotive,Globex
Contraption,SKU-1087,21.84,226,Household,Wonka Industries
Widget,SKU-1002,280.81,77,Toys,Globex
<start>
Product Name: Contraption | SKU: SKU-1079 | Price: 139.82 | Stock Quantity: 36 | Category: Sports | Supplier Name: ACME Corp
Product Name: Gadget | SKU: SKU-1093 | Price: 305.29 | Stock Quantity: 216 | Category: Toys | Supplier Name: Wayne Enterprises
Product Name: Whatchamacallit | SKU: SKU-1044 | Price: 160.94 | Stock Quantity: 119 | Category: Sports | Supplier Name: ACME Corp
Product Name: Gizmo | SKU: SKU-1027 | Price: 219.07 | Stock Quantity: 342 | Category: Household | Supplier Name: ACME Corp
Product Name: Doohickey | SKU: SKU-1075 | Price: 302.54 | Stock Quantity: 322 | Category: Automotive | Supplier Name: Globex
Product Name: Contraption | SKU: SKU-1087 | Price: 21.84 | Stock Quantity: 226 | Category: Household | Supplier Name: Wonka Industries
Product Name: Widget | SKU: SKU-1002 | Price: 280.81 | Stock Quantity: 77 | Category: Toys | Supplier Name: Globex
<end>Please transform the following Yml data into json:
- Condition: Snowy
  Day: Saturday
  Temperature (C): -4.6
- Condition: Stormy
  Day: Wednesday
  Temperature (C): 15.2
- Condition: Cloudy
  Day: Friday
  Temperature (C): -4.6
- Condition: Windy
  Day: Tuesday
  Temperature (C): -7.1
- Condition: Foggy
  Day: Wednesday
  Temperature (C): 35.0
- Condition: Foggy
  Day: Wednesday
  Temperature (C): 4.2
- Condition: Snowy
  Day: Tuesday
  Temperature (C): -9.7
- Condition: Snowy
  Day: Saturday
  Temperature (C): -1.5
<start>
[
    {
        "Condition": "Snowy",
        "Temperature (C)": -4.6,
        "Day": "Saturday"
    },
    {
        "Condition": "Stormy",
        "Temperature (C)": 15.2,
        "Day": "Wednesday"
    },
    {
        "Condition": "Cloudy",
        "Temperature (C)": -4.6,
        "Day": "Friday"
    },
    {
        "Condition": "Windy",
        "Temperature (C)": -7.1,
        "Day": "Tuesday"
    },
    {
        "Condition": "Foggy",
        "Temperature (C)": 35.0,
        "Day": "Wednesday"
    },
    {
        "Condition": "Foggy",
        "Temperature (C)": 4.2,
        "Day": "Wednesday"
    },
    {
        "Condition": "Snowy",
        "Temperature (C)": -9.7,
        "Day": "Tuesday"
    },
    {
        "Condition": "Snowy",
        "Temperature (C)": -1.5,
        "Day": "Saturday"
    }
]
<end>Convert this markdown to Plain text:
| Company | Sector | Market Cap | Stock Price | Annual Revenue (B) |
| --- | --- | --- | --- | --- |
| BioPharm | Finance | Mega Cap | 360.06 | 195.31 |
| FinanceWorks | Finance | Large Cap | 715.15 | 156.48 |
| GlobalTrade | Aerospace | Large Cap | 63.71 | 94.2 |
| BioPharm | Automotive | Large Cap | 370.61 | 274.43 |
| FinanceWorks | Healthcare | Large Cap | 343.91 | 156.32 |
| HealthPlus | Aerospace | Large Cap | 430.6 | 115.49 |
| BioPharm | Automotive | Small Cap | 63.71 | 236.1 |
| TechCorp | Healthcare | Small Cap | 318.21 | 156.32 |
| BioPharm | Aerospace | Mega Cap | 360.06 | 190.59 |
| HealthPlus | Energy | Large Cap | 145.99 | 243.09 |<start>
Company: BioPharm | Sector: Finance | Market Cap: Mega Cap | Stock Price: 360.06 | Annual Revenue (B): 195.31
Company: FinanceWorks | Sector: Finance | Market Cap: Large Cap | Stock Price: 715.15 | Annual Revenue (B): 156.48
Company: GlobalTrade | Sector: Aerospace | Market Cap: Large Cap | Stock Price: 63.71 | Annual Revenue (B): 94.2
Company: BioPharm | Sector: Automotive | Market Cap: Large Cap | Stock Price: 370.61 | Annual Revenue (B): 274.43
Company: FinanceWorks | Sector: Healthcare | Market Cap: Large Cap | Stock Price: 343.91 | Annual Revenue (B): 156.32
Company: HealthPlus | Sector: Aerospace | Market Cap: Large Cap | Stock Price: 430.6 | Annual Revenue (B): 115.49
Company: BioPharm | Sector: Automotive | Market Cap: Small Cap | Stock Price: 63.71 | Annual Revenue (B): 236.1
Company: TechCorp | Sector: Healthcare | Market Cap: Small Cap | Stock Price: 318.21 | Annual Revenue (B): 156.32
Company: BioPharm | Sector: Aerospace | Market Cap: Mega Cap | Stock Price: 360.06 | Annual Revenue (B): 190.59
Company: HealthPlus | Sector: Energy | Market Cap: Large Cap | Stock Price: 145.99 | Annual Revenue (B): 243.09
<end>Please transform the following markdown data into plain text:
| Company | Date | Open Price | Close Price | High Price | Low Price |
| --- | --- | --- | --- | --- | --- |
| TechnoCorp | 2022-12-09 | 625.85 | 1010.04 | 1010.04 | 625.85 |
| AeroSystems | 2014-12-14 | 942.74 | 345.76 | 942.74 | 160.81 |
| FinanceTrust | 2020-08-12 | 293.4 | 587.67 | 1406.14 | 293.4 |
| TechnoCorp | 2022-01-16 | 1180.51 | 558.84 | 1180.51 | 558.84 |
| MediaGroup | 2019-04-14 | 112.49 | 83.32 | 127.82 | 83.32 |
| HealthGen | 2013-01-11 | 804.96 | 1196.85 | 1196.85 | 804.96 |
| FinanceTrust | 2023-02-06 | 558.84 | 549.18 | 609.34 | 549.18 |
| HealthGen | 2010-03-22 | 549.18 | 1406.14 | 1406.14 | 300.94 |<start>
Company: TechnoCorp | Date: 2022-12-09 | Open Price: 625.85 | Close Price: 1010.04 | High Price: 1010.04 | Low Price: 625.85
Company: AeroSystems | Date: 2014-12-14 | Open Price: 942.74 | Close Price: 345.76 | High Price: 942.74 | Low Price: 160.81
Company: FinanceTrust | Date: 2020-08-12 | Open Price: 293.4 | Close Price: 587.67 | High Price: 1406.14 | Low Price: 293.4
Company: TechnoCorp | Date: 2022-01-16 | Open Price: 1180.51 | Close Price: 558.84 | High Price: 1180.51 | Low Price: 558.84
Company: MediaGroup | Date: 2019-04-14 | Open Price: 112.49 | Close Price: 83.32 | High Price: 127.82 | Low Price: 83.32
Company: HealthGen | Date: 2013-01-11 | Open Price: 804.96 | Close Price: 1196.85 | High Price: 1196.85 | Low Price: 804.96
Company: FinanceTrust | Date: 2023-02-06 | Open Price: 558.84 | Close Price: 549.18 | High Price: 609.34 | Low Price: 549.18
Company: HealthGen | Date: 2010-03-22 | Open Price: 549.18 | Close Price: 1406.14 | High Price: 1406.14 | Low Price: 300.94
<end>Please transform the following json data into csv:
[
    {
        "Location": "New York",
        "Temperature (C)": 29.0,
        "Humidity (%)": 100,
        "Wind Speed (km/h)": 15.6,
        "Day": "Saturday"
    },
    {
        "Location": "Los Angeles",
        "Temperature (C)": 3.0,
        "Humidity (%)": 74,
        "Wind Speed (km/h)": 15.1,
        "Day": "Monday"
    },
    {
        "Location": "Denver",
        "Temperature (C)": -7.2,
        "Humidity (%)": 91,
        "Wind Speed (km/h)": 28.1,
        "Day": "Sunday"
    },
    {
        "Location": "Houston",
        "Temperature (C)": -2.7,
        "Humidity (%)": 67,
        "Wind Speed (km/h)": 3.0,
        "Day": "Friday"
    },
    {
        "Location": "Seattle",
        "Temperature (C)": 7.4,
        "Humidity (%)": 71,
        "Wind Speed (km/h)": 22.8,
        "Day": "Monday"
    },
    {
        "Location": "New York",
        "Temperature (C)": 31.9,
        "Humidity (%)": 82,
        "Wind Speed (km/h)": 15.6,
        "Day": "Saturday"
    }
]<start>
Location,Temperature (C),Humidity (%),Wind Speed (km/h),Day
New York,29.0,100,15.6,Saturday
Los Angeles,3.0,74,15.1,Monday
Denver,-7.2,91,28.1,Sunday
Houston,-2.7,67,3.0,Friday
Seattle,7.4,71,22.8,Monday
New York,31.9,82,15.6,Saturday
<end>Transform this csv structure to a markdown format:
Product Name,SKU,Price,Stock Quantity,Category,Supplier Name
Doohickey,SKU-1092,183.74,111,Electronics,Umbrella Corp
Apparatus,SKU-1053,276.72,410,Automotive,Umbrella Corp
Doohickey,SKU-1094,417.28,110,Sports,Globex
Apparatus,SKU-1098,280.26,420,Household,ACME Corp
Thingamajig,SKU-1018,395.57,135,Sports,Globex
Apparatus,SKU-1014,179.51,321,Sports,Wayne Enterprises
Gadget,SKU-1099,40.87,463,Toys,Umbrella Corp
Widget,SKU-1015,264.16,388,Toys,ACME Corp
Device,SKU-1003,210.38,59,Toys,Wayne Enterprises
Widget,SKU-1010,290.76,340,Toys,Globex
<start>
| Product Name | SKU | Price | Stock Quantity | Category | Supplier Name |
| --- | --- | --- | --- | --- | --- |
| Doohickey | SKU-1092 | 183.74 | 111 | Electronics | Umbrella Corp |
| Apparatus | SKU-1053 | 276.72 | 410 | Automotive | Umbrella Corp |
| Doohickey | SKU-1094 | 417.28 | 110 | Sports | Globex |
| Apparatus | SKU-1098 | 280.26 | 420 | Household | ACME Corp |
| Thingamajig | SKU-1018 | 395.57 | 135 | Sports | Globex |
| Apparatus | SKU-1014 | 179.51 | 321 | Sports | Wayne Enterprises |
| Gadget | SKU-1099 | 40.87 | 463 | Toys | Umbrella Corp |
| Widget | SKU-1015 | 264.16 | 388 | Toys | ACME Corp |
| Device | SKU-1003 | 210.38 | 59 | Toys | Wayne Enterprises |
| Widget | SKU-1010 | 290.76 | 340 | Toys | Globex |
<end>Here's some yml data, can you convert it to plain text?
- Category: Toys
  Product Name: Contraption
  SKU: SKU-1039
  Stock Quantity: 112
  Supplier Name: ACME Corp
- Category: Toys
  Product Name: Apparatus
  SKU: SKU-1004
  Stock Quantity: 231
  Supplier Name: ACME Corp
- Category: Electronics
  Product Name: Device
  SKU: SKU-1096
  Stock Quantity: 491
  Supplier Name: Umbrella Corp
- Category: Automotive
  Product Name: Apparatus
  SKU: SKU-1033
  Stock Quantity: 347
  Supplier Name: Wonka Industries
- Category: Sports
  Product Name: Doohickey
  SKU: SKU-1006
  Stock Quantity: 313
  Supplier Name: Wonka Industries
<start>
Product Name: Contraption | SKU: SKU-1039 | Stock Quantity: 112 | Category: Toys | Supplier Name: ACME Corp
Product Name: Apparatus | SKU: SKU-1004 | Stock Quantity: 231 | Category: Toys | Supplier Name: ACME Corp
Product Name: Device | SKU: SKU-1096 | Stock Quantity: 491 | Category: Electronics | Supplier Name: Umbrella Corp
Product Name: Apparatus | SKU: SKU-1033 | Stock Quantity: 347 | Category: Automotive | Supplier Name: Wonka Industries
Product Name: Doohickey | SKU: SKU-1006 | Stock Quantity: 313 | Category: Sports | Supplier Name: Wonka Industries
<end>Transform this PLAIN TEXT structure to a markdown format:
Database Name: ProductsDB | Cache Hit Ratio (%): 70.61 | Connection Count: 84
Database Name: ProfilesDB | Cache Hit Ratio (%): 77.77 | Connection Count: 94
Database Name: SessionsDB | Cache Hit Ratio (%): 72.52 | Connection Count: 149
Database Name: ProfilesDB | Cache Hit Ratio (%): 81.48 | Connection Count: 14
Database Name: LogsDB | Cache Hit Ratio (%): 90.19 | Connection Count: 90
Database Name: ProductsDB | Cache Hit Ratio (%): 72.97 | Connection Count: 33
Database Name: UserDB | Cache Hit Ratio (%): 97.41 | Connection Count: 486
Database Name: MetricsDB | Cache Hit Ratio (%): 72.24 | Connection Count: 339
<start>
| Database Name | Cache Hit Ratio (%) | Connection Count |
| --- | --- | --- |
| ProductsDB | 70.61 | 84 |
| ProfilesDB | 77.77 | 94 |
| SessionsDB | 72.52 | 149 |
| ProfilesDB | 81.48 | 14 |
| LogsDB | 90.19 | 90 |
| ProductsDB | 72.97 | 33 |
| UserDB | 97.41 | 486 |
| MetricsDB | 72.24 | 339 |
<end>Convert this Yml to csv:
- Cache Hit Ratio (%): 88.91
  Connection Count: 144
  Database Name: UserDB
  Timestamp: '2021-04-16 17:45:41'
- Cache Hit Ratio (%): 93.42
  Connection Count: 464
  Database Name: UserDB
  Timestamp: '2023-05-26 10:36:57'
- Cache Hit Ratio (%): 84.77
  Connection Count: 205
  Database Name: AnalyticsDB
  Timestamp: '2023-07-03 13:33:11'
<start>
Database Name,Cache Hit Ratio (%),Connection Count,Timestamp
UserDB,88.91,144,2021-04-16 17:45:41
UserDB,93.42,464,2023-05-26 10:36:57
AnalyticsDB,84.77,205,2023-07-03 13:33:11
<end>Can you change this Plain text into markdown?
Restaurant Name: BBQ Barn | Location: Phoenix
Restaurant Name: Sushi World | Location: Los Angeles
Restaurant Name: Pizza Planet | Location: Seattle
Restaurant Name: Curry Corner | Location: Los Angeles
Restaurant Name: The Golden Spoon | Location: Seattle
<start>
| Restaurant Name | Location |
| --- | --- |
| BBQ Barn | Phoenix |
| Sushi World | Los Angeles |
| Pizza Planet | Seattle |
| Curry Corner | Los Angeles |
| The Golden Spoon | Seattle |
<end>Can you change this json into Csv?
[
    {
        "Name": "Adrianna",
        "Age": 27,
        "Birth Month": "December",
        "City": "Los Angeles",
        "Income": 465000
    },
    {
        "Name": "Adrienne",
        "Age": 54,
        "Birth Month": "August",
        "City": "Nashville",
        "Income": 345000
    },
    {
        "Name": "Kristen",
        "Age": 51,
        "Birth Month": "February",
        "City": "Houston",
        "Income": 285000
    }
]<start>
Name,Age,Birth Month,City,Income
Adrianna,27,December,Los Angeles,465000
Adrienne,54,August,Nashville,345000
Kristen,51,February,Houston,285000
<end>Please transform the following csv data into yml:
Database Name,Queries per Second,Cache Hit Ratio (%),Connection Count,Average Latency (ms)
ProductsDB,513.59,86.95,219,55.34
ProductsDB,3794.47,85.24,493,49.53
UserDB,1425.99,93.71,374,17.73
ProfilesDB,4314.12,89.15,159,52.73
UserDB,3629.94,86.15,112,54.25
UserDB,1166.69,81.98,99,88.33
LogsDB,1425.99,90.91,99,5.89
AnalyticsDB,4817.6,87.55,29,55.34
<start>
- Average Latency (ms): 55.34
  Cache Hit Ratio (%): 86.95
  Connection Count: 219
  Database Name: ProductsDB
  Queries per Second: 513.59
- Average Latency (ms): 49.53
  Cache Hit Ratio (%): 85.24
  Connection Count: 493
  Database Name: ProductsDB
  Queries per Second: 3794.47
- Average Latency (ms): 17.73
  Cache Hit Ratio (%): 93.71
  Connection Count: 374
  Database Name: UserDB
  Queries per Second: 1425.99
- Average Latency (ms): 52.73
  Cache Hit Ratio (%): 89.15
  Connection Count: 159
  Database Name: ProfilesDB
  Queries per Second: 4314.12
- Average Latency (ms): 54.25
  Cache Hit Ratio (%): 86.15
  Connection Count: 112
  Database Name: UserDB
  Queries per Second: 3629.94
- Average Latency (ms): 88.33
  Cache Hit Ratio (%): 81.98
  Connection Count: 99
  Database Name: UserDB
  Queries per Second: 1166.69
- Average Latency (ms): 5.89
  Cache Hit Ratio (%): 90.91
  Connection Count: 99
  Database Name: LogsDB
  Queries per Second: 1425.99
- Average Latency (ms): 55.34
  Cache Hit Ratio (%): 87.55
  Connection Count: 29
  Database Name: AnalyticsDB
  Queries per Second: 4817.6
<end>Convert this csv to yaml:
Director,Release Year,Box Office Earnings (M)
Orin Shadowalker,2009,768.37
Mara Moonshadow,2011,341.28
Cade Firebrand,2003,83.17
Talon Blackthorn,1978,85.91
<start>
- Box Office Earnings (M): 768.37
  Director: Orin Shadowalker
  Release Year: 2009
- Box Office Earnings (M): 341.28
  Director: Mara Moonshadow
  Release Year: 2011
- Box Office Earnings (M): 83.17
  Director: Cade Firebrand
  Release Year: 2003
- Box Office Earnings (M): 85.91
  Director: Talon Blackthorn
  Release Year: 1978
<end>Transform this json structure to a yml format:
[
    {
        "Title": "A Journey Through Time",
        "Author": "Galen Starfire",
        "Genre": "Thriller",
        "Publication Year": 1996,
        "Rating": 4.9
    },
    {
        "Title": "A Journey Through Time",
        "Author": "Kara Firebrand",
        "Genre": "Science Fiction",
        "Publication Year": 1984,
        "Rating": 4.2
    },
    {
        "Title": "Shadows of Solitude",
        "Author": "Sylvia Nightshade",
        "Genre": "Science Fiction",
        "Publication Year": 1955,
        "Rating": 4.9
    },
    {
        "Title": "Legends of the Rift",
        "Author": "Sylvia Nightshade",
        "Genre": "Romance",
        "Publication Year": 2016,
        "Rating": 4.3
    },
    {
        "Title": "Legends of the Rift",
        "Author": "Luna Silverleaf",
        "Genre": "Science Fiction",
        "Publication Year": 1985,
        "Rating": 3.6
    },
    {
        "Title": "The Forgotten World",
        "Author": "Elara Moonshadow",
        "Genre": "Mystery",
        "Publication Year": 2010,
        "Rating": 3.0
    },
    {
        "Title": "Whispers of the Abyss",
        "Author": "Kara Firebrand",
        "Genre": "Horror",
        "Publication Year": 2000,
        "Rating": 1.5
    },
    {
        "Title": "Echoes of Eternity",
        "Author": "Draven Blackthorn",
        "Genre": "Historical",
        "Publication Year": 2000,
        "Rating": 4.4
    },
    {
        "Title": "The Crystal Key",
        "Author": "Luna Silverleaf",
        "Genre": "Fantasy",
        "Publication Year": 1995,
        "Rating": 2.6
    }
]<start>
- Author: Galen Starfire
  Genre: Thriller
  Publication Year: 1996
  Rating: 4.9
  Title: A Journey Through Time
- Author: Kara Firebrand
  Genre: Science Fiction
  Publication Year: 1984
  Rating: 4.2
  Title: A Journey Through Time
- Author: Sylvia Nightshade
  Genre: Science Fiction
  Publication Year: 1955
  Rating: 4.9
  Title: Shadows of Solitude
- Author: Sylvia Nightshade
  Genre: Romance
  Publication Year: 2016
  Rating: 4.3
  Title: Legends of the Rift
- Author: Luna Silverleaf
  Genre: Science Fiction
  Publication Year: 1985
  Rating: 3.6
  Title: Legends of the Rift
- Author: Elara Moonshadow
  Genre: Mystery
  Publication Year: 2010
  Rating: 3.0
  Title: The Forgotten World
- Author: Kara Firebrand
  Genre: Horror
  Publication Year: 2000
  Rating: 1.5
  Title: Whispers of the Abyss
- Author: Draven Blackthorn
  Genre: Historical
  Publication Year: 2000
  Rating: 4.4
  Title: Echoes of Eternity
- Author: Luna Silverleaf
  Genre: Fantasy
  Publication Year: 1995
  Rating: 2.6
  Title: The Crystal Key
<end>Please transform the following plain text data into yaml:
Title: The Silent Grove | Genre: Non-Fiction | Rating: 3.6
Title: Shadows of Solitude | Genre: Fantasy | Rating: 2.5
Title: Legends of the Rift | Genre: Science Fiction | Rating: 3.2
Title: A Journey Through Time | Genre: Science Fiction | Rating: 3.2
Title: Whispers of the Abyss | Genre: Science Fiction | Rating: 2.1
Title: The Crystal Key | Genre: Horror | Rating: 4.7
Title: The Crystal Key | Genre: Thriller | Rating: 3.6
Title: A Journey Through Time | Genre: Horror | Rating: 4.2
<start>
- Genre: Non-Fiction
  Rating: 3.6
  Title: The Silent Grove
- Genre: Fantasy
  Rating: 2.5
  Title: Shadows of Solitude
- Genre: Science Fiction
  Rating: 3.2
  Title: Legends of the Rift
- Genre: Science Fiction
  Rating: 3.2
  Title: A Journey Through Time
- Genre: Science Fiction
  Rating: 2.1
  Title: Whispers of the Abyss
- Genre: Horror
  Rating: 4.7
  Title: The Crystal Key
- Genre: Thriller
  Rating: 3.6
  Title: The Crystal Key
- Genre: Horror
  Rating: 4.2
  Title: A Journey Through Time
<end>Here's some Csv data, can you convert it to JSON?
Trip Name,End Location,Fuel Used (gallons)
Mountain Adventure,Phoenix,72.8
Forest Journey,Miami,28.5
Historic Route,Houston,35.1
Mountain Adventure,Los Angeles,43.5
Coast to Coast,Miami,7.3
Historic Route,Phoenix,11.4
<start>
[
    {
        "Trip Name": "Mountain Adventure",
        "End Location": "Phoenix",
        "Fuel Used (gallons)": 72.8
    },
    {
        "Trip Name": "Forest Journey",
        "End Location": "Miami",
        "Fuel Used (gallons)": 28.5
    },
    {
        "Trip Name": "Historic Route",
        "End Location": "Houston",
        "Fuel Used (gallons)": 35.1
    },
    {
        "Trip Name": "Mountain Adventure",
        "End Location": "Los Angeles",
        "Fuel Used (gallons)": 43.5
    },
    {
        "Trip Name": "Coast to Coast",
        "End Location": "Miami",
        "Fuel Used (gallons)": 7.3
    },
    {
        "Trip Name": "Historic Route",
        "End Location": "Phoenix",
        "Fuel Used (gallons)": 11.4
    }
]
<end>Convert this yml to Markdown:
- Average Latency (ms): 21.33
  Cache Hit Ratio (%): 73.72
  Connection Count: 367
  Database Name: UserDB
  Timestamp: '2023-03-05 00:26:10'
- Average Latency (ms): 89.63
  Cache Hit Ratio (%): 89.02
  Connection Count: 145
  Database Name: ProductsDB
  Timestamp: '2022-08-15 08:30:36'
- Average Latency (ms): 50.68
  Cache Hit Ratio (%): 92.12
  Connection Count: 473
  Database Name: AnalyticsDB
  Timestamp: '2021-02-23 07:09:29'
- Average Latency (ms): 60.96
  Cache Hit Ratio (%): 81.49
  Connection Count: 149
  Database Name: AnalyticsDB
  Timestamp: '2022-12-02 15:04:47'
- Average Latency (ms): 91.11
  Cache Hit Ratio (%): 89.02
  Connection Count: 236
  Database Name: ProductsDB
  Timestamp: '2023-02-01 19:36:29'
- Average Latency (ms): 67.32
  Cache Hit Ratio (%): 96.48
  Connection Count: 413
  Database Name: SessionsDB
  Timestamp: '2022-02-07 16:56:09'
- Average Latency (ms): 37.93
  Cache Hit Ratio (%): 96.1
  Connection Count: 299
  Database Name: ProductsDB
  Timestamp: '2023-01-22 02:10:42'
<start>
| Database Name | Cache Hit Ratio (%) | Connection Count | Average Latency (ms) | Timestamp |
| --- | --- | --- | --- | --- |
| UserDB | 73.72 | 367 | 21.33 | 2023-03-05 00:26:10 |
| ProductsDB | 89.02 | 145 | 89.63 | 2022-08-15 08:30:36 |
| AnalyticsDB | 92.12 | 473 | 50.68 | 2021-02-23 07:09:29 |
| AnalyticsDB | 81.49 | 149 | 60.96 | 2022-12-02 15:04:47 |
| ProductsDB | 89.02 | 236 | 91.11 | 2023-02-01 19:36:29 |
| SessionsDB | 96.48 | 413 | 67.32 | 2022-02-07 16:56:09 |
| ProductsDB | 96.1 | 299 | 37.93 | 2023-01-22 02:10:42 |
<end>Here's some plain text data, can you convert it to Json?
Date: 2021-01-27 | Close Price: 433.56 | High Price: 433.56 | Volume: 3296823
Date: 2010-07-15 | Close Price: 515.62 | High Price: 623.19 | Volume: 6189512
Date: 2014-10-07 | Close Price: 925.65 | High Price: 925.65 | Volume: 3529832
Date: 2023-12-15 | Close Price: 122.32 | High Price: 534.1 | Volume: 9473369
Date: 2019-05-11 | Close Price: 122.32 | High Price: 1250.91 | Volume: 6645865
<start>
[
    {
        "Date": "2021-01-27",
        "Close Price": 433.56,
        "High Price": 433.56,
        "Volume": 3296823
    },
    {
        "Date": "2010-07-15",
        "Close Price": 515.62,
        "High Price": 623.19,
        "Volume": 6189512
    },
    {
        "Date": "2014-10-07",
        "Close Price": 925.65,
        "High Price": 925.65,
        "Volume": 3529832
    },
    {
        "Date": "2023-12-15",
        "Close Price": 122.32,
        "High Price": 534.1,
        "Volume": 9473369
    },
    {
        "Date": "2019-05-11",
        "Close Price": 122.32,
        "High Price": 1250.91,
        "Volume": 6645865
    }
]
<end>Transform this PLAIN TEXT structure to a json format:
SKU: SKU-1013 | Stock Quantity: 56 | Category: Sports | Supplier Name: Globex
SKU: SKU-1084 | Stock Quantity: 113 | Category: Electronics | Supplier Name: ACME Corp
SKU: SKU-1073 | Stock Quantity: 168 | Category: Electronics | Supplier Name: Umbrella Corp
SKU: SKU-1005 | Stock Quantity: 216 | Category: Automotive | Supplier Name: Umbrella Corp
SKU: SKU-1092 | Stock Quantity: 438 | Category: Electronics | Supplier Name: Wonka Industries
SKU: SKU-1037 | Stock Quantity: 194 | Category: Toys | Supplier Name: Wonka Industries
SKU: SKU-1031 | Stock Quantity: 336 | Category: Toys | Supplier Name: Wonka Industries
<start>
[
    {
        "SKU": "SKU-1013",
        "Stock Quantity": 56,
        "Category": "Sports",
        "Supplier Name": "Globex"
    },
    {
        "SKU": "SKU-1084",
        "Stock Quantity": 113,
        "Category": "Electronics",
        "Supplier Name": "ACME Corp"
    },
    {
        "SKU": "SKU-1073",
        "Stock Quantity": 168,
        "Category": "Electronics",
        "Supplier Name": "Umbrella Corp"
    },
    {
        "SKU": "SKU-1005",
        "Stock Quantity": 216,
        "Category": "Automotive",
        "Supplier Name": "Umbrella Corp"
    },
    {
        "SKU": "SKU-1092",
        "Stock Quantity": 438,
        "Category": "Electronics",
        "Supplier Name": "Wonka Industries"
    },
    {
        "SKU": "SKU-1037",
        "Stock Quantity": 194,
        "Category": "Toys",
        "Supplier Name": "Wonka Industries"
    },
    {
        "SKU": "SKU-1031",
        "Stock Quantity": 336,
        "Category": "Toys",
        "Supplier Name": "Wonka Industries"
    }
]
<end>Can you change this Yml into plain text?
- Condition: Snowy
  Day: Wednesday
  Location: Los Angeles
- Condition: Sunny
  Day: Thursday
  Location: Chicago
- Condition: Cloudy
  Day: Wednesday
  Location: Los Angeles
- Condition: Windy
  Day: Thursday
  Location: Chicago
- Condition: Foggy
  Day: Sunday
  Location: New York
- Condition: Sunny
  Day: Sunday
  Location: Houston
- Condition: Cloudy
  Day: Thursday
  Location: Seattle
<start>
Location: Los Angeles | Condition: Snowy | Day: Wednesday
Location: Chicago | Condition: Sunny | Day: Thursday
Location: Los Angeles | Condition: Cloudy | Day: Wednesday
Location: Chicago | Condition: Windy | Day: Thursday
Location: New York | Condition: Foggy | Day: Sunday
Location: Houston | Condition: Sunny | Day: Sunday
Location: Seattle | Condition: Cloudy | Day: Thursday
<end>Convert this JSON to markdown:
[
    {
        "Device Type": "Pressure Sensor",
        "Location": "Garage",
        "Battery Level (%)": 78.6,
        "Reading Value": 71.62
    },
    {
        "Device Type": "Motion Detector",
        "Location": "Garden",
        "Battery Level (%)": 11.8,
        "Reading Value": -19.7
    },
    {
        "Device Type": "Pressure Sensor",
        "Location": "Garden",
        "Battery Level (%)": 99.9,
        "Reading Value": 20.99
    },
    {
        "Device Type": "Motion Detector",
        "Location": "Garden",
        "Battery Level (%)": 91.6,
        "Reading Value": 3.97
    }
]<start>
| Device Type | Location | Battery Level (%) | Reading Value |
| --- | --- | --- | --- |
| Pressure Sensor | Garage | 78.6 | 71.62 |
| Motion Detector | Garden | 11.8 | -19.7 |
| Pressure Sensor | Garden | 99.9 | 20.99 |
| Motion Detector | Garden | 91.6 | 3.97 |
<end>Convert this markdown to yml:
| Device ID | Device Type | Location | Battery Level (%) | Reading Value | Timestamp |
| --- | --- | --- | --- | --- | --- |
| device-0094 | Humidity Sensor | Hallway | 41.5 | 11.3 | 2022-05-04 13:42:19 |
| device-0086 | Motion Detector | Office | 28.2 | 57.0 | 2023-10-18 03:09:22 |
| device-0073 | Humidity Sensor | Garden | 88.5 | 27.36 | 2021-09-02 11:44:18 |
| device-0006 | Temperature Sensor | Bathroom | 26.0 | -3.84 | 2023-08-06 02:27:12 |
| device-0079 | Pressure Sensor | Garage | 51.3 | -37.77 | 2021-05-17 09:04:42 |
| device-0020 | Temperature Sensor | Living Room | 73.0 | 13.44 | 2022-03-14 21:12:00 |
| device-0039 | Motion Detector | Office | 72.2 | 64.94 | 2023-10-24 15:16:20 |
| device-0092 | Pressure Sensor | Garage | 95.0 | 1.97 | 2021-08-06 08:06:08 |
| device-0054 | Humidity Sensor | Kitchen | 88.1 | -11.05 | 2023-07-27 12:46:38 |
| device-0098 | Humidity Sensor | Bedroom | 80.1 | 20.44 | 2021-11-26 11:57:30 |<start>
- Battery Level (%): 41.5
  Device ID: device-0094
  Device Type: Humidity Sensor
  Location: Hallway
  Reading Value: 11.3
  Timestamp: '2022-05-04 13:42:19'
- Battery Level (%): 28.2
  Device ID: device-0086
  Device Type: Motion Detector
  Location: Office
  Reading Value: 57.0
  Timestamp: '2023-10-18 03:09:22'
- Battery Level (%): 88.5
  Device ID: device-0073
  Device Type: Humidity Sensor
  Location: Garden
  Reading Value: 27.36
  Timestamp: '2021-09-02 11:44:18'
- Battery Level (%): 26.0
  Device ID: device-0006
  Device Type: Temperature Sensor
  Location: Bathroom
  Reading Value: -3.84
  Timestamp: '2023-08-06 02:27:12'
- Battery Level (%): 51.3
  Device ID: device-0079
  Device Type: Pressure Sensor
  Location: Garage
  Reading Value: -37.77
  Timestamp: '2021-05-17 09:04:42'
- Battery Level (%): 73.0
  Device ID: device-0020
  Device Type: Temperature Sensor
  Location: Living Room
  Reading Value: 13.44
  Timestamp: '2022-03-14 21:12:00'
- Battery Level (%): 72.2
  Device ID: device-0039
  Device Type: Motion Detector
  Location: Office
  Reading Value: 64.94
  Timestamp: '2023-10-24 15:16:20'
- Battery Level (%): 95.0
  Device ID: device-0092
  Device Type: Pressure Sensor
  Location: Garage
  Reading Value: 1.97
  Timestamp: '2021-08-06 08:06:08'
- Battery Level (%): 88.1
  Device ID: device-0054
  Device Type: Humidity Sensor
  Location: Kitchen
  Reading Value: -11.05
  Timestamp: '2023-07-27 12:46:38'
- Battery Level (%): 80.1
  Device ID: device-0098
  Device Type: Humidity Sensor
  Location: Bedroom
  Reading Value: 20.44
  Timestamp: '2021-11-26 11:57:30'
<end>Here's some JSON data, can you convert it to yml?
[
    {
        "Company": "AeroSpace",
        "Sector": "Automotive",
        "Stock Price": 873.55,
        "Annual Revenue (B)": 229.02
    },
    {
        "Company": "HealthPlus",
        "Sector": "Aerospace",
        "Stock Price": 990.04,
        "Annual Revenue (B)": 234.92
    },
    {
        "Company": "BioPharm",
        "Sector": "Finance",
        "Stock Price": 750.46,
        "Annual Revenue (B)": 222.99
    },
    {
        "Company": "BioPharm",
        "Sector": "Aerospace",
        "Stock Price": 525.26,
        "Annual Revenue (B)": 342.31
    },
    {
        "Company": "GlobalTrade",
        "Sector": "Retail",
        "Stock Price": 178.42,
        "Annual Revenue (B)": 342.31
    },
    {
        "Company": "BioPharm",
        "Sector": "Biotech",
        "Stock Price": 84.22,
        "Annual Revenue (B)": 52.85
    }
]<start>
- Annual Revenue (B): 229.02
  Company: AeroSpace
  Sector: Automotive
  Stock Price: 873.55
- Annual Revenue (B): 234.92
  Company: HealthPlus
  Sector: Aerospace
  Stock Price: 990.04
- Annual Revenue (B): 222.99
  Company: BioPharm
  Sector: Finance
  Stock Price: 750.46
- Annual Revenue (B): 342.31
  Company: BioPharm
  Sector: Aerospace
  Stock Price: 525.26
- Annual Revenue (B): 342.31
  Company: GlobalTrade
  Sector: Retail
  Stock Price: 178.42
- Annual Revenue (B): 52.85
  Company: BioPharm
  Sector: Biotech
  Stock Price: 84.22
<end>Here's some Yaml data, can you convert it to csv?
- Cache Hit Ratio (%): 80.2
  Connection Count: 22
  Timestamp: '2021-12-19 02:57:57'
- Cache Hit Ratio (%): 73.08
  Connection Count: 325
  Timestamp: '2022-04-18 19:27:47'
- Cache Hit Ratio (%): 84.93
  Connection Count: 130
  Timestamp: '2021-02-07 10:09:50'
- Cache Hit Ratio (%): 94.37
  Connection Count: 181
  Timestamp: '2021-08-26 14:14:16'
- Cache Hit Ratio (%): 80.2
  Connection Count: 408
  Timestamp: '2021-12-07 11:25:47'
- Cache Hit Ratio (%): 90.86
  Connection Count: 258
  Timestamp: '2023-07-17 13:03:29'
- Cache Hit Ratio (%): 95.75
  Connection Count: 423
  Timestamp: '2022-09-19 01:37:19'
- Cache Hit Ratio (%): 91.67
  Connection Count: 359
  Timestamp: '2022-05-12 16:59:34'
<start>
Cache Hit Ratio (%),Connection Count,Timestamp
80.2,22,2021-12-19 02:57:57
73.08,325,2022-04-18 19:27:47
84.93,130,2021-02-07 10:09:50
94.37,181,2021-08-26 14:14:16
80.2,408,2021-12-07 11:25:47
90.86,258,2023-07-17 13:03:29
95.75,423,2022-09-19 01:37:19
91.67,359,2022-05-12 16:59:34
<end>Can you change this yaml into csv?
- Distance (miles): 2147.6
  Duration (hours): 51.8
  End Location: Chicago
  Fuel Used (gallons): 24.5
  Start Location: Denver
  Trip Name: City Explorer
- Distance (miles): 1038.2
  Duration (hours): 1.6
  End Location: San Francisco
  Fuel Used (gallons): 63.0
  Start Location: New York
  Trip Name: Forest Journey
- Distance (miles): 2599.8
  Duration (hours): 34.3
  End Location: Houston
  Fuel Used (gallons): 7.3
  Start Location: Denver
  Trip Name: Lakeside Retreat
- Distance (miles): 814.6
  Duration (hours): 44.2
  End Location: Chicago
  Fuel Used (gallons): 86.3
  Start Location: Denver
  Trip Name: Coast to Coast
<start>
Trip Name,Start Location,End Location,Distance (miles),Duration (hours),Fuel Used (gallons)
City Explorer,Denver,Chicago,2147.6,51.8,24.5
Forest Journey,New York,San Francisco,1038.2,1.6,63.0
Lakeside Retreat,Denver,Houston,2599.8,34.3,7.3
Coast to Coast,Denver,Chicago,814.6,44.2,86.3
<end>Here's some Csv data, can you convert it to MARKDOWN?
Company,Date,Open Price,High Price,Low Price
RetailWorld,2017-07-26,1107.24,1232.93,476.89
HealthGen,2016-12-22,300.16,1138.36,300.16
AeroSystems,2010-12-07,287.8,390.99,287.8
MediaGroup,2023-11-20,633.58,1232.93,152.69
<start>
| Company | Date | Open Price | High Price | Low Price |
| --- | --- | --- | --- | --- |
| RetailWorld | 2017-07-26 | 1107.24 | 1232.93 | 476.89 |
| HealthGen | 2016-12-22 | 300.16 | 1138.36 | 300.16 |
| AeroSystems | 2010-12-07 | 287.8 | 390.99 | 287.8 |
| MediaGroup | 2023-11-20 | 633.58 | 1232.93 | 152.69 |
<end>Here's some csv data, can you convert it to Plain text?
Title,Author,Genre,Publication Year,Rating
Legends of the Rift,Sylvia Nightshade,Horror,1970,4.3
Legends of the Rift,Rowan Ashborne,Science Fiction,2003,4.2
The Crystal Key,Sylvia Nightshade,Mystery,1951,3.0
Tales of the Brave,Sylvia Nightshade,Thriller,2006,3.9
The Silent Grove,Galen Starfire,Horror,2012,3.6
<start>
Title: Legends of the Rift | Author: Sylvia Nightshade | Genre: Horror | Publication Year: 1970 | Rating: 4.3
Title: Legends of the Rift | Author: Rowan Ashborne | Genre: Science Fiction | Publication Year: 2003 | Rating: 4.2
Title: The Crystal Key | Author: Sylvia Nightshade | Genre: Mystery | Publication Year: 1951 | Rating: 3.0
Title: Tales of the Brave | Author: Sylvia Nightshade | Genre: Thriller | Publication Year: 2006 | Rating: 3.9
Title: The Silent Grove | Author: Galen Starfire | Genre: Horror | Publication Year: 2012 | Rating: 3.6
<end>Transform this JSON structure to a markdown format:
[
    {
        "Product Name": "Doohickey",
        "SKU": "SKU-1049",
        "Price": 291.16,
        "Stock Quantity": 217
    },
    {
        "Product Name": "Doohickey",
        "SKU": "SKU-1064",
        "Price": 256.99,
        "Stock Quantity": 137
    },
    {
        "Product Name": "Instrument",
        "SKU": "SKU-1035",
        "Price": 268.34,
        "Stock Quantity": 308
    },
    {
        "Product Name": "Gadget",
        "SKU": "SKU-1090",
        "Price": 27.95,
        "Stock Quantity": 117
    },
    {
        "Product Name": "Doohickey",
        "SKU": "SKU-1007",
        "Price": 261.11,
        "Stock Quantity": 291
    },
    {
        "Product Name": "Instrument",
        "SKU": "SKU-1068",
        "Price": 277.56,
        "Stock Quantity": 180
    },
    {
        "Product Name": "Doohickey",
        "SKU": "SKU-1083",
        "Price": 249.9,
        "Stock Quantity": 446
    }
]<start>
| Product Name | SKU | Price | Stock Quantity |
| --- | --- | --- | --- |
| Doohickey | SKU-1049 | 291.16 | 217 |
| Doohickey | SKU-1064 | 256.99 | 137 |
| Instrument | SKU-1035 | 268.34 | 308 |
| Gadget | SKU-1090 | 27.95 | 117 |
| Doohickey | SKU-1007 | 261.11 | 291 |
| Instrument | SKU-1068 | 277.56 | 180 |
| Doohickey | SKU-1083 | 249.9 | 446 |
<end>Please transform the following Json data into PLAIN TEXT:
[
    {
        "Sector": "Finance",
        "Market Cap": "Mega Cap",
        "Stock Price": 753.41,
        "Annual Revenue (B)": 404.25
    },
    {
        "Sector": "Retail",
        "Market Cap": "Large Cap",
        "Stock Price": 441.58,
        "Annual Revenue (B)": 129.16
    },
    {
        "Sector": "Automotive",
        "Market Cap": "Small Cap",
        "Stock Price": 165.88,
        "Annual Revenue (B)": 214.9
    },
    {
        "Sector": "Retail",
        "Market Cap": "Large Cap",
        "Stock Price": 481.51,
        "Annual Revenue (B)": 194.91
    },
    {
        "Sector": "Healthcare",
        "Market Cap": "Small Cap",
        "Stock Price": 243.65,
        "Annual Revenue (B)": 300.75
    },
    {
        "Sector": "Biotech",
        "Market Cap": "Mega Cap",
        "Stock Price": 592.58,
        "Annual Revenue (B)": 81.58
    }
]<start>
Sector: Finance | Market Cap: Mega Cap | Stock Price: 753.41 | Annual Revenue (B): 404.25
Sector: Retail | Market Cap: Large Cap | Stock Price: 441.58 | Annual Revenue (B): 129.16
Sector: Automotive | Market Cap: Small Cap | Stock Price: 165.88 | Annual Revenue (B): 214.9
Sector: Retail | Market Cap: Large Cap | Stock Price: 481.51 | Annual Revenue (B): 194.91
Sector: Healthcare | Market Cap: Small Cap | Stock Price: 243.65 | Annual Revenue (B): 300.75
Sector: Biotech | Market Cap: Mega Cap | Stock Price: 592.58 | Annual Revenue (B): 81.58
<end>Transform this json structure to a yaml format:
[
    {
        "Company": "TechCorp",
        "Sector": "Automotive",
        "Market Cap": "Mega Cap",
        "Stock Price": 662.05,
        "Annual Revenue (B)": 112.28,
        "Quarter": "Q1"
    },
    {
        "Company": "Foodies",
        "Sector": "Energy",
        "Market Cap": "Large Cap",
        "Stock Price": 540.86,
        "Annual Revenue (B)": 364.18,
        "Quarter": "Q2"
    },
    {
        "Company": "Foodies",
        "Sector": "Biotech",
        "Market Cap": "Small Cap",
        "Stock Price": 455.47,
        "Annual Revenue (B)": 113.8,
        "Quarter": "Q3"
    },
    {
        "Company": "RetailHub",
        "Sector": "Automotive",
        "Market Cap": "Mid Cap",
        "Stock Price": 283.96,
        "Annual Revenue (B)": 92.2,
        "Quarter": "Q4"
    },
    {
        "Company": "AeroSpace",
        "Sector": "Healthcare",
        "Market Cap": "Mid Cap",
        "Stock Price": 596.1,
        "Annual Revenue (B)": 121.93,
        "Quarter": "Q3"
    },
    {
        "Company": "GlobalTrade",
        "Sector": "Energy",
        "Market Cap": "Small Cap",
        "Stock Price": 376.43,
        "Annual Revenue (B)": 289.44,
        "Quarter": "Q1"
    },
    {
        "Company": "HealthPlus",
        "Sector": "Technology",
        "Market Cap": "Large Cap",
        "Stock Price": 88.26,
        "Annual Revenue (B)": 370.8,
        "Quarter": "Q1"
    },
    {
        "Company": "EcoEnergy",
        "Sector": "Technology",
        "Market Cap": "Small Cap",
        "Stock Price": 188.1,
        "Annual Revenue (B)": 122.71,
        "Quarter": "Q3"
    },
    {
        "Company": "GlobalTrade",
        "Sector": "Retail",
        "Market Cap": "Large Cap",
        "Stock Price": 253.52,
        "Annual Revenue (B)": 92.2,
        "Quarter": "Q1"
    },
    {
        "Company": "AeroSpace",
        "Sector": "Aerospace",
        "Market Cap": "Large Cap",
        "Stock Price": 666.79,
        "Annual Revenue (B)": 174.48,
        "Quarter": "Q1"
    }
]<start>
- Annual Revenue (B): 112.28
  Company: TechCorp
  Market Cap: Mega Cap
  Quarter: Q1
  Sector: Automotive
  Stock Price: 662.05
- Annual Revenue (B): 364.18
  Company: Foodies
  Market Cap: Large Cap
  Quarter: Q2
  Sector: Energy
  Stock Price: 540.86
- Annual Revenue (B): 113.8
  Company: Foodies
  Market Cap: Small Cap
  Quarter: Q3
  Sector: Biotech
  Stock Price: 455.47
- Annual Revenue (B): 92.2
  Company: RetailHub
  Market Cap: Mid Cap
  Quarter: Q4
  Sector: Automotive
  Stock Price: 283.96
- Annual Revenue (B): 121.93
  Company: AeroSpace
  Market Cap: Mid Cap
  Quarter: Q3
  Sector: Healthcare
  Stock Price: 596.1
- Annual Revenue (B): 289.44
  Company: GlobalTrade
  Market Cap: Small Cap
  Quarter: Q1
  Sector: Energy
  Stock Price: 376.43
- Annual Revenue (B): 370.8
  Company: HealthPlus
  Market Cap: Large Cap
  Quarter: Q1
  Sector: Technology
  Stock Price: 88.26
- Annual Revenue (B): 122.71
  Company: EcoEnergy
  Market Cap: Small Cap
  Quarter: Q3
  Sector: Technology
  Stock Price: 188.1
- Annual Revenue (B): 92.2
  Company: GlobalTrade
  Market Cap: Large Cap
  Quarter: Q1
  Sector: Retail
  Stock Price: 253.52
- Annual Revenue (B): 174.48
  Company: AeroSpace
  Market Cap: Large Cap
  Quarter: Q1
  Sector: Aerospace
  Stock Price: 666.79
<end>Please transform the following Csv data into Markdown:
Product Name,SKU,Price
Whatchamacallit,SKU-1027,492.07
Instrument,SKU-1043,95.32
Apparatus,SKU-1080,247.41
Whatchamacallit,SKU-1004,150.54
Doohickey,SKU-1029,153.38
Whatchamacallit,SKU-1098,235.1
Widget,SKU-1020,141.87
Apparatus,SKU-1085,424.55
Doohickey,SKU-1022,18.42
<start>
| Product Name | SKU | Price |
| --- | --- | --- |
| Whatchamacallit | SKU-1027 | 492.07 |
| Instrument | SKU-1043 | 95.32 |
| Apparatus | SKU-1080 | 247.41 |
| Whatchamacallit | SKU-1004 | 150.54 |
| Doohickey | SKU-1029 | 153.38 |
| Whatchamacallit | SKU-1098 | 235.1 |
| Widget | SKU-1020 | 141.87 |
| Apparatus | SKU-1085 | 424.55 |
| Doohickey | SKU-1022 | 18.42 |
<end>Convert this CSV to markdown:
Company,Date,Open Price,Close Price,High Price,Volume
AeroSystems,2012-03-28,266.4,576.31,811.5,245639
GreenEnergy,2011-10-07,1014.53,1215.91,1245.92,3764094
AeroSystems,2018-01-03,921.33,314.22,1245.92,3570870
GreenEnergy,2019-10-23,908.3,811.5,908.3,6536103
BioLife,2012-12-23,569.52,1294.74,1294.74,7168667
AutoMotive,2022-01-10,495.93,1058.33,1058.33,1081236
RetailWorld,2011-08-26,116.94,829.27,829.27,8449343
GreenEnergy,2010-03-23,1215.91,569.52,1215.91,9616414
TechnoCorp,2015-03-15,737.55,209.77,820.04,5403992
FinanceTrust,2017-08-27,976.2,908.37,976.2,3764094
<start>
| Company | Date | Open Price | Close Price | High Price | Volume |
| --- | --- | --- | --- | --- | --- |
| AeroSystems | 2012-03-28 | 266.4 | 576.31 | 811.5 | 245639 |
| GreenEnergy | 2011-10-07 | 1014.53 | 1215.91 | 1245.92 | 3764094 |
| AeroSystems | 2018-01-03 | 921.33 | 314.22 | 1245.92 | 3570870 |
| GreenEnergy | 2019-10-23 | 908.3 | 811.5 | 908.3 | 6536103 |
| BioLife | 2012-12-23 | 569.52 | 1294.74 | 1294.74 | 7168667 |
| AutoMotive | 2022-01-10 | 495.93 | 1058.33 | 1058.33 | 1081236 |
| RetailWorld | 2011-08-26 | 116.94 | 829.27 | 829.27 | 8449343 |
| GreenEnergy | 2010-03-23 | 1215.91 | 569.52 | 1215.91 | 9616414 |
| TechnoCorp | 2015-03-15 | 737.55 | 209.77 | 820.04 | 5403992 |
| FinanceTrust | 2017-08-27 | 976.2 | 908.37 | 976.2 | 3764094 |
<end>Here's some markdown data, can you convert it to plain text?
| Start Location | End Location | Distance (miles) | Duration (hours) | Fuel Used (gallons) |
| --- | --- | --- | --- | --- |
| New York | San Francisco | 777.4 | 45.8 | 31.5 |
| Houston | Phoenix | 2240.6 | 57.0 | 11.5 |
| Los Angeles | Houston | 2641.3 | 41.7 | 33.3 |
| Phoenix | Denver | 1440.9 | 64.1 | 16.3 |
| Houston | San Francisco | 918.3 | 51.7 | 29.2 |
| Phoenix | Houston | 1552.3 | 2.5 | 50.4 |
| New York | Houston | 538.5 | 60.2 | 67.4 |<start>
Start Location: New York | End Location: San Francisco | Distance (miles): 777.4 | Duration (hours): 45.8 | Fuel Used (gallons): 31.5
Start Location: Houston | End Location: Phoenix | Distance (miles): 2240.6 | Duration (hours): 57.0 | Fuel Used (gallons): 11.5
Start Location: Los Angeles | End Location: Houston | Distance (miles): 2641.3 | Duration (hours): 41.7 | Fuel Used (gallons): 33.3
Start Location: Phoenix | End Location: Denver | Distance (miles): 1440.9 | Duration (hours): 64.1 | Fuel Used (gallons): 16.3
Start Location: Houston | End Location: San Francisco | Distance (miles): 918.3 | Duration (hours): 51.7 | Fuel Used (gallons): 29.2
Start Location: Phoenix | End Location: Houston | Distance (miles): 1552.3 | Duration (hours): 2.5 | Fuel Used (gallons): 50.4
Start Location: New York | End Location: Houston | Distance (miles): 538.5 | Duration (hours): 60.2 | Fuel Used (gallons): 67.4
<end>Please transform the following YML data into markdown:
- Box Office Earnings (M): 298.2
  Genre: Action
  Release Year: 2006
- Box Office Earnings (M): 390.19
  Genre: Drama
  Release Year: 1994
- Box Office Earnings (M): 618.57
  Genre: Thriller
  Release Year: 2006
- Box Office Earnings (M): 945.01
  Genre: Sci-Fi
  Release Year: 1989
- Box Office Earnings (M): 675.67
  Genre: Fantasy
  Release Year: 1973
- Box Office Earnings (M): 533.78
  Genre: Thriller
  Release Year: 1983
- Box Office Earnings (M): 195.69
  Genre: Horror
  Release Year: 2019
- Box Office Earnings (M): 845.18
  Genre: Thriller
  Release Year: 1984
- Box Office Earnings (M): 631.76
  Genre: Horror
  Release Year: 1974
<start>
| Genre | Release Year | Box Office Earnings (M) |
| --- | --- | --- |
| Action | 2006 | 298.2 |
| Drama | 1994 | 390.19 |
| Thriller | 2006 | 618.57 |
| Sci-Fi | 1989 | 945.01 |
| Fantasy | 1973 | 675.67 |
| Thriller | 1983 | 533.78 |
| Horror | 2019 | 195.69 |
| Thriller | 1984 | 845.18 |
| Horror | 1974 | 631.76 |
<end>Convert this MARKDOWN to plain text:
| Product Name | Price | Stock Quantity | Category | Supplier Name |
| --- | --- | --- | --- | --- |
| Device | 90.46 | 450 | Household | Umbrella Corp |
| Instrument | 76.81 | 362 | Electronics | Wayne Enterprises |
| Contraption | 458.82 | 167 | Sports | Umbrella Corp |
| Instrument | 117.27 | 349 | Household | Globex |
| Device | 268.08 | 441 | Electronics | Wayne Enterprises |
| Widget | 206.35 | 441 | Household | ACME Corp |
| Device | 88.53 | 115 | Toys | Wonka Industries |
| Gadget | 368.32 | 164 | Automotive | Globex |<start>
Product Name: Device | Price: 90.46 | Stock Quantity: 450 | Category: Household | Supplier Name: Umbrella Corp
Product Name: Instrument | Price: 76.81 | Stock Quantity: 362 | Category: Electronics | Supplier Name: Wayne Enterprises
Product Name: Contraption | Price: 458.82 | Stock Quantity: 167 | Category: Sports | Supplier Name: Umbrella Corp
Product Name: Instrument | Price: 117.27 | Stock Quantity: 349 | Category: Household | Supplier Name: Globex
Product Name: Device | Price: 268.08 | Stock Quantity: 441 | Category: Electronics | Supplier Name: Wayne Enterprises
Product Name: Widget | Price: 206.35 | Stock Quantity: 441 | Category: Household | Supplier Name: ACME Corp
Product Name: Device | Price: 88.53 | Stock Quantity: 115 | Category: Toys | Supplier Name: Wonka Industries
Product Name: Gadget | Price: 368.32 | Stock Quantity: 164 | Category: Automotive | Supplier Name: Globex
<end>Transform this plain text structure to a JSON format:
Device ID: device-0029 | Device Type: Temperature Sensor | Location: Garden | Battery Level (%): 36.8 | Reading Value: 13.2
Device ID: device-0047 | Device Type: Pressure Sensor | Location: Hallway | Battery Level (%): 28.7 | Reading Value: 9.54
Device ID: device-0057 | Device Type: Temperature Sensor | Location: Office | Battery Level (%): 91.3 | Reading Value: 12.13
Device ID: device-0068 | Device Type: Humidity Sensor | Location: Office | Battery Level (%): 71.3 | Reading Value: -28.15
Device ID: device-0099 | Device Type: Temperature Sensor | Location: Bathroom | Battery Level (%): 30.7 | Reading Value: -11.84
<start>
[
    {
        "Device ID": "device-0029",
        "Device Type": "Temperature Sensor",
        "Location": "Garden",
        "Battery Level (%)": 36.8,
        "Reading Value": 13.2
    },
    {
        "Device ID": "device-0047",
        "Device Type": "Pressure Sensor",
        "Location": "Hallway",
        "Battery Level (%)": 28.7,
        "Reading Value": 9.54
    },
    {
        "Device ID": "device-0057",
        "Device Type": "Temperature Sensor",
        "Location": "Office",
        "Battery Level (%)": 91.3,
        "Reading Value": 12.13
    },
    {
        "Device ID": "device-0068",
        "Device Type": "Humidity Sensor",
        "Location": "Office",
        "Battery Level (%)": 71.3,
        "Reading Value": -28.15
    },
    {
        "Device ID": "device-0099",
        "Device Type": "Temperature Sensor",
        "Location": "Bathroom",
        "Battery Level (%)": 30.7,
        "Reading Value": -11.84
    }
]
<end>Transform this markdown structure to a YML format:
| Trip Name | Start Location | End Location | Distance (miles) | Duration (hours) | Fuel Used (gallons) |
| --- | --- | --- | --- | --- | --- |
| Highway Odyssey | Denver | Chicago | 487.9 | 3.4 | 41.5 |
| Coast to Coast | San Francisco | Los Angeles | 890.9 | 55.1 | 85.1 |
| City Explorer | Los Angeles | Denver | 684.4 | 31.2 | 64.5 |
| Mountain Adventure | San Francisco | Phoenix | 1614.2 | 15.8 | 50.0 |
| Forest Journey | Los Angeles | Chicago | 763.9 | 32.4 | 74.1 |<start>
- Distance (miles): 487.9
  Duration (hours): 3.4
  End Location: Chicago
  Fuel Used (gallons): 41.5
  Start Location: Denver
  Trip Name: Highway Odyssey
- Distance (miles): 890.9
  Duration (hours): 55.1
  End Location: Los Angeles
  Fuel Used (gallons): 85.1
  Start Location: San Francisco
  Trip Name: Coast to Coast
- Distance (miles): 684.4
  Duration (hours): 31.2
  End Location: Denver
  Fuel Used (gallons): 64.5
  Start Location: Los Angeles
  Trip Name: City Explorer
- Distance (miles): 1614.2
  Duration (hours): 15.8
  End Location: Phoenix
  Fuel Used (gallons): 50.0
  Start Location: San Francisco
  Trip Name: Mountain Adventure
- Distance (miles): 763.9
  Duration (hours): 32.4
  End Location: Chicago
  Fuel Used (gallons): 74.1
  Start Location: Los Angeles
  Trip Name: Forest Journey
<end>Here's some plain text data, can you convert it to YAML?
Director: Talon Blackthorn | Genre: Comedy
Director: Mara Moonshadow | Genre: Thriller
Director: Lira Silverleaf | Genre: Action
Director: Aria Ravenwood | Genre: Thriller
Director: Mara Moonshadow | Genre: Drama
Director: Aria Ravenwood | Genre: Sci-Fi
<start>
- Director: Talon Blackthorn
  Genre: Comedy
- Director: Mara Moonshadow
  Genre: Thriller
- Director: Lira Silverleaf
  Genre: Action
- Director: Aria Ravenwood
  Genre: Thriller
- Director: Mara Moonshadow
  Genre: Drama
- Director: Aria Ravenwood
  Genre: Sci-Fi
<end>Transform this Markdown structure to a csv format:
| Title | Director | Genre |
| --- | --- | --- |
| Starbound Odyssey | Zara Stormrider | Drama |
| Rise of the Titans | Mara Moonshadow | Horror |
| The Endless Horizon | Lira Silverleaf | Horror |
| Mystery of the Depths | Lira Silverleaf | Adventure |
| Beyond the Veil | Talon Blackthorn | Horror |<start>
Title,Director,Genre
Starbound Odyssey,Zara Stormrider,Drama
Rise of the Titans,Mara Moonshadow,Horror
The Endless Horizon,Lira Silverleaf,Horror
Mystery of the Depths,Lira Silverleaf,Adventure
Beyond the Veil,Talon Blackthorn,Horror
<end>Can you change this CSV into PLAIN TEXT?
Director,Genre,Release Year,Box Office Earnings (M)
Rylan Frostblade,Sci-Fi,2023,412.2
Cade Firebrand,Horror,2004,446.44
Talon Blackthorn,Action,1975,798.64
Talon Blackthorn,Thriller,2001,776.09
Lira Silverleaf,Horror,2005,211.87
Zara Stormrider,Drama,1981,73.22
<start>
Director: Rylan Frostblade | Genre: Sci-Fi | Release Year: 2023 | Box Office Earnings (M): 412.2
Director: Cade Firebrand | Genre: Horror | Release Year: 2004 | Box Office Earnings (M): 446.44
Director: Talon Blackthorn | Genre: Action | Release Year: 1975 | Box Office Earnings (M): 798.64
Director: Talon Blackthorn | Genre: Thriller | Release Year: 2001 | Box Office Earnings (M): 776.09
Director: Lira Silverleaf | Genre: Horror | Release Year: 2005 | Box Office Earnings (M): 211.87
Director: Zara Stormrider | Genre: Drama | Release Year: 1981 | Box Office Earnings (M): 73.22
<end>Transform this CSV structure to a JSON format:
Company,Market Cap,Quarter
AeroSpace,Small Cap,Q4
GlobalTrade,Mega Cap,Q3
TechCorp,Mid Cap,Q2
<start>
[
    {
        "Company": "AeroSpace",
        "Market Cap": "Small Cap",
        "Quarter": "Q4"
    },
    {
        "Company": "GlobalTrade",
        "Market Cap": "Mega Cap",
        "Quarter": "Q3"
    },
    {
        "Company": "TechCorp",
        "Market Cap": "Mid Cap",
        "Quarter": "Q2"
    }
]
<end>Can you change this Yaml into markdown?
- Box Office Earnings (M): 363.19
  Director: Zara Stormrider
  Genre: Drama
  Release Year: 1982
  Title: Edge of Infinity
- Box Office Earnings (M): 750.17
  Director: Zara Stormrider
  Genre: Drama
  Release Year: 2016
  Title: Rise of the Titans
- Box Office Earnings (M): 148.13
  Director: Mara Moonshadow
  Genre: Drama
  Release Year: 2020
  Title: Edge of Infinity
- Box Office Earnings (M): 322.25
  Director: Orin Shadowalker
  Genre: Sci-Fi
  Release Year: 1995
  Title: Mystery of the Depths
- Box Office Earnings (M): 330.47
  Director: Cade Firebrand
  Genre: Fantasy
  Release Year: 1981
  Title: Rise of the Titans
<start>
| Title | Director | Genre | Release Year | Box Office Earnings (M) |
| --- | --- | --- | --- | --- |
| Edge of Infinity | Zara Stormrider | Drama | 1982 | 363.19 |
| Rise of the Titans | Zara Stormrider | Drama | 2016 | 750.17 |
| Edge of Infinity | Mara Moonshadow | Drama | 2020 | 148.13 |
| Mystery of the Depths | Orin Shadowalker | Sci-Fi | 1995 | 322.25 |
| Rise of the Titans | Cade Firebrand | Fantasy | 1981 | 330.47 |
<end>Can you change this csv into MARKDOWN?
Trip Name,Start Location,End Location,Duration (hours),Fuel Used (gallons)
Mountain Adventure,San Francisco,Phoenix,44.9,97.2
Coast to Coast,Denver,Chicago,11.7,70.0
Mountain Adventure,San Francisco,Phoenix,43.9,59.6
Desert Drive,Phoenix,Los Angeles,45.1,34.2
Canyon Trek,Houston,San Francisco,57.8,66.6
Forest Journey,Houston,Denver,11.7,47.1
<start>
| Trip Name | Start Location | End Location | Duration (hours) | Fuel Used (gallons) |
| --- | --- | --- | --- | --- |
| Mountain Adventure | San Francisco | Phoenix | 44.9 | 97.2 |
| Coast to Coast | Denver | Chicago | 11.7 | 70.0 |
| Mountain Adventure | San Francisco | Phoenix | 43.9 | 59.6 |
| Desert Drive | Phoenix | Los Angeles | 45.1 | 34.2 |
| Canyon Trek | Houston | San Francisco | 57.8 | 66.6 |
| Forest Journey | Houston | Denver | 11.7 | 47.1 |
<end>Please transform the following Yml data into plain text:
- Genre: Romance
  Publication Year: 2022
  Rating: 1.5
  Title: Shadows of Solitude
- Genre: Non-Fiction
  Publication Year: 1952
  Rating: 1.9
  Title: Echoes of Eternity
- Genre: Romance
  Publication Year: 1987
  Rating: 4.5
  Title: Whispers of the Abyss
- Genre: Fantasy
  Publication Year: 1950
  Rating: 2.6
  Title: The Crystal Key
<start>
Title: Shadows of Solitude | Genre: Romance | Publication Year: 2022 | Rating: 1.5
Title: Echoes of Eternity | Genre: Non-Fiction | Publication Year: 1952 | Rating: 1.9
Title: Whispers of the Abyss | Genre: Romance | Publication Year: 1987 | Rating: 4.5
Title: The Crystal Key | Genre: Fantasy | Publication Year: 1950 | Rating: 2.6
<end>Can you change this yaml into plain text?
- Age: 32
  Birth Month: August
  Income: 35000
  Name: Gerald
- Age: 68
  Birth Month: January
  Income: 290000
  Name: Mallory
- Age: 53
  Birth Month: September
  Income: 350000
  Name: Kiara
- Age: 23
  Birth Month: February
  Income: 170000
  Name: Alexis
<start>
Name: Gerald | Age: 32 | Birth Month: August | Income: 35000
Name: Mallory | Age: 68 | Birth Month: January | Income: 290000
Name: Kiara | Age: 53 | Birth Month: September | Income: 350000
Name: Alexis | Age: 23 | Birth Month: February | Income: 170000
<end>Convert this YAML to Json:
- Company: BioLife
  High Price: 1342.06
  Low Price: 901.65
  Open Price: 901.65
- Company: RetailWorld
  High Price: 924.63
  Low Price: 624.37
  Open Price: 924.63
- Company: AeroSystems
  High Price: 1292.76
  Low Price: 622.36
  Open Price: 622.36
- Company: FoodChain
  High Price: 1162.26
  Low Price: 187.18
  Open Price: 227.73
- Company: FinanceTrust
  High Price: 475.6
  Low Price: 35.94
  Open Price: 475.6
- Company: HealthGen
  High Price: 858.77
  Low Price: 141.54
  Open Price: 424.18
- Company: AeroSystems
  High Price: 1350.68
  Low Price: 187.18
  Open Price: 1350.68
- Company: FinanceTrust
  High Price: 1497.57
  Low Price: 227.73
  Open Price: 227.73
<start>
[
    {
        "Company": "BioLife",
        "Open Price": 901.65,
        "High Price": 1342.06,
        "Low Price": 901.65
    },
    {
        "Company": "RetailWorld",
        "Open Price": 924.63,
        "High Price": 924.63,
        "Low Price": 624.37
    },
    {
        "Company": "AeroSystems",
        "Open Price": 622.36,
        "High Price": 1292.76,
        "Low Price": 622.36
    },
    {
        "Company": "FoodChain",
        "Open Price": 227.73,
        "High Price": 1162.26,
        "Low Price": 187.18
    },
    {
        "Company": "FinanceTrust",
        "Open Price": 475.6,
        "High Price": 475.6,
        "Low Price": 35.94
    },
    {
        "Company": "HealthGen",
        "Open Price": 424.18,
        "High Price": 858.77,
        "Low Price": 141.54
    },
    {
        "Company": "AeroSystems",
        "Open Price": 1350.68,
        "High Price": 1350.68,
        "Low Price": 187.18
    },
    {
        "Company": "FinanceTrust",
        "Open Price": 227.73,
        "High Price": 1497.57,
        "Low Price": 227.73
    }
]
<end>Transform this CSV structure to a Json format:
Director,Genre,Release Year,Box Office Earnings (M)
Mara Moonshadow,Adventure,2005,680.81
Cade Firebrand,Horror,2011,304.92
Selene Darkwhisper,Comedy,2007,582.23
Aria Ravenwood,Action,2014,871.0
Cade Firebrand,Sci-Fi,1978,743.55
Selene Darkwhisper,Adventure,1972,456.99
<start>
[
    {
        "Director": "Mara Moonshadow",
        "Genre": "Adventure",
        "Release Year": 2005,
        "Box Office Earnings (M)": 680.81
    },
    {
        "Director": "Cade Firebrand",
        "Genre": "Horror",
        "Release Year": 2011,
        "Box Office Earnings (M)": 304.92
    },
    {
        "Director": "Selene Darkwhisper",
        "Genre": "Comedy",
        "Release Year": 2007,
        "Box Office Earnings (M)": 582.23
    },
    {
        "Director": "Aria Ravenwood",
        "Genre": "Action",
        "Release Year": 2014,
        "Box Office Earnings (M)": 871.0
    },
    {
        "Director": "Cade Firebrand",
        "Genre": "Sci-Fi",
        "Release Year": 1978,
        "Box Office Earnings (M)": 743.55
    },
    {
        "Director": "Selene Darkwhisper",
        "Genre": "Adventure",
        "Release Year": 1972,
        "Box Office Earnings (M)": 456.99
    }
]
<end>Can you change this CSV into plain text?
Database Name,Cache Hit Ratio (%),Connection Count,Timestamp
AnalyticsDB,72.55,453,2022-10-26 08:44:39
ProductsDB,99.28,201,2023-01-05 19:20:17
UserDB,82.27,343,2023-06-19 21:38:37
SalesDB,93.23,301,2023-12-12 21:20:43
MetricsDB,83.28,134,2021-02-05 11:25:57
LogsDB,96.14,107,2021-08-08 13:14:54
InventoryDB,96.52,181,2021-05-11 08:33:18
ProfilesDB,77.48,490,2021-06-15 22:10:54
AnalyticsDB,75.04,51,2021-01-18 10:50:59
<start>
Database Name: AnalyticsDB | Cache Hit Ratio (%): 72.55 | Connection Count: 453 | Timestamp: 2022-10-26 08:44:39
Database Name: ProductsDB | Cache Hit Ratio (%): 99.28 | Connection Count: 201 | Timestamp: 2023-01-05 19:20:17
Database Name: UserDB | Cache Hit Ratio (%): 82.27 | Connection Count: 343 | Timestamp: 2023-06-19 21:38:37
Database Name: SalesDB | Cache Hit Ratio (%): 93.23 | Connection Count: 301 | Timestamp: 2023-12-12 21:20:43
Database Name: MetricsDB | Cache Hit Ratio (%): 83.28 | Connection Count: 134 | Timestamp: 2021-02-05 11:25:57
Database Name: LogsDB | Cache Hit Ratio (%): 96.14 | Connection Count: 107 | Timestamp: 2021-08-08 13:14:54
Database Name: InventoryDB | Cache Hit Ratio (%): 96.52 | Connection Count: 181 | Timestamp: 2021-05-11 08:33:18
Database Name: ProfilesDB | Cache Hit Ratio (%): 77.48 | Connection Count: 490 | Timestamp: 2021-06-15 22:10:54
Database Name: AnalyticsDB | Cache Hit Ratio (%): 75.04 | Connection Count: 51 | Timestamp: 2021-01-18 10:50:59
<end>Please transform the following markdown data into Yml:
| Location | Condition | Humidity (%) | Day |
| --- | --- | --- | --- |
| Denver | Sunny | 60 | Sunday |
| Chicago | Rainy | 51 | Saturday |
| New York | Sunny | 49 | Sunday |
| Los Angeles | Windy | 83 | Thursday |
| Denver | Cloudy | 37 | Thursday |
| Miami | Foggy | 91 | Saturday |<start>
- Condition: Sunny
  Day: Sunday
  Humidity (%): 60
  Location: Denver
- Condition: Rainy
  Day: Saturday
  Humidity (%): 51
  Location: Chicago
- Condition: Sunny
  Day: Sunday
  Humidity (%): 49
  Location: New York
- Condition: Windy
  Day: Thursday
  Humidity (%): 83
  Location: Los Angeles
- Condition: Cloudy
  Day: Thursday
  Humidity (%): 37
  Location: Denver
- Condition: Foggy
  Day: Saturday
  Humidity (%): 91
  Location: Miami
<end>Transform this csv structure to a YML format:
Director,Genre,Release Year,Box Office Earnings (M)
Orin Shadowalker,Sci-Fi,2019,84.82
Mara Moonshadow,Adventure,2018,111.26
Rylan Frostblade,Action,1981,896.14
Mara Moonshadow,Thriller,2021,656.01
Orin Shadowalker,Comedy,1999,838.01
Selene Darkwhisper,Thriller,2020,851.04
Rylan Frostblade,Thriller,1991,938.74
Mara Moonshadow,Drama,1974,123.05
Zara Stormrider,Sci-Fi,1982,111.26
Mara Moonshadow,Drama,2004,251.81
<start>
- Box Office Earnings (M): 84.82
  Director: Orin Shadowalker
  Genre: Sci-Fi
  Release Year: 2019
- Box Office Earnings (M): 111.26
  Director: Mara Moonshadow
  Genre: Adventure
  Release Year: 2018
- Box Office Earnings (M): 896.14
  Director: Rylan Frostblade
  Genre: Action
  Release Year: 1981
- Box Office Earnings (M): 656.01
  Director: Mara Moonshadow
  Genre: Thriller
  Release Year: 2021
- Box Office Earnings (M): 838.01
  Director: Orin Shadowalker
  Genre: Comedy
  Release Year: 1999
- Box Office Earnings (M): 851.04
  Director: Selene Darkwhisper
  Genre: Thriller
  Release Year: 2020
- Box Office Earnings (M): 938.74
  Director: Rylan Frostblade
  Genre: Thriller
  Release Year: 1991
- Box Office Earnings (M): 123.05
  Director: Mara Moonshadow
  Genre: Drama
  Release Year: 1974
- Box Office Earnings (M): 111.26
  Director: Zara Stormrider
  Genre: Sci-Fi
  Release Year: 1982
- Box Office Earnings (M): 251.81
  Director: Mara Moonshadow
  Genre: Drama
  Release Year: 2004
<end>Please transform the following PLAIN TEXT data into markdown:
Location: Houston | Condition: Foggy | Temperature (C): 28.6 | Humidity (%): 88 | Wind Speed (km/h): 15.4 | Day: Monday
Location: Denver | Condition: Foggy | Temperature (C): 18.9 | Humidity (%): 75 | Wind Speed (km/h): 5.8 | Day: Thursday
Location: Denver | Condition: Windy | Temperature (C): -3.5 | Humidity (%): 37 | Wind Speed (km/h): 12.8 | Day: Monday
Location: Phoenix | Condition: Stormy | Temperature (C): 32.8 | Humidity (%): 35 | Wind Speed (km/h): 27.3 | Day: Tuesday
Location: Chicago | Condition: Snowy | Temperature (C): 10.3 | Humidity (%): 66 | Wind Speed (km/h): 26.0 | Day: Monday
Location: Chicago | Condition: Windy | Temperature (C): 28.4 | Humidity (%): 98 | Wind Speed (km/h): 21.0 | Day: Sunday
Location: New York | Condition: Stormy | Temperature (C): -0.8 | Humidity (%): 62 | Wind Speed (km/h): 9.9 | Day: Friday
Location: Chicago | Condition: Sunny | Temperature (C): -1.1 | Humidity (%): 87 | Wind Speed (km/h): 4.3 | Day: Sunday
<start>
| Location | Condition | Temperature (C) | Humidity (%) | Wind Speed (km/h) | Day |
| --- | --- | --- | --- | --- | --- |
| Houston | Foggy | 28.6 | 88 | 15.4 | Monday |
| Denver | Foggy | 18.9 | 75 | 5.8 | Thursday |
| Denver | Windy | -3.5 | 37 | 12.8 | Monday |
| Phoenix | Stormy | 32.8 | 35 | 27.3 | Tuesday |
| Chicago | Snowy | 10.3 | 66 | 26.0 | Monday |
| Chicago | Windy | 28.4 | 98 | 21.0 | Sunday |
| New York | Stormy | -0.8 | 62 | 9.9 | Friday |
| Chicago | Sunny | -1.1 | 87 | 4.3 | Sunday |
<end>Convert this Plain text to csv:
Title: The Last Sky | Author: Isla Windrider | Genre: Historical | Publication Year: 1991 | Rating: 2.9
Title: The Crystal Key | Author: Galen Starfire | Genre: Science Fiction | Publication Year: 2016 | Rating: 2.6
Title: The Forgotten World | Author: Kara Firebrand | Genre: Science Fiction | Publication Year: 1950 | Rating: 1.5
Title: Echoes of Eternity | Author: Draven Blackthorn | Genre: Historical | Publication Year: 1980 | Rating: 2.1
Title: A Journey Through Time | Author: Galen Starfire | Genre: Science Fiction | Publication Year: 1988 | Rating: 3.1
Title: A Journey Through Time | Author: Elara Moonshadow | Genre: Horror | Publication Year: 2001 | Rating: 4.2
Title: Legends of the Rift | Author: Kara Firebrand | Genre: Romance | Publication Year: 1968 | Rating: 4.6
Title: Legends of the Rift | Author: Luna Silverleaf | Genre: Non-Fiction | Publication Year: 1972 | Rating: 4.7
Title: A Journey Through Time | Author: Orion Frostblade | Genre: Thriller | Publication Year: 1976 | Rating: 1.1
Title: Whispers of the Abyss | Author: Sylvia Nightshade | Genre: Science Fiction | Publication Year: 1968 | Rating: 4.4
<start>
Title,Author,Genre,Publication Year,Rating
The Last Sky,Isla Windrider,Historical,1991,2.9
The Crystal Key,Galen Starfire,Science Fiction,2016,2.6
The Forgotten World,Kara Firebrand,Science Fiction,1950,1.5
Echoes of Eternity,Draven Blackthorn,Historical,1980,2.1
A Journey Through Time,Galen Starfire,Science Fiction,1988,3.1
A Journey Through Time,Elara Moonshadow,Horror,2001,4.2
Legends of the Rift,Kara Firebrand,Romance,1968,4.6
Legends of the Rift,Luna Silverleaf,Non-Fiction,1972,4.7
A Journey Through Time,Orion Frostblade,Thriller,1976,1.1
Whispers of the Abyss,Sylvia Nightshade,Science Fiction,1968,4.4
<end>Here's some Csv data, can you convert it to json?
Company,Sector,Market Cap,Quarter
AutoDrive,Aerospace,Mid Cap,Q3
TechCorp,Healthcare,Small Cap,Q1
BioPharm,Retail,Mid Cap,Q2
AeroSpace,Energy,Mid Cap,Q4
BioPharm,Biotech,Small Cap,Q1
BioPharm,Finance,Small Cap,Q2
RetailHub,Biotech,Mid Cap,Q3
AeroSpace,Energy,Mega Cap,Q3
RetailHub,Retail,Mega Cap,Q3
AeroSpace,Finance,Mega Cap,Q1
<start>
[
    {
        "Company": "AutoDrive",
        "Sector": "Aerospace",
        "Market Cap": "Mid Cap",
        "Quarter": "Q3"
    },
    {
        "Company": "TechCorp",
        "Sector": "Healthcare",
        "Market Cap": "Small Cap",
        "Quarter": "Q1"
    },
    {
        "Company": "BioPharm",
        "Sector": "Retail",
        "Market Cap": "Mid Cap",
        "Quarter": "Q2"
    },
    {
        "Company": "AeroSpace",
        "Sector": "Energy",
        "Market Cap": "Mid Cap",
        "Quarter": "Q4"
    },
    {
        "Company": "BioPharm",
        "Sector": "Biotech",
        "Market Cap": "Small Cap",
        "Quarter": "Q1"
    },
    {
        "Company": "BioPharm",
        "Sector": "Finance",
        "Market Cap": "Small Cap",
        "Quarter": "Q2"
    },
    {
        "Company": "RetailHub",
        "Sector": "Biotech",
        "Market Cap": "Mid Cap",
        "Quarter": "Q3"
    },
    {
        "Company": "AeroSpace",
        "Sector": "Energy",
        "Market Cap": "Mega Cap",
        "Quarter": "Q3"
    },
    {
        "Company": "RetailHub",
        "Sector": "Retail",
        "Market Cap": "Mega Cap",
        "Quarter": "Q3"
    },
    {
        "Company": "AeroSpace",
        "Sector": "Finance",
        "Market Cap": "Mega Cap",
        "Quarter": "Q1"
    }
]
<end>Transform this Json structure to a markdown format:
[
    {
        "Age": 52,
        "City": "New York",
        "Income": 405000
    },
    {
        "Age": 62,
        "City": "Baltimore",
        "Income": 50000
    },
    {
        "Age": 33,
        "City": "Columbus",
        "Income": 275000
    },
    {
        "Age": 30,
        "City": "Houston",
        "Income": 80000
    },
    {
        "Age": 69,
        "City": "Denver",
        "Income": 130000
    },
    {
        "Age": 29,
        "City": "Milwaukee",
        "Income": 65000
    }
]<start>
| Age | City | Income |
| --- | --- | --- |
| 52 | New York | 405000 |
| 62 | Baltimore | 50000 |
| 33 | Columbus | 275000 |
| 30 | Houston | 80000 |
| 69 | Denver | 130000 |
| 29 | Milwaukee | 65000 |
<end>Convert this plain text to csv:
Title: Shadows of Solitude | Publication Year: 2000 | Rating: 4.3
Title: The Crystal Key | Publication Year: 1955 | Rating: 3.6
Title: Legends of the Rift | Publication Year: 2008 | Rating: 1.2
Title: Whispers of the Abyss | Publication Year: 1960 | Rating: 4.0
Title: The Silent Grove | Publication Year: 1976 | Rating: 3.7
Title: The Last Sky | Publication Year: 1997 | Rating: 2.5
Title: Whispers of the Abyss | Publication Year: 1987 | Rating: 2.6
Title: Echoes of Eternity | Publication Year: 1996 | Rating: 3.5
Title: The Last Sky | Publication Year: 2015 | Rating: 2.4
<start>
Title,Publication Year,Rating
Shadows of Solitude,2000,4.3
The Crystal Key,1955,3.6
Legends of the Rift,2008,1.2
Whispers of the Abyss,1960,4.0
The Silent Grove,1976,3.7
The Last Sky,1997,2.5
Whispers of the Abyss,1987,2.6
Echoes of Eternity,1996,3.5
The Last Sky,2015,2.4
<end>Here's some MARKDOWN data, can you convert it to yml?
| Genre | Release Year |
| --- | --- |
| Thriller | 1986 |
| Action | 1978 |
| Horror | 2016 |<start>
- Genre: Thriller
  Release Year: 1986
- Genre: Action
  Release Year: 1978
- Genre: Horror
  Release Year: 2016
<end>Please transform the following plain text data into YAML:
Date: 2011-07-13 | Open Price: 1213.09 | High Price: 1213.09 | Low Price: 711.3 | Volume: 412010
Date: 2010-02-04 | Open Price: 121.67 | High Price: 1436.18 | Low Price: 121.67 | Volume: 6659204
Date: 2020-08-15 | Open Price: 21.59 | High Price: 833.08 | Low Price: 21.59 | Volume: 1821538
<start>
- Date: '2011-07-13'
  High Price: 1213.09
  Low Price: 711.3
  Open Price: 1213.09
  Volume: 412010
- Date: '2010-02-04'
  High Price: 1436.18
  Low Price: 121.67
  Open Price: 121.67
  Volume: 6659204
- Date: '2020-08-15'
  High Price: 833.08
  Low Price: 21.59
  Open Price: 21.59
  Volume: 1821538
<end>Here's some MARKDOWN data, can you convert it to plain text?
| Device Type | Battery Level (%) | Timestamp |
| --- | --- | --- |
| Pressure Sensor | 54.2 | 2021-10-26 04:11:40 |
| Light Sensor | 55.5 | 2023-09-23 04:50:55 |
| Temperature Sensor | 16.3 | 2023-05-09 09:47:31 |
| Motion Detector | 41.9 | 2022-05-04 01:47:22 |
| Humidity Sensor | 50.2 | 2022-08-21 01:39:33 |
| Temperature Sensor | 56.2 | 2022-09-26 06:52:33 |
| Humidity Sensor | 63.1 | 2022-12-14 05:59:55 |
| Humidity Sensor | 16.3 | 2023-05-01 22:04:48 |
| Temperature Sensor | 51.8 | 2021-12-22 04:31:24 |
| Light Sensor | 50.3 | 2022-05-27 05:35:27 |<start>
Device Type: Pressure Sensor | Battery Level (%): 54.2 | Timestamp: 2021-10-26 04:11:40
Device Type: Light Sensor | Battery Level (%): 55.5 | Timestamp: 2023-09-23 04:50:55
Device Type: Temperature Sensor | Battery Level (%): 16.3 | Timestamp: 2023-05-09 09:47:31
Device Type: Motion Detector | Battery Level (%): 41.9 | Timestamp: 2022-05-04 01:47:22
Device Type: Humidity Sensor | Battery Level (%): 50.2 | Timestamp: 2022-08-21 01:39:33
Device Type: Temperature Sensor | Battery Level (%): 56.2 | Timestamp: 2022-09-26 06:52:33
Device Type: Humidity Sensor | Battery Level (%): 63.1 | Timestamp: 2022-12-14 05:59:55
Device Type: Humidity Sensor | Battery Level (%): 16.3 | Timestamp: 2023-05-01 22:04:48
Device Type: Temperature Sensor | Battery Level (%): 51.8 | Timestamp: 2021-12-22 04:31:24
Device Type: Light Sensor | Battery Level (%): 50.3 | Timestamp: 2022-05-27 05:35:27
<end>Here's some yml data, can you convert it to PLAIN TEXT?
- Director: Drake Nightshade
  Genre: Horror
  Title: The Great Expedition
- Director: Cade Firebrand
  Genre: Action
  Title: Rise of the Titans
- Director: Zara Stormrider
  Genre: Adventure
  Title: Starbound Odyssey
- Director: Selene Darkwhisper
  Genre: Sci-Fi
  Title: The Final Voyage
- Director: Mara Moonshadow
  Genre: Adventure
  Title: Starbound Odyssey
- Director: Lira Silverleaf
  Genre: Drama
  Title: Mystery of the Depths
- Director: Selene Darkwhisper
  Genre: Comedy
  Title: The Final Voyage
- Director: Rylan Frostblade
  Genre: Sci-Fi
  Title: Rise of the Titans
- Director: Selene Darkwhisper
  Genre: Action
  Title: Dreamwalker
<start>
Title: The Great Expedition | Director: Drake Nightshade | Genre: Horror
Title: Rise of the Titans | Director: Cade Firebrand | Genre: Action
Title: Starbound Odyssey | Director: Zara Stormrider | Genre: Adventure
Title: The Final Voyage | Director: Selene Darkwhisper | Genre: Sci-Fi
Title: Starbound Odyssey | Director: Mara Moonshadow | Genre: Adventure
Title: Mystery of the Depths | Director: Lira Silverleaf | Genre: Drama
Title: The Final Voyage | Director: Selene Darkwhisper | Genre: Comedy
Title: Rise of the Titans | Director: Rylan Frostblade | Genre: Sci-Fi
Title: Dreamwalker | Director: Selene Darkwhisper | Genre: Action
<end>Transform this yaml structure to a JSON format:
- Close Price: 66.99
  Date: '2019-12-02'
  High Price: 1471.77
  Low Price: 66.99
  Open Price: 869.37
  Volume: 5498311
- Close Price: 1059.84
  Date: '2021-08-01'
  High Price: 1059.84
  Low Price: 418.42
  Open Price: 1052.83
  Volume: 7352876
- Close Price: 1060.54
  Date: '2017-04-27'
  High Price: 1060.54
  Low Price: 519.42
  Open Price: 519.42
  Volume: 5386301
<start>
[
    {
        "Date": "2019-12-02",
        "Open Price": 869.37,
        "Close Price": 66.99,
        "High Price": 1471.77,
        "Low Price": 66.99,
        "Volume": 5498311
    },
    {
        "Date": "2021-08-01",
        "Open Price": 1052.83,
        "Close Price": 1059.84,
        "High Price": 1059.84,
        "Low Price": 418.42,
        "Volume": 7352876
    },
    {
        "Date": "2017-04-27",
        "Open Price": 519.42,
        "Close Price": 1060.54,
        "High Price": 1060.54,
        "Low Price": 519.42,
        "Volume": 5386301
    }
]
<end>Convert this Csv to yaml:
Date,High Price,Low Price,Volume
2018-08-04,1158.43,695.03,6516545
2023-03-21,245.03,172.84,4028998
2011-12-15,1158.43,450.0,3546568
<start>
- Date: '2018-08-04'
  High Price: 1158.43
  Low Price: 695.03
  Volume: 6516545
- Date: '2023-03-21'
  High Price: 245.03
  Low Price: 172.84
  Volume: 4028998
- Date: '2011-12-15'
  High Price: 1158.43
  Low Price: 450.0
  Volume: 3546568
<end>Can you change this Markdown into Yml?
| Trip Name | Start Location | Distance (miles) | Duration (hours) | Fuel Used (gallons) |
| --- | --- | --- | --- | --- |
| Canyon Trek | New York | 1936.9 | 18.1 | 67.7 |
| Desert Drive | Chicago | 2445.5 | 25.9 | 37.6 |
| Desert Drive | San Francisco | 112.2 | 11.0 | 71.0 |
| Lakeside Retreat | New York | 112.2 | 71.2 | 46.0 |
| Lakeside Retreat | Los Angeles | 1564.5 | 69.3 | 88.9 |<start>
- Distance (miles): 1936.9
  Duration (hours): 18.1
  Fuel Used (gallons): 67.7
  Start Location: New York
  Trip Name: Canyon Trek
- Distance (miles): 2445.5
  Duration (hours): 25.9
  Fuel Used (gallons): 37.6
  Start Location: Chicago
  Trip Name: Desert Drive
- Distance (miles): 112.2
  Duration (hours): 11.0
  Fuel Used (gallons): 71.0
  Start Location: San Francisco
  Trip Name: Desert Drive
- Distance (miles): 112.2
  Duration (hours): 71.2
  Fuel Used (gallons): 46.0
  Start Location: New York
  Trip Name: Lakeside Retreat
- Distance (miles): 1564.5
  Duration (hours): 69.3
  Fuel Used (gallons): 88.9
  Start Location: Los Angeles
  Trip Name: Lakeside Retreat
<end>Here's some yml data, can you convert it to plain text?
- Close Price: 894.95
  Date: '2020-09-15'
  High Price: 1152.04
  Low Price: 894.95
  Open Price: 1152.04
  Volume: 8788183
- Close Price: 965.45
  Date: '2019-06-01'
  High Price: 965.45
  Low Price: 649.2
  Open Price: 687.0
  Volume: 8588474
- Close Price: 83.3
  Date: '2014-04-12'
  High Price: 1215.21
  Low Price: 83.3
  Open Price: 1215.21
  Volume: 4686030
- Close Price: 1385.38
  Date: '2010-03-11'
  High Price: 1385.38
  Low Price: 1215.21
  Open Price: 1215.21
  Volume: 5904232
<start>
Date: 2020-09-15 | Open Price: 1152.04 | Close Price: 894.95 | High Price: 1152.04 | Low Price: 894.95 | Volume: 8788183
Date: 2019-06-01 | Open Price: 687.0 | Close Price: 965.45 | High Price: 965.45 | Low Price: 649.2 | Volume: 8588474
Date: 2014-04-12 | Open Price: 1215.21 | Close Price: 83.3 | High Price: 1215.21 | Low Price: 83.3 | Volume: 4686030
Date: 2010-03-11 | Open Price: 1215.21 | Close Price: 1385.38 | High Price: 1385.38 | Low Price: 1215.21 | Volume: 5904232
<end>Can you change this Json into csv?
[
    {
        "Author": "Luna Silverleaf",
        "Genre": "Romance",
        "Rating": 2.3
    },
    {
        "Author": "Galen Starfire",
        "Genre": "Horror",
        "Rating": 1.3
    },
    {
        "Author": "Kara Firebrand",
        "Genre": "Non-Fiction",
        "Rating": 3.4
    },
    {
        "Author": "Galen Starfire",
        "Genre": "Historical",
        "Rating": 1.6
    },
    {
        "Author": "Rowan Ashborne",
        "Genre": "Romance",
        "Rating": 4.1
    }
]<start>
Author,Genre,Rating
Luna Silverleaf,Romance,2.3
Galen Starfire,Horror,1.3
Kara Firebrand,Non-Fiction,3.4
Galen Starfire,Historical,1.6
Rowan Ashborne,Romance,4.1
<end>Here's some Csv data, can you convert it to plain text?
Title,Release Year,Box Office Earnings (M)
Beyond the Veil,2012,354.76
Starbound Odyssey,2021,925.52
Dreamwalker,2006,60.55
Escape from Earth,2008,210.25
Edge of Infinity,2005,981.16
<start>
Title: Beyond the Veil | Release Year: 2012 | Box Office Earnings (M): 354.76
Title: Starbound Odyssey | Release Year: 2021 | Box Office Earnings (M): 925.52
Title: Dreamwalker | Release Year: 2006 | Box Office Earnings (M): 60.55
Title: Escape from Earth | Release Year: 2008 | Box Office Earnings (M): 210.25
Title: Edge of Infinity | Release Year: 2005 | Box Office Earnings (M): 981.16
<end>Here's some yml data, can you convert it to plain text?
- Birth Month: February
  City: Baltimore
  Income: 270000
  Name: Autumn
- Birth Month: June
  City: Memphis
  Income: 65000
  Name: Sherman
- Birth Month: December
  City: Louisville
  Income: 430000
  Name: Brooklyn
<start>
Name: Autumn | Birth Month: February | City: Baltimore | Income: 270000
Name: Sherman | Birth Month: June | City: Memphis | Income: 65000
Name: Brooklyn | Birth Month: December | City: Louisville | Income: 430000
<end>Please transform the following json data into Markdown:
[
    {
        "Name": "Heidi",
        "Age": 56,
        "City": "Nashville",
        "Income": 235000
    },
    {
        "Name": "Hiram",
        "Age": 44,
        "City": "Phoenix",
        "Income": 235000
    },
    {
        "Name": "Bess",
        "Age": 62,
        "City": "Las Vegas",
        "Income": 70000
    }
]<start>
| Name | Age | City | Income |
| --- | --- | --- | --- |
| Heidi | 56 | Nashville | 235000 |
| Hiram | 44 | Phoenix | 235000 |
| Bess | 62 | Las Vegas | 70000 |
<end>Transform this markdown structure to a Csv format:
| Title | Director | Genre | Release Year |
| --- | --- | --- | --- |
| Starbound Odyssey | Drake Nightshade | Adventure | 2001 |
| Dreamwalker | Mara Moonshadow | Thriller | 1980 |
| The Great Expedition | Rylan Frostblade | Thriller | 2012 |<start>
Title,Director,Genre,Release Year
Starbound Odyssey,Drake Nightshade,Adventure,2001
Dreamwalker,Mara Moonshadow,Thriller,1980
The Great Expedition,Rylan Frostblade,Thriller,2012
<end>Please transform the following yml data into Csv:
- Cuisine: Chinese
  Location: Houston
  Price Range: $
  Rating: 1
  Restaurant Name: Sushi World
- Cuisine: French
  Location: Phoenix
  Price Range: $$$$$
  Rating: 2
  Restaurant Name: Burger Haven
- Cuisine: Italian
  Location: Seattle
  Price Range: $$$$
  Rating: 3
  Restaurant Name: Pizza Planet
- Cuisine: Mediterranean
  Location: Miami
  Price Range: $
  Rating: 2
  Restaurant Name: Vegan Delight
- Cuisine: Indian
  Location: New York
  Price Range: $$$$
  Rating: 3
  Restaurant Name: The Steakhouse
- Cuisine: American
  Location: Los Angeles
  Price Range: $$$$$
  Rating: 5
  Restaurant Name: Pizza Planet
<start>
Restaurant Name,Cuisine,Location,Rating,Price Range
Sushi World,Chinese,Houston,1,$
Burger Haven,French,Phoenix,2,$$$$$
Pizza Planet,Italian,Seattle,3,$$$$
Vegan Delight,Mediterranean,Miami,2,$
The Steakhouse,Indian,New York,3,$$$$
Pizza Planet,American,Los Angeles,5,$$$$$
<end>Can you change this markdown into Yml?
| Name | Age | Income |
| --- | --- | --- |
| Dawn | 64 | 390000 |
| Rena | 34 | 405000 |
| Marco | 52 | 310000 |
| Gage | 26 | 345000 |
| Luella | 39 | 45000 |
| Jeffrey | 43 | 235000 |
| Neil | 64 | 75000 |
| Kathryn | 65 | 110000 |<start>
- Age: 64
  Income: 390000
  Name: Dawn
- Age: 34
  Income: 405000
  Name: Rena
- Age: 52
  Income: 310000
  Name: Marco
- Age: 26
  Income: 345000
  Name: Gage
- Age: 39
  Income: 45000
  Name: Luella
- Age: 43
  Income: 235000
  Name: Jeffrey
- Age: 64
  Income: 75000
  Name: Neil
- Age: 65
  Income: 110000
  Name: Kathryn
<end>Please transform the following csv data into plain text:
Device ID,Location,Battery Level (%),Reading Value,Timestamp
device-0037,Bedroom,86.4,61.06,2023-03-18 00:47:24
device-0024,Living Room,52.2,31.44,2021-06-04 17:18:53
device-0083,Office,32.3,52.95,2023-07-11 06:49:59
device-0012,Bedroom,42.9,29.18,2022-04-12 18:32:21
<start>
Device ID: device-0037 | Location: Bedroom | Battery Level (%): 86.4 | Reading Value: 61.06 | Timestamp: 2023-03-18 00:47:24
Device ID: device-0024 | Location: Living Room | Battery Level (%): 52.2 | Reading Value: 31.44 | Timestamp: 2021-06-04 17:18:53
Device ID: device-0083 | Location: Office | Battery Level (%): 32.3 | Reading Value: 52.95 | Timestamp: 2023-07-11 06:49:59
Device ID: device-0012 | Location: Bedroom | Battery Level (%): 42.9 | Reading Value: 29.18 | Timestamp: 2022-04-12 18:32:21
<end>Transform this plain text structure to a CSV format:
Company: BioPharm | Sector: Automotive | Market Cap: Mid Cap | Annual Revenue (B): 375.05 | Quarter: Q1
Company: AutoDrive | Sector: Healthcare | Market Cap: Large Cap | Annual Revenue (B): 265.71 | Quarter: Q4
Company: Foodies | Sector: Energy | Market Cap: Large Cap | Annual Revenue (B): 242.89 | Quarter: Q2
Company: AutoDrive | Sector: Finance | Market Cap: Mid Cap | Annual Revenue (B): 481.35 | Quarter: Q2
Company: TechCorp | Sector: Automotive | Market Cap: Small Cap | Annual Revenue (B): 347.02 | Quarter: Q4
Company: BioPharm | Sector: Technology | Market Cap: Mega Cap | Annual Revenue (B): 258.88 | Quarter: Q2
<start>
Company,Sector,Market Cap,Annual Revenue (B),Quarter
BioPharm,Automotive,Mid Cap,375.05,Q1
AutoDrive,Healthcare,Large Cap,265.71,Q4
Foodies,Energy,Large Cap,242.89,Q2
AutoDrive,Finance,Mid Cap,481.35,Q2
TechCorp,Automotive,Small Cap,347.02,Q4
BioPharm,Technology,Mega Cap,258.88,Q2
<end>Transform this json structure to a Plain text format:
[
    {
        "Company": "FinanceTrust",
        "Date": "2011-03-17",
        "Open Price": 149.37,
        "Close Price": 1062.27,
        "High Price": 1327.04,
        "Low Price": 149.37,
        "Volume": 4522099
    },
    {
        "Company": "AutoMotive",
        "Date": "2013-06-25",
        "Open Price": 169.58,
        "Close Price": 472.57,
        "High Price": 1424.08,
        "Low Price": 117.11,
        "Volume": 1431473
    },
    {
        "Company": "BioLife",
        "Date": "2012-08-05",
        "Open Price": 536.77,
        "Close Price": 1446.99,
        "High Price": 1446.99,
        "Low Price": 536.77,
        "Volume": 9172908
    },
    {
        "Company": "GreenEnergy",
        "Date": "2010-12-20",
        "Open Price": 419.59,
        "Close Price": 668.32,
        "High Price": 668.32,
        "Low Price": 419.59,
        "Volume": 3679318
    },
    {
        "Company": "FinanceTrust",
        "Date": "2015-03-11",
        "Open Price": 1098.51,
        "Close Price": 969.46,
        "High Price": 1098.51,
        "Low Price": 829.8,
        "Volume": 6198746
    }
]<start>
Company: FinanceTrust | Date: 2011-03-17 | Open Price: 149.37 | Close Price: 1062.27 | High Price: 1327.04 | Low Price: 149.37 | Volume: 4522099
Company: AutoMotive | Date: 2013-06-25 | Open Price: 169.58 | Close Price: 472.57 | High Price: 1424.08 | Low Price: 117.11 | Volume: 1431473
Company: BioLife | Date: 2012-08-05 | Open Price: 536.77 | Close Price: 1446.99 | High Price: 1446.99 | Low Price: 536.77 | Volume: 9172908
Company: GreenEnergy | Date: 2010-12-20 | Open Price: 419.59 | Close Price: 668.32 | High Price: 668.32 | Low Price: 419.59 | Volume: 3679318
Company: FinanceTrust | Date: 2015-03-11 | Open Price: 1098.51 | Close Price: 969.46 | High Price: 1098.51 | Low Price: 829.8 | Volume: 6198746
<end>Please transform the following Yml data into markdown:
- Age: 37
  Birth Month: July
  City: New York
  Name: Michele
- Age: 66
  Birth Month: August
  City: Charlotte
  Name: Francisco
- Age: 50
  Birth Month: February
  City: San Jose
  Name: Christy
<start>
| Name | Age | Birth Month | City |
| --- | --- | --- | --- |
| Michele | 37 | July | New York |
| Francisco | 66 | August | Charlotte |
| Christy | 50 | February | San Jose |
<end>Transform this YAML structure to a json format:
- Age: 27
  Birth Month: July
  City: Milwaukee
  Income: 295000
  Name: Colin
- Age: 32
  Birth Month: June
  City: Boston
  Income: 455000
  Name: Etta
- Age: 67
  Birth Month: January
  City: Denver
  Income: 95000
  Name: Kurt
- Age: 57
  Birth Month: April
  City: Fort Worth
  Income: 175000
  Name: Karen
<start>
[
    {
        "Name": "Colin",
        "Age": 27,
        "Birth Month": "July",
        "City": "Milwaukee",
        "Income": 295000
    },
    {
        "Name": "Etta",
        "Age": 32,
        "Birth Month": "June",
        "City": "Boston",
        "Income": 455000
    },
    {
        "Name": "Kurt",
        "Age": 67,
        "Birth Month": "January",
        "City": "Denver",
        "Income": 95000
    },
    {
        "Name": "Karen",
        "Age": 57,
        "Birth Month": "April",
        "City": "Fort Worth",
        "Income": 175000
    }
]
<end>Can you change this json into Markdown?
[
    {
        "Title": "The Great Expedition",
        "Director": "Selene Darkwhisper",
        "Genre": "Comedy",
        "Box Office Earnings (M)": 659.95
    },
    {
        "Title": "The Great Expedition",
        "Director": "Orin Shadowalker",
        "Genre": "Action",
        "Box Office Earnings (M)": 944.1
    },
    {
        "Title": "The Endless Horizon",
        "Director": "Rylan Frostblade",
        "Genre": "Action",
        "Box Office Earnings (M)": 891.45
    },
    {
        "Title": "Mystery of the Depths",
        "Director": "Selene Darkwhisper",
        "Genre": "Horror",
        "Box Office Earnings (M)": 886.51
    },
    {
        "Title": "Mystery of the Depths",
        "Director": "Talon Blackthorn",
        "Genre": "Comedy",
        "Box Office Earnings (M)": 458.3
    },
    {
        "Title": "The Final Voyage",
        "Director": "Cade Firebrand",
        "Genre": "Comedy",
        "Box Office Earnings (M)": 162.22
    },
    {
        "Title": "The Great Expedition",
        "Director": "Lira Silverleaf",
        "Genre": "Adventure",
        "Box Office Earnings (M)": 754.74
    }
]<start>
| Title | Director | Genre | Box Office Earnings (M) |
| --- | --- | --- | --- |
| The Great Expedition | Selene Darkwhisper | Comedy | 659.95 |
| The Great Expedition | Orin Shadowalker | Action | 944.1 |
| The Endless Horizon | Rylan Frostblade | Action | 891.45 |
| Mystery of the Depths | Selene Darkwhisper | Horror | 886.51 |
| Mystery of the Depths | Talon Blackthorn | Comedy | 458.3 |
| The Final Voyage | Cade Firebrand | Comedy | 162.22 |
| The Great Expedition | Lira Silverleaf | Adventure | 754.74 |
<end>Here's some yml data, can you convert it to csv?
- Close Price: 829.36
  Company: AutoMotive
  Date: '2018-08-01'
  High Price: 1258.46
  Open Price: 1258.46
  Volume: 1704717
- Close Price: 1038.6
  Company: MediaGroup
  Date: '2021-03-24'
  High Price: 1038.6
  Open Price: 552.48
  Volume: 7469153
- Close Price: 1038.6
  Company: TechnoCorp
  Date: '2012-10-08'
  High Price: 1038.6
  Open Price: 1038.6
  Volume: 6666264
<start>
Company,Date,Open Price,Close Price,High Price,Volume
AutoMotive,2018-08-01,1258.46,829.36,1258.46,1704717
MediaGroup,2021-03-24,552.48,1038.6,1038.6,7469153
TechnoCorp,2012-10-08,1038.6,1038.6,1038.6,6666264
<end>Here's some yml data, can you convert it to MARKDOWN?
- Box Office Earnings (M): 699.6
  Director: Orin Shadowalker
  Genre: Comedy
  Release Year: 1972
  Title: Dreamwalker
- Box Office Earnings (M): 337.91
  Director: Lira Silverleaf
  Genre: Adventure
  Release Year: 2008
  Title: Edge of Infinity
- Box Office Earnings (M): 293.39
  Director: Orin Shadowalker
  Genre: Thriller
  Release Year: 1977
  Title: The Great Expedition
- Box Office Earnings (M): 261.88
  Director: Talon Blackthorn
  Genre: Action
  Release Year: 1975
  Title: The Great Expedition
- Box Office Earnings (M): 132.2
  Director: Rylan Frostblade
  Genre: Drama
  Release Year: 1997
  Title: The Great Expedition
- Box Office Earnings (M): 155.76
  Director: Lira Silverleaf
  Genre: Adventure
  Release Year: 2008
  Title: Mystery of the Depths
- Box Office Earnings (M): 803.19
  Director: Drake Nightshade
  Genre: Fantasy
  Release Year: 1975
  Title: Rise of the Titans
- Box Office Earnings (M): 502.58
  Director: Mara Moonshadow
  Genre: Adventure
  Release Year: 1990
  Title: Starbound Odyssey
- Box Office Earnings (M): 816.09
  Director: Drake Nightshade
  Genre: Sci-Fi
  Release Year: 1972
  Title: Mystery of the Depths
<start>
| Title | Director | Genre | Release Year | Box Office Earnings (M) |
| --- | --- | --- | --- | --- |
| Dreamwalker | Orin Shadowalker | Comedy | 1972 | 699.6 |
| Edge of Infinity | Lira Silverleaf | Adventure | 2008 | 337.91 |
| The Great Expedition | Orin Shadowalker | Thriller | 1977 | 293.39 |
| The Great Expedition | Talon Blackthorn | Action | 1975 | 261.88 |
| The Great Expedition | Rylan Frostblade | Drama | 1997 | 132.2 |
| Mystery of the Depths | Lira Silverleaf | Adventure | 2008 | 155.76 |
| Rise of the Titans | Drake Nightshade | Fantasy | 1975 | 803.19 |
| Starbound Odyssey | Mara Moonshadow | Adventure | 1990 | 502.58 |
| Mystery of the Depths | Drake Nightshade | Sci-Fi | 1972 | 816.09 |
<end>Convert this plain text to yml:
Title: The Final Voyage | Director: Drake Nightshade | Genre: Drama | Box Office Earnings (M): 814.93
Title: Rise of the Titans | Director: Rylan Frostblade | Genre: Sci-Fi | Box Office Earnings (M): 109.9
Title: The Final Voyage | Director: Cade Firebrand | Genre: Horror | Box Office Earnings (M): 96.37
Title: Beyond the Veil | Director: Selene Darkwhisper | Genre: Drama | Box Office Earnings (M): 109.9
Title: Mystery of the Depths | Director: Zara Stormrider | Genre: Fantasy | Box Office Earnings (M): 369.07
Title: Rise of the Titans | Director: Aria Ravenwood | Genre: Thriller | Box Office Earnings (M): 872.27
<start>
- Box Office Earnings (M): 814.93
  Director: Drake Nightshade
  Genre: Drama
  Title: The Final Voyage
- Box Office Earnings (M): 109.9
  Director: Rylan Frostblade
  Genre: Sci-Fi
  Title: Rise of the Titans
- Box Office Earnings (M): 96.37
  Director: Cade Firebrand
  Genre: Horror
  Title: The Final Voyage
- Box Office Earnings (M): 109.9
  Director: Selene Darkwhisper
  Genre: Drama
  Title: Beyond the Veil
- Box Office Earnings (M): 369.07
  Director: Zara Stormrider
  Genre: Fantasy
  Title: Mystery of the Depths
- Box Office Earnings (M): 872.27
  Director: Aria Ravenwood
  Genre: Thriller
  Title: Rise of the Titans
<end>Convert this markdown to json:
| Restaurant Name | Cuisine | Location | Rating |
| --- | --- | --- | --- |
| Vegan Delight | Mediterranean | Los Angeles | 5 |
| Pizza Planet | Mediterranean | Seattle | 3 |
| The Steakhouse | Indian | Miami | 1 |
| Pasta Palace | Indian | Phoenix | 5 |
| The Steakhouse | American | Chicago | 2 |
| Sushi World | Indian | Seattle | 1 |
| Taco Town | Mediterranean | New York | 2 |
| Pasta Palace | Mexican | Seattle | 2 |
| Taco Town | Italian | Seattle | 5 |
| Taco Town | Italian | Houston | 1 |<start>
[
    {
        "Restaurant Name": "Vegan Delight",
        "Cuisine": "Mediterranean",
        "Location": "Los Angeles",
        "Rating": 5
    },
    {
        "Restaurant Name": "Pizza Planet",
        "Cuisine": "Mediterranean",
        "Location": "Seattle",
        "Rating": 3
    },
    {
        "Restaurant Name": "The Steakhouse",
        "Cuisine": "Indian",
        "Location": "Miami",
        "Rating": 1
    },
    {
        "Restaurant Name": "Pasta Palace",
        "Cuisine": "Indian",
        "Location": "Phoenix",
        "Rating": 5
    },
    {
        "Restaurant Name": "The Steakhouse",
        "Cuisine": "American",
        "Location": "Chicago",
        "Rating": 2
    },
    {
        "Restaurant Name": "Sushi World",
        "Cuisine": "Indian",
        "Location": "Seattle",
        "Rating": 1
    },
    {
        "Restaurant Name": "Taco Town",
        "Cuisine": "Mediterranean",
        "Location": "New York",
        "Rating": 2
    },
    {
        "Restaurant Name": "Pasta Palace",
        "Cuisine": "Mexican",
        "Location": "Seattle",
        "Rating": 2
    },
    {
        "Restaurant Name": "Taco Town",
        "Cuisine": "Italian",
        "Location": "Seattle",
        "Rating": 5
    },
    {
        "Restaurant Name": "Taco Town",
        "Cuisine": "Italian",
        "Location": "Houston",
        "Rating": 1
    }
]
<end>Please transform the following csv data into PLAIN TEXT:
Birth Month,City
January,Los Angeles
July,Phoenix
March,El Paso
April,Oklahoma City
<start>
Birth Month: January | City: Los Angeles
Birth Month: July | City: Phoenix
Birth Month: March | City: El Paso
Birth Month: April | City: Oklahoma City
<end>Transform this json structure to a Csv format:
[
    {
        "Company": "FinanceTrust",
        "Date": "2013-06-02",
        "Open Price": 462.1,
        "Close Price": 968.18,
        "High Price": 968.18,
        "Volume": 4953071
    },
    {
        "Company": "BioLife",
        "Date": "2021-07-14",
        "Open Price": 887.23,
        "Close Price": 81.54,
        "High Price": 887.23,
        "Volume": 8603197
    },
    {
        "Company": "HealthGen",
        "Date": "2013-04-23",
        "Open Price": 885.33,
        "Close Price": 885.33,
        "High Price": 885.33,
        "Volume": 3746212
    },
    {
        "Company": "FinanceTrust",
        "Date": "2018-01-07",
        "Open Price": 1117.67,
        "Close Price": 337.26,
        "High Price": 1117.67,
        "Volume": 8603197
    },
    {
        "Company": "MediaGroup",
        "Date": "2011-09-04",
        "Open Price": 28.25,
        "Close Price": 598.97,
        "High Price": 598.97,
        "Volume": 5620186
    },
    {
        "Company": "MediaGroup",
        "Date": "2016-06-18",
        "Open Price": 28.25,
        "Close Price": 491.8,
        "High Price": 1345.78,
        "Volume": 8696869
    },
    {
        "Company": "AeroSystems",
        "Date": "2018-03-06",
        "Open Price": 454.6,
        "Close Price": 591.77,
        "High Price": 591.77,
        "Volume": 1154904
    },
    {
        "Company": "AeroSystems",
        "Date": "2014-03-14",
        "Open Price": 1412.73,
        "Close Price": 642.13,
        "High Price": 1412.73,
        "Volume": 1506046
    }
]<start>
Company,Date,Open Price,Close Price,High Price,Volume
FinanceTrust,2013-06-02,462.1,968.18,968.18,4953071
BioLife,2021-07-14,887.23,81.54,887.23,8603197
HealthGen,2013-04-23,885.33,885.33,885.33,3746212
FinanceTrust,2018-01-07,1117.67,337.26,1117.67,8603197
MediaGroup,2011-09-04,28.25,598.97,598.97,5620186
MediaGroup,2016-06-18,28.25,491.8,1345.78,8696869
AeroSystems,2018-03-06,454.6,591.77,591.77,1154904
AeroSystems,2014-03-14,1412.73,642.13,1412.73,1506046
<end>Can you change this plain text into Json?
Company: TechnoCorp | Date: 2010-08-03 | Close Price: 1316.23 | High Price: 1443.5 | Low Price: 1082.24
Company: AutoMotive | Date: 2020-04-20 | Close Price: 1014.83 | High Price: 1318.25 | Low Price: 293.67
Company: GreenEnergy | Date: 2013-05-14 | Close Price: 199.28 | High Price: 1014.83 | Low Price: 199.28
Company: TechnoCorp | Date: 2022-12-06 | Close Price: 407.21 | High Price: 1105.0 | Low Price: 407.21
Company: GreenEnergy | Date: 2022-12-19 | Close Price: 926.03 | High Price: 1318.25 | Low Price: 926.03
Company: FoodChain | Date: 2012-12-18 | Close Price: 1127.89 | High Price: 1127.89 | Low Price: 294.22
Company: HealthGen | Date: 2015-05-06 | Close Price: 152.95 | High Price: 1390.08 | Low Price: 104.49
Company: FoodChain | Date: 2012-11-04 | Close Price: 53.37 | High Price: 1027.89 | Low Price: 53.37
Company: BioLife | Date: 2011-10-28 | Close Price: 1342.1 | High Price: 1342.1 | Low Price: 644.3
Company: TechnoCorp | Date: 2011-04-01 | Close Price: 48.52 | High Price: 644.77 | Low Price: 48.52
<start>
[
    {
        "Company": "TechnoCorp",
        "Date": "2010-08-03",
        "Close Price": 1316.23,
        "High Price": 1443.5,
        "Low Price": 1082.24
    },
    {
        "Company": "AutoMotive",
        "Date": "2020-04-20",
        "Close Price": 1014.83,
        "High Price": 1318.25,
        "Low Price": 293.67
    },
    {
        "Company": "GreenEnergy",
        "Date": "2013-05-14",
        "Close Price": 199.28,
        "High Price": 1014.83,
        "Low Price": 199.28
    },
    {
        "Company": "TechnoCorp",
        "Date": "2022-12-06",
        "Close Price": 407.21,
        "High Price": 1105.0,
        "Low Price": 407.21
    },
    {
        "Company": "GreenEnergy",
        "Date": "2022-12-19",
        "Close Price": 926.03,
        "High Price": 1318.25,
        "Low Price": 926.03
    },
    {
        "Company": "FoodChain",
        "Date": "2012-12-18",
        "Close Price": 1127.89,
        "High Price": 1127.89,
        "Low Price": 294.22
    },
    {
        "Company": "HealthGen",
        "Date": "2015-05-06",
        "Close Price": 152.95,
        "High Price": 1390.08,
        "Low Price": 104.49
    },
    {
        "Company": "FoodChain",
        "Date": "2012-11-04",
        "Close Price": 53.37,
        "High Price": 1027.89,
        "Low Price": 53.37
    },
    {
        "Company": "BioLife",
        "Date": "2011-10-28",
        "Close Price": 1342.1,
        "High Price": 1342.1,
        "Low Price": 644.3
    },
    {
        "Company": "TechnoCorp",
        "Date": "2011-04-01",
        "Close Price": 48.52,
        "High Price": 644.77,
        "Low Price": 48.52
    }
]
<end>Please transform the following MARKDOWN data into Json:
| Name | Age | Income |
| --- | --- | --- |
| Terry | 45 | 220000 |
| Liam | 18 | 115000 |
| Jayden | 56 | 260000 |
| Ruben | 51 | 310000 |
| Joseph | 46 | 385000 |
| Melody | 25 | 405000 |
| Dick | 26 | 305000 |<start>
[
    {
        "Name": "Terry",
        "Age": 45,
        "Income": 220000
    },
    {
        "Name": "Liam",
        "Age": 18,
        "Income": 115000
    },
    {
        "Name": "Jayden",
        "Age": 56,
        "Income": 260000
    },
    {
        "Name": "Ruben",
        "Age": 51,
        "Income": 310000
    },
    {
        "Name": "Joseph",
        "Age": 46,
        "Income": 385000
    },
    {
        "Name": "Melody",
        "Age": 25,
        "Income": 405000
    },
    {
        "Name": "Dick",
        "Age": 26,
        "Income": 305000
    }
]
<end>Please transform the following MARKDOWN data into Json:
| Company | Stock Price | Quarter |
| --- | --- | --- |
| GlobalTrade | 833.95 | Q1 |
| GlobalTrade | 293.24 | Q4 |
| EcoEnergy | 603.5 | Q4 |
| FinanceWorks | 883.29 | Q1 |
| HealthPlus | 337.16 | Q1 |<start>
[
    {
        "Company": "GlobalTrade",
        "Stock Price": 833.95,
        "Quarter": "Q1"
    },
    {
        "Company": "GlobalTrade",
        "Stock Price": 293.24,
        "Quarter": "Q4"
    },
    {
        "Company": "EcoEnergy",
        "Stock Price": 603.5,
        "Quarter": "Q4"
    },
    {
        "Company": "FinanceWorks",
        "Stock Price": 883.29,
        "Quarter": "Q1"
    },
    {
        "Company": "HealthPlus",
        "Stock Price": 337.16,
        "Quarter": "Q1"
    }
]
<end>Convert this yaml to csv:
- Average Latency (ms): 57.05
  Connection Count: 120
  Timestamp: '2022-07-18 02:15:46'
- Average Latency (ms): 47.16
  Connection Count: 337
  Timestamp: '2023-04-18 09:04:04'
- Average Latency (ms): 32.3
  Connection Count: 103
  Timestamp: '2023-04-20 02:42:32'
- Average Latency (ms): 9.29
  Connection Count: 223
  Timestamp: '2021-01-01 06:54:01'
- Average Latency (ms): 95.61
  Connection Count: 448
  Timestamp: '2021-05-01 21:13:59'
- Average Latency (ms): 67.14
  Connection Count: 474
  Timestamp: '2022-01-07 07:47:56'
<start>
Connection Count,Average Latency (ms),Timestamp
120,57.05,2022-07-18 02:15:46
337,47.16,2023-04-18 09:04:04
103,32.3,2023-04-20 02:42:32
223,9.29,2021-01-01 06:54:01
448,95.61,2021-05-01 21:13:59
474,67.14,2022-01-07 07:47:56
<end>Transform this yaml structure to a markdown format:
- Battery Level (%): 40.4
  Device Type: Light Sensor
  Location: Garden
  Reading Value: -10.69
- Battery Level (%): 68.2
  Device Type: Motion Detector
  Location: Garden
  Reading Value: 34.87
- Battery Level (%): 83.7
  Device Type: Motion Detector
  Location: Hallway
  Reading Value: 79.94
- Battery Level (%): 18.0
  Device Type: Light Sensor
  Location: Garage
  Reading Value: 76.51
<start>
| Device Type | Location | Battery Level (%) | Reading Value |
| --- | --- | --- | --- |
| Light Sensor | Garden | 40.4 | -10.69 |
| Motion Detector | Garden | 68.2 | 34.87 |
| Motion Detector | Hallway | 83.7 | 79.94 |
| Light Sensor | Garage | 18.0 | 76.51 |
<end>Here's some csv data, can you convert it to plain text?
Name,Age
Kaleb,40
Dick,39
Ira,19
Brittany,55
Earnest,51
<start>
Name: Kaleb | Age: 40
Name: Dick | Age: 39
Name: Ira | Age: 19
Name: Brittany | Age: 55
Name: Earnest | Age: 51
<end>Here's some Yml data, can you convert it to Markdown?
- Humidity (%): 72
  Location: Houston
  Wind Speed (km/h): 8.7
- Humidity (%): 65
  Location: Los Angeles
  Wind Speed (km/h): 0.0
- Humidity (%): 30
  Location: Miami
  Wind Speed (km/h): 8.6
- Humidity (%): 71
  Location: New York
  Wind Speed (km/h): 10.4
- Humidity (%): 96
  Location: Houston
  Wind Speed (km/h): 12.9
- Humidity (%): 56
  Location: Chicago
  Wind Speed (km/h): 15.5
- Humidity (%): 54
  Location: Phoenix
  Wind Speed (km/h): 4.4
- Humidity (%): 55
  Location: Seattle
  Wind Speed (km/h): 19.4
<start>
| Location | Humidity (%) | Wind Speed (km/h) |
| --- | --- | --- |
| Houston | 72 | 8.7 |
| Los Angeles | 65 | 0.0 |
| Miami | 30 | 8.6 |
| New York | 71 | 10.4 |
| Houston | 96 | 12.9 |
| Chicago | 56 | 15.5 |
| Phoenix | 54 | 4.4 |
| Seattle | 55 | 19.4 |
<end>Convert this json to Plain text:
[
    {
        "Database Name": "InventoryDB",
        "Queries per Second": 4175.83,
        "Cache Hit Ratio (%)": 78.47,
        "Connection Count": 485,
        "Average Latency (ms)": 94.75,
        "Timestamp": "2023-07-03 20:13:07"
    },
    {
        "Database Name": "LogsDB",
        "Queries per Second": 1855.49,
        "Cache Hit Ratio (%)": 88.98,
        "Connection Count": 41,
        "Average Latency (ms)": 41.31,
        "Timestamp": "2023-01-27 11:44:55"
    },
    {
        "Database Name": "OrdersDB",
        "Queries per Second": 652.27,
        "Cache Hit Ratio (%)": 79.97,
        "Connection Count": 196,
        "Average Latency (ms)": 30.05,
        "Timestamp": "2022-12-09 09:45:00"
    },
    {
        "Database Name": "ProductsDB",
        "Queries per Second": 4928.84,
        "Cache Hit Ratio (%)": 92.25,
        "Connection Count": 234,
        "Average Latency (ms)": 27.43,
        "Timestamp": "2023-08-22 07:32:25"
    },
    {
        "Database Name": "MetricsDB",
        "Queries per Second": 392.52,
        "Cache Hit Ratio (%)": 73.45,
        "Connection Count": 154,
        "Average Latency (ms)": 39.49,
        "Timestamp": "2022-08-19 12:30:24"
    },
    {
        "Database Name": "AnalyticsDB",
        "Queries per Second": 462.06,
        "Cache Hit Ratio (%)": 70.55,
        "Connection Count": 409,
        "Average Latency (ms)": 52.62,
        "Timestamp": "2022-01-23 05:46:47"
    },
    {
        "Database Name": "ProductsDB",
        "Queries per Second": 2093.49,
        "Cache Hit Ratio (%)": 85.56,
        "Connection Count": 154,
        "Average Latency (ms)": 80.23,
        "Timestamp": "2022-12-17 19:44:42"
    },
    {
        "Database Name": "ProductsDB",
        "Queries per Second": 1093.56,
        "Cache Hit Ratio (%)": 84.67,
        "Connection Count": 488,
        "Average Latency (ms)": 41.65,
        "Timestamp": "2023-09-21 05:34:37"
    },
    {
        "Database Name": "AnalyticsDB",
        "Queries per Second": 1395.23,
        "Cache Hit Ratio (%)": 99.36,
        "Connection Count": 388,
        "Average Latency (ms)": 57.66,
        "Timestamp": "2021-10-16 14:39:53"
    }
]<start>
Database Name: InventoryDB | Queries per Second: 4175.83 | Cache Hit Ratio (%): 78.47 | Connection Count: 485 | Average Latency (ms): 94.75 | Timestamp: 2023-07-03 20:13:07
Database Name: LogsDB | Queries per Second: 1855.49 | Cache Hit Ratio (%): 88.98 | Connection Count: 41 | Average Latency (ms): 41.31 | Timestamp: 2023-01-27 11:44:55
Database Name: OrdersDB | Queries per Second: 652.27 | Cache Hit Ratio (%): 79.97 | Connection Count: 196 | Average Latency (ms): 30.05 | Timestamp: 2022-12-09 09:45:00
Database Name: ProductsDB | Queries per Second: 4928.84 | Cache Hit Ratio (%): 92.25 | Connection Count: 234 | Average Latency (ms): 27.43 | Timestamp: 2023-08-22 07:32:25
Database Name: MetricsDB | Queries per Second: 392.52 | Cache Hit Ratio (%): 73.45 | Connection Count: 154 | Average Latency (ms): 39.49 | Timestamp: 2022-08-19 12:30:24
Database Name: AnalyticsDB | Queries per Second: 462.06 | Cache Hit Ratio (%): 70.55 | Connection Count: 409 | Average Latency (ms): 52.62 | Timestamp: 2022-01-23 05:46:47
Database Name: ProductsDB | Queries per Second: 2093.49 | Cache Hit Ratio (%): 85.56 | Connection Count: 154 | Average Latency (ms): 80.23 | Timestamp: 2022-12-17 19:44:42
Database Name: ProductsDB | Queries per Second: 1093.56 | Cache Hit Ratio (%): 84.67 | Connection Count: 488 | Average Latency (ms): 41.65 | Timestamp: 2023-09-21 05:34:37
Database Name: AnalyticsDB | Queries per Second: 1395.23 | Cache Hit Ratio (%): 99.36 | Connection Count: 388 | Average Latency (ms): 57.66 | Timestamp: 2021-10-16 14:39:53
<end>Here's some Json data, can you convert it to YAML?
[
    {
        "Database Name": "SessionsDB",
        "Cache Hit Ratio (%)": 95.28,
        "Average Latency (ms)": 23.36,
        "Timestamp": "2023-11-19 00:08:02"
    },
    {
        "Database Name": "SalesDB",
        "Cache Hit Ratio (%)": 82.03,
        "Average Latency (ms)": 69.11,
        "Timestamp": "2021-03-17 02:47:35"
    },
    {
        "Database Name": "InventoryDB",
        "Cache Hit Ratio (%)": 98.73,
        "Average Latency (ms)": 80.31,
        "Timestamp": "2021-09-26 06:01:46"
    },
    {
        "Database Name": "InventoryDB",
        "Cache Hit Ratio (%)": 70.46,
        "Average Latency (ms)": 6.77,
        "Timestamp": "2022-06-13 02:01:04"
    },
    {
        "Database Name": "LogsDB",
        "Cache Hit Ratio (%)": 71.2,
        "Average Latency (ms)": 60.29,
        "Timestamp": "2023-10-20 10:55:57"
    },
    {
        "Database Name": "MetricsDB",
        "Cache Hit Ratio (%)": 93.28,
        "Average Latency (ms)": 65.27,
        "Timestamp": "2022-12-27 22:50:31"
    },
    {
        "Database Name": "OrdersDB",
        "Cache Hit Ratio (%)": 99.36,
        "Average Latency (ms)": 78.09,
        "Timestamp": "2022-05-03 03:42:57"
    },
    {
        "Database Name": "InventoryDB",
        "Cache Hit Ratio (%)": 86.97,
        "Average Latency (ms)": 23.01,
        "Timestamp": "2021-08-21 08:52:06"
    },
    {
        "Database Name": "ProductsDB",
        "Cache Hit Ratio (%)": 86.05,
        "Average Latency (ms)": 26.53,
        "Timestamp": "2021-05-10 11:58:08"
    }
]<start>
- Average Latency (ms): 23.36
  Cache Hit Ratio (%): 95.28
  Database Name: SessionsDB
  Timestamp: '2023-11-19 00:08:02'
- Average Latency (ms): 69.11
  Cache Hit Ratio (%): 82.03
  Database Name: SalesDB
  Timestamp: '2021-03-17 02:47:35'
- Average Latency (ms): 80.31
  Cache Hit Ratio (%): 98.73
  Database Name: InventoryDB
  Timestamp: '2021-09-26 06:01:46'
- Average Latency (ms): 6.77
  Cache Hit Ratio (%): 70.46
  Database Name: InventoryDB
  Timestamp: '2022-06-13 02:01:04'
- Average Latency (ms): 60.29
  Cache Hit Ratio (%): 71.2
  Database Name: LogsDB
  Timestamp: '2023-10-20 10:55:57'
- Average Latency (ms): 65.27
  Cache Hit Ratio (%): 93.28
  Database Name: MetricsDB
  Timestamp: '2022-12-27 22:50:31'
- Average Latency (ms): 78.09
  Cache Hit Ratio (%): 99.36
  Database Name: OrdersDB
  Timestamp: '2022-05-03 03:42:57'
- Average Latency (ms): 23.01
  Cache Hit Ratio (%): 86.97
  Database Name: InventoryDB
  Timestamp: '2021-08-21 08:52:06'
- Average Latency (ms): 26.53
  Cache Hit Ratio (%): 86.05
  Database Name: ProductsDB
  Timestamp: '2021-05-10 11:58:08'
<end>Can you change this YAML into csv?
- Condition: Windy
  Day: Wednesday
  Humidity (%): 50
  Temperature (C): 19.3
  Wind Speed (km/h): 11.8
- Condition: Foggy
  Day: Sunday
  Humidity (%): 23
  Temperature (C): 23.2
  Wind Speed (km/h): 23.0
- Condition: Rainy
  Day: Friday
  Humidity (%): 63
  Temperature (C): 32.8
  Wind Speed (km/h): 17.2
- Condition: Sunny
  Day: Wednesday
  Humidity (%): 53
  Temperature (C): 20.1
  Wind Speed (km/h): 15.8
- Condition: Snowy
  Day: Friday
  Humidity (%): 84
  Temperature (C): 6.5
  Wind Speed (km/h): 8.0
- Condition: Foggy
  Day: Sunday
  Humidity (%): 86
  Temperature (C): 2.2
  Wind Speed (km/h): 21.5
- Condition: Rainy
  Day: Saturday
  Humidity (%): 65
  Temperature (C): 16.5
  Wind Speed (km/h): 15.3
- Condition: Stormy
  Day: Monday
  Humidity (%): 25
  Temperature (C): -1.8
  Wind Speed (km/h): 26.5
<start>
Condition,Temperature (C),Humidity (%),Wind Speed (km/h),Day
Windy,19.3,50,11.8,Wednesday
Foggy,23.2,23,23.0,Sunday
Rainy,32.8,63,17.2,Friday
Sunny,20.1,53,15.8,Wednesday
Snowy,6.5,84,8.0,Friday
Foggy,2.2,86,21.5,Sunday
Rainy,16.5,65,15.3,Saturday
Stormy,-1.8,25,26.5,Monday
<end>Please transform the following yaml data into CSV:
- Condition: Foggy
  Day: Thursday
  Humidity (%): 71
  Location: Houston
  Temperature (C): 7.1
  Wind Speed (km/h): 26.2
- Condition: Windy
  Day: Sunday
  Humidity (%): 76
  Location: Miami
  Temperature (C): 33.7
  Wind Speed (km/h): 26.8
- Condition: Snowy
  Day: Tuesday
  Humidity (%): 43
  Location: Seattle
  Temperature (C): 8.8
  Wind Speed (km/h): 21.8
<start>
Location,Condition,Temperature (C),Humidity (%),Wind Speed (km/h),Day
Houston,Foggy,7.1,71,26.2,Thursday
Miami,Windy,33.7,76,26.8,Sunday
Seattle,Snowy,8.8,43,21.8,Tuesday
<end>Can you change this yaml into plain text?
- Average Latency (ms): 11.86
  Cache Hit Ratio (%): 89.44
  Connection Count: 98
  Database Name: SalesDB
  Queries per Second: 1608.18
- Average Latency (ms): 22.64
  Cache Hit Ratio (%): 96.18
  Connection Count: 292
  Database Name: LogsDB
  Queries per Second: 997.65
- Average Latency (ms): 99.94
  Cache Hit Ratio (%): 73.36
  Connection Count: 106
  Database Name: MetricsDB
  Queries per Second: 2488.69
- Average Latency (ms): 83.09
  Cache Hit Ratio (%): 85.15
  Connection Count: 440
  Database Name: OrdersDB
  Queries per Second: 2707.61
- Average Latency (ms): 36.59
  Cache Hit Ratio (%): 95.36
  Connection Count: 416
  Database Name: OrdersDB
  Queries per Second: 3813.44
<start>
Database Name: SalesDB | Queries per Second: 1608.18 | Cache Hit Ratio (%): 89.44 | Connection Count: 98 | Average Latency (ms): 11.86
Database Name: LogsDB | Queries per Second: 997.65 | Cache Hit Ratio (%): 96.18 | Connection Count: 292 | Average Latency (ms): 22.64
Database Name: MetricsDB | Queries per Second: 2488.69 | Cache Hit Ratio (%): 73.36 | Connection Count: 106 | Average Latency (ms): 99.94
Database Name: OrdersDB | Queries per Second: 2707.61 | Cache Hit Ratio (%): 85.15 | Connection Count: 440 | Average Latency (ms): 83.09
Database Name: OrdersDB | Queries per Second: 3813.44 | Cache Hit Ratio (%): 95.36 | Connection Count: 416 | Average Latency (ms): 36.59
<end>Can you change this csv into Yaml?
Queries per Second,Cache Hit Ratio (%),Average Latency (ms),Timestamp
3021.81,99.68,21.71,2022-12-12 17:56:29
609.58,88.19,65.95,2021-07-02 09:49:36
4161.96,70.56,13.83,2023-05-13 14:08:12
4161.96,72.45,82.52,2023-06-13 10:05:20
2517.38,78.34,20.42,2022-09-26 12:02:02
<start>
- Average Latency (ms): 21.71
  Cache Hit Ratio (%): 99.68
  Queries per Second: 3021.81
  Timestamp: '2022-12-12 17:56:29'
- Average Latency (ms): 65.95
  Cache Hit Ratio (%): 88.19
  Queries per Second: 609.58
  Timestamp: '2021-07-02 09:49:36'
- Average Latency (ms): 13.83
  Cache Hit Ratio (%): 70.56
  Queries per Second: 4161.96
  Timestamp: '2023-05-13 14:08:12'
- Average Latency (ms): 82.52
  Cache Hit Ratio (%): 72.45
  Queries per Second: 4161.96
  Timestamp: '2023-06-13 10:05:20'
- Average Latency (ms): 20.42
  Cache Hit Ratio (%): 78.34
  Queries per Second: 2517.38
  Timestamp: '2022-09-26 12:02:02'
<end>Convert this markdown to plain text:
| Restaurant Name | Cuisine | Location | Rating | Price Range |
| --- | --- | --- | --- | --- |
| BBQ Barn | Italian | Chicago | 1 | $$$ |
| Vegan Delight | Chinese | Chicago | 1 | $$$ |
| Pizza Planet | Mexican | Chicago | 1 | $$$$$ |<start>
Restaurant Name: BBQ Barn | Cuisine: Italian | Location: Chicago | Rating: 1 | Price Range: $$$
Restaurant Name: Vegan Delight | Cuisine: Chinese | Location: Chicago | Rating: 1 | Price Range: $$$
Restaurant Name: Pizza Planet | Cuisine: Mexican | Location: Chicago | Rating: 1 | Price Range: $$$$$
<end>Here's some CSV data, can you convert it to markdown?
Condition,Temperature (C),Wind Speed (km/h),Day
Cloudy,21.0,5.9,Friday
Windy,8.8,0.4,Sunday
Sunny,8.7,22.7,Tuesday
Rainy,38.1,22.6,Sunday
Foggy,8.9,9.2,Thursday
Stormy,36.6,17.6,Friday
Windy,23.8,15.9,Sunday
Foggy,33.1,17.6,Wednesday
Cloudy,11.9,27.0,Friday
<start>
| Condition | Temperature (C) | Wind Speed (km/h) | Day |
| --- | --- | --- | --- |
| Cloudy | 21.0 | 5.9 | Friday |
| Windy | 8.8 | 0.4 | Sunday |
| Sunny | 8.7 | 22.7 | Tuesday |
| Rainy | 38.1 | 22.6 | Sunday |
| Foggy | 8.9 | 9.2 | Thursday |
| Stormy | 36.6 | 17.6 | Friday |
| Windy | 23.8 | 15.9 | Sunday |
| Foggy | 33.1 | 17.6 | Wednesday |
| Cloudy | 11.9 | 27.0 | Friday |
<end>Please transform the following markdown data into CSV:
| Date | Open Price | Close Price | High Price | Volume |
| --- | --- | --- | --- | --- |
| 2023-06-01 | 128.61 | 820.74 | 1333.56 | 9896153 |
| 2015-09-25 | 325.57 | 1444.99 | 1444.99 | 6681187 |
| 2013-07-17 | 325.57 | 590.49 | 590.49 | 1752098 |<start>
Date,Open Price,Close Price,High Price,Volume
2023-06-01,128.61,820.74,1333.56,9896153
2015-09-25,325.57,1444.99,1444.99,6681187
2013-07-17,325.57,590.49,590.49,1752098
<end>Transform this plain text structure to a markdown format:
SKU: SKU-1018 | Price: 42.53 | Stock Quantity: 344 | Category: Automotive
SKU: SKU-1055 | Price: 184.25 | Stock Quantity: 429 | Category: Sports
SKU: SKU-1076 | Price: 329.46 | Stock Quantity: 270 | Category: Electronics
SKU: SKU-1023 | Price: 287.48 | Stock Quantity: 325 | Category: Electronics
SKU: SKU-1093 | Price: 114.4 | Stock Quantity: 337 | Category: Household
<start>
| SKU | Price | Stock Quantity | Category |
| --- | --- | --- | --- |
| SKU-1018 | 42.53 | 344 | Automotive |
| SKU-1055 | 184.25 | 429 | Sports |
| SKU-1076 | 329.46 | 270 | Electronics |
| SKU-1023 | 287.48 | 325 | Electronics |
| SKU-1093 | 114.4 | 337 | Household |
<end>Here's some markdown data, can you convert it to Yml?
| Name | Age | Birth Month |
| --- | --- | --- |
| Nina | 49 | May |
| Meredith | 55 | November |
| Arnold | 31 | June |
| Cristian | 36 | May |
| Myrtle | 33 | May |<start>
- Age: 49
  Birth Month: May
  Name: Nina
- Age: 55
  Birth Month: November
  Name: Meredith
- Age: 31
  Birth Month: June
  Name: Arnold
- Age: 36
  Birth Month: May
  Name: Cristian
- Age: 33
  Birth Month: May
  Name: Myrtle
<end>Convert this yaml to MARKDOWN:
- Author: Galen Starfire
  Genre: Mystery
  Publication Year: 1983
  Rating: 3.3
  Title: Echoes of Eternity
- Author: Draven Blackthorn
  Genre: Thriller
  Publication Year: 1997
  Rating: 3.4
  Title: Legends of the Rift
- Author: Draven Blackthorn
  Genre: Science Fiction
  Publication Year: 1989
  Rating: 2.2
  Title: Echoes of Eternity
- Author: Rowan Ashborne
  Genre: Romance
  Publication Year: 1989
  Rating: 3.0
  Title: Echoes of Eternity
- Author: Orion Frostblade
  Genre: Mystery
  Publication Year: 1977
  Rating: 4.4
  Title: The Last Sky
<start>
| Title | Author | Genre | Publication Year | Rating |
| --- | --- | --- | --- | --- |
| Echoes of Eternity | Galen Starfire | Mystery | 1983 | 3.3 |
| Legends of the Rift | Draven Blackthorn | Thriller | 1997 | 3.4 |
| Echoes of Eternity | Draven Blackthorn | Science Fiction | 1989 | 2.2 |
| Echoes of Eternity | Rowan Ashborne | Romance | 1989 | 3.0 |
| The Last Sky | Orion Frostblade | Mystery | 1977 | 4.4 |
<end>Please transform the following json data into markdown:
[
    {
        "Cuisine": "American",
        "Location": "Phoenix",
        "Rating": 5,
        "Price Range": "$"
    },
    {
        "Cuisine": "Italian",
        "Location": "Seattle",
        "Rating": 3,
        "Price Range": "$$$$$"
    },
    {
        "Cuisine": "Mexican",
        "Location": "New York",
        "Rating": 5,
        "Price Range": "$"
    },
    {
        "Cuisine": "Indian",
        "Location": "Houston",
        "Rating": 5,
        "Price Range": "$$$$"
    }
]<start>
| Cuisine | Location | Rating | Price Range |
| --- | --- | --- | --- |
| American | Phoenix | 5 | $ |
| Italian | Seattle | 3 | $$$$$ |
| Mexican | New York | 5 | $ |
| Indian | Houston | 5 | $$$$ |
<end>Please transform the following MARKDOWN data into json:
| Title | Director | Genre | Box Office Earnings (M) |
| --- | --- | --- | --- |
| Escape from Earth | Orin Shadowalker | Comedy | 956.86 |
| The Great Expedition | Mara Moonshadow | Adventure | 879.08 |
| Escape from Earth | Zara Stormrider | Fantasy | 731.0 |
| The Endless Horizon | Rylan Frostblade | Sci-Fi | 635.48 |
| Escape from Earth | Talon Blackthorn | Adventure | 438.9 |
| The Great Expedition | Orin Shadowalker | Fantasy | 247.99 |<start>
[
    {
        "Title": "Escape from Earth",
        "Director": "Orin Shadowalker",
        "Genre": "Comedy",
        "Box Office Earnings (M)": 956.86
    },
    {
        "Title": "The Great Expedition",
        "Director": "Mara Moonshadow",
        "Genre": "Adventure",
        "Box Office Earnings (M)": 879.08
    },
    {
        "Title": "Escape from Earth",
        "Director": "Zara Stormrider",
        "Genre": "Fantasy",
        "Box Office Earnings (M)": 731.0
    },
    {
        "Title": "The Endless Horizon",
        "Director": "Rylan Frostblade",
        "Genre": "Sci-Fi",
        "Box Office Earnings (M)": 635.48
    },
    {
        "Title": "Escape from Earth",
        "Director": "Talon Blackthorn",
        "Genre": "Adventure",
        "Box Office Earnings (M)": 438.9
    },
    {
        "Title": "The Great Expedition",
        "Director": "Orin Shadowalker",
        "Genre": "Fantasy",
        "Box Office Earnings (M)": 247.99
    }
]
<end>Transform this json structure to a markdown format:
[
    {
        "Date": "2013-10-24",
        "Open Price": 554.65,
        "Close Price": 1271.16,
        "High Price": 1341.13,
        "Low Price": 184.39,
        "Volume": 8129230
    },
    {
        "Date": "2017-11-06",
        "Open Price": 273.07,
        "Close Price": 704.01,
        "High Price": 763.31,
        "Low Price": 273.07,
        "Volume": 7722333
    },
    {
        "Date": "2016-06-08",
        "Open Price": 1349.42,
        "Close Price": 554.65,
        "High Price": 1349.42,
        "Low Price": 471.12,
        "Volume": 2200012
    },
    {
        "Date": "2010-02-14",
        "Open Price": 1271.16,
        "Close Price": 1201.4,
        "High Price": 1271.16,
        "Low Price": 639.39,
        "Volume": 3818145
    },
    {
        "Date": "2023-04-11",
        "Open Price": 966.36,
        "Close Price": 842.18,
        "High Price": 966.36,
        "Low Price": 285.0,
        "Volume": 8740179
    }
]<start>
| Date | Open Price | Close Price | High Price | Low Price | Volume |
| --- | --- | --- | --- | --- | --- |
| 2013-10-24 | 554.65 | 1271.16 | 1341.13 | 184.39 | 8129230 |
| 2017-11-06 | 273.07 | 704.01 | 763.31 | 273.07 | 7722333 |
| 2016-06-08 | 1349.42 | 554.65 | 1349.42 | 471.12 | 2200012 |
| 2010-02-14 | 1271.16 | 1201.4 | 1271.16 | 639.39 | 3818145 |
| 2023-04-11 | 966.36 | 842.18 | 966.36 | 285.0 | 8740179 |
<end>Here's some json data, can you convert it to csv?
[
    {
        "Distance (miles)": 1274.0,
        "Duration (hours)": 37.6,
        "Fuel Used (gallons)": 80.8
    },
    {
        "Distance (miles)": 2332.5,
        "Duration (hours)": 69.4,
        "Fuel Used (gallons)": 81.5
    },
    {
        "Distance (miles)": 2677.3,
        "Duration (hours)": 38.0,
        "Fuel Used (gallons)": 32.8
    },
    {
        "Distance (miles)": 1470.9,
        "Duration (hours)": 9.9,
        "Fuel Used (gallons)": 41.1
    },
    {
        "Distance (miles)": 1526.1,
        "Duration (hours)": 33.9,
        "Fuel Used (gallons)": 26.8
    },
    {
        "Distance (miles)": 1460.6,
        "Duration (hours)": 37.0,
        "Fuel Used (gallons)": 28.2
    },
    {
        "Distance (miles)": 945.9,
        "Duration (hours)": 68.6,
        "Fuel Used (gallons)": 81.8
    },
    {
        "Distance (miles)": 2499.4,
        "Duration (hours)": 37.6,
        "Fuel Used (gallons)": 27.4
    },
    {
        "Distance (miles)": 1611.2,
        "Duration (hours)": 36.3,
        "Fuel Used (gallons)": 30.1
    }
]<start>
Distance (miles),Duration (hours),Fuel Used (gallons)
1274.0,37.6,80.8
2332.5,69.4,81.5
2677.3,38.0,32.8
1470.9,9.9,41.1
1526.1,33.9,26.8
1460.6,37.0,28.2
945.9,68.6,81.8
2499.4,37.6,27.4
1611.2,36.3,30.1
<end>Here's some csv data, can you convert it to plain text?
Trip Name,End Location,Distance (miles),Duration (hours),Fuel Used (gallons)
Valley Voyage,Phoenix,127.1,1.1,14.1
Forest Journey,Phoenix,1402.9,31.2,87.6
Mountain Adventure,Phoenix,806.3,31.0,18.8
<start>
Trip Name: Valley Voyage | End Location: Phoenix | Distance (miles): 127.1 | Duration (hours): 1.1 | Fuel Used (gallons): 14.1
Trip Name: Forest Journey | End Location: Phoenix | Distance (miles): 1402.9 | Duration (hours): 31.2 | Fuel Used (gallons): 87.6
Trip Name: Mountain Adventure | End Location: Phoenix | Distance (miles): 806.3 | Duration (hours): 31.0 | Fuel Used (gallons): 18.8
<end>Convert this plain text to Yaml:
Name: Alexa | Birth Month: September | City: New York | Income: 385000
Name: Sean | Birth Month: August | City: Portland | Income: 400000
Name: Lillian | Birth Month: April | City: Jacksonville | Income: 225000
Name: Sergio | Birth Month: January | City: Louisville | Income: 280000
Name: Cheyenne | Birth Month: December | City: Baltimore | Income: 65000
Name: Quinn | Birth Month: August | City: Detroit | Income: 375000
Name: Leila | Birth Month: March | City: Boston | Income: 110000
Name: Jada | Birth Month: February | City: Las Vegas | Income: 90000
<start>
- Birth Month: September
  City: New York
  Income: 385000
  Name: Alexa
- Birth Month: August
  City: Portland
  Income: 400000
  Name: Sean
- Birth Month: April
  City: Jacksonville
  Income: 225000
  Name: Lillian
- Birth Month: January
  City: Louisville
  Income: 280000
  Name: Sergio
- Birth Month: December
  City: Baltimore
  Income: 65000
  Name: Cheyenne
- Birth Month: August
  City: Detroit
  Income: 375000
  Name: Quinn
- Birth Month: March
  City: Boston
  Income: 110000
  Name: Leila
- Birth Month: February
  City: Las Vegas
  Income: 90000
  Name: Jada
<end>Transform this YAML structure to a Markdown format:
- Device ID: device-0022
  Device Type: Humidity Sensor
  Location: Office
  Timestamp: '2023-02-18 16:00:36'
- Device ID: device-0041
  Device Type: Motion Detector
  Location: Living Room
  Timestamp: '2021-05-22 16:47:43'
- Device ID: device-0074
  Device Type: Temperature Sensor
  Location: Garden
  Timestamp: '2022-01-25 15:00:35'
- Device ID: device-0095
  Device Type: Light Sensor
  Location: Bathroom
  Timestamp: '2022-02-24 21:03:55'
- Device ID: device-0034
  Device Type: Motion Detector
  Location: Garden
  Timestamp: '2022-06-12 03:36:11'
- Device ID: device-0097
  Device Type: Humidity Sensor
  Location: Office
  Timestamp: '2023-02-25 21:54:43'
- Device ID: device-0076
  Device Type: Light Sensor
  Location: Garage
  Timestamp: '2021-01-09 03:12:51'
- Device ID: device-0020
  Device Type: Temperature Sensor
  Location: Office
  Timestamp: '2023-11-12 06:30:53'
<start>
| Device ID | Device Type | Location | Timestamp |
| --- | --- | --- | --- |
| device-0022 | Humidity Sensor | Office | 2023-02-18 16:00:36 |
| device-0041 | Motion Detector | Living Room | 2021-05-22 16:47:43 |
| device-0074 | Temperature Sensor | Garden | 2022-01-25 15:00:35 |
| device-0095 | Light Sensor | Bathroom | 2022-02-24 21:03:55 |
| device-0034 | Motion Detector | Garden | 2022-06-12 03:36:11 |
| device-0097 | Humidity Sensor | Office | 2023-02-25 21:54:43 |
| device-0076 | Light Sensor | Garage | 2021-01-09 03:12:51 |
| device-0020 | Temperature Sensor | Office | 2023-11-12 06:30:53 |
<end>Convert this markdown to PLAIN TEXT:
| Trip Name | End Location | Distance (miles) | Duration (hours) | Fuel Used (gallons) |
| --- | --- | --- | --- | --- |
| Lakeside Retreat | Miami | 1235.1 | 24.3 | 27.1 |
| Coast to Coast | Phoenix | 1452.6 | 34.3 | 29.8 |
| Desert Drive | Chicago | 1619.4 | 58.0 | 11.1 |
| Highway Odyssey | Miami | 376.8 | 59.7 | 96.9 |
| Valley Voyage | Chicago | 2992.4 | 64.6 | 94.9 |
| Desert Drive | Houston | 2863.4 | 51.5 | 7.0 |
| Historic Route | Los Angeles | 263.8 | 15.0 | 8.5 |
| Highway Odyssey | Denver | 331.4 | 66.6 | 70.3 |
| Coast to Coast | Phoenix | 2981.5 | 13.6 | 8.5 |<start>
Trip Name: Lakeside Retreat | End Location: Miami | Distance (miles): 1235.1 | Duration (hours): 24.3 | Fuel Used (gallons): 27.1
Trip Name: Coast to Coast | End Location: Phoenix | Distance (miles): 1452.6 | Duration (hours): 34.3 | Fuel Used (gallons): 29.8
Trip Name: Desert Drive | End Location: Chicago | Distance (miles): 1619.4 | Duration (hours): 58.0 | Fuel Used (gallons): 11.1
Trip Name: Highway Odyssey | End Location: Miami | Distance (miles): 376.8 | Duration (hours): 59.7 | Fuel Used (gallons): 96.9
Trip Name: Valley Voyage | End Location: Chicago | Distance (miles): 2992.4 | Duration (hours): 64.6 | Fuel Used (gallons): 94.9
Trip Name: Desert Drive | End Location: Houston | Distance (miles): 2863.4 | Duration (hours): 51.5 | Fuel Used (gallons): 7.0
Trip Name: Historic Route | End Location: Los Angeles | Distance (miles): 263.8 | Duration (hours): 15.0 | Fuel Used (gallons): 8.5
Trip Name: Highway Odyssey | End Location: Denver | Distance (miles): 331.4 | Duration (hours): 66.6 | Fuel Used (gallons): 70.3
Trip Name: Coast to Coast | End Location: Phoenix | Distance (miles): 2981.5 | Duration (hours): 13.6 | Fuel Used (gallons): 8.5
<end>Can you change this JSON into MARKDOWN?
[
    {
        "Title": "The Crystal Key",
        "Publication Year": 1982
    },
    {
        "Title": "Whispers of the Abyss",
        "Publication Year": 1977
    },
    {
        "Title": "Echoes of Eternity",
        "Publication Year": 1987
    },
    {
        "Title": "Whispers of the Abyss",
        "Publication Year": 2010
    },
    {
        "Title": "A Journey Through Time",
        "Publication Year": 2023
    },
    {
        "Title": "Tales of the Brave",
        "Publication Year": 1968
    },
    {
        "Title": "The Forgotten World",
        "Publication Year": 1989
    }
]<start>
| Title | Publication Year |
| --- | --- |
| The Crystal Key | 1982 |
| Whispers of the Abyss | 1977 |
| Echoes of Eternity | 1987 |
| Whispers of the Abyss | 2010 |
| A Journey Through Time | 2023 |
| Tales of the Brave | 1968 |
| The Forgotten World | 1989 |
<end>Here's some JSON data, can you convert it to csv?
[
    {
        "Device ID": "device-0016",
        "Location": "Hallway",
        "Battery Level (%)": 56.7,
        "Reading Value": -29.62,
        "Timestamp": "2021-10-06 01:12:40"
    },
    {
        "Device ID": "device-0062",
        "Location": "Garden",
        "Battery Level (%)": 10.3,
        "Reading Value": 84.18,
        "Timestamp": "2023-07-10 00:52:06"
    },
    {
        "Device ID": "device-0056",
        "Location": "Bathroom",
        "Battery Level (%)": 65.5,
        "Reading Value": 63.07,
        "Timestamp": "2021-07-09 15:35:55"
    },
    {
        "Device ID": "device-0036",
        "Location": "Garage",
        "Battery Level (%)": 52.8,
        "Reading Value": 13.89,
        "Timestamp": "2021-09-08 21:40:53"
    },
    {
        "Device ID": "device-0095",
        "Location": "Office",
        "Battery Level (%)": 10.3,
        "Reading Value": -35.82,
        "Timestamp": "2021-06-09 13:40:47"
    },
    {
        "Device ID": "device-0078",
        "Location": "Bathroom",
        "Battery Level (%)": 67.6,
        "Reading Value": 8.41,
        "Timestamp": "2022-02-04 15:16:17"
    }
]<start>
Device ID,Location,Battery Level (%),Reading Value,Timestamp
device-0016,Hallway,56.7,-29.62,2021-10-06 01:12:40
device-0062,Garden,10.3,84.18,2023-07-10 00:52:06
device-0056,Bathroom,65.5,63.07,2021-07-09 15:35:55
device-0036,Garage,52.8,13.89,2021-09-08 21:40:53
device-0095,Office,10.3,-35.82,2021-06-09 13:40:47
device-0078,Bathroom,67.6,8.41,2022-02-04 15:16:17
<end>Transform this CSV structure to a Markdown format:
Name,Birth Month
Peyton,January
Erick,March
Eloise,July
Lisa,August
Lyle,November
Conner,July
Mathew,July
Ariana,June
Victor,August
Emma,October
<start>
| Name | Birth Month |
| --- | --- |
| Peyton | January |
| Erick | March |
| Eloise | July |
| Lisa | August |
| Lyle | November |
| Conner | July |
| Mathew | July |
| Ariana | June |
| Victor | August |
| Emma | October |
<end>Please transform the following MARKDOWN data into Yaml:
| Location | Condition | Humidity (%) | Wind Speed (km/h) | Day |
| --- | --- | --- | --- | --- |
| Los Angeles | Snowy | 29 | 15.0 | Friday |
| Phoenix | Rainy | 100 | 12.7 | Saturday |
| Denver | Snowy | 97 | 1.4 | Saturday |
| Seattle | Snowy | 60 | 10.9 | Wednesday |
| Miami | Snowy | 69 | 16.5 | Thursday |
| Phoenix | Windy | 100 | 21.4 | Monday |<start>
- Condition: Snowy
  Day: Friday
  Humidity (%): 29
  Location: Los Angeles
  Wind Speed (km/h): 15.0
- Condition: Rainy
  Day: Saturday
  Humidity (%): 100
  Location: Phoenix
  Wind Speed (km/h): 12.7
- Condition: Snowy
  Day: Saturday
  Humidity (%): 97
  Location: Denver
  Wind Speed (km/h): 1.4
- Condition: Snowy
  Day: Wednesday
  Humidity (%): 60
  Location: Seattle
  Wind Speed (km/h): 10.9
- Condition: Snowy
  Day: Thursday
  Humidity (%): 69
  Location: Miami
  Wind Speed (km/h): 16.5
- Condition: Windy
  Day: Monday
  Humidity (%): 100
  Location: Phoenix
  Wind Speed (km/h): 21.4
<end>Can you change this json into csv?
[
    {
        "Database Name": "AnalyticsDB",
        "Queries per Second": 3444.18,
        "Cache Hit Ratio (%)": 72.86,
        "Connection Count": 430,
        "Average Latency (ms)": 58.87,
        "Timestamp": "2021-04-04 18:29:39"
    },
    {
        "Database Name": "InventoryDB",
        "Queries per Second": 238.69,
        "Cache Hit Ratio (%)": 96.79,
        "Connection Count": 162,
        "Average Latency (ms)": 61.25,
        "Timestamp": "2022-12-12 13:24:03"
    },
    {
        "Database Name": "MetricsDB",
        "Queries per Second": 3341.99,
        "Cache Hit Ratio (%)": 87.52,
        "Connection Count": 232,
        "Average Latency (ms)": 22.84,
        "Timestamp": "2022-05-15 23:43:01"
    },
    {
        "Database Name": "ProfilesDB",
        "Queries per Second": 73.33,
        "Cache Hit Ratio (%)": 95.3,
        "Connection Count": 447,
        "Average Latency (ms)": 62.96,
        "Timestamp": "2022-11-11 15:47:20"
    }
]<start>
Database Name,Queries per Second,Cache Hit Ratio (%),Connection Count,Average Latency (ms),Timestamp
AnalyticsDB,3444.18,72.86,430,58.87,2021-04-04 18:29:39
InventoryDB,238.69,96.79,162,61.25,2022-12-12 13:24:03
MetricsDB,3341.99,87.52,232,22.84,2022-05-15 23:43:01
ProfilesDB,73.33,95.3,447,62.96,2022-11-11 15:47:20
<end>Can you change this plain text into markdown?
Title: Escape from Earth | Genre: Comedy | Release Year: 2006 | Box Office Earnings (M): 186.45
Title: The Great Expedition | Genre: Drama | Release Year: 1970 | Box Office Earnings (M): 836.93
Title: Dreamwalker | Genre: Sci-Fi | Release Year: 1999 | Box Office Earnings (M): 645.86
Title: Escape from Earth | Genre: Comedy | Release Year: 1993 | Box Office Earnings (M): 512.68
Title: The Endless Horizon | Genre: Thriller | Release Year: 2001 | Box Office Earnings (M): 604.66
Title: Escape from Earth | Genre: Comedy | Release Year: 2004 | Box Office Earnings (M): 836.93
<start>
| Title | Genre | Release Year | Box Office Earnings (M) |
| --- | --- | --- | --- |
| Escape from Earth | Comedy | 2006 | 186.45 |
| The Great Expedition | Drama | 1970 | 836.93 |
| Dreamwalker | Sci-Fi | 1999 | 645.86 |
| Escape from Earth | Comedy | 1993 | 512.68 |
| The Endless Horizon | Thriller | 2001 | 604.66 |
| Escape from Earth | Comedy | 2004 | 836.93 |
<end>Transform this MARKDOWN structure to a json format:
| Title | Director | Box Office Earnings (M) |
| --- | --- | --- |
| The Endless Horizon | Selene Darkwhisper | 20.44 |
| The Great Expedition | Aria Ravenwood | 754.25 |
| Beyond the Veil | Selene Darkwhisper | 552.51 |
| Dreamwalker | Lira Silverleaf | 89.48 |
| Edge of Infinity | Talon Blackthorn | 552.51 |
| Rise of the Titans | Talon Blackthorn | 139.26 |
| Dreamwalker | Drake Nightshade | 747.69 |
| Edge of Infinity | Lira Silverleaf | 324.84 |
| Mystery of the Depths | Selene Darkwhisper | 235.05 |
| The Endless Horizon | Rylan Frostblade | 922.5 |<start>
[
    {
        "Title": "The Endless Horizon",
        "Director": "Selene Darkwhisper",
        "Box Office Earnings (M)": 20.44
    },
    {
        "Title": "The Great Expedition",
        "Director": "Aria Ravenwood",
        "Box Office Earnings (M)": 754.25
    },
    {
        "Title": "Beyond the Veil",
        "Director": "Selene Darkwhisper",
        "Box Office Earnings (M)": 552.51
    },
    {
        "Title": "Dreamwalker",
        "Director": "Lira Silverleaf",
        "Box Office Earnings (M)": 89.48
    },
    {
        "Title": "Edge of Infinity",
        "Director": "Talon Blackthorn",
        "Box Office Earnings (M)": 552.51
    },
    {
        "Title": "Rise of the Titans",
        "Director": "Talon Blackthorn",
        "Box Office Earnings (M)": 139.26
    },
    {
        "Title": "Dreamwalker",
        "Director": "Drake Nightshade",
        "Box Office Earnings (M)": 747.69
    },
    {
        "Title": "Edge of Infinity",
        "Director": "Lira Silverleaf",
        "Box Office Earnings (M)": 324.84
    },
    {
        "Title": "Mystery of the Depths",
        "Director": "Selene Darkwhisper",
        "Box Office Earnings (M)": 235.05
    },
    {
        "Title": "The Endless Horizon",
        "Director": "Rylan Frostblade",
        "Box Office Earnings (M)": 922.5
    }
]
<end>Please transform the following Plain text data into markdown:
Restaurant Name: Burger Haven | Cuisine: Japanese | Location: Chicago | Rating: 5 | Price Range: $
Restaurant Name: Taco Town | Cuisine: French | Location: Seattle | Rating: 4 | Price Range: $
Restaurant Name: Burger Haven | Cuisine: Italian | Location: San Francisco | Rating: 1 | Price Range: $$$$
Restaurant Name: Vegan Delight | Cuisine: French | Location: Seattle | Rating: 1 | Price Range: $$
Restaurant Name: Pizza Planet | Cuisine: Mediterranean | Location: Los Angeles | Rating: 5 | Price Range: $$$$
Restaurant Name: Vegan Delight | Cuisine: Mexican | Location: Chicago | Rating: 4 | Price Range: $$$$$
<start>
| Restaurant Name | Cuisine | Location | Rating | Price Range |
| --- | --- | --- | --- | --- |
| Burger Haven | Japanese | Chicago | 5 | $ |
| Taco Town | French | Seattle | 4 | $ |
| Burger Haven | Italian | San Francisco | 1 | $$$$ |
| Vegan Delight | French | Seattle | 1 | $$ |
| Pizza Planet | Mediterranean | Los Angeles | 5 | $$$$ |
| Vegan Delight | Mexican | Chicago | 4 | $$$$$ |
<end>Transform this csv structure to a MARKDOWN format:
Location,Condition,Temperature (C),Humidity (%),Wind Speed (km/h),Day
Chicago,Snowy,12.6,72,18.9,Tuesday
Denver,Stormy,22.3,63,19.3,Monday
Phoenix,Sunny,37.9,32,7.1,Sunday
<start>
| Location | Condition | Temperature (C) | Humidity (%) | Wind Speed (km/h) | Day |
| --- | --- | --- | --- | --- | --- |
| Chicago | Snowy | 12.6 | 72 | 18.9 | Tuesday |
| Denver | Stormy | 22.3 | 63 | 19.3 | Monday |
| Phoenix | Sunny | 37.9 | 32 | 7.1 | Sunday |
<end>Please transform the following Plain text data into Markdown:
Product Name: Device | SKU: SKU-1038 | Stock Quantity: 384 | Category: Toys | Supplier Name: Globex
Product Name: Apparatus | SKU: SKU-1075 | Stock Quantity: 266 | Category: Sports | Supplier Name: Globex
Product Name: Widget | SKU: SKU-1075 | Stock Quantity: 474 | Category: Automotive | Supplier Name: Wonka Industries
Product Name: Gizmo | SKU: SKU-1067 | Stock Quantity: 33 | Category: Sports | Supplier Name: Globex
<start>
| Product Name | SKU | Stock Quantity | Category | Supplier Name |
| --- | --- | --- | --- | --- |
| Device | SKU-1038 | 384 | Toys | Globex |
| Apparatus | SKU-1075 | 266 | Sports | Globex |
| Widget | SKU-1075 | 474 | Automotive | Wonka Industries |
| Gizmo | SKU-1067 | 33 | Sports | Globex |
<end>Here's some CSV data, can you convert it to markdown?
Company,Sector,Market Cap,Stock Price,Annual Revenue (B),Quarter
BioPharm,Technology,Mid Cap,378.58,323.71,Q4
BioPharm,Healthcare,Mega Cap,190.27,162.45,Q2
HealthPlus,Automotive,Mega Cap,429.55,205.8,Q1
BioPharm,Biotech,Mid Cap,521.53,152.57,Q3
HealthPlus,Healthcare,Mega Cap,275.84,215.03,Q3
FinanceWorks,Retail,Mega Cap,429.55,190.17,Q3
BioPharm,Automotive,Mid Cap,908.19,339.67,Q4
RetailHub,Automotive,Small Cap,170.93,430.52,Q2
TechCorp,Retail,Mega Cap,864.65,471.89,Q3
<start>
| Company | Sector | Market Cap | Stock Price | Annual Revenue (B) | Quarter |
| --- | --- | --- | --- | --- | --- |
| BioPharm | Technology | Mid Cap | 378.58 | 323.71 | Q4 |
| BioPharm | Healthcare | Mega Cap | 190.27 | 162.45 | Q2 |
| HealthPlus | Automotive | Mega Cap | 429.55 | 205.8 | Q1 |
| BioPharm | Biotech | Mid Cap | 521.53 | 152.57 | Q3 |
| HealthPlus | Healthcare | Mega Cap | 275.84 | 215.03 | Q3 |
| FinanceWorks | Retail | Mega Cap | 429.55 | 190.17 | Q3 |
| BioPharm | Automotive | Mid Cap | 908.19 | 339.67 | Q4 |
| RetailHub | Automotive | Small Cap | 170.93 | 430.52 | Q2 |
| TechCorp | Retail | Mega Cap | 864.65 | 471.89 | Q3 |
<end>Here's some plain text data, can you convert it to Yaml?
Location: Seattle | Condition: Cloudy | Temperature (C): 16.0 | Wind Speed (km/h): 20.0 | Day: Tuesday
Location: Houston | Condition: Sunny | Temperature (C): 22.8 | Wind Speed (km/h): 19.3 | Day: Friday
Location: Phoenix | Condition: Sunny | Temperature (C): 27.9 | Wind Speed (km/h): 6.2 | Day: Thursday
<start>
- Condition: Cloudy
  Day: Tuesday
  Location: Seattle
  Temperature (C): 16.0
  Wind Speed (km/h): 20.0
- Condition: Sunny
  Day: Friday
  Location: Houston
  Temperature (C): 22.8
  Wind Speed (km/h): 19.3
- Condition: Sunny
  Day: Thursday
  Location: Phoenix
  Temperature (C): 27.9
  Wind Speed (km/h): 6.2
<end>Transform this CSV structure to a markdown format:
Name,Age,Birth Month
Leon,23,October
Jessie,53,December
Billie,24,June
<start>
| Name | Age | Birth Month |
| --- | --- | --- |
| Leon | 23 | October |
| Jessie | 53 | December |
| Billie | 24 | June |
<end>Transform this markdown structure to a Yml format:
| Device ID | Device Type | Location | Reading Value | Timestamp |
| --- | --- | --- | --- | --- |
| device-0078 | Motion Detector | Hallway | 30.77 | 2021-10-19 22:47:55 |
| device-0044 | Motion Detector | Garden | -34.05 | 2023-05-24 13:53:29 |
| device-0072 | Light Sensor | Bedroom | -20.5 | 2021-05-26 05:44:44 |
| device-0082 | Temperature Sensor | Garden | 32.7 | 2022-02-25 19:47:50 |<start>
- Device ID: device-0078
  Device Type: Motion Detector
  Location: Hallway
  Reading Value: 30.77
  Timestamp: '2021-10-19 22:47:55'
- Device ID: device-0044
  Device Type: Motion Detector
  Location: Garden
  Reading Value: -34.05
  Timestamp: '2023-05-24 13:53:29'
- Device ID: device-0072
  Device Type: Light Sensor
  Location: Bedroom
  Reading Value: -20.5
  Timestamp: '2021-05-26 05:44:44'
- Device ID: device-0082
  Device Type: Temperature Sensor
  Location: Garden
  Reading Value: 32.7
  Timestamp: '2022-02-25 19:47:50'
<end>Please transform the following Plain text data into csv:
Company: TechCorp | Sector: Technology | Stock Price: 326.43 | Annual Revenue (B): 62.16
Company: AutoDrive | Sector: Automotive | Stock Price: 573.37 | Annual Revenue (B): 440.26
Company: AeroSpace | Sector: Technology | Stock Price: 249.37 | Annual Revenue (B): 440.26
Company: HealthPlus | Sector: Biotech | Stock Price: 348.12 | Annual Revenue (B): 266.31
<start>
Company,Sector,Stock Price,Annual Revenue (B)
TechCorp,Technology,326.43,62.16
AutoDrive,Automotive,573.37,440.26
AeroSpace,Technology,249.37,440.26
HealthPlus,Biotech,348.12,266.31
<end>Can you change this JSON into plain text?
[
    {
        "Title": "Echoes of Eternity",
        "Rating": 3.7
    },
    {
        "Title": "The Forgotten World",
        "Rating": 2.3
    },
    {
        "Title": "Legends of the Rift",
        "Rating": 3.2
    }
]<start>
Title: Echoes of Eternity | Rating: 3.7
Title: The Forgotten World | Rating: 2.3
Title: Legends of the Rift | Rating: 3.2
<end>Convert this YML to Json:
- Author: Orion Frostblade
  Genre: Horror
  Publication Year: 1977
  Rating: 2.4
  Title: Whispers of the Abyss
- Author: Orion Frostblade
  Genre: Romance
  Publication Year: 1963
  Rating: 2.3
  Title: Shadows of Solitude
- Author: Elara Moonshadow
  Genre: Science Fiction
  Publication Year: 1962
  Rating: 2.4
  Title: The Forgotten World
- Author: Elara Moonshadow
  Genre: Science Fiction
  Publication Year: 1990
  Rating: 4.4
  Title: A Journey Through Time
- Author: Orion Frostblade
  Genre: Non-Fiction
  Publication Year: 1954
  Rating: 3.0
  Title: Whispers of the Abyss
- Author: Rowan Ashborne
  Genre: Horror
  Publication Year: 2006
  Rating: 2.2
  Title: The Silent Grove
- Author: Elara Moonshadow
  Genre: Non-Fiction
  Publication Year: 1995
  Rating: 3.3
  Title: Whispers of the Abyss
- Author: Sylvia Nightshade
  Genre: Historical
  Publication Year: 1964
  Rating: 3.7
  Title: Legends of the Rift
- Author: Elara Moonshadow
  Genre: Thriller
  Publication Year: 1989
  Rating: 3.4
  Title: The Silent Grove
<start>
[
    {
        "Title": "Whispers of the Abyss",
        "Author": "Orion Frostblade",
        "Genre": "Horror",
        "Publication Year": 1977,
        "Rating": 2.4
    },
    {
        "Title": "Shadows of Solitude",
        "Author": "Orion Frostblade",
        "Genre": "Romance",
        "Publication Year": 1963,
        "Rating": 2.3
    },
    {
        "Title": "The Forgotten World",
        "Author": "Elara Moonshadow",
        "Genre": "Science Fiction",
        "Publication Year": 1962,
        "Rating": 2.4
    },
    {
        "Title": "A Journey Through Time",
        "Author": "Elara Moonshadow",
        "Genre": "Science Fiction",
        "Publication Year": 1990,
        "Rating": 4.4
    },
    {
        "Title": "Whispers of the Abyss",
        "Author": "Orion Frostblade",
        "Genre": "Non-Fiction",
        "Publication Year": 1954,
        "Rating": 3.0
    },
    {
        "Title": "The Silent Grove",
        "Author": "Rowan Ashborne",
        "Genre": "Horror",
        "Publication Year": 2006,
        "Rating": 2.2
    },
    {
        "Title": "Whispers of the Abyss",
        "Author": "Elara Moonshadow",
        "Genre": "Non-Fiction",
        "Publication Year": 1995,
        "Rating": 3.3
    },
    {
        "Title": "Legends of the Rift",
        "Author": "Sylvia Nightshade",
        "Genre": "Historical",
        "Publication Year": 1964,
        "Rating": 3.7
    },
    {
        "Title": "The Silent Grove",
        "Author": "Elara Moonshadow",
        "Genre": "Thriller",
        "Publication Year": 1989,
        "Rating": 3.4
    }
]
<end>Convert this json to MARKDOWN:
[
    {
        "Cache Hit Ratio (%)": 74.33,
        "Average Latency (ms)": 42.13,
        "Timestamp": "2021-12-08 00:03:33"
    },
    {
        "Cache Hit Ratio (%)": 84.14,
        "Average Latency (ms)": 76.83,
        "Timestamp": "2021-02-28 09:46:26"
    },
    {
        "Cache Hit Ratio (%)": 83.75,
        "Average Latency (ms)": 54.95,
        "Timestamp": "2021-04-21 18:28:57"
    },
    {
        "Cache Hit Ratio (%)": 96.13,
        "Average Latency (ms)": 23.4,
        "Timestamp": "2021-02-24 05:51:26"
    },
    {
        "Cache Hit Ratio (%)": 87.23,
        "Average Latency (ms)": 48.29,
        "Timestamp": "2023-11-27 22:50:44"
    },
    {
        "Cache Hit Ratio (%)": 85.19,
        "Average Latency (ms)": 87.1,
        "Timestamp": "2022-10-26 07:24:51"
    },
    {
        "Cache Hit Ratio (%)": 93.59,
        "Average Latency (ms)": 63.54,
        "Timestamp": "2022-05-08 10:20:00"
    },
    {
        "Cache Hit Ratio (%)": 92.68,
        "Average Latency (ms)": 76.83,
        "Timestamp": "2023-09-01 01:28:30"
    },
    {
        "Cache Hit Ratio (%)": 87.59,
        "Average Latency (ms)": 14.64,
        "Timestamp": "2021-03-25 11:47:24"
    },
    {
        "Cache Hit Ratio (%)": 88.94,
        "Average Latency (ms)": 30.49,
        "Timestamp": "2021-12-15 11:47:43"
    }
]<start>
| Cache Hit Ratio (%) | Average Latency (ms) | Timestamp |
| --- | --- | --- |
| 74.33 | 42.13 | 2021-12-08 00:03:33 |
| 84.14 | 76.83 | 2021-02-28 09:46:26 |
| 83.75 | 54.95 | 2021-04-21 18:28:57 |
| 96.13 | 23.4 | 2021-02-24 05:51:26 |
| 87.23 | 48.29 | 2023-11-27 22:50:44 |
| 85.19 | 87.1 | 2022-10-26 07:24:51 |
| 93.59 | 63.54 | 2022-05-08 10:20:00 |
| 92.68 | 76.83 | 2023-09-01 01:28:30 |
| 87.59 | 14.64 | 2021-03-25 11:47:24 |
| 88.94 | 30.49 | 2021-12-15 11:47:43 |
<end>Can you change this csv into json?
Title,Box Office Earnings (M)
Rise of the Titans,608.97
Escape from Earth,551.97
Edge of Infinity,795.09
Mystery of the Depths,177.84
The Great Expedition,153.7
Dreamwalker,12.42
Escape from Earth,586.13
<start>
[
    {
        "Title": "Rise of the Titans",
        "Box Office Earnings (M)": 608.97
    },
    {
        "Title": "Escape from Earth",
        "Box Office Earnings (M)": 551.97
    },
    {
        "Title": "Edge of Infinity",
        "Box Office Earnings (M)": 795.09
    },
    {
        "Title": "Mystery of the Depths",
        "Box Office Earnings (M)": 177.84
    },
    {
        "Title": "The Great Expedition",
        "Box Office Earnings (M)": 153.7
    },
    {
        "Title": "Dreamwalker",
        "Box Office Earnings (M)": 12.42
    },
    {
        "Title": "Escape from Earth",
        "Box Office Earnings (M)": 586.13
    }
]
<end>Transform this plain text structure to a Yaml format:
Product Name: Instrument | SKU: SKU-1005 | Stock Quantity: 180
Product Name: Thingamajig | SKU: SKU-1009 | Stock Quantity: 387
Product Name: Thingamajig | SKU: SKU-1041 | Stock Quantity: 424
Product Name: Doohickey | SKU: SKU-1005 | Stock Quantity: 314
<start>
- Product Name: Instrument
  SKU: SKU-1005
  Stock Quantity: 180
- Product Name: Thingamajig
  SKU: SKU-1009
  Stock Quantity: 387
- Product Name: Thingamajig
  SKU: SKU-1041
  Stock Quantity: 424
- Product Name: Doohickey
  SKU: SKU-1005
  Stock Quantity: 314
<end>Convert this plain text to markdown:
Location: Miami | Temperature (C): 0.1 | Humidity (%): 67 | Wind Speed (km/h): 5.8 | Day: Monday
Location: Los Angeles | Temperature (C): -5.1 | Humidity (%): 58 | Wind Speed (km/h): 27.8 | Day: Thursday
Location: Denver | Temperature (C): -5.4 | Humidity (%): 48 | Wind Speed (km/h): 2.4 | Day: Saturday
Location: Chicago | Temperature (C): 8.9 | Humidity (%): 93 | Wind Speed (km/h): 13.8 | Day: Monday
Location: Los Angeles | Temperature (C): 8.7 | Humidity (%): 58 | Wind Speed (km/h): 28.3 | Day: Tuesday
Location: New York | Temperature (C): 8.7 | Humidity (%): 28 | Wind Speed (km/h): 3.8 | Day: Wednesday
Location: Phoenix | Temperature (C): 26.8 | Humidity (%): 100 | Wind Speed (km/h): 25.4 | Day: Thursday
Location: Phoenix | Temperature (C): 3.6 | Humidity (%): 70 | Wind Speed (km/h): 22.3 | Day: Friday
<start>
| Location | Temperature (C) | Humidity (%) | Wind Speed (km/h) | Day |
| --- | --- | --- | --- | --- |
| Miami | 0.1 | 67 | 5.8 | Monday |
| Los Angeles | -5.1 | 58 | 27.8 | Thursday |
| Denver | -5.4 | 48 | 2.4 | Saturday |
| Chicago | 8.9 | 93 | 13.8 | Monday |
| Los Angeles | 8.7 | 58 | 28.3 | Tuesday |
| New York | 8.7 | 28 | 3.8 | Wednesday |
| Phoenix | 26.8 | 100 | 25.4 | Thursday |
| Phoenix | 3.6 | 70 | 22.3 | Friday |
<end>Transform this JSON structure to a YML format:
[
    {
        "Sector": "Automotive",
        "Market Cap": "Mega Cap",
        "Stock Price": 488.88,
        "Annual Revenue (B)": 256.65,
        "Quarter": "Q2"
    },
    {
        "Sector": "Automotive",
        "Market Cap": "Small Cap",
        "Stock Price": 262.88,
        "Annual Revenue (B)": 441.85,
        "Quarter": "Q2"
    },
    {
        "Sector": "Energy",
        "Market Cap": "Mid Cap",
        "Stock Price": 759.13,
        "Annual Revenue (B)": 169.77,
        "Quarter": "Q4"
    },
    {
        "Sector": "Biotech",
        "Market Cap": "Large Cap",
        "Stock Price": 147.15,
        "Annual Revenue (B)": 68.0,
        "Quarter": "Q2"
    }
]<start>
- Annual Revenue (B): 256.65
  Market Cap: Mega Cap
  Quarter: Q2
  Sector: Automotive
  Stock Price: 488.88
- Annual Revenue (B): 441.85
  Market Cap: Small Cap
  Quarter: Q2
  Sector: Automotive
  Stock Price: 262.88
- Annual Revenue (B): 169.77
  Market Cap: Mid Cap
  Quarter: Q4
  Sector: Energy
  Stock Price: 759.13
- Annual Revenue (B): 68.0
  Market Cap: Large Cap
  Quarter: Q2
  Sector: Biotech
  Stock Price: 147.15
<end>Here's some csv data, can you convert it to PLAIN TEXT?
Database Name,Cache Hit Ratio (%),Connection Count,Timestamp
MetricsDB,94.64,321,2021-03-22 07:37:04
OrdersDB,84.63,270,2022-06-14 06:23:14
AnalyticsDB,83.08,330,2021-04-08 03:58:28
MetricsDB,78.91,319,2022-12-13 10:49:46
SalesDB,99.89,130,2021-01-07 05:30:44
UserDB,80.11,270,2023-03-16 07:51:11
AnalyticsDB,70.19,348,2023-05-02 12:51:40
<start>
Database Name: MetricsDB | Cache Hit Ratio (%): 94.64 | Connection Count: 321 | Timestamp: 2021-03-22 07:37:04
Database Name: OrdersDB | Cache Hit Ratio (%): 84.63 | Connection Count: 270 | Timestamp: 2022-06-14 06:23:14
Database Name: AnalyticsDB | Cache Hit Ratio (%): 83.08 | Connection Count: 330 | Timestamp: 2021-04-08 03:58:28
Database Name: MetricsDB | Cache Hit Ratio (%): 78.91 | Connection Count: 319 | Timestamp: 2022-12-13 10:49:46
Database Name: SalesDB | Cache Hit Ratio (%): 99.89 | Connection Count: 130 | Timestamp: 2021-01-07 05:30:44
Database Name: UserDB | Cache Hit Ratio (%): 80.11 | Connection Count: 270 | Timestamp: 2023-03-16 07:51:11
Database Name: AnalyticsDB | Cache Hit Ratio (%): 70.19 | Connection Count: 348 | Timestamp: 2023-05-02 12:51:40
<end>Here's some json data, can you convert it to Yaml?
[
    {
        "Location": "Denver",
        "Condition": "Cloudy",
        "Humidity (%)": 80
    },
    {
        "Location": "Miami",
        "Condition": "Stormy",
        "Humidity (%)": 49
    },
    {
        "Location": "New York",
        "Condition": "Sunny",
        "Humidity (%)": 29
    },
    {
        "Location": "Phoenix",
        "Condition": "Sunny",
        "Humidity (%)": 77
    },
    {
        "Location": "Chicago",
        "Condition": "Windy",
        "Humidity (%)": 27
    },
    {
        "Location": "New York",
        "Condition": "Foggy",
        "Humidity (%)": 46
    }
]<start>
- Condition: Cloudy
  Humidity (%): 80
  Location: Denver
- Condition: Stormy
  Humidity (%): 49
  Location: Miami
- Condition: Sunny
  Humidity (%): 29
  Location: New York
- Condition: Sunny
  Humidity (%): 77
  Location: Phoenix
- Condition: Windy
  Humidity (%): 27
  Location: Chicago
- Condition: Foggy
  Humidity (%): 46
  Location: New York
<end>Please transform the following plain text data into Markdown:
Device Type: Pressure Sensor | Location: Hallway | Reading Value: 25.86
Device Type: Pressure Sensor | Location: Bathroom | Reading Value: 71.44
Device Type: Pressure Sensor | Location: Kitchen | Reading Value: 12.93
Device Type: Motion Detector | Location: Office | Reading Value: 73.7
Device Type: Pressure Sensor | Location: Living Room | Reading Value: -34.62
Device Type: Light Sensor | Location: Bedroom | Reading Value: -25.12
<start>
| Device Type | Location | Reading Value |
| --- | --- | --- |
| Pressure Sensor | Hallway | 25.86 |
| Pressure Sensor | Bathroom | 71.44 |
| Pressure Sensor | Kitchen | 12.93 |
| Motion Detector | Office | 73.7 |
| Pressure Sensor | Living Room | -34.62 |
| Light Sensor | Bedroom | -25.12 |
<end>Can you change this yml into csv?
- Annual Revenue (B): 240.31
  Company: TechCorp
  Market Cap: Small Cap
  Quarter: Q2
  Sector: Automotive
  Stock Price: 853.78
- Annual Revenue (B): 338.57
  Company: RetailHub
  Market Cap: Small Cap
  Quarter: Q4
  Sector: Energy
  Stock Price: 827.84
- Annual Revenue (B): 441.04
  Company: GlobalTrade
  Market Cap: Small Cap
  Quarter: Q2
  Sector: Aerospace
  Stock Price: 656.22
- Annual Revenue (B): 231.66
  Company: FinanceWorks
  Market Cap: Large Cap
  Quarter: Q1
  Sector: Energy
  Stock Price: 307.44
- Annual Revenue (B): 196.85
  Company: Foodies
  Market Cap: Large Cap
  Quarter: Q2
  Sector: Healthcare
  Stock Price: 891.11
- Annual Revenue (B): 366.83
  Company: AutoDrive
  Market Cap: Mid Cap
  Quarter: Q2
  Sector: Energy
  Stock Price: 795.07
<start>
Company,Sector,Market Cap,Stock Price,Annual Revenue (B),Quarter
TechCorp,Automotive,Small Cap,853.78,240.31,Q2
RetailHub,Energy,Small Cap,827.84,338.57,Q4
GlobalTrade,Aerospace,Small Cap,656.22,441.04,Q2
FinanceWorks,Energy,Large Cap,307.44,231.66,Q1
Foodies,Healthcare,Large Cap,891.11,196.85,Q2
AutoDrive,Energy,Mid Cap,795.07,366.83,Q2
<end>Please transform the following Yaml data into json:
- Genre: Non-Fiction
  Publication Year: 1993
  Rating: 2.3
  Title: Whispers of the Abyss
- Genre: Historical
  Publication Year: 1985
  Rating: 3.8
  Title: The Last Sky
- Genre: Non-Fiction
  Publication Year: 1971
  Rating: 3.9
  Title: Legends of the Rift
<start>
[
    {
        "Title": "Whispers of the Abyss",
        "Genre": "Non-Fiction",
        "Publication Year": 1993,
        "Rating": 2.3
    },
    {
        "Title": "The Last Sky",
        "Genre": "Historical",
        "Publication Year": 1985,
        "Rating": 3.8
    },
    {
        "Title": "Legends of the Rift",
        "Genre": "Non-Fiction",
        "Publication Year": 1971,
        "Rating": 3.9
    }
]
<end>Transform this yml structure to a CSV format:
- Battery Level (%): 66.0
  Device ID: device-0062
  Device Type: Pressure Sensor
  Location: Kitchen
  Reading Value: -7.45
  Timestamp: '2023-10-11 03:03:51'
- Battery Level (%): 50.7
  Device ID: device-0099
  Device Type: Light Sensor
  Location: Living Room
  Reading Value: 33.34
  Timestamp: '2022-03-07 04:12:37'
- Battery Level (%): 21.8
  Device ID: device-0026
  Device Type: Light Sensor
  Location: Bedroom
  Reading Value: -36.91
  Timestamp: '2022-07-09 12:57:20'
<start>
Device ID,Device Type,Location,Battery Level (%),Reading Value,Timestamp
device-0062,Pressure Sensor,Kitchen,66.0,-7.45,2023-10-11 03:03:51
device-0099,Light Sensor,Living Room,50.7,33.34,2022-03-07 04:12:37
device-0026,Light Sensor,Bedroom,21.8,-36.91,2022-07-09 12:57:20
<end>Here's some Plain text data, can you convert it to csv?
Name: Donovan | Birth Month: October | Income: 145000
Name: Joseph | Birth Month: December | Income: 195000
Name: Cassie | Birth Month: December | Income: 370000
Name: Kerri | Birth Month: September | Income: 25000
Name: Kaiden | Birth Month: December | Income: 440000
Name: Greg | Birth Month: June | Income: 230000
Name: Christine | Birth Month: December | Income: 260000
Name: Sara | Birth Month: April | Income: 25000
Name: Alfred | Birth Month: May | Income: 370000
<start>
Name,Birth Month,Income
Donovan,October,145000
Joseph,December,195000
Cassie,December,370000
Kerri,September,25000
Kaiden,December,440000
Greg,June,230000
Christine,December,260000
Sara,April,25000
Alfred,May,370000
<end>Please transform the following markdown data into PLAIN TEXT:
| Device Type | Location | Battery Level (%) | Timestamp |
| --- | --- | --- | --- |
| Motion Detector | Garage | 65.4 | 2023-09-17 01:13:47 |
| Pressure Sensor | Kitchen | 27.2 | 2021-04-10 05:54:58 |
| Temperature Sensor | Hallway | 67.9 | 2023-07-06 17:21:40 |
| Motion Detector | Garage | 28.5 | 2021-11-23 09:15:26 |
| Light Sensor | Bedroom | 21.1 | 2022-10-12 02:15:58 |
| Motion Detector | Office | 13.6 | 2023-11-03 23:46:53 |
| Light Sensor | Kitchen | 40.1 | 2022-04-02 20:54:05 |
| Temperature Sensor | Garage | 91.2 | 2022-08-09 12:39:28 |
| Pressure Sensor | Bedroom | 94.9 | 2023-03-20 12:02:03 |
| Light Sensor | Hallway | 67.7 | 2022-10-22 08:59:10 |<start>
Device Type: Motion Detector | Location: Garage | Battery Level (%): 65.4 | Timestamp: 2023-09-17 01:13:47
Device Type: Pressure Sensor | Location: Kitchen | Battery Level (%): 27.2 | Timestamp: 2021-04-10 05:54:58
Device Type: Temperature Sensor | Location: Hallway | Battery Level (%): 67.9 | Timestamp: 2023-07-06 17:21:40
Device Type: Motion Detector | Location: Garage | Battery Level (%): 28.5 | Timestamp: 2021-11-23 09:15:26
Device Type: Light Sensor | Location: Bedroom | Battery Level (%): 21.1 | Timestamp: 2022-10-12 02:15:58
Device Type: Motion Detector | Location: Office | Battery Level (%): 13.6 | Timestamp: 2023-11-03 23:46:53
Device Type: Light Sensor | Location: Kitchen | Battery Level (%): 40.1 | Timestamp: 2022-04-02 20:54:05
Device Type: Temperature Sensor | Location: Garage | Battery Level (%): 91.2 | Timestamp: 2022-08-09 12:39:28
Device Type: Pressure Sensor | Location: Bedroom | Battery Level (%): 94.9 | Timestamp: 2023-03-20 12:02:03
Device Type: Light Sensor | Location: Hallway | Battery Level (%): 67.7 | Timestamp: 2022-10-22 08:59:10
<end>Can you change this CSV into JSON?
Location,Condition,Humidity (%),Wind Speed (km/h),Day
New York,Stormy,32,9.0,Tuesday
New York,Sunny,82,10.4,Saturday
Miami,Foggy,81,15.0,Sunday
Seattle,Sunny,68,1.0,Wednesday
Denver,Snowy,49,29.3,Sunday
<start>
[
    {
        "Location": "New York",
        "Condition": "Stormy",
        "Humidity (%)": 32,
        "Wind Speed (km/h)": 9.0,
        "Day": "Tuesday"
    },
    {
        "Location": "New York",
        "Condition": "Sunny",
        "Humidity (%)": 82,
        "Wind Speed (km/h)": 10.4,
        "Day": "Saturday"
    },
    {
        "Location": "Miami",
        "Condition": "Foggy",
        "Humidity (%)": 81,
        "Wind Speed (km/h)": 15.0,
        "Day": "Sunday"
    },
    {
        "Location": "Seattle",
        "Condition": "Sunny",
        "Humidity (%)": 68,
        "Wind Speed (km/h)": 1.0,
        "Day": "Wednesday"
    },
    {
        "Location": "Denver",
        "Condition": "Snowy",
        "Humidity (%)": 49,
        "Wind Speed (km/h)": 29.3,
        "Day": "Sunday"
    }
]
<end>Can you change this yaml into Plain text?
- Author: Rowan Ashborne
  Title: The Last Sky
- Author: Luna Silverleaf
  Title: Legends of the Rift
- Author: Isla Windrider
  Title: Legends of the Rift
- Author: Galen Starfire
  Title: A Journey Through Time
- Author: Galen Starfire
  Title: The Crystal Key
- Author: Rowan Ashborne
  Title: Legends of the Rift
<start>
Title: The Last Sky | Author: Rowan Ashborne
Title: Legends of the Rift | Author: Luna Silverleaf
Title: Legends of the Rift | Author: Isla Windrider
Title: A Journey Through Time | Author: Galen Starfire
Title: The Crystal Key | Author: Galen Starfire
Title: Legends of the Rift | Author: Rowan Ashborne
<end>Here's some json data, can you convert it to CSV?
[
    {
        "Restaurant Name": "Vegan Delight",
        "Cuisine": "Chinese",
        "Rating": 2
    },
    {
        "Restaurant Name": "Sushi World",
        "Cuisine": "French",
        "Rating": 5
    },
    {
        "Restaurant Name": "The Steakhouse",
        "Cuisine": "American",
        "Rating": 1
    },
    {
        "Restaurant Name": "Vegan Delight",
        "Cuisine": "American",
        "Rating": 3
    },
    {
        "Restaurant Name": "Vegan Delight",
        "Cuisine": "American",
        "Rating": 5
    },
    {
        "Restaurant Name": "Burger Haven",
        "Cuisine": "American",
        "Rating": 4
    }
]<start>
Restaurant Name,Cuisine,Rating
Vegan Delight,Chinese,2
Sushi World,French,5
The Steakhouse,American,1
Vegan Delight,American,3
Vegan Delight,American,5
Burger Haven,American,4
<end>Please transform the following markdown data into CSV:
| Device ID | Device Type | Location | Battery Level (%) | Timestamp |
| --- | --- | --- | --- | --- |
| device-0020 | Temperature Sensor | Office | 35.9 | 2022-11-15 02:37:51 |
| device-0032 | Motion Detector | Hallway | 93.8 | 2021-11-24 00:58:25 |
| device-0007 | Light Sensor | Hallway | 54.5 | 2023-01-24 06:00:16 |
| device-0098 | Motion Detector | Garage | 84.6 | 2021-08-25 20:17:17 |
| device-0081 | Temperature Sensor | Office | 30.7 | 2023-04-28 19:14:29 |
| device-0097 | Humidity Sensor | Living Room | 41.4 | 2022-10-11 21:07:33 |
| device-0036 | Pressure Sensor | Bedroom | 69.3 | 2023-03-11 13:45:06 |<start>
Device ID,Device Type,Location,Battery Level (%),Timestamp
device-0020,Temperature Sensor,Office,35.9,2022-11-15 02:37:51
device-0032,Motion Detector,Hallway,93.8,2021-11-24 00:58:25
device-0007,Light Sensor,Hallway,54.5,2023-01-24 06:00:16
device-0098,Motion Detector,Garage,84.6,2021-08-25 20:17:17
device-0081,Temperature Sensor,Office,30.7,2023-04-28 19:14:29
device-0097,Humidity Sensor,Living Room,41.4,2022-10-11 21:07:33
device-0036,Pressure Sensor,Bedroom,69.3,2023-03-11 13:45:06
<end>Transform this Json structure to a plain text format:
[
    {
        "Device Type": "Motion Detector",
        "Battery Level (%)": 54.4,
        "Timestamp": "2022-02-24 23:53:39"
    },
    {
        "Device Type": "Humidity Sensor",
        "Battery Level (%)": 46.0,
        "Timestamp": "2021-05-01 03:40:37"
    },
    {
        "Device Type": "Pressure Sensor",
        "Battery Level (%)": 16.4,
        "Timestamp": "2022-01-11 14:57:05"
    },
    {
        "Device Type": "Pressure Sensor",
        "Battery Level (%)": 25.6,
        "Timestamp": "2022-04-04 09:28:37"
    },
    {
        "Device Type": "Pressure Sensor",
        "Battery Level (%)": 24.8,
        "Timestamp": "2022-04-18 21:46:36"
    },
    {
        "Device Type": "Motion Detector",
        "Battery Level (%)": 45.4,
        "Timestamp": "2023-12-27 22:04:09"
    }
]<start>
Device Type: Motion Detector | Battery Level (%): 54.4 | Timestamp: 2022-02-24 23:53:39
Device Type: Humidity Sensor | Battery Level (%): 46.0 | Timestamp: 2021-05-01 03:40:37
Device Type: Pressure Sensor | Battery Level (%): 16.4 | Timestamp: 2022-01-11 14:57:05
Device Type: Pressure Sensor | Battery Level (%): 25.6 | Timestamp: 2022-04-04 09:28:37
Device Type: Pressure Sensor | Battery Level (%): 24.8 | Timestamp: 2022-04-18 21:46:36
Device Type: Motion Detector | Battery Level (%): 45.4 | Timestamp: 2023-12-27 22:04:09
<end>Can you change this CSV into plain text?
Queries per Second,Cache Hit Ratio (%),Average Latency (ms)
4459.92,75.05,99.82
4962.47,94.28,99.82
1039.82,82.01,8.71
4648.82,91.85,76.26
2775.65,82.01,23.6
2377.35,91.85,62.7
106.45,84.92,41.83
2505.47,71.89,54.37
2316.52,85.39,56.56
<start>
Queries per Second: 4459.92 | Cache Hit Ratio (%): 75.05 | Average Latency (ms): 99.82
Queries per Second: 4962.47 | Cache Hit Ratio (%): 94.28 | Average Latency (ms): 99.82
Queries per Second: 1039.82 | Cache Hit Ratio (%): 82.01 | Average Latency (ms): 8.71
Queries per Second: 4648.82 | Cache Hit Ratio (%): 91.85 | Average Latency (ms): 76.26
Queries per Second: 2775.65 | Cache Hit Ratio (%): 82.01 | Average Latency (ms): 23.6
Queries per Second: 2377.35 | Cache Hit Ratio (%): 91.85 | Average Latency (ms): 62.7
Queries per Second: 106.45 | Cache Hit Ratio (%): 84.92 | Average Latency (ms): 41.83
Queries per Second: 2505.47 | Cache Hit Ratio (%): 71.89 | Average Latency (ms): 54.37
Queries per Second: 2316.52 | Cache Hit Ratio (%): 85.39 | Average Latency (ms): 56.56
<end>