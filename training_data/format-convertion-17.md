Here's some markdown data, can you convert it to Json?
| Location | Humidity (%) | Wind Speed (km/h) | Day |
| --- | --- | --- | --- |
| Houston | 33 | 4.7 | Wednesday |
| Miami | 76 | 17.9 | Tuesday |
| Denver | 56 | 12.2 | Wednesday |
| Denver | 34 | 3.0 | Tuesday |<start>
[
    {
        "Location": "Houston",
        "Humidity (%)": 33,
        "Wind Speed (km/h)": 4.7,
        "Day": "Wednesday"
    },
    {
        "Location": "Miami",
        "Humidity (%)": 76,
        "Wind Speed (km/h)": 17.9,
        "Day": "Tuesday"
    },
    {
        "Location": "Denver",
        "Humidity (%)": 56,
        "Wind Speed (km/h)": 12.2,
        "Day": "Wednesday"
    },
    {
        "Location": "Denver",
        "Humidity (%)": 34,
        "Wind Speed (km/h)": 3.0,
        "Day": "Tuesday"
    }
]
<end>Convert this plain text to csv:
Company: AutoDrive | Sector: Biotech | Market Cap: Small Cap | Stock Price: 860.58 | Annual Revenue (B): 226.65 | Quarter: Q2
Company: GlobalTrade | Sector: Retail | Market Cap: Small Cap | Stock Price: 85.34 | Annual Revenue (B): 425.81 | Quarter: Q3
Company: EcoEnergy | Sector: Aerospace | Market Cap: Small Cap | Stock Price: 337.89 | Annual Revenue (B): 91.05 | Quarter: Q1
Company: TechCorp | Sector: Biotech | Market Cap: Large Cap | Stock Price: 40.68 | Annual Revenue (B): 98.57 | Quarter: Q1
Company: TechCorp | Sector: Finance | Market Cap: Mega Cap | Stock Price: 183.41 | Annual Revenue (B): 486.49 | Quarter: Q2
Company: BioPharm | Sector: Aerospace | Market Cap: Large Cap | Stock Price: 58.95 | Annual Revenue (B): 183.84 | Quarter: Q4
<start>
Company,Sector,Market Cap,Stock Price,Annual Revenue (B),Quarter
AutoDrive,Biotech,Small Cap,860.58,226.65,Q2
GlobalTrade,Retail,Small Cap,85.34,425.81,Q3
EcoEnergy,Aerospace,Small Cap,337.89,91.05,Q1
TechCorp,Biotech,Large Cap,40.68,98.57,Q1
TechCorp,Finance,Mega Cap,183.41,486.49,Q2
BioPharm,Aerospace,Large Cap,58.95,183.84,Q4
<end>Please transform the following CSV data into plain text:
Queries per Second,Cache Hit Ratio (%),Connection Count,Average Latency (ms)
453.91,96.24,122,86.42
2978.72,73.43,42,16.06
4482.76,80.08,204,40.87
4777.61,93.14,81,65.96
1519.08,89.33,265,86.42
921.18,88.55,128,85.52
3252.24,74.71,62,87.78
1892.54,86.62,226,45.72
4693.57,84.92,325,7.3
<start>
Queries per Second: 453.91 | Cache Hit Ratio (%): 96.24 | Connection Count: 122 | Average Latency (ms): 86.42
Queries per Second: 2978.72 | Cache Hit Ratio (%): 73.43 | Connection Count: 42 | Average Latency (ms): 16.06
Queries per Second: 4482.76 | Cache Hit Ratio (%): 80.08 | Connection Count: 204 | Average Latency (ms): 40.87
Queries per Second: 4777.61 | Cache Hit Ratio (%): 93.14 | Connection Count: 81 | Average Latency (ms): 65.96
Queries per Second: 1519.08 | Cache Hit Ratio (%): 89.33 | Connection Count: 265 | Average Latency (ms): 86.42
Queries per Second: 921.18 | Cache Hit Ratio (%): 88.55 | Connection Count: 128 | Average Latency (ms): 85.52
Queries per Second: 3252.24 | Cache Hit Ratio (%): 74.71 | Connection Count: 62 | Average Latency (ms): 87.78
Queries per Second: 1892.54 | Cache Hit Ratio (%): 86.62 | Connection Count: 226 | Average Latency (ms): 45.72
Queries per Second: 4693.57 | Cache Hit Ratio (%): 84.92 | Connection Count: 325 | Average Latency (ms): 7.3
<end>Here's some csv data, can you convert it to Markdown?
Restaurant Name,Location
Burger Haven,Seattle
Sushi World,New York
The Golden Spoon,Phoenix
The Golden Spoon,New York
The Golden Spoon,Houston
BBQ Barn,Chicago
Burger Haven,Phoenix
Pizza Planet,Los Angeles
<start>
| Restaurant Name | Location |
| --- | --- |
| Burger Haven | Seattle |
| Sushi World | New York |
| The Golden Spoon | Phoenix |
| The Golden Spoon | New York |
| The Golden Spoon | Houston |
| BBQ Barn | Chicago |
| Burger Haven | Phoenix |
| Pizza Planet | Los Angeles |
<end>Convert this markdown to csv:
| Product Name | SKU | Price |
| --- | --- | --- |
| Gadget | SKU-1062 | 76.29 |
| Instrument | SKU-1073 | 435.78 |
| Thingamajig | SKU-1058 | 327.72 |
| Doohickey | SKU-1083 | 247.87 |
| Thingamajig | SKU-1092 | 164.73 |
| Apparatus | SKU-1031 | 287.52 |
| Contraption | SKU-1047 | 196.5 |
| Apparatus | SKU-1096 | 18.29 |
| Widget | SKU-1008 | 486.5 |
| Whatchamacallit | SKU-1018 | 259.38 |<start>
Product Name,SKU,Price
Gadget,SKU-1062,76.29
Instrument,SKU-1073,435.78
Thingamajig,SKU-1058,327.72
Doohickey,SKU-1083,247.87
Thingamajig,SKU-1092,164.73
Apparatus,SKU-1031,287.52
Contraption,SKU-1047,196.5
Apparatus,SKU-1096,18.29
Widget,SKU-1008,486.5
Whatchamacallit,SKU-1018,259.38
<end>Transform this PLAIN TEXT structure to a Csv format:
Market Cap: Small Cap | Annual Revenue (B): 344.36 | Quarter: Q3
Market Cap: Mid Cap | Annual Revenue (B): 68.25 | Quarter: Q1
Market Cap: Large Cap | Annual Revenue (B): 186.54 | Quarter: Q4
Market Cap: Large Cap | Annual Revenue (B): 241.2 | Quarter: Q3
Market Cap: Large Cap | Annual Revenue (B): 429.65 | Quarter: Q4
<start>
Market Cap,Annual Revenue (B),Quarter
Small Cap,344.36,Q3
Mid Cap,68.25,Q1
Large Cap,186.54,Q4
Large Cap,241.2,Q3
Large Cap,429.65,Q4
<end>Can you change this JSON into Csv?
[
    {
        "Device ID": "device-0001",
        "Device Type": "Light Sensor",
        "Location": "Bedroom",
        "Battery Level (%)": 61.6,
        "Reading Value": -35.6
    },
    {
        "Device ID": "device-0023",
        "Device Type": "Temperature Sensor",
        "Location": "Bathroom",
        "Battery Level (%)": 73.1,
        "Reading Value": 66.87
    },
    {
        "Device ID": "device-0079",
        "Device Type": "Motion Detector",
        "Location": "Bedroom",
        "Battery Level (%)": 28.8,
        "Reading Value": 16.1
    },
    {
        "Device ID": "device-0070",
        "Device Type": "Pressure Sensor",
        "Location": "Office",
        "Battery Level (%)": 53.1,
        "Reading Value": 50.76
    },
    {
        "Device ID": "device-0038",
        "Device Type": "Temperature Sensor",
        "Location": "Garage",
        "Battery Level (%)": 88.5,
        "Reading Value": 80.14
    },
    {
        "Device ID": "device-0052",
        "Device Type": "Pressure Sensor",
        "Location": "Office",
        "Battery Level (%)": 29.8,
        "Reading Value": 69.02
    },
    {
        "Device ID": "device-0018",
        "Device Type": "Temperature Sensor",
        "Location": "Kitchen",
        "Battery Level (%)": 60.8,
        "Reading Value": 82.01
    },
    {
        "Device ID": "device-0053",
        "Device Type": "Pressure Sensor",
        "Location": "Bedroom",
        "Battery Level (%)": 62.8,
        "Reading Value": 19.87
    },
    {
        "Device ID": "device-0049",
        "Device Type": "Temperature Sensor",
        "Location": "Garden",
        "Battery Level (%)": 16.9,
        "Reading Value": 16.1
    }
]<start>
Device ID,Device Type,Location,Battery Level (%),Reading Value
device-0001,Light Sensor,Bedroom,61.6,-35.6
device-0023,Temperature Sensor,Bathroom,73.1,66.87
device-0079,Motion Detector,Bedroom,28.8,16.1
device-0070,Pressure Sensor,Office,53.1,50.76
device-0038,Temperature Sensor,Garage,88.5,80.14
device-0052,Pressure Sensor,Office,29.8,69.02
device-0018,Temperature Sensor,Kitchen,60.8,82.01
device-0053,Pressure Sensor,Bedroom,62.8,19.87
device-0049,Temperature Sensor,Garden,16.9,16.1
<end>Can you change this Json into Csv?
[
    {
        "Location": "Seattle",
        "Condition": "Sunny",
        "Temperature (C)": 8.3,
        "Humidity (%)": 86,
        "Wind Speed (km/h)": 27.7,
        "Day": "Monday"
    },
    {
        "Location": "Denver",
        "Condition": "Snowy",
        "Temperature (C)": 36.3,
        "Humidity (%)": 65,
        "Wind Speed (km/h)": 23.3,
        "Day": "Saturday"
    },
    {
        "Location": "Chicago",
        "Condition": "Foggy",
        "Temperature (C)": 26.6,
        "Humidity (%)": 34,
        "Wind Speed (km/h)": 21.0,
        "Day": "Friday"
    }
]<start>
Location,Condition,Temperature (C),Humidity (%),Wind Speed (km/h),Day
Seattle,Sunny,8.3,86,27.7,Monday
Denver,Snowy,36.3,65,23.3,Saturday
Chicago,Foggy,26.6,34,21.0,Friday
<end>Convert this markdown to PLAIN TEXT:
| Product Name | SKU | Price | Stock Quantity | Category | Supplier Name |
| --- | --- | --- | --- | --- | --- |
| Device | SKU-1080 | 204.32 | 499 | Toys | Umbrella Corp |
| Whatchamacallit | SKU-1055 | 112.05 | 239 | Sports | Wonka Industries |
| Widget | SKU-1062 | 261.06 | 70 | Electronics | Wonka Industries |
| Gizmo | SKU-1086 | 475.99 | 476 | Electronics | ACME Corp |
| Thingamajig | SKU-1081 | 81.26 | 172 | Automotive | Umbrella Corp |
| Device | SKU-1028 | 429.63 | 63 | Toys | Wonka Industries |
| Widget | SKU-1004 | 240.28 | 28 | Toys | Wonka Industries |
| Doohickey | SKU-1002 | 115.36 | 417 | Toys | ACME Corp |
| Device | SKU-1040 | 136.85 | 319 | Sports | ACME Corp |<start>
Product Name: Device | SKU: SKU-1080 | Price: 204.32 | Stock Quantity: 499 | Category: Toys | Supplier Name: Umbrella Corp
Product Name: Whatchamacallit | SKU: SKU-1055 | Price: 112.05 | Stock Quantity: 239 | Category: Sports | Supplier Name: Wonka Industries
Product Name: Widget | SKU: SKU-1062 | Price: 261.06 | Stock Quantity: 70 | Category: Electronics | Supplier Name: Wonka Industries
Product Name: Gizmo | SKU: SKU-1086 | Price: 475.99 | Stock Quantity: 476 | Category: Electronics | Supplier Name: ACME Corp
Product Name: Thingamajig | SKU: SKU-1081 | Price: 81.26 | Stock Quantity: 172 | Category: Automotive | Supplier Name: Umbrella Corp
Product Name: Device | SKU: SKU-1028 | Price: 429.63 | Stock Quantity: 63 | Category: Toys | Supplier Name: Wonka Industries
Product Name: Widget | SKU: SKU-1004 | Price: 240.28 | Stock Quantity: 28 | Category: Toys | Supplier Name: Wonka Industries
Product Name: Doohickey | SKU: SKU-1002 | Price: 115.36 | Stock Quantity: 417 | Category: Toys | Supplier Name: ACME Corp
Product Name: Device | SKU: SKU-1040 | Price: 136.85 | Stock Quantity: 319 | Category: Sports | Supplier Name: ACME Corp
<end>Convert this CSV to json:
Name,City
Floyd,Milwaukee
Andrew,Austin
Declan,Washington
Kendall,Columbus
Virgie,Nashville
Eli,San Diego
Faith,Los Angeles
Jake,Indianapolis
Amanda,Detroit
<start>
[
    {
        "Name": "Floyd",
        "City": "Milwaukee"
    },
    {
        "Name": "Andrew",
        "City": "Austin"
    },
    {
        "Name": "Declan",
        "City": "Washington"
    },
    {
        "Name": "Kendall",
        "City": "Columbus"
    },
    {
        "Name": "Virgie",
        "City": "Nashville"
    },
    {
        "Name": "Eli",
        "City": "San Diego"
    },
    {
        "Name": "Faith",
        "City": "Los Angeles"
    },
    {
        "Name": "Jake",
        "City": "Indianapolis"
    },
    {
        "Name": "Amanda",
        "City": "Detroit"
    }
]
<end>Transform this CSV structure to a markdown format:
Product Name,Price,Stock Quantity,Supplier Name
Device,200.67,464,Globex
Gizmo,415.92,94,ACME Corp
Contraption,199.94,472,Globex
Gizmo,398.79,54,ACME Corp
Instrument,305.36,372,Globex
Device,50.41,431,Wonka Industries
<start>
| Product Name | Price | Stock Quantity | Supplier Name |
| --- | --- | --- | --- |
| Device | 200.67 | 464 | Globex |
| Gizmo | 415.92 | 94 | ACME Corp |
| Contraption | 199.94 | 472 | Globex |
| Gizmo | 398.79 | 54 | ACME Corp |
| Instrument | 305.36 | 372 | Globex |
| Device | 50.41 | 431 | Wonka Industries |
<end>Please transform the following JSON data into csv:
[
    {
        "Company": "GlobalTrade",
        "Sector": "Energy",
        "Market Cap": "Mega Cap",
        "Annual Revenue (B)": 301.13
    },
    {
        "Company": "GlobalTrade",
        "Sector": "Aerospace",
        "Market Cap": "Mid Cap",
        "Annual Revenue (B)": 369.11
    },
    {
        "Company": "FinanceWorks",
        "Sector": "Aerospace",
        "Market Cap": "Large Cap",
        "Annual Revenue (B)": 219.49
    },
    {
        "Company": "BioPharm",
        "Sector": "Healthcare",
        "Market Cap": "Small Cap",
        "Annual Revenue (B)": 160.23
    }
]<start>
Company,Sector,Market Cap,Annual Revenue (B)
GlobalTrade,Energy,Mega Cap,301.13
GlobalTrade,Aerospace,Mid Cap,369.11
FinanceWorks,Aerospace,Large Cap,219.49
BioPharm,Healthcare,Small Cap,160.23
<end>Please transform the following Json data into YML:
[
    {
        "Title": "A Journey Through Time",
        "Genre": "Mystery",
        "Publication Year": 1988
    },
    {
        "Title": "A Journey Through Time",
        "Genre": "Historical",
        "Publication Year": 1956
    },
    {
        "Title": "Tales of the Brave",
        "Genre": "Historical",
        "Publication Year": 2002
    },
    {
        "Title": "Echoes of Eternity",
        "Genre": "Horror",
        "Publication Year": 1958
    }
]<start>
- Genre: Mystery
  Publication Year: 1988
  Title: A Journey Through Time
- Genre: Historical
  Publication Year: 1956
  Title: A Journey Through Time
- Genre: Historical
  Publication Year: 2002
  Title: Tales of the Brave
- Genre: Horror
  Publication Year: 1958
  Title: Echoes of Eternity
<end>Can you change this yaml into MARKDOWN?
- SKU: SKU-1033
  Stock Quantity: 123
  Supplier Name: Umbrella Corp
- SKU: SKU-1082
  Stock Quantity: 296
  Supplier Name: Umbrella Corp
- SKU: SKU-1021
  Stock Quantity: 349
  Supplier Name: Umbrella Corp
- SKU: SKU-1099
  Stock Quantity: 132
  Supplier Name: Wayne Enterprises
- SKU: SKU-1015
  Stock Quantity: 123
  Supplier Name: ACME Corp
- SKU: SKU-1048
  Stock Quantity: 303
  Supplier Name: Wayne Enterprises
- SKU: SKU-1018
  Stock Quantity: 303
  Supplier Name: Wonka Industries
- SKU: SKU-1054
  Stock Quantity: 50
  Supplier Name: Globex
- SKU: SKU-1060
  Stock Quantity: 273
  Supplier Name: Globex
<start>
| SKU | Stock Quantity | Supplier Name |
| --- | --- | --- |
| SKU-1033 | 123 | Umbrella Corp |
| SKU-1082 | 296 | Umbrella Corp |
| SKU-1021 | 349 | Umbrella Corp |
| SKU-1099 | 132 | Wayne Enterprises |
| SKU-1015 | 123 | ACME Corp |
| SKU-1048 | 303 | Wayne Enterprises |
| SKU-1018 | 303 | Wonka Industries |
| SKU-1054 | 50 | Globex |
| SKU-1060 | 273 | Globex |
<end>Transform this MARKDOWN structure to a yml format:
| Database Name | Queries per Second | Cache Hit Ratio (%) | Connection Count | Average Latency (ms) | Timestamp |
| --- | --- | --- | --- | --- | --- |
| SalesDB | 2911.89 | 71.7 | 79 | 45.92 | 2022-02-20 06:33:56 |
| MetricsDB | 4810.62 | 91.04 | 444 | 9.16 | 2023-12-25 13:44:38 |
| ProductsDB | 795.24 | 81.8 | 135 | 7.35 | 2021-03-15 19:09:08 |
| MetricsDB | 3078.88 | 76.13 | 428 | 13.72 | 2022-12-25 03:14:59 |
| MetricsDB | 850.88 | 98.96 | 157 | 8.68 | 2022-06-16 09:45:07 |<start>
- Average Latency (ms): 45.92
  Cache Hit Ratio (%): 71.7
  Connection Count: 79
  Database Name: SalesDB
  Queries per Second: 2911.89
  Timestamp: '2022-02-20 06:33:56'
- Average Latency (ms): 9.16
  Cache Hit Ratio (%): 91.04
  Connection Count: 444
  Database Name: MetricsDB
  Queries per Second: 4810.62
  Timestamp: '2023-12-25 13:44:38'
- Average Latency (ms): 7.35
  Cache Hit Ratio (%): 81.8
  Connection Count: 135
  Database Name: ProductsDB
  Queries per Second: 795.24
  Timestamp: '2021-03-15 19:09:08'
- Average Latency (ms): 13.72
  Cache Hit Ratio (%): 76.13
  Connection Count: 428
  Database Name: MetricsDB
  Queries per Second: 3078.88
  Timestamp: '2022-12-25 03:14:59'
- Average Latency (ms): 8.68
  Cache Hit Ratio (%): 98.96
  Connection Count: 157
  Database Name: MetricsDB
  Queries per Second: 850.88
  Timestamp: '2022-06-16 09:45:07'
<end>Convert this yaml to json:
- Age: 28
  Birth Month: March
  City: Los Angeles
- Age: 66
  Birth Month: September
  City: San Antonio
- Age: 31
  Birth Month: September
  City: New York
- Age: 25
  Birth Month: November
  City: Milwaukee
<start>
[
    {
        "Age": 28,
        "Birth Month": "March",
        "City": "Los Angeles"
    },
    {
        "Age": 66,
        "Birth Month": "September",
        "City": "San Antonio"
    },
    {
        "Age": 31,
        "Birth Month": "September",
        "City": "New York"
    },
    {
        "Age": 25,
        "Birth Month": "November",
        "City": "Milwaukee"
    }
]
<end>Please transform the following Plain text data into Json:
Title: Legends of the Rift | Author: Thorne Ironwood | Genre: Non-Fiction | Publication Year: 2012 | Rating: 1.3
Title: Whispers of the Abyss | Author: Luna Silverleaf | Genre: Non-Fiction | Publication Year: 2001 | Rating: 1.8
Title: The Last Sky | Author: Rowan Ashborne | Genre: Horror | Publication Year: 1980 | Rating: 4.2
Title: Tales of the Brave | Author: Orion Frostblade | Genre: Thriller | Publication Year: 1988 | Rating: 1.8
<start>
[
    {
        "Title": "Legends of the Rift",
        "Author": "Thorne Ironwood",
        "Genre": "Non-Fiction",
        "Publication Year": 2012,
        "Rating": 1.3
    },
    {
        "Title": "Whispers of the Abyss",
        "Author": "Luna Silverleaf",
        "Genre": "Non-Fiction",
        "Publication Year": 2001,
        "Rating": 1.8
    },
    {
        "Title": "The Last Sky",
        "Author": "Rowan Ashborne",
        "Genre": "Horror",
        "Publication Year": 1980,
        "Rating": 4.2
    },
    {
        "Title": "Tales of the Brave",
        "Author": "Orion Frostblade",
        "Genre": "Thriller",
        "Publication Year": 1988,
        "Rating": 1.8
    }
]
<end>Transform this Markdown structure to a PLAIN TEXT format:
| Company | Annual Revenue (B) | Quarter |
| --- | --- | --- |
| AutoDrive | 372.77 | Q4 |
| AutoDrive | 55.17 | Q1 |
| HealthPlus | 97.67 | Q4 |
| RetailHub | 489.93 | Q3 |
| TechCorp | 172.59 | Q2 |
| HealthPlus | 97.67 | Q2 |<start>
Company: AutoDrive | Annual Revenue (B): 372.77 | Quarter: Q4
Company: AutoDrive | Annual Revenue (B): 55.17 | Quarter: Q1
Company: HealthPlus | Annual Revenue (B): 97.67 | Quarter: Q4
Company: RetailHub | Annual Revenue (B): 489.93 | Quarter: Q3
Company: TechCorp | Annual Revenue (B): 172.59 | Quarter: Q2
Company: HealthPlus | Annual Revenue (B): 97.67 | Quarter: Q2
<end>Transform this json structure to a markdown format:
[
    {
        "SKU": "SKU-1043",
        "Price": 175.4,
        "Category": "Electronics",
        "Supplier Name": "ACME Corp"
    },
    {
        "SKU": "SKU-1052",
        "Price": 480.21,
        "Category": "Toys",
        "Supplier Name": "Wonka Industries"
    },
    {
        "SKU": "SKU-1098",
        "Price": 470.91,
        "Category": "Automotive",
        "Supplier Name": "Umbrella Corp"
    },
    {
        "SKU": "SKU-1022",
        "Price": 442.64,
        "Category": "Automotive",
        "Supplier Name": "Umbrella Corp"
    },
    {
        "SKU": "SKU-1046",
        "Price": 295.53,
        "Category": "Sports",
        "Supplier Name": "Wonka Industries"
    },
    {
        "SKU": "SKU-1010",
        "Price": 458.04,
        "Category": "Electronics",
        "Supplier Name": "ACME Corp"
    }
]<start>
| SKU | Price | Category | Supplier Name |
| --- | --- | --- | --- |
| SKU-1043 | 175.4 | Electronics | ACME Corp |
| SKU-1052 | 480.21 | Toys | Wonka Industries |
| SKU-1098 | 470.91 | Automotive | Umbrella Corp |
| SKU-1022 | 442.64 | Automotive | Umbrella Corp |
| SKU-1046 | 295.53 | Sports | Wonka Industries |
| SKU-1010 | 458.04 | Electronics | ACME Corp |
<end>Convert this PLAIN TEXT to JSON:
Location: Office | Reading Value: -28.64 | Timestamp: 2022-03-07 00:00:49
Location: Office | Reading Value: -32.71 | Timestamp: 2021-12-07 12:19:34
Location: Bedroom | Reading Value: -37.47 | Timestamp: 2023-04-14 14:19:34
Location: Hallway | Reading Value: 80.2 | Timestamp: 2021-07-28 14:50:55
Location: Garden | Reading Value: -15.5 | Timestamp: 2022-05-24 23:12:43
Location: Bathroom | Reading Value: -28.64 | Timestamp: 2021-07-27 21:23:57
Location: Garage | Reading Value: 75.04 | Timestamp: 2023-08-16 06:11:16
Location: Hallway | Reading Value: 21.13 | Timestamp: 2023-11-01 16:49:34
<start>
[
    {
        "Location": "Office",
        "Reading Value": -28.64,
        "Timestamp": "2022-03-07 00:00:49"
    },
    {
        "Location": "Office",
        "Reading Value": -32.71,
        "Timestamp": "2021-12-07 12:19:34"
    },
    {
        "Location": "Bedroom",
        "Reading Value": -37.47,
        "Timestamp": "2023-04-14 14:19:34"
    },
    {
        "Location": "Hallway",
        "Reading Value": 80.2,
        "Timestamp": "2021-07-28 14:50:55"
    },
    {
        "Location": "Garden",
        "Reading Value": -15.5,
        "Timestamp": "2022-05-24 23:12:43"
    },
    {
        "Location": "Bathroom",
        "Reading Value": -28.64,
        "Timestamp": "2021-07-27 21:23:57"
    },
    {
        "Location": "Garage",
        "Reading Value": 75.04,
        "Timestamp": "2023-08-16 06:11:16"
    },
    {
        "Location": "Hallway",
        "Reading Value": 21.13,
        "Timestamp": "2023-11-01 16:49:34"
    }
]
<end>Convert this yaml to plain text:
- Author: Luna Silverleaf
  Publication Year: 2014
  Rating: 2.9
- Author: Draven Blackthorn
  Publication Year: 1983
  Rating: 4.7
- Author: Orion Frostblade
  Publication Year: 1955
  Rating: 1.1
- Author: Sylvia Nightshade
  Publication Year: 2005
  Rating: 2.2
- Author: Isla Windrider
  Publication Year: 2022
  Rating: 4.3
<start>
Author: Luna Silverleaf | Publication Year: 2014 | Rating: 2.9
Author: Draven Blackthorn | Publication Year: 1983 | Rating: 4.7
Author: Orion Frostblade | Publication Year: 1955 | Rating: 1.1
Author: Sylvia Nightshade | Publication Year: 2005 | Rating: 2.2
Author: Isla Windrider | Publication Year: 2022 | Rating: 4.3
<end>Can you change this json into MARKDOWN?
[
    {
        "Database Name": "MetricsDB",
        "Queries per Second": 3906.76,
        "Cache Hit Ratio (%)": 91.72,
        "Connection Count": 31,
        "Timestamp": "2021-08-01 17:44:49"
    },
    {
        "Database Name": "UserDB",
        "Queries per Second": 603.41,
        "Cache Hit Ratio (%)": 78.19,
        "Connection Count": 193,
        "Timestamp": "2021-07-05 01:58:08"
    },
    {
        "Database Name": "UserDB",
        "Queries per Second": 407.94,
        "Cache Hit Ratio (%)": 71.06,
        "Connection Count": 489,
        "Timestamp": "2022-11-21 05:34:06"
    },
    {
        "Database Name": "AnalyticsDB",
        "Queries per Second": 3817.44,
        "Cache Hit Ratio (%)": 90.29,
        "Connection Count": 310,
        "Timestamp": "2023-04-22 11:53:38"
    },
    {
        "Database Name": "UserDB",
        "Queries per Second": 264.31,
        "Cache Hit Ratio (%)": 93.0,
        "Connection Count": 378,
        "Timestamp": "2021-09-18 08:08:40"
    },
    {
        "Database Name": "InventoryDB",
        "Queries per Second": 3259.88,
        "Cache Hit Ratio (%)": 94.26,
        "Connection Count": 113,
        "Timestamp": "2022-10-23 04:37:27"
    },
    {
        "Database Name": "MetricsDB",
        "Queries per Second": 4262.61,
        "Cache Hit Ratio (%)": 99.29,
        "Connection Count": 340,
        "Timestamp": "2022-01-18 16:36:07"
    }
]<start>
| Database Name | Queries per Second | Cache Hit Ratio (%) | Connection Count | Timestamp |
| --- | --- | --- | --- | --- |
| MetricsDB | 3906.76 | 91.72 | 31 | 2021-08-01 17:44:49 |
| UserDB | 603.41 | 78.19 | 193 | 2021-07-05 01:58:08 |
| UserDB | 407.94 | 71.06 | 489 | 2022-11-21 05:34:06 |
| AnalyticsDB | 3817.44 | 90.29 | 310 | 2023-04-22 11:53:38 |
| UserDB | 264.31 | 93.0 | 378 | 2021-09-18 08:08:40 |
| InventoryDB | 3259.88 | 94.26 | 113 | 2022-10-23 04:37:27 |
| MetricsDB | 4262.61 | 99.29 | 340 | 2022-01-18 16:36:07 |
<end>Transform this yml structure to a PLAIN TEXT format:
- Distance (miles): 1813.3
  Duration (hours): 29.7
  End Location: Houston
  Fuel Used (gallons): 57.4
  Trip Name: Lakeside Retreat
- Distance (miles): 1885.9
  Duration (hours): 25.4
  End Location: Houston
  Fuel Used (gallons): 59.4
  Trip Name: Desert Drive
- Distance (miles): 1835.2
  Duration (hours): 39.1
  End Location: Phoenix
  Fuel Used (gallons): 16.4
  Trip Name: Canyon Trek
- Distance (miles): 111.7
  Duration (hours): 70.4
  End Location: Chicago
  Fuel Used (gallons): 24.1
  Trip Name: Forest Journey
- Distance (miles): 873.6
  Duration (hours): 42.4
  End Location: Houston
  Fuel Used (gallons): 43.4
  Trip Name: Mountain Adventure
- Distance (miles): 282.4
  Duration (hours): 34.6
  End Location: San Francisco
  Fuel Used (gallons): 24.1
  Trip Name: Valley Voyage
<start>
Trip Name: Lakeside Retreat | End Location: Houston | Distance (miles): 1813.3 | Duration (hours): 29.7 | Fuel Used (gallons): 57.4
Trip Name: Desert Drive | End Location: Houston | Distance (miles): 1885.9 | Duration (hours): 25.4 | Fuel Used (gallons): 59.4
Trip Name: Canyon Trek | End Location: Phoenix | Distance (miles): 1835.2 | Duration (hours): 39.1 | Fuel Used (gallons): 16.4
Trip Name: Forest Journey | End Location: Chicago | Distance (miles): 111.7 | Duration (hours): 70.4 | Fuel Used (gallons): 24.1
Trip Name: Mountain Adventure | End Location: Houston | Distance (miles): 873.6 | Duration (hours): 42.4 | Fuel Used (gallons): 43.4
Trip Name: Valley Voyage | End Location: San Francisco | Distance (miles): 282.4 | Duration (hours): 34.6 | Fuel Used (gallons): 24.1
<end>Transform this yml structure to a markdown format:
- Average Latency (ms): 29.65
  Cache Hit Ratio (%): 73.79
  Connection Count: 180
  Database Name: InventoryDB
  Queries per Second: 3079.1
  Timestamp: '2021-11-09 18:08:06'
- Average Latency (ms): 95.12
  Cache Hit Ratio (%): 77.42
  Connection Count: 183
  Database Name: ProductsDB
  Queries per Second: 1981.49
  Timestamp: '2023-04-28 03:59:48'
- Average Latency (ms): 70.35
  Cache Hit Ratio (%): 86.18
  Connection Count: 334
  Database Name: LogsDB
  Queries per Second: 3800.2
  Timestamp: '2021-09-02 13:57:25'
- Average Latency (ms): 70.35
  Cache Hit Ratio (%): 77.55
  Connection Count: 32
  Database Name: AnalyticsDB
  Queries per Second: 4797.84
  Timestamp: '2023-03-14 02:23:04'
- Average Latency (ms): 85.25
  Cache Hit Ratio (%): 73.73
  Connection Count: 264
  Database Name: OrdersDB
  Queries per Second: 190.71
  Timestamp: '2021-11-22 10:18:20'
<start>
| Database Name | Queries per Second | Cache Hit Ratio (%) | Connection Count | Average Latency (ms) | Timestamp |
| --- | --- | --- | --- | --- | --- |
| InventoryDB | 3079.1 | 73.79 | 180 | 29.65 | 2021-11-09 18:08:06 |
| ProductsDB | 1981.49 | 77.42 | 183 | 95.12 | 2023-04-28 03:59:48 |
| LogsDB | 3800.2 | 86.18 | 334 | 70.35 | 2021-09-02 13:57:25 |
| AnalyticsDB | 4797.84 | 77.55 | 32 | 70.35 | 2023-03-14 02:23:04 |
| OrdersDB | 190.71 | 73.73 | 264 | 85.25 | 2021-11-22 10:18:20 |
<end>Here's some json data, can you convert it to CSV?
[
    {
        "Product Name": "Contraption",
        "SKU": "SKU-1097",
        "Stock Quantity": 145,
        "Category": "Household",
        "Supplier Name": "Wonka Industries"
    },
    {
        "Product Name": "Thingamajig",
        "SKU": "SKU-1097",
        "Stock Quantity": 0,
        "Category": "Household",
        "Supplier Name": "Umbrella Corp"
    },
    {
        "Product Name": "Widget",
        "SKU": "SKU-1088",
        "Stock Quantity": 214,
        "Category": "Automotive",
        "Supplier Name": "ACME Corp"
    },
    {
        "Product Name": "Apparatus",
        "SKU": "SKU-1073",
        "Stock Quantity": 294,
        "Category": "Automotive",
        "Supplier Name": "Wayne Enterprises"
    },
    {
        "Product Name": "Device",
        "SKU": "SKU-1078",
        "Stock Quantity": 281,
        "Category": "Electronics",
        "Supplier Name": "Globex"
    },
    {
        "Product Name": "Apparatus",
        "SKU": "SKU-1027",
        "Stock Quantity": 370,
        "Category": "Electronics",
        "Supplier Name": "Wayne Enterprises"
    },
    {
        "Product Name": "Contraption",
        "SKU": "SKU-1095",
        "Stock Quantity": 380,
        "Category": "Electronics",
        "Supplier Name": "Globex"
    }
]<start>
Product Name,SKU,Stock Quantity,Category,Supplier Name
Contraption,SKU-1097,145,Household,Wonka Industries
Thingamajig,SKU-1097,0,Household,Umbrella Corp
Widget,SKU-1088,214,Automotive,ACME Corp
Apparatus,SKU-1073,294,Automotive,Wayne Enterprises
Device,SKU-1078,281,Electronics,Globex
Apparatus,SKU-1027,370,Electronics,Wayne Enterprises
Contraption,SKU-1095,380,Electronics,Globex
<end>Convert this csv to Plain text:
Database Name,Connection Count,Timestamp
InventoryDB,244,2021-04-25 15:23:41
AnalyticsDB,304,2023-01-02 18:52:38
MetricsDB,482,2022-01-26 04:12:52
SessionsDB,285,2022-09-24 02:59:34
SalesDB,394,2023-04-28 19:39:23
AnalyticsDB,10,2023-01-05 19:00:16
<start>
Database Name: InventoryDB | Connection Count: 244 | Timestamp: 2021-04-25 15:23:41
Database Name: AnalyticsDB | Connection Count: 304 | Timestamp: 2023-01-02 18:52:38
Database Name: MetricsDB | Connection Count: 482 | Timestamp: 2022-01-26 04:12:52
Database Name: SessionsDB | Connection Count: 285 | Timestamp: 2022-09-24 02:59:34
Database Name: SalesDB | Connection Count: 394 | Timestamp: 2023-04-28 19:39:23
Database Name: AnalyticsDB | Connection Count: 10 | Timestamp: 2023-01-05 19:00:16
<end>Convert this json to MARKDOWN:
[
    {
        "Database Name": "ProfilesDB",
        "Queries per Second": 3428.71,
        "Cache Hit Ratio (%)": 98.69,
        "Connection Count": 445,
        "Average Latency (ms)": 70.71
    },
    {
        "Database Name": "UserDB",
        "Queries per Second": 3101.29,
        "Cache Hit Ratio (%)": 98.87,
        "Connection Count": 16,
        "Average Latency (ms)": 18.26
    },
    {
        "Database Name": "SalesDB",
        "Queries per Second": 1573.98,
        "Cache Hit Ratio (%)": 84.42,
        "Connection Count": 32,
        "Average Latency (ms)": 73.05
    },
    {
        "Database Name": "LogsDB",
        "Queries per Second": 4399.85,
        "Cache Hit Ratio (%)": 91.28,
        "Connection Count": 186,
        "Average Latency (ms)": 92.44
    },
    {
        "Database Name": "MetricsDB",
        "Queries per Second": 4399.85,
        "Cache Hit Ratio (%)": 79.28,
        "Connection Count": 327,
        "Average Latency (ms)": 97.39
    },
    {
        "Database Name": "UserDB",
        "Queries per Second": 1145.83,
        "Cache Hit Ratio (%)": 76.13,
        "Connection Count": 269,
        "Average Latency (ms)": 37.76
    },
    {
        "Database Name": "AnalyticsDB",
        "Queries per Second": 879.39,
        "Cache Hit Ratio (%)": 95.22,
        "Connection Count": 157,
        "Average Latency (ms)": 19.68
    },
    {
        "Database Name": "LogsDB",
        "Queries per Second": 2029.09,
        "Cache Hit Ratio (%)": 70.72,
        "Connection Count": 165,
        "Average Latency (ms)": 59.7
    },
    {
        "Database Name": "MetricsDB",
        "Queries per Second": 1918.28,
        "Cache Hit Ratio (%)": 87.39,
        "Connection Count": 31,
        "Average Latency (ms)": 47.93
    }
]<start>
| Database Name | Queries per Second | Cache Hit Ratio (%) | Connection Count | Average Latency (ms) |
| --- | --- | --- | --- | --- |
| ProfilesDB | 3428.71 | 98.69 | 445 | 70.71 |
| UserDB | 3101.29 | 98.87 | 16 | 18.26 |
| SalesDB | 1573.98 | 84.42 | 32 | 73.05 |
| LogsDB | 4399.85 | 91.28 | 186 | 92.44 |
| MetricsDB | 4399.85 | 79.28 | 327 | 97.39 |
| UserDB | 1145.83 | 76.13 | 269 | 37.76 |
| AnalyticsDB | 879.39 | 95.22 | 157 | 19.68 |
| LogsDB | 2029.09 | 70.72 | 165 | 59.7 |
| MetricsDB | 1918.28 | 87.39 | 31 | 47.93 |
<end>Here's some markdown data, can you convert it to json?
| Name | Age | Birth Month |
| --- | --- | --- |
| Silas | 50 | December |
| Roxie | 49 | February |
| Maxwell | 26 | June |
| Sherri | 43 | September |
| Minnie | 40 | May |
| Parker | 25 | May |
| Ebony | 24 | September |
| Beth | 47 | November |
| Chris | 40 | October |
| Amy | 44 | January |<start>
[
    {
        "Name": "Silas",
        "Age": 50,
        "Birth Month": "December"
    },
    {
        "Name": "Roxie",
        "Age": 49,
        "Birth Month": "February"
    },
    {
        "Name": "Maxwell",
        "Age": 26,
        "Birth Month": "June"
    },
    {
        "Name": "Sherri",
        "Age": 43,
        "Birth Month": "September"
    },
    {
        "Name": "Minnie",
        "Age": 40,
        "Birth Month": "May"
    },
    {
        "Name": "Parker",
        "Age": 25,
        "Birth Month": "May"
    },
    {
        "Name": "Ebony",
        "Age": 24,
        "Birth Month": "September"
    },
    {
        "Name": "Beth",
        "Age": 47,
        "Birth Month": "November"
    },
    {
        "Name": "Chris",
        "Age": 40,
        "Birth Month": "October"
    },
    {
        "Name": "Amy",
        "Age": 44,
        "Birth Month": "January"
    }
]
<end>Here's some json data, can you convert it to markdown?
[
    {
        "Name": "Ed",
        "Age": 65,
        "City": "Baltimore"
    },
    {
        "Name": "Dollie",
        "Age": 48,
        "City": "Washington"
    },
    {
        "Name": "Brielle",
        "Age": 41,
        "City": "San Diego"
    },
    {
        "Name": "Jacqueline",
        "Age": 31,
        "City": "Jacksonville"
    },
    {
        "Name": "Eli",
        "Age": 33,
        "City": "San Antonio"
    }
]<start>
| Name | Age | City |
| --- | --- | --- |
| Ed | 65 | Baltimore |
| Dollie | 48 | Washington |
| Brielle | 41 | San Diego |
| Jacqueline | 31 | Jacksonville |
| Eli | 33 | San Antonio |
<end>Can you change this plain text into Markdown?
Start Location: San Francisco | Distance (miles): 379.6 | Duration (hours): 11.5 | Fuel Used (gallons): 46.1
Start Location: Phoenix | Distance (miles): 1681.6 | Duration (hours): 49.5 | Fuel Used (gallons): 50.2
Start Location: Denver | Distance (miles): 2213.2 | Duration (hours): 43.2 | Fuel Used (gallons): 7.8
Start Location: New York | Distance (miles): 2588.5 | Duration (hours): 10.9 | Fuel Used (gallons): 24.6
Start Location: Phoenix | Distance (miles): 2337.6 | Duration (hours): 69.9 | Fuel Used (gallons): 98.4
Start Location: Houston | Distance (miles): 720.6 | Duration (hours): 57.5 | Fuel Used (gallons): 17.1
Start Location: Los Angeles | Distance (miles): 2362.5 | Duration (hours): 69.7 | Fuel Used (gallons): 70.5
<start>
| Start Location | Distance (miles) | Duration (hours) | Fuel Used (gallons) |
| --- | --- | --- | --- |
| San Francisco | 379.6 | 11.5 | 46.1 |
| Phoenix | 1681.6 | 49.5 | 50.2 |
| Denver | 2213.2 | 43.2 | 7.8 |
| New York | 2588.5 | 10.9 | 24.6 |
| Phoenix | 2337.6 | 69.9 | 98.4 |
| Houston | 720.6 | 57.5 | 17.1 |
| Los Angeles | 2362.5 | 69.7 | 70.5 |
<end>Here's some JSON data, can you convert it to Markdown?
[
    {
        "Age": 45,
        "Birth Month": "March"
    },
    {
        "Age": 33,
        "Birth Month": "February"
    },
    {
        "Age": 46,
        "Birth Month": "December"
    },
    {
        "Age": 63,
        "Birth Month": "August"
    },
    {
        "Age": 60,
        "Birth Month": "August"
    },
    {
        "Age": 22,
        "Birth Month": "June"
    },
    {
        "Age": 50,
        "Birth Month": "June"
    },
    {
        "Age": 69,
        "Birth Month": "September"
    },
    {
        "Age": 21,
        "Birth Month": "January"
    },
    {
        "Age": 47,
        "Birth Month": "July"
    }
]<start>
| Age | Birth Month |
| --- | --- |
| 45 | March |
| 33 | February |
| 46 | December |
| 63 | August |
| 60 | August |
| 22 | June |
| 50 | June |
| 69 | September |
| 21 | January |
| 47 | July |
<end>Can you change this yml into markdown?
- Price Range: $$$$
  Rating: 3
  Restaurant Name: Curry Corner
- Price Range: $$$$
  Rating: 1
  Restaurant Name: Curry Corner
- Price Range: $$$
  Rating: 2
  Restaurant Name: The Steakhouse
- Price Range: $$$$
  Rating: 1
  Restaurant Name: Burger Haven
- Price Range: $$$
  Rating: 2
  Restaurant Name: Pasta Palace
- Price Range: $
  Rating: 1
  Restaurant Name: Pizza Planet
<start>
| Restaurant Name | Rating | Price Range |
| --- | --- | --- |
| Curry Corner | 3 | $$$$ |
| Curry Corner | 1 | $$$$ |
| The Steakhouse | 2 | $$$ |
| Burger Haven | 1 | $$$$ |
| Pasta Palace | 2 | $$$ |
| Pizza Planet | 1 | $ |
<end>Transform this Json structure to a plain text format:
[
    {
        "Device ID": "device-0007",
        "Battery Level (%)": 82.5,
        "Reading Value": 17.59,
        "Timestamp": "2021-01-28 07:58:32"
    },
    {
        "Device ID": "device-0008",
        "Battery Level (%)": 87.1,
        "Reading Value": -16.57,
        "Timestamp": "2022-01-26 01:39:24"
    },
    {
        "Device ID": "device-0032",
        "Battery Level (%)": 14.1,
        "Reading Value": 7.3,
        "Timestamp": "2022-11-20 01:16:17"
    }
]<start>
Device ID: device-0007 | Battery Level (%): 82.5 | Reading Value: 17.59 | Timestamp: 2021-01-28 07:58:32
Device ID: device-0008 | Battery Level (%): 87.1 | Reading Value: -16.57 | Timestamp: 2022-01-26 01:39:24
Device ID: device-0032 | Battery Level (%): 14.1 | Reading Value: 7.3 | Timestamp: 2022-11-20 01:16:17
<end>Convert this CSV to YML:
Device ID,Device Type,Location,Battery Level (%),Reading Value
device-0024,Motion Detector,Kitchen,74.7,14.54
device-0043,Temperature Sensor,Bathroom,15.6,5.6
device-0060,Temperature Sensor,Garage,77.7,-31.83
device-0006,Humidity Sensor,Living Room,29.7,65.91
<start>
- Battery Level (%): 74.7
  Device ID: device-0024
  Device Type: Motion Detector
  Location: Kitchen
  Reading Value: 14.54
- Battery Level (%): 15.6
  Device ID: device-0043
  Device Type: Temperature Sensor
  Location: Bathroom
  Reading Value: 5.6
- Battery Level (%): 77.7
  Device ID: device-0060
  Device Type: Temperature Sensor
  Location: Garage
  Reading Value: -31.83
- Battery Level (%): 29.7
  Device ID: device-0006
  Device Type: Humidity Sensor
  Location: Living Room
  Reading Value: 65.91
<end>Transform this markdown structure to a JSON format:
| Age | Birth Month | Income |
| --- | --- | --- |
| 22 | December | 420000 |
| 62 | March | 375000 |
| 48 | June | 200000 |
| 68 | May | 210000 |
| 21 | November | 60000 |
| 20 | May | 40000 |
| 48 | February | 265000 |
| 29 | January | 65000 |
| 65 | March | 25000 |
| 32 | April | 180000 |<start>
[
    {
        "Age": 22,
        "Birth Month": "December",
        "Income": 420000
    },
    {
        "Age": 62,
        "Birth Month": "March",
        "Income": 375000
    },
    {
        "Age": 48,
        "Birth Month": "June",
        "Income": 200000
    },
    {
        "Age": 68,
        "Birth Month": "May",
        "Income": 210000
    },
    {
        "Age": 21,
        "Birth Month": "November",
        "Income": 60000
    },
    {
        "Age": 20,
        "Birth Month": "May",
        "Income": 40000
    },
    {
        "Age": 48,
        "Birth Month": "February",
        "Income": 265000
    },
    {
        "Age": 29,
        "Birth Month": "January",
        "Income": 65000
    },
    {
        "Age": 65,
        "Birth Month": "March",
        "Income": 25000
    },
    {
        "Age": 32,
        "Birth Month": "April",
        "Income": 180000
    }
]
<end>Please transform the following Csv data into YML:
Device ID,Battery Level (%),Reading Value
device-0068,88.2,48.79
device-0020,85.5,-26.33
device-0080,80.8,59.31
device-0032,22.8,-38.35
device-0072,62.1,70.19
device-0057,92.0,22.23
device-0001,34.3,-26.52
device-0040,49.8,14.01
device-0083,21.6,-38.84
device-0004,11.0,6.69
<start>
- Battery Level (%): 88.2
  Device ID: device-0068
  Reading Value: 48.79
- Battery Level (%): 85.5
  Device ID: device-0020
  Reading Value: -26.33
- Battery Level (%): 80.8
  Device ID: device-0080
  Reading Value: 59.31
- Battery Level (%): 22.8
  Device ID: device-0032
  Reading Value: -38.35
- Battery Level (%): 62.1
  Device ID: device-0072
  Reading Value: 70.19
- Battery Level (%): 92.0
  Device ID: device-0057
  Reading Value: 22.23
- Battery Level (%): 34.3
  Device ID: device-0001
  Reading Value: -26.52
- Battery Level (%): 49.8
  Device ID: device-0040
  Reading Value: 14.01
- Battery Level (%): 21.6
  Device ID: device-0083
  Reading Value: -38.84
- Battery Level (%): 11.0
  Device ID: device-0004
  Reading Value: 6.69
<end>Here's some plain text data, can you convert it to yml?
Trip Name: Historic Route | Start Location: Miami | End Location: Denver | Distance (miles): 2859.3 | Duration (hours): 43.9
Trip Name: Highway Odyssey | Start Location: Miami | End Location: San Francisco | Distance (miles): 995.3 | Duration (hours): 59.0
Trip Name: Highway Odyssey | Start Location: San Francisco | End Location: New York | Distance (miles): 1748.2 | Duration (hours): 62.8
Trip Name: Desert Drive | Start Location: Los Angeles | End Location: Phoenix | Distance (miles): 1472.1 | Duration (hours): 64.7
Trip Name: Desert Drive | Start Location: New York | End Location: Los Angeles | Distance (miles): 743.1 | Duration (hours): 21.6
Trip Name: Desert Drive | Start Location: Denver | End Location: Houston | Distance (miles): 1862.7 | Duration (hours): 15.7
Trip Name: Highway Odyssey | Start Location: New York | End Location: Phoenix | Distance (miles): 982.4 | Duration (hours): 17.1
Trip Name: Lakeside Retreat | Start Location: Houston | End Location: Phoenix | Distance (miles): 84.7 | Duration (hours): 48.3
Trip Name: Valley Voyage | Start Location: Houston | End Location: Phoenix | Distance (miles): 1833.3 | Duration (hours): 62.0
<start>
- Distance (miles): 2859.3
  Duration (hours): 43.9
  End Location: Denver
  Start Location: Miami
  Trip Name: Historic Route
- Distance (miles): 995.3
  Duration (hours): 59.0
  End Location: San Francisco
  Start Location: Miami
  Trip Name: Highway Odyssey
- Distance (miles): 1748.2
  Duration (hours): 62.8
  End Location: New York
  Start Location: San Francisco
  Trip Name: Highway Odyssey
- Distance (miles): 1472.1
  Duration (hours): 64.7
  End Location: Phoenix
  Start Location: Los Angeles
  Trip Name: Desert Drive
- Distance (miles): 743.1
  Duration (hours): 21.6
  End Location: Los Angeles
  Start Location: New York
  Trip Name: Desert Drive
- Distance (miles): 1862.7
  Duration (hours): 15.7
  End Location: Houston
  Start Location: Denver
  Trip Name: Desert Drive
- Distance (miles): 982.4
  Duration (hours): 17.1
  End Location: Phoenix
  Start Location: New York
  Trip Name: Highway Odyssey
- Distance (miles): 84.7
  Duration (hours): 48.3
  End Location: Phoenix
  Start Location: Houston
  Trip Name: Lakeside Retreat
- Distance (miles): 1833.3
  Duration (hours): 62.0
  End Location: Phoenix
  Start Location: Houston
  Trip Name: Valley Voyage
<end>Transform this CSV structure to a Json format:
Device ID,Device Type,Location,Battery Level (%),Reading Value,Timestamp
device-0097,Motion Detector,Bathroom,80.5,-7.72,2021-06-19 01:52:32
device-0018,Humidity Sensor,Bathroom,62.8,27.97,2022-06-19 00:29:56
device-0032,Pressure Sensor,Bathroom,91.6,-23.37,2022-07-25 08:27:46
device-0013,Light Sensor,Bedroom,10.8,27.97,2023-06-28 05:39:39
<start>
[
    {
        "Device ID": "device-0097",
        "Device Type": "Motion Detector",
        "Location": "Bathroom",
        "Battery Level (%)": 80.5,
        "Reading Value": -7.72,
        "Timestamp": "2021-06-19 01:52:32"
    },
    {
        "Device ID": "device-0018",
        "Device Type": "Humidity Sensor",
        "Location": "Bathroom",
        "Battery Level (%)": 62.8,
        "Reading Value": 27.97,
        "Timestamp": "2022-06-19 00:29:56"
    },
    {
        "Device ID": "device-0032",
        "Device Type": "Pressure Sensor",
        "Location": "Bathroom",
        "Battery Level (%)": 91.6,
        "Reading Value": -23.37,
        "Timestamp": "2022-07-25 08:27:46"
    },
    {
        "Device ID": "device-0013",
        "Device Type": "Light Sensor",
        "Location": "Bedroom",
        "Battery Level (%)": 10.8,
        "Reading Value": 27.97,
        "Timestamp": "2023-06-28 05:39:39"
    }
]
<end>Can you change this Markdown into CSV?
| Title | Genre | Box Office Earnings (M) |
| --- | --- | --- |
| Beyond the Veil | Comedy | 624.23 |
| Beyond the Veil | Comedy | 929.22 |
| Dreamwalker | Thriller | 207.29 |
| Escape from Earth | Horror | 89.76 |
| The Final Voyage | Horror | 497.5 |
| Dreamwalker | Adventure | 552.06 |
| Starbound Odyssey | Adventure | 907.19 |
| Escape from Earth | Sci-Fi | 921.04 |
| Rise of the Titans | Adventure | 251.94 |
| The Final Voyage | Thriller | 253.51 |<start>
Title,Genre,Box Office Earnings (M)
Beyond the Veil,Comedy,624.23
Beyond the Veil,Comedy,929.22
Dreamwalker,Thriller,207.29
Escape from Earth,Horror,89.76
The Final Voyage,Horror,497.5
Dreamwalker,Adventure,552.06
Starbound Odyssey,Adventure,907.19
Escape from Earth,Sci-Fi,921.04
Rise of the Titans,Adventure,251.94
The Final Voyage,Thriller,253.51
<end>Convert this Plain text to yml:
Restaurant Name: Vegan Delight | Cuisine: American | Location: Miami | Rating: 5
Restaurant Name: Pizza Planet | Cuisine: Mediterranean | Location: Phoenix | Rating: 5
Restaurant Name: Taco Town | Cuisine: Italian | Location: Seattle | Rating: 1
<start>
- Cuisine: American
  Location: Miami
  Rating: 5
  Restaurant Name: Vegan Delight
- Cuisine: Mediterranean
  Location: Phoenix
  Rating: 5
  Restaurant Name: Pizza Planet
- Cuisine: Italian
  Location: Seattle
  Rating: 1
  Restaurant Name: Taco Town
<end>Can you change this plain text into markdown?
Name: Serenity | Age: 49 | Income: 175000
Name: Derrick | Age: 30 | Income: 390000
Name: Estella | Age: 32 | Income: 250000
Name: Kyle | Age: 26 | Income: 425000
Name: Jake | Age: 66 | Income: 415000
Name: Lydia | Age: 40 | Income: 335000
Name: Florence | Age: 30 | Income: 365000
Name: Tristan | Age: 68 | Income: 405000
Name: Reginald | Age: 31 | Income: 115000
Name: Norma | Age: 44 | Income: 140000
<start>
| Name | Age | Income |
| --- | --- | --- |
| Serenity | 49 | 175000 |
| Derrick | 30 | 390000 |
| Estella | 32 | 250000 |
| Kyle | 26 | 425000 |
| Jake | 66 | 415000 |
| Lydia | 40 | 335000 |
| Florence | 30 | 365000 |
| Tristan | 68 | 405000 |
| Reginald | 31 | 115000 |
| Norma | 44 | 140000 |
<end>Please transform the following Csv data into Yml:
Title,Author,Genre,Publication Year,Rating
Whispers of the Abyss,Orion Frostblade,Fantasy,1988,2.6
The Silent Grove,Elara Moonshadow,Thriller,2003,3.2
The Forgotten World,Draven Blackthorn,Horror,2003,4.3
The Last Sky,Orion Frostblade,Horror,1962,4.2
Echoes of Eternity,Sylvia Nightshade,Non-Fiction,1994,1.9
Shadows of Solitude,Kara Firebrand,Science Fiction,2006,2.6
A Journey Through Time,Orion Frostblade,Science Fiction,1978,2.5
<start>
- Author: Orion Frostblade
  Genre: Fantasy
  Publication Year: 1988
  Rating: 2.6
  Title: Whispers of the Abyss
- Author: Elara Moonshadow
  Genre: Thriller
  Publication Year: 2003
  Rating: 3.2
  Title: The Silent Grove
- Author: Draven Blackthorn
  Genre: Horror
  Publication Year: 2003
  Rating: 4.3
  Title: The Forgotten World
- Author: Orion Frostblade
  Genre: Horror
  Publication Year: 1962
  Rating: 4.2
  Title: The Last Sky
- Author: Sylvia Nightshade
  Genre: Non-Fiction
  Publication Year: 1994
  Rating: 1.9
  Title: Echoes of Eternity
- Author: Kara Firebrand
  Genre: Science Fiction
  Publication Year: 2006
  Rating: 2.6
  Title: Shadows of Solitude
- Author: Orion Frostblade
  Genre: Science Fiction
  Publication Year: 1978
  Rating: 2.5
  Title: A Journey Through Time
<end>Transform this Markdown structure to a CSV format:
| Database Name | Queries per Second | Cache Hit Ratio (%) | Connection Count | Average Latency (ms) | Timestamp |
| --- | --- | --- | --- | --- | --- |
| ProductsDB | 1816.37 | 75.7 | 109 | 41.82 | 2022-01-21 08:38:15 |
| SalesDB | 1042.39 | 85.64 | 139 | 67.29 | 2022-02-02 11:18:06 |
| MetricsDB | 3990.36 | 92.57 | 86 | 69.24 | 2023-06-05 20:25:27 |<start>
Database Name,Queries per Second,Cache Hit Ratio (%),Connection Count,Average Latency (ms),Timestamp
ProductsDB,1816.37,75.7,109,41.82,2022-01-21 08:38:15
SalesDB,1042.39,85.64,139,67.29,2022-02-02 11:18:06
MetricsDB,3990.36,92.57,86,69.24,2023-06-05 20:25:27
<end>Transform this Csv structure to a json format:
Product Name,SKU,Price,Stock Quantity,Category,Supplier Name
Apparatus,SKU-1036,270.93,403,Automotive,ACME Corp
Device,SKU-1060,23.54,127,Household,Umbrella Corp
Widget,SKU-1025,222.43,25,Household,Wonka Industries
Gizmo,SKU-1062,245.07,4,Sports,ACME Corp
Gadget,SKU-1074,106.3,244,Household,Globex
Contraption,SKU-1039,137.83,232,Sports,Globex
Doohickey,SKU-1094,150.56,80,Automotive,Wonka Industries
Whatchamacallit,SKU-1005,209.12,439,Household,ACME Corp
<start>
[
    {
        "Product Name": "Apparatus",
        "SKU": "SKU-1036",
        "Price": 270.93,
        "Stock Quantity": 403,
        "Category": "Automotive",
        "Supplier Name": "ACME Corp"
    },
    {
        "Product Name": "Device",
        "SKU": "SKU-1060",
        "Price": 23.54,
        "Stock Quantity": 127,
        "Category": "Household",
        "Supplier Name": "Umbrella Corp"
    },
    {
        "Product Name": "Widget",
        "SKU": "SKU-1025",
        "Price": 222.43,
        "Stock Quantity": 25,
        "Category": "Household",
        "Supplier Name": "Wonka Industries"
    },
    {
        "Product Name": "Gizmo",
        "SKU": "SKU-1062",
        "Price": 245.07,
        "Stock Quantity": 4,
        "Category": "Sports",
        "Supplier Name": "ACME Corp"
    },
    {
        "Product Name": "Gadget",
        "SKU": "SKU-1074",
        "Price": 106.3,
        "Stock Quantity": 244,
        "Category": "Household",
        "Supplier Name": "Globex"
    },
    {
        "Product Name": "Contraption",
        "SKU": "SKU-1039",
        "Price": 137.83,
        "Stock Quantity": 232,
        "Category": "Sports",
        "Supplier Name": "Globex"
    },
    {
        "Product Name": "Doohickey",
        "SKU": "SKU-1094",
        "Price": 150.56,
        "Stock Quantity": 80,
        "Category": "Automotive",
        "Supplier Name": "Wonka Industries"
    },
    {
        "Product Name": "Whatchamacallit",
        "SKU": "SKU-1005",
        "Price": 209.12,
        "Stock Quantity": 439,
        "Category": "Household",
        "Supplier Name": "ACME Corp"
    }
]
<end>Can you change this markdown into json?
| Company | Stock Price | Annual Revenue (B) | Quarter |
| --- | --- | --- | --- |
| FinanceWorks | 489.79 | 84.64 | Q4 |
| BioPharm | 53.61 | 311.59 | Q2 |
| BioPharm | 379.37 | 209.11 | Q2 |<start>
[
    {
        "Company": "FinanceWorks",
        "Stock Price": 489.79,
        "Annual Revenue (B)": 84.64,
        "Quarter": "Q4"
    },
    {
        "Company": "BioPharm",
        "Stock Price": 53.61,
        "Annual Revenue (B)": 311.59,
        "Quarter": "Q2"
    },
    {
        "Company": "BioPharm",
        "Stock Price": 379.37,
        "Annual Revenue (B)": 209.11,
        "Quarter": "Q2"
    }
]
<end>Convert this PLAIN TEXT to markdown:
Battery Level (%): 70.7 | Reading Value: -15.17 | Timestamp: 2021-09-02 07:00:05
Battery Level (%): 47.1 | Reading Value: 64.43 | Timestamp: 2022-10-07 02:01:41
Battery Level (%): 38.9 | Reading Value: 23.47 | Timestamp: 2021-09-13 12:57:02
Battery Level (%): 28.9 | Reading Value: 30.05 | Timestamp: 2021-01-03 14:44:00
<start>
| Battery Level (%) | Reading Value | Timestamp |
| --- | --- | --- |
| 70.7 | -15.17 | 2021-09-02 07:00:05 |
| 47.1 | 64.43 | 2022-10-07 02:01:41 |
| 38.9 | 23.47 | 2021-09-13 12:57:02 |
| 28.9 | 30.05 | 2021-01-03 14:44:00 |
<end>Here's some Plain text data, can you convert it to MARKDOWN?
Location: Phoenix | Condition: Windy | Temperature (C): 6.5 | Humidity (%): 82 | Wind Speed (km/h): 21.8
Location: Chicago | Condition: Stormy | Temperature (C): 2.2 | Humidity (%): 51 | Wind Speed (km/h): 23.8
Location: Los Angeles | Condition: Rainy | Temperature (C): 1.5 | Humidity (%): 71 | Wind Speed (km/h): 13.9
Location: Phoenix | Condition: Windy | Temperature (C): -4.0 | Humidity (%): 61 | Wind Speed (km/h): 15.2
Location: Denver | Condition: Rainy | Temperature (C): 26.8 | Humidity (%): 81 | Wind Speed (km/h): 19.5
Location: Chicago | Condition: Windy | Temperature (C): 37.4 | Humidity (%): 36 | Wind Speed (km/h): 2.8
Location: New York | Condition: Rainy | Temperature (C): 33.2 | Humidity (%): 54 | Wind Speed (km/h): 26.0
Location: Chicago | Condition: Stormy | Temperature (C): -0.2 | Humidity (%): 53 | Wind Speed (km/h): 27.1
Location: Houston | Condition: Rainy | Temperature (C): 4.7 | Humidity (%): 32 | Wind Speed (km/h): 25.8
Location: New York | Condition: Stormy | Temperature (C): 6.5 | Humidity (%): 22 | Wind Speed (km/h): 9.7
<start>
| Location | Condition | Temperature (C) | Humidity (%) | Wind Speed (km/h) |
| --- | --- | --- | --- | --- |
| Phoenix | Windy | 6.5 | 82 | 21.8 |
| Chicago | Stormy | 2.2 | 51 | 23.8 |
| Los Angeles | Rainy | 1.5 | 71 | 13.9 |
| Phoenix | Windy | -4.0 | 61 | 15.2 |
| Denver | Rainy | 26.8 | 81 | 19.5 |
| Chicago | Windy | 37.4 | 36 | 2.8 |
| New York | Rainy | 33.2 | 54 | 26.0 |
| Chicago | Stormy | -0.2 | 53 | 27.1 |
| Houston | Rainy | 4.7 | 32 | 25.8 |
| New York | Stormy | 6.5 | 22 | 9.7 |
<end>Convert this json to Markdown:
[
    {
        "Device ID": "device-0085",
        "Device Type": "Light Sensor",
        "Location": "Office",
        "Battery Level (%)": 35.9,
        "Reading Value": -34.5,
        "Timestamp": "2023-04-19 05:47:44"
    },
    {
        "Device ID": "device-0044",
        "Device Type": "Motion Detector",
        "Location": "Living Room",
        "Battery Level (%)": 58.7,
        "Reading Value": -34.5,
        "Timestamp": "2021-03-02 21:46:54"
    },
    {
        "Device ID": "device-0088",
        "Device Type": "Motion Detector",
        "Location": "Garage",
        "Battery Level (%)": 58.8,
        "Reading Value": 67.87,
        "Timestamp": "2022-11-13 14:06:18"
    },
    {
        "Device ID": "device-0091",
        "Device Type": "Pressure Sensor",
        "Location": "Bedroom",
        "Battery Level (%)": 62.9,
        "Reading Value": -5.51,
        "Timestamp": "2022-08-01 10:14:30"
    },
    {
        "Device ID": "device-0053",
        "Device Type": "Temperature Sensor",
        "Location": "Garden",
        "Battery Level (%)": 17.1,
        "Reading Value": 6.69,
        "Timestamp": "2022-12-22 17:10:38"
    },
    {
        "Device ID": "device-0009",
        "Device Type": "Temperature Sensor",
        "Location": "Garden",
        "Battery Level (%)": 62.0,
        "Reading Value": 43.33,
        "Timestamp": "2022-04-16 06:29:21"
    },
    {
        "Device ID": "device-0092",
        "Device Type": "Humidity Sensor",
        "Location": "Bedroom",
        "Battery Level (%)": 56.8,
        "Reading Value": 1.5,
        "Timestamp": "2023-12-10 21:10:32"
    },
    {
        "Device ID": "device-0084",
        "Device Type": "Light Sensor",
        "Location": "Bedroom",
        "Battery Level (%)": 98.4,
        "Reading Value": 77.6,
        "Timestamp": "2023-05-15 21:19:52"
    },
    {
        "Device ID": "device-0013",
        "Device Type": "Humidity Sensor",
        "Location": "Hallway",
        "Battery Level (%)": 60.3,
        "Reading Value": 29.49,
        "Timestamp": "2023-04-13 19:30:43"
    }
]<start>
| Device ID | Device Type | Location | Battery Level (%) | Reading Value | Timestamp |
| --- | --- | --- | --- | --- | --- |
| device-0085 | Light Sensor | Office | 35.9 | -34.5 | 2023-04-19 05:47:44 |
| device-0044 | Motion Detector | Living Room | 58.7 | -34.5 | 2021-03-02 21:46:54 |
| device-0088 | Motion Detector | Garage | 58.8 | 67.87 | 2022-11-13 14:06:18 |
| device-0091 | Pressure Sensor | Bedroom | 62.9 | -5.51 | 2022-08-01 10:14:30 |
| device-0053 | Temperature Sensor | Garden | 17.1 | 6.69 | 2022-12-22 17:10:38 |
| device-0009 | Temperature Sensor | Garden | 62.0 | 43.33 | 2022-04-16 06:29:21 |
| device-0092 | Humidity Sensor | Bedroom | 56.8 | 1.5 | 2023-12-10 21:10:32 |
| device-0084 | Light Sensor | Bedroom | 98.4 | 77.6 | 2023-05-15 21:19:52 |
| device-0013 | Humidity Sensor | Hallway | 60.3 | 29.49 | 2023-04-13 19:30:43 |
<end>Transform this csv structure to a json format:
Title,Author,Genre,Publication Year,Rating
Echoes of Eternity,Draven Blackthorn,Horror,2006,4.9
Tales of the Brave,Galen Starfire,Non-Fiction,1980,1.8
Shadows of Solitude,Rowan Ashborne,Mystery,1985,4.9
<start>
[
    {
        "Title": "Echoes of Eternity",
        "Author": "Draven Blackthorn",
        "Genre": "Horror",
        "Publication Year": 2006,
        "Rating": 4.9
    },
    {
        "Title": "Tales of the Brave",
        "Author": "Galen Starfire",
        "Genre": "Non-Fiction",
        "Publication Year": 1980,
        "Rating": 1.8
    },
    {
        "Title": "Shadows of Solitude",
        "Author": "Rowan Ashborne",
        "Genre": "Mystery",
        "Publication Year": 1985,
        "Rating": 4.9
    }
]
<end>Transform this YML structure to a Json format:
- Location: Phoenix
  Price Range: $$$$$
  Rating: 1
  Restaurant Name: Curry Corner
- Location: San Francisco
  Price Range: $
  Rating: 5
  Restaurant Name: The Steakhouse
- Location: Phoenix
  Price Range: $$$
  Rating: 2
  Restaurant Name: Pasta Palace
- Location: Phoenix
  Price Range: $$$
  Rating: 5
  Restaurant Name: Taco Town
- Location: Seattle
  Price Range: $$
  Rating: 3
  Restaurant Name: Curry Corner
- Location: San Francisco
  Price Range: $$
  Rating: 3
  Restaurant Name: Vegan Delight
- Location: Phoenix
  Price Range: $$$$
  Rating: 2
  Restaurant Name: The Golden Spoon
- Location: New York
  Price Range: $$$$
  Rating: 3
  Restaurant Name: Curry Corner
- Location: Houston
  Price Range: $$$
  Rating: 4
  Restaurant Name: The Golden Spoon
- Location: Chicago
  Price Range: $$$
  Rating: 5
  Restaurant Name: Taco Town
<start>
[
    {
        "Restaurant Name": "Curry Corner",
        "Location": "Phoenix",
        "Rating": 1,
        "Price Range": "$$$$$"
    },
    {
        "Restaurant Name": "The Steakhouse",
        "Location": "San Francisco",
        "Rating": 5,
        "Price Range": "$"
    },
    {
        "Restaurant Name": "Pasta Palace",
        "Location": "Phoenix",
        "Rating": 2,
        "Price Range": "$$$"
    },
    {
        "Restaurant Name": "Taco Town",
        "Location": "Phoenix",
        "Rating": 5,
        "Price Range": "$$$"
    },
    {
        "Restaurant Name": "Curry Corner",
        "Location": "Seattle",
        "Rating": 3,
        "Price Range": "$$"
    },
    {
        "Restaurant Name": "Vegan Delight",
        "Location": "San Francisco",
        "Rating": 3,
        "Price Range": "$$"
    },
    {
        "Restaurant Name": "The Golden Spoon",
        "Location": "Phoenix",
        "Rating": 2,
        "Price Range": "$$$$"
    },
    {
        "Restaurant Name": "Curry Corner",
        "Location": "New York",
        "Rating": 3,
        "Price Range": "$$$$"
    },
    {
        "Restaurant Name": "The Golden Spoon",
        "Location": "Houston",
        "Rating": 4,
        "Price Range": "$$$"
    },
    {
        "Restaurant Name": "Taco Town",
        "Location": "Chicago",
        "Rating": 5,
        "Price Range": "$$$"
    }
]
<end>Here's some CSV data, can you convert it to json?
Author,Genre
Kara Firebrand,Non-Fiction
Isla Windrider,Thriller
Elara Moonshadow,Romance
<start>
[
    {
        "Author": "Kara Firebrand",
        "Genre": "Non-Fiction"
    },
    {
        "Author": "Isla Windrider",
        "Genre": "Thriller"
    },
    {
        "Author": "Elara Moonshadow",
        "Genre": "Romance"
    }
]
<end>Here's some Json data, can you convert it to MARKDOWN?
[
    {
        "Company": "BioLife",
        "Open Price": 1271.87,
        "Close Price": 307.22,
        "High Price": 1271.87
    },
    {
        "Company": "RetailWorld",
        "Open Price": 1497.17,
        "Close Price": 50.1,
        "High Price": 1497.17
    },
    {
        "Company": "AutoMotive",
        "Open Price": 628.97,
        "Close Price": 317.37,
        "High Price": 1065.15
    },
    {
        "Company": "GreenEnergy",
        "Open Price": 778.69,
        "Close Price": 405.0,
        "High Price": 778.69
    },
    {
        "Company": "BioLife",
        "Open Price": 1419.89,
        "Close Price": 984.5,
        "High Price": 1419.89
    },
    {
        "Company": "GreenEnergy",
        "Open Price": 176.32,
        "Close Price": 155.82,
        "High Price": 176.32
    },
    {
        "Company": "TechnoCorp",
        "Open Price": 723.52,
        "Close Price": 1428.97,
        "High Price": 1428.97
    },
    {
        "Company": "FinanceTrust",
        "Open Price": 203.63,
        "Close Price": 205.33,
        "High Price": 235.77
    },
    {
        "Company": "FinanceTrust",
        "Open Price": 190.14,
        "Close Price": 1467.86,
        "High Price": 1467.86
    },
    {
        "Company": "AutoMotive",
        "Open Price": 652.87,
        "Close Price": 529.7,
        "High Price": 652.87
    }
]<start>
| Company | Open Price | Close Price | High Price |
| --- | --- | --- | --- |
| BioLife | 1271.87 | 307.22 | 1271.87 |
| RetailWorld | 1497.17 | 50.1 | 1497.17 |
| AutoMotive | 628.97 | 317.37 | 1065.15 |
| GreenEnergy | 778.69 | 405.0 | 778.69 |
| BioLife | 1419.89 | 984.5 | 1419.89 |
| GreenEnergy | 176.32 | 155.82 | 176.32 |
| TechnoCorp | 723.52 | 1428.97 | 1428.97 |
| FinanceTrust | 203.63 | 205.33 | 235.77 |
| FinanceTrust | 190.14 | 1467.86 | 1467.86 |
| AutoMotive | 652.87 | 529.7 | 652.87 |
<end>Transform this yml structure to a plain text format:
- Connection Count: 131
  Database Name: MetricsDB
  Timestamp: '2023-04-11 07:43:32'
- Connection Count: 433
  Database Name: InventoryDB
  Timestamp: '2021-11-10 17:22:38'
- Connection Count: 110
  Database Name: UserDB
  Timestamp: '2022-12-12 17:12:04'
- Connection Count: 131
  Database Name: SessionsDB
  Timestamp: '2023-09-17 23:11:54'
- Connection Count: 406
  Database Name: SessionsDB
  Timestamp: '2022-09-12 01:51:47'
- Connection Count: 53
  Database Name: ProductsDB
  Timestamp: '2021-03-08 17:11:07'
- Connection Count: 308
  Database Name: ProfilesDB
  Timestamp: '2021-01-24 08:57:24'
- Connection Count: 141
  Database Name: OrdersDB
  Timestamp: '2021-03-27 16:58:07'
- Connection Count: 318
  Database Name: InventoryDB
  Timestamp: '2022-07-04 00:01:29'
<start>
Database Name: MetricsDB | Connection Count: 131 | Timestamp: 2023-04-11 07:43:32
Database Name: InventoryDB | Connection Count: 433 | Timestamp: 2021-11-10 17:22:38
Database Name: UserDB | Connection Count: 110 | Timestamp: 2022-12-12 17:12:04
Database Name: SessionsDB | Connection Count: 131 | Timestamp: 2023-09-17 23:11:54
Database Name: SessionsDB | Connection Count: 406 | Timestamp: 2022-09-12 01:51:47
Database Name: ProductsDB | Connection Count: 53 | Timestamp: 2021-03-08 17:11:07
Database Name: ProfilesDB | Connection Count: 308 | Timestamp: 2021-01-24 08:57:24
Database Name: OrdersDB | Connection Count: 141 | Timestamp: 2021-03-27 16:58:07
Database Name: InventoryDB | Connection Count: 318 | Timestamp: 2022-07-04 00:01:29
<end>Here's some plain text data, can you convert it to YAML?
Product Name: Doohickey | SKU: SKU-1094 | Price: 332.23 | Supplier Name: Globex
Product Name: Apparatus | SKU: SKU-1024 | Price: 132.01 | Supplier Name: Umbrella Corp
Product Name: Contraption | SKU: SKU-1090 | Price: 160.97 | Supplier Name: Wonka Industries
Product Name: Instrument | SKU: SKU-1004 | Price: 256.45 | Supplier Name: Umbrella Corp
<start>
- Price: 332.23
  Product Name: Doohickey
  SKU: SKU-1094
  Supplier Name: Globex
- Price: 132.01
  Product Name: Apparatus
  SKU: SKU-1024
  Supplier Name: Umbrella Corp
- Price: 160.97
  Product Name: Contraption
  SKU: SKU-1090
  Supplier Name: Wonka Industries
- Price: 256.45
  Product Name: Instrument
  SKU: SKU-1004
  Supplier Name: Umbrella Corp
<end>Convert this csv to yml:
Location,Condition,Temperature (C),Day
Chicago,Rainy,22.1,Tuesday
Chicago,Rainy,11.0,Tuesday
Houston,Foggy,17.6,Saturday
Miami,Windy,31.3,Wednesday
Seattle,Rainy,3.9,Monday
Los Angeles,Windy,20.4,Sunday
Chicago,Windy,34.3,Saturday
Seattle,Foggy,-9.2,Wednesday
Houston,Sunny,8.9,Thursday
Los Angeles,Stormy,16.5,Saturday
<start>
- Condition: Rainy
  Day: Tuesday
  Location: Chicago
  Temperature (C): 22.1
- Condition: Rainy
  Day: Tuesday
  Location: Chicago
  Temperature (C): 11.0
- Condition: Foggy
  Day: Saturday
  Location: Houston
  Temperature (C): 17.6
- Condition: Windy
  Day: Wednesday
  Location: Miami
  Temperature (C): 31.3
- Condition: Rainy
  Day: Monday
  Location: Seattle
  Temperature (C): 3.9
- Condition: Windy
  Day: Sunday
  Location: Los Angeles
  Temperature (C): 20.4
- Condition: Windy
  Day: Saturday
  Location: Chicago
  Temperature (C): 34.3
- Condition: Foggy
  Day: Wednesday
  Location: Seattle
  Temperature (C): -9.2
- Condition: Sunny
  Day: Thursday
  Location: Houston
  Temperature (C): 8.9
- Condition: Stormy
  Day: Saturday
  Location: Los Angeles
  Temperature (C): 16.5
<end>Here's some Markdown data, can you convert it to plain text?
| Name | City | Income |
| --- | --- | --- |
| Maryann | Denver | 415000 |
| Floyd | Las Vegas | 130000 |
| Maxwell | San Diego | 265000 |<start>
Name: Maryann | City: Denver | Income: 415000
Name: Floyd | City: Las Vegas | Income: 130000
Name: Maxwell | City: San Diego | Income: 265000
<end>Please transform the following Csv data into Markdown:
Device ID,Battery Level (%),Reading Value,Timestamp
device-0036,61.1,59.51,2022-05-09 11:06:49
device-0093,28.9,-4.3,2022-07-28 20:18:01
device-0073,73.9,-1.6,2021-09-08 18:35:44
<start>
| Device ID | Battery Level (%) | Reading Value | Timestamp |
| --- | --- | --- | --- |
| device-0036 | 61.1 | 59.51 | 2022-05-09 11:06:49 |
| device-0093 | 28.9 | -4.3 | 2022-07-28 20:18:01 |
| device-0073 | 73.9 | -1.6 | 2021-09-08 18:35:44 |
<end>Here's some plain text data, can you convert it to markdown?
Author: Elara Moonshadow | Genre: Non-Fiction | Rating: 4.9
Author: Luna Silverleaf | Genre: Historical | Rating: 2.6
Author: Draven Blackthorn | Genre: Romance | Rating: 3.3
Author: Orion Frostblade | Genre: Thriller | Rating: 2.2
Author: Luna Silverleaf | Genre: Science Fiction | Rating: 3.0
<start>
| Author | Genre | Rating |
| --- | --- | --- |
| Elara Moonshadow | Non-Fiction | 4.9 |
| Luna Silverleaf | Historical | 2.6 |
| Draven Blackthorn | Romance | 3.3 |
| Orion Frostblade | Thriller | 2.2 |
| Luna Silverleaf | Science Fiction | 3.0 |
<end>Transform this PLAIN TEXT structure to a JSON format:
Open Price: 533.52 | Close Price: 795.3 | High Price: 795.3 | Low Price: 533.52 | Volume: 9505232
Open Price: 166.29 | Close Price: 166.29 | High Price: 578.09 | Low Price: 166.29 | Volume: 4468988
Open Price: 902.23 | Close Price: 1428.53 | High Price: 1428.53 | Low Price: 902.23 | Volume: 4468988
Open Price: 527.66 | Close Price: 961.59 | High Price: 961.59 | Low Price: 527.66 | Volume: 918242
Open Price: 309.16 | Close Price: 108.35 | High Price: 1030.4 | Low Price: 108.35 | Volume: 4684854
Open Price: 1224.15 | Close Price: 632.83 | High Price: 1224.15 | Low Price: 632.83 | Volume: 5302361
Open Price: 746.09 | Close Price: 616.6 | High Price: 787.17 | Low Price: 616.6 | Volume: 7315046
Open Price: 1386.71 | Close Price: 1338.25 | High Price: 1386.71 | Low Price: 233.33 | Volume: 2817528
Open Price: 546.04 | Close Price: 690.38 | High Price: 997.59 | Low Price: 309.16 | Volume: 327689
<start>
[
    {
        "Open Price": 533.52,
        "Close Price": 795.3,
        "High Price": 795.3,
        "Low Price": 533.52,
        "Volume": 9505232
    },
    {
        "Open Price": 166.29,
        "Close Price": 166.29,
        "High Price": 578.09,
        "Low Price": 166.29,
        "Volume": 4468988
    },
    {
        "Open Price": 902.23,
        "Close Price": 1428.53,
        "High Price": 1428.53,
        "Low Price": 902.23,
        "Volume": 4468988
    },
    {
        "Open Price": 527.66,
        "Close Price": 961.59,
        "High Price": 961.59,
        "Low Price": 527.66,
        "Volume": 918242
    },
    {
        "Open Price": 309.16,
        "Close Price": 108.35,
        "High Price": 1030.4,
        "Low Price": 108.35,
        "Volume": 4684854
    },
    {
        "Open Price": 1224.15,
        "Close Price": 632.83,
        "High Price": 1224.15,
        "Low Price": 632.83,
        "Volume": 5302361
    },
    {
        "Open Price": 746.09,
        "Close Price": 616.6,
        "High Price": 787.17,
        "Low Price": 616.6,
        "Volume": 7315046
    },
    {
        "Open Price": 1386.71,
        "Close Price": 1338.25,
        "High Price": 1386.71,
        "Low Price": 233.33,
        "Volume": 2817528
    },
    {
        "Open Price": 546.04,
        "Close Price": 690.38,
        "High Price": 997.59,
        "Low Price": 309.16,
        "Volume": 327689
    }
]
<end>Here's some CSV data, can you convert it to plain text?
Trip Name,Start Location,Fuel Used (gallons)
Valley Voyage,Chicago,53.6
Mountain Adventure,San Francisco,51.2
Forest Journey,San Francisco,71.2
Historic Route,Phoenix,9.1
Valley Voyage,San Francisco,73.7
<start>
Trip Name: Valley Voyage | Start Location: Chicago | Fuel Used (gallons): 53.6
Trip Name: Mountain Adventure | Start Location: San Francisco | Fuel Used (gallons): 51.2
Trip Name: Forest Journey | Start Location: San Francisco | Fuel Used (gallons): 71.2
Trip Name: Historic Route | Start Location: Phoenix | Fuel Used (gallons): 9.1
Trip Name: Valley Voyage | Start Location: San Francisco | Fuel Used (gallons): 73.7
<end>Transform this Json structure to a Markdown format:
[
    {
        "Product Name": "Apparatus",
        "SKU": "SKU-1036",
        "Stock Quantity": 185,
        "Category": "Automotive"
    },
    {
        "Product Name": "Gizmo",
        "SKU": "SKU-1041",
        "Stock Quantity": 121,
        "Category": "Sports"
    },
    {
        "Product Name": "Contraption",
        "SKU": "SKU-1021",
        "Stock Quantity": 72,
        "Category": "Sports"
    },
    {
        "Product Name": "Instrument",
        "SKU": "SKU-1028",
        "Stock Quantity": 257,
        "Category": "Electronics"
    }
]<start>
| Product Name | SKU | Stock Quantity | Category |
| --- | --- | --- | --- |
| Apparatus | SKU-1036 | 185 | Automotive |
| Gizmo | SKU-1041 | 121 | Sports |
| Contraption | SKU-1021 | 72 | Sports |
| Instrument | SKU-1028 | 257 | Electronics |
<end>Please transform the following markdown data into json:
| Date | Open Price | High Price | Volume |
| --- | --- | --- | --- |
| 2013-10-07 | 816.9 | 1398.99 | 7191458 |
| 2020-12-08 | 492.77 | 492.77 | 795264 |
| 2018-12-18 | 955.72 | 955.72 | 2924734 |<start>
[
    {
        "Date": "2013-10-07",
        "Open Price": 816.9,
        "High Price": 1398.99,
        "Volume": 7191458
    },
    {
        "Date": "2020-12-08",
        "Open Price": 492.77,
        "High Price": 492.77,
        "Volume": 795264
    },
    {
        "Date": "2018-12-18",
        "Open Price": 955.72,
        "High Price": 955.72,
        "Volume": 2924734
    }
]
<end>Please transform the following markdown data into CSV:
| Company | Date | Open Price | Close Price | High Price | Low Price | Volume |
| --- | --- | --- | --- | --- | --- | --- |
| HealthGen | 2015-12-20 | 136.11 | 592.26 | 592.26 | 136.11 | 7412689 |
| HealthGen | 2011-12-01 | 47.09 | 314.62 | 553.22 | 47.09 | 2318011 |
| RetailWorld | 2023-05-10 | 339.22 | 261.68 | 339.22 | 246.09 | 9016066 |<start>
Company,Date,Open Price,Close Price,High Price,Low Price,Volume
HealthGen,2015-12-20,136.11,592.26,592.26,136.11,7412689
HealthGen,2011-12-01,47.09,314.62,553.22,47.09,2318011
RetailWorld,2023-05-10,339.22,261.68,339.22,246.09,9016066
<end>Convert this Markdown to yaml:
| Company | Sector | Market Cap | Annual Revenue (B) | Quarter |
| --- | --- | --- | --- | --- |
| AutoDrive | Energy | Small Cap | 186.11 | Q2 |
| GlobalTrade | Biotech | Mega Cap | 161.41 | Q1 |
| EcoEnergy | Technology | Small Cap | 181.96 | Q4 |
| GlobalTrade | Technology | Small Cap | 93.38 | Q1 |<start>
- Annual Revenue (B): 186.11
  Company: AutoDrive
  Market Cap: Small Cap
  Quarter: Q2
  Sector: Energy
- Annual Revenue (B): 161.41
  Company: GlobalTrade
  Market Cap: Mega Cap
  Quarter: Q1
  Sector: Biotech
- Annual Revenue (B): 181.96
  Company: EcoEnergy
  Market Cap: Small Cap
  Quarter: Q4
  Sector: Technology
- Annual Revenue (B): 93.38
  Company: GlobalTrade
  Market Cap: Small Cap
  Quarter: Q1
  Sector: Technology
<end>Can you change this Csv into MARKDOWN?
Device ID,Location,Timestamp
device-0022,Hallway,2022-12-21 07:33:21
device-0005,Kitchen,2022-05-14 20:48:06
device-0003,Hallway,2022-08-13 01:37:58
device-0094,Garden,2023-08-18 12:30:05
device-0021,Bathroom,2023-10-01 18:42:13
device-0092,Garden,2022-12-01 12:07:33
device-0036,Garden,2022-08-28 11:32:21
<start>
| Device ID | Location | Timestamp |
| --- | --- | --- |
| device-0022 | Hallway | 2022-12-21 07:33:21 |
| device-0005 | Kitchen | 2022-05-14 20:48:06 |
| device-0003 | Hallway | 2022-08-13 01:37:58 |
| device-0094 | Garden | 2023-08-18 12:30:05 |
| device-0021 | Bathroom | 2023-10-01 18:42:13 |
| device-0092 | Garden | 2022-12-01 12:07:33 |
| device-0036 | Garden | 2022-08-28 11:32:21 |
<end>Convert this CSV to json:
Title,Author,Genre
The Silent Grove,Isla Windrider,Mystery
Echoes of Eternity,Isla Windrider,Historical
A Journey Through Time,Sylvia Nightshade,Non-Fiction
Echoes of Eternity,Galen Starfire,Mystery
Whispers of the Abyss,Sylvia Nightshade,Mystery
<start>
[
    {
        "Title": "The Silent Grove",
        "Author": "Isla Windrider",
        "Genre": "Mystery"
    },
    {
        "Title": "Echoes of Eternity",
        "Author": "Isla Windrider",
        "Genre": "Historical"
    },
    {
        "Title": "A Journey Through Time",
        "Author": "Sylvia Nightshade",
        "Genre": "Non-Fiction"
    },
    {
        "Title": "Echoes of Eternity",
        "Author": "Galen Starfire",
        "Genre": "Mystery"
    },
    {
        "Title": "Whispers of the Abyss",
        "Author": "Sylvia Nightshade",
        "Genre": "Mystery"
    }
]
<end>Transform this Plain text structure to a Markdown format:
Company: GreenEnergy | Open Price: 1100.12 | Close Price: 130.86 | High Price: 1100.12
Company: BioLife | Open Price: 1353.73 | Close Price: 592.45 | High Price: 1353.73
Company: HealthGen | Open Price: 1381.28 | Close Price: 1398.5 | High Price: 1398.5
<start>
| Company | Open Price | Close Price | High Price |
| --- | --- | --- | --- |
| GreenEnergy | 1100.12 | 130.86 | 1100.12 |
| BioLife | 1353.73 | 592.45 | 1353.73 |
| HealthGen | 1381.28 | 1398.5 | 1398.5 |
<end>Convert this Plain text to csv:
Restaurant Name: Burger Haven | Cuisine: Italian | Location: Houston | Rating: 3 | Price Range: $$
Restaurant Name: BBQ Barn | Cuisine: Chinese | Location: Seattle | Rating: 1 | Price Range: $$$
Restaurant Name: Burger Haven | Cuisine: American | Location: Miami | Rating: 1 | Price Range: $$
Restaurant Name: Pizza Planet | Cuisine: Chinese | Location: New York | Rating: 4 | Price Range: $$$$
Restaurant Name: Curry Corner | Cuisine: Italian | Location: San Francisco | Rating: 2 | Price Range: $$$$$
<start>
Restaurant Name,Cuisine,Location,Rating,Price Range
Burger Haven,Italian,Houston,3,$$
BBQ Barn,Chinese,Seattle,1,$$$
Burger Haven,American,Miami,1,$$
Pizza Planet,Chinese,New York,4,$$$$
Curry Corner,Italian,San Francisco,2,$$$$$
<end>Please transform the following Plain text data into csv:
Company: FinanceWorks | Sector: Finance | Market Cap: Small Cap | Stock Price: 373.59 | Annual Revenue (B): 147.33 | Quarter: Q1
Company: GlobalTrade | Sector: Healthcare | Market Cap: Mid Cap | Stock Price: 674.98 | Annual Revenue (B): 350.08 | Quarter: Q1
Company: FinanceWorks | Sector: Retail | Market Cap: Mega Cap | Stock Price: 492.16 | Annual Revenue (B): 213.1 | Quarter: Q4
Company: TechCorp | Sector: Automotive | Market Cap: Large Cap | Stock Price: 649.45 | Annual Revenue (B): 179.36 | Quarter: Q4
Company: BioPharm | Sector: Healthcare | Market Cap: Mega Cap | Stock Price: 915.68 | Annual Revenue (B): 52.25 | Quarter: Q4
Company: AeroSpace | Sector: Retail | Market Cap: Small Cap | Stock Price: 986.46 | Annual Revenue (B): 383.78 | Quarter: Q3
Company: HealthPlus | Sector: Biotech | Market Cap: Mega Cap | Stock Price: 975.62 | Annual Revenue (B): 109.01 | Quarter: Q3
Company: FinanceWorks | Sector: Biotech | Market Cap: Large Cap | Stock Price: 915.68 | Annual Revenue (B): 256.1 | Quarter: Q2
Company: TechCorp | Sector: Retail | Market Cap: Mid Cap | Stock Price: 518.85 | Annual Revenue (B): 270.59 | Quarter: Q1
Company: BioPharm | Sector: Retail | Market Cap: Large Cap | Stock Price: 889.58 | Annual Revenue (B): 171.75 | Quarter: Q3
<start>
Company,Sector,Market Cap,Stock Price,Annual Revenue (B),Quarter
FinanceWorks,Finance,Small Cap,373.59,147.33,Q1
GlobalTrade,Healthcare,Mid Cap,674.98,350.08,Q1
FinanceWorks,Retail,Mega Cap,492.16,213.1,Q4
TechCorp,Automotive,Large Cap,649.45,179.36,Q4
BioPharm,Healthcare,Mega Cap,915.68,52.25,Q4
AeroSpace,Retail,Small Cap,986.46,383.78,Q3
HealthPlus,Biotech,Mega Cap,975.62,109.01,Q3
FinanceWorks,Biotech,Large Cap,915.68,256.1,Q2
TechCorp,Retail,Mid Cap,518.85,270.59,Q1
BioPharm,Retail,Large Cap,889.58,171.75,Q3
<end>Here's some csv data, can you convert it to YML?
Company,Date,Close Price,High Price,Low Price,Volume
TechnoCorp,2023-03-02,501.28,1371.39,501.28,952799
MediaGroup,2015-09-13,248.28,863.21,82.39,3859975
AeroSystems,2022-01-18,373.73,538.36,292.67,8130014
<start>
- Close Price: 501.28
  Company: TechnoCorp
  Date: '2023-03-02'
  High Price: 1371.39
  Low Price: 501.28
  Volume: 952799
- Close Price: 248.28
  Company: MediaGroup
  Date: '2015-09-13'
  High Price: 863.21
  Low Price: 82.39
  Volume: 3859975
- Close Price: 373.73
  Company: AeroSystems
  Date: '2022-01-18'
  High Price: 538.36
  Low Price: 292.67
  Volume: 8130014
<end>Convert this plain text to Json:
Name: Angelica | City: Columbus | Income: 90000
Name: Kellie | City: Detroit | Income: 35000
Name: Kayla | City: Louisville | Income: 245000
Name: Floyd | City: Jacksonville | Income: 405000
<start>
[
    {
        "Name": "Angelica",
        "City": "Columbus",
        "Income": 90000
    },
    {
        "Name": "Kellie",
        "City": "Detroit",
        "Income": 35000
    },
    {
        "Name": "Kayla",
        "City": "Louisville",
        "Income": 245000
    },
    {
        "Name": "Floyd",
        "City": "Jacksonville",
        "Income": 405000
    }
]
<end>Please transform the following plain text data into CSV:
Genre: Historical | Publication Year: 1954
Genre: Mystery | Publication Year: 2011
Genre: Horror | Publication Year: 1982
Genre: Science Fiction | Publication Year: 2021
Genre: Historical | Publication Year: 1967
Genre: Horror | Publication Year: 1972
<start>
Genre,Publication Year
Historical,1954
Mystery,2011
Horror,1982
Science Fiction,2021
Historical,1967
Horror,1972
<end>Convert this YAML to PLAIN TEXT:
- Condition: Cloudy
  Temperature (C): -3.9
  Wind Speed (km/h): 11.2
- Condition: Windy
  Temperature (C): -3.2
  Wind Speed (km/h): 8.3
- Condition: Sunny
  Temperature (C): 39.6
  Wind Speed (km/h): 20.3
- Condition: Cloudy
  Temperature (C): 34.0
  Wind Speed (km/h): 25.4
- Condition: Sunny
  Temperature (C): 27.3
  Wind Speed (km/h): 0.3
<start>
Condition: Cloudy | Temperature (C): -3.9 | Wind Speed (km/h): 11.2
Condition: Windy | Temperature (C): -3.2 | Wind Speed (km/h): 8.3
Condition: Sunny | Temperature (C): 39.6 | Wind Speed (km/h): 20.3
Condition: Cloudy | Temperature (C): 34.0 | Wind Speed (km/h): 25.4
Condition: Sunny | Temperature (C): 27.3 | Wind Speed (km/h): 0.3
<end>Transform this YML structure to a JSON format:
- Battery Level (%): 22.5
  Device ID: device-0094
  Timestamp: '2023-10-22 09:26:37'
- Battery Level (%): 71.3
  Device ID: device-0043
  Timestamp: '2022-04-27 18:14:26'
- Battery Level (%): 61.6
  Device ID: device-0054
  Timestamp: '2021-11-26 11:19:58'
<start>
[
    {
        "Device ID": "device-0094",
        "Battery Level (%)": 22.5,
        "Timestamp": "2023-10-22 09:26:37"
    },
    {
        "Device ID": "device-0043",
        "Battery Level (%)": 71.3,
        "Timestamp": "2022-04-27 18:14:26"
    },
    {
        "Device ID": "device-0054",
        "Battery Level (%)": 61.6,
        "Timestamp": "2021-11-26 11:19:58"
    }
]
<end>Can you change this YML into markdown?
- Company: HealthGen
  Date: '2013-01-24'
  Open Price: 1190.95
  Volume: 2196281
- Company: FoodChain
  Date: '2012-05-11'
  Open Price: 769.65
  Volume: 8296390
- Company: MediaGroup
  Date: '2018-11-13'
  Open Price: 868.85
  Volume: 8629718
- Company: RetailWorld
  Date: '2019-11-14'
  Open Price: 1365.39
  Volume: 4347352
- Company: AutoMotive
  Date: '2013-08-03'
  Open Price: 1249.73
  Volume: 1059470
- Company: MediaGroup
  Date: '2011-07-25'
  Open Price: 1219.04
  Volume: 1004192
<start>
| Company | Date | Open Price | Volume |
| --- | --- | --- | --- |
| HealthGen | 2013-01-24 | 1190.95 | 2196281 |
| FoodChain | 2012-05-11 | 769.65 | 8296390 |
| MediaGroup | 2018-11-13 | 868.85 | 8629718 |
| RetailWorld | 2019-11-14 | 1365.39 | 4347352 |
| AutoMotive | 2013-08-03 | 1249.73 | 1059470 |
| MediaGroup | 2011-07-25 | 1219.04 | 1004192 |
<end>Here's some markdown data, can you convert it to csv?
| Title | Director | Genre | Release Year | Box Office Earnings (M) |
| --- | --- | --- | --- | --- |
| Escape from Earth | Talon Blackthorn | Sci-Fi | 2007 | 963.51 |
| Beyond the Veil | Talon Blackthorn | Action | 2001 | 588.09 |
| The Great Expedition | Aria Ravenwood | Thriller | 2012 | 599.49 |<start>
Title,Director,Genre,Release Year,Box Office Earnings (M)
Escape from Earth,Talon Blackthorn,Sci-Fi,2007,963.51
Beyond the Veil,Talon Blackthorn,Action,2001,588.09
The Great Expedition,Aria Ravenwood,Thriller,2012,599.49
<end>Please transform the following markdown data into json:
| Title | Author | Publication Year |
| --- | --- | --- |
| Shadows of Solitude | Rowan Ashborne | 1952 |
| The Forgotten World | Elara Moonshadow | 2014 |
| The Forgotten World | Galen Starfire | 1997 |
| Echoes of Eternity | Luna Silverleaf | 1972 |
| Echoes of Eternity | Galen Starfire | 1972 |<start>
[
    {
        "Title": "Shadows of Solitude",
        "Author": "Rowan Ashborne",
        "Publication Year": 1952
    },
    {
        "Title": "The Forgotten World",
        "Author": "Elara Moonshadow",
        "Publication Year": 2014
    },
    {
        "Title": "The Forgotten World",
        "Author": "Galen Starfire",
        "Publication Year": 1997
    },
    {
        "Title": "Echoes of Eternity",
        "Author": "Luna Silverleaf",
        "Publication Year": 1972
    },
    {
        "Title": "Echoes of Eternity",
        "Author": "Galen Starfire",
        "Publication Year": 1972
    }
]
<end>Please transform the following yml data into json:
- Genre: Fantasy
  Publication Year: 2012
  Rating: 1.8
- Genre: Romance
  Publication Year: 1970
  Rating: 1.2
- Genre: Mystery
  Publication Year: 2018
  Rating: 2.5
- Genre: Historical
  Publication Year: 1978
  Rating: 2.6
- Genre: Thriller
  Publication Year: 1961
  Rating: 4.1
- Genre: Horror
  Publication Year: 2014
  Rating: 1.9
- Genre: Thriller
  Publication Year: 1997
  Rating: 4.2
- Genre: Romance
  Publication Year: 1955
  Rating: 4.7
<start>
[
    {
        "Genre": "Fantasy",
        "Publication Year": 2012,
        "Rating": 1.8
    },
    {
        "Genre": "Romance",
        "Publication Year": 1970,
        "Rating": 1.2
    },
    {
        "Genre": "Mystery",
        "Publication Year": 2018,
        "Rating": 2.5
    },
    {
        "Genre": "Historical",
        "Publication Year": 1978,
        "Rating": 2.6
    },
    {
        "Genre": "Thriller",
        "Publication Year": 1961,
        "Rating": 4.1
    },
    {
        "Genre": "Horror",
        "Publication Year": 2014,
        "Rating": 1.9
    },
    {
        "Genre": "Thriller",
        "Publication Year": 1997,
        "Rating": 4.2
    },
    {
        "Genre": "Romance",
        "Publication Year": 1955,
        "Rating": 4.7
    }
]
<end>Can you change this JSON into csv?
[
    {
        "Device Type": "Motion Detector",
        "Location": "Living Room",
        "Reading Value": 52.53,
        "Timestamp": "2022-11-27 00:41:59"
    },
    {
        "Device Type": "Light Sensor",
        "Location": "Bedroom",
        "Reading Value": 29.95,
        "Timestamp": "2023-10-05 23:20:49"
    },
    {
        "Device Type": "Humidity Sensor",
        "Location": "Garage",
        "Reading Value": 76.16,
        "Timestamp": "2022-12-21 16:58:48"
    },
    {
        "Device Type": "Temperature Sensor",
        "Location": "Garden",
        "Reading Value": -6.66,
        "Timestamp": "2022-09-03 08:32:56"
    },
    {
        "Device Type": "Light Sensor",
        "Location": "Garden",
        "Reading Value": 57.69,
        "Timestamp": "2023-07-10 05:31:59"
    }
]<start>
Device Type,Location,Reading Value,Timestamp
Motion Detector,Living Room,52.53,2022-11-27 00:41:59
Light Sensor,Bedroom,29.95,2023-10-05 23:20:49
Humidity Sensor,Garage,76.16,2022-12-21 16:58:48
Temperature Sensor,Garden,-6.66,2022-09-03 08:32:56
Light Sensor,Garden,57.69,2023-07-10 05:31:59
<end>Convert this CSV to PLAIN TEXT:
Company,Sector,Stock Price,Annual Revenue (B)
FinanceWorks,Finance,133.83,50.55
Foodies,Healthcare,17.84,94.29
TechCorp,Healthcare,658.7,337.55
AeroSpace,Finance,843.67,210.99
TechCorp,Finance,711.19,257.38
TechCorp,Energy,243.87,458.35
<start>
Company: FinanceWorks | Sector: Finance | Stock Price: 133.83 | Annual Revenue (B): 50.55
Company: Foodies | Sector: Healthcare | Stock Price: 17.84 | Annual Revenue (B): 94.29
Company: TechCorp | Sector: Healthcare | Stock Price: 658.7 | Annual Revenue (B): 337.55
Company: AeroSpace | Sector: Finance | Stock Price: 843.67 | Annual Revenue (B): 210.99
Company: TechCorp | Sector: Finance | Stock Price: 711.19 | Annual Revenue (B): 257.38
Company: TechCorp | Sector: Energy | Stock Price: 243.87 | Annual Revenue (B): 458.35
<end>Please transform the following Markdown data into JSON:
| Company | Date | Open Price | Close Price | High Price | Low Price |
| --- | --- | --- | --- | --- | --- |
| HealthGen | 2019-10-08 | 267.78 | 1291.84 | 1291.84 | 267.78 |
| AutoMotive | 2010-07-11 | 1095.16 | 934.94 | 1095.16 | 934.94 |
| TechnoCorp | 2019-12-05 | 173.07 | 462.0 | 1265.25 | 173.07 |
| AeroSystems | 2020-09-23 | 462.0 | 1168.57 | 1168.57 | 249.5 |
| RetailWorld | 2012-03-12 | 599.33 | 618.11 | 656.23 | 175.59 |
| GreenEnergy | 2011-03-16 | 525.69 | 1444.14 | 1444.14 | 311.2 |
| FoodChain | 2020-12-12 | 884.23 | 88.73 | 884.23 | 88.73 |
| FoodChain | 2023-05-06 | 299.42 | 52.95 | 299.42 | 52.95 |
| AeroSystems | 2020-12-10 | 1194.12 | 40.12 | 1194.12 | 40.12 |<start>
[
    {
        "Company": "HealthGen",
        "Date": "2019-10-08",
        "Open Price": 267.78,
        "Close Price": 1291.84,
        "High Price": 1291.84,
        "Low Price": 267.78
    },
    {
        "Company": "AutoMotive",
        "Date": "2010-07-11",
        "Open Price": 1095.16,
        "Close Price": 934.94,
        "High Price": 1095.16,
        "Low Price": 934.94
    },
    {
        "Company": "TechnoCorp",
        "Date": "2019-12-05",
        "Open Price": 173.07,
        "Close Price": 462.0,
        "High Price": 1265.25,
        "Low Price": 173.07
    },
    {
        "Company": "AeroSystems",
        "Date": "2020-09-23",
        "Open Price": 462.0,
        "Close Price": 1168.57,
        "High Price": 1168.57,
        "Low Price": 249.5
    },
    {
        "Company": "RetailWorld",
        "Date": "2012-03-12",
        "Open Price": 599.33,
        "Close Price": 618.11,
        "High Price": 656.23,
        "Low Price": 175.59
    },
    {
        "Company": "GreenEnergy",
        "Date": "2011-03-16",
        "Open Price": 525.69,
        "Close Price": 1444.14,
        "High Price": 1444.14,
        "Low Price": 311.2
    },
    {
        "Company": "FoodChain",
        "Date": "2020-12-12",
        "Open Price": 884.23,
        "Close Price": 88.73,
        "High Price": 884.23,
        "Low Price": 88.73
    },
    {
        "Company": "FoodChain",
        "Date": "2023-05-06",
        "Open Price": 299.42,
        "Close Price": 52.95,
        "High Price": 299.42,
        "Low Price": 52.95
    },
    {
        "Company": "AeroSystems",
        "Date": "2020-12-10",
        "Open Price": 1194.12,
        "Close Price": 40.12,
        "High Price": 1194.12,
        "Low Price": 40.12
    }
]
<end>Transform this Markdown structure to a YAML format:
| Name | Age | Birth Month | City | Income |
| --- | --- | --- | --- | --- |
| Shelly | 38 | December | El Paso | 55000 |
| Ivan | 20 | March | New York | 55000 |
| Joy | 34 | August | Los Angeles | 120000 |
| Cecil | 26 | July | Dallas | 155000 |
| Perry | 39 | September | Memphis | 235000 |
| Blake | 63 | February | Washington | 490000 |
| Nettie | 68 | December | Detroit | 440000 |
| Levi | 18 | September | El Paso | 340000 |<start>
- Age: 38
  Birth Month: December
  City: El Paso
  Income: 55000
  Name: Shelly
- Age: 20
  Birth Month: March
  City: New York
  Income: 55000
  Name: Ivan
- Age: 34
  Birth Month: August
  City: Los Angeles
  Income: 120000
  Name: Joy
- Age: 26
  Birth Month: July
  City: Dallas
  Income: 155000
  Name: Cecil
- Age: 39
  Birth Month: September
  City: Memphis
  Income: 235000
  Name: Perry
- Age: 63
  Birth Month: February
  City: Washington
  Income: 490000
  Name: Blake
- Age: 68
  Birth Month: December
  City: Detroit
  Income: 440000
  Name: Nettie
- Age: 18
  Birth Month: September
  City: El Paso
  Income: 340000
  Name: Levi
<end>Please transform the following MARKDOWN data into json:
| Author | Genre | Rating |
| --- | --- | --- |
| Kara Firebrand | Fantasy | 4.8 |
| Thorne Ironwood | Science Fiction | 4.4 |
| Kara Firebrand | Thriller | 1.6 |
| Draven Blackthorn | Mystery | 2.6 |
| Thorne Ironwood | Mystery | 3.5 |<start>
[
    {
        "Author": "Kara Firebrand",
        "Genre": "Fantasy",
        "Rating": 4.8
    },
    {
        "Author": "Thorne Ironwood",
        "Genre": "Science Fiction",
        "Rating": 4.4
    },
    {
        "Author": "Kara Firebrand",
        "Genre": "Thriller",
        "Rating": 1.6
    },
    {
        "Author": "Draven Blackthorn",
        "Genre": "Mystery",
        "Rating": 2.6
    },
    {
        "Author": "Thorne Ironwood",
        "Genre": "Mystery",
        "Rating": 3.5
    }
]
<end>Convert this markdown to CSV:
| Genre | Publication Year | Rating |
| --- | --- | --- |
| Non-Fiction | 2001 | 1.2 |
| Horror | 1975 | 1.8 |
| Science Fiction | 2011 | 1.9 |
| Romance | 1997 | 4.1 |<start>
Genre,Publication Year,Rating
Non-Fiction,2001,1.2
Horror,1975,1.8
Science Fiction,2011,1.9
Romance,1997,4.1
<end>Transform this json structure to a Csv format:
[
    {
        "Genre": "Romance",
        "Rating": 3.0
    },
    {
        "Genre": "Romance",
        "Rating": 2.4
    },
    {
        "Genre": "Thriller",
        "Rating": 4.1
    },
    {
        "Genre": "Romance",
        "Rating": 3.3
    },
    {
        "Genre": "Fantasy",
        "Rating": 4.1
    },
    {
        "Genre": "Mystery",
        "Rating": 2.8
    }
]<start>
Genre,Rating
Romance,3.0
Romance,2.4
Thriller,4.1
Romance,3.3
Fantasy,4.1
Mystery,2.8
<end>Here's some csv data, can you convert it to JSON?
Location,Condition,Day
Los Angeles,Stormy,Monday
Chicago,Foggy,Saturday
New York,Sunny,Tuesday
Seattle,Cloudy,Sunday
<start>
[
    {
        "Location": "Los Angeles",
        "Condition": "Stormy",
        "Day": "Monday"
    },
    {
        "Location": "Chicago",
        "Condition": "Foggy",
        "Day": "Saturday"
    },
    {
        "Location": "New York",
        "Condition": "Sunny",
        "Day": "Tuesday"
    },
    {
        "Location": "Seattle",
        "Condition": "Cloudy",
        "Day": "Sunday"
    }
]
<end>Please transform the following JSON data into PLAIN TEXT:
[
    {
        "Author": "Kara Firebrand",
        "Genre": "Mystery",
        "Publication Year": 2014,
        "Rating": 1.2
    },
    {
        "Author": "Thorne Ironwood",
        "Genre": "Romance",
        "Publication Year": 1981,
        "Rating": 2.7
    },
    {
        "Author": "Kara Firebrand",
        "Genre": "Thriller",
        "Publication Year": 1979,
        "Rating": 2.2
    },
    {
        "Author": "Galen Starfire",
        "Genre": "Non-Fiction",
        "Publication Year": 1997,
        "Rating": 4.4
    },
    {
        "Author": "Thorne Ironwood",
        "Genre": "Horror",
        "Publication Year": 1990,
        "Rating": 1.4
    },
    {
        "Author": "Sylvia Nightshade",
        "Genre": "Mystery",
        "Publication Year": 1977,
        "Rating": 4.5
    },
    {
        "Author": "Luna Silverleaf",
        "Genre": "Non-Fiction",
        "Publication Year": 2000,
        "Rating": 1.9
    },
    {
        "Author": "Luna Silverleaf",
        "Genre": "Romance",
        "Publication Year": 1958,
        "Rating": 2.3
    }
]<start>
Author: Kara Firebrand | Genre: Mystery | Publication Year: 2014 | Rating: 1.2
Author: Thorne Ironwood | Genre: Romance | Publication Year: 1981 | Rating: 2.7
Author: Kara Firebrand | Genre: Thriller | Publication Year: 1979 | Rating: 2.2
Author: Galen Starfire | Genre: Non-Fiction | Publication Year: 1997 | Rating: 4.4
Author: Thorne Ironwood | Genre: Horror | Publication Year: 1990 | Rating: 1.4
Author: Sylvia Nightshade | Genre: Mystery | Publication Year: 1977 | Rating: 4.5
Author: Luna Silverleaf | Genre: Non-Fiction | Publication Year: 2000 | Rating: 1.9
Author: Luna Silverleaf | Genre: Romance | Publication Year: 1958 | Rating: 2.3
<end>Can you change this CSV into markdown?
Product Name,SKU,Price,Stock Quantity,Supplier Name
Apparatus,SKU-1087,310.66,403,Globex
Thingamajig,SKU-1058,328.68,294,Umbrella Corp
Instrument,SKU-1028,488.37,438,Wonka Industries
Instrument,SKU-1005,11.11,455,Wonka Industries
<start>
| Product Name | SKU | Price | Stock Quantity | Supplier Name |
| --- | --- | --- | --- | --- |
| Apparatus | SKU-1087 | 310.66 | 403 | Globex |
| Thingamajig | SKU-1058 | 328.68 | 294 | Umbrella Corp |
| Instrument | SKU-1028 | 488.37 | 438 | Wonka Industries |
| Instrument | SKU-1005 | 11.11 | 455 | Wonka Industries |
<end>Can you change this JSON into MARKDOWN?
[
    {
        "Company": "TechCorp",
        "Sector": "Aerospace",
        "Market Cap": "Mid Cap",
        "Stock Price": 790.86,
        "Annual Revenue (B)": 441.16,
        "Quarter": "Q3"
    },
    {
        "Company": "FinanceWorks",
        "Sector": "Biotech",
        "Market Cap": "Large Cap",
        "Stock Price": 298.24,
        "Annual Revenue (B)": 482.92,
        "Quarter": "Q4"
    },
    {
        "Company": "Foodies",
        "Sector": "Energy",
        "Market Cap": "Large Cap",
        "Stock Price": 747.54,
        "Annual Revenue (B)": 302.78,
        "Quarter": "Q3"
    },
    {
        "Company": "HealthPlus",
        "Sector": "Automotive",
        "Market Cap": "Large Cap",
        "Stock Price": 986.97,
        "Annual Revenue (B)": 98.69,
        "Quarter": "Q1"
    }
]<start>
| Company | Sector | Market Cap | Stock Price | Annual Revenue (B) | Quarter |
| --- | --- | --- | --- | --- | --- |
| TechCorp | Aerospace | Mid Cap | 790.86 | 441.16 | Q3 |
| FinanceWorks | Biotech | Large Cap | 298.24 | 482.92 | Q4 |
| Foodies | Energy | Large Cap | 747.54 | 302.78 | Q3 |
| HealthPlus | Automotive | Large Cap | 986.97 | 98.69 | Q1 |
<end>Please transform the following csv data into markdown:
Restaurant Name,Location,Rating,Price Range
Sushi World,Phoenix,4,$$
Taco Town,Miami,3,$$$
Burger Haven,New York,5,$$
Sushi World,Phoenix,5,$$$
Curry Corner,New York,2,$
Pasta Palace,Miami,5,$$
Sushi World,Phoenix,5,$$$$
Curry Corner,Houston,3,$$$$
<start>
| Restaurant Name | Location | Rating | Price Range |
| --- | --- | --- | --- |
| Sushi World | Phoenix | 4 | $$ |
| Taco Town | Miami | 3 | $$$ |
| Burger Haven | New York | 5 | $$ |
| Sushi World | Phoenix | 5 | $$$ |
| Curry Corner | New York | 2 | $ |
| Pasta Palace | Miami | 5 | $$ |
| Sushi World | Phoenix | 5 | $$$$ |
| Curry Corner | Houston | 3 | $$$$ |
<end>Transform this yaml structure to a markdown format:
- Condition: Rainy
  Humidity (%): 84
  Temperature (C): 24.0
  Wind Speed (km/h): 26.7
- Condition: Windy
  Humidity (%): 42
  Temperature (C): -0.4
  Wind Speed (km/h): 19.7
- Condition: Stormy
  Humidity (%): 99
  Temperature (C): 1.5
  Wind Speed (km/h): 12.0
- Condition: Snowy
  Humidity (%): 51
  Temperature (C): 24.5
  Wind Speed (km/h): 21.2
- Condition: Stormy
  Humidity (%): 49
  Temperature (C): -3.3
  Wind Speed (km/h): 28.5
- Condition: Sunny
  Humidity (%): 87
  Temperature (C): -3.6
  Wind Speed (km/h): 1.7
- Condition: Cloudy
  Humidity (%): 38
  Temperature (C): 39.0
  Wind Speed (km/h): 6.2
- Condition: Stormy
  Humidity (%): 81
  Temperature (C): 15.7
  Wind Speed (km/h): 15.4
- Condition: Rainy
  Humidity (%): 28
  Temperature (C): 37.8
  Wind Speed (km/h): 28.0
<start>
| Condition | Temperature (C) | Humidity (%) | Wind Speed (km/h) |
| --- | --- | --- | --- |
| Rainy | 24.0 | 84 | 26.7 |
| Windy | -0.4 | 42 | 19.7 |
| Stormy | 1.5 | 99 | 12.0 |
| Snowy | 24.5 | 51 | 21.2 |
| Stormy | -3.3 | 49 | 28.5 |
| Sunny | -3.6 | 87 | 1.7 |
| Cloudy | 39.0 | 38 | 6.2 |
| Stormy | 15.7 | 81 | 15.4 |
| Rainy | 37.8 | 28 | 28.0 |
<end>Can you change this Json into yaml?
[
    {
        "Age": 19,
        "City": "Nashville"
    },
    {
        "Age": 44,
        "City": "Indianapolis"
    },
    {
        "Age": 26,
        "City": "Charlotte"
    },
    {
        "Age": 58,
        "City": "Nashville"
    },
    {
        "Age": 56,
        "City": "Los Angeles"
    }
]<start>
- Age: 19
  City: Nashville
- Age: 44
  City: Indianapolis
- Age: 26
  City: Charlotte
- Age: 58
  City: Nashville
- Age: 56
  City: Los Angeles
<end>Here's some Json data, can you convert it to plain text?
[
    {
        "Company": "MediaGroup",
        "Date": "2022-02-03",
        "Open Price": 1397.76,
        "High Price": 1397.76,
        "Volume": 4755487
    },
    {
        "Company": "RetailWorld",
        "Date": "2021-12-28",
        "Open Price": 123.64,
        "High Price": 1257.68,
        "Volume": 8914344
    },
    {
        "Company": "AeroSystems",
        "Date": "2023-07-18",
        "Open Price": 1107.46,
        "High Price": 1257.68,
        "Volume": 1460889
    },
    {
        "Company": "AutoMotive",
        "Date": "2023-03-18",
        "Open Price": 1419.92,
        "High Price": 1419.92,
        "Volume": 6477821
    },
    {
        "Company": "FoodChain",
        "Date": "2019-06-04",
        "Open Price": 1340.1,
        "High Price": 1340.1,
        "Volume": 2830226
    },
    {
        "Company": "MediaGroup",
        "Date": "2016-06-02",
        "Open Price": 461.59,
        "High Price": 849.44,
        "Volume": 8589019
    }
]<start>
Company: MediaGroup | Date: 2022-02-03 | Open Price: 1397.76 | High Price: 1397.76 | Volume: 4755487
Company: RetailWorld | Date: 2021-12-28 | Open Price: 123.64 | High Price: 1257.68 | Volume: 8914344
Company: AeroSystems | Date: 2023-07-18 | Open Price: 1107.46 | High Price: 1257.68 | Volume: 1460889
Company: AutoMotive | Date: 2023-03-18 | Open Price: 1419.92 | High Price: 1419.92 | Volume: 6477821
Company: FoodChain | Date: 2019-06-04 | Open Price: 1340.1 | High Price: 1340.1 | Volume: 2830226
Company: MediaGroup | Date: 2016-06-02 | Open Price: 461.59 | High Price: 849.44 | Volume: 8589019
<end>Convert this Csv to plain text:
Company,Sector,Market Cap,Annual Revenue (B)
FinanceWorks,Retail,Mid Cap,428.11
BioPharm,Healthcare,Large Cap,264.12
AutoDrive,Energy,Mega Cap,130.24
AutoDrive,Automotive,Mid Cap,140.63
<start>
Company: FinanceWorks | Sector: Retail | Market Cap: Mid Cap | Annual Revenue (B): 428.11
Company: BioPharm | Sector: Healthcare | Market Cap: Large Cap | Annual Revenue (B): 264.12
Company: AutoDrive | Sector: Energy | Market Cap: Mega Cap | Annual Revenue (B): 130.24
Company: AutoDrive | Sector: Automotive | Market Cap: Mid Cap | Annual Revenue (B): 140.63
<end>Convert this JSON to plain text:
[
    {
        "Company": "BioLife",
        "Date": "2018-02-04",
        "Open Price": 129.08,
        "Close Price": 922.04,
        "High Price": 922.04,
        "Low Price": 129.08,
        "Volume": 9365925
    },
    {
        "Company": "MediaGroup",
        "Date": "2019-08-20",
        "Open Price": 521.45,
        "Close Price": 1400.69,
        "High Price": 1400.69,
        "Low Price": 90.67,
        "Volume": 1334987
    },
    {
        "Company": "FinanceTrust",
        "Date": "2015-01-13",
        "Open Price": 205.45,
        "Close Price": 399.91,
        "High Price": 1248.76,
        "Low Price": 205.45,
        "Volume": 3701583
    },
    {
        "Company": "FoodChain",
        "Date": "2015-01-02",
        "Open Price": 1428.64,
        "Close Price": 1414.8,
        "High Price": 1428.64,
        "Low Price": 509.18,
        "Volume": 9682313
    },
    {
        "Company": "AeroSystems",
        "Date": "2011-03-04",
        "Open Price": 346.37,
        "Close Price": 953.86,
        "High Price": 953.86,
        "Low Price": 62.19,
        "Volume": 9003264
    },
    {
        "Company": "TechnoCorp",
        "Date": "2020-10-18",
        "Open Price": 932.53,
        "Close Price": 244.07,
        "High Price": 1108.37,
        "Low Price": 244.07,
        "Volume": 2302521
    },
    {
        "Company": "BioLife",
        "Date": "2014-12-01",
        "Open Price": 191.94,
        "Close Price": 399.91,
        "High Price": 732.23,
        "Low Price": 191.94,
        "Volume": 6891241
    }
]<start>
Company: BioLife | Date: 2018-02-04 | Open Price: 129.08 | Close Price: 922.04 | High Price: 922.04 | Low Price: 129.08 | Volume: 9365925
Company: MediaGroup | Date: 2019-08-20 | Open Price: 521.45 | Close Price: 1400.69 | High Price: 1400.69 | Low Price: 90.67 | Volume: 1334987
Company: FinanceTrust | Date: 2015-01-13 | Open Price: 205.45 | Close Price: 399.91 | High Price: 1248.76 | Low Price: 205.45 | Volume: 3701583
Company: FoodChain | Date: 2015-01-02 | Open Price: 1428.64 | Close Price: 1414.8 | High Price: 1428.64 | Low Price: 509.18 | Volume: 9682313
Company: AeroSystems | Date: 2011-03-04 | Open Price: 346.37 | Close Price: 953.86 | High Price: 953.86 | Low Price: 62.19 | Volume: 9003264
Company: TechnoCorp | Date: 2020-10-18 | Open Price: 932.53 | Close Price: 244.07 | High Price: 1108.37 | Low Price: 244.07 | Volume: 2302521
Company: BioLife | Date: 2014-12-01 | Open Price: 191.94 | Close Price: 399.91 | High Price: 732.23 | Low Price: 191.94 | Volume: 6891241
<end>Please transform the following json data into Plain text:
[
    {
        "Restaurant Name": "Burger Haven",
        "Location": "Chicago",
        "Rating": 5,
        "Price Range": "$$$$$"
    },
    {
        "Restaurant Name": "Vegan Delight",
        "Location": "Seattle",
        "Rating": 2,
        "Price Range": "$$$$"
    },
    {
        "Restaurant Name": "Burger Haven",
        "Location": "Seattle",
        "Rating": 2,
        "Price Range": "$$$$$"
    },
    {
        "Restaurant Name": "Pasta Palace",
        "Location": "Phoenix",
        "Rating": 2,
        "Price Range": "$$$"
    },
    {
        "Restaurant Name": "BBQ Barn",
        "Location": "Phoenix",
        "Rating": 2,
        "Price Range": "$$$$$"
    }
]<start>
Restaurant Name: Burger Haven | Location: Chicago | Rating: 5 | Price Range: $$$$$
Restaurant Name: Vegan Delight | Location: Seattle | Rating: 2 | Price Range: $$$$
Restaurant Name: Burger Haven | Location: Seattle | Rating: 2 | Price Range: $$$$$
Restaurant Name: Pasta Palace | Location: Phoenix | Rating: 2 | Price Range: $$$
Restaurant Name: BBQ Barn | Location: Phoenix | Rating: 2 | Price Range: $$$$$
<end>Please transform the following CSV data into MARKDOWN:
Product Name,SKU,Stock Quantity,Category,Supplier Name
Thingamajig,SKU-1046,380,Household,Wayne Enterprises
Device,SKU-1029,446,Automotive,Umbrella Corp
Device,SKU-1046,440,Sports,Umbrella Corp
Gadget,SKU-1022,180,Automotive,Wonka Industries
Doohickey,SKU-1016,232,Household,ACME Corp
Gizmo,SKU-1048,290,Automotive,Umbrella Corp
Whatchamacallit,SKU-1086,389,Electronics,ACME Corp
Device,SKU-1075,49,Toys,Globex
Thingamajig,SKU-1026,452,Electronics,Wonka Industries
<start>
| Product Name | SKU | Stock Quantity | Category | Supplier Name |
| --- | --- | --- | --- | --- |
| Thingamajig | SKU-1046 | 380 | Household | Wayne Enterprises |
| Device | SKU-1029 | 446 | Automotive | Umbrella Corp |
| Device | SKU-1046 | 440 | Sports | Umbrella Corp |
| Gadget | SKU-1022 | 180 | Automotive | Wonka Industries |
| Doohickey | SKU-1016 | 232 | Household | ACME Corp |
| Gizmo | SKU-1048 | 290 | Automotive | Umbrella Corp |
| Whatchamacallit | SKU-1086 | 389 | Electronics | ACME Corp |
| Device | SKU-1075 | 49 | Toys | Globex |
| Thingamajig | SKU-1026 | 452 | Electronics | Wonka Industries |
<end>Here's some csv data, can you convert it to markdown?
Price,Stock Quantity,Category
448.29,476,Household
316.09,316,Household
145.94,53,Electronics
103.27,22,Automotive
51.38,343,Toys
38.86,90,Household
<start>
| Price | Stock Quantity | Category |
| --- | --- | --- |
| 448.29 | 476 | Household |
| 316.09 | 316 | Household |
| 145.94 | 53 | Electronics |
| 103.27 | 22 | Automotive |
| 51.38 | 343 | Toys |
| 38.86 | 90 | Household |
<end>Transform this Yaml structure to a MARKDOWN format:
- Age: 43
  Birth Month: December
  City: Austin
  Income: 140000
  Name: Sheena
- Age: 64
  Birth Month: October
  City: Louisville
  Income: 240000
  Name: Nichole
- Age: 52
  Birth Month: December
  City: Phoenix
  Income: 270000
  Name: Vera
- Age: 42
  Birth Month: August
  City: Boston
  Income: 145000
  Name: Isabella
- Age: 38
  Birth Month: July
  City: Charlotte
  Income: 295000
  Name: Kayla
- Age: 20
  Birth Month: February
  City: Nashville
  Income: 350000
  Name: Deanna
- Age: 57
  Birth Month: April
  City: Boston
  Income: 305000
  Name: Hadley
- Age: 23
  Birth Month: July
  City: Baltimore
  Income: 60000
  Name: Mindy
<start>
| Name | Age | Birth Month | City | Income |
| --- | --- | --- | --- | --- |
| Sheena | 43 | December | Austin | 140000 |
| Nichole | 64 | October | Louisville | 240000 |
| Vera | 52 | December | Phoenix | 270000 |
| Isabella | 42 | August | Boston | 145000 |
| Kayla | 38 | July | Charlotte | 295000 |
| Deanna | 20 | February | Nashville | 350000 |
| Hadley | 57 | April | Boston | 305000 |
| Mindy | 23 | July | Baltimore | 60000 |
<end>Can you change this plain text into yaml?
Title: Echoes of Eternity | Author: Draven Blackthorn | Rating: 2.7
Title: Tales of the Brave | Author: Rowan Ashborne | Rating: 2.3
Title: The Forgotten World | Author: Isla Windrider | Rating: 4.6
Title: Shadows of Solitude | Author: Thorne Ironwood | Rating: 3.7
Title: Echoes of Eternity | Author: Sylvia Nightshade | Rating: 1.6
Title: Legends of the Rift | Author: Orion Frostblade | Rating: 1.6
Title: Whispers of the Abyss | Author: Draven Blackthorn | Rating: 2.4
<start>
- Author: Draven Blackthorn
  Rating: 2.7
  Title: Echoes of Eternity
- Author: Rowan Ashborne
  Rating: 2.3
  Title: Tales of the Brave
- Author: Isla Windrider
  Rating: 4.6
  Title: The Forgotten World
- Author: Thorne Ironwood
  Rating: 3.7
  Title: Shadows of Solitude
- Author: Sylvia Nightshade
  Rating: 1.6
  Title: Echoes of Eternity
- Author: Orion Frostblade
  Rating: 1.6
  Title: Legends of the Rift
- Author: Draven Blackthorn
  Rating: 2.4
  Title: Whispers of the Abyss
<end>Transform this json structure to a markdown format:
[
    {
        "Device Type": "Motion Detector",
        "Location": "Hallway",
        "Battery Level (%)": 84.9,
        "Timestamp": "2023-12-16 13:53:51"
    },
    {
        "Device Type": "Temperature Sensor",
        "Location": "Living Room",
        "Battery Level (%)": 90.0,
        "Timestamp": "2022-09-20 16:46:47"
    },
    {
        "Device Type": "Humidity Sensor",
        "Location": "Hallway",
        "Battery Level (%)": 24.5,
        "Timestamp": "2023-09-14 08:01:29"
    },
    {
        "Device Type": "Pressure Sensor",
        "Location": "Kitchen",
        "Battery Level (%)": 15.8,
        "Timestamp": "2021-09-04 15:32:41"
    },
    {
        "Device Type": "Temperature Sensor",
        "Location": "Garden",
        "Battery Level (%)": 16.0,
        "Timestamp": "2022-10-09 03:10:20"
    },
    {
        "Device Type": "Light Sensor",
        "Location": "Kitchen",
        "Battery Level (%)": 65.3,
        "Timestamp": "2023-09-19 22:26:16"
    },
    {
        "Device Type": "Humidity Sensor",
        "Location": "Office",
        "Battery Level (%)": 58.1,
        "Timestamp": "2021-02-26 06:27:10"
    },
    {
        "Device Type": "Temperature Sensor",
        "Location": "Garage",
        "Battery Level (%)": 42.8,
        "Timestamp": "2023-11-04 03:59:05"
    }
]<start>
| Device Type | Location | Battery Level (%) | Timestamp |
| --- | --- | --- | --- |
| Motion Detector | Hallway | 84.9 | 2023-12-16 13:53:51 |
| Temperature Sensor | Living Room | 90.0 | 2022-09-20 16:46:47 |
| Humidity Sensor | Hallway | 24.5 | 2023-09-14 08:01:29 |
| Pressure Sensor | Kitchen | 15.8 | 2021-09-04 15:32:41 |
| Temperature Sensor | Garden | 16.0 | 2022-10-09 03:10:20 |
| Light Sensor | Kitchen | 65.3 | 2023-09-19 22:26:16 |
| Humidity Sensor | Office | 58.1 | 2021-02-26 06:27:10 |
| Temperature Sensor | Garage | 42.8 | 2023-11-04 03:59:05 |
<end>Please transform the following csv data into PLAIN TEXT:
Market Cap,Annual Revenue (B),Quarter
Mega Cap,456.77,Q3
Mid Cap,470.81,Q3
Mega Cap,149.83,Q3
Mega Cap,230.62,Q4
Mega Cap,460.01,Q4
Mega Cap,149.83,Q3
<start>
Market Cap: Mega Cap | Annual Revenue (B): 456.77 | Quarter: Q3
Market Cap: Mid Cap | Annual Revenue (B): 470.81 | Quarter: Q3
Market Cap: Mega Cap | Annual Revenue (B): 149.83 | Quarter: Q3
Market Cap: Mega Cap | Annual Revenue (B): 230.62 | Quarter: Q4
Market Cap: Mega Cap | Annual Revenue (B): 460.01 | Quarter: Q4
Market Cap: Mega Cap | Annual Revenue (B): 149.83 | Quarter: Q3
<end>Please transform the following Yaml data into json:
- Age: 45
  City: San Francisco
  Income: 465000
- Age: 36
  City: Charlotte
  Income: 50000
- Age: 55
  City: Memphis
  Income: 105000
- Age: 66
  City: San Antonio
  Income: 340000
- Age: 68
  City: Houston
  Income: 265000
- Age: 25
  City: Dallas
  Income: 385000
<start>
[
    {
        "Age": 45,
        "City": "San Francisco",
        "Income": 465000
    },
    {
        "Age": 36,
        "City": "Charlotte",
        "Income": 50000
    },
    {
        "Age": 55,
        "City": "Memphis",
        "Income": 105000
    },
    {
        "Age": 66,
        "City": "San Antonio",
        "Income": 340000
    },
    {
        "Age": 68,
        "City": "Houston",
        "Income": 265000
    },
    {
        "Age": 25,
        "City": "Dallas",
        "Income": 385000
    }
]
<end>Please transform the following JSON data into Plain text:
[
    {
        "Location": "Denver",
        "Condition": "Sunny",
        "Temperature (C)": 9.0,
        "Humidity (%)": 42,
        "Wind Speed (km/h)": 5.0,
        "Day": "Sunday"
    },
    {
        "Location": "Seattle",
        "Condition": "Windy",
        "Temperature (C)": 29.6,
        "Humidity (%)": 99,
        "Wind Speed (km/h)": 17.7,
        "Day": "Saturday"
    },
    {
        "Location": "Los Angeles",
        "Condition": "Windy",
        "Temperature (C)": 35.6,
        "Humidity (%)": 47,
        "Wind Speed (km/h)": 2.1,
        "Day": "Friday"
    },
    {
        "Location": "New York",
        "Condition": "Windy",
        "Temperature (C)": 17.0,
        "Humidity (%)": 91,
        "Wind Speed (km/h)": 21.5,
        "Day": "Saturday"
    },
    {
        "Location": "Seattle",
        "Condition": "Cloudy",
        "Temperature (C)": 18.7,
        "Humidity (%)": 100,
        "Wind Speed (km/h)": 19.1,
        "Day": "Saturday"
    }
]<start>
Location: Denver | Condition: Sunny | Temperature (C): 9.0 | Humidity (%): 42 | Wind Speed (km/h): 5.0 | Day: Sunday
Location: Seattle | Condition: Windy | Temperature (C): 29.6 | Humidity (%): 99 | Wind Speed (km/h): 17.7 | Day: Saturday
Location: Los Angeles | Condition: Windy | Temperature (C): 35.6 | Humidity (%): 47 | Wind Speed (km/h): 2.1 | Day: Friday
Location: New York | Condition: Windy | Temperature (C): 17.0 | Humidity (%): 91 | Wind Speed (km/h): 21.5 | Day: Saturday
Location: Seattle | Condition: Cloudy | Temperature (C): 18.7 | Humidity (%): 100 | Wind Speed (km/h): 19.1 | Day: Saturday
<end>Can you change this CSV into JSON?
Company,Date,Open Price,Close Price,High Price,Low Price,Volume
TechnoCorp,2010-03-20,1113.53,671.28,1113.53,671.28,5821384
AeroSystems,2015-03-19,1239.93,959.62,1239.93,959.62,1288414
GreenEnergy,2018-08-11,215.53,634.11,634.11,215.53,9491678
AeroSystems,2016-12-23,1368.67,446.49,1368.67,446.49,5821384
BioLife,2016-02-25,685.92,802.32,802.32,685.92,1562364
FinanceTrust,2012-08-03,274.41,1495.87,1495.87,274.41,8439772
TechnoCorp,2017-09-09,1152.52,881.22,1152.52,591.07,2052501
BioLife,2022-12-28,1093.62,1276.72,1276.72,492.37,598657
HealthGen,2015-06-22,745.18,1439.34,1439.34,745.18,1392184
<start>
[
    {
        "Company": "TechnoCorp",
        "Date": "2010-03-20",
        "Open Price": 1113.53,
        "Close Price": 671.28,
        "High Price": 1113.53,
        "Low Price": 671.28,
        "Volume": 5821384
    },
    {
        "Company": "AeroSystems",
        "Date": "2015-03-19",
        "Open Price": 1239.93,
        "Close Price": 959.62,
        "High Price": 1239.93,
        "Low Price": 959.62,
        "Volume": 1288414
    },
    {
        "Company": "GreenEnergy",
        "Date": "2018-08-11",
        "Open Price": 215.53,
        "Close Price": 634.11,
        "High Price": 634.11,
        "Low Price": 215.53,
        "Volume": 9491678
    },
    {
        "Company": "AeroSystems",
        "Date": "2016-12-23",
        "Open Price": 1368.67,
        "Close Price": 446.49,
        "High Price": 1368.67,
        "Low Price": 446.49,
        "Volume": 5821384
    },
    {
        "Company": "BioLife",
        "Date": "2016-02-25",
        "Open Price": 685.92,
        "Close Price": 802.32,
        "High Price": 802.32,
        "Low Price": 685.92,
        "Volume": 1562364
    },
    {
        "Company": "FinanceTrust",
        "Date": "2012-08-03",
        "Open Price": 274.41,
        "Close Price": 1495.87,
        "High Price": 1495.87,
        "Low Price": 274.41,
        "Volume": 8439772
    },
    {
        "Company": "TechnoCorp",
        "Date": "2017-09-09",
        "Open Price": 1152.52,
        "Close Price": 881.22,
        "High Price": 1152.52,
        "Low Price": 591.07,
        "Volume": 2052501
    },
    {
        "Company": "BioLife",
        "Date": "2022-12-28",
        "Open Price": 1093.62,
        "Close Price": 1276.72,
        "High Price": 1276.72,
        "Low Price": 492.37,
        "Volume": 598657
    },
    {
        "Company": "HealthGen",
        "Date": "2015-06-22",
        "Open Price": 745.18,
        "Close Price": 1439.34,
        "High Price": 1439.34,
        "Low Price": 745.18,
        "Volume": 1392184
    }
]
<end>Convert this json to Plain text:
[
    {
        "Location": "Bathroom",
        "Battery Level (%)": 20.6,
        "Reading Value": 29.7,
        "Timestamp": "2021-04-13 23:49:48"
    },
    {
        "Location": "Office",
        "Battery Level (%)": 12.8,
        "Reading Value": -9.08,
        "Timestamp": "2022-02-25 19:22:41"
    },
    {
        "Location": "Hallway",
        "Battery Level (%)": 48.3,
        "Reading Value": 30.94,
        "Timestamp": "2021-05-02 05:05:05"
    }
]<start>
Location: Bathroom | Battery Level (%): 20.6 | Reading Value: 29.7 | Timestamp: 2021-04-13 23:49:48
Location: Office | Battery Level (%): 12.8 | Reading Value: -9.08 | Timestamp: 2022-02-25 19:22:41
Location: Hallway | Battery Level (%): 48.3 | Reading Value: 30.94 | Timestamp: 2021-05-02 05:05:05
<end>Transform this json structure to a markdown format:
[
    {
        "Trip Name": "Desert Drive",
        "Start Location": "Chicago",
        "End Location": "Los Angeles",
        "Distance (miles)": 1326.4,
        "Duration (hours)": 61.2,
        "Fuel Used (gallons)": 57.7
    },
    {
        "Trip Name": "Highway Odyssey",
        "Start Location": "Chicago",
        "End Location": "Phoenix",
        "Distance (miles)": 1250.8,
        "Duration (hours)": 14.3,
        "Fuel Used (gallons)": 10.0
    },
    {
        "Trip Name": "Lakeside Retreat",
        "Start Location": "Los Angeles",
        "End Location": "Denver",
        "Distance (miles)": 308.0,
        "Duration (hours)": 62.8,
        "Fuel Used (gallons)": 97.9
    },
    {
        "Trip Name": "Coast to Coast",
        "Start Location": "San Francisco",
        "End Location": "Phoenix",
        "Distance (miles)": 1600.6,
        "Duration (hours)": 68.9,
        "Fuel Used (gallons)": 16.7
    },
    {
        "Trip Name": "Historic Route",
        "Start Location": "Houston",
        "End Location": "Los Angeles",
        "Distance (miles)": 120.3,
        "Duration (hours)": 11.7,
        "Fuel Used (gallons)": 43.4
    },
    {
        "Trip Name": "Valley Voyage",
        "Start Location": "Denver",
        "End Location": "San Francisco",
        "Distance (miles)": 1346.1,
        "Duration (hours)": 50.4,
        "Fuel Used (gallons)": 50.2
    },
    {
        "Trip Name": "Highway Odyssey",
        "Start Location": "San Francisco",
        "End Location": "Denver",
        "Distance (miles)": 1857.5,
        "Duration (hours)": 50.4,
        "Fuel Used (gallons)": 50.2
    },
    {
        "Trip Name": "Coast to Coast",
        "Start Location": "Phoenix",
        "End Location": "Denver",
        "Distance (miles)": 1242.0,
        "Duration (hours)": 62.8,
        "Fuel Used (gallons)": 33.8
    },
    {
        "Trip Name": "Valley Voyage",
        "Start Location": "Phoenix",
        "End Location": "Los Angeles",
        "Distance (miles)": 1242.0,
        "Duration (hours)": 54.8,
        "Fuel Used (gallons)": 50.8
    }
]<start>
| Trip Name | Start Location | End Location | Distance (miles) | Duration (hours) | Fuel Used (gallons) |
| --- | --- | --- | --- | --- | --- |
| Desert Drive | Chicago | Los Angeles | 1326.4 | 61.2 | 57.7 |
| Highway Odyssey | Chicago | Phoenix | 1250.8 | 14.3 | 10.0 |
| Lakeside Retreat | Los Angeles | Denver | 308.0 | 62.8 | 97.9 |
| Coast to Coast | San Francisco | Phoenix | 1600.6 | 68.9 | 16.7 |
| Historic Route | Houston | Los Angeles | 120.3 | 11.7 | 43.4 |
| Valley Voyage | Denver | San Francisco | 1346.1 | 50.4 | 50.2 |
| Highway Odyssey | San Francisco | Denver | 1857.5 | 50.4 | 50.2 |
| Coast to Coast | Phoenix | Denver | 1242.0 | 62.8 | 33.8 |
| Valley Voyage | Phoenix | Los Angeles | 1242.0 | 54.8 | 50.8 |
<end>Convert this MARKDOWN to Plain text:
| Temperature (C) | Wind Speed (km/h) | Day |
| --- | --- | --- |
| 24.8 | 20.0 | Saturday |
| 33.6 | 14.2 | Tuesday |
| -8.7 | 18.6 | Sunday |
| 25.3 | 28.6 | Monday |
| 6.1 | 4.6 | Sunday |
| -9.5 | 3.3 | Thursday |
| 39.7 | 20.2 | Wednesday |
| 8.7 | 28.6 | Tuesday |
| 28.5 | 17.1 | Sunday |<start>
Temperature (C): 24.8 | Wind Speed (km/h): 20.0 | Day: Saturday
Temperature (C): 33.6 | Wind Speed (km/h): 14.2 | Day: Tuesday
Temperature (C): -8.7 | Wind Speed (km/h): 18.6 | Day: Sunday
Temperature (C): 25.3 | Wind Speed (km/h): 28.6 | Day: Monday
Temperature (C): 6.1 | Wind Speed (km/h): 4.6 | Day: Sunday
Temperature (C): -9.5 | Wind Speed (km/h): 3.3 | Day: Thursday
Temperature (C): 39.7 | Wind Speed (km/h): 20.2 | Day: Wednesday
Temperature (C): 8.7 | Wind Speed (km/h): 28.6 | Day: Tuesday
Temperature (C): 28.5 | Wind Speed (km/h): 17.1 | Day: Sunday
<end>Can you change this yml into csv?
- Age: 27
  Birth Month: December
  City: El Paso
  Income: 45000
  Name: Sammy
- Age: 66
  Birth Month: December
  City: San Jose
  Income: 455000
  Name: Hazel
- Age: 35
  Birth Month: December
  City: Oklahoma City
  Income: 310000
  Name: Adrianna
- Age: 53
  Birth Month: June
  City: Washington
  Income: 355000
  Name: Nicholas
- Age: 65
  Birth Month: December
  City: Nashville
  Income: 40000
  Name: Blanche
<start>
Name,Age,Birth Month,City,Income
Sammy,27,December,El Paso,45000
Hazel,66,December,San Jose,455000
Adrianna,35,December,Oklahoma City,310000
Nicholas,53,June,Washington,355000
Blanche,65,December,Nashville,40000
<end>Transform this yml structure to a Plain text format:
- Birth Month: May
  Name: Birdie
- Birth Month: May
  Name: Kara
- Birth Month: October
  Name: Leslie
<start>
Name: Birdie | Birth Month: May
Name: Kara | Birth Month: May
Name: Leslie | Birth Month: October
<end>Here's some PLAIN TEXT data, can you convert it to yaml?
Company: AutoDrive | Sector: Technology | Market Cap: Mid Cap | Stock Price: 839.14 | Annual Revenue (B): 483.9 | Quarter: Q1
Company: RetailHub | Sector: Technology | Market Cap: Small Cap | Stock Price: 724.47 | Annual Revenue (B): 196.34 | Quarter: Q3
Company: RetailHub | Sector: Retail | Market Cap: Small Cap | Stock Price: 690.43 | Annual Revenue (B): 67.35 | Quarter: Q2
Company: RetailHub | Sector: Energy | Market Cap: Large Cap | Stock Price: 720.39 | Annual Revenue (B): 257.0 | Quarter: Q4
Company: GlobalTrade | Sector: Finance | Market Cap: Large Cap | Stock Price: 690.43 | Annual Revenue (B): 439.98 | Quarter: Q3
<start>
- Annual Revenue (B): 483.9
  Company: AutoDrive
  Market Cap: Mid Cap
  Quarter: Q1
  Sector: Technology
  Stock Price: 839.14
- Annual Revenue (B): 196.34
  Company: RetailHub
  Market Cap: Small Cap
  Quarter: Q3
  Sector: Technology
  Stock Price: 724.47
- Annual Revenue (B): 67.35
  Company: RetailHub
  Market Cap: Small Cap
  Quarter: Q2
  Sector: Retail
  Stock Price: 690.43
- Annual Revenue (B): 257.0
  Company: RetailHub
  Market Cap: Large Cap
  Quarter: Q4
  Sector: Energy
  Stock Price: 720.39
- Annual Revenue (B): 439.98
  Company: GlobalTrade
  Market Cap: Large Cap
  Quarter: Q3
  Sector: Finance
  Stock Price: 690.43
<end>Convert this markdown to YML:
| Director | Box Office Earnings (M) |
| --- | --- |
| Lira Silverleaf | 547.88 |
| Orin Shadowalker | 881.9 |
| Aria Ravenwood | 273.41 |
| Cade Firebrand | 909.06 |
| Drake Nightshade | 361.61 |
| Aria Ravenwood | 384.92 |
| Orin Shadowalker | 186.87 |
| Drake Nightshade | 103.46 |<start>
- Box Office Earnings (M): 547.88
  Director: Lira Silverleaf
- Box Office Earnings (M): 881.9
  Director: Orin Shadowalker
- Box Office Earnings (M): 273.41
  Director: Aria Ravenwood
- Box Office Earnings (M): 909.06
  Director: Cade Firebrand
- Box Office Earnings (M): 361.61
  Director: Drake Nightshade
- Box Office Earnings (M): 384.92
  Director: Aria Ravenwood
- Box Office Earnings (M): 186.87
  Director: Orin Shadowalker
- Box Office Earnings (M): 103.46
  Director: Drake Nightshade
<end>Transform this yml structure to a csv format:
- Location: Phoenix
  Rating: 2
- Location: Los Angeles
  Rating: 3
- Location: New York
  Rating: 4
- Location: Phoenix
  Rating: 4
- Location: Los Angeles
  Rating: 5
- Location: Los Angeles
  Rating: 1
<start>
Location,Rating
Phoenix,2
Los Angeles,3
New York,4
Phoenix,4
Los Angeles,5
Los Angeles,1
<end>Can you change this yaml into JSON?
- Category: Sports
  Price: 447.7
  Product Name: Device
  SKU: SKU-1058
  Stock Quantity: 437
  Supplier Name: Wonka Industries
- Category: Automotive
  Price: 342.18
  Product Name: Thingamajig
  SKU: SKU-1010
  Stock Quantity: 254
  Supplier Name: Umbrella Corp
- Category: Electronics
  Price: 301.89
  Product Name: Instrument
  SKU: SKU-1032
  Stock Quantity: 423
  Supplier Name: Umbrella Corp
- Category: Household
  Price: 129.77
  Product Name: Apparatus
  SKU: SKU-1028
  Stock Quantity: 388
  Supplier Name: Wonka Industries
- Category: Sports
  Price: 369.49
  Product Name: Gizmo
  SKU: SKU-1052
  Stock Quantity: 320
  Supplier Name: ACME Corp
- Category: Toys
  Price: 113.19
  Product Name: Gadget
  SKU: SKU-1091
  Stock Quantity: 29
  Supplier Name: Wonka Industries
- Category: Electronics
  Price: 458.24
  Product Name: Doohickey
  SKU: SKU-1052
  Stock Quantity: 429
  Supplier Name: Wayne Enterprises
<start>
[
    {
        "Product Name": "Device",
        "SKU": "SKU-1058",
        "Price": 447.7,
        "Stock Quantity": 437,
        "Category": "Sports",
        "Supplier Name": "Wonka Industries"
    },
    {
        "Product Name": "Thingamajig",
        "SKU": "SKU-1010",
        "Price": 342.18,
        "Stock Quantity": 254,
        "Category": "Automotive",
        "Supplier Name": "Umbrella Corp"
    },
    {
        "Product Name": "Instrument",
        "SKU": "SKU-1032",
        "Price": 301.89,
        "Stock Quantity": 423,
        "Category": "Electronics",
        "Supplier Name": "Umbrella Corp"
    },
    {
        "Product Name": "Apparatus",
        "SKU": "SKU-1028",
        "Price": 129.77,
        "Stock Quantity": 388,
        "Category": "Household",
        "Supplier Name": "Wonka Industries"
    },
    {
        "Product Name": "Gizmo",
        "SKU": "SKU-1052",
        "Price": 369.49,
        "Stock Quantity": 320,
        "Category": "Sports",
        "Supplier Name": "ACME Corp"
    },
    {
        "Product Name": "Gadget",
        "SKU": "SKU-1091",
        "Price": 113.19,
        "Stock Quantity": 29,
        "Category": "Toys",
        "Supplier Name": "Wonka Industries"
    },
    {
        "Product Name": "Doohickey",
        "SKU": "SKU-1052",
        "Price": 458.24,
        "Stock Quantity": 429,
        "Category": "Electronics",
        "Supplier Name": "Wayne Enterprises"
    }
]
<end>Please transform the following JSON data into csv:
[
    {
        "Database Name": "ProfilesDB",
        "Queries per Second": 4066.86,
        "Average Latency (ms)": 52.4
    },
    {
        "Database Name": "UserDB",
        "Queries per Second": 929.2,
        "Average Latency (ms)": 98.73
    },
    {
        "Database Name": "UserDB",
        "Queries per Second": 3043.98,
        "Average Latency (ms)": 40.77
    },
    {
        "Database Name": "ProfilesDB",
        "Queries per Second": 208.65,
        "Average Latency (ms)": 14.29
    },
    {
        "Database Name": "InventoryDB",
        "Queries per Second": 371.36,
        "Average Latency (ms)": 40.77
    },
    {
        "Database Name": "LogsDB",
        "Queries per Second": 520.18,
        "Average Latency (ms)": 60.22
    },
    {
        "Database Name": "SessionsDB",
        "Queries per Second": 4013.6,
        "Average Latency (ms)": 31.99
    },
    {
        "Database Name": "SalesDB",
        "Queries per Second": 208.65,
        "Average Latency (ms)": 95.7
    },
    {
        "Database Name": "MetricsDB",
        "Queries per Second": 2260.49,
        "Average Latency (ms)": 38.0
    }
]<start>
Database Name,Queries per Second,Average Latency (ms)
ProfilesDB,4066.86,52.4
UserDB,929.2,98.73
UserDB,3043.98,40.77
ProfilesDB,208.65,14.29
InventoryDB,371.36,40.77
LogsDB,520.18,60.22
SessionsDB,4013.6,31.99
SalesDB,208.65,95.7
MetricsDB,2260.49,38.0
<end>Please transform the following plain text data into json:
Location: Chicago | Condition: Snowy | Temperature (C): 26.9 | Wind Speed (km/h): 12.8 | Day: Thursday
Location: New York | Condition: Cloudy | Temperature (C): 39.1 | Wind Speed (km/h): 11.3 | Day: Tuesday
Location: Los Angeles | Condition: Snowy | Temperature (C): 21.6 | Wind Speed (km/h): 13.4 | Day: Tuesday
Location: Chicago | Condition: Rainy | Temperature (C): 11.1 | Wind Speed (km/h): 24.9 | Day: Sunday
Location: Seattle | Condition: Stormy | Temperature (C): 12.1 | Wind Speed (km/h): 21.7 | Day: Wednesday
Location: Miami | Condition: Cloudy | Temperature (C): 23.3 | Wind Speed (km/h): 27.9 | Day: Saturday
Location: Denver | Condition: Cloudy | Temperature (C): 24.5 | Wind Speed (km/h): 17.8 | Day: Sunday
Location: Los Angeles | Condition: Snowy | Temperature (C): 8.6 | Wind Speed (km/h): 26.1 | Day: Tuesday
Location: Phoenix | Condition: Rainy | Temperature (C): 8.6 | Wind Speed (km/h): 15.0 | Day: Wednesday
Location: Denver | Condition: Foggy | Temperature (C): 17.4 | Wind Speed (km/h): 29.2 | Day: Thursday
<start>
[
    {
        "Location": "Chicago",
        "Condition": "Snowy",
        "Temperature (C)": 26.9,
        "Wind Speed (km/h)": 12.8,
        "Day": "Thursday"
    },
    {
        "Location": "New York",
        "Condition": "Cloudy",
        "Temperature (C)": 39.1,
        "Wind Speed (km/h)": 11.3,
        "Day": "Tuesday"
    },
    {
        "Location": "Los Angeles",
        "Condition": "Snowy",
        "Temperature (C)": 21.6,
        "Wind Speed (km/h)": 13.4,
        "Day": "Tuesday"
    },
    {
        "Location": "Chicago",
        "Condition": "Rainy",
        "Temperature (C)": 11.1,
        "Wind Speed (km/h)": 24.9,
        "Day": "Sunday"
    },
    {
        "Location": "Seattle",
        "Condition": "Stormy",
        "Temperature (C)": 12.1,
        "Wind Speed (km/h)": 21.7,
        "Day": "Wednesday"
    },
    {
        "Location": "Miami",
        "Condition": "Cloudy",
        "Temperature (C)": 23.3,
        "Wind Speed (km/h)": 27.9,
        "Day": "Saturday"
    },
    {
        "Location": "Denver",
        "Condition": "Cloudy",
        "Temperature (C)": 24.5,
        "Wind Speed (km/h)": 17.8,
        "Day": "Sunday"
    },
    {
        "Location": "Los Angeles",
        "Condition": "Snowy",
        "Temperature (C)": 8.6,
        "Wind Speed (km/h)": 26.1,
        "Day": "Tuesday"
    },
    {
        "Location": "Phoenix",
        "Condition": "Rainy",
        "Temperature (C)": 8.6,
        "Wind Speed (km/h)": 15.0,
        "Day": "Wednesday"
    },
    {
        "Location": "Denver",
        "Condition": "Foggy",
        "Temperature (C)": 17.4,
        "Wind Speed (km/h)": 29.2,
        "Day": "Thursday"
    }
]
<end>Here's some PLAIN TEXT data, can you convert it to Markdown?
Device ID: device-0067 | Device Type: Pressure Sensor | Location: Hallway | Reading Value: 9.46
Device ID: device-0017 | Device Type: Pressure Sensor | Location: Bedroom | Reading Value: 50.38
Device ID: device-0091 | Device Type: Motion Detector | Location: Office | Reading Value: -21.61
Device ID: device-0087 | Device Type: Light Sensor | Location: Living Room | Reading Value: 22.02
Device ID: device-0073 | Device Type: Motion Detector | Location: Kitchen | Reading Value: -1.01
Device ID: device-0083 | Device Type: Temperature Sensor | Location: Bedroom | Reading Value: -1.49
<start>
| Device ID | Device Type | Location | Reading Value |
| --- | --- | --- | --- |
| device-0067 | Pressure Sensor | Hallway | 9.46 |
| device-0017 | Pressure Sensor | Bedroom | 50.38 |
| device-0091 | Motion Detector | Office | -21.61 |
| device-0087 | Light Sensor | Living Room | 22.02 |
| device-0073 | Motion Detector | Kitchen | -1.01 |
| device-0083 | Temperature Sensor | Bedroom | -1.49 |
<end>Transform this MARKDOWN structure to a yaml format:
| Genre | Box Office Earnings (M) |
| --- | --- |
| Adventure | 780.6 |
| Comedy | 285.63 |
| Thriller | 781.9 |
| Sci-Fi | 687.58 |
| Action | 284.42 |<start>
- Box Office Earnings (M): 780.6
  Genre: Adventure
- Box Office Earnings (M): 285.63
  Genre: Comedy
- Box Office Earnings (M): 781.9
  Genre: Thriller
- Box Office Earnings (M): 687.58
  Genre: Sci-Fi
- Box Office Earnings (M): 284.42
  Genre: Action
<end>Convert this YML to JSON:
- Battery Level (%): 94.0
  Device ID: device-0037
  Device Type: Light Sensor
  Location: Garden
  Reading Value: 72.68
  Timestamp: '2022-06-16 13:00:19'
- Battery Level (%): 38.1
  Device ID: device-0065
  Device Type: Pressure Sensor
  Location: Garden
  Reading Value: 63.81
  Timestamp: '2022-02-21 04:13:41'
- Battery Level (%): 95.7
  Device ID: device-0085
  Device Type: Light Sensor
  Location: Garden
  Reading Value: -13.26
  Timestamp: '2021-01-17 16:32:54'
- Battery Level (%): 38.0
  Device ID: device-0087
  Device Type: Light Sensor
  Location: Garage
  Reading Value: -37.2
  Timestamp: '2023-10-09 10:53:51'
- Battery Level (%): 39.6
  Device ID: device-0009
  Device Type: Temperature Sensor
  Location: Office
  Reading Value: 51.82
  Timestamp: '2022-01-04 07:43:19'
- Battery Level (%): 13.2
  Device ID: device-0001
  Device Type: Light Sensor
  Location: Bedroom
  Reading Value: 42.31
  Timestamp: '2021-07-27 05:16:33'
- Battery Level (%): 15.9
  Device ID: device-0001
  Device Type: Pressure Sensor
  Location: Kitchen
  Reading Value: 51.82
  Timestamp: '2021-06-09 13:19:39'
<start>
[
    {
        "Device ID": "device-0037",
        "Device Type": "Light Sensor",
        "Location": "Garden",
        "Battery Level (%)": 94.0,
        "Reading Value": 72.68,
        "Timestamp": "2022-06-16 13:00:19"
    },
    {
        "Device ID": "device-0065",
        "Device Type": "Pressure Sensor",
        "Location": "Garden",
        "Battery Level (%)": 38.1,
        "Reading Value": 63.81,
        "Timestamp": "2022-02-21 04:13:41"
    },
    {
        "Device ID": "device-0085",
        "Device Type": "Light Sensor",
        "Location": "Garden",
        "Battery Level (%)": 95.7,
        "Reading Value": -13.26,
        "Timestamp": "2021-01-17 16:32:54"
    },
    {
        "Device ID": "device-0087",
        "Device Type": "Light Sensor",
        "Location": "Garage",
        "Battery Level (%)": 38.0,
        "Reading Value": -37.2,
        "Timestamp": "2023-10-09 10:53:51"
    },
    {
        "Device ID": "device-0009",
        "Device Type": "Temperature Sensor",
        "Location": "Office",
        "Battery Level (%)": 39.6,
        "Reading Value": 51.82,
        "Timestamp": "2022-01-04 07:43:19"
    },
    {
        "Device ID": "device-0001",
        "Device Type": "Light Sensor",
        "Location": "Bedroom",
        "Battery Level (%)": 13.2,
        "Reading Value": 42.31,
        "Timestamp": "2021-07-27 05:16:33"
    },
    {
        "Device ID": "device-0001",
        "Device Type": "Pressure Sensor",
        "Location": "Kitchen",
        "Battery Level (%)": 15.9,
        "Reading Value": 51.82,
        "Timestamp": "2021-06-09 13:19:39"
    }
]
<end>Here's some CSV data, can you convert it to json?
Device ID,Device Type,Location,Battery Level (%),Reading Value,Timestamp
device-0024,Light Sensor,Kitchen,91.3,14.32,2022-01-20 10:32:38
device-0072,Temperature Sensor,Office,98.2,83.64,2023-03-17 22:02:51
device-0040,Temperature Sensor,Hallway,71.3,-23.47,2022-11-03 21:31:50
device-0041,Pressure Sensor,Bathroom,11.9,-31.27,2021-11-26 09:04:42
device-0054,Motion Detector,Garden,14.4,24.22,2023-01-27 10:57:14
<start>
[
    {
        "Device ID": "device-0024",
        "Device Type": "Light Sensor",
        "Location": "Kitchen",
        "Battery Level (%)": 91.3,
        "Reading Value": 14.32,
        "Timestamp": "2022-01-20 10:32:38"
    },
    {
        "Device ID": "device-0072",
        "Device Type": "Temperature Sensor",
        "Location": "Office",
        "Battery Level (%)": 98.2,
        "Reading Value": 83.64,
        "Timestamp": "2023-03-17 22:02:51"
    },
    {
        "Device ID": "device-0040",
        "Device Type": "Temperature Sensor",
        "Location": "Hallway",
        "Battery Level (%)": 71.3,
        "Reading Value": -23.47,
        "Timestamp": "2022-11-03 21:31:50"
    },
    {
        "Device ID": "device-0041",
        "Device Type": "Pressure Sensor",
        "Location": "Bathroom",
        "Battery Level (%)": 11.9,
        "Reading Value": -31.27,
        "Timestamp": "2021-11-26 09:04:42"
    },
    {
        "Device ID": "device-0054",
        "Device Type": "Motion Detector",
        "Location": "Garden",
        "Battery Level (%)": 14.4,
        "Reading Value": 24.22,
        "Timestamp": "2023-01-27 10:57:14"
    }
]
<end>Please transform the following json data into csv:
[
    {
        "Title": "The Great Expedition",
        "Director": "Talon Blackthorn",
        "Release Year": 2012,
        "Box Office Earnings (M)": 210.08
    },
    {
        "Title": "The Final Voyage",
        "Director": "Aria Ravenwood",
        "Release Year": 1997,
        "Box Office Earnings (M)": 745.25
    },
    {
        "Title": "The Great Expedition",
        "Director": "Drake Nightshade",
        "Release Year": 1997,
        "Box Office Earnings (M)": 745.14
    },
    {
        "Title": "Dreamwalker",
        "Director": "Zara Stormrider",
        "Release Year": 1990,
        "Box Office Earnings (M)": 341.28
    },
    {
        "Title": "The Great Expedition",
        "Director": "Selene Darkwhisper",
        "Release Year": 2011,
        "Box Office Earnings (M)": 536.15
    },
    {
        "Title": "Dreamwalker",
        "Director": "Rylan Frostblade",
        "Release Year": 2010,
        "Box Office Earnings (M)": 156.58
    },
    {
        "Title": "Escape from Earth",
        "Director": "Lira Silverleaf",
        "Release Year": 2001,
        "Box Office Earnings (M)": 283.91
    }
]<start>
Title,Director,Release Year,Box Office Earnings (M)
The Great Expedition,Talon Blackthorn,2012,210.08
The Final Voyage,Aria Ravenwood,1997,745.25
The Great Expedition,Drake Nightshade,1997,745.14
Dreamwalker,Zara Stormrider,1990,341.28
The Great Expedition,Selene Darkwhisper,2011,536.15
Dreamwalker,Rylan Frostblade,2010,156.58
Escape from Earth,Lira Silverleaf,2001,283.91
<end>Convert this plain text to markdown:
Director: Lira Silverleaf | Release Year: 2007
Director: Orin Shadowalker | Release Year: 1971
Director: Orin Shadowalker | Release Year: 1986
Director: Mara Moonshadow | Release Year: 2017
<start>
| Director | Release Year |
| --- | --- |
| Lira Silverleaf | 2007 |
| Orin Shadowalker | 1971 |
| Orin Shadowalker | 1986 |
| Mara Moonshadow | 2017 |
<end>Here's some markdown data, can you convert it to Plain text?
| Condition | Humidity (%) | Wind Speed (km/h) |
| --- | --- | --- |
| Snowy | 97 | 19.9 |
| Cloudy | 42 | 27.6 |
| Foggy | 27 | 13.4 |
| Snowy | 59 | 15.4 |
| Snowy | 37 | 7.9 |
| Windy | 37 | 27.6 |
| Stormy | 36 | 15.3 |<start>
Condition: Snowy | Humidity (%): 97 | Wind Speed (km/h): 19.9
Condition: Cloudy | Humidity (%): 42 | Wind Speed (km/h): 27.6
Condition: Foggy | Humidity (%): 27 | Wind Speed (km/h): 13.4
Condition: Snowy | Humidity (%): 59 | Wind Speed (km/h): 15.4
Condition: Snowy | Humidity (%): 37 | Wind Speed (km/h): 7.9
Condition: Windy | Humidity (%): 37 | Wind Speed (km/h): 27.6
Condition: Stormy | Humidity (%): 36 | Wind Speed (km/h): 15.3
<end>Can you change this Yaml into PLAIN TEXT?
- Distance (miles): 391.7
  Fuel Used (gallons): 28.8
  Start Location: Phoenix
  Trip Name: Coast to Coast
- Distance (miles): 2140.3
  Fuel Used (gallons): 17.4
  Start Location: Miami
  Trip Name: Highway Odyssey
- Distance (miles): 2425.6
  Fuel Used (gallons): 45.9
  Start Location: Miami
  Trip Name: Canyon Trek
<start>
Trip Name: Coast to Coast | Start Location: Phoenix | Distance (miles): 391.7 | Fuel Used (gallons): 28.8
Trip Name: Highway Odyssey | Start Location: Miami | Distance (miles): 2140.3 | Fuel Used (gallons): 17.4
Trip Name: Canyon Trek | Start Location: Miami | Distance (miles): 2425.6 | Fuel Used (gallons): 45.9
<end>Convert this plain text to json:
Trip Name: Forest Journey | Start Location: Los Angeles | Distance (miles): 2707.7 | Duration (hours): 68.5
Trip Name: Lakeside Retreat | Start Location: Houston | Distance (miles): 1239.4 | Duration (hours): 17.8
Trip Name: Forest Journey | Start Location: Houston | Distance (miles): 1618.0 | Duration (hours): 52.5
Trip Name: City Explorer | Start Location: Los Angeles | Distance (miles): 1111.4 | Duration (hours): 9.7
Trip Name: Mountain Adventure | Start Location: Los Angeles | Distance (miles): 614.0 | Duration (hours): 29.0
Trip Name: Historic Route | Start Location: Miami | Distance (miles): 1239.4 | Duration (hours): 17.8
Trip Name: Historic Route | Start Location: Los Angeles | Distance (miles): 1239.4 | Duration (hours): 22.3
Trip Name: Desert Drive | Start Location: Phoenix | Distance (miles): 2199.8 | Duration (hours): 11.8
Trip Name: City Explorer | Start Location: San Francisco | Distance (miles): 581.2 | Duration (hours): 55.5
Trip Name: Historic Route | Start Location: New York | Distance (miles): 476.5 | Duration (hours): 9.3
<start>
[
    {
        "Trip Name": "Forest Journey",
        "Start Location": "Los Angeles",
        "Distance (miles)": 2707.7,
        "Duration (hours)": 68.5
    },
    {
        "Trip Name": "Lakeside Retreat",
        "Start Location": "Houston",
        "Distance (miles)": 1239.4,
        "Duration (hours)": 17.8
    },
    {
        "Trip Name": "Forest Journey",
        "Start Location": "Houston",
        "Distance (miles)": 1618.0,
        "Duration (hours)": 52.5
    },
    {
        "Trip Name": "City Explorer",
        "Start Location": "Los Angeles",
        "Distance (miles)": 1111.4,
        "Duration (hours)": 9.7
    },
    {
        "Trip Name": "Mountain Adventure",
        "Start Location": "Los Angeles",
        "Distance (miles)": 614.0,
        "Duration (hours)": 29.0
    },
    {
        "Trip Name": "Historic Route",
        "Start Location": "Miami",
        "Distance (miles)": 1239.4,
        "Duration (hours)": 17.8
    },
    {
        "Trip Name": "Historic Route",
        "Start Location": "Los Angeles",
        "Distance (miles)": 1239.4,
        "Duration (hours)": 22.3
    },
    {
        "Trip Name": "Desert Drive",
        "Start Location": "Phoenix",
        "Distance (miles)": 2199.8,
        "Duration (hours)": 11.8
    },
    {
        "Trip Name": "City Explorer",
        "Start Location": "San Francisco",
        "Distance (miles)": 581.2,
        "Duration (hours)": 55.5
    },
    {
        "Trip Name": "Historic Route",
        "Start Location": "New York",
        "Distance (miles)": 476.5,
        "Duration (hours)": 9.3
    }
]
<end>Transform this PLAIN TEXT structure to a CSV format:
Product Name: Contraption | SKU: SKU-1060 | Price: 438.6 | Stock Quantity: 407 | Supplier Name: Umbrella Corp
Product Name: Whatchamacallit | SKU: SKU-1030 | Price: 158.79 | Stock Quantity: 495 | Supplier Name: Wayne Enterprises
Product Name: Widget | SKU: SKU-1079 | Price: 463.35 | Stock Quantity: 229 | Supplier Name: ACME Corp
Product Name: Instrument | SKU: SKU-1042 | Price: 100.52 | Stock Quantity: 89 | Supplier Name: Wonka Industries
Product Name: Apparatus | SKU: SKU-1002 | Price: 155.19 | Stock Quantity: 61 | Supplier Name: Wonka Industries
Product Name: Widget | SKU: SKU-1064 | Price: 245.95 | Stock Quantity: 127 | Supplier Name: Umbrella Corp
Product Name: Gizmo | SKU: SKU-1014 | Price: 38.93 | Stock Quantity: 72 | Supplier Name: Wonka Industries
<start>
Product Name,SKU,Price,Stock Quantity,Supplier Name
Contraption,SKU-1060,438.6,407,Umbrella Corp
Whatchamacallit,SKU-1030,158.79,495,Wayne Enterprises
Widget,SKU-1079,463.35,229,ACME Corp
Instrument,SKU-1042,100.52,89,Wonka Industries
Apparatus,SKU-1002,155.19,61,Wonka Industries
Widget,SKU-1064,245.95,127,Umbrella Corp
Gizmo,SKU-1014,38.93,72,Wonka Industries
<end>Can you change this CSV into Markdown?
Publication Year,Rating
2001,2.1
1995,3.9
1954,1.9
1997,4.0
1994,1.9
1993,1.9
1982,4.0
<start>
| Publication Year | Rating |
| --- | --- |
| 2001 | 2.1 |
| 1995 | 3.9 |
| 1954 | 1.9 |
| 1997 | 4.0 |
| 1994 | 1.9 |
| 1993 | 1.9 |
| 1982 | 4.0 |
<end>Please transform the following csv data into plain text:
Location,Condition,Temperature (C),Day
New York,Sunny,22.9,Thursday
Denver,Snowy,3.6,Friday
Denver,Windy,-10.0,Thursday
Chicago,Stormy,23.7,Tuesday
<start>
Location: New York | Condition: Sunny | Temperature (C): 22.9 | Day: Thursday
Location: Denver | Condition: Snowy | Temperature (C): 3.6 | Day: Friday
Location: Denver | Condition: Windy | Temperature (C): -10.0 | Day: Thursday
Location: Chicago | Condition: Stormy | Temperature (C): 23.7 | Day: Tuesday
<end>Here's some yml data, can you convert it to PLAIN TEXT?
- Annual Revenue (B): 427.75
  Company: Foodies
  Market Cap: Small Cap
  Quarter: Q1
  Sector: Aerospace
  Stock Price: 216.98
- Annual Revenue (B): 142.63
  Company: AeroSpace
  Market Cap: Mid Cap
  Quarter: Q3
  Sector: Retail
  Stock Price: 823.06
- Annual Revenue (B): 96.01
  Company: GlobalTrade
  Market Cap: Small Cap
  Quarter: Q3
  Sector: Automotive
  Stock Price: 668.03
- Annual Revenue (B): 64.55
  Company: AeroSpace
  Market Cap: Mid Cap
  Quarter: Q2
  Sector: Automotive
  Stock Price: 510.95
- Annual Revenue (B): 215.05
  Company: FinanceWorks
  Market Cap: Small Cap
  Quarter: Q2
  Sector: Healthcare
  Stock Price: 728.95
- Annual Revenue (B): 488.86
  Company: FinanceWorks
  Market Cap: Small Cap
  Quarter: Q4
  Sector: Automotive
  Stock Price: 816.25
- Annual Revenue (B): 206.65
  Company: GlobalTrade
  Market Cap: Mid Cap
  Quarter: Q4
  Sector: Retail
  Stock Price: 239.69
<start>
Company: Foodies | Sector: Aerospace | Market Cap: Small Cap | Stock Price: 216.98 | Annual Revenue (B): 427.75 | Quarter: Q1
Company: AeroSpace | Sector: Retail | Market Cap: Mid Cap | Stock Price: 823.06 | Annual Revenue (B): 142.63 | Quarter: Q3
Company: GlobalTrade | Sector: Automotive | Market Cap: Small Cap | Stock Price: 668.03 | Annual Revenue (B): 96.01 | Quarter: Q3
Company: AeroSpace | Sector: Automotive | Market Cap: Mid Cap | Stock Price: 510.95 | Annual Revenue (B): 64.55 | Quarter: Q2
Company: FinanceWorks | Sector: Healthcare | Market Cap: Small Cap | Stock Price: 728.95 | Annual Revenue (B): 215.05 | Quarter: Q2
Company: FinanceWorks | Sector: Automotive | Market Cap: Small Cap | Stock Price: 816.25 | Annual Revenue (B): 488.86 | Quarter: Q4
Company: GlobalTrade | Sector: Retail | Market Cap: Mid Cap | Stock Price: 239.69 | Annual Revenue (B): 206.65 | Quarter: Q4
<end>Please transform the following YAML data into csv:
- Author: Kara Firebrand
  Genre: Fantasy
  Publication Year: 1980
  Rating: 3.5
  Title: The Last Sky
- Author: Thorne Ironwood
  Genre: Fantasy
  Publication Year: 2021
  Rating: 2.8
  Title: The Last Sky
- Author: Luna Silverleaf
  Genre: Mystery
  Publication Year: 1965
  Rating: 2.4
  Title: Tales of the Brave
<start>
Title,Author,Genre,Publication Year,Rating
The Last Sky,Kara Firebrand,Fantasy,1980,3.5
The Last Sky,Thorne Ironwood,Fantasy,2021,2.8
Tales of the Brave,Luna Silverleaf,Mystery,1965,2.4
<end>Convert this markdown to csv:
| Trip Name | Start Location | End Location | Distance (miles) | Duration (hours) | Fuel Used (gallons) |
| --- | --- | --- | --- | --- | --- |
| Lakeside Retreat | Miami | Denver | 1950.2 | 67.0 | 73.2 |
| Historic Route | Chicago | San Francisco | 2314.5 | 42.0 | 5.5 |
| Valley Voyage | Denver | Miami | 302.5 | 38.3 | 31.3 |
| Forest Journey | Phoenix | San Francisco | 1378.3 | 49.3 | 73.6 |
| Desert Drive | Chicago | Houston | 1001.3 | 41.1 | 97.8 |
| Canyon Trek | Denver | San Francisco | 955.6 | 1.4 | 59.6 |
| Mountain Adventure | Houston | Los Angeles | 786.1 | 57.3 | 67.9 |<start>
Trip Name,Start Location,End Location,Distance (miles),Duration (hours),Fuel Used (gallons)
Lakeside Retreat,Miami,Denver,1950.2,67.0,73.2
Historic Route,Chicago,San Francisco,2314.5,42.0,5.5
Valley Voyage,Denver,Miami,302.5,38.3,31.3
Forest Journey,Phoenix,San Francisco,1378.3,49.3,73.6
Desert Drive,Chicago,Houston,1001.3,41.1,97.8
Canyon Trek,Denver,San Francisco,955.6,1.4,59.6
Mountain Adventure,Houston,Los Angeles,786.1,57.3,67.9
<end>Transform this plain text structure to a csv format:
Product Name: Instrument | SKU: SKU-1046 | Supplier Name: Wayne Enterprises
Product Name: Device | SKU: SKU-1048 | Supplier Name: Wonka Industries
Product Name: Apparatus | SKU: SKU-1002 | Supplier Name: Umbrella Corp
Product Name: Doohickey | SKU: SKU-1045 | Supplier Name: ACME Corp
<start>
Product Name,SKU,Supplier Name
Instrument,SKU-1046,Wayne Enterprises
Device,SKU-1048,Wonka Industries
Apparatus,SKU-1002,Umbrella Corp
Doohickey,SKU-1045,ACME Corp
<end>Can you change this yaml into json?
- Day: Tuesday
  Location: New York
  Wind Speed (km/h): 13.9
- Day: Thursday
  Location: Los Angeles
  Wind Speed (km/h): 15.3
- Day: Friday
  Location: New York
  Wind Speed (km/h): 23.4
- Day: Friday
  Location: Miami
  Wind Speed (km/h): 15.9
<start>
[
    {
        "Location": "New York",
        "Wind Speed (km/h)": 13.9,
        "Day": "Tuesday"
    },
    {
        "Location": "Los Angeles",
        "Wind Speed (km/h)": 15.3,
        "Day": "Thursday"
    },
    {
        "Location": "New York",
        "Wind Speed (km/h)": 23.4,
        "Day": "Friday"
    },
    {
        "Location": "Miami",
        "Wind Speed (km/h)": 15.9,
        "Day": "Friday"
    }
]
<end>Can you change this Yaml into MARKDOWN?
- Condition: Foggy
  Day: Wednesday
  Humidity (%): 35
  Location: Los Angeles
  Temperature (C): 10.2
  Wind Speed (km/h): 14.5
- Condition: Sunny
  Day: Sunday
  Humidity (%): 23
  Location: Phoenix
  Temperature (C): 1.4
  Wind Speed (km/h): 9.9
- Condition: Rainy
  Day: Monday
  Humidity (%): 58
  Location: Miami
  Temperature (C): 2.0
  Wind Speed (km/h): 14.1
<start>
| Location | Condition | Temperature (C) | Humidity (%) | Wind Speed (km/h) | Day |
| --- | --- | --- | --- | --- | --- |
| Los Angeles | Foggy | 10.2 | 35 | 14.5 | Wednesday |
| Phoenix | Sunny | 1.4 | 23 | 9.9 | Sunday |
| Miami | Rainy | 2.0 | 58 | 14.1 | Monday |
<end>Please transform the following MARKDOWN data into plain text:
| Database Name | Queries per Second | Connection Count | Average Latency (ms) | Timestamp |
| --- | --- | --- | --- | --- |
| LogsDB | 646.94 | 23 | 43.03 | 2023-05-26 18:51:09 |
| InventoryDB | 840.22 | 441 | 65.86 | 2022-05-16 01:06:35 |
| ProductsDB | 4773.91 | 447 | 15.79 | 2022-08-21 17:57:20 |
| LogsDB | 635.99 | 459 | 30.83 | 2022-11-06 22:26:48 |
| UserDB | 4231.28 | 459 | 85.97 | 2021-08-17 08:56:34 |
| OrdersDB | 3569.79 | 150 | 70.83 | 2023-04-14 22:52:10 |
| InventoryDB | 4448.49 | 345 | 3.52 | 2022-08-27 03:06:33 |
| LogsDB | 4448.49 | 313 | 21.46 | 2023-03-14 20:14:50 |
| LogsDB | 445.47 | 156 | 13.15 | 2021-07-23 13:09:49 |<start>
Database Name: LogsDB | Queries per Second: 646.94 | Connection Count: 23 | Average Latency (ms): 43.03 | Timestamp: 2023-05-26 18:51:09
Database Name: InventoryDB | Queries per Second: 840.22 | Connection Count: 441 | Average Latency (ms): 65.86 | Timestamp: 2022-05-16 01:06:35
Database Name: ProductsDB | Queries per Second: 4773.91 | Connection Count: 447 | Average Latency (ms): 15.79 | Timestamp: 2022-08-21 17:57:20
Database Name: LogsDB | Queries per Second: 635.99 | Connection Count: 459 | Average Latency (ms): 30.83 | Timestamp: 2022-11-06 22:26:48
Database Name: UserDB | Queries per Second: 4231.28 | Connection Count: 459 | Average Latency (ms): 85.97 | Timestamp: 2021-08-17 08:56:34
Database Name: OrdersDB | Queries per Second: 3569.79 | Connection Count: 150 | Average Latency (ms): 70.83 | Timestamp: 2023-04-14 22:52:10
Database Name: InventoryDB | Queries per Second: 4448.49 | Connection Count: 345 | Average Latency (ms): 3.52 | Timestamp: 2022-08-27 03:06:33
Database Name: LogsDB | Queries per Second: 4448.49 | Connection Count: 313 | Average Latency (ms): 21.46 | Timestamp: 2023-03-14 20:14:50
Database Name: LogsDB | Queries per Second: 445.47 | Connection Count: 156 | Average Latency (ms): 13.15 | Timestamp: 2021-07-23 13:09:49
<end>Please transform the following markdown data into plain text:
| Title | Director |
| --- | --- |
| The Final Voyage | Rylan Frostblade |
| Dreamwalker | Orin Shadowalker |
| Mystery of the Depths | Zara Stormrider |
| Rise of the Titans | Mara Moonshadow |
| The Great Expedition | Lira Silverleaf |
| Beyond the Veil | Lira Silverleaf |
| Beyond the Veil | Orin Shadowalker |
| Edge of Infinity | Talon Blackthorn |
| Starbound Odyssey | Talon Blackthorn |<start>
Title: The Final Voyage | Director: Rylan Frostblade
Title: Dreamwalker | Director: Orin Shadowalker
Title: Mystery of the Depths | Director: Zara Stormrider
Title: Rise of the Titans | Director: Mara Moonshadow
Title: The Great Expedition | Director: Lira Silverleaf
Title: Beyond the Veil | Director: Lira Silverleaf
Title: Beyond the Veil | Director: Orin Shadowalker
Title: Edge of Infinity | Director: Talon Blackthorn
Title: Starbound Odyssey | Director: Talon Blackthorn
<end>Please transform the following PLAIN TEXT data into CSV:
Device ID: device-0040 | Location: Garden | Battery Level (%): 79.0 | Reading Value: 38.03 | Timestamp: 2021-07-16 07:49:45
Device ID: device-0047 | Location: Bedroom | Battery Level (%): 65.1 | Reading Value: -33.46 | Timestamp: 2023-08-08 13:32:07
Device ID: device-0054 | Location: Garden | Battery Level (%): 75.3 | Reading Value: -35.55 | Timestamp: 2023-02-02 01:33:03
Device ID: device-0065 | Location: Garage | Battery Level (%): 99.1 | Reading Value: 27.72 | Timestamp: 2023-04-26 08:10:18
Device ID: device-0016 | Location: Living Room | Battery Level (%): 99.1 | Reading Value: 46.21 | Timestamp: 2023-03-25 12:24:15
Device ID: device-0082 | Location: Bedroom | Battery Level (%): 50.5 | Reading Value: 83.77 | Timestamp: 2022-04-25 04:38:06
Device ID: device-0096 | Location: Kitchen | Battery Level (%): 94.5 | Reading Value: 14.94 | Timestamp: 2022-12-13 13:15:48
Device ID: device-0049 | Location: Office | Battery Level (%): 17.8 | Reading Value: -16.33 | Timestamp: 2022-08-02 01:48:32
Device ID: device-0077 | Location: Garden | Battery Level (%): 93.8 | Reading Value: -11.55 | Timestamp: 2022-10-11 23:57:20
Device ID: device-0021 | Location: Bedroom | Battery Level (%): 95.7 | Reading Value: -11.55 | Timestamp: 2023-12-04 22:56:24
<start>
Device ID,Location,Battery Level (%),Reading Value,Timestamp
device-0040,Garden,79.0,38.03,2021-07-16 07:49:45
device-0047,Bedroom,65.1,-33.46,2023-08-08 13:32:07
device-0054,Garden,75.3,-35.55,2023-02-02 01:33:03
device-0065,Garage,99.1,27.72,2023-04-26 08:10:18
device-0016,Living Room,99.1,46.21,2023-03-25 12:24:15
device-0082,Bedroom,50.5,83.77,2022-04-25 04:38:06
device-0096,Kitchen,94.5,14.94,2022-12-13 13:15:48
device-0049,Office,17.8,-16.33,2022-08-02 01:48:32
device-0077,Garden,93.8,-11.55,2022-10-11 23:57:20
device-0021,Bedroom,95.7,-11.55,2023-12-04 22:56:24
<end>Please transform the following json data into markdown:
[
    {
        "SKU": "SKU-1080",
        "Price": 423.31,
        "Category": "Household",
        "Supplier Name": "Wayne Enterprises"
    },
    {
        "SKU": "SKU-1044",
        "Price": 251.46,
        "Category": "Household",
        "Supplier Name": "Globex"
    },
    {
        "SKU": "SKU-1009",
        "Price": 74.15,
        "Category": "Electronics",
        "Supplier Name": "Globex"
    },
    {
        "SKU": "SKU-1034",
        "Price": 198.38,
        "Category": "Electronics",
        "Supplier Name": "Wonka Industries"
    },
    {
        "SKU": "SKU-1031",
        "Price": 370.76,
        "Category": "Toys",
        "Supplier Name": "Wayne Enterprises"
    }
]<start>
| SKU | Price | Category | Supplier Name |
| --- | --- | --- | --- |
| SKU-1080 | 423.31 | Household | Wayne Enterprises |
| SKU-1044 | 251.46 | Household | Globex |
| SKU-1009 | 74.15 | Electronics | Globex |
| SKU-1034 | 198.38 | Electronics | Wonka Industries |
| SKU-1031 | 370.76 | Toys | Wayne Enterprises |
<end>Please transform the following Plain text data into csv:
Device ID: device-0100 | Device Type: Motion Detector | Reading Value: 8.5 | Timestamp: 2022-02-07 18:45:00
Device ID: device-0071 | Device Type: Motion Detector | Reading Value: 58.85 | Timestamp: 2021-03-06 08:16:49
Device ID: device-0029 | Device Type: Pressure Sensor | Reading Value: 62.87 | Timestamp: 2021-12-01 15:23:24
<start>
Device ID,Device Type,Reading Value,Timestamp
device-0100,Motion Detector,8.5,2022-02-07 18:45:00
device-0071,Motion Detector,58.85,2021-03-06 08:16:49
device-0029,Pressure Sensor,62.87,2021-12-01 15:23:24
<end>Transform this markdown structure to a CSV format:
| Sector | Market Cap | Annual Revenue (B) |
| --- | --- | --- |
| Biotech | Mega Cap | 413.07 |
| Automotive | Small Cap | 162.96 |
| Biotech | Mega Cap | 114.57 |
| Energy | Mid Cap | 430.53 |
| Finance | Mid Cap | 289.04 |
| Automotive | Mid Cap | 111.8 |<start>
Sector,Market Cap,Annual Revenue (B)
Biotech,Mega Cap,413.07
Automotive,Small Cap,162.96
Biotech,Mega Cap,114.57
Energy,Mid Cap,430.53
Finance,Mid Cap,289.04
Automotive,Mid Cap,111.8
<end>Here's some yml data, can you convert it to Markdown?
- Box Office Earnings (M): 85.24
  Director: Selene Darkwhisper
  Release Year: 2004
  Title: The Great Expedition
- Box Office Earnings (M): 594.83
  Director: Cade Firebrand
  Release Year: 2018
  Title: Escape from Earth
- Box Office Earnings (M): 230.13
  Director: Rylan Frostblade
  Release Year: 2004
  Title: Dreamwalker
- Box Office Earnings (M): 560.16
  Director: Cade Firebrand
  Release Year: 1995
  Title: Starbound Odyssey
- Box Office Earnings (M): 846.81
  Director: Drake Nightshade
  Release Year: 2006
  Title: The Endless Horizon
- Box Office Earnings (M): 13.95
  Director: Rylan Frostblade
  Release Year: 2007
  Title: Rise of the Titans
- Box Office Earnings (M): 546.87
  Director: Drake Nightshade
  Release Year: 2012
  Title: The Endless Horizon
- Box Office Earnings (M): 912.87
  Director: Drake Nightshade
  Release Year: 2003
  Title: The Great Expedition
<start>
| Title | Director | Release Year | Box Office Earnings (M) |
| --- | --- | --- | --- |
| The Great Expedition | Selene Darkwhisper | 2004 | 85.24 |
| Escape from Earth | Cade Firebrand | 2018 | 594.83 |
| Dreamwalker | Rylan Frostblade | 2004 | 230.13 |
| Starbound Odyssey | Cade Firebrand | 1995 | 560.16 |
| The Endless Horizon | Drake Nightshade | 2006 | 846.81 |
| Rise of the Titans | Rylan Frostblade | 2007 | 13.95 |
| The Endless Horizon | Drake Nightshade | 2012 | 546.87 |
| The Great Expedition | Drake Nightshade | 2003 | 912.87 |
<end>Please transform the following CSV data into Json:
Queries per Second,Cache Hit Ratio (%),Timestamp
4211.25,78.15,2022-09-02 12:34:16
1620.77,85.49,2022-10-28 13:38:45
176.77,81.23,2022-06-14 11:35:47
2231.87,76.09,2022-11-01 15:33:44
1469.48,71.38,2021-05-15 03:57:22
4923.37,87.38,2023-10-23 11:19:29
1167.49,82.15,2022-01-28 02:30:41
<start>
[
    {
        "Queries per Second": 4211.25,
        "Cache Hit Ratio (%)": 78.15,
        "Timestamp": "2022-09-02 12:34:16"
    },
    {
        "Queries per Second": 1620.77,
        "Cache Hit Ratio (%)": 85.49,
        "Timestamp": "2022-10-28 13:38:45"
    },
    {
        "Queries per Second": 176.77,
        "Cache Hit Ratio (%)": 81.23,
        "Timestamp": "2022-06-14 11:35:47"
    },
    {
        "Queries per Second": 2231.87,
        "Cache Hit Ratio (%)": 76.09,
        "Timestamp": "2022-11-01 15:33:44"
    },
    {
        "Queries per Second": 1469.48,
        "Cache Hit Ratio (%)": 71.38,
        "Timestamp": "2021-05-15 03:57:22"
    },
    {
        "Queries per Second": 4923.37,
        "Cache Hit Ratio (%)": 87.38,
        "Timestamp": "2023-10-23 11:19:29"
    },
    {
        "Queries per Second": 1167.49,
        "Cache Hit Ratio (%)": 82.15,
        "Timestamp": "2022-01-28 02:30:41"
    }
]
<end>Here's some Plain text data, can you convert it to Markdown?
Start Location: San Francisco | End Location: Chicago | Distance (miles): 2675.9 | Duration (hours): 45.6 | Fuel Used (gallons): 16.5
Start Location: Houston | End Location: Miami | Distance (miles): 1803.0 | Duration (hours): 66.7 | Fuel Used (gallons): 77.1
Start Location: New York | End Location: Denver | Distance (miles): 2361.4 | Duration (hours): 17.1 | Fuel Used (gallons): 54.6
Start Location: New York | End Location: Chicago | Distance (miles): 2675.9 | Duration (hours): 22.1 | Fuel Used (gallons): 97.8
Start Location: Houston | End Location: Denver | Distance (miles): 463.8 | Duration (hours): 25.0 | Fuel Used (gallons): 12.2
Start Location: New York | End Location: Houston | Distance (miles): 2769.8 | Duration (hours): 19.2 | Fuel Used (gallons): 12.5
<start>
| Start Location | End Location | Distance (miles) | Duration (hours) | Fuel Used (gallons) |
| --- | --- | --- | --- | --- |
| San Francisco | Chicago | 2675.9 | 45.6 | 16.5 |
| Houston | Miami | 1803.0 | 66.7 | 77.1 |
| New York | Denver | 2361.4 | 17.1 | 54.6 |
| New York | Chicago | 2675.9 | 22.1 | 97.8 |
| Houston | Denver | 463.8 | 25.0 | 12.2 |
| New York | Houston | 2769.8 | 19.2 | 12.5 |
<end>Can you change this JSON into Csv?
[
    {
        "Device ID": "device-0047",
        "Device Type": "Motion Detector",
        "Location": "Hallway",
        "Battery Level (%)": 62.6,
        "Timestamp": "2023-09-09 22:25:28"
    },
    {
        "Device ID": "device-0012",
        "Device Type": "Pressure Sensor",
        "Location": "Hallway",
        "Battery Level (%)": 93.3,
        "Timestamp": "2021-04-13 01:23:14"
    },
    {
        "Device ID": "device-0016",
        "Device Type": "Pressure Sensor",
        "Location": "Bedroom",
        "Battery Level (%)": 93.1,
        "Timestamp": "2023-10-19 08:27:23"
    },
    {
        "Device ID": "device-0027",
        "Device Type": "Motion Detector",
        "Location": "Garage",
        "Battery Level (%)": 39.3,
        "Timestamp": "2023-09-18 22:54:36"
    },
    {
        "Device ID": "device-0022",
        "Device Type": "Humidity Sensor",
        "Location": "Office",
        "Battery Level (%)": 54.5,
        "Timestamp": "2023-09-11 22:23:59"
    }
]<start>
Device ID,Device Type,Location,Battery Level (%),Timestamp
device-0047,Motion Detector,Hallway,62.6,2023-09-09 22:25:28
device-0012,Pressure Sensor,Hallway,93.3,2021-04-13 01:23:14
device-0016,Pressure Sensor,Bedroom,93.1,2023-10-19 08:27:23
device-0027,Motion Detector,Garage,39.3,2023-09-18 22:54:36
device-0022,Humidity Sensor,Office,54.5,2023-09-11 22:23:59
<end>Transform this MARKDOWN structure to a plain text format:
| Title | Genre | Release Year | Box Office Earnings (M) |
| --- | --- | --- | --- |
| Escape from Earth | Horror | 1985 | 430.67 |
| Starbound Odyssey | Drama | 1970 | 468.58 |
| Edge of Infinity | Sci-Fi | 2000 | 553.79 |
| Dreamwalker | Comedy | 1990 | 490.13 |
| Edge of Infinity | Action | 1989 | 837.52 |
| The Great Expedition | Sci-Fi | 2005 | 837.52 |<start>
Title: Escape from Earth | Genre: Horror | Release Year: 1985 | Box Office Earnings (M): 430.67
Title: Starbound Odyssey | Genre: Drama | Release Year: 1970 | Box Office Earnings (M): 468.58
Title: Edge of Infinity | Genre: Sci-Fi | Release Year: 2000 | Box Office Earnings (M): 553.79
Title: Dreamwalker | Genre: Comedy | Release Year: 1990 | Box Office Earnings (M): 490.13
Title: Edge of Infinity | Genre: Action | Release Year: 1989 | Box Office Earnings (M): 837.52
Title: The Great Expedition | Genre: Sci-Fi | Release Year: 2005 | Box Office Earnings (M): 837.52
<end>Here's some YAML data, can you convert it to markdown?
- Category: Sports
  Stock Quantity: 324
  Supplier Name: Umbrella Corp
- Category: Sports
  Stock Quantity: 440
  Supplier Name: Wonka Industries
- Category: Automotive
  Stock Quantity: 236
  Supplier Name: Globex
- Category: Electronics
  Stock Quantity: 132
  Supplier Name: Wonka Industries
- Category: Toys
  Stock Quantity: 260
  Supplier Name: Wayne Enterprises
- Category: Electronics
  Stock Quantity: 445
  Supplier Name: Globex
<start>
| Stock Quantity | Category | Supplier Name |
| --- | --- | --- |
| 324 | Sports | Umbrella Corp |
| 440 | Sports | Wonka Industries |
| 236 | Automotive | Globex |
| 132 | Electronics | Wonka Industries |
| 260 | Toys | Wayne Enterprises |
| 445 | Electronics | Globex |
<end>Convert this MARKDOWN to CSV:
| Age | Birth Month | Income |
| --- | --- | --- |
| 38 | March | 295000 |
| 33 | May | 300000 |
| 24 | May | 345000 |
| 21 | March | 355000 |<start>
Age,Birth Month,Income
38,March,295000
33,May,300000
24,May,345000
21,March,355000
<end>Can you change this Json into markdown?
[
    {
        "Product Name": "Doohickey",
        "SKU": "SKU-1068",
        "Price": 47.67,
        "Stock Quantity": 93,
        "Category": "Automotive"
    },
    {
        "Product Name": "Device",
        "SKU": "SKU-1078",
        "Price": 286.15,
        "Stock Quantity": 175,
        "Category": "Automotive"
    },
    {
        "Product Name": "Device",
        "SKU": "SKU-1075",
        "Price": 468.51,
        "Stock Quantity": 294,
        "Category": "Electronics"
    },
    {
        "Product Name": "Doohickey",
        "SKU": "SKU-1096",
        "Price": 396.39,
        "Stock Quantity": 74,
        "Category": "Toys"
    },
    {
        "Product Name": "Gizmo",
        "SKU": "SKU-1058",
        "Price": 468.03,
        "Stock Quantity": 397,
        "Category": "Sports"
    },
    {
        "Product Name": "Device",
        "SKU": "SKU-1043",
        "Price": 114.42,
        "Stock Quantity": 134,
        "Category": "Household"
    }
]<start>
| Product Name | SKU | Price | Stock Quantity | Category |
| --- | --- | --- | --- | --- |
| Doohickey | SKU-1068 | 47.67 | 93 | Automotive |
| Device | SKU-1078 | 286.15 | 175 | Automotive |
| Device | SKU-1075 | 468.51 | 294 | Electronics |
| Doohickey | SKU-1096 | 396.39 | 74 | Toys |
| Gizmo | SKU-1058 | 468.03 | 397 | Sports |
| Device | SKU-1043 | 114.42 | 134 | Household |
<end>Convert this json to plain text:
[
    {
        "Restaurant Name": "Taco Town",
        "Cuisine": "Japanese",
        "Location": "Seattle",
        "Rating": 2
    },
    {
        "Restaurant Name": "The Steakhouse",
        "Cuisine": "Mediterranean",
        "Location": "Houston",
        "Rating": 2
    },
    {
        "Restaurant Name": "Sushi World",
        "Cuisine": "Indian",
        "Location": "New York",
        "Rating": 4
    },
    {
        "Restaurant Name": "The Steakhouse",
        "Cuisine": "Mediterranean",
        "Location": "Los Angeles",
        "Rating": 5
    },
    {
        "Restaurant Name": "Curry Corner",
        "Cuisine": "Indian",
        "Location": "Chicago",
        "Rating": 1
    },
    {
        "Restaurant Name": "BBQ Barn",
        "Cuisine": "Japanese",
        "Location": "Chicago",
        "Rating": 3
    },
    {
        "Restaurant Name": "Vegan Delight",
        "Cuisine": "Mediterranean",
        "Location": "New York",
        "Rating": 1
    },
    {
        "Restaurant Name": "Pizza Planet",
        "Cuisine": "Italian",
        "Location": "Houston",
        "Rating": 3
    }
]<start>
Restaurant Name: Taco Town | Cuisine: Japanese | Location: Seattle | Rating: 2
Restaurant Name: The Steakhouse | Cuisine: Mediterranean | Location: Houston | Rating: 2
Restaurant Name: Sushi World | Cuisine: Indian | Location: New York | Rating: 4
Restaurant Name: The Steakhouse | Cuisine: Mediterranean | Location: Los Angeles | Rating: 5
Restaurant Name: Curry Corner | Cuisine: Indian | Location: Chicago | Rating: 1
Restaurant Name: BBQ Barn | Cuisine: Japanese | Location: Chicago | Rating: 3
Restaurant Name: Vegan Delight | Cuisine: Mediterranean | Location: New York | Rating: 1
Restaurant Name: Pizza Planet | Cuisine: Italian | Location: Houston | Rating: 3
<end>Please transform the following Json data into plain text:
[
    {
        "Company": "HealthPlus",
        "Sector": "Finance",
        "Stock Price": 586.17,
        "Annual Revenue (B)": 181.68,
        "Quarter": "Q4"
    },
    {
        "Company": "Foodies",
        "Sector": "Healthcare",
        "Stock Price": 576.3,
        "Annual Revenue (B)": 446.17,
        "Quarter": "Q4"
    },
    {
        "Company": "TechCorp",
        "Sector": "Aerospace",
        "Stock Price": 394.23,
        "Annual Revenue (B)": 149.31,
        "Quarter": "Q3"
    },
    {
        "Company": "Foodies",
        "Sector": "Healthcare",
        "Stock Price": 977.66,
        "Annual Revenue (B)": 257.31,
        "Quarter": "Q1"
    },
    {
        "Company": "AeroSpace",
        "Sector": "Energy",
        "Stock Price": 750.79,
        "Annual Revenue (B)": 117.27,
        "Quarter": "Q4"
    },
    {
        "Company": "GlobalTrade",
        "Sector": "Technology",
        "Stock Price": 527.47,
        "Annual Revenue (B)": 194.14,
        "Quarter": "Q3"
    },
    {
        "Company": "RetailHub",
        "Sector": "Automotive",
        "Stock Price": 579.25,
        "Annual Revenue (B)": 78.71,
        "Quarter": "Q4"
    },
    {
        "Company": "TechCorp",
        "Sector": "Energy",
        "Stock Price": 791.12,
        "Annual Revenue (B)": 179.66,
        "Quarter": "Q1"
    }
]<start>
Company: HealthPlus | Sector: Finance | Stock Price: 586.17 | Annual Revenue (B): 181.68 | Quarter: Q4
Company: Foodies | Sector: Healthcare | Stock Price: 576.3 | Annual Revenue (B): 446.17 | Quarter: Q4
Company: TechCorp | Sector: Aerospace | Stock Price: 394.23 | Annual Revenue (B): 149.31 | Quarter: Q3
Company: Foodies | Sector: Healthcare | Stock Price: 977.66 | Annual Revenue (B): 257.31 | Quarter: Q1
Company: AeroSpace | Sector: Energy | Stock Price: 750.79 | Annual Revenue (B): 117.27 | Quarter: Q4
Company: GlobalTrade | Sector: Technology | Stock Price: 527.47 | Annual Revenue (B): 194.14 | Quarter: Q3
Company: RetailHub | Sector: Automotive | Stock Price: 579.25 | Annual Revenue (B): 78.71 | Quarter: Q4
Company: TechCorp | Sector: Energy | Stock Price: 791.12 | Annual Revenue (B): 179.66 | Quarter: Q1
<end>Here's some Markdown data, can you convert it to plain text?
| Title | Genre | Publication Year |
| --- | --- | --- |
| The Last Sky | Science Fiction | 2015 |
| The Silent Grove | Non-Fiction | 1987 |
| Echoes of Eternity | Fantasy | 1960 |<start>
Title: The Last Sky | Genre: Science Fiction | Publication Year: 2015
Title: The Silent Grove | Genre: Non-Fiction | Publication Year: 1987
Title: Echoes of Eternity | Genre: Fantasy | Publication Year: 1960
<end>Transform this YAML structure to a plain text format:
- Cuisine: American
  Location: Phoenix
  Price Range: $$$$$
  Rating: 3
  Restaurant Name: Pasta Palace
- Cuisine: French
  Location: New York
  Price Range: $$$$$
  Rating: 1
  Restaurant Name: Pizza Planet
- Cuisine: Chinese
  Location: Seattle
  Price Range: $$$$$
  Rating: 1
  Restaurant Name: Pasta Palace
- Cuisine: Chinese
  Location: Houston
  Price Range: $$
  Rating: 1
  Restaurant Name: The Steakhouse
- Cuisine: Japanese
  Location: Chicago
  Price Range: $$$$
  Rating: 5
  Restaurant Name: Curry Corner
- Cuisine: French
  Location: Houston
  Price Range: $
  Rating: 1
  Restaurant Name: Vegan Delight
- Cuisine: Indian
  Location: Houston
  Price Range: $
  Rating: 5
  Restaurant Name: The Golden Spoon
- Cuisine: American
  Location: Los Angeles
  Price Range: $$$$$
  Rating: 5
  Restaurant Name: Vegan Delight
<start>
Restaurant Name: Pasta Palace | Cuisine: American | Location: Phoenix | Rating: 3 | Price Range: $$$$$
Restaurant Name: Pizza Planet | Cuisine: French | Location: New York | Rating: 1 | Price Range: $$$$$
Restaurant Name: Pasta Palace | Cuisine: Chinese | Location: Seattle | Rating: 1 | Price Range: $$$$$
Restaurant Name: The Steakhouse | Cuisine: Chinese | Location: Houston | Rating: 1 | Price Range: $$
Restaurant Name: Curry Corner | Cuisine: Japanese | Location: Chicago | Rating: 5 | Price Range: $$$$
Restaurant Name: Vegan Delight | Cuisine: French | Location: Houston | Rating: 1 | Price Range: $
Restaurant Name: The Golden Spoon | Cuisine: Indian | Location: Houston | Rating: 5 | Price Range: $
Restaurant Name: Vegan Delight | Cuisine: American | Location: Los Angeles | Rating: 5 | Price Range: $$$$$
<end>Please transform the following csv data into MARKDOWN:
Age,Income
56,245000
59,65000
25,120000
62,265000
18,290000
36,335000
51,85000
33,280000
47,125000
63,225000
<start>
| Age | Income |
| --- | --- |
| 56 | 245000 |
| 59 | 65000 |
| 25 | 120000 |
| 62 | 265000 |
| 18 | 290000 |
| 36 | 335000 |
| 51 | 85000 |
| 33 | 280000 |
| 47 | 125000 |
| 63 | 225000 |
<end>Can you change this PLAIN TEXT into yml?
Device ID: device-0087 | Device Type: Pressure Sensor | Location: Bathroom | Battery Level (%): 96.0 | Reading Value: -6.15 | Timestamp: 2022-08-21 04:31:18
Device ID: device-0034 | Device Type: Temperature Sensor | Location: Hallway | Battery Level (%): 47.9 | Reading Value: 64.83 | Timestamp: 2023-01-23 01:33:26
Device ID: device-0060 | Device Type: Pressure Sensor | Location: Bedroom | Battery Level (%): 78.3 | Reading Value: 57.57 | Timestamp: 2021-01-15 02:56:37
Device ID: device-0084 | Device Type: Humidity Sensor | Location: Office | Battery Level (%): 77.5 | Reading Value: -35.14 | Timestamp: 2022-08-17 22:18:15
Device ID: device-0033 | Device Type: Pressure Sensor | Location: Hallway | Battery Level (%): 90.8 | Reading Value: -23.03 | Timestamp: 2023-11-17 14:31:04
Device ID: device-0064 | Device Type: Temperature Sensor | Location: Garden | Battery Level (%): 91.6 | Reading Value: -29.7 | Timestamp: 2022-07-06 08:48:06
<start>
- Battery Level (%): 96.0
  Device ID: device-0087
  Device Type: Pressure Sensor
  Location: Bathroom
  Reading Value: -6.15
  Timestamp: '2022-08-21 04:31:18'
- Battery Level (%): 47.9
  Device ID: device-0034
  Device Type: Temperature Sensor
  Location: Hallway
  Reading Value: 64.83
  Timestamp: '2023-01-23 01:33:26'
- Battery Level (%): 78.3
  Device ID: device-0060
  Device Type: Pressure Sensor
  Location: Bedroom
  Reading Value: 57.57
  Timestamp: '2021-01-15 02:56:37'
- Battery Level (%): 77.5
  Device ID: device-0084
  Device Type: Humidity Sensor
  Location: Office
  Reading Value: -35.14
  Timestamp: '2022-08-17 22:18:15'
- Battery Level (%): 90.8
  Device ID: device-0033
  Device Type: Pressure Sensor
  Location: Hallway
  Reading Value: -23.03
  Timestamp: '2023-11-17 14:31:04'
- Battery Level (%): 91.6
  Device ID: device-0064
  Device Type: Temperature Sensor
  Location: Garden
  Reading Value: -29.7
  Timestamp: '2022-07-06 08:48:06'
<end>Please transform the following Json data into CSV:
[
    {
        "Company": "BioPharm",
        "Sector": "Energy",
        "Annual Revenue (B)": 141.38,
        "Quarter": "Q3"
    },
    {
        "Company": "RetailHub",
        "Sector": "Biotech",
        "Annual Revenue (B)": 239.11,
        "Quarter": "Q1"
    },
    {
        "Company": "TechCorp",
        "Sector": "Finance",
        "Annual Revenue (B)": 357.42,
        "Quarter": "Q4"
    }
]<start>
Company,Sector,Annual Revenue (B),Quarter
BioPharm,Energy,141.38,Q3
RetailHub,Biotech,239.11,Q1
TechCorp,Finance,357.42,Q4
<end>Please transform the following csv data into plain text:
Company,Date,High Price,Low Price,Volume
BioLife,2017-04-09,1068.23,241.74,1454489
HealthGen,2021-03-16,1405.59,416.75,9111467
AutoMotive,2023-12-28,1473.28,41.15,8828934
HealthGen,2017-06-10,1281.73,282.78,5596656
MediaGroup,2020-08-09,1283.34,471.07,7326565
AutoMotive,2021-04-13,719.35,519.15,5905716
FinanceTrust,2011-10-09,1335.54,50.88,9412784
AutoMotive,2020-08-15,1419.15,1281.73,6641632
<start>
Company: BioLife | Date: 2017-04-09 | High Price: 1068.23 | Low Price: 241.74 | Volume: 1454489
Company: HealthGen | Date: 2021-03-16 | High Price: 1405.59 | Low Price: 416.75 | Volume: 9111467
Company: AutoMotive | Date: 2023-12-28 | High Price: 1473.28 | Low Price: 41.15 | Volume: 8828934
Company: HealthGen | Date: 2017-06-10 | High Price: 1281.73 | Low Price: 282.78 | Volume: 5596656
Company: MediaGroup | Date: 2020-08-09 | High Price: 1283.34 | Low Price: 471.07 | Volume: 7326565
Company: AutoMotive | Date: 2021-04-13 | High Price: 719.35 | Low Price: 519.15 | Volume: 5905716
Company: FinanceTrust | Date: 2011-10-09 | High Price: 1335.54 | Low Price: 50.88 | Volume: 9412784
Company: AutoMotive | Date: 2020-08-15 | High Price: 1419.15 | Low Price: 1281.73 | Volume: 6641632
<end>Transform this Json structure to a Yml format:
[
    {
        "Name": "Cora",
        "Income": 355000
    },
    {
        "Name": "Kelli",
        "Income": 365000
    },
    {
        "Name": "Alexander",
        "Income": 280000
    },
    {
        "Name": "Stacey",
        "Income": 220000
    },
    {
        "Name": "Kristine",
        "Income": 335000
    },
    {
        "Name": "Jonathan",
        "Income": 475000
    },
    {
        "Name": "Hilda",
        "Income": 350000
    },
    {
        "Name": "Alyssa",
        "Income": 40000
    },
    {
        "Name": "Lucille",
        "Income": 180000
    }
]<start>
- Income: 355000
  Name: Cora
- Income: 365000
  Name: Kelli
- Income: 280000
  Name: Alexander
- Income: 220000
  Name: Stacey
- Income: 335000
  Name: Kristine
- Income: 475000
  Name: Jonathan
- Income: 350000
  Name: Hilda
- Income: 40000
  Name: Alyssa
- Income: 180000
  Name: Lucille
<end>Can you change this markdown into plain text?
| Device Type | Location | Battery Level (%) | Timestamp |
| --- | --- | --- | --- |
| Pressure Sensor | Garage | 91.3 | 2021-11-16 17:30:09 |
| Pressure Sensor | Garden | 93.8 | 2021-07-01 19:50:07 |
| Temperature Sensor | Kitchen | 47.6 | 2022-12-20 19:53:33 |
| Motion Detector | Garage | 62.2 | 2022-07-26 12:19:29 |
| Humidity Sensor | Bathroom | 11.8 | 2021-12-18 04:14:38 |
| Motion Detector | Office | 18.3 | 2021-05-17 18:49:47 |
| Motion Detector | Office | 46.0 | 2022-06-02 20:21:14 |
| Pressure Sensor | Kitchen | 37.9 | 2022-10-17 12:10:55 |
| Light Sensor | Hallway | 81.0 | 2022-10-19 06:33:26 |
| Humidity Sensor | Hallway | 27.3 | 2021-01-27 11:15:46 |<start>
Device Type: Pressure Sensor | Location: Garage | Battery Level (%): 91.3 | Timestamp: 2021-11-16 17:30:09
Device Type: Pressure Sensor | Location: Garden | Battery Level (%): 93.8 | Timestamp: 2021-07-01 19:50:07
Device Type: Temperature Sensor | Location: Kitchen | Battery Level (%): 47.6 | Timestamp: 2022-12-20 19:53:33
Device Type: Motion Detector | Location: Garage | Battery Level (%): 62.2 | Timestamp: 2022-07-26 12:19:29
Device Type: Humidity Sensor | Location: Bathroom | Battery Level (%): 11.8 | Timestamp: 2021-12-18 04:14:38
Device Type: Motion Detector | Location: Office | Battery Level (%): 18.3 | Timestamp: 2021-05-17 18:49:47
Device Type: Motion Detector | Location: Office | Battery Level (%): 46.0 | Timestamp: 2022-06-02 20:21:14
Device Type: Pressure Sensor | Location: Kitchen | Battery Level (%): 37.9 | Timestamp: 2022-10-17 12:10:55
Device Type: Light Sensor | Location: Hallway | Battery Level (%): 81.0 | Timestamp: 2022-10-19 06:33:26
Device Type: Humidity Sensor | Location: Hallway | Battery Level (%): 27.3 | Timestamp: 2021-01-27 11:15:46
<end>Here's some Markdown data, can you convert it to yml?
| Title | Rating |
| --- | --- |
| The Forgotten World | 3.8 |
| The Forgotten World | 2.8 |
| A Journey Through Time | 2.8 |
| Legends of the Rift | 2.0 |
| Shadows of Solitude | 4.8 |
| The Last Sky | 3.5 |<start>
- Rating: 3.8
  Title: The Forgotten World
- Rating: 2.8
  Title: The Forgotten World
- Rating: 2.8
  Title: A Journey Through Time
- Rating: 2.0
  Title: Legends of the Rift
- Rating: 4.8
  Title: Shadows of Solitude
- Rating: 3.5
  Title: The Last Sky
<end>Convert this Json to YAML:
[
    {
        "Title": "Beyond the Veil",
        "Director": "Zara Stormrider",
        "Genre": "Adventure",
        "Release Year": 1993,
        "Box Office Earnings (M)": 306.95
    },
    {
        "Title": "Beyond the Veil",
        "Director": "Aria Ravenwood",
        "Genre": "Action",
        "Release Year": 2013,
        "Box Office Earnings (M)": 315.62
    },
    {
        "Title": "The Great Expedition",
        "Director": "Selene Darkwhisper",
        "Genre": "Comedy",
        "Release Year": 1976,
        "Box Office Earnings (M)": 519.44
    },
    {
        "Title": "The Great Expedition",
        "Director": "Talon Blackthorn",
        "Genre": "Fantasy",
        "Release Year": 2003,
        "Box Office Earnings (M)": 36.99
    },
    {
        "Title": "The Great Expedition",
        "Director": "Selene Darkwhisper",
        "Genre": "Action",
        "Release Year": 1970,
        "Box Office Earnings (M)": 49.4
    },
    {
        "Title": "Dreamwalker",
        "Director": "Aria Ravenwood",
        "Genre": "Horror",
        "Release Year": 1993,
        "Box Office Earnings (M)": 762.22
    },
    {
        "Title": "Beyond the Veil",
        "Director": "Orin Shadowalker",
        "Genre": "Fantasy",
        "Release Year": 1983,
        "Box Office Earnings (M)": 428.63
    },
    {
        "Title": "Edge of Infinity",
        "Director": "Rylan Frostblade",
        "Genre": "Adventure",
        "Release Year": 1976,
        "Box Office Earnings (M)": 119.74
    }
]<start>
- Box Office Earnings (M): 306.95
  Director: Zara Stormrider
  Genre: Adventure
  Release Year: 1993
  Title: Beyond the Veil
- Box Office Earnings (M): 315.62
  Director: Aria Ravenwood
  Genre: Action
  Release Year: 2013
  Title: Beyond the Veil
- Box Office Earnings (M): 519.44
  Director: Selene Darkwhisper
  Genre: Comedy
  Release Year: 1976
  Title: The Great Expedition
- Box Office Earnings (M): 36.99
  Director: Talon Blackthorn
  Genre: Fantasy
  Release Year: 2003
  Title: The Great Expedition
- Box Office Earnings (M): 49.4
  Director: Selene Darkwhisper
  Genre: Action
  Release Year: 1970
  Title: The Great Expedition
- Box Office Earnings (M): 762.22
  Director: Aria Ravenwood
  Genre: Horror
  Release Year: 1993
  Title: Dreamwalker
- Box Office Earnings (M): 428.63
  Director: Orin Shadowalker
  Genre: Fantasy
  Release Year: 1983
  Title: Beyond the Veil
- Box Office Earnings (M): 119.74
  Director: Rylan Frostblade
  Genre: Adventure
  Release Year: 1976
  Title: Edge of Infinity
<end>Please transform the following yml data into JSON:
- Director: Mara Moonshadow
  Genre: Horror
  Release Year: 1989
  Title: Edge of Infinity
- Director: Orin Shadowalker
  Genre: Fantasy
  Release Year: 2005
  Title: The Final Voyage
- Director: Talon Blackthorn
  Genre: Horror
  Release Year: 2000
  Title: Rise of the Titans
<start>
[
    {
        "Title": "Edge of Infinity",
        "Director": "Mara Moonshadow",
        "Genre": "Horror",
        "Release Year": 1989
    },
    {
        "Title": "The Final Voyage",
        "Director": "Orin Shadowalker",
        "Genre": "Fantasy",
        "Release Year": 2005
    },
    {
        "Title": "Rise of the Titans",
        "Director": "Talon Blackthorn",
        "Genre": "Horror",
        "Release Year": 2000
    }
]
<end>Here's some json data, can you convert it to plain text?
[
    {
        "Cache Hit Ratio (%)": 98.79,
        "Connection Count": 81,
        "Timestamp": "2023-09-04 17:26:17"
    },
    {
        "Cache Hit Ratio (%)": 92.56,
        "Connection Count": 99,
        "Timestamp": "2021-05-12 19:45:00"
    },
    {
        "Cache Hit Ratio (%)": 73.18,
        "Connection Count": 100,
        "Timestamp": "2022-06-07 10:03:21"
    },
    {
        "Cache Hit Ratio (%)": 72.09,
        "Connection Count": 63,
        "Timestamp": "2023-08-21 04:14:16"
    },
    {
        "Cache Hit Ratio (%)": 90.67,
        "Connection Count": 361,
        "Timestamp": "2023-05-28 14:17:09"
    },
    {
        "Cache Hit Ratio (%)": 95.98,
        "Connection Count": 71,
        "Timestamp": "2023-11-09 05:50:06"
    },
    {
        "Cache Hit Ratio (%)": 74.01,
        "Connection Count": 326,
        "Timestamp": "2021-02-18 20:30:57"
    }
]<start>
Cache Hit Ratio (%): 98.79 | Connection Count: 81 | Timestamp: 2023-09-04 17:26:17
Cache Hit Ratio (%): 92.56 | Connection Count: 99 | Timestamp: 2021-05-12 19:45:00
Cache Hit Ratio (%): 73.18 | Connection Count: 100 | Timestamp: 2022-06-07 10:03:21
Cache Hit Ratio (%): 72.09 | Connection Count: 63 | Timestamp: 2023-08-21 04:14:16
Cache Hit Ratio (%): 90.67 | Connection Count: 361 | Timestamp: 2023-05-28 14:17:09
Cache Hit Ratio (%): 95.98 | Connection Count: 71 | Timestamp: 2023-11-09 05:50:06
Cache Hit Ratio (%): 74.01 | Connection Count: 326 | Timestamp: 2021-02-18 20:30:57
<end>Can you change this json into Plain text?
[
    {
        "Trip Name": "City Explorer",
        "Start Location": "New York",
        "End Location": "Miami",
        "Distance (miles)": 2717.8,
        "Duration (hours)": 63.8,
        "Fuel Used (gallons)": 29.3
    },
    {
        "Trip Name": "Historic Route",
        "Start Location": "Miami",
        "End Location": "Houston",
        "Distance (miles)": 736.7,
        "Duration (hours)": 4.6,
        "Fuel Used (gallons)": 29.3
    },
    {
        "Trip Name": "City Explorer",
        "Start Location": "New York",
        "End Location": "Los Angeles",
        "Distance (miles)": 2589.5,
        "Duration (hours)": 69.5,
        "Fuel Used (gallons)": 82.1
    },
    {
        "Trip Name": "Coast to Coast",
        "Start Location": "Houston",
        "End Location": "Miami",
        "Distance (miles)": 2404.2,
        "Duration (hours)": 27.6,
        "Fuel Used (gallons)": 77.2
    },
    {
        "Trip Name": "Historic Route",
        "Start Location": "Los Angeles",
        "End Location": "Phoenix",
        "Distance (miles)": 936.2,
        "Duration (hours)": 11.8,
        "Fuel Used (gallons)": 56.4
    },
    {
        "Trip Name": "City Explorer",
        "Start Location": "Los Angeles",
        "End Location": "Houston",
        "Distance (miles)": 1715.4,
        "Duration (hours)": 10.8,
        "Fuel Used (gallons)": 69.0
    },
    {
        "Trip Name": "Valley Voyage",
        "Start Location": "Los Angeles",
        "End Location": "Denver",
        "Distance (miles)": 2051.0,
        "Duration (hours)": 33.4,
        "Fuel Used (gallons)": 90.8
    }
]<start>
Trip Name: City Explorer | Start Location: New York | End Location: Miami | Distance (miles): 2717.8 | Duration (hours): 63.8 | Fuel Used (gallons): 29.3
Trip Name: Historic Route | Start Location: Miami | End Location: Houston | Distance (miles): 736.7 | Duration (hours): 4.6 | Fuel Used (gallons): 29.3
Trip Name: City Explorer | Start Location: New York | End Location: Los Angeles | Distance (miles): 2589.5 | Duration (hours): 69.5 | Fuel Used (gallons): 82.1
Trip Name: Coast to Coast | Start Location: Houston | End Location: Miami | Distance (miles): 2404.2 | Duration (hours): 27.6 | Fuel Used (gallons): 77.2
Trip Name: Historic Route | Start Location: Los Angeles | End Location: Phoenix | Distance (miles): 936.2 | Duration (hours): 11.8 | Fuel Used (gallons): 56.4
Trip Name: City Explorer | Start Location: Los Angeles | End Location: Houston | Distance (miles): 1715.4 | Duration (hours): 10.8 | Fuel Used (gallons): 69.0
Trip Name: Valley Voyage | Start Location: Los Angeles | End Location: Denver | Distance (miles): 2051.0 | Duration (hours): 33.4 | Fuel Used (gallons): 90.8
<end>Can you change this csv into plain text?
Title,Author
The Last Sky,Kara Firebrand
The Forgotten World,Sylvia Nightshade
The Silent Grove,Luna Silverleaf
Tales of the Brave,Orion Frostblade
The Forgotten World,Draven Blackthorn
A Journey Through Time,Galen Starfire
The Crystal Key,Orion Frostblade
<start>
Title: The Last Sky | Author: Kara Firebrand
Title: The Forgotten World | Author: Sylvia Nightshade
Title: The Silent Grove | Author: Luna Silverleaf
Title: Tales of the Brave | Author: Orion Frostblade
Title: The Forgotten World | Author: Draven Blackthorn
Title: A Journey Through Time | Author: Galen Starfire
Title: The Crystal Key | Author: Orion Frostblade
<end>Can you change this Markdown into csv?
| Location | Condition | Temperature (C) | Wind Speed (km/h) | Day |
| --- | --- | --- | --- | --- |
| Miami | Rainy | 20.4 | 10.8 | Thursday |
| Houston | Stormy | 8.3 | 2.3 | Saturday |
| Denver | Cloudy | 18.6 | 24.1 | Friday |<start>
Location,Condition,Temperature (C),Wind Speed (km/h),Day
Miami,Rainy,20.4,10.8,Thursday
Houston,Stormy,8.3,2.3,Saturday
Denver,Cloudy,18.6,24.1,Friday
<end>Convert this yml to csv:
- Director: Talon Blackthorn
  Release Year: 1984
  Title: Rise of the Titans
- Director: Mara Moonshadow
  Release Year: 2015
  Title: Dreamwalker
- Director: Zara Stormrider
  Release Year: 1984
  Title: The Final Voyage
- Director: Zara Stormrider
  Release Year: 1976
  Title: Rise of the Titans
<start>
Title,Director,Release Year
Rise of the Titans,Talon Blackthorn,1984
Dreamwalker,Mara Moonshadow,2015
The Final Voyage,Zara Stormrider,1984
Rise of the Titans,Zara Stormrider,1976
<end>Transform this yml structure to a MARKDOWN format:
- Company: FinanceWorks
  Sector: Energy
  Stock Price: 99.29
- Company: EcoEnergy
  Sector: Retail
  Stock Price: 462.9
- Company: AutoDrive
  Sector: Healthcare
  Stock Price: 189.87
- Company: TechCorp
  Sector: Technology
  Stock Price: 904.51
<start>
| Company | Sector | Stock Price |
| --- | --- | --- |
| FinanceWorks | Energy | 99.29 |
| EcoEnergy | Retail | 462.9 |
| AutoDrive | Healthcare | 189.87 |
| TechCorp | Technology | 904.51 |
<end>Convert this MARKDOWN to Plain text:
| Restaurant Name | Price Range |
| --- | --- |
| The Golden Spoon | $$ |
| Burger Haven | $$$$$ |
| Pizza Planet | $$$$ |<start>
Restaurant Name: The Golden Spoon | Price Range: $$
Restaurant Name: Burger Haven | Price Range: $$$$$
Restaurant Name: Pizza Planet | Price Range: $$$$
<end>Here's some markdown data, can you convert it to json?
| Name | Age | Birth Month | Income |
| --- | --- | --- | --- |
| Sophia | 68 | July | 345000 |
| Don | 28 | November | 115000 |
| Thomas | 39 | September | 85000 |
| Verna | 65 | June | 225000 |
| Earl | 38 | July | 90000 |
| Edgar | 41 | January | 295000 |
| Dawn | 49 | June | 125000 |
| Aiden | 35 | March | 40000 |<start>
[
    {
        "Name": "Sophia",
        "Age": 68,
        "Birth Month": "July",
        "Income": 345000
    },
    {
        "Name": "Don",
        "Age": 28,
        "Birth Month": "November",
        "Income": 115000
    },
    {
        "Name": "Thomas",
        "Age": 39,
        "Birth Month": "September",
        "Income": 85000
    },
    {
        "Name": "Verna",
        "Age": 65,
        "Birth Month": "June",
        "Income": 225000
    },
    {
        "Name": "Earl",
        "Age": 38,
        "Birth Month": "July",
        "Income": 90000
    },
    {
        "Name": "Edgar",
        "Age": 41,
        "Birth Month": "January",
        "Income": 295000
    },
    {
        "Name": "Dawn",
        "Age": 49,
        "Birth Month": "June",
        "Income": 125000
    },
    {
        "Name": "Aiden",
        "Age": 35,
        "Birth Month": "March",
        "Income": 40000
    }
]
<end>Here's some csv data, can you convert it to Json?
Location,Temperature (C),Humidity (%),Wind Speed (km/h)
Miami,-6.5,82,26.7
Los Angeles,18.6,66,22.6
Houston,-3.8,57,28.7
Denver,-9.3,21,7.9
<start>
[
    {
        "Location": "Miami",
        "Temperature (C)": -6.5,
        "Humidity (%)": 82,
        "Wind Speed (km/h)": 26.7
    },
    {
        "Location": "Los Angeles",
        "Temperature (C)": 18.6,
        "Humidity (%)": 66,
        "Wind Speed (km/h)": 22.6
    },
    {
        "Location": "Houston",
        "Temperature (C)": -3.8,
        "Humidity (%)": 57,
        "Wind Speed (km/h)": 28.7
    },
    {
        "Location": "Denver",
        "Temperature (C)": -9.3,
        "Humidity (%)": 21,
        "Wind Speed (km/h)": 7.9
    }
]
<end>Transform this Plain text structure to a markdown format:
Name: Cody | Age: 20 | Birth Month: December | City: Charlotte | Income: 200000
Name: Paulette | Age: 49 | Birth Month: November | City: Las Vegas | Income: 290000
Name: Harriet | Age: 32 | Birth Month: June | City: San Francisco | Income: 235000
Name: June | Age: 30 | Birth Month: October | City: San Antonio | Income: 485000
Name: Carson | Age: 23 | Birth Month: September | City: El Paso | Income: 375000
Name: Allison | Age: 53 | Birth Month: February | City: San Diego | Income: 145000
Name: Reese | Age: 25 | Birth Month: November | City: Portland | Income: 350000
Name: Arnold | Age: 49 | Birth Month: January | City: Columbus | Income: 160000
<start>
| Name | Age | Birth Month | City | Income |
| --- | --- | --- | --- | --- |
| Cody | 20 | December | Charlotte | 200000 |
| Paulette | 49 | November | Las Vegas | 290000 |
| Harriet | 32 | June | San Francisco | 235000 |
| June | 30 | October | San Antonio | 485000 |
| Carson | 23 | September | El Paso | 375000 |
| Allison | 53 | February | San Diego | 145000 |
| Reese | 25 | November | Portland | 350000 |
| Arnold | 49 | January | Columbus | 160000 |
<end>Can you change this yml into csv?
- Close Price: 598.27
  Company: BioLife
  Date: '2011-10-28'
  High Price: 928.6
  Low Price: 598.27
  Open Price: 928.6
  Volume: 2032168
- Close Price: 215.37
  Company: BioLife
  Date: '2019-10-12'
  High Price: 1226.63
  Low Price: 215.37
  Open Price: 249.81
  Volume: 2003744
- Close Price: 1038.28
  Company: BioLife
  Date: '2018-11-15'
  High Price: 1038.28
  Low Price: 677.39
  Open Price: 786.2
  Volume: 3511625
- Close Price: 13.06
  Company: RetailWorld
  Date: '2010-04-15'
  High Price: 1374.49
  Low Price: 13.06
  Open Price: 1374.49
  Volume: 221313
- Close Price: 142.68
  Company: GreenEnergy
  Date: '2019-07-10'
  High Price: 1038.28
  Low Price: 130.11
  Open Price: 130.11
  Volume: 3511625
- Close Price: 244.29
  Company: TechnoCorp
  Date: '2015-06-10'
  High Price: 299.76
  Low Price: 244.29
  Open Price: 249.81
  Volume: 8063915
<start>
Company,Date,Open Price,Close Price,High Price,Low Price,Volume
BioLife,2011-10-28,928.6,598.27,928.6,598.27,2032168
BioLife,2019-10-12,249.81,215.37,1226.63,215.37,2003744
BioLife,2018-11-15,786.2,1038.28,1038.28,677.39,3511625
RetailWorld,2010-04-15,1374.49,13.06,1374.49,13.06,221313
GreenEnergy,2019-07-10,130.11,142.68,1038.28,130.11,3511625
TechnoCorp,2015-06-10,249.81,244.29,299.76,244.29,8063915
<end>Convert this markdown to CSV:
| Title | Author | Genre | Publication Year | Rating |
| --- | --- | --- | --- | --- |
| The Crystal Key | Orion Frostblade | Mystery | 1996 | 3.6 |
| Whispers of the Abyss | Luna Silverleaf | Romance | 1979 | 4.6 |
| The Silent Grove | Draven Blackthorn | Non-Fiction | 1969 | 2.6 |
| The Silent Grove | Elara Moonshadow | Science Fiction | 1992 | 1.2 |
| Whispers of the Abyss | Orion Frostblade | Mystery | 1978 | 3.8 |
| The Crystal Key | Draven Blackthorn | Horror | 1987 | 1.1 |
| Echoes of Eternity | Orion Frostblade | Romance | 1976 | 4.3 |
| The Forgotten World | Thorne Ironwood | Non-Fiction | 1967 | 1.5 |<start>
Title,Author,Genre,Publication Year,Rating
The Crystal Key,Orion Frostblade,Mystery,1996,3.6
Whispers of the Abyss,Luna Silverleaf,Romance,1979,4.6
The Silent Grove,Draven Blackthorn,Non-Fiction,1969,2.6
The Silent Grove,Elara Moonshadow,Science Fiction,1992,1.2
Whispers of the Abyss,Orion Frostblade,Mystery,1978,3.8
The Crystal Key,Draven Blackthorn,Horror,1987,1.1
Echoes of Eternity,Orion Frostblade,Romance,1976,4.3
The Forgotten World,Thorne Ironwood,Non-Fiction,1967,1.5
<end>Please transform the following csv data into markdown:
Product Name,SKU,Stock Quantity,Category
Doohickey,SKU-1019,179,Household
Device,SKU-1060,139,Sports
Widget,SKU-1010,316,Electronics
<start>
| Product Name | SKU | Stock Quantity | Category |
| --- | --- | --- | --- |
| Doohickey | SKU-1019 | 179 | Household |
| Device | SKU-1060 | 139 | Sports |
| Widget | SKU-1010 | 316 | Electronics |
<end>Please transform the following plain text data into yml:
Company: AutoMotive | Date: 2011-12-05 | Open Price: 1484.98 | High Price: 1484.98 | Low Price: 127.83 | Volume: 4994610
Company: AeroSystems | Date: 2023-10-27 | Open Price: 1046.15 | High Price: 1470.86 | Low Price: 1046.15 | Volume: 7269988
Company: TechnoCorp | Date: 2014-02-28 | Open Price: 104.68 | High Price: 1056.05 | Low Price: 104.68 | Volume: 6038456
Company: FinanceTrust | Date: 2021-10-19 | Open Price: 430.61 | High Price: 1414.68 | Low Price: 20.25 | Volume: 8935484
<start>
- Company: AutoMotive
  Date: '2011-12-05'
  High Price: 1484.98
  Low Price: 127.83
  Open Price: 1484.98
  Volume: 4994610
- Company: AeroSystems
  Date: '2023-10-27'
  High Price: 1470.86
  Low Price: 1046.15
  Open Price: 1046.15
  Volume: 7269988
- Company: TechnoCorp
  Date: '2014-02-28'
  High Price: 1056.05
  Low Price: 104.68
  Open Price: 104.68
  Volume: 6038456
- Company: FinanceTrust
  Date: '2021-10-19'
  High Price: 1414.68
  Low Price: 20.25
  Open Price: 430.61
  Volume: 8935484
<end>Can you change this MARKDOWN into plain text?
| Trip Name | Start Location | End Location | Distance (miles) | Duration (hours) | Fuel Used (gallons) |
| --- | --- | --- | --- | --- | --- |
| Highway Odyssey | Phoenix | New York | 629.5 | 60.0 | 5.7 |
| Canyon Trek | Miami | San Francisco | 1659.9 | 38.7 | 47.4 |
| Valley Voyage | Chicago | Houston | 2894.9 | 39.4 | 44.3 |
| Forest Journey | Miami | New York | 560.8 | 26.8 | 54.6 |
| Desert Drive | Los Angeles | Denver | 1134.0 | 36.1 | 5.7 |<start>
Trip Name: Highway Odyssey | Start Location: Phoenix | End Location: New York | Distance (miles): 629.5 | Duration (hours): 60.0 | Fuel Used (gallons): 5.7
Trip Name: Canyon Trek | Start Location: Miami | End Location: San Francisco | Distance (miles): 1659.9 | Duration (hours): 38.7 | Fuel Used (gallons): 47.4
Trip Name: Valley Voyage | Start Location: Chicago | End Location: Houston | Distance (miles): 2894.9 | Duration (hours): 39.4 | Fuel Used (gallons): 44.3
Trip Name: Forest Journey | Start Location: Miami | End Location: New York | Distance (miles): 560.8 | Duration (hours): 26.8 | Fuel Used (gallons): 54.6
Trip Name: Desert Drive | Start Location: Los Angeles | End Location: Denver | Distance (miles): 1134.0 | Duration (hours): 36.1 | Fuel Used (gallons): 5.7
<end>Can you change this markdown into Yaml?
| SKU | Price | Stock Quantity | Category |
| --- | --- | --- | --- |
| SKU-1026 | 53.35 | 55 | Automotive |
| SKU-1090 | 493.46 | 197 | Household |
| SKU-1046 | 125.86 | 216 | Household |
| SKU-1013 | 106.26 | 87 | Electronics |
| SKU-1085 | 82.05 | 4 | Toys |
| SKU-1099 | 277.85 | 91 | Household |
| SKU-1014 | 74.93 | 55 | Electronics |
| SKU-1077 | 221.24 | 479 | Household |
| SKU-1008 | 423.5 | 457 | Electronics |
| SKU-1080 | 427.85 | 412 | Automotive |<start>
- Category: Automotive
  Price: 53.35
  SKU: SKU-1026
  Stock Quantity: 55
- Category: Household
  Price: 493.46
  SKU: SKU-1090
  Stock Quantity: 197
- Category: Household
  Price: 125.86
  SKU: SKU-1046
  Stock Quantity: 216
- Category: Electronics
  Price: 106.26
  SKU: SKU-1013
  Stock Quantity: 87
- Category: Toys
  Price: 82.05
  SKU: SKU-1085
  Stock Quantity: 4
- Category: Household
  Price: 277.85
  SKU: SKU-1099
  Stock Quantity: 91
- Category: Electronics
  Price: 74.93
  SKU: SKU-1014
  Stock Quantity: 55
- Category: Household
  Price: 221.24
  SKU: SKU-1077
  Stock Quantity: 479
- Category: Electronics
  Price: 423.5
  SKU: SKU-1008
  Stock Quantity: 457
- Category: Automotive
  Price: 427.85
  SKU: SKU-1080
  Stock Quantity: 412
<end>Here's some csv data, can you convert it to MARKDOWN?
Device ID,Battery Level (%),Reading Value,Timestamp
device-0058,77.1,55.13,2023-11-04 13:19:48
device-0046,31.7,31.04,2022-02-27 08:51:46
device-0016,46.9,72.77,2021-08-12 19:45:15
device-0029,90.3,19.89,2023-12-13 04:48:06
device-0036,43.5,21.51,2021-09-23 05:32:47
device-0021,34.9,-11.98,2023-02-21 03:58:46
<start>
| Device ID | Battery Level (%) | Reading Value | Timestamp |
| --- | --- | --- | --- |
| device-0058 | 77.1 | 55.13 | 2023-11-04 13:19:48 |
| device-0046 | 31.7 | 31.04 | 2022-02-27 08:51:46 |
| device-0016 | 46.9 | 72.77 | 2021-08-12 19:45:15 |
| device-0029 | 90.3 | 19.89 | 2023-12-13 04:48:06 |
| device-0036 | 43.5 | 21.51 | 2021-09-23 05:32:47 |
| device-0021 | 34.9 | -11.98 | 2023-02-21 03:58:46 |
<end>Convert this JSON to PLAIN TEXT:
[
    {
        "Location": "Los Angeles",
        "Condition": "Snowy",
        "Temperature (C)": 12.5,
        "Humidity (%)": 62
    },
    {
        "Location": "Phoenix",
        "Condition": "Windy",
        "Temperature (C)": 23.5,
        "Humidity (%)": 95
    },
    {
        "Location": "Chicago",
        "Condition": "Rainy",
        "Temperature (C)": -8.4,
        "Humidity (%)": 63
    },
    {
        "Location": "Chicago",
        "Condition": "Windy",
        "Temperature (C)": 38.8,
        "Humidity (%)": 45
    }
]<start>
Location: Los Angeles | Condition: Snowy | Temperature (C): 12.5 | Humidity (%): 62
Location: Phoenix | Condition: Windy | Temperature (C): 23.5 | Humidity (%): 95
Location: Chicago | Condition: Rainy | Temperature (C): -8.4 | Humidity (%): 63
Location: Chicago | Condition: Windy | Temperature (C): 38.8 | Humidity (%): 45
<end>Transform this csv structure to a MARKDOWN format:
Device ID,Location,Battery Level (%),Timestamp
device-0004,Office,62.7,2021-09-01 07:07:09
device-0021,Bathroom,41.8,2022-02-11 16:37:44
device-0055,Living Room,23.6,2023-12-14 04:17:48
device-0060,Living Room,55.2,2021-06-25 12:37:20
device-0043,Garden,75.0,2021-03-17 12:30:43
device-0098,Kitchen,33.2,2021-07-26 07:20:20
device-0080,Garden,62.7,2021-12-18 15:52:32
device-0082,Bedroom,68.1,2022-05-01 14:34:55
device-0059,Bedroom,74.3,2021-10-22 23:13:52
device-0086,Kitchen,44.3,2022-07-25 13:30:54
<start>
| Device ID | Location | Battery Level (%) | Timestamp |
| --- | --- | --- | --- |
| device-0004 | Office | 62.7 | 2021-09-01 07:07:09 |
| device-0021 | Bathroom | 41.8 | 2022-02-11 16:37:44 |
| device-0055 | Living Room | 23.6 | 2023-12-14 04:17:48 |
| device-0060 | Living Room | 55.2 | 2021-06-25 12:37:20 |
| device-0043 | Garden | 75.0 | 2021-03-17 12:30:43 |
| device-0098 | Kitchen | 33.2 | 2021-07-26 07:20:20 |
| device-0080 | Garden | 62.7 | 2021-12-18 15:52:32 |
| device-0082 | Bedroom | 68.1 | 2022-05-01 14:34:55 |
| device-0059 | Bedroom | 74.3 | 2021-10-22 23:13:52 |
| device-0086 | Kitchen | 44.3 | 2022-07-25 13:30:54 |
<end>Transform this csv structure to a yaml format:
Temperature (C),Humidity (%),Day
17.4,56,Friday
33.9,26,Tuesday
33.9,40,Friday
-7.6,56,Saturday
11.3,88,Saturday
-7.6,90,Sunday
29.1,68,Saturday
3.5,80,Thursday
-9.3,28,Sunday
13.2,65,Saturday
<start>
- Day: Friday
  Humidity (%): 56
  Temperature (C): 17.4
- Day: Tuesday
  Humidity (%): 26
  Temperature (C): 33.9
- Day: Friday
  Humidity (%): 40
  Temperature (C): 33.9
- Day: Saturday
  Humidity (%): 56
  Temperature (C): -7.6
- Day: Saturday
  Humidity (%): 88
  Temperature (C): 11.3
- Day: Sunday
  Humidity (%): 90
  Temperature (C): -7.6
- Day: Saturday
  Humidity (%): 68
  Temperature (C): 29.1
- Day: Thursday
  Humidity (%): 80
  Temperature (C): 3.5
- Day: Sunday
  Humidity (%): 28
  Temperature (C): -9.3
- Day: Saturday
  Humidity (%): 65
  Temperature (C): 13.2
<end>Here's some markdown data, can you convert it to JSON?
| Database Name | Queries per Second | Cache Hit Ratio (%) | Average Latency (ms) | Timestamp |
| --- | --- | --- | --- | --- |
| MetricsDB | 2920.31 | 99.1 | 35.94 | 2022-05-19 05:11:27 |
| MetricsDB | 1205.94 | 88.07 | 47.21 | 2023-02-07 02:11:38 |
| MetricsDB | 3326.85 | 83.56 | 89.57 | 2022-12-23 06:37:45 |
| UserDB | 4708.69 | 98.05 | 13.77 | 2021-01-04 11:28:08 |
| SessionsDB | 4343.53 | 74.19 | 5.63 | 2023-01-18 09:34:40 |
| InventoryDB | 3029.04 | 99.1 | 71.74 | 2022-01-24 01:50:46 |<start>
[
    {
        "Database Name": "MetricsDB",
        "Queries per Second": 2920.31,
        "Cache Hit Ratio (%)": 99.1,
        "Average Latency (ms)": 35.94,
        "Timestamp": "2022-05-19 05:11:27"
    },
    {
        "Database Name": "MetricsDB",
        "Queries per Second": 1205.94,
        "Cache Hit Ratio (%)": 88.07,
        "Average Latency (ms)": 47.21,
        "Timestamp": "2023-02-07 02:11:38"
    },
    {
        "Database Name": "MetricsDB",
        "Queries per Second": 3326.85,
        "Cache Hit Ratio (%)": 83.56,
        "Average Latency (ms)": 89.57,
        "Timestamp": "2022-12-23 06:37:45"
    },
    {
        "Database Name": "UserDB",
        "Queries per Second": 4708.69,
        "Cache Hit Ratio (%)": 98.05,
        "Average Latency (ms)": 13.77,
        "Timestamp": "2021-01-04 11:28:08"
    },
    {
        "Database Name": "SessionsDB",
        "Queries per Second": 4343.53,
        "Cache Hit Ratio (%)": 74.19,
        "Average Latency (ms)": 5.63,
        "Timestamp": "2023-01-18 09:34:40"
    },
    {
        "Database Name": "InventoryDB",
        "Queries per Second": 3029.04,
        "Cache Hit Ratio (%)": 99.1,
        "Average Latency (ms)": 71.74,
        "Timestamp": "2022-01-24 01:50:46"
    }
]
<end>Please transform the following PLAIN TEXT data into JSON:
Location: New York | Condition: Snowy | Temperature (C): -4.6 | Humidity (%): 51 | Day: Saturday
Location: Houston | Condition: Snowy | Temperature (C): 24.4 | Humidity (%): 79 | Day: Saturday
Location: New York | Condition: Foggy | Temperature (C): 8.4 | Humidity (%): 88 | Day: Wednesday
Location: Phoenix | Condition: Sunny | Temperature (C): 0.2 | Humidity (%): 33 | Day: Monday
<start>
[
    {
        "Location": "New York",
        "Condition": "Snowy",
        "Temperature (C)": -4.6,
        "Humidity (%)": 51,
        "Day": "Saturday"
    },
    {
        "Location": "Houston",
        "Condition": "Snowy",
        "Temperature (C)": 24.4,
        "Humidity (%)": 79,
        "Day": "Saturday"
    },
    {
        "Location": "New York",
        "Condition": "Foggy",
        "Temperature (C)": 8.4,
        "Humidity (%)": 88,
        "Day": "Wednesday"
    },
    {
        "Location": "Phoenix",
        "Condition": "Sunny",
        "Temperature (C)": 0.2,
        "Humidity (%)": 33,
        "Day": "Monday"
    }
]
<end>Please transform the following markdown data into plain text:
| Market Cap | Stock Price | Annual Revenue (B) |
| --- | --- | --- |
| Mega Cap | 955.38 | 83.53 |
| Large Cap | 134.12 | 85.88 |
| Large Cap | 941.9 | 66.31 |<start>
Market Cap: Mega Cap | Stock Price: 955.38 | Annual Revenue (B): 83.53
Market Cap: Large Cap | Stock Price: 134.12 | Annual Revenue (B): 85.88
Market Cap: Large Cap | Stock Price: 941.9 | Annual Revenue (B): 66.31
<end>Here's some Json data, can you convert it to csv?
[
    {
        "Device ID": "device-0054",
        "Device Type": "Humidity Sensor",
        "Location": "Kitchen",
        "Battery Level (%)": 92.4,
        "Reading Value": -14.1,
        "Timestamp": "2021-11-07 06:17:49"
    },
    {
        "Device ID": "device-0023",
        "Device Type": "Light Sensor",
        "Location": "Living Room",
        "Battery Level (%)": 41.7,
        "Reading Value": -23.95,
        "Timestamp": "2021-07-17 22:34:13"
    },
    {
        "Device ID": "device-0057",
        "Device Type": "Temperature Sensor",
        "Location": "Office",
        "Battery Level (%)": 15.4,
        "Reading Value": 14.45,
        "Timestamp": "2021-09-22 00:09:10"
    },
    {
        "Device ID": "device-0049",
        "Device Type": "Light Sensor",
        "Location": "Hallway",
        "Battery Level (%)": 35.7,
        "Reading Value": -16.79,
        "Timestamp": "2021-10-08 15:48:12"
    }
]<start>
Device ID,Device Type,Location,Battery Level (%),Reading Value,Timestamp
device-0054,Humidity Sensor,Kitchen,92.4,-14.1,2021-11-07 06:17:49
device-0023,Light Sensor,Living Room,41.7,-23.95,2021-07-17 22:34:13
device-0057,Temperature Sensor,Office,15.4,14.45,2021-09-22 00:09:10
device-0049,Light Sensor,Hallway,35.7,-16.79,2021-10-08 15:48:12
<end>Here's some JSON data, can you convert it to PLAIN TEXT?
[
    {
        "Title": "Whispers of the Abyss",
        "Publication Year": 1989,
        "Rating": 4.0
    },
    {
        "Title": "The Silent Grove",
        "Publication Year": 1961,
        "Rating": 3.4
    },
    {
        "Title": "The Last Sky",
        "Publication Year": 1966,
        "Rating": 3.4
    },
    {
        "Title": "Shadows of Solitude",
        "Publication Year": 2017,
        "Rating": 3.8
    },
    {
        "Title": "The Crystal Key",
        "Publication Year": 1968,
        "Rating": 3.6
    },
    {
        "Title": "The Last Sky",
        "Publication Year": 2017,
        "Rating": 1.4
    }
]<start>
Title: Whispers of the Abyss | Publication Year: 1989 | Rating: 4.0
Title: The Silent Grove | Publication Year: 1961 | Rating: 3.4
Title: The Last Sky | Publication Year: 1966 | Rating: 3.4
Title: Shadows of Solitude | Publication Year: 2017 | Rating: 3.8
Title: The Crystal Key | Publication Year: 1968 | Rating: 3.6
Title: The Last Sky | Publication Year: 2017 | Rating: 1.4
<end>Please transform the following csv data into markdown:
Location,Battery Level (%),Timestamp
Office,81.1,2021-10-05 09:05:13
Kitchen,95.0,2021-12-17 17:23:09
Office,28.6,2023-12-02 20:45:19
Kitchen,34.0,2023-11-09 10:36:57
Kitchen,25.7,2022-03-05 02:28:16
Garden,89.3,2021-08-12 15:05:42
<start>
| Location | Battery Level (%) | Timestamp |
| --- | --- | --- |
| Office | 81.1 | 2021-10-05 09:05:13 |
| Kitchen | 95.0 | 2021-12-17 17:23:09 |
| Office | 28.6 | 2023-12-02 20:45:19 |
| Kitchen | 34.0 | 2023-11-09 10:36:57 |
| Kitchen | 25.7 | 2022-03-05 02:28:16 |
| Garden | 89.3 | 2021-08-12 15:05:42 |
<end>Please transform the following json data into Plain text:
[
    {
        "Cuisine": "Japanese",
        "Rating": 4,
        "Price Range": "$$$$"
    },
    {
        "Cuisine": "Italian",
        "Rating": 4,
        "Price Range": "$$$$"
    },
    {
        "Cuisine": "Italian",
        "Rating": 1,
        "Price Range": "$$$"
    },
    {
        "Cuisine": "American",
        "Rating": 4,
        "Price Range": "$"
    },
    {
        "Cuisine": "Mexican",
        "Rating": 2,
        "Price Range": "$$$$$"
    }
]<start>
Cuisine: Japanese | Rating: 4 | Price Range: $$$$
Cuisine: Italian | Rating: 4 | Price Range: $$$$
Cuisine: Italian | Rating: 1 | Price Range: $$$
Cuisine: American | Rating: 4 | Price Range: $
Cuisine: Mexican | Rating: 2 | Price Range: $$$$$
<end>Convert this MARKDOWN to plain text:
| Location | Condition | Temperature (C) | Humidity (%) | Day |
| --- | --- | --- | --- | --- |
| Los Angeles | Rainy | -9.2 | 37 | Monday |
| Phoenix | Windy | -1.0 | 28 | Tuesday |
| Chicago | Sunny | 20.1 | 86 | Tuesday |
| Los Angeles | Rainy | 35.3 | 75 | Wednesday |
| Denver | Stormy | -1.0 | 41 | Thursday |
| Chicago | Windy | 17.5 | 46 | Sunday |
| Miami | Stormy | 16.2 | 85 | Saturday |
| Chicago | Cloudy | 3.7 | 57 | Friday |
| Houston | Stormy | 22.2 | 64 | Monday |
| Los Angeles | Cloudy | 17.6 | 50 | Sunday |<start>
Location: Los Angeles | Condition: Rainy | Temperature (C): -9.2 | Humidity (%): 37 | Day: Monday
Location: Phoenix | Condition: Windy | Temperature (C): -1.0 | Humidity (%): 28 | Day: Tuesday
Location: Chicago | Condition: Sunny | Temperature (C): 20.1 | Humidity (%): 86 | Day: Tuesday
Location: Los Angeles | Condition: Rainy | Temperature (C): 35.3 | Humidity (%): 75 | Day: Wednesday
Location: Denver | Condition: Stormy | Temperature (C): -1.0 | Humidity (%): 41 | Day: Thursday
Location: Chicago | Condition: Windy | Temperature (C): 17.5 | Humidity (%): 46 | Day: Sunday
Location: Miami | Condition: Stormy | Temperature (C): 16.2 | Humidity (%): 85 | Day: Saturday
Location: Chicago | Condition: Cloudy | Temperature (C): 3.7 | Humidity (%): 57 | Day: Friday
Location: Houston | Condition: Stormy | Temperature (C): 22.2 | Humidity (%): 64 | Day: Monday
Location: Los Angeles | Condition: Cloudy | Temperature (C): 17.6 | Humidity (%): 50 | Day: Sunday
<end>Please transform the following markdown data into yaml:
| Company | Sector | Market Cap | Stock Price |
| --- | --- | --- | --- |
| HealthPlus | Biotech | Large Cap | 855.55 |
| BioPharm | Biotech | Small Cap | 40.51 |
| BioPharm | Finance | Mega Cap | 568.36 |
| GlobalTrade | Energy | Mid Cap | 903.04 |<start>
- Company: HealthPlus
  Market Cap: Large Cap
  Sector: Biotech
  Stock Price: 855.55
- Company: BioPharm
  Market Cap: Small Cap
  Sector: Biotech
  Stock Price: 40.51
- Company: BioPharm
  Market Cap: Mega Cap
  Sector: Finance
  Stock Price: 568.36
- Company: GlobalTrade
  Market Cap: Mid Cap
  Sector: Energy
  Stock Price: 903.04
<end>Here's some Csv data, can you convert it to Json?
Company,Sector,Market Cap,Stock Price,Annual Revenue (B),Quarter
GlobalTrade,Technology,Small Cap,890.55,151.55,Q4
Foodies,Finance,Mid Cap,649.4,72.72,Q3
Foodies,Aerospace,Large Cap,355.6,76.46,Q4
<start>
[
    {
        "Company": "GlobalTrade",
        "Sector": "Technology",
        "Market Cap": "Small Cap",
        "Stock Price": 890.55,
        "Annual Revenue (B)": 151.55,
        "Quarter": "Q4"
    },
    {
        "Company": "Foodies",
        "Sector": "Finance",
        "Market Cap": "Mid Cap",
        "Stock Price": 649.4,
        "Annual Revenue (B)": 72.72,
        "Quarter": "Q3"
    },
    {
        "Company": "Foodies",
        "Sector": "Aerospace",
        "Market Cap": "Large Cap",
        "Stock Price": 355.6,
        "Annual Revenue (B)": 76.46,
        "Quarter": "Q4"
    }
]
<end>Please transform the following markdown data into json:
| Location | Condition | Wind Speed (km/h) | Day |
| --- | --- | --- | --- |
| Miami | Cloudy | 24.2 | Saturday |
| New York | Rainy | 26.8 | Monday |
| Houston | Rainy | 12.1 | Monday |
| Denver | Sunny | 9.0 | Sunday |
| Miami | Windy | 21.9 | Saturday |
| Seattle | Snowy | 28.6 | Tuesday |
| Los Angeles | Stormy | 18.5 | Wednesday |
| Phoenix | Cloudy | 14.1 | Monday |
| New York | Sunny | 15.7 | Friday |<start>
[
    {
        "Location": "Miami",
        "Condition": "Cloudy",
        "Wind Speed (km/h)": 24.2,
        "Day": "Saturday"
    },
    {
        "Location": "New York",
        "Condition": "Rainy",
        "Wind Speed (km/h)": 26.8,
        "Day": "Monday"
    },
    {
        "Location": "Houston",
        "Condition": "Rainy",
        "Wind Speed (km/h)": 12.1,
        "Day": "Monday"
    },
    {
        "Location": "Denver",
        "Condition": "Sunny",
        "Wind Speed (km/h)": 9.0,
        "Day": "Sunday"
    },
    {
        "Location": "Miami",
        "Condition": "Windy",
        "Wind Speed (km/h)": 21.9,
        "Day": "Saturday"
    },
    {
        "Location": "Seattle",
        "Condition": "Snowy",
        "Wind Speed (km/h)": 28.6,
        "Day": "Tuesday"
    },
    {
        "Location": "Los Angeles",
        "Condition": "Stormy",
        "Wind Speed (km/h)": 18.5,
        "Day": "Wednesday"
    },
    {
        "Location": "Phoenix",
        "Condition": "Cloudy",
        "Wind Speed (km/h)": 14.1,
        "Day": "Monday"
    },
    {
        "Location": "New York",
        "Condition": "Sunny",
        "Wind Speed (km/h)": 15.7,
        "Day": "Friday"
    }
]
<end>Convert this json to CSV:
[
    {
        "Company": "BioLife",
        "Open Price": 84.89,
        "High Price": 1110.82,
        "Low Price": 84.89,
        "Volume": 6761374
    },
    {
        "Company": "MediaGroup",
        "Open Price": 401.76,
        "High Price": 914.53,
        "Low Price": 300.98,
        "Volume": 2998558
    },
    {
        "Company": "GreenEnergy",
        "Open Price": 117.01,
        "High Price": 1463.53,
        "Low Price": 117.01,
        "Volume": 2841141
    },
    {
        "Company": "MediaGroup",
        "Open Price": 1208.2,
        "High Price": 1216.51,
        "Low Price": 1208.2,
        "Volume": 9434431
    },
    {
        "Company": "RetailWorld",
        "Open Price": 184.88,
        "High Price": 535.81,
        "Low Price": 184.88,
        "Volume": 2763386
    },
    {
        "Company": "TechnoCorp",
        "Open Price": 952.59,
        "High Price": 1463.53,
        "Low Price": 142.12,
        "Volume": 1119164
    },
    {
        "Company": "BioLife",
        "Open Price": 1066.05,
        "High Price": 1066.05,
        "Low Price": 495.69,
        "Volume": 2284237
    },
    {
        "Company": "FoodChain",
        "Open Price": 518.63,
        "High Price": 1411.05,
        "Low Price": 518.63,
        "Volume": 4175173
    }
]<start>
Company,Open Price,High Price,Low Price,Volume
BioLife,84.89,1110.82,84.89,6761374
MediaGroup,401.76,914.53,300.98,2998558
GreenEnergy,117.01,1463.53,117.01,2841141
MediaGroup,1208.2,1216.51,1208.2,9434431
RetailWorld,184.88,535.81,184.88,2763386
TechnoCorp,952.59,1463.53,142.12,1119164
BioLife,1066.05,1066.05,495.69,2284237
FoodChain,518.63,1411.05,518.63,4175173
<end>Transform this plain text structure to a Json format:
Restaurant Name: Pasta Palace | Rating: 4 | Price Range: $
Restaurant Name: The Golden Spoon | Rating: 3 | Price Range: $
Restaurant Name: Vegan Delight | Rating: 3 | Price Range: $$
Restaurant Name: The Steakhouse | Rating: 5 | Price Range: $$
<start>
[
    {
        "Restaurant Name": "Pasta Palace",
        "Rating": 4,
        "Price Range": "$"
    },
    {
        "Restaurant Name": "The Golden Spoon",
        "Rating": 3,
        "Price Range": "$"
    },
    {
        "Restaurant Name": "Vegan Delight",
        "Rating": 3,
        "Price Range": "$$"
    },
    {
        "Restaurant Name": "The Steakhouse",
        "Rating": 5,
        "Price Range": "$$"
    }
]
<end>Transform this CSV structure to a MARKDOWN format:
Product Name,SKU,Stock Quantity,Category,Supplier Name
Apparatus,SKU-1091,394,Household,Umbrella Corp
Whatchamacallit,SKU-1027,393,Household,Umbrella Corp
Gizmo,SKU-1040,204,Toys,Globex
Device,SKU-1044,140,Toys,Umbrella Corp
Doohickey,SKU-1069,382,Automotive,Umbrella Corp
Instrument,SKU-1056,420,Sports,Wayne Enterprises
Widget,SKU-1055,53,Electronics,Globex
<start>
| Product Name | SKU | Stock Quantity | Category | Supplier Name |
| --- | --- | --- | --- | --- |
| Apparatus | SKU-1091 | 394 | Household | Umbrella Corp |
| Whatchamacallit | SKU-1027 | 393 | Household | Umbrella Corp |
| Gizmo | SKU-1040 | 204 | Toys | Globex |
| Device | SKU-1044 | 140 | Toys | Umbrella Corp |
| Doohickey | SKU-1069 | 382 | Automotive | Umbrella Corp |
| Instrument | SKU-1056 | 420 | Sports | Wayne Enterprises |
| Widget | SKU-1055 | 53 | Electronics | Globex |
<end>Transform this Json structure to a plain text format:
[
    {
        "Product Name": "Gizmo",
        "Price": 163.2,
        "Supplier Name": "Globex"
    },
    {
        "Product Name": "Whatchamacallit",
        "Price": 376.04,
        "Supplier Name": "Wonka Industries"
    },
    {
        "Product Name": "Gadget",
        "Price": 90.87,
        "Supplier Name": "Umbrella Corp"
    },
    {
        "Product Name": "Thingamajig",
        "Price": 99.94,
        "Supplier Name": "Wayne Enterprises"
    },
    {
        "Product Name": "Gadget",
        "Price": 73.75,
        "Supplier Name": "Wonka Industries"
    }
]<start>
Product Name: Gizmo | Price: 163.2 | Supplier Name: Globex
Product Name: Whatchamacallit | Price: 376.04 | Supplier Name: Wonka Industries
Product Name: Gadget | Price: 90.87 | Supplier Name: Umbrella Corp
Product Name: Thingamajig | Price: 99.94 | Supplier Name: Wayne Enterprises
Product Name: Gadget | Price: 73.75 | Supplier Name: Wonka Industries
<end>Convert this Plain text to Json:
Database Name: SessionsDB | Queries per Second: 697.37 | Cache Hit Ratio (%): 85.75 | Connection Count: 215 | Average Latency (ms): 64.27
Database Name: SessionsDB | Queries per Second: 4455.15 | Cache Hit Ratio (%): 87.5 | Connection Count: 205 | Average Latency (ms): 99.19
Database Name: ProfilesDB | Queries per Second: 3195.35 | Cache Hit Ratio (%): 97.89 | Connection Count: 95 | Average Latency (ms): 60.81
Database Name: ProfilesDB | Queries per Second: 1278.44 | Cache Hit Ratio (%): 73.58 | Connection Count: 250 | Average Latency (ms): 4.93
Database Name: ProductsDB | Queries per Second: 1884.68 | Cache Hit Ratio (%): 73.12 | Connection Count: 225 | Average Latency (ms): 92.49
Database Name: OrdersDB | Queries per Second: 3489.46 | Cache Hit Ratio (%): 98.17 | Connection Count: 239 | Average Latency (ms): 12.44
Database Name: SalesDB | Queries per Second: 1732.11 | Cache Hit Ratio (%): 74.86 | Connection Count: 259 | Average Latency (ms): 92.13
Database Name: ProfilesDB | Queries per Second: 4469.67 | Cache Hit Ratio (%): 93.0 | Connection Count: 355 | Average Latency (ms): 7.0
Database Name: SalesDB | Queries per Second: 1884.68 | Cache Hit Ratio (%): 74.86 | Connection Count: 181 | Average Latency (ms): 42.97
<start>
[
    {
        "Database Name": "SessionsDB",
        "Queries per Second": 697.37,
        "Cache Hit Ratio (%)": 85.75,
        "Connection Count": 215,
        "Average Latency (ms)": 64.27
    },
    {
        "Database Name": "SessionsDB",
        "Queries per Second": 4455.15,
        "Cache Hit Ratio (%)": 87.5,
        "Connection Count": 205,
        "Average Latency (ms)": 99.19
    },
    {
        "Database Name": "ProfilesDB",
        "Queries per Second": 3195.35,
        "Cache Hit Ratio (%)": 97.89,
        "Connection Count": 95,
        "Average Latency (ms)": 60.81
    },
    {
        "Database Name": "ProfilesDB",
        "Queries per Second": 1278.44,
        "Cache Hit Ratio (%)": 73.58,
        "Connection Count": 250,
        "Average Latency (ms)": 4.93
    },
    {
        "Database Name": "ProductsDB",
        "Queries per Second": 1884.68,
        "Cache Hit Ratio (%)": 73.12,
        "Connection Count": 225,
        "Average Latency (ms)": 92.49
    },
    {
        "Database Name": "OrdersDB",
        "Queries per Second": 3489.46,
        "Cache Hit Ratio (%)": 98.17,
        "Connection Count": 239,
        "Average Latency (ms)": 12.44
    },
    {
        "Database Name": "SalesDB",
        "Queries per Second": 1732.11,
        "Cache Hit Ratio (%)": 74.86,
        "Connection Count": 259,
        "Average Latency (ms)": 92.13
    },
    {
        "Database Name": "ProfilesDB",
        "Queries per Second": 4469.67,
        "Cache Hit Ratio (%)": 93.0,
        "Connection Count": 355,
        "Average Latency (ms)": 7.0
    },
    {
        "Database Name": "SalesDB",
        "Queries per Second": 1884.68,
        "Cache Hit Ratio (%)": 74.86,
        "Connection Count": 181,
        "Average Latency (ms)": 42.97
    }
]
<end>Transform this Yml structure to a CSV format:
- City: Phoenix
  Income: 220000
- City: Washington
  Income: 250000
- City: Los Angeles
  Income: 300000
- City: Chicago
  Income: 110000
- City: Dallas
  Income: 470000
- City: Indianapolis
  Income: 325000
- City: Jacksonville
  Income: 420000
<start>
City,Income
Phoenix,220000
Washington,250000
Los Angeles,300000
Chicago,110000
Dallas,470000
Indianapolis,325000
Jacksonville,420000
<end>Here's some yaml data, can you convert it to csv?
- Battery Level (%): 50.6
  Device ID: device-0078
  Device Type: Temperature Sensor
  Location: Hallway
  Reading Value: -14.9
  Timestamp: '2022-12-28 10:48:14'
- Battery Level (%): 66.6
  Device ID: device-0014
  Device Type: Humidity Sensor
  Location: Living Room
  Reading Value: -21.01
  Timestamp: '2022-09-10 08:56:06'
- Battery Level (%): 40.4
  Device ID: device-0052
  Device Type: Humidity Sensor
  Location: Bathroom
  Reading Value: 45.76
  Timestamp: '2022-07-24 01:17:54'
<start>
Device ID,Device Type,Location,Battery Level (%),Reading Value,Timestamp
device-0078,Temperature Sensor,Hallway,50.6,-14.9,2022-12-28 10:48:14
device-0014,Humidity Sensor,Living Room,66.6,-21.01,2022-09-10 08:56:06
device-0052,Humidity Sensor,Bathroom,40.4,45.76,2022-07-24 01:17:54
<end>Can you change this Yml into Csv?
- Author: Isla Windrider
  Title: Shadows of Solitude
- Author: Sylvia Nightshade
  Title: The Forgotten World
- Author: Isla Windrider
  Title: A Journey Through Time
- Author: Elara Moonshadow
  Title: Legends of the Rift
- Author: Thorne Ironwood
  Title: Echoes of Eternity
- Author: Draven Blackthorn
  Title: The Silent Grove
- Author: Rowan Ashborne
  Title: The Silent Grove
- Author: Isla Windrider
  Title: Shadows of Solitude
<start>
Title,Author
Shadows of Solitude,Isla Windrider
The Forgotten World,Sylvia Nightshade
A Journey Through Time,Isla Windrider
Legends of the Rift,Elara Moonshadow
Echoes of Eternity,Thorne Ironwood
The Silent Grove,Draven Blackthorn
The Silent Grove,Rowan Ashborne
Shadows of Solitude,Isla Windrider
<end>