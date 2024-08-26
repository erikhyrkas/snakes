Convert this Json to plain text:
[
    {
        "Sector": "Automotive",
        "Market Cap": "Large Cap",
        "Stock Price": 56.51,
        "Annual Revenue (B)": 271.58,
        "Quarter": "Q3"
    },
    {
        "Sector": "Aerospace",
        "Market Cap": "Mid Cap",
        "Stock Price": 313.13,
        "Annual Revenue (B)": 222.69,
        "Quarter": "Q2"
    },
    {
        "Sector": "Biotech",
        "Market Cap": "Mid Cap",
        "Stock Price": 686.31,
        "Annual Revenue (B)": 474.51,
        "Quarter": "Q3"
    },
    {
        "Sector": "Retail",
        "Market Cap": "Mid Cap",
        "Stock Price": 486.14,
        "Annual Revenue (B)": 297.68,
        "Quarter": "Q1"
    },
    {
        "Sector": "Biotech",
        "Market Cap": "Mega Cap",
        "Stock Price": 984.13,
        "Annual Revenue (B)": 335.03,
        "Quarter": "Q3"
    },
    {
        "Sector": "Healthcare",
        "Market Cap": "Mid Cap",
        "Stock Price": 12.41,
        "Annual Revenue (B)": 183.79,
        "Quarter": "Q3"
    },
    {
        "Sector": "Healthcare",
        "Market Cap": "Small Cap",
        "Stock Price": 208.17,
        "Annual Revenue (B)": 172.4,
        "Quarter": "Q3"
    },
    {
        "Sector": "Aerospace",
        "Market Cap": "Large Cap",
        "Stock Price": 989.28,
        "Annual Revenue (B)": 356.39,
        "Quarter": "Q2"
    }
]<start>
Sector: Automotive | Market Cap: Large Cap | Stock Price: 56.51 | Annual Revenue (B): 271.58 | Quarter: Q3
Sector: Aerospace | Market Cap: Mid Cap | Stock Price: 313.13 | Annual Revenue (B): 222.69 | Quarter: Q2
Sector: Biotech | Market Cap: Mid Cap | Stock Price: 686.31 | Annual Revenue (B): 474.51 | Quarter: Q3
Sector: Retail | Market Cap: Mid Cap | Stock Price: 486.14 | Annual Revenue (B): 297.68 | Quarter: Q1
Sector: Biotech | Market Cap: Mega Cap | Stock Price: 984.13 | Annual Revenue (B): 335.03 | Quarter: Q3
Sector: Healthcare | Market Cap: Mid Cap | Stock Price: 12.41 | Annual Revenue (B): 183.79 | Quarter: Q3
Sector: Healthcare | Market Cap: Small Cap | Stock Price: 208.17 | Annual Revenue (B): 172.4 | Quarter: Q3
Sector: Aerospace | Market Cap: Large Cap | Stock Price: 989.28 | Annual Revenue (B): 356.39 | Quarter: Q2
<end>Can you change this yml into markdown?
- Price: 325.97
  Product Name: Thingamajig
  Stock Quantity: 163
- Price: 337.04
  Product Name: Whatchamacallit
  Stock Quantity: 471
- Price: 100.46
  Product Name: Device
  Stock Quantity: 133
- Price: 481.43
  Product Name: Gadget
  Stock Quantity: 217
- Price: 191.62
  Product Name: Widget
  Stock Quantity: 86
- Price: 218.79
  Product Name: Instrument
  Stock Quantity: 190
- Price: 56.84
  Product Name: Apparatus
  Stock Quantity: 364
- Price: 282.37
  Product Name: Contraption
  Stock Quantity: 460
<start>
| Product Name | Price | Stock Quantity |
| --- | --- | --- |
| Thingamajig | 325.97 | 163 |
| Whatchamacallit | 337.04 | 471 |
| Device | 100.46 | 133 |
| Gadget | 481.43 | 217 |
| Widget | 191.62 | 86 |
| Instrument | 218.79 | 190 |
| Apparatus | 56.84 | 364 |
| Contraption | 282.37 | 460 |
<end>Transform this Json structure to a PLAIN TEXT format:
[
    {
        "Company": "RetailWorld",
        "Date": "2012-02-04",
        "Open Price": 848.68,
        "Close Price": 983.1,
        "High Price": 983.1,
        "Low Price": 402.07,
        "Volume": 7455176
    },
    {
        "Company": "MediaGroup",
        "Date": "2013-01-16",
        "Open Price": 1285.8,
        "Close Price": 1268.63,
        "High Price": 1285.8,
        "Low Price": 37.83,
        "Volume": 1861604
    },
    {
        "Company": "GreenEnergy",
        "Date": "2015-05-16",
        "Open Price": 848.68,
        "Close Price": 510.96,
        "High Price": 848.68,
        "Low Price": 24.0,
        "Volume": 9558547
    }
]<start>
Company: RetailWorld | Date: 2012-02-04 | Open Price: 848.68 | Close Price: 983.1 | High Price: 983.1 | Low Price: 402.07 | Volume: 7455176
Company: MediaGroup | Date: 2013-01-16 | Open Price: 1285.8 | Close Price: 1268.63 | High Price: 1285.8 | Low Price: 37.83 | Volume: 1861604
Company: GreenEnergy | Date: 2015-05-16 | Open Price: 848.68 | Close Price: 510.96 | High Price: 848.68 | Low Price: 24.0 | Volume: 9558547
<end>Please transform the following csv data into json:
Location,Condition,Temperature (C),Humidity (%),Wind Speed (km/h),Day
Chicago,Foggy,14.1,77,6.1,Monday
Seattle,Sunny,7.9,41,24.3,Saturday
Chicago,Stormy,7.3,39,29.0,Wednesday
New York,Windy,35.2,39,9.9,Monday
Los Angeles,Snowy,-6.6,38,22.1,Tuesday
Miami,Rainy,10.0,72,9.9,Monday
<start>
[
    {
        "Location": "Chicago",
        "Condition": "Foggy",
        "Temperature (C)": 14.1,
        "Humidity (%)": 77,
        "Wind Speed (km/h)": 6.1,
        "Day": "Monday"
    },
    {
        "Location": "Seattle",
        "Condition": "Sunny",
        "Temperature (C)": 7.9,
        "Humidity (%)": 41,
        "Wind Speed (km/h)": 24.3,
        "Day": "Saturday"
    },
    {
        "Location": "Chicago",
        "Condition": "Stormy",
        "Temperature (C)": 7.3,
        "Humidity (%)": 39,
        "Wind Speed (km/h)": 29.0,
        "Day": "Wednesday"
    },
    {
        "Location": "New York",
        "Condition": "Windy",
        "Temperature (C)": 35.2,
        "Humidity (%)": 39,
        "Wind Speed (km/h)": 9.9,
        "Day": "Monday"
    },
    {
        "Location": "Los Angeles",
        "Condition": "Snowy",
        "Temperature (C)": -6.6,
        "Humidity (%)": 38,
        "Wind Speed (km/h)": 22.1,
        "Day": "Tuesday"
    },
    {
        "Location": "Miami",
        "Condition": "Rainy",
        "Temperature (C)": 10.0,
        "Humidity (%)": 72,
        "Wind Speed (km/h)": 9.9,
        "Day": "Monday"
    }
]
<end>Can you change this Csv into json?
Company,Sector,Market Cap,Stock Price,Annual Revenue (B),Quarter
EcoEnergy,Healthcare,Mid Cap,893.32,425.7,Q4
Foodies,Retail,Mega Cap,451.6,276.2,Q2
HealthPlus,Biotech,Small Cap,791.53,453.13,Q2
EcoEnergy,Automotive,Small Cap,26.37,63.15,Q1
TechCorp,Technology,Large Cap,671.9,68.51,Q3
FinanceWorks,Finance,Large Cap,626.11,403.0,Q1
AeroSpace,Biotech,Mega Cap,304.44,460.45,Q4
<start>
[
    {
        "Company": "EcoEnergy",
        "Sector": "Healthcare",
        "Market Cap": "Mid Cap",
        "Stock Price": 893.32,
        "Annual Revenue (B)": 425.7,
        "Quarter": "Q4"
    },
    {
        "Company": "Foodies",
        "Sector": "Retail",
        "Market Cap": "Mega Cap",
        "Stock Price": 451.6,
        "Annual Revenue (B)": 276.2,
        "Quarter": "Q2"
    },
    {
        "Company": "HealthPlus",
        "Sector": "Biotech",
        "Market Cap": "Small Cap",
        "Stock Price": 791.53,
        "Annual Revenue (B)": 453.13,
        "Quarter": "Q2"
    },
    {
        "Company": "EcoEnergy",
        "Sector": "Automotive",
        "Market Cap": "Small Cap",
        "Stock Price": 26.37,
        "Annual Revenue (B)": 63.15,
        "Quarter": "Q1"
    },
    {
        "Company": "TechCorp",
        "Sector": "Technology",
        "Market Cap": "Large Cap",
        "Stock Price": 671.9,
        "Annual Revenue (B)": 68.51,
        "Quarter": "Q3"
    },
    {
        "Company": "FinanceWorks",
        "Sector": "Finance",
        "Market Cap": "Large Cap",
        "Stock Price": 626.11,
        "Annual Revenue (B)": 403.0,
        "Quarter": "Q1"
    },
    {
        "Company": "AeroSpace",
        "Sector": "Biotech",
        "Market Cap": "Mega Cap",
        "Stock Price": 304.44,
        "Annual Revenue (B)": 460.45,
        "Quarter": "Q4"
    }
]
<end>Can you change this plain text into json?
Title: A Journey Through Time | Author: Thorne Ironwood | Rating: 2.8
Title: Whispers of the Abyss | Author: Galen Starfire | Rating: 1.4
Title: The Crystal Key | Author: Draven Blackthorn | Rating: 4.6
Title: The Last Sky | Author: Rowan Ashborne | Rating: 2.5
<start>
[
    {
        "Title": "A Journey Through Time",
        "Author": "Thorne Ironwood",
        "Rating": 2.8
    },
    {
        "Title": "Whispers of the Abyss",
        "Author": "Galen Starfire",
        "Rating": 1.4
    },
    {
        "Title": "The Crystal Key",
        "Author": "Draven Blackthorn",
        "Rating": 4.6
    },
    {
        "Title": "The Last Sky",
        "Author": "Rowan Ashborne",
        "Rating": 2.5
    }
]
<end>Can you change this json into yml?
[
    {
        "Restaurant Name": "Pasta Palace",
        "Cuisine": "French",
        "Price Range": "$$$"
    },
    {
        "Restaurant Name": "The Steakhouse",
        "Cuisine": "Mexican",
        "Price Range": "$"
    },
    {
        "Restaurant Name": "The Steakhouse",
        "Cuisine": "Mediterranean",
        "Price Range": "$$$$"
    }
]<start>
- Cuisine: French
  Price Range: $$$
  Restaurant Name: Pasta Palace
- Cuisine: Mexican
  Price Range: $
  Restaurant Name: The Steakhouse
- Cuisine: Mediterranean
  Price Range: $$$$
  Restaurant Name: The Steakhouse
<end>Can you change this MARKDOWN into plain text?
| Title | Author | Publication Year |
| --- | --- | --- |
| Echoes of Eternity | Elara Moonshadow | 2001 |
| The Last Sky | Rowan Ashborne | 1980 |
| A Journey Through Time | Thorne Ironwood | 1977 |
| The Silent Grove | Thorne Ironwood | 1999 |
| The Last Sky | Elara Moonshadow | 1961 |<start>
Title: Echoes of Eternity | Author: Elara Moonshadow | Publication Year: 2001
Title: The Last Sky | Author: Rowan Ashborne | Publication Year: 1980
Title: A Journey Through Time | Author: Thorne Ironwood | Publication Year: 1977
Title: The Silent Grove | Author: Thorne Ironwood | Publication Year: 1999
Title: The Last Sky | Author: Elara Moonshadow | Publication Year: 1961
<end>Convert this Yaml to Csv:
- Age: 23
  Birth Month: January
  City: New York
  Income: 360000
- Age: 47
  Birth Month: November
  City: Nashville
  Income: 410000
- Age: 47
  Birth Month: August
  City: Jacksonville
  Income: 470000
- Age: 29
  Birth Month: July
  City: El Paso
  Income: 475000
- Age: 23
  Birth Month: June
  City: Milwaukee
  Income: 170000
- Age: 51
  Birth Month: October
  City: Dallas
  Income: 370000
- Age: 36
  Birth Month: February
  City: Milwaukee
  Income: 495000
- Age: 44
  Birth Month: May
  City: Baltimore
  Income: 345000
<start>
Age,Birth Month,City,Income
23,January,New York,360000
47,November,Nashville,410000
47,August,Jacksonville,470000
29,July,El Paso,475000
23,June,Milwaukee,170000
51,October,Dallas,370000
36,February,Milwaukee,495000
44,May,Baltimore,345000
<end>Transform this plain text structure to a yaml format:
Distance (miles): 2071.4 | Duration (hours): 38.9 | Fuel Used (gallons): 55.2
Distance (miles): 1772.3 | Duration (hours): 6.5 | Fuel Used (gallons): 77.2
Distance (miles): 2095.0 | Duration (hours): 6.1 | Fuel Used (gallons): 67.2
Distance (miles): 1107.3 | Duration (hours): 59.5 | Fuel Used (gallons): 15.5
Distance (miles): 2048.6 | Duration (hours): 67.5 | Fuel Used (gallons): 8.0
Distance (miles): 219.8 | Duration (hours): 59.9 | Fuel Used (gallons): 62.9
<start>
- Distance (miles): 2071.4
  Duration (hours): 38.9
  Fuel Used (gallons): 55.2
- Distance (miles): 1772.3
  Duration (hours): 6.5
  Fuel Used (gallons): 77.2
- Distance (miles): 2095.0
  Duration (hours): 6.1
  Fuel Used (gallons): 67.2
- Distance (miles): 1107.3
  Duration (hours): 59.5
  Fuel Used (gallons): 15.5
- Distance (miles): 2048.6
  Duration (hours): 67.5
  Fuel Used (gallons): 8.0
- Distance (miles): 219.8
  Duration (hours): 59.9
  Fuel Used (gallons): 62.9
<end>Can you change this markdown into CSV?
| Cuisine | Location | Price Range |
| --- | --- | --- |
| Japanese | Miami | $$$ |
| Mediterranean | Phoenix | $ |
| French | Miami | $$$$ |<start>
Cuisine,Location,Price Range
Japanese,Miami,$$$
Mediterranean,Phoenix,$
French,Miami,$$$$
<end>Transform this YAML structure to a markdown format:
- Cuisine: Japanese
  Location: Miami
  Price Range: $
  Rating: 5
  Restaurant Name: Vegan Delight
- Cuisine: American
  Location: Chicago
  Price Range: $$
  Rating: 3
  Restaurant Name: BBQ Barn
- Cuisine: Mexican
  Location: Miami
  Price Range: $$$
  Rating: 4
  Restaurant Name: Pasta Palace
- Cuisine: Italian
  Location: San Francisco
  Price Range: $$$$$
  Rating: 3
  Restaurant Name: Burger Haven
- Cuisine: French
  Location: New York
  Price Range: $$$
  Rating: 3
  Restaurant Name: Pizza Planet
- Cuisine: Mediterranean
  Location: New York
  Price Range: $$
  Rating: 4
  Restaurant Name: Vegan Delight
<start>
| Restaurant Name | Cuisine | Location | Rating | Price Range |
| --- | --- | --- | --- | --- |
| Vegan Delight | Japanese | Miami | 5 | $ |
| BBQ Barn | American | Chicago | 3 | $$ |
| Pasta Palace | Mexican | Miami | 4 | $$$ |
| Burger Haven | Italian | San Francisco | 3 | $$$$$ |
| Pizza Planet | French | New York | 3 | $$$ |
| Vegan Delight | Mediterranean | New York | 4 | $$ |
<end>Please transform the following csv data into Json:
Company,Sector,Market Cap,Stock Price,Annual Revenue (B),Quarter
BioPharm,Energy,Small Cap,824.82,262.94,Q1
AeroSpace,Retail,Mega Cap,341.28,329.83,Q1
FinanceWorks,Aerospace,Mid Cap,286.91,75.23,Q3
FinanceWorks,Aerospace,Mid Cap,509.9,472.55,Q1
<start>
[
    {
        "Company": "BioPharm",
        "Sector": "Energy",
        "Market Cap": "Small Cap",
        "Stock Price": 824.82,
        "Annual Revenue (B)": 262.94,
        "Quarter": "Q1"
    },
    {
        "Company": "AeroSpace",
        "Sector": "Retail",
        "Market Cap": "Mega Cap",
        "Stock Price": 341.28,
        "Annual Revenue (B)": 329.83,
        "Quarter": "Q1"
    },
    {
        "Company": "FinanceWorks",
        "Sector": "Aerospace",
        "Market Cap": "Mid Cap",
        "Stock Price": 286.91,
        "Annual Revenue (B)": 75.23,
        "Quarter": "Q3"
    },
    {
        "Company": "FinanceWorks",
        "Sector": "Aerospace",
        "Market Cap": "Mid Cap",
        "Stock Price": 509.9,
        "Annual Revenue (B)": 472.55,
        "Quarter": "Q1"
    }
]
<end>Can you change this plain text into Yml?
Trip Name: Forest Journey | Start Location: Phoenix | End Location: Houston | Duration (hours): 26.8 | Fuel Used (gallons): 46.0
Trip Name: Forest Journey | Start Location: Los Angeles | End Location: San Francisco | Duration (hours): 25.5 | Fuel Used (gallons): 44.9
Trip Name: Historic Route | Start Location: Chicago | End Location: Miami | Duration (hours): 34.9 | Fuel Used (gallons): 89.9
Trip Name: Canyon Trek | Start Location: San Francisco | End Location: Chicago | Duration (hours): 62.9 | Fuel Used (gallons): 83.8
Trip Name: Canyon Trek | Start Location: Phoenix | End Location: Los Angeles | Duration (hours): 66.7 | Fuel Used (gallons): 55.7
Trip Name: Lakeside Retreat | Start Location: New York | End Location: Chicago | Duration (hours): 66.7 | Fuel Used (gallons): 29.3
<start>
- Duration (hours): 26.8
  End Location: Houston
  Fuel Used (gallons): 46.0
  Start Location: Phoenix
  Trip Name: Forest Journey
- Duration (hours): 25.5
  End Location: San Francisco
  Fuel Used (gallons): 44.9
  Start Location: Los Angeles
  Trip Name: Forest Journey
- Duration (hours): 34.9
  End Location: Miami
  Fuel Used (gallons): 89.9
  Start Location: Chicago
  Trip Name: Historic Route
- Duration (hours): 62.9
  End Location: Chicago
  Fuel Used (gallons): 83.8
  Start Location: San Francisco
  Trip Name: Canyon Trek
- Duration (hours): 66.7
  End Location: Los Angeles
  Fuel Used (gallons): 55.7
  Start Location: Phoenix
  Trip Name: Canyon Trek
- Duration (hours): 66.7
  End Location: Chicago
  Fuel Used (gallons): 29.3
  Start Location: New York
  Trip Name: Lakeside Retreat
<end>Please transform the following plain text data into json:
Company: RetailHub | Sector: Finance | Market Cap: Mid Cap | Annual Revenue (B): 381.16 | Quarter: Q4
Company: HealthPlus | Sector: Retail | Market Cap: Large Cap | Annual Revenue (B): 456.61 | Quarter: Q1
Company: GlobalTrade | Sector: Finance | Market Cap: Small Cap | Annual Revenue (B): 434.74 | Quarter: Q1
Company: RetailHub | Sector: Healthcare | Market Cap: Large Cap | Annual Revenue (B): 344.03 | Quarter: Q3
Company: RetailHub | Sector: Biotech | Market Cap: Mega Cap | Annual Revenue (B): 239.72 | Quarter: Q4
<start>
[
    {
        "Company": "RetailHub",
        "Sector": "Finance",
        "Market Cap": "Mid Cap",
        "Annual Revenue (B)": 381.16,
        "Quarter": "Q4"
    },
    {
        "Company": "HealthPlus",
        "Sector": "Retail",
        "Market Cap": "Large Cap",
        "Annual Revenue (B)": 456.61,
        "Quarter": "Q1"
    },
    {
        "Company": "GlobalTrade",
        "Sector": "Finance",
        "Market Cap": "Small Cap",
        "Annual Revenue (B)": 434.74,
        "Quarter": "Q1"
    },
    {
        "Company": "RetailHub",
        "Sector": "Healthcare",
        "Market Cap": "Large Cap",
        "Annual Revenue (B)": 344.03,
        "Quarter": "Q3"
    },
    {
        "Company": "RetailHub",
        "Sector": "Biotech",
        "Market Cap": "Mega Cap",
        "Annual Revenue (B)": 239.72,
        "Quarter": "Q4"
    }
]
<end>Can you change this JSON into markdown?
[
    {
        "Company": "BioLife",
        "Date": "2011-07-21",
        "Open Price": 805.54,
        "Low Price": 805.54,
        "Volume": 8219841
    },
    {
        "Company": "FinanceTrust",
        "Date": "2016-04-13",
        "Open Price": 871.64,
        "Low Price": 231.84,
        "Volume": 2128246
    },
    {
        "Company": "AutoMotive",
        "Date": "2015-05-08",
        "Open Price": 1050.12,
        "Low Price": 1050.12,
        "Volume": 9428779
    }
]<start>
| Company | Date | Open Price | Low Price | Volume |
| --- | --- | --- | --- | --- |
| BioLife | 2011-07-21 | 805.54 | 805.54 | 8219841 |
| FinanceTrust | 2016-04-13 | 871.64 | 231.84 | 2128246 |
| AutoMotive | 2015-05-08 | 1050.12 | 1050.12 | 9428779 |
<end>Please transform the following Plain text data into markdown:
Database Name: AnalyticsDB | Connection Count: 213 | Average Latency (ms): 28.48
Database Name: OrdersDB | Connection Count: 100 | Average Latency (ms): 39.07
Database Name: SalesDB | Connection Count: 220 | Average Latency (ms): 72.65
Database Name: InventoryDB | Connection Count: 443 | Average Latency (ms): 89.52
<start>
| Database Name | Connection Count | Average Latency (ms) |
| --- | --- | --- |
| AnalyticsDB | 213 | 28.48 |
| OrdersDB | 100 | 39.07 |
| SalesDB | 220 | 72.65 |
| InventoryDB | 443 | 89.52 |
<end>Can you change this MARKDOWN into plain text?
| Product Name | SKU | Stock Quantity | Category | Supplier Name |
| --- | --- | --- | --- | --- |
| Doohickey | SKU-1068 | 295 | Automotive | ACME Corp |
| Thingamajig | SKU-1031 | 71 | Toys | ACME Corp |
| Widget | SKU-1049 | 155 | Household | ACME Corp |
| Apparatus | SKU-1030 | 59 | Electronics | Umbrella Corp |
| Thingamajig | SKU-1041 | 76 | Automotive | Umbrella Corp |
| Contraption | SKU-1050 | 351 | Household | Umbrella Corp |
| Whatchamacallit | SKU-1016 | 148 | Toys | ACME Corp |<start>
Product Name: Doohickey | SKU: SKU-1068 | Stock Quantity: 295 | Category: Automotive | Supplier Name: ACME Corp
Product Name: Thingamajig | SKU: SKU-1031 | Stock Quantity: 71 | Category: Toys | Supplier Name: ACME Corp
Product Name: Widget | SKU: SKU-1049 | Stock Quantity: 155 | Category: Household | Supplier Name: ACME Corp
Product Name: Apparatus | SKU: SKU-1030 | Stock Quantity: 59 | Category: Electronics | Supplier Name: Umbrella Corp
Product Name: Thingamajig | SKU: SKU-1041 | Stock Quantity: 76 | Category: Automotive | Supplier Name: Umbrella Corp
Product Name: Contraption | SKU: SKU-1050 | Stock Quantity: 351 | Category: Household | Supplier Name: Umbrella Corp
Product Name: Whatchamacallit | SKU: SKU-1016 | Stock Quantity: 148 | Category: Toys | Supplier Name: ACME Corp
<end>Transform this MARKDOWN structure to a PLAIN TEXT format:
| Company | Date | Open Price | Close Price | Low Price | Volume |
| --- | --- | --- | --- | --- | --- |
| BioLife | 2015-09-07 | 746.88 | 395.12 | 395.12 | 7967147 |
| AeroSystems | 2015-02-19 | 588.23 | 686.53 | 588.23 | 4710871 |
| AutoMotive | 2023-05-07 | 460.6 | 416.0 | 13.72 | 6237510 |
| AeroSystems | 2019-07-05 | 650.69 | 1495.25 | 650.69 | 1140187 |
| GreenEnergy | 2020-07-07 | 290.86 | 431.46 | 290.86 | 8344448 |
| GreenEnergy | 2014-11-18 | 1279.5 | 395.12 | 395.12 | 9294483 |
| HealthGen | 2015-12-12 | 785.8 | 33.01 | 33.01 | 6117910 |
| FinanceTrust | 2010-05-13 | 624.44 | 13.72 | 13.72 | 2609969 |
| HealthGen | 2019-09-08 | 459.43 | 1495.25 | 459.43 | 3985991 |<start>
Company: BioLife | Date: 2015-09-07 | Open Price: 746.88 | Close Price: 395.12 | Low Price: 395.12 | Volume: 7967147
Company: AeroSystems | Date: 2015-02-19 | Open Price: 588.23 | Close Price: 686.53 | Low Price: 588.23 | Volume: 4710871
Company: AutoMotive | Date: 2023-05-07 | Open Price: 460.6 | Close Price: 416.0 | Low Price: 13.72 | Volume: 6237510
Company: AeroSystems | Date: 2019-07-05 | Open Price: 650.69 | Close Price: 1495.25 | Low Price: 650.69 | Volume: 1140187
Company: GreenEnergy | Date: 2020-07-07 | Open Price: 290.86 | Close Price: 431.46 | Low Price: 290.86 | Volume: 8344448
Company: GreenEnergy | Date: 2014-11-18 | Open Price: 1279.5 | Close Price: 395.12 | Low Price: 395.12 | Volume: 9294483
Company: HealthGen | Date: 2015-12-12 | Open Price: 785.8 | Close Price: 33.01 | Low Price: 33.01 | Volume: 6117910
Company: FinanceTrust | Date: 2010-05-13 | Open Price: 624.44 | Close Price: 13.72 | Low Price: 13.72 | Volume: 2609969
Company: HealthGen | Date: 2019-09-08 | Open Price: 459.43 | Close Price: 1495.25 | Low Price: 459.43 | Volume: 3985991
<end>Transform this plain text structure to a Yml format:
Device ID: device-0100 | Device Type: Humidity Sensor | Location: Office | Battery Level (%): 46.1 | Timestamp: 2021-11-10 06:13:19
Device ID: device-0069 | Device Type: Temperature Sensor | Location: Bathroom | Battery Level (%): 38.7 | Timestamp: 2021-08-02 10:20:57
Device ID: device-0078 | Device Type: Light Sensor | Location: Hallway | Battery Level (%): 32.5 | Timestamp: 2023-10-14 06:02:26
Device ID: device-0043 | Device Type: Humidity Sensor | Location: Living Room | Battery Level (%): 99.3 | Timestamp: 2023-05-05 05:53:21
Device ID: device-0022 | Device Type: Temperature Sensor | Location: Garage | Battery Level (%): 53.0 | Timestamp: 2022-09-03 16:30:18
<start>
- Battery Level (%): 46.1
  Device ID: device-0100
  Device Type: Humidity Sensor
  Location: Office
  Timestamp: '2021-11-10 06:13:19'
- Battery Level (%): 38.7
  Device ID: device-0069
  Device Type: Temperature Sensor
  Location: Bathroom
  Timestamp: '2021-08-02 10:20:57'
- Battery Level (%): 32.5
  Device ID: device-0078
  Device Type: Light Sensor
  Location: Hallway
  Timestamp: '2023-10-14 06:02:26'
- Battery Level (%): 99.3
  Device ID: device-0043
  Device Type: Humidity Sensor
  Location: Living Room
  Timestamp: '2023-05-05 05:53:21'
- Battery Level (%): 53.0
  Device ID: device-0022
  Device Type: Temperature Sensor
  Location: Garage
  Timestamp: '2022-09-03 16:30:18'
<end>Please transform the following markdown data into json:
| Database Name | Cache Hit Ratio (%) | Average Latency (ms) | Timestamp |
| --- | --- | --- | --- |
| LogsDB | 73.69 | 44.01 | 2022-07-08 16:28:59 |
| MetricsDB | 70.2 | 19.1 | 2022-02-08 05:24:26 |
| OrdersDB | 74.26 | 61.3 | 2021-12-03 13:32:11 |
| ProductsDB | 98.85 | 67.15 | 2022-07-15 19:59:14 |
| InventoryDB | 88.3 | 66.4 | 2021-09-26 17:38:07 |
| LogsDB | 79.8 | 30.64 | 2023-08-22 02:50:51 |
| SalesDB | 86.05 | 74.44 | 2022-04-11 11:04:10 |
| SalesDB | 77.86 | 6.15 | 2021-04-19 10:26:53 |
| LogsDB | 87.24 | 5.04 | 2022-09-25 23:32:08 |
| ProductsDB | 86.96 | 5.93 | 2023-02-10 07:01:27 |<start>
[
    {
        "Database Name": "LogsDB",
        "Cache Hit Ratio (%)": 73.69,
        "Average Latency (ms)": 44.01,
        "Timestamp": "2022-07-08 16:28:59"
    },
    {
        "Database Name": "MetricsDB",
        "Cache Hit Ratio (%)": 70.2,
        "Average Latency (ms)": 19.1,
        "Timestamp": "2022-02-08 05:24:26"
    },
    {
        "Database Name": "OrdersDB",
        "Cache Hit Ratio (%)": 74.26,
        "Average Latency (ms)": 61.3,
        "Timestamp": "2021-12-03 13:32:11"
    },
    {
        "Database Name": "ProductsDB",
        "Cache Hit Ratio (%)": 98.85,
        "Average Latency (ms)": 67.15,
        "Timestamp": "2022-07-15 19:59:14"
    },
    {
        "Database Name": "InventoryDB",
        "Cache Hit Ratio (%)": 88.3,
        "Average Latency (ms)": 66.4,
        "Timestamp": "2021-09-26 17:38:07"
    },
    {
        "Database Name": "LogsDB",
        "Cache Hit Ratio (%)": 79.8,
        "Average Latency (ms)": 30.64,
        "Timestamp": "2023-08-22 02:50:51"
    },
    {
        "Database Name": "SalesDB",
        "Cache Hit Ratio (%)": 86.05,
        "Average Latency (ms)": 74.44,
        "Timestamp": "2022-04-11 11:04:10"
    },
    {
        "Database Name": "SalesDB",
        "Cache Hit Ratio (%)": 77.86,
        "Average Latency (ms)": 6.15,
        "Timestamp": "2021-04-19 10:26:53"
    },
    {
        "Database Name": "LogsDB",
        "Cache Hit Ratio (%)": 87.24,
        "Average Latency (ms)": 5.04,
        "Timestamp": "2022-09-25 23:32:08"
    },
    {
        "Database Name": "ProductsDB",
        "Cache Hit Ratio (%)": 86.96,
        "Average Latency (ms)": 5.93,
        "Timestamp": "2023-02-10 07:01:27"
    }
]
<end>Transform this yml structure to a MARKDOWN format:
- Device ID: device-0045
  Reading Value: 80.91
  Timestamp: '2022-02-18 23:16:36'
- Device ID: device-0053
  Reading Value: 30.16
  Timestamp: '2023-11-15 10:48:58'
- Device ID: device-0019
  Reading Value: 84.59
  Timestamp: '2022-01-06 09:50:02'
- Device ID: device-0074
  Reading Value: -10.68
  Timestamp: '2021-11-07 09:13:53'
- Device ID: device-0098
  Reading Value: 84.59
  Timestamp: '2021-05-25 08:39:31'
- Device ID: device-0020
  Reading Value: -8.87
  Timestamp: '2022-07-12 02:51:14'
- Device ID: device-0081
  Reading Value: -8.87
  Timestamp: '2021-02-16 04:44:11'
<start>
| Device ID | Reading Value | Timestamp |
| --- | --- | --- |
| device-0045 | 80.91 | 2022-02-18 23:16:36 |
| device-0053 | 30.16 | 2023-11-15 10:48:58 |
| device-0019 | 84.59 | 2022-01-06 09:50:02 |
| device-0074 | -10.68 | 2021-11-07 09:13:53 |
| device-0098 | 84.59 | 2021-05-25 08:39:31 |
| device-0020 | -8.87 | 2022-07-12 02:51:14 |
| device-0081 | -8.87 | 2021-02-16 04:44:11 |
<end>Transform this CSV structure to a Json format:
Product Name,SKU,Price,Stock Quantity,Category,Supplier Name
Apparatus,SKU-1038,393.64,496,Toys,Globex
Doohickey,SKU-1004,205.65,466,Household,ACME Corp
Thingamajig,SKU-1002,59.85,218,Automotive,ACME Corp
Apparatus,SKU-1029,160.42,329,Toys,Wonka Industries
Apparatus,SKU-1065,236.09,243,Toys,Wonka Industries
Contraption,SKU-1021,414.5,136,Electronics,Globex
<start>
[
    {
        "Product Name": "Apparatus",
        "SKU": "SKU-1038",
        "Price": 393.64,
        "Stock Quantity": 496,
        "Category": "Toys",
        "Supplier Name": "Globex"
    },
    {
        "Product Name": "Doohickey",
        "SKU": "SKU-1004",
        "Price": 205.65,
        "Stock Quantity": 466,
        "Category": "Household",
        "Supplier Name": "ACME Corp"
    },
    {
        "Product Name": "Thingamajig",
        "SKU": "SKU-1002",
        "Price": 59.85,
        "Stock Quantity": 218,
        "Category": "Automotive",
        "Supplier Name": "ACME Corp"
    },
    {
        "Product Name": "Apparatus",
        "SKU": "SKU-1029",
        "Price": 160.42,
        "Stock Quantity": 329,
        "Category": "Toys",
        "Supplier Name": "Wonka Industries"
    },
    {
        "Product Name": "Apparatus",
        "SKU": "SKU-1065",
        "Price": 236.09,
        "Stock Quantity": 243,
        "Category": "Toys",
        "Supplier Name": "Wonka Industries"
    },
    {
        "Product Name": "Contraption",
        "SKU": "SKU-1021",
        "Price": 414.5,
        "Stock Quantity": 136,
        "Category": "Electronics",
        "Supplier Name": "Globex"
    }
]
<end>Please transform the following YML data into markdown:
- Category: Automotive
  Price: 109.2
  SKU: SKU-1027
  Stock Quantity: 82
- Category: Toys
  Price: 495.81
  SKU: SKU-1083
  Stock Quantity: 220
- Category: Electronics
  Price: 37.85
  SKU: SKU-1057
  Stock Quantity: 91
- Category: Household
  Price: 470.19
  SKU: SKU-1082
  Stock Quantity: 443
- Category: Sports
  Price: 267.51
  SKU: SKU-1078
  Stock Quantity: 320
- Category: Sports
  Price: 429.47
  SKU: SKU-1044
  Stock Quantity: 445
- Category: Sports
  Price: 58.94
  SKU: SKU-1087
  Stock Quantity: 468
- Category: Toys
  Price: 130.13
  SKU: SKU-1065
  Stock Quantity: 99
<start>
| SKU | Price | Stock Quantity | Category |
| --- | --- | --- | --- |
| SKU-1027 | 109.2 | 82 | Automotive |
| SKU-1083 | 495.81 | 220 | Toys |
| SKU-1057 | 37.85 | 91 | Electronics |
| SKU-1082 | 470.19 | 443 | Household |
| SKU-1078 | 267.51 | 320 | Sports |
| SKU-1044 | 429.47 | 445 | Sports |
| SKU-1087 | 58.94 | 468 | Sports |
| SKU-1065 | 130.13 | 99 | Toys |
<end>Transform this plain text structure to a CSV format:
Sector: Finance | Market Cap: Small Cap | Annual Revenue (B): 262.12 | Quarter: Q1
Sector: Technology | Market Cap: Mid Cap | Annual Revenue (B): 491.74 | Quarter: Q3
Sector: Retail | Market Cap: Large Cap | Annual Revenue (B): 220.0 | Quarter: Q3
Sector: Biotech | Market Cap: Mega Cap | Annual Revenue (B): 443.57 | Quarter: Q1
Sector: Retail | Market Cap: Mid Cap | Annual Revenue (B): 276.86 | Quarter: Q1
Sector: Finance | Market Cap: Small Cap | Annual Revenue (B): 411.37 | Quarter: Q2
Sector: Biotech | Market Cap: Mega Cap | Annual Revenue (B): 257.06 | Quarter: Q2
Sector: Biotech | Market Cap: Small Cap | Annual Revenue (B): 434.07 | Quarter: Q1
Sector: Energy | Market Cap: Small Cap | Annual Revenue (B): 491.74 | Quarter: Q2
Sector: Biotech | Market Cap: Small Cap | Annual Revenue (B): 163.39 | Quarter: Q3
<start>
Sector,Market Cap,Annual Revenue (B),Quarter
Finance,Small Cap,262.12,Q1
Technology,Mid Cap,491.74,Q3
Retail,Large Cap,220.0,Q3
Biotech,Mega Cap,443.57,Q1
Retail,Mid Cap,276.86,Q1
Finance,Small Cap,411.37,Q2
Biotech,Mega Cap,257.06,Q2
Biotech,Small Cap,434.07,Q1
Energy,Small Cap,491.74,Q2
Biotech,Small Cap,163.39,Q3
<end>Convert this YML to Plain text:
- Location: Los Angeles
  Temperature (C): -2.4
  Wind Speed (km/h): 15.3
- Location: Phoenix
  Temperature (C): 0.2
  Wind Speed (km/h): 9.3
- Location: Denver
  Temperature (C): 10.5
  Wind Speed (km/h): 27.0
- Location: Denver
  Temperature (C): 38.8
  Wind Speed (km/h): 15.5
<start>
Location: Los Angeles | Temperature (C): -2.4 | Wind Speed (km/h): 15.3
Location: Phoenix | Temperature (C): 0.2 | Wind Speed (km/h): 9.3
Location: Denver | Temperature (C): 10.5 | Wind Speed (km/h): 27.0
Location: Denver | Temperature (C): 38.8 | Wind Speed (km/h): 15.5
<end>Can you change this yaml into Markdown?
- Price: 231.43
  Product Name: Gizmo
  SKU: SKU-1061
  Stock Quantity: 240
- Price: 14.67
  Product Name: Gizmo
  SKU: SKU-1004
  Stock Quantity: 357
- Price: 122.81
  Product Name: Whatchamacallit
  SKU: SKU-1020
  Stock Quantity: 464
<start>
| Product Name | SKU | Price | Stock Quantity |
| --- | --- | --- | --- |
| Gizmo | SKU-1061 | 231.43 | 240 |
| Gizmo | SKU-1004 | 14.67 | 357 |
| Whatchamacallit | SKU-1020 | 122.81 | 464 |
<end>Convert this JSON to YML:
[
    {
        "Company": "FoodChain",
        "Date": "2018-09-19",
        "Open Price": 1121.17,
        "Close Price": 596.45,
        "High Price": 1121.17,
        "Low Price": 262.75,
        "Volume": 3124330
    },
    {
        "Company": "FinanceTrust",
        "Date": "2023-06-08",
        "Open Price": 1207.81,
        "Close Price": 1482.88,
        "High Price": 1482.88,
        "Low Price": 1089.16,
        "Volume": 3289143
    },
    {
        "Company": "TechnoCorp",
        "Date": "2018-06-22",
        "Open Price": 149.91,
        "Close Price": 646.58,
        "High Price": 1465.29,
        "Low Price": 149.91,
        "Volume": 7076606
    },
    {
        "Company": "AeroSystems",
        "Date": "2013-08-05",
        "Open Price": 709.35,
        "Close Price": 1154.1,
        "High Price": 1154.1,
        "Low Price": 709.35,
        "Volume": 4915555
    },
    {
        "Company": "BioLife",
        "Date": "2013-12-06",
        "Open Price": 622.75,
        "Close Price": 1472.95,
        "High Price": 1472.95,
        "Low Price": 622.75,
        "Volume": 9094196
    },
    {
        "Company": "HealthGen",
        "Date": "2022-12-10",
        "Open Price": 226.56,
        "Close Price": 545.36,
        "High Price": 1036.62,
        "Low Price": 226.56,
        "Volume": 5468693
    },
    {
        "Company": "HealthGen",
        "Date": "2014-07-14",
        "Open Price": 735.93,
        "Close Price": 892.09,
        "High Price": 892.09,
        "Low Price": 735.93,
        "Volume": 6279261
    }
]<start>
- Close Price: 596.45
  Company: FoodChain
  Date: '2018-09-19'
  High Price: 1121.17
  Low Price: 262.75
  Open Price: 1121.17
  Volume: 3124330
- Close Price: 1482.88
  Company: FinanceTrust
  Date: '2023-06-08'
  High Price: 1482.88
  Low Price: 1089.16
  Open Price: 1207.81
  Volume: 3289143
- Close Price: 646.58
  Company: TechnoCorp
  Date: '2018-06-22'
  High Price: 1465.29
  Low Price: 149.91
  Open Price: 149.91
  Volume: 7076606
- Close Price: 1154.1
  Company: AeroSystems
  Date: '2013-08-05'
  High Price: 1154.1
  Low Price: 709.35
  Open Price: 709.35
  Volume: 4915555
- Close Price: 1472.95
  Company: BioLife
  Date: '2013-12-06'
  High Price: 1472.95
  Low Price: 622.75
  Open Price: 622.75
  Volume: 9094196
- Close Price: 545.36
  Company: HealthGen
  Date: '2022-12-10'
  High Price: 1036.62
  Low Price: 226.56
  Open Price: 226.56
  Volume: 5468693
- Close Price: 892.09
  Company: HealthGen
  Date: '2014-07-14'
  High Price: 892.09
  Low Price: 735.93
  Open Price: 735.93
  Volume: 6279261
<end>Please transform the following markdown data into json:
| Condition | Temperature (C) | Wind Speed (km/h) | Day |
| --- | --- | --- | --- |
| Foggy | 24.1 | 4.5 | Saturday |
| Sunny | 36.4 | 10.7 | Tuesday |
| Foggy | 2.2 | 0.3 | Thursday |
| Sunny | 24.5 | 24.6 | Saturday |
| Cloudy | 1.2 | 10.9 | Wednesday |<start>
[
    {
        "Condition": "Foggy",
        "Temperature (C)": 24.1,
        "Wind Speed (km/h)": 4.5,
        "Day": "Saturday"
    },
    {
        "Condition": "Sunny",
        "Temperature (C)": 36.4,
        "Wind Speed (km/h)": 10.7,
        "Day": "Tuesday"
    },
    {
        "Condition": "Foggy",
        "Temperature (C)": 2.2,
        "Wind Speed (km/h)": 0.3,
        "Day": "Thursday"
    },
    {
        "Condition": "Sunny",
        "Temperature (C)": 24.5,
        "Wind Speed (km/h)": 24.6,
        "Day": "Saturday"
    },
    {
        "Condition": "Cloudy",
        "Temperature (C)": 1.2,
        "Wind Speed (km/h)": 10.9,
        "Day": "Wednesday"
    }
]
<end>Transform this Yml structure to a Plain text format:
- Distance (miles): 1158.3
  Duration (hours): 45.9
  End Location: Miami
  Fuel Used (gallons): 18.8
  Start Location: San Francisco
  Trip Name: Mountain Adventure
- Distance (miles): 1660.9
  Duration (hours): 31.8
  End Location: Miami
  Fuel Used (gallons): 33.7
  Start Location: Denver
  Trip Name: City Explorer
- Distance (miles): 2855.6
  Duration (hours): 53.1
  End Location: Los Angeles
  Fuel Used (gallons): 64.9
  Start Location: Phoenix
  Trip Name: Desert Drive
- Distance (miles): 800.0
  Duration (hours): 34.3
  End Location: Miami
  Fuel Used (gallons): 53.1
  Start Location: Denver
  Trip Name: Coast to Coast
<start>
Trip Name: Mountain Adventure | Start Location: San Francisco | End Location: Miami | Distance (miles): 1158.3 | Duration (hours): 45.9 | Fuel Used (gallons): 18.8
Trip Name: City Explorer | Start Location: Denver | End Location: Miami | Distance (miles): 1660.9 | Duration (hours): 31.8 | Fuel Used (gallons): 33.7
Trip Name: Desert Drive | Start Location: Phoenix | End Location: Los Angeles | Distance (miles): 2855.6 | Duration (hours): 53.1 | Fuel Used (gallons): 64.9
Trip Name: Coast to Coast | Start Location: Denver | End Location: Miami | Distance (miles): 800.0 | Duration (hours): 34.3 | Fuel Used (gallons): 53.1
<end>Transform this PLAIN TEXT structure to a markdown format:
Name: Luke | Age: 51 | Birth Month: January | Income: 235000
Name: Clifford | Age: 51 | Birth Month: February | Income: 395000
Name: Amy | Age: 43 | Birth Month: July | Income: 45000
Name: Imogene | Age: 38 | Birth Month: June | Income: 40000
Name: Imogene | Age: 49 | Birth Month: July | Income: 315000
<start>
| Name | Age | Birth Month | Income |
| --- | --- | --- | --- |
| Luke | 51 | January | 235000 |
| Clifford | 51 | February | 395000 |
| Amy | 43 | July | 45000 |
| Imogene | 38 | June | 40000 |
| Imogene | 49 | July | 315000 |
<end>Please transform the following Markdown data into csv:
| Queries per Second | Cache Hit Ratio (%) | Connection Count | Average Latency (ms) |
| --- | --- | --- | --- |
| 3859.85 | 93.93 | 420 | 36.6 |
| 3901.75 | 80.38 | 429 | 99.27 |
| 1580.9 | 93.47 | 192 | 57.98 |
| 4625.94 | 87.42 | 336 | 59.96 |
| 2375.3 | 72.51 | 80 | 62.93 |
| 1238.28 | 93.16 | 286 | 66.94 |
| 1536.65 | 84.17 | 237 | 73.13 |<start>
Queries per Second,Cache Hit Ratio (%),Connection Count,Average Latency (ms)
3859.85,93.93,420,36.6
3901.75,80.38,429,99.27
1580.9,93.47,192,57.98
4625.94,87.42,336,59.96
2375.3,72.51,80,62.93
1238.28,93.16,286,66.94
1536.65,84.17,237,73.13
<end>Please transform the following plain text data into Json:
Director: Mara Moonshadow | Box Office Earnings (M): 392.41
Director: Drake Nightshade | Box Office Earnings (M): 553.78
Director: Aria Ravenwood | Box Office Earnings (M): 691.47
Director: Rylan Frostblade | Box Office Earnings (M): 67.62
Director: Cade Firebrand | Box Office Earnings (M): 889.1
<start>
[
    {
        "Director": "Mara Moonshadow",
        "Box Office Earnings (M)": 392.41
    },
    {
        "Director": "Drake Nightshade",
        "Box Office Earnings (M)": 553.78
    },
    {
        "Director": "Aria Ravenwood",
        "Box Office Earnings (M)": 691.47
    },
    {
        "Director": "Rylan Frostblade",
        "Box Office Earnings (M)": 67.62
    },
    {
        "Director": "Cade Firebrand",
        "Box Office Earnings (M)": 889.1
    }
]
<end>Convert this JSON to plain text:
[
    {
        "Trip Name": "Canyon Trek",
        "Start Location": "Houston",
        "End Location": "Phoenix",
        "Distance (miles)": 2190.6,
        "Duration (hours)": 48.5,
        "Fuel Used (gallons)": 63.0
    },
    {
        "Trip Name": "City Explorer",
        "Start Location": "New York",
        "End Location": "Los Angeles",
        "Distance (miles)": 1476.4,
        "Duration (hours)": 44.5,
        "Fuel Used (gallons)": 81.5
    },
    {
        "Trip Name": "Mountain Adventure",
        "Start Location": "New York",
        "End Location": "Phoenix",
        "Distance (miles)": 2944.4,
        "Duration (hours)": 27.5,
        "Fuel Used (gallons)": 24.0
    },
    {
        "Trip Name": "Lakeside Retreat",
        "Start Location": "Houston",
        "End Location": "Denver",
        "Distance (miles)": 1754.5,
        "Duration (hours)": 22.6,
        "Fuel Used (gallons)": 69.1
    },
    {
        "Trip Name": "Valley Voyage",
        "Start Location": "Miami",
        "End Location": "San Francisco",
        "Distance (miles)": 136.5,
        "Duration (hours)": 36.0,
        "Fuel Used (gallons)": 89.3
    },
    {
        "Trip Name": "Canyon Trek",
        "Start Location": "Phoenix",
        "End Location": "Houston",
        "Distance (miles)": 2236.3,
        "Duration (hours)": 1.8,
        "Fuel Used (gallons)": 33.7
    }
]<start>
Trip Name: Canyon Trek | Start Location: Houston | End Location: Phoenix | Distance (miles): 2190.6 | Duration (hours): 48.5 | Fuel Used (gallons): 63.0
Trip Name: City Explorer | Start Location: New York | End Location: Los Angeles | Distance (miles): 1476.4 | Duration (hours): 44.5 | Fuel Used (gallons): 81.5
Trip Name: Mountain Adventure | Start Location: New York | End Location: Phoenix | Distance (miles): 2944.4 | Duration (hours): 27.5 | Fuel Used (gallons): 24.0
Trip Name: Lakeside Retreat | Start Location: Houston | End Location: Denver | Distance (miles): 1754.5 | Duration (hours): 22.6 | Fuel Used (gallons): 69.1
Trip Name: Valley Voyage | Start Location: Miami | End Location: San Francisco | Distance (miles): 136.5 | Duration (hours): 36.0 | Fuel Used (gallons): 89.3
Trip Name: Canyon Trek | Start Location: Phoenix | End Location: Houston | Distance (miles): 2236.3 | Duration (hours): 1.8 | Fuel Used (gallons): 33.7
<end>Please transform the following Yaml data into Csv:
- Average Latency (ms): 27.41
  Cache Hit Ratio (%): 75.3
  Connection Count: 381
  Database Name: InventoryDB
  Queries per Second: 2846.35
  Timestamp: '2021-10-11 08:05:07'
- Average Latency (ms): 51.81
  Cache Hit Ratio (%): 70.18
  Connection Count: 409
  Database Name: ProfilesDB
  Queries per Second: 1363.72
  Timestamp: '2021-02-21 12:11:03'
- Average Latency (ms): 54.54
  Cache Hit Ratio (%): 92.13
  Connection Count: 380
  Database Name: SalesDB
  Queries per Second: 1453.56
  Timestamp: '2023-08-18 09:32:52'
- Average Latency (ms): 75.93
  Cache Hit Ratio (%): 85.16
  Connection Count: 335
  Database Name: LogsDB
  Queries per Second: 4325.52
  Timestamp: '2023-05-07 10:30:44'
- Average Latency (ms): 55.85
  Cache Hit Ratio (%): 71.38
  Connection Count: 326
  Database Name: AnalyticsDB
  Queries per Second: 3592.11
  Timestamp: '2023-02-14 19:16:46'
- Average Latency (ms): 64.49
  Cache Hit Ratio (%): 86.23
  Connection Count: 77
  Database Name: MetricsDB
  Queries per Second: 2043.17
  Timestamp: '2021-10-04 12:09:29'
- Average Latency (ms): 21.22
  Cache Hit Ratio (%): 89.94
  Connection Count: 249
  Database Name: OrdersDB
  Queries per Second: 4325.52
  Timestamp: '2023-09-10 17:54:09'
- Average Latency (ms): 57.98
  Cache Hit Ratio (%): 88.16
  Connection Count: 26
  Database Name: ProfilesDB
  Queries per Second: 1058.52
  Timestamp: '2022-06-20 20:26:07'
<start>
Database Name,Queries per Second,Cache Hit Ratio (%),Connection Count,Average Latency (ms),Timestamp
InventoryDB,2846.35,75.3,381,27.41,2021-10-11 08:05:07
ProfilesDB,1363.72,70.18,409,51.81,2021-02-21 12:11:03
SalesDB,1453.56,92.13,380,54.54,2023-08-18 09:32:52
LogsDB,4325.52,85.16,335,75.93,2023-05-07 10:30:44
AnalyticsDB,3592.11,71.38,326,55.85,2023-02-14 19:16:46
MetricsDB,2043.17,86.23,77,64.49,2021-10-04 12:09:29
OrdersDB,4325.52,89.94,249,21.22,2023-09-10 17:54:09
ProfilesDB,1058.52,88.16,26,57.98,2022-06-20 20:26:07
<end>Can you change this yaml into JSON?
- Cache Hit Ratio (%): 86.86
  Connection Count: 469
  Database Name: ProductsDB
  Queries per Second: 1605.64
  Timestamp: '2022-05-24 16:13:31'
- Cache Hit Ratio (%): 82.59
  Connection Count: 497
  Database Name: InventoryDB
  Queries per Second: 3284.54
  Timestamp: '2021-03-19 22:11:32'
- Cache Hit Ratio (%): 80.2
  Connection Count: 57
  Database Name: SalesDB
  Queries per Second: 153.17
  Timestamp: '2023-05-03 22:36:04'
- Cache Hit Ratio (%): 86.53
  Connection Count: 20
  Database Name: OrdersDB
  Queries per Second: 64.85
  Timestamp: '2023-04-05 09:26:07'
- Cache Hit Ratio (%): 74.85
  Connection Count: 201
  Database Name: LogsDB
  Queries per Second: 1917.01
  Timestamp: '2021-12-13 06:13:45'
- Cache Hit Ratio (%): 85.6
  Connection Count: 350
  Database Name: OrdersDB
  Queries per Second: 1001.17
  Timestamp: '2023-03-11 02:24:21'
<start>
[
    {
        "Database Name": "ProductsDB",
        "Queries per Second": 1605.64,
        "Cache Hit Ratio (%)": 86.86,
        "Connection Count": 469,
        "Timestamp": "2022-05-24 16:13:31"
    },
    {
        "Database Name": "InventoryDB",
        "Queries per Second": 3284.54,
        "Cache Hit Ratio (%)": 82.59,
        "Connection Count": 497,
        "Timestamp": "2021-03-19 22:11:32"
    },
    {
        "Database Name": "SalesDB",
        "Queries per Second": 153.17,
        "Cache Hit Ratio (%)": 80.2,
        "Connection Count": 57,
        "Timestamp": "2023-05-03 22:36:04"
    },
    {
        "Database Name": "OrdersDB",
        "Queries per Second": 64.85,
        "Cache Hit Ratio (%)": 86.53,
        "Connection Count": 20,
        "Timestamp": "2023-04-05 09:26:07"
    },
    {
        "Database Name": "LogsDB",
        "Queries per Second": 1917.01,
        "Cache Hit Ratio (%)": 74.85,
        "Connection Count": 201,
        "Timestamp": "2021-12-13 06:13:45"
    },
    {
        "Database Name": "OrdersDB",
        "Queries per Second": 1001.17,
        "Cache Hit Ratio (%)": 85.6,
        "Connection Count": 350,
        "Timestamp": "2023-03-11 02:24:21"
    }
]
<end>Here's some YAML data, can you convert it to MARKDOWN?
- Battery Level (%): 63.5
  Device ID: device-0032
  Device Type: Motion Detector
  Location: Office
  Reading Value: 49.21
  Timestamp: '2023-01-01 19:02:32'
- Battery Level (%): 40.1
  Device ID: device-0026
  Device Type: Light Sensor
  Location: Office
  Reading Value: 29.76
  Timestamp: '2021-04-17 02:30:26'
- Battery Level (%): 77.5
  Device ID: device-0045
  Device Type: Light Sensor
  Location: Bedroom
  Reading Value: 11.61
  Timestamp: '2023-02-06 21:21:14'
- Battery Level (%): 88.2
  Device ID: device-0032
  Device Type: Light Sensor
  Location: Living Room
  Reading Value: 59.33
  Timestamp: '2023-09-27 08:07:05'
- Battery Level (%): 73.9
  Device ID: device-0021
  Device Type: Pressure Sensor
  Location: Bedroom
  Reading Value: 80.54
  Timestamp: '2023-08-24 02:53:04'
- Battery Level (%): 98.9
  Device ID: device-0038
  Device Type: Light Sensor
  Location: Bathroom
  Reading Value: 25.26
  Timestamp: '2022-06-26 20:41:16'
- Battery Level (%): 75.9
  Device ID: device-0023
  Device Type: Motion Detector
  Location: Garden
  Reading Value: -26.33
  Timestamp: '2023-06-17 01:10:43'
- Battery Level (%): 63.5
  Device ID: device-0088
  Device Type: Temperature Sensor
  Location: Bathroom
  Reading Value: -30.37
  Timestamp: '2022-01-23 21:22:45'
- Battery Level (%): 35.6
  Device ID: device-0071
  Device Type: Pressure Sensor
  Location: Garage
  Reading Value: 7.24
  Timestamp: '2023-11-27 00:40:53'
<start>
| Device ID | Device Type | Location | Battery Level (%) | Reading Value | Timestamp |
| --- | --- | --- | --- | --- | --- |
| device-0032 | Motion Detector | Office | 63.5 | 49.21 | 2023-01-01 19:02:32 |
| device-0026 | Light Sensor | Office | 40.1 | 29.76 | 2021-04-17 02:30:26 |
| device-0045 | Light Sensor | Bedroom | 77.5 | 11.61 | 2023-02-06 21:21:14 |
| device-0032 | Light Sensor | Living Room | 88.2 | 59.33 | 2023-09-27 08:07:05 |
| device-0021 | Pressure Sensor | Bedroom | 73.9 | 80.54 | 2023-08-24 02:53:04 |
| device-0038 | Light Sensor | Bathroom | 98.9 | 25.26 | 2022-06-26 20:41:16 |
| device-0023 | Motion Detector | Garden | 75.9 | -26.33 | 2023-06-17 01:10:43 |
| device-0088 | Temperature Sensor | Bathroom | 63.5 | -30.37 | 2022-01-23 21:22:45 |
| device-0071 | Pressure Sensor | Garage | 35.6 | 7.24 | 2023-11-27 00:40:53 |
<end>Please transform the following YML data into CSV:
- Condition: Stormy
  Day: Monday
  Humidity (%): 80
  Location: New York
  Temperature (C): 24.6
  Wind Speed (km/h): 20.8
- Condition: Snowy
  Day: Saturday
  Humidity (%): 46
  Location: Houston
  Temperature (C): 12.4
  Wind Speed (km/h): 14.8
- Condition: Windy
  Day: Sunday
  Humidity (%): 51
  Location: Los Angeles
  Temperature (C): -8.2
  Wind Speed (km/h): 19.4
- Condition: Stormy
  Day: Tuesday
  Humidity (%): 47
  Location: Phoenix
  Temperature (C): 34.4
  Wind Speed (km/h): 20.1
- Condition: Rainy
  Day: Tuesday
  Humidity (%): 99
  Location: Houston
  Temperature (C): 14.9
  Wind Speed (km/h): 8.1
<start>
Location,Condition,Temperature (C),Humidity (%),Wind Speed (km/h),Day
New York,Stormy,24.6,80,20.8,Monday
Houston,Snowy,12.4,46,14.8,Saturday
Los Angeles,Windy,-8.2,51,19.4,Sunday
Phoenix,Stormy,34.4,47,20.1,Tuesday
Houston,Rainy,14.9,99,8.1,Tuesday
<end>Convert this CSV to Json:
Device ID,Device Type,Location,Battery Level (%),Reading Value
device-0040,Motion Detector,Living Room,66.2,26.39
device-0024,Motion Detector,Office,94.2,-25.93
device-0044,Motion Detector,Bedroom,98.9,68.65
device-0060,Humidity Sensor,Bedroom,84.1,43.15
device-0065,Temperature Sensor,Kitchen,67.7,-0.23
<start>
[
    {
        "Device ID": "device-0040",
        "Device Type": "Motion Detector",
        "Location": "Living Room",
        "Battery Level (%)": 66.2,
        "Reading Value": 26.39
    },
    {
        "Device ID": "device-0024",
        "Device Type": "Motion Detector",
        "Location": "Office",
        "Battery Level (%)": 94.2,
        "Reading Value": -25.93
    },
    {
        "Device ID": "device-0044",
        "Device Type": "Motion Detector",
        "Location": "Bedroom",
        "Battery Level (%)": 98.9,
        "Reading Value": 68.65
    },
    {
        "Device ID": "device-0060",
        "Device Type": "Humidity Sensor",
        "Location": "Bedroom",
        "Battery Level (%)": 84.1,
        "Reading Value": 43.15
    },
    {
        "Device ID": "device-0065",
        "Device Type": "Temperature Sensor",
        "Location": "Kitchen",
        "Battery Level (%)": 67.7,
        "Reading Value": -0.23
    }
]
<end>Can you change this csv into markdown?
Database Name,Cache Hit Ratio (%),Connection Count,Average Latency (ms)
ProductsDB,92.72,179,79.96
OrdersDB,81.54,325,40.52
LogsDB,70.81,371,85.9
LogsDB,73.57,351,39.17
ProductsDB,92.15,132,83.54
<start>
| Database Name | Cache Hit Ratio (%) | Connection Count | Average Latency (ms) |
| --- | --- | --- | --- |
| ProductsDB | 92.72 | 179 | 79.96 |
| OrdersDB | 81.54 | 325 | 40.52 |
| LogsDB | 70.81 | 371 | 85.9 |
| LogsDB | 73.57 | 351 | 39.17 |
| ProductsDB | 92.15 | 132 | 83.54 |
<end>Please transform the following PLAIN TEXT data into Csv:
Name: Dominique | Birth Month: November | City: Memphis | Income: 345000
Name: Edith | Birth Month: August | City: Phoenix | Income: 475000
Name: Verna | Birth Month: October | City: New York | Income: 430000
Name: Carmen | Birth Month: September | City: San Francisco | Income: 220000
Name: Johnny | Birth Month: April | City: Columbus | Income: 430000
<start>
Name,Birth Month,City,Income
Dominique,November,Memphis,345000
Edith,August,Phoenix,475000
Verna,October,New York,430000
Carmen,September,San Francisco,220000
Johnny,April,Columbus,430000
<end>Please transform the following markdown data into Yaml:
| Location | Condition | Humidity (%) |
| --- | --- | --- |
| Phoenix | Snowy | 95 |
| New York | Cloudy | 21 |
| Phoenix | Sunny | 56 |<start>
- Condition: Snowy
  Humidity (%): 95
  Location: Phoenix
- Condition: Cloudy
  Humidity (%): 21
  Location: New York
- Condition: Sunny
  Humidity (%): 56
  Location: Phoenix
<end>Convert this markdown to Csv:
| Cache Hit Ratio (%) | Connection Count | Timestamp |
| --- | --- | --- |
| 86.44 | 54 | 2023-11-23 19:57:53 |
| 99.89 | 327 | 2023-10-23 12:37:37 |
| 76.52 | 186 | 2022-04-26 21:30:37 |
| 98.7 | 119 | 2022-12-20 07:30:58 |<start>
Cache Hit Ratio (%),Connection Count,Timestamp
86.44,54,2023-11-23 19:57:53
99.89,327,2023-10-23 12:37:37
76.52,186,2022-04-26 21:30:37
98.7,119,2022-12-20 07:30:58
<end>Can you change this Csv into Yml?
Name,Birth Month
Piper,July
Susan,March
Valerie,February
James,October
Larry,October
Deanna,November
Barry,October
Gavin,February
Tara,December
Alicia,April
<start>
- Birth Month: July
  Name: Piper
- Birth Month: March
  Name: Susan
- Birth Month: February
  Name: Valerie
- Birth Month: October
  Name: James
- Birth Month: October
  Name: Larry
- Birth Month: November
  Name: Deanna
- Birth Month: October
  Name: Barry
- Birth Month: February
  Name: Gavin
- Birth Month: December
  Name: Tara
- Birth Month: April
  Name: Alicia
<end>Can you change this yml into MARKDOWN?
- Condition: Stormy
  Day: Sunday
  Location: Miami
  Temperature (C): 3.1
  Wind Speed (km/h): 12.6
- Condition: Rainy
  Day: Sunday
  Location: Los Angeles
  Temperature (C): 24.5
  Wind Speed (km/h): 29.9
- Condition: Sunny
  Day: Tuesday
  Location: New York
  Temperature (C): -3.1
  Wind Speed (km/h): 29.9
- Condition: Sunny
  Day: Sunday
  Location: Chicago
  Temperature (C): 23.9
  Wind Speed (km/h): 23.6
- Condition: Windy
  Day: Tuesday
  Location: Miami
  Temperature (C): 27.9
  Wind Speed (km/h): 12.6
- Condition: Foggy
  Day: Wednesday
  Location: Houston
  Temperature (C): 35.1
  Wind Speed (km/h): 19.3
- Condition: Rainy
  Day: Tuesday
  Location: Chicago
  Temperature (C): 19.1
  Wind Speed (km/h): 19.4
- Condition: Foggy
  Day: Monday
  Location: Houston
  Temperature (C): 34.1
  Wind Speed (km/h): 1.7
- Condition: Cloudy
  Day: Monday
  Location: Miami
  Temperature (C): 34.1
  Wind Speed (km/h): 10.6
- Condition: Cloudy
  Day: Sunday
  Location: Los Angeles
  Temperature (C): 1.9
  Wind Speed (km/h): 20.3
<start>
| Location | Condition | Temperature (C) | Wind Speed (km/h) | Day |
| --- | --- | --- | --- | --- |
| Miami | Stormy | 3.1 | 12.6 | Sunday |
| Los Angeles | Rainy | 24.5 | 29.9 | Sunday |
| New York | Sunny | -3.1 | 29.9 | Tuesday |
| Chicago | Sunny | 23.9 | 23.6 | Sunday |
| Miami | Windy | 27.9 | 12.6 | Tuesday |
| Houston | Foggy | 35.1 | 19.3 | Wednesday |
| Chicago | Rainy | 19.1 | 19.4 | Tuesday |
| Houston | Foggy | 34.1 | 1.7 | Monday |
| Miami | Cloudy | 34.1 | 10.6 | Monday |
| Los Angeles | Cloudy | 1.9 | 20.3 | Sunday |
<end>Please transform the following YML data into json:
- Director: Talon Blackthorn
  Genre: Adventure
  Release Year: 2014
- Director: Zara Stormrider
  Genre: Action
  Release Year: 2002
- Director: Aria Ravenwood
  Genre: Comedy
  Release Year: 1980
- Director: Orin Shadowalker
  Genre: Horror
  Release Year: 2006
- Director: Rylan Frostblade
  Genre: Fantasy
  Release Year: 1971
- Director: Zara Stormrider
  Genre: Action
  Release Year: 2010
- Director: Talon Blackthorn
  Genre: Adventure
  Release Year: 1971
<start>
[
    {
        "Director": "Talon Blackthorn",
        "Genre": "Adventure",
        "Release Year": 2014
    },
    {
        "Director": "Zara Stormrider",
        "Genre": "Action",
        "Release Year": 2002
    },
    {
        "Director": "Aria Ravenwood",
        "Genre": "Comedy",
        "Release Year": 1980
    },
    {
        "Director": "Orin Shadowalker",
        "Genre": "Horror",
        "Release Year": 2006
    },
    {
        "Director": "Rylan Frostblade",
        "Genre": "Fantasy",
        "Release Year": 1971
    },
    {
        "Director": "Zara Stormrider",
        "Genre": "Action",
        "Release Year": 2010
    },
    {
        "Director": "Talon Blackthorn",
        "Genre": "Adventure",
        "Release Year": 1971
    }
]
<end>Here's some PLAIN TEXT data, can you convert it to JSON?
Director: Aria Ravenwood | Genre: Fantasy
Director: Lira Silverleaf | Genre: Action
Director: Cade Firebrand | Genre: Horror
Director: Aria Ravenwood | Genre: Comedy
Director: Talon Blackthorn | Genre: Drama
Director: Lira Silverleaf | Genre: Drama
Director: Aria Ravenwood | Genre: Drama
Director: Rylan Frostblade | Genre: Fantasy
Director: Talon Blackthorn | Genre: Comedy
Director: Zara Stormrider | Genre: Thriller
<start>
[
    {
        "Director": "Aria Ravenwood",
        "Genre": "Fantasy"
    },
    {
        "Director": "Lira Silverleaf",
        "Genre": "Action"
    },
    {
        "Director": "Cade Firebrand",
        "Genre": "Horror"
    },
    {
        "Director": "Aria Ravenwood",
        "Genre": "Comedy"
    },
    {
        "Director": "Talon Blackthorn",
        "Genre": "Drama"
    },
    {
        "Director": "Lira Silverleaf",
        "Genre": "Drama"
    },
    {
        "Director": "Aria Ravenwood",
        "Genre": "Drama"
    },
    {
        "Director": "Rylan Frostblade",
        "Genre": "Fantasy"
    },
    {
        "Director": "Talon Blackthorn",
        "Genre": "Comedy"
    },
    {
        "Director": "Zara Stormrider",
        "Genre": "Thriller"
    }
]
<end>Can you change this MARKDOWN into csv?
| Open Price | Close Price | High Price | Low Price | Volume |
| --- | --- | --- | --- | --- |
| 750.36 | 660.59 | 750.36 | 660.59 | 9881829 |
| 361.84 | 750.36 | 750.36 | 361.84 | 8597065 |
| 885.68 | 1183.4 | 1183.4 | 885.68 | 762595 |
| 1246.29 | 902.0 | 1246.29 | 228.54 | 5354944 |
| 1484.46 | 753.25 | 1484.46 | 492.02 | 8675096 |
| 397.83 | 596.47 | 596.47 | 397.83 | 650976 |
| 561.44 | 167.7 | 694.9 | 167.7 | 5617555 |
| 881.17 | 1311.23 | 1335.0 | 881.17 | 8696106 |
| 302.61 | 1431.53 | 1431.53 | 302.61 | 650976 |
| 1482.79 | 1249.24 | 1482.79 | 660.59 | 5933291 |<start>
Open Price,Close Price,High Price,Low Price,Volume
750.36,660.59,750.36,660.59,9881829
361.84,750.36,750.36,361.84,8597065
885.68,1183.4,1183.4,885.68,762595
1246.29,902.0,1246.29,228.54,5354944
1484.46,753.25,1484.46,492.02,8675096
397.83,596.47,596.47,397.83,650976
561.44,167.7,694.9,167.7,5617555
881.17,1311.23,1335.0,881.17,8696106
302.61,1431.53,1431.53,302.61,650976
1482.79,1249.24,1482.79,660.59,5933291
<end>Transform this MARKDOWN structure to a YAML format:
| Condition | Wind Speed (km/h) | Day |
| --- | --- | --- |
| Stormy | 4.1 | Sunday |
| Windy | 1.3 | Monday |
| Stormy | 24.7 | Tuesday |
| Rainy | 2.3 | Wednesday |
| Windy | 6.1 | Sunday |<start>
- Condition: Stormy
  Day: Sunday
  Wind Speed (km/h): 4.1
- Condition: Windy
  Day: Monday
  Wind Speed (km/h): 1.3
- Condition: Stormy
  Day: Tuesday
  Wind Speed (km/h): 24.7
- Condition: Rainy
  Day: Wednesday
  Wind Speed (km/h): 2.3
- Condition: Windy
  Day: Sunday
  Wind Speed (km/h): 6.1
<end>Transform this YML structure to a plain text format:
- Battery Level (%): 26.2
  Device ID: device-0004
  Device Type: Temperature Sensor
  Reading Value: -27.52
- Battery Level (%): 93.0
  Device ID: device-0025
  Device Type: Pressure Sensor
  Reading Value: 32.68
- Battery Level (%): 78.3
  Device ID: device-0080
  Device Type: Temperature Sensor
  Reading Value: 32.68
- Battery Level (%): 42.8
  Device ID: device-0031
  Device Type: Temperature Sensor
  Reading Value: 64.15
- Battery Level (%): 93.2
  Device ID: device-0084
  Device Type: Humidity Sensor
  Reading Value: 47.63
<start>
Device ID: device-0004 | Device Type: Temperature Sensor | Battery Level (%): 26.2 | Reading Value: -27.52
Device ID: device-0025 | Device Type: Pressure Sensor | Battery Level (%): 93.0 | Reading Value: 32.68
Device ID: device-0080 | Device Type: Temperature Sensor | Battery Level (%): 78.3 | Reading Value: 32.68
Device ID: device-0031 | Device Type: Temperature Sensor | Battery Level (%): 42.8 | Reading Value: 64.15
Device ID: device-0084 | Device Type: Humidity Sensor | Battery Level (%): 93.2 | Reading Value: 47.63
<end>Transform this Csv structure to a json format:
Price,Stock Quantity,Category,Supplier Name
164.9,9,Electronics,Globex
153.4,100,Sports,Wayne Enterprises
319.0,225,Household,ACME Corp
10.29,354,Toys,Wayne Enterprises
434.97,233,Household,Wonka Industries
466.89,337,Sports,Wonka Industries
32.71,190,Electronics,Umbrella Corp
254.5,314,Toys,Umbrella Corp
<start>
[
    {
        "Price": 164.9,
        "Stock Quantity": 9,
        "Category": "Electronics",
        "Supplier Name": "Globex"
    },
    {
        "Price": 153.4,
        "Stock Quantity": 100,
        "Category": "Sports",
        "Supplier Name": "Wayne Enterprises"
    },
    {
        "Price": 319.0,
        "Stock Quantity": 225,
        "Category": "Household",
        "Supplier Name": "ACME Corp"
    },
    {
        "Price": 10.29,
        "Stock Quantity": 354,
        "Category": "Toys",
        "Supplier Name": "Wayne Enterprises"
    },
    {
        "Price": 434.97,
        "Stock Quantity": 233,
        "Category": "Household",
        "Supplier Name": "Wonka Industries"
    },
    {
        "Price": 466.89,
        "Stock Quantity": 337,
        "Category": "Sports",
        "Supplier Name": "Wonka Industries"
    },
    {
        "Price": 32.71,
        "Stock Quantity": 190,
        "Category": "Electronics",
        "Supplier Name": "Umbrella Corp"
    },
    {
        "Price": 254.5,
        "Stock Quantity": 314,
        "Category": "Toys",
        "Supplier Name": "Umbrella Corp"
    }
]
<end>Here's some csv data, can you convert it to yml?
Product Name,SKU,Stock Quantity,Category
Gizmo,SKU-1054,411,Automotive
Doohickey,SKU-1073,186,Electronics
Device,SKU-1059,122,Automotive
Widget,SKU-1068,38,Sports
Apparatus,SKU-1031,33,Electronics
Apparatus,SKU-1068,146,Household
Widget,SKU-1032,478,Electronics
Whatchamacallit,SKU-1029,343,Automotive
Gizmo,SKU-1089,113,Sports
Instrument,SKU-1020,212,Toys
<start>
- Category: Automotive
  Product Name: Gizmo
  SKU: SKU-1054
  Stock Quantity: 411
- Category: Electronics
  Product Name: Doohickey
  SKU: SKU-1073
  Stock Quantity: 186
- Category: Automotive
  Product Name: Device
  SKU: SKU-1059
  Stock Quantity: 122
- Category: Sports
  Product Name: Widget
  SKU: SKU-1068
  Stock Quantity: 38
- Category: Electronics
  Product Name: Apparatus
  SKU: SKU-1031
  Stock Quantity: 33
- Category: Household
  Product Name: Apparatus
  SKU: SKU-1068
  Stock Quantity: 146
- Category: Electronics
  Product Name: Widget
  SKU: SKU-1032
  Stock Quantity: 478
- Category: Automotive
  Product Name: Whatchamacallit
  SKU: SKU-1029
  Stock Quantity: 343
- Category: Sports
  Product Name: Gizmo
  SKU: SKU-1089
  Stock Quantity: 113
- Category: Toys
  Product Name: Instrument
  SKU: SKU-1020
  Stock Quantity: 212
<end>Transform this plain text structure to a json format:
Product Name: Doohickey | SKU: SKU-1089 | Stock Quantity: 172 | Category: Toys | Supplier Name: Globex
Product Name: Thingamajig | SKU: SKU-1067 | Stock Quantity: 125 | Category: Automotive | Supplier Name: Wonka Industries
Product Name: Contraption | SKU: SKU-1026 | Stock Quantity: 64 | Category: Electronics | Supplier Name: Wonka Industries
Product Name: Whatchamacallit | SKU: SKU-1068 | Stock Quantity: 203 | Category: Toys | Supplier Name: Globex
Product Name: Thingamajig | SKU: SKU-1082 | Stock Quantity: 268 | Category: Electronics | Supplier Name: Umbrella Corp
Product Name: Doohickey | SKU: SKU-1042 | Stock Quantity: 12 | Category: Household | Supplier Name: Umbrella Corp
Product Name: Thingamajig | SKU: SKU-1007 | Stock Quantity: 53 | Category: Sports | Supplier Name: Wayne Enterprises
Product Name: Instrument | SKU: SKU-1099 | Stock Quantity: 384 | Category: Household | Supplier Name: Wayne Enterprises
<start>
[
    {
        "Product Name": "Doohickey",
        "SKU": "SKU-1089",
        "Stock Quantity": 172,
        "Category": "Toys",
        "Supplier Name": "Globex"
    },
    {
        "Product Name": "Thingamajig",
        "SKU": "SKU-1067",
        "Stock Quantity": 125,
        "Category": "Automotive",
        "Supplier Name": "Wonka Industries"
    },
    {
        "Product Name": "Contraption",
        "SKU": "SKU-1026",
        "Stock Quantity": 64,
        "Category": "Electronics",
        "Supplier Name": "Wonka Industries"
    },
    {
        "Product Name": "Whatchamacallit",
        "SKU": "SKU-1068",
        "Stock Quantity": 203,
        "Category": "Toys",
        "Supplier Name": "Globex"
    },
    {
        "Product Name": "Thingamajig",
        "SKU": "SKU-1082",
        "Stock Quantity": 268,
        "Category": "Electronics",
        "Supplier Name": "Umbrella Corp"
    },
    {
        "Product Name": "Doohickey",
        "SKU": "SKU-1042",
        "Stock Quantity": 12,
        "Category": "Household",
        "Supplier Name": "Umbrella Corp"
    },
    {
        "Product Name": "Thingamajig",
        "SKU": "SKU-1007",
        "Stock Quantity": 53,
        "Category": "Sports",
        "Supplier Name": "Wayne Enterprises"
    },
    {
        "Product Name": "Instrument",
        "SKU": "SKU-1099",
        "Stock Quantity": 384,
        "Category": "Household",
        "Supplier Name": "Wayne Enterprises"
    }
]
<end>Here's some Yaml data, can you convert it to Markdown?
- Average Latency (ms): 66.49
  Database Name: OrdersDB
  Queries per Second: 1623.02
- Average Latency (ms): 66.49
  Database Name: LogsDB
  Queries per Second: 439.79
- Average Latency (ms): 15.66
  Database Name: MetricsDB
  Queries per Second: 4672.94
- Average Latency (ms): 20.82
  Database Name: SalesDB
  Queries per Second: 4045.03
- Average Latency (ms): 10.66
  Database Name: UserDB
  Queries per Second: 315.43
- Average Latency (ms): 40.79
  Database Name: SessionsDB
  Queries per Second: 1358.78
- Average Latency (ms): 81.57
  Database Name: SalesDB
  Queries per Second: 3851.82
- Average Latency (ms): 87.0
  Database Name: LogsDB
  Queries per Second: 4554.2
<start>
| Database Name | Queries per Second | Average Latency (ms) |
| --- | --- | --- |
| OrdersDB | 1623.02 | 66.49 |
| LogsDB | 439.79 | 66.49 |
| MetricsDB | 4672.94 | 15.66 |
| SalesDB | 4045.03 | 20.82 |
| UserDB | 315.43 | 10.66 |
| SessionsDB | 1358.78 | 40.79 |
| SalesDB | 3851.82 | 81.57 |
| LogsDB | 4554.2 | 87.0 |
<end>Convert this MARKDOWN to PLAIN TEXT:
| Title | Author | Genre | Publication Year | Rating |
| --- | --- | --- | --- | --- |
| Echoes of Eternity | Sylvia Nightshade | Horror | 2001 | 3.1 |
| Legends of the Rift | Orion Frostblade | Horror | 1996 | 2.8 |
| The Silent Grove | Elara Moonshadow | Fantasy | 1950 | 4.6 |
| A Journey Through Time | Kara Firebrand | Historical | 1966 | 1.4 |
| Echoes of Eternity | Orion Frostblade | Fantasy | 1962 | 4.1 |
| Tales of the Brave | Thorne Ironwood | Thriller | 1986 | 2.2 |
| Echoes of Eternity | Galen Starfire | Mystery | 2009 | 3.6 |
| The Forgotten World | Luna Silverleaf | Fantasy | 1979 | 3.0 |
| The Forgotten World | Sylvia Nightshade | Romance | 2007 | 1.5 |<start>
Title: Echoes of Eternity | Author: Sylvia Nightshade | Genre: Horror | Publication Year: 2001 | Rating: 3.1
Title: Legends of the Rift | Author: Orion Frostblade | Genre: Horror | Publication Year: 1996 | Rating: 2.8
Title: The Silent Grove | Author: Elara Moonshadow | Genre: Fantasy | Publication Year: 1950 | Rating: 4.6
Title: A Journey Through Time | Author: Kara Firebrand | Genre: Historical | Publication Year: 1966 | Rating: 1.4
Title: Echoes of Eternity | Author: Orion Frostblade | Genre: Fantasy | Publication Year: 1962 | Rating: 4.1
Title: Tales of the Brave | Author: Thorne Ironwood | Genre: Thriller | Publication Year: 1986 | Rating: 2.2
Title: Echoes of Eternity | Author: Galen Starfire | Genre: Mystery | Publication Year: 2009 | Rating: 3.6
Title: The Forgotten World | Author: Luna Silverleaf | Genre: Fantasy | Publication Year: 1979 | Rating: 3.0
Title: The Forgotten World | Author: Sylvia Nightshade | Genre: Romance | Publication Year: 2007 | Rating: 1.5
<end>Transform this csv structure to a YML format:
Genre,Publication Year
Fantasy,1976
Science Fiction,1986
Thriller,1991
Thriller,1956
Horror,2014
Science Fiction,2017
<start>
- Genre: Fantasy
  Publication Year: 1976
- Genre: Science Fiction
  Publication Year: 1986
- Genre: Thriller
  Publication Year: 1991
- Genre: Thriller
  Publication Year: 1956
- Genre: Horror
  Publication Year: 2014
- Genre: Science Fiction
  Publication Year: 2017
<end>Transform this YML structure to a MARKDOWN format:
- Cuisine: American
  Price Range: $$$
- Cuisine: American
  Price Range: $$$$$
- Cuisine: Mediterranean
  Price Range: $
- Cuisine: Chinese
  Price Range: $
- Cuisine: American
  Price Range: $
- Cuisine: Mexican
  Price Range: $
- Cuisine: Mediterranean
  Price Range: $$$$$
- Cuisine: Mexican
  Price Range: $$$$$
- Cuisine: Mexican
  Price Range: $$$
<start>
| Cuisine | Price Range |
| --- | --- |
| American | $$$ |
| American | $$$$$ |
| Mediterranean | $ |
| Chinese | $ |
| American | $ |
| Mexican | $ |
| Mediterranean | $$$$$ |
| Mexican | $$$$$ |
| Mexican | $$$ |
<end>Please transform the following MARKDOWN data into csv:
| Location | Condition | Temperature (C) | Humidity (%) | Wind Speed (km/h) | Day |
| --- | --- | --- | --- | --- | --- |
| Denver | Cloudy | 8.7 | 67 | 18.3 | Thursday |
| Phoenix | Windy | -6.8 | 91 | 0.6 | Thursday |
| Houston | Foggy | 39.9 | 63 | 1.3 | Friday |
| Phoenix | Snowy | 30.3 | 90 | 6.3 | Friday |<start>
Location,Condition,Temperature (C),Humidity (%),Wind Speed (km/h),Day
Denver,Cloudy,8.7,67,18.3,Thursday
Phoenix,Windy,-6.8,91,0.6,Thursday
Houston,Foggy,39.9,63,1.3,Friday
Phoenix,Snowy,30.3,90,6.3,Friday
<end>Can you change this json into markdown?
[
    {
        "Restaurant Name": "Taco Town",
        "Cuisine": "Italian",
        "Location": "New York",
        "Rating": 5,
        "Price Range": "$"
    },
    {
        "Restaurant Name": "Taco Town",
        "Cuisine": "American",
        "Location": "Phoenix",
        "Rating": 4,
        "Price Range": "$"
    },
    {
        "Restaurant Name": "Vegan Delight",
        "Cuisine": "Chinese",
        "Location": "Miami",
        "Rating": 5,
        "Price Range": "$"
    },
    {
        "Restaurant Name": "BBQ Barn",
        "Cuisine": "Indian",
        "Location": "San Francisco",
        "Rating": 2,
        "Price Range": "$$$"
    }
]<start>
| Restaurant Name | Cuisine | Location | Rating | Price Range |
| --- | --- | --- | --- | --- |
| Taco Town | Italian | New York | 5 | $ |
| Taco Town | American | Phoenix | 4 | $ |
| Vegan Delight | Chinese | Miami | 5 | $ |
| BBQ Barn | Indian | San Francisco | 2 | $$$ |
<end>Transform this JSON structure to a Markdown format:
[
    {
        "Queries per Second": 876.99,
        "Cache Hit Ratio (%)": 71.02,
        "Connection Count": 429,
        "Average Latency (ms)": 99.54,
        "Timestamp": "2021-08-17 06:12:38"
    },
    {
        "Queries per Second": 2247.39,
        "Cache Hit Ratio (%)": 77.65,
        "Connection Count": 24,
        "Average Latency (ms)": 88.37,
        "Timestamp": "2022-06-01 01:48:06"
    },
    {
        "Queries per Second": 3425.91,
        "Cache Hit Ratio (%)": 92.56,
        "Connection Count": 334,
        "Average Latency (ms)": 36.72,
        "Timestamp": "2021-11-20 14:32:15"
    },
    {
        "Queries per Second": 3097.51,
        "Cache Hit Ratio (%)": 75.2,
        "Connection Count": 357,
        "Average Latency (ms)": 21.49,
        "Timestamp": "2021-06-09 23:16:28"
    },
    {
        "Queries per Second": 2743.67,
        "Cache Hit Ratio (%)": 93.97,
        "Connection Count": 420,
        "Average Latency (ms)": 26.25,
        "Timestamp": "2022-11-04 13:30:30"
    },
    {
        "Queries per Second": 2226.0,
        "Cache Hit Ratio (%)": 97.21,
        "Connection Count": 432,
        "Average Latency (ms)": 3.69,
        "Timestamp": "2022-09-26 04:44:32"
    },
    {
        "Queries per Second": 4498.51,
        "Cache Hit Ratio (%)": 77.65,
        "Connection Count": 149,
        "Average Latency (ms)": 86.57,
        "Timestamp": "2023-10-23 11:34:26"
    },
    {
        "Queries per Second": 2247.39,
        "Cache Hit Ratio (%)": 85.89,
        "Connection Count": 354,
        "Average Latency (ms)": 72.06,
        "Timestamp": "2022-04-25 20:47:56"
    }
]<start>
| Queries per Second | Cache Hit Ratio (%) | Connection Count | Average Latency (ms) | Timestamp |
| --- | --- | --- | --- | --- |
| 876.99 | 71.02 | 429 | 99.54 | 2021-08-17 06:12:38 |
| 2247.39 | 77.65 | 24 | 88.37 | 2022-06-01 01:48:06 |
| 3425.91 | 92.56 | 334 | 36.72 | 2021-11-20 14:32:15 |
| 3097.51 | 75.2 | 357 | 21.49 | 2021-06-09 23:16:28 |
| 2743.67 | 93.97 | 420 | 26.25 | 2022-11-04 13:30:30 |
| 2226.0 | 97.21 | 432 | 3.69 | 2022-09-26 04:44:32 |
| 4498.51 | 77.65 | 149 | 86.57 | 2023-10-23 11:34:26 |
| 2247.39 | 85.89 | 354 | 72.06 | 2022-04-25 20:47:56 |
<end>Can you change this yml into csv?
- Director: Orin Shadowalker
  Release Year: 1998
  Title: The Final Voyage
- Director: Rylan Frostblade
  Release Year: 2018
  Title: Edge of Infinity
- Director: Lira Silverleaf
  Release Year: 1991
  Title: The Endless Horizon
- Director: Selene Darkwhisper
  Release Year: 2017
  Title: Starbound Odyssey
- Director: Lira Silverleaf
  Release Year: 2003
  Title: Beyond the Veil
- Director: Cade Firebrand
  Release Year: 1997
  Title: Dreamwalker
- Director: Zara Stormrider
  Release Year: 2003
  Title: Dreamwalker
<start>
Title,Director,Release Year
The Final Voyage,Orin Shadowalker,1998
Edge of Infinity,Rylan Frostblade,2018
The Endless Horizon,Lira Silverleaf,1991
Starbound Odyssey,Selene Darkwhisper,2017
Beyond the Veil,Lira Silverleaf,2003
Dreamwalker,Cade Firebrand,1997
Dreamwalker,Zara Stormrider,2003
<end>Can you change this JSON into Plain text?
[
    {
        "Database Name": "SalesDB",
        "Queries per Second": 1608.73,
        "Cache Hit Ratio (%)": 82.42,
        "Connection Count": 416
    },
    {
        "Database Name": "SalesDB",
        "Queries per Second": 4490.07,
        "Cache Hit Ratio (%)": 82.42,
        "Connection Count": 417
    },
    {
        "Database Name": "AnalyticsDB",
        "Queries per Second": 905.47,
        "Cache Hit Ratio (%)": 90.04,
        "Connection Count": 483
    },
    {
        "Database Name": "ProductsDB",
        "Queries per Second": 4554.29,
        "Cache Hit Ratio (%)": 75.41,
        "Connection Count": 200
    },
    {
        "Database Name": "OrdersDB",
        "Queries per Second": 2373.26,
        "Cache Hit Ratio (%)": 90.04,
        "Connection Count": 424
    },
    {
        "Database Name": "LogsDB",
        "Queries per Second": 4516.94,
        "Cache Hit Ratio (%)": 81.5,
        "Connection Count": 483
    },
    {
        "Database Name": "SalesDB",
        "Queries per Second": 1099.57,
        "Cache Hit Ratio (%)": 74.35,
        "Connection Count": 233
    },
    {
        "Database Name": "OrdersDB",
        "Queries per Second": 3048.43,
        "Cache Hit Ratio (%)": 97.07,
        "Connection Count": 129
    },
    {
        "Database Name": "AnalyticsDB",
        "Queries per Second": 1679.65,
        "Cache Hit Ratio (%)": 71.91,
        "Connection Count": 417
    }
]<start>
Database Name: SalesDB | Queries per Second: 1608.73 | Cache Hit Ratio (%): 82.42 | Connection Count: 416
Database Name: SalesDB | Queries per Second: 4490.07 | Cache Hit Ratio (%): 82.42 | Connection Count: 417
Database Name: AnalyticsDB | Queries per Second: 905.47 | Cache Hit Ratio (%): 90.04 | Connection Count: 483
Database Name: ProductsDB | Queries per Second: 4554.29 | Cache Hit Ratio (%): 75.41 | Connection Count: 200
Database Name: OrdersDB | Queries per Second: 2373.26 | Cache Hit Ratio (%): 90.04 | Connection Count: 424
Database Name: LogsDB | Queries per Second: 4516.94 | Cache Hit Ratio (%): 81.5 | Connection Count: 483
Database Name: SalesDB | Queries per Second: 1099.57 | Cache Hit Ratio (%): 74.35 | Connection Count: 233
Database Name: OrdersDB | Queries per Second: 3048.43 | Cache Hit Ratio (%): 97.07 | Connection Count: 129
Database Name: AnalyticsDB | Queries per Second: 1679.65 | Cache Hit Ratio (%): 71.91 | Connection Count: 417
<end>Please transform the following plain text data into JSON:
Director: Drake Nightshade | Genre: Comedy
Director: Lira Silverleaf | Genre: Sci-Fi
Director: Selene Darkwhisper | Genre: Horror
Director: Mara Moonshadow | Genre: Action
Director: Aria Ravenwood | Genre: Fantasy
Director: Zara Stormrider | Genre: Comedy
Director: Rylan Frostblade | Genre: Comedy
Director: Talon Blackthorn | Genre: Sci-Fi
<start>
[
    {
        "Director": "Drake Nightshade",
        "Genre": "Comedy"
    },
    {
        "Director": "Lira Silverleaf",
        "Genre": "Sci-Fi"
    },
    {
        "Director": "Selene Darkwhisper",
        "Genre": "Horror"
    },
    {
        "Director": "Mara Moonshadow",
        "Genre": "Action"
    },
    {
        "Director": "Aria Ravenwood",
        "Genre": "Fantasy"
    },
    {
        "Director": "Zara Stormrider",
        "Genre": "Comedy"
    },
    {
        "Director": "Rylan Frostblade",
        "Genre": "Comedy"
    },
    {
        "Director": "Talon Blackthorn",
        "Genre": "Sci-Fi"
    }
]
<end>Here's some plain text data, can you convert it to markdown?
Start Location: Chicago | End Location: Denver | Distance (miles): 402.6 | Duration (hours): 6.4
Start Location: Miami | End Location: Denver | Distance (miles): 2520.0 | Duration (hours): 54.5
Start Location: Los Angeles | End Location: San Francisco | Distance (miles): 1461.1 | Duration (hours): 18.3
Start Location: New York | End Location: Miami | Distance (miles): 2594.0 | Duration (hours): 48.4
Start Location: Los Angeles | End Location: Chicago | Distance (miles): 1152.7 | Duration (hours): 17.2
Start Location: Denver | End Location: New York | Distance (miles): 1736.4 | Duration (hours): 17.2
Start Location: New York | End Location: Chicago | Distance (miles): 1063.8 | Duration (hours): 32.7
Start Location: Los Angeles | End Location: San Francisco | Distance (miles): 2025.9 | Duration (hours): 43.1
Start Location: Miami | End Location: San Francisco | Distance (miles): 244.9 | Duration (hours): 69.9
<start>
| Start Location | End Location | Distance (miles) | Duration (hours) |
| --- | --- | --- | --- |
| Chicago | Denver | 402.6 | 6.4 |
| Miami | Denver | 2520.0 | 54.5 |
| Los Angeles | San Francisco | 1461.1 | 18.3 |
| New York | Miami | 2594.0 | 48.4 |
| Los Angeles | Chicago | 1152.7 | 17.2 |
| Denver | New York | 1736.4 | 17.2 |
| New York | Chicago | 1063.8 | 32.7 |
| Los Angeles | San Francisco | 2025.9 | 43.1 |
| Miami | San Francisco | 244.9 | 69.9 |
<end>Here's some plain text data, can you convert it to Yml?
Genre: Science Fiction | Publication Year: 1958
Genre: Science Fiction | Publication Year: 1958
Genre: Historical | Publication Year: 1965
Genre: Fantasy | Publication Year: 1992
Genre: Mystery | Publication Year: 2006
Genre: Horror | Publication Year: 1951
Genre: Fantasy | Publication Year: 1978
Genre: Science Fiction | Publication Year: 1977
<start>
- Genre: Science Fiction
  Publication Year: 1958
- Genre: Science Fiction
  Publication Year: 1958
- Genre: Historical
  Publication Year: 1965
- Genre: Fantasy
  Publication Year: 1992
- Genre: Mystery
  Publication Year: 2006
- Genre: Horror
  Publication Year: 1951
- Genre: Fantasy
  Publication Year: 1978
- Genre: Science Fiction
  Publication Year: 1977
<end>Can you change this JSON into CSV?
[
    {
        "SKU": "SKU-1065",
        "Price": 383.2,
        "Stock Quantity": 168,
        "Category": "Household"
    },
    {
        "SKU": "SKU-1026",
        "Price": 419.87,
        "Stock Quantity": 270,
        "Category": "Toys"
    },
    {
        "SKU": "SKU-1099",
        "Price": 277.86,
        "Stock Quantity": 344,
        "Category": "Sports"
    },
    {
        "SKU": "SKU-1039",
        "Price": 457.64,
        "Stock Quantity": 330,
        "Category": "Toys"
    },
    {
        "SKU": "SKU-1031",
        "Price": 359.32,
        "Stock Quantity": 347,
        "Category": "Household"
    },
    {
        "SKU": "SKU-1080",
        "Price": 107.02,
        "Stock Quantity": 492,
        "Category": "Household"
    },
    {
        "SKU": "SKU-1028",
        "Price": 450.74,
        "Stock Quantity": 471,
        "Category": "Sports"
    },
    {
        "SKU": "SKU-1083",
        "Price": 83.26,
        "Stock Quantity": 84,
        "Category": "Sports"
    },
    {
        "SKU": "SKU-1084",
        "Price": 429.51,
        "Stock Quantity": 100,
        "Category": "Toys"
    }
]<start>
SKU,Price,Stock Quantity,Category
SKU-1065,383.2,168,Household
SKU-1026,419.87,270,Toys
SKU-1099,277.86,344,Sports
SKU-1039,457.64,330,Toys
SKU-1031,359.32,347,Household
SKU-1080,107.02,492,Household
SKU-1028,450.74,471,Sports
SKU-1083,83.26,84,Sports
SKU-1084,429.51,100,Toys
<end>Transform this plain text structure to a csv format:
Company: MediaGroup | Open Price: 1274.91 | High Price: 1274.91 | Volume: 7675438
Company: MediaGroup | Open Price: 1050.54 | High Price: 1423.45 | Volume: 2000559
Company: FinanceTrust | Open Price: 1393.31 | High Price: 1393.31 | Volume: 9057378
Company: FoodChain | Open Price: 1386.93 | High Price: 1386.93 | Volume: 2630372
Company: TechnoCorp | Open Price: 1364.02 | High Price: 1364.02 | Volume: 9675970
Company: FinanceTrust | Open Price: 10.53 | High Price: 1296.24 | Volume: 6368421
Company: HealthGen | Open Price: 1224.82 | High Price: 1224.82 | Volume: 7458333
Company: FinanceTrust | Open Price: 670.13 | High Price: 1003.79 | Volume: 686042
Company: MediaGroup | Open Price: 1423.45 | High Price: 1423.45 | Volume: 5053661
<start>
Company,Open Price,High Price,Volume
MediaGroup,1274.91,1274.91,7675438
MediaGroup,1050.54,1423.45,2000559
FinanceTrust,1393.31,1393.31,9057378
FoodChain,1386.93,1386.93,2630372
TechnoCorp,1364.02,1364.02,9675970
FinanceTrust,10.53,1296.24,6368421
HealthGen,1224.82,1224.82,7458333
FinanceTrust,670.13,1003.79,686042
MediaGroup,1423.45,1423.45,5053661
<end>Please transform the following json data into plain text:
[
    {
        "Company": "GreenEnergy",
        "Date": "2023-05-15",
        "Close Price": 666.41,
        "High Price": 1069.87,
        "Low Price": 666.41
    },
    {
        "Company": "RetailWorld",
        "Date": "2019-08-25",
        "Close Price": 996.36,
        "High Price": 1166.75,
        "Low Price": 996.36
    },
    {
        "Company": "BioLife",
        "Date": "2015-01-14",
        "Close Price": 521.63,
        "High Price": 842.39,
        "Low Price": 401.77
    },
    {
        "Company": "FinanceTrust",
        "Date": "2010-08-08",
        "Close Price": 842.39,
        "High Price": 1463.78,
        "Low Price": 528.56
    },
    {
        "Company": "GreenEnergy",
        "Date": "2021-01-04",
        "Close Price": 1432.6,
        "High Price": 1432.6,
        "Low Price": 185.03
    },
    {
        "Company": "BioLife",
        "Date": "2023-05-27",
        "Close Price": 288.38,
        "High Price": 1276.6,
        "Low Price": 22.32
    },
    {
        "Company": "TechnoCorp",
        "Date": "2019-04-25",
        "Close Price": 16.77,
        "High Price": 726.73,
        "Low Price": 16.77
    },
    {
        "Company": "FoodChain",
        "Date": "2018-03-10",
        "Close Price": 1472.26,
        "High Price": 1472.26,
        "Low Price": 521.63
    }
]<start>
Company: GreenEnergy | Date: 2023-05-15 | Close Price: 666.41 | High Price: 1069.87 | Low Price: 666.41
Company: RetailWorld | Date: 2019-08-25 | Close Price: 996.36 | High Price: 1166.75 | Low Price: 996.36
Company: BioLife | Date: 2015-01-14 | Close Price: 521.63 | High Price: 842.39 | Low Price: 401.77
Company: FinanceTrust | Date: 2010-08-08 | Close Price: 842.39 | High Price: 1463.78 | Low Price: 528.56
Company: GreenEnergy | Date: 2021-01-04 | Close Price: 1432.6 | High Price: 1432.6 | Low Price: 185.03
Company: BioLife | Date: 2023-05-27 | Close Price: 288.38 | High Price: 1276.6 | Low Price: 22.32
Company: TechnoCorp | Date: 2019-04-25 | Close Price: 16.77 | High Price: 726.73 | Low Price: 16.77
Company: FoodChain | Date: 2018-03-10 | Close Price: 1472.26 | High Price: 1472.26 | Low Price: 521.63
<end>Please transform the following CSV data into markdown:
Title,Genre,Release Year
Edge of Infinity,Sci-Fi,2006
Beyond the Veil,Thriller,2002
Starbound Odyssey,Comedy,2023
Dreamwalker,Horror,2022
<start>
| Title | Genre | Release Year |
| --- | --- | --- |
| Edge of Infinity | Sci-Fi | 2006 |
| Beyond the Veil | Thriller | 2002 |
| Starbound Odyssey | Comedy | 2023 |
| Dreamwalker | Horror | 2022 |
<end>Transform this json structure to a markdown format:
[
    {
        "Company": "FinanceTrust",
        "Date": "2023-01-03",
        "Close Price": 433.65,
        "High Price": 433.65,
        "Volume": 7983585
    },
    {
        "Company": "BioLife",
        "Date": "2014-10-16",
        "Close Price": 923.86,
        "High Price": 923.86,
        "Volume": 8225185
    },
    {
        "Company": "AeroSystems",
        "Date": "2010-09-12",
        "Close Price": 31.26,
        "High Price": 818.16,
        "Volume": 1946807
    },
    {
        "Company": "RetailWorld",
        "Date": "2016-08-20",
        "Close Price": 136.22,
        "High Price": 589.04,
        "Volume": 840997
    },
    {
        "Company": "FinanceTrust",
        "Date": "2019-03-18",
        "Close Price": 817.91,
        "High Price": 817.91,
        "Volume": 5423497
    },
    {
        "Company": "RetailWorld",
        "Date": "2019-08-20",
        "Close Price": 18.47,
        "High Price": 1175.95,
        "Volume": 6977093
    }
]<start>
| Company | Date | Close Price | High Price | Volume |
| --- | --- | --- | --- | --- |
| FinanceTrust | 2023-01-03 | 433.65 | 433.65 | 7983585 |
| BioLife | 2014-10-16 | 923.86 | 923.86 | 8225185 |
| AeroSystems | 2010-09-12 | 31.26 | 818.16 | 1946807 |
| RetailWorld | 2016-08-20 | 136.22 | 589.04 | 840997 |
| FinanceTrust | 2019-03-18 | 817.91 | 817.91 | 5423497 |
| RetailWorld | 2019-08-20 | 18.47 | 1175.95 | 6977093 |
<end>Please transform the following markdown data into plain text:
| Device ID | Device Type | Battery Level (%) | Reading Value | Timestamp |
| --- | --- | --- | --- | --- |
| device-0038 | Light Sensor | 21.8 | 79.81 | 2021-04-11 02:28:48 |
| device-0012 | Light Sensor | 73.0 | 69.01 | 2023-12-02 13:42:54 |
| device-0015 | Humidity Sensor | 67.1 | 6.11 | 2022-10-13 05:52:49 |<start>
Device ID: device-0038 | Device Type: Light Sensor | Battery Level (%): 21.8 | Reading Value: 79.81 | Timestamp: 2021-04-11 02:28:48
Device ID: device-0012 | Device Type: Light Sensor | Battery Level (%): 73.0 | Reading Value: 69.01 | Timestamp: 2023-12-02 13:42:54
Device ID: device-0015 | Device Type: Humidity Sensor | Battery Level (%): 67.1 | Reading Value: 6.11 | Timestamp: 2022-10-13 05:52:49
<end>Please transform the following markdown data into Csv:
| Device ID | Device Type | Reading Value |
| --- | --- | --- |
| device-0052 | Light Sensor | -19.91 |
| device-0078 | Temperature Sensor | 14.16 |
| device-0061 | Pressure Sensor | 80.42 |
| device-0076 | Light Sensor | 26.05 |
| device-0064 | Pressure Sensor | 76.11 |
| device-0070 | Pressure Sensor | 80.42 |
| device-0014 | Temperature Sensor | 29.77 |
| device-0084 | Light Sensor | 8.78 |
| device-0026 | Humidity Sensor | -39.67 |
| device-0089 | Humidity Sensor | -3.81 |<start>
Device ID,Device Type,Reading Value
device-0052,Light Sensor,-19.91
device-0078,Temperature Sensor,14.16
device-0061,Pressure Sensor,80.42
device-0076,Light Sensor,26.05
device-0064,Pressure Sensor,76.11
device-0070,Pressure Sensor,80.42
device-0014,Temperature Sensor,29.77
device-0084,Light Sensor,8.78
device-0026,Humidity Sensor,-39.67
device-0089,Humidity Sensor,-3.81
<end>Transform this MARKDOWN structure to a YAML format:
| Restaurant Name | Cuisine | Rating | Price Range |
| --- | --- | --- | --- |
| BBQ Barn | Mediterranean | 4 | $ |
| Pasta Palace | American | 1 | $$$ |
| Vegan Delight | Mediterranean | 2 | $$$ |
| Curry Corner | Indian | 2 | $ |
| Vegan Delight | American | 2 | $$$ |
| Curry Corner | Indian | 4 | $$$ |
| Vegan Delight | Chinese | 3 | $ |
| The Steakhouse | French | 1 | $$$ |<start>
- Cuisine: Mediterranean
  Price Range: $
  Rating: 4
  Restaurant Name: BBQ Barn
- Cuisine: American
  Price Range: $$$
  Rating: 1
  Restaurant Name: Pasta Palace
- Cuisine: Mediterranean
  Price Range: $$$
  Rating: 2
  Restaurant Name: Vegan Delight
- Cuisine: Indian
  Price Range: $
  Rating: 2
  Restaurant Name: Curry Corner
- Cuisine: American
  Price Range: $$$
  Rating: 2
  Restaurant Name: Vegan Delight
- Cuisine: Indian
  Price Range: $$$
  Rating: 4
  Restaurant Name: Curry Corner
- Cuisine: Chinese
  Price Range: $
  Rating: 3
  Restaurant Name: Vegan Delight
- Cuisine: French
  Price Range: $$$
  Rating: 1
  Restaurant Name: The Steakhouse
<end>Here's some CSV data, can you convert it to JSON?
Trip Name,End Location,Distance (miles),Duration (hours),Fuel Used (gallons)
Highway Odyssey,Los Angeles,2816.5,1.5,23.6
Coast to Coast,Phoenix,1658.0,34.7,71.9
Canyon Trek,Phoenix,2481.5,10.1,30.4
Canyon Trek,Phoenix,413.9,25.4,63.7
<start>
[
    {
        "Trip Name": "Highway Odyssey",
        "End Location": "Los Angeles",
        "Distance (miles)": 2816.5,
        "Duration (hours)": 1.5,
        "Fuel Used (gallons)": 23.6
    },
    {
        "Trip Name": "Coast to Coast",
        "End Location": "Phoenix",
        "Distance (miles)": 1658.0,
        "Duration (hours)": 34.7,
        "Fuel Used (gallons)": 71.9
    },
    {
        "Trip Name": "Canyon Trek",
        "End Location": "Phoenix",
        "Distance (miles)": 2481.5,
        "Duration (hours)": 10.1,
        "Fuel Used (gallons)": 30.4
    },
    {
        "Trip Name": "Canyon Trek",
        "End Location": "Phoenix",
        "Distance (miles)": 413.9,
        "Duration (hours)": 25.4,
        "Fuel Used (gallons)": 63.7
    }
]
<end>Convert this YAML to Plain text:
- Distance (miles): 2149.0
  Duration (hours): 44.7
  End Location: Los Angeles
  Fuel Used (gallons): 13.6
- Distance (miles): 2389.1
  Duration (hours): 19.8
  End Location: Los Angeles
  Fuel Used (gallons): 37.5
- Distance (miles): 1507.1
  Duration (hours): 47.3
  End Location: Chicago
  Fuel Used (gallons): 76.0
- Distance (miles): 2736.4
  Duration (hours): 10.2
  End Location: Los Angeles
  Fuel Used (gallons): 87.2
- Distance (miles): 1758.0
  Duration (hours): 15.7
  End Location: Phoenix
  Fuel Used (gallons): 90.5
- Distance (miles): 2956.5
  Duration (hours): 1.4
  End Location: New York
  Fuel Used (gallons): 17.6
- Distance (miles): 2749.4
  Duration (hours): 29.6
  End Location: New York
  Fuel Used (gallons): 97.6
- Distance (miles): 848.0
  Duration (hours): 13.2
  End Location: San Francisco
  Fuel Used (gallons): 83.0
<start>
End Location: Los Angeles | Distance (miles): 2149.0 | Duration (hours): 44.7 | Fuel Used (gallons): 13.6
End Location: Los Angeles | Distance (miles): 2389.1 | Duration (hours): 19.8 | Fuel Used (gallons): 37.5
End Location: Chicago | Distance (miles): 1507.1 | Duration (hours): 47.3 | Fuel Used (gallons): 76.0
End Location: Los Angeles | Distance (miles): 2736.4 | Duration (hours): 10.2 | Fuel Used (gallons): 87.2
End Location: Phoenix | Distance (miles): 1758.0 | Duration (hours): 15.7 | Fuel Used (gallons): 90.5
End Location: New York | Distance (miles): 2956.5 | Duration (hours): 1.4 | Fuel Used (gallons): 17.6
End Location: New York | Distance (miles): 2749.4 | Duration (hours): 29.6 | Fuel Used (gallons): 97.6
End Location: San Francisco | Distance (miles): 848.0 | Duration (hours): 13.2 | Fuel Used (gallons): 83.0
<end>Here's some Json data, can you convert it to Markdown?
[
    {
        "Device ID": "device-0036",
        "Device Type": "Pressure Sensor",
        "Timestamp": "2021-03-06 01:10:10"
    },
    {
        "Device ID": "device-0088",
        "Device Type": "Pressure Sensor",
        "Timestamp": "2021-08-25 14:43:59"
    },
    {
        "Device ID": "device-0081",
        "Device Type": "Pressure Sensor",
        "Timestamp": "2023-06-04 12:12:03"
    }
]<start>
| Device ID | Device Type | Timestamp |
| --- | --- | --- |
| device-0036 | Pressure Sensor | 2021-03-06 01:10:10 |
| device-0088 | Pressure Sensor | 2021-08-25 14:43:59 |
| device-0081 | Pressure Sensor | 2023-06-04 12:12:03 |
<end>Can you change this yaml into CSV?
- Close Price: 512.91
  Company: GreenEnergy
  Date: '2019-03-13'
  High Price: 1478.39
  Volume: 4357714
- Close Price: 178.92
  Company: TechnoCorp
  Date: '2022-06-23'
  High Price: 978.54
  Volume: 2410294
- Close Price: 893.56
  Company: MediaGroup
  Date: '2022-10-16'
  High Price: 893.56
  Volume: 2117957
- Close Price: 1190.8
  Company: BioLife
  Date: '2013-02-08'
  High Price: 1243.52
  Volume: 1516148
- Close Price: 720.23
  Company: BioLife
  Date: '2011-11-08'
  High Price: 936.86
  Volume: 3509830
- Close Price: 100.74
  Company: GreenEnergy
  Date: '2015-02-25'
  High Price: 1294.73
  Volume: 3054659
- Close Price: 886.87
  Company: RetailWorld
  Date: '2010-05-23'
  High Price: 1190.8
  Volume: 9993187
- Close Price: 59.72
  Company: HealthGen
  Date: '2012-01-01'
  High Price: 851.91
  Volume: 3449630
- Close Price: 886.87
  Company: MediaGroup
  Date: '2023-08-07'
  High Price: 886.87
  Volume: 1516148
<start>
Company,Date,Close Price,High Price,Volume
GreenEnergy,2019-03-13,512.91,1478.39,4357714
TechnoCorp,2022-06-23,178.92,978.54,2410294
MediaGroup,2022-10-16,893.56,893.56,2117957
BioLife,2013-02-08,1190.8,1243.52,1516148
BioLife,2011-11-08,720.23,936.86,3509830
GreenEnergy,2015-02-25,100.74,1294.73,3054659
RetailWorld,2010-05-23,886.87,1190.8,9993187
HealthGen,2012-01-01,59.72,851.91,3449630
MediaGroup,2023-08-07,886.87,886.87,1516148
<end>Here's some CSV data, can you convert it to Markdown?
Company,Market Cap,Stock Price
FinanceWorks,Large Cap,774.36
HealthPlus,Mid Cap,468.5
EcoEnergy,Small Cap,408.58
HealthPlus,Mega Cap,209.22
RetailHub,Large Cap,495.68
BioPharm,Large Cap,192.31
BioPharm,Small Cap,441.13
RetailHub,Small Cap,898.13
<start>
| Company | Market Cap | Stock Price |
| --- | --- | --- |
| FinanceWorks | Large Cap | 774.36 |
| HealthPlus | Mid Cap | 468.5 |
| EcoEnergy | Small Cap | 408.58 |
| HealthPlus | Mega Cap | 209.22 |
| RetailHub | Large Cap | 495.68 |
| BioPharm | Large Cap | 192.31 |
| BioPharm | Small Cap | 441.13 |
| RetailHub | Small Cap | 898.13 |
<end>Please transform the following Plain text data into JSON:
Device ID: device-0094 | Device Type: Light Sensor | Location: Office | Battery Level (%): 88.7 | Reading Value: 8.09 | Timestamp: 2021-08-28 23:46:25
Device ID: device-0076 | Device Type: Temperature Sensor | Location: Bathroom | Battery Level (%): 29.9 | Reading Value: 39.16 | Timestamp: 2022-08-21 02:05:57
Device ID: device-0079 | Device Type: Humidity Sensor | Location: Living Room | Battery Level (%): 86.2 | Reading Value: 46.25 | Timestamp: 2022-03-11 04:35:26
Device ID: device-0090 | Device Type: Humidity Sensor | Location: Kitchen | Battery Level (%): 28.7 | Reading Value: -16.95 | Timestamp: 2022-06-16 10:35:34
<start>
[
    {
        "Device ID": "device-0094",
        "Device Type": "Light Sensor",
        "Location": "Office",
        "Battery Level (%)": 88.7,
        "Reading Value": 8.09,
        "Timestamp": "2021-08-28 23:46:25"
    },
    {
        "Device ID": "device-0076",
        "Device Type": "Temperature Sensor",
        "Location": "Bathroom",
        "Battery Level (%)": 29.9,
        "Reading Value": 39.16,
        "Timestamp": "2022-08-21 02:05:57"
    },
    {
        "Device ID": "device-0079",
        "Device Type": "Humidity Sensor",
        "Location": "Living Room",
        "Battery Level (%)": 86.2,
        "Reading Value": 46.25,
        "Timestamp": "2022-03-11 04:35:26"
    },
    {
        "Device ID": "device-0090",
        "Device Type": "Humidity Sensor",
        "Location": "Kitchen",
        "Battery Level (%)": 28.7,
        "Reading Value": -16.95,
        "Timestamp": "2022-06-16 10:35:34"
    }
]
<end>Transform this PLAIN TEXT structure to a YAML format:
Director: Selene Darkwhisper | Genre: Comedy | Box Office Earnings (M): 984.19
Director: Lira Silverleaf | Genre: Adventure | Box Office Earnings (M): 196.9
Director: Drake Nightshade | Genre: Comedy | Box Office Earnings (M): 954.91
Director: Zara Stormrider | Genre: Horror | Box Office Earnings (M): 667.01
Director: Selene Darkwhisper | Genre: Horror | Box Office Earnings (M): 261.26
Director: Talon Blackthorn | Genre: Sci-Fi | Box Office Earnings (M): 453.44
<start>
- Box Office Earnings (M): 984.19
  Director: Selene Darkwhisper
  Genre: Comedy
- Box Office Earnings (M): 196.9
  Director: Lira Silverleaf
  Genre: Adventure
- Box Office Earnings (M): 954.91
  Director: Drake Nightshade
  Genre: Comedy
- Box Office Earnings (M): 667.01
  Director: Zara Stormrider
  Genre: Horror
- Box Office Earnings (M): 261.26
  Director: Selene Darkwhisper
  Genre: Horror
- Box Office Earnings (M): 453.44
  Director: Talon Blackthorn
  Genre: Sci-Fi
<end>Transform this Json structure to a csv format:
[
    {
        "Name": "Estelle",
        "Age": 46,
        "City": "Boston"
    },
    {
        "Name": "Paul",
        "Age": 32,
        "City": "Baltimore"
    },
    {
        "Name": "Lewis",
        "Age": 25,
        "City": "San Diego"
    },
    {
        "Name": "Emmett",
        "Age": 58,
        "City": "Portland"
    },
    {
        "Name": "Carson",
        "Age": 36,
        "City": "Dallas"
    },
    {
        "Name": "Lola",
        "Age": 54,
        "City": "San Antonio"
    },
    {
        "Name": "Harry",
        "Age": 26,
        "City": "El Paso"
    },
    {
        "Name": "Mark",
        "Age": 18,
        "City": "Houston"
    },
    {
        "Name": "Garrett",
        "Age": 26,
        "City": "Austin"
    },
    {
        "Name": "Willow",
        "Age": 47,
        "City": "Charlotte"
    }
]<start>
Name,Age,City
Estelle,46,Boston
Paul,32,Baltimore
Lewis,25,San Diego
Emmett,58,Portland
Carson,36,Dallas
Lola,54,San Antonio
Harry,26,El Paso
Mark,18,Houston
Garrett,26,Austin
Willow,47,Charlotte
<end>Here's some csv data, can you convert it to plain text?
Location,Condition,Temperature (C),Humidity (%),Wind Speed (km/h),Day
Chicago,Foggy,17.4,71,28.4,Wednesday
Phoenix,Cloudy,12.0,56,2.5,Thursday
Denver,Stormy,-9.8,28,0.3,Tuesday
Miami,Windy,-6.5,92,13.9,Monday
Chicago,Sunny,-6.0,33,29.4,Wednesday
Phoenix,Stormy,-0.4,60,16.2,Thursday
<start>
Location: Chicago | Condition: Foggy | Temperature (C): 17.4 | Humidity (%): 71 | Wind Speed (km/h): 28.4 | Day: Wednesday
Location: Phoenix | Condition: Cloudy | Temperature (C): 12.0 | Humidity (%): 56 | Wind Speed (km/h): 2.5 | Day: Thursday
Location: Denver | Condition: Stormy | Temperature (C): -9.8 | Humidity (%): 28 | Wind Speed (km/h): 0.3 | Day: Tuesday
Location: Miami | Condition: Windy | Temperature (C): -6.5 | Humidity (%): 92 | Wind Speed (km/h): 13.9 | Day: Monday
Location: Chicago | Condition: Sunny | Temperature (C): -6.0 | Humidity (%): 33 | Wind Speed (km/h): 29.4 | Day: Wednesday
Location: Phoenix | Condition: Stormy | Temperature (C): -0.4 | Humidity (%): 60 | Wind Speed (km/h): 16.2 | Day: Thursday
<end>Here's some yaml data, can you convert it to markdown?
- Device Type: Light Sensor
  Location: Hallway
  Timestamp: '2021-03-25 10:08:12'
- Device Type: Light Sensor
  Location: Garden
  Timestamp: '2021-07-12 09:28:58'
- Device Type: Temperature Sensor
  Location: Garden
  Timestamp: '2021-08-01 09:49:42'
- Device Type: Humidity Sensor
  Location: Kitchen
  Timestamp: '2023-07-12 15:59:26'
- Device Type: Pressure Sensor
  Location: Hallway
  Timestamp: '2021-03-12 04:25:51'
<start>
| Device Type | Location | Timestamp |
| --- | --- | --- |
| Light Sensor | Hallway | 2021-03-25 10:08:12 |
| Light Sensor | Garden | 2021-07-12 09:28:58 |
| Temperature Sensor | Garden | 2021-08-01 09:49:42 |
| Humidity Sensor | Kitchen | 2023-07-12 15:59:26 |
| Pressure Sensor | Hallway | 2021-03-12 04:25:51 |
<end>Here's some YAML data, can you convert it to MARKDOWN?
- Age: 23
  Birth Month: October
  City: Indianapolis
  Income: 45000
  Name: Roscoe
- Age: 26
  Birth Month: December
  City: San Francisco
  Income: 445000
  Name: Claude
- Age: 26
  Birth Month: December
  City: San Francisco
  Income: 230000
  Name: Jon
- Age: 20
  Birth Month: March
  City: Phoenix
  Income: 430000
  Name: Jay
- Age: 40
  Birth Month: April
  City: El Paso
  Income: 50000
  Name: Celia
- Age: 44
  Birth Month: October
  City: Louisville
  Income: 195000
  Name: Claude
- Age: 67
  Birth Month: September
  City: Washington
  Income: 230000
  Name: Gwendolyn
- Age: 38
  Birth Month: January
  City: Charlotte
  Income: 190000
  Name: Angel
<start>
| Name | Age | Birth Month | City | Income |
| --- | --- | --- | --- | --- |
| Roscoe | 23 | October | Indianapolis | 45000 |
| Claude | 26 | December | San Francisco | 445000 |
| Jon | 26 | December | San Francisco | 230000 |
| Jay | 20 | March | Phoenix | 430000 |
| Celia | 40 | April | El Paso | 50000 |
| Claude | 44 | October | Louisville | 195000 |
| Gwendolyn | 67 | September | Washington | 230000 |
| Angel | 38 | January | Charlotte | 190000 |
<end>Convert this json to yaml:
[
    {
        "Restaurant Name": "The Steakhouse",
        "Cuisine": "French"
    },
    {
        "Restaurant Name": "The Golden Spoon",
        "Cuisine": "Chinese"
    },
    {
        "Restaurant Name": "The Golden Spoon",
        "Cuisine": "Mediterranean"
    },
    {
        "Restaurant Name": "Taco Town",
        "Cuisine": "Mediterranean"
    },
    {
        "Restaurant Name": "BBQ Barn",
        "Cuisine": "French"
    },
    {
        "Restaurant Name": "Pizza Planet",
        "Cuisine": "Indian"
    },
    {
        "Restaurant Name": "Pizza Planet",
        "Cuisine": "Italian"
    },
    {
        "Restaurant Name": "Pasta Palace",
        "Cuisine": "French"
    },
    {
        "Restaurant Name": "Pizza Planet",
        "Cuisine": "Mediterranean"
    }
]<start>
- Cuisine: French
  Restaurant Name: The Steakhouse
- Cuisine: Chinese
  Restaurant Name: The Golden Spoon
- Cuisine: Mediterranean
  Restaurant Name: The Golden Spoon
- Cuisine: Mediterranean
  Restaurant Name: Taco Town
- Cuisine: French
  Restaurant Name: BBQ Barn
- Cuisine: Indian
  Restaurant Name: Pizza Planet
- Cuisine: Italian
  Restaurant Name: Pizza Planet
- Cuisine: French
  Restaurant Name: Pasta Palace
- Cuisine: Mediterranean
  Restaurant Name: Pizza Planet
<end>Can you change this Markdown into YAML?
| Device ID | Location | Battery Level (%) | Reading Value | Timestamp |
| --- | --- | --- | --- | --- |
| device-0063 | Hallway | 73.3 | 58.71 | 2023-08-24 18:48:34 |
| device-0096 | Hallway | 54.1 | 42.3 | 2021-01-08 20:11:17 |
| device-0045 | Kitchen | 46.7 | 6.52 | 2022-11-18 15:22:18 |
| device-0016 | Garden | 81.0 | -24.8 | 2021-06-10 11:02:33 |<start>
- Battery Level (%): 73.3
  Device ID: device-0063
  Location: Hallway
  Reading Value: 58.71
  Timestamp: '2023-08-24 18:48:34'
- Battery Level (%): 54.1
  Device ID: device-0096
  Location: Hallway
  Reading Value: 42.3
  Timestamp: '2021-01-08 20:11:17'
- Battery Level (%): 46.7
  Device ID: device-0045
  Location: Kitchen
  Reading Value: 6.52
  Timestamp: '2022-11-18 15:22:18'
- Battery Level (%): 81.0
  Device ID: device-0016
  Location: Garden
  Reading Value: -24.8
  Timestamp: '2021-06-10 11:02:33'
<end>Please transform the following csv data into Json:
Name,Age,Birth Month,City,Income
Maria,35,December,Austin,465000
Luna,55,February,Nashville,175000
Heather,38,February,Charlotte,175000
Garry,45,July,Houston,215000
Emil,23,February,Charlotte,340000
Marlene,49,February,San Jose,345000
Irene,44,March,San Diego,475000
Heidi,44,June,Memphis,355000
Ola,28,March,Columbus,125000
Tammy,33,October,Memphis,90000
<start>
[
    {
        "Name": "Maria",
        "Age": 35,
        "Birth Month": "December",
        "City": "Austin",
        "Income": 465000
    },
    {
        "Name": "Luna",
        "Age": 55,
        "Birth Month": "February",
        "City": "Nashville",
        "Income": 175000
    },
    {
        "Name": "Heather",
        "Age": 38,
        "Birth Month": "February",
        "City": "Charlotte",
        "Income": 175000
    },
    {
        "Name": "Garry",
        "Age": 45,
        "Birth Month": "July",
        "City": "Houston",
        "Income": 215000
    },
    {
        "Name": "Emil",
        "Age": 23,
        "Birth Month": "February",
        "City": "Charlotte",
        "Income": 340000
    },
    {
        "Name": "Marlene",
        "Age": 49,
        "Birth Month": "February",
        "City": "San Jose",
        "Income": 345000
    },
    {
        "Name": "Irene",
        "Age": 44,
        "Birth Month": "March",
        "City": "San Diego",
        "Income": 475000
    },
    {
        "Name": "Heidi",
        "Age": 44,
        "Birth Month": "June",
        "City": "Memphis",
        "Income": 355000
    },
    {
        "Name": "Ola",
        "Age": 28,
        "Birth Month": "March",
        "City": "Columbus",
        "Income": 125000
    },
    {
        "Name": "Tammy",
        "Age": 33,
        "Birth Month": "October",
        "City": "Memphis",
        "Income": 90000
    }
]
<end>Convert this plain text to Csv:
Restaurant Name: BBQ Barn | Cuisine: Chinese | Price Range: $$$$$
Restaurant Name: Curry Corner | Cuisine: American | Price Range: $$$$
Restaurant Name: Sushi World | Cuisine: Indian | Price Range: $
Restaurant Name: Vegan Delight | Cuisine: French | Price Range: $$$$
Restaurant Name: Curry Corner | Cuisine: Japanese | Price Range: $$$$
<start>
Restaurant Name,Cuisine,Price Range
BBQ Barn,Chinese,$$$$$
Curry Corner,American,$$$$
Sushi World,Indian,$
Vegan Delight,French,$$$$
Curry Corner,Japanese,$$$$
<end>Transform this csv structure to a yaml format:
Title,Genre
Legends of the Rift,Historical
Shadows of Solitude,Thriller
Shadows of Solitude,Horror
Shadows of Solitude,Horror
<start>
- Genre: Historical
  Title: Legends of the Rift
- Genre: Thriller
  Title: Shadows of Solitude
- Genre: Horror
  Title: Shadows of Solitude
- Genre: Horror
  Title: Shadows of Solitude
<end>Please transform the following Csv data into Plain text:
Product Name,SKU,Price,Category,Supplier Name
Apparatus,SKU-1030,282.67,Electronics,Umbrella Corp
Doohickey,SKU-1024,362.4,Electronics,Umbrella Corp
Widget,SKU-1057,188.6,Electronics,Wonka Industries
Apparatus,SKU-1011,207.32,Toys,Wonka Industries
<start>
Product Name: Apparatus | SKU: SKU-1030 | Price: 282.67 | Category: Electronics | Supplier Name: Umbrella Corp
Product Name: Doohickey | SKU: SKU-1024 | Price: 362.4 | Category: Electronics | Supplier Name: Umbrella Corp
Product Name: Widget | SKU: SKU-1057 | Price: 188.6 | Category: Electronics | Supplier Name: Wonka Industries
Product Name: Apparatus | SKU: SKU-1011 | Price: 207.32 | Category: Toys | Supplier Name: Wonka Industries
<end>Please transform the following csv data into JSON:
Start Location,Distance (miles),Duration (hours)
New York,2015.3,29.6
Houston,1884.8,61.9
Chicago,483.5,6.6
Los Angeles,622.4,29.0
Phoenix,194.4,69.1
Chicago,2392.5,60.9
<start>
[
    {
        "Start Location": "New York",
        "Distance (miles)": 2015.3,
        "Duration (hours)": 29.6
    },
    {
        "Start Location": "Houston",
        "Distance (miles)": 1884.8,
        "Duration (hours)": 61.9
    },
    {
        "Start Location": "Chicago",
        "Distance (miles)": 483.5,
        "Duration (hours)": 6.6
    },
    {
        "Start Location": "Los Angeles",
        "Distance (miles)": 622.4,
        "Duration (hours)": 29.0
    },
    {
        "Start Location": "Phoenix",
        "Distance (miles)": 194.4,
        "Duration (hours)": 69.1
    },
    {
        "Start Location": "Chicago",
        "Distance (miles)": 2392.5,
        "Duration (hours)": 60.9
    }
]
<end>Here's some csv data, can you convert it to JSON?
Director,Genre,Box Office Earnings (M)
Talon Blackthorn,Thriller,573.64
Drake Nightshade,Comedy,160.33
Mara Moonshadow,Thriller,330.15
Zara Stormrider,Drama,197.74
Mara Moonshadow,Adventure,563.8
Mara Moonshadow,Drama,870.93
Zara Stormrider,Thriller,160.33
<start>
[
    {
        "Director": "Talon Blackthorn",
        "Genre": "Thriller",
        "Box Office Earnings (M)": 573.64
    },
    {
        "Director": "Drake Nightshade",
        "Genre": "Comedy",
        "Box Office Earnings (M)": 160.33
    },
    {
        "Director": "Mara Moonshadow",
        "Genre": "Thriller",
        "Box Office Earnings (M)": 330.15
    },
    {
        "Director": "Zara Stormrider",
        "Genre": "Drama",
        "Box Office Earnings (M)": 197.74
    },
    {
        "Director": "Mara Moonshadow",
        "Genre": "Adventure",
        "Box Office Earnings (M)": 563.8
    },
    {
        "Director": "Mara Moonshadow",
        "Genre": "Drama",
        "Box Office Earnings (M)": 870.93
    },
    {
        "Director": "Zara Stormrider",
        "Genre": "Thriller",
        "Box Office Earnings (M)": 160.33
    }
]
<end>Transform this yml structure to a markdown format:
- Average Latency (ms): 16.32
  Cache Hit Ratio (%): 70.23
  Connection Count: 293
  Database Name: SalesDB
  Queries per Second: 3836.28
  Timestamp: '2023-09-28 11:29:34'
- Average Latency (ms): 76.65
  Cache Hit Ratio (%): 91.2
  Connection Count: 131
  Database Name: ProductsDB
  Queries per Second: 4841.1
  Timestamp: '2021-09-02 16:23:05'
- Average Latency (ms): 94.27
  Cache Hit Ratio (%): 70.33
  Connection Count: 363
  Database Name: LogsDB
  Queries per Second: 4701.17
  Timestamp: '2023-06-22 09:52:45'
- Average Latency (ms): 58.64
  Cache Hit Ratio (%): 75.59
  Connection Count: 483
  Database Name: LogsDB
  Queries per Second: 1473.97
  Timestamp: '2023-07-13 00:06:05'
- Average Latency (ms): 77.59
  Cache Hit Ratio (%): 77.06
  Connection Count: 159
  Database Name: UserDB
  Queries per Second: 1890.51
  Timestamp: '2023-09-02 03:10:29'
- Average Latency (ms): 60.67
  Cache Hit Ratio (%): 90.62
  Connection Count: 455
  Database Name: LogsDB
  Queries per Second: 4161.79
  Timestamp: '2022-08-23 04:35:50'
- Average Latency (ms): 9.1
  Cache Hit Ratio (%): 75.82
  Connection Count: 257
  Database Name: ProductsDB
  Queries per Second: 2481.7
  Timestamp: '2021-10-04 10:50:01'
- Average Latency (ms): 16.21
  Cache Hit Ratio (%): 98.32
  Connection Count: 138
  Database Name: ProfilesDB
  Queries per Second: 2268.55
  Timestamp: '2022-01-11 12:20:20'
<start>
| Database Name | Queries per Second | Cache Hit Ratio (%) | Connection Count | Average Latency (ms) | Timestamp |
| --- | --- | --- | --- | --- | --- |
| SalesDB | 3836.28 | 70.23 | 293 | 16.32 | 2023-09-28 11:29:34 |
| ProductsDB | 4841.1 | 91.2 | 131 | 76.65 | 2021-09-02 16:23:05 |
| LogsDB | 4701.17 | 70.33 | 363 | 94.27 | 2023-06-22 09:52:45 |
| LogsDB | 1473.97 | 75.59 | 483 | 58.64 | 2023-07-13 00:06:05 |
| UserDB | 1890.51 | 77.06 | 159 | 77.59 | 2023-09-02 03:10:29 |
| LogsDB | 4161.79 | 90.62 | 455 | 60.67 | 2022-08-23 04:35:50 |
| ProductsDB | 2481.7 | 75.82 | 257 | 9.1 | 2021-10-04 10:50:01 |
| ProfilesDB | 2268.55 | 98.32 | 138 | 16.21 | 2022-01-11 12:20:20 |
<end>Can you change this plain text into json?
Sector: Aerospace | Market Cap: Mega Cap | Stock Price: 653.76
Sector: Aerospace | Market Cap: Small Cap | Stock Price: 650.99
Sector: Retail | Market Cap: Mega Cap | Stock Price: 16.66
Sector: Automotive | Market Cap: Mega Cap | Stock Price: 612.39
Sector: Technology | Market Cap: Mega Cap | Stock Price: 488.06
<start>
[
    {
        "Sector": "Aerospace",
        "Market Cap": "Mega Cap",
        "Stock Price": 653.76
    },
    {
        "Sector": "Aerospace",
        "Market Cap": "Small Cap",
        "Stock Price": 650.99
    },
    {
        "Sector": "Retail",
        "Market Cap": "Mega Cap",
        "Stock Price": 16.66
    },
    {
        "Sector": "Automotive",
        "Market Cap": "Mega Cap",
        "Stock Price": 612.39
    },
    {
        "Sector": "Technology",
        "Market Cap": "Mega Cap",
        "Stock Price": 488.06
    }
]
<end>Here's some Plain text data, can you convert it to csv?
Trip Name: Canyon Trek | Start Location: Denver | End Location: San Francisco | Distance (miles): 870.9 | Duration (hours): 59.1 | Fuel Used (gallons): 94.7
Trip Name: Historic Route | Start Location: Miami | End Location: Chicago | Distance (miles): 2074.1 | Duration (hours): 41.7 | Fuel Used (gallons): 95.7
Trip Name: Mountain Adventure | Start Location: Miami | End Location: San Francisco | Distance (miles): 2283.9 | Duration (hours): 61.5 | Fuel Used (gallons): 25.5
Trip Name: Desert Drive | Start Location: Los Angeles | End Location: San Francisco | Distance (miles): 840.8 | Duration (hours): 71.1 | Fuel Used (gallons): 27.9
Trip Name: City Explorer | Start Location: Chicago | End Location: Houston | Distance (miles): 2631.8 | Duration (hours): 18.1 | Fuel Used (gallons): 55.4
Trip Name: Lakeside Retreat | Start Location: Denver | End Location: San Francisco | Distance (miles): 2390.4 | Duration (hours): 28.3 | Fuel Used (gallons): 55.9
Trip Name: Valley Voyage | Start Location: Denver | End Location: Phoenix | Distance (miles): 200.8 | Duration (hours): 23.9 | Fuel Used (gallons): 17.2
Trip Name: Canyon Trek | Start Location: New York | End Location: Houston | Distance (miles): 979.2 | Duration (hours): 67.0 | Fuel Used (gallons): 17.2
Trip Name: Highway Odyssey | Start Location: Miami | End Location: Phoenix | Distance (miles): 2236.9 | Duration (hours): 10.4 | Fuel Used (gallons): 28.7
Trip Name: Historic Route | Start Location: Miami | End Location: Phoenix | Distance (miles): 1252.8 | Duration (hours): 28.3 | Fuel Used (gallons): 88.8
<start>
Trip Name,Start Location,End Location,Distance (miles),Duration (hours),Fuel Used (gallons)
Canyon Trek,Denver,San Francisco,870.9,59.1,94.7
Historic Route,Miami,Chicago,2074.1,41.7,95.7
Mountain Adventure,Miami,San Francisco,2283.9,61.5,25.5
Desert Drive,Los Angeles,San Francisco,840.8,71.1,27.9
City Explorer,Chicago,Houston,2631.8,18.1,55.4
Lakeside Retreat,Denver,San Francisco,2390.4,28.3,55.9
Valley Voyage,Denver,Phoenix,200.8,23.9,17.2
Canyon Trek,New York,Houston,979.2,67.0,17.2
Highway Odyssey,Miami,Phoenix,2236.9,10.4,28.7
Historic Route,Miami,Phoenix,1252.8,28.3,88.8
<end>Convert this Yaml to json:
- Annual Revenue (B): 470.43
  Company: AutoDrive
  Market Cap: Mega Cap
  Quarter: Q2
  Sector: Biotech
  Stock Price: 839.8
- Annual Revenue (B): 80.69
  Company: RetailHub
  Market Cap: Mid Cap
  Quarter: Q3
  Sector: Finance
  Stock Price: 438.64
- Annual Revenue (B): 68.07
  Company: Foodies
  Market Cap: Small Cap
  Quarter: Q3
  Sector: Aerospace
  Stock Price: 572.14
<start>
[
    {
        "Company": "AutoDrive",
        "Sector": "Biotech",
        "Market Cap": "Mega Cap",
        "Stock Price": 839.8,
        "Annual Revenue (B)": 470.43,
        "Quarter": "Q2"
    },
    {
        "Company": "RetailHub",
        "Sector": "Finance",
        "Market Cap": "Mid Cap",
        "Stock Price": 438.64,
        "Annual Revenue (B)": 80.69,
        "Quarter": "Q3"
    },
    {
        "Company": "Foodies",
        "Sector": "Aerospace",
        "Market Cap": "Small Cap",
        "Stock Price": 572.14,
        "Annual Revenue (B)": 68.07,
        "Quarter": "Q3"
    }
]
<end>Can you change this yaml into Markdown?
- Annual Revenue (B): 98.2
  Company: GlobalTrade
  Quarter: Q4
  Sector: Finance
- Annual Revenue (B): 180.08
  Company: BioPharm
  Quarter: Q2
  Sector: Automotive
- Annual Revenue (B): 377.24
  Company: Foodies
  Quarter: Q3
  Sector: Aerospace
<start>
| Company | Sector | Annual Revenue (B) | Quarter |
| --- | --- | --- | --- |
| GlobalTrade | Finance | 98.2 | Q4 |
| BioPharm | Automotive | 180.08 | Q2 |
| Foodies | Aerospace | 377.24 | Q3 |
<end>Here's some markdown data, can you convert it to plain text?
| Open Price | Close Price | High Price | Low Price | Volume |
| --- | --- | --- | --- | --- |
| 175.74 | 662.76 | 662.76 | 175.74 | 6893816 |
| 1461.18 | 714.87 | 1461.18 | 714.87 | 5446983 |
| 263.28 | 1219.88 | 1219.88 | 263.28 | 8230195 |
| 662.76 | 1309.88 | 1309.88 | 662.76 | 3655593 |<start>
Open Price: 175.74 | Close Price: 662.76 | High Price: 662.76 | Low Price: 175.74 | Volume: 6893816
Open Price: 1461.18 | Close Price: 714.87 | High Price: 1461.18 | Low Price: 714.87 | Volume: 5446983
Open Price: 263.28 | Close Price: 1219.88 | High Price: 1219.88 | Low Price: 263.28 | Volume: 8230195
Open Price: 662.76 | Close Price: 1309.88 | High Price: 1309.88 | Low Price: 662.76 | Volume: 3655593
<end>Here's some csv data, can you convert it to markdown?
Company,Date,Open Price,Close Price,High Price,Low Price,Volume
FoodChain,2013-10-16,1123.32,972.53,1123.32,972.53,5915831
RetailWorld,2012-08-08,1431.54,910.11,1431.54,142.38,1985631
RetailWorld,2016-01-24,181.72,129.81,1478.78,129.81,4417289
RetailWorld,2013-06-20,1453.74,142.38,1453.74,142.38,6676436
FinanceTrust,2012-07-06,105.73,1282.79,1282.79,105.73,5915831
MediaGroup,2023-10-14,182.25,1446.47,1446.47,182.25,3019977
<start>
| Company | Date | Open Price | Close Price | High Price | Low Price | Volume |
| --- | --- | --- | --- | --- | --- | --- |
| FoodChain | 2013-10-16 | 1123.32 | 972.53 | 1123.32 | 972.53 | 5915831 |
| RetailWorld | 2012-08-08 | 1431.54 | 910.11 | 1431.54 | 142.38 | 1985631 |
| RetailWorld | 2016-01-24 | 181.72 | 129.81 | 1478.78 | 129.81 | 4417289 |
| RetailWorld | 2013-06-20 | 1453.74 | 142.38 | 1453.74 | 142.38 | 6676436 |
| FinanceTrust | 2012-07-06 | 105.73 | 1282.79 | 1282.79 | 105.73 | 5915831 |
| MediaGroup | 2023-10-14 | 182.25 | 1446.47 | 1446.47 | 182.25 | 3019977 |
<end>Convert this CSV to plain text:
Stock Quantity,Category,Supplier Name
89,Electronics,Umbrella Corp
187,Toys,ACME Corp
7,Household,Umbrella Corp
273,Sports,Umbrella Corp
405,Automotive,Umbrella Corp
<start>
Stock Quantity: 89 | Category: Electronics | Supplier Name: Umbrella Corp
Stock Quantity: 187 | Category: Toys | Supplier Name: ACME Corp
Stock Quantity: 7 | Category: Household | Supplier Name: Umbrella Corp
Stock Quantity: 273 | Category: Sports | Supplier Name: Umbrella Corp
Stock Quantity: 405 | Category: Automotive | Supplier Name: Umbrella Corp
<end>Convert this csv to markdown:
SKU,Price,Stock Quantity,Category
SKU-1088,73.9,14,Sports
SKU-1035,97.37,380,Sports
SKU-1087,64.67,312,Electronics
SKU-1051,305.01,279,Toys
SKU-1096,114.99,465,Household
SKU-1055,418.91,204,Electronics
<start>
| SKU | Price | Stock Quantity | Category |
| --- | --- | --- | --- |
| SKU-1088 | 73.9 | 14 | Sports |
| SKU-1035 | 97.37 | 380 | Sports |
| SKU-1087 | 64.67 | 312 | Electronics |
| SKU-1051 | 305.01 | 279 | Toys |
| SKU-1096 | 114.99 | 465 | Household |
| SKU-1055 | 418.91 | 204 | Electronics |
<end>Convert this plain text to json:
Device ID: device-0058 | Device Type: Pressure Sensor | Location: Kitchen | Battery Level (%): 33.4 | Reading Value: 22.93
Device ID: device-0089 | Device Type: Pressure Sensor | Location: Living Room | Battery Level (%): 76.6 | Reading Value: -16.89
Device ID: device-0006 | Device Type: Temperature Sensor | Location: Bedroom | Battery Level (%): 85.8 | Reading Value: 71.74
Device ID: device-0036 | Device Type: Light Sensor | Location: Living Room | Battery Level (%): 98.0 | Reading Value: -27.96
Device ID: device-0064 | Device Type: Temperature Sensor | Location: Bedroom | Battery Level (%): 25.4 | Reading Value: -16.89
Device ID: device-0051 | Device Type: Temperature Sensor | Location: Hallway | Battery Level (%): 15.5 | Reading Value: -5.99
Device ID: device-0040 | Device Type: Pressure Sensor | Location: Office | Battery Level (%): 38.7 | Reading Value: 9.53
Device ID: device-0002 | Device Type: Temperature Sensor | Location: Garden | Battery Level (%): 41.6 | Reading Value: 21.79
Device ID: device-0065 | Device Type: Light Sensor | Location: Living Room | Battery Level (%): 39.8 | Reading Value: -9.29
<start>
[
    {
        "Device ID": "device-0058",
        "Device Type": "Pressure Sensor",
        "Location": "Kitchen",
        "Battery Level (%)": 33.4,
        "Reading Value": 22.93
    },
    {
        "Device ID": "device-0089",
        "Device Type": "Pressure Sensor",
        "Location": "Living Room",
        "Battery Level (%)": 76.6,
        "Reading Value": -16.89
    },
    {
        "Device ID": "device-0006",
        "Device Type": "Temperature Sensor",
        "Location": "Bedroom",
        "Battery Level (%)": 85.8,
        "Reading Value": 71.74
    },
    {
        "Device ID": "device-0036",
        "Device Type": "Light Sensor",
        "Location": "Living Room",
        "Battery Level (%)": 98.0,
        "Reading Value": -27.96
    },
    {
        "Device ID": "device-0064",
        "Device Type": "Temperature Sensor",
        "Location": "Bedroom",
        "Battery Level (%)": 25.4,
        "Reading Value": -16.89
    },
    {
        "Device ID": "device-0051",
        "Device Type": "Temperature Sensor",
        "Location": "Hallway",
        "Battery Level (%)": 15.5,
        "Reading Value": -5.99
    },
    {
        "Device ID": "device-0040",
        "Device Type": "Pressure Sensor",
        "Location": "Office",
        "Battery Level (%)": 38.7,
        "Reading Value": 9.53
    },
    {
        "Device ID": "device-0002",
        "Device Type": "Temperature Sensor",
        "Location": "Garden",
        "Battery Level (%)": 41.6,
        "Reading Value": 21.79
    },
    {
        "Device ID": "device-0065",
        "Device Type": "Light Sensor",
        "Location": "Living Room",
        "Battery Level (%)": 39.8,
        "Reading Value": -9.29
    }
]
<end>Convert this Plain text to json:
Location: Miami | Humidity (%): 44 | Day: Monday
Location: Denver | Humidity (%): 23 | Day: Friday
Location: Houston | Humidity (%): 80 | Day: Friday
Location: Seattle | Humidity (%): 50 | Day: Wednesday
Location: Houston | Humidity (%): 40 | Day: Saturday
<start>
[
    {
        "Location": "Miami",
        "Humidity (%)": 44,
        "Day": "Monday"
    },
    {
        "Location": "Denver",
        "Humidity (%)": 23,
        "Day": "Friday"
    },
    {
        "Location": "Houston",
        "Humidity (%)": 80,
        "Day": "Friday"
    },
    {
        "Location": "Seattle",
        "Humidity (%)": 50,
        "Day": "Wednesday"
    },
    {
        "Location": "Houston",
        "Humidity (%)": 40,
        "Day": "Saturday"
    }
]
<end>Please transform the following csv data into PLAIN TEXT:
Device ID,Device Type,Battery Level (%),Timestamp
device-0083,Motion Detector,79.6,2022-12-12 00:06:54
device-0093,Light Sensor,70.1,2023-06-08 10:51:16
device-0015,Humidity Sensor,93.4,2022-02-17 23:26:44
device-0100,Pressure Sensor,24.9,2021-12-22 00:00:59
device-0023,Humidity Sensor,46.5,2023-09-20 15:42:25
device-0011,Humidity Sensor,93.4,2022-11-21 16:12:43
device-0006,Temperature Sensor,47.3,2021-02-04 19:06:55
device-0082,Temperature Sensor,37.2,2021-11-18 20:30:59
<start>
Device ID: device-0083 | Device Type: Motion Detector | Battery Level (%): 79.6 | Timestamp: 2022-12-12 00:06:54
Device ID: device-0093 | Device Type: Light Sensor | Battery Level (%): 70.1 | Timestamp: 2023-06-08 10:51:16
Device ID: device-0015 | Device Type: Humidity Sensor | Battery Level (%): 93.4 | Timestamp: 2022-02-17 23:26:44
Device ID: device-0100 | Device Type: Pressure Sensor | Battery Level (%): 24.9 | Timestamp: 2021-12-22 00:00:59
Device ID: device-0023 | Device Type: Humidity Sensor | Battery Level (%): 46.5 | Timestamp: 2023-09-20 15:42:25
Device ID: device-0011 | Device Type: Humidity Sensor | Battery Level (%): 93.4 | Timestamp: 2022-11-21 16:12:43
Device ID: device-0006 | Device Type: Temperature Sensor | Battery Level (%): 47.3 | Timestamp: 2021-02-04 19:06:55
Device ID: device-0082 | Device Type: Temperature Sensor | Battery Level (%): 37.2 | Timestamp: 2021-11-18 20:30:59
<end>Can you change this Json into Csv?
[
    {
        "Location": "Houston",
        "Condition": "Stormy",
        "Temperature (C)": 31.0,
        "Humidity (%)": 66,
        "Wind Speed (km/h)": 3.6,
        "Day": "Wednesday"
    },
    {
        "Location": "Seattle",
        "Condition": "Stormy",
        "Temperature (C)": 4.0,
        "Humidity (%)": 55,
        "Wind Speed (km/h)": 12.2,
        "Day": "Saturday"
    },
    {
        "Location": "Chicago",
        "Condition": "Windy",
        "Temperature (C)": 23.3,
        "Humidity (%)": 72,
        "Wind Speed (km/h)": 8.7,
        "Day": "Monday"
    }
]<start>
Location,Condition,Temperature (C),Humidity (%),Wind Speed (km/h),Day
Houston,Stormy,31.0,66,3.6,Wednesday
Seattle,Stormy,4.0,55,12.2,Saturday
Chicago,Windy,23.3,72,8.7,Monday
<end>Transform this JSON structure to a markdown format:
[
    {
        "Sector": "Finance",
        "Stock Price": 137.53,
        "Quarter": "Q2"
    },
    {
        "Sector": "Finance",
        "Stock Price": 298.6,
        "Quarter": "Q1"
    },
    {
        "Sector": "Automotive",
        "Stock Price": 844.15,
        "Quarter": "Q1"
    },
    {
        "Sector": "Technology",
        "Stock Price": 347.9,
        "Quarter": "Q4"
    },
    {
        "Sector": "Finance",
        "Stock Price": 264.28,
        "Quarter": "Q2"
    },
    {
        "Sector": "Retail",
        "Stock Price": 363.88,
        "Quarter": "Q1"
    },
    {
        "Sector": "Retail",
        "Stock Price": 632.54,
        "Quarter": "Q1"
    },
    {
        "Sector": "Automotive",
        "Stock Price": 371.13,
        "Quarter": "Q1"
    },
    {
        "Sector": "Energy",
        "Stock Price": 606.06,
        "Quarter": "Q3"
    },
    {
        "Sector": "Aerospace",
        "Stock Price": 779.92,
        "Quarter": "Q3"
    }
]<start>
| Sector | Stock Price | Quarter |
| --- | --- | --- |
| Finance | 137.53 | Q2 |
| Finance | 298.6 | Q1 |
| Automotive | 844.15 | Q1 |
| Technology | 347.9 | Q4 |
| Finance | 264.28 | Q2 |
| Retail | 363.88 | Q1 |
| Retail | 632.54 | Q1 |
| Automotive | 371.13 | Q1 |
| Energy | 606.06 | Q3 |
| Aerospace | 779.92 | Q3 |
<end>Please transform the following CSV data into Yaml:
Company,Date,Open Price,Close Price,High Price,Low Price,Volume
GreenEnergy,2023-05-21,1319.12,1418.49,1418.49,1315.16,5259564
HealthGen,2019-03-12,670.72,121.05,670.72,121.05,787077
FoodChain,2015-02-14,540.67,555.78,1142.66,540.67,4054953
MediaGroup,2013-01-06,670.72,139.45,967.0,127.1,336875
BioLife,2014-04-21,786.1,223.48,786.1,223.48,5541865
AeroSystems,2020-05-04,1481.94,1073.93,1481.94,121.05,2890760
<start>
- Close Price: 1418.49
  Company: GreenEnergy
  Date: '2023-05-21'
  High Price: 1418.49
  Low Price: 1315.16
  Open Price: 1319.12
  Volume: 5259564
- Close Price: 121.05
  Company: HealthGen
  Date: '2019-03-12'
  High Price: 670.72
  Low Price: 121.05
  Open Price: 670.72
  Volume: 787077
- Close Price: 555.78
  Company: FoodChain
  Date: '2015-02-14'
  High Price: 1142.66
  Low Price: 540.67
  Open Price: 540.67
  Volume: 4054953
- Close Price: 139.45
  Company: MediaGroup
  Date: '2013-01-06'
  High Price: 967.0
  Low Price: 127.1
  Open Price: 670.72
  Volume: 336875
- Close Price: 223.48
  Company: BioLife
  Date: '2014-04-21'
  High Price: 786.1
  Low Price: 223.48
  Open Price: 786.1
  Volume: 5541865
- Close Price: 1073.93
  Company: AeroSystems
  Date: '2020-05-04'
  High Price: 1481.94
  Low Price: 121.05
  Open Price: 1481.94
  Volume: 2890760
<end>Here's some Json data, can you convert it to Markdown?
[
    {
        "Start Location": "Miami",
        "End Location": "Chicago",
        "Distance (miles)": 2404.5,
        "Duration (hours)": 48.8,
        "Fuel Used (gallons)": 70.3
    },
    {
        "Start Location": "Phoenix",
        "End Location": "New York",
        "Distance (miles)": 363.7,
        "Duration (hours)": 36.2,
        "Fuel Used (gallons)": 69.8
    },
    {
        "Start Location": "Los Angeles",
        "End Location": "Miami",
        "Distance (miles)": 2334.2,
        "Duration (hours)": 55.8,
        "Fuel Used (gallons)": 44.7
    },
    {
        "Start Location": "Chicago",
        "End Location": "Houston",
        "Distance (miles)": 1665.6,
        "Duration (hours)": 51.1,
        "Fuel Used (gallons)": 31.4
    },
    {
        "Start Location": "San Francisco",
        "End Location": "Denver",
        "Distance (miles)": 1968.3,
        "Duration (hours)": 47.8,
        "Fuel Used (gallons)": 71.8
    },
    {
        "Start Location": "San Francisco",
        "End Location": "New York",
        "Distance (miles)": 1825.7,
        "Duration (hours)": 70.2,
        "Fuel Used (gallons)": 15.7
    },
    {
        "Start Location": "Phoenix",
        "End Location": "Los Angeles",
        "Distance (miles)": 140.1,
        "Duration (hours)": 21.6,
        "Fuel Used (gallons)": 80.2
    },
    {
        "Start Location": "San Francisco",
        "End Location": "Houston",
        "Distance (miles)": 2299.5,
        "Duration (hours)": 65.8,
        "Fuel Used (gallons)": 33.6
    },
    {
        "Start Location": "San Francisco",
        "End Location": "Phoenix",
        "Distance (miles)": 1170.7,
        "Duration (hours)": 10.8,
        "Fuel Used (gallons)": 67.9
    },
    {
        "Start Location": "Chicago",
        "End Location": "New York",
        "Distance (miles)": 674.1,
        "Duration (hours)": 19.7,
        "Fuel Used (gallons)": 31.4
    }
]<start>
| Start Location | End Location | Distance (miles) | Duration (hours) | Fuel Used (gallons) |
| --- | --- | --- | --- | --- |
| Miami | Chicago | 2404.5 | 48.8 | 70.3 |
| Phoenix | New York | 363.7 | 36.2 | 69.8 |
| Los Angeles | Miami | 2334.2 | 55.8 | 44.7 |
| Chicago | Houston | 1665.6 | 51.1 | 31.4 |
| San Francisco | Denver | 1968.3 | 47.8 | 71.8 |
| San Francisco | New York | 1825.7 | 70.2 | 15.7 |
| Phoenix | Los Angeles | 140.1 | 21.6 | 80.2 |
| San Francisco | Houston | 2299.5 | 65.8 | 33.6 |
| San Francisco | Phoenix | 1170.7 | 10.8 | 67.9 |
| Chicago | New York | 674.1 | 19.7 | 31.4 |
<end>Convert this markdown to plain text:
| Company | Sector | Market Cap | Stock Price | Annual Revenue (B) | Quarter |
| --- | --- | --- | --- | --- | --- |
| RetailHub | Aerospace | Mid Cap | 118.24 | 173.91 | Q2 |
| AutoDrive | Automotive | Mega Cap | 107.47 | 315.33 | Q3 |
| AeroSpace | Healthcare | Large Cap | 274.53 | 159.32 | Q2 |
| AeroSpace | Retail | Mega Cap | 147.35 | 294.75 | Q3 |<start>
Company: RetailHub | Sector: Aerospace | Market Cap: Mid Cap | Stock Price: 118.24 | Annual Revenue (B): 173.91 | Quarter: Q2
Company: AutoDrive | Sector: Automotive | Market Cap: Mega Cap | Stock Price: 107.47 | Annual Revenue (B): 315.33 | Quarter: Q3
Company: AeroSpace | Sector: Healthcare | Market Cap: Large Cap | Stock Price: 274.53 | Annual Revenue (B): 159.32 | Quarter: Q2
Company: AeroSpace | Sector: Retail | Market Cap: Mega Cap | Stock Price: 147.35 | Annual Revenue (B): 294.75 | Quarter: Q3
<end>Please transform the following json data into Plain text:
[
    {
        "Trip Name": "Valley Voyage",
        "Start Location": "Miami",
        "End Location": "New York",
        "Fuel Used (gallons)": 8.0
    },
    {
        "Trip Name": "Lakeside Retreat",
        "Start Location": "Denver",
        "End Location": "Los Angeles",
        "Fuel Used (gallons)": 9.7
    },
    {
        "Trip Name": "Forest Journey",
        "Start Location": "Denver",
        "End Location": "San Francisco",
        "Fuel Used (gallons)": 74.9
    },
    {
        "Trip Name": "City Explorer",
        "Start Location": "Chicago",
        "End Location": "San Francisco",
        "Fuel Used (gallons)": 77.5
    },
    {
        "Trip Name": "Lakeside Retreat",
        "Start Location": "Houston",
        "End Location": "Denver",
        "Fuel Used (gallons)": 60.1
    }
]<start>
Trip Name: Valley Voyage | Start Location: Miami | End Location: New York | Fuel Used (gallons): 8.0
Trip Name: Lakeside Retreat | Start Location: Denver | End Location: Los Angeles | Fuel Used (gallons): 9.7
Trip Name: Forest Journey | Start Location: Denver | End Location: San Francisco | Fuel Used (gallons): 74.9
Trip Name: City Explorer | Start Location: Chicago | End Location: San Francisco | Fuel Used (gallons): 77.5
Trip Name: Lakeside Retreat | Start Location: Houston | End Location: Denver | Fuel Used (gallons): 60.1
<end>Transform this Json structure to a Yml format:
[
    {
        "Location": "Phoenix",
        "Price Range": "$$$$$"
    },
    {
        "Location": "New York",
        "Price Range": "$$$$$"
    },
    {
        "Location": "Houston",
        "Price Range": "$$$$"
    },
    {
        "Location": "Miami",
        "Price Range": "$$"
    },
    {
        "Location": "Los Angeles",
        "Price Range": "$$$$$"
    },
    {
        "Location": "Phoenix",
        "Price Range": "$$$$"
    },
    {
        "Location": "Houston",
        "Price Range": "$$$$"
    },
    {
        "Location": "Chicago",
        "Price Range": "$$$$"
    }
]<start>
- Location: Phoenix
  Price Range: $$$$$
- Location: New York
  Price Range: $$$$$
- Location: Houston
  Price Range: $$$$
- Location: Miami
  Price Range: $$
- Location: Los Angeles
  Price Range: $$$$$
- Location: Phoenix
  Price Range: $$$$
- Location: Houston
  Price Range: $$$$
- Location: Chicago
  Price Range: $$$$
<end>Please transform the following plain text data into json:
Database Name: AnalyticsDB | Queries per Second: 4812.02 | Connection Count: 392 | Timestamp: 2022-08-10 06:59:14
Database Name: ProductsDB | Queries per Second: 996.89 | Connection Count: 120 | Timestamp: 2023-02-24 23:47:46
Database Name: ProfilesDB | Queries per Second: 3151.33 | Connection Count: 498 | Timestamp: 2023-08-09 12:24:16
Database Name: ProfilesDB | Queries per Second: 3413.15 | Connection Count: 476 | Timestamp: 2023-07-18 23:30:50
Database Name: ProfilesDB | Queries per Second: 2806.67 | Connection Count: 445 | Timestamp: 2022-04-16 09:50:26
Database Name: AnalyticsDB | Queries per Second: 2632.46 | Connection Count: 469 | Timestamp: 2023-02-13 18:23:59
Database Name: SalesDB | Queries per Second: 796.83 | Connection Count: 90 | Timestamp: 2023-06-07 12:52:51
Database Name: ProductsDB | Queries per Second: 2806.67 | Connection Count: 152 | Timestamp: 2022-12-18 13:23:45
<start>
[
    {
        "Database Name": "AnalyticsDB",
        "Queries per Second": 4812.02,
        "Connection Count": 392,
        "Timestamp": "2022-08-10 06:59:14"
    },
    {
        "Database Name": "ProductsDB",
        "Queries per Second": 996.89,
        "Connection Count": 120,
        "Timestamp": "2023-02-24 23:47:46"
    },
    {
        "Database Name": "ProfilesDB",
        "Queries per Second": 3151.33,
        "Connection Count": 498,
        "Timestamp": "2023-08-09 12:24:16"
    },
    {
        "Database Name": "ProfilesDB",
        "Queries per Second": 3413.15,
        "Connection Count": 476,
        "Timestamp": "2023-07-18 23:30:50"
    },
    {
        "Database Name": "ProfilesDB",
        "Queries per Second": 2806.67,
        "Connection Count": 445,
        "Timestamp": "2022-04-16 09:50:26"
    },
    {
        "Database Name": "AnalyticsDB",
        "Queries per Second": 2632.46,
        "Connection Count": 469,
        "Timestamp": "2023-02-13 18:23:59"
    },
    {
        "Database Name": "SalesDB",
        "Queries per Second": 796.83,
        "Connection Count": 90,
        "Timestamp": "2023-06-07 12:52:51"
    },
    {
        "Database Name": "ProductsDB",
        "Queries per Second": 2806.67,
        "Connection Count": 152,
        "Timestamp": "2022-12-18 13:23:45"
    }
]
<end>Can you change this json into csv?
[
    {
        "Company": "Foodies",
        "Market Cap": "Small Cap",
        "Annual Revenue (B)": 367.83
    },
    {
        "Company": "Foodies",
        "Market Cap": "Large Cap",
        "Annual Revenue (B)": 120.82
    },
    {
        "Company": "TechCorp",
        "Market Cap": "Small Cap",
        "Annual Revenue (B)": 492.08
    },
    {
        "Company": "AutoDrive",
        "Market Cap": "Small Cap",
        "Annual Revenue (B)": 492.08
    },
    {
        "Company": "EcoEnergy",
        "Market Cap": "Mega Cap",
        "Annual Revenue (B)": 147.34
    },
    {
        "Company": "Foodies",
        "Market Cap": "Mega Cap",
        "Annual Revenue (B)": 298.72
    }
]<start>
Company,Market Cap,Annual Revenue (B)
Foodies,Small Cap,367.83
Foodies,Large Cap,120.82
TechCorp,Small Cap,492.08
AutoDrive,Small Cap,492.08
EcoEnergy,Mega Cap,147.34
Foodies,Mega Cap,298.72
<end>Can you change this Json into markdown?
[
    {
        "Price": 22.44,
        "Stock Quantity": 434,
        "Category": "Household",
        "Supplier Name": "Umbrella Corp"
    },
    {
        "Price": 387.57,
        "Stock Quantity": 312,
        "Category": "Electronics",
        "Supplier Name": "Umbrella Corp"
    },
    {
        "Price": 418.71,
        "Stock Quantity": 316,
        "Category": "Electronics",
        "Supplier Name": "Globex"
    },
    {
        "Price": 52.54,
        "Stock Quantity": 280,
        "Category": "Toys",
        "Supplier Name": "Wayne Enterprises"
    },
    {
        "Price": 329.35,
        "Stock Quantity": 212,
        "Category": "Electronics",
        "Supplier Name": "Wayne Enterprises"
    },
    {
        "Price": 436.57,
        "Stock Quantity": 314,
        "Category": "Sports",
        "Supplier Name": "Umbrella Corp"
    }
]<start>
| Price | Stock Quantity | Category | Supplier Name |
| --- | --- | --- | --- |
| 22.44 | 434 | Household | Umbrella Corp |
| 387.57 | 312 | Electronics | Umbrella Corp |
| 418.71 | 316 | Electronics | Globex |
| 52.54 | 280 | Toys | Wayne Enterprises |
| 329.35 | 212 | Electronics | Wayne Enterprises |
| 436.57 | 314 | Sports | Umbrella Corp |
<end>Can you change this markdown into csv?
| Database Name | Queries per Second | Cache Hit Ratio (%) |
| --- | --- | --- |
| SessionsDB | 3831.29 | 81.07 |
| LogsDB | 86.21 | 73.03 |
| AnalyticsDB | 4567.78 | 87.89 |
| SalesDB | 837.5 | 97.98 |
| ProductsDB | 3557.0 | 87.11 |
| LogsDB | 1975.02 | 88.11 |
| MetricsDB | 837.5 | 90.04 |<start>
Database Name,Queries per Second,Cache Hit Ratio (%)
SessionsDB,3831.29,81.07
LogsDB,86.21,73.03
AnalyticsDB,4567.78,87.89
SalesDB,837.5,97.98
ProductsDB,3557.0,87.11
LogsDB,1975.02,88.11
MetricsDB,837.5,90.04
<end>Please transform the following plain text data into Markdown:
Queries per Second: 1184.65 | Average Latency (ms): 99.57 | Timestamp: 2022-01-22 06:12:23
Queries per Second: 3265.94 | Average Latency (ms): 68.07 | Timestamp: 2022-05-28 05:53:48
Queries per Second: 3048.35 | Average Latency (ms): 95.63 | Timestamp: 2023-08-16 10:18:35
Queries per Second: 923.33 | Average Latency (ms): 61.94 | Timestamp: 2022-03-27 00:23:50
<start>
| Queries per Second | Average Latency (ms) | Timestamp |
| --- | --- | --- |
| 1184.65 | 99.57 | 2022-01-22 06:12:23 |
| 3265.94 | 68.07 | 2022-05-28 05:53:48 |
| 3048.35 | 95.63 | 2023-08-16 10:18:35 |
| 923.33 | 61.94 | 2022-03-27 00:23:50 |
<end>Please transform the following MARKDOWN data into Csv:
| Trip Name | Start Location | End Location | Duration (hours) |
| --- | --- | --- | --- |
| Valley Voyage | Houston | San Francisco | 50.7 |
| Mountain Adventure | Houston | New York | 23.8 |
| Historic Route | Chicago | Phoenix | 28.5 |
| Forest Journey | Chicago | Phoenix | 1.8 |
| Canyon Trek | Los Angeles | New York | 8.2 |
| Desert Drive | Miami | New York | 57.6 |<start>
Trip Name,Start Location,End Location,Duration (hours)
Valley Voyage,Houston,San Francisco,50.7
Mountain Adventure,Houston,New York,23.8
Historic Route,Chicago,Phoenix,28.5
Forest Journey,Chicago,Phoenix,1.8
Canyon Trek,Los Angeles,New York,8.2
Desert Drive,Miami,New York,57.6
<end>Here's some MARKDOWN data, can you convert it to Json?
| Title | Author | Publication Year | Rating |
| --- | --- | --- | --- |
| Echoes of Eternity | Draven Blackthorn | 1984 | 2.3 |
| The Forgotten World | Orion Frostblade | 1967 | 4.4 |
| Tales of the Brave | Kara Firebrand | 2023 | 2.4 |
| The Crystal Key | Sylvia Nightshade | 1957 | 3.3 |
| The Silent Grove | Luna Silverleaf | 1978 | 2.6 |
| Tales of the Brave | Elara Moonshadow | 2010 | 3.1 |
| The Last Sky | Rowan Ashborne | 1950 | 1.7 |
| The Last Sky | Rowan Ashborne | 1953 | 1.3 |<start>
[
    {
        "Title": "Echoes of Eternity",
        "Author": "Draven Blackthorn",
        "Publication Year": 1984,
        "Rating": 2.3
    },
    {
        "Title": "The Forgotten World",
        "Author": "Orion Frostblade",
        "Publication Year": 1967,
        "Rating": 4.4
    },
    {
        "Title": "Tales of the Brave",
        "Author": "Kara Firebrand",
        "Publication Year": 2023,
        "Rating": 2.4
    },
    {
        "Title": "The Crystal Key",
        "Author": "Sylvia Nightshade",
        "Publication Year": 1957,
        "Rating": 3.3
    },
    {
        "Title": "The Silent Grove",
        "Author": "Luna Silverleaf",
        "Publication Year": 1978,
        "Rating": 2.6
    },
    {
        "Title": "Tales of the Brave",
        "Author": "Elara Moonshadow",
        "Publication Year": 2010,
        "Rating": 3.1
    },
    {
        "Title": "The Last Sky",
        "Author": "Rowan Ashborne",
        "Publication Year": 1950,
        "Rating": 1.7
    },
    {
        "Title": "The Last Sky",
        "Author": "Rowan Ashborne",
        "Publication Year": 1953,
        "Rating": 1.3
    }
]
<end>Convert this plain text to markdown:
Sector: Technology | Market Cap: Mid Cap | Stock Price: 430.31 | Quarter: Q2
Sector: Finance | Market Cap: Large Cap | Stock Price: 110.22 | Quarter: Q1
Sector: Energy | Market Cap: Mid Cap | Stock Price: 110.22 | Quarter: Q2
Sector: Technology | Market Cap: Mega Cap | Stock Price: 837.11 | Quarter: Q1
<start>
| Sector | Market Cap | Stock Price | Quarter |
| --- | --- | --- | --- |
| Technology | Mid Cap | 430.31 | Q2 |
| Finance | Large Cap | 110.22 | Q1 |
| Energy | Mid Cap | 110.22 | Q2 |
| Technology | Mega Cap | 837.11 | Q1 |
<end>Here's some Plain text data, can you convert it to Csv?
Title: Legends of the Rift | Author: Thorne Ironwood | Publication Year: 1968
Title: Whispers of the Abyss | Author: Isla Windrider | Publication Year: 1979
Title: The Silent Grove | Author: Galen Starfire | Publication Year: 1992
<start>
Title,Author,Publication Year
Legends of the Rift,Thorne Ironwood,1968
Whispers of the Abyss,Isla Windrider,1979
The Silent Grove,Galen Starfire,1992
<end>Convert this yml to Plain text:
- Age: 19
  City: Indianapolis
- Age: 60
  City: Milwaukee
- Age: 34
  City: Milwaukee
<start>
Age: 19 | City: Indianapolis
Age: 60 | City: Milwaukee
Age: 34 | City: Milwaukee
<end>Can you change this csv into JSON?
Company,Date,Open Price,Volume
AutoMotive,2011-02-04,983.16,3920813
MediaGroup,2020-02-03,256.25,9941172
FinanceTrust,2020-07-17,661.41,8995396
BioLife,2015-01-25,171.69,2657234
AeroSystems,2019-01-26,550.83,3642932
GreenEnergy,2012-07-05,454.16,3374263
TechnoCorp,2019-06-22,964.59,2483629
TechnoCorp,2014-07-28,1421.44,4919150
RetailWorld,2020-06-03,215.36,6618021
<start>
[
    {
        "Company": "AutoMotive",
        "Date": "2011-02-04",
        "Open Price": 983.16,
        "Volume": 3920813
    },
    {
        "Company": "MediaGroup",
        "Date": "2020-02-03",
        "Open Price": 256.25,
        "Volume": 9941172
    },
    {
        "Company": "FinanceTrust",
        "Date": "2020-07-17",
        "Open Price": 661.41,
        "Volume": 8995396
    },
    {
        "Company": "BioLife",
        "Date": "2015-01-25",
        "Open Price": 171.69,
        "Volume": 2657234
    },
    {
        "Company": "AeroSystems",
        "Date": "2019-01-26",
        "Open Price": 550.83,
        "Volume": 3642932
    },
    {
        "Company": "GreenEnergy",
        "Date": "2012-07-05",
        "Open Price": 454.16,
        "Volume": 3374263
    },
    {
        "Company": "TechnoCorp",
        "Date": "2019-06-22",
        "Open Price": 964.59,
        "Volume": 2483629
    },
    {
        "Company": "TechnoCorp",
        "Date": "2014-07-28",
        "Open Price": 1421.44,
        "Volume": 4919150
    },
    {
        "Company": "RetailWorld",
        "Date": "2020-06-03",
        "Open Price": 215.36,
        "Volume": 6618021
    }
]
<end>Convert this plain text to CSV:
Title: Escape from Earth | Genre: Comedy
Title: Beyond the Veil | Genre: Thriller
Title: The Endless Horizon | Genre: Thriller
Title: The Final Voyage | Genre: Comedy
Title: The Final Voyage | Genre: Fantasy
Title: The Final Voyage | Genre: Sci-Fi
Title: Escape from Earth | Genre: Fantasy
Title: Beyond the Veil | Genre: Comedy
Title: Edge of Infinity | Genre: Comedy
<start>
Title,Genre
Escape from Earth,Comedy
Beyond the Veil,Thriller
The Endless Horizon,Thriller
The Final Voyage,Comedy
The Final Voyage,Fantasy
The Final Voyage,Sci-Fi
Escape from Earth,Fantasy
Beyond the Veil,Comedy
Edge of Infinity,Comedy
<end>Can you change this CSV into Plain text?
Device ID,Location,Reading Value,Timestamp
device-0089,Hallway,31.0,2022-08-21 01:28:44
device-0092,Garage,11.5,2022-10-09 12:14:31
device-0066,Bedroom,-22.72,2023-02-10 01:26:44
device-0009,Garden,-22.72,2021-03-19 21:57:23
device-0009,Bedroom,59.99,2023-10-19 13:05:22
device-0043,Living Room,29.19,2021-05-22 00:17:45
<start>
Device ID: device-0089 | Location: Hallway | Reading Value: 31.0 | Timestamp: 2022-08-21 01:28:44
Device ID: device-0092 | Location: Garage | Reading Value: 11.5 | Timestamp: 2022-10-09 12:14:31
Device ID: device-0066 | Location: Bedroom | Reading Value: -22.72 | Timestamp: 2023-02-10 01:26:44
Device ID: device-0009 | Location: Garden | Reading Value: -22.72 | Timestamp: 2021-03-19 21:57:23
Device ID: device-0009 | Location: Bedroom | Reading Value: 59.99 | Timestamp: 2023-10-19 13:05:22
Device ID: device-0043 | Location: Living Room | Reading Value: 29.19 | Timestamp: 2021-05-22 00:17:45
<end>Can you change this markdown into PLAIN TEXT?
| Device ID | Location | Timestamp |
| --- | --- | --- |
| device-0070 | Living Room | 2021-01-03 22:38:50 |
| device-0083 | Office | 2023-05-01 01:21:09 |
| device-0022 | Bedroom | 2023-10-24 09:42:58 |<start>
Device ID: device-0070 | Location: Living Room | Timestamp: 2021-01-03 22:38:50
Device ID: device-0083 | Location: Office | Timestamp: 2023-05-01 01:21:09
Device ID: device-0022 | Location: Bedroom | Timestamp: 2023-10-24 09:42:58
<end>Here's some Markdown data, can you convert it to json?
| Database Name | Cache Hit Ratio (%) | Connection Count | Average Latency (ms) |
| --- | --- | --- | --- |
| ProductsDB | 81.35 | 221 | 30.8 |
| OrdersDB | 79.54 | 37 | 72.25 |
| AnalyticsDB | 77.93 | 440 | 89.28 |
| UserDB | 77.04 | 163 | 13.11 |
| ProductsDB | 83.34 | 104 | 45.51 |
| LogsDB | 81.77 | 377 | 27.07 |
| AnalyticsDB | 77.93 | 375 | 23.68 |
| ProductsDB | 88.42 | 131 | 28.1 |
| OrdersDB | 98.61 | 390 | 29.18 |<start>
[
    {
        "Database Name": "ProductsDB",
        "Cache Hit Ratio (%)": 81.35,
        "Connection Count": 221,
        "Average Latency (ms)": 30.8
    },
    {
        "Database Name": "OrdersDB",
        "Cache Hit Ratio (%)": 79.54,
        "Connection Count": 37,
        "Average Latency (ms)": 72.25
    },
    {
        "Database Name": "AnalyticsDB",
        "Cache Hit Ratio (%)": 77.93,
        "Connection Count": 440,
        "Average Latency (ms)": 89.28
    },
    {
        "Database Name": "UserDB",
        "Cache Hit Ratio (%)": 77.04,
        "Connection Count": 163,
        "Average Latency (ms)": 13.11
    },
    {
        "Database Name": "ProductsDB",
        "Cache Hit Ratio (%)": 83.34,
        "Connection Count": 104,
        "Average Latency (ms)": 45.51
    },
    {
        "Database Name": "LogsDB",
        "Cache Hit Ratio (%)": 81.77,
        "Connection Count": 377,
        "Average Latency (ms)": 27.07
    },
    {
        "Database Name": "AnalyticsDB",
        "Cache Hit Ratio (%)": 77.93,
        "Connection Count": 375,
        "Average Latency (ms)": 23.68
    },
    {
        "Database Name": "ProductsDB",
        "Cache Hit Ratio (%)": 88.42,
        "Connection Count": 131,
        "Average Latency (ms)": 28.1
    },
    {
        "Database Name": "OrdersDB",
        "Cache Hit Ratio (%)": 98.61,
        "Connection Count": 390,
        "Average Latency (ms)": 29.18
    }
]
<end>Transform this Csv structure to a Markdown format:
Title,Author,Genre
Legends of the Rift,Kara Firebrand,Horror
The Forgotten World,Rowan Ashborne,Horror
Echoes of Eternity,Luna Silverleaf,Historical
Tales of the Brave,Galen Starfire,Science Fiction
Shadows of Solitude,Draven Blackthorn,Historical
Whispers of the Abyss,Thorne Ironwood,Horror
Echoes of Eternity,Isla Windrider,Horror
<start>
| Title | Author | Genre |
| --- | --- | --- |
| Legends of the Rift | Kara Firebrand | Horror |
| The Forgotten World | Rowan Ashborne | Horror |
| Echoes of Eternity | Luna Silverleaf | Historical |
| Tales of the Brave | Galen Starfire | Science Fiction |
| Shadows of Solitude | Draven Blackthorn | Historical |
| Whispers of the Abyss | Thorne Ironwood | Horror |
| Echoes of Eternity | Isla Windrider | Horror |
<end>Transform this Json structure to a CSV format:
[
    {
        "Product Name": "Thingamajig",
        "SKU": "SKU-1070",
        "Price": 160.34,
        "Stock Quantity": 250,
        "Category": "Electronics",
        "Supplier Name": "ACME Corp"
    },
    {
        "Product Name": "Whatchamacallit",
        "SKU": "SKU-1091",
        "Price": 177.95,
        "Stock Quantity": 24,
        "Category": "Sports",
        "Supplier Name": "Wonka Industries"
    },
    {
        "Product Name": "Whatchamacallit",
        "SKU": "SKU-1033",
        "Price": 108.74,
        "Stock Quantity": 211,
        "Category": "Household",
        "Supplier Name": "ACME Corp"
    },
    {
        "Product Name": "Whatchamacallit",
        "SKU": "SKU-1063",
        "Price": 12.54,
        "Stock Quantity": 330,
        "Category": "Toys",
        "Supplier Name": "Wayne Enterprises"
    },
    {
        "Product Name": "Apparatus",
        "SKU": "SKU-1060",
        "Price": 433.05,
        "Stock Quantity": 104,
        "Category": "Automotive",
        "Supplier Name": "Globex"
    }
]<start>
Product Name,SKU,Price,Stock Quantity,Category,Supplier Name
Thingamajig,SKU-1070,160.34,250,Electronics,ACME Corp
Whatchamacallit,SKU-1091,177.95,24,Sports,Wonka Industries
Whatchamacallit,SKU-1033,108.74,211,Household,ACME Corp
Whatchamacallit,SKU-1063,12.54,330,Toys,Wayne Enterprises
Apparatus,SKU-1060,433.05,104,Automotive,Globex
<end>Transform this yml structure to a markdown format:
- Age: 40
  Birth Month: August
  City: Los Angeles
  Income: 165000
  Name: Harley
- Age: 53
  Birth Month: October
  City: New York
  Income: 260000
  Name: Jeanne
- Age: 36
  Birth Month: July
  City: Nashville
  Income: 415000
  Name: Sarah
- Age: 51
  Birth Month: July
  City: Fort Worth
  Income: 380000
  Name: Wilbert
- Age: 53
  Birth Month: April
  City: Louisville
  Income: 65000
  Name: Henrietta
- Age: 26
  Birth Month: May
  City: Phoenix
  Income: 55000
  Name: Courtney
- Age: 62
  Birth Month: February
  City: Oklahoma City
  Income: 425000
  Name: Paula
- Age: 18
  Birth Month: July
  City: Fort Worth
  Income: 310000
  Name: Aria
- Age: 45
  Birth Month: August
  City: New York
  Income: 155000
  Name: Paulette
<start>
| Name | Age | Birth Month | City | Income |
| --- | --- | --- | --- | --- |
| Harley | 40 | August | Los Angeles | 165000 |
| Jeanne | 53 | October | New York | 260000 |
| Sarah | 36 | July | Nashville | 415000 |
| Wilbert | 51 | July | Fort Worth | 380000 |
| Henrietta | 53 | April | Louisville | 65000 |
| Courtney | 26 | May | Phoenix | 55000 |
| Paula | 62 | February | Oklahoma City | 425000 |
| Aria | 18 | July | Fort Worth | 310000 |
| Paulette | 45 | August | New York | 155000 |
<end>Can you change this plain text into markdown?
Genre: Action | Box Office Earnings (M): 943.39
Genre: Horror | Box Office Earnings (M): 347.61
Genre: Drama | Box Office Earnings (M): 71.43
Genre: Drama | Box Office Earnings (M): 230.08
Genre: Drama | Box Office Earnings (M): 242.6
<start>
| Genre | Box Office Earnings (M) |
| --- | --- |
| Action | 943.39 |
| Horror | 347.61 |
| Drama | 71.43 |
| Drama | 230.08 |
| Drama | 242.6 |
<end>Transform this Json structure to a plain text format:
[
    {
        "Device ID": "device-0012",
        "Device Type": "Temperature Sensor",
        "Battery Level (%)": 76.3,
        "Reading Value": 83.03,
        "Timestamp": "2021-01-12 20:39:10"
    },
    {
        "Device ID": "device-0003",
        "Device Type": "Light Sensor",
        "Battery Level (%)": 24.1,
        "Reading Value": 31.33,
        "Timestamp": "2023-04-12 13:28:46"
    },
    {
        "Device ID": "device-0032",
        "Device Type": "Motion Detector",
        "Battery Level (%)": 91.5,
        "Reading Value": 19.37,
        "Timestamp": "2021-09-11 12:09:34"
    }
]<start>
Device ID: device-0012 | Device Type: Temperature Sensor | Battery Level (%): 76.3 | Reading Value: 83.03 | Timestamp: 2021-01-12 20:39:10
Device ID: device-0003 | Device Type: Light Sensor | Battery Level (%): 24.1 | Reading Value: 31.33 | Timestamp: 2023-04-12 13:28:46
Device ID: device-0032 | Device Type: Motion Detector | Battery Level (%): 91.5 | Reading Value: 19.37 | Timestamp: 2021-09-11 12:09:34
<end>Convert this Csv to plain text:
Company,Open Price,Close Price,High Price,Low Price,Volume
FinanceTrust,643.63,492.73,643.63,222.45,4134122
AeroSystems,149.04,616.22,616.22,113.08,4947603
RetailWorld,1104.39,1281.98,1281.98,197.65,5833494
MediaGroup,945.44,159.83,945.44,159.83,4045769
AeroSystems,1307.01,1104.39,1307.01,197.65,1389073
AutoMotive,373.78,552.48,552.48,373.78,1888948
GreenEnergy,717.71,85.96,717.71,85.96,5890443
HealthGen,1056.48,1048.65,1056.48,19.9,6189265
BioLife,765.27,961.36,961.36,172.74,1111682
<start>
Company: FinanceTrust | Open Price: 643.63 | Close Price: 492.73 | High Price: 643.63 | Low Price: 222.45 | Volume: 4134122
Company: AeroSystems | Open Price: 149.04 | Close Price: 616.22 | High Price: 616.22 | Low Price: 113.08 | Volume: 4947603
Company: RetailWorld | Open Price: 1104.39 | Close Price: 1281.98 | High Price: 1281.98 | Low Price: 197.65 | Volume: 5833494
Company: MediaGroup | Open Price: 945.44 | Close Price: 159.83 | High Price: 945.44 | Low Price: 159.83 | Volume: 4045769
Company: AeroSystems | Open Price: 1307.01 | Close Price: 1104.39 | High Price: 1307.01 | Low Price: 197.65 | Volume: 1389073
Company: AutoMotive | Open Price: 373.78 | Close Price: 552.48 | High Price: 552.48 | Low Price: 373.78 | Volume: 1888948
Company: GreenEnergy | Open Price: 717.71 | Close Price: 85.96 | High Price: 717.71 | Low Price: 85.96 | Volume: 5890443
Company: HealthGen | Open Price: 1056.48 | Close Price: 1048.65 | High Price: 1056.48 | Low Price: 19.9 | Volume: 6189265
Company: BioLife | Open Price: 765.27 | Close Price: 961.36 | High Price: 961.36 | Low Price: 172.74 | Volume: 1111682
<end>Transform this Csv structure to a yml format:
Company,Date,Open Price,Close Price,High Price,Volume
HealthGen,2018-04-09,290.55,1360.11,1360.11,9825732
GreenEnergy,2023-07-20,1270.88,1497.88,1497.88,4517257
MediaGroup,2018-01-07,82.72,281.77,805.25,4643140
FoodChain,2017-04-05,587.95,1485.33,1485.33,8026112
AeroSystems,2016-02-15,69.83,513.19,1497.88,5014386
AutoMotive,2012-09-13,1166.54,49.84,1341.73,2649436
RetailWorld,2018-09-18,1455.37,55.53,1455.37,2365636
<start>
- Close Price: 1360.11
  Company: HealthGen
  Date: '2018-04-09'
  High Price: 1360.11
  Open Price: 290.55
  Volume: 9825732
- Close Price: 1497.88
  Company: GreenEnergy
  Date: '2023-07-20'
  High Price: 1497.88
  Open Price: 1270.88
  Volume: 4517257
- Close Price: 281.77
  Company: MediaGroup
  Date: '2018-01-07'
  High Price: 805.25
  Open Price: 82.72
  Volume: 4643140
- Close Price: 1485.33
  Company: FoodChain
  Date: '2017-04-05'
  High Price: 1485.33
  Open Price: 587.95
  Volume: 8026112
- Close Price: 513.19
  Company: AeroSystems
  Date: '2016-02-15'
  High Price: 1497.88
  Open Price: 69.83
  Volume: 5014386
- Close Price: 49.84
  Company: AutoMotive
  Date: '2012-09-13'
  High Price: 1341.73
  Open Price: 1166.54
  Volume: 2649436
- Close Price: 55.53
  Company: RetailWorld
  Date: '2018-09-18'
  High Price: 1455.37
  Open Price: 1455.37
  Volume: 2365636
<end>Convert this plain text to markdown:
Age: 64 | Birth Month: February | City: Los Angeles | Income: 475000
Age: 23 | Birth Month: May | City: El Paso | Income: 125000
Age: 28 | Birth Month: December | City: Seattle | Income: 365000
Age: 57 | Birth Month: January | City: Indianapolis | Income: 90000
Age: 48 | Birth Month: January | City: San Jose | Income: 285000
Age: 57 | Birth Month: August | City: El Paso | Income: 115000
Age: 50 | Birth Month: December | City: San Jose | Income: 405000
Age: 30 | Birth Month: November | City: Detroit | Income: 170000
<start>
| Age | Birth Month | City | Income |
| --- | --- | --- | --- |
| 64 | February | Los Angeles | 475000 |
| 23 | May | El Paso | 125000 |
| 28 | December | Seattle | 365000 |
| 57 | January | Indianapolis | 90000 |
| 48 | January | San Jose | 285000 |
| 57 | August | El Paso | 115000 |
| 50 | December | San Jose | 405000 |
| 30 | November | Detroit | 170000 |
<end>Transform this markdown structure to a yml format:
| Name | Age | City |
| --- | --- | --- |
| Rachael | 54 | Detroit |
| Emilia | 19 | Detroit |
| Dewey | 23 | Denver |
| Erma | 48 | Jacksonville |
| Roberta | 51 | Washington |
| Dick | 19 | Chicago |
| Gladys | 39 | Charlotte |
| Thomas | 47 | Oklahoma City |
| Stefanie | 59 | Dallas |<start>
- Age: 54
  City: Detroit
  Name: Rachael
- Age: 19
  City: Detroit
  Name: Emilia
- Age: 23
  City: Denver
  Name: Dewey
- Age: 48
  City: Jacksonville
  Name: Erma
- Age: 51
  City: Washington
  Name: Roberta
- Age: 19
  City: Chicago
  Name: Dick
- Age: 39
  City: Charlotte
  Name: Gladys
- Age: 47
  City: Oklahoma City
  Name: Thomas
- Age: 59
  City: Dallas
  Name: Stefanie
<end>Convert this csv to json:
Location,Condition,Temperature (C),Humidity (%),Wind Speed (km/h)
New York,Cloudy,20.2,42,16.0
Seattle,Stormy,37.8,60,10.2
Phoenix,Rainy,12.5,50,15.7
Los Angeles,Windy,3.6,65,16.0
Los Angeles,Snowy,10.7,37,25.4
Chicago,Cloudy,24.9,56,5.0
Houston,Snowy,-9.7,58,29.2
Los Angeles,Stormy,-5.0,25,17.6
<start>
[
    {
        "Location": "New York",
        "Condition": "Cloudy",
        "Temperature (C)": 20.2,
        "Humidity (%)": 42,
        "Wind Speed (km/h)": 16.0
    },
    {
        "Location": "Seattle",
        "Condition": "Stormy",
        "Temperature (C)": 37.8,
        "Humidity (%)": 60,
        "Wind Speed (km/h)": 10.2
    },
    {
        "Location": "Phoenix",
        "Condition": "Rainy",
        "Temperature (C)": 12.5,
        "Humidity (%)": 50,
        "Wind Speed (km/h)": 15.7
    },
    {
        "Location": "Los Angeles",
        "Condition": "Windy",
        "Temperature (C)": 3.6,
        "Humidity (%)": 65,
        "Wind Speed (km/h)": 16.0
    },
    {
        "Location": "Los Angeles",
        "Condition": "Snowy",
        "Temperature (C)": 10.7,
        "Humidity (%)": 37,
        "Wind Speed (km/h)": 25.4
    },
    {
        "Location": "Chicago",
        "Condition": "Cloudy",
        "Temperature (C)": 24.9,
        "Humidity (%)": 56,
        "Wind Speed (km/h)": 5.0
    },
    {
        "Location": "Houston",
        "Condition": "Snowy",
        "Temperature (C)": -9.7,
        "Humidity (%)": 58,
        "Wind Speed (km/h)": 29.2
    },
    {
        "Location": "Los Angeles",
        "Condition": "Stormy",
        "Temperature (C)": -5.0,
        "Humidity (%)": 25,
        "Wind Speed (km/h)": 17.6
    }
]
<end>Please transform the following plain text data into markdown:
Trip Name: Canyon Trek | Start Location: Chicago | Distance (miles): 722.7 | Fuel Used (gallons): 65.6
Trip Name: Highway Odyssey | Start Location: San Francisco | Distance (miles): 1547.7 | Fuel Used (gallons): 22.0
Trip Name: Historic Route | Start Location: Chicago | Distance (miles): 2772.9 | Fuel Used (gallons): 45.8
Trip Name: Desert Drive | Start Location: San Francisco | Distance (miles): 555.5 | Fuel Used (gallons): 92.1
Trip Name: Lakeside Retreat | Start Location: San Francisco | Distance (miles): 1451.7 | Fuel Used (gallons): 7.7
<start>
| Trip Name | Start Location | Distance (miles) | Fuel Used (gallons) |
| --- | --- | --- | --- |
| Canyon Trek | Chicago | 722.7 | 65.6 |
| Highway Odyssey | San Francisco | 1547.7 | 22.0 |
| Historic Route | Chicago | 2772.9 | 45.8 |
| Desert Drive | San Francisco | 555.5 | 92.1 |
| Lakeside Retreat | San Francisco | 1451.7 | 7.7 |
<end>Please transform the following json data into CSV:
[
    {
        "Device Type": "Motion Detector",
        "Location": "Bedroom",
        "Battery Level (%)": 95.7,
        "Reading Value": 22.66
    },
    {
        "Device Type": "Temperature Sensor",
        "Location": "Garden",
        "Battery Level (%)": 44.1,
        "Reading Value": 58.08
    },
    {
        "Device Type": "Pressure Sensor",
        "Location": "Kitchen",
        "Battery Level (%)": 99.7,
        "Reading Value": 20.72
    },
    {
        "Device Type": "Humidity Sensor",
        "Location": "Hallway",
        "Battery Level (%)": 38.5,
        "Reading Value": -20.71
    },
    {
        "Device Type": "Pressure Sensor",
        "Location": "Office",
        "Battery Level (%)": 92.0,
        "Reading Value": 49.3
    },
    {
        "Device Type": "Light Sensor",
        "Location": "Bedroom",
        "Battery Level (%)": 97.3,
        "Reading Value": -30.59
    },
    {
        "Device Type": "Motion Detector",
        "Location": "Office",
        "Battery Level (%)": 83.1,
        "Reading Value": 62.84
    },
    {
        "Device Type": "Humidity Sensor",
        "Location": "Kitchen",
        "Battery Level (%)": 45.8,
        "Reading Value": -25.99
    },
    {
        "Device Type": "Humidity Sensor",
        "Location": "Bathroom",
        "Battery Level (%)": 70.5,
        "Reading Value": 75.99
    }
]<start>
Device Type,Location,Battery Level (%),Reading Value
Motion Detector,Bedroom,95.7,22.66
Temperature Sensor,Garden,44.1,58.08
Pressure Sensor,Kitchen,99.7,20.72
Humidity Sensor,Hallway,38.5,-20.71
Pressure Sensor,Office,92.0,49.3
Light Sensor,Bedroom,97.3,-30.59
Motion Detector,Office,83.1,62.84
Humidity Sensor,Kitchen,45.8,-25.99
Humidity Sensor,Bathroom,70.5,75.99
<end>Convert this Csv to Plain text:
Product Name,Price,Category,Supplier Name
Doohickey,257.56,Electronics,Wonka Industries
Gizmo,88.64,Toys,Umbrella Corp
Apparatus,431.47,Automotive,Umbrella Corp
Widget,349.06,Sports,Umbrella Corp
Contraption,269.13,Toys,Umbrella Corp
<start>
Product Name: Doohickey | Price: 257.56 | Category: Electronics | Supplier Name: Wonka Industries
Product Name: Gizmo | Price: 88.64 | Category: Toys | Supplier Name: Umbrella Corp
Product Name: Apparatus | Price: 431.47 | Category: Automotive | Supplier Name: Umbrella Corp
Product Name: Widget | Price: 349.06 | Category: Sports | Supplier Name: Umbrella Corp
Product Name: Contraption | Price: 269.13 | Category: Toys | Supplier Name: Umbrella Corp
<end>Here's some YAML data, can you convert it to csv?
- Genre: Mystery
  Rating: 2.4
  Title: Tales of the Brave
- Genre: Science Fiction
  Rating: 3.1
  Title: The Crystal Key
- Genre: Non-Fiction
  Rating: 3.8
  Title: The Crystal Key
- Genre: Mystery
  Rating: 2.4
  Title: The Crystal Key
<start>
Title,Genre,Rating
Tales of the Brave,Mystery,2.4
The Crystal Key,Science Fiction,3.1
The Crystal Key,Non-Fiction,3.8
The Crystal Key,Mystery,2.4
<end>Please transform the following YML data into JSON:
- Category: Electronics
  Price: 474.47
  Product Name: Whatchamacallit
  SKU: SKU-1004
  Stock Quantity: 97
  Supplier Name: Wayne Enterprises
- Category: Electronics
  Price: 372.82
  Product Name: Apparatus
  SKU: SKU-1045
  Stock Quantity: 134
  Supplier Name: ACME Corp
- Category: Toys
  Price: 16.23
  Product Name: Doohickey
  SKU: SKU-1070
  Stock Quantity: 168
  Supplier Name: Globex
- Category: Toys
  Price: 218.45
  Product Name: Gizmo
  SKU: SKU-1098
  Stock Quantity: 185
  Supplier Name: Umbrella Corp
- Category: Sports
  Price: 287.04
  Product Name: Gadget
  SKU: SKU-1018
  Stock Quantity: 132
  Supplier Name: Wayne Enterprises
- Category: Automotive
  Price: 118.11
  Product Name: Apparatus
  SKU: SKU-1071
  Stock Quantity: 69
  Supplier Name: ACME Corp
<start>
[
    {
        "Product Name": "Whatchamacallit",
        "SKU": "SKU-1004",
        "Price": 474.47,
        "Stock Quantity": 97,
        "Category": "Electronics",
        "Supplier Name": "Wayne Enterprises"
    },
    {
        "Product Name": "Apparatus",
        "SKU": "SKU-1045",
        "Price": 372.82,
        "Stock Quantity": 134,
        "Category": "Electronics",
        "Supplier Name": "ACME Corp"
    },
    {
        "Product Name": "Doohickey",
        "SKU": "SKU-1070",
        "Price": 16.23,
        "Stock Quantity": 168,
        "Category": "Toys",
        "Supplier Name": "Globex"
    },
    {
        "Product Name": "Gizmo",
        "SKU": "SKU-1098",
        "Price": 218.45,
        "Stock Quantity": 185,
        "Category": "Toys",
        "Supplier Name": "Umbrella Corp"
    },
    {
        "Product Name": "Gadget",
        "SKU": "SKU-1018",
        "Price": 287.04,
        "Stock Quantity": 132,
        "Category": "Sports",
        "Supplier Name": "Wayne Enterprises"
    },
    {
        "Product Name": "Apparatus",
        "SKU": "SKU-1071",
        "Price": 118.11,
        "Stock Quantity": 69,
        "Category": "Automotive",
        "Supplier Name": "ACME Corp"
    }
]
<end>Transform this Yml structure to a Csv format:
- Condition: Stormy
  Humidity (%): 56
  Location: Phoenix
  Temperature (C): 30.2
  Wind Speed (km/h): 13.0
- Condition: Sunny
  Humidity (%): 63
  Location: Miami
  Temperature (C): 31.0
  Wind Speed (km/h): 4.1
- Condition: Sunny
  Humidity (%): 71
  Location: New York
  Temperature (C): 29.9
  Wind Speed (km/h): 16.5
- Condition: Cloudy
  Humidity (%): 53
  Location: New York
  Temperature (C): -7.4
  Wind Speed (km/h): 4.7
- Condition: Windy
  Humidity (%): 35
  Location: Houston
  Temperature (C): 16.4
  Wind Speed (km/h): 21.4
- Condition: Sunny
  Humidity (%): 45
  Location: Seattle
  Temperature (C): 5.6
  Wind Speed (km/h): 8.2
- Condition: Windy
  Humidity (%): 25
  Location: Seattle
  Temperature (C): 24.1
  Wind Speed (km/h): 29.8
- Condition: Stormy
  Humidity (%): 88
  Location: Houston
  Temperature (C): 28.3
  Wind Speed (km/h): 6.0
<start>
Location,Condition,Temperature (C),Humidity (%),Wind Speed (km/h)
Phoenix,Stormy,30.2,56,13.0
Miami,Sunny,31.0,63,4.1
New York,Sunny,29.9,71,16.5
New York,Cloudy,-7.4,53,4.7
Houston,Windy,16.4,35,21.4
Seattle,Sunny,5.6,45,8.2
Seattle,Windy,24.1,25,29.8
Houston,Stormy,28.3,88,6.0
<end>Please transform the following json data into yml:
[
    {
        "Name": "Freddie",
        "Age": 48,
        "Birth Month": "June",
        "City": "Phoenix",
        "Income": 80000
    },
    {
        "Name": "Erin",
        "Age": 64,
        "Birth Month": "January",
        "City": "Washington",
        "Income": 290000
    },
    {
        "Name": "Alexia",
        "Age": 57,
        "Birth Month": "April",
        "City": "Seattle",
        "Income": 155000
    },
    {
        "Name": "Irma",
        "Age": 24,
        "Birth Month": "February",
        "City": "Austin",
        "Income": 410000
    },
    {
        "Name": "Clinton",
        "Age": 48,
        "Birth Month": "August",
        "City": "Washington",
        "Income": 385000
    },
    {
        "Name": "Amelia",
        "Age": 28,
        "Birth Month": "March",
        "City": "New York",
        "Income": 495000
    },
    {
        "Name": "Mandy",
        "Age": 30,
        "Birth Month": "October",
        "City": "Milwaukee",
        "Income": 45000
    },
    {
        "Name": "August",
        "Age": 27,
        "Birth Month": "July",
        "City": "San Jose",
        "Income": 175000
    },
    {
        "Name": "Jazmin",
        "Age": 60,
        "Birth Month": "January",
        "City": "Columbus",
        "Income": 230000
    }
]<start>
- Age: 48
  Birth Month: June
  City: Phoenix
  Income: 80000
  Name: Freddie
- Age: 64
  Birth Month: January
  City: Washington
  Income: 290000
  Name: Erin
- Age: 57
  Birth Month: April
  City: Seattle
  Income: 155000
  Name: Alexia
- Age: 24
  Birth Month: February
  City: Austin
  Income: 410000
  Name: Irma
- Age: 48
  Birth Month: August
  City: Washington
  Income: 385000
  Name: Clinton
- Age: 28
  Birth Month: March
  City: New York
  Income: 495000
  Name: Amelia
- Age: 30
  Birth Month: October
  City: Milwaukee
  Income: 45000
  Name: Mandy
- Age: 27
  Birth Month: July
  City: San Jose
  Income: 175000
  Name: August
- Age: 60
  Birth Month: January
  City: Columbus
  Income: 230000
  Name: Jazmin
<end>Please transform the following yml data into csv:
- Battery Level (%): 23.8
  Device ID: device-0083
  Device Type: Humidity Sensor
  Location: Garage
  Reading Value: -23.87
- Battery Level (%): 23.8
  Device ID: device-0064
  Device Type: Motion Detector
  Location: Living Room
  Reading Value: 40.51
- Battery Level (%): 21.3
  Device ID: device-0076
  Device Type: Pressure Sensor
  Location: Garden
  Reading Value: -18.24
- Battery Level (%): 96.2
  Device ID: device-0025
  Device Type: Pressure Sensor
  Location: Kitchen
  Reading Value: -24.06
- Battery Level (%): 29.0
  Device ID: device-0097
  Device Type: Light Sensor
  Location: Bathroom
  Reading Value: 12.67
- Battery Level (%): 69.2
  Device ID: device-0093
  Device Type: Motion Detector
  Location: Kitchen
  Reading Value: 54.14
- Battery Level (%): 48.8
  Device ID: device-0003
  Device Type: Humidity Sensor
  Location: Garden
  Reading Value: 30.93
- Battery Level (%): 33.3
  Device ID: device-0051
  Device Type: Pressure Sensor
  Location: Bathroom
  Reading Value: -36.71
- Battery Level (%): 74.9
  Device ID: device-0012
  Device Type: Pressure Sensor
  Location: Office
  Reading Value: 24.59
<start>
Device ID,Device Type,Location,Battery Level (%),Reading Value
device-0083,Humidity Sensor,Garage,23.8,-23.87
device-0064,Motion Detector,Living Room,23.8,40.51
device-0076,Pressure Sensor,Garden,21.3,-18.24
device-0025,Pressure Sensor,Kitchen,96.2,-24.06
device-0097,Light Sensor,Bathroom,29.0,12.67
device-0093,Motion Detector,Kitchen,69.2,54.14
device-0003,Humidity Sensor,Garden,48.8,30.93
device-0051,Pressure Sensor,Bathroom,33.3,-36.71
device-0012,Pressure Sensor,Office,74.9,24.59
<end>Please transform the following plain text data into csv:
Queries per Second: 531.21 | Cache Hit Ratio (%): 99.5 | Connection Count: 359
Queries per Second: 3717.46 | Cache Hit Ratio (%): 86.74 | Connection Count: 121
Queries per Second: 3959.27 | Cache Hit Ratio (%): 89.8 | Connection Count: 275
Queries per Second: 3405.7 | Cache Hit Ratio (%): 73.95 | Connection Count: 14
Queries per Second: 3437.84 | Cache Hit Ratio (%): 90.03 | Connection Count: 196
<start>
Queries per Second,Cache Hit Ratio (%),Connection Count
531.21,99.5,359
3717.46,86.74,121
3959.27,89.8,275
3405.7,73.95,14
3437.84,90.03,196
<end>Transform this json structure to a plain text format:
[
    {
        "Location": "Phoenix",
        "Temperature (C)": 34.0,
        "Humidity (%)": 72
    },
    {
        "Location": "Los Angeles",
        "Temperature (C)": 12.2,
        "Humidity (%)": 43
    },
    {
        "Location": "Miami",
        "Temperature (C)": 1.1,
        "Humidity (%)": 36
    },
    {
        "Location": "Seattle",
        "Temperature (C)": 7.0,
        "Humidity (%)": 32
    },
    {
        "Location": "Los Angeles",
        "Temperature (C)": 12.2,
        "Humidity (%)": 30
    },
    {
        "Location": "Chicago",
        "Temperature (C)": 2.1,
        "Humidity (%)": 34
    },
    {
        "Location": "Seattle",
        "Temperature (C)": 1.1,
        "Humidity (%)": 36
    },
    {
        "Location": "Denver",
        "Temperature (C)": 27.0,
        "Humidity (%)": 39
    },
    {
        "Location": "Chicago",
        "Temperature (C)": 0.8,
        "Humidity (%)": 58
    },
    {
        "Location": "Miami",
        "Temperature (C)": -8.8,
        "Humidity (%)": 30
    }
]<start>
Location: Phoenix | Temperature (C): 34.0 | Humidity (%): 72
Location: Los Angeles | Temperature (C): 12.2 | Humidity (%): 43
Location: Miami | Temperature (C): 1.1 | Humidity (%): 36
Location: Seattle | Temperature (C): 7.0 | Humidity (%): 32
Location: Los Angeles | Temperature (C): 12.2 | Humidity (%): 30
Location: Chicago | Temperature (C): 2.1 | Humidity (%): 34
Location: Seattle | Temperature (C): 1.1 | Humidity (%): 36
Location: Denver | Temperature (C): 27.0 | Humidity (%): 39
Location: Chicago | Temperature (C): 0.8 | Humidity (%): 58
Location: Miami | Temperature (C): -8.8 | Humidity (%): 30
<end>Can you change this json into YAML?
[
    {
        "Trip Name": "Mountain Adventure",
        "Start Location": "Houston",
        "End Location": "New York",
        "Distance (miles)": 2477.5,
        "Duration (hours)": 71.3,
        "Fuel Used (gallons)": 35.4
    },
    {
        "Trip Name": "Lakeside Retreat",
        "Start Location": "San Francisco",
        "End Location": "Los Angeles",
        "Distance (miles)": 2227.1,
        "Duration (hours)": 29.2,
        "Fuel Used (gallons)": 74.4
    },
    {
        "Trip Name": "Highway Odyssey",
        "Start Location": "Denver",
        "End Location": "Los Angeles",
        "Distance (miles)": 2173.9,
        "Duration (hours)": 28.2,
        "Fuel Used (gallons)": 35.4
    },
    {
        "Trip Name": "Canyon Trek",
        "Start Location": "San Francisco",
        "End Location": "Denver",
        "Distance (miles)": 1753.3,
        "Duration (hours)": 39.6,
        "Fuel Used (gallons)": 18.0
    },
    {
        "Trip Name": "Mountain Adventure",
        "Start Location": "Chicago",
        "End Location": "San Francisco",
        "Distance (miles)": 777.8,
        "Duration (hours)": 24.0,
        "Fuel Used (gallons)": 68.8
    },
    {
        "Trip Name": "Valley Voyage",
        "Start Location": "New York",
        "End Location": "Houston",
        "Distance (miles)": 444.8,
        "Duration (hours)": 39.6,
        "Fuel Used (gallons)": 27.3
    },
    {
        "Trip Name": "Lakeside Retreat",
        "Start Location": "Los Angeles",
        "End Location": "Denver",
        "Distance (miles)": 1077.8,
        "Duration (hours)": 8.7,
        "Fuel Used (gallons)": 72.0
    },
    {
        "Trip Name": "Desert Drive",
        "Start Location": "Houston",
        "End Location": "New York",
        "Distance (miles)": 1854.5,
        "Duration (hours)": 26.5,
        "Fuel Used (gallons)": 94.6
    }
]<start>
- Distance (miles): 2477.5
  Duration (hours): 71.3
  End Location: New York
  Fuel Used (gallons): 35.4
  Start Location: Houston
  Trip Name: Mountain Adventure
- Distance (miles): 2227.1
  Duration (hours): 29.2
  End Location: Los Angeles
  Fuel Used (gallons): 74.4
  Start Location: San Francisco
  Trip Name: Lakeside Retreat
- Distance (miles): 2173.9
  Duration (hours): 28.2
  End Location: Los Angeles
  Fuel Used (gallons): 35.4
  Start Location: Denver
  Trip Name: Highway Odyssey
- Distance (miles): 1753.3
  Duration (hours): 39.6
  End Location: Denver
  Fuel Used (gallons): 18.0
  Start Location: San Francisco
  Trip Name: Canyon Trek
- Distance (miles): 777.8
  Duration (hours): 24.0
  End Location: San Francisco
  Fuel Used (gallons): 68.8
  Start Location: Chicago
  Trip Name: Mountain Adventure
- Distance (miles): 444.8
  Duration (hours): 39.6
  End Location: Houston
  Fuel Used (gallons): 27.3
  Start Location: New York
  Trip Name: Valley Voyage
- Distance (miles): 1077.8
  Duration (hours): 8.7
  End Location: Denver
  Fuel Used (gallons): 72.0
  Start Location: Los Angeles
  Trip Name: Lakeside Retreat
- Distance (miles): 1854.5
  Duration (hours): 26.5
  End Location: New York
  Fuel Used (gallons): 94.6
  Start Location: Houston
  Trip Name: Desert Drive
<end>Can you change this plain text into Yaml?
Company: BioLife | Date: 2014-10-24 | Open Price: 230.07 | Close Price: 682.01 | High Price: 682.01 | Low Price: 230.07 | Volume: 6962029
Company: AutoMotive | Date: 2023-12-25 | Open Price: 1489.77 | Close Price: 1224.3 | High Price: 1489.77 | Low Price: 1036.38 | Volume: 7462941
Company: FinanceTrust | Date: 2020-10-03 | Open Price: 1391.18 | Close Price: 939.17 | High Price: 1391.18 | Low Price: 704.59 | Volume: 6721325
Company: FoodChain | Date: 2022-05-17 | Open Price: 1333.33 | Close Price: 23.47 | High Price: 1333.33 | Low Price: 23.47 | Volume: 4672038
Company: GreenEnergy | Date: 2010-11-05 | Open Price: 504.02 | Close Price: 946.5 | High Price: 1090.83 | Low Price: 230.07 | Volume: 4502283
Company: BioLife | Date: 2013-09-03 | Open Price: 867.83 | Close Price: 1084.45 | High Price: 1386.47 | Low Price: 211.92 | Volume: 3716439
<start>
- Close Price: 682.01
  Company: BioLife
  Date: '2014-10-24'
  High Price: 682.01
  Low Price: 230.07
  Open Price: 230.07
  Volume: 6962029
- Close Price: 1224.3
  Company: AutoMotive
  Date: '2023-12-25'
  High Price: 1489.77
  Low Price: 1036.38
  Open Price: 1489.77
  Volume: 7462941
- Close Price: 939.17
  Company: FinanceTrust
  Date: '2020-10-03'
  High Price: 1391.18
  Low Price: 704.59
  Open Price: 1391.18
  Volume: 6721325
- Close Price: 23.47
  Company: FoodChain
  Date: '2022-05-17'
  High Price: 1333.33
  Low Price: 23.47
  Open Price: 1333.33
  Volume: 4672038
- Close Price: 946.5
  Company: GreenEnergy
  Date: '2010-11-05'
  High Price: 1090.83
  Low Price: 230.07
  Open Price: 504.02
  Volume: 4502283
- Close Price: 1084.45
  Company: BioLife
  Date: '2013-09-03'
  High Price: 1386.47
  Low Price: 211.92
  Open Price: 867.83
  Volume: 3716439
<end>Please transform the following Plain text data into Json:
Company: BioPharm | Sector: Aerospace | Market Cap: Mega Cap | Quarter: Q3
Company: HealthPlus | Sector: Energy | Market Cap: Small Cap | Quarter: Q2
Company: HealthPlus | Sector: Finance | Market Cap: Large Cap | Quarter: Q4
Company: FinanceWorks | Sector: Healthcare | Market Cap: Mega Cap | Quarter: Q3
Company: AeroSpace | Sector: Biotech | Market Cap: Large Cap | Quarter: Q1
Company: BioPharm | Sector: Finance | Market Cap: Small Cap | Quarter: Q2
Company: TechCorp | Sector: Biotech | Market Cap: Large Cap | Quarter: Q3
Company: AeroSpace | Sector: Biotech | Market Cap: Large Cap | Quarter: Q1
<start>
[
    {
        "Company": "BioPharm",
        "Sector": "Aerospace",
        "Market Cap": "Mega Cap",
        "Quarter": "Q3"
    },
    {
        "Company": "HealthPlus",
        "Sector": "Energy",
        "Market Cap": "Small Cap",
        "Quarter": "Q2"
    },
    {
        "Company": "HealthPlus",
        "Sector": "Finance",
        "Market Cap": "Large Cap",
        "Quarter": "Q4"
    },
    {
        "Company": "FinanceWorks",
        "Sector": "Healthcare",
        "Market Cap": "Mega Cap",
        "Quarter": "Q3"
    },
    {
        "Company": "AeroSpace",
        "Sector": "Biotech",
        "Market Cap": "Large Cap",
        "Quarter": "Q1"
    },
    {
        "Company": "BioPharm",
        "Sector": "Finance",
        "Market Cap": "Small Cap",
        "Quarter": "Q2"
    },
    {
        "Company": "TechCorp",
        "Sector": "Biotech",
        "Market Cap": "Large Cap",
        "Quarter": "Q3"
    },
    {
        "Company": "AeroSpace",
        "Sector": "Biotech",
        "Market Cap": "Large Cap",
        "Quarter": "Q1"
    }
]
<end>Here's some plain text data, can you convert it to json?
Database Name: ProfilesDB | Queries per Second: 106.0 | Cache Hit Ratio (%): 94.84 | Connection Count: 50 | Average Latency (ms): 49.23
Database Name: OrdersDB | Queries per Second: 802.29 | Cache Hit Ratio (%): 74.1 | Connection Count: 352 | Average Latency (ms): 67.04
Database Name: OrdersDB | Queries per Second: 3966.72 | Cache Hit Ratio (%): 91.59 | Connection Count: 175 | Average Latency (ms): 61.54
Database Name: SessionsDB | Queries per Second: 2372.91 | Cache Hit Ratio (%): 93.61 | Connection Count: 326 | Average Latency (ms): 8.32
Database Name: InventoryDB | Queries per Second: 2735.67 | Cache Hit Ratio (%): 86.74 | Connection Count: 253 | Average Latency (ms): 96.73
Database Name: ProfilesDB | Queries per Second: 2743.82 | Cache Hit Ratio (%): 93.31 | Connection Count: 475 | Average Latency (ms): 86.89
Database Name: AnalyticsDB | Queries per Second: 1346.31 | Cache Hit Ratio (%): 97.82 | Connection Count: 335 | Average Latency (ms): 38.85
<start>
[
    {
        "Database Name": "ProfilesDB",
        "Queries per Second": 106.0,
        "Cache Hit Ratio (%)": 94.84,
        "Connection Count": 50,
        "Average Latency (ms)": 49.23
    },
    {
        "Database Name": "OrdersDB",
        "Queries per Second": 802.29,
        "Cache Hit Ratio (%)": 74.1,
        "Connection Count": 352,
        "Average Latency (ms)": 67.04
    },
    {
        "Database Name": "OrdersDB",
        "Queries per Second": 3966.72,
        "Cache Hit Ratio (%)": 91.59,
        "Connection Count": 175,
        "Average Latency (ms)": 61.54
    },
    {
        "Database Name": "SessionsDB",
        "Queries per Second": 2372.91,
        "Cache Hit Ratio (%)": 93.61,
        "Connection Count": 326,
        "Average Latency (ms)": 8.32
    },
    {
        "Database Name": "InventoryDB",
        "Queries per Second": 2735.67,
        "Cache Hit Ratio (%)": 86.74,
        "Connection Count": 253,
        "Average Latency (ms)": 96.73
    },
    {
        "Database Name": "ProfilesDB",
        "Queries per Second": 2743.82,
        "Cache Hit Ratio (%)": 93.31,
        "Connection Count": 475,
        "Average Latency (ms)": 86.89
    },
    {
        "Database Name": "AnalyticsDB",
        "Queries per Second": 1346.31,
        "Cache Hit Ratio (%)": 97.82,
        "Connection Count": 335,
        "Average Latency (ms)": 38.85
    }
]
<end>Here's some Json data, can you convert it to CSV?
[
    {
        "Restaurant Name": "Vegan Delight",
        "Price Range": "$$"
    },
    {
        "Restaurant Name": "The Golden Spoon",
        "Price Range": "$$$$"
    },
    {
        "Restaurant Name": "Pizza Planet",
        "Price Range": "$$$$"
    },
    {
        "Restaurant Name": "Pizza Planet",
        "Price Range": "$"
    }
]<start>
Restaurant Name,Price Range
Vegan Delight,$$
The Golden Spoon,$$$$
Pizza Planet,$$$$
Pizza Planet,$
<end>Transform this markdown structure to a json format:
| Title | Release Year | Box Office Earnings (M) |
| --- | --- | --- |
| The Great Expedition | 1974 | 885.05 |
| Rise of the Titans | 1983 | 843.73 |
| Dreamwalker | 2010 | 122.06 |
| Beyond the Veil | 1984 | 453.84 |
| Mystery of the Depths | 2004 | 885.05 |
| Starbound Odyssey | 1981 | 612.23 |
| Beyond the Veil | 1970 | 828.18 |<start>
[
    {
        "Title": "The Great Expedition",
        "Release Year": 1974,
        "Box Office Earnings (M)": 885.05
    },
    {
        "Title": "Rise of the Titans",
        "Release Year": 1983,
        "Box Office Earnings (M)": 843.73
    },
    {
        "Title": "Dreamwalker",
        "Release Year": 2010,
        "Box Office Earnings (M)": 122.06
    },
    {
        "Title": "Beyond the Veil",
        "Release Year": 1984,
        "Box Office Earnings (M)": 453.84
    },
    {
        "Title": "Mystery of the Depths",
        "Release Year": 2004,
        "Box Office Earnings (M)": 885.05
    },
    {
        "Title": "Starbound Odyssey",
        "Release Year": 1981,
        "Box Office Earnings (M)": 612.23
    },
    {
        "Title": "Beyond the Veil",
        "Release Year": 1970,
        "Box Office Earnings (M)": 828.18
    }
]
<end>Please transform the following plain text data into markdown:
Product Name: Gizmo | SKU: SKU-1044 | Price: 210.89 | Stock Quantity: 208 | Supplier Name: Wayne Enterprises
Product Name: Whatchamacallit | SKU: SKU-1056 | Price: 64.36 | Stock Quantity: 63 | Supplier Name: Globex
Product Name: Doohickey | SKU: SKU-1042 | Price: 126.3 | Stock Quantity: 449 | Supplier Name: Umbrella Corp
Product Name: Instrument | SKU: SKU-1097 | Price: 97.45 | Stock Quantity: 366 | Supplier Name: Globex
Product Name: Gizmo | SKU: SKU-1052 | Price: 188.99 | Stock Quantity: 461 | Supplier Name: Globex
Product Name: Instrument | SKU: SKU-1092 | Price: 65.45 | Stock Quantity: 413 | Supplier Name: Wayne Enterprises
Product Name: Device | SKU: SKU-1065 | Price: 90.45 | Stock Quantity: 58 | Supplier Name: ACME Corp
Product Name: Whatchamacallit | SKU: SKU-1044 | Price: 21.3 | Stock Quantity: 467 | Supplier Name: Globex
<start>
| Product Name | SKU | Price | Stock Quantity | Supplier Name |
| --- | --- | --- | --- | --- |
| Gizmo | SKU-1044 | 210.89 | 208 | Wayne Enterprises |
| Whatchamacallit | SKU-1056 | 64.36 | 63 | Globex |
| Doohickey | SKU-1042 | 126.3 | 449 | Umbrella Corp |
| Instrument | SKU-1097 | 97.45 | 366 | Globex |
| Gizmo | SKU-1052 | 188.99 | 461 | Globex |
| Instrument | SKU-1092 | 65.45 | 413 | Wayne Enterprises |
| Device | SKU-1065 | 90.45 | 58 | ACME Corp |
| Whatchamacallit | SKU-1044 | 21.3 | 467 | Globex |
<end>Here's some PLAIN TEXT data, can you convert it to csv?
Restaurant Name: BBQ Barn | Location: Los Angeles | Rating: 3
Restaurant Name: Taco Town | Location: Seattle | Rating: 1
Restaurant Name: Sushi World | Location: New York | Rating: 1
Restaurant Name: The Golden Spoon | Location: Seattle | Rating: 4
<start>
Restaurant Name,Location,Rating
BBQ Barn,Los Angeles,3
Taco Town,Seattle,1
Sushi World,New York,1
The Golden Spoon,Seattle,4
<end>Here's some json data, can you convert it to MARKDOWN?
[
    {
        "Location": "Los Angeles",
        "Condition": "Stormy",
        "Temperature (C)": -9.8,
        "Humidity (%)": 78
    },
    {
        "Location": "Seattle",
        "Condition": "Rainy",
        "Temperature (C)": 28.9,
        "Humidity (%)": 33
    },
    {
        "Location": "Houston",
        "Condition": "Stormy",
        "Temperature (C)": 6.3,
        "Humidity (%)": 78
    },
    {
        "Location": "Houston",
        "Condition": "Snowy",
        "Temperature (C)": 18.6,
        "Humidity (%)": 37
    },
    {
        "Location": "New York",
        "Condition": "Windy",
        "Temperature (C)": 7.0,
        "Humidity (%)": 78
    }
]<start>
| Location | Condition | Temperature (C) | Humidity (%) |
| --- | --- | --- | --- |
| Los Angeles | Stormy | -9.8 | 78 |
| Seattle | Rainy | 28.9 | 33 |
| Houston | Stormy | 6.3 | 78 |
| Houston | Snowy | 18.6 | 37 |
| New York | Windy | 7.0 | 78 |
<end>Please transform the following json data into Markdown:
[
    {
        "Database Name": "AnalyticsDB",
        "Queries per Second": 4664.46,
        "Cache Hit Ratio (%)": 73.25,
        "Connection Count": 46,
        "Timestamp": "2021-09-17 15:14:49"
    },
    {
        "Database Name": "MetricsDB",
        "Queries per Second": 3021.84,
        "Cache Hit Ratio (%)": 84.95,
        "Connection Count": 47,
        "Timestamp": "2022-11-25 14:40:35"
    },
    {
        "Database Name": "OrdersDB",
        "Queries per Second": 3021.84,
        "Cache Hit Ratio (%)": 97.07,
        "Connection Count": 210,
        "Timestamp": "2021-02-16 10:17:01"
    },
    {
        "Database Name": "ProductsDB",
        "Queries per Second": 4589.66,
        "Cache Hit Ratio (%)": 98.59,
        "Connection Count": 448,
        "Timestamp": "2021-12-25 22:52:19"
    },
    {
        "Database Name": "SalesDB",
        "Queries per Second": 3125.38,
        "Cache Hit Ratio (%)": 79.16,
        "Connection Count": 246,
        "Timestamp": "2023-01-22 06:57:34"
    },
    {
        "Database Name": "UserDB",
        "Queries per Second": 1927.06,
        "Cache Hit Ratio (%)": 93.52,
        "Connection Count": 131,
        "Timestamp": "2022-02-25 22:08:30"
    },
    {
        "Database Name": "OrdersDB",
        "Queries per Second": 102.4,
        "Cache Hit Ratio (%)": 90.81,
        "Connection Count": 22,
        "Timestamp": "2021-03-16 12:13:36"
    },
    {
        "Database Name": "SalesDB",
        "Queries per Second": 4102.12,
        "Cache Hit Ratio (%)": 90.67,
        "Connection Count": 344,
        "Timestamp": "2022-02-19 17:28:15"
    }
]<start>
| Database Name | Queries per Second | Cache Hit Ratio (%) | Connection Count | Timestamp |
| --- | --- | --- | --- | --- |
| AnalyticsDB | 4664.46 | 73.25 | 46 | 2021-09-17 15:14:49 |
| MetricsDB | 3021.84 | 84.95 | 47 | 2022-11-25 14:40:35 |
| OrdersDB | 3021.84 | 97.07 | 210 | 2021-02-16 10:17:01 |
| ProductsDB | 4589.66 | 98.59 | 448 | 2021-12-25 22:52:19 |
| SalesDB | 3125.38 | 79.16 | 246 | 2023-01-22 06:57:34 |
| UserDB | 1927.06 | 93.52 | 131 | 2022-02-25 22:08:30 |
| OrdersDB | 102.4 | 90.81 | 22 | 2021-03-16 12:13:36 |
| SalesDB | 4102.12 | 90.67 | 344 | 2022-02-19 17:28:15 |
<end>Transform this json structure to a csv format:
[
    {
        "Product Name": "Doohickey",
        "SKU": "SKU-1020",
        "Price": 326.78,
        "Stock Quantity": 100,
        "Category": "Toys",
        "Supplier Name": "ACME Corp"
    },
    {
        "Product Name": "Gadget",
        "SKU": "SKU-1002",
        "Price": 218.05,
        "Stock Quantity": 33,
        "Category": "Electronics",
        "Supplier Name": "Wayne Enterprises"
    },
    {
        "Product Name": "Contraption",
        "SKU": "SKU-1033",
        "Price": 210.77,
        "Stock Quantity": 279,
        "Category": "Household",
        "Supplier Name": "Wayne Enterprises"
    },
    {
        "Product Name": "Widget",
        "SKU": "SKU-1038",
        "Price": 69.84,
        "Stock Quantity": 316,
        "Category": "Household",
        "Supplier Name": "Umbrella Corp"
    },
    {
        "Product Name": "Widget",
        "SKU": "SKU-1082",
        "Price": 383.78,
        "Stock Quantity": 67,
        "Category": "Household",
        "Supplier Name": "Wonka Industries"
    }
]<start>
Product Name,SKU,Price,Stock Quantity,Category,Supplier Name
Doohickey,SKU-1020,326.78,100,Toys,ACME Corp
Gadget,SKU-1002,218.05,33,Electronics,Wayne Enterprises
Contraption,SKU-1033,210.77,279,Household,Wayne Enterprises
Widget,SKU-1038,69.84,316,Household,Umbrella Corp
Widget,SKU-1082,383.78,67,Household,Wonka Industries
<end>Please transform the following MARKDOWN data into PLAIN TEXT:
| Title | Release Year | Box Office Earnings (M) |
| --- | --- | --- |
| Starbound Odyssey | 1988 | 499.29 |
| The Endless Horizon | 1998 | 222.3 |
| Mystery of the Depths | 1978 | 58.62 |
| Dreamwalker | 1996 | 110.79 |
| Mystery of the Depths | 1997 | 443.34 |
| Dreamwalker | 1976 | 219.23 |<start>
Title: Starbound Odyssey | Release Year: 1988 | Box Office Earnings (M): 499.29
Title: The Endless Horizon | Release Year: 1998 | Box Office Earnings (M): 222.3
Title: Mystery of the Depths | Release Year: 1978 | Box Office Earnings (M): 58.62
Title: Dreamwalker | Release Year: 1996 | Box Office Earnings (M): 110.79
Title: Mystery of the Depths | Release Year: 1997 | Box Office Earnings (M): 443.34
Title: Dreamwalker | Release Year: 1976 | Box Office Earnings (M): 219.23
<end>Here's some Yaml data, can you convert it to csv?
- Device ID: device-0076
  Device Type: Temperature Sensor
  Location: Living Room
  Reading Value: -15.01
  Timestamp: '2023-07-12 02:15:31'
- Device ID: device-0009
  Device Type: Light Sensor
  Location: Office
  Reading Value: -33.42
  Timestamp: '2021-09-20 02:51:40'
- Device ID: device-0087
  Device Type: Temperature Sensor
  Location: Hallway
  Reading Value: 48.83
  Timestamp: '2023-07-17 10:58:25'
- Device ID: device-0044
  Device Type: Pressure Sensor
  Location: Garage
  Reading Value: 13.12
  Timestamp: '2022-04-06 22:26:18'
- Device ID: device-0010
  Device Type: Motion Detector
  Location: Office
  Reading Value: 57.72
  Timestamp: '2023-09-10 15:49:25'
- Device ID: device-0082
  Device Type: Pressure Sensor
  Location: Living Room
  Reading Value: 49.29
  Timestamp: '2022-09-23 04:40:11'
- Device ID: device-0004
  Device Type: Motion Detector
  Location: Garden
  Reading Value: 23.58
  Timestamp: '2021-01-10 01:43:21'
- Device ID: device-0093
  Device Type: Pressure Sensor
  Location: Bedroom
  Reading Value: 49.21
  Timestamp: '2022-01-28 01:20:54'
- Device ID: device-0095
  Device Type: Humidity Sensor
  Location: Hallway
  Reading Value: 57.77
  Timestamp: '2021-02-20 17:51:03'
- Device ID: device-0058
  Device Type: Humidity Sensor
  Location: Garage
  Reading Value: 10.86
  Timestamp: '2021-11-25 05:37:58'
<start>
Device ID,Device Type,Location,Reading Value,Timestamp
device-0076,Temperature Sensor,Living Room,-15.01,2023-07-12 02:15:31
device-0009,Light Sensor,Office,-33.42,2021-09-20 02:51:40
device-0087,Temperature Sensor,Hallway,48.83,2023-07-17 10:58:25
device-0044,Pressure Sensor,Garage,13.12,2022-04-06 22:26:18
device-0010,Motion Detector,Office,57.72,2023-09-10 15:49:25
device-0082,Pressure Sensor,Living Room,49.29,2022-09-23 04:40:11
device-0004,Motion Detector,Garden,23.58,2021-01-10 01:43:21
device-0093,Pressure Sensor,Bedroom,49.21,2022-01-28 01:20:54
device-0095,Humidity Sensor,Hallway,57.77,2021-02-20 17:51:03
device-0058,Humidity Sensor,Garage,10.86,2021-11-25 05:37:58
<end>Here's some JSON data, can you convert it to Plain text?
[
    {
        "Location": "New York",
        "Temperature (C)": 38.0,
        "Humidity (%)": 26,
        "Day": "Tuesday"
    },
    {
        "Location": "Seattle",
        "Temperature (C)": 20.5,
        "Humidity (%)": 31,
        "Day": "Friday"
    },
    {
        "Location": "Los Angeles",
        "Temperature (C)": -1.5,
        "Humidity (%)": 31,
        "Day": "Thursday"
    }
]<start>
Location: New York | Temperature (C): 38.0 | Humidity (%): 26 | Day: Tuesday
Location: Seattle | Temperature (C): 20.5 | Humidity (%): 31 | Day: Friday
Location: Los Angeles | Temperature (C): -1.5 | Humidity (%): 31 | Day: Thursday
<end>Here's some MARKDOWN data, can you convert it to Plain text?
| Title | Director | Genre | Release Year | Box Office Earnings (M) |
| --- | --- | --- | --- | --- |
| The Final Voyage | Zara Stormrider | Action | 1987 | 735.39 |
| The Final Voyage | Talon Blackthorn | Horror | 2008 | 515.88 |
| Rise of the Titans | Mara Moonshadow | Fantasy | 2013 | 491.51 |
| Escape from Earth | Selene Darkwhisper | Drama | 1988 | 437.39 |
| The Great Expedition | Aria Ravenwood | Horror | 1971 | 700.0 |
| Escape from Earth | Cade Firebrand | Sci-Fi | 2005 | 830.55 |
| Rise of the Titans | Orin Shadowalker | Action | 2000 | 321.71 |
| Starbound Odyssey | Talon Blackthorn | Thriller | 2006 | 527.72 |
| Mystery of the Depths | Cade Firebrand | Sci-Fi | 2006 | 810.23 |
| Rise of the Titans | Rylan Frostblade | Fantasy | 2009 | 299.06 |<start>
Title: The Final Voyage | Director: Zara Stormrider | Genre: Action | Release Year: 1987 | Box Office Earnings (M): 735.39
Title: The Final Voyage | Director: Talon Blackthorn | Genre: Horror | Release Year: 2008 | Box Office Earnings (M): 515.88
Title: Rise of the Titans | Director: Mara Moonshadow | Genre: Fantasy | Release Year: 2013 | Box Office Earnings (M): 491.51
Title: Escape from Earth | Director: Selene Darkwhisper | Genre: Drama | Release Year: 1988 | Box Office Earnings (M): 437.39
Title: The Great Expedition | Director: Aria Ravenwood | Genre: Horror | Release Year: 1971 | Box Office Earnings (M): 700.0
Title: Escape from Earth | Director: Cade Firebrand | Genre: Sci-Fi | Release Year: 2005 | Box Office Earnings (M): 830.55
Title: Rise of the Titans | Director: Orin Shadowalker | Genre: Action | Release Year: 2000 | Box Office Earnings (M): 321.71
Title: Starbound Odyssey | Director: Talon Blackthorn | Genre: Thriller | Release Year: 2006 | Box Office Earnings (M): 527.72
Title: Mystery of the Depths | Director: Cade Firebrand | Genre: Sci-Fi | Release Year: 2006 | Box Office Earnings (M): 810.23
Title: Rise of the Titans | Director: Rylan Frostblade | Genre: Fantasy | Release Year: 2009 | Box Office Earnings (M): 299.06
<end>Convert this Markdown to json:
| Cache Hit Ratio (%) | Connection Count | Average Latency (ms) |
| --- | --- | --- |
| 94.44 | 158 | 31.77 |
| 86.44 | 120 | 70.44 |
| 89.18 | 342 | 13.84 |
| 86.41 | 260 | 45.69 |
| 89.37 | 195 | 55.52 |<start>
[
    {
        "Cache Hit Ratio (%)": 94.44,
        "Connection Count": 158,
        "Average Latency (ms)": 31.77
    },
    {
        "Cache Hit Ratio (%)": 86.44,
        "Connection Count": 120,
        "Average Latency (ms)": 70.44
    },
    {
        "Cache Hit Ratio (%)": 89.18,
        "Connection Count": 342,
        "Average Latency (ms)": 13.84
    },
    {
        "Cache Hit Ratio (%)": 86.41,
        "Connection Count": 260,
        "Average Latency (ms)": 45.69
    },
    {
        "Cache Hit Ratio (%)": 89.37,
        "Connection Count": 195,
        "Average Latency (ms)": 55.52
    }
]
<end>Here's some MARKDOWN data, can you convert it to Plain text?
| Name | Birth Month |
| --- | --- |
| Gabriela | October |
| Aidan | June |
| Cameron | October |
| Phyllis | January |
| Leona | June |
| Martha | August |
| Ola | December |
| Mandy | June |
| Makenzie | January |<start>
Name: Gabriela | Birth Month: October
Name: Aidan | Birth Month: June
Name: Cameron | Birth Month: October
Name: Phyllis | Birth Month: January
Name: Leona | Birth Month: June
Name: Martha | Birth Month: August
Name: Ola | Birth Month: December
Name: Mandy | Birth Month: June
Name: Makenzie | Birth Month: January
<end>Here's some MARKDOWN data, can you convert it to csv?
| Database Name | Connection Count | Timestamp |
| --- | --- | --- |
| InventoryDB | 404 | 2022-06-04 23:47:21 |
| InventoryDB | 207 | 2021-03-13 09:31:26 |
| InventoryDB | 378 | 2021-10-10 01:40:35 |<start>
Database Name,Connection Count,Timestamp
InventoryDB,404,2022-06-04 23:47:21
InventoryDB,207,2021-03-13 09:31:26
InventoryDB,378,2021-10-10 01:40:35
<end>Transform this Csv structure to a markdown format:
Company,Date,Open Price,High Price,Low Price,Volume
BioLife,2014-11-17,721.51,1214.51,227.91,2826451
FinanceTrust,2018-05-20,31.07,905.78,31.07,9802627
GreenEnergy,2018-08-22,877.39,1227.15,877.39,9802627
<start>
| Company | Date | Open Price | High Price | Low Price | Volume |
| --- | --- | --- | --- | --- | --- |
| BioLife | 2014-11-17 | 721.51 | 1214.51 | 227.91 | 2826451 |
| FinanceTrust | 2018-05-20 | 31.07 | 905.78 | 31.07 | 9802627 |
| GreenEnergy | 2018-08-22 | 877.39 | 1227.15 | 877.39 | 9802627 |
<end>Can you change this markdown into plain text?
| Title | Author | Publication Year |
| --- | --- | --- |
| The Last Sky | Orion Frostblade | 1986 |
| The Last Sky | Galen Starfire | 1953 |
| Echoes of Eternity | Rowan Ashborne | 2001 |
| Whispers of the Abyss | Sylvia Nightshade | 1978 |
| The Silent Grove | Isla Windrider | 1978 |<start>
Title: The Last Sky | Author: Orion Frostblade | Publication Year: 1986
Title: The Last Sky | Author: Galen Starfire | Publication Year: 1953
Title: Echoes of Eternity | Author: Rowan Ashborne | Publication Year: 2001
Title: Whispers of the Abyss | Author: Sylvia Nightshade | Publication Year: 1978
Title: The Silent Grove | Author: Isla Windrider | Publication Year: 1978
<end>Can you change this json into csv?
[
    {
        "Company": "BioPharm",
        "Sector": "Finance",
        "Market Cap": "Mega Cap",
        "Stock Price": 796.51,
        "Annual Revenue (B)": 366.35,
        "Quarter": "Q2"
    },
    {
        "Company": "EcoEnergy",
        "Sector": "Automotive",
        "Market Cap": "Mid Cap",
        "Stock Price": 459.72,
        "Annual Revenue (B)": 444.43,
        "Quarter": "Q3"
    },
    {
        "Company": "AutoDrive",
        "Sector": "Biotech",
        "Market Cap": "Large Cap",
        "Stock Price": 927.36,
        "Annual Revenue (B)": 262.38,
        "Quarter": "Q2"
    },
    {
        "Company": "GlobalTrade",
        "Sector": "Biotech",
        "Market Cap": "Small Cap",
        "Stock Price": 410.0,
        "Annual Revenue (B)": 366.35,
        "Quarter": "Q1"
    },
    {
        "Company": "AutoDrive",
        "Sector": "Biotech",
        "Market Cap": "Large Cap",
        "Stock Price": 743.87,
        "Annual Revenue (B)": 203.79,
        "Quarter": "Q4"
    }
]<start>
Company,Sector,Market Cap,Stock Price,Annual Revenue (B),Quarter
BioPharm,Finance,Mega Cap,796.51,366.35,Q2
EcoEnergy,Automotive,Mid Cap,459.72,444.43,Q3
AutoDrive,Biotech,Large Cap,927.36,262.38,Q2
GlobalTrade,Biotech,Small Cap,410.0,366.35,Q1
AutoDrive,Biotech,Large Cap,743.87,203.79,Q4
<end>Here's some PLAIN TEXT data, can you convert it to csv?
Title: Mystery of the Depths | Genre: Drama | Box Office Earnings (M): 530.15
Title: Rise of the Titans | Genre: Adventure | Box Office Earnings (M): 704.2
Title: The Final Voyage | Genre: Sci-Fi | Box Office Earnings (M): 717.98
Title: Mystery of the Depths | Genre: Horror | Box Office Earnings (M): 807.45
Title: Escape from Earth | Genre: Sci-Fi | Box Office Earnings (M): 902.28
Title: Dreamwalker | Genre: Sci-Fi | Box Office Earnings (M): 929.13
Title: The Final Voyage | Genre: Drama | Box Office Earnings (M): 490.84
Title: Starbound Odyssey | Genre: Thriller | Box Office Earnings (M): 71.55
<start>
Title,Genre,Box Office Earnings (M)
Mystery of the Depths,Drama,530.15
Rise of the Titans,Adventure,704.2
The Final Voyage,Sci-Fi,717.98
Mystery of the Depths,Horror,807.45
Escape from Earth,Sci-Fi,902.28
Dreamwalker,Sci-Fi,929.13
The Final Voyage,Drama,490.84
Starbound Odyssey,Thriller,71.55
<end>Convert this Markdown to json:
| Database Name | Queries per Second | Cache Hit Ratio (%) | Connection Count | Average Latency (ms) | Timestamp |
| --- | --- | --- | --- | --- | --- |
| ProductsDB | 3401.35 | 77.13 | 486 | 95.8 | 2023-07-23 22:14:56 |
| OrdersDB | 1344.92 | 76.43 | 85 | 97.87 | 2021-03-15 16:40:12 |
| AnalyticsDB | 3624.52 | 89.79 | 228 | 95.69 | 2023-08-11 06:53:59 |<start>
[
    {
        "Database Name": "ProductsDB",
        "Queries per Second": 3401.35,
        "Cache Hit Ratio (%)": 77.13,
        "Connection Count": 486,
        "Average Latency (ms)": 95.8,
        "Timestamp": "2023-07-23 22:14:56"
    },
    {
        "Database Name": "OrdersDB",
        "Queries per Second": 1344.92,
        "Cache Hit Ratio (%)": 76.43,
        "Connection Count": 85,
        "Average Latency (ms)": 97.87,
        "Timestamp": "2021-03-15 16:40:12"
    },
    {
        "Database Name": "AnalyticsDB",
        "Queries per Second": 3624.52,
        "Cache Hit Ratio (%)": 89.79,
        "Connection Count": 228,
        "Average Latency (ms)": 95.69,
        "Timestamp": "2023-08-11 06:53:59"
    }
]
<end>Convert this Yml to plain text:
- Condition: Sunny
  Day: Saturday
  Location: Los Angeles
  Temperature (C): 18.4
  Wind Speed (km/h): 13.7
- Condition: Stormy
  Day: Wednesday
  Location: Houston
  Temperature (C): 9.3
  Wind Speed (km/h): 17.6
- Condition: Sunny
  Day: Friday
  Location: Los Angeles
  Temperature (C): 5.0
  Wind Speed (km/h): 27.6
- Condition: Snowy
  Day: Monday
  Location: Denver
  Temperature (C): 10.6
  Wind Speed (km/h): 26.4
- Condition: Stormy
  Day: Tuesday
  Location: Seattle
  Temperature (C): 29.3
  Wind Speed (km/h): 6.9
- Condition: Sunny
  Day: Friday
  Location: Los Angeles
  Temperature (C): 14.4
  Wind Speed (km/h): 6.7
- Condition: Windy
  Day: Saturday
  Location: Houston
  Temperature (C): 32.2
  Wind Speed (km/h): 21.6
- Condition: Rainy
  Day: Monday
  Location: Miami
  Temperature (C): -5.3
  Wind Speed (km/h): 20.8
- Condition: Cloudy
  Day: Friday
  Location: Phoenix
  Temperature (C): 16.4
  Wind Speed (km/h): 23.2
<start>
Location: Los Angeles | Condition: Sunny | Temperature (C): 18.4 | Wind Speed (km/h): 13.7 | Day: Saturday
Location: Houston | Condition: Stormy | Temperature (C): 9.3 | Wind Speed (km/h): 17.6 | Day: Wednesday
Location: Los Angeles | Condition: Sunny | Temperature (C): 5.0 | Wind Speed (km/h): 27.6 | Day: Friday
Location: Denver | Condition: Snowy | Temperature (C): 10.6 | Wind Speed (km/h): 26.4 | Day: Monday
Location: Seattle | Condition: Stormy | Temperature (C): 29.3 | Wind Speed (km/h): 6.9 | Day: Tuesday
Location: Los Angeles | Condition: Sunny | Temperature (C): 14.4 | Wind Speed (km/h): 6.7 | Day: Friday
Location: Houston | Condition: Windy | Temperature (C): 32.2 | Wind Speed (km/h): 21.6 | Day: Saturday
Location: Miami | Condition: Rainy | Temperature (C): -5.3 | Wind Speed (km/h): 20.8 | Day: Monday
Location: Phoenix | Condition: Cloudy | Temperature (C): 16.4 | Wind Speed (km/h): 23.2 | Day: Friday
<end>Transform this yaml structure to a CSV format:
- Annual Revenue (B): 411.96
  Company: Foodies
  Market Cap: Mid Cap
  Quarter: Q1
  Sector: Automotive
  Stock Price: 333.03
- Annual Revenue (B): 234.85
  Company: TechCorp
  Market Cap: Mid Cap
  Quarter: Q4
  Sector: Aerospace
  Stock Price: 905.29
- Annual Revenue (B): 335.11
  Company: HealthPlus
  Market Cap: Small Cap
  Quarter: Q2
  Sector: Aerospace
  Stock Price: 659.67
- Annual Revenue (B): 63.73
  Company: GlobalTrade
  Market Cap: Small Cap
  Quarter: Q1
  Sector: Finance
  Stock Price: 939.99
- Annual Revenue (B): 271.69
  Company: BioPharm
  Market Cap: Large Cap
  Quarter: Q4
  Sector: Retail
  Stock Price: 645.38
- Annual Revenue (B): 112.82
  Company: AeroSpace
  Market Cap: Small Cap
  Quarter: Q3
  Sector: Technology
  Stock Price: 338.78
- Annual Revenue (B): 135.32
  Company: FinanceWorks
  Market Cap: Large Cap
  Quarter: Q1
  Sector: Healthcare
  Stock Price: 672.12
<start>
Company,Sector,Market Cap,Stock Price,Annual Revenue (B),Quarter
Foodies,Automotive,Mid Cap,333.03,411.96,Q1
TechCorp,Aerospace,Mid Cap,905.29,234.85,Q4
HealthPlus,Aerospace,Small Cap,659.67,335.11,Q2
GlobalTrade,Finance,Small Cap,939.99,63.73,Q1
BioPharm,Retail,Large Cap,645.38,271.69,Q4
AeroSpace,Technology,Small Cap,338.78,112.82,Q3
FinanceWorks,Healthcare,Large Cap,672.12,135.32,Q1
<end>Convert this PLAIN TEXT to Yaml:
End Location: Houston | Distance (miles): 1249.9 | Duration (hours): 13.8 | Fuel Used (gallons): 67.6
End Location: New York | Distance (miles): 2785.9 | Duration (hours): 6.9 | Fuel Used (gallons): 31.3
End Location: Houston | Distance (miles): 2799.6 | Duration (hours): 4.8 | Fuel Used (gallons): 24.3
End Location: Los Angeles | Distance (miles): 1466.8 | Duration (hours): 64.6 | Fuel Used (gallons): 11.6
End Location: San Francisco | Distance (miles): 800.0 | Duration (hours): 50.5 | Fuel Used (gallons): 31.3
End Location: Denver | Distance (miles): 1973.6 | Duration (hours): 38.2 | Fuel Used (gallons): 94.7
End Location: Chicago | Distance (miles): 2453.9 | Duration (hours): 66.5 | Fuel Used (gallons): 61.8
End Location: San Francisco | Distance (miles): 2616.8 | Duration (hours): 52.1 | Fuel Used (gallons): 40.6
<start>
- Distance (miles): 1249.9
  Duration (hours): 13.8
  End Location: Houston
  Fuel Used (gallons): 67.6
- Distance (miles): 2785.9
  Duration (hours): 6.9
  End Location: New York
  Fuel Used (gallons): 31.3
- Distance (miles): 2799.6
  Duration (hours): 4.8
  End Location: Houston
  Fuel Used (gallons): 24.3
- Distance (miles): 1466.8
  Duration (hours): 64.6
  End Location: Los Angeles
  Fuel Used (gallons): 11.6
- Distance (miles): 800.0
  Duration (hours): 50.5
  End Location: San Francisco
  Fuel Used (gallons): 31.3
- Distance (miles): 1973.6
  Duration (hours): 38.2
  End Location: Denver
  Fuel Used (gallons): 94.7
- Distance (miles): 2453.9
  Duration (hours): 66.5
  End Location: Chicago
  Fuel Used (gallons): 61.8
- Distance (miles): 2616.8
  Duration (hours): 52.1
  End Location: San Francisco
  Fuel Used (gallons): 40.6
<end>Here's some CSV data, can you convert it to plain text?
Device ID,Device Type,Location,Battery Level (%),Reading Value,Timestamp
device-0032,Humidity Sensor,Bathroom,81.7,14.24,2023-01-02 18:06:28
device-0046,Light Sensor,Bathroom,80.6,0.83,2022-03-01 16:46:08
device-0089,Light Sensor,Bathroom,21.2,11.02,2022-08-08 09:17:53
<start>
Device ID: device-0032 | Device Type: Humidity Sensor | Location: Bathroom | Battery Level (%): 81.7 | Reading Value: 14.24 | Timestamp: 2023-01-02 18:06:28
Device ID: device-0046 | Device Type: Light Sensor | Location: Bathroom | Battery Level (%): 80.6 | Reading Value: 0.83 | Timestamp: 2022-03-01 16:46:08
Device ID: device-0089 | Device Type: Light Sensor | Location: Bathroom | Battery Level (%): 21.2 | Reading Value: 11.02 | Timestamp: 2022-08-08 09:17:53
<end>Convert this Markdown to plain text:
| Title | Author | Genre | Publication Year | Rating |
| --- | --- | --- | --- | --- |
| Tales of the Brave | Sylvia Nightshade | Mystery | 1997 | 4.7 |
| The Forgotten World | Sylvia Nightshade | Fantasy | 1988 | 3.0 |
| Legends of the Rift | Isla Windrider | Historical | 2014 | 4.8 |
| The Last Sky | Sylvia Nightshade | Fantasy | 1963 | 1.6 |
| A Journey Through Time | Draven Blackthorn | Horror | 1986 | 3.0 |
| Shadows of Solitude | Luna Silverleaf | Historical | 1975 | 4.9 |<start>
Title: Tales of the Brave | Author: Sylvia Nightshade | Genre: Mystery | Publication Year: 1997 | Rating: 4.7
Title: The Forgotten World | Author: Sylvia Nightshade | Genre: Fantasy | Publication Year: 1988 | Rating: 3.0
Title: Legends of the Rift | Author: Isla Windrider | Genre: Historical | Publication Year: 2014 | Rating: 4.8
Title: The Last Sky | Author: Sylvia Nightshade | Genre: Fantasy | Publication Year: 1963 | Rating: 1.6
Title: A Journey Through Time | Author: Draven Blackthorn | Genre: Horror | Publication Year: 1986 | Rating: 3.0
Title: Shadows of Solitude | Author: Luna Silverleaf | Genre: Historical | Publication Year: 1975 | Rating: 4.9
<end>Please transform the following csv data into json:
Sector,Market Cap,Stock Price,Quarter
Aerospace,Large Cap,560.52,Q4
Energy,Mid Cap,196.04,Q3
Healthcare,Mega Cap,701.44,Q4
<start>
[
    {
        "Sector": "Aerospace",
        "Market Cap": "Large Cap",
        "Stock Price": 560.52,
        "Quarter": "Q4"
    },
    {
        "Sector": "Energy",
        "Market Cap": "Mid Cap",
        "Stock Price": 196.04,
        "Quarter": "Q3"
    },
    {
        "Sector": "Healthcare",
        "Market Cap": "Mega Cap",
        "Stock Price": 701.44,
        "Quarter": "Q4"
    }
]
<end>Can you change this Csv into MARKDOWN?
Name,Age,Birth Month,City,Income
Ernest,23,April,Washington,270000
Shawn,23,January,Las Vegas,410000
Shawna,64,August,Louisville,145000
Ina,50,July,Charlotte,480000
<start>
| Name | Age | Birth Month | City | Income |
| --- | --- | --- | --- | --- |
| Ernest | 23 | April | Washington | 270000 |
| Shawn | 23 | January | Las Vegas | 410000 |
| Shawna | 64 | August | Louisville | 145000 |
| Ina | 50 | July | Charlotte | 480000 |
<end>Please transform the following YML data into PLAIN TEXT:
- Battery Level (%): 67.6
  Device ID: device-0023
  Location: Living Room
  Reading Value: -21.74
- Battery Level (%): 39.1
  Device ID: device-0033
  Location: Garden
  Reading Value: -25.42
- Battery Level (%): 23.0
  Device ID: device-0096
  Location: Garden
  Reading Value: -28.78
- Battery Level (%): 78.1
  Device ID: device-0095
  Location: Bathroom
  Reading Value: -32.85
- Battery Level (%): 45.1
  Device ID: device-0079
  Location: Living Room
  Reading Value: 76.95
<start>
Device ID: device-0023 | Location: Living Room | Battery Level (%): 67.6 | Reading Value: -21.74
Device ID: device-0033 | Location: Garden | Battery Level (%): 39.1 | Reading Value: -25.42
Device ID: device-0096 | Location: Garden | Battery Level (%): 23.0 | Reading Value: -28.78
Device ID: device-0095 | Location: Bathroom | Battery Level (%): 78.1 | Reading Value: -32.85
Device ID: device-0079 | Location: Living Room | Battery Level (%): 45.1 | Reading Value: 76.95
<end>Transform this csv structure to a Json format:
Location,Wind Speed (km/h),Day
Miami,23.0,Saturday
Chicago,0.1,Thursday
Miami,15.3,Thursday
Phoenix,14.7,Tuesday
Chicago,11.5,Wednesday
Seattle,19.9,Saturday
Chicago,5.9,Monday
<start>
[
    {
        "Location": "Miami",
        "Wind Speed (km/h)": 23.0,
        "Day": "Saturday"
    },
    {
        "Location": "Chicago",
        "Wind Speed (km/h)": 0.1,
        "Day": "Thursday"
    },
    {
        "Location": "Miami",
        "Wind Speed (km/h)": 15.3,
        "Day": "Thursday"
    },
    {
        "Location": "Phoenix",
        "Wind Speed (km/h)": 14.7,
        "Day": "Tuesday"
    },
    {
        "Location": "Chicago",
        "Wind Speed (km/h)": 11.5,
        "Day": "Wednesday"
    },
    {
        "Location": "Seattle",
        "Wind Speed (km/h)": 19.9,
        "Day": "Saturday"
    },
    {
        "Location": "Chicago",
        "Wind Speed (km/h)": 5.9,
        "Day": "Monday"
    }
]
<end>Here's some plain text data, can you convert it to yaml?
Trip Name: Historic Route | Start Location: Denver | Duration (hours): 21.7 | Fuel Used (gallons): 36.6
Trip Name: Mountain Adventure | Start Location: Miami | Duration (hours): 57.4 | Fuel Used (gallons): 90.6
Trip Name: Valley Voyage | Start Location: Denver | Duration (hours): 64.0 | Fuel Used (gallons): 36.6
Trip Name: Desert Drive | Start Location: Miami | Duration (hours): 53.2 | Fuel Used (gallons): 63.3
Trip Name: Forest Journey | Start Location: Chicago | Duration (hours): 53.2 | Fuel Used (gallons): 53.1
<start>
- Duration (hours): 21.7
  Fuel Used (gallons): 36.6
  Start Location: Denver
  Trip Name: Historic Route
- Duration (hours): 57.4
  Fuel Used (gallons): 90.6
  Start Location: Miami
  Trip Name: Mountain Adventure
- Duration (hours): 64.0
  Fuel Used (gallons): 36.6
  Start Location: Denver
  Trip Name: Valley Voyage
- Duration (hours): 53.2
  Fuel Used (gallons): 63.3
  Start Location: Miami
  Trip Name: Desert Drive
- Duration (hours): 53.2
  Fuel Used (gallons): 53.1
  Start Location: Chicago
  Trip Name: Forest Journey
<end>Convert this YAML to csv:
- Author: Isla Windrider
  Genre: Non-Fiction
  Publication Year: 2000
  Rating: 4.6
  Title: The Last Sky
- Author: Galen Starfire
  Genre: Romance
  Publication Year: 2014
  Rating: 3.6
  Title: The Last Sky
- Author: Rowan Ashborne
  Genre: Romance
  Publication Year: 2020
  Rating: 4.1
  Title: Tales of the Brave
- Author: Elara Moonshadow
  Genre: Fantasy
  Publication Year: 1966
  Rating: 3.2
  Title: Legends of the Rift
- Author: Galen Starfire
  Genre: Fantasy
  Publication Year: 2019
  Rating: 3.6
  Title: Echoes of Eternity
- Author: Rowan Ashborne
  Genre: Non-Fiction
  Publication Year: 1984
  Rating: 2.5
  Title: Tales of the Brave
- Author: Orion Frostblade
  Genre: Historical
  Publication Year: 1981
  Rating: 3.0
  Title: Legends of the Rift
- Author: Rowan Ashborne
  Genre: Fantasy
  Publication Year: 2004
  Rating: 2.0
  Title: Legends of the Rift
- Author: Rowan Ashborne
  Genre: Science Fiction
  Publication Year: 1951
  Rating: 3.0
  Title: Tales of the Brave
<start>
Title,Author,Genre,Publication Year,Rating
The Last Sky,Isla Windrider,Non-Fiction,2000,4.6
The Last Sky,Galen Starfire,Romance,2014,3.6
Tales of the Brave,Rowan Ashborne,Romance,2020,4.1
Legends of the Rift,Elara Moonshadow,Fantasy,1966,3.2
Echoes of Eternity,Galen Starfire,Fantasy,2019,3.6
Tales of the Brave,Rowan Ashborne,Non-Fiction,1984,2.5
Legends of the Rift,Orion Frostblade,Historical,1981,3.0
Legends of the Rift,Rowan Ashborne,Fantasy,2004,2.0
Tales of the Brave,Rowan Ashborne,Science Fiction,1951,3.0
<end>Transform this Json structure to a YAML format:
[
    {
        "SKU": "SKU-1081",
        "Stock Quantity": 361,
        "Category": "Electronics"
    },
    {
        "SKU": "SKU-1007",
        "Stock Quantity": 348,
        "Category": "Automotive"
    },
    {
        "SKU": "SKU-1019",
        "Stock Quantity": 131,
        "Category": "Automotive"
    },
    {
        "SKU": "SKU-1094",
        "Stock Quantity": 349,
        "Category": "Automotive"
    },
    {
        "SKU": "SKU-1080",
        "Stock Quantity": 300,
        "Category": "Toys"
    },
    {
        "SKU": "SKU-1036",
        "Stock Quantity": 19,
        "Category": "Sports"
    },
    {
        "SKU": "SKU-1069",
        "Stock Quantity": 195,
        "Category": "Household"
    }
]<start>
- Category: Electronics
  SKU: SKU-1081
  Stock Quantity: 361
- Category: Automotive
  SKU: SKU-1007
  Stock Quantity: 348
- Category: Automotive
  SKU: SKU-1019
  Stock Quantity: 131
- Category: Automotive
  SKU: SKU-1094
  Stock Quantity: 349
- Category: Toys
  SKU: SKU-1080
  Stock Quantity: 300
- Category: Sports
  SKU: SKU-1036
  Stock Quantity: 19
- Category: Household
  SKU: SKU-1069
  Stock Quantity: 195
<end>Transform this csv structure to a json format:
Company,Open Price,Close Price,High Price,Low Price,Volume
RetailWorld,1469.83,382.17,1469.83,382.17,1767127
RetailWorld,1458.31,71.79,1458.31,71.79,3502911
HealthGen,49.88,431.24,1326.84,49.88,8119644
AutoMotive,856.84,732.31,1012.9,732.31,5048076
MediaGroup,120.85,701.96,701.96,120.85,5462724
BioLife,701.96,761.44,761.44,584.08,9479400
FoodChain,118.61,669.69,669.69,118.61,9909821
<start>
[
    {
        "Company": "RetailWorld",
        "Open Price": 1469.83,
        "Close Price": 382.17,
        "High Price": 1469.83,
        "Low Price": 382.17,
        "Volume": 1767127
    },
    {
        "Company": "RetailWorld",
        "Open Price": 1458.31,
        "Close Price": 71.79,
        "High Price": 1458.31,
        "Low Price": 71.79,
        "Volume": 3502911
    },
    {
        "Company": "HealthGen",
        "Open Price": 49.88,
        "Close Price": 431.24,
        "High Price": 1326.84,
        "Low Price": 49.88,
        "Volume": 8119644
    },
    {
        "Company": "AutoMotive",
        "Open Price": 856.84,
        "Close Price": 732.31,
        "High Price": 1012.9,
        "Low Price": 732.31,
        "Volume": 5048076
    },
    {
        "Company": "MediaGroup",
        "Open Price": 120.85,
        "Close Price": 701.96,
        "High Price": 701.96,
        "Low Price": 120.85,
        "Volume": 5462724
    },
    {
        "Company": "BioLife",
        "Open Price": 701.96,
        "Close Price": 761.44,
        "High Price": 761.44,
        "Low Price": 584.08,
        "Volume": 9479400
    },
    {
        "Company": "FoodChain",
        "Open Price": 118.61,
        "Close Price": 669.69,
        "High Price": 669.69,
        "Low Price": 118.61,
        "Volume": 9909821
    }
]
<end>Can you change this Plain text into yml?
Company: Foodies | Market Cap: Mega Cap | Quarter: Q1
Company: RetailHub | Market Cap: Mid Cap | Quarter: Q3
Company: HealthPlus | Market Cap: Small Cap | Quarter: Q4
<start>
- Company: Foodies
  Market Cap: Mega Cap
  Quarter: Q1
- Company: RetailHub
  Market Cap: Mid Cap
  Quarter: Q3
- Company: HealthPlus
  Market Cap: Small Cap
  Quarter: Q4
<end>Transform this plain text structure to a json format:
Title: Tales of the Brave | Author: Galen Starfire | Genre: Historical | Publication Year: 2016 | Rating: 3.2
Title: Legends of the Rift | Author: Kara Firebrand | Genre: Horror | Publication Year: 1965 | Rating: 2.6
Title: The Crystal Key | Author: Isla Windrider | Genre: Historical | Publication Year: 1951 | Rating: 2.1
Title: The Last Sky | Author: Isla Windrider | Genre: Mystery | Publication Year: 1992 | Rating: 4.8
Title: Tales of the Brave | Author: Rowan Ashborne | Genre: Non-Fiction | Publication Year: 1995 | Rating: 4.3
Title: The Silent Grove | Author: Orion Frostblade | Genre: Thriller | Publication Year: 1958 | Rating: 4.0
Title: Legends of the Rift | Author: Isla Windrider | Genre: Science Fiction | Publication Year: 1960 | Rating: 4.6
Title: The Last Sky | Author: Elara Moonshadow | Genre: Mystery | Publication Year: 1961 | Rating: 1.9
Title: The Last Sky | Author: Draven Blackthorn | Genre: Non-Fiction | Publication Year: 1955 | Rating: 3.1
Title: The Forgotten World | Author: Luna Silverleaf | Genre: Non-Fiction | Publication Year: 1988 | Rating: 2.3
<start>
[
    {
        "Title": "Tales of the Brave",
        "Author": "Galen Starfire",
        "Genre": "Historical",
        "Publication Year": 2016,
        "Rating": 3.2
    },
    {
        "Title": "Legends of the Rift",
        "Author": "Kara Firebrand",
        "Genre": "Horror",
        "Publication Year": 1965,
        "Rating": 2.6
    },
    {
        "Title": "The Crystal Key",
        "Author": "Isla Windrider",
        "Genre": "Historical",
        "Publication Year": 1951,
        "Rating": 2.1
    },
    {
        "Title": "The Last Sky",
        "Author": "Isla Windrider",
        "Genre": "Mystery",
        "Publication Year": 1992,
        "Rating": 4.8
    },
    {
        "Title": "Tales of the Brave",
        "Author": "Rowan Ashborne",
        "Genre": "Non-Fiction",
        "Publication Year": 1995,
        "Rating": 4.3
    },
    {
        "Title": "The Silent Grove",
        "Author": "Orion Frostblade",
        "Genre": "Thriller",
        "Publication Year": 1958,
        "Rating": 4.0
    },
    {
        "Title": "Legends of the Rift",
        "Author": "Isla Windrider",
        "Genre": "Science Fiction",
        "Publication Year": 1960,
        "Rating": 4.6
    },
    {
        "Title": "The Last Sky",
        "Author": "Elara Moonshadow",
        "Genre": "Mystery",
        "Publication Year": 1961,
        "Rating": 1.9
    },
    {
        "Title": "The Last Sky",
        "Author": "Draven Blackthorn",
        "Genre": "Non-Fiction",
        "Publication Year": 1955,
        "Rating": 3.1
    },
    {
        "Title": "The Forgotten World",
        "Author": "Luna Silverleaf",
        "Genre": "Non-Fiction",
        "Publication Year": 1988,
        "Rating": 2.3
    }
]
<end>Please transform the following markdown data into yaml:
| Company | Date | Close Price | Low Price | Volume |
| --- | --- | --- | --- | --- |
| AutoMotive | 2022-11-19 | 447.14 | 57.44 | 2830707 |
| FinanceTrust | 2017-08-09 | 1101.87 | 877.2 | 2920764 |
| TechnoCorp | 2015-03-25 | 175.73 | 175.73 | 2920764 |<start>
- Close Price: 447.14
  Company: AutoMotive
  Date: '2022-11-19'
  Low Price: 57.44
  Volume: 2830707
- Close Price: 1101.87
  Company: FinanceTrust
  Date: '2017-08-09'
  Low Price: 877.2
  Volume: 2920764
- Close Price: 175.73
  Company: TechnoCorp
  Date: '2015-03-25'
  Low Price: 175.73
  Volume: 2920764
<end>Can you change this JSON into yml?
[
    {
        "Battery Level (%)": 21.3,
        "Reading Value": 23.57,
        "Timestamp": "2022-10-09 19:15:53"
    },
    {
        "Battery Level (%)": 84.5,
        "Reading Value": 5.61,
        "Timestamp": "2022-09-28 06:42:21"
    },
    {
        "Battery Level (%)": 77.0,
        "Reading Value": 67.56,
        "Timestamp": "2021-02-18 23:11:31"
    }
]<start>
- Battery Level (%): 21.3
  Reading Value: 23.57
  Timestamp: '2022-10-09 19:15:53'
- Battery Level (%): 84.5
  Reading Value: 5.61
  Timestamp: '2022-09-28 06:42:21'
- Battery Level (%): 77.0
  Reading Value: 67.56
  Timestamp: '2021-02-18 23:11:31'
<end>Please transform the following JSON data into csv:
[
    {
        "Location": "New York",
        "Condition": "Stormy",
        "Temperature (C)": -7.8,
        "Humidity (%)": 22,
        "Wind Speed (km/h)": 13.0,
        "Day": "Friday"
    },
    {
        "Location": "Denver",
        "Condition": "Snowy",
        "Temperature (C)": 27.9,
        "Humidity (%)": 64,
        "Wind Speed (km/h)": 29.2,
        "Day": "Friday"
    },
    {
        "Location": "Phoenix",
        "Condition": "Stormy",
        "Temperature (C)": 38.8,
        "Humidity (%)": 67,
        "Wind Speed (km/h)": 22.3,
        "Day": "Saturday"
    },
    {
        "Location": "Miami",
        "Condition": "Cloudy",
        "Temperature (C)": -8.7,
        "Humidity (%)": 73,
        "Wind Speed (km/h)": 13.0,
        "Day": "Tuesday"
    },
    {
        "Location": "Chicago",
        "Condition": "Sunny",
        "Temperature (C)": 13.2,
        "Humidity (%)": 60,
        "Wind Speed (km/h)": 14.2,
        "Day": "Saturday"
    },
    {
        "Location": "New York",
        "Condition": "Snowy",
        "Temperature (C)": 2.6,
        "Humidity (%)": 82,
        "Wind Speed (km/h)": 16.4,
        "Day": "Saturday"
    },
    {
        "Location": "New York",
        "Condition": "Sunny",
        "Temperature (C)": 27.3,
        "Humidity (%)": 82,
        "Wind Speed (km/h)": 4.5,
        "Day": "Monday"
    },
    {
        "Location": "Denver",
        "Condition": "Cloudy",
        "Temperature (C)": 20.5,
        "Humidity (%)": 98,
        "Wind Speed (km/h)": 14.2,
        "Day": "Tuesday"
    },
    {
        "Location": "Phoenix",
        "Condition": "Snowy",
        "Temperature (C)": 19.6,
        "Humidity (%)": 60,
        "Wind Speed (km/h)": 22.7,
        "Day": "Saturday"
    }
]<start>
Location,Condition,Temperature (C),Humidity (%),Wind Speed (km/h),Day
New York,Stormy,-7.8,22,13.0,Friday
Denver,Snowy,27.9,64,29.2,Friday
Phoenix,Stormy,38.8,67,22.3,Saturday
Miami,Cloudy,-8.7,73,13.0,Tuesday
Chicago,Sunny,13.2,60,14.2,Saturday
New York,Snowy,2.6,82,16.4,Saturday
New York,Sunny,27.3,82,4.5,Monday
Denver,Cloudy,20.5,98,14.2,Tuesday
Phoenix,Snowy,19.6,60,22.7,Saturday
<end>Here's some Plain text data, can you convert it to json?
SKU: SKU-1056 | Stock Quantity: 52 | Category: Toys | Supplier Name: Globex
SKU: SKU-1044 | Stock Quantity: 114 | Category: Sports | Supplier Name: ACME Corp
SKU: SKU-1075 | Stock Quantity: 107 | Category: Household | Supplier Name: Umbrella Corp
SKU: SKU-1033 | Stock Quantity: 367 | Category: Toys | Supplier Name: Globex
SKU: SKU-1095 | Stock Quantity: 179 | Category: Automotive | Supplier Name: Umbrella Corp
SKU: SKU-1010 | Stock Quantity: 3 | Category: Sports | Supplier Name: Wonka Industries
SKU: SKU-1066 | Stock Quantity: 96 | Category: Household | Supplier Name: ACME Corp
SKU: SKU-1067 | Stock Quantity: 132 | Category: Electronics | Supplier Name: Wonka Industries
SKU: SKU-1048 | Stock Quantity: 205 | Category: Automotive | Supplier Name: Wonka Industries
SKU: SKU-1011 | Stock Quantity: 68 | Category: Toys | Supplier Name: Globex
<start>
[
    {
        "SKU": "SKU-1056",
        "Stock Quantity": 52,
        "Category": "Toys",
        "Supplier Name": "Globex"
    },
    {
        "SKU": "SKU-1044",
        "Stock Quantity": 114,
        "Category": "Sports",
        "Supplier Name": "ACME Corp"
    },
    {
        "SKU": "SKU-1075",
        "Stock Quantity": 107,
        "Category": "Household",
        "Supplier Name": "Umbrella Corp"
    },
    {
        "SKU": "SKU-1033",
        "Stock Quantity": 367,
        "Category": "Toys",
        "Supplier Name": "Globex"
    },
    {
        "SKU": "SKU-1095",
        "Stock Quantity": 179,
        "Category": "Automotive",
        "Supplier Name": "Umbrella Corp"
    },
    {
        "SKU": "SKU-1010",
        "Stock Quantity": 3,
        "Category": "Sports",
        "Supplier Name": "Wonka Industries"
    },
    {
        "SKU": "SKU-1066",
        "Stock Quantity": 96,
        "Category": "Household",
        "Supplier Name": "ACME Corp"
    },
    {
        "SKU": "SKU-1067",
        "Stock Quantity": 132,
        "Category": "Electronics",
        "Supplier Name": "Wonka Industries"
    },
    {
        "SKU": "SKU-1048",
        "Stock Quantity": 205,
        "Category": "Automotive",
        "Supplier Name": "Wonka Industries"
    },
    {
        "SKU": "SKU-1011",
        "Stock Quantity": 68,
        "Category": "Toys",
        "Supplier Name": "Globex"
    }
]
<end>Here's some csv data, can you convert it to yml?
Title,Author,Genre,Publication Year,Rating
The Crystal Key,Draven Blackthorn,Science Fiction,2004,3.1
The Silent Grove,Draven Blackthorn,Fantasy,2004,1.2
A Journey Through Time,Thorne Ironwood,Thriller,1987,4.5
Tales of the Brave,Thorne Ironwood,Thriller,2008,4.2
The Crystal Key,Luna Silverleaf,Horror,2006,3.1
Legends of the Rift,Draven Blackthorn,Science Fiction,2007,1.2
Shadows of Solitude,Kara Firebrand,Horror,1985,4.0
Echoes of Eternity,Rowan Ashborne,Horror,1985,4.0
The Forgotten World,Sylvia Nightshade,Fantasy,1950,3.0
The Silent Grove,Rowan Ashborne,Mystery,1982,2.3
<start>
- Author: Draven Blackthorn
  Genre: Science Fiction
  Publication Year: 2004
  Rating: 3.1
  Title: The Crystal Key
- Author: Draven Blackthorn
  Genre: Fantasy
  Publication Year: 2004
  Rating: 1.2
  Title: The Silent Grove
- Author: Thorne Ironwood
  Genre: Thriller
  Publication Year: 1987
  Rating: 4.5
  Title: A Journey Through Time
- Author: Thorne Ironwood
  Genre: Thriller
  Publication Year: 2008
  Rating: 4.2
  Title: Tales of the Brave
- Author: Luna Silverleaf
  Genre: Horror
  Publication Year: 2006
  Rating: 3.1
  Title: The Crystal Key
- Author: Draven Blackthorn
  Genre: Science Fiction
  Publication Year: 2007
  Rating: 1.2
  Title: Legends of the Rift
- Author: Kara Firebrand
  Genre: Horror
  Publication Year: 1985
  Rating: 4.0
  Title: Shadows of Solitude
- Author: Rowan Ashborne
  Genre: Horror
  Publication Year: 1985
  Rating: 4.0
  Title: Echoes of Eternity
- Author: Sylvia Nightshade
  Genre: Fantasy
  Publication Year: 1950
  Rating: 3.0
  Title: The Forgotten World
- Author: Rowan Ashborne
  Genre: Mystery
  Publication Year: 1982
  Rating: 2.3
  Title: The Silent Grove
<end>Convert this MARKDOWN to YML:
| Database Name | Queries per Second | Cache Hit Ratio (%) | Average Latency (ms) | Timestamp |
| --- | --- | --- | --- | --- |
| SessionsDB | 1513.67 | 96.72 | 20.0 | 2022-03-18 20:30:08 |
| LogsDB | 2715.12 | 82.93 | 42.13 | 2021-12-10 21:20:57 |
| InventoryDB | 4271.74 | 76.2 | 30.17 | 2021-08-25 14:31:21 |<start>
- Average Latency (ms): 20.0
  Cache Hit Ratio (%): 96.72
  Database Name: SessionsDB
  Queries per Second: 1513.67
  Timestamp: '2022-03-18 20:30:08'
- Average Latency (ms): 42.13
  Cache Hit Ratio (%): 82.93
  Database Name: LogsDB
  Queries per Second: 2715.12
  Timestamp: '2021-12-10 21:20:57'
- Average Latency (ms): 30.17
  Cache Hit Ratio (%): 76.2
  Database Name: InventoryDB
  Queries per Second: 4271.74
  Timestamp: '2021-08-25 14:31:21'
<end>Can you change this Json into YAML?
[
    {
        "Queries per Second": 3110.72,
        "Connection Count": 487,
        "Timestamp": "2023-09-15 19:21:11"
    },
    {
        "Queries per Second": 2619.79,
        "Connection Count": 92,
        "Timestamp": "2023-01-05 17:00:38"
    },
    {
        "Queries per Second": 625.28,
        "Connection Count": 321,
        "Timestamp": "2021-07-22 07:46:26"
    },
    {
        "Queries per Second": 3858.26,
        "Connection Count": 166,
        "Timestamp": "2022-08-24 00:57:20"
    },
    {
        "Queries per Second": 3736.04,
        "Connection Count": 97,
        "Timestamp": "2021-09-21 01:44:37"
    },
    {
        "Queries per Second": 2259.77,
        "Connection Count": 25,
        "Timestamp": "2021-12-25 02:04:42"
    },
    {
        "Queries per Second": 4661.38,
        "Connection Count": 394,
        "Timestamp": "2023-06-26 03:08:49"
    },
    {
        "Queries per Second": 3098.7,
        "Connection Count": 186,
        "Timestamp": "2022-06-19 06:03:22"
    },
    {
        "Queries per Second": 1110.36,
        "Connection Count": 171,
        "Timestamp": "2022-04-11 07:25:21"
    }
]<start>
- Connection Count: 487
  Queries per Second: 3110.72
  Timestamp: '2023-09-15 19:21:11'
- Connection Count: 92
  Queries per Second: 2619.79
  Timestamp: '2023-01-05 17:00:38'
- Connection Count: 321
  Queries per Second: 625.28
  Timestamp: '2021-07-22 07:46:26'
- Connection Count: 166
  Queries per Second: 3858.26
  Timestamp: '2022-08-24 00:57:20'
- Connection Count: 97
  Queries per Second: 3736.04
  Timestamp: '2021-09-21 01:44:37'
- Connection Count: 25
  Queries per Second: 2259.77
  Timestamp: '2021-12-25 02:04:42'
- Connection Count: 394
  Queries per Second: 4661.38
  Timestamp: '2023-06-26 03:08:49'
- Connection Count: 186
  Queries per Second: 3098.7
  Timestamp: '2022-06-19 06:03:22'
- Connection Count: 171
  Queries per Second: 1110.36
  Timestamp: '2022-04-11 07:25:21'
<end>Can you change this csv into yml?
Device ID,Device Type,Location
device-0071,Light Sensor,Living Room
device-0097,Light Sensor,Garage
device-0037,Light Sensor,Office
device-0014,Light Sensor,Office
device-0020,Light Sensor,Hallway
<start>
- Device ID: device-0071
  Device Type: Light Sensor
  Location: Living Room
- Device ID: device-0097
  Device Type: Light Sensor
  Location: Garage
- Device ID: device-0037
  Device Type: Light Sensor
  Location: Office
- Device ID: device-0014
  Device Type: Light Sensor
  Location: Office
- Device ID: device-0020
  Device Type: Light Sensor
  Location: Hallway
<end>Please transform the following YAML data into PLAIN TEXT:
- Duration (hours): 59.7
  End Location: San Francisco
  Trip Name: Historic Route
- Duration (hours): 14.6
  End Location: Houston
  Trip Name: Historic Route
- Duration (hours): 48.0
  End Location: Miami
  Trip Name: City Explorer
- Duration (hours): 51.3
  End Location: Chicago
  Trip Name: Desert Drive
- Duration (hours): 11.7
  End Location: San Francisco
  Trip Name: Valley Voyage
- Duration (hours): 36.3
  End Location: Miami
  Trip Name: Coast to Coast
- Duration (hours): 46.8
  End Location: Los Angeles
  Trip Name: Forest Journey
- Duration (hours): 19.2
  End Location: San Francisco
  Trip Name: Lakeside Retreat
<start>
Trip Name: Historic Route | End Location: San Francisco | Duration (hours): 59.7
Trip Name: Historic Route | End Location: Houston | Duration (hours): 14.6
Trip Name: City Explorer | End Location: Miami | Duration (hours): 48.0
Trip Name: Desert Drive | End Location: Chicago | Duration (hours): 51.3
Trip Name: Valley Voyage | End Location: San Francisco | Duration (hours): 11.7
Trip Name: Coast to Coast | End Location: Miami | Duration (hours): 36.3
Trip Name: Forest Journey | End Location: Los Angeles | Duration (hours): 46.8
Trip Name: Lakeside Retreat | End Location: San Francisco | Duration (hours): 19.2
<end>Here's some CSV data, can you convert it to Plain text?
Restaurant Name,Location,Rating,Price Range
Vegan Delight,Houston,3,$$$
Pasta Palace,Los Angeles,4,$$$$
Burger Haven,Miami,2,$$
Taco Town,San Francisco,1,$
<start>
Restaurant Name: Vegan Delight | Location: Houston | Rating: 3 | Price Range: $$$
Restaurant Name: Pasta Palace | Location: Los Angeles | Rating: 4 | Price Range: $$$$
Restaurant Name: Burger Haven | Location: Miami | Rating: 2 | Price Range: $$
Restaurant Name: Taco Town | Location: San Francisco | Rating: 1 | Price Range: $
<end>Convert this Plain text to yml:
Restaurant Name: Pasta Palace | Cuisine: Japanese | Rating: 2 | Price Range: $$
Restaurant Name: Pasta Palace | Cuisine: French | Rating: 2 | Price Range: $$
Restaurant Name: The Steakhouse | Cuisine: Chinese | Rating: 2 | Price Range: $$$
Restaurant Name: Sushi World | Cuisine: Mediterranean | Rating: 3 | Price Range: $
Restaurant Name: Burger Haven | Cuisine: Chinese | Rating: 2 | Price Range: $
Restaurant Name: Pizza Planet | Cuisine: French | Rating: 2 | Price Range: $$$
Restaurant Name: Pasta Palace | Cuisine: Italian | Rating: 3 | Price Range: $$$$$
Restaurant Name: Pasta Palace | Cuisine: French | Rating: 5 | Price Range: $$$$
Restaurant Name: Pizza Planet | Cuisine: Mexican | Rating: 3 | Price Range: $$
Restaurant Name: Pizza Planet | Cuisine: Chinese | Rating: 5 | Price Range: $$$
<start>
- Cuisine: Japanese
  Price Range: $$
  Rating: 2
  Restaurant Name: Pasta Palace
- Cuisine: French
  Price Range: $$
  Rating: 2
  Restaurant Name: Pasta Palace
- Cuisine: Chinese
  Price Range: $$$
  Rating: 2
  Restaurant Name: The Steakhouse
- Cuisine: Mediterranean
  Price Range: $
  Rating: 3
  Restaurant Name: Sushi World
- Cuisine: Chinese
  Price Range: $
  Rating: 2
  Restaurant Name: Burger Haven
- Cuisine: French
  Price Range: $$$
  Rating: 2
  Restaurant Name: Pizza Planet
- Cuisine: Italian
  Price Range: $$$$$
  Rating: 3
  Restaurant Name: Pasta Palace
- Cuisine: French
  Price Range: $$$$
  Rating: 5
  Restaurant Name: Pasta Palace
- Cuisine: Mexican
  Price Range: $$
  Rating: 3
  Restaurant Name: Pizza Planet
- Cuisine: Chinese
  Price Range: $$$
  Rating: 5
  Restaurant Name: Pizza Planet
<end>Please transform the following json data into MARKDOWN:
[
    {
        "Location": "Chicago",
        "Condition": "Foggy",
        "Humidity (%)": 50,
        "Day": "Friday"
    },
    {
        "Location": "Seattle",
        "Condition": "Rainy",
        "Humidity (%)": 75,
        "Day": "Friday"
    },
    {
        "Location": "Denver",
        "Condition": "Sunny",
        "Humidity (%)": 36,
        "Day": "Saturday"
    },
    {
        "Location": "Phoenix",
        "Condition": "Stormy",
        "Humidity (%)": 45,
        "Day": "Sunday"
    }
]<start>
| Location | Condition | Humidity (%) | Day |
| --- | --- | --- | --- |
| Chicago | Foggy | 50 | Friday |
| Seattle | Rainy | 75 | Friday |
| Denver | Sunny | 36 | Saturday |
| Phoenix | Stormy | 45 | Sunday |
<end>Here's some csv data, can you convert it to markdown?
Name,Age,Birth Month,City
Bernard,40,January,Boston
Collin,32,November,Memphis
Lulu,22,February,Denver
Justin,63,February,Detroit
Kristen,31,November,Charlotte
Betty,62,January,Fort Worth
Olive,38,May,Austin
Micah,53,December,Boston
Mila,21,April,San Francisco
<start>
| Name | Age | Birth Month | City |
| --- | --- | --- | --- |
| Bernard | 40 | January | Boston |
| Collin | 32 | November | Memphis |
| Lulu | 22 | February | Denver |
| Justin | 63 | February | Detroit |
| Kristen | 31 | November | Charlotte |
| Betty | 62 | January | Fort Worth |
| Olive | 38 | May | Austin |
| Micah | 53 | December | Boston |
| Mila | 21 | April | San Francisco |
<end>Please transform the following json data into Markdown:
[
    {
        "Genre": "Fantasy",
        "Box Office Earnings (M)": 302.72
    },
    {
        "Genre": "Adventure",
        "Box Office Earnings (M)": 302.72
    },
    {
        "Genre": "Fantasy",
        "Box Office Earnings (M)": 311.94
    },
    {
        "Genre": "Drama",
        "Box Office Earnings (M)": 155.39
    },
    {
        "Genre": "Fantasy",
        "Box Office Earnings (M)": 830.22
    },
    {
        "Genre": "Horror",
        "Box Office Earnings (M)": 462.73
    }
]<start>
| Genre | Box Office Earnings (M) |
| --- | --- |
| Fantasy | 302.72 |
| Adventure | 302.72 |
| Fantasy | 311.94 |
| Drama | 155.39 |
| Fantasy | 830.22 |
| Horror | 462.73 |
<end>Here's some yml data, can you convert it to Markdown?
- Distance (miles): 1756.6
  Duration (hours): 32.4
  End Location: Los Angeles
- Distance (miles): 1719.0
  Duration (hours): 23.1
  End Location: Miami
- Distance (miles): 1041.0
  Duration (hours): 13.3
  End Location: Miami
- Distance (miles): 1719.0
  Duration (hours): 51.2
  End Location: Denver
- Distance (miles): 2324.0
  Duration (hours): 53.6
  End Location: New York
- Distance (miles): 1356.2
  Duration (hours): 38.7
  End Location: Denver
<start>
| End Location | Distance (miles) | Duration (hours) |
| --- | --- | --- |
| Los Angeles | 1756.6 | 32.4 |
| Miami | 1719.0 | 23.1 |
| Miami | 1041.0 | 13.3 |
| Denver | 1719.0 | 51.2 |
| New York | 2324.0 | 53.6 |
| Denver | 1356.2 | 38.7 |
<end>Convert this plain text to markdown:
Trip Name: Lakeside Retreat | End Location: Los Angeles | Distance (miles): 1550.2 | Duration (hours): 10.8 | Fuel Used (gallons): 81.8
Trip Name: Lakeside Retreat | End Location: Miami | Distance (miles): 2532.2 | Duration (hours): 13.2 | Fuel Used (gallons): 91.9
Trip Name: Valley Voyage | End Location: Los Angeles | Distance (miles): 2411.4 | Duration (hours): 59.7 | Fuel Used (gallons): 46.3
<start>
| Trip Name | End Location | Distance (miles) | Duration (hours) | Fuel Used (gallons) |
| --- | --- | --- | --- | --- |
| Lakeside Retreat | Los Angeles | 1550.2 | 10.8 | 81.8 |
| Lakeside Retreat | Miami | 2532.2 | 13.2 | 91.9 |
| Valley Voyage | Los Angeles | 2411.4 | 59.7 | 46.3 |
<end>