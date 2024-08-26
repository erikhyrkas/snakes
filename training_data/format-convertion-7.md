Convert this plain text to yaml:
Company: FinanceTrust | Date: 2022-06-12 | Open Price: 1115.84 | Close Price: 69.62 | Low Price: 69.62 | Volume: 3848975
Company: RetailWorld | Date: 2023-07-05 | Open Price: 37.35 | Close Price: 879.97 | Low Price: 37.35 | Volume: 4450699
Company: AeroSystems | Date: 2018-09-12 | Open Price: 517.16 | Close Price: 389.87 | Low Price: 389.87 | Volume: 1346783
Company: AeroSystems | Date: 2022-08-26 | Open Price: 791.27 | Close Price: 1007.36 | Low Price: 781.95 | Volume: 2377777
Company: MediaGroup | Date: 2010-12-14 | Open Price: 824.39 | Close Price: 309.21 | Low Price: 309.21 | Volume: 866539
Company: FinanceTrust | Date: 2019-09-27 | Open Price: 1012.24 | Close Price: 879.97 | Low Price: 879.97 | Volume: 2288101
Company: FinanceTrust | Date: 2018-05-26 | Open Price: 517.11 | Close Price: 346.46 | Low Price: 346.46 | Volume: 3419246
<start>
- Close Price: 69.62
  Company: FinanceTrust
  Date: '2022-06-12'
  Low Price: 69.62
  Open Price: 1115.84
  Volume: 3848975
- Close Price: 879.97
  Company: RetailWorld
  Date: '2023-07-05'
  Low Price: 37.35
  Open Price: 37.35
  Volume: 4450699
- Close Price: 389.87
  Company: AeroSystems
  Date: '2018-09-12'
  Low Price: 389.87
  Open Price: 517.16
  Volume: 1346783
- Close Price: 1007.36
  Company: AeroSystems
  Date: '2022-08-26'
  Low Price: 781.95
  Open Price: 791.27
  Volume: 2377777
- Close Price: 309.21
  Company: MediaGroup
  Date: '2010-12-14'
  Low Price: 309.21
  Open Price: 824.39
  Volume: 866539
- Close Price: 879.97
  Company: FinanceTrust
  Date: '2019-09-27'
  Low Price: 879.97
  Open Price: 1012.24
  Volume: 2288101
- Close Price: 346.46
  Company: FinanceTrust
  Date: '2018-05-26'
  Low Price: 346.46
  Open Price: 517.11
  Volume: 3419246
<end>Convert this yaml to json:
- Close Price: 1099.98
  Company: MediaGroup
  Date: '2015-09-13'
  Low Price: 321.89
  Volume: 7971778
- Close Price: 1006.01
  Company: AeroSystems
  Date: '2015-02-22'
  Low Price: 663.95
  Volume: 9829946
- Close Price: 868.07
  Company: AeroSystems
  Date: '2013-06-05'
  Low Price: 706.45
  Volume: 1071075
- Close Price: 497.39
  Company: RetailWorld
  Date: '2010-10-05'
  Low Price: 497.39
  Volume: 4515261
<start>
[
    {
        "Company": "MediaGroup",
        "Date": "2015-09-13",
        "Close Price": 1099.98,
        "Low Price": 321.89,
        "Volume": 7971778
    },
    {
        "Company": "AeroSystems",
        "Date": "2015-02-22",
        "Close Price": 1006.01,
        "Low Price": 663.95,
        "Volume": 9829946
    },
    {
        "Company": "AeroSystems",
        "Date": "2013-06-05",
        "Close Price": 868.07,
        "Low Price": 706.45,
        "Volume": 1071075
    },
    {
        "Company": "RetailWorld",
        "Date": "2010-10-05",
        "Close Price": 497.39,
        "Low Price": 497.39,
        "Volume": 4515261
    }
]
<end>Transform this markdown structure to a csv format:
| Product Name | SKU | Price | Category | Supplier Name |
| --- | --- | --- | --- | --- |
| Apparatus | SKU-1052 | 189.15 | Sports | Wayne Enterprises |
| Device | SKU-1000 | 260.25 | Toys | Globex |
| Device | SKU-1010 | 219.98 | Electronics | Globex |
| Gizmo | SKU-1021 | 348.76 | Household | Wayne Enterprises |
| Apparatus | SKU-1028 | 299.21 | Electronics | ACME Corp |
| Thingamajig | SKU-1034 | 354.92 | Automotive | Globex |
| Apparatus | SKU-1070 | 232.7 | Sports | Wonka Industries |
| Contraption | SKU-1035 | 339.09 | Toys | Umbrella Corp |
| Widget | SKU-1070 | 130.27 | Automotive | Wonka Industries |
| Gizmo | SKU-1028 | 99.02 | Sports | Wonka Industries |<start>
Product Name,SKU,Price,Category,Supplier Name
Apparatus,SKU-1052,189.15,Sports,Wayne Enterprises
Device,SKU-1000,260.25,Toys,Globex
Device,SKU-1010,219.98,Electronics,Globex
Gizmo,SKU-1021,348.76,Household,Wayne Enterprises
Apparatus,SKU-1028,299.21,Electronics,ACME Corp
Thingamajig,SKU-1034,354.92,Automotive,Globex
Apparatus,SKU-1070,232.7,Sports,Wonka Industries
Contraption,SKU-1035,339.09,Toys,Umbrella Corp
Widget,SKU-1070,130.27,Automotive,Wonka Industries
Gizmo,SKU-1028,99.02,Sports,Wonka Industries
<end>Here's some Yml data, can you convert it to markdown?
- Category: Toys
  Price: 325.51
  Product Name: Widget
  SKU: SKU-1002
  Stock Quantity: 11
  Supplier Name: ACME Corp
- Category: Household
  Price: 491.75
  Product Name: Gizmo
  SKU: SKU-1079
  Stock Quantity: 66
  Supplier Name: Wonka Industries
- Category: Electronics
  Price: 488.32
  Product Name: Widget
  SKU: SKU-1099
  Stock Quantity: 311
  Supplier Name: Globex
- Category: Toys
  Price: 380.63
  Product Name: Thingamajig
  SKU: SKU-1049
  Stock Quantity: 149
  Supplier Name: Globex
- Category: Automotive
  Price: 354.38
  Product Name: Device
  SKU: SKU-1088
  Stock Quantity: 475
  Supplier Name: Wonka Industries
- Category: Electronics
  Price: 322.2
  Product Name: Contraption
  SKU: SKU-1085
  Stock Quantity: 493
  Supplier Name: Wonka Industries
<start>
| Product Name | SKU | Price | Stock Quantity | Category | Supplier Name |
| --- | --- | --- | --- | --- | --- |
| Widget | SKU-1002 | 325.51 | 11 | Toys | ACME Corp |
| Gizmo | SKU-1079 | 491.75 | 66 | Household | Wonka Industries |
| Widget | SKU-1099 | 488.32 | 311 | Electronics | Globex |
| Thingamajig | SKU-1049 | 380.63 | 149 | Toys | Globex |
| Device | SKU-1088 | 354.38 | 475 | Automotive | Wonka Industries |
| Contraption | SKU-1085 | 322.2 | 493 | Electronics | Wonka Industries |
<end>Here's some Markdown data, can you convert it to JSON?
| Date | Open Price | Close Price | High Price | Low Price |
| --- | --- | --- | --- | --- |
| 2023-08-05 | 1256.33 | 1444.77 | 1444.77 | 1256.33 |
| 2015-07-15 | 444.74 | 1238.5 | 1249.57 | 444.74 |
| 2010-03-09 | 733.15 | 1333.51 | 1333.51 | 733.15 |
| 2022-08-16 | 1281.28 | 1215.81 | 1281.28 | 718.22 |<start>
[
    {
        "Date": "2023-08-05",
        "Open Price": 1256.33,
        "Close Price": 1444.77,
        "High Price": 1444.77,
        "Low Price": 1256.33
    },
    {
        "Date": "2015-07-15",
        "Open Price": 444.74,
        "Close Price": 1238.5,
        "High Price": 1249.57,
        "Low Price": 444.74
    },
    {
        "Date": "2010-03-09",
        "Open Price": 733.15,
        "Close Price": 1333.51,
        "High Price": 1333.51,
        "Low Price": 733.15
    },
    {
        "Date": "2022-08-16",
        "Open Price": 1281.28,
        "Close Price": 1215.81,
        "High Price": 1281.28,
        "Low Price": 718.22
    }
]
<end>Can you change this json into CSV?
[
    {
        "Title": "Echoes of Eternity",
        "Author": "Draven Blackthorn",
        "Genre": "Fantasy",
        "Publication Year": 2016
    },
    {
        "Title": "The Forgotten World",
        "Author": "Kara Firebrand",
        "Genre": "Fantasy",
        "Publication Year": 1985
    },
    {
        "Title": "Whispers of the Abyss",
        "Author": "Orion Frostblade",
        "Genre": "Romance",
        "Publication Year": 1974
    },
    {
        "Title": "The Forgotten World",
        "Author": "Thorne Ironwood",
        "Genre": "Horror",
        "Publication Year": 1976
    },
    {
        "Title": "The Last Sky",
        "Author": "Sylvia Nightshade",
        "Genre": "Non-Fiction",
        "Publication Year": 1969
    },
    {
        "Title": "Whispers of the Abyss",
        "Author": "Rowan Ashborne",
        "Genre": "Science Fiction",
        "Publication Year": 1972
    },
    {
        "Title": "The Silent Grove",
        "Author": "Elara Moonshadow",
        "Genre": "Historical",
        "Publication Year": 1952
    },
    {
        "Title": "The Last Sky",
        "Author": "Kara Firebrand",
        "Genre": "Historical",
        "Publication Year": 1998
    },
    {
        "Title": "The Forgotten World",
        "Author": "Orion Frostblade",
        "Genre": "Science Fiction",
        "Publication Year": 2023
    }
]<start>
Title,Author,Genre,Publication Year
Echoes of Eternity,Draven Blackthorn,Fantasy,2016
The Forgotten World,Kara Firebrand,Fantasy,1985
Whispers of the Abyss,Orion Frostblade,Romance,1974
The Forgotten World,Thorne Ironwood,Horror,1976
The Last Sky,Sylvia Nightshade,Non-Fiction,1969
Whispers of the Abyss,Rowan Ashborne,Science Fiction,1972
The Silent Grove,Elara Moonshadow,Historical,1952
The Last Sky,Kara Firebrand,Historical,1998
The Forgotten World,Orion Frostblade,Science Fiction,2023
<end>Transform this Markdown structure to a plain text format:
| Location | Condition | Wind Speed (km/h) | Day |
| --- | --- | --- | --- |
| Miami | Foggy | 19.0 | Sunday |
| Miami | Sunny | 15.6 | Monday |
| Chicago | Windy | 10.5 | Friday |
| Denver | Stormy | 6.3 | Tuesday |
| Miami | Sunny | 26.2 | Tuesday |
| Houston | Windy | 6.3 | Friday |
| Chicago | Sunny | 26.1 | Sunday |<start>
Location: Miami | Condition: Foggy | Wind Speed (km/h): 19.0 | Day: Sunday
Location: Miami | Condition: Sunny | Wind Speed (km/h): 15.6 | Day: Monday
Location: Chicago | Condition: Windy | Wind Speed (km/h): 10.5 | Day: Friday
Location: Denver | Condition: Stormy | Wind Speed (km/h): 6.3 | Day: Tuesday
Location: Miami | Condition: Sunny | Wind Speed (km/h): 26.2 | Day: Tuesday
Location: Houston | Condition: Windy | Wind Speed (km/h): 6.3 | Day: Friday
Location: Chicago | Condition: Sunny | Wind Speed (km/h): 26.1 | Day: Sunday
<end>Please transform the following PLAIN TEXT data into JSON:
Title: A Journey Through Time | Author: Rowan Ashborne | Rating: 4.4
Title: Legends of the Rift | Author: Kara Firebrand | Rating: 2.1
Title: A Journey Through Time | Author: Thorne Ironwood | Rating: 1.3
Title: Tales of the Brave | Author: Orion Frostblade | Rating: 3.8
Title: Legends of the Rift | Author: Kara Firebrand | Rating: 3.4
Title: The Crystal Key | Author: Orion Frostblade | Rating: 3.6
<start>
[
    {
        "Title": "A Journey Through Time",
        "Author": "Rowan Ashborne",
        "Rating": 4.4
    },
    {
        "Title": "Legends of the Rift",
        "Author": "Kara Firebrand",
        "Rating": 2.1
    },
    {
        "Title": "A Journey Through Time",
        "Author": "Thorne Ironwood",
        "Rating": 1.3
    },
    {
        "Title": "Tales of the Brave",
        "Author": "Orion Frostblade",
        "Rating": 3.8
    },
    {
        "Title": "Legends of the Rift",
        "Author": "Kara Firebrand",
        "Rating": 3.4
    },
    {
        "Title": "The Crystal Key",
        "Author": "Orion Frostblade",
        "Rating": 3.6
    }
]
<end>Convert this YML to CSV:
- Close Price: 608.1
  Company: FoodChain
  Date: '2010-10-22'
  High Price: 1172.2
  Low Price: 551.35
  Open Price: 1172.2
  Volume: 5182745
- Close Price: 885.93
  Company: FoodChain
  Date: '2019-12-12'
  High Price: 1203.68
  Low Price: 154.08
  Open Price: 154.08
  Volume: 5487420
- Close Price: 815.46
  Company: RetailWorld
  Date: '2021-12-01'
  High Price: 1024.07
  Low Price: 815.46
  Open Price: 1024.07
  Volume: 3053458
- Close Price: 1307.5
  Company: TechnoCorp
  Date: '2010-07-22'
  High Price: 1493.83
  Low Price: 678.01
  Open Price: 984.43
  Volume: 9341541
- Close Price: 919.16
  Company: FoodChain
  Date: '2010-01-13'
  High Price: 1213.0
  Low Price: 919.16
  Open Price: 1213.0
  Volume: 2921648
<start>
Company,Date,Open Price,Close Price,High Price,Low Price,Volume
FoodChain,2010-10-22,1172.2,608.1,1172.2,551.35,5182745
FoodChain,2019-12-12,154.08,885.93,1203.68,154.08,5487420
RetailWorld,2021-12-01,1024.07,815.46,1024.07,815.46,3053458
TechnoCorp,2010-07-22,984.43,1307.5,1493.83,678.01,9341541
FoodChain,2010-01-13,1213.0,919.16,1213.0,919.16,2921648
<end>Convert this CSV to YAML:
Name,Income
Joan,345000
Jordan,115000
Geneva,160000
Sheila,155000
<start>
- Income: 345000
  Name: Joan
- Income: 115000
  Name: Jordan
- Income: 160000
  Name: Geneva
- Income: 155000
  Name: Sheila
<end>Convert this PLAIN TEXT to markdown:
Open Price: 877.91 | High Price: 1461.58 | Low Price: 598.38 | Volume: 3148761
Open Price: 828.82 | High Price: 1316.7 | Low Price: 342.84 | Volume: 6923116
Open Price: 332.46 | High Price: 842.34 | Low Price: 332.46 | Volume: 1333764
Open Price: 469.27 | High Price: 1144.6 | Low Price: 469.27 | Volume: 1576521
Open Price: 1069.01 | High Price: 1446.86 | Low Price: 1069.01 | Volume: 8059812
Open Price: 832.26 | High Price: 1235.55 | Low Price: 169.99 | Volume: 3450794
Open Price: 952.18 | High Price: 1428.94 | Low Price: 25.21 | Volume: 136639
Open Price: 254.97 | High Price: 254.97 | Low Price: 115.03 | Volume: 2658887
Open Price: 603.54 | High Price: 1069.01 | Low Price: 266.15 | Volume: 6537691
<start>
| Open Price | High Price | Low Price | Volume |
| --- | --- | --- | --- |
| 877.91 | 1461.58 | 598.38 | 3148761 |
| 828.82 | 1316.7 | 342.84 | 6923116 |
| 332.46 | 842.34 | 332.46 | 1333764 |
| 469.27 | 1144.6 | 469.27 | 1576521 |
| 1069.01 | 1446.86 | 1069.01 | 8059812 |
| 832.26 | 1235.55 | 169.99 | 3450794 |
| 952.18 | 1428.94 | 25.21 | 136639 |
| 254.97 | 254.97 | 115.03 | 2658887 |
| 603.54 | 1069.01 | 266.15 | 6537691 |
<end>Here's some Json data, can you convert it to Plain text?
[
    {
        "Author": "Luna Silverleaf",
        "Genre": "Fantasy",
        "Publication Year": 1993,
        "Rating": 2.3
    },
    {
        "Author": "Kara Firebrand",
        "Genre": "Horror",
        "Publication Year": 2006,
        "Rating": 2.2
    },
    {
        "Author": "Sylvia Nightshade",
        "Genre": "Non-Fiction",
        "Publication Year": 1972,
        "Rating": 4.3
    }
]<start>
Author: Luna Silverleaf | Genre: Fantasy | Publication Year: 1993 | Rating: 2.3
Author: Kara Firebrand | Genre: Horror | Publication Year: 2006 | Rating: 2.2
Author: Sylvia Nightshade | Genre: Non-Fiction | Publication Year: 1972 | Rating: 4.3
<end>Please transform the following Csv data into JSON:
Device ID,Device Type,Location,Battery Level (%),Reading Value
device-0004,Motion Detector,Bedroom,41.0,0.78
device-0047,Pressure Sensor,Bathroom,74.8,19.03
device-0077,Humidity Sensor,Hallway,62.4,26.33
device-0077,Pressure Sensor,Kitchen,95.8,45.35
device-0008,Light Sensor,Kitchen,26.8,14.29
device-0072,Temperature Sensor,Kitchen,74.8,11.03
device-0012,Humidity Sensor,Office,82.6,-16.97
<start>
[
    {
        "Device ID": "device-0004",
        "Device Type": "Motion Detector",
        "Location": "Bedroom",
        "Battery Level (%)": 41.0,
        "Reading Value": 0.78
    },
    {
        "Device ID": "device-0047",
        "Device Type": "Pressure Sensor",
        "Location": "Bathroom",
        "Battery Level (%)": 74.8,
        "Reading Value": 19.03
    },
    {
        "Device ID": "device-0077",
        "Device Type": "Humidity Sensor",
        "Location": "Hallway",
        "Battery Level (%)": 62.4,
        "Reading Value": 26.33
    },
    {
        "Device ID": "device-0077",
        "Device Type": "Pressure Sensor",
        "Location": "Kitchen",
        "Battery Level (%)": 95.8,
        "Reading Value": 45.35
    },
    {
        "Device ID": "device-0008",
        "Device Type": "Light Sensor",
        "Location": "Kitchen",
        "Battery Level (%)": 26.8,
        "Reading Value": 14.29
    },
    {
        "Device ID": "device-0072",
        "Device Type": "Temperature Sensor",
        "Location": "Kitchen",
        "Battery Level (%)": 74.8,
        "Reading Value": 11.03
    },
    {
        "Device ID": "device-0012",
        "Device Type": "Humidity Sensor",
        "Location": "Office",
        "Battery Level (%)": 82.6,
        "Reading Value": -16.97
    }
]
<end>Please transform the following Markdown data into Plain text:
| Name | Age | Birth Month | Income |
| --- | --- | --- | --- |
| Millie | 39 | March | 360000 |
| Brandon | 23 | August | 35000 |
| Lydia | 43 | April | 350000 |
| Tracie | 27 | November | 70000 |<start>
Name: Millie | Age: 39 | Birth Month: March | Income: 360000
Name: Brandon | Age: 23 | Birth Month: August | Income: 35000
Name: Lydia | Age: 43 | Birth Month: April | Income: 350000
Name: Tracie | Age: 27 | Birth Month: November | Income: 70000
<end>Convert this csv to JSON:
Title,Release Year
Dreamwalker,1990
Rise of the Titans,1977
The Final Voyage,2004
<start>
[
    {
        "Title": "Dreamwalker",
        "Release Year": 1990
    },
    {
        "Title": "Rise of the Titans",
        "Release Year": 1977
    },
    {
        "Title": "The Final Voyage",
        "Release Year": 2004
    }
]
<end>Please transform the following yaml data into Csv:
- Average Latency (ms): 85.71
  Connection Count: 140
  Queries per Second: 260.57
- Average Latency (ms): 34.78
  Connection Count: 458
  Queries per Second: 4206.78
- Average Latency (ms): 57.36
  Connection Count: 50
  Queries per Second: 1592.85
- Average Latency (ms): 35.07
  Connection Count: 226
  Queries per Second: 3172.82
- Average Latency (ms): 65.99
  Connection Count: 33
  Queries per Second: 2717.13
- Average Latency (ms): 62.88
  Connection Count: 140
  Queries per Second: 470.11
- Average Latency (ms): 57.76
  Connection Count: 478
  Queries per Second: 2431.21
<start>
Queries per Second,Connection Count,Average Latency (ms)
260.57,140,85.71
4206.78,458,34.78
1592.85,50,57.36
3172.82,226,35.07
2717.13,33,65.99
470.11,140,62.88
2431.21,478,57.76
<end>Transform this Json structure to a Csv format:
[
    {
        "Device ID": "device-0033",
        "Device Type": "Temperature Sensor",
        "Location": "Bathroom",
        "Battery Level (%)": 52.3,
        "Reading Value": -13.44,
        "Timestamp": "2022-08-08 08:01:17"
    },
    {
        "Device ID": "device-0020",
        "Device Type": "Temperature Sensor",
        "Location": "Office",
        "Battery Level (%)": 56.7,
        "Reading Value": 41.47,
        "Timestamp": "2023-04-08 00:28:39"
    },
    {
        "Device ID": "device-0023",
        "Device Type": "Light Sensor",
        "Location": "Bedroom",
        "Battery Level (%)": 14.4,
        "Reading Value": 39.7,
        "Timestamp": "2023-06-15 13:22:45"
    }
]<start>
Device ID,Device Type,Location,Battery Level (%),Reading Value,Timestamp
device-0033,Temperature Sensor,Bathroom,52.3,-13.44,2022-08-08 08:01:17
device-0020,Temperature Sensor,Office,56.7,41.47,2023-04-08 00:28:39
device-0023,Light Sensor,Bedroom,14.4,39.7,2023-06-15 13:22:45
<end>Please transform the following MARKDOWN data into Plain text:
| Location | Condition | Temperature (C) | Wind Speed (km/h) |
| --- | --- | --- | --- |
| Seattle | Foggy | 23.7 | 18.9 |
| Seattle | Snowy | 20.0 | 27.1 |
| New York | Sunny | 8.1 | 14.0 |<start>
Location: Seattle | Condition: Foggy | Temperature (C): 23.7 | Wind Speed (km/h): 18.9
Location: Seattle | Condition: Snowy | Temperature (C): 20.0 | Wind Speed (km/h): 27.1
Location: New York | Condition: Sunny | Temperature (C): 8.1 | Wind Speed (km/h): 14.0
<end>Transform this Plain text structure to a Csv format:
Age: 40 | City: Chicago | Income: 120000
Age: 27 | City: Houston | Income: 340000
Age: 48 | City: Denver | Income: 100000
Age: 28 | City: San Antonio | Income: 30000
Age: 38 | City: Denver | Income: 475000
Age: 62 | City: Charlotte | Income: 290000
Age: 31 | City: New York | Income: 380000
Age: 29 | City: El Paso | Income: 430000
Age: 18 | City: Milwaukee | Income: 140000
Age: 41 | City: Jacksonville | Income: 350000
<start>
Age,City,Income
40,Chicago,120000
27,Houston,340000
48,Denver,100000
28,San Antonio,30000
38,Denver,475000
62,Charlotte,290000
31,New York,380000
29,El Paso,430000
18,Milwaukee,140000
41,Jacksonville,350000
<end>Please transform the following Plain text data into json:
Market Cap: Mega Cap | Stock Price: 676.85 | Annual Revenue (B): 301.6 | Quarter: Q2
Market Cap: Small Cap | Stock Price: 521.47 | Annual Revenue (B): 424.81 | Quarter: Q3
Market Cap: Small Cap | Stock Price: 764.33 | Annual Revenue (B): 405.52 | Quarter: Q1
Market Cap: Small Cap | Stock Price: 368.18 | Annual Revenue (B): 297.12 | Quarter: Q4
Market Cap: Mega Cap | Stock Price: 529.78 | Annual Revenue (B): 405.44 | Quarter: Q1
Market Cap: Mega Cap | Stock Price: 779.46 | Annual Revenue (B): 241.92 | Quarter: Q4
Market Cap: Mega Cap | Stock Price: 713.93 | Annual Revenue (B): 490.98 | Quarter: Q4
<start>
[
    {
        "Market Cap": "Mega Cap",
        "Stock Price": 676.85,
        "Annual Revenue (B)": 301.6,
        "Quarter": "Q2"
    },
    {
        "Market Cap": "Small Cap",
        "Stock Price": 521.47,
        "Annual Revenue (B)": 424.81,
        "Quarter": "Q3"
    },
    {
        "Market Cap": "Small Cap",
        "Stock Price": 764.33,
        "Annual Revenue (B)": 405.52,
        "Quarter": "Q1"
    },
    {
        "Market Cap": "Small Cap",
        "Stock Price": 368.18,
        "Annual Revenue (B)": 297.12,
        "Quarter": "Q4"
    },
    {
        "Market Cap": "Mega Cap",
        "Stock Price": 529.78,
        "Annual Revenue (B)": 405.44,
        "Quarter": "Q1"
    },
    {
        "Market Cap": "Mega Cap",
        "Stock Price": 779.46,
        "Annual Revenue (B)": 241.92,
        "Quarter": "Q4"
    },
    {
        "Market Cap": "Mega Cap",
        "Stock Price": 713.93,
        "Annual Revenue (B)": 490.98,
        "Quarter": "Q4"
    }
]
<end>Please transform the following yml data into MARKDOWN:
- Author: Isla Windrider
  Title: Shadows of Solitude
- Author: Luna Silverleaf
  Title: Legends of the Rift
- Author: Rowan Ashborne
  Title: The Last Sky
- Author: Galen Starfire
  Title: A Journey Through Time
- Author: Kara Firebrand
  Title: Shadows of Solitude
- Author: Kara Firebrand
  Title: The Last Sky
<start>
| Title | Author |
| --- | --- |
| Shadows of Solitude | Isla Windrider |
| Legends of the Rift | Luna Silverleaf |
| The Last Sky | Rowan Ashborne |
| A Journey Through Time | Galen Starfire |
| Shadows of Solitude | Kara Firebrand |
| The Last Sky | Kara Firebrand |
<end>Convert this YML to CSV:
- Location: Houston
  Price Range: $$$
  Rating: 3
  Restaurant Name: Taco Town
- Location: Miami
  Price Range: $$$
  Rating: 3
  Restaurant Name: Vegan Delight
- Location: Miami
  Price Range: $$
  Rating: 4
  Restaurant Name: The Steakhouse
- Location: Houston
  Price Range: $$$
  Rating: 3
  Restaurant Name: Curry Corner
<start>
Restaurant Name,Location,Rating,Price Range
Taco Town,Houston,3,$$$
Vegan Delight,Miami,3,$$$
The Steakhouse,Miami,4,$$
Curry Corner,Houston,3,$$$
<end>Please transform the following plain text data into MARKDOWN:
Device ID: device-0026 | Location: Garden | Battery Level (%): 77.4
Device ID: device-0037 | Location: Bathroom | Battery Level (%): 57.4
Device ID: device-0026 | Location: Hallway | Battery Level (%): 19.4
Device ID: device-0058 | Location: Office | Battery Level (%): 23.4
Device ID: device-0099 | Location: Living Room | Battery Level (%): 17.2
Device ID: device-0019 | Location: Garden | Battery Level (%): 55.7
Device ID: device-0061 | Location: Living Room | Battery Level (%): 34.3
Device ID: device-0038 | Location: Office | Battery Level (%): 23.4
Device ID: device-0073 | Location: Bathroom | Battery Level (%): 68.7
Device ID: device-0005 | Location: Bedroom | Battery Level (%): 82.2
<start>
| Device ID | Location | Battery Level (%) |
| --- | --- | --- |
| device-0026 | Garden | 77.4 |
| device-0037 | Bathroom | 57.4 |
| device-0026 | Hallway | 19.4 |
| device-0058 | Office | 23.4 |
| device-0099 | Living Room | 17.2 |
| device-0019 | Garden | 55.7 |
| device-0061 | Living Room | 34.3 |
| device-0038 | Office | 23.4 |
| device-0073 | Bathroom | 68.7 |
| device-0005 | Bedroom | 82.2 |
<end>Can you change this YAML into Plain text?
- Category: Toys
  Price: 218.21
  Product Name: Gadget
  SKU: SKU-1067
  Stock Quantity: 164
  Supplier Name: Wonka Industries
- Category: Sports
  Price: 291.04
  Product Name: Thingamajig
  SKU: SKU-1016
  Stock Quantity: 241
  Supplier Name: Umbrella Corp
- Category: Toys
  Price: 106.8
  Product Name: Whatchamacallit
  SKU: SKU-1078
  Stock Quantity: 5
  Supplier Name: Globex
- Category: Sports
  Price: 487.52
  Product Name: Device
  SKU: SKU-1060
  Stock Quantity: 250
  Supplier Name: Wayne Enterprises
- Category: Toys
  Price: 38.36
  Product Name: Gizmo
  SKU: SKU-1005
  Stock Quantity: 99
  Supplier Name: Umbrella Corp
<start>
Product Name: Gadget | SKU: SKU-1067 | Price: 218.21 | Stock Quantity: 164 | Category: Toys | Supplier Name: Wonka Industries
Product Name: Thingamajig | SKU: SKU-1016 | Price: 291.04 | Stock Quantity: 241 | Category: Sports | Supplier Name: Umbrella Corp
Product Name: Whatchamacallit | SKU: SKU-1078 | Price: 106.8 | Stock Quantity: 5 | Category: Toys | Supplier Name: Globex
Product Name: Device | SKU: SKU-1060 | Price: 487.52 | Stock Quantity: 250 | Category: Sports | Supplier Name: Wayne Enterprises
Product Name: Gizmo | SKU: SKU-1005 | Price: 38.36 | Stock Quantity: 99 | Category: Toys | Supplier Name: Umbrella Corp
<end>Please transform the following markdown data into YAML:
| Restaurant Name | Location | Rating | Price Range |
| --- | --- | --- | --- |
| Burger Haven | San Francisco | 1 | $ |
| Vegan Delight | Chicago | 1 | $$ |
| Sushi World | San Francisco | 2 | $$$ |
| Burger Haven | Phoenix | 2 | $$$$ |
| Pizza Planet | Chicago | 1 | $$$$ |
| The Golden Spoon | Houston | 1 | $$ |
| Sushi World | Los Angeles | 1 | $$$$$ |
| BBQ Barn | Chicago | 4 | $ |
| The Golden Spoon | Miami | 3 | $ |
| The Steakhouse | Seattle | 4 | $$$ |<start>
- Location: San Francisco
  Price Range: $
  Rating: 1
  Restaurant Name: Burger Haven
- Location: Chicago
  Price Range: $$
  Rating: 1
  Restaurant Name: Vegan Delight
- Location: San Francisco
  Price Range: $$$
  Rating: 2
  Restaurant Name: Sushi World
- Location: Phoenix
  Price Range: $$$$
  Rating: 2
  Restaurant Name: Burger Haven
- Location: Chicago
  Price Range: $$$$
  Rating: 1
  Restaurant Name: Pizza Planet
- Location: Houston
  Price Range: $$
  Rating: 1
  Restaurant Name: The Golden Spoon
- Location: Los Angeles
  Price Range: $$$$$
  Rating: 1
  Restaurant Name: Sushi World
- Location: Chicago
  Price Range: $
  Rating: 4
  Restaurant Name: BBQ Barn
- Location: Miami
  Price Range: $
  Rating: 3
  Restaurant Name: The Golden Spoon
- Location: Seattle
  Price Range: $$$
  Rating: 4
  Restaurant Name: The Steakhouse
<end>Here's some JSON data, can you convert it to MARKDOWN?
[
    {
        "Title": "The Great Expedition",
        "Director": "Zara Stormrider",
        "Genre": "Drama",
        "Release Year": 1970
    },
    {
        "Title": "Beyond the Veil",
        "Director": "Lira Silverleaf",
        "Genre": "Drama",
        "Release Year": 1973
    },
    {
        "Title": "The Final Voyage",
        "Director": "Rylan Frostblade",
        "Genre": "Adventure",
        "Release Year": 2013
    },
    {
        "Title": "Mystery of the Depths",
        "Director": "Orin Shadowalker",
        "Genre": "Action",
        "Release Year": 1979
    },
    {
        "Title": "Mystery of the Depths",
        "Director": "Aria Ravenwood",
        "Genre": "Sci-Fi",
        "Release Year": 2009
    },
    {
        "Title": "Rise of the Titans",
        "Director": "Zara Stormrider",
        "Genre": "Fantasy",
        "Release Year": 2022
    },
    {
        "Title": "The Great Expedition",
        "Director": "Zara Stormrider",
        "Genre": "Drama",
        "Release Year": 1988
    },
    {
        "Title": "Mystery of the Depths",
        "Director": "Selene Darkwhisper",
        "Genre": "Horror",
        "Release Year": 2013
    },
    {
        "Title": "The Final Voyage",
        "Director": "Drake Nightshade",
        "Genre": "Drama",
        "Release Year": 1994
    },
    {
        "Title": "Rise of the Titans",
        "Director": "Cade Firebrand",
        "Genre": "Sci-Fi",
        "Release Year": 2014
    }
]<start>
| Title | Director | Genre | Release Year |
| --- | --- | --- | --- |
| The Great Expedition | Zara Stormrider | Drama | 1970 |
| Beyond the Veil | Lira Silverleaf | Drama | 1973 |
| The Final Voyage | Rylan Frostblade | Adventure | 2013 |
| Mystery of the Depths | Orin Shadowalker | Action | 1979 |
| Mystery of the Depths | Aria Ravenwood | Sci-Fi | 2009 |
| Rise of the Titans | Zara Stormrider | Fantasy | 2022 |
| The Great Expedition | Zara Stormrider | Drama | 1988 |
| Mystery of the Depths | Selene Darkwhisper | Horror | 2013 |
| The Final Voyage | Drake Nightshade | Drama | 1994 |
| Rise of the Titans | Cade Firebrand | Sci-Fi | 2014 |
<end>Please transform the following MARKDOWN data into json:
| Company | Date | Low Price | Volume |
| --- | --- | --- | --- |
| FoodChain | 2014-01-23 | 1176.46 | 4975790 |
| AutoMotive | 2010-05-13 | 193.18 | 5212938 |
| MediaGroup | 2016-04-03 | 109.86 | 6584098 |<start>
[
    {
        "Company": "FoodChain",
        "Date": "2014-01-23",
        "Low Price": 1176.46,
        "Volume": 4975790
    },
    {
        "Company": "AutoMotive",
        "Date": "2010-05-13",
        "Low Price": 193.18,
        "Volume": 5212938
    },
    {
        "Company": "MediaGroup",
        "Date": "2016-04-03",
        "Low Price": 109.86,
        "Volume": 6584098
    }
]
<end>Please transform the following CSV data into json:
Device Type,Location,Battery Level (%),Reading Value,Timestamp
Motion Detector,Garage,67.6,4.61,2022-01-05 04:12:02
Humidity Sensor,Kitchen,58.7,-38.65,2023-05-25 07:06:08
Humidity Sensor,Garage,57.1,-7.75,2023-06-09 20:57:50
Motion Detector,Bathroom,39.4,-28.05,2023-01-08 19:38:10
<start>
[
    {
        "Device Type": "Motion Detector",
        "Location": "Garage",
        "Battery Level (%)": 67.6,
        "Reading Value": 4.61,
        "Timestamp": "2022-01-05 04:12:02"
    },
    {
        "Device Type": "Humidity Sensor",
        "Location": "Kitchen",
        "Battery Level (%)": 58.7,
        "Reading Value": -38.65,
        "Timestamp": "2023-05-25 07:06:08"
    },
    {
        "Device Type": "Humidity Sensor",
        "Location": "Garage",
        "Battery Level (%)": 57.1,
        "Reading Value": -7.75,
        "Timestamp": "2023-06-09 20:57:50"
    },
    {
        "Device Type": "Motion Detector",
        "Location": "Bathroom",
        "Battery Level (%)": 39.4,
        "Reading Value": -28.05,
        "Timestamp": "2023-01-08 19:38:10"
    }
]
<end>Convert this Plain text to Yaml:
Device ID: device-0029 | Device Type: Humidity Sensor | Battery Level (%): 66.4 | Timestamp: 2022-05-19 00:25:33
Device ID: device-0020 | Device Type: Temperature Sensor | Battery Level (%): 99.9 | Timestamp: 2023-04-18 08:36:27
Device ID: device-0090 | Device Type: Pressure Sensor | Battery Level (%): 20.8 | Timestamp: 2021-01-21 14:28:32
Device ID: device-0002 | Device Type: Light Sensor | Battery Level (%): 66.4 | Timestamp: 2022-08-28 07:42:08
Device ID: device-0052 | Device Type: Temperature Sensor | Battery Level (%): 29.1 | Timestamp: 2022-06-13 14:19:24
<start>
- Battery Level (%): 66.4
  Device ID: device-0029
  Device Type: Humidity Sensor
  Timestamp: '2022-05-19 00:25:33'
- Battery Level (%): 99.9
  Device ID: device-0020
  Device Type: Temperature Sensor
  Timestamp: '2023-04-18 08:36:27'
- Battery Level (%): 20.8
  Device ID: device-0090
  Device Type: Pressure Sensor
  Timestamp: '2021-01-21 14:28:32'
- Battery Level (%): 66.4
  Device ID: device-0002
  Device Type: Light Sensor
  Timestamp: '2022-08-28 07:42:08'
- Battery Level (%): 29.1
  Device ID: device-0052
  Device Type: Temperature Sensor
  Timestamp: '2022-06-13 14:19:24'
<end>Convert this Markdown to plain text:
| Title | Director | Genre | Box Office Earnings (M) |
| --- | --- | --- | --- |
| The Endless Horizon | Talon Blackthorn | Horror | 614.52 |
| Mystery of the Depths | Rylan Frostblade | Sci-Fi | 419.4 |
| The Final Voyage | Mara Moonshadow | Thriller | 467.51 |
| Beyond the Veil | Cade Firebrand | Comedy | 747.93 |
| Dreamwalker | Orin Shadowalker | Sci-Fi | 577.54 |
| Rise of the Titans | Rylan Frostblade | Action | 747.93 |<start>
Title: The Endless Horizon | Director: Talon Blackthorn | Genre: Horror | Box Office Earnings (M): 614.52
Title: Mystery of the Depths | Director: Rylan Frostblade | Genre: Sci-Fi | Box Office Earnings (M): 419.4
Title: The Final Voyage | Director: Mara Moonshadow | Genre: Thriller | Box Office Earnings (M): 467.51
Title: Beyond the Veil | Director: Cade Firebrand | Genre: Comedy | Box Office Earnings (M): 747.93
Title: Dreamwalker | Director: Orin Shadowalker | Genre: Sci-Fi | Box Office Earnings (M): 577.54
Title: Rise of the Titans | Director: Rylan Frostblade | Genre: Action | Box Office Earnings (M): 747.93
<end>Please transform the following plain text data into CSV:
Genre: Fantasy | Box Office Earnings (M): 87.53
Genre: Drama | Box Office Earnings (M): 122.53
Genre: Comedy | Box Office Earnings (M): 726.61
<start>
Genre,Box Office Earnings (M)
Fantasy,87.53
Drama,122.53
Comedy,726.61
<end>Here's some Json data, can you convert it to MARKDOWN?
[
    {
        "Start Location": "Houston",
        "End Location": "New York",
        "Fuel Used (gallons)": 48.6
    },
    {
        "Start Location": "Houston",
        "End Location": "Phoenix",
        "Fuel Used (gallons)": 57.0
    },
    {
        "Start Location": "Denver",
        "End Location": "Phoenix",
        "Fuel Used (gallons)": 90.5
    },
    {
        "Start Location": "Chicago",
        "End Location": "New York",
        "Fuel Used (gallons)": 21.3
    },
    {
        "Start Location": "Houston",
        "End Location": "San Francisco",
        "Fuel Used (gallons)": 90.7
    },
    {
        "Start Location": "Miami",
        "End Location": "Phoenix",
        "Fuel Used (gallons)": 67.1
    },
    {
        "Start Location": "San Francisco",
        "End Location": "Miami",
        "Fuel Used (gallons)": 83.7
    },
    {
        "Start Location": "Denver",
        "End Location": "Los Angeles",
        "Fuel Used (gallons)": 62.2
    }
]<start>
| Start Location | End Location | Fuel Used (gallons) |
| --- | --- | --- |
| Houston | New York | 48.6 |
| Houston | Phoenix | 57.0 |
| Denver | Phoenix | 90.5 |
| Chicago | New York | 21.3 |
| Houston | San Francisco | 90.7 |
| Miami | Phoenix | 67.1 |
| San Francisco | Miami | 83.7 |
| Denver | Los Angeles | 62.2 |
<end>Convert this CSV to MARKDOWN:
Device ID,Location,Battery Level (%),Timestamp
device-0066,Office,32.9,2021-06-03 13:46:52
device-0018,Bathroom,69.6,2021-07-09 09:34:33
device-0038,Bathroom,40.8,2023-10-12 06:43:20
device-0079,Living Room,19.7,2021-01-25 21:38:45
device-0040,Bathroom,72.7,2023-09-05 20:35:15
device-0004,Garden,92.6,2022-11-20 19:09:44
device-0051,Living Room,52.3,2021-08-16 14:01:50
<start>
| Device ID | Location | Battery Level (%) | Timestamp |
| --- | --- | --- | --- |
| device-0066 | Office | 32.9 | 2021-06-03 13:46:52 |
| device-0018 | Bathroom | 69.6 | 2021-07-09 09:34:33 |
| device-0038 | Bathroom | 40.8 | 2023-10-12 06:43:20 |
| device-0079 | Living Room | 19.7 | 2021-01-25 21:38:45 |
| device-0040 | Bathroom | 72.7 | 2023-09-05 20:35:15 |
| device-0004 | Garden | 92.6 | 2022-11-20 19:09:44 |
| device-0051 | Living Room | 52.3 | 2021-08-16 14:01:50 |
<end>Transform this MARKDOWN structure to a Json format:
| Company | Sector | Stock Price | Annual Revenue (B) |
| --- | --- | --- | --- |
| GlobalTrade | Finance | 479.13 | 356.43 |
| HealthPlus | Biotech | 341.77 | 337.35 |
| AeroSpace | Finance | 769.73 | 73.88 |
| TechCorp | Aerospace | 615.27 | 108.22 |
| EcoEnergy | Technology | 530.94 | 345.44 |
| GlobalTrade | Aerospace | 799.24 | 337.92 |
| EcoEnergy | Healthcare | 423.77 | 473.15 |<start>
[
    {
        "Company": "GlobalTrade",
        "Sector": "Finance",
        "Stock Price": 479.13,
        "Annual Revenue (B)": 356.43
    },
    {
        "Company": "HealthPlus",
        "Sector": "Biotech",
        "Stock Price": 341.77,
        "Annual Revenue (B)": 337.35
    },
    {
        "Company": "AeroSpace",
        "Sector": "Finance",
        "Stock Price": 769.73,
        "Annual Revenue (B)": 73.88
    },
    {
        "Company": "TechCorp",
        "Sector": "Aerospace",
        "Stock Price": 615.27,
        "Annual Revenue (B)": 108.22
    },
    {
        "Company": "EcoEnergy",
        "Sector": "Technology",
        "Stock Price": 530.94,
        "Annual Revenue (B)": 345.44
    },
    {
        "Company": "GlobalTrade",
        "Sector": "Aerospace",
        "Stock Price": 799.24,
        "Annual Revenue (B)": 337.92
    },
    {
        "Company": "EcoEnergy",
        "Sector": "Healthcare",
        "Stock Price": 423.77,
        "Annual Revenue (B)": 473.15
    }
]
<end>Please transform the following MARKDOWN data into Json:
| Location | Condition | Temperature (C) | Humidity (%) | Wind Speed (km/h) | Day |
| --- | --- | --- | --- | --- | --- |
| Denver | Rainy | -7.1 | 33 | 10.3 | Saturday |
| New York | Rainy | 23.8 | 91 | 3.9 | Saturday |
| New York | Stormy | 31.7 | 53 | 0.7 | Sunday |
| Phoenix | Stormy | -8.7 | 59 | 8.3 | Thursday |
| Denver | Stormy | 21.1 | 82 | 24.1 | Tuesday |<start>
[
    {
        "Location": "Denver",
        "Condition": "Rainy",
        "Temperature (C)": -7.1,
        "Humidity (%)": 33,
        "Wind Speed (km/h)": 10.3,
        "Day": "Saturday"
    },
    {
        "Location": "New York",
        "Condition": "Rainy",
        "Temperature (C)": 23.8,
        "Humidity (%)": 91,
        "Wind Speed (km/h)": 3.9,
        "Day": "Saturday"
    },
    {
        "Location": "New York",
        "Condition": "Stormy",
        "Temperature (C)": 31.7,
        "Humidity (%)": 53,
        "Wind Speed (km/h)": 0.7,
        "Day": "Sunday"
    },
    {
        "Location": "Phoenix",
        "Condition": "Stormy",
        "Temperature (C)": -8.7,
        "Humidity (%)": 59,
        "Wind Speed (km/h)": 8.3,
        "Day": "Thursday"
    },
    {
        "Location": "Denver",
        "Condition": "Stormy",
        "Temperature (C)": 21.1,
        "Humidity (%)": 82,
        "Wind Speed (km/h)": 24.1,
        "Day": "Tuesday"
    }
]
<end>Please transform the following markdown data into Csv:
| Open Price | High Price | Low Price | Volume |
| --- | --- | --- | --- |
| 1373.84 | 1394.04 | 130.71 | 4052985 |
| 409.79 | 942.92 | 333.85 | 631567 |
| 349.78 | 1014.43 | 349.78 | 8288148 |
| 838.61 | 838.61 | 380.36 | 9743305 |
| 691.79 | 1375.1 | 500.04 | 4052985 |
| 894.42 | 894.42 | 256.66 | 2037071 |
| 223.96 | 1434.92 | 223.96 | 6833914 |
| 934.24 | 942.92 | 273.56 | 7841738 |
| 1082.07 | 1255.49 | 32.64 | 2257109 |
| 654.49 | 1373.84 | 130.75 | 2815004 |<start>
Open Price,High Price,Low Price,Volume
1373.84,1394.04,130.71,4052985
409.79,942.92,333.85,631567
349.78,1014.43,349.78,8288148
838.61,838.61,380.36,9743305
691.79,1375.1,500.04,4052985
894.42,894.42,256.66,2037071
223.96,1434.92,223.96,6833914
934.24,942.92,273.56,7841738
1082.07,1255.49,32.64,2257109
654.49,1373.84,130.75,2815004
<end>Convert this MARKDOWN to json:
| Product Name | Price | Stock Quantity | Category |
| --- | --- | --- | --- |
| Doohickey | 30.88 | 219 | Electronics |
| Instrument | 348.59 | 51 | Toys |
| Apparatus | 37.77 | 245 | Household |
| Device | 481.68 | 135 | Household |<start>
[
    {
        "Product Name": "Doohickey",
        "Price": 30.88,
        "Stock Quantity": 219,
        "Category": "Electronics"
    },
    {
        "Product Name": "Instrument",
        "Price": 348.59,
        "Stock Quantity": 51,
        "Category": "Toys"
    },
    {
        "Product Name": "Apparatus",
        "Price": 37.77,
        "Stock Quantity": 245,
        "Category": "Household"
    },
    {
        "Product Name": "Device",
        "Price": 481.68,
        "Stock Quantity": 135,
        "Category": "Household"
    }
]
<end>Here's some CSV data, can you convert it to yml?
Title,Author,Genre,Publication Year,Rating
The Silent Grove,Thorne Ironwood,Science Fiction,2020,4.2
A Journey Through Time,Draven Blackthorn,Horror,2022,1.6
Legends of the Rift,Thorne Ironwood,Horror,1958,2.7
Echoes of Eternity,Elara Moonshadow,Thriller,2008,1.9
The Crystal Key,Kara Firebrand,Romance,1991,4.9
The Silent Grove,Draven Blackthorn,Horror,1960,4.3
The Forgotten World,Elara Moonshadow,Historical,1997,2.3
<start>
- Author: Thorne Ironwood
  Genre: Science Fiction
  Publication Year: 2020
  Rating: 4.2
  Title: The Silent Grove
- Author: Draven Blackthorn
  Genre: Horror
  Publication Year: 2022
  Rating: 1.6
  Title: A Journey Through Time
- Author: Thorne Ironwood
  Genre: Horror
  Publication Year: 1958
  Rating: 2.7
  Title: Legends of the Rift
- Author: Elara Moonshadow
  Genre: Thriller
  Publication Year: 2008
  Rating: 1.9
  Title: Echoes of Eternity
- Author: Kara Firebrand
  Genre: Romance
  Publication Year: 1991
  Rating: 4.9
  Title: The Crystal Key
- Author: Draven Blackthorn
  Genre: Horror
  Publication Year: 1960
  Rating: 4.3
  Title: The Silent Grove
- Author: Elara Moonshadow
  Genre: Historical
  Publication Year: 1997
  Rating: 2.3
  Title: The Forgotten World
<end>Transform this Plain text structure to a json format:
Restaurant Name: Curry Corner | Price Range: $$$$$
Restaurant Name: Pizza Planet | Price Range: $$$$
Restaurant Name: The Golden Spoon | Price Range: $
Restaurant Name: Pasta Palace | Price Range: $$$
Restaurant Name: Burger Haven | Price Range: $$$
Restaurant Name: Burger Haven | Price Range: $$$$$
<start>
[
    {
        "Restaurant Name": "Curry Corner",
        "Price Range": "$$$$$"
    },
    {
        "Restaurant Name": "Pizza Planet",
        "Price Range": "$$$$"
    },
    {
        "Restaurant Name": "The Golden Spoon",
        "Price Range": "$"
    },
    {
        "Restaurant Name": "Pasta Palace",
        "Price Range": "$$$"
    },
    {
        "Restaurant Name": "Burger Haven",
        "Price Range": "$$$"
    },
    {
        "Restaurant Name": "Burger Haven",
        "Price Range": "$$$$$"
    }
]
<end>Transform this csv structure to a Json format:
Database Name,Queries per Second,Cache Hit Ratio (%),Connection Count
MetricsDB,1359.58,82.58,412
SessionsDB,826.52,82.39,419
SessionsDB,3060.38,89.37,387
LogsDB,4684.67,88.63,389
InventoryDB,4545.51,72.25,336
ProductsDB,4906.77,82.58,123
AnalyticsDB,3072.21,76.36,268
<start>
[
    {
        "Database Name": "MetricsDB",
        "Queries per Second": 1359.58,
        "Cache Hit Ratio (%)": 82.58,
        "Connection Count": 412
    },
    {
        "Database Name": "SessionsDB",
        "Queries per Second": 826.52,
        "Cache Hit Ratio (%)": 82.39,
        "Connection Count": 419
    },
    {
        "Database Name": "SessionsDB",
        "Queries per Second": 3060.38,
        "Cache Hit Ratio (%)": 89.37,
        "Connection Count": 387
    },
    {
        "Database Name": "LogsDB",
        "Queries per Second": 4684.67,
        "Cache Hit Ratio (%)": 88.63,
        "Connection Count": 389
    },
    {
        "Database Name": "InventoryDB",
        "Queries per Second": 4545.51,
        "Cache Hit Ratio (%)": 72.25,
        "Connection Count": 336
    },
    {
        "Database Name": "ProductsDB",
        "Queries per Second": 4906.77,
        "Cache Hit Ratio (%)": 82.58,
        "Connection Count": 123
    },
    {
        "Database Name": "AnalyticsDB",
        "Queries per Second": 3072.21,
        "Cache Hit Ratio (%)": 76.36,
        "Connection Count": 268
    }
]
<end>Please transform the following Plain text data into csv:
Location: Chicago | Temperature (C): 20.9 | Humidity (%): 52 | Wind Speed (km/h): 16.7 | Day: Sunday
Location: Los Angeles | Temperature (C): 33.4 | Humidity (%): 86 | Wind Speed (km/h): 24.1 | Day: Tuesday
Location: Denver | Temperature (C): 9.2 | Humidity (%): 70 | Wind Speed (km/h): 20.9 | Day: Saturday
Location: New York | Temperature (C): 35.6 | Humidity (%): 95 | Wind Speed (km/h): 29.3 | Day: Monday
Location: Houston | Temperature (C): 10.9 | Humidity (%): 86 | Wind Speed (km/h): 2.3 | Day: Thursday
Location: Denver | Temperature (C): 23.1 | Humidity (%): 47 | Wind Speed (km/h): 9.0 | Day: Wednesday
Location: Seattle | Temperature (C): 0.3 | Humidity (%): 60 | Wind Speed (km/h): 27.8 | Day: Tuesday
Location: Phoenix | Temperature (C): -6.8 | Humidity (%): 22 | Wind Speed (km/h): 7.4 | Day: Saturday
Location: Denver | Temperature (C): 23.1 | Humidity (%): 43 | Wind Speed (km/h): 29.3 | Day: Thursday
<start>
Location,Temperature (C),Humidity (%),Wind Speed (km/h),Day
Chicago,20.9,52,16.7,Sunday
Los Angeles,33.4,86,24.1,Tuesday
Denver,9.2,70,20.9,Saturday
New York,35.6,95,29.3,Monday
Houston,10.9,86,2.3,Thursday
Denver,23.1,47,9.0,Wednesday
Seattle,0.3,60,27.8,Tuesday
Phoenix,-6.8,22,7.4,Saturday
Denver,23.1,43,29.3,Thursday
<end>Please transform the following csv data into markdown:
Publication Year,Rating
1999,1.6
1967,3.4
1986,3.1
1999,1.9
1989,4.8
1968,3.5
1964,4.7
2008,4.6
<start>
| Publication Year | Rating |
| --- | --- |
| 1999 | 1.6 |
| 1967 | 3.4 |
| 1986 | 3.1 |
| 1999 | 1.9 |
| 1989 | 4.8 |
| 1968 | 3.5 |
| 1964 | 4.7 |
| 2008 | 4.6 |
<end>Can you change this Csv into YML?
Name,Birth Month,City,Income
Melinda,June,Columbus,150000
James,April,Detroit,140000
Carson,June,Columbus,150000
Blake,July,Nashville,270000
Kathleen,December,Portland,265000
<start>
- Birth Month: June
  City: Columbus
  Income: 150000
  Name: Melinda
- Birth Month: April
  City: Detroit
  Income: 140000
  Name: James
- Birth Month: June
  City: Columbus
  Income: 150000
  Name: Carson
- Birth Month: July
  City: Nashville
  Income: 270000
  Name: Blake
- Birth Month: December
  City: Portland
  Income: 265000
  Name: Kathleen
<end>Transform this CSV structure to a markdown format:
Device ID,Location,Reading Value
device-0061,Kitchen,-24.82
device-0063,Office,-39.65
device-0024,Hallway,49.23
device-0033,Bathroom,43.59
device-0053,Living Room,22.18
<start>
| Device ID | Location | Reading Value |
| --- | --- | --- |
| device-0061 | Kitchen | -24.82 |
| device-0063 | Office | -39.65 |
| device-0024 | Hallway | 49.23 |
| device-0033 | Bathroom | 43.59 |
| device-0053 | Living Room | 22.18 |
<end>Convert this MARKDOWN to Csv:
| Release Year | Box Office Earnings (M) |
| --- | --- |
| 1971 | 18.16 |
| 1987 | 399.74 |
| 2010 | 486.08 |
| 1995 | 486.08 |
| 2017 | 118.45 |
| 1987 | 480.89 |
| 1999 | 131.56 |
| 1990 | 195.22 |
| 2015 | 770.86 |
| 1971 | 808.32 |<start>
Release Year,Box Office Earnings (M)
1971,18.16
1987,399.74
2010,486.08
1995,486.08
2017,118.45
1987,480.89
1999,131.56
1990,195.22
2015,770.86
1971,808.32
<end>Here's some JSON data, can you convert it to Plain text?
[
    {
        "Title": "The Last Sky",
        "Author": "Sylvia Nightshade",
        "Genre": "Romance",
        "Publication Year": 1952,
        "Rating": 3.9
    },
    {
        "Title": "Tales of the Brave",
        "Author": "Rowan Ashborne",
        "Genre": "Science Fiction",
        "Publication Year": 1950,
        "Rating": 2.4
    },
    {
        "Title": "The Forgotten World",
        "Author": "Orion Frostblade",
        "Genre": "Non-Fiction",
        "Publication Year": 2007,
        "Rating": 1.4
    },
    {
        "Title": "A Journey Through Time",
        "Author": "Galen Starfire",
        "Genre": "Horror",
        "Publication Year": 2013,
        "Rating": 4.0
    },
    {
        "Title": "Legends of the Rift",
        "Author": "Rowan Ashborne",
        "Genre": "Science Fiction",
        "Publication Year": 1985,
        "Rating": 2.0
    },
    {
        "Title": "Echoes of Eternity",
        "Author": "Thorne Ironwood",
        "Genre": "Fantasy",
        "Publication Year": 1996,
        "Rating": 3.5
    },
    {
        "Title": "A Journey Through Time",
        "Author": "Isla Windrider",
        "Genre": "Horror",
        "Publication Year": 2006,
        "Rating": 4.4
    },
    {
        "Title": "Tales of the Brave",
        "Author": "Sylvia Nightshade",
        "Genre": "Historical",
        "Publication Year": 2007,
        "Rating": 1.7
    },
    {
        "Title": "Legends of the Rift",
        "Author": "Sylvia Nightshade",
        "Genre": "Horror",
        "Publication Year": 1989,
        "Rating": 4.8
    }
]<start>
Title: The Last Sky | Author: Sylvia Nightshade | Genre: Romance | Publication Year: 1952 | Rating: 3.9
Title: Tales of the Brave | Author: Rowan Ashborne | Genre: Science Fiction | Publication Year: 1950 | Rating: 2.4
Title: The Forgotten World | Author: Orion Frostblade | Genre: Non-Fiction | Publication Year: 2007 | Rating: 1.4
Title: A Journey Through Time | Author: Galen Starfire | Genre: Horror | Publication Year: 2013 | Rating: 4.0
Title: Legends of the Rift | Author: Rowan Ashborne | Genre: Science Fiction | Publication Year: 1985 | Rating: 2.0
Title: Echoes of Eternity | Author: Thorne Ironwood | Genre: Fantasy | Publication Year: 1996 | Rating: 3.5
Title: A Journey Through Time | Author: Isla Windrider | Genre: Horror | Publication Year: 2006 | Rating: 4.4
Title: Tales of the Brave | Author: Sylvia Nightshade | Genre: Historical | Publication Year: 2007 | Rating: 1.7
Title: Legends of the Rift | Author: Sylvia Nightshade | Genre: Horror | Publication Year: 1989 | Rating: 4.8
<end>Here's some JSON data, can you convert it to Markdown?
[
    {
        "Trip Name": "Desert Drive",
        "Start Location": "Houston",
        "End Location": "Los Angeles",
        "Distance (miles)": 2202.4,
        "Fuel Used (gallons)": 62.7
    },
    {
        "Trip Name": "Coast to Coast",
        "Start Location": "Chicago",
        "End Location": "New York",
        "Distance (miles)": 1763.2,
        "Fuel Used (gallons)": 75.5
    },
    {
        "Trip Name": "Mountain Adventure",
        "Start Location": "Los Angeles",
        "End Location": "Chicago",
        "Distance (miles)": 1683.4,
        "Fuel Used (gallons)": 27.0
    },
    {
        "Trip Name": "Forest Journey",
        "Start Location": "Houston",
        "End Location": "Chicago",
        "Distance (miles)": 1745.6,
        "Fuel Used (gallons)": 74.4
    },
    {
        "Trip Name": "Lakeside Retreat",
        "Start Location": "New York",
        "End Location": "Los Angeles",
        "Distance (miles)": 600.5,
        "Fuel Used (gallons)": 93.9
    },
    {
        "Trip Name": "City Explorer",
        "Start Location": "Phoenix",
        "End Location": "Houston",
        "Distance (miles)": 2018.9,
        "Fuel Used (gallons)": 5.7
    },
    {
        "Trip Name": "Lakeside Retreat",
        "Start Location": "Los Angeles",
        "End Location": "Chicago",
        "Distance (miles)": 945.8,
        "Fuel Used (gallons)": 23.7
    },
    {
        "Trip Name": "City Explorer",
        "Start Location": "Houston",
        "End Location": "Phoenix",
        "Distance (miles)": 2732.0,
        "Fuel Used (gallons)": 20.2
    }
]<start>
| Trip Name | Start Location | End Location | Distance (miles) | Fuel Used (gallons) |
| --- | --- | --- | --- | --- |
| Desert Drive | Houston | Los Angeles | 2202.4 | 62.7 |
| Coast to Coast | Chicago | New York | 1763.2 | 75.5 |
| Mountain Adventure | Los Angeles | Chicago | 1683.4 | 27.0 |
| Forest Journey | Houston | Chicago | 1745.6 | 74.4 |
| Lakeside Retreat | New York | Los Angeles | 600.5 | 93.9 |
| City Explorer | Phoenix | Houston | 2018.9 | 5.7 |
| Lakeside Retreat | Los Angeles | Chicago | 945.8 | 23.7 |
| City Explorer | Houston | Phoenix | 2732.0 | 20.2 |
<end>Please transform the following markdown data into csv:
| Restaurant Name | Rating |
| --- | --- |
| Curry Corner | 3 |
| Sushi World | 5 |
| Vegan Delight | 5 |
| Vegan Delight | 2 |
| BBQ Barn | 2 |
| Curry Corner | 4 |<start>
Restaurant Name,Rating
Curry Corner,3
Sushi World,5
Vegan Delight,5
Vegan Delight,2
BBQ Barn,2
Curry Corner,4
<end>Can you change this markdown into json?
| Author | Rating |
| --- | --- |
| Draven Blackthorn | 1.9 |
| Draven Blackthorn | 4.2 |
| Kara Firebrand | 4.2 |
| Thorne Ironwood | 3.3 |
| Draven Blackthorn | 1.3 |<start>
[
    {
        "Author": "Draven Blackthorn",
        "Rating": 1.9
    },
    {
        "Author": "Draven Blackthorn",
        "Rating": 4.2
    },
    {
        "Author": "Kara Firebrand",
        "Rating": 4.2
    },
    {
        "Author": "Thorne Ironwood",
        "Rating": 3.3
    },
    {
        "Author": "Draven Blackthorn",
        "Rating": 1.3
    }
]
<end>Can you change this MARKDOWN into json?
| Location | Condition | Wind Speed (km/h) |
| --- | --- | --- |
| Miami | Cloudy | 14.9 |
| Chicago | Windy | 15.8 |
| Miami | Foggy | 8.9 |
| Denver | Rainy | 26.2 |
| Miami | Windy | 13.3 |
| New York | Foggy | 28.6 |<start>
[
    {
        "Location": "Miami",
        "Condition": "Cloudy",
        "Wind Speed (km/h)": 14.9
    },
    {
        "Location": "Chicago",
        "Condition": "Windy",
        "Wind Speed (km/h)": 15.8
    },
    {
        "Location": "Miami",
        "Condition": "Foggy",
        "Wind Speed (km/h)": 8.9
    },
    {
        "Location": "Denver",
        "Condition": "Rainy",
        "Wind Speed (km/h)": 26.2
    },
    {
        "Location": "Miami",
        "Condition": "Windy",
        "Wind Speed (km/h)": 13.3
    },
    {
        "Location": "New York",
        "Condition": "Foggy",
        "Wind Speed (km/h)": 28.6
    }
]
<end>Convert this csv to markdown:
Title,Genre,Release Year,Box Office Earnings (M)
Edge of Infinity,Adventure,2017,52.98
Mystery of the Depths,Action,1992,504.6
The Final Voyage,Drama,1979,415.18
Rise of the Titans,Horror,1989,658.93
The Endless Horizon,Adventure,2018,85.56
Edge of Infinity,Horror,2014,725.62
Edge of Infinity,Fantasy,1981,660.94
<start>
| Title | Genre | Release Year | Box Office Earnings (M) |
| --- | --- | --- | --- |
| Edge of Infinity | Adventure | 2017 | 52.98 |
| Mystery of the Depths | Action | 1992 | 504.6 |
| The Final Voyage | Drama | 1979 | 415.18 |
| Rise of the Titans | Horror | 1989 | 658.93 |
| The Endless Horizon | Adventure | 2018 | 85.56 |
| Edge of Infinity | Horror | 2014 | 725.62 |
| Edge of Infinity | Fantasy | 1981 | 660.94 |
<end>Convert this PLAIN TEXT to markdown:
Age: 41 | Income: 200000
Age: 30 | Income: 235000
Age: 68 | Income: 465000
Age: 35 | Income: 270000
Age: 51 | Income: 470000
Age: 68 | Income: 400000
Age: 25 | Income: 250000
Age: 42 | Income: 405000
<start>
| Age | Income |
| --- | --- |
| 41 | 200000 |
| 30 | 235000 |
| 68 | 465000 |
| 35 | 270000 |
| 51 | 470000 |
| 68 | 400000 |
| 25 | 250000 |
| 42 | 405000 |
<end>Can you change this markdown into yaml?
| Location | Condition | Temperature (C) |
| --- | --- | --- |
| New York | Snowy | 20.6 |
| Phoenix | Cloudy | 25.8 |
| Los Angeles | Cloudy | 32.5 |
| Chicago | Sunny | 25.5 |<start>
- Condition: Snowy
  Location: New York
  Temperature (C): 20.6
- Condition: Cloudy
  Location: Phoenix
  Temperature (C): 25.8
- Condition: Cloudy
  Location: Los Angeles
  Temperature (C): 32.5
- Condition: Sunny
  Location: Chicago
  Temperature (C): 25.5
<end>Can you change this Json into yml?
[
    {
        "Location": "Chicago",
        "Price Range": "$$$$$"
    },
    {
        "Location": "Seattle",
        "Price Range": "$$$"
    },
    {
        "Location": "San Francisco",
        "Price Range": "$$$$$"
    },
    {
        "Location": "Houston",
        "Price Range": "$$"
    },
    {
        "Location": "New York",
        "Price Range": "$$$"
    },
    {
        "Location": "New York",
        "Price Range": "$$$$"
    },
    {
        "Location": "San Francisco",
        "Price Range": "$$$$"
    },
    {
        "Location": "Houston",
        "Price Range": "$$$"
    }
]<start>
- Location: Chicago
  Price Range: $$$$$
- Location: Seattle
  Price Range: $$$
- Location: San Francisco
  Price Range: $$$$$
- Location: Houston
  Price Range: $$
- Location: New York
  Price Range: $$$
- Location: New York
  Price Range: $$$$
- Location: San Francisco
  Price Range: $$$$
- Location: Houston
  Price Range: $$$
<end>Transform this PLAIN TEXT structure to a yaml format:
Market Cap: Mid Cap | Stock Price: 599.69 | Annual Revenue (B): 97.3 | Quarter: Q2
Market Cap: Large Cap | Stock Price: 657.41 | Annual Revenue (B): 98.07 | Quarter: Q2
Market Cap: Small Cap | Stock Price: 129.73 | Annual Revenue (B): 143.7 | Quarter: Q4
<start>
- Annual Revenue (B): 97.3
  Market Cap: Mid Cap
  Quarter: Q2
  Stock Price: 599.69
- Annual Revenue (B): 98.07
  Market Cap: Large Cap
  Quarter: Q2
  Stock Price: 657.41
- Annual Revenue (B): 143.7
  Market Cap: Small Cap
  Quarter: Q4
  Stock Price: 129.73
<end>Can you change this Markdown into plain text?
| Trip Name | Start Location | End Location | Distance (miles) | Fuel Used (gallons) |
| --- | --- | --- | --- | --- |
| Forest Journey | Chicago | Denver | 2548.9 | 91.1 |
| City Explorer | New York | Houston | 2868.3 | 65.1 |
| Coast to Coast | Miami | Chicago | 2174.4 | 21.1 |
| Forest Journey | Denver | Los Angeles | 2584.3 | 71.7 |
| Highway Odyssey | Miami | Houston | 2527.3 | 22.9 |
| Highway Odyssey | San Francisco | New York | 1104.0 | 94.1 |
| Historic Route | Chicago | Denver | 2494.8 | 56.4 |
| Canyon Trek | Miami | New York | 812.6 | 77.2 |
| Desert Drive | Houston | Miami | 2649.3 | 34.8 |
| Highway Odyssey | Phoenix | Houston | 2238.1 | 81.9 |<start>
Trip Name: Forest Journey | Start Location: Chicago | End Location: Denver | Distance (miles): 2548.9 | Fuel Used (gallons): 91.1
Trip Name: City Explorer | Start Location: New York | End Location: Houston | Distance (miles): 2868.3 | Fuel Used (gallons): 65.1
Trip Name: Coast to Coast | Start Location: Miami | End Location: Chicago | Distance (miles): 2174.4 | Fuel Used (gallons): 21.1
Trip Name: Forest Journey | Start Location: Denver | End Location: Los Angeles | Distance (miles): 2584.3 | Fuel Used (gallons): 71.7
Trip Name: Highway Odyssey | Start Location: Miami | End Location: Houston | Distance (miles): 2527.3 | Fuel Used (gallons): 22.9
Trip Name: Highway Odyssey | Start Location: San Francisco | End Location: New York | Distance (miles): 1104.0 | Fuel Used (gallons): 94.1
Trip Name: Historic Route | Start Location: Chicago | End Location: Denver | Distance (miles): 2494.8 | Fuel Used (gallons): 56.4
Trip Name: Canyon Trek | Start Location: Miami | End Location: New York | Distance (miles): 812.6 | Fuel Used (gallons): 77.2
Trip Name: Desert Drive | Start Location: Houston | End Location: Miami | Distance (miles): 2649.3 | Fuel Used (gallons): 34.8
Trip Name: Highway Odyssey | Start Location: Phoenix | End Location: Houston | Distance (miles): 2238.1 | Fuel Used (gallons): 81.9
<end>Here's some JSON data, can you convert it to yaml?
[
    {
        "Product Name": "Device",
        "SKU": "SKU-1016",
        "Price": 150.66,
        "Stock Quantity": 159,
        "Category": "Toys",
        "Supplier Name": "ACME Corp"
    },
    {
        "Product Name": "Gadget",
        "SKU": "SKU-1020",
        "Price": 90.17,
        "Stock Quantity": 64,
        "Category": "Household",
        "Supplier Name": "Globex"
    },
    {
        "Product Name": "Thingamajig",
        "SKU": "SKU-1024",
        "Price": 11.61,
        "Stock Quantity": 470,
        "Category": "Automotive",
        "Supplier Name": "Umbrella Corp"
    },
    {
        "Product Name": "Whatchamacallit",
        "SKU": "SKU-1037",
        "Price": 465.35,
        "Stock Quantity": 493,
        "Category": "Sports",
        "Supplier Name": "Wonka Industries"
    },
    {
        "Product Name": "Thingamajig",
        "SKU": "SKU-1029",
        "Price": 361.23,
        "Stock Quantity": 404,
        "Category": "Household",
        "Supplier Name": "ACME Corp"
    },
    {
        "Product Name": "Thingamajig",
        "SKU": "SKU-1092",
        "Price": 466.65,
        "Stock Quantity": 266,
        "Category": "Electronics",
        "Supplier Name": "Umbrella Corp"
    },
    {
        "Product Name": "Gizmo",
        "SKU": "SKU-1086",
        "Price": 230.89,
        "Stock Quantity": 323,
        "Category": "Sports",
        "Supplier Name": "Umbrella Corp"
    },
    {
        "Product Name": "Doohickey",
        "SKU": "SKU-1021",
        "Price": 213.39,
        "Stock Quantity": 124,
        "Category": "Household",
        "Supplier Name": "ACME Corp"
    },
    {
        "Product Name": "Widget",
        "SKU": "SKU-1057",
        "Price": 165.75,
        "Stock Quantity": 233,
        "Category": "Automotive",
        "Supplier Name": "Globex"
    }
]<start>
- Category: Toys
  Price: 150.66
  Product Name: Device
  SKU: SKU-1016
  Stock Quantity: 159
  Supplier Name: ACME Corp
- Category: Household
  Price: 90.17
  Product Name: Gadget
  SKU: SKU-1020
  Stock Quantity: 64
  Supplier Name: Globex
- Category: Automotive
  Price: 11.61
  Product Name: Thingamajig
  SKU: SKU-1024
  Stock Quantity: 470
  Supplier Name: Umbrella Corp
- Category: Sports
  Price: 465.35
  Product Name: Whatchamacallit
  SKU: SKU-1037
  Stock Quantity: 493
  Supplier Name: Wonka Industries
- Category: Household
  Price: 361.23
  Product Name: Thingamajig
  SKU: SKU-1029
  Stock Quantity: 404
  Supplier Name: ACME Corp
- Category: Electronics
  Price: 466.65
  Product Name: Thingamajig
  SKU: SKU-1092
  Stock Quantity: 266
  Supplier Name: Umbrella Corp
- Category: Sports
  Price: 230.89
  Product Name: Gizmo
  SKU: SKU-1086
  Stock Quantity: 323
  Supplier Name: Umbrella Corp
- Category: Household
  Price: 213.39
  Product Name: Doohickey
  SKU: SKU-1021
  Stock Quantity: 124
  Supplier Name: ACME Corp
- Category: Automotive
  Price: 165.75
  Product Name: Widget
  SKU: SKU-1057
  Stock Quantity: 233
  Supplier Name: Globex
<end>Can you change this Markdown into csv?
| Name | Age | Birth Month | City | Income |
| --- | --- | --- | --- | --- |
| Josephine | 60 | August | San Jose | 315000 |
| Tasha | 22 | June | Los Angeles | 105000 |
| Theodore | 45 | September | New York | 150000 |
| Johnnie | 18 | February | Milwaukee | 420000 |<start>
Name,Age,Birth Month,City,Income
Josephine,60,August,San Jose,315000
Tasha,22,June,Los Angeles,105000
Theodore,45,September,New York,150000
Johnnie,18,February,Milwaukee,420000
<end>Transform this MARKDOWN structure to a Csv format:
| Restaurant Name | Cuisine | Location | Rating | Price Range |
| --- | --- | --- | --- | --- |
| Pizza Planet | Mexican | Miami | 2 | $$$$ |
| BBQ Barn | Mediterranean | Miami | 4 | $$ |
| The Steakhouse | Chinese | Chicago | 4 | $ |
| Pasta Palace | Japanese | Los Angeles | 1 | $$$$ |
| BBQ Barn | Chinese | New York | 1 | $$ |
| Pasta Palace | Italian | Seattle | 1 | $ |<start>
Restaurant Name,Cuisine,Location,Rating,Price Range
Pizza Planet,Mexican,Miami,2,$$$$
BBQ Barn,Mediterranean,Miami,4,$$
The Steakhouse,Chinese,Chicago,4,$
Pasta Palace,Japanese,Los Angeles,1,$$$$
BBQ Barn,Chinese,New York,1,$$
Pasta Palace,Italian,Seattle,1,$
<end>Can you change this plain text into Yaml?
Device ID: device-0066 | Reading Value: 38.91 | Timestamp: 2023-08-03 20:26:42
Device ID: device-0077 | Reading Value: -22.32 | Timestamp: 2023-04-25 04:27:28
Device ID: device-0008 | Reading Value: 62.83 | Timestamp: 2021-12-20 01:28:23
Device ID: device-0095 | Reading Value: 59.71 | Timestamp: 2022-04-18 17:42:27
Device ID: device-0083 | Reading Value: 41.7 | Timestamp: 2022-10-22 12:18:47
Device ID: device-0023 | Reading Value: -30.21 | Timestamp: 2021-10-28 20:14:34
Device ID: device-0019 | Reading Value: 69.89 | Timestamp: 2022-04-20 06:17:50
Device ID: device-0024 | Reading Value: -22.32 | Timestamp: 2022-08-19 18:06:01
<start>
- Device ID: device-0066
  Reading Value: 38.91
  Timestamp: '2023-08-03 20:26:42'
- Device ID: device-0077
  Reading Value: -22.32
  Timestamp: '2023-04-25 04:27:28'
- Device ID: device-0008
  Reading Value: 62.83
  Timestamp: '2021-12-20 01:28:23'
- Device ID: device-0095
  Reading Value: 59.71
  Timestamp: '2022-04-18 17:42:27'
- Device ID: device-0083
  Reading Value: 41.7
  Timestamp: '2022-10-22 12:18:47'
- Device ID: device-0023
  Reading Value: -30.21
  Timestamp: '2021-10-28 20:14:34'
- Device ID: device-0019
  Reading Value: 69.89
  Timestamp: '2022-04-20 06:17:50'
- Device ID: device-0024
  Reading Value: -22.32
  Timestamp: '2022-08-19 18:06:01'
<end>Please transform the following Yml data into csv:
- Author: Thorne Ironwood
  Genre: Horror
  Publication Year: 2015
  Rating: 4.0
  Title: The Crystal Key
- Author: Thorne Ironwood
  Genre: Mystery
  Publication Year: 2006
  Rating: 3.1
  Title: The Last Sky
- Author: Elara Moonshadow
  Genre: Science Fiction
  Publication Year: 1999
  Rating: 4.7
  Title: The Silent Grove
- Author: Elara Moonshadow
  Genre: Non-Fiction
  Publication Year: 1952
  Rating: 3.1
  Title: Legends of the Rift
- Author: Galen Starfire
  Genre: Mystery
  Publication Year: 1999
  Rating: 2.6
  Title: The Last Sky
- Author: Galen Starfire
  Genre: Non-Fiction
  Publication Year: 2019
  Rating: 4.7
  Title: Shadows of Solitude
- Author: Isla Windrider
  Genre: Non-Fiction
  Publication Year: 1975
  Rating: 1.9
  Title: Shadows of Solitude
- Author: Draven Blackthorn
  Genre: Mystery
  Publication Year: 2023
  Rating: 3.1
  Title: The Crystal Key
- Author: Luna Silverleaf
  Genre: Thriller
  Publication Year: 1975
  Rating: 1.6
  Title: Whispers of the Abyss
<start>
Title,Author,Genre,Publication Year,Rating
The Crystal Key,Thorne Ironwood,Horror,2015,4.0
The Last Sky,Thorne Ironwood,Mystery,2006,3.1
The Silent Grove,Elara Moonshadow,Science Fiction,1999,4.7
Legends of the Rift,Elara Moonshadow,Non-Fiction,1952,3.1
The Last Sky,Galen Starfire,Mystery,1999,2.6
Shadows of Solitude,Galen Starfire,Non-Fiction,2019,4.7
Shadows of Solitude,Isla Windrider,Non-Fiction,1975,1.9
The Crystal Key,Draven Blackthorn,Mystery,2023,3.1
Whispers of the Abyss,Luna Silverleaf,Thriller,1975,1.6
<end>Here's some PLAIN TEXT data, can you convert it to Csv?
Title: Tales of the Brave | Author: Sylvia Nightshade | Genre: Mystery | Publication Year: 2021 | Rating: 1.5
Title: Echoes of Eternity | Author: Kara Firebrand | Genre: Thriller | Publication Year: 1969 | Rating: 3.1
Title: Shadows of Solitude | Author: Isla Windrider | Genre: Historical | Publication Year: 2013 | Rating: 2.4
Title: Echoes of Eternity | Author: Draven Blackthorn | Genre: Mystery | Publication Year: 1972 | Rating: 4.4
Title: The Silent Grove | Author: Sylvia Nightshade | Genre: Historical | Publication Year: 1981 | Rating: 4.8
Title: Echoes of Eternity | Author: Elara Moonshadow | Genre: Thriller | Publication Year: 1987 | Rating: 4.1
<start>
Title,Author,Genre,Publication Year,Rating
Tales of the Brave,Sylvia Nightshade,Mystery,2021,1.5
Echoes of Eternity,Kara Firebrand,Thriller,1969,3.1
Shadows of Solitude,Isla Windrider,Historical,2013,2.4
Echoes of Eternity,Draven Blackthorn,Mystery,1972,4.4
The Silent Grove,Sylvia Nightshade,Historical,1981,4.8
Echoes of Eternity,Elara Moonshadow,Thriller,1987,4.1
<end>Convert this Csv to plain text:
Location,Condition,Temperature (C),Humidity (%),Wind Speed (km/h),Day
Los Angeles,Rainy,25.6,100,24.5,Sunday
New York,Snowy,2.5,94,20.4,Wednesday
New York,Cloudy,-7.1,68,4.7,Thursday
Los Angeles,Cloudy,31.8,45,10.8,Saturday
Los Angeles,Sunny,38.6,78,4.9,Monday
Houston,Rainy,29.7,60,22.1,Monday
<start>
Location: Los Angeles | Condition: Rainy | Temperature (C): 25.6 | Humidity (%): 100 | Wind Speed (km/h): 24.5 | Day: Sunday
Location: New York | Condition: Snowy | Temperature (C): 2.5 | Humidity (%): 94 | Wind Speed (km/h): 20.4 | Day: Wednesday
Location: New York | Condition: Cloudy | Temperature (C): -7.1 | Humidity (%): 68 | Wind Speed (km/h): 4.7 | Day: Thursday
Location: Los Angeles | Condition: Cloudy | Temperature (C): 31.8 | Humidity (%): 45 | Wind Speed (km/h): 10.8 | Day: Saturday
Location: Los Angeles | Condition: Sunny | Temperature (C): 38.6 | Humidity (%): 78 | Wind Speed (km/h): 4.9 | Day: Monday
Location: Houston | Condition: Rainy | Temperature (C): 29.7 | Humidity (%): 60 | Wind Speed (km/h): 22.1 | Day: Monday
<end>Here's some Csv data, can you convert it to YML?
Company,High Price,Low Price,Volume
FinanceTrust,1410.01,770.02,3639333
FoodChain,265.25,133.67,8880479
TechnoCorp,1331.77,91.92,1526557
RetailWorld,792.85,716.83,2164332
AutoMotive,1218.82,788.67,8683236
GreenEnergy,1156.69,24.58,7637488
FoodChain,1111.29,441.45,1498173
RetailWorld,1468.19,104.19,825678
BioLife,1032.0,486.64,7727828
<start>
- Company: FinanceTrust
  High Price: 1410.01
  Low Price: 770.02
  Volume: 3639333
- Company: FoodChain
  High Price: 265.25
  Low Price: 133.67
  Volume: 8880479
- Company: TechnoCorp
  High Price: 1331.77
  Low Price: 91.92
  Volume: 1526557
- Company: RetailWorld
  High Price: 792.85
  Low Price: 716.83
  Volume: 2164332
- Company: AutoMotive
  High Price: 1218.82
  Low Price: 788.67
  Volume: 8683236
- Company: GreenEnergy
  High Price: 1156.69
  Low Price: 24.58
  Volume: 7637488
- Company: FoodChain
  High Price: 1111.29
  Low Price: 441.45
  Volume: 1498173
- Company: RetailWorld
  High Price: 1468.19
  Low Price: 104.19
  Volume: 825678
- Company: BioLife
  High Price: 1032.0
  Low Price: 486.64
  Volume: 7727828
<end>Can you change this csv into json?
Company,Date,Open Price,Close Price,High Price,Low Price,Volume
FoodChain,2014-04-12,1216.43,168.13,1216.43,168.13,1779476
FoodChain,2016-09-18,282.72,787.0,787.0,282.72,7204410
GreenEnergy,2017-06-04,508.26,1085.43,1085.43,508.26,8919515
HealthGen,2019-06-24,689.68,718.16,718.16,689.68,2820715
HealthGen,2016-05-26,1059.78,582.36,1295.34,55.0,6401868
MediaGroup,2021-04-08,335.36,508.26,537.56,335.36,7410275
<start>
[
    {
        "Company": "FoodChain",
        "Date": "2014-04-12",
        "Open Price": 1216.43,
        "Close Price": 168.13,
        "High Price": 1216.43,
        "Low Price": 168.13,
        "Volume": 1779476
    },
    {
        "Company": "FoodChain",
        "Date": "2016-09-18",
        "Open Price": 282.72,
        "Close Price": 787.0,
        "High Price": 787.0,
        "Low Price": 282.72,
        "Volume": 7204410
    },
    {
        "Company": "GreenEnergy",
        "Date": "2017-06-04",
        "Open Price": 508.26,
        "Close Price": 1085.43,
        "High Price": 1085.43,
        "Low Price": 508.26,
        "Volume": 8919515
    },
    {
        "Company": "HealthGen",
        "Date": "2019-06-24",
        "Open Price": 689.68,
        "Close Price": 718.16,
        "High Price": 718.16,
        "Low Price": 689.68,
        "Volume": 2820715
    },
    {
        "Company": "HealthGen",
        "Date": "2016-05-26",
        "Open Price": 1059.78,
        "Close Price": 582.36,
        "High Price": 1295.34,
        "Low Price": 55.0,
        "Volume": 6401868
    },
    {
        "Company": "MediaGroup",
        "Date": "2021-04-08",
        "Open Price": 335.36,
        "Close Price": 508.26,
        "High Price": 537.56,
        "Low Price": 335.36,
        "Volume": 7410275
    }
]
<end>Here's some JSON data, can you convert it to markdown?
[
    {
        "Age": 31,
        "Birth Month": "August",
        "City": "Oklahoma City",
        "Income": 260000
    },
    {
        "Age": 59,
        "Birth Month": "July",
        "City": "Baltimore",
        "Income": 95000
    },
    {
        "Age": 55,
        "Birth Month": "December",
        "City": "Jacksonville",
        "Income": 305000
    },
    {
        "Age": 35,
        "Birth Month": "November",
        "City": "Boston",
        "Income": 420000
    }
]<start>
| Age | Birth Month | City | Income |
| --- | --- | --- | --- |
| 31 | August | Oklahoma City | 260000 |
| 59 | July | Baltimore | 95000 |
| 55 | December | Jacksonville | 305000 |
| 35 | November | Boston | 420000 |
<end>Here's some Plain text data, can you convert it to Markdown?
Genre: Fantasy | Release Year: 1998
Genre: Fantasy | Release Year: 2014
Genre: Horror | Release Year: 1998
Genre: Thriller | Release Year: 1978
Genre: Comedy | Release Year: 1995
<start>
| Genre | Release Year |
| --- | --- |
| Fantasy | 1998 |
| Fantasy | 2014 |
| Horror | 1998 |
| Thriller | 1978 |
| Comedy | 1995 |
<end>Transform this MARKDOWN structure to a JSON format:
| Product Name | SKU | Stock Quantity | Supplier Name |
| --- | --- | --- | --- |
| Widget | SKU-1008 | 376 | Wayne Enterprises |
| Gadget | SKU-1064 | 395 | Wayne Enterprises |
| Contraption | SKU-1048 | 31 | ACME Corp |
| Doohickey | SKU-1098 | 10 | Umbrella Corp |
| Instrument | SKU-1079 | 182 | Umbrella Corp |<start>
[
    {
        "Product Name": "Widget",
        "SKU": "SKU-1008",
        "Stock Quantity": 376,
        "Supplier Name": "Wayne Enterprises"
    },
    {
        "Product Name": "Gadget",
        "SKU": "SKU-1064",
        "Stock Quantity": 395,
        "Supplier Name": "Wayne Enterprises"
    },
    {
        "Product Name": "Contraption",
        "SKU": "SKU-1048",
        "Stock Quantity": 31,
        "Supplier Name": "ACME Corp"
    },
    {
        "Product Name": "Doohickey",
        "SKU": "SKU-1098",
        "Stock Quantity": 10,
        "Supplier Name": "Umbrella Corp"
    },
    {
        "Product Name": "Instrument",
        "SKU": "SKU-1079",
        "Stock Quantity": 182,
        "Supplier Name": "Umbrella Corp"
    }
]
<end>Here's some Json data, can you convert it to yaml?
[
    {
        "End Location": "San Francisco",
        "Duration (hours)": 45.2,
        "Fuel Used (gallons)": 66.7
    },
    {
        "End Location": "San Francisco",
        "Duration (hours)": 61.1,
        "Fuel Used (gallons)": 98.7
    },
    {
        "End Location": "Phoenix",
        "Duration (hours)": 49.2,
        "Fuel Used (gallons)": 27.5
    },
    {
        "End Location": "Phoenix",
        "Duration (hours)": 57.0,
        "Fuel Used (gallons)": 95.0
    }
]<start>
- Duration (hours): 45.2
  End Location: San Francisco
  Fuel Used (gallons): 66.7
- Duration (hours): 61.1
  End Location: San Francisco
  Fuel Used (gallons): 98.7
- Duration (hours): 49.2
  End Location: Phoenix
  Fuel Used (gallons): 27.5
- Duration (hours): 57.0
  End Location: Phoenix
  Fuel Used (gallons): 95.0
<end>Please transform the following csv data into Markdown:
Company,Close Price,High Price,Low Price
AutoMotive,303.03,1249.98,259.17
AeroSystems,873.91,873.91,140.95
TechnoCorp,112.88,1342.08,50.98
<start>
| Company | Close Price | High Price | Low Price |
| --- | --- | --- | --- |
| AutoMotive | 303.03 | 1249.98 | 259.17 |
| AeroSystems | 873.91 | 873.91 | 140.95 |
| TechnoCorp | 112.88 | 1342.08 | 50.98 |
<end>Convert this YAML to markdown:
- Cuisine: Chinese
  Restaurant Name: Pasta Palace
- Cuisine: Chinese
  Restaurant Name: The Steakhouse
- Cuisine: Japanese
  Restaurant Name: Curry Corner
- Cuisine: Indian
  Restaurant Name: The Golden Spoon
- Cuisine: Indian
  Restaurant Name: Vegan Delight
- Cuisine: Japanese
  Restaurant Name: Pizza Planet
<start>
| Restaurant Name | Cuisine |
| --- | --- |
| Pasta Palace | Chinese |
| The Steakhouse | Chinese |
| Curry Corner | Japanese |
| The Golden Spoon | Indian |
| Vegan Delight | Indian |
| Pizza Planet | Japanese |
<end>Here's some plain text data, can you convert it to csv?
Company: GreenEnergy | Date: 2011-08-05 | Close Price: 1084.99 | High Price: 1084.99 | Volume: 6149460
Company: RetailWorld | Date: 2019-09-03 | Close Price: 786.27 | High Price: 786.27 | Volume: 5848803
Company: HealthGen | Date: 2021-03-22 | Close Price: 843.06 | High Price: 1169.71 | Volume: 9650609
Company: HealthGen | Date: 2010-07-14 | Close Price: 1251.23 | High Price: 1251.23 | Volume: 2511982
Company: BioLife | Date: 2019-01-10 | Close Price: 242.87 | High Price: 631.72 | Volume: 1313393
Company: AutoMotive | Date: 2023-06-11 | Close Price: 1169.71 | High Price: 1169.71 | Volume: 9263021
Company: GreenEnergy | Date: 2010-08-02 | Close Price: 332.25 | High Price: 1210.85 | Volume: 1195576
<start>
Company,Date,Close Price,High Price,Volume
GreenEnergy,2011-08-05,1084.99,1084.99,6149460
RetailWorld,2019-09-03,786.27,786.27,5848803
HealthGen,2021-03-22,843.06,1169.71,9650609
HealthGen,2010-07-14,1251.23,1251.23,2511982
BioLife,2019-01-10,242.87,631.72,1313393
AutoMotive,2023-06-11,1169.71,1169.71,9263021
GreenEnergy,2010-08-02,332.25,1210.85,1195576
<end>Convert this csv to yaml:
Company,Sector,Market Cap,Stock Price,Annual Revenue (B),Quarter
AeroSpace,Biotech,Mid Cap,627.5,77.74,Q2
Foodies,Energy,Mid Cap,274.68,445.32,Q2
RetailHub,Healthcare,Small Cap,414.79,190.43,Q3
RetailHub,Energy,Mid Cap,895.34,411.31,Q4
FinanceWorks,Healthcare,Small Cap,265.42,466.38,Q1
AutoDrive,Energy,Mega Cap,741.98,86.66,Q1
EcoEnergy,Automotive,Mid Cap,200.02,116.19,Q1
RetailHub,Energy,Small Cap,217.1,448.55,Q3
<start>
- Annual Revenue (B): 77.74
  Company: AeroSpace
  Market Cap: Mid Cap
  Quarter: Q2
  Sector: Biotech
  Stock Price: 627.5
- Annual Revenue (B): 445.32
  Company: Foodies
  Market Cap: Mid Cap
  Quarter: Q2
  Sector: Energy
  Stock Price: 274.68
- Annual Revenue (B): 190.43
  Company: RetailHub
  Market Cap: Small Cap
  Quarter: Q3
  Sector: Healthcare
  Stock Price: 414.79
- Annual Revenue (B): 411.31
  Company: RetailHub
  Market Cap: Mid Cap
  Quarter: Q4
  Sector: Energy
  Stock Price: 895.34
- Annual Revenue (B): 466.38
  Company: FinanceWorks
  Market Cap: Small Cap
  Quarter: Q1
  Sector: Healthcare
  Stock Price: 265.42
- Annual Revenue (B): 86.66
  Company: AutoDrive
  Market Cap: Mega Cap
  Quarter: Q1
  Sector: Energy
  Stock Price: 741.98
- Annual Revenue (B): 116.19
  Company: EcoEnergy
  Market Cap: Mid Cap
  Quarter: Q1
  Sector: Automotive
  Stock Price: 200.02
- Annual Revenue (B): 448.55
  Company: RetailHub
  Market Cap: Small Cap
  Quarter: Q3
  Sector: Energy
  Stock Price: 217.1
<end>Here's some CSV data, can you convert it to Json?
Restaurant Name,Cuisine,Location,Rating,Price Range
Burger Haven,Italian,New York,4,$$$
The Golden Spoon,Indian,Chicago,4,$$$
Burger Haven,Indian,Miami,3,$$$$
The Golden Spoon,American,San Francisco,3,$
The Steakhouse,Japanese,Seattle,1,$
Curry Corner,Chinese,Chicago,5,$$$
Taco Town,Indian,Chicago,1,$$$$$
<start>
[
    {
        "Restaurant Name": "Burger Haven",
        "Cuisine": "Italian",
        "Location": "New York",
        "Rating": 4,
        "Price Range": "$$$"
    },
    {
        "Restaurant Name": "The Golden Spoon",
        "Cuisine": "Indian",
        "Location": "Chicago",
        "Rating": 4,
        "Price Range": "$$$"
    },
    {
        "Restaurant Name": "Burger Haven",
        "Cuisine": "Indian",
        "Location": "Miami",
        "Rating": 3,
        "Price Range": "$$$$"
    },
    {
        "Restaurant Name": "The Golden Spoon",
        "Cuisine": "American",
        "Location": "San Francisco",
        "Rating": 3,
        "Price Range": "$"
    },
    {
        "Restaurant Name": "The Steakhouse",
        "Cuisine": "Japanese",
        "Location": "Seattle",
        "Rating": 1,
        "Price Range": "$"
    },
    {
        "Restaurant Name": "Curry Corner",
        "Cuisine": "Chinese",
        "Location": "Chicago",
        "Rating": 5,
        "Price Range": "$$$"
    },
    {
        "Restaurant Name": "Taco Town",
        "Cuisine": "Indian",
        "Location": "Chicago",
        "Rating": 1,
        "Price Range": "$$$$$"
    }
]
<end>Convert this YAML to CSV:
- Battery Level (%): 46.6
  Device Type: Humidity Sensor
  Location: Living Room
  Reading Value: 9.45
  Timestamp: '2023-01-23 01:47:07'
- Battery Level (%): 95.6
  Device Type: Temperature Sensor
  Location: Office
  Reading Value: 72.14
  Timestamp: '2022-03-24 06:25:20'
- Battery Level (%): 68.7
  Device Type: Temperature Sensor
  Location: Kitchen
  Reading Value: -8.43
  Timestamp: '2023-06-17 07:59:18'
- Battery Level (%): 54.8
  Device Type: Humidity Sensor
  Location: Garage
  Reading Value: 50.34
  Timestamp: '2021-03-07 05:16:15'
- Battery Level (%): 79.4
  Device Type: Temperature Sensor
  Location: Office
  Reading Value: -37.13
  Timestamp: '2023-04-15 13:35:09'
- Battery Level (%): 52.2
  Device Type: Light Sensor
  Location: Garden
  Reading Value: 61.01
  Timestamp: '2023-04-09 13:29:53'
- Battery Level (%): 67.8
  Device Type: Humidity Sensor
  Location: Bedroom
  Reading Value: 61.12
  Timestamp: '2021-11-05 16:56:19'
- Battery Level (%): 54.1
  Device Type: Pressure Sensor
  Location: Hallway
  Reading Value: -9.2
  Timestamp: '2021-08-10 09:14:11'
- Battery Level (%): 13.4
  Device Type: Motion Detector
  Location: Hallway
  Reading Value: 48.28
  Timestamp: '2023-01-26 00:20:37'
<start>
Device Type,Location,Battery Level (%),Reading Value,Timestamp
Humidity Sensor,Living Room,46.6,9.45,2023-01-23 01:47:07
Temperature Sensor,Office,95.6,72.14,2022-03-24 06:25:20
Temperature Sensor,Kitchen,68.7,-8.43,2023-06-17 07:59:18
Humidity Sensor,Garage,54.8,50.34,2021-03-07 05:16:15
Temperature Sensor,Office,79.4,-37.13,2023-04-15 13:35:09
Light Sensor,Garden,52.2,61.01,2023-04-09 13:29:53
Humidity Sensor,Bedroom,67.8,61.12,2021-11-05 16:56:19
Pressure Sensor,Hallway,54.1,-9.2,2021-08-10 09:14:11
Motion Detector,Hallway,13.4,48.28,2023-01-26 00:20:37
<end>Please transform the following csv data into json:
Name,City,Income
Krista,Boston,285000
Kingston,Las Vegas,490000
Priscilla,San Jose,55000
<start>
[
    {
        "Name": "Krista",
        "City": "Boston",
        "Income": 285000
    },
    {
        "Name": "Kingston",
        "City": "Las Vegas",
        "Income": 490000
    },
    {
        "Name": "Priscilla",
        "City": "San Jose",
        "Income": 55000
    }
]
<end>Please transform the following Markdown data into csv:
| Author | Publication Year |
| --- | --- |
| Galen Starfire | 1965 |
| Elara Moonshadow | 1995 |
| Orion Frostblade | 1971 |
| Galen Starfire | 1951 |
| Luna Silverleaf | 1957 |
| Thorne Ironwood | 2004 |
| Thorne Ironwood | 1950 |
| Thorne Ironwood | 2009 |
| Isla Windrider | 1998 |<start>
Author,Publication Year
Galen Starfire,1965
Elara Moonshadow,1995
Orion Frostblade,1971
Galen Starfire,1951
Luna Silverleaf,1957
Thorne Ironwood,2004
Thorne Ironwood,1950
Thorne Ironwood,2009
Isla Windrider,1998
<end>Transform this markdown structure to a yaml format:
| Product Name | Price | Category |
| --- | --- | --- |
| Gadget | 299.75 | Toys |
| Whatchamacallit | 57.54 | Household |
| Contraption | 17.46 | Sports |
| Instrument | 153.94 | Toys |
| Thingamajig | 207.6 | Toys |
| Thingamajig | 442.68 | Toys |
| Widget | 172.88 | Toys |
| Gizmo | 266.56 | Electronics |<start>
- Category: Toys
  Price: 299.75
  Product Name: Gadget
- Category: Household
  Price: 57.54
  Product Name: Whatchamacallit
- Category: Sports
  Price: 17.46
  Product Name: Contraption
- Category: Toys
  Price: 153.94
  Product Name: Instrument
- Category: Toys
  Price: 207.6
  Product Name: Thingamajig
- Category: Toys
  Price: 442.68
  Product Name: Thingamajig
- Category: Toys
  Price: 172.88
  Product Name: Widget
- Category: Electronics
  Price: 266.56
  Product Name: Gizmo
<end>Convert this Yml to PLAIN TEXT:
- Age: 57
  City: San Francisco
  Income: 430000
  Name: Asher
- Age: 62
  City: Denver
  Income: 495000
  Name: Harry
- Age: 54
  City: San Jose
  Income: 300000
  Name: Joshua
- Age: 66
  City: Washington
  Income: 60000
  Name: Jaxon
- Age: 37
  City: Memphis
  Income: 70000
  Name: Faye
<start>
Name: Asher | Age: 57 | City: San Francisco | Income: 430000
Name: Harry | Age: 62 | City: Denver | Income: 495000
Name: Joshua | Age: 54 | City: San Jose | Income: 300000
Name: Jaxon | Age: 66 | City: Washington | Income: 60000
Name: Faye | Age: 37 | City: Memphis | Income: 70000
<end>Convert this Markdown to json:
| Name | Age | Income |
| --- | --- | --- |
| Isabel | 26 | 140000 |
| Oscar | 33 | 85000 |
| Vincent | 19 | 315000 |
| April | 27 | 330000 |
| Suzanne | 53 | 455000 |
| Cindy | 29 | 320000 |<start>
[
    {
        "Name": "Isabel",
        "Age": 26,
        "Income": 140000
    },
    {
        "Name": "Oscar",
        "Age": 33,
        "Income": 85000
    },
    {
        "Name": "Vincent",
        "Age": 19,
        "Income": 315000
    },
    {
        "Name": "April",
        "Age": 27,
        "Income": 330000
    },
    {
        "Name": "Suzanne",
        "Age": 53,
        "Income": 455000
    },
    {
        "Name": "Cindy",
        "Age": 29,
        "Income": 320000
    }
]
<end>Convert this PLAIN TEXT to json:
Sector: Aerospace | Stock Price: 351.53 | Quarter: Q2
Sector: Finance | Stock Price: 759.24 | Quarter: Q3
Sector: Technology | Stock Price: 599.21 | Quarter: Q1
Sector: Technology | Stock Price: 380.87 | Quarter: Q4
Sector: Energy | Stock Price: 329.29 | Quarter: Q4
Sector: Healthcare | Stock Price: 166.45 | Quarter: Q2
Sector: Energy | Stock Price: 380.87 | Quarter: Q4
Sector: Healthcare | Stock Price: 80.24 | Quarter: Q3
Sector: Finance | Stock Price: 426.54 | Quarter: Q1
<start>
[
    {
        "Sector": "Aerospace",
        "Stock Price": 351.53,
        "Quarter": "Q2"
    },
    {
        "Sector": "Finance",
        "Stock Price": 759.24,
        "Quarter": "Q3"
    },
    {
        "Sector": "Technology",
        "Stock Price": 599.21,
        "Quarter": "Q1"
    },
    {
        "Sector": "Technology",
        "Stock Price": 380.87,
        "Quarter": "Q4"
    },
    {
        "Sector": "Energy",
        "Stock Price": 329.29,
        "Quarter": "Q4"
    },
    {
        "Sector": "Healthcare",
        "Stock Price": 166.45,
        "Quarter": "Q2"
    },
    {
        "Sector": "Energy",
        "Stock Price": 380.87,
        "Quarter": "Q4"
    },
    {
        "Sector": "Healthcare",
        "Stock Price": 80.24,
        "Quarter": "Q3"
    },
    {
        "Sector": "Finance",
        "Stock Price": 426.54,
        "Quarter": "Q1"
    }
]
<end>Convert this Csv to MARKDOWN:
Location,Condition,Temperature (C),Humidity (%),Wind Speed (km/h),Day
Los Angeles,Stormy,32.7,30,28.2,Friday
Miami,Foggy,33.4,61,10.3,Friday
Miami,Sunny,9.1,76,18.3,Wednesday
Seattle,Stormy,7.8,88,16.4,Wednesday
Chicago,Snowy,-3.5,76,23.5,Monday
Miami,Snowy,5.7,51,4.9,Saturday
Los Angeles,Snowy,15.6,80,10.0,Sunday
<start>
| Location | Condition | Temperature (C) | Humidity (%) | Wind Speed (km/h) | Day |
| --- | --- | --- | --- | --- | --- |
| Los Angeles | Stormy | 32.7 | 30 | 28.2 | Friday |
| Miami | Foggy | 33.4 | 61 | 10.3 | Friday |
| Miami | Sunny | 9.1 | 76 | 18.3 | Wednesday |
| Seattle | Stormy | 7.8 | 88 | 16.4 | Wednesday |
| Chicago | Snowy | -3.5 | 76 | 23.5 | Monday |
| Miami | Snowy | 5.7 | 51 | 4.9 | Saturday |
| Los Angeles | Snowy | 15.6 | 80 | 10.0 | Sunday |
<end>Convert this Csv to plain text:
Queries per Second,Connection Count,Average Latency (ms),Timestamp
1140.8,51,46.39,2021-07-23 06:06:31
3095.08,72,30.29,2021-05-08 15:54:57
4581.3,247,77.4,2023-01-25 09:41:54
3205.04,398,69.89,2022-06-08 22:47:30
3671.3,137,43.67,2021-01-27 05:39:32
1492.11,66,29.14,2022-01-06 05:17:22
<start>
Queries per Second: 1140.8 | Connection Count: 51 | Average Latency (ms): 46.39 | Timestamp: 2021-07-23 06:06:31
Queries per Second: 3095.08 | Connection Count: 72 | Average Latency (ms): 30.29 | Timestamp: 2021-05-08 15:54:57
Queries per Second: 4581.3 | Connection Count: 247 | Average Latency (ms): 77.4 | Timestamp: 2023-01-25 09:41:54
Queries per Second: 3205.04 | Connection Count: 398 | Average Latency (ms): 69.89 | Timestamp: 2022-06-08 22:47:30
Queries per Second: 3671.3 | Connection Count: 137 | Average Latency (ms): 43.67 | Timestamp: 2021-01-27 05:39:32
Queries per Second: 1492.11 | Connection Count: 66 | Average Latency (ms): 29.14 | Timestamp: 2022-01-06 05:17:22
<end>Here's some csv data, can you convert it to markdown?
Title,Author,Genre,Publication Year,Rating
Legends of the Rift,Isla Windrider,Mystery,1983,1.3
The Forgotten World,Draven Blackthorn,Historical,2005,3.9
The Last Sky,Elara Moonshadow,Fantasy,2013,1.8
A Journey Through Time,Galen Starfire,Horror,1962,1.3
Legends of the Rift,Sylvia Nightshade,Thriller,2008,1.9
<start>
| Title | Author | Genre | Publication Year | Rating |
| --- | --- | --- | --- | --- |
| Legends of the Rift | Isla Windrider | Mystery | 1983 | 1.3 |
| The Forgotten World | Draven Blackthorn | Historical | 2005 | 3.9 |
| The Last Sky | Elara Moonshadow | Fantasy | 2013 | 1.8 |
| A Journey Through Time | Galen Starfire | Horror | 1962 | 1.3 |
| Legends of the Rift | Sylvia Nightshade | Thriller | 2008 | 1.9 |
<end>Transform this markdown structure to a Csv format:
| Author | Genre | Publication Year | Rating |
| --- | --- | --- | --- |
| Elara Moonshadow | Horror | 1954 | 2.4 |
| Rowan Ashborne | Thriller | 1963 | 1.8 |
| Luna Silverleaf | Romance | 2008 | 3.6 |
| Rowan Ashborne | Mystery | 1950 | 3.6 |<start>
Author,Genre,Publication Year,Rating
Elara Moonshadow,Horror,1954,2.4
Rowan Ashborne,Thriller,1963,1.8
Luna Silverleaf,Romance,2008,3.6
Rowan Ashborne,Mystery,1950,3.6
<end>Convert this csv to PLAIN TEXT:
Trip Name,Start Location,Distance (miles)
Historic Route,Miami,834.7
Lakeside Retreat,Denver,1434.3
Valley Voyage,Miami,2097.5
Historic Route,Chicago,485.2
Historic Route,New York,278.1
Lakeside Retreat,Houston,770.2
Forest Journey,Denver,2915.5
<start>
Trip Name: Historic Route | Start Location: Miami | Distance (miles): 834.7
Trip Name: Lakeside Retreat | Start Location: Denver | Distance (miles): 1434.3
Trip Name: Valley Voyage | Start Location: Miami | Distance (miles): 2097.5
Trip Name: Historic Route | Start Location: Chicago | Distance (miles): 485.2
Trip Name: Historic Route | Start Location: New York | Distance (miles): 278.1
Trip Name: Lakeside Retreat | Start Location: Houston | Distance (miles): 770.2
Trip Name: Forest Journey | Start Location: Denver | Distance (miles): 2915.5
<end>Please transform the following MARKDOWN data into yaml:
| Trip Name | Start Location | End Location | Duration (hours) |
| --- | --- | --- | --- |
| Highway Odyssey | Chicago | San Francisco | 8.6 |
| Forest Journey | Chicago | Los Angeles | 58.6 |
| City Explorer | New York | Phoenix | 62.8 |
| Valley Voyage | Denver | Miami | 22.8 |
| Highway Odyssey | Chicago | New York | 31.2 |<start>
- Duration (hours): 8.6
  End Location: San Francisco
  Start Location: Chicago
  Trip Name: Highway Odyssey
- Duration (hours): 58.6
  End Location: Los Angeles
  Start Location: Chicago
  Trip Name: Forest Journey
- Duration (hours): 62.8
  End Location: Phoenix
  Start Location: New York
  Trip Name: City Explorer
- Duration (hours): 22.8
  End Location: Miami
  Start Location: Denver
  Trip Name: Valley Voyage
- Duration (hours): 31.2
  End Location: New York
  Start Location: Chicago
  Trip Name: Highway Odyssey
<end>Convert this csv to Markdown:
Location,Condition,Temperature (C),Humidity (%),Wind Speed (km/h),Day
Miami,Stormy,10.1,28,17.2,Tuesday
Denver,Windy,22.4,55,19.4,Monday
Houston,Foggy,22.0,96,26.7,Wednesday
Phoenix,Cloudy,-0.8,93,27.9,Sunday
Denver,Snowy,22.4,63,6.4,Tuesday
Houston,Rainy,34.5,89,22.1,Tuesday
Chicago,Windy,36.9,63,17.2,Saturday
Miami,Rainy,36.0,52,11.1,Thursday
Phoenix,Snowy,2.2,23,6.0,Tuesday
Denver,Sunny,19.1,28,2.2,Friday
<start>
| Location | Condition | Temperature (C) | Humidity (%) | Wind Speed (km/h) | Day |
| --- | --- | --- | --- | --- | --- |
| Miami | Stormy | 10.1 | 28 | 17.2 | Tuesday |
| Denver | Windy | 22.4 | 55 | 19.4 | Monday |
| Houston | Foggy | 22.0 | 96 | 26.7 | Wednesday |
| Phoenix | Cloudy | -0.8 | 93 | 27.9 | Sunday |
| Denver | Snowy | 22.4 | 63 | 6.4 | Tuesday |
| Houston | Rainy | 34.5 | 89 | 22.1 | Tuesday |
| Chicago | Windy | 36.9 | 63 | 17.2 | Saturday |
| Miami | Rainy | 36.0 | 52 | 11.1 | Thursday |
| Phoenix | Snowy | 2.2 | 23 | 6.0 | Tuesday |
| Denver | Sunny | 19.1 | 28 | 2.2 | Friday |
<end>Here's some YAML data, can you convert it to plain text?
- Battery Level (%): 29.9
  Device ID: device-0049
  Reading Value: 40.66
  Timestamp: '2023-04-21 12:56:27'
- Battery Level (%): 27.0
  Device ID: device-0092
  Reading Value: 2.45
  Timestamp: '2022-07-07 14:37:59'
- Battery Level (%): 67.8
  Device ID: device-0035
  Reading Value: 73.65
  Timestamp: '2022-06-05 04:38:03'
- Battery Level (%): 75.7
  Device ID: device-0003
  Reading Value: -29.6
  Timestamp: '2022-12-14 10:09:02'
- Battery Level (%): 38.2
  Device ID: device-0042
  Reading Value: -39.49
  Timestamp: '2022-02-09 09:00:13'
<start>
Device ID: device-0049 | Battery Level (%): 29.9 | Reading Value: 40.66 | Timestamp: 2023-04-21 12:56:27
Device ID: device-0092 | Battery Level (%): 27.0 | Reading Value: 2.45 | Timestamp: 2022-07-07 14:37:59
Device ID: device-0035 | Battery Level (%): 67.8 | Reading Value: 73.65 | Timestamp: 2022-06-05 04:38:03
Device ID: device-0003 | Battery Level (%): 75.7 | Reading Value: -29.6 | Timestamp: 2022-12-14 10:09:02
Device ID: device-0042 | Battery Level (%): 38.2 | Reading Value: -39.49 | Timestamp: 2022-02-09 09:00:13
<end>Please transform the following plain text data into YML:
Title: Whispers of the Abyss | Genre: Historical | Publication Year: 1999 | Rating: 5.0
Title: The Silent Grove | Genre: Romance | Publication Year: 1957 | Rating: 4.8
Title: The Silent Grove | Genre: Fantasy | Publication Year: 1985 | Rating: 3.7
Title: The Forgotten World | Genre: Fantasy | Publication Year: 1974 | Rating: 2.6
Title: Legends of the Rift | Genre: Science Fiction | Publication Year: 1962 | Rating: 2.8
<start>
- Genre: Historical
  Publication Year: 1999
  Rating: 5.0
  Title: Whispers of the Abyss
- Genre: Romance
  Publication Year: 1957
  Rating: 4.8
  Title: The Silent Grove
- Genre: Fantasy
  Publication Year: 1985
  Rating: 3.7
  Title: The Silent Grove
- Genre: Fantasy
  Publication Year: 1974
  Rating: 2.6
  Title: The Forgotten World
- Genre: Science Fiction
  Publication Year: 1962
  Rating: 2.8
  Title: Legends of the Rift
<end>Here's some markdown data, can you convert it to JSON?
| Cuisine | Location | Rating |
| --- | --- | --- |
| Mexican | Chicago | 2 |
| Mexican | Seattle | 3 |
| Italian | New York | 5 |
| Indian | Chicago | 5 |
| Japanese | Miami | 5 |
| Italian | San Francisco | 4 |
| Chinese | Chicago | 3 |<start>
[
    {
        "Cuisine": "Mexican",
        "Location": "Chicago",
        "Rating": 2
    },
    {
        "Cuisine": "Mexican",
        "Location": "Seattle",
        "Rating": 3
    },
    {
        "Cuisine": "Italian",
        "Location": "New York",
        "Rating": 5
    },
    {
        "Cuisine": "Indian",
        "Location": "Chicago",
        "Rating": 5
    },
    {
        "Cuisine": "Japanese",
        "Location": "Miami",
        "Rating": 5
    },
    {
        "Cuisine": "Italian",
        "Location": "San Francisco",
        "Rating": 4
    },
    {
        "Cuisine": "Chinese",
        "Location": "Chicago",
        "Rating": 3
    }
]
<end>Here's some Yml data, can you convert it to Markdown?
- Company: BioPharm
  Market Cap: Mega Cap
  Stock Price: 625.7
- Company: BioPharm
  Market Cap: Mid Cap
  Stock Price: 886.61
- Company: EcoEnergy
  Market Cap: Large Cap
  Stock Price: 902.05
- Company: GlobalTrade
  Market Cap: Small Cap
  Stock Price: 220.86
- Company: GlobalTrade
  Market Cap: Mid Cap
  Stock Price: 515.83
<start>
| Company | Market Cap | Stock Price |
| --- | --- | --- |
| BioPharm | Mega Cap | 625.7 |
| BioPharm | Mid Cap | 886.61 |
| EcoEnergy | Large Cap | 902.05 |
| GlobalTrade | Small Cap | 220.86 |
| GlobalTrade | Mid Cap | 515.83 |
<end>Can you change this yml into markdown?
- Genre: Horror
  Release Year: 1990
- Genre: Drama
  Release Year: 2012
- Genre: Sci-Fi
  Release Year: 2014
- Genre: Adventure
  Release Year: 2020
- Genre: Sci-Fi
  Release Year: 2018
- Genre: Action
  Release Year: 2010
- Genre: Fantasy
  Release Year: 2017
<start>
| Genre | Release Year |
| --- | --- |
| Horror | 1990 |
| Drama | 2012 |
| Sci-Fi | 2014 |
| Adventure | 2020 |
| Sci-Fi | 2018 |
| Action | 2010 |
| Fantasy | 2017 |
<end>Here's some Yml data, can you convert it to json?
- Close Price: 282.34
  Date: '2012-04-26'
  High Price: 412.11
  Low Price: 21.6
  Open Price: 21.6
- Close Price: 1493.43
  Date: '2014-06-20'
  High Price: 1493.43
  Low Price: 119.21
  Open Price: 618.8
- Close Price: 891.74
  Date: '2023-06-25'
  High Price: 1022.0
  Low Price: 119.21
  Open Price: 411.91
- Close Price: 1215.33
  Date: '2016-12-20'
  High Price: 1493.43
  Low Price: 398.38
  Open Price: 1493.43
- Close Price: 378.23
  Date: '2012-02-13'
  High Price: 894.9
  Low Price: 378.23
  Open Price: 894.9
- Close Price: 1156.34
  Date: '2017-10-20'
  High Price: 1204.08
  Low Price: 722.43
  Open Price: 1204.08
- Close Price: 608.59
  Date: '2013-12-08'
  High Price: 722.43
  Low Price: 50.46
  Open Price: 722.43
<start>
[
    {
        "Date": "2012-04-26",
        "Open Price": 21.6,
        "Close Price": 282.34,
        "High Price": 412.11,
        "Low Price": 21.6
    },
    {
        "Date": "2014-06-20",
        "Open Price": 618.8,
        "Close Price": 1493.43,
        "High Price": 1493.43,
        "Low Price": 119.21
    },
    {
        "Date": "2023-06-25",
        "Open Price": 411.91,
        "Close Price": 891.74,
        "High Price": 1022.0,
        "Low Price": 119.21
    },
    {
        "Date": "2016-12-20",
        "Open Price": 1493.43,
        "Close Price": 1215.33,
        "High Price": 1493.43,
        "Low Price": 398.38
    },
    {
        "Date": "2012-02-13",
        "Open Price": 894.9,
        "Close Price": 378.23,
        "High Price": 894.9,
        "Low Price": 378.23
    },
    {
        "Date": "2017-10-20",
        "Open Price": 1204.08,
        "Close Price": 1156.34,
        "High Price": 1204.08,
        "Low Price": 722.43
    },
    {
        "Date": "2013-12-08",
        "Open Price": 722.43,
        "Close Price": 608.59,
        "High Price": 722.43,
        "Low Price": 50.46
    }
]
<end>Here's some csv data, can you convert it to markdown?
Title,Director,Genre,Release Year,Box Office Earnings (M)
The Endless Horizon,Drake Nightshade,Thriller,1990,560.28
The Final Voyage,Lira Silverleaf,Adventure,2011,560.28
The Final Voyage,Rylan Frostblade,Sci-Fi,2022,68.56
Rise of the Titans,Drake Nightshade,Comedy,2005,960.23
The Endless Horizon,Aria Ravenwood,Thriller,2011,935.15
Escape from Earth,Selene Darkwhisper,Comedy,2011,877.93
Edge of Infinity,Selene Darkwhisper,Action,2011,208.82
<start>
| Title | Director | Genre | Release Year | Box Office Earnings (M) |
| --- | --- | --- | --- | --- |
| The Endless Horizon | Drake Nightshade | Thriller | 1990 | 560.28 |
| The Final Voyage | Lira Silverleaf | Adventure | 2011 | 560.28 |
| The Final Voyage | Rylan Frostblade | Sci-Fi | 2022 | 68.56 |
| Rise of the Titans | Drake Nightshade | Comedy | 2005 | 960.23 |
| The Endless Horizon | Aria Ravenwood | Thriller | 2011 | 935.15 |
| Escape from Earth | Selene Darkwhisper | Comedy | 2011 | 877.93 |
| Edge of Infinity | Selene Darkwhisper | Action | 2011 | 208.82 |
<end>Convert this CSV to yaml:
Company,Sector,Market Cap,Stock Price,Annual Revenue (B),Quarter
HealthPlus,Aerospace,Mega Cap,542.98,240.51,Q2
EcoEnergy,Retail,Mid Cap,346.36,224.62,Q2
RetailHub,Energy,Small Cap,903.01,179.14,Q3
AutoDrive,Aerospace,Mid Cap,857.09,142.28,Q4
TechCorp,Aerospace,Small Cap,151.92,484.1,Q4
EcoEnergy,Technology,Mega Cap,916.0,316.55,Q1
<start>
- Annual Revenue (B): 240.51
  Company: HealthPlus
  Market Cap: Mega Cap
  Quarter: Q2
  Sector: Aerospace
  Stock Price: 542.98
- Annual Revenue (B): 224.62
  Company: EcoEnergy
  Market Cap: Mid Cap
  Quarter: Q2
  Sector: Retail
  Stock Price: 346.36
- Annual Revenue (B): 179.14
  Company: RetailHub
  Market Cap: Small Cap
  Quarter: Q3
  Sector: Energy
  Stock Price: 903.01
- Annual Revenue (B): 142.28
  Company: AutoDrive
  Market Cap: Mid Cap
  Quarter: Q4
  Sector: Aerospace
  Stock Price: 857.09
- Annual Revenue (B): 484.1
  Company: TechCorp
  Market Cap: Small Cap
  Quarter: Q4
  Sector: Aerospace
  Stock Price: 151.92
- Annual Revenue (B): 316.55
  Company: EcoEnergy
  Market Cap: Mega Cap
  Quarter: Q1
  Sector: Technology
  Stock Price: 916.0
<end>Here's some Json data, can you convert it to CSV?
[
    {
        "Trip Name": "Valley Voyage",
        "Start Location": "Phoenix",
        "End Location": "Chicago",
        "Distance (miles)": 791.0,
        "Duration (hours)": 4.8,
        "Fuel Used (gallons)": 75.3
    },
    {
        "Trip Name": "Valley Voyage",
        "Start Location": "Denver",
        "End Location": "New York",
        "Distance (miles)": 1605.5,
        "Duration (hours)": 49.9,
        "Fuel Used (gallons)": 51.7
    },
    {
        "Trip Name": "Coast to Coast",
        "Start Location": "Miami",
        "End Location": "Phoenix",
        "Distance (miles)": 2563.4,
        "Duration (hours)": 53.9,
        "Fuel Used (gallons)": 21.5
    },
    {
        "Trip Name": "Forest Journey",
        "Start Location": "Los Angeles",
        "End Location": "San Francisco",
        "Distance (miles)": 2368.9,
        "Duration (hours)": 63.6,
        "Fuel Used (gallons)": 27.5
    },
    {
        "Trip Name": "Coast to Coast",
        "Start Location": "Chicago",
        "End Location": "Los Angeles",
        "Distance (miles)": 1691.9,
        "Duration (hours)": 61.3,
        "Fuel Used (gallons)": 40.0
    },
    {
        "Trip Name": "Lakeside Retreat",
        "Start Location": "New York",
        "End Location": "Miami",
        "Distance (miles)": 1691.9,
        "Duration (hours)": 31.5,
        "Fuel Used (gallons)": 6.2
    }
]<start>
Trip Name,Start Location,End Location,Distance (miles),Duration (hours),Fuel Used (gallons)
Valley Voyage,Phoenix,Chicago,791.0,4.8,75.3
Valley Voyage,Denver,New York,1605.5,49.9,51.7
Coast to Coast,Miami,Phoenix,2563.4,53.9,21.5
Forest Journey,Los Angeles,San Francisco,2368.9,63.6,27.5
Coast to Coast,Chicago,Los Angeles,1691.9,61.3,40.0
Lakeside Retreat,New York,Miami,1691.9,31.5,6.2
<end>Transform this MARKDOWN structure to a Csv format:
| Name | Age | Birth Month | City | Income |
| --- | --- | --- | --- | --- |
| Sheila | 64 | July | Nashville | 385000 |
| Clara | 28 | July | Boston | 125000 |
| Bessie | 52 | August | Milwaukee | 125000 |
| Roosevelt | 63 | June | Dallas | 50000 |
| Bonnie | 63 | June | Phoenix | 330000 |
| Sidney | 50 | May | San Antonio | 220000 |
| Rachel | 34 | June | Indianapolis | 275000 |
| Ruben | 56 | February | Phoenix | 340000 |
| Carole | 30 | January | Portland | 175000 |
| Amelia | 27 | November | New York | 395000 |<start>
Name,Age,Birth Month,City,Income
Sheila,64,July,Nashville,385000
Clara,28,July,Boston,125000
Bessie,52,August,Milwaukee,125000
Roosevelt,63,June,Dallas,50000
Bonnie,63,June,Phoenix,330000
Sidney,50,May,San Antonio,220000
Rachel,34,June,Indianapolis,275000
Ruben,56,February,Phoenix,340000
Carole,30,January,Portland,175000
Amelia,27,November,New York,395000
<end>Convert this markdown to PLAIN TEXT:
| Company | Sector | Market Cap | Stock Price | Quarter |
| --- | --- | --- | --- | --- |
| TechCorp | Biotech | Mega Cap | 764.0 | Q1 |
| HealthPlus | Energy | Small Cap | 561.52 | Q1 |
| AutoDrive | Aerospace | Large Cap | 591.43 | Q3 |<start>
Company: TechCorp | Sector: Biotech | Market Cap: Mega Cap | Stock Price: 764.0 | Quarter: Q1
Company: HealthPlus | Sector: Energy | Market Cap: Small Cap | Stock Price: 561.52 | Quarter: Q1
Company: AutoDrive | Sector: Aerospace | Market Cap: Large Cap | Stock Price: 591.43 | Quarter: Q3
<end>Transform this Yaml structure to a csv format:
- Category: Toys
  Product Name: Apparatus
  SKU: SKU-1039
  Stock Quantity: 47
- Category: Automotive
  Product Name: Gadget
  SKU: SKU-1014
  Stock Quantity: 20
- Category: Household
  Product Name: Doohickey
  SKU: SKU-1043
  Stock Quantity: 189
- Category: Electronics
  Product Name: Whatchamacallit
  SKU: SKU-1026
  Stock Quantity: 417
- Category: Automotive
  Product Name: Contraption
  SKU: SKU-1063
  Stock Quantity: 463
- Category: Electronics
  Product Name: Device
  SKU: SKU-1056
  Stock Quantity: 275
- Category: Automotive
  Product Name: Contraption
  SKU: SKU-1068
  Stock Quantity: 432
- Category: Electronics
  Product Name: Whatchamacallit
  SKU: SKU-1008
  Stock Quantity: 169
- Category: Electronics
  Product Name: Thingamajig
  SKU: SKU-1009
  Stock Quantity: 297
- Category: Sports
  Product Name: Widget
  SKU: SKU-1048
  Stock Quantity: 211
<start>
Product Name,SKU,Stock Quantity,Category
Apparatus,SKU-1039,47,Toys
Gadget,SKU-1014,20,Automotive
Doohickey,SKU-1043,189,Household
Whatchamacallit,SKU-1026,417,Electronics
Contraption,SKU-1063,463,Automotive
Device,SKU-1056,275,Electronics
Contraption,SKU-1068,432,Automotive
Whatchamacallit,SKU-1008,169,Electronics
Thingamajig,SKU-1009,297,Electronics
Widget,SKU-1048,211,Sports
<end>Please transform the following Csv data into Json:
Company,Sector,Market Cap,Stock Price,Annual Revenue (B),Quarter
Foodies,Technology,Large Cap,193.02,56.51,Q4
BioPharm,Finance,Mid Cap,422.46,476.42,Q1
GlobalTrade,Automotive,Small Cap,864.21,239.9,Q1
Foodies,Energy,Mega Cap,802.9,51.29,Q1
RetailHub,Healthcare,Mid Cap,256.32,354.74,Q3
RetailHub,Retail,Mid Cap,801.4,142.31,Q1
<start>
[
    {
        "Company": "Foodies",
        "Sector": "Technology",
        "Market Cap": "Large Cap",
        "Stock Price": 193.02,
        "Annual Revenue (B)": 56.51,
        "Quarter": "Q4"
    },
    {
        "Company": "BioPharm",
        "Sector": "Finance",
        "Market Cap": "Mid Cap",
        "Stock Price": 422.46,
        "Annual Revenue (B)": 476.42,
        "Quarter": "Q1"
    },
    {
        "Company": "GlobalTrade",
        "Sector": "Automotive",
        "Market Cap": "Small Cap",
        "Stock Price": 864.21,
        "Annual Revenue (B)": 239.9,
        "Quarter": "Q1"
    },
    {
        "Company": "Foodies",
        "Sector": "Energy",
        "Market Cap": "Mega Cap",
        "Stock Price": 802.9,
        "Annual Revenue (B)": 51.29,
        "Quarter": "Q1"
    },
    {
        "Company": "RetailHub",
        "Sector": "Healthcare",
        "Market Cap": "Mid Cap",
        "Stock Price": 256.32,
        "Annual Revenue (B)": 354.74,
        "Quarter": "Q3"
    },
    {
        "Company": "RetailHub",
        "Sector": "Retail",
        "Market Cap": "Mid Cap",
        "Stock Price": 801.4,
        "Annual Revenue (B)": 142.31,
        "Quarter": "Q1"
    }
]
<end>Transform this json structure to a markdown format:
[
    {
        "Title": "Tales of the Brave",
        "Author": "Orion Frostblade",
        "Publication Year": 1980,
        "Rating": 4.3
    },
    {
        "Title": "The Forgotten World",
        "Author": "Galen Starfire",
        "Publication Year": 1996,
        "Rating": 4.4
    },
    {
        "Title": "The Silent Grove",
        "Author": "Elara Moonshadow",
        "Publication Year": 1972,
        "Rating": 1.7
    },
    {
        "Title": "A Journey Through Time",
        "Author": "Thorne Ironwood",
        "Publication Year": 1984,
        "Rating": 4.9
    }
]<start>
| Title | Author | Publication Year | Rating |
| --- | --- | --- | --- |
| Tales of the Brave | Orion Frostblade | 1980 | 4.3 |
| The Forgotten World | Galen Starfire | 1996 | 4.4 |
| The Silent Grove | Elara Moonshadow | 1972 | 1.7 |
| A Journey Through Time | Thorne Ironwood | 1984 | 4.9 |
<end>Here's some plain text data, can you convert it to CSV?
Company: FinanceWorks | Sector: Biotech | Market Cap: Small Cap | Stock Price: 904.4 | Annual Revenue (B): 144.66 | Quarter: Q3
Company: EcoEnergy | Sector: Healthcare | Market Cap: Mid Cap | Stock Price: 594.08 | Annual Revenue (B): 496.98 | Quarter: Q3
Company: EcoEnergy | Sector: Aerospace | Market Cap: Mega Cap | Stock Price: 843.48 | Annual Revenue (B): 268.71 | Quarter: Q2
Company: FinanceWorks | Sector: Energy | Market Cap: Mid Cap | Stock Price: 272.75 | Annual Revenue (B): 144.66 | Quarter: Q4
Company: GlobalTrade | Sector: Aerospace | Market Cap: Small Cap | Stock Price: 587.78 | Annual Revenue (B): 464.08 | Quarter: Q1
Company: RetailHub | Sector: Energy | Market Cap: Large Cap | Stock Price: 159.91 | Annual Revenue (B): 404.28 | Quarter: Q3
<start>
Company,Sector,Market Cap,Stock Price,Annual Revenue (B),Quarter
FinanceWorks,Biotech,Small Cap,904.4,144.66,Q3
EcoEnergy,Healthcare,Mid Cap,594.08,496.98,Q3
EcoEnergy,Aerospace,Mega Cap,843.48,268.71,Q2
FinanceWorks,Energy,Mid Cap,272.75,144.66,Q4
GlobalTrade,Aerospace,Small Cap,587.78,464.08,Q1
RetailHub,Energy,Large Cap,159.91,404.28,Q3
<end>Can you change this yml into CSV?
- Age: 66
  City: San Francisco
- Age: 58
  City: Portland
- Age: 32
  City: Nashville
- Age: 35
  City: Baltimore
- Age: 20
  City: Indianapolis
<start>
Age,City
66,San Francisco
58,Portland
32,Nashville
35,Baltimore
20,Indianapolis
<end>Here's some Yml data, can you convert it to MARKDOWN?
- Average Latency (ms): 4.37
  Cache Hit Ratio (%): 74.64
  Connection Count: 416
  Database Name: ProfilesDB
  Queries per Second: 822.64
  Timestamp: '2023-11-18 14:02:50'
- Average Latency (ms): 39.19
  Cache Hit Ratio (%): 98.62
  Connection Count: 37
  Database Name: UserDB
  Queries per Second: 1486.55
  Timestamp: '2023-05-24 06:01:11'
- Average Latency (ms): 80.48
  Cache Hit Ratio (%): 97.12
  Connection Count: 350
  Database Name: OrdersDB
  Queries per Second: 345.25
  Timestamp: '2022-09-13 06:41:55'
- Average Latency (ms): 39.72
  Cache Hit Ratio (%): 87.76
  Connection Count: 181
  Database Name: SalesDB
  Queries per Second: 1933.45
  Timestamp: '2022-03-24 18:54:00'
- Average Latency (ms): 46.24
  Cache Hit Ratio (%): 99.31
  Connection Count: 209
  Database Name: SalesDB
  Queries per Second: 1914.76
  Timestamp: '2023-12-10 09:19:03'
- Average Latency (ms): 41.51
  Cache Hit Ratio (%): 71.12
  Connection Count: 84
  Database Name: SalesDB
  Queries per Second: 3211.64
  Timestamp: '2021-04-25 01:56:56'
<start>
| Database Name | Queries per Second | Cache Hit Ratio (%) | Connection Count | Average Latency (ms) | Timestamp |
| --- | --- | --- | --- | --- | --- |
| ProfilesDB | 822.64 | 74.64 | 416 | 4.37 | 2023-11-18 14:02:50 |
| UserDB | 1486.55 | 98.62 | 37 | 39.19 | 2023-05-24 06:01:11 |
| OrdersDB | 345.25 | 97.12 | 350 | 80.48 | 2022-09-13 06:41:55 |
| SalesDB | 1933.45 | 87.76 | 181 | 39.72 | 2022-03-24 18:54:00 |
| SalesDB | 1914.76 | 99.31 | 209 | 46.24 | 2023-12-10 09:19:03 |
| SalesDB | 3211.64 | 71.12 | 84 | 41.51 | 2021-04-25 01:56:56 |
<end>Transform this Csv structure to a yaml format:
Company,Date,Open Price,Close Price,High Price,Low Price,Volume
HealthGen,2019-10-19,557.84,1137.77,1137.77,557.84,5985281
HealthGen,2022-02-04,670.72,586.72,1119.91,586.72,7850059
HealthGen,2016-10-18,859.01,187.27,859.01,187.27,7115957
TechnoCorp,2021-04-01,904.46,824.69,904.46,824.69,7186786
<start>
- Close Price: 1137.77
  Company: HealthGen
  Date: '2019-10-19'
  High Price: 1137.77
  Low Price: 557.84
  Open Price: 557.84
  Volume: 5985281
- Close Price: 586.72
  Company: HealthGen
  Date: '2022-02-04'
  High Price: 1119.91
  Low Price: 586.72
  Open Price: 670.72
  Volume: 7850059
- Close Price: 187.27
  Company: HealthGen
  Date: '2016-10-18'
  High Price: 859.01
  Low Price: 187.27
  Open Price: 859.01
  Volume: 7115957
- Close Price: 824.69
  Company: TechnoCorp
  Date: '2021-04-01'
  High Price: 904.46
  Low Price: 824.69
  Open Price: 904.46
  Volume: 7186786
<end>Can you change this markdown into json?
| Company | Date | Close Price | High Price | Low Price | Volume |
| --- | --- | --- | --- | --- | --- |
| RetailWorld | 2022-09-03 | 976.42 | 1229.29 | 63.25 | 1767728 |
| FoodChain | 2012-01-16 | 980.4 | 980.4 | 434.52 | 8627207 |
| TechnoCorp | 2017-08-23 | 591.69 | 1427.74 | 591.69 | 497724 |
| GreenEnergy | 2014-07-02 | 976.42 | 1453.8 | 140.03 | 7515588 |
| FoodChain | 2017-10-06 | 1139.92 | 1139.92 | 848.94 | 8597570 |<start>
[
    {
        "Company": "RetailWorld",
        "Date": "2022-09-03",
        "Close Price": 976.42,
        "High Price": 1229.29,
        "Low Price": 63.25,
        "Volume": 1767728
    },
    {
        "Company": "FoodChain",
        "Date": "2012-01-16",
        "Close Price": 980.4,
        "High Price": 980.4,
        "Low Price": 434.52,
        "Volume": 8627207
    },
    {
        "Company": "TechnoCorp",
        "Date": "2017-08-23",
        "Close Price": 591.69,
        "High Price": 1427.74,
        "Low Price": 591.69,
        "Volume": 497724
    },
    {
        "Company": "GreenEnergy",
        "Date": "2014-07-02",
        "Close Price": 976.42,
        "High Price": 1453.8,
        "Low Price": 140.03,
        "Volume": 7515588
    },
    {
        "Company": "FoodChain",
        "Date": "2017-10-06",
        "Close Price": 1139.92,
        "High Price": 1139.92,
        "Low Price": 848.94,
        "Volume": 8597570
    }
]
<end>Transform this markdown structure to a plain text format:
| Title | Genre | Release Year |
| --- | --- | --- |
| Beyond the Veil | Action | 1977 |
| Escape from Earth | Drama | 1998 |
| Rise of the Titans | Comedy | 1985 |
| Dreamwalker | Adventure | 1999 |
| Starbound Odyssey | Fantasy | 2013 |
| Escape from Earth | Sci-Fi | 2013 |
| Mystery of the Depths | Horror | 1996 |
| Mystery of the Depths | Comedy | 2013 |
| Escape from Earth | Horror | 1999 |<start>
Title: Beyond the Veil | Genre: Action | Release Year: 1977
Title: Escape from Earth | Genre: Drama | Release Year: 1998
Title: Rise of the Titans | Genre: Comedy | Release Year: 1985
Title: Dreamwalker | Genre: Adventure | Release Year: 1999
Title: Starbound Odyssey | Genre: Fantasy | Release Year: 2013
Title: Escape from Earth | Genre: Sci-Fi | Release Year: 2013
Title: Mystery of the Depths | Genre: Horror | Release Year: 1996
Title: Mystery of the Depths | Genre: Comedy | Release Year: 2013
Title: Escape from Earth | Genre: Horror | Release Year: 1999
<end>Please transform the following markdown data into PLAIN TEXT:
| Restaurant Name | Cuisine | Price Range |
| --- | --- | --- |
| Burger Haven | Italian | $$$$ |
| Burger Haven | Mediterranean | $$$$$ |
| Burger Haven | American | $$ |
| Sushi World | Mediterranean | $$$$ |
| Sushi World | Italian | $$$ |<start>
Restaurant Name: Burger Haven | Cuisine: Italian | Price Range: $$$$
Restaurant Name: Burger Haven | Cuisine: Mediterranean | Price Range: $$$$$
Restaurant Name: Burger Haven | Cuisine: American | Price Range: $$
Restaurant Name: Sushi World | Cuisine: Mediterranean | Price Range: $$$$
Restaurant Name: Sushi World | Cuisine: Italian | Price Range: $$$
<end>Here's some Yaml data, can you convert it to Plain text?
- Close Price: 1356.71
  Company: GreenEnergy
  Date: '2015-02-20'
  High Price: 1356.71
  Low Price: 777.39
  Volume: 1661209
- Close Price: 12.84
  Company: MediaGroup
  Date: '2010-06-02'
  High Price: 708.14
  Low Price: 12.84
  Volume: 1372251
- Close Price: 906.33
  Company: GreenEnergy
  Date: '2014-03-22'
  High Price: 1498.68
  Low Price: 318.34
  Volume: 5952856
- Close Price: 1356.71
  Company: FoodChain
  Date: '2017-04-27'
  High Price: 1356.71
  Low Price: 115.12
  Volume: 2051637
- Close Price: 1356.71
  Company: TechnoCorp
  Date: '2019-04-10'
  High Price: 1356.71
  Low Price: 1114.62
  Volume: 6556818
- Close Price: 806.6
  Company: MediaGroup
  Date: '2019-10-01'
  High Price: 968.92
  Low Price: 11.32
  Volume: 264259
- Close Price: 968.86
  Company: AeroSystems
  Date: '2022-03-06'
  High Price: 968.86
  Low Price: 165.84
  Volume: 3328578
- Close Price: 1300.26
  Company: MediaGroup
  Date: '2011-04-25'
  High Price: 1300.26
  Low Price: 510.15
  Volume: 5913468
- Close Price: 657.87
  Company: RetailWorld
  Date: '2018-06-17'
  High Price: 1305.31
  Low Price: 547.08
  Volume: 7792468
- Close Price: 1094.53
  Company: AeroSystems
  Date: '2010-12-02'
  High Price: 1094.53
  Low Price: 76.36
  Volume: 1956019
<start>
Company: GreenEnergy | Date: 2015-02-20 | Close Price: 1356.71 | High Price: 1356.71 | Low Price: 777.39 | Volume: 1661209
Company: MediaGroup | Date: 2010-06-02 | Close Price: 12.84 | High Price: 708.14 | Low Price: 12.84 | Volume: 1372251
Company: GreenEnergy | Date: 2014-03-22 | Close Price: 906.33 | High Price: 1498.68 | Low Price: 318.34 | Volume: 5952856
Company: FoodChain | Date: 2017-04-27 | Close Price: 1356.71 | High Price: 1356.71 | Low Price: 115.12 | Volume: 2051637
Company: TechnoCorp | Date: 2019-04-10 | Close Price: 1356.71 | High Price: 1356.71 | Low Price: 1114.62 | Volume: 6556818
Company: MediaGroup | Date: 2019-10-01 | Close Price: 806.6 | High Price: 968.92 | Low Price: 11.32 | Volume: 264259
Company: AeroSystems | Date: 2022-03-06 | Close Price: 968.86 | High Price: 968.86 | Low Price: 165.84 | Volume: 3328578
Company: MediaGroup | Date: 2011-04-25 | Close Price: 1300.26 | High Price: 1300.26 | Low Price: 510.15 | Volume: 5913468
Company: RetailWorld | Date: 2018-06-17 | Close Price: 657.87 | High Price: 1305.31 | Low Price: 547.08 | Volume: 7792468
Company: AeroSystems | Date: 2010-12-02 | Close Price: 1094.53 | High Price: 1094.53 | Low Price: 76.36 | Volume: 1956019
<end>Transform this yml structure to a Json format:
- Rating: 3.6
  Title: The Silent Grove
- Rating: 3.8
  Title: Tales of the Brave
- Rating: 3.7
  Title: A Journey Through Time
- Rating: 2.0
  Title: Tales of the Brave
- Rating: 1.6
  Title: Shadows of Solitude
- Rating: 2.5
  Title: Echoes of Eternity
- Rating: 4.9
  Title: The Forgotten World
- Rating: 2.6
  Title: The Last Sky
- Rating: 1.8
  Title: A Journey Through Time
<start>
[
    {
        "Title": "The Silent Grove",
        "Rating": 3.6
    },
    {
        "Title": "Tales of the Brave",
        "Rating": 3.8
    },
    {
        "Title": "A Journey Through Time",
        "Rating": 3.7
    },
    {
        "Title": "Tales of the Brave",
        "Rating": 2.0
    },
    {
        "Title": "Shadows of Solitude",
        "Rating": 1.6
    },
    {
        "Title": "Echoes of Eternity",
        "Rating": 2.5
    },
    {
        "Title": "The Forgotten World",
        "Rating": 4.9
    },
    {
        "Title": "The Last Sky",
        "Rating": 2.6
    },
    {
        "Title": "A Journey Through Time",
        "Rating": 1.8
    }
]
<end>Can you change this Json into Yml?
[
    {
        "Trip Name": "Valley Voyage",
        "Start Location": "Los Angeles",
        "End Location": "Phoenix",
        "Distance (miles)": 1403.6,
        "Duration (hours)": 59.9,
        "Fuel Used (gallons)": 76.4
    },
    {
        "Trip Name": "Coast to Coast",
        "Start Location": "New York",
        "End Location": "Miami",
        "Distance (miles)": 2396.0,
        "Duration (hours)": 36.1,
        "Fuel Used (gallons)": 19.6
    },
    {
        "Trip Name": "Lakeside Retreat",
        "Start Location": "New York",
        "End Location": "San Francisco",
        "Distance (miles)": 1368.3,
        "Duration (hours)": 60.6,
        "Fuel Used (gallons)": 17.7
    },
    {
        "Trip Name": "Valley Voyage",
        "Start Location": "Houston",
        "End Location": "San Francisco",
        "Distance (miles)": 1172.8,
        "Duration (hours)": 21.1,
        "Fuel Used (gallons)": 66.1
    },
    {
        "Trip Name": "Coast to Coast",
        "Start Location": "Los Angeles",
        "End Location": "Phoenix",
        "Distance (miles)": 2063.6,
        "Duration (hours)": 49.2,
        "Fuel Used (gallons)": 85.1
    },
    {
        "Trip Name": "Valley Voyage",
        "Start Location": "New York",
        "End Location": "Los Angeles",
        "Distance (miles)": 2396.0,
        "Duration (hours)": 7.5,
        "Fuel Used (gallons)": 97.5
    },
    {
        "Trip Name": "City Explorer",
        "Start Location": "Chicago",
        "End Location": "San Francisco",
        "Distance (miles)": 2051.2,
        "Duration (hours)": 48.6,
        "Fuel Used (gallons)": 55.6
    },
    {
        "Trip Name": "Highway Odyssey",
        "Start Location": "Denver",
        "End Location": "Los Angeles",
        "Distance (miles)": 1440.9,
        "Duration (hours)": 22.9,
        "Fuel Used (gallons)": 91.2
    },
    {
        "Trip Name": "Desert Drive",
        "Start Location": "Phoenix",
        "End Location": "San Francisco",
        "Distance (miles)": 2177.5,
        "Duration (hours)": 57.7,
        "Fuel Used (gallons)": 8.0
    }
]<start>
- Distance (miles): 1403.6
  Duration (hours): 59.9
  End Location: Phoenix
  Fuel Used (gallons): 76.4
  Start Location: Los Angeles
  Trip Name: Valley Voyage
- Distance (miles): 2396.0
  Duration (hours): 36.1
  End Location: Miami
  Fuel Used (gallons): 19.6
  Start Location: New York
  Trip Name: Coast to Coast
- Distance (miles): 1368.3
  Duration (hours): 60.6
  End Location: San Francisco
  Fuel Used (gallons): 17.7
  Start Location: New York
  Trip Name: Lakeside Retreat
- Distance (miles): 1172.8
  Duration (hours): 21.1
  End Location: San Francisco
  Fuel Used (gallons): 66.1
  Start Location: Houston
  Trip Name: Valley Voyage
- Distance (miles): 2063.6
  Duration (hours): 49.2
  End Location: Phoenix
  Fuel Used (gallons): 85.1
  Start Location: Los Angeles
  Trip Name: Coast to Coast
- Distance (miles): 2396.0
  Duration (hours): 7.5
  End Location: Los Angeles
  Fuel Used (gallons): 97.5
  Start Location: New York
  Trip Name: Valley Voyage
- Distance (miles): 2051.2
  Duration (hours): 48.6
  End Location: San Francisco
  Fuel Used (gallons): 55.6
  Start Location: Chicago
  Trip Name: City Explorer
- Distance (miles): 1440.9
  Duration (hours): 22.9
  End Location: Los Angeles
  Fuel Used (gallons): 91.2
  Start Location: Denver
  Trip Name: Highway Odyssey
- Distance (miles): 2177.5
  Duration (hours): 57.7
  End Location: San Francisco
  Fuel Used (gallons): 8.0
  Start Location: Phoenix
  Trip Name: Desert Drive
<end>Transform this Csv structure to a yml format:
Trip Name,Start Location,Distance (miles),Duration (hours),Fuel Used (gallons)
Lakeside Retreat,San Francisco,1565.5,27.2,66.0
Forest Journey,San Francisco,2616.1,16.9,35.8
Highway Odyssey,Houston,928.9,10.2,9.1
Canyon Trek,Los Angeles,2703.9,9.7,28.2
Lakeside Retreat,Houston,2905.3,21.2,90.1
<start>
- Distance (miles): 1565.5
  Duration (hours): 27.2
  Fuel Used (gallons): 66.0
  Start Location: San Francisco
  Trip Name: Lakeside Retreat
- Distance (miles): 2616.1
  Duration (hours): 16.9
  Fuel Used (gallons): 35.8
  Start Location: San Francisco
  Trip Name: Forest Journey
- Distance (miles): 928.9
  Duration (hours): 10.2
  Fuel Used (gallons): 9.1
  Start Location: Houston
  Trip Name: Highway Odyssey
- Distance (miles): 2703.9
  Duration (hours): 9.7
  Fuel Used (gallons): 28.2
  Start Location: Los Angeles
  Trip Name: Canyon Trek
- Distance (miles): 2905.3
  Duration (hours): 21.2
  Fuel Used (gallons): 90.1
  Start Location: Houston
  Trip Name: Lakeside Retreat
<end>Please transform the following PLAIN TEXT data into csv:
Restaurant Name: The Steakhouse | Cuisine: Mexican | Location: San Francisco | Rating: 5 | Price Range: $
Restaurant Name: Burger Haven | Cuisine: Mexican | Location: Houston | Rating: 1 | Price Range: $
Restaurant Name: Taco Town | Cuisine: French | Location: Los Angeles | Rating: 3 | Price Range: $$$$$
Restaurant Name: The Steakhouse | Cuisine: Mediterranean | Location: Seattle | Rating: 2 | Price Range: $$$$
Restaurant Name: The Golden Spoon | Cuisine: Mexican | Location: San Francisco | Rating: 1 | Price Range: $$$$
Restaurant Name: Pasta Palace | Cuisine: Mexican | Location: San Francisco | Rating: 4 | Price Range: $$$$
Restaurant Name: Curry Corner | Cuisine: Indian | Location: Miami | Rating: 1 | Price Range: $$
Restaurant Name: Curry Corner | Cuisine: Mexican | Location: Chicago | Rating: 3 | Price Range: $$$$$
Restaurant Name: Taco Town | Cuisine: American | Location: New York | Rating: 3 | Price Range: $$
Restaurant Name: BBQ Barn | Cuisine: Mexican | Location: Houston | Rating: 3 | Price Range: $
<start>
Restaurant Name,Cuisine,Location,Rating,Price Range
The Steakhouse,Mexican,San Francisco,5,$
Burger Haven,Mexican,Houston,1,$
Taco Town,French,Los Angeles,3,$$$$$
The Steakhouse,Mediterranean,Seattle,2,$$$$
The Golden Spoon,Mexican,San Francisco,1,$$$$
Pasta Palace,Mexican,San Francisco,4,$$$$
Curry Corner,Indian,Miami,1,$$
Curry Corner,Mexican,Chicago,3,$$$$$
Taco Town,American,New York,3,$$
BBQ Barn,Mexican,Houston,3,$
<end>Here's some PLAIN TEXT data, can you convert it to Csv?
Restaurant Name: The Golden Spoon | Cuisine: Indian | Location: Phoenix
Restaurant Name: Vegan Delight | Cuisine: Italian | Location: Los Angeles
Restaurant Name: Curry Corner | Cuisine: French | Location: Los Angeles
Restaurant Name: The Steakhouse | Cuisine: Mexican | Location: Houston
Restaurant Name: BBQ Barn | Cuisine: Mediterranean | Location: Seattle
Restaurant Name: Pizza Planet | Cuisine: American | Location: New York
<start>
Restaurant Name,Cuisine,Location
The Golden Spoon,Indian,Phoenix
Vegan Delight,Italian,Los Angeles
Curry Corner,French,Los Angeles
The Steakhouse,Mexican,Houston
BBQ Barn,Mediterranean,Seattle
Pizza Planet,American,New York
<end>Here's some CSV data, can you convert it to MARKDOWN?
Location,Condition,Temperature (C),Humidity (%),Wind Speed (km/h),Day
Miami,Foggy,-0.8,45,4.4,Saturday
Houston,Foggy,17.0,48,28.3,Thursday
Houston,Stormy,27.1,74,8.4,Sunday
<start>
| Location | Condition | Temperature (C) | Humidity (%) | Wind Speed (km/h) | Day |
| --- | --- | --- | --- | --- | --- |
| Miami | Foggy | -0.8 | 45 | 4.4 | Saturday |
| Houston | Foggy | 17.0 | 48 | 28.3 | Thursday |
| Houston | Stormy | 27.1 | 74 | 8.4 | Sunday |
<end>Here's some YML data, can you convert it to plain text?
- Category: Sports
  Price: 435.14
  Product Name: Contraption
  SKU: SKU-1065
  Stock Quantity: 436
  Supplier Name: Umbrella Corp
- Category: Electronics
  Price: 79.74
  Product Name: Device
  SKU: SKU-1053
  Stock Quantity: 142
  Supplier Name: ACME Corp
- Category: Automotive
  Price: 454.87
  Product Name: Whatchamacallit
  SKU: SKU-1042
  Stock Quantity: 400
  Supplier Name: Umbrella Corp
- Category: Household
  Price: 481.24
  Product Name: Instrument
  SKU: SKU-1077
  Stock Quantity: 25
  Supplier Name: ACME Corp
- Category: Toys
  Price: 121.81
  Product Name: Device
  SKU: SKU-1029
  Stock Quantity: 431
  Supplier Name: Wayne Enterprises
- Category: Toys
  Price: 374.81
  Product Name: Apparatus
  SKU: SKU-1012
  Stock Quantity: 120
  Supplier Name: ACME Corp
- Category: Automotive
  Price: 355.1
  Product Name: Contraption
  SKU: SKU-1060
  Stock Quantity: 96
  Supplier Name: ACME Corp
- Category: Electronics
  Price: 73.07
  Product Name: Device
  SKU: SKU-1085
  Stock Quantity: 143
  Supplier Name: Wayne Enterprises
<start>
Product Name: Contraption | SKU: SKU-1065 | Price: 435.14 | Stock Quantity: 436 | Category: Sports | Supplier Name: Umbrella Corp
Product Name: Device | SKU: SKU-1053 | Price: 79.74 | Stock Quantity: 142 | Category: Electronics | Supplier Name: ACME Corp
Product Name: Whatchamacallit | SKU: SKU-1042 | Price: 454.87 | Stock Quantity: 400 | Category: Automotive | Supplier Name: Umbrella Corp
Product Name: Instrument | SKU: SKU-1077 | Price: 481.24 | Stock Quantity: 25 | Category: Household | Supplier Name: ACME Corp
Product Name: Device | SKU: SKU-1029 | Price: 121.81 | Stock Quantity: 431 | Category: Toys | Supplier Name: Wayne Enterprises
Product Name: Apparatus | SKU: SKU-1012 | Price: 374.81 | Stock Quantity: 120 | Category: Toys | Supplier Name: ACME Corp
Product Name: Contraption | SKU: SKU-1060 | Price: 355.1 | Stock Quantity: 96 | Category: Automotive | Supplier Name: ACME Corp
Product Name: Device | SKU: SKU-1085 | Price: 73.07 | Stock Quantity: 143 | Category: Electronics | Supplier Name: Wayne Enterprises
<end>Convert this csv to Plain text:
Rating,Price Range
2,$
3,$$
1,$$$$$
4,$$$
2,$$$
1,$
4,$$$
5,$$
<start>
Rating: 2 | Price Range: $
Rating: 3 | Price Range: $$
Rating: 1 | Price Range: $$$$$
Rating: 4 | Price Range: $$$
Rating: 2 | Price Range: $$$
Rating: 1 | Price Range: $
Rating: 4 | Price Range: $$$
Rating: 5 | Price Range: $$
<end>Can you change this yml into plain text?
- Box Office Earnings (M): 458.75
  Director: Orin Shadowalker
  Genre: Comedy
  Release Year: 1997
  Title: Mystery of the Depths
- Box Office Earnings (M): 762.36
  Director: Lira Silverleaf
  Genre: Comedy
  Release Year: 2007
  Title: Dreamwalker
- Box Office Earnings (M): 981.63
  Director: Selene Darkwhisper
  Genre: Action
  Release Year: 1980
  Title: Escape from Earth
- Box Office Earnings (M): 346.92
  Director: Aria Ravenwood
  Genre: Comedy
  Release Year: 1972
  Title: Starbound Odyssey
- Box Office Earnings (M): 158.85
  Director: Orin Shadowalker
  Genre: Action
  Release Year: 1993
  Title: Dreamwalker
<start>
Title: Mystery of the Depths | Director: Orin Shadowalker | Genre: Comedy | Release Year: 1997 | Box Office Earnings (M): 458.75
Title: Dreamwalker | Director: Lira Silverleaf | Genre: Comedy | Release Year: 2007 | Box Office Earnings (M): 762.36
Title: Escape from Earth | Director: Selene Darkwhisper | Genre: Action | Release Year: 1980 | Box Office Earnings (M): 981.63
Title: Starbound Odyssey | Director: Aria Ravenwood | Genre: Comedy | Release Year: 1972 | Box Office Earnings (M): 346.92
Title: Dreamwalker | Director: Orin Shadowalker | Genre: Action | Release Year: 1993 | Box Office Earnings (M): 158.85
<end>Convert this markdown to yaml:
| Trip Name | Start Location | Distance (miles) | Duration (hours) | Fuel Used (gallons) |
| --- | --- | --- | --- | --- |
| City Explorer | New York | 72.4 | 15.0 | 55.0 |
| Desert Drive | Houston | 435.1 | 18.8 | 9.3 |
| Forest Journey | San Francisco | 299.5 | 43.6 | 62.9 |
| Lakeside Retreat | San Francisco | 1873.7 | 47.4 | 94.2 |
| Coast to Coast | Los Angeles | 816.4 | 63.9 | 62.0 |
| Valley Voyage | New York | 1241.6 | 29.3 | 63.9 |
| Valley Voyage | Miami | 2112.1 | 54.1 | 67.3 |
| Canyon Trek | Denver | 1514.2 | 37.6 | 42.6 |
| Lakeside Retreat | Chicago | 2882.3 | 31.7 | 49.9 |
| Valley Voyage | New York | 1217.8 | 65.6 | 40.2 |<start>
- Distance (miles): 72.4
  Duration (hours): 15.0
  Fuel Used (gallons): 55.0
  Start Location: New York
  Trip Name: City Explorer
- Distance (miles): 435.1
  Duration (hours): 18.8
  Fuel Used (gallons): 9.3
  Start Location: Houston
  Trip Name: Desert Drive
- Distance (miles): 299.5
  Duration (hours): 43.6
  Fuel Used (gallons): 62.9
  Start Location: San Francisco
  Trip Name: Forest Journey
- Distance (miles): 1873.7
  Duration (hours): 47.4
  Fuel Used (gallons): 94.2
  Start Location: San Francisco
  Trip Name: Lakeside Retreat
- Distance (miles): 816.4
  Duration (hours): 63.9
  Fuel Used (gallons): 62.0
  Start Location: Los Angeles
  Trip Name: Coast to Coast
- Distance (miles): 1241.6
  Duration (hours): 29.3
  Fuel Used (gallons): 63.9
  Start Location: New York
  Trip Name: Valley Voyage
- Distance (miles): 2112.1
  Duration (hours): 54.1
  Fuel Used (gallons): 67.3
  Start Location: Miami
  Trip Name: Valley Voyage
- Distance (miles): 1514.2
  Duration (hours): 37.6
  Fuel Used (gallons): 42.6
  Start Location: Denver
  Trip Name: Canyon Trek
- Distance (miles): 2882.3
  Duration (hours): 31.7
  Fuel Used (gallons): 49.9
  Start Location: Chicago
  Trip Name: Lakeside Retreat
- Distance (miles): 1217.8
  Duration (hours): 65.6
  Fuel Used (gallons): 40.2
  Start Location: New York
  Trip Name: Valley Voyage
<end>Can you change this csv into markdown?
Restaurant Name,Location,Price Range
Pasta Palace,Los Angeles,$$
Sushi World,New York,$
Sushi World,Miami,$$$$$
Burger Haven,Chicago,$$
Taco Town,New York,$$$$
The Golden Spoon,New York,$$
The Golden Spoon,Chicago,$$
BBQ Barn,Seattle,$
<start>
| Restaurant Name | Location | Price Range |
| --- | --- | --- |
| Pasta Palace | Los Angeles | $$ |
| Sushi World | New York | $ |
| Sushi World | Miami | $$$$$ |
| Burger Haven | Chicago | $$ |
| Taco Town | New York | $$$$ |
| The Golden Spoon | New York | $$ |
| The Golden Spoon | Chicago | $$ |
| BBQ Barn | Seattle | $ |
<end>Convert this json to plain text:
[
    {
        "Trip Name": "Canyon Trek",
        "Start Location": "Phoenix",
        "End Location": "Los Angeles",
        "Distance (miles)": 2589.5,
        "Duration (hours)": 35.9,
        "Fuel Used (gallons)": 46.2
    },
    {
        "Trip Name": "Forest Journey",
        "Start Location": "Denver",
        "End Location": "Houston",
        "Distance (miles)": 286.9,
        "Duration (hours)": 10.9,
        "Fuel Used (gallons)": 62.2
    },
    {
        "Trip Name": "Canyon Trek",
        "Start Location": "Phoenix",
        "End Location": "Houston",
        "Distance (miles)": 815.6,
        "Duration (hours)": 22.3,
        "Fuel Used (gallons)": 99.6
    },
    {
        "Trip Name": "Mountain Adventure",
        "Start Location": "Miami",
        "End Location": "San Francisco",
        "Distance (miles)": 1865.9,
        "Duration (hours)": 34.4,
        "Fuel Used (gallons)": 20.6
    },
    {
        "Trip Name": "Canyon Trek",
        "Start Location": "New York",
        "End Location": "Phoenix",
        "Distance (miles)": 414.3,
        "Duration (hours)": 4.8,
        "Fuel Used (gallons)": 70.9
    },
    {
        "Trip Name": "Forest Journey",
        "Start Location": "Denver",
        "End Location": "Phoenix",
        "Distance (miles)": 2727.7,
        "Duration (hours)": 57.9,
        "Fuel Used (gallons)": 81.7
    },
    {
        "Trip Name": "Mountain Adventure",
        "Start Location": "New York",
        "End Location": "Phoenix",
        "Distance (miles)": 1516.3,
        "Duration (hours)": 35.9,
        "Fuel Used (gallons)": 99.5
    },
    {
        "Trip Name": "Valley Voyage",
        "Start Location": "Denver",
        "End Location": "New York",
        "Distance (miles)": 414.3,
        "Duration (hours)": 57.0,
        "Fuel Used (gallons)": 13.1
    },
    {
        "Trip Name": "Canyon Trek",
        "Start Location": "Denver",
        "End Location": "Los Angeles",
        "Distance (miles)": 151.7,
        "Duration (hours)": 13.4,
        "Fuel Used (gallons)": 9.0
    }
]<start>
Trip Name: Canyon Trek | Start Location: Phoenix | End Location: Los Angeles | Distance (miles): 2589.5 | Duration (hours): 35.9 | Fuel Used (gallons): 46.2
Trip Name: Forest Journey | Start Location: Denver | End Location: Houston | Distance (miles): 286.9 | Duration (hours): 10.9 | Fuel Used (gallons): 62.2
Trip Name: Canyon Trek | Start Location: Phoenix | End Location: Houston | Distance (miles): 815.6 | Duration (hours): 22.3 | Fuel Used (gallons): 99.6
Trip Name: Mountain Adventure | Start Location: Miami | End Location: San Francisco | Distance (miles): 1865.9 | Duration (hours): 34.4 | Fuel Used (gallons): 20.6
Trip Name: Canyon Trek | Start Location: New York | End Location: Phoenix | Distance (miles): 414.3 | Duration (hours): 4.8 | Fuel Used (gallons): 70.9
Trip Name: Forest Journey | Start Location: Denver | End Location: Phoenix | Distance (miles): 2727.7 | Duration (hours): 57.9 | Fuel Used (gallons): 81.7
Trip Name: Mountain Adventure | Start Location: New York | End Location: Phoenix | Distance (miles): 1516.3 | Duration (hours): 35.9 | Fuel Used (gallons): 99.5
Trip Name: Valley Voyage | Start Location: Denver | End Location: New York | Distance (miles): 414.3 | Duration (hours): 57.0 | Fuel Used (gallons): 13.1
Trip Name: Canyon Trek | Start Location: Denver | End Location: Los Angeles | Distance (miles): 151.7 | Duration (hours): 13.4 | Fuel Used (gallons): 9.0
<end>Can you change this PLAIN TEXT into yaml?
Name: Jon | Birth Month: May | City: Las Vegas | Income: 130000
Name: Aliyah | Birth Month: August | City: Los Angeles | Income: 320000
Name: Carmen | Birth Month: December | City: Indianapolis | Income: 60000
Name: Winnie | Birth Month: March | City: Charlotte | Income: 40000
Name: Hilda | Birth Month: October | City: Columbus | Income: 400000
Name: Irene | Birth Month: January | City: Louisville | Income: 40000
Name: Bonnie | Birth Month: June | City: Las Vegas | Income: 420000
Name: Mack | Birth Month: March | City: El Paso | Income: 80000
Name: Asher | Birth Month: July | City: Nashville | Income: 145000
<start>
- Birth Month: May
  City: Las Vegas
  Income: 130000
  Name: Jon
- Birth Month: August
  City: Los Angeles
  Income: 320000
  Name: Aliyah
- Birth Month: December
  City: Indianapolis
  Income: 60000
  Name: Carmen
- Birth Month: March
  City: Charlotte
  Income: 40000
  Name: Winnie
- Birth Month: October
  City: Columbus
  Income: 400000
  Name: Hilda
- Birth Month: January
  City: Louisville
  Income: 40000
  Name: Irene
- Birth Month: June
  City: Las Vegas
  Income: 420000
  Name: Bonnie
- Birth Month: March
  City: El Paso
  Income: 80000
  Name: Mack
- Birth Month: July
  City: Nashville
  Income: 145000
  Name: Asher
<end>Convert this yml to markdown:
- Author: Elara Moonshadow
  Genre: Fantasy
  Publication Year: 1954
  Title: The Last Sky
- Author: Galen Starfire
  Genre: Historical
  Publication Year: 2008
  Title: Legends of the Rift
- Author: Elara Moonshadow
  Genre: Thriller
  Publication Year: 2021
  Title: Legends of the Rift
- Author: Galen Starfire
  Genre: Science Fiction
  Publication Year: 1962
  Title: A Journey Through Time
- Author: Rowan Ashborne
  Genre: Fantasy
  Publication Year: 1978
  Title: The Silent Grove
- Author: Rowan Ashborne
  Genre: Mystery
  Publication Year: 1966
  Title: Shadows of Solitude
- Author: Orion Frostblade
  Genre: Horror
  Publication Year: 1954
  Title: Legends of the Rift
- Author: Isla Windrider
  Genre: Historical
  Publication Year: 1995
  Title: Whispers of the Abyss
<start>
| Title | Author | Genre | Publication Year |
| --- | --- | --- | --- |
| The Last Sky | Elara Moonshadow | Fantasy | 1954 |
| Legends of the Rift | Galen Starfire | Historical | 2008 |
| Legends of the Rift | Elara Moonshadow | Thriller | 2021 |
| A Journey Through Time | Galen Starfire | Science Fiction | 1962 |
| The Silent Grove | Rowan Ashborne | Fantasy | 1978 |
| Shadows of Solitude | Rowan Ashborne | Mystery | 1966 |
| Legends of the Rift | Orion Frostblade | Horror | 1954 |
| Whispers of the Abyss | Isla Windrider | Historical | 1995 |
<end>Please transform the following yml data into JSON:
- Cache Hit Ratio (%): 93.77
  Connection Count: 230
  Queries per Second: 4749.45
  Timestamp: '2021-01-16 16:16:56'
- Cache Hit Ratio (%): 94.91
  Connection Count: 307
  Queries per Second: 69.19
  Timestamp: '2022-12-13 04:17:29'
- Cache Hit Ratio (%): 88.52
  Connection Count: 58
  Queries per Second: 3731.59
  Timestamp: '2022-06-27 08:52:46'
- Cache Hit Ratio (%): 95.59
  Connection Count: 87
  Queries per Second: 4372.32
  Timestamp: '2021-08-26 12:27:55'
- Cache Hit Ratio (%): 84.62
  Connection Count: 443
  Queries per Second: 3472.15
  Timestamp: '2023-01-06 15:07:01'
<start>
[
    {
        "Queries per Second": 4749.45,
        "Cache Hit Ratio (%)": 93.77,
        "Connection Count": 230,
        "Timestamp": "2021-01-16 16:16:56"
    },
    {
        "Queries per Second": 69.19,
        "Cache Hit Ratio (%)": 94.91,
        "Connection Count": 307,
        "Timestamp": "2022-12-13 04:17:29"
    },
    {
        "Queries per Second": 3731.59,
        "Cache Hit Ratio (%)": 88.52,
        "Connection Count": 58,
        "Timestamp": "2022-06-27 08:52:46"
    },
    {
        "Queries per Second": 4372.32,
        "Cache Hit Ratio (%)": 95.59,
        "Connection Count": 87,
        "Timestamp": "2021-08-26 12:27:55"
    },
    {
        "Queries per Second": 3472.15,
        "Cache Hit Ratio (%)": 84.62,
        "Connection Count": 443,
        "Timestamp": "2023-01-06 15:07:01"
    }
]
<end>Here's some Json data, can you convert it to MARKDOWN?
[
    {
        "SKU": "SKU-1025",
        "Price": 121.62,
        "Stock Quantity": 409,
        "Category": "Sports",
        "Supplier Name": "ACME Corp"
    },
    {
        "SKU": "SKU-1091",
        "Price": 135.31,
        "Stock Quantity": 89,
        "Category": "Sports",
        "Supplier Name": "Umbrella Corp"
    },
    {
        "SKU": "SKU-1011",
        "Price": 10.39,
        "Stock Quantity": 46,
        "Category": "Toys",
        "Supplier Name": "Globex"
    },
    {
        "SKU": "SKU-1044",
        "Price": 303.06,
        "Stock Quantity": 428,
        "Category": "Sports",
        "Supplier Name": "Wayne Enterprises"
    },
    {
        "SKU": "SKU-1091",
        "Price": 411.79,
        "Stock Quantity": 6,
        "Category": "Electronics",
        "Supplier Name": "Wayne Enterprises"
    },
    {
        "SKU": "SKU-1056",
        "Price": 235.98,
        "Stock Quantity": 97,
        "Category": "Household",
        "Supplier Name": "Wonka Industries"
    },
    {
        "SKU": "SKU-1038",
        "Price": 143.94,
        "Stock Quantity": 307,
        "Category": "Toys",
        "Supplier Name": "Globex"
    },
    {
        "SKU": "SKU-1093",
        "Price": 91.86,
        "Stock Quantity": 359,
        "Category": "Toys",
        "Supplier Name": "Wayne Enterprises"
    },
    {
        "SKU": "SKU-1056",
        "Price": 93.21,
        "Stock Quantity": 242,
        "Category": "Electronics",
        "Supplier Name": "Wonka Industries"
    },
    {
        "SKU": "SKU-1097",
        "Price": 245.57,
        "Stock Quantity": 361,
        "Category": "Toys",
        "Supplier Name": "Wayne Enterprises"
    }
]<start>
| SKU | Price | Stock Quantity | Category | Supplier Name |
| --- | --- | --- | --- | --- |
| SKU-1025 | 121.62 | 409 | Sports | ACME Corp |
| SKU-1091 | 135.31 | 89 | Sports | Umbrella Corp |
| SKU-1011 | 10.39 | 46 | Toys | Globex |
| SKU-1044 | 303.06 | 428 | Sports | Wayne Enterprises |
| SKU-1091 | 411.79 | 6 | Electronics | Wayne Enterprises |
| SKU-1056 | 235.98 | 97 | Household | Wonka Industries |
| SKU-1038 | 143.94 | 307 | Toys | Globex |
| SKU-1093 | 91.86 | 359 | Toys | Wayne Enterprises |
| SKU-1056 | 93.21 | 242 | Electronics | Wonka Industries |
| SKU-1097 | 245.57 | 361 | Toys | Wayne Enterprises |
<end>Transform this PLAIN TEXT structure to a Markdown format:
Author: Elara Moonshadow | Publication Year: 1965
Author: Isla Windrider | Publication Year: 1989
Author: Kara Firebrand | Publication Year: 1984
Author: Orion Frostblade | Publication Year: 2022
Author: Rowan Ashborne | Publication Year: 1993
Author: Orion Frostblade | Publication Year: 1965
Author: Draven Blackthorn | Publication Year: 1957
Author: Galen Starfire | Publication Year: 1979
Author: Kara Firebrand | Publication Year: 2009
Author: Orion Frostblade | Publication Year: 1952
<start>
| Author | Publication Year |
| --- | --- |
| Elara Moonshadow | 1965 |
| Isla Windrider | 1989 |
| Kara Firebrand | 1984 |
| Orion Frostblade | 2022 |
| Rowan Ashborne | 1993 |
| Orion Frostblade | 1965 |
| Draven Blackthorn | 1957 |
| Galen Starfire | 1979 |
| Kara Firebrand | 2009 |
| Orion Frostblade | 1952 |
<end>Convert this Yml to MARKDOWN:
- Author: Galen Starfire
  Genre: Thriller
  Publication Year: 1976
  Rating: 2.3
  Title: Legends of the Rift
- Author: Orion Frostblade
  Genre: Horror
  Publication Year: 1961
  Rating: 1.5
  Title: Echoes of Eternity
- Author: Rowan Ashborne
  Genre: Historical
  Publication Year: 2004
  Rating: 2.0
  Title: Legends of the Rift
<start>
| Title | Author | Genre | Publication Year | Rating |
| --- | --- | --- | --- | --- |
| Legends of the Rift | Galen Starfire | Thriller | 1976 | 2.3 |
| Echoes of Eternity | Orion Frostblade | Horror | 1961 | 1.5 |
| Legends of the Rift | Rowan Ashborne | Historical | 2004 | 2.0 |
<end>Here's some plain text data, can you convert it to json?
Restaurant Name: Curry Corner | Cuisine: Italian | Location: Houston | Rating: 4
Restaurant Name: Pasta Palace | Cuisine: Mediterranean | Location: Chicago | Rating: 4
Restaurant Name: Vegan Delight | Cuisine: Italian | Location: New York | Rating: 1
Restaurant Name: Curry Corner | Cuisine: Indian | Location: Seattle | Rating: 3
Restaurant Name: Vegan Delight | Cuisine: Italian | Location: Seattle | Rating: 4
Restaurant Name: Pasta Palace | Cuisine: Mediterranean | Location: Seattle | Rating: 1
Restaurant Name: Pizza Planet | Cuisine: French | Location: San Francisco | Rating: 4
Restaurant Name: Pizza Planet | Cuisine: Mediterranean | Location: Los Angeles | Rating: 5
Restaurant Name: BBQ Barn | Cuisine: American | Location: San Francisco | Rating: 3
<start>
[
    {
        "Restaurant Name": "Curry Corner",
        "Cuisine": "Italian",
        "Location": "Houston",
        "Rating": 4
    },
    {
        "Restaurant Name": "Pasta Palace",
        "Cuisine": "Mediterranean",
        "Location": "Chicago",
        "Rating": 4
    },
    {
        "Restaurant Name": "Vegan Delight",
        "Cuisine": "Italian",
        "Location": "New York",
        "Rating": 1
    },
    {
        "Restaurant Name": "Curry Corner",
        "Cuisine": "Indian",
        "Location": "Seattle",
        "Rating": 3
    },
    {
        "Restaurant Name": "Vegan Delight",
        "Cuisine": "Italian",
        "Location": "Seattle",
        "Rating": 4
    },
    {
        "Restaurant Name": "Pasta Palace",
        "Cuisine": "Mediterranean",
        "Location": "Seattle",
        "Rating": 1
    },
    {
        "Restaurant Name": "Pizza Planet",
        "Cuisine": "French",
        "Location": "San Francisco",
        "Rating": 4
    },
    {
        "Restaurant Name": "Pizza Planet",
        "Cuisine": "Mediterranean",
        "Location": "Los Angeles",
        "Rating": 5
    },
    {
        "Restaurant Name": "BBQ Barn",
        "Cuisine": "American",
        "Location": "San Francisco",
        "Rating": 3
    }
]
<end>Here's some YAML data, can you convert it to Markdown?
- Battery Level (%): 90.7
  Device Type: Motion Detector
  Location: Garage
  Reading Value: -12.89
- Battery Level (%): 61.7
  Device Type: Motion Detector
  Location: Hallway
  Reading Value: 84.07
- Battery Level (%): 65.3
  Device Type: Humidity Sensor
  Location: Garden
  Reading Value: -37.1
- Battery Level (%): 27.9
  Device Type: Temperature Sensor
  Location: Kitchen
  Reading Value: -37.29
- Battery Level (%): 98.3
  Device Type: Pressure Sensor
  Location: Office
  Reading Value: 19.08
- Battery Level (%): 42.6
  Device Type: Motion Detector
  Location: Office
  Reading Value: 50.25
<start>
| Device Type | Location | Battery Level (%) | Reading Value |
| --- | --- | --- | --- |
| Motion Detector | Garage | 90.7 | -12.89 |
| Motion Detector | Hallway | 61.7 | 84.07 |
| Humidity Sensor | Garden | 65.3 | -37.1 |
| Temperature Sensor | Kitchen | 27.9 | -37.29 |
| Pressure Sensor | Office | 98.3 | 19.08 |
| Motion Detector | Office | 42.6 | 50.25 |
<end>Convert this Plain text to Markdown:
Company: TechnoCorp | Date: 2014-10-10 | Open Price: 1112.43 | Close Price: 232.18 | High Price: 1112.43 | Low Price: 232.18 | Volume: 9481513
Company: RetailWorld | Date: 2014-09-24 | Open Price: 1322.77 | Close Price: 87.06 | High Price: 1322.77 | Low Price: 87.06 | Volume: 8810623
Company: HealthGen | Date: 2015-09-14 | Open Price: 639.2 | Close Price: 666.77 | High Price: 666.77 | Low Price: 639.2 | Volume: 3857142
Company: HealthGen | Date: 2017-04-22 | Open Price: 108.47 | Close Price: 603.36 | High Price: 1428.01 | Low Price: 108.47 | Volume: 6331080
Company: AutoMotive | Date: 2016-05-23 | Open Price: 474.34 | Close Price: 448.78 | High Price: 567.06 | Low Price: 448.78 | Volume: 853755
Company: TechnoCorp | Date: 2014-06-15 | Open Price: 338.45 | Close Price: 534.74 | High Price: 639.14 | Low Price: 338.45 | Volume: 1718835
Company: GreenEnergy | Date: 2014-10-28 | Open Price: 362.29 | Close Price: 611.01 | High Price: 611.01 | Low Price: 41.38 | Volume: 8982280
Company: BioLife | Date: 2019-03-11 | Open Price: 705.03 | Close Price: 786.49 | High Price: 786.49 | Low Price: 705.03 | Volume: 9255488
Company: AutoMotive | Date: 2021-08-27 | Open Price: 232.18 | Close Price: 706.88 | High Price: 1144.25 | Low Price: 232.18 | Volume: 5608054
<start>
| Company | Date | Open Price | Close Price | High Price | Low Price | Volume |
| --- | --- | --- | --- | --- | --- | --- |
| TechnoCorp | 2014-10-10 | 1112.43 | 232.18 | 1112.43 | 232.18 | 9481513 |
| RetailWorld | 2014-09-24 | 1322.77 | 87.06 | 1322.77 | 87.06 | 8810623 |
| HealthGen | 2015-09-14 | 639.2 | 666.77 | 666.77 | 639.2 | 3857142 |
| HealthGen | 2017-04-22 | 108.47 | 603.36 | 1428.01 | 108.47 | 6331080 |
| AutoMotive | 2016-05-23 | 474.34 | 448.78 | 567.06 | 448.78 | 853755 |
| TechnoCorp | 2014-06-15 | 338.45 | 534.74 | 639.14 | 338.45 | 1718835 |
| GreenEnergy | 2014-10-28 | 362.29 | 611.01 | 611.01 | 41.38 | 8982280 |
| BioLife | 2019-03-11 | 705.03 | 786.49 | 786.49 | 705.03 | 9255488 |
| AutoMotive | 2021-08-27 | 232.18 | 706.88 | 1144.25 | 232.18 | 5608054 |
<end>Here's some CSV data, can you convert it to plain text?
Name,Income
Monique,420000
Emerson,75000
Isaiah,410000
<start>
Name: Monique | Income: 420000
Name: Emerson | Income: 75000
Name: Isaiah | Income: 410000
<end>Please transform the following csv data into JSON:
Device ID,Device Type,Location,Battery Level (%),Reading Value,Timestamp
device-0004,Humidity Sensor,Hallway,32.3,49.01,2023-06-09 17:00:25
device-0054,Motion Detector,Kitchen,22.3,40.04,2021-02-16 13:01:19
device-0044,Motion Detector,Garage,17.9,-38.05,2023-04-01 22:11:25
<start>
[
    {
        "Device ID": "device-0004",
        "Device Type": "Humidity Sensor",
        "Location": "Hallway",
        "Battery Level (%)": 32.3,
        "Reading Value": 49.01,
        "Timestamp": "2023-06-09 17:00:25"
    },
    {
        "Device ID": "device-0054",
        "Device Type": "Motion Detector",
        "Location": "Kitchen",
        "Battery Level (%)": 22.3,
        "Reading Value": 40.04,
        "Timestamp": "2021-02-16 13:01:19"
    },
    {
        "Device ID": "device-0044",
        "Device Type": "Motion Detector",
        "Location": "Garage",
        "Battery Level (%)": 17.9,
        "Reading Value": -38.05,
        "Timestamp": "2023-04-01 22:11:25"
    }
]
<end>Convert this plain text to yaml:
Queries per Second: 2796.2 | Cache Hit Ratio (%): 98.03 | Average Latency (ms): 68.25
Queries per Second: 2786.94 | Cache Hit Ratio (%): 99.68 | Average Latency (ms): 7.14
Queries per Second: 2655.99 | Cache Hit Ratio (%): 80.31 | Average Latency (ms): 43.77
Queries per Second: 4940.71 | Cache Hit Ratio (%): 86.71 | Average Latency (ms): 68.25
Queries per Second: 1841.25 | Cache Hit Ratio (%): 99.52 | Average Latency (ms): 96.5
Queries per Second: 3393.21 | Cache Hit Ratio (%): 99.13 | Average Latency (ms): 89.57
Queries per Second: 3630.79 | Cache Hit Ratio (%): 84.84 | Average Latency (ms): 25.6
<start>
- Average Latency (ms): 68.25
  Cache Hit Ratio (%): 98.03
  Queries per Second: 2796.2
- Average Latency (ms): 7.14
  Cache Hit Ratio (%): 99.68
  Queries per Second: 2786.94
- Average Latency (ms): 43.77
  Cache Hit Ratio (%): 80.31
  Queries per Second: 2655.99
- Average Latency (ms): 68.25
  Cache Hit Ratio (%): 86.71
  Queries per Second: 4940.71
- Average Latency (ms): 96.5
  Cache Hit Ratio (%): 99.52
  Queries per Second: 1841.25
- Average Latency (ms): 89.57
  Cache Hit Ratio (%): 99.13
  Queries per Second: 3393.21
- Average Latency (ms): 25.6
  Cache Hit Ratio (%): 84.84
  Queries per Second: 3630.79
<end>Convert this plain text to JSON:
Genre: Non-Fiction | Rating: 3.8
Genre: Mystery | Rating: 4.3
Genre: Non-Fiction | Rating: 2.3
Genre: Thriller | Rating: 3.4
Genre: Thriller | Rating: 1.4
Genre: Thriller | Rating: 2.1
Genre: Romance | Rating: 1.2
Genre: Historical | Rating: 4.9
<start>
[
    {
        "Genre": "Non-Fiction",
        "Rating": 3.8
    },
    {
        "Genre": "Mystery",
        "Rating": 4.3
    },
    {
        "Genre": "Non-Fiction",
        "Rating": 2.3
    },
    {
        "Genre": "Thriller",
        "Rating": 3.4
    },
    {
        "Genre": "Thriller",
        "Rating": 1.4
    },
    {
        "Genre": "Thriller",
        "Rating": 2.1
    },
    {
        "Genre": "Romance",
        "Rating": 1.2
    },
    {
        "Genre": "Historical",
        "Rating": 4.9
    }
]
<end>Convert this yaml to markdown:
- Box Office Earnings (M): 928.18
  Genre: Fantasy
  Release Year: 1977
  Title: The Final Voyage
- Box Office Earnings (M): 914.56
  Genre: Comedy
  Release Year: 2002
  Title: The Final Voyage
- Box Office Earnings (M): 80.84
  Genre: Sci-Fi
  Release Year: 2002
  Title: Mystery of the Depths
<start>
| Title | Genre | Release Year | Box Office Earnings (M) |
| --- | --- | --- | --- |
| The Final Voyage | Fantasy | 1977 | 928.18 |
| The Final Voyage | Comedy | 2002 | 914.56 |
| Mystery of the Depths | Sci-Fi | 2002 | 80.84 |
<end>Can you change this MARKDOWN into json?
| Title | Director | Box Office Earnings (M) |
| --- | --- | --- |
| Dreamwalker | Aria Ravenwood | 730.17 |
| Dreamwalker | Orin Shadowalker | 119.83 |
| Beyond the Veil | Drake Nightshade | 143.78 |
| The Great Expedition | Mara Moonshadow | 308.61 |
| Dreamwalker | Drake Nightshade | 527.43 |
| The Final Voyage | Cade Firebrand | 184.72 |
| Edge of Infinity | Aria Ravenwood | 258.57 |
| Edge of Infinity | Talon Blackthorn | 875.94 |<start>
[
    {
        "Title": "Dreamwalker",
        "Director": "Aria Ravenwood",
        "Box Office Earnings (M)": 730.17
    },
    {
        "Title": "Dreamwalker",
        "Director": "Orin Shadowalker",
        "Box Office Earnings (M)": 119.83
    },
    {
        "Title": "Beyond the Veil",
        "Director": "Drake Nightshade",
        "Box Office Earnings (M)": 143.78
    },
    {
        "Title": "The Great Expedition",
        "Director": "Mara Moonshadow",
        "Box Office Earnings (M)": 308.61
    },
    {
        "Title": "Dreamwalker",
        "Director": "Drake Nightshade",
        "Box Office Earnings (M)": 527.43
    },
    {
        "Title": "The Final Voyage",
        "Director": "Cade Firebrand",
        "Box Office Earnings (M)": 184.72
    },
    {
        "Title": "Edge of Infinity",
        "Director": "Aria Ravenwood",
        "Box Office Earnings (M)": 258.57
    },
    {
        "Title": "Edge of Infinity",
        "Director": "Talon Blackthorn",
        "Box Office Earnings (M)": 875.94
    }
]
<end>Convert this yaml to markdown:
- Category: Household
  Price: 307.18
  Product Name: Widget
  SKU: SKU-1029
  Supplier Name: Umbrella Corp
- Category: Household
  Price: 394.77
  Product Name: Contraption
  SKU: SKU-1076
  Supplier Name: Wonka Industries
- Category: Automotive
  Price: 470.54
  Product Name: Gizmo
  SKU: SKU-1023
  Supplier Name: Wonka Industries
- Category: Sports
  Price: 147.46
  Product Name: Apparatus
  SKU: SKU-1079
  Supplier Name: Wayne Enterprises
- Category: Toys
  Price: 471.18
  Product Name: Gadget
  SKU: SKU-1004
  Supplier Name: ACME Corp
- Category: Electronics
  Price: 131.64
  Product Name: Gadget
  SKU: SKU-1004
  Supplier Name: Umbrella Corp
- Category: Electronics
  Price: 381.63
  Product Name: Gadget
  SKU: SKU-1093
  Supplier Name: ACME Corp
- Category: Electronics
  Price: 196.21
  Product Name: Instrument
  SKU: SKU-1032
  Supplier Name: Umbrella Corp
- Category: Toys
  Price: 451.77
  Product Name: Thingamajig
  SKU: SKU-1013
  Supplier Name: Globex
<start>
| Product Name | SKU | Price | Category | Supplier Name |
| --- | --- | --- | --- | --- |
| Widget | SKU-1029 | 307.18 | Household | Umbrella Corp |
| Contraption | SKU-1076 | 394.77 | Household | Wonka Industries |
| Gizmo | SKU-1023 | 470.54 | Automotive | Wonka Industries |
| Apparatus | SKU-1079 | 147.46 | Sports | Wayne Enterprises |
| Gadget | SKU-1004 | 471.18 | Toys | ACME Corp |
| Gadget | SKU-1004 | 131.64 | Electronics | Umbrella Corp |
| Gadget | SKU-1093 | 381.63 | Electronics | ACME Corp |
| Instrument | SKU-1032 | 196.21 | Electronics | Umbrella Corp |
| Thingamajig | SKU-1013 | 451.77 | Toys | Globex |
<end>Convert this Json to PLAIN TEXT:
[
    {
        "Product Name": "Widget",
        "SKU": "SKU-1004",
        "Price": 93.19,
        "Stock Quantity": 450,
        "Supplier Name": "ACME Corp"
    },
    {
        "Product Name": "Whatchamacallit",
        "SKU": "SKU-1047",
        "Price": 249.75,
        "Stock Quantity": 121,
        "Supplier Name": "Wayne Enterprises"
    },
    {
        "Product Name": "Apparatus",
        "SKU": "SKU-1019",
        "Price": 269.92,
        "Stock Quantity": 221,
        "Supplier Name": "ACME Corp"
    },
    {
        "Product Name": "Apparatus",
        "SKU": "SKU-1014",
        "Price": 402.58,
        "Stock Quantity": 344,
        "Supplier Name": "Globex"
    }
]<start>
Product Name: Widget | SKU: SKU-1004 | Price: 93.19 | Stock Quantity: 450 | Supplier Name: ACME Corp
Product Name: Whatchamacallit | SKU: SKU-1047 | Price: 249.75 | Stock Quantity: 121 | Supplier Name: Wayne Enterprises
Product Name: Apparatus | SKU: SKU-1019 | Price: 269.92 | Stock Quantity: 221 | Supplier Name: ACME Corp
Product Name: Apparatus | SKU: SKU-1014 | Price: 402.58 | Stock Quantity: 344 | Supplier Name: Globex
<end>Here's some Csv data, can you convert it to markdown?
Database Name,Cache Hit Ratio (%),Connection Count,Timestamp
UserDB,84.84,88,2021-12-07 14:35:22
SalesDB,93.5,145,2021-07-17 20:18:06
OrdersDB,83.49,170,2021-03-16 19:57:16
LogsDB,93.37,26,2023-05-09 21:44:45
AnalyticsDB,90.08,243,2021-05-19 16:58:17
InventoryDB,87.55,382,2021-10-20 23:20:00
ProductsDB,80.4,95,2023-10-08 01:25:48
<start>
| Database Name | Cache Hit Ratio (%) | Connection Count | Timestamp |
| --- | --- | --- | --- |
| UserDB | 84.84 | 88 | 2021-12-07 14:35:22 |
| SalesDB | 93.5 | 145 | 2021-07-17 20:18:06 |
| OrdersDB | 83.49 | 170 | 2021-03-16 19:57:16 |
| LogsDB | 93.37 | 26 | 2023-05-09 21:44:45 |
| AnalyticsDB | 90.08 | 243 | 2021-05-19 16:58:17 |
| InventoryDB | 87.55 | 382 | 2021-10-20 23:20:00 |
| ProductsDB | 80.4 | 95 | 2023-10-08 01:25:48 |
<end>Can you change this yml into markdown?
- Annual Revenue (B): 458.89
  Market Cap: Large Cap
  Sector: Automotive
- Annual Revenue (B): 321.02
  Market Cap: Mega Cap
  Sector: Biotech
- Annual Revenue (B): 217.3
  Market Cap: Small Cap
  Sector: Retail
- Annual Revenue (B): 347.43
  Market Cap: Mega Cap
  Sector: Healthcare
- Annual Revenue (B): 187.77
  Market Cap: Small Cap
  Sector: Biotech
- Annual Revenue (B): 487.89
  Market Cap: Mega Cap
  Sector: Healthcare
- Annual Revenue (B): 347.04
  Market Cap: Mega Cap
  Sector: Retail
- Annual Revenue (B): 118.72
  Market Cap: Mid Cap
  Sector: Aerospace
- Annual Revenue (B): 278.33
  Market Cap: Small Cap
  Sector: Biotech
<start>
| Sector | Market Cap | Annual Revenue (B) |
| --- | --- | --- |
| Automotive | Large Cap | 458.89 |
| Biotech | Mega Cap | 321.02 |
| Retail | Small Cap | 217.3 |
| Healthcare | Mega Cap | 347.43 |
| Biotech | Small Cap | 187.77 |
| Healthcare | Mega Cap | 487.89 |
| Retail | Mega Cap | 347.04 |
| Aerospace | Mid Cap | 118.72 |
| Biotech | Small Cap | 278.33 |
<end>Here's some csv data, can you convert it to Json?
Condition,Temperature (C),Wind Speed (km/h),Day
Windy,6.3,6.1,Saturday
Snowy,0.9,11.2,Thursday
Foggy,14.3,11.2,Saturday
Foggy,-8.7,26.9,Monday
Cloudy,31.7,24.9,Wednesday
Rainy,35.8,16.3,Sunday
Windy,24.5,25.3,Friday
<start>
[
    {
        "Condition": "Windy",
        "Temperature (C)": 6.3,
        "Wind Speed (km/h)": 6.1,
        "Day": "Saturday"
    },
    {
        "Condition": "Snowy",
        "Temperature (C)": 0.9,
        "Wind Speed (km/h)": 11.2,
        "Day": "Thursday"
    },
    {
        "Condition": "Foggy",
        "Temperature (C)": 14.3,
        "Wind Speed (km/h)": 11.2,
        "Day": "Saturday"
    },
    {
        "Condition": "Foggy",
        "Temperature (C)": -8.7,
        "Wind Speed (km/h)": 26.9,
        "Day": "Monday"
    },
    {
        "Condition": "Cloudy",
        "Temperature (C)": 31.7,
        "Wind Speed (km/h)": 24.9,
        "Day": "Wednesday"
    },
    {
        "Condition": "Rainy",
        "Temperature (C)": 35.8,
        "Wind Speed (km/h)": 16.3,
        "Day": "Sunday"
    },
    {
        "Condition": "Windy",
        "Temperature (C)": 24.5,
        "Wind Speed (km/h)": 25.3,
        "Day": "Friday"
    }
]
<end>Transform this plain text structure to a Markdown format:
Database Name: AnalyticsDB | Queries per Second: 2582.93 | Cache Hit Ratio (%): 70.67 | Average Latency (ms): 5.34
Database Name: LogsDB | Queries per Second: 1616.99 | Cache Hit Ratio (%): 90.9 | Average Latency (ms): 12.93
Database Name: UserDB | Queries per Second: 1473.14 | Cache Hit Ratio (%): 91.98 | Average Latency (ms): 12.93
Database Name: SessionsDB | Queries per Second: 3961.68 | Cache Hit Ratio (%): 81.4 | Average Latency (ms): 84.74
<start>
| Database Name | Queries per Second | Cache Hit Ratio (%) | Average Latency (ms) |
| --- | --- | --- | --- |
| AnalyticsDB | 2582.93 | 70.67 | 5.34 |
| LogsDB | 1616.99 | 90.9 | 12.93 |
| UserDB | 1473.14 | 91.98 | 12.93 |
| SessionsDB | 3961.68 | 81.4 | 84.74 |
<end>Convert this json to markdown:
[
    {
        "Product Name": "Whatchamacallit",
        "SKU": "SKU-1005",
        "Price": 497.81
    },
    {
        "Product Name": "Contraption",
        "SKU": "SKU-1026",
        "Price": 477.1
    },
    {
        "Product Name": "Apparatus",
        "SKU": "SKU-1061",
        "Price": 156.61
    },
    {
        "Product Name": "Thingamajig",
        "SKU": "SKU-1020",
        "Price": 56.12
    },
    {
        "Product Name": "Apparatus",
        "SKU": "SKU-1057",
        "Price": 312.67
    },
    {
        "Product Name": "Apparatus",
        "SKU": "SKU-1086",
        "Price": 400.1
    },
    {
        "Product Name": "Whatchamacallit",
        "SKU": "SKU-1021",
        "Price": 481.95
    },
    {
        "Product Name": "Whatchamacallit",
        "SKU": "SKU-1076",
        "Price": 266.27
    },
    {
        "Product Name": "Apparatus",
        "SKU": "SKU-1001",
        "Price": 325.99
    }
]<start>
| Product Name | SKU | Price |
| --- | --- | --- |
| Whatchamacallit | SKU-1005 | 497.81 |
| Contraption | SKU-1026 | 477.1 |
| Apparatus | SKU-1061 | 156.61 |
| Thingamajig | SKU-1020 | 56.12 |
| Apparatus | SKU-1057 | 312.67 |
| Apparatus | SKU-1086 | 400.1 |
| Whatchamacallit | SKU-1021 | 481.95 |
| Whatchamacallit | SKU-1076 | 266.27 |
| Apparatus | SKU-1001 | 325.99 |
<end>Please transform the following YML data into csv:
- Close Price: 848.37
  Date: '2021-10-17'
  High Price: 1389.0
  Open Price: 593.53
  Volume: 145484
- Close Price: 160.72
  Date: '2019-06-20'
  High Price: 962.22
  Open Price: 703.39
  Volume: 7438534
- Close Price: 615.69
  Date: '2015-03-04'
  High Price: 1415.25
  Open Price: 1415.25
  Volume: 9629605
<start>
Date,Open Price,Close Price,High Price,Volume
2021-10-17,593.53,848.37,1389.0,145484
2019-06-20,703.39,160.72,962.22,7438534
2015-03-04,1415.25,615.69,1415.25,9629605
<end>Can you change this plain text into markdown?
Age: 55 | Birth Month: January | City: San Antonio | Income: 450000
Age: 67 | Birth Month: June | City: San Antonio | Income: 85000
Age: 38 | Birth Month: March | City: Chicago | Income: 100000
Age: 41 | Birth Month: June | City: Indianapolis | Income: 50000
Age: 56 | Birth Month: August | City: Los Angeles | Income: 450000
Age: 60 | Birth Month: December | City: Boston | Income: 205000
Age: 43 | Birth Month: December | City: Las Vegas | Income: 50000
Age: 33 | Birth Month: August | City: New York | Income: 315000
<start>
| Age | Birth Month | City | Income |
| --- | --- | --- | --- |
| 55 | January | San Antonio | 450000 |
| 67 | June | San Antonio | 85000 |
| 38 | March | Chicago | 100000 |
| 41 | June | Indianapolis | 50000 |
| 56 | August | Los Angeles | 450000 |
| 60 | December | Boston | 205000 |
| 43 | December | Las Vegas | 50000 |
| 33 | August | New York | 315000 |
<end>Can you change this csv into json?
Title,Rating
Whispers of the Abyss,3.2
Tales of the Brave,5.0
Echoes of Eternity,4.0
The Forgotten World,2.6
Legends of the Rift,3.8
Tales of the Brave,4.8
The Last Sky,3.8
The Silent Grove,4.8
<start>
[
    {
        "Title": "Whispers of the Abyss",
        "Rating": 3.2
    },
    {
        "Title": "Tales of the Brave",
        "Rating": 5.0
    },
    {
        "Title": "Echoes of Eternity",
        "Rating": 4.0
    },
    {
        "Title": "The Forgotten World",
        "Rating": 2.6
    },
    {
        "Title": "Legends of the Rift",
        "Rating": 3.8
    },
    {
        "Title": "Tales of the Brave",
        "Rating": 4.8
    },
    {
        "Title": "The Last Sky",
        "Rating": 3.8
    },
    {
        "Title": "The Silent Grove",
        "Rating": 4.8
    }
]
<end>Please transform the following yaml data into MARKDOWN:
- Day: Saturday
  Humidity (%): 81
  Temperature (C): -1.0
- Day: Saturday
  Humidity (%): 60
  Temperature (C): 28.9
- Day: Sunday
  Humidity (%): 34
  Temperature (C): -6.1
- Day: Friday
  Humidity (%): 68
  Temperature (C): 18.2
<start>
| Temperature (C) | Humidity (%) | Day |
| --- | --- | --- |
| -1.0 | 81 | Saturday |
| 28.9 | 60 | Saturday |
| -6.1 | 34 | Sunday |
| 18.2 | 68 | Friday |
<end>Here's some Markdown data, can you convert it to plain text?
| Company | Date | Open Price | Volume |
| --- | --- | --- | --- |
| HealthGen | 2014-01-10 | 446.32 | 2026806 |
| GreenEnergy | 2012-12-10 | 86.65 | 859178 |
| AutoMotive | 2012-09-21 | 313.36 | 4350146 |
| BioLife | 2019-10-15 | 351.72 | 2610707 |
| BioLife | 2016-05-16 | 446.32 | 1637258 |
| RetailWorld | 2015-07-15 | 506.71 | 2610707 |
| MediaGroup | 2017-06-28 | 1370.2 | 3348765 |
| FinanceTrust | 2013-12-14 | 754.68 | 8081919 |
| MediaGroup | 2021-11-22 | 1223.93 | 1050271 |
| AutoMotive | 2022-10-27 | 1172.07 | 6026910 |<start>
Company: HealthGen | Date: 2014-01-10 | Open Price: 446.32 | Volume: 2026806
Company: GreenEnergy | Date: 2012-12-10 | Open Price: 86.65 | Volume: 859178
Company: AutoMotive | Date: 2012-09-21 | Open Price: 313.36 | Volume: 4350146
Company: BioLife | Date: 2019-10-15 | Open Price: 351.72 | Volume: 2610707
Company: BioLife | Date: 2016-05-16 | Open Price: 446.32 | Volume: 1637258
Company: RetailWorld | Date: 2015-07-15 | Open Price: 506.71 | Volume: 2610707
Company: MediaGroup | Date: 2017-06-28 | Open Price: 1370.2 | Volume: 3348765
Company: FinanceTrust | Date: 2013-12-14 | Open Price: 754.68 | Volume: 8081919
Company: MediaGroup | Date: 2021-11-22 | Open Price: 1223.93 | Volume: 1050271
Company: AutoMotive | Date: 2022-10-27 | Open Price: 1172.07 | Volume: 6026910
<end>Transform this yaml structure to a json format:
- Distance (miles): 612.0
  Duration (hours): 49.4
  End Location: Los Angeles
  Fuel Used (gallons): 9.2
  Start Location: Phoenix
  Trip Name: Forest Journey
- Distance (miles): 908.7
  Duration (hours): 55.4
  End Location: Phoenix
  Fuel Used (gallons): 29.0
  Start Location: Los Angeles
  Trip Name: Canyon Trek
- Distance (miles): 317.8
  Duration (hours): 23.5
  End Location: Los Angeles
  Fuel Used (gallons): 29.3
  Start Location: Phoenix
  Trip Name: Desert Drive
- Distance (miles): 1492.6
  Duration (hours): 61.7
  End Location: Miami
  Fuel Used (gallons): 95.7
  Start Location: San Francisco
  Trip Name: Historic Route
- Distance (miles): 1475.1
  Duration (hours): 11.1
  End Location: Los Angeles
  Fuel Used (gallons): 10.6
  Start Location: Phoenix
  Trip Name: Lakeside Retreat
- Distance (miles): 1761.8
  Duration (hours): 7.8
  End Location: Los Angeles
  Fuel Used (gallons): 87.8
  Start Location: New York
  Trip Name: Lakeside Retreat
- Distance (miles): 2980.5
  Duration (hours): 16.8
  End Location: Miami
  Fuel Used (gallons): 91.1
  Start Location: Houston
  Trip Name: City Explorer
- Distance (miles): 2769.5
  Duration (hours): 7.8
  End Location: New York
  Fuel Used (gallons): 61.4
  Start Location: Chicago
  Trip Name: Coast to Coast
- Distance (miles): 929.6
  Duration (hours): 35.5
  End Location: Miami
  Fuel Used (gallons): 56.1
  Start Location: San Francisco
  Trip Name: Historic Route
<start>
[
    {
        "Trip Name": "Forest Journey",
        "Start Location": "Phoenix",
        "End Location": "Los Angeles",
        "Distance (miles)": 612.0,
        "Duration (hours)": 49.4,
        "Fuel Used (gallons)": 9.2
    },
    {
        "Trip Name": "Canyon Trek",
        "Start Location": "Los Angeles",
        "End Location": "Phoenix",
        "Distance (miles)": 908.7,
        "Duration (hours)": 55.4,
        "Fuel Used (gallons)": 29.0
    },
    {
        "Trip Name": "Desert Drive",
        "Start Location": "Phoenix",
        "End Location": "Los Angeles",
        "Distance (miles)": 317.8,
        "Duration (hours)": 23.5,
        "Fuel Used (gallons)": 29.3
    },
    {
        "Trip Name": "Historic Route",
        "Start Location": "San Francisco",
        "End Location": "Miami",
        "Distance (miles)": 1492.6,
        "Duration (hours)": 61.7,
        "Fuel Used (gallons)": 95.7
    },
    {
        "Trip Name": "Lakeside Retreat",
        "Start Location": "Phoenix",
        "End Location": "Los Angeles",
        "Distance (miles)": 1475.1,
        "Duration (hours)": 11.1,
        "Fuel Used (gallons)": 10.6
    },
    {
        "Trip Name": "Lakeside Retreat",
        "Start Location": "New York",
        "End Location": "Los Angeles",
        "Distance (miles)": 1761.8,
        "Duration (hours)": 7.8,
        "Fuel Used (gallons)": 87.8
    },
    {
        "Trip Name": "City Explorer",
        "Start Location": "Houston",
        "End Location": "Miami",
        "Distance (miles)": 2980.5,
        "Duration (hours)": 16.8,
        "Fuel Used (gallons)": 91.1
    },
    {
        "Trip Name": "Coast to Coast",
        "Start Location": "Chicago",
        "End Location": "New York",
        "Distance (miles)": 2769.5,
        "Duration (hours)": 7.8,
        "Fuel Used (gallons)": 61.4
    },
    {
        "Trip Name": "Historic Route",
        "Start Location": "San Francisco",
        "End Location": "Miami",
        "Distance (miles)": 929.6,
        "Duration (hours)": 35.5,
        "Fuel Used (gallons)": 56.1
    }
]
<end>Convert this json to MARKDOWN:
[
    {
        "Author": "Sylvia Nightshade",
        "Genre": "Historical",
        "Rating": 3.6
    },
    {
        "Author": "Sylvia Nightshade",
        "Genre": "Non-Fiction",
        "Rating": 4.6
    },
    {
        "Author": "Thorne Ironwood",
        "Genre": "Non-Fiction",
        "Rating": 4.3
    }
]<start>
| Author | Genre | Rating |
| --- | --- | --- |
| Sylvia Nightshade | Historical | 3.6 |
| Sylvia Nightshade | Non-Fiction | 4.6 |
| Thorne Ironwood | Non-Fiction | 4.3 |
<end>Can you change this JSON into PLAIN TEXT?
[
    {
        "Device ID": "device-0085",
        "Device Type": "Motion Detector",
        "Location": "Hallway",
        "Battery Level (%)": 94.2,
        "Reading Value": 82.18,
        "Timestamp": "2021-08-22 22:07:47"
    },
    {
        "Device ID": "device-0021",
        "Device Type": "Motion Detector",
        "Location": "Bathroom",
        "Battery Level (%)": 22.4,
        "Reading Value": 1.57,
        "Timestamp": "2021-05-05 05:15:53"
    },
    {
        "Device ID": "device-0047",
        "Device Type": "Motion Detector",
        "Location": "Bathroom",
        "Battery Level (%)": 35.6,
        "Reading Value": 6.63,
        "Timestamp": "2021-02-03 13:20:59"
    },
    {
        "Device ID": "device-0100",
        "Device Type": "Temperature Sensor",
        "Location": "Garage",
        "Battery Level (%)": 95.2,
        "Reading Value": 66.02,
        "Timestamp": "2022-11-24 10:12:37"
    },
    {
        "Device ID": "device-0076",
        "Device Type": "Light Sensor",
        "Location": "Living Room",
        "Battery Level (%)": 86.5,
        "Reading Value": 71.41,
        "Timestamp": "2023-12-13 04:51:48"
    },
    {
        "Device ID": "device-0039",
        "Device Type": "Motion Detector",
        "Location": "Office",
        "Battery Level (%)": 43.9,
        "Reading Value": 82.18,
        "Timestamp": "2023-10-15 05:42:54"
    },
    {
        "Device ID": "device-0062",
        "Device Type": "Pressure Sensor",
        "Location": "Living Room",
        "Battery Level (%)": 46.5,
        "Reading Value": -13.09,
        "Timestamp": "2022-05-17 04:10:46"
    },
    {
        "Device ID": "device-0072",
        "Device Type": "Motion Detector",
        "Location": "Bedroom",
        "Battery Level (%)": 94.2,
        "Reading Value": 33.8,
        "Timestamp": "2023-03-26 12:28:59"
    }
]<start>
Device ID: device-0085 | Device Type: Motion Detector | Location: Hallway | Battery Level (%): 94.2 | Reading Value: 82.18 | Timestamp: 2021-08-22 22:07:47
Device ID: device-0021 | Device Type: Motion Detector | Location: Bathroom | Battery Level (%): 22.4 | Reading Value: 1.57 | Timestamp: 2021-05-05 05:15:53
Device ID: device-0047 | Device Type: Motion Detector | Location: Bathroom | Battery Level (%): 35.6 | Reading Value: 6.63 | Timestamp: 2021-02-03 13:20:59
Device ID: device-0100 | Device Type: Temperature Sensor | Location: Garage | Battery Level (%): 95.2 | Reading Value: 66.02 | Timestamp: 2022-11-24 10:12:37
Device ID: device-0076 | Device Type: Light Sensor | Location: Living Room | Battery Level (%): 86.5 | Reading Value: 71.41 | Timestamp: 2023-12-13 04:51:48
Device ID: device-0039 | Device Type: Motion Detector | Location: Office | Battery Level (%): 43.9 | Reading Value: 82.18 | Timestamp: 2023-10-15 05:42:54
Device ID: device-0062 | Device Type: Pressure Sensor | Location: Living Room | Battery Level (%): 46.5 | Reading Value: -13.09 | Timestamp: 2022-05-17 04:10:46
Device ID: device-0072 | Device Type: Motion Detector | Location: Bedroom | Battery Level (%): 94.2 | Reading Value: 33.8 | Timestamp: 2023-03-26 12:28:59
<end>Can you change this csv into yml?
Name,Income
Jorge,435000
Alexis,240000
Brooklyn,210000
<start>
- Income: 435000
  Name: Jorge
- Income: 240000
  Name: Alexis
- Income: 210000
  Name: Brooklyn
<end>Convert this json to Markdown:
[
    {
        "Sector": "Healthcare",
        "Market Cap": "Mid Cap",
        "Stock Price": 275.56,
        "Annual Revenue (B)": 169.24,
        "Quarter": "Q3"
    },
    {
        "Sector": "Finance",
        "Market Cap": "Mid Cap",
        "Stock Price": 126.55,
        "Annual Revenue (B)": 179.91,
        "Quarter": "Q4"
    },
    {
        "Sector": "Automotive",
        "Market Cap": "Large Cap",
        "Stock Price": 357.44,
        "Annual Revenue (B)": 314.77,
        "Quarter": "Q2"
    },
    {
        "Sector": "Automotive",
        "Market Cap": "Mid Cap",
        "Stock Price": 345.18,
        "Annual Revenue (B)": 193.6,
        "Quarter": "Q1"
    },
    {
        "Sector": "Aerospace",
        "Market Cap": "Large Cap",
        "Stock Price": 625.14,
        "Annual Revenue (B)": 369.94,
        "Quarter": "Q3"
    },
    {
        "Sector": "Energy",
        "Market Cap": "Large Cap",
        "Stock Price": 724.7,
        "Annual Revenue (B)": 331.88,
        "Quarter": "Q1"
    }
]<start>
| Sector | Market Cap | Stock Price | Annual Revenue (B) | Quarter |
| --- | --- | --- | --- | --- |
| Healthcare | Mid Cap | 275.56 | 169.24 | Q3 |
| Finance | Mid Cap | 126.55 | 179.91 | Q4 |
| Automotive | Large Cap | 357.44 | 314.77 | Q2 |
| Automotive | Mid Cap | 345.18 | 193.6 | Q1 |
| Aerospace | Large Cap | 625.14 | 369.94 | Q3 |
| Energy | Large Cap | 724.7 | 331.88 | Q1 |
<end>Can you change this Csv into json?
Database Name,Queries per Second,Connection Count,Average Latency (ms)
AnalyticsDB,4694.02,363,80.57
UserDB,4380.76,384,61.11
MetricsDB,3912.98,207,11.49
LogsDB,1953.38,225,46.36
SalesDB,1517.12,193,63.84
OrdersDB,56.96,243,16.52
<start>
[
    {
        "Database Name": "AnalyticsDB",
        "Queries per Second": 4694.02,
        "Connection Count": 363,
        "Average Latency (ms)": 80.57
    },
    {
        "Database Name": "UserDB",
        "Queries per Second": 4380.76,
        "Connection Count": 384,
        "Average Latency (ms)": 61.11
    },
    {
        "Database Name": "MetricsDB",
        "Queries per Second": 3912.98,
        "Connection Count": 207,
        "Average Latency (ms)": 11.49
    },
    {
        "Database Name": "LogsDB",
        "Queries per Second": 1953.38,
        "Connection Count": 225,
        "Average Latency (ms)": 46.36
    },
    {
        "Database Name": "SalesDB",
        "Queries per Second": 1517.12,
        "Connection Count": 193,
        "Average Latency (ms)": 63.84
    },
    {
        "Database Name": "OrdersDB",
        "Queries per Second": 56.96,
        "Connection Count": 243,
        "Average Latency (ms)": 16.52
    }
]
<end>Transform this yaml structure to a plain text format:
- Price Range: $$$$$
  Restaurant Name: Pasta Palace
- Price Range: $$$
  Restaurant Name: The Golden Spoon
- Price Range: $$$$$
  Restaurant Name: Burger Haven
- Price Range: $
  Restaurant Name: Sushi World
<start>
Restaurant Name: Pasta Palace | Price Range: $$$$$
Restaurant Name: The Golden Spoon | Price Range: $$$
Restaurant Name: Burger Haven | Price Range: $$$$$
Restaurant Name: Sushi World | Price Range: $
<end>Here's some Csv data, can you convert it to markdown?
Restaurant Name,Cuisine,Location,Rating,Price Range
Burger Haven,Mediterranean,Miami,3,$$$$$
The Golden Spoon,Mediterranean,Los Angeles,1,$$$$$
The Golden Spoon,Japanese,Seattle,2,$$$
Burger Haven,Indian,Los Angeles,4,$$$
<start>
| Restaurant Name | Cuisine | Location | Rating | Price Range |
| --- | --- | --- | --- | --- |
| Burger Haven | Mediterranean | Miami | 3 | $$$$$ |
| The Golden Spoon | Mediterranean | Los Angeles | 1 | $$$$$ |
| The Golden Spoon | Japanese | Seattle | 2 | $$$ |
| Burger Haven | Indian | Los Angeles | 4 | $$$ |
<end>Here's some csv data, can you convert it to json?
Name,Age,City,Income
Aubrey,19,Oklahoma City,285000
Victor,36,Memphis,260000
Meagan,47,Detroit,375000
Beulah,35,Portland,450000
<start>
[
    {
        "Name": "Aubrey",
        "Age": 19,
        "City": "Oklahoma City",
        "Income": 285000
    },
    {
        "Name": "Victor",
        "Age": 36,
        "City": "Memphis",
        "Income": 260000
    },
    {
        "Name": "Meagan",
        "Age": 47,
        "City": "Detroit",
        "Income": 375000
    },
    {
        "Name": "Beulah",
        "Age": 35,
        "City": "Portland",
        "Income": 450000
    }
]
<end>Please transform the following yaml data into csv:
- Category: Sports
  Price: 186.13
  Product Name: Whatchamacallit
  Supplier Name: Globex
- Category: Toys
  Price: 37.48
  Product Name: Apparatus
  Supplier Name: Wayne Enterprises
- Category: Automotive
  Price: 225.55
  Product Name: Doohickey
  Supplier Name: Umbrella Corp
<start>
Product Name,Price,Category,Supplier Name
Whatchamacallit,186.13,Sports,Globex
Apparatus,37.48,Toys,Wayne Enterprises
Doohickey,225.55,Automotive,Umbrella Corp
<end>Convert this CSV to json:
Date,Open Price,Close Price,High Price,Volume
2020-02-12,545.73,1164.13,1164.13,8903925
2012-06-09,77.38,389.15,651.88,9294172
2021-07-03,1222.76,463.28,1222.76,1711347
<start>
[
    {
        "Date": "2020-02-12",
        "Open Price": 545.73,
        "Close Price": 1164.13,
        "High Price": 1164.13,
        "Volume": 8903925
    },
    {
        "Date": "2012-06-09",
        "Open Price": 77.38,
        "Close Price": 389.15,
        "High Price": 651.88,
        "Volume": 9294172
    },
    {
        "Date": "2021-07-03",
        "Open Price": 1222.76,
        "Close Price": 463.28,
        "High Price": 1222.76,
        "Volume": 1711347
    }
]
<end>Convert this Plain text to markdown:
Title: The Final Voyage | Director: Talon Blackthorn
Title: Dreamwalker | Director: Orin Shadowalker
Title: Dreamwalker | Director: Zara Stormrider
<start>
| Title | Director |
| --- | --- |
| The Final Voyage | Talon Blackthorn |
| Dreamwalker | Orin Shadowalker |
| Dreamwalker | Zara Stormrider |
<end>Convert this Plain text to JSON:
Location: Denver | Condition: Foggy | Temperature (C): -7.0 | Humidity (%): 95 | Wind Speed (km/h): 23.6 | Day: Saturday
Location: Los Angeles | Condition: Snowy | Temperature (C): 4.9 | Humidity (%): 32 | Wind Speed (km/h): 23.6 | Day: Monday
Location: Los Angeles | Condition: Snowy | Temperature (C): 19.5 | Humidity (%): 92 | Wind Speed (km/h): 2.6 | Day: Sunday
Location: Miami | Condition: Stormy | Temperature (C): 21.6 | Humidity (%): 93 | Wind Speed (km/h): 22.2 | Day: Tuesday
Location: Seattle | Condition: Stormy | Temperature (C): -7.0 | Humidity (%): 66 | Wind Speed (km/h): 21.1 | Day: Tuesday
Location: Chicago | Condition: Windy | Temperature (C): 7.8 | Humidity (%): 20 | Wind Speed (km/h): 21.0 | Day: Wednesday
Location: Seattle | Condition: Sunny | Temperature (C): 5.3 | Humidity (%): 61 | Wind Speed (km/h): 26.4 | Day: Monday
Location: New York | Condition: Stormy | Temperature (C): 1.2 | Humidity (%): 96 | Wind Speed (km/h): 21.5 | Day: Monday
Location: New York | Condition: Snowy | Temperature (C): 36.4 | Humidity (%): 61 | Wind Speed (km/h): 23.6 | Day: Thursday
Location: Miami | Condition: Windy | Temperature (C): -0.7 | Humidity (%): 51 | Wind Speed (km/h): 28.3 | Day: Wednesday
<start>
[
    {
        "Location": "Denver",
        "Condition": "Foggy",
        "Temperature (C)": -7.0,
        "Humidity (%)": 95,
        "Wind Speed (km/h)": 23.6,
        "Day": "Saturday"
    },
    {
        "Location": "Los Angeles",
        "Condition": "Snowy",
        "Temperature (C)": 4.9,
        "Humidity (%)": 32,
        "Wind Speed (km/h)": 23.6,
        "Day": "Monday"
    },
    {
        "Location": "Los Angeles",
        "Condition": "Snowy",
        "Temperature (C)": 19.5,
        "Humidity (%)": 92,
        "Wind Speed (km/h)": 2.6,
        "Day": "Sunday"
    },
    {
        "Location": "Miami",
        "Condition": "Stormy",
        "Temperature (C)": 21.6,
        "Humidity (%)": 93,
        "Wind Speed (km/h)": 22.2,
        "Day": "Tuesday"
    },
    {
        "Location": "Seattle",
        "Condition": "Stormy",
        "Temperature (C)": -7.0,
        "Humidity (%)": 66,
        "Wind Speed (km/h)": 21.1,
        "Day": "Tuesday"
    },
    {
        "Location": "Chicago",
        "Condition": "Windy",
        "Temperature (C)": 7.8,
        "Humidity (%)": 20,
        "Wind Speed (km/h)": 21.0,
        "Day": "Wednesday"
    },
    {
        "Location": "Seattle",
        "Condition": "Sunny",
        "Temperature (C)": 5.3,
        "Humidity (%)": 61,
        "Wind Speed (km/h)": 26.4,
        "Day": "Monday"
    },
    {
        "Location": "New York",
        "Condition": "Stormy",
        "Temperature (C)": 1.2,
        "Humidity (%)": 96,
        "Wind Speed (km/h)": 21.5,
        "Day": "Monday"
    },
    {
        "Location": "New York",
        "Condition": "Snowy",
        "Temperature (C)": 36.4,
        "Humidity (%)": 61,
        "Wind Speed (km/h)": 23.6,
        "Day": "Thursday"
    },
    {
        "Location": "Miami",
        "Condition": "Windy",
        "Temperature (C)": -0.7,
        "Humidity (%)": 51,
        "Wind Speed (km/h)": 28.3,
        "Day": "Wednesday"
    }
]
<end>Please transform the following plain text data into yml:
Queries per Second: 2608.66 | Cache Hit Ratio (%): 93.13 | Connection Count: 443 | Timestamp: 2023-06-22 09:03:10
Queries per Second: 3771.52 | Cache Hit Ratio (%): 99.3 | Connection Count: 215 | Timestamp: 2023-03-16 03:45:20
Queries per Second: 726.11 | Cache Hit Ratio (%): 78.11 | Connection Count: 286 | Timestamp: 2021-07-22 03:11:40
Queries per Second: 98.28 | Cache Hit Ratio (%): 73.86 | Connection Count: 262 | Timestamp: 2023-07-17 06:32:02
Queries per Second: 2652.61 | Cache Hit Ratio (%): 89.95 | Connection Count: 112 | Timestamp: 2022-07-21 09:45:45
<start>
- Cache Hit Ratio (%): 93.13
  Connection Count: 443
  Queries per Second: 2608.66
  Timestamp: '2023-06-22 09:03:10'
- Cache Hit Ratio (%): 99.3
  Connection Count: 215
  Queries per Second: 3771.52
  Timestamp: '2023-03-16 03:45:20'
- Cache Hit Ratio (%): 78.11
  Connection Count: 286
  Queries per Second: 726.11
  Timestamp: '2021-07-22 03:11:40'
- Cache Hit Ratio (%): 73.86
  Connection Count: 262
  Queries per Second: 98.28
  Timestamp: '2023-07-17 06:32:02'
- Cache Hit Ratio (%): 89.95
  Connection Count: 112
  Queries per Second: 2652.61
  Timestamp: '2022-07-21 09:45:45'
<end>Convert this CSV to JSON:
Title,Author,Rating
The Forgotten World,Sylvia Nightshade,4.6
The Last Sky,Orion Frostblade,2.6
A Journey Through Time,Galen Starfire,1.5
The Silent Grove,Rowan Ashborne,3.4
Legends of the Rift,Thorne Ironwood,3.8
Tales of the Brave,Luna Silverleaf,2.9
Legends of the Rift,Galen Starfire,2.4
Whispers of the Abyss,Kara Firebrand,1.6
The Silent Grove,Sylvia Nightshade,3.5
<start>
[
    {
        "Title": "The Forgotten World",
        "Author": "Sylvia Nightshade",
        "Rating": 4.6
    },
    {
        "Title": "The Last Sky",
        "Author": "Orion Frostblade",
        "Rating": 2.6
    },
    {
        "Title": "A Journey Through Time",
        "Author": "Galen Starfire",
        "Rating": 1.5
    },
    {
        "Title": "The Silent Grove",
        "Author": "Rowan Ashborne",
        "Rating": 3.4
    },
    {
        "Title": "Legends of the Rift",
        "Author": "Thorne Ironwood",
        "Rating": 3.8
    },
    {
        "Title": "Tales of the Brave",
        "Author": "Luna Silverleaf",
        "Rating": 2.9
    },
    {
        "Title": "Legends of the Rift",
        "Author": "Galen Starfire",
        "Rating": 2.4
    },
    {
        "Title": "Whispers of the Abyss",
        "Author": "Kara Firebrand",
        "Rating": 1.6
    },
    {
        "Title": "The Silent Grove",
        "Author": "Sylvia Nightshade",
        "Rating": 3.5
    }
]
<end>Can you change this Markdown into PLAIN TEXT?
| Device ID | Device Type | Location | Battery Level (%) | Reading Value | Timestamp |
| --- | --- | --- | --- | --- | --- |
| device-0037 | Motion Detector | Garden | 48.3 | -23.19 | 2022-05-24 18:31:43 |
| device-0002 | Pressure Sensor | Garage | 34.3 | 50.47 | 2021-03-02 18:41:26 |
| device-0073 | Motion Detector | Bedroom | 63.2 | 45.25 | 2021-07-04 23:29:57 |
| device-0061 | Motion Detector | Bathroom | 98.9 | -1.77 | 2022-04-10 14:02:43 |
| device-0084 | Humidity Sensor | Living Room | 70.4 | 33.16 | 2023-02-04 18:13:51 |
| device-0021 | Temperature Sensor | Garage | 77.6 | 60.91 | 2023-08-16 11:24:24 |
| device-0032 | Temperature Sensor | Garage | 88.6 | -34.75 | 2021-09-02 09:35:36 |<start>
Device ID: device-0037 | Device Type: Motion Detector | Location: Garden | Battery Level (%): 48.3 | Reading Value: -23.19 | Timestamp: 2022-05-24 18:31:43
Device ID: device-0002 | Device Type: Pressure Sensor | Location: Garage | Battery Level (%): 34.3 | Reading Value: 50.47 | Timestamp: 2021-03-02 18:41:26
Device ID: device-0073 | Device Type: Motion Detector | Location: Bedroom | Battery Level (%): 63.2 | Reading Value: 45.25 | Timestamp: 2021-07-04 23:29:57
Device ID: device-0061 | Device Type: Motion Detector | Location: Bathroom | Battery Level (%): 98.9 | Reading Value: -1.77 | Timestamp: 2022-04-10 14:02:43
Device ID: device-0084 | Device Type: Humidity Sensor | Location: Living Room | Battery Level (%): 70.4 | Reading Value: 33.16 | Timestamp: 2023-02-04 18:13:51
Device ID: device-0021 | Device Type: Temperature Sensor | Location: Garage | Battery Level (%): 77.6 | Reading Value: 60.91 | Timestamp: 2023-08-16 11:24:24
Device ID: device-0032 | Device Type: Temperature Sensor | Location: Garage | Battery Level (%): 88.6 | Reading Value: -34.75 | Timestamp: 2021-09-02 09:35:36
<end>Convert this Csv to Markdown:
Company,Date,Open Price,Close Price,High Price
MediaGroup,2021-08-23,1153.03,465.15,1153.03
HealthGen,2022-05-05,234.16,767.58,1153.03
GreenEnergy,2019-12-02,96.6,870.33,870.33
HealthGen,2016-09-10,1102.05,327.51,1196.24
BioLife,2017-10-06,727.05,1173.6,1173.6
TechnoCorp,2015-12-22,397.98,774.68,774.68
RetailWorld,2017-04-07,549.06,1185.62,1191.03
<start>
| Company | Date | Open Price | Close Price | High Price |
| --- | --- | --- | --- | --- |
| MediaGroup | 2021-08-23 | 1153.03 | 465.15 | 1153.03 |
| HealthGen | 2022-05-05 | 234.16 | 767.58 | 1153.03 |
| GreenEnergy | 2019-12-02 | 96.6 | 870.33 | 870.33 |
| HealthGen | 2016-09-10 | 1102.05 | 327.51 | 1196.24 |
| BioLife | 2017-10-06 | 727.05 | 1173.6 | 1173.6 |
| TechnoCorp | 2015-12-22 | 397.98 | 774.68 | 774.68 |
| RetailWorld | 2017-04-07 | 549.06 | 1185.62 | 1191.03 |
<end>Here's some Markdown data, can you convert it to yaml?
| Device ID | Device Type | Location | Battery Level (%) | Timestamp |
| --- | --- | --- | --- | --- |
| device-0082 | Temperature Sensor | Bathroom | 21.1 | 2021-08-14 13:37:51 |
| device-0005 | Pressure Sensor | Living Room | 79.2 | 2022-04-16 03:25:29 |
| device-0003 | Motion Detector | Bathroom | 49.6 | 2021-01-05 21:50:09 |
| device-0056 | Pressure Sensor | Living Room | 34.3 | 2022-02-26 20:25:55 |
| device-0064 | Pressure Sensor | Garden | 61.7 | 2021-02-13 21:14:54 |
| device-0076 | Pressure Sensor | Bathroom | 24.2 | 2022-07-16 19:39:15 |
| device-0089 | Motion Detector | Kitchen | 95.2 | 2023-01-19 17:53:28 |
| device-0013 | Humidity Sensor | Bathroom | 79.9 | 2021-06-02 19:00:13 |
| device-0052 | Temperature Sensor | Garden | 79.2 | 2022-04-11 06:52:00 |<start>
- Battery Level (%): 21.1
  Device ID: device-0082
  Device Type: Temperature Sensor
  Location: Bathroom
  Timestamp: '2021-08-14 13:37:51'
- Battery Level (%): 79.2
  Device ID: device-0005
  Device Type: Pressure Sensor
  Location: Living Room
  Timestamp: '2022-04-16 03:25:29'
- Battery Level (%): 49.6
  Device ID: device-0003
  Device Type: Motion Detector
  Location: Bathroom
  Timestamp: '2021-01-05 21:50:09'
- Battery Level (%): 34.3
  Device ID: device-0056
  Device Type: Pressure Sensor
  Location: Living Room
  Timestamp: '2022-02-26 20:25:55'
- Battery Level (%): 61.7
  Device ID: device-0064
  Device Type: Pressure Sensor
  Location: Garden
  Timestamp: '2021-02-13 21:14:54'
- Battery Level (%): 24.2
  Device ID: device-0076
  Device Type: Pressure Sensor
  Location: Bathroom
  Timestamp: '2022-07-16 19:39:15'
- Battery Level (%): 95.2
  Device ID: device-0089
  Device Type: Motion Detector
  Location: Kitchen
  Timestamp: '2023-01-19 17:53:28'
- Battery Level (%): 79.9
  Device ID: device-0013
  Device Type: Humidity Sensor
  Location: Bathroom
  Timestamp: '2021-06-02 19:00:13'
- Battery Level (%): 79.2
  Device ID: device-0052
  Device Type: Temperature Sensor
  Location: Garden
  Timestamp: '2022-04-11 06:52:00'
<end>Here's some Markdown data, can you convert it to yml?
| Company | Date | Open Price | Close Price | High Price | Low Price |
| --- | --- | --- | --- | --- | --- |
| RetailWorld | 2016-02-21 | 1245.18 | 615.84 | 1245.18 | 615.84 |
| FoodChain | 2020-04-01 | 1139.92 | 57.88 | 1139.92 | 57.88 |
| FinanceTrust | 2017-11-17 | 623.53 | 247.26 | 1404.27 | 247.26 |
| AutoMotive | 2014-10-18 | 564.27 | 1297.04 | 1297.04 | 115.65 |
| HealthGen | 2020-03-26 | 49.92 | 671.22 | 671.22 | 49.92 |
| AeroSystems | 2010-03-21 | 133.25 | 678.97 | 1033.72 | 133.25 |
| RetailWorld | 2016-07-04 | 215.68 | 179.97 | 215.68 | 179.97 |<start>
- Close Price: 615.84
  Company: RetailWorld
  Date: '2016-02-21'
  High Price: 1245.18
  Low Price: 615.84
  Open Price: 1245.18
- Close Price: 57.88
  Company: FoodChain
  Date: '2020-04-01'
  High Price: 1139.92
  Low Price: 57.88
  Open Price: 1139.92
- Close Price: 247.26
  Company: FinanceTrust
  Date: '2017-11-17'
  High Price: 1404.27
  Low Price: 247.26
  Open Price: 623.53
- Close Price: 1297.04
  Company: AutoMotive
  Date: '2014-10-18'
  High Price: 1297.04
  Low Price: 115.65
  Open Price: 564.27
- Close Price: 671.22
  Company: HealthGen
  Date: '2020-03-26'
  High Price: 671.22
  Low Price: 49.92
  Open Price: 49.92
- Close Price: 678.97
  Company: AeroSystems
  Date: '2010-03-21'
  High Price: 1033.72
  Low Price: 133.25
  Open Price: 133.25
- Close Price: 179.97
  Company: RetailWorld
  Date: '2016-07-04'
  High Price: 215.68
  Low Price: 179.97
  Open Price: 215.68
<end>Can you change this csv into PLAIN TEXT?
Location,Condition,Temperature (C),Humidity (%),Wind Speed (km/h)
New York,Foggy,14.4,24,16.7
New York,Rainy,37.3,53,12.1
Miami,Cloudy,17.5,67,17.0
Los Angeles,Cloudy,6.3,35,13.1
<start>
Location: New York | Condition: Foggy | Temperature (C): 14.4 | Humidity (%): 24 | Wind Speed (km/h): 16.7
Location: New York | Condition: Rainy | Temperature (C): 37.3 | Humidity (%): 53 | Wind Speed (km/h): 12.1
Location: Miami | Condition: Cloudy | Temperature (C): 17.5 | Humidity (%): 67 | Wind Speed (km/h): 17.0
Location: Los Angeles | Condition: Cloudy | Temperature (C): 6.3 | Humidity (%): 35 | Wind Speed (km/h): 13.1
<end>Here's some CSV data, can you convert it to markdown?
Product Name,SKU,Stock Quantity,Category,Supplier Name
Device,SKU-1069,356,Sports,Globex
Instrument,SKU-1079,261,Automotive,Umbrella Corp
Contraption,SKU-1080,284,Household,ACME Corp
Whatchamacallit,SKU-1076,169,Household,ACME Corp
Contraption,SKU-1037,165,Automotive,ACME Corp
Contraption,SKU-1040,252,Automotive,Globex
Thingamajig,SKU-1093,345,Household,ACME Corp
Instrument,SKU-1020,304,Household,ACME Corp
Whatchamacallit,SKU-1010,4,Toys,ACME Corp
Gizmo,SKU-1011,208,Sports,Wonka Industries
<start>
| Product Name | SKU | Stock Quantity | Category | Supplier Name |
| --- | --- | --- | --- | --- |
| Device | SKU-1069 | 356 | Sports | Globex |
| Instrument | SKU-1079 | 261 | Automotive | Umbrella Corp |
| Contraption | SKU-1080 | 284 | Household | ACME Corp |
| Whatchamacallit | SKU-1076 | 169 | Household | ACME Corp |
| Contraption | SKU-1037 | 165 | Automotive | ACME Corp |
| Contraption | SKU-1040 | 252 | Automotive | Globex |
| Thingamajig | SKU-1093 | 345 | Household | ACME Corp |
| Instrument | SKU-1020 | 304 | Household | ACME Corp |
| Whatchamacallit | SKU-1010 | 4 | Toys | ACME Corp |
| Gizmo | SKU-1011 | 208 | Sports | Wonka Industries |
<end>Here's some json data, can you convert it to CSV?
[
    {
        "Title": "A Journey Through Time",
        "Author": "Draven Blackthorn",
        "Genre": "Romance",
        "Publication Year": 2022,
        "Rating": 2.5
    },
    {
        "Title": "The Forgotten World",
        "Author": "Orion Frostblade",
        "Genre": "Mystery",
        "Publication Year": 1973,
        "Rating": 4.2
    },
    {
        "Title": "Whispers of the Abyss",
        "Author": "Elara Moonshadow",
        "Genre": "Mystery",
        "Publication Year": 1982,
        "Rating": 2.2
    },
    {
        "Title": "Tales of the Brave",
        "Author": "Elara Moonshadow",
        "Genre": "Mystery",
        "Publication Year": 1984,
        "Rating": 3.8
    },
    {
        "Title": "The Silent Grove",
        "Author": "Elara Moonshadow",
        "Genre": "Science Fiction",
        "Publication Year": 1975,
        "Rating": 1.8
    }
]<start>
Title,Author,Genre,Publication Year,Rating
A Journey Through Time,Draven Blackthorn,Romance,2022,2.5
The Forgotten World,Orion Frostblade,Mystery,1973,4.2
Whispers of the Abyss,Elara Moonshadow,Mystery,1982,2.2
Tales of the Brave,Elara Moonshadow,Mystery,1984,3.8
The Silent Grove,Elara Moonshadow,Science Fiction,1975,1.8
<end>Please transform the following MARKDOWN data into Csv:
| Birth Month | City | Income |
| --- | --- | --- |
| August | San Diego | 395000 |
| March | Washington | 150000 |
| April | Las Vegas | 380000 |
| July | Memphis | 385000 |
| October | Houston | 185000 |<start>
Birth Month,City,Income
August,San Diego,395000
March,Washington,150000
April,Las Vegas,380000
July,Memphis,385000
October,Houston,185000
<end>Can you change this PLAIN TEXT into JSON?
Market Cap: Mega Cap | Stock Price: 448.86 | Annual Revenue (B): 349.8
Market Cap: Small Cap | Stock Price: 576.62 | Annual Revenue (B): 173.33
Market Cap: Mega Cap | Stock Price: 320.81 | Annual Revenue (B): 494.05
Market Cap: Mid Cap | Stock Price: 898.87 | Annual Revenue (B): 454.91
Market Cap: Large Cap | Stock Price: 253.28 | Annual Revenue (B): 163.55
Market Cap: Mega Cap | Stock Price: 898.87 | Annual Revenue (B): 347.87
Market Cap: Mega Cap | Stock Price: 136.08 | Annual Revenue (B): 355.89
Market Cap: Small Cap | Stock Price: 356.46 | Annual Revenue (B): 173.33
Market Cap: Mid Cap | Stock Price: 898.87 | Annual Revenue (B): 192.7
Market Cap: Mid Cap | Stock Price: 354.15 | Annual Revenue (B): 414.94
<start>
[
    {
        "Market Cap": "Mega Cap",
        "Stock Price": 448.86,
        "Annual Revenue (B)": 349.8
    },
    {
        "Market Cap": "Small Cap",
        "Stock Price": 576.62,
        "Annual Revenue (B)": 173.33
    },
    {
        "Market Cap": "Mega Cap",
        "Stock Price": 320.81,
        "Annual Revenue (B)": 494.05
    },
    {
        "Market Cap": "Mid Cap",
        "Stock Price": 898.87,
        "Annual Revenue (B)": 454.91
    },
    {
        "Market Cap": "Large Cap",
        "Stock Price": 253.28,
        "Annual Revenue (B)": 163.55
    },
    {
        "Market Cap": "Mega Cap",
        "Stock Price": 898.87,
        "Annual Revenue (B)": 347.87
    },
    {
        "Market Cap": "Mega Cap",
        "Stock Price": 136.08,
        "Annual Revenue (B)": 355.89
    },
    {
        "Market Cap": "Small Cap",
        "Stock Price": 356.46,
        "Annual Revenue (B)": 173.33
    },
    {
        "Market Cap": "Mid Cap",
        "Stock Price": 898.87,
        "Annual Revenue (B)": 192.7
    },
    {
        "Market Cap": "Mid Cap",
        "Stock Price": 354.15,
        "Annual Revenue (B)": 414.94
    }
]
<end>Here's some json data, can you convert it to yml?
[
    {
        "Company": "BioPharm",
        "Sector": "Finance",
        "Market Cap": "Small Cap",
        "Stock Price": 512.13,
        "Annual Revenue (B)": 345.9,
        "Quarter": "Q1"
    },
    {
        "Company": "TechCorp",
        "Sector": "Healthcare",
        "Market Cap": "Mid Cap",
        "Stock Price": 801.95,
        "Annual Revenue (B)": 86.22,
        "Quarter": "Q3"
    },
    {
        "Company": "BioPharm",
        "Sector": "Retail",
        "Market Cap": "Mega Cap",
        "Stock Price": 122.98,
        "Annual Revenue (B)": 272.42,
        "Quarter": "Q2"
    },
    {
        "Company": "Foodies",
        "Sector": "Aerospace",
        "Market Cap": "Small Cap",
        "Stock Price": 691.56,
        "Annual Revenue (B)": 331.56,
        "Quarter": "Q1"
    }
]<start>
- Annual Revenue (B): 345.9
  Company: BioPharm
  Market Cap: Small Cap
  Quarter: Q1
  Sector: Finance
  Stock Price: 512.13
- Annual Revenue (B): 86.22
  Company: TechCorp
  Market Cap: Mid Cap
  Quarter: Q3
  Sector: Healthcare
  Stock Price: 801.95
- Annual Revenue (B): 272.42
  Company: BioPharm
  Market Cap: Mega Cap
  Quarter: Q2
  Sector: Retail
  Stock Price: 122.98
- Annual Revenue (B): 331.56
  Company: Foodies
  Market Cap: Small Cap
  Quarter: Q1
  Sector: Aerospace
  Stock Price: 691.56
<end>Can you change this Yaml into plain text?
- Author: Elara Moonshadow
  Genre: Mystery
  Rating: 2.7
  Title: The Crystal Key
- Author: Orion Frostblade
  Genre: Fantasy
  Rating: 1.6
  Title: The Last Sky
- Author: Thorne Ironwood
  Genre: Science Fiction
  Rating: 3.9
  Title: The Forgotten World
- Author: Galen Starfire
  Genre: Mystery
  Rating: 3.2
  Title: Legends of the Rift
- Author: Galen Starfire
  Genre: Horror
  Rating: 1.7
  Title: Legends of the Rift
- Author: Elara Moonshadow
  Genre: Non-Fiction
  Rating: 3.4
  Title: The Last Sky
- Author: Draven Blackthorn
  Genre: Science Fiction
  Rating: 1.5
  Title: Whispers of the Abyss
- Author: Galen Starfire
  Genre: Non-Fiction
  Rating: 3.8
  Title: Legends of the Rift
<start>
Title: The Crystal Key | Author: Elara Moonshadow | Genre: Mystery | Rating: 2.7
Title: The Last Sky | Author: Orion Frostblade | Genre: Fantasy | Rating: 1.6
Title: The Forgotten World | Author: Thorne Ironwood | Genre: Science Fiction | Rating: 3.9
Title: Legends of the Rift | Author: Galen Starfire | Genre: Mystery | Rating: 3.2
Title: Legends of the Rift | Author: Galen Starfire | Genre: Horror | Rating: 1.7
Title: The Last Sky | Author: Elara Moonshadow | Genre: Non-Fiction | Rating: 3.4
Title: Whispers of the Abyss | Author: Draven Blackthorn | Genre: Science Fiction | Rating: 1.5
Title: Legends of the Rift | Author: Galen Starfire | Genre: Non-Fiction | Rating: 3.8
<end>Can you change this Csv into yml?
Condition,Temperature (C),Day
Stormy,19.6,Sunday
Cloudy,20.3,Sunday
Stormy,17.2,Tuesday
Rainy,30.5,Wednesday
Cloudy,23.0,Sunday
Foggy,37.8,Sunday
Sunny,26.6,Sunday
Snowy,26.7,Wednesday
Stormy,17.7,Tuesday
Stormy,37.4,Thursday
<start>
- Condition: Stormy
  Day: Sunday
  Temperature (C): 19.6
- Condition: Cloudy
  Day: Sunday
  Temperature (C): 20.3
- Condition: Stormy
  Day: Tuesday
  Temperature (C): 17.2
- Condition: Rainy
  Day: Wednesday
  Temperature (C): 30.5
- Condition: Cloudy
  Day: Sunday
  Temperature (C): 23.0
- Condition: Foggy
  Day: Sunday
  Temperature (C): 37.8
- Condition: Sunny
  Day: Sunday
  Temperature (C): 26.6
- Condition: Snowy
  Day: Wednesday
  Temperature (C): 26.7
- Condition: Stormy
  Day: Tuesday
  Temperature (C): 17.7
- Condition: Stormy
  Day: Thursday
  Temperature (C): 37.4
<end>Convert this Markdown to json:
| Company | Sector | Market Cap | Stock Price | Annual Revenue (B) | Quarter |
| --- | --- | --- | --- | --- | --- |
| AutoDrive | Technology | Mid Cap | 128.63 | 334.67 | Q2 |
| BioPharm | Technology | Mid Cap | 228.29 | 345.49 | Q2 |
| EcoEnergy | Biotech | Mega Cap | 140.9 | 101.3 | Q4 |
| Foodies | Finance | Mega Cap | 992.32 | 200.21 | Q1 |
| HealthPlus | Healthcare | Small Cap | 140.9 | 397.43 | Q3 |
| GlobalTrade | Technology | Mega Cap | 234.97 | 339.94 | Q3 |
| FinanceWorks | Healthcare | Mega Cap | 475.1 | 167.92 | Q4 |
| TechCorp | Finance | Mid Cap | 346.85 | 228.26 | Q4 |<start>
[
    {
        "Company": "AutoDrive",
        "Sector": "Technology",
        "Market Cap": "Mid Cap",
        "Stock Price": 128.63,
        "Annual Revenue (B)": 334.67,
        "Quarter": "Q2"
    },
    {
        "Company": "BioPharm",
        "Sector": "Technology",
        "Market Cap": "Mid Cap",
        "Stock Price": 228.29,
        "Annual Revenue (B)": 345.49,
        "Quarter": "Q2"
    },
    {
        "Company": "EcoEnergy",
        "Sector": "Biotech",
        "Market Cap": "Mega Cap",
        "Stock Price": 140.9,
        "Annual Revenue (B)": 101.3,
        "Quarter": "Q4"
    },
    {
        "Company": "Foodies",
        "Sector": "Finance",
        "Market Cap": "Mega Cap",
        "Stock Price": 992.32,
        "Annual Revenue (B)": 200.21,
        "Quarter": "Q1"
    },
    {
        "Company": "HealthPlus",
        "Sector": "Healthcare",
        "Market Cap": "Small Cap",
        "Stock Price": 140.9,
        "Annual Revenue (B)": 397.43,
        "Quarter": "Q3"
    },
    {
        "Company": "GlobalTrade",
        "Sector": "Technology",
        "Market Cap": "Mega Cap",
        "Stock Price": 234.97,
        "Annual Revenue (B)": 339.94,
        "Quarter": "Q3"
    },
    {
        "Company": "FinanceWorks",
        "Sector": "Healthcare",
        "Market Cap": "Mega Cap",
        "Stock Price": 475.1,
        "Annual Revenue (B)": 167.92,
        "Quarter": "Q4"
    },
    {
        "Company": "TechCorp",
        "Sector": "Finance",
        "Market Cap": "Mid Cap",
        "Stock Price": 346.85,
        "Annual Revenue (B)": 228.26,
        "Quarter": "Q4"
    }
]
<end>Please transform the following CSV data into MARKDOWN:
Trip Name,Start Location,End Location,Distance (miles),Duration (hours),Fuel Used (gallons)
Forest Journey,Houston,Los Angeles,2632.8,23.4,28.8
Forest Journey,Chicago,Denver,693.7,49.8,19.1
Desert Drive,New York,Denver,1874.6,57.8,43.8
<start>
| Trip Name | Start Location | End Location | Distance (miles) | Duration (hours) | Fuel Used (gallons) |
| --- | --- | --- | --- | --- | --- |
| Forest Journey | Houston | Los Angeles | 2632.8 | 23.4 | 28.8 |
| Forest Journey | Chicago | Denver | 693.7 | 49.8 | 19.1 |
| Desert Drive | New York | Denver | 1874.6 | 57.8 | 43.8 |
<end>Transform this markdown structure to a CSV format:
| Restaurant Name | Cuisine | Rating |
| --- | --- | --- |
| The Golden Spoon | American | 5 |
| Vegan Delight | French | 1 |
| Taco Town | Mediterranean | 1 |
| The Golden Spoon | Mediterranean | 5 |
| Curry Corner | Indian | 3 |<start>
Restaurant Name,Cuisine,Rating
The Golden Spoon,American,5
Vegan Delight,French,1
Taco Town,Mediterranean,1
The Golden Spoon,Mediterranean,5
Curry Corner,Indian,3
<end>Convert this plain text to Markdown:
Company: Foodies | Sector: Healthcare | Annual Revenue (B): 246.01 | Quarter: Q1
Company: AutoDrive | Sector: Automotive | Annual Revenue (B): 435.64 | Quarter: Q1
Company: BioPharm | Sector: Technology | Annual Revenue (B): 248.55 | Quarter: Q1
Company: EcoEnergy | Sector: Technology | Annual Revenue (B): 218.96 | Quarter: Q2
Company: Foodies | Sector: Finance | Annual Revenue (B): 248.55 | Quarter: Q4
Company: FinanceWorks | Sector: Retail | Annual Revenue (B): 463.32 | Quarter: Q4
<start>
| Company | Sector | Annual Revenue (B) | Quarter |
| --- | --- | --- | --- |
| Foodies | Healthcare | 246.01 | Q1 |
| AutoDrive | Automotive | 435.64 | Q1 |
| BioPharm | Technology | 248.55 | Q1 |
| EcoEnergy | Technology | 218.96 | Q2 |
| Foodies | Finance | 248.55 | Q4 |
| FinanceWorks | Retail | 463.32 | Q4 |
<end>Convert this markdown to plain text:
| Rating | Price Range |
| --- | --- |
| 4 | $$$$$ |
| 1 | $$ |
| 2 | $ |
| 2 | $$$ |
| 1 | $$$$ |
| 1 | $$$$$ |
| 5 | $$$ |<start>
Rating: 4 | Price Range: $$$$$
Rating: 1 | Price Range: $$
Rating: 2 | Price Range: $
Rating: 2 | Price Range: $$$
Rating: 1 | Price Range: $$$$
Rating: 1 | Price Range: $$$$$
Rating: 5 | Price Range: $$$
<end>Transform this MARKDOWN structure to a Yaml format:
| Company | Date | Open Price | Low Price | Volume |
| --- | --- | --- | --- | --- |
| BioLife | 2014-09-22 | 155.95 | 51.22 | 538080 |
| RetailWorld | 2012-12-03 | 137.25 | 17.15 | 4390233 |
| GreenEnergy | 2017-08-21 | 524.81 | 500.37 | 538080 |
| BioLife | 2016-08-10 | 811.98 | 671.61 | 6740067 |
| AeroSystems | 2013-10-16 | 1334.24 | 155.16 | 5704465 |<start>
- Company: BioLife
  Date: '2014-09-22'
  Low Price: 51.22
  Open Price: 155.95
  Volume: 538080
- Company: RetailWorld
  Date: '2012-12-03'
  Low Price: 17.15
  Open Price: 137.25
  Volume: 4390233
- Company: GreenEnergy
  Date: '2017-08-21'
  Low Price: 500.37
  Open Price: 524.81
  Volume: 538080
- Company: BioLife
  Date: '2016-08-10'
  Low Price: 671.61
  Open Price: 811.98
  Volume: 6740067
- Company: AeroSystems
  Date: '2013-10-16'
  Low Price: 155.16
  Open Price: 1334.24
  Volume: 5704465
<end>Please transform the following JSON data into Yml:
[
    {
        "Name": "Ximena",
        "Birth Month": "September",
        "City": "Los Angeles",
        "Income": 100000
    },
    {
        "Name": "Lizzie",
        "Birth Month": "February",
        "City": "San Francisco",
        "Income": 200000
    },
    {
        "Name": "Marion",
        "Birth Month": "May",
        "City": "Louisville",
        "Income": 65000
    },
    {
        "Name": "Kevin",
        "Birth Month": "October",
        "City": "San Francisco",
        "Income": 100000
    },
    {
        "Name": "Anton",
        "Birth Month": "January",
        "City": "Dallas",
        "Income": 270000
    },
    {
        "Name": "Dominique",
        "Birth Month": "June",
        "City": "Denver",
        "Income": 95000
    },
    {
        "Name": "Harrison",
        "Birth Month": "August",
        "City": "Nashville",
        "Income": 360000
    },
    {
        "Name": "Janet",
        "Birth Month": "December",
        "City": "Columbus",
        "Income": 260000
    }
]<start>
- Birth Month: September
  City: Los Angeles
  Income: 100000
  Name: Ximena
- Birth Month: February
  City: San Francisco
  Income: 200000
  Name: Lizzie
- Birth Month: May
  City: Louisville
  Income: 65000
  Name: Marion
- Birth Month: October
  City: San Francisco
  Income: 100000
  Name: Kevin
- Birth Month: January
  City: Dallas
  Income: 270000
  Name: Anton
- Birth Month: June
  City: Denver
  Income: 95000
  Name: Dominique
- Birth Month: August
  City: Nashville
  Income: 360000
  Name: Harrison
- Birth Month: December
  City: Columbus
  Income: 260000
  Name: Janet
<end>Convert this YAML to Markdown:
- Average Latency (ms): 80.52
  Cache Hit Ratio (%): 78.84
  Connection Count: 324
  Database Name: MetricsDB
  Queries per Second: 4893.32
  Timestamp: '2021-07-28 13:18:24'
- Average Latency (ms): 44.24
  Cache Hit Ratio (%): 71.97
  Connection Count: 45
  Database Name: UserDB
  Queries per Second: 1836.21
  Timestamp: '2022-11-22 06:24:28'
- Average Latency (ms): 80.52
  Cache Hit Ratio (%): 92.86
  Connection Count: 253
  Database Name: ProductsDB
  Queries per Second: 1517.96
  Timestamp: '2022-01-09 20:26:39'
- Average Latency (ms): 17.86
  Cache Hit Ratio (%): 98.13
  Connection Count: 223
  Database Name: InventoryDB
  Queries per Second: 526.71
  Timestamp: '2023-12-11 19:51:57'
- Average Latency (ms): 3.99
  Cache Hit Ratio (%): 96.86
  Connection Count: 305
  Database Name: OrdersDB
  Queries per Second: 2574.99
  Timestamp: '2022-04-27 04:19:35'
- Average Latency (ms): 59.53
  Cache Hit Ratio (%): 94.07
  Connection Count: 441
  Database Name: SessionsDB
  Queries per Second: 3162.6
  Timestamp: '2021-05-13 06:57:44'
<start>
| Database Name | Queries per Second | Cache Hit Ratio (%) | Connection Count | Average Latency (ms) | Timestamp |
| --- | --- | --- | --- | --- | --- |
| MetricsDB | 4893.32 | 78.84 | 324 | 80.52 | 2021-07-28 13:18:24 |
| UserDB | 1836.21 | 71.97 | 45 | 44.24 | 2022-11-22 06:24:28 |
| ProductsDB | 1517.96 | 92.86 | 253 | 80.52 | 2022-01-09 20:26:39 |
| InventoryDB | 526.71 | 98.13 | 223 | 17.86 | 2023-12-11 19:51:57 |
| OrdersDB | 2574.99 | 96.86 | 305 | 3.99 | 2022-04-27 04:19:35 |
| SessionsDB | 3162.6 | 94.07 | 441 | 59.53 | 2021-05-13 06:57:44 |
<end>Can you change this plain text into JSON?
Trip Name: Mountain Adventure | Start Location: Denver | End Location: New York | Distance (miles): 156.6 | Fuel Used (gallons): 44.6
Trip Name: Mountain Adventure | Start Location: Chicago | End Location: Houston | Distance (miles): 466.1 | Fuel Used (gallons): 50.8
Trip Name: Mountain Adventure | Start Location: San Francisco | End Location: Phoenix | Distance (miles): 2475.9 | Fuel Used (gallons): 37.6
Trip Name: Valley Voyage | Start Location: Miami | End Location: San Francisco | Distance (miles): 1840.2 | Fuel Used (gallons): 18.1
Trip Name: City Explorer | Start Location: Denver | End Location: Houston | Distance (miles): 687.8 | Fuel Used (gallons): 92.4
Trip Name: Highway Odyssey | Start Location: Denver | End Location: Miami | Distance (miles): 2159.1 | Fuel Used (gallons): 94.9
Trip Name: Historic Route | Start Location: Phoenix | End Location: San Francisco | Distance (miles): 1789.6 | Fuel Used (gallons): 67.1
Trip Name: Desert Drive | Start Location: Los Angeles | End Location: Denver | Distance (miles): 2063.9 | Fuel Used (gallons): 29.9
Trip Name: Coast to Coast | Start Location: Phoenix | End Location: Chicago | Distance (miles): 2394.9 | Fuel Used (gallons): 35.3
Trip Name: City Explorer | Start Location: Phoenix | End Location: San Francisco | Distance (miles): 1789.6 | Fuel Used (gallons): 62.1
<start>
[
    {
        "Trip Name": "Mountain Adventure",
        "Start Location": "Denver",
        "End Location": "New York",
        "Distance (miles)": 156.6,
        "Fuel Used (gallons)": 44.6
    },
    {
        "Trip Name": "Mountain Adventure",
        "Start Location": "Chicago",
        "End Location": "Houston",
        "Distance (miles)": 466.1,
        "Fuel Used (gallons)": 50.8
    },
    {
        "Trip Name": "Mountain Adventure",
        "Start Location": "San Francisco",
        "End Location": "Phoenix",
        "Distance (miles)": 2475.9,
        "Fuel Used (gallons)": 37.6
    },
    {
        "Trip Name": "Valley Voyage",
        "Start Location": "Miami",
        "End Location": "San Francisco",
        "Distance (miles)": 1840.2,
        "Fuel Used (gallons)": 18.1
    },
    {
        "Trip Name": "City Explorer",
        "Start Location": "Denver",
        "End Location": "Houston",
        "Distance (miles)": 687.8,
        "Fuel Used (gallons)": 92.4
    },
    {
        "Trip Name": "Highway Odyssey",
        "Start Location": "Denver",
        "End Location": "Miami",
        "Distance (miles)": 2159.1,
        "Fuel Used (gallons)": 94.9
    },
    {
        "Trip Name": "Historic Route",
        "Start Location": "Phoenix",
        "End Location": "San Francisco",
        "Distance (miles)": 1789.6,
        "Fuel Used (gallons)": 67.1
    },
    {
        "Trip Name": "Desert Drive",
        "Start Location": "Los Angeles",
        "End Location": "Denver",
        "Distance (miles)": 2063.9,
        "Fuel Used (gallons)": 29.9
    },
    {
        "Trip Name": "Coast to Coast",
        "Start Location": "Phoenix",
        "End Location": "Chicago",
        "Distance (miles)": 2394.9,
        "Fuel Used (gallons)": 35.3
    },
    {
        "Trip Name": "City Explorer",
        "Start Location": "Phoenix",
        "End Location": "San Francisco",
        "Distance (miles)": 1789.6,
        "Fuel Used (gallons)": 62.1
    }
]
<end>Can you change this PLAIN TEXT into Csv?
Company: BioPharm | Sector: Retail | Market Cap: Mega Cap | Stock Price: 113.53 | Annual Revenue (B): 252.22 | Quarter: Q1
Company: AutoDrive | Sector: Healthcare | Market Cap: Mid Cap | Stock Price: 501.88 | Annual Revenue (B): 323.03 | Quarter: Q2
Company: GlobalTrade | Sector: Energy | Market Cap: Large Cap | Stock Price: 733.78 | Annual Revenue (B): 475.93 | Quarter: Q2
Company: GlobalTrade | Sector: Finance | Market Cap: Small Cap | Stock Price: 113.53 | Annual Revenue (B): 77.0 | Quarter: Q1
Company: AeroSpace | Sector: Finance | Market Cap: Mega Cap | Stock Price: 11.32 | Annual Revenue (B): 328.56 | Quarter: Q3
<start>
Company,Sector,Market Cap,Stock Price,Annual Revenue (B),Quarter
BioPharm,Retail,Mega Cap,113.53,252.22,Q1
AutoDrive,Healthcare,Mid Cap,501.88,323.03,Q2
GlobalTrade,Energy,Large Cap,733.78,475.93,Q2
GlobalTrade,Finance,Small Cap,113.53,77.0,Q1
AeroSpace,Finance,Mega Cap,11.32,328.56,Q3
<end>Transform this markdown structure to a csv format:
| Name | Age | Birth Month | City | Income |
| --- | --- | --- | --- | --- |
| Veronica | 69 | May | Portland | 320000 |
| Mila | 41 | July | Jacksonville | 140000 |
| Annette | 38 | May | Houston | 130000 |
| Jade | 32 | October | San Antonio | 30000 |<start>
Name,Age,Birth Month,City,Income
Veronica,69,May,Portland,320000
Mila,41,July,Jacksonville,140000
Annette,38,May,Houston,130000
Jade,32,October,San Antonio,30000
<end>Transform this markdown structure to a CSV format:
| Title | Director | Genre | Box Office Earnings (M) |
| --- | --- | --- | --- |
| Mystery of the Depths | Aria Ravenwood | Thriller | 739.02 |
| Dreamwalker | Talon Blackthorn | Comedy | 752.84 |
| Mystery of the Depths | Aria Ravenwood | Thriller | 635.06 |
| Dreamwalker | Selene Darkwhisper | Fantasy | 869.93 |
| Mystery of the Depths | Cade Firebrand | Comedy | 672.79 |
| The Final Voyage | Aria Ravenwood | Action | 965.67 |
| Starbound Odyssey | Cade Firebrand | Sci-Fi | 924.42 |
| Mystery of the Depths | Drake Nightshade | Sci-Fi | 533.21 |
| The Endless Horizon | Aria Ravenwood | Action | 65.98 |
| Beyond the Veil | Talon Blackthorn | Fantasy | 139.16 |<start>
Title,Director,Genre,Box Office Earnings (M)
Mystery of the Depths,Aria Ravenwood,Thriller,739.02
Dreamwalker,Talon Blackthorn,Comedy,752.84
Mystery of the Depths,Aria Ravenwood,Thriller,635.06
Dreamwalker,Selene Darkwhisper,Fantasy,869.93
Mystery of the Depths,Cade Firebrand,Comedy,672.79
The Final Voyage,Aria Ravenwood,Action,965.67
Starbound Odyssey,Cade Firebrand,Sci-Fi,924.42
Mystery of the Depths,Drake Nightshade,Sci-Fi,533.21
The Endless Horizon,Aria Ravenwood,Action,65.98
Beyond the Veil,Talon Blackthorn,Fantasy,139.16
<end>Can you change this CSV into plain text?
Restaurant Name,Location
Vegan Delight,Houston
Pizza Planet,Los Angeles
Taco Town,Houston
Vegan Delight,Houston
Pizza Planet,Phoenix
The Steakhouse,Los Angeles
<start>
Restaurant Name: Vegan Delight | Location: Houston
Restaurant Name: Pizza Planet | Location: Los Angeles
Restaurant Name: Taco Town | Location: Houston
Restaurant Name: Vegan Delight | Location: Houston
Restaurant Name: Pizza Planet | Location: Phoenix
Restaurant Name: The Steakhouse | Location: Los Angeles
<end>Here's some Json data, can you convert it to plain text?
[
    {
        "Open Price": 193.35,
        "Close Price": 1479.0,
        "High Price": 1479.0,
        "Low Price": 193.35,
        "Volume": 469996
    },
    {
        "Open Price": 309.66,
        "Close Price": 579.86,
        "High Price": 579.86,
        "Low Price": 245.32,
        "Volume": 3109368
    },
    {
        "Open Price": 46.99,
        "Close Price": 738.45,
        "High Price": 738.45,
        "Low Price": 46.99,
        "Volume": 5314020
    }
]<start>
Open Price: 193.35 | Close Price: 1479.0 | High Price: 1479.0 | Low Price: 193.35 | Volume: 469996
Open Price: 309.66 | Close Price: 579.86 | High Price: 579.86 | Low Price: 245.32 | Volume: 3109368
Open Price: 46.99 | Close Price: 738.45 | High Price: 738.45 | Low Price: 46.99 | Volume: 5314020
<end>Here's some csv data, can you convert it to yml?
Company,Sector,Stock Price,Annual Revenue (B),Quarter
HealthPlus,Technology,539.6,377.9,Q3
BioPharm,Automotive,646.34,217.67,Q1
RetailHub,Automotive,910.99,205.67,Q3
HealthPlus,Automotive,759.18,196.92,Q4
FinanceWorks,Aerospace,816.64,438.55,Q1
RetailHub,Biotech,128.34,216.97,Q2
<start>
- Annual Revenue (B): 377.9
  Company: HealthPlus
  Quarter: Q3
  Sector: Technology
  Stock Price: 539.6
- Annual Revenue (B): 217.67
  Company: BioPharm
  Quarter: Q1
  Sector: Automotive
  Stock Price: 646.34
- Annual Revenue (B): 205.67
  Company: RetailHub
  Quarter: Q3
  Sector: Automotive
  Stock Price: 910.99
- Annual Revenue (B): 196.92
  Company: HealthPlus
  Quarter: Q4
  Sector: Automotive
  Stock Price: 759.18
- Annual Revenue (B): 438.55
  Company: FinanceWorks
  Quarter: Q1
  Sector: Aerospace
  Stock Price: 816.64
- Annual Revenue (B): 216.97
  Company: RetailHub
  Quarter: Q2
  Sector: Biotech
  Stock Price: 128.34
<end>Transform this CSV structure to a markdown format:
Name,Age,Birth Month,City,Income
Reuben,20,November,Denver,245000
Mariah,53,February,San Jose,350000
Naomi,48,February,Dallas,30000
Crystal,25,August,Nashville,430000
Charlie,54,December,Denver,85000
Lance,52,December,Seattle,30000
Tasha,44,September,Nashville,490000
Joanna,36,June,Chicago,275000
<start>
| Name | Age | Birth Month | City | Income |
| --- | --- | --- | --- | --- |
| Reuben | 20 | November | Denver | 245000 |
| Mariah | 53 | February | San Jose | 350000 |
| Naomi | 48 | February | Dallas | 30000 |
| Crystal | 25 | August | Nashville | 430000 |
| Charlie | 54 | December | Denver | 85000 |
| Lance | 52 | December | Seattle | 30000 |
| Tasha | 44 | September | Nashville | 490000 |
| Joanna | 36 | June | Chicago | 275000 |
<end>Here's some Markdown data, can you convert it to Plain text?
| Title | Author | Genre | Publication Year |
| --- | --- | --- | --- |
| The Forgotten World | Thorne Ironwood | Historical | 1977 |
| The Crystal Key | Galen Starfire | Science Fiction | 1983 |
| The Forgotten World | Sylvia Nightshade | Fantasy | 1987 |
| The Forgotten World | Luna Silverleaf | Romance | 1980 |
| The Silent Grove | Elara Moonshadow | Historical | 2009 |
| Echoes of Eternity | Thorne Ironwood | Historical | 1975 |<start>
Title: The Forgotten World | Author: Thorne Ironwood | Genre: Historical | Publication Year: 1977
Title: The Crystal Key | Author: Galen Starfire | Genre: Science Fiction | Publication Year: 1983
Title: The Forgotten World | Author: Sylvia Nightshade | Genre: Fantasy | Publication Year: 1987
Title: The Forgotten World | Author: Luna Silverleaf | Genre: Romance | Publication Year: 1980
Title: The Silent Grove | Author: Elara Moonshadow | Genre: Historical | Publication Year: 2009
Title: Echoes of Eternity | Author: Thorne Ironwood | Genre: Historical | Publication Year: 1975
<end>Here's some JSON data, can you convert it to markdown?
[
    {
        "Sector": "Energy",
        "Market Cap": "Large Cap",
        "Stock Price": 618.55,
        "Annual Revenue (B)": 220.46,
        "Quarter": "Q2"
    },
    {
        "Sector": "Aerospace",
        "Market Cap": "Small Cap",
        "Stock Price": 921.16,
        "Annual Revenue (B)": 324.23,
        "Quarter": "Q3"
    },
    {
        "Sector": "Biotech",
        "Market Cap": "Mega Cap",
        "Stock Price": 567.92,
        "Annual Revenue (B)": 275.57,
        "Quarter": "Q3"
    },
    {
        "Sector": "Automotive",
        "Market Cap": "Mid Cap",
        "Stock Price": 427.77,
        "Annual Revenue (B)": 432.55,
        "Quarter": "Q2"
    },
    {
        "Sector": "Technology",
        "Market Cap": "Small Cap",
        "Stock Price": 373.13,
        "Annual Revenue (B)": 291.35,
        "Quarter": "Q2"
    },
    {
        "Sector": "Retail",
        "Market Cap": "Mid Cap",
        "Stock Price": 413.84,
        "Annual Revenue (B)": 250.05,
        "Quarter": "Q2"
    },
    {
        "Sector": "Biotech",
        "Market Cap": "Small Cap",
        "Stock Price": 138.52,
        "Annual Revenue (B)": 425.83,
        "Quarter": "Q3"
    }
]<start>
| Sector | Market Cap | Stock Price | Annual Revenue (B) | Quarter |
| --- | --- | --- | --- | --- |
| Energy | Large Cap | 618.55 | 220.46 | Q2 |
| Aerospace | Small Cap | 921.16 | 324.23 | Q3 |
| Biotech | Mega Cap | 567.92 | 275.57 | Q3 |
| Automotive | Mid Cap | 427.77 | 432.55 | Q2 |
| Technology | Small Cap | 373.13 | 291.35 | Q2 |
| Retail | Mid Cap | 413.84 | 250.05 | Q2 |
| Biotech | Small Cap | 138.52 | 425.83 | Q3 |
<end>Convert this markdown to yaml:
| Company | Market Cap | Stock Price | Quarter |
| --- | --- | --- | --- |
| Foodies | Small Cap | 35.25 | Q4 |
| HealthPlus | Large Cap | 398.72 | Q3 |
| AeroSpace | Small Cap | 884.49 | Q3 |
| FinanceWorks | Small Cap | 816.89 | Q3 |
| GlobalTrade | Mega Cap | 775.96 | Q4 |
| TechCorp | Mid Cap | 722.93 | Q4 |
| AutoDrive | Mega Cap | 881.85 | Q1 |
| AeroSpace | Large Cap | 722.93 | Q3 |
| RetailHub | Mid Cap | 85.41 | Q4 |
| TechCorp | Small Cap | 416.8 | Q2 |<start>
- Company: Foodies
  Market Cap: Small Cap
  Quarter: Q4
  Stock Price: 35.25
- Company: HealthPlus
  Market Cap: Large Cap
  Quarter: Q3
  Stock Price: 398.72
- Company: AeroSpace
  Market Cap: Small Cap
  Quarter: Q3
  Stock Price: 884.49
- Company: FinanceWorks
  Market Cap: Small Cap
  Quarter: Q3
  Stock Price: 816.89
- Company: GlobalTrade
  Market Cap: Mega Cap
  Quarter: Q4
  Stock Price: 775.96
- Company: TechCorp
  Market Cap: Mid Cap
  Quarter: Q4
  Stock Price: 722.93
- Company: AutoDrive
  Market Cap: Mega Cap
  Quarter: Q1
  Stock Price: 881.85
- Company: AeroSpace
  Market Cap: Large Cap
  Quarter: Q3
  Stock Price: 722.93
- Company: RetailHub
  Market Cap: Mid Cap
  Quarter: Q4
  Stock Price: 85.41
- Company: TechCorp
  Market Cap: Small Cap
  Quarter: Q2
  Stock Price: 416.8
<end>Transform this JSON structure to a CSV format:
[
    {
        "Product Name": "Apparatus",
        "Price": 486.67,
        "Category": "Household",
        "Supplier Name": "ACME Corp"
    },
    {
        "Product Name": "Doohickey",
        "Price": 255.02,
        "Category": "Sports",
        "Supplier Name": "Wayne Enterprises"
    },
    {
        "Product Name": "Contraption",
        "Price": 377.84,
        "Category": "Electronics",
        "Supplier Name": "Umbrella Corp"
    },
    {
        "Product Name": "Apparatus",
        "Price": 115.53,
        "Category": "Toys",
        "Supplier Name": "Wonka Industries"
    },
    {
        "Product Name": "Gizmo",
        "Price": 42.21,
        "Category": "Automotive",
        "Supplier Name": "Wayne Enterprises"
    },
    {
        "Product Name": "Widget",
        "Price": 245.8,
        "Category": "Household",
        "Supplier Name": "Wonka Industries"
    },
    {
        "Product Name": "Device",
        "Price": 222.6,
        "Category": "Toys",
        "Supplier Name": "ACME Corp"
    }
]<start>
Product Name,Price,Category,Supplier Name
Apparatus,486.67,Household,ACME Corp
Doohickey,255.02,Sports,Wayne Enterprises
Contraption,377.84,Electronics,Umbrella Corp
Apparatus,115.53,Toys,Wonka Industries
Gizmo,42.21,Automotive,Wayne Enterprises
Widget,245.8,Household,Wonka Industries
Device,222.6,Toys,ACME Corp
<end>Transform this markdown structure to a Json format:
| Title | Author | Genre |
| --- | --- | --- |
| Legends of the Rift | Kara Firebrand | Non-Fiction |
| Shadows of Solitude | Isla Windrider | Mystery |
| Tales of the Brave | Thorne Ironwood | Horror |
| A Journey Through Time | Orion Frostblade | Non-Fiction |
| The Crystal Key | Elara Moonshadow | Science Fiction |
| Echoes of Eternity | Orion Frostblade | Fantasy |
| Tales of the Brave | Draven Blackthorn | Mystery |
| Tales of the Brave | Orion Frostblade | Fantasy |
| Whispers of the Abyss | Orion Frostblade | Science Fiction |<start>
[
    {
        "Title": "Legends of the Rift",
        "Author": "Kara Firebrand",
        "Genre": "Non-Fiction"
    },
    {
        "Title": "Shadows of Solitude",
        "Author": "Isla Windrider",
        "Genre": "Mystery"
    },
    {
        "Title": "Tales of the Brave",
        "Author": "Thorne Ironwood",
        "Genre": "Horror"
    },
    {
        "Title": "A Journey Through Time",
        "Author": "Orion Frostblade",
        "Genre": "Non-Fiction"
    },
    {
        "Title": "The Crystal Key",
        "Author": "Elara Moonshadow",
        "Genre": "Science Fiction"
    },
    {
        "Title": "Echoes of Eternity",
        "Author": "Orion Frostblade",
        "Genre": "Fantasy"
    },
    {
        "Title": "Tales of the Brave",
        "Author": "Draven Blackthorn",
        "Genre": "Mystery"
    },
    {
        "Title": "Tales of the Brave",
        "Author": "Orion Frostblade",
        "Genre": "Fantasy"
    },
    {
        "Title": "Whispers of the Abyss",
        "Author": "Orion Frostblade",
        "Genre": "Science Fiction"
    }
]
<end>Convert this MARKDOWN to plain text:
| Company | Sector | Market Cap | Stock Price | Annual Revenue (B) | Quarter |
| --- | --- | --- | --- | --- | --- |
| AeroSpace | Automotive | Mid Cap | 132.06 | 408.04 | Q1 |
| EcoEnergy | Automotive | Large Cap | 704.08 | 325.08 | Q4 |
| AeroSpace | Automotive | Mid Cap | 842.76 | 422.15 | Q1 |
| AeroSpace | Finance | Small Cap | 553.66 | 394.99 | Q3 |
| GlobalTrade | Finance | Mega Cap | 722.27 | 394.99 | Q2 |
| BioPharm | Energy | Small Cap | 846.55 | 156.13 | Q1 |
| Foodies | Technology | Mega Cap | 132.06 | 168.66 | Q3 |
| Foodies | Healthcare | Large Cap | 607.51 | 425.72 | Q1 |
| EcoEnergy | Healthcare | Mega Cap | 704.08 | 334.86 | Q3 |
| AeroSpace | Finance | Large Cap | 556.65 | 129.77 | Q4 |<start>
Company: AeroSpace | Sector: Automotive | Market Cap: Mid Cap | Stock Price: 132.06 | Annual Revenue (B): 408.04 | Quarter: Q1
Company: EcoEnergy | Sector: Automotive | Market Cap: Large Cap | Stock Price: 704.08 | Annual Revenue (B): 325.08 | Quarter: Q4
Company: AeroSpace | Sector: Automotive | Market Cap: Mid Cap | Stock Price: 842.76 | Annual Revenue (B): 422.15 | Quarter: Q1
Company: AeroSpace | Sector: Finance | Market Cap: Small Cap | Stock Price: 553.66 | Annual Revenue (B): 394.99 | Quarter: Q3
Company: GlobalTrade | Sector: Finance | Market Cap: Mega Cap | Stock Price: 722.27 | Annual Revenue (B): 394.99 | Quarter: Q2
Company: BioPharm | Sector: Energy | Market Cap: Small Cap | Stock Price: 846.55 | Annual Revenue (B): 156.13 | Quarter: Q1
Company: Foodies | Sector: Technology | Market Cap: Mega Cap | Stock Price: 132.06 | Annual Revenue (B): 168.66 | Quarter: Q3
Company: Foodies | Sector: Healthcare | Market Cap: Large Cap | Stock Price: 607.51 | Annual Revenue (B): 425.72 | Quarter: Q1
Company: EcoEnergy | Sector: Healthcare | Market Cap: Mega Cap | Stock Price: 704.08 | Annual Revenue (B): 334.86 | Quarter: Q3
Company: AeroSpace | Sector: Finance | Market Cap: Large Cap | Stock Price: 556.65 | Annual Revenue (B): 129.77 | Quarter: Q4
<end>Please transform the following Markdown data into CSV:
| Device ID | Location | Battery Level (%) | Reading Value | Timestamp |
| --- | --- | --- | --- | --- |
| device-0017 | Garden | 91.3 | -10.03 | 2022-03-05 19:55:52 |
| device-0030 | Garden | 73.1 | 65.49 | 2022-02-09 12:35:14 |
| device-0083 | Bedroom | 42.1 | 26.75 | 2023-10-07 19:49:56 |
| device-0080 | Office | 73.1 | 79.44 | 2022-12-16 04:56:10 |
| device-0095 | Living Room | 99.5 | -10.03 | 2021-08-10 09:26:54 |
| device-0064 | Living Room | 41.8 | 22.83 | 2023-01-17 12:25:48 |
| device-0038 | Office | 39.1 | 43.33 | 2022-08-17 10:11:08 |
| device-0030 | Bedroom | 67.2 | 51.52 | 2021-05-28 05:40:46 |
| device-0002 | Hallway | 35.5 | -13.69 | 2021-06-20 22:11:29 |<start>
Device ID,Location,Battery Level (%),Reading Value,Timestamp
device-0017,Garden,91.3,-10.03,2022-03-05 19:55:52
device-0030,Garden,73.1,65.49,2022-02-09 12:35:14
device-0083,Bedroom,42.1,26.75,2023-10-07 19:49:56
device-0080,Office,73.1,79.44,2022-12-16 04:56:10
device-0095,Living Room,99.5,-10.03,2021-08-10 09:26:54
device-0064,Living Room,41.8,22.83,2023-01-17 12:25:48
device-0038,Office,39.1,43.33,2022-08-17 10:11:08
device-0030,Bedroom,67.2,51.52,2021-05-28 05:40:46
device-0002,Hallway,35.5,-13.69,2021-06-20 22:11:29
<end>Here's some JSON data, can you convert it to plain text?
[
    {
        "Name": "Isla",
        "City": "Charlotte",
        "Income": 340000
    },
    {
        "Name": "Gordon",
        "City": "Indianapolis",
        "Income": 495000
    },
    {
        "Name": "George",
        "City": "Milwaukee",
        "Income": 410000
    },
    {
        "Name": "Kayden",
        "City": "Oklahoma City",
        "Income": 400000
    },
    {
        "Name": "Harvey",
        "City": "Boston",
        "Income": 290000
    },
    {
        "Name": "Riley",
        "City": "Las Vegas",
        "Income": 120000
    },
    {
        "Name": "Carter",
        "City": "San Francisco",
        "Income": 275000
    },
    {
        "Name": "Geoffrey",
        "City": "Milwaukee",
        "Income": 230000
    }
]<start>
Name: Isla | City: Charlotte | Income: 340000
Name: Gordon | City: Indianapolis | Income: 495000
Name: George | City: Milwaukee | Income: 410000
Name: Kayden | City: Oklahoma City | Income: 400000
Name: Harvey | City: Boston | Income: 290000
Name: Riley | City: Las Vegas | Income: 120000
Name: Carter | City: San Francisco | Income: 275000
Name: Geoffrey | City: Milwaukee | Income: 230000
<end>