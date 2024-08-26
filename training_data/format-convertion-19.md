Here's some csv data, can you convert it to Json?
Company,Date,Open Price,Close Price
FoodChain,2014-07-08,208.01,1391.82
FoodChain,2010-08-25,441.24,504.04
FinanceTrust,2015-02-22,1309.66,1054.53
AeroSystems,2011-02-21,1391.82,1092.97
<start>
[
    {
        "Company": "FoodChain",
        "Date": "2014-07-08",
        "Open Price": 208.01,
        "Close Price": 1391.82
    },
    {
        "Company": "FoodChain",
        "Date": "2010-08-25",
        "Open Price": 441.24,
        "Close Price": 504.04
    },
    {
        "Company": "FinanceTrust",
        "Date": "2015-02-22",
        "Open Price": 1309.66,
        "Close Price": 1054.53
    },
    {
        "Company": "AeroSystems",
        "Date": "2011-02-21",
        "Open Price": 1391.82,
        "Close Price": 1092.97
    }
]
<end>Transform this plain text structure to a CSV format:
Title: Mystery of the Depths | Release Year: 2023 | Box Office Earnings (M): 407.29
Title: The Great Expedition | Release Year: 1977 | Box Office Earnings (M): 474.83
Title: Rise of the Titans | Release Year: 1974 | Box Office Earnings (M): 274.3
Title: Edge of Infinity | Release Year: 1992 | Box Office Earnings (M): 672.85
Title: Rise of the Titans | Release Year: 2021 | Box Office Earnings (M): 235.37
Title: Starbound Odyssey | Release Year: 1992 | Box Office Earnings (M): 687.37
Title: Escape from Earth | Release Year: 2009 | Box Office Earnings (M): 935.09
Title: Escape from Earth | Release Year: 1997 | Box Office Earnings (M): 645.77
<start>
Title,Release Year,Box Office Earnings (M)
Mystery of the Depths,2023,407.29
The Great Expedition,1977,474.83
Rise of the Titans,1974,274.3
Edge of Infinity,1992,672.85
Rise of the Titans,2021,235.37
Starbound Odyssey,1992,687.37
Escape from Earth,2009,935.09
Escape from Earth,1997,645.77
<end>Here's some MARKDOWN data, can you convert it to json?
| Trip Name | Start Location | Distance (miles) | Duration (hours) | Fuel Used (gallons) |
| --- | --- | --- | --- | --- |
| Lakeside Retreat | New York | 2784.4 | 38.9 | 34.3 |
| Highway Odyssey | San Francisco | 2657.3 | 50.9 | 9.0 |
| Canyon Trek | New York | 661.9 | 28.3 | 79.8 |
| Highway Odyssey | New York | 2784.4 | 31.5 | 86.5 |<start>
[
    {
        "Trip Name": "Lakeside Retreat",
        "Start Location": "New York",
        "Distance (miles)": 2784.4,
        "Duration (hours)": 38.9,
        "Fuel Used (gallons)": 34.3
    },
    {
        "Trip Name": "Highway Odyssey",
        "Start Location": "San Francisco",
        "Distance (miles)": 2657.3,
        "Duration (hours)": 50.9,
        "Fuel Used (gallons)": 9.0
    },
    {
        "Trip Name": "Canyon Trek",
        "Start Location": "New York",
        "Distance (miles)": 661.9,
        "Duration (hours)": 28.3,
        "Fuel Used (gallons)": 79.8
    },
    {
        "Trip Name": "Highway Odyssey",
        "Start Location": "New York",
        "Distance (miles)": 2784.4,
        "Duration (hours)": 31.5,
        "Fuel Used (gallons)": 86.5
    }
]
<end>Transform this csv structure to a YML format:
Location,Temperature (C),Humidity (%),Wind Speed (km/h),Day
Phoenix,-8.4,44,12.7,Friday
New York,-9.0,63,9.2,Tuesday
Denver,22.8,56,3.6,Wednesday
Houston,12.2,29,21.7,Sunday
Los Angeles,-9.0,63,29.2,Wednesday
Los Angeles,24.5,98,28.7,Sunday
Denver,6.4,63,13.9,Monday
Seattle,-1.9,73,19.9,Wednesday
<start>
- Day: Friday
  Humidity (%): 44
  Location: Phoenix
  Temperature (C): -8.4
  Wind Speed (km/h): 12.7
- Day: Tuesday
  Humidity (%): 63
  Location: New York
  Temperature (C): -9.0
  Wind Speed (km/h): 9.2
- Day: Wednesday
  Humidity (%): 56
  Location: Denver
  Temperature (C): 22.8
  Wind Speed (km/h): 3.6
- Day: Sunday
  Humidity (%): 29
  Location: Houston
  Temperature (C): 12.2
  Wind Speed (km/h): 21.7
- Day: Wednesday
  Humidity (%): 63
  Location: Los Angeles
  Temperature (C): -9.0
  Wind Speed (km/h): 29.2
- Day: Sunday
  Humidity (%): 98
  Location: Los Angeles
  Temperature (C): 24.5
  Wind Speed (km/h): 28.7
- Day: Monday
  Humidity (%): 63
  Location: Denver
  Temperature (C): 6.4
  Wind Speed (km/h): 13.9
- Day: Wednesday
  Humidity (%): 73
  Location: Seattle
  Temperature (C): -1.9
  Wind Speed (km/h): 19.9
<end>Convert this csv to yaml:
Device ID,Device Type,Location,Battery Level (%)
device-0022,Light Sensor,Bathroom,33.0
device-0033,Temperature Sensor,Bedroom,76.2
device-0028,Temperature Sensor,Bathroom,82.9
device-0056,Humidity Sensor,Garage,72.1
device-0047,Humidity Sensor,Bedroom,82.9
<start>
- Battery Level (%): 33.0
  Device ID: device-0022
  Device Type: Light Sensor
  Location: Bathroom
- Battery Level (%): 76.2
  Device ID: device-0033
  Device Type: Temperature Sensor
  Location: Bedroom
- Battery Level (%): 82.9
  Device ID: device-0028
  Device Type: Temperature Sensor
  Location: Bathroom
- Battery Level (%): 72.1
  Device ID: device-0056
  Device Type: Humidity Sensor
  Location: Garage
- Battery Level (%): 82.9
  Device ID: device-0047
  Device Type: Humidity Sensor
  Location: Bedroom
<end>Transform this markdown structure to a Plain text format:
| Title | Genre | Publication Year |
| --- | --- | --- |
| Whispers of the Abyss | Fantasy | 1994 |
| Whispers of the Abyss | Romance | 2005 |
| Whispers of the Abyss | Non-Fiction | 2010 |<start>
Title: Whispers of the Abyss | Genre: Fantasy | Publication Year: 1994
Title: Whispers of the Abyss | Genre: Romance | Publication Year: 2005
Title: Whispers of the Abyss | Genre: Non-Fiction | Publication Year: 2010
<end>Can you change this CSV into markdown?
Restaurant Name,Cuisine,Location,Price Range
The Golden Spoon,Mediterranean,Chicago,$$$
The Golden Spoon,American,Miami,$$$
Pasta Palace,Japanese,San Francisco,$$$
Pasta Palace,Italian,San Francisco,$
<start>
| Restaurant Name | Cuisine | Location | Price Range |
| --- | --- | --- | --- |
| The Golden Spoon | Mediterranean | Chicago | $$$ |
| The Golden Spoon | American | Miami | $$$ |
| Pasta Palace | Japanese | San Francisco | $$$ |
| Pasta Palace | Italian | San Francisco | $ |
<end>Transform this plain text structure to a yml format:
Restaurant Name: Pasta Palace | Cuisine: Mexican | Location: New York | Rating: 3 | Price Range: $$$
Restaurant Name: BBQ Barn | Cuisine: French | Location: New York | Rating: 1 | Price Range: $$$$
Restaurant Name: BBQ Barn | Cuisine: Mexican | Location: San Francisco | Rating: 1 | Price Range: $$$$$
Restaurant Name: Taco Town | Cuisine: American | Location: Phoenix | Rating: 3 | Price Range: $$$
Restaurant Name: BBQ Barn | Cuisine: Japanese | Location: New York | Rating: 2 | Price Range: $
Restaurant Name: Sushi World | Cuisine: American | Location: Miami | Rating: 1 | Price Range: $$$
Restaurant Name: Pizza Planet | Cuisine: Mexican | Location: Houston | Rating: 3 | Price Range: $$
<start>
- Cuisine: Mexican
  Location: New York
  Price Range: $$$
  Rating: 3
  Restaurant Name: Pasta Palace
- Cuisine: French
  Location: New York
  Price Range: $$$$
  Rating: 1
  Restaurant Name: BBQ Barn
- Cuisine: Mexican
  Location: San Francisco
  Price Range: $$$$$
  Rating: 1
  Restaurant Name: BBQ Barn
- Cuisine: American
  Location: Phoenix
  Price Range: $$$
  Rating: 3
  Restaurant Name: Taco Town
- Cuisine: Japanese
  Location: New York
  Price Range: $
  Rating: 2
  Restaurant Name: BBQ Barn
- Cuisine: American
  Location: Miami
  Price Range: $$$
  Rating: 1
  Restaurant Name: Sushi World
- Cuisine: Mexican
  Location: Houston
  Price Range: $$
  Rating: 3
  Restaurant Name: Pizza Planet
<end>Convert this Plain text to Json:
Product Name: Device | SKU: SKU-1012 | Price: 481.7 | Stock Quantity: 445 | Category: Sports | Supplier Name: Wonka Industries
Product Name: Gadget | SKU: SKU-1033 | Price: 92.55 | Stock Quantity: 470 | Category: Automotive | Supplier Name: Wonka Industries
Product Name: Instrument | SKU: SKU-1031 | Price: 350.8 | Stock Quantity: 186 | Category: Household | Supplier Name: Wonka Industries
Product Name: Widget | SKU: SKU-1073 | Price: 181.61 | Stock Quantity: 22 | Category: Sports | Supplier Name: Wayne Enterprises
Product Name: Doohickey | SKU: SKU-1043 | Price: 27.4 | Stock Quantity: 343 | Category: Toys | Supplier Name: Umbrella Corp
Product Name: Apparatus | SKU: SKU-1004 | Price: 98.01 | Stock Quantity: 225 | Category: Toys | Supplier Name: Wonka Industries
Product Name: Apparatus | SKU: SKU-1045 | Price: 13.86 | Stock Quantity: 25 | Category: Electronics | Supplier Name: Wonka Industries
Product Name: Thingamajig | SKU: SKU-1077 | Price: 253.05 | Stock Quantity: 457 | Category: Sports | Supplier Name: Wonka Industries
Product Name: Instrument | SKU: SKU-1045 | Price: 433.02 | Stock Quantity: 294 | Category: Electronics | Supplier Name: Wayne Enterprises
<start>
[
    {
        "Product Name": "Device",
        "SKU": "SKU-1012",
        "Price": 481.7,
        "Stock Quantity": 445,
        "Category": "Sports",
        "Supplier Name": "Wonka Industries"
    },
    {
        "Product Name": "Gadget",
        "SKU": "SKU-1033",
        "Price": 92.55,
        "Stock Quantity": 470,
        "Category": "Automotive",
        "Supplier Name": "Wonka Industries"
    },
    {
        "Product Name": "Instrument",
        "SKU": "SKU-1031",
        "Price": 350.8,
        "Stock Quantity": 186,
        "Category": "Household",
        "Supplier Name": "Wonka Industries"
    },
    {
        "Product Name": "Widget",
        "SKU": "SKU-1073",
        "Price": 181.61,
        "Stock Quantity": 22,
        "Category": "Sports",
        "Supplier Name": "Wayne Enterprises"
    },
    {
        "Product Name": "Doohickey",
        "SKU": "SKU-1043",
        "Price": 27.4,
        "Stock Quantity": 343,
        "Category": "Toys",
        "Supplier Name": "Umbrella Corp"
    },
    {
        "Product Name": "Apparatus",
        "SKU": "SKU-1004",
        "Price": 98.01,
        "Stock Quantity": 225,
        "Category": "Toys",
        "Supplier Name": "Wonka Industries"
    },
    {
        "Product Name": "Apparatus",
        "SKU": "SKU-1045",
        "Price": 13.86,
        "Stock Quantity": 25,
        "Category": "Electronics",
        "Supplier Name": "Wonka Industries"
    },
    {
        "Product Name": "Thingamajig",
        "SKU": "SKU-1077",
        "Price": 253.05,
        "Stock Quantity": 457,
        "Category": "Sports",
        "Supplier Name": "Wonka Industries"
    },
    {
        "Product Name": "Instrument",
        "SKU": "SKU-1045",
        "Price": 433.02,
        "Stock Quantity": 294,
        "Category": "Electronics",
        "Supplier Name": "Wayne Enterprises"
    }
]
<end>Convert this YML to plain text:
- Age: 54
  Birth Month: August
  Name: Sheena
- Age: 47
  Birth Month: November
  Name: Lynda
- Age: 32
  Birth Month: May
  Name: Norma
- Age: 48
  Birth Month: March
  Name: Mable
- Age: 30
  Birth Month: October
  Name: Marsha
- Age: 26
  Birth Month: June
  Name: Edward
- Age: 31
  Birth Month: August
  Name: Janet
<start>
Name: Sheena | Age: 54 | Birth Month: August
Name: Lynda | Age: 47 | Birth Month: November
Name: Norma | Age: 32 | Birth Month: May
Name: Mable | Age: 48 | Birth Month: March
Name: Marsha | Age: 30 | Birth Month: October
Name: Edward | Age: 26 | Birth Month: June
Name: Janet | Age: 31 | Birth Month: August
<end>Can you change this plain text into CSV?
Company: RetailWorld | Date: 2011-12-21 | Open Price: 162.94 | Close Price: 334.42 | High Price: 1435.91 | Low Price: 56.91 | Volume: 8138549
Company: RetailWorld | Date: 2019-10-18 | Open Price: 18.01 | Close Price: 1118.92 | High Price: 1118.92 | Low Price: 18.01 | Volume: 9213888
Company: FinanceTrust | Date: 2014-10-04 | Open Price: 107.21 | Close Price: 1494.8 | High Price: 1494.8 | Low Price: 107.21 | Volume: 7507277
Company: HealthGen | Date: 2021-04-01 | Open Price: 1241.85 | Close Price: 163.51 | High Price: 1241.85 | Low Price: 162.94 | Volume: 8138549
Company: AutoMotive | Date: 2010-07-12 | Open Price: 689.92 | Close Price: 359.34 | High Price: 689.92 | Low Price: 359.34 | Volume: 4876923
Company: FinanceTrust | Date: 2017-11-12 | Open Price: 546.83 | Close Price: 457.65 | High Price: 1253.66 | Low Price: 457.65 | Volume: 363566
<start>
Company,Date,Open Price,Close Price,High Price,Low Price,Volume
RetailWorld,2011-12-21,162.94,334.42,1435.91,56.91,8138549
RetailWorld,2019-10-18,18.01,1118.92,1118.92,18.01,9213888
FinanceTrust,2014-10-04,107.21,1494.8,1494.8,107.21,7507277
HealthGen,2021-04-01,1241.85,163.51,1241.85,162.94,8138549
AutoMotive,2010-07-12,689.92,359.34,689.92,359.34,4876923
FinanceTrust,2017-11-12,546.83,457.65,1253.66,457.65,363566
<end>Transform this Csv structure to a Json format:
Product Name,SKU,Stock Quantity,Category,Supplier Name
Thingamajig,SKU-1090,75,Electronics,Wonka Industries
Doohickey,SKU-1018,330,Toys,Wayne Enterprises
Contraption,SKU-1000,55,Automotive,ACME Corp
Widget,SKU-1080,67,Automotive,ACME Corp
Device,SKU-1012,302,Automotive,Wonka Industries
Contraption,SKU-1092,441,Sports,Wonka Industries
Contraption,SKU-1073,363,Sports,Globex
Contraption,SKU-1046,472,Electronics,Wonka Industries
Gadget,SKU-1041,371,Toys,Wonka Industries
Device,SKU-1071,391,Household,Wayne Enterprises
<start>
[
    {
        "Product Name": "Thingamajig",
        "SKU": "SKU-1090",
        "Stock Quantity": 75,
        "Category": "Electronics",
        "Supplier Name": "Wonka Industries"
    },
    {
        "Product Name": "Doohickey",
        "SKU": "SKU-1018",
        "Stock Quantity": 330,
        "Category": "Toys",
        "Supplier Name": "Wayne Enterprises"
    },
    {
        "Product Name": "Contraption",
        "SKU": "SKU-1000",
        "Stock Quantity": 55,
        "Category": "Automotive",
        "Supplier Name": "ACME Corp"
    },
    {
        "Product Name": "Widget",
        "SKU": "SKU-1080",
        "Stock Quantity": 67,
        "Category": "Automotive",
        "Supplier Name": "ACME Corp"
    },
    {
        "Product Name": "Device",
        "SKU": "SKU-1012",
        "Stock Quantity": 302,
        "Category": "Automotive",
        "Supplier Name": "Wonka Industries"
    },
    {
        "Product Name": "Contraption",
        "SKU": "SKU-1092",
        "Stock Quantity": 441,
        "Category": "Sports",
        "Supplier Name": "Wonka Industries"
    },
    {
        "Product Name": "Contraption",
        "SKU": "SKU-1073",
        "Stock Quantity": 363,
        "Category": "Sports",
        "Supplier Name": "Globex"
    },
    {
        "Product Name": "Contraption",
        "SKU": "SKU-1046",
        "Stock Quantity": 472,
        "Category": "Electronics",
        "Supplier Name": "Wonka Industries"
    },
    {
        "Product Name": "Gadget",
        "SKU": "SKU-1041",
        "Stock Quantity": 371,
        "Category": "Toys",
        "Supplier Name": "Wonka Industries"
    },
    {
        "Product Name": "Device",
        "SKU": "SKU-1071",
        "Stock Quantity": 391,
        "Category": "Household",
        "Supplier Name": "Wayne Enterprises"
    }
]
<end>Can you change this MARKDOWN into yaml?
| Title | Director | Genre | Release Year | Box Office Earnings (M) |
| --- | --- | --- | --- | --- |
| Beyond the Veil | Talon Blackthorn | Drama | 2022 | 519.02 |
| Dreamwalker | Zara Stormrider | Sci-Fi | 2018 | 272.87 |
| Escape from Earth | Talon Blackthorn | Thriller | 1987 | 225.28 |
| The Endless Horizon | Zara Stormrider | Adventure | 1975 | 890.21 |
| Dreamwalker | Aria Ravenwood | Comedy | 2006 | 531.78 |
| The Endless Horizon | Aria Ravenwood | Action | 1976 | 497.81 |
| Starbound Odyssey | Orin Shadowalker | Sci-Fi | 1977 | 647.98 |
| The Great Expedition | Selene Darkwhisper | Comedy | 1976 | 601.34 |<start>
- Box Office Earnings (M): 519.02
  Director: Talon Blackthorn
  Genre: Drama
  Release Year: 2022
  Title: Beyond the Veil
- Box Office Earnings (M): 272.87
  Director: Zara Stormrider
  Genre: Sci-Fi
  Release Year: 2018
  Title: Dreamwalker
- Box Office Earnings (M): 225.28
  Director: Talon Blackthorn
  Genre: Thriller
  Release Year: 1987
  Title: Escape from Earth
- Box Office Earnings (M): 890.21
  Director: Zara Stormrider
  Genre: Adventure
  Release Year: 1975
  Title: The Endless Horizon
- Box Office Earnings (M): 531.78
  Director: Aria Ravenwood
  Genre: Comedy
  Release Year: 2006
  Title: Dreamwalker
- Box Office Earnings (M): 497.81
  Director: Aria Ravenwood
  Genre: Action
  Release Year: 1976
  Title: The Endless Horizon
- Box Office Earnings (M): 647.98
  Director: Orin Shadowalker
  Genre: Sci-Fi
  Release Year: 1977
  Title: Starbound Odyssey
- Box Office Earnings (M): 601.34
  Director: Selene Darkwhisper
  Genre: Comedy
  Release Year: 1976
  Title: The Great Expedition
<end>Convert this csv to json:
Condition,Temperature (C),Humidity (%),Wind Speed (km/h),Day
Foggy,0.7,93,9.4,Wednesday
Snowy,-5.5,97,9.1,Monday
Sunny,-9.8,21,10.4,Sunday
Rainy,33.3,56,13.4,Thursday
Cloudy,-2.2,94,29.4,Sunday
Windy,18.7,50,2.7,Thursday
Sunny,-8.9,76,18.9,Sunday
Cloudy,33.3,78,27.8,Sunday
<start>
[
    {
        "Condition": "Foggy",
        "Temperature (C)": 0.7,
        "Humidity (%)": 93,
        "Wind Speed (km/h)": 9.4,
        "Day": "Wednesday"
    },
    {
        "Condition": "Snowy",
        "Temperature (C)": -5.5,
        "Humidity (%)": 97,
        "Wind Speed (km/h)": 9.1,
        "Day": "Monday"
    },
    {
        "Condition": "Sunny",
        "Temperature (C)": -9.8,
        "Humidity (%)": 21,
        "Wind Speed (km/h)": 10.4,
        "Day": "Sunday"
    },
    {
        "Condition": "Rainy",
        "Temperature (C)": 33.3,
        "Humidity (%)": 56,
        "Wind Speed (km/h)": 13.4,
        "Day": "Thursday"
    },
    {
        "Condition": "Cloudy",
        "Temperature (C)": -2.2,
        "Humidity (%)": 94,
        "Wind Speed (km/h)": 29.4,
        "Day": "Sunday"
    },
    {
        "Condition": "Windy",
        "Temperature (C)": 18.7,
        "Humidity (%)": 50,
        "Wind Speed (km/h)": 2.7,
        "Day": "Thursday"
    },
    {
        "Condition": "Sunny",
        "Temperature (C)": -8.9,
        "Humidity (%)": 76,
        "Wind Speed (km/h)": 18.9,
        "Day": "Sunday"
    },
    {
        "Condition": "Cloudy",
        "Temperature (C)": 33.3,
        "Humidity (%)": 78,
        "Wind Speed (km/h)": 27.8,
        "Day": "Sunday"
    }
]
<end>Convert this csv to markdown:
Database Name,Queries per Second,Cache Hit Ratio (%),Connection Count,Average Latency (ms),Timestamp
OrdersDB,4496.0,85.19,186,44.67,2023-05-18 07:38:36
ProfilesDB,1363.54,80.16,232,85.79,2023-06-09 12:56:27
MetricsDB,1737.14,85.13,389,54.31,2021-09-02 21:54:36
LogsDB,3706.84,84.83,325,71.27,2021-10-09 02:37:00
<start>
| Database Name | Queries per Second | Cache Hit Ratio (%) | Connection Count | Average Latency (ms) | Timestamp |
| --- | --- | --- | --- | --- | --- |
| OrdersDB | 4496.0 | 85.19 | 186 | 44.67 | 2023-05-18 07:38:36 |
| ProfilesDB | 1363.54 | 80.16 | 232 | 85.79 | 2023-06-09 12:56:27 |
| MetricsDB | 1737.14 | 85.13 | 389 | 54.31 | 2021-09-02 21:54:36 |
| LogsDB | 3706.84 | 84.83 | 325 | 71.27 | 2021-10-09 02:37:00 |
<end>Please transform the following Csv data into yml:
Condition,Humidity (%),Day
Rainy,56,Saturday
Windy,33,Tuesday
Rainy,90,Thursday
Rainy,94,Friday
Sunny,92,Saturday
Rainy,31,Tuesday
Sunny,33,Monday
<start>
- Condition: Rainy
  Day: Saturday
  Humidity (%): 56
- Condition: Windy
  Day: Tuesday
  Humidity (%): 33
- Condition: Rainy
  Day: Thursday
  Humidity (%): 90
- Condition: Rainy
  Day: Friday
  Humidity (%): 94
- Condition: Sunny
  Day: Saturday
  Humidity (%): 92
- Condition: Rainy
  Day: Tuesday
  Humidity (%): 31
- Condition: Sunny
  Day: Monday
  Humidity (%): 33
<end>Convert this json to markdown:
[
    {
        "Title": "The Crystal Key",
        "Author": "Thorne Ironwood",
        "Genre": "Romance",
        "Rating": 1.3
    },
    {
        "Title": "The Forgotten World",
        "Author": "Thorne Ironwood",
        "Genre": "Historical",
        "Rating": 1.8
    },
    {
        "Title": "Legends of the Rift",
        "Author": "Kara Firebrand",
        "Genre": "Romance",
        "Rating": 2.1
    },
    {
        "Title": "Echoes of Eternity",
        "Author": "Thorne Ironwood",
        "Genre": "Science Fiction",
        "Rating": 2.3
    },
    {
        "Title": "Whispers of the Abyss",
        "Author": "Elara Moonshadow",
        "Genre": "Fantasy",
        "Rating": 2.1
    },
    {
        "Title": "Tales of the Brave",
        "Author": "Galen Starfire",
        "Genre": "Thriller",
        "Rating": 4.2
    },
    {
        "Title": "Shadows of Solitude",
        "Author": "Draven Blackthorn",
        "Genre": "Science Fiction",
        "Rating": 4.3
    },
    {
        "Title": "Whispers of the Abyss",
        "Author": "Kara Firebrand",
        "Genre": "Non-Fiction",
        "Rating": 4.6
    },
    {
        "Title": "The Forgotten World",
        "Author": "Rowan Ashborne",
        "Genre": "Romance",
        "Rating": 2.0
    }
]<start>
| Title | Author | Genre | Rating |
| --- | --- | --- | --- |
| The Crystal Key | Thorne Ironwood | Romance | 1.3 |
| The Forgotten World | Thorne Ironwood | Historical | 1.8 |
| Legends of the Rift | Kara Firebrand | Romance | 2.1 |
| Echoes of Eternity | Thorne Ironwood | Science Fiction | 2.3 |
| Whispers of the Abyss | Elara Moonshadow | Fantasy | 2.1 |
| Tales of the Brave | Galen Starfire | Thriller | 4.2 |
| Shadows of Solitude | Draven Blackthorn | Science Fiction | 4.3 |
| Whispers of the Abyss | Kara Firebrand | Non-Fiction | 4.6 |
| The Forgotten World | Rowan Ashborne | Romance | 2.0 |
<end>Transform this yaml structure to a Plain text format:
- Close Price: 681.09
  Date: '2023-05-07'
  Low Price: 681.09
  Open Price: 796.22
  Volume: 1992684
- Close Price: 606.6
  Date: '2019-03-24'
  Low Price: 458.45
  Open Price: 627.27
  Volume: 5104322
- Close Price: 1470.45
  Date: '2019-09-23'
  Low Price: 285.04
  Open Price: 918.2
  Volume: 7646757
- Close Price: 403.07
  Date: '2022-12-18'
  Low Price: 403.07
  Open Price: 457.8
  Volume: 3390253
<start>
Date: 2023-05-07 | Open Price: 796.22 | Close Price: 681.09 | Low Price: 681.09 | Volume: 1992684
Date: 2019-03-24 | Open Price: 627.27 | Close Price: 606.6 | Low Price: 458.45 | Volume: 5104322
Date: 2019-09-23 | Open Price: 918.2 | Close Price: 1470.45 | Low Price: 285.04 | Volume: 7646757
Date: 2022-12-18 | Open Price: 457.8 | Close Price: 403.07 | Low Price: 403.07 | Volume: 3390253
<end>Can you change this csv into plain text?
Trip Name,Start Location,End Location,Distance (miles),Duration (hours),Fuel Used (gallons)
Historic Route,San Francisco,Houston,1637.0,19.4,90.5
Lakeside Retreat,San Francisco,Miami,2288.6,60.2,36.7
Highway Odyssey,Denver,Chicago,2365.1,59.3,21.2
Coast to Coast,Miami,Los Angeles,1805.4,70.8,75.9
Desert Drive,Phoenix,Los Angeles,1805.4,29.1,10.0
<start>
Trip Name: Historic Route | Start Location: San Francisco | End Location: Houston | Distance (miles): 1637.0 | Duration (hours): 19.4 | Fuel Used (gallons): 90.5
Trip Name: Lakeside Retreat | Start Location: San Francisco | End Location: Miami | Distance (miles): 2288.6 | Duration (hours): 60.2 | Fuel Used (gallons): 36.7
Trip Name: Highway Odyssey | Start Location: Denver | End Location: Chicago | Distance (miles): 2365.1 | Duration (hours): 59.3 | Fuel Used (gallons): 21.2
Trip Name: Coast to Coast | Start Location: Miami | End Location: Los Angeles | Distance (miles): 1805.4 | Duration (hours): 70.8 | Fuel Used (gallons): 75.9
Trip Name: Desert Drive | Start Location: Phoenix | End Location: Los Angeles | Distance (miles): 1805.4 | Duration (hours): 29.1 | Fuel Used (gallons): 10.0
<end>Transform this markdown structure to a Plain text format:
| Company | Date | Open Price | Close Price | Low Price | Volume |
| --- | --- | --- | --- | --- | --- |
| MediaGroup | 2019-04-10 | 24.99 | 1217.02 | 24.99 | 173740 |
| HealthGen | 2018-12-17 | 532.4 | 483.04 | 168.31 | 7485340 |
| GreenEnergy | 2017-06-08 | 1153.44 | 237.52 | 237.52 | 2215313 |
| FinanceTrust | 2023-03-06 | 1474.72 | 644.96 | 644.96 | 770380 |
| GreenEnergy | 2011-06-21 | 431.66 | 1217.02 | 431.66 | 1784194 |
| RetailWorld | 2021-07-19 | 969.05 | 266.92 | 266.92 | 5585140 |
| BioLife | 2012-07-18 | 346.46 | 324.66 | 324.66 | 3492584 |
| HealthGen | 2022-12-23 | 535.92 | 940.26 | 535.92 | 3224898 |
| FoodChain | 2020-03-26 | 415.49 | 1483.4 | 415.49 | 3056884 |
| RetailWorld | 2012-07-03 | 969.05 | 1120.75 | 532.4 | 8219936 |<start>
Company: MediaGroup | Date: 2019-04-10 | Open Price: 24.99 | Close Price: 1217.02 | Low Price: 24.99 | Volume: 173740
Company: HealthGen | Date: 2018-12-17 | Open Price: 532.4 | Close Price: 483.04 | Low Price: 168.31 | Volume: 7485340
Company: GreenEnergy | Date: 2017-06-08 | Open Price: 1153.44 | Close Price: 237.52 | Low Price: 237.52 | Volume: 2215313
Company: FinanceTrust | Date: 2023-03-06 | Open Price: 1474.72 | Close Price: 644.96 | Low Price: 644.96 | Volume: 770380
Company: GreenEnergy | Date: 2011-06-21 | Open Price: 431.66 | Close Price: 1217.02 | Low Price: 431.66 | Volume: 1784194
Company: RetailWorld | Date: 2021-07-19 | Open Price: 969.05 | Close Price: 266.92 | Low Price: 266.92 | Volume: 5585140
Company: BioLife | Date: 2012-07-18 | Open Price: 346.46 | Close Price: 324.66 | Low Price: 324.66 | Volume: 3492584
Company: HealthGen | Date: 2022-12-23 | Open Price: 535.92 | Close Price: 940.26 | Low Price: 535.92 | Volume: 3224898
Company: FoodChain | Date: 2020-03-26 | Open Price: 415.49 | Close Price: 1483.4 | Low Price: 415.49 | Volume: 3056884
Company: RetailWorld | Date: 2012-07-03 | Open Price: 969.05 | Close Price: 1120.75 | Low Price: 532.4 | Volume: 8219936
<end>Convert this yaml to plain text:
- Cuisine: Indian
  Rating: 2
- Cuisine: Chinese
  Rating: 4
- Cuisine: Italian
  Rating: 1
- Cuisine: Japanese
  Rating: 3
- Cuisine: Japanese
  Rating: 4
- Cuisine: Chinese
  Rating: 1
- Cuisine: American
  Rating: 2
<start>
Cuisine: Indian | Rating: 2
Cuisine: Chinese | Rating: 4
Cuisine: Italian | Rating: 1
Cuisine: Japanese | Rating: 3
Cuisine: Japanese | Rating: 4
Cuisine: Chinese | Rating: 1
Cuisine: American | Rating: 2
<end>Can you change this json into Markdown?
[
    {
        "Restaurant Name": "Curry Corner",
        "Cuisine": "Italian",
        "Rating": 5,
        "Price Range": "$$$"
    },
    {
        "Restaurant Name": "Sushi World",
        "Cuisine": "French",
        "Rating": 1,
        "Price Range": "$$$$$"
    },
    {
        "Restaurant Name": "Burger Haven",
        "Cuisine": "Mediterranean",
        "Rating": 3,
        "Price Range": "$$$"
    },
    {
        "Restaurant Name": "Vegan Delight",
        "Cuisine": "Mediterranean",
        "Rating": 2,
        "Price Range": "$$$$$"
    },
    {
        "Restaurant Name": "Pasta Palace",
        "Cuisine": "Italian",
        "Rating": 2,
        "Price Range": "$"
    }
]<start>
| Restaurant Name | Cuisine | Rating | Price Range |
| --- | --- | --- | --- |
| Curry Corner | Italian | 5 | $$$ |
| Sushi World | French | 1 | $$$$$ |
| Burger Haven | Mediterranean | 3 | $$$ |
| Vegan Delight | Mediterranean | 2 | $$$$$ |
| Pasta Palace | Italian | 2 | $ |
<end>Please transform the following json data into Csv:
[
    {
        "Company": "FinanceTrust",
        "Date": "2021-06-24",
        "Open Price": 1378.84,
        "Close Price": 364.9,
        "High Price": 1378.84,
        "Low Price": 364.9
    },
    {
        "Company": "FoodChain",
        "Date": "2011-12-10",
        "Open Price": 1283.61,
        "Close Price": 1387.28,
        "High Price": 1387.28,
        "Low Price": 275.25
    },
    {
        "Company": "AeroSystems",
        "Date": "2012-08-19",
        "Open Price": 842.8,
        "Close Price": 1089.85,
        "High Price": 1089.85,
        "Low Price": 450.81
    },
    {
        "Company": "FinanceTrust",
        "Date": "2010-09-02",
        "Open Price": 635.37,
        "Close Price": 195.15,
        "High Price": 1261.68,
        "Low Price": 195.15
    },
    {
        "Company": "RetailWorld",
        "Date": "2022-04-11",
        "Open Price": 1000.54,
        "Close Price": 359.53,
        "High Price": 1000.54,
        "Low Price": 359.53
    },
    {
        "Company": "RetailWorld",
        "Date": "2022-04-08",
        "Open Price": 1047.17,
        "Close Price": 450.81,
        "High Price": 1447.14,
        "Low Price": 421.02
    },
    {
        "Company": "GreenEnergy",
        "Date": "2016-11-06",
        "Open Price": 833.84,
        "Close Price": 679.73,
        "High Price": 833.84,
        "Low Price": 247.19
    }
]<start>
Company,Date,Open Price,Close Price,High Price,Low Price
FinanceTrust,2021-06-24,1378.84,364.9,1378.84,364.9
FoodChain,2011-12-10,1283.61,1387.28,1387.28,275.25
AeroSystems,2012-08-19,842.8,1089.85,1089.85,450.81
FinanceTrust,2010-09-02,635.37,195.15,1261.68,195.15
RetailWorld,2022-04-11,1000.54,359.53,1000.54,359.53
RetailWorld,2022-04-08,1047.17,450.81,1447.14,421.02
GreenEnergy,2016-11-06,833.84,679.73,833.84,247.19
<end>Convert this PLAIN TEXT to yml:
Location: San Francisco | Price Range: $$$$
Location: San Francisco | Price Range: $$$
Location: Los Angeles | Price Range: $$
Location: Houston | Price Range: $$
Location: Houston | Price Range: $$
Location: New York | Price Range: $$$$$
Location: Chicago | Price Range: $$$$$
<start>
- Location: San Francisco
  Price Range: $$$$
- Location: San Francisco
  Price Range: $$$
- Location: Los Angeles
  Price Range: $$
- Location: Houston
  Price Range: $$
- Location: Houston
  Price Range: $$
- Location: New York
  Price Range: $$$$$
- Location: Chicago
  Price Range: $$$$$
<end>Convert this Plain text to yml:
Trip Name: City Explorer | Start Location: Houston | End Location: Los Angeles | Duration (hours): 10.0 | Fuel Used (gallons): 18.6
Trip Name: Canyon Trek | Start Location: San Francisco | End Location: Houston | Duration (hours): 35.4 | Fuel Used (gallons): 62.8
Trip Name: Lakeside Retreat | Start Location: Chicago | End Location: Los Angeles | Duration (hours): 24.4 | Fuel Used (gallons): 95.4
<start>
- Duration (hours): 10.0
  End Location: Los Angeles
  Fuel Used (gallons): 18.6
  Start Location: Houston
  Trip Name: City Explorer
- Duration (hours): 35.4
  End Location: Houston
  Fuel Used (gallons): 62.8
  Start Location: San Francisco
  Trip Name: Canyon Trek
- Duration (hours): 24.4
  End Location: Los Angeles
  Fuel Used (gallons): 95.4
  Start Location: Chicago
  Trip Name: Lakeside Retreat
<end>Please transform the following markdown data into Csv:
| Trip Name | Start Location | Distance (miles) |
| --- | --- | --- |
| Mountain Adventure | Miami | 2921.1 |
| Forest Journey | New York | 1004.9 |
| Highway Odyssey | New York | 2481.2 |
| Coast to Coast | Miami | 2481.2 |
| Canyon Trek | New York | 891.3 |
| Forest Journey | Miami | 145.7 |
| Historic Route | Los Angeles | 1836.3 |<start>
Trip Name,Start Location,Distance (miles)
Mountain Adventure,Miami,2921.1
Forest Journey,New York,1004.9
Highway Odyssey,New York,2481.2
Coast to Coast,Miami,2481.2
Canyon Trek,New York,891.3
Forest Journey,Miami,145.7
Historic Route,Los Angeles,1836.3
<end>Convert this json to MARKDOWN:
[
    {
        "Company": "AutoDrive",
        "Sector": "Retail",
        "Market Cap": "Mid Cap",
        "Stock Price": 823.28,
        "Annual Revenue (B)": 345.38,
        "Quarter": "Q3"
    },
    {
        "Company": "HealthPlus",
        "Sector": "Finance",
        "Market Cap": "Mid Cap",
        "Stock Price": 484.69,
        "Annual Revenue (B)": 461.33,
        "Quarter": "Q1"
    },
    {
        "Company": "AeroSpace",
        "Sector": "Aerospace",
        "Market Cap": "Mega Cap",
        "Stock Price": 978.82,
        "Annual Revenue (B)": 91.24,
        "Quarter": "Q3"
    },
    {
        "Company": "GlobalTrade",
        "Sector": "Aerospace",
        "Market Cap": "Large Cap",
        "Stock Price": 738.16,
        "Annual Revenue (B)": 328.9,
        "Quarter": "Q4"
    }
]<start>
| Company | Sector | Market Cap | Stock Price | Annual Revenue (B) | Quarter |
| --- | --- | --- | --- | --- | --- |
| AutoDrive | Retail | Mid Cap | 823.28 | 345.38 | Q3 |
| HealthPlus | Finance | Mid Cap | 484.69 | 461.33 | Q1 |
| AeroSpace | Aerospace | Mega Cap | 978.82 | 91.24 | Q3 |
| GlobalTrade | Aerospace | Large Cap | 738.16 | 328.9 | Q4 |
<end>Can you change this csv into Json?
Name,City,Income
Wayne,Boston,60000
Minnie,Los Angeles,245000
Miriam,San Diego,60000
<start>
[
    {
        "Name": "Wayne",
        "City": "Boston",
        "Income": 60000
    },
    {
        "Name": "Minnie",
        "City": "Los Angeles",
        "Income": 245000
    },
    {
        "Name": "Miriam",
        "City": "San Diego",
        "Income": 60000
    }
]
<end>Can you change this plain text into markdown?
Title: Starbound Odyssey | Director: Orin Shadowalker | Genre: Sci-Fi | Release Year: 1986 | Box Office Earnings (M): 494.84
Title: Escape from Earth | Director: Mara Moonshadow | Genre: Sci-Fi | Release Year: 2001 | Box Office Earnings (M): 72.45
Title: The Great Expedition | Director: Mara Moonshadow | Genre: Horror | Release Year: 2001 | Box Office Earnings (M): 219.21
Title: Edge of Infinity | Director: Aria Ravenwood | Genre: Thriller | Release Year: 2008 | Box Office Earnings (M): 251.67
Title: The Endless Horizon | Director: Lira Silverleaf | Genre: Thriller | Release Year: 2003 | Box Office Earnings (M): 220.41
Title: Rise of the Titans | Director: Rylan Frostblade | Genre: Comedy | Release Year: 2001 | Box Office Earnings (M): 599.81
Title: Edge of Infinity | Director: Orin Shadowalker | Genre: Drama | Release Year: 1993 | Box Office Earnings (M): 323.37
Title: Starbound Odyssey | Director: Lira Silverleaf | Genre: Fantasy | Release Year: 2019 | Box Office Earnings (M): 755.67
Title: Rise of the Titans | Director: Mara Moonshadow | Genre: Comedy | Release Year: 1990 | Box Office Earnings (M): 362.43
<start>
| Title | Director | Genre | Release Year | Box Office Earnings (M) |
| --- | --- | --- | --- | --- |
| Starbound Odyssey | Orin Shadowalker | Sci-Fi | 1986 | 494.84 |
| Escape from Earth | Mara Moonshadow | Sci-Fi | 2001 | 72.45 |
| The Great Expedition | Mara Moonshadow | Horror | 2001 | 219.21 |
| Edge of Infinity | Aria Ravenwood | Thriller | 2008 | 251.67 |
| The Endless Horizon | Lira Silverleaf | Thriller | 2003 | 220.41 |
| Rise of the Titans | Rylan Frostblade | Comedy | 2001 | 599.81 |
| Edge of Infinity | Orin Shadowalker | Drama | 1993 | 323.37 |
| Starbound Odyssey | Lira Silverleaf | Fantasy | 2019 | 755.67 |
| Rise of the Titans | Mara Moonshadow | Comedy | 1990 | 362.43 |
<end>Convert this PLAIN TEXT to CSV:
Title: Mystery of the Depths | Director: Talon Blackthorn | Genre: Comedy | Release Year: 2020 | Box Office Earnings (M): 501.28
Title: The Endless Horizon | Director: Zara Stormrider | Genre: Comedy | Release Year: 2020 | Box Office Earnings (M): 742.28
Title: Beyond the Veil | Director: Orin Shadowalker | Genre: Fantasy | Release Year: 1990 | Box Office Earnings (M): 941.2
Title: Rise of the Titans | Director: Talon Blackthorn | Genre: Action | Release Year: 1999 | Box Office Earnings (M): 377.61
Title: The Final Voyage | Director: Rylan Frostblade | Genre: Adventure | Release Year: 1986 | Box Office Earnings (M): 183.48
Title: Edge of Infinity | Director: Aria Ravenwood | Genre: Drama | Release Year: 2001 | Box Office Earnings (M): 240.43
Title: Mystery of the Depths | Director: Zara Stormrider | Genre: Thriller | Release Year: 2012 | Box Office Earnings (M): 216.28
<start>
Title,Director,Genre,Release Year,Box Office Earnings (M)
Mystery of the Depths,Talon Blackthorn,Comedy,2020,501.28
The Endless Horizon,Zara Stormrider,Comedy,2020,742.28
Beyond the Veil,Orin Shadowalker,Fantasy,1990,941.2
Rise of the Titans,Talon Blackthorn,Action,1999,377.61
The Final Voyage,Rylan Frostblade,Adventure,1986,183.48
Edge of Infinity,Aria Ravenwood,Drama,2001,240.43
Mystery of the Depths,Zara Stormrider,Thriller,2012,216.28
<end>Please transform the following json data into yml:
[
    {
        "Company": "RetailHub",
        "Sector": "Automotive",
        "Market Cap": "Small Cap",
        "Annual Revenue (B)": 216.12,
        "Quarter": "Q2"
    },
    {
        "Company": "TechCorp",
        "Sector": "Retail",
        "Market Cap": "Mid Cap",
        "Annual Revenue (B)": 335.68,
        "Quarter": "Q4"
    },
    {
        "Company": "AutoDrive",
        "Sector": "Retail",
        "Market Cap": "Large Cap",
        "Annual Revenue (B)": 304.76,
        "Quarter": "Q4"
    },
    {
        "Company": "HealthPlus",
        "Sector": "Finance",
        "Market Cap": "Small Cap",
        "Annual Revenue (B)": 344.14,
        "Quarter": "Q4"
    },
    {
        "Company": "RetailHub",
        "Sector": "Finance",
        "Market Cap": "Mega Cap",
        "Annual Revenue (B)": 428.53,
        "Quarter": "Q3"
    }
]<start>
- Annual Revenue (B): 216.12
  Company: RetailHub
  Market Cap: Small Cap
  Quarter: Q2
  Sector: Automotive
- Annual Revenue (B): 335.68
  Company: TechCorp
  Market Cap: Mid Cap
  Quarter: Q4
  Sector: Retail
- Annual Revenue (B): 304.76
  Company: AutoDrive
  Market Cap: Large Cap
  Quarter: Q4
  Sector: Retail
- Annual Revenue (B): 344.14
  Company: HealthPlus
  Market Cap: Small Cap
  Quarter: Q4
  Sector: Finance
- Annual Revenue (B): 428.53
  Company: RetailHub
  Market Cap: Mega Cap
  Quarter: Q3
  Sector: Finance
<end>Can you change this Csv into yml?
Title,Director,Genre,Release Year,Box Office Earnings (M)
Mystery of the Depths,Talon Blackthorn,Drama,2003,814.62
Escape from Earth,Talon Blackthorn,Drama,1973,943.82
Escape from Earth,Cade Firebrand,Thriller,1999,130.77
The Final Voyage,Zara Stormrider,Horror,1986,848.04
Beyond the Veil,Selene Darkwhisper,Horror,1971,555.52
The Endless Horizon,Lira Silverleaf,Sci-Fi,1993,410.32
The Endless Horizon,Talon Blackthorn,Sci-Fi,1975,807.39
<start>
- Box Office Earnings (M): 814.62
  Director: Talon Blackthorn
  Genre: Drama
  Release Year: 2003
  Title: Mystery of the Depths
- Box Office Earnings (M): 943.82
  Director: Talon Blackthorn
  Genre: Drama
  Release Year: 1973
  Title: Escape from Earth
- Box Office Earnings (M): 130.77
  Director: Cade Firebrand
  Genre: Thriller
  Release Year: 1999
  Title: Escape from Earth
- Box Office Earnings (M): 848.04
  Director: Zara Stormrider
  Genre: Horror
  Release Year: 1986
  Title: The Final Voyage
- Box Office Earnings (M): 555.52
  Director: Selene Darkwhisper
  Genre: Horror
  Release Year: 1971
  Title: Beyond the Veil
- Box Office Earnings (M): 410.32
  Director: Lira Silverleaf
  Genre: Sci-Fi
  Release Year: 1993
  Title: The Endless Horizon
- Box Office Earnings (M): 807.39
  Director: Talon Blackthorn
  Genre: Sci-Fi
  Release Year: 1975
  Title: The Endless Horizon
<end>Here's some CSV data, can you convert it to yaml?
Device Type,Location,Battery Level (%),Reading Value
Humidity Sensor,Hallway,24.9,15.53
Humidity Sensor,Bedroom,74.1,74.28
Motion Detector,Bedroom,92.1,28.9
<start>
- Battery Level (%): 24.9
  Device Type: Humidity Sensor
  Location: Hallway
  Reading Value: 15.53
- Battery Level (%): 74.1
  Device Type: Humidity Sensor
  Location: Bedroom
  Reading Value: 74.28
- Battery Level (%): 92.1
  Device Type: Motion Detector
  Location: Bedroom
  Reading Value: 28.9
<end>Can you change this MARKDOWN into Csv?
| Name | Age | Birth Month | City | Income |
| --- | --- | --- | --- | --- |
| Isla | 39 | September | Denver | 110000 |
| Lucille | 43 | September | Las Vegas | 455000 |
| Gregory | 59 | May | Fort Worth | 330000 |
| Terry | 24 | October | San Antonio | 450000 |
| Ashlyn | 23 | October | Los Angeles | 255000 |<start>
Name,Age,Birth Month,City,Income
Isla,39,September,Denver,110000
Lucille,43,September,Las Vegas,455000
Gregory,59,May,Fort Worth,330000
Terry,24,October,San Antonio,450000
Ashlyn,23,October,Los Angeles,255000
<end>Can you change this YML into Markdown?
- Close Price: 564.47
  Company: AeroSystems
  Date: '2021-02-20'
  High Price: 1000.7
  Low Price: 564.47
  Open Price: 1000.7
  Volume: 7015830
- Close Price: 589.04
  Company: TechnoCorp
  Date: '2015-11-14'
  High Price: 1456.55
  Low Price: 589.04
  Open Price: 1456.55
  Volume: 6885693
- Close Price: 1485.56
  Company: HealthGen
  Date: '2018-02-26'
  High Price: 1485.56
  Low Price: 185.59
  Open Price: 185.59
  Volume: 3664786
- Close Price: 1081.63
  Company: BioLife
  Date: '2011-06-27'
  High Price: 1081.63
  Low Price: 70.97
  Open Price: 616.68
  Volume: 2529052
<start>
| Company | Date | Open Price | Close Price | High Price | Low Price | Volume |
| --- | --- | --- | --- | --- | --- | --- |
| AeroSystems | 2021-02-20 | 1000.7 | 564.47 | 1000.7 | 564.47 | 7015830 |
| TechnoCorp | 2015-11-14 | 1456.55 | 589.04 | 1456.55 | 589.04 | 6885693 |
| HealthGen | 2018-02-26 | 185.59 | 1485.56 | 1485.56 | 185.59 | 3664786 |
| BioLife | 2011-06-27 | 616.68 | 1081.63 | 1081.63 | 70.97 | 2529052 |
<end>Convert this csv to Plain text:
Title,Director,Genre,Release Year,Box Office Earnings (M)
Rise of the Titans,Rylan Frostblade,Drama,1982,68.06
Mystery of the Depths,Drake Nightshade,Thriller,2015,676.2
Dreamwalker,Cade Firebrand,Adventure,2014,189.13
Mystery of the Depths,Drake Nightshade,Action,1983,356.74
Dreamwalker,Zara Stormrider,Adventure,1991,828.11
Beyond the Veil,Drake Nightshade,Drama,2008,68.06
Rise of the Titans,Rylan Frostblade,Action,1989,118.25
Beyond the Veil,Mara Moonshadow,Horror,1998,173.83
<start>
Title: Rise of the Titans | Director: Rylan Frostblade | Genre: Drama | Release Year: 1982 | Box Office Earnings (M): 68.06
Title: Mystery of the Depths | Director: Drake Nightshade | Genre: Thriller | Release Year: 2015 | Box Office Earnings (M): 676.2
Title: Dreamwalker | Director: Cade Firebrand | Genre: Adventure | Release Year: 2014 | Box Office Earnings (M): 189.13
Title: Mystery of the Depths | Director: Drake Nightshade | Genre: Action | Release Year: 1983 | Box Office Earnings (M): 356.74
Title: Dreamwalker | Director: Zara Stormrider | Genre: Adventure | Release Year: 1991 | Box Office Earnings (M): 828.11
Title: Beyond the Veil | Director: Drake Nightshade | Genre: Drama | Release Year: 2008 | Box Office Earnings (M): 68.06
Title: Rise of the Titans | Director: Rylan Frostblade | Genre: Action | Release Year: 1989 | Box Office Earnings (M): 118.25
Title: Beyond the Veil | Director: Mara Moonshadow | Genre: Horror | Release Year: 1998 | Box Office Earnings (M): 173.83
<end>Transform this PLAIN TEXT structure to a Markdown format:
Title: Edge of Infinity | Director: Selene Darkwhisper | Genre: Action
Title: The Endless Horizon | Director: Rylan Frostblade | Genre: Action
Title: Beyond the Veil | Director: Mara Moonshadow | Genre: Horror
Title: Dreamwalker | Director: Aria Ravenwood | Genre: Thriller
Title: The Final Voyage | Director: Mara Moonshadow | Genre: Fantasy
Title: Mystery of the Depths | Director: Selene Darkwhisper | Genre: Comedy
Title: Escape from Earth | Director: Mara Moonshadow | Genre: Adventure
Title: Beyond the Veil | Director: Zara Stormrider | Genre: Drama
Title: Starbound Odyssey | Director: Talon Blackthorn | Genre: Fantasy
<start>
| Title | Director | Genre |
| --- | --- | --- |
| Edge of Infinity | Selene Darkwhisper | Action |
| The Endless Horizon | Rylan Frostblade | Action |
| Beyond the Veil | Mara Moonshadow | Horror |
| Dreamwalker | Aria Ravenwood | Thriller |
| The Final Voyage | Mara Moonshadow | Fantasy |
| Mystery of the Depths | Selene Darkwhisper | Comedy |
| Escape from Earth | Mara Moonshadow | Adventure |
| Beyond the Veil | Zara Stormrider | Drama |
| Starbound Odyssey | Talon Blackthorn | Fantasy |
<end>Please transform the following YML data into Plain text:
- Average Latency (ms): 99.63
  Cache Hit Ratio (%): 85.6
  Connection Count: 210
  Database Name: MetricsDB
  Queries per Second: 1741.69
  Timestamp: '2022-03-10 09:19:08'
- Average Latency (ms): 25.57
  Cache Hit Ratio (%): 85.66
  Connection Count: 201
  Database Name: MetricsDB
  Queries per Second: 3628.94
  Timestamp: '2023-11-15 14:52:08'
- Average Latency (ms): 78.63
  Cache Hit Ratio (%): 85.66
  Connection Count: 215
  Database Name: ProductsDB
  Queries per Second: 4564.66
  Timestamp: '2021-02-03 20:18:55'
- Average Latency (ms): 33.76
  Cache Hit Ratio (%): 92.47
  Connection Count: 31
  Database Name: ProfilesDB
  Queries per Second: 2603.21
  Timestamp: '2023-09-21 13:03:34'
- Average Latency (ms): 42.82
  Cache Hit Ratio (%): 70.27
  Connection Count: 178
  Database Name: LogsDB
  Queries per Second: 4624.42
  Timestamp: '2022-03-21 03:57:57'
- Average Latency (ms): 92.51
  Cache Hit Ratio (%): 73.19
  Connection Count: 159
  Database Name: MetricsDB
  Queries per Second: 4178.35
  Timestamp: '2023-04-12 06:51:41'
- Average Latency (ms): 9.11
  Cache Hit Ratio (%): 72.34
  Connection Count: 279
  Database Name: LogsDB
  Queries per Second: 3001.0
  Timestamp: '2023-07-26 05:34:01'
- Average Latency (ms): 43.66
  Cache Hit Ratio (%): 73.19
  Connection Count: 451
  Database Name: SessionsDB
  Queries per Second: 1907.05
  Timestamp: '2023-02-03 06:35:55'
<start>
Database Name: MetricsDB | Queries per Second: 1741.69 | Cache Hit Ratio (%): 85.6 | Connection Count: 210 | Average Latency (ms): 99.63 | Timestamp: 2022-03-10 09:19:08
Database Name: MetricsDB | Queries per Second: 3628.94 | Cache Hit Ratio (%): 85.66 | Connection Count: 201 | Average Latency (ms): 25.57 | Timestamp: 2023-11-15 14:52:08
Database Name: ProductsDB | Queries per Second: 4564.66 | Cache Hit Ratio (%): 85.66 | Connection Count: 215 | Average Latency (ms): 78.63 | Timestamp: 2021-02-03 20:18:55
Database Name: ProfilesDB | Queries per Second: 2603.21 | Cache Hit Ratio (%): 92.47 | Connection Count: 31 | Average Latency (ms): 33.76 | Timestamp: 2023-09-21 13:03:34
Database Name: LogsDB | Queries per Second: 4624.42 | Cache Hit Ratio (%): 70.27 | Connection Count: 178 | Average Latency (ms): 42.82 | Timestamp: 2022-03-21 03:57:57
Database Name: MetricsDB | Queries per Second: 4178.35 | Cache Hit Ratio (%): 73.19 | Connection Count: 159 | Average Latency (ms): 92.51 | Timestamp: 2023-04-12 06:51:41
Database Name: LogsDB | Queries per Second: 3001.0 | Cache Hit Ratio (%): 72.34 | Connection Count: 279 | Average Latency (ms): 9.11 | Timestamp: 2023-07-26 05:34:01
Database Name: SessionsDB | Queries per Second: 1907.05 | Cache Hit Ratio (%): 73.19 | Connection Count: 451 | Average Latency (ms): 43.66 | Timestamp: 2023-02-03 06:35:55
<end>Here's some yaml data, can you convert it to CSV?
- Age: 57
  City: Milwaukee
  Name: Miguel
- Age: 18
  City: Memphis
  Name: Ted
- Age: 59
  City: Portland
  Name: Jackie
- Age: 69
  City: El Paso
  Name: Carrie
- Age: 68
  City: Las Vegas
  Name: Dalton
- Age: 54
  City: Oklahoma City
  Name: Etta
- Age: 65
  City: New York
  Name: Debra
- Age: 66
  City: Oklahoma City
  Name: Bryson
<start>
Name,Age,City
Miguel,57,Milwaukee
Ted,18,Memphis
Jackie,59,Portland
Carrie,69,El Paso
Dalton,68,Las Vegas
Etta,54,Oklahoma City
Debra,65,New York
Bryson,66,Oklahoma City
<end>Here's some yml data, can you convert it to PLAIN TEXT?
- Box Office Earnings (M): 22.51
  Director: Zara Stormrider
  Release Year: 1988
  Title: Mystery of the Depths
- Box Office Earnings (M): 472.22
  Director: Rylan Frostblade
  Release Year: 2010
  Title: Rise of the Titans
- Box Office Earnings (M): 653.97
  Director: Selene Darkwhisper
  Release Year: 1986
  Title: Beyond the Veil
- Box Office Earnings (M): 568.57
  Director: Orin Shadowalker
  Release Year: 1991
  Title: Beyond the Veil
- Box Office Earnings (M): 653.97
  Director: Rylan Frostblade
  Release Year: 1986
  Title: Starbound Odyssey
- Box Office Earnings (M): 907.95
  Director: Mara Moonshadow
  Release Year: 2023
  Title: Mystery of the Depths
- Box Office Earnings (M): 157.48
  Director: Talon Blackthorn
  Release Year: 1994
  Title: Dreamwalker
- Box Office Earnings (M): 804.68
  Director: Zara Stormrider
  Release Year: 1993
  Title: The Great Expedition
<start>
Title: Mystery of the Depths | Director: Zara Stormrider | Release Year: 1988 | Box Office Earnings (M): 22.51
Title: Rise of the Titans | Director: Rylan Frostblade | Release Year: 2010 | Box Office Earnings (M): 472.22
Title: Beyond the Veil | Director: Selene Darkwhisper | Release Year: 1986 | Box Office Earnings (M): 653.97
Title: Beyond the Veil | Director: Orin Shadowalker | Release Year: 1991 | Box Office Earnings (M): 568.57
Title: Starbound Odyssey | Director: Rylan Frostblade | Release Year: 1986 | Box Office Earnings (M): 653.97
Title: Mystery of the Depths | Director: Mara Moonshadow | Release Year: 2023 | Box Office Earnings (M): 907.95
Title: Dreamwalker | Director: Talon Blackthorn | Release Year: 1994 | Box Office Earnings (M): 157.48
Title: The Great Expedition | Director: Zara Stormrider | Release Year: 1993 | Box Office Earnings (M): 804.68
<end>Transform this json structure to a plain text format:
[
    {
        "Product Name": "Thingamajig",
        "SKU": "SKU-1030",
        "Price": 158.24,
        "Stock Quantity": 128,
        "Category": "Toys",
        "Supplier Name": "Wayne Enterprises"
    },
    {
        "Product Name": "Widget",
        "SKU": "SKU-1032",
        "Price": 362.91,
        "Stock Quantity": 378,
        "Category": "Household",
        "Supplier Name": "Globex"
    },
    {
        "Product Name": "Doohickey",
        "SKU": "SKU-1011",
        "Price": 108.98,
        "Stock Quantity": 220,
        "Category": "Household",
        "Supplier Name": "Wonka Industries"
    },
    {
        "Product Name": "Gadget",
        "SKU": "SKU-1084",
        "Price": 160.68,
        "Stock Quantity": 107,
        "Category": "Toys",
        "Supplier Name": "Wayne Enterprises"
    },
    {
        "Product Name": "Instrument",
        "SKU": "SKU-1080",
        "Price": 268.33,
        "Stock Quantity": 434,
        "Category": "Toys",
        "Supplier Name": "Wonka Industries"
    }
]<start>
Product Name: Thingamajig | SKU: SKU-1030 | Price: 158.24 | Stock Quantity: 128 | Category: Toys | Supplier Name: Wayne Enterprises
Product Name: Widget | SKU: SKU-1032 | Price: 362.91 | Stock Quantity: 378 | Category: Household | Supplier Name: Globex
Product Name: Doohickey | SKU: SKU-1011 | Price: 108.98 | Stock Quantity: 220 | Category: Household | Supplier Name: Wonka Industries
Product Name: Gadget | SKU: SKU-1084 | Price: 160.68 | Stock Quantity: 107 | Category: Toys | Supplier Name: Wayne Enterprises
Product Name: Instrument | SKU: SKU-1080 | Price: 268.33 | Stock Quantity: 434 | Category: Toys | Supplier Name: Wonka Industries
<end>Convert this PLAIN TEXT to markdown:
Director: Selene Darkwhisper | Genre: Sci-Fi | Release Year: 2003 | Box Office Earnings (M): 807.08
Director: Aria Ravenwood | Genre: Drama | Release Year: 1991 | Box Office Earnings (M): 638.45
Director: Lira Silverleaf | Genre: Comedy | Release Year: 1984 | Box Office Earnings (M): 952.57
<start>
| Director | Genre | Release Year | Box Office Earnings (M) |
| --- | --- | --- | --- |
| Selene Darkwhisper | Sci-Fi | 2003 | 807.08 |
| Aria Ravenwood | Drama | 1991 | 638.45 |
| Lira Silverleaf | Comedy | 1984 | 952.57 |
<end>Transform this YAML structure to a csv format:
- Annual Revenue (B): 182.72
  Company: AeroSpace
  Market Cap: Mega Cap
  Quarter: Q3
  Sector: Energy
  Stock Price: 303.15
- Annual Revenue (B): 357.97
  Company: Foodies
  Market Cap: Mega Cap
  Quarter: Q2
  Sector: Retail
  Stock Price: 984.45
- Annual Revenue (B): 202.4
  Company: BioPharm
  Market Cap: Mid Cap
  Quarter: Q4
  Sector: Finance
  Stock Price: 145.88
- Annual Revenue (B): 222.6
  Company: AeroSpace
  Market Cap: Mega Cap
  Quarter: Q1
  Sector: Automotive
  Stock Price: 382.4
- Annual Revenue (B): 356.38
  Company: AutoDrive
  Market Cap: Large Cap
  Quarter: Q4
  Sector: Technology
  Stock Price: 224.59
- Annual Revenue (B): 225.63
  Company: TechCorp
  Market Cap: Mega Cap
  Quarter: Q1
  Sector: Retail
  Stock Price: 311.56
- Annual Revenue (B): 183.49
  Company: FinanceWorks
  Market Cap: Mega Cap
  Quarter: Q2
  Sector: Automotive
  Stock Price: 809.74
- Annual Revenue (B): 80.94
  Company: RetailHub
  Market Cap: Mid Cap
  Quarter: Q3
  Sector: Retail
  Stock Price: 224.59
<start>
Company,Sector,Market Cap,Stock Price,Annual Revenue (B),Quarter
AeroSpace,Energy,Mega Cap,303.15,182.72,Q3
Foodies,Retail,Mega Cap,984.45,357.97,Q2
BioPharm,Finance,Mid Cap,145.88,202.4,Q4
AeroSpace,Automotive,Mega Cap,382.4,222.6,Q1
AutoDrive,Technology,Large Cap,224.59,356.38,Q4
TechCorp,Retail,Mega Cap,311.56,225.63,Q1
FinanceWorks,Automotive,Mega Cap,809.74,183.49,Q2
RetailHub,Retail,Mid Cap,224.59,80.94,Q3
<end>Here's some markdown data, can you convert it to Csv?
| Company | Sector | Market Cap | Annual Revenue (B) |
| --- | --- | --- | --- |
| EcoEnergy | Aerospace | Mid Cap | 474.51 |
| HealthPlus | Technology | Large Cap | 67.58 |
| EcoEnergy | Finance | Mega Cap | 80.8 |
| RetailHub | Finance | Large Cap | 354.69 |
| BioPharm | Retail | Mega Cap | 318.24 |
| AutoDrive | Automotive | Large Cap | 326.63 |
| RetailHub | Retail | Large Cap | 144.19 |
| AutoDrive | Technology | Small Cap | 474.51 |
| GlobalTrade | Healthcare | Mid Cap | 65.17 |<start>
Company,Sector,Market Cap,Annual Revenue (B)
EcoEnergy,Aerospace,Mid Cap,474.51
HealthPlus,Technology,Large Cap,67.58
EcoEnergy,Finance,Mega Cap,80.8
RetailHub,Finance,Large Cap,354.69
BioPharm,Retail,Mega Cap,318.24
AutoDrive,Automotive,Large Cap,326.63
RetailHub,Retail,Large Cap,144.19
AutoDrive,Technology,Small Cap,474.51
GlobalTrade,Healthcare,Mid Cap,65.17
<end>Convert this json to Yaml:
[
    {
        "Trip Name": "Lakeside Retreat",
        "Start Location": "Phoenix",
        "End Location": "Chicago",
        "Distance (miles)": 885.2,
        "Duration (hours)": 36.2,
        "Fuel Used (gallons)": 21.6
    },
    {
        "Trip Name": "Coast to Coast",
        "Start Location": "Los Angeles",
        "End Location": "Denver",
        "Distance (miles)": 861.8,
        "Duration (hours)": 3.8,
        "Fuel Used (gallons)": 27.0
    },
    {
        "Trip Name": "Historic Route",
        "Start Location": "Los Angeles",
        "End Location": "New York",
        "Distance (miles)": 1472.2,
        "Duration (hours)": 35.0,
        "Fuel Used (gallons)": 58.0
    }
]<start>
- Distance (miles): 885.2
  Duration (hours): 36.2
  End Location: Chicago
  Fuel Used (gallons): 21.6
  Start Location: Phoenix
  Trip Name: Lakeside Retreat
- Distance (miles): 861.8
  Duration (hours): 3.8
  End Location: Denver
  Fuel Used (gallons): 27.0
  Start Location: Los Angeles
  Trip Name: Coast to Coast
- Distance (miles): 1472.2
  Duration (hours): 35.0
  End Location: New York
  Fuel Used (gallons): 58.0
  Start Location: Los Angeles
  Trip Name: Historic Route
<end>Please transform the following json data into Plain text:
[
    {
        "SKU": "SKU-1023",
        "Stock Quantity": 92,
        "Supplier Name": "Globex"
    },
    {
        "SKU": "SKU-1084",
        "Stock Quantity": 306,
        "Supplier Name": "Globex"
    },
    {
        "SKU": "SKU-1052",
        "Stock Quantity": 342,
        "Supplier Name": "Umbrella Corp"
    },
    {
        "SKU": "SKU-1092",
        "Stock Quantity": 142,
        "Supplier Name": "Globex"
    },
    {
        "SKU": "SKU-1036",
        "Stock Quantity": 39,
        "Supplier Name": "Umbrella Corp"
    },
    {
        "SKU": "SKU-1051",
        "Stock Quantity": 349,
        "Supplier Name": "ACME Corp"
    },
    {
        "SKU": "SKU-1057",
        "Stock Quantity": 269,
        "Supplier Name": "Umbrella Corp"
    }
]<start>
SKU: SKU-1023 | Stock Quantity: 92 | Supplier Name: Globex
SKU: SKU-1084 | Stock Quantity: 306 | Supplier Name: Globex
SKU: SKU-1052 | Stock Quantity: 342 | Supplier Name: Umbrella Corp
SKU: SKU-1092 | Stock Quantity: 142 | Supplier Name: Globex
SKU: SKU-1036 | Stock Quantity: 39 | Supplier Name: Umbrella Corp
SKU: SKU-1051 | Stock Quantity: 349 | Supplier Name: ACME Corp
SKU: SKU-1057 | Stock Quantity: 269 | Supplier Name: Umbrella Corp
<end>Convert this plain text to JSON:
Director: Zara Stormrider | Genre: Adventure | Release Year: 1987 | Box Office Earnings (M): 887.62
Director: Orin Shadowalker | Genre: Sci-Fi | Release Year: 1991 | Box Office Earnings (M): 721.53
Director: Lira Silverleaf | Genre: Comedy | Release Year: 2013 | Box Office Earnings (M): 127.62
Director: Drake Nightshade | Genre: Horror | Release Year: 1988 | Box Office Earnings (M): 563.06
Director: Talon Blackthorn | Genre: Action | Release Year: 1975 | Box Office Earnings (M): 586.93
Director: Talon Blackthorn | Genre: Adventure | Release Year: 1972 | Box Office Earnings (M): 200.28
<start>
[
    {
        "Director": "Zara Stormrider",
        "Genre": "Adventure",
        "Release Year": 1987,
        "Box Office Earnings (M)": 887.62
    },
    {
        "Director": "Orin Shadowalker",
        "Genre": "Sci-Fi",
        "Release Year": 1991,
        "Box Office Earnings (M)": 721.53
    },
    {
        "Director": "Lira Silverleaf",
        "Genre": "Comedy",
        "Release Year": 2013,
        "Box Office Earnings (M)": 127.62
    },
    {
        "Director": "Drake Nightshade",
        "Genre": "Horror",
        "Release Year": 1988,
        "Box Office Earnings (M)": 563.06
    },
    {
        "Director": "Talon Blackthorn",
        "Genre": "Action",
        "Release Year": 1975,
        "Box Office Earnings (M)": 586.93
    },
    {
        "Director": "Talon Blackthorn",
        "Genre": "Adventure",
        "Release Year": 1972,
        "Box Office Earnings (M)": 200.28
    }
]
<end>Transform this markdown structure to a Csv format:
| Trip Name | Start Location | End Location | Distance (miles) | Duration (hours) | Fuel Used (gallons) |
| --- | --- | --- | --- | --- | --- |
| Historic Route | Phoenix | New York | 1398.6 | 5.0 | 14.9 |
| Canyon Trek | Houston | Chicago | 2491.2 | 1.3 | 13.0 |
| Canyon Trek | Denver | Phoenix | 1261.4 | 52.3 | 38.6 |
| Canyon Trek | Los Angeles | Houston | 2653.4 | 1.3 | 39.4 |
| City Explorer | Houston | Chicago | 1483.1 | 30.3 | 51.5 |
| Canyon Trek | Houston | Los Angeles | 1652.0 | 67.5 | 8.1 |
| Desert Drive | Phoenix | Los Angeles | 1882.7 | 64.9 | 33.7 |
| Desert Drive | Los Angeles | San Francisco | 2427.1 | 67.4 | 96.2 |<start>
Trip Name,Start Location,End Location,Distance (miles),Duration (hours),Fuel Used (gallons)
Historic Route,Phoenix,New York,1398.6,5.0,14.9
Canyon Trek,Houston,Chicago,2491.2,1.3,13.0
Canyon Trek,Denver,Phoenix,1261.4,52.3,38.6
Canyon Trek,Los Angeles,Houston,2653.4,1.3,39.4
City Explorer,Houston,Chicago,1483.1,30.3,51.5
Canyon Trek,Houston,Los Angeles,1652.0,67.5,8.1
Desert Drive,Phoenix,Los Angeles,1882.7,64.9,33.7
Desert Drive,Los Angeles,San Francisco,2427.1,67.4,96.2
<end>Convert this JSON to Csv:
[
    {
        "Product Name": "Doohickey",
        "SKU": "SKU-1056",
        "Stock Quantity": 438,
        "Category": "Electronics",
        "Supplier Name": "Wonka Industries"
    },
    {
        "Product Name": "Whatchamacallit",
        "SKU": "SKU-1052",
        "Stock Quantity": 491,
        "Category": "Electronics",
        "Supplier Name": "ACME Corp"
    },
    {
        "Product Name": "Instrument",
        "SKU": "SKU-1032",
        "Stock Quantity": 197,
        "Category": "Toys",
        "Supplier Name": "Wonka Industries"
    },
    {
        "Product Name": "Doohickey",
        "SKU": "SKU-1026",
        "Stock Quantity": 89,
        "Category": "Sports",
        "Supplier Name": "ACME Corp"
    },
    {
        "Product Name": "Contraption",
        "SKU": "SKU-1003",
        "Stock Quantity": 186,
        "Category": "Automotive",
        "Supplier Name": "ACME Corp"
    }
]<start>
Product Name,SKU,Stock Quantity,Category,Supplier Name
Doohickey,SKU-1056,438,Electronics,Wonka Industries
Whatchamacallit,SKU-1052,491,Electronics,ACME Corp
Instrument,SKU-1032,197,Toys,Wonka Industries
Doohickey,SKU-1026,89,Sports,ACME Corp
Contraption,SKU-1003,186,Automotive,ACME Corp
<end>Here's some Json data, can you convert it to CSV?
[
    {
        "Title": "The Last Sky",
        "Author": "Kara Firebrand",
        "Genre": "Non-Fiction",
        "Rating": 1.3
    },
    {
        "Title": "A Journey Through Time",
        "Author": "Draven Blackthorn",
        "Genre": "Horror",
        "Rating": 1.8
    },
    {
        "Title": "Shadows of Solitude",
        "Author": "Orion Frostblade",
        "Genre": "Science Fiction",
        "Rating": 2.4
    },
    {
        "Title": "The Crystal Key",
        "Author": "Galen Starfire",
        "Genre": "Fantasy",
        "Rating": 3.5
    },
    {
        "Title": "The Last Sky",
        "Author": "Thorne Ironwood",
        "Genre": "Historical",
        "Rating": 1.5
    },
    {
        "Title": "The Last Sky",
        "Author": "Kara Firebrand",
        "Genre": "Romance",
        "Rating": 4.0
    },
    {
        "Title": "The Crystal Key",
        "Author": "Rowan Ashborne",
        "Genre": "Thriller",
        "Rating": 4.3
    }
]<start>
Title,Author,Genre,Rating
The Last Sky,Kara Firebrand,Non-Fiction,1.3
A Journey Through Time,Draven Blackthorn,Horror,1.8
Shadows of Solitude,Orion Frostblade,Science Fiction,2.4
The Crystal Key,Galen Starfire,Fantasy,3.5
The Last Sky,Thorne Ironwood,Historical,1.5
The Last Sky,Kara Firebrand,Romance,4.0
The Crystal Key,Rowan Ashborne,Thriller,4.3
<end>Here's some CSV data, can you convert it to markdown?
Product Name,SKU,Price,Stock Quantity,Category,Supplier Name
Whatchamacallit,SKU-1076,339.61,467,Household,Wayne Enterprises
Contraption,SKU-1066,348.84,6,Toys,Globex
Thingamajig,SKU-1040,348.37,335,Household,ACME Corp
Whatchamacallit,SKU-1039,135.94,481,Electronics,Wonka Industries
<start>
| Product Name | SKU | Price | Stock Quantity | Category | Supplier Name |
| --- | --- | --- | --- | --- | --- |
| Whatchamacallit | SKU-1076 | 339.61 | 467 | Household | Wayne Enterprises |
| Contraption | SKU-1066 | 348.84 | 6 | Toys | Globex |
| Thingamajig | SKU-1040 | 348.37 | 335 | Household | ACME Corp |
| Whatchamacallit | SKU-1039 | 135.94 | 481 | Electronics | Wonka Industries |
<end>Here's some CSV data, can you convert it to PLAIN TEXT?
Date,Open Price,Close Price,Low Price
2011-03-01,497.89,330.77,330.77
2017-08-17,991.09,497.89,212.0
2022-09-06,1063.67,1105.68,535.48
2011-12-11,1063.67,875.27,637.34
2011-06-15,898.34,53.01,53.01
2019-09-28,313.43,275.91,275.91
<start>
Date: 2011-03-01 | Open Price: 497.89 | Close Price: 330.77 | Low Price: 330.77
Date: 2017-08-17 | Open Price: 991.09 | Close Price: 497.89 | Low Price: 212.0
Date: 2022-09-06 | Open Price: 1063.67 | Close Price: 1105.68 | Low Price: 535.48
Date: 2011-12-11 | Open Price: 1063.67 | Close Price: 875.27 | Low Price: 637.34
Date: 2011-06-15 | Open Price: 898.34 | Close Price: 53.01 | Low Price: 53.01
Date: 2019-09-28 | Open Price: 313.43 | Close Price: 275.91 | Low Price: 275.91
<end>Please transform the following YML data into csv:
- Condition: Stormy
  Day: Wednesday
  Humidity (%): 33
  Temperature (C): -9.7
  Wind Speed (km/h): 0.3
- Condition: Sunny
  Day: Monday
  Humidity (%): 38
  Temperature (C): 7.5
  Wind Speed (km/h): 27.2
- Condition: Rainy
  Day: Tuesday
  Humidity (%): 35
  Temperature (C): 13.9
  Wind Speed (km/h): 10.4
- Condition: Windy
  Day: Sunday
  Humidity (%): 56
  Temperature (C): 12.0
  Wind Speed (km/h): 4.0
- Condition: Sunny
  Day: Sunday
  Humidity (%): 30
  Temperature (C): 3.6
  Wind Speed (km/h): 10.3
- Condition: Sunny
  Day: Tuesday
  Humidity (%): 50
  Temperature (C): 36.8
  Wind Speed (km/h): 16.1
- Condition: Windy
  Day: Thursday
  Humidity (%): 55
  Temperature (C): 31.8
  Wind Speed (km/h): 1.4
- Condition: Cloudy
  Day: Sunday
  Humidity (%): 66
  Temperature (C): 19.5
  Wind Speed (km/h): 27.2
- Condition: Snowy
  Day: Sunday
  Humidity (%): 72
  Temperature (C): 2.7
  Wind Speed (km/h): 1.0
<start>
Condition,Temperature (C),Humidity (%),Wind Speed (km/h),Day
Stormy,-9.7,33,0.3,Wednesday
Sunny,7.5,38,27.2,Monday
Rainy,13.9,35,10.4,Tuesday
Windy,12.0,56,4.0,Sunday
Sunny,3.6,30,10.3,Sunday
Sunny,36.8,50,16.1,Tuesday
Windy,31.8,55,1.4,Thursday
Cloudy,19.5,66,27.2,Sunday
Snowy,2.7,72,1.0,Sunday
<end>Please transform the following json data into Plain text:
[
    {
        "Company": "GlobalTrade",
        "Sector": "Biotech",
        "Market Cap": "Mid Cap",
        "Stock Price": 70.8,
        "Annual Revenue (B)": 300.25,
        "Quarter": "Q1"
    },
    {
        "Company": "TechCorp",
        "Sector": "Energy",
        "Market Cap": "Mega Cap",
        "Stock Price": 527.19,
        "Annual Revenue (B)": 419.54,
        "Quarter": "Q4"
    },
    {
        "Company": "TechCorp",
        "Sector": "Healthcare",
        "Market Cap": "Large Cap",
        "Stock Price": 593.1,
        "Annual Revenue (B)": 324.01,
        "Quarter": "Q3"
    },
    {
        "Company": "EcoEnergy",
        "Sector": "Automotive",
        "Market Cap": "Large Cap",
        "Stock Price": 582.22,
        "Annual Revenue (B)": 148.7,
        "Quarter": "Q2"
    },
    {
        "Company": "AutoDrive",
        "Sector": "Technology",
        "Market Cap": "Mega Cap",
        "Stock Price": 672.45,
        "Annual Revenue (B)": 150.17,
        "Quarter": "Q2"
    }
]<start>
Company: GlobalTrade | Sector: Biotech | Market Cap: Mid Cap | Stock Price: 70.8 | Annual Revenue (B): 300.25 | Quarter: Q1
Company: TechCorp | Sector: Energy | Market Cap: Mega Cap | Stock Price: 527.19 | Annual Revenue (B): 419.54 | Quarter: Q4
Company: TechCorp | Sector: Healthcare | Market Cap: Large Cap | Stock Price: 593.1 | Annual Revenue (B): 324.01 | Quarter: Q3
Company: EcoEnergy | Sector: Automotive | Market Cap: Large Cap | Stock Price: 582.22 | Annual Revenue (B): 148.7 | Quarter: Q2
Company: AutoDrive | Sector: Technology | Market Cap: Mega Cap | Stock Price: 672.45 | Annual Revenue (B): 150.17 | Quarter: Q2
<end>Can you change this Json into markdown?
[
    {
        "Start Location": "New York",
        "End Location": "Houston",
        "Fuel Used (gallons)": 32.1
    },
    {
        "Start Location": "Los Angeles",
        "End Location": "Phoenix",
        "Fuel Used (gallons)": 8.9
    },
    {
        "Start Location": "Los Angeles",
        "End Location": "Phoenix",
        "Fuel Used (gallons)": 31.9
    },
    {
        "Start Location": "Miami",
        "End Location": "New York",
        "Fuel Used (gallons)": 92.4
    },
    {
        "Start Location": "New York",
        "End Location": "San Francisco",
        "Fuel Used (gallons)": 58.7
    },
    {
        "Start Location": "New York",
        "End Location": "Houston",
        "Fuel Used (gallons)": 37.6
    },
    {
        "Start Location": "Miami",
        "End Location": "New York",
        "Fuel Used (gallons)": 78.8
    },
    {
        "Start Location": "Chicago",
        "End Location": "San Francisco",
        "Fuel Used (gallons)": 95.4
    }
]<start>
| Start Location | End Location | Fuel Used (gallons) |
| --- | --- | --- |
| New York | Houston | 32.1 |
| Los Angeles | Phoenix | 8.9 |
| Los Angeles | Phoenix | 31.9 |
| Miami | New York | 92.4 |
| New York | San Francisco | 58.7 |
| New York | Houston | 37.6 |
| Miami | New York | 78.8 |
| Chicago | San Francisco | 95.4 |
<end>Here's some PLAIN TEXT data, can you convert it to YML?
Birth Month: July | City: Denver | Income: 40000
Birth Month: March | City: Portland | Income: 285000
Birth Month: January | City: Los Angeles | Income: 55000
Birth Month: April | City: Portland | Income: 60000
Birth Month: March | City: Nashville | Income: 105000
Birth Month: June | City: Phoenix | Income: 320000
Birth Month: November | City: Chicago | Income: 290000
Birth Month: September | City: Nashville | Income: 195000
Birth Month: April | City: El Paso | Income: 485000
Birth Month: November | City: Louisville | Income: 325000
<start>
- Birth Month: July
  City: Denver
  Income: 40000
- Birth Month: March
  City: Portland
  Income: 285000
- Birth Month: January
  City: Los Angeles
  Income: 55000
- Birth Month: April
  City: Portland
  Income: 60000
- Birth Month: March
  City: Nashville
  Income: 105000
- Birth Month: June
  City: Phoenix
  Income: 320000
- Birth Month: November
  City: Chicago
  Income: 290000
- Birth Month: September
  City: Nashville
  Income: 195000
- Birth Month: April
  City: El Paso
  Income: 485000
- Birth Month: November
  City: Louisville
  Income: 325000
<end>Here's some PLAIN TEXT data, can you convert it to yml?
Restaurant Name: Burger Haven | Cuisine: Chinese | Price Range: $$$$
Restaurant Name: Vegan Delight | Cuisine: Japanese | Price Range: $$$$
Restaurant Name: BBQ Barn | Cuisine: French | Price Range: $
<start>
- Cuisine: Chinese
  Price Range: $$$$
  Restaurant Name: Burger Haven
- Cuisine: Japanese
  Price Range: $$$$
  Restaurant Name: Vegan Delight
- Cuisine: French
  Price Range: $
  Restaurant Name: BBQ Barn
<end>Transform this csv structure to a json format:
Location,Temperature (C),Humidity (%),Day
New York,18.9,60,Sunday
Los Angeles,-6.5,100,Friday
Houston,-5.2,100,Friday
Seattle,4.7,66,Friday
Phoenix,1.0,84,Friday
New York,22.0,77,Tuesday
Miami,5.7,38,Saturday
Seattle,24.8,48,Tuesday
Seattle,7.5,72,Saturday
Chicago,5.4,81,Sunday
<start>
[
    {
        "Location": "New York",
        "Temperature (C)": 18.9,
        "Humidity (%)": 60,
        "Day": "Sunday"
    },
    {
        "Location": "Los Angeles",
        "Temperature (C)": -6.5,
        "Humidity (%)": 100,
        "Day": "Friday"
    },
    {
        "Location": "Houston",
        "Temperature (C)": -5.2,
        "Humidity (%)": 100,
        "Day": "Friday"
    },
    {
        "Location": "Seattle",
        "Temperature (C)": 4.7,
        "Humidity (%)": 66,
        "Day": "Friday"
    },
    {
        "Location": "Phoenix",
        "Temperature (C)": 1.0,
        "Humidity (%)": 84,
        "Day": "Friday"
    },
    {
        "Location": "New York",
        "Temperature (C)": 22.0,
        "Humidity (%)": 77,
        "Day": "Tuesday"
    },
    {
        "Location": "Miami",
        "Temperature (C)": 5.7,
        "Humidity (%)": 38,
        "Day": "Saturday"
    },
    {
        "Location": "Seattle",
        "Temperature (C)": 24.8,
        "Humidity (%)": 48,
        "Day": "Tuesday"
    },
    {
        "Location": "Seattle",
        "Temperature (C)": 7.5,
        "Humidity (%)": 72,
        "Day": "Saturday"
    },
    {
        "Location": "Chicago",
        "Temperature (C)": 5.4,
        "Humidity (%)": 81,
        "Day": "Sunday"
    }
]
<end>Transform this MARKDOWN structure to a Csv format:
| Location | Condition | Humidity (%) | Day |
| --- | --- | --- | --- |
| New York | Sunny | 79 | Tuesday |
| Los Angeles | Sunny | 30 | Friday |
| Phoenix | Foggy | 68 | Monday |
| Los Angeles | Windy | 59 | Saturday |
| Denver | Windy | 21 | Monday |
| Houston | Foggy | 64 | Tuesday |
| Phoenix | Sunny | 25 | Thursday |
| Seattle | Stormy | 41 | Wednesday |
| Miami | Rainy | 96 | Friday |<start>
Location,Condition,Humidity (%),Day
New York,Sunny,79,Tuesday
Los Angeles,Sunny,30,Friday
Phoenix,Foggy,68,Monday
Los Angeles,Windy,59,Saturday
Denver,Windy,21,Monday
Houston,Foggy,64,Tuesday
Phoenix,Sunny,25,Thursday
Seattle,Stormy,41,Wednesday
Miami,Rainy,96,Friday
<end>Convert this MARKDOWN to json:
| Product Name | SKU | Price | Stock Quantity | Supplier Name |
| --- | --- | --- | --- | --- |
| Whatchamacallit | SKU-1030 | 101.79 | 32 | Globex |
| Apparatus | SKU-1091 | 333.4 | 124 | ACME Corp |
| Whatchamacallit | SKU-1075 | 486.6 | 234 | ACME Corp |
| Contraption | SKU-1068 | 349.79 | 179 | Wonka Industries |
| Device | SKU-1036 | 193.33 | 241 | Umbrella Corp |
| Doohickey | SKU-1072 | 152.12 | 42 | Wonka Industries |
| Widget | SKU-1052 | 113.89 | 224 | ACME Corp |<start>
[
    {
        "Product Name": "Whatchamacallit",
        "SKU": "SKU-1030",
        "Price": 101.79,
        "Stock Quantity": 32,
        "Supplier Name": "Globex"
    },
    {
        "Product Name": "Apparatus",
        "SKU": "SKU-1091",
        "Price": 333.4,
        "Stock Quantity": 124,
        "Supplier Name": "ACME Corp"
    },
    {
        "Product Name": "Whatchamacallit",
        "SKU": "SKU-1075",
        "Price": 486.6,
        "Stock Quantity": 234,
        "Supplier Name": "ACME Corp"
    },
    {
        "Product Name": "Contraption",
        "SKU": "SKU-1068",
        "Price": 349.79,
        "Stock Quantity": 179,
        "Supplier Name": "Wonka Industries"
    },
    {
        "Product Name": "Device",
        "SKU": "SKU-1036",
        "Price": 193.33,
        "Stock Quantity": 241,
        "Supplier Name": "Umbrella Corp"
    },
    {
        "Product Name": "Doohickey",
        "SKU": "SKU-1072",
        "Price": 152.12,
        "Stock Quantity": 42,
        "Supplier Name": "Wonka Industries"
    },
    {
        "Product Name": "Widget",
        "SKU": "SKU-1052",
        "Price": 113.89,
        "Stock Quantity": 224,
        "Supplier Name": "ACME Corp"
    }
]
<end>Please transform the following Yaml data into json:
- Day: Monday
  Humidity (%): 98
  Location: Chicago
  Temperature (C): 36.7
- Day: Thursday
  Humidity (%): 34
  Location: Houston
  Temperature (C): 4.8
- Day: Wednesday
  Humidity (%): 97
  Location: Seattle
  Temperature (C): 27.8
- Day: Wednesday
  Humidity (%): 96
  Location: New York
  Temperature (C): 12.7
- Day: Sunday
  Humidity (%): 39
  Location: Chicago
  Temperature (C): 19.2
<start>
[
    {
        "Location": "Chicago",
        "Temperature (C)": 36.7,
        "Humidity (%)": 98,
        "Day": "Monday"
    },
    {
        "Location": "Houston",
        "Temperature (C)": 4.8,
        "Humidity (%)": 34,
        "Day": "Thursday"
    },
    {
        "Location": "Seattle",
        "Temperature (C)": 27.8,
        "Humidity (%)": 97,
        "Day": "Wednesday"
    },
    {
        "Location": "New York",
        "Temperature (C)": 12.7,
        "Humidity (%)": 96,
        "Day": "Wednesday"
    },
    {
        "Location": "Chicago",
        "Temperature (C)": 19.2,
        "Humidity (%)": 39,
        "Day": "Sunday"
    }
]
<end>Here's some yaml data, can you convert it to MARKDOWN?
- Box Office Earnings (M): 907.91
  Director: Orin Shadowalker
  Genre: Adventure
  Release Year: 1982
  Title: The Endless Horizon
- Box Office Earnings (M): 535.8
  Director: Talon Blackthorn
  Genre: Adventure
  Release Year: 2017
  Title: Starbound Odyssey
- Box Office Earnings (M): 161.6
  Director: Selene Darkwhisper
  Genre: Sci-Fi
  Release Year: 2012
  Title: Edge of Infinity
- Box Office Earnings (M): 366.55
  Director: Selene Darkwhisper
  Genre: Horror
  Release Year: 2002
  Title: The Endless Horizon
- Box Office Earnings (M): 87.82
  Director: Mara Moonshadow
  Genre: Fantasy
  Release Year: 1994
  Title: Beyond the Veil
- Box Office Earnings (M): 453.45
  Director: Rylan Frostblade
  Genre: Thriller
  Release Year: 2008
  Title: The Endless Horizon
- Box Office Earnings (M): 444.6
  Director: Mara Moonshadow
  Genre: Sci-Fi
  Release Year: 1974
  Title: The Great Expedition
- Box Office Earnings (M): 638.33
  Director: Orin Shadowalker
  Genre: Sci-Fi
  Release Year: 1995
  Title: Starbound Odyssey
<start>
| Title | Director | Genre | Release Year | Box Office Earnings (M) |
| --- | --- | --- | --- | --- |
| The Endless Horizon | Orin Shadowalker | Adventure | 1982 | 907.91 |
| Starbound Odyssey | Talon Blackthorn | Adventure | 2017 | 535.8 |
| Edge of Infinity | Selene Darkwhisper | Sci-Fi | 2012 | 161.6 |
| The Endless Horizon | Selene Darkwhisper | Horror | 2002 | 366.55 |
| Beyond the Veil | Mara Moonshadow | Fantasy | 1994 | 87.82 |
| The Endless Horizon | Rylan Frostblade | Thriller | 2008 | 453.45 |
| The Great Expedition | Mara Moonshadow | Sci-Fi | 1974 | 444.6 |
| Starbound Odyssey | Orin Shadowalker | Sci-Fi | 1995 | 638.33 |
<end>Convert this Json to Yaml:
[
    {
        "Restaurant Name": "Pasta Palace",
        "Location": "Phoenix"
    },
    {
        "Restaurant Name": "Pasta Palace",
        "Location": "Chicago"
    },
    {
        "Restaurant Name": "Curry Corner",
        "Location": "Los Angeles"
    },
    {
        "Restaurant Name": "Taco Town",
        "Location": "San Francisco"
    },
    {
        "Restaurant Name": "Pizza Planet",
        "Location": "New York"
    },
    {
        "Restaurant Name": "Taco Town",
        "Location": "Chicago"
    }
]<start>
- Location: Phoenix
  Restaurant Name: Pasta Palace
- Location: Chicago
  Restaurant Name: Pasta Palace
- Location: Los Angeles
  Restaurant Name: Curry Corner
- Location: San Francisco
  Restaurant Name: Taco Town
- Location: New York
  Restaurant Name: Pizza Planet
- Location: Chicago
  Restaurant Name: Taco Town
<end>Convert this yml to Plain text:
- Condition: Sunny
  Day: Monday
  Humidity (%): 62
  Location: Seattle
  Temperature (C): 15.2
  Wind Speed (km/h): 9.6
- Condition: Foggy
  Day: Saturday
  Humidity (%): 100
  Location: Seattle
  Temperature (C): -0.6
  Wind Speed (km/h): 27.3
- Condition: Stormy
  Day: Tuesday
  Humidity (%): 95
  Location: Seattle
  Temperature (C): 8.1
  Wind Speed (km/h): 9.6
- Condition: Rainy
  Day: Tuesday
  Humidity (%): 62
  Location: Seattle
  Temperature (C): 8.3
  Wind Speed (km/h): 23.2
- Condition: Sunny
  Day: Tuesday
  Humidity (%): 53
  Location: Denver
  Temperature (C): 28.5
  Wind Speed (km/h): 14.7
<start>
Location: Seattle | Condition: Sunny | Temperature (C): 15.2 | Humidity (%): 62 | Wind Speed (km/h): 9.6 | Day: Monday
Location: Seattle | Condition: Foggy | Temperature (C): -0.6 | Humidity (%): 100 | Wind Speed (km/h): 27.3 | Day: Saturday
Location: Seattle | Condition: Stormy | Temperature (C): 8.1 | Humidity (%): 95 | Wind Speed (km/h): 9.6 | Day: Tuesday
Location: Seattle | Condition: Rainy | Temperature (C): 8.3 | Humidity (%): 62 | Wind Speed (km/h): 23.2 | Day: Tuesday
Location: Denver | Condition: Sunny | Temperature (C): 28.5 | Humidity (%): 53 | Wind Speed (km/h): 14.7 | Day: Tuesday
<end>Convert this markdown to JSON:
| Title | Director | Release Year | Box Office Earnings (M) |
| --- | --- | --- | --- |
| Mystery of the Depths | Aria Ravenwood | 1996 | 794.38 |
| The Final Voyage | Aria Ravenwood | 1981 | 371.78 |
| The Endless Horizon | Orin Shadowalker | 1989 | 911.54 |
| Dreamwalker | Orin Shadowalker | 2013 | 248.92 |
| Beyond the Veil | Selene Darkwhisper | 2011 | 506.56 |
| The Great Expedition | Mara Moonshadow | 2021 | 851.08 |
| The Great Expedition | Mara Moonshadow | 1970 | 745.9 |
| Dreamwalker | Aria Ravenwood | 2014 | 715.3 |<start>
[
    {
        "Title": "Mystery of the Depths",
        "Director": "Aria Ravenwood",
        "Release Year": 1996,
        "Box Office Earnings (M)": 794.38
    },
    {
        "Title": "The Final Voyage",
        "Director": "Aria Ravenwood",
        "Release Year": 1981,
        "Box Office Earnings (M)": 371.78
    },
    {
        "Title": "The Endless Horizon",
        "Director": "Orin Shadowalker",
        "Release Year": 1989,
        "Box Office Earnings (M)": 911.54
    },
    {
        "Title": "Dreamwalker",
        "Director": "Orin Shadowalker",
        "Release Year": 2013,
        "Box Office Earnings (M)": 248.92
    },
    {
        "Title": "Beyond the Veil",
        "Director": "Selene Darkwhisper",
        "Release Year": 2011,
        "Box Office Earnings (M)": 506.56
    },
    {
        "Title": "The Great Expedition",
        "Director": "Mara Moonshadow",
        "Release Year": 2021,
        "Box Office Earnings (M)": 851.08
    },
    {
        "Title": "The Great Expedition",
        "Director": "Mara Moonshadow",
        "Release Year": 1970,
        "Box Office Earnings (M)": 745.9
    },
    {
        "Title": "Dreamwalker",
        "Director": "Aria Ravenwood",
        "Release Year": 2014,
        "Box Office Earnings (M)": 715.3
    }
]
<end>Convert this Plain text to CSV:
Director: Drake Nightshade | Box Office Earnings (M): 425.16
Director: Orin Shadowalker | Box Office Earnings (M): 291.57
Director: Rylan Frostblade | Box Office Earnings (M): 77.34
Director: Aria Ravenwood | Box Office Earnings (M): 521.6
Director: Aria Ravenwood | Box Office Earnings (M): 343.98
Director: Selene Darkwhisper | Box Office Earnings (M): 255.79
Director: Orin Shadowalker | Box Office Earnings (M): 187.48
Director: Aria Ravenwood | Box Office Earnings (M): 703.89
Director: Zara Stormrider | Box Office Earnings (M): 99.98
<start>
Director,Box Office Earnings (M)
Drake Nightshade,425.16
Orin Shadowalker,291.57
Rylan Frostblade,77.34
Aria Ravenwood,521.6
Aria Ravenwood,343.98
Selene Darkwhisper,255.79
Orin Shadowalker,187.48
Aria Ravenwood,703.89
Zara Stormrider,99.98
<end>Convert this YAML to plain text:
- Age: 53
  Birth Month: January
  City: Oklahoma City
  Name: Felix
- Age: 20
  Birth Month: December
  City: New York
  Name: Carmen
- Age: 63
  Birth Month: January
  City: Detroit
  Name: Ollie
<start>
Name: Felix | Age: 53 | Birth Month: January | City: Oklahoma City
Name: Carmen | Age: 20 | Birth Month: December | City: New York
Name: Ollie | Age: 63 | Birth Month: January | City: Detroit
<end>Can you change this Csv into Json?
Database Name,Queries per Second,Cache Hit Ratio (%),Connection Count,Average Latency (ms),Timestamp
AnalyticsDB,1245.6,86.5,499,2.84,2023-05-01 10:04:48
OrdersDB,3704.65,95.53,228,44.29,2021-12-22 20:44:56
SalesDB,2528.31,95.9,60,86.27,2022-08-06 02:06:36
UserDB,361.26,79.13,379,2.84,2022-10-12 15:03:54
SalesDB,2789.41,93.44,247,65.15,2023-07-17 17:37:33
InventoryDB,4388.4,94.77,297,77.15,2023-10-22 12:47:24
AnalyticsDB,845.16,86.5,319,35.7,2022-05-13 17:31:13
<start>
[
    {
        "Database Name": "AnalyticsDB",
        "Queries per Second": 1245.6,
        "Cache Hit Ratio (%)": 86.5,
        "Connection Count": 499,
        "Average Latency (ms)": 2.84,
        "Timestamp": "2023-05-01 10:04:48"
    },
    {
        "Database Name": "OrdersDB",
        "Queries per Second": 3704.65,
        "Cache Hit Ratio (%)": 95.53,
        "Connection Count": 228,
        "Average Latency (ms)": 44.29,
        "Timestamp": "2021-12-22 20:44:56"
    },
    {
        "Database Name": "SalesDB",
        "Queries per Second": 2528.31,
        "Cache Hit Ratio (%)": 95.9,
        "Connection Count": 60,
        "Average Latency (ms)": 86.27,
        "Timestamp": "2022-08-06 02:06:36"
    },
    {
        "Database Name": "UserDB",
        "Queries per Second": 361.26,
        "Cache Hit Ratio (%)": 79.13,
        "Connection Count": 379,
        "Average Latency (ms)": 2.84,
        "Timestamp": "2022-10-12 15:03:54"
    },
    {
        "Database Name": "SalesDB",
        "Queries per Second": 2789.41,
        "Cache Hit Ratio (%)": 93.44,
        "Connection Count": 247,
        "Average Latency (ms)": 65.15,
        "Timestamp": "2023-07-17 17:37:33"
    },
    {
        "Database Name": "InventoryDB",
        "Queries per Second": 4388.4,
        "Cache Hit Ratio (%)": 94.77,
        "Connection Count": 297,
        "Average Latency (ms)": 77.15,
        "Timestamp": "2023-10-22 12:47:24"
    },
    {
        "Database Name": "AnalyticsDB",
        "Queries per Second": 845.16,
        "Cache Hit Ratio (%)": 86.5,
        "Connection Count": 319,
        "Average Latency (ms)": 35.7,
        "Timestamp": "2022-05-13 17:31:13"
    }
]
<end>Here's some Csv data, can you convert it to yml?
Title,Director,Genre,Box Office Earnings (M)
Escape from Earth,Mara Moonshadow,Thriller,631.56
The Final Voyage,Drake Nightshade,Fantasy,566.95
Escape from Earth,Cade Firebrand,Horror,822.55
Dreamwalker,Drake Nightshade,Horror,988.85
Mystery of the Depths,Zara Stormrider,Fantasy,47.0
<start>
- Box Office Earnings (M): 631.56
  Director: Mara Moonshadow
  Genre: Thriller
  Title: Escape from Earth
- Box Office Earnings (M): 566.95
  Director: Drake Nightshade
  Genre: Fantasy
  Title: The Final Voyage
- Box Office Earnings (M): 822.55
  Director: Cade Firebrand
  Genre: Horror
  Title: Escape from Earth
- Box Office Earnings (M): 988.85
  Director: Drake Nightshade
  Genre: Horror
  Title: Dreamwalker
- Box Office Earnings (M): 47.0
  Director: Zara Stormrider
  Genre: Fantasy
  Title: Mystery of the Depths
<end>Please transform the following markdown data into csv:
| Company | Sector | Market Cap | Stock Price | Annual Revenue (B) | Quarter |
| --- | --- | --- | --- | --- | --- |
| AutoDrive | Technology | Large Cap | 934.53 | 80.9 | Q4 |
| RetailHub | Retail | Mega Cap | 515.95 | 474.55 | Q3 |
| EcoEnergy | Technology | Mid Cap | 412.48 | 433.64 | Q4 |
| BioPharm | Retail | Mega Cap | 700.91 | 261.91 | Q4 |<start>
Company,Sector,Market Cap,Stock Price,Annual Revenue (B),Quarter
AutoDrive,Technology,Large Cap,934.53,80.9,Q4
RetailHub,Retail,Mega Cap,515.95,474.55,Q3
EcoEnergy,Technology,Mid Cap,412.48,433.64,Q4
BioPharm,Retail,Mega Cap,700.91,261.91,Q4
<end>Can you change this Yaml into Json?
- Condition: Sunny
  Day: Sunday
  Location: Los Angeles
  Wind Speed (km/h): 15.2
- Condition: Snowy
  Day: Monday
  Location: Los Angeles
  Wind Speed (km/h): 5.8
- Condition: Snowy
  Day: Wednesday
  Location: Chicago
  Wind Speed (km/h): 20.6
- Condition: Cloudy
  Day: Saturday
  Location: New York
  Wind Speed (km/h): 18.4
- Condition: Rainy
  Day: Thursday
  Location: Houston
  Wind Speed (km/h): 5.0
- Condition: Rainy
  Day: Saturday
  Location: Miami
  Wind Speed (km/h): 19.2
- Condition: Rainy
  Day: Tuesday
  Location: Houston
  Wind Speed (km/h): 15.4
<start>
[
    {
        "Location": "Los Angeles",
        "Condition": "Sunny",
        "Wind Speed (km/h)": 15.2,
        "Day": "Sunday"
    },
    {
        "Location": "Los Angeles",
        "Condition": "Snowy",
        "Wind Speed (km/h)": 5.8,
        "Day": "Monday"
    },
    {
        "Location": "Chicago",
        "Condition": "Snowy",
        "Wind Speed (km/h)": 20.6,
        "Day": "Wednesday"
    },
    {
        "Location": "New York",
        "Condition": "Cloudy",
        "Wind Speed (km/h)": 18.4,
        "Day": "Saturday"
    },
    {
        "Location": "Houston",
        "Condition": "Rainy",
        "Wind Speed (km/h)": 5.0,
        "Day": "Thursday"
    },
    {
        "Location": "Miami",
        "Condition": "Rainy",
        "Wind Speed (km/h)": 19.2,
        "Day": "Saturday"
    },
    {
        "Location": "Houston",
        "Condition": "Rainy",
        "Wind Speed (km/h)": 15.4,
        "Day": "Tuesday"
    }
]
<end>Transform this csv structure to a json format:
Title,Director,Genre,Release Year,Box Office Earnings (M)
Starbound Odyssey,Lira Silverleaf,Horror,1985,563.88
The Endless Horizon,Selene Darkwhisper,Adventure,2005,946.76
Rise of the Titans,Selene Darkwhisper,Horror,1978,608.5
Starbound Odyssey,Lira Silverleaf,Sci-Fi,1970,990.64
Rise of the Titans,Drake Nightshade,Action,1975,608.5
Rise of the Titans,Cade Firebrand,Comedy,1975,211.33
Rise of the Titans,Drake Nightshade,Action,1979,98.46
Mystery of the Depths,Cade Firebrand,Sci-Fi,1970,730.87
<start>
[
    {
        "Title": "Starbound Odyssey",
        "Director": "Lira Silverleaf",
        "Genre": "Horror",
        "Release Year": 1985,
        "Box Office Earnings (M)": 563.88
    },
    {
        "Title": "The Endless Horizon",
        "Director": "Selene Darkwhisper",
        "Genre": "Adventure",
        "Release Year": 2005,
        "Box Office Earnings (M)": 946.76
    },
    {
        "Title": "Rise of the Titans",
        "Director": "Selene Darkwhisper",
        "Genre": "Horror",
        "Release Year": 1978,
        "Box Office Earnings (M)": 608.5
    },
    {
        "Title": "Starbound Odyssey",
        "Director": "Lira Silverleaf",
        "Genre": "Sci-Fi",
        "Release Year": 1970,
        "Box Office Earnings (M)": 990.64
    },
    {
        "Title": "Rise of the Titans",
        "Director": "Drake Nightshade",
        "Genre": "Action",
        "Release Year": 1975,
        "Box Office Earnings (M)": 608.5
    },
    {
        "Title": "Rise of the Titans",
        "Director": "Cade Firebrand",
        "Genre": "Comedy",
        "Release Year": 1975,
        "Box Office Earnings (M)": 211.33
    },
    {
        "Title": "Rise of the Titans",
        "Director": "Drake Nightshade",
        "Genre": "Action",
        "Release Year": 1979,
        "Box Office Earnings (M)": 98.46
    },
    {
        "Title": "Mystery of the Depths",
        "Director": "Cade Firebrand",
        "Genre": "Sci-Fi",
        "Release Year": 1970,
        "Box Office Earnings (M)": 730.87
    }
]
<end>Transform this Markdown structure to a PLAIN TEXT format:
| Location | Condition | Temperature (C) | Humidity (%) | Wind Speed (km/h) | Day |
| --- | --- | --- | --- | --- | --- |
| Denver | Foggy | -0.2 | 78 | 23.8 | Thursday |
| New York | Stormy | 21.5 | 30 | 19.1 | Wednesday |
| Seattle | Windy | 25.9 | 94 | 24.5 | Saturday |
| Chicago | Cloudy | 21.5 | 86 | 21.0 | Thursday |
| Houston | Windy | 2.0 | 59 | 23.8 | Tuesday |<start>
Location: Denver | Condition: Foggy | Temperature (C): -0.2 | Humidity (%): 78 | Wind Speed (km/h): 23.8 | Day: Thursday
Location: New York | Condition: Stormy | Temperature (C): 21.5 | Humidity (%): 30 | Wind Speed (km/h): 19.1 | Day: Wednesday
Location: Seattle | Condition: Windy | Temperature (C): 25.9 | Humidity (%): 94 | Wind Speed (km/h): 24.5 | Day: Saturday
Location: Chicago | Condition: Cloudy | Temperature (C): 21.5 | Humidity (%): 86 | Wind Speed (km/h): 21.0 | Day: Thursday
Location: Houston | Condition: Windy | Temperature (C): 2.0 | Humidity (%): 59 | Wind Speed (km/h): 23.8 | Day: Tuesday
<end>Convert this csv to PLAIN TEXT:
Product Name,Price,Stock Quantity,Category
Apparatus,369.59,53,Household
Thingamajig,255.88,481,Toys
Thingamajig,239.71,25,Toys
<start>
Product Name: Apparatus | Price: 369.59 | Stock Quantity: 53 | Category: Household
Product Name: Thingamajig | Price: 255.88 | Stock Quantity: 481 | Category: Toys
Product Name: Thingamajig | Price: 239.71 | Stock Quantity: 25 | Category: Toys
<end>Please transform the following Csv data into MARKDOWN:
Trip Name,Start Location,End Location,Distance (miles),Duration (hours),Fuel Used (gallons)
Canyon Trek,Denver,Phoenix,1996.2,33.1,91.4
Coast to Coast,Houston,Denver,816.9,58.6,72.5
Canyon Trek,San Francisco,New York,2883.4,10.3,59.6
Valley Voyage,Miami,Houston,2066.2,67.6,18.0
<start>
| Trip Name | Start Location | End Location | Distance (miles) | Duration (hours) | Fuel Used (gallons) |
| --- | --- | --- | --- | --- | --- |
| Canyon Trek | Denver | Phoenix | 1996.2 | 33.1 | 91.4 |
| Coast to Coast | Houston | Denver | 816.9 | 58.6 | 72.5 |
| Canyon Trek | San Francisco | New York | 2883.4 | 10.3 | 59.6 |
| Valley Voyage | Miami | Houston | 2066.2 | 67.6 | 18.0 |
<end>Can you change this csv into plain text?
Company,Annual Revenue (B),Quarter
GlobalTrade,380.47,Q4
HealthPlus,246.6,Q4
GlobalTrade,420.65,Q3
<start>
Company: GlobalTrade | Annual Revenue (B): 380.47 | Quarter: Q4
Company: HealthPlus | Annual Revenue (B): 246.6 | Quarter: Q4
Company: GlobalTrade | Annual Revenue (B): 420.65 | Quarter: Q3
<end>Transform this json structure to a plain text format:
[
    {
        "Title": "Rise of the Titans",
        "Director": "Aria Ravenwood",
        "Genre": "Action",
        "Box Office Earnings (M)": 802.83
    },
    {
        "Title": "Escape from Earth",
        "Director": "Mara Moonshadow",
        "Genre": "Adventure",
        "Box Office Earnings (M)": 707.87
    },
    {
        "Title": "Edge of Infinity",
        "Director": "Talon Blackthorn",
        "Genre": "Sci-Fi",
        "Box Office Earnings (M)": 533.63
    },
    {
        "Title": "The Final Voyage",
        "Director": "Drake Nightshade",
        "Genre": "Drama",
        "Box Office Earnings (M)": 24.01
    },
    {
        "Title": "Mystery of the Depths",
        "Director": "Aria Ravenwood",
        "Genre": "Horror",
        "Box Office Earnings (M)": 792.18
    }
]<start>
Title: Rise of the Titans | Director: Aria Ravenwood | Genre: Action | Box Office Earnings (M): 802.83
Title: Escape from Earth | Director: Mara Moonshadow | Genre: Adventure | Box Office Earnings (M): 707.87
Title: Edge of Infinity | Director: Talon Blackthorn | Genre: Sci-Fi | Box Office Earnings (M): 533.63
Title: The Final Voyage | Director: Drake Nightshade | Genre: Drama | Box Office Earnings (M): 24.01
Title: Mystery of the Depths | Director: Aria Ravenwood | Genre: Horror | Box Office Earnings (M): 792.18
<end>Please transform the following PLAIN TEXT data into csv:
Title: Echoes of Eternity | Author: Galen Starfire | Genre: Mystery | Publication Year: 2017 | Rating: 2.7
Title: Tales of the Brave | Author: Galen Starfire | Genre: Historical | Publication Year: 2001 | Rating: 2.8
Title: The Forgotten World | Author: Kara Firebrand | Genre: Thriller | Publication Year: 1953 | Rating: 1.0
Title: Whispers of the Abyss | Author: Luna Silverleaf | Genre: Romance | Publication Year: 1987 | Rating: 4.6
Title: Shadows of Solitude | Author: Orion Frostblade | Genre: Thriller | Publication Year: 1969 | Rating: 3.2
Title: The Silent Grove | Author: Luna Silverleaf | Genre: Romance | Publication Year: 2021 | Rating: 2.5
<start>
Title,Author,Genre,Publication Year,Rating
Echoes of Eternity,Galen Starfire,Mystery,2017,2.7
Tales of the Brave,Galen Starfire,Historical,2001,2.8
The Forgotten World,Kara Firebrand,Thriller,1953,1.0
Whispers of the Abyss,Luna Silverleaf,Romance,1987,4.6
Shadows of Solitude,Orion Frostblade,Thriller,1969,3.2
The Silent Grove,Luna Silverleaf,Romance,2021,2.5
<end>Please transform the following plain text data into yml:
Location: Houston | Temperature (C): 6.6 | Humidity (%): 53 | Wind Speed (km/h): 12.2 | Day: Thursday
Location: Seattle | Temperature (C): 28.3 | Humidity (%): 67 | Wind Speed (km/h): 19.8 | Day: Sunday
Location: Denver | Temperature (C): 24.2 | Humidity (%): 83 | Wind Speed (km/h): 22.5 | Day: Sunday
Location: Miami | Temperature (C): 0.2 | Humidity (%): 49 | Wind Speed (km/h): 14.7 | Day: Saturday
Location: Denver | Temperature (C): 23.5 | Humidity (%): 40 | Wind Speed (km/h): 19.8 | Day: Tuesday
Location: Los Angeles | Temperature (C): 12.3 | Humidity (%): 98 | Wind Speed (km/h): 18.0 | Day: Saturday
<start>
- Day: Thursday
  Humidity (%): 53
  Location: Houston
  Temperature (C): 6.6
  Wind Speed (km/h): 12.2
- Day: Sunday
  Humidity (%): 67
  Location: Seattle
  Temperature (C): 28.3
  Wind Speed (km/h): 19.8
- Day: Sunday
  Humidity (%): 83
  Location: Denver
  Temperature (C): 24.2
  Wind Speed (km/h): 22.5
- Day: Saturday
  Humidity (%): 49
  Location: Miami
  Temperature (C): 0.2
  Wind Speed (km/h): 14.7
- Day: Tuesday
  Humidity (%): 40
  Location: Denver
  Temperature (C): 23.5
  Wind Speed (km/h): 19.8
- Day: Saturday
  Humidity (%): 98
  Location: Los Angeles
  Temperature (C): 12.3
  Wind Speed (km/h): 18.0
<end>Please transform the following JSON data into markdown:
[
    {
        "Database Name": "InventoryDB",
        "Queries per Second": 177.67,
        "Cache Hit Ratio (%)": 71.01,
        "Connection Count": 46,
        "Average Latency (ms)": 57.55,
        "Timestamp": "2023-02-02 20:06:07"
    },
    {
        "Database Name": "UserDB",
        "Queries per Second": 542.89,
        "Cache Hit Ratio (%)": 83.09,
        "Connection Count": 448,
        "Average Latency (ms)": 52.39,
        "Timestamp": "2021-09-05 09:45:15"
    },
    {
        "Database Name": "MetricsDB",
        "Queries per Second": 3279.52,
        "Cache Hit Ratio (%)": 81.77,
        "Connection Count": 146,
        "Average Latency (ms)": 46.86,
        "Timestamp": "2021-02-10 08:48:20"
    }
]<start>
| Database Name | Queries per Second | Cache Hit Ratio (%) | Connection Count | Average Latency (ms) | Timestamp |
| --- | --- | --- | --- | --- | --- |
| InventoryDB | 177.67 | 71.01 | 46 | 57.55 | 2023-02-02 20:06:07 |
| UserDB | 542.89 | 83.09 | 448 | 52.39 | 2021-09-05 09:45:15 |
| MetricsDB | 3279.52 | 81.77 | 146 | 46.86 | 2021-02-10 08:48:20 |
<end>Here's some Yml data, can you convert it to json?
- Distance (miles): 1269.1
  Duration (hours): 11.3
  Fuel Used (gallons): 5.5
  Start Location: Phoenix
  Trip Name: Coast to Coast
- Distance (miles): 1149.0
  Duration (hours): 43.4
  Fuel Used (gallons): 98.7
  Start Location: Chicago
  Trip Name: Valley Voyage
- Distance (miles): 581.6
  Duration (hours): 21.3
  Fuel Used (gallons): 72.4
  Start Location: Phoenix
  Trip Name: City Explorer
- Distance (miles): 2586.4
  Duration (hours): 21.3
  Fuel Used (gallons): 71.6
  Start Location: Chicago
  Trip Name: City Explorer
- Distance (miles): 1494.8
  Duration (hours): 10.0
  Fuel Used (gallons): 45.4
  Start Location: Houston
  Trip Name: Desert Drive
- Distance (miles): 371.5
  Duration (hours): 46.0
  Fuel Used (gallons): 91.0
  Start Location: Denver
  Trip Name: Canyon Trek
- Distance (miles): 753.4
  Duration (hours): 19.2
  Fuel Used (gallons): 67.8
  Start Location: Houston
  Trip Name: Valley Voyage
- Distance (miles): 296.8
  Duration (hours): 50.6
  Fuel Used (gallons): 7.2
  Start Location: Los Angeles
  Trip Name: Mountain Adventure
- Distance (miles): 1948.7
  Duration (hours): 50.6
  Fuel Used (gallons): 23.4
  Start Location: Houston
  Trip Name: Mountain Adventure
- Distance (miles): 1986.6
  Duration (hours): 20.1
  Fuel Used (gallons): 50.5
  Start Location: Houston
  Trip Name: Forest Journey
<start>
[
    {
        "Trip Name": "Coast to Coast",
        "Start Location": "Phoenix",
        "Distance (miles)": 1269.1,
        "Duration (hours)": 11.3,
        "Fuel Used (gallons)": 5.5
    },
    {
        "Trip Name": "Valley Voyage",
        "Start Location": "Chicago",
        "Distance (miles)": 1149.0,
        "Duration (hours)": 43.4,
        "Fuel Used (gallons)": 98.7
    },
    {
        "Trip Name": "City Explorer",
        "Start Location": "Phoenix",
        "Distance (miles)": 581.6,
        "Duration (hours)": 21.3,
        "Fuel Used (gallons)": 72.4
    },
    {
        "Trip Name": "City Explorer",
        "Start Location": "Chicago",
        "Distance (miles)": 2586.4,
        "Duration (hours)": 21.3,
        "Fuel Used (gallons)": 71.6
    },
    {
        "Trip Name": "Desert Drive",
        "Start Location": "Houston",
        "Distance (miles)": 1494.8,
        "Duration (hours)": 10.0,
        "Fuel Used (gallons)": 45.4
    },
    {
        "Trip Name": "Canyon Trek",
        "Start Location": "Denver",
        "Distance (miles)": 371.5,
        "Duration (hours)": 46.0,
        "Fuel Used (gallons)": 91.0
    },
    {
        "Trip Name": "Valley Voyage",
        "Start Location": "Houston",
        "Distance (miles)": 753.4,
        "Duration (hours)": 19.2,
        "Fuel Used (gallons)": 67.8
    },
    {
        "Trip Name": "Mountain Adventure",
        "Start Location": "Los Angeles",
        "Distance (miles)": 296.8,
        "Duration (hours)": 50.6,
        "Fuel Used (gallons)": 7.2
    },
    {
        "Trip Name": "Mountain Adventure",
        "Start Location": "Houston",
        "Distance (miles)": 1948.7,
        "Duration (hours)": 50.6,
        "Fuel Used (gallons)": 23.4
    },
    {
        "Trip Name": "Forest Journey",
        "Start Location": "Houston",
        "Distance (miles)": 1986.6,
        "Duration (hours)": 20.1,
        "Fuel Used (gallons)": 50.5
    }
]
<end>Convert this Markdown to plain text:
| Restaurant Name | Location |
| --- | --- |
| Vegan Delight | San Francisco |
| Vegan Delight | Miami |
| Taco Town | San Francisco |
| The Golden Spoon | Phoenix |
| The Golden Spoon | Los Angeles |<start>
Restaurant Name: Vegan Delight | Location: San Francisco
Restaurant Name: Vegan Delight | Location: Miami
Restaurant Name: Taco Town | Location: San Francisco
Restaurant Name: The Golden Spoon | Location: Phoenix
Restaurant Name: The Golden Spoon | Location: Los Angeles
<end>Please transform the following csv data into yml:
Device ID,Device Type,Reading Value,Timestamp
device-0064,Motion Detector,45.47,2023-12-04 05:32:59
device-0016,Pressure Sensor,-13.64,2022-02-18 16:53:51
device-0064,Motion Detector,67.78,2021-03-22 16:00:28
<start>
- Device ID: device-0064
  Device Type: Motion Detector
  Reading Value: 45.47
  Timestamp: '2023-12-04 05:32:59'
- Device ID: device-0016
  Device Type: Pressure Sensor
  Reading Value: -13.64
  Timestamp: '2022-02-18 16:53:51'
- Device ID: device-0064
  Device Type: Motion Detector
  Reading Value: 67.78
  Timestamp: '2021-03-22 16:00:28'
<end>Transform this YML structure to a Plain text format:
- Genre: Thriller
  Publication Year: 2016
  Title: Tales of the Brave
- Genre: Non-Fiction
  Publication Year: 1973
  Title: The Last Sky
- Genre: Mystery
  Publication Year: 1951
  Title: The Forgotten World
- Genre: Romance
  Publication Year: 1956
  Title: The Last Sky
- Genre: Mystery
  Publication Year: 1955
  Title: The Last Sky
- Genre: Science Fiction
  Publication Year: 2005
  Title: The Forgotten World
- Genre: Mystery
  Publication Year: 2014
  Title: Shadows of Solitude
- Genre: Science Fiction
  Publication Year: 1986
  Title: The Forgotten World
<start>
Title: Tales of the Brave | Genre: Thriller | Publication Year: 2016
Title: The Last Sky | Genre: Non-Fiction | Publication Year: 1973
Title: The Forgotten World | Genre: Mystery | Publication Year: 1951
Title: The Last Sky | Genre: Romance | Publication Year: 1956
Title: The Last Sky | Genre: Mystery | Publication Year: 1955
Title: The Forgotten World | Genre: Science Fiction | Publication Year: 2005
Title: Shadows of Solitude | Genre: Mystery | Publication Year: 2014
Title: The Forgotten World | Genre: Science Fiction | Publication Year: 1986
<end>Can you change this csv into plain text?
Director,Release Year,Box Office Earnings (M)
Aria Ravenwood,2006,453.75
Lira Silverleaf,1998,230.58
Selene Darkwhisper,1984,424.19
<start>
Director: Aria Ravenwood | Release Year: 2006 | Box Office Earnings (M): 453.75
Director: Lira Silverleaf | Release Year: 1998 | Box Office Earnings (M): 230.58
Director: Selene Darkwhisper | Release Year: 1984 | Box Office Earnings (M): 424.19
<end>Please transform the following Plain text data into Csv:
Product Name: Widget | SKU: SKU-1005 | Price: 261.64 | Supplier Name: ACME Corp
Product Name: Gadget | SKU: SKU-1007 | Price: 156.41 | Supplier Name: Wonka Industries
Product Name: Thingamajig | SKU: SKU-1002 | Price: 39.21 | Supplier Name: ACME Corp
Product Name: Thingamajig | SKU: SKU-1092 | Price: 126.62 | Supplier Name: Wonka Industries
Product Name: Gadget | SKU: SKU-1032 | Price: 428.5 | Supplier Name: Umbrella Corp
Product Name: Instrument | SKU: SKU-1027 | Price: 468.25 | Supplier Name: ACME Corp
Product Name: Device | SKU: SKU-1020 | Price: 483.51 | Supplier Name: Wayne Enterprises
Product Name: Doohickey | SKU: SKU-1007 | Price: 158.43 | Supplier Name: Globex
<start>
Product Name,SKU,Price,Supplier Name
Widget,SKU-1005,261.64,ACME Corp
Gadget,SKU-1007,156.41,Wonka Industries
Thingamajig,SKU-1002,39.21,ACME Corp
Thingamajig,SKU-1092,126.62,Wonka Industries
Gadget,SKU-1032,428.5,Umbrella Corp
Instrument,SKU-1027,468.25,ACME Corp
Device,SKU-1020,483.51,Wayne Enterprises
Doohickey,SKU-1007,158.43,Globex
<end>Here's some markdown data, can you convert it to plain text?
| Title | Genre | Publication Year | Rating |
| --- | --- | --- | --- |
| Legends of the Rift | Thriller | 2018 | 2.9 |
| The Last Sky | Horror | 2016 | 4.5 |
| The Silent Grove | Horror | 1966 | 4.3 |
| The Forgotten World | Historical | 2008 | 2.5 |
| Shadows of Solitude | Horror | 1963 | 2.6 |<start>
Title: Legends of the Rift | Genre: Thriller | Publication Year: 2018 | Rating: 2.9
Title: The Last Sky | Genre: Horror | Publication Year: 2016 | Rating: 4.5
Title: The Silent Grove | Genre: Horror | Publication Year: 1966 | Rating: 4.3
Title: The Forgotten World | Genre: Historical | Publication Year: 2008 | Rating: 2.5
Title: Shadows of Solitude | Genre: Horror | Publication Year: 1963 | Rating: 2.6
<end>Please transform the following Plain text data into markdown:
Restaurant Name: BBQ Barn | Cuisine: French | Location: Houston | Rating: 4
Restaurant Name: Pizza Planet | Cuisine: American | Location: Chicago | Rating: 2
Restaurant Name: Burger Haven | Cuisine: Indian | Location: Miami | Rating: 2
<start>
| Restaurant Name | Cuisine | Location | Rating |
| --- | --- | --- | --- |
| BBQ Barn | French | Houston | 4 |
| Pizza Planet | American | Chicago | 2 |
| Burger Haven | Indian | Miami | 2 |
<end>Here's some yml data, can you convert it to Json?
- Age: 32
  Birth Month: December
  Name: Kristen
- Age: 21
  Birth Month: December
  Name: Rickey
- Age: 47
  Birth Month: March
  Name: Devon
- Age: 42
  Birth Month: July
  Name: Jeffrey
- Age: 37
  Birth Month: July
  Name: Camila
- Age: 43
  Birth Month: September
  Name: Javier
- Age: 50
  Birth Month: July
  Name: Morgan
- Age: 33
  Birth Month: July
  Name: Ray
<start>
[
    {
        "Name": "Kristen",
        "Age": 32,
        "Birth Month": "December"
    },
    {
        "Name": "Rickey",
        "Age": 21,
        "Birth Month": "December"
    },
    {
        "Name": "Devon",
        "Age": 47,
        "Birth Month": "March"
    },
    {
        "Name": "Jeffrey",
        "Age": 42,
        "Birth Month": "July"
    },
    {
        "Name": "Camila",
        "Age": 37,
        "Birth Month": "July"
    },
    {
        "Name": "Javier",
        "Age": 43,
        "Birth Month": "September"
    },
    {
        "Name": "Morgan",
        "Age": 50,
        "Birth Month": "July"
    },
    {
        "Name": "Ray",
        "Age": 33,
        "Birth Month": "July"
    }
]
<end>Can you change this Markdown into Yml?
| Name | Age | Birth Month | City | Income |
| --- | --- | --- | --- | --- |
| Mindy | 25 | June | San Antonio | 395000 |
| Jennifer | 61 | September | Memphis | 270000 |
| Laverne | 41 | November | Oklahoma City | 90000 |
| Joanna | 47 | November | Denver | 170000 |
| Cristian | 42 | July | Nashville | 100000 |
| Norah | 35 | October | New York | 150000 |<start>
- Age: 25
  Birth Month: June
  City: San Antonio
  Income: 395000
  Name: Mindy
- Age: 61
  Birth Month: September
  City: Memphis
  Income: 270000
  Name: Jennifer
- Age: 41
  Birth Month: November
  City: Oklahoma City
  Income: 90000
  Name: Laverne
- Age: 47
  Birth Month: November
  City: Denver
  Income: 170000
  Name: Joanna
- Age: 42
  Birth Month: July
  City: Nashville
  Income: 100000
  Name: Cristian
- Age: 35
  Birth Month: October
  City: New York
  Income: 150000
  Name: Norah
<end>Please transform the following CSV data into yaml:
Genre,Release Year,Box Office Earnings (M)
Horror,1993,462.34
Action,2015,248.34
Horror,2012,469.93
Fantasy,1973,409.31
Comedy,2006,765.26
Comedy,1970,345.74
Adventure,1983,112.07
<start>
- Box Office Earnings (M): 462.34
  Genre: Horror
  Release Year: 1993
- Box Office Earnings (M): 248.34
  Genre: Action
  Release Year: 2015
- Box Office Earnings (M): 469.93
  Genre: Horror
  Release Year: 2012
- Box Office Earnings (M): 409.31
  Genre: Fantasy
  Release Year: 1973
- Box Office Earnings (M): 765.26
  Genre: Comedy
  Release Year: 2006
- Box Office Earnings (M): 345.74
  Genre: Comedy
  Release Year: 1970
- Box Office Earnings (M): 112.07
  Genre: Adventure
  Release Year: 1983
<end>Convert this markdown to YAML:
| Name | Birth Month |
| --- | --- |
| Alisha | July |
| Kari | June |
| Sarah | September |
| Omar | January |
| Gage | May |<start>
- Birth Month: July
  Name: Alisha
- Birth Month: June
  Name: Kari
- Birth Month: September
  Name: Sarah
- Birth Month: January
  Name: Omar
- Birth Month: May
  Name: Gage
<end>Please transform the following MARKDOWN data into plain text:
| Title | Author | Publication Year |
| --- | --- | --- |
| Tales of the Brave | Isla Windrider | 1953 |
| A Journey Through Time | Sylvia Nightshade | 1991 |
| The Crystal Key | Kara Firebrand | 2002 |
| The Crystal Key | Orion Frostblade | 1978 |
| Shadows of Solitude | Galen Starfire | 2014 |
| Whispers of the Abyss | Orion Frostblade | 1952 |
| Whispers of the Abyss | Kara Firebrand | 2020 |
| Whispers of the Abyss | Luna Silverleaf | 1985 |<start>
Title: Tales of the Brave | Author: Isla Windrider | Publication Year: 1953
Title: A Journey Through Time | Author: Sylvia Nightshade | Publication Year: 1991
Title: The Crystal Key | Author: Kara Firebrand | Publication Year: 2002
Title: The Crystal Key | Author: Orion Frostblade | Publication Year: 1978
Title: Shadows of Solitude | Author: Galen Starfire | Publication Year: 2014
Title: Whispers of the Abyss | Author: Orion Frostblade | Publication Year: 1952
Title: Whispers of the Abyss | Author: Kara Firebrand | Publication Year: 2020
Title: Whispers of the Abyss | Author: Luna Silverleaf | Publication Year: 1985
<end>Can you change this csv into json?
Company,Close Price,High Price,Low Price
MediaGroup,257.65,532.54,257.65
AutoMotive,1469.45,1469.45,1277.91
HealthGen,727.83,1064.04,245.51
AeroSystems,933.62,933.62,166.49
RetailWorld,1146.4,1469.45,1146.4
MediaGroup,239.93,831.0,177.84
HealthGen,166.49,960.73,166.49
GreenEnergy,242.78,887.78,51.13
HealthGen,1325.75,1325.75,926.76
FoodChain,733.09,1257.13,239.93
<start>
[
    {
        "Company": "MediaGroup",
        "Close Price": 257.65,
        "High Price": 532.54,
        "Low Price": 257.65
    },
    {
        "Company": "AutoMotive",
        "Close Price": 1469.45,
        "High Price": 1469.45,
        "Low Price": 1277.91
    },
    {
        "Company": "HealthGen",
        "Close Price": 727.83,
        "High Price": 1064.04,
        "Low Price": 245.51
    },
    {
        "Company": "AeroSystems",
        "Close Price": 933.62,
        "High Price": 933.62,
        "Low Price": 166.49
    },
    {
        "Company": "RetailWorld",
        "Close Price": 1146.4,
        "High Price": 1469.45,
        "Low Price": 1146.4
    },
    {
        "Company": "MediaGroup",
        "Close Price": 239.93,
        "High Price": 831.0,
        "Low Price": 177.84
    },
    {
        "Company": "HealthGen",
        "Close Price": 166.49,
        "High Price": 960.73,
        "Low Price": 166.49
    },
    {
        "Company": "GreenEnergy",
        "Close Price": 242.78,
        "High Price": 887.78,
        "Low Price": 51.13
    },
    {
        "Company": "HealthGen",
        "Close Price": 1325.75,
        "High Price": 1325.75,
        "Low Price": 926.76
    },
    {
        "Company": "FoodChain",
        "Close Price": 733.09,
        "High Price": 1257.13,
        "Low Price": 239.93
    }
]
<end>Transform this json structure to a plain text format:
[
    {
        "Company": "RetailWorld",
        "Date": "2023-02-10",
        "Open Price": 1312.78,
        "Close Price": 900.59,
        "High Price": 1312.78,
        "Low Price": 900.59,
        "Volume": 7336318
    },
    {
        "Company": "AeroSystems",
        "Date": "2014-04-23",
        "Open Price": 243.36,
        "Close Price": 377.31,
        "High Price": 1018.18,
        "Low Price": 243.36,
        "Volume": 8272303
    },
    {
        "Company": "RetailWorld",
        "Date": "2020-11-01",
        "Open Price": 1424.11,
        "Close Price": 540.48,
        "High Price": 1424.11,
        "Low Price": 540.48,
        "Volume": 9486477
    },
    {
        "Company": "MediaGroup",
        "Date": "2013-01-19",
        "Open Price": 243.36,
        "Close Price": 1150.56,
        "High Price": 1312.78,
        "Low Price": 243.36,
        "Volume": 6856563
    },
    {
        "Company": "FoodChain",
        "Date": "2020-02-09",
        "Open Price": 1207.05,
        "Close Price": 879.1,
        "High Price": 1207.05,
        "Low Price": 175.37,
        "Volume": 4392981
    },
    {
        "Company": "FinanceTrust",
        "Date": "2019-08-22",
        "Open Price": 1407.71,
        "Close Price": 285.06,
        "High Price": 1407.71,
        "Low Price": 285.06,
        "Volume": 9486477
    },
    {
        "Company": "GreenEnergy",
        "Date": "2012-10-02",
        "Open Price": 1294.84,
        "Close Price": 1119.69,
        "High Price": 1294.84,
        "Low Price": 540.48,
        "Volume": 9049417
    },
    {
        "Company": "FinanceTrust",
        "Date": "2017-01-22",
        "Open Price": 1191.06,
        "Close Price": 955.48,
        "High Price": 1191.06,
        "Low Price": 175.37,
        "Volume": 1066217
    },
    {
        "Company": "FinanceTrust",
        "Date": "2019-12-08",
        "Open Price": 644.59,
        "Close Price": 1294.84,
        "High Price": 1294.84,
        "Low Price": 644.59,
        "Volume": 7336318
    }
]<start>
Company: RetailWorld | Date: 2023-02-10 | Open Price: 1312.78 | Close Price: 900.59 | High Price: 1312.78 | Low Price: 900.59 | Volume: 7336318
Company: AeroSystems | Date: 2014-04-23 | Open Price: 243.36 | Close Price: 377.31 | High Price: 1018.18 | Low Price: 243.36 | Volume: 8272303
Company: RetailWorld | Date: 2020-11-01 | Open Price: 1424.11 | Close Price: 540.48 | High Price: 1424.11 | Low Price: 540.48 | Volume: 9486477
Company: MediaGroup | Date: 2013-01-19 | Open Price: 243.36 | Close Price: 1150.56 | High Price: 1312.78 | Low Price: 243.36 | Volume: 6856563
Company: FoodChain | Date: 2020-02-09 | Open Price: 1207.05 | Close Price: 879.1 | High Price: 1207.05 | Low Price: 175.37 | Volume: 4392981
Company: FinanceTrust | Date: 2019-08-22 | Open Price: 1407.71 | Close Price: 285.06 | High Price: 1407.71 | Low Price: 285.06 | Volume: 9486477
Company: GreenEnergy | Date: 2012-10-02 | Open Price: 1294.84 | Close Price: 1119.69 | High Price: 1294.84 | Low Price: 540.48 | Volume: 9049417
Company: FinanceTrust | Date: 2017-01-22 | Open Price: 1191.06 | Close Price: 955.48 | High Price: 1191.06 | Low Price: 175.37 | Volume: 1066217
Company: FinanceTrust | Date: 2019-12-08 | Open Price: 644.59 | Close Price: 1294.84 | High Price: 1294.84 | Low Price: 644.59 | Volume: 7336318
<end>Here's some JSON data, can you convert it to yaml?
[
    {
        "SKU": "SKU-1099",
        "Stock Quantity": 43,
        "Supplier Name": "Globex"
    },
    {
        "SKU": "SKU-1066",
        "Stock Quantity": 189,
        "Supplier Name": "ACME Corp"
    },
    {
        "SKU": "SKU-1066",
        "Stock Quantity": 98,
        "Supplier Name": "Globex"
    },
    {
        "SKU": "SKU-1028",
        "Stock Quantity": 491,
        "Supplier Name": "ACME Corp"
    },
    {
        "SKU": "SKU-1057",
        "Stock Quantity": 50,
        "Supplier Name": "Wayne Enterprises"
    }
]<start>
- SKU: SKU-1099
  Stock Quantity: 43
  Supplier Name: Globex
- SKU: SKU-1066
  Stock Quantity: 189
  Supplier Name: ACME Corp
- SKU: SKU-1066
  Stock Quantity: 98
  Supplier Name: Globex
- SKU: SKU-1028
  Stock Quantity: 491
  Supplier Name: ACME Corp
- SKU: SKU-1057
  Stock Quantity: 50
  Supplier Name: Wayne Enterprises
<end>Transform this Plain text structure to a CSV format:
Stock Price: 645.73 | Annual Revenue (B): 54.71 | Quarter: Q4
Stock Price: 823.96 | Annual Revenue (B): 330.07 | Quarter: Q4
Stock Price: 338.69 | Annual Revenue (B): 396.28 | Quarter: Q1
Stock Price: 810.0 | Annual Revenue (B): 231.18 | Quarter: Q2
Stock Price: 717.44 | Annual Revenue (B): 349.25 | Quarter: Q1
Stock Price: 175.84 | Annual Revenue (B): 275.47 | Quarter: Q4
Stock Price: 959.19 | Annual Revenue (B): 123.01 | Quarter: Q4
Stock Price: 596.73 | Annual Revenue (B): 243.74 | Quarter: Q2
Stock Price: 13.16 | Annual Revenue (B): 367.44 | Quarter: Q3
<start>
Stock Price,Annual Revenue (B),Quarter
645.73,54.71,Q4
823.96,330.07,Q4
338.69,396.28,Q1
810.0,231.18,Q2
717.44,349.25,Q1
175.84,275.47,Q4
959.19,123.01,Q4
596.73,243.74,Q2
13.16,367.44,Q3
<end>Transform this csv structure to a JSON format:
Genre,Release Year,Box Office Earnings (M)
Drama,1983,395.04
Fantasy,1990,591.44
Drama,1994,881.7
Horror,2000,680.5
Horror,2020,188.32
Drama,1977,949.27
Drama,1989,443.59
Fantasy,2019,573.53
<start>
[
    {
        "Genre": "Drama",
        "Release Year": 1983,
        "Box Office Earnings (M)": 395.04
    },
    {
        "Genre": "Fantasy",
        "Release Year": 1990,
        "Box Office Earnings (M)": 591.44
    },
    {
        "Genre": "Drama",
        "Release Year": 1994,
        "Box Office Earnings (M)": 881.7
    },
    {
        "Genre": "Horror",
        "Release Year": 2000,
        "Box Office Earnings (M)": 680.5
    },
    {
        "Genre": "Horror",
        "Release Year": 2020,
        "Box Office Earnings (M)": 188.32
    },
    {
        "Genre": "Drama",
        "Release Year": 1977,
        "Box Office Earnings (M)": 949.27
    },
    {
        "Genre": "Drama",
        "Release Year": 1989,
        "Box Office Earnings (M)": 443.59
    },
    {
        "Genre": "Fantasy",
        "Release Year": 2019,
        "Box Office Earnings (M)": 573.53
    }
]
<end>Here's some Markdown data, can you convert it to Csv?
| Device ID | Device Type | Location | Battery Level (%) | Reading Value |
| --- | --- | --- | --- | --- |
| device-0084 | Temperature Sensor | Bathroom | 72.5 | -23.99 |
| device-0027 | Humidity Sensor | Garden | 67.3 | 7.62 |
| device-0067 | Temperature Sensor | Bathroom | 20.2 | -18.76 |
| device-0002 | Motion Detector | Garage | 90.8 | 26.68 |
| device-0031 | Pressure Sensor | Office | 63.2 | 8.07 |
| device-0084 | Motion Detector | Bathroom | 56.7 | 33.61 |<start>
Device ID,Device Type,Location,Battery Level (%),Reading Value
device-0084,Temperature Sensor,Bathroom,72.5,-23.99
device-0027,Humidity Sensor,Garden,67.3,7.62
device-0067,Temperature Sensor,Bathroom,20.2,-18.76
device-0002,Motion Detector,Garage,90.8,26.68
device-0031,Pressure Sensor,Office,63.2,8.07
device-0084,Motion Detector,Bathroom,56.7,33.61
<end>Can you change this markdown into Yml?
| Publication Year | Rating |
| --- | --- |
| 1963 | 4.5 |
| 1968 | 1.5 |
| 1969 | 1.2 |
| 1959 | 4.5 |
| 2008 | 1.1 |
| 2020 | 3.4 |<start>
- Publication Year: 1963
  Rating: 4.5
- Publication Year: 1968
  Rating: 1.5
- Publication Year: 1969
  Rating: 1.2
- Publication Year: 1959
  Rating: 4.5
- Publication Year: 2008
  Rating: 1.1
- Publication Year: 2020
  Rating: 3.4
<end>Convert this MARKDOWN to JSON:
| Product Name | SKU | Price | Stock Quantity | Category | Supplier Name |
| --- | --- | --- | --- | --- | --- |
| Widget | SKU-1011 | 469.92 | 478 | Electronics | Globex |
| Doohickey | SKU-1085 | 434.73 | 73 | Electronics | Wayne Enterprises |
| Doohickey | SKU-1011 | 429.48 | 166 | Toys | Umbrella Corp |<start>
[
    {
        "Product Name": "Widget",
        "SKU": "SKU-1011",
        "Price": 469.92,
        "Stock Quantity": 478,
        "Category": "Electronics",
        "Supplier Name": "Globex"
    },
    {
        "Product Name": "Doohickey",
        "SKU": "SKU-1085",
        "Price": 434.73,
        "Stock Quantity": 73,
        "Category": "Electronics",
        "Supplier Name": "Wayne Enterprises"
    },
    {
        "Product Name": "Doohickey",
        "SKU": "SKU-1011",
        "Price": 429.48,
        "Stock Quantity": 166,
        "Category": "Toys",
        "Supplier Name": "Umbrella Corp"
    }
]
<end>Please transform the following plain text data into json:
Name: Mikayla | Age: 26 | Birth Month: April | Income: 405000
Name: Muriel | Age: 29 | Birth Month: January | Income: 430000
Name: Rita | Age: 32 | Birth Month: December | Income: 470000
Name: Hector | Age: 43 | Birth Month: June | Income: 25000
Name: Kaden | Age: 27 | Birth Month: December | Income: 55000
<start>
[
    {
        "Name": "Mikayla",
        "Age": 26,
        "Birth Month": "April",
        "Income": 405000
    },
    {
        "Name": "Muriel",
        "Age": 29,
        "Birth Month": "January",
        "Income": 430000
    },
    {
        "Name": "Rita",
        "Age": 32,
        "Birth Month": "December",
        "Income": 470000
    },
    {
        "Name": "Hector",
        "Age": 43,
        "Birth Month": "June",
        "Income": 25000
    },
    {
        "Name": "Kaden",
        "Age": 27,
        "Birth Month": "December",
        "Income": 55000
    }
]
<end>Here's some YAML data, can you convert it to plain text?
- Cuisine: Italian
  Location: Chicago
  Price Range: $$$
- Cuisine: Japanese
  Location: Los Angeles
  Price Range: $$$
- Cuisine: Indian
  Location: Phoenix
  Price Range: $$$
- Cuisine: Chinese
  Location: Seattle
  Price Range: $$$$$
- Cuisine: French
  Location: Chicago
  Price Range: $$$$$
- Cuisine: Italian
  Location: Los Angeles
  Price Range: $$
<start>
Cuisine: Italian | Location: Chicago | Price Range: $$$
Cuisine: Japanese | Location: Los Angeles | Price Range: $$$
Cuisine: Indian | Location: Phoenix | Price Range: $$$
Cuisine: Chinese | Location: Seattle | Price Range: $$$$$
Cuisine: French | Location: Chicago | Price Range: $$$$$
Cuisine: Italian | Location: Los Angeles | Price Range: $$
<end>Can you change this Markdown into PLAIN TEXT?
| Company | Market Cap | Stock Price |
| --- | --- | --- |
| Foodies | Mid Cap | 98.61 |
| HealthPlus | Mega Cap | 609.79 |
| RetailHub | Small Cap | 681.12 |
| AutoDrive | Mega Cap | 220.1 |
| AeroSpace | Large Cap | 132.02 |<start>
Company: Foodies | Market Cap: Mid Cap | Stock Price: 98.61
Company: HealthPlus | Market Cap: Mega Cap | Stock Price: 609.79
Company: RetailHub | Market Cap: Small Cap | Stock Price: 681.12
Company: AutoDrive | Market Cap: Mega Cap | Stock Price: 220.1
Company: AeroSpace | Market Cap: Large Cap | Stock Price: 132.02
<end>Here's some plain text data, can you convert it to CSV?
Restaurant Name: The Steakhouse | Cuisine: Chinese | Location: Phoenix | Rating: 1
Restaurant Name: Pasta Palace | Cuisine: Indian | Location: Los Angeles | Rating: 2
Restaurant Name: Vegan Delight | Cuisine: Mexican | Location: Houston | Rating: 5
Restaurant Name: Pasta Palace | Cuisine: Italian | Location: New York | Rating: 5
Restaurant Name: Vegan Delight | Cuisine: French | Location: New York | Rating: 1
<start>
Restaurant Name,Cuisine,Location,Rating
The Steakhouse,Chinese,Phoenix,1
Pasta Palace,Indian,Los Angeles,2
Vegan Delight,Mexican,Houston,5
Pasta Palace,Italian,New York,5
Vegan Delight,French,New York,1
<end>Please transform the following Yml data into MARKDOWN:
- Annual Revenue (B): 340.09
  Market Cap: Large Cap
  Quarter: Q1
- Annual Revenue (B): 499.38
  Market Cap: Large Cap
  Quarter: Q2
- Annual Revenue (B): 92.63
  Market Cap: Large Cap
  Quarter: Q2
<start>
| Market Cap | Annual Revenue (B) | Quarter |
| --- | --- | --- |
| Large Cap | 340.09 | Q1 |
| Large Cap | 499.38 | Q2 |
| Large Cap | 92.63 | Q2 |
<end>Here's some JSON data, can you convert it to yml?
[
    {
        "Location": "Phoenix",
        "Condition": "Snowy",
        "Temperature (C)": 29.6,
        "Humidity (%)": 95,
        "Wind Speed (km/h)": 28.7,
        "Day": "Thursday"
    },
    {
        "Location": "New York",
        "Condition": "Rainy",
        "Temperature (C)": -0.9,
        "Humidity (%)": 61,
        "Wind Speed (km/h)": 0.1,
        "Day": "Tuesday"
    },
    {
        "Location": "New York",
        "Condition": "Rainy",
        "Temperature (C)": 17.9,
        "Humidity (%)": 58,
        "Wind Speed (km/h)": 27.8,
        "Day": "Monday"
    },
    {
        "Location": "New York",
        "Condition": "Stormy",
        "Temperature (C)": 29.2,
        "Humidity (%)": 88,
        "Wind Speed (km/h)": 21.1,
        "Day": "Saturday"
    },
    {
        "Location": "Chicago",
        "Condition": "Stormy",
        "Temperature (C)": 35.0,
        "Humidity (%)": 33,
        "Wind Speed (km/h)": 25.7,
        "Day": "Sunday"
    },
    {
        "Location": "Houston",
        "Condition": "Stormy",
        "Temperature (C)": 9.7,
        "Humidity (%)": 48,
        "Wind Speed (km/h)": 5.9,
        "Day": "Sunday"
    },
    {
        "Location": "Seattle",
        "Condition": "Foggy",
        "Temperature (C)": 13.9,
        "Humidity (%)": 76,
        "Wind Speed (km/h)": 24.8,
        "Day": "Monday"
    }
]<start>
- Condition: Snowy
  Day: Thursday
  Humidity (%): 95
  Location: Phoenix
  Temperature (C): 29.6
  Wind Speed (km/h): 28.7
- Condition: Rainy
  Day: Tuesday
  Humidity (%): 61
  Location: New York
  Temperature (C): -0.9
  Wind Speed (km/h): 0.1
- Condition: Rainy
  Day: Monday
  Humidity (%): 58
  Location: New York
  Temperature (C): 17.9
  Wind Speed (km/h): 27.8
- Condition: Stormy
  Day: Saturday
  Humidity (%): 88
  Location: New York
  Temperature (C): 29.2
  Wind Speed (km/h): 21.1
- Condition: Stormy
  Day: Sunday
  Humidity (%): 33
  Location: Chicago
  Temperature (C): 35.0
  Wind Speed (km/h): 25.7
- Condition: Stormy
  Day: Sunday
  Humidity (%): 48
  Location: Houston
  Temperature (C): 9.7
  Wind Speed (km/h): 5.9
- Condition: Foggy
  Day: Monday
  Humidity (%): 76
  Location: Seattle
  Temperature (C): 13.9
  Wind Speed (km/h): 24.8
<end>Here's some csv data, can you convert it to plain text?
Location,Condition,Temperature (C),Day
Denver,Cloudy,36.7,Saturday
Miami,Sunny,-3.8,Thursday
Seattle,Stormy,38.0,Wednesday
Miami,Foggy,22.4,Saturday
Chicago,Foggy,38.0,Tuesday
New York,Snowy,32.7,Sunday
New York,Cloudy,-8.1,Friday
Phoenix,Cloudy,24.4,Tuesday
Los Angeles,Sunny,36.1,Saturday
Miami,Stormy,24.7,Wednesday
<start>
Location: Denver | Condition: Cloudy | Temperature (C): 36.7 | Day: Saturday
Location: Miami | Condition: Sunny | Temperature (C): -3.8 | Day: Thursday
Location: Seattle | Condition: Stormy | Temperature (C): 38.0 | Day: Wednesday
Location: Miami | Condition: Foggy | Temperature (C): 22.4 | Day: Saturday
Location: Chicago | Condition: Foggy | Temperature (C): 38.0 | Day: Tuesday
Location: New York | Condition: Snowy | Temperature (C): 32.7 | Day: Sunday
Location: New York | Condition: Cloudy | Temperature (C): -8.1 | Day: Friday
Location: Phoenix | Condition: Cloudy | Temperature (C): 24.4 | Day: Tuesday
Location: Los Angeles | Condition: Sunny | Temperature (C): 36.1 | Day: Saturday
Location: Miami | Condition: Stormy | Temperature (C): 24.7 | Day: Wednesday
<end>Please transform the following plain text data into MARKDOWN:
Location: New York | Condition: Snowy | Temperature (C): 35.6 | Humidity (%): 28 | Wind Speed (km/h): 22.9 | Day: Saturday
Location: New York | Condition: Sunny | Temperature (C): 32.3 | Humidity (%): 44 | Wind Speed (km/h): 7.2 | Day: Saturday
Location: Denver | Condition: Rainy | Temperature (C): 10.1 | Humidity (%): 72 | Wind Speed (km/h): 15.5 | Day: Sunday
Location: Miami | Condition: Snowy | Temperature (C): 18.6 | Humidity (%): 66 | Wind Speed (km/h): 0.5 | Day: Friday
Location: New York | Condition: Snowy | Temperature (C): 13.2 | Humidity (%): 66 | Wind Speed (km/h): 15.2 | Day: Thursday
Location: Chicago | Condition: Sunny | Temperature (C): 9.9 | Humidity (%): 59 | Wind Speed (km/h): 23.8 | Day: Sunday
<start>
| Location | Condition | Temperature (C) | Humidity (%) | Wind Speed (km/h) | Day |
| --- | --- | --- | --- | --- | --- |
| New York | Snowy | 35.6 | 28 | 22.9 | Saturday |
| New York | Sunny | 32.3 | 44 | 7.2 | Saturday |
| Denver | Rainy | 10.1 | 72 | 15.5 | Sunday |
| Miami | Snowy | 18.6 | 66 | 0.5 | Friday |
| New York | Snowy | 13.2 | 66 | 15.2 | Thursday |
| Chicago | Sunny | 9.9 | 59 | 23.8 | Sunday |
<end>Transform this PLAIN TEXT structure to a csv format:
Start Location: Los Angeles | End Location: Denver | Distance (miles): 1469.4 | Duration (hours): 53.9
Start Location: Phoenix | End Location: San Francisco | Distance (miles): 2995.6 | Duration (hours): 40.9
Start Location: Phoenix | End Location: New York | Distance (miles): 2268.5 | Duration (hours): 66.5
Start Location: Phoenix | End Location: New York | Distance (miles): 2311.7 | Duration (hours): 42.6
<start>
Start Location,End Location,Distance (miles),Duration (hours)
Los Angeles,Denver,1469.4,53.9
Phoenix,San Francisco,2995.6,40.9
Phoenix,New York,2268.5,66.5
Phoenix,New York,2311.7,42.6
<end>Transform this markdown structure to a yaml format:
| Start Location | End Location | Duration (hours) |
| --- | --- | --- |
| Phoenix | Chicago | 57.8 |
| Los Angeles | Chicago | 36.3 |
| Los Angeles | Houston | 10.0 |
| New York | Phoenix | 63.3 |
| Phoenix | Chicago | 12.4 |<start>
- Duration (hours): 57.8
  End Location: Chicago
  Start Location: Phoenix
- Duration (hours): 36.3
  End Location: Chicago
  Start Location: Los Angeles
- Duration (hours): 10.0
  End Location: Houston
  Start Location: Los Angeles
- Duration (hours): 63.3
  End Location: Phoenix
  Start Location: New York
- Duration (hours): 12.4
  End Location: Chicago
  Start Location: Phoenix
<end>Here's some markdown data, can you convert it to yaml?
| Trip Name | Start Location | End Location | Duration (hours) |
| --- | --- | --- | --- |
| Lakeside Retreat | Miami | Houston | 25.4 |
| Highway Odyssey | Phoenix | Miami | 48.0 |
| Historic Route | San Francisco | New York | 52.9 |
| Highway Odyssey | Phoenix | San Francisco | 31.2 |
| Valley Voyage | New York | Miami | 18.5 |
| City Explorer | Chicago | Los Angeles | 32.8 |
| Highway Odyssey | Phoenix | Miami | 24.2 |<start>
- Duration (hours): 25.4
  End Location: Houston
  Start Location: Miami
  Trip Name: Lakeside Retreat
- Duration (hours): 48.0
  End Location: Miami
  Start Location: Phoenix
  Trip Name: Highway Odyssey
- Duration (hours): 52.9
  End Location: New York
  Start Location: San Francisco
  Trip Name: Historic Route
- Duration (hours): 31.2
  End Location: San Francisco
  Start Location: Phoenix
  Trip Name: Highway Odyssey
- Duration (hours): 18.5
  End Location: Miami
  Start Location: New York
  Trip Name: Valley Voyage
- Duration (hours): 32.8
  End Location: Los Angeles
  Start Location: Chicago
  Trip Name: City Explorer
- Duration (hours): 24.2
  End Location: Miami
  Start Location: Phoenix
  Trip Name: Highway Odyssey
<end>Here's some MARKDOWN data, can you convert it to csv?
| SKU | Price | Category | Supplier Name |
| --- | --- | --- | --- |
| SKU-1009 | 225.82 | Automotive | Umbrella Corp |
| SKU-1049 | 446.41 | Sports | Globex |
| SKU-1052 | 302.29 | Automotive | Wonka Industries |
| SKU-1036 | 53.99 | Automotive | Umbrella Corp |
| SKU-1083 | 177.11 | Toys | Umbrella Corp |
| SKU-1010 | 444.72 | Household | Wonka Industries |
| SKU-1091 | 487.15 | Household | Wonka Industries |
| SKU-1058 | 186.99 | Sports | Umbrella Corp |
| SKU-1055 | 387.53 | Sports | Wayne Enterprises |<start>
SKU,Price,Category,Supplier Name
SKU-1009,225.82,Automotive,Umbrella Corp
SKU-1049,446.41,Sports,Globex
SKU-1052,302.29,Automotive,Wonka Industries
SKU-1036,53.99,Automotive,Umbrella Corp
SKU-1083,177.11,Toys,Umbrella Corp
SKU-1010,444.72,Household,Wonka Industries
SKU-1091,487.15,Household,Wonka Industries
SKU-1058,186.99,Sports,Umbrella Corp
SKU-1055,387.53,Sports,Wayne Enterprises
<end>Here's some json data, can you convert it to markdown?
[
    {
        "Company": "HealthGen",
        "Date": "2014-05-22",
        "Open Price": 1054.24,
        "Close Price": 390.33,
        "High Price": 1406.67,
        "Low Price": 390.33,
        "Volume": 7165340
    },
    {
        "Company": "FinanceTrust",
        "Date": "2010-03-19",
        "Open Price": 1133.17,
        "Close Price": 1299.76,
        "High Price": 1299.76,
        "Low Price": 674.86,
        "Volume": 1098518
    },
    {
        "Company": "RetailWorld",
        "Date": "2023-09-19",
        "Open Price": 179.72,
        "Close Price": 1038.49,
        "High Price": 1038.49,
        "Low Price": 179.72,
        "Volume": 6016802
    },
    {
        "Company": "FoodChain",
        "Date": "2020-11-03",
        "Open Price": 963.2,
        "Close Price": 1067.0,
        "High Price": 1067.0,
        "Low Price": 705.26,
        "Volume": 4512442
    },
    {
        "Company": "TechnoCorp",
        "Date": "2021-01-10",
        "Open Price": 529.38,
        "Close Price": 1320.26,
        "High Price": 1320.26,
        "Low Price": 529.38,
        "Volume": 8098162
    }
]<start>
| Company | Date | Open Price | Close Price | High Price | Low Price | Volume |
| --- | --- | --- | --- | --- | --- | --- |
| HealthGen | 2014-05-22 | 1054.24 | 390.33 | 1406.67 | 390.33 | 7165340 |
| FinanceTrust | 2010-03-19 | 1133.17 | 1299.76 | 1299.76 | 674.86 | 1098518 |
| RetailWorld | 2023-09-19 | 179.72 | 1038.49 | 1038.49 | 179.72 | 6016802 |
| FoodChain | 2020-11-03 | 963.2 | 1067.0 | 1067.0 | 705.26 | 4512442 |
| TechnoCorp | 2021-01-10 | 529.38 | 1320.26 | 1320.26 | 529.38 | 8098162 |
<end>Convert this Csv to yml:
Location,Reading Value,Timestamp
Hallway,25.67,2023-02-20 23:13:38
Bedroom,63.33,2022-04-06 10:52:30
Bathroom,-38.1,2021-12-18 04:25:07
Living Room,-26.69,2022-04-19 13:15:13
Hallway,76.4,2023-10-26 12:18:52
Bedroom,34.38,2022-09-13 18:00:42
Bedroom,76.59,2022-08-15 07:18:30
Hallway,-2.28,2022-09-08 21:06:16
Bedroom,45.29,2023-09-21 16:39:08
Bathroom,63.33,2022-07-18 06:48:46
<start>
- Location: Hallway
  Reading Value: 25.67
  Timestamp: '2023-02-20 23:13:38'
- Location: Bedroom
  Reading Value: 63.33
  Timestamp: '2022-04-06 10:52:30'
- Location: Bathroom
  Reading Value: -38.1
  Timestamp: '2021-12-18 04:25:07'
- Location: Living Room
  Reading Value: -26.69
  Timestamp: '2022-04-19 13:15:13'
- Location: Hallway
  Reading Value: 76.4
  Timestamp: '2023-10-26 12:18:52'
- Location: Bedroom
  Reading Value: 34.38
  Timestamp: '2022-09-13 18:00:42'
- Location: Bedroom
  Reading Value: 76.59
  Timestamp: '2022-08-15 07:18:30'
- Location: Hallway
  Reading Value: -2.28
  Timestamp: '2022-09-08 21:06:16'
- Location: Bedroom
  Reading Value: 45.29
  Timestamp: '2023-09-21 16:39:08'
- Location: Bathroom
  Reading Value: 63.33
  Timestamp: '2022-07-18 06:48:46'
<end>Please transform the following JSON data into Markdown:
[
    {
        "Device ID": "device-0092",
        "Reading Value": -33.57,
        "Timestamp": "2021-09-24 18:21:44"
    },
    {
        "Device ID": "device-0007",
        "Reading Value": 29.78,
        "Timestamp": "2021-10-09 08:46:11"
    },
    {
        "Device ID": "device-0045",
        "Reading Value": -27.71,
        "Timestamp": "2021-09-19 07:29:54"
    },
    {
        "Device ID": "device-0003",
        "Reading Value": 34.1,
        "Timestamp": "2021-11-15 00:34:48"
    },
    {
        "Device ID": "device-0072",
        "Reading Value": 64.85,
        "Timestamp": "2022-08-20 07:40:19"
    },
    {
        "Device ID": "device-0089",
        "Reading Value": 82.45,
        "Timestamp": "2023-04-11 03:38:38"
    },
    {
        "Device ID": "device-0003",
        "Reading Value": -5.25,
        "Timestamp": "2021-11-03 08:18:22"
    },
    {
        "Device ID": "device-0095",
        "Reading Value": 42.97,
        "Timestamp": "2021-11-08 14:59:31"
    },
    {
        "Device ID": "device-0022",
        "Reading Value": -23.8,
        "Timestamp": "2023-01-12 08:21:55"
    },
    {
        "Device ID": "device-0058",
        "Reading Value": 19.12,
        "Timestamp": "2022-06-05 01:01:14"
    }
]<start>
| Device ID | Reading Value | Timestamp |
| --- | --- | --- |
| device-0092 | -33.57 | 2021-09-24 18:21:44 |
| device-0007 | 29.78 | 2021-10-09 08:46:11 |
| device-0045 | -27.71 | 2021-09-19 07:29:54 |
| device-0003 | 34.1 | 2021-11-15 00:34:48 |
| device-0072 | 64.85 | 2022-08-20 07:40:19 |
| device-0089 | 82.45 | 2023-04-11 03:38:38 |
| device-0003 | -5.25 | 2021-11-03 08:18:22 |
| device-0095 | 42.97 | 2021-11-08 14:59:31 |
| device-0022 | -23.8 | 2023-01-12 08:21:55 |
| device-0058 | 19.12 | 2022-06-05 01:01:14 |
<end>Convert this markdown to json:
| Product Name | SKU | Price | Category | Supplier Name |
| --- | --- | --- | --- | --- |
| Widget | SKU-1036 | 180.19 | Sports | Wayne Enterprises |
| Gadget | SKU-1065 | 436.48 | Electronics | Umbrella Corp |
| Apparatus | SKU-1002 | 94.67 | Toys | ACME Corp |
| Gadget | SKU-1022 | 349.42 | Household | ACME Corp |<start>
[
    {
        "Product Name": "Widget",
        "SKU": "SKU-1036",
        "Price": 180.19,
        "Category": "Sports",
        "Supplier Name": "Wayne Enterprises"
    },
    {
        "Product Name": "Gadget",
        "SKU": "SKU-1065",
        "Price": 436.48,
        "Category": "Electronics",
        "Supplier Name": "Umbrella Corp"
    },
    {
        "Product Name": "Apparatus",
        "SKU": "SKU-1002",
        "Price": 94.67,
        "Category": "Toys",
        "Supplier Name": "ACME Corp"
    },
    {
        "Product Name": "Gadget",
        "SKU": "SKU-1022",
        "Price": 349.42,
        "Category": "Household",
        "Supplier Name": "ACME Corp"
    }
]
<end>Can you change this markdown into YML?
| Database Name | Queries per Second | Cache Hit Ratio (%) | Connection Count | Average Latency (ms) | Timestamp |
| --- | --- | --- | --- | --- | --- |
| AnalyticsDB | 438.94 | 74.86 | 409 | 74.93 | 2023-03-08 22:05:53 |
| UserDB | 4417.81 | 97.24 | 156 | 35.37 | 2021-08-14 03:28:30 |
| UserDB | 3969.41 | 70.09 | 240 | 70.64 | 2022-04-16 21:18:19 |
| AnalyticsDB | 245.88 | 76.64 | 366 | 8.21 | 2022-02-01 01:11:16 |<start>
- Average Latency (ms): 74.93
  Cache Hit Ratio (%): 74.86
  Connection Count: 409
  Database Name: AnalyticsDB
  Queries per Second: 438.94
  Timestamp: '2023-03-08 22:05:53'
- Average Latency (ms): 35.37
  Cache Hit Ratio (%): 97.24
  Connection Count: 156
  Database Name: UserDB
  Queries per Second: 4417.81
  Timestamp: '2021-08-14 03:28:30'
- Average Latency (ms): 70.64
  Cache Hit Ratio (%): 70.09
  Connection Count: 240
  Database Name: UserDB
  Queries per Second: 3969.41
  Timestamp: '2022-04-16 21:18:19'
- Average Latency (ms): 8.21
  Cache Hit Ratio (%): 76.64
  Connection Count: 366
  Database Name: AnalyticsDB
  Queries per Second: 245.88
  Timestamp: '2022-02-01 01:11:16'
<end>Please transform the following json data into markdown:
[
    {
        "Genre": "Adventure",
        "Release Year": 2009
    },
    {
        "Genre": "Horror",
        "Release Year": 1990
    },
    {
        "Genre": "Horror",
        "Release Year": 1976
    },
    {
        "Genre": "Drama",
        "Release Year": 2013
    }
]<start>
| Genre | Release Year |
| --- | --- |
| Adventure | 2009 |
| Horror | 1990 |
| Horror | 1976 |
| Drama | 2013 |
<end>Convert this csv to Plain text:
Title,Author,Publication Year,Rating
Whispers of the Abyss,Galen Starfire,1992,3.4
The Last Sky,Elara Moonshadow,2022,4.2
The Last Sky,Kara Firebrand,1982,3.2
A Journey Through Time,Rowan Ashborne,2019,4.8
Echoes of Eternity,Galen Starfire,2008,3.7
The Last Sky,Sylvia Nightshade,1988,4.2
The Crystal Key,Luna Silverleaf,1989,3.8
<start>
Title: Whispers of the Abyss | Author: Galen Starfire | Publication Year: 1992 | Rating: 3.4
Title: The Last Sky | Author: Elara Moonshadow | Publication Year: 2022 | Rating: 4.2
Title: The Last Sky | Author: Kara Firebrand | Publication Year: 1982 | Rating: 3.2
Title: A Journey Through Time | Author: Rowan Ashborne | Publication Year: 2019 | Rating: 4.8
Title: Echoes of Eternity | Author: Galen Starfire | Publication Year: 2008 | Rating: 3.7
Title: The Last Sky | Author: Sylvia Nightshade | Publication Year: 1988 | Rating: 4.2
Title: The Crystal Key | Author: Luna Silverleaf | Publication Year: 1989 | Rating: 3.8
<end>Can you change this CSV into Markdown?
Date,Close Price,High Price,Low Price
2013-07-18,286.01,342.92,286.01
2017-01-22,44.84,1202.91,44.84
2019-05-09,1255.11,1463.67,804.51
<start>
| Date | Close Price | High Price | Low Price |
| --- | --- | --- | --- |
| 2013-07-18 | 286.01 | 342.92 | 286.01 |
| 2017-01-22 | 44.84 | 1202.91 | 44.84 |
| 2019-05-09 | 1255.11 | 1463.67 | 804.51 |
<end>Here's some csv data, can you convert it to markdown?
Product Name,SKU,Price,Category,Supplier Name
Gadget,SKU-1041,421.16,Electronics,ACME Corp
Thingamajig,SKU-1012,263.03,Toys,Wayne Enterprises
Widget,SKU-1099,13.9,Electronics,Umbrella Corp
Widget,SKU-1038,275.6,Household,ACME Corp
Gizmo,SKU-1013,467.7,Household,ACME Corp
Instrument,SKU-1064,347.91,Sports,ACME Corp
Gadget,SKU-1074,201.32,Household,Umbrella Corp
Contraption,SKU-1049,13.39,Electronics,ACME Corp
Gadget,SKU-1086,237.15,Household,Wonka Industries
Doohickey,SKU-1007,186.75,Toys,Umbrella Corp
<start>
| Product Name | SKU | Price | Category | Supplier Name |
| --- | --- | --- | --- | --- |
| Gadget | SKU-1041 | 421.16 | Electronics | ACME Corp |
| Thingamajig | SKU-1012 | 263.03 | Toys | Wayne Enterprises |
| Widget | SKU-1099 | 13.9 | Electronics | Umbrella Corp |
| Widget | SKU-1038 | 275.6 | Household | ACME Corp |
| Gizmo | SKU-1013 | 467.7 | Household | ACME Corp |
| Instrument | SKU-1064 | 347.91 | Sports | ACME Corp |
| Gadget | SKU-1074 | 201.32 | Household | Umbrella Corp |
| Contraption | SKU-1049 | 13.39 | Electronics | ACME Corp |
| Gadget | SKU-1086 | 237.15 | Household | Wonka Industries |
| Doohickey | SKU-1007 | 186.75 | Toys | Umbrella Corp |
<end>Please transform the following PLAIN TEXT data into MARKDOWN:
Database Name: ProductsDB | Cache Hit Ratio (%): 86.38 | Connection Count: 247 | Average Latency (ms): 30.84
Database Name: InventoryDB | Cache Hit Ratio (%): 87.62 | Connection Count: 319 | Average Latency (ms): 28.86
Database Name: MetricsDB | Cache Hit Ratio (%): 95.13 | Connection Count: 99 | Average Latency (ms): 15.83
Database Name: ProductsDB | Cache Hit Ratio (%): 88.84 | Connection Count: 160 | Average Latency (ms): 63.24
Database Name: InventoryDB | Cache Hit Ratio (%): 88.04 | Connection Count: 135 | Average Latency (ms): 2.97
Database Name: SessionsDB | Cache Hit Ratio (%): 80.79 | Connection Count: 209 | Average Latency (ms): 69.68
Database Name: SessionsDB | Cache Hit Ratio (%): 88.37 | Connection Count: 463 | Average Latency (ms): 23.92
<start>
| Database Name | Cache Hit Ratio (%) | Connection Count | Average Latency (ms) |
| --- | --- | --- | --- |
| ProductsDB | 86.38 | 247 | 30.84 |
| InventoryDB | 87.62 | 319 | 28.86 |
| MetricsDB | 95.13 | 99 | 15.83 |
| ProductsDB | 88.84 | 160 | 63.24 |
| InventoryDB | 88.04 | 135 | 2.97 |
| SessionsDB | 80.79 | 209 | 69.68 |
| SessionsDB | 88.37 | 463 | 23.92 |
<end>Transform this yaml structure to a JSON format:
- Box Office Earnings (M): 301.33
  Director: Drake Nightshade
  Genre: Adventure
  Release Year: 1982
- Box Office Earnings (M): 788.6
  Director: Aria Ravenwood
  Genre: Sci-Fi
  Release Year: 1998
- Box Office Earnings (M): 781.11
  Director: Rylan Frostblade
  Genre: Comedy
  Release Year: 2023
- Box Office Earnings (M): 301.33
  Director: Aria Ravenwood
  Genre: Thriller
  Release Year: 2001
- Box Office Earnings (M): 352.45
  Director: Orin Shadowalker
  Genre: Action
  Release Year: 1978
- Box Office Earnings (M): 82.06
  Director: Selene Darkwhisper
  Genre: Action
  Release Year: 1977
- Box Office Earnings (M): 143.51
  Director: Selene Darkwhisper
  Genre: Adventure
  Release Year: 1971
- Box Office Earnings (M): 565.1
  Director: Talon Blackthorn
  Genre: Sci-Fi
  Release Year: 1994
- Box Office Earnings (M): 155.07
  Director: Aria Ravenwood
  Genre: Drama
  Release Year: 1975
- Box Office Earnings (M): 202.13
  Director: Cade Firebrand
  Genre: Adventure
  Release Year: 1978
<start>
[
    {
        "Director": "Drake Nightshade",
        "Genre": "Adventure",
        "Release Year": 1982,
        "Box Office Earnings (M)": 301.33
    },
    {
        "Director": "Aria Ravenwood",
        "Genre": "Sci-Fi",
        "Release Year": 1998,
        "Box Office Earnings (M)": 788.6
    },
    {
        "Director": "Rylan Frostblade",
        "Genre": "Comedy",
        "Release Year": 2023,
        "Box Office Earnings (M)": 781.11
    },
    {
        "Director": "Aria Ravenwood",
        "Genre": "Thriller",
        "Release Year": 2001,
        "Box Office Earnings (M)": 301.33
    },
    {
        "Director": "Orin Shadowalker",
        "Genre": "Action",
        "Release Year": 1978,
        "Box Office Earnings (M)": 352.45
    },
    {
        "Director": "Selene Darkwhisper",
        "Genre": "Action",
        "Release Year": 1977,
        "Box Office Earnings (M)": 82.06
    },
    {
        "Director": "Selene Darkwhisper",
        "Genre": "Adventure",
        "Release Year": 1971,
        "Box Office Earnings (M)": 143.51
    },
    {
        "Director": "Talon Blackthorn",
        "Genre": "Sci-Fi",
        "Release Year": 1994,
        "Box Office Earnings (M)": 565.1
    },
    {
        "Director": "Aria Ravenwood",
        "Genre": "Drama",
        "Release Year": 1975,
        "Box Office Earnings (M)": 155.07
    },
    {
        "Director": "Cade Firebrand",
        "Genre": "Adventure",
        "Release Year": 1978,
        "Box Office Earnings (M)": 202.13
    }
]
<end>Please transform the following Yaml data into markdown:
- Category: Household
  Price: 389.42
  Product Name: Whatchamacallit
  SKU: SKU-1033
  Stock Quantity: 405
  Supplier Name: Umbrella Corp
- Category: Automotive
  Price: 155.01
  Product Name: Whatchamacallit
  SKU: SKU-1074
  Stock Quantity: 389
  Supplier Name: Globex
- Category: Toys
  Price: 164.25
  Product Name: Gizmo
  SKU: SKU-1075
  Stock Quantity: 453
  Supplier Name: Globex
- Category: Electronics
  Price: 128.44
  Product Name: Doohickey
  SKU: SKU-1066
  Stock Quantity: 73
  Supplier Name: Wayne Enterprises
- Category: Electronics
  Price: 312.03
  Product Name: Whatchamacallit
  SKU: SKU-1055
  Stock Quantity: 215
  Supplier Name: Wayne Enterprises
- Category: Household
  Price: 275.14
  Product Name: Widget
  SKU: SKU-1064
  Stock Quantity: 481
  Supplier Name: ACME Corp
- Category: Household
  Price: 221.09
  Product Name: Contraption
  SKU: SKU-1061
  Stock Quantity: 445
  Supplier Name: Wonka Industries
<start>
| Product Name | SKU | Price | Stock Quantity | Category | Supplier Name |
| --- | --- | --- | --- | --- | --- |
| Whatchamacallit | SKU-1033 | 389.42 | 405 | Household | Umbrella Corp |
| Whatchamacallit | SKU-1074 | 155.01 | 389 | Automotive | Globex |
| Gizmo | SKU-1075 | 164.25 | 453 | Toys | Globex |
| Doohickey | SKU-1066 | 128.44 | 73 | Electronics | Wayne Enterprises |
| Whatchamacallit | SKU-1055 | 312.03 | 215 | Electronics | Wayne Enterprises |
| Widget | SKU-1064 | 275.14 | 481 | Household | ACME Corp |
| Contraption | SKU-1061 | 221.09 | 445 | Household | Wonka Industries |
<end>Can you change this Plain text into json?
Start Location: Chicago | Distance (miles): 1628.1 | Duration (hours): 39.7 | Fuel Used (gallons): 37.4
Start Location: New York | Distance (miles): 1065.1 | Duration (hours): 40.0 | Fuel Used (gallons): 71.3
Start Location: San Francisco | Distance (miles): 1480.0 | Duration (hours): 14.5 | Fuel Used (gallons): 89.5
Start Location: Miami | Distance (miles): 2635.0 | Duration (hours): 18.6 | Fuel Used (gallons): 43.2
Start Location: Phoenix | Distance (miles): 1688.2 | Duration (hours): 40.8 | Fuel Used (gallons): 36.4
Start Location: Phoenix | Distance (miles): 256.7 | Duration (hours): 57.9 | Fuel Used (gallons): 95.5
Start Location: Los Angeles | Distance (miles): 1276.9 | Duration (hours): 44.4 | Fuel Used (gallons): 84.9
Start Location: Los Angeles | Distance (miles): 463.3 | Duration (hours): 21.2 | Fuel Used (gallons): 51.2
Start Location: New York | Distance (miles): 657.0 | Duration (hours): 40.0 | Fuel Used (gallons): 35.9
Start Location: Chicago | Distance (miles): 2308.0 | Duration (hours): 64.6 | Fuel Used (gallons): 23.6
<start>
[
    {
        "Start Location": "Chicago",
        "Distance (miles)": 1628.1,
        "Duration (hours)": 39.7,
        "Fuel Used (gallons)": 37.4
    },
    {
        "Start Location": "New York",
        "Distance (miles)": 1065.1,
        "Duration (hours)": 40.0,
        "Fuel Used (gallons)": 71.3
    },
    {
        "Start Location": "San Francisco",
        "Distance (miles)": 1480.0,
        "Duration (hours)": 14.5,
        "Fuel Used (gallons)": 89.5
    },
    {
        "Start Location": "Miami",
        "Distance (miles)": 2635.0,
        "Duration (hours)": 18.6,
        "Fuel Used (gallons)": 43.2
    },
    {
        "Start Location": "Phoenix",
        "Distance (miles)": 1688.2,
        "Duration (hours)": 40.8,
        "Fuel Used (gallons)": 36.4
    },
    {
        "Start Location": "Phoenix",
        "Distance (miles)": 256.7,
        "Duration (hours)": 57.9,
        "Fuel Used (gallons)": 95.5
    },
    {
        "Start Location": "Los Angeles",
        "Distance (miles)": 1276.9,
        "Duration (hours)": 44.4,
        "Fuel Used (gallons)": 84.9
    },
    {
        "Start Location": "Los Angeles",
        "Distance (miles)": 463.3,
        "Duration (hours)": 21.2,
        "Fuel Used (gallons)": 51.2
    },
    {
        "Start Location": "New York",
        "Distance (miles)": 657.0,
        "Duration (hours)": 40.0,
        "Fuel Used (gallons)": 35.9
    },
    {
        "Start Location": "Chicago",
        "Distance (miles)": 2308.0,
        "Duration (hours)": 64.6,
        "Fuel Used (gallons)": 23.6
    }
]
<end>Please transform the following csv data into PLAIN TEXT:
Device ID,Location,Reading Value
device-0005,Garden,48.26
device-0019,Living Room,51.65
device-0007,Garage,-24.01
device-0026,Office,67.32
device-0056,Living Room,10.18
<start>
Device ID: device-0005 | Location: Garden | Reading Value: 48.26
Device ID: device-0019 | Location: Living Room | Reading Value: 51.65
Device ID: device-0007 | Location: Garage | Reading Value: -24.01
Device ID: device-0026 | Location: Office | Reading Value: 67.32
Device ID: device-0056 | Location: Living Room | Reading Value: 10.18
<end>Transform this plain text structure to a MARKDOWN format:
Title: The Final Voyage | Director: Aria Ravenwood | Genre: Fantasy | Release Year: 1986 | Box Office Earnings (M): 772.48
Title: Beyond the Veil | Director: Rylan Frostblade | Genre: Comedy | Release Year: 1989 | Box Office Earnings (M): 476.32
Title: Starbound Odyssey | Director: Rylan Frostblade | Genre: Comedy | Release Year: 1985 | Box Office Earnings (M): 669.77
Title: Mystery of the Depths | Director: Talon Blackthorn | Genre: Adventure | Release Year: 2005 | Box Office Earnings (M): 108.64
Title: Escape from Earth | Director: Rylan Frostblade | Genre: Comedy | Release Year: 2005 | Box Office Earnings (M): 529.16
Title: Escape from Earth | Director: Cade Firebrand | Genre: Horror | Release Year: 2019 | Box Office Earnings (M): 165.52
Title: Dreamwalker | Director: Rylan Frostblade | Genre: Sci-Fi | Release Year: 1975 | Box Office Earnings (M): 604.14
<start>
| Title | Director | Genre | Release Year | Box Office Earnings (M) |
| --- | --- | --- | --- | --- |
| The Final Voyage | Aria Ravenwood | Fantasy | 1986 | 772.48 |
| Beyond the Veil | Rylan Frostblade | Comedy | 1989 | 476.32 |
| Starbound Odyssey | Rylan Frostblade | Comedy | 1985 | 669.77 |
| Mystery of the Depths | Talon Blackthorn | Adventure | 2005 | 108.64 |
| Escape from Earth | Rylan Frostblade | Comedy | 2005 | 529.16 |
| Escape from Earth | Cade Firebrand | Horror | 2019 | 165.52 |
| Dreamwalker | Rylan Frostblade | Sci-Fi | 1975 | 604.14 |
<end>Please transform the following Plain text data into Markdown:
Company: TechnoCorp | Date: 2011-02-18 | High Price: 1367.5 | Volume: 7974866
Company: MediaGroup | Date: 2015-05-28 | High Price: 1222.32 | Volume: 2058227
Company: RetailWorld | Date: 2010-01-08 | High Price: 1367.5 | Volume: 6392402
Company: FoodChain | Date: 2011-10-04 | High Price: 1292.49 | Volume: 6498521
Company: AutoMotive | Date: 2023-11-03 | High Price: 1439.96 | Volume: 9945909
Company: RetailWorld | Date: 2020-11-02 | High Price: 1202.73 | Volume: 8588676
Company: AutoMotive | Date: 2020-07-24 | High Price: 1281.21 | Volume: 6909994
Company: HealthGen | Date: 2019-10-10 | High Price: 986.18 | Volume: 9685028
<start>
| Company | Date | High Price | Volume |
| --- | --- | --- | --- |
| TechnoCorp | 2011-02-18 | 1367.5 | 7974866 |
| MediaGroup | 2015-05-28 | 1222.32 | 2058227 |
| RetailWorld | 2010-01-08 | 1367.5 | 6392402 |
| FoodChain | 2011-10-04 | 1292.49 | 6498521 |
| AutoMotive | 2023-11-03 | 1439.96 | 9945909 |
| RetailWorld | 2020-11-02 | 1202.73 | 8588676 |
| AutoMotive | 2020-07-24 | 1281.21 | 6909994 |
| HealthGen | 2019-10-10 | 986.18 | 9685028 |
<end>Please transform the following Csv data into JSON:
Device ID,Device Type,Location,Battery Level (%),Reading Value,Timestamp
device-0068,Light Sensor,Bathroom,51.3,-0.72,2021-11-05 10:36:01
device-0065,Humidity Sensor,Bathroom,43.6,50.67,2023-01-01 20:29:57
device-0035,Pressure Sensor,Bathroom,80.4,50.31,2023-03-06 01:06:41
device-0054,Light Sensor,Living Room,34.8,36.62,2023-08-08 13:54:41
device-0054,Motion Detector,Garage,65.8,-28.34,2023-04-19 00:25:44
device-0079,Pressure Sensor,Garden,80.1,-13.18,2022-09-03 02:36:40
device-0043,Humidity Sensor,Kitchen,79.1,-16.67,2023-02-26 01:57:32
<start>
[
    {
        "Device ID": "device-0068",
        "Device Type": "Light Sensor",
        "Location": "Bathroom",
        "Battery Level (%)": 51.3,
        "Reading Value": -0.72,
        "Timestamp": "2021-11-05 10:36:01"
    },
    {
        "Device ID": "device-0065",
        "Device Type": "Humidity Sensor",
        "Location": "Bathroom",
        "Battery Level (%)": 43.6,
        "Reading Value": 50.67,
        "Timestamp": "2023-01-01 20:29:57"
    },
    {
        "Device ID": "device-0035",
        "Device Type": "Pressure Sensor",
        "Location": "Bathroom",
        "Battery Level (%)": 80.4,
        "Reading Value": 50.31,
        "Timestamp": "2023-03-06 01:06:41"
    },
    {
        "Device ID": "device-0054",
        "Device Type": "Light Sensor",
        "Location": "Living Room",
        "Battery Level (%)": 34.8,
        "Reading Value": 36.62,
        "Timestamp": "2023-08-08 13:54:41"
    },
    {
        "Device ID": "device-0054",
        "Device Type": "Motion Detector",
        "Location": "Garage",
        "Battery Level (%)": 65.8,
        "Reading Value": -28.34,
        "Timestamp": "2023-04-19 00:25:44"
    },
    {
        "Device ID": "device-0079",
        "Device Type": "Pressure Sensor",
        "Location": "Garden",
        "Battery Level (%)": 80.1,
        "Reading Value": -13.18,
        "Timestamp": "2022-09-03 02:36:40"
    },
    {
        "Device ID": "device-0043",
        "Device Type": "Humidity Sensor",
        "Location": "Kitchen",
        "Battery Level (%)": 79.1,
        "Reading Value": -16.67,
        "Timestamp": "2023-02-26 01:57:32"
    }
]
<end>Here's some JSON data, can you convert it to PLAIN TEXT?
[
    {
        "Device Type": "Temperature Sensor",
        "Reading Value": 62.57,
        "Timestamp": "2021-03-07 20:05:40"
    },
    {
        "Device Type": "Motion Detector",
        "Reading Value": -18.26,
        "Timestamp": "2022-02-18 16:29:56"
    },
    {
        "Device Type": "Temperature Sensor",
        "Reading Value": 81.16,
        "Timestamp": "2021-10-16 13:45:56"
    },
    {
        "Device Type": "Light Sensor",
        "Reading Value": 38.42,
        "Timestamp": "2023-10-19 11:07:09"
    }
]<start>
Device Type: Temperature Sensor | Reading Value: 62.57 | Timestamp: 2021-03-07 20:05:40
Device Type: Motion Detector | Reading Value: -18.26 | Timestamp: 2022-02-18 16:29:56
Device Type: Temperature Sensor | Reading Value: 81.16 | Timestamp: 2021-10-16 13:45:56
Device Type: Light Sensor | Reading Value: 38.42 | Timestamp: 2023-10-19 11:07:09
<end>Convert this MARKDOWN to JSON:
| Company | Date | Open Price | Close Price | High Price | Low Price | Volume |
| --- | --- | --- | --- | --- | --- | --- |
| AeroSystems | 2022-09-26 | 108.33 | 1433.36 | 1433.36 | 108.33 | 7449710 |
| BioLife | 2013-11-12 | 1142.18 | 966.47 | 1310.08 | 965.01 | 1490849 |
| MediaGroup | 2016-08-11 | 86.97 | 1364.07 | 1364.07 | 86.97 | 9219232 |
| TechnoCorp | 2020-08-19 | 1066.69 | 154.6 | 1367.91 | 154.6 | 112444 |
| AeroSystems | 2019-01-17 | 1342.11 | 372.58 | 1342.11 | 12.15 | 7939351 |
| BioLife | 2016-01-05 | 67.87 | 108.33 | 686.31 | 67.87 | 3570950 |
| RetailWorld | 2013-02-24 | 1145.81 | 525.94 | 1145.81 | 525.94 | 8101513 |
| AutoMotive | 2014-05-06 | 86.97 | 1156.2 | 1156.2 | 86.97 | 6616008 |
| FoodChain | 2018-02-01 | 686.31 | 1474.63 | 1474.63 | 108.41 | 5684951 |<start>
[
    {
        "Company": "AeroSystems",
        "Date": "2022-09-26",
        "Open Price": 108.33,
        "Close Price": 1433.36,
        "High Price": 1433.36,
        "Low Price": 108.33,
        "Volume": 7449710
    },
    {
        "Company": "BioLife",
        "Date": "2013-11-12",
        "Open Price": 1142.18,
        "Close Price": 966.47,
        "High Price": 1310.08,
        "Low Price": 965.01,
        "Volume": 1490849
    },
    {
        "Company": "MediaGroup",
        "Date": "2016-08-11",
        "Open Price": 86.97,
        "Close Price": 1364.07,
        "High Price": 1364.07,
        "Low Price": 86.97,
        "Volume": 9219232
    },
    {
        "Company": "TechnoCorp",
        "Date": "2020-08-19",
        "Open Price": 1066.69,
        "Close Price": 154.6,
        "High Price": 1367.91,
        "Low Price": 154.6,
        "Volume": 112444
    },
    {
        "Company": "AeroSystems",
        "Date": "2019-01-17",
        "Open Price": 1342.11,
        "Close Price": 372.58,
        "High Price": 1342.11,
        "Low Price": 12.15,
        "Volume": 7939351
    },
    {
        "Company": "BioLife",
        "Date": "2016-01-05",
        "Open Price": 67.87,
        "Close Price": 108.33,
        "High Price": 686.31,
        "Low Price": 67.87,
        "Volume": 3570950
    },
    {
        "Company": "RetailWorld",
        "Date": "2013-02-24",
        "Open Price": 1145.81,
        "Close Price": 525.94,
        "High Price": 1145.81,
        "Low Price": 525.94,
        "Volume": 8101513
    },
    {
        "Company": "AutoMotive",
        "Date": "2014-05-06",
        "Open Price": 86.97,
        "Close Price": 1156.2,
        "High Price": 1156.2,
        "Low Price": 86.97,
        "Volume": 6616008
    },
    {
        "Company": "FoodChain",
        "Date": "2018-02-01",
        "Open Price": 686.31,
        "Close Price": 1474.63,
        "High Price": 1474.63,
        "Low Price": 108.41,
        "Volume": 5684951
    }
]
<end>Please transform the following Json data into yml:
[
    {
        "Name": "Trevor",
        "Age": 53,
        "Birth Month": "October",
        "City": "El Paso",
        "Income": 375000
    },
    {
        "Name": "Cecil",
        "Age": 56,
        "Birth Month": "September",
        "City": "Boston",
        "Income": 110000
    },
    {
        "Name": "Michael",
        "Age": 58,
        "Birth Month": "April",
        "City": "Jacksonville",
        "Income": 285000
    },
    {
        "Name": "Kelly",
        "Age": 64,
        "Birth Month": "June",
        "City": "Dallas",
        "Income": 80000
    },
    {
        "Name": "Jocelyn",
        "Age": 64,
        "Birth Month": "November",
        "City": "Milwaukee",
        "Income": 50000
    },
    {
        "Name": "Elizabeth",
        "Age": 41,
        "Birth Month": "August",
        "City": "Los Angeles",
        "Income": 385000
    }
]<start>
- Age: 53
  Birth Month: October
  City: El Paso
  Income: 375000
  Name: Trevor
- Age: 56
  Birth Month: September
  City: Boston
  Income: 110000
  Name: Cecil
- Age: 58
  Birth Month: April
  City: Jacksonville
  Income: 285000
  Name: Michael
- Age: 64
  Birth Month: June
  City: Dallas
  Income: 80000
  Name: Kelly
- Age: 64
  Birth Month: November
  City: Milwaukee
  Income: 50000
  Name: Jocelyn
- Age: 41
  Birth Month: August
  City: Los Angeles
  Income: 385000
  Name: Elizabeth
<end>Convert this Plain text to markdown:
Restaurant Name: BBQ Barn | Rating: 1 | Price Range: $$
Restaurant Name: Pasta Palace | Rating: 5 | Price Range: $$$
Restaurant Name: Curry Corner | Rating: 2 | Price Range: $$
Restaurant Name: BBQ Barn | Rating: 1 | Price Range: $$
Restaurant Name: The Golden Spoon | Rating: 5 | Price Range: $$$$
Restaurant Name: The Golden Spoon | Rating: 4 | Price Range: $$$$$
Restaurant Name: Sushi World | Rating: 1 | Price Range: $
Restaurant Name: The Steakhouse | Rating: 4 | Price Range: $$
<start>
| Restaurant Name | Rating | Price Range |
| --- | --- | --- |
| BBQ Barn | 1 | $$ |
| Pasta Palace | 5 | $$$ |
| Curry Corner | 2 | $$ |
| BBQ Barn | 1 | $$ |
| The Golden Spoon | 5 | $$$$ |
| The Golden Spoon | 4 | $$$$$ |
| Sushi World | 1 | $ |
| The Steakhouse | 4 | $$ |
<end>Please transform the following yaml data into Json:
- Close Price: 1174.37
  Company: AutoMotive
  Date: '2013-01-21'
  High Price: 1174.37
  Low Price: 68.3
  Open Price: 68.3
  Volume: 7772309
- Close Price: 136.22
  Company: MediaGroup
  Date: '2022-04-04'
  High Price: 764.73
  Low Price: 136.22
  Open Price: 764.73
  Volume: 2815653
- Close Price: 68.3
  Company: MediaGroup
  Date: '2011-05-21'
  High Price: 1484.38
  Low Price: 68.3
  Open Price: 445.12
  Volume: 7207898
<start>
[
    {
        "Company": "AutoMotive",
        "Date": "2013-01-21",
        "Open Price": 68.3,
        "Close Price": 1174.37,
        "High Price": 1174.37,
        "Low Price": 68.3,
        "Volume": 7772309
    },
    {
        "Company": "MediaGroup",
        "Date": "2022-04-04",
        "Open Price": 764.73,
        "Close Price": 136.22,
        "High Price": 764.73,
        "Low Price": 136.22,
        "Volume": 2815653
    },
    {
        "Company": "MediaGroup",
        "Date": "2011-05-21",
        "Open Price": 445.12,
        "Close Price": 68.3,
        "High Price": 1484.38,
        "Low Price": 68.3,
        "Volume": 7207898
    }
]
<end>Convert this csv to YML:
Genre,Publication Year
Fantasy,1979
Science Fiction,1999
Non-Fiction,1985
<start>
- Genre: Fantasy
  Publication Year: 1979
- Genre: Science Fiction
  Publication Year: 1999
- Genre: Non-Fiction
  Publication Year: 1985
<end>Transform this markdown structure to a JSON format:
| Trip Name | Start Location | Duration (hours) |
| --- | --- | --- |
| Lakeside Retreat | Los Angeles | 60.5 |
| City Explorer | San Francisco | 38.2 |
| Coast to Coast | Los Angeles | 53.1 |
| Mountain Adventure | Denver | 18.4 |
| Desert Drive | Phoenix | 2.6 |
| City Explorer | Chicago | 29.7 |<start>
[
    {
        "Trip Name": "Lakeside Retreat",
        "Start Location": "Los Angeles",
        "Duration (hours)": 60.5
    },
    {
        "Trip Name": "City Explorer",
        "Start Location": "San Francisco",
        "Duration (hours)": 38.2
    },
    {
        "Trip Name": "Coast to Coast",
        "Start Location": "Los Angeles",
        "Duration (hours)": 53.1
    },
    {
        "Trip Name": "Mountain Adventure",
        "Start Location": "Denver",
        "Duration (hours)": 18.4
    },
    {
        "Trip Name": "Desert Drive",
        "Start Location": "Phoenix",
        "Duration (hours)": 2.6
    },
    {
        "Trip Name": "City Explorer",
        "Start Location": "Chicago",
        "Duration (hours)": 29.7
    }
]
<end>Here's some plain text data, can you convert it to json?
Director: Mara Moonshadow | Genre: Sci-Fi | Box Office Earnings (M): 985.19
Director: Talon Blackthorn | Genre: Horror | Box Office Earnings (M): 412.6
Director: Cade Firebrand | Genre: Sci-Fi | Box Office Earnings (M): 189.18
Director: Aria Ravenwood | Genre: Comedy | Box Office Earnings (M): 493.37
Director: Rylan Frostblade | Genre: Action | Box Office Earnings (M): 927.09
Director: Aria Ravenwood | Genre: Thriller | Box Office Earnings (M): 362.27
<start>
[
    {
        "Director": "Mara Moonshadow",
        "Genre": "Sci-Fi",
        "Box Office Earnings (M)": 985.19
    },
    {
        "Director": "Talon Blackthorn",
        "Genre": "Horror",
        "Box Office Earnings (M)": 412.6
    },
    {
        "Director": "Cade Firebrand",
        "Genre": "Sci-Fi",
        "Box Office Earnings (M)": 189.18
    },
    {
        "Director": "Aria Ravenwood",
        "Genre": "Comedy",
        "Box Office Earnings (M)": 493.37
    },
    {
        "Director": "Rylan Frostblade",
        "Genre": "Action",
        "Box Office Earnings (M)": 927.09
    },
    {
        "Director": "Aria Ravenwood",
        "Genre": "Thriller",
        "Box Office Earnings (M)": 362.27
    }
]
<end>Please transform the following csv data into markdown:
Device ID,Device Type,Location,Battery Level (%),Reading Value
device-0044,Motion Detector,Office,94.8,-19.46
device-0029,Pressure Sensor,Bedroom,38.0,82.38
device-0096,Light Sensor,Garden,28.4,31.0
device-0014,Pressure Sensor,Bathroom,88.8,37.36
device-0028,Temperature Sensor,Bathroom,25.2,-8.03
device-0080,Humidity Sensor,Garage,51.3,6.29
device-0099,Motion Detector,Garden,94.8,23.57
device-0030,Humidity Sensor,Bathroom,10.3,16.0
device-0064,Light Sensor,Garden,72.3,23.27
<start>
| Device ID | Device Type | Location | Battery Level (%) | Reading Value |
| --- | --- | --- | --- | --- |
| device-0044 | Motion Detector | Office | 94.8 | -19.46 |
| device-0029 | Pressure Sensor | Bedroom | 38.0 | 82.38 |
| device-0096 | Light Sensor | Garden | 28.4 | 31.0 |
| device-0014 | Pressure Sensor | Bathroom | 88.8 | 37.36 |
| device-0028 | Temperature Sensor | Bathroom | 25.2 | -8.03 |
| device-0080 | Humidity Sensor | Garage | 51.3 | 6.29 |
| device-0099 | Motion Detector | Garden | 94.8 | 23.57 |
| device-0030 | Humidity Sensor | Bathroom | 10.3 | 16.0 |
| device-0064 | Light Sensor | Garden | 72.3 | 23.27 |
<end>Here's some Markdown data, can you convert it to Json?
| Device Type | Location | Battery Level (%) | Reading Value |
| --- | --- | --- | --- |
| Pressure Sensor | Garden | 84.6 | 84.33 |
| Motion Detector | Garage | 66.0 | 24.88 |
| Pressure Sensor | Garage | 17.9 | 84.49 |
| Motion Detector | Bedroom | 60.4 | -12.08 |
| Temperature Sensor | Kitchen | 76.6 | 46.77 |
| Temperature Sensor | Bathroom | 10.4 | -39.34 |
| Motion Detector | Living Room | 66.9 | 77.72 |<start>
[
    {
        "Device Type": "Pressure Sensor",
        "Location": "Garden",
        "Battery Level (%)": 84.6,
        "Reading Value": 84.33
    },
    {
        "Device Type": "Motion Detector",
        "Location": "Garage",
        "Battery Level (%)": 66.0,
        "Reading Value": 24.88
    },
    {
        "Device Type": "Pressure Sensor",
        "Location": "Garage",
        "Battery Level (%)": 17.9,
        "Reading Value": 84.49
    },
    {
        "Device Type": "Motion Detector",
        "Location": "Bedroom",
        "Battery Level (%)": 60.4,
        "Reading Value": -12.08
    },
    {
        "Device Type": "Temperature Sensor",
        "Location": "Kitchen",
        "Battery Level (%)": 76.6,
        "Reading Value": 46.77
    },
    {
        "Device Type": "Temperature Sensor",
        "Location": "Bathroom",
        "Battery Level (%)": 10.4,
        "Reading Value": -39.34
    },
    {
        "Device Type": "Motion Detector",
        "Location": "Living Room",
        "Battery Level (%)": 66.9,
        "Reading Value": 77.72
    }
]
<end>Convert this json to plain text:
[
    {
        "Temperature (C)": 1.1,
        "Humidity (%)": 83,
        "Wind Speed (km/h)": 9.0
    },
    {
        "Temperature (C)": 1.0,
        "Humidity (%)": 100,
        "Wind Speed (km/h)": 18.5
    },
    {
        "Temperature (C)": -6.1,
        "Humidity (%)": 22,
        "Wind Speed (km/h)": 22.2
    },
    {
        "Temperature (C)": 18.1,
        "Humidity (%)": 84,
        "Wind Speed (km/h)": 7.3
    }
]<start>
Temperature (C): 1.1 | Humidity (%): 83 | Wind Speed (km/h): 9.0
Temperature (C): 1.0 | Humidity (%): 100 | Wind Speed (km/h): 18.5
Temperature (C): -6.1 | Humidity (%): 22 | Wind Speed (km/h): 22.2
Temperature (C): 18.1 | Humidity (%): 84 | Wind Speed (km/h): 7.3
<end>Transform this Json structure to a CSV format:
[
    {
        "Genre": "Horror",
        "Rating": 3.8
    },
    {
        "Genre": "Horror",
        "Rating": 4.6
    },
    {
        "Genre": "Thriller",
        "Rating": 2.9
    },
    {
        "Genre": "Mystery",
        "Rating": 3.4
    },
    {
        "Genre": "Thriller",
        "Rating": 4.4
    },
    {
        "Genre": "Historical",
        "Rating": 3.3
    },
    {
        "Genre": "Non-Fiction",
        "Rating": 1.1
    },
    {
        "Genre": "Non-Fiction",
        "Rating": 3.5
    }
]<start>
Genre,Rating
Horror,3.8
Horror,4.6
Thriller,2.9
Mystery,3.4
Thriller,4.4
Historical,3.3
Non-Fiction,1.1
Non-Fiction,3.5
<end>Please transform the following PLAIN TEXT data into Markdown:
Location: Denver | Condition: Foggy | Wind Speed (km/h): 0.2 | Day: Friday
Location: New York | Condition: Snowy | Wind Speed (km/h): 2.6 | Day: Friday
Location: Seattle | Condition: Foggy | Wind Speed (km/h): 3.1 | Day: Thursday
Location: Los Angeles | Condition: Cloudy | Wind Speed (km/h): 5.5 | Day: Monday
Location: Houston | Condition: Cloudy | Wind Speed (km/h): 28.6 | Day: Tuesday
Location: Chicago | Condition: Stormy | Wind Speed (km/h): 26.2 | Day: Friday
Location: Miami | Condition: Windy | Wind Speed (km/h): 4.7 | Day: Sunday
<start>
| Location | Condition | Wind Speed (km/h) | Day |
| --- | --- | --- | --- |
| Denver | Foggy | 0.2 | Friday |
| New York | Snowy | 2.6 | Friday |
| Seattle | Foggy | 3.1 | Thursday |
| Los Angeles | Cloudy | 5.5 | Monday |
| Houston | Cloudy | 28.6 | Tuesday |
| Chicago | Stormy | 26.2 | Friday |
| Miami | Windy | 4.7 | Sunday |
<end>Can you change this JSON into MARKDOWN?
[
    {
        "Age": 21,
        "City": "Washington",
        "Income": 265000
    },
    {
        "Age": 60,
        "City": "San Antonio",
        "Income": 385000
    },
    {
        "Age": 28,
        "City": "Los Angeles",
        "Income": 60000
    },
    {
        "Age": 66,
        "City": "Chicago",
        "Income": 35000
    },
    {
        "Age": 45,
        "City": "Boston",
        "Income": 440000
    },
    {
        "Age": 59,
        "City": "Fort Worth",
        "Income": 25000
    },
    {
        "Age": 57,
        "City": "Jacksonville",
        "Income": 430000
    },
    {
        "Age": 57,
        "City": "Jacksonville",
        "Income": 235000
    },
    {
        "Age": 57,
        "City": "Columbus",
        "Income": 355000
    },
    {
        "Age": 30,
        "City": "Memphis",
        "Income": 280000
    }
]<start>
| Age | City | Income |
| --- | --- | --- |
| 21 | Washington | 265000 |
| 60 | San Antonio | 385000 |
| 28 | Los Angeles | 60000 |
| 66 | Chicago | 35000 |
| 45 | Boston | 440000 |
| 59 | Fort Worth | 25000 |
| 57 | Jacksonville | 430000 |
| 57 | Jacksonville | 235000 |
| 57 | Columbus | 355000 |
| 30 | Memphis | 280000 |
<end>Please transform the following Yaml data into MARKDOWN:
- Close Price: 375.07
  Company: MediaGroup
  Date: '2018-12-26'
  High Price: 772.57
  Low Price: 375.07
  Volume: 4400821
- Close Price: 1053.6
  Company: HealthGen
  Date: '2012-05-28'
  High Price: 1053.6
  Low Price: 545.91
  Volume: 3853952
- Close Price: 742.74
  Company: BioLife
  Date: '2019-02-05'
  High Price: 1440.91
  Low Price: 192.36
  Volume: 6798511
- Close Price: 1303.93
  Company: GreenEnergy
  Date: '2018-07-15'
  High Price: 1303.93
  Low Price: 227.28
  Volume: 5926921
- Close Price: 1213.87
  Company: AutoMotive
  Date: '2011-09-04'
  High Price: 1455.96
  Low Price: 154.26
  Volume: 767465
- Close Price: 38.61
  Company: AeroSystems
  Date: '2023-03-19'
  High Price: 1412.56
  Low Price: 38.61
  Volume: 8017619
- Close Price: 671.96
  Company: AeroSystems
  Date: '2021-05-16'
  High Price: 671.96
  Low Price: 98.65
  Volume: 1945539
- Close Price: 887.45
  Company: FoodChain
  Date: '2021-04-24'
  High Price: 1263.03
  Low Price: 646.3
  Volume: 3853952
- Close Price: 763.45
  Company: TechnoCorp
  Date: '2010-01-19'
  High Price: 1481.03
  Low Price: 385.62
  Volume: 9540857
<start>
| Company | Date | Close Price | High Price | Low Price | Volume |
| --- | --- | --- | --- | --- | --- |
| MediaGroup | 2018-12-26 | 375.07 | 772.57 | 375.07 | 4400821 |
| HealthGen | 2012-05-28 | 1053.6 | 1053.6 | 545.91 | 3853952 |
| BioLife | 2019-02-05 | 742.74 | 1440.91 | 192.36 | 6798511 |
| GreenEnergy | 2018-07-15 | 1303.93 | 1303.93 | 227.28 | 5926921 |
| AutoMotive | 2011-09-04 | 1213.87 | 1455.96 | 154.26 | 767465 |
| AeroSystems | 2023-03-19 | 38.61 | 1412.56 | 38.61 | 8017619 |
| AeroSystems | 2021-05-16 | 671.96 | 671.96 | 98.65 | 1945539 |
| FoodChain | 2021-04-24 | 887.45 | 1263.03 | 646.3 | 3853952 |
| TechnoCorp | 2010-01-19 | 763.45 | 1481.03 | 385.62 | 9540857 |
<end>Can you change this yaml into json?
- Annual Revenue (B): 284.92
  Company: RetailHub
  Market Cap: Large Cap
  Quarter: Q3
  Stock Price: 925.0
- Annual Revenue (B): 65.79
  Company: TechCorp
  Market Cap: Large Cap
  Quarter: Q1
  Stock Price: 942.12
- Annual Revenue (B): 366.1
  Company: RetailHub
  Market Cap: Large Cap
  Quarter: Q3
  Stock Price: 813.91
<start>
[
    {
        "Company": "RetailHub",
        "Market Cap": "Large Cap",
        "Stock Price": 925.0,
        "Annual Revenue (B)": 284.92,
        "Quarter": "Q3"
    },
    {
        "Company": "TechCorp",
        "Market Cap": "Large Cap",
        "Stock Price": 942.12,
        "Annual Revenue (B)": 65.79,
        "Quarter": "Q1"
    },
    {
        "Company": "RetailHub",
        "Market Cap": "Large Cap",
        "Stock Price": 813.91,
        "Annual Revenue (B)": 366.1,
        "Quarter": "Q3"
    }
]
<end>Can you change this csv into Markdown?
Title,Author,Genre,Publication Year,Rating
Tales of the Brave,Luna Silverleaf,Historical,1966,1.5
Echoes of Eternity,Draven Blackthorn,Non-Fiction,2014,4.0
Legends of the Rift,Luna Silverleaf,Fantasy,1990,1.3
Tales of the Brave,Luna Silverleaf,Romance,1959,3.8
Legends of the Rift,Luna Silverleaf,Romance,1959,2.1
<start>
| Title | Author | Genre | Publication Year | Rating |
| --- | --- | --- | --- | --- |
| Tales of the Brave | Luna Silverleaf | Historical | 1966 | 1.5 |
| Echoes of Eternity | Draven Blackthorn | Non-Fiction | 2014 | 4.0 |
| Legends of the Rift | Luna Silverleaf | Fantasy | 1990 | 1.3 |
| Tales of the Brave | Luna Silverleaf | Romance | 1959 | 3.8 |
| Legends of the Rift | Luna Silverleaf | Romance | 1959 | 2.1 |
<end>Please transform the following markdown data into JSON:
| Cuisine | Location |
| --- | --- |
| Chinese | New York |
| Mexican | San Francisco |
| American | Seattle |
| Mexican | Houston |
| Mexican | San Francisco |
| Mediterranean | San Francisco |
| Chinese | Houston |
| Italian | Miami |<start>
[
    {
        "Cuisine": "Chinese",
        "Location": "New York"
    },
    {
        "Cuisine": "Mexican",
        "Location": "San Francisco"
    },
    {
        "Cuisine": "American",
        "Location": "Seattle"
    },
    {
        "Cuisine": "Mexican",
        "Location": "Houston"
    },
    {
        "Cuisine": "Mexican",
        "Location": "San Francisco"
    },
    {
        "Cuisine": "Mediterranean",
        "Location": "San Francisco"
    },
    {
        "Cuisine": "Chinese",
        "Location": "Houston"
    },
    {
        "Cuisine": "Italian",
        "Location": "Miami"
    }
]
<end>Here's some plain text data, can you convert it to json?
Title: The Crystal Key | Genre: Science Fiction | Publication Year: 2019 | Rating: 3.2
Title: The Forgotten World | Genre: Mystery | Publication Year: 1982 | Rating: 5.0
Title: Echoes of Eternity | Genre: Mystery | Publication Year: 1957 | Rating: 1.7
Title: Echoes of Eternity | Genre: Horror | Publication Year: 1992 | Rating: 1.3
Title: The Crystal Key | Genre: Romance | Publication Year: 1981 | Rating: 1.7
<start>
[
    {
        "Title": "The Crystal Key",
        "Genre": "Science Fiction",
        "Publication Year": 2019,
        "Rating": 3.2
    },
    {
        "Title": "The Forgotten World",
        "Genre": "Mystery",
        "Publication Year": 1982,
        "Rating": 5.0
    },
    {
        "Title": "Echoes of Eternity",
        "Genre": "Mystery",
        "Publication Year": 1957,
        "Rating": 1.7
    },
    {
        "Title": "Echoes of Eternity",
        "Genre": "Horror",
        "Publication Year": 1992,
        "Rating": 1.3
    },
    {
        "Title": "The Crystal Key",
        "Genre": "Romance",
        "Publication Year": 1981,
        "Rating": 1.7
    }
]
<end>Here's some JSON data, can you convert it to MARKDOWN?
[
    {
        "Location": "Los Angeles",
        "Humidity (%)": 73,
        "Wind Speed (km/h)": 17.0
    },
    {
        "Location": "New York",
        "Humidity (%)": 42,
        "Wind Speed (km/h)": 6.9
    },
    {
        "Location": "Seattle",
        "Humidity (%)": 70,
        "Wind Speed (km/h)": 29.8
    },
    {
        "Location": "New York",
        "Humidity (%)": 68,
        "Wind Speed (km/h)": 28.3
    },
    {
        "Location": "Denver",
        "Humidity (%)": 88,
        "Wind Speed (km/h)": 7.1
    }
]<start>
| Location | Humidity (%) | Wind Speed (km/h) |
| --- | --- | --- |
| Los Angeles | 73 | 17.0 |
| New York | 42 | 6.9 |
| Seattle | 70 | 29.8 |
| New York | 68 | 28.3 |
| Denver | 88 | 7.1 |
<end>Transform this Csv structure to a Markdown format:
Title,Director,Genre,Release Year,Box Office Earnings (M)
Beyond the Veil,Orin Shadowalker,Fantasy,1980,628.49
The Endless Horizon,Aria Ravenwood,Drama,1973,177.85
Escape from Earth,Rylan Frostblade,Fantasy,1985,615.5
<start>
| Title | Director | Genre | Release Year | Box Office Earnings (M) |
| --- | --- | --- | --- | --- |
| Beyond the Veil | Orin Shadowalker | Fantasy | 1980 | 628.49 |
| The Endless Horizon | Aria Ravenwood | Drama | 1973 | 177.85 |
| Escape from Earth | Rylan Frostblade | Fantasy | 1985 | 615.5 |
<end>Please transform the following PLAIN TEXT data into YML:
Device ID: device-0016 | Location: Bathroom | Timestamp: 2023-07-19 18:51:06
Device ID: device-0019 | Location: Bathroom | Timestamp: 2021-08-11 13:50:08
Device ID: device-0032 | Location: Garden | Timestamp: 2023-11-06 03:48:10
Device ID: device-0048 | Location: Bedroom | Timestamp: 2023-04-20 05:14:38
Device ID: device-0066 | Location: Office | Timestamp: 2023-08-04 11:18:33
Device ID: device-0079 | Location: Kitchen | Timestamp: 2023-05-25 12:57:44
Device ID: device-0034 | Location: Hallway | Timestamp: 2022-09-03 13:59:28
Device ID: device-0077 | Location: Bedroom | Timestamp: 2021-03-23 22:02:55
Device ID: device-0092 | Location: Garage | Timestamp: 2022-12-15 20:40:04
Device ID: device-0034 | Location: Office | Timestamp: 2023-08-15 06:02:02
<start>
- Device ID: device-0016
  Location: Bathroom
  Timestamp: '2023-07-19 18:51:06'
- Device ID: device-0019
  Location: Bathroom
  Timestamp: '2021-08-11 13:50:08'
- Device ID: device-0032
  Location: Garden
  Timestamp: '2023-11-06 03:48:10'
- Device ID: device-0048
  Location: Bedroom
  Timestamp: '2023-04-20 05:14:38'
- Device ID: device-0066
  Location: Office
  Timestamp: '2023-08-04 11:18:33'
- Device ID: device-0079
  Location: Kitchen
  Timestamp: '2023-05-25 12:57:44'
- Device ID: device-0034
  Location: Hallway
  Timestamp: '2022-09-03 13:59:28'
- Device ID: device-0077
  Location: Bedroom
  Timestamp: '2021-03-23 22:02:55'
- Device ID: device-0092
  Location: Garage
  Timestamp: '2022-12-15 20:40:04'
- Device ID: device-0034
  Location: Office
  Timestamp: '2023-08-15 06:02:02'
<end>Can you change this yml into PLAIN TEXT?
- Condition: Snowy
  Day: Thursday
  Humidity (%): 57
  Location: New York
  Temperature (C): 26.5
  Wind Speed (km/h): 11.9
- Condition: Snowy
  Day: Thursday
  Humidity (%): 38
  Location: Miami
  Temperature (C): 15.0
  Wind Speed (km/h): 21.5
- Condition: Cloudy
  Day: Saturday
  Humidity (%): 56
  Location: New York
  Temperature (C): 20.5
  Wind Speed (km/h): 3.5
- Condition: Sunny
  Day: Tuesday
  Humidity (%): 72
  Location: Phoenix
  Temperature (C): 30.9
  Wind Speed (km/h): 13.0
- Condition: Stormy
  Day: Wednesday
  Humidity (%): 84
  Location: Los Angeles
  Temperature (C): 9.2
  Wind Speed (km/h): 1.3
- Condition: Cloudy
  Day: Sunday
  Humidity (%): 87
  Location: Houston
  Temperature (C): 26.7
  Wind Speed (km/h): 17.0
- Condition: Cloudy
  Day: Wednesday
  Humidity (%): 71
  Location: Miami
  Temperature (C): -7.1
  Wind Speed (km/h): 1.3
- Condition: Foggy
  Day: Friday
  Humidity (%): 45
  Location: Phoenix
  Temperature (C): 0.3
  Wind Speed (km/h): 0.3
- Condition: Snowy
  Day: Saturday
  Humidity (%): 64
  Location: Denver
  Temperature (C): 2.3
  Wind Speed (km/h): 28.4
- Condition: Windy
  Day: Saturday
  Humidity (%): 36
  Location: Phoenix
  Temperature (C): -4.2
  Wind Speed (km/h): 6.0
<start>
Location: New York | Condition: Snowy | Temperature (C): 26.5 | Humidity (%): 57 | Wind Speed (km/h): 11.9 | Day: Thursday
Location: Miami | Condition: Snowy | Temperature (C): 15.0 | Humidity (%): 38 | Wind Speed (km/h): 21.5 | Day: Thursday
Location: New York | Condition: Cloudy | Temperature (C): 20.5 | Humidity (%): 56 | Wind Speed (km/h): 3.5 | Day: Saturday
Location: Phoenix | Condition: Sunny | Temperature (C): 30.9 | Humidity (%): 72 | Wind Speed (km/h): 13.0 | Day: Tuesday
Location: Los Angeles | Condition: Stormy | Temperature (C): 9.2 | Humidity (%): 84 | Wind Speed (km/h): 1.3 | Day: Wednesday
Location: Houston | Condition: Cloudy | Temperature (C): 26.7 | Humidity (%): 87 | Wind Speed (km/h): 17.0 | Day: Sunday
Location: Miami | Condition: Cloudy | Temperature (C): -7.1 | Humidity (%): 71 | Wind Speed (km/h): 1.3 | Day: Wednesday
Location: Phoenix | Condition: Foggy | Temperature (C): 0.3 | Humidity (%): 45 | Wind Speed (km/h): 0.3 | Day: Friday
Location: Denver | Condition: Snowy | Temperature (C): 2.3 | Humidity (%): 64 | Wind Speed (km/h): 28.4 | Day: Saturday
Location: Phoenix | Condition: Windy | Temperature (C): -4.2 | Humidity (%): 36 | Wind Speed (km/h): 6.0 | Day: Saturday
<end>Transform this csv structure to a plain text format:
Location,Condition,Temperature (C),Humidity (%),Wind Speed (km/h),Day
Denver,Cloudy,37.3,61,26.4,Wednesday
Seattle,Cloudy,2.7,67,15.7,Monday
Denver,Cloudy,17.1,99,6.4,Wednesday
Los Angeles,Sunny,2.1,47,28.1,Friday
New York,Rainy,23.1,89,13.6,Friday
<start>
Location: Denver | Condition: Cloudy | Temperature (C): 37.3 | Humidity (%): 61 | Wind Speed (km/h): 26.4 | Day: Wednesday
Location: Seattle | Condition: Cloudy | Temperature (C): 2.7 | Humidity (%): 67 | Wind Speed (km/h): 15.7 | Day: Monday
Location: Denver | Condition: Cloudy | Temperature (C): 17.1 | Humidity (%): 99 | Wind Speed (km/h): 6.4 | Day: Wednesday
Location: Los Angeles | Condition: Sunny | Temperature (C): 2.1 | Humidity (%): 47 | Wind Speed (km/h): 28.1 | Day: Friday
Location: New York | Condition: Rainy | Temperature (C): 23.1 | Humidity (%): 89 | Wind Speed (km/h): 13.6 | Day: Friday
<end>Transform this json structure to a Yml format:
[
    {
        "Stock Price": 859.53,
        "Annual Revenue (B)": 203.27,
        "Quarter": "Q4"
    },
    {
        "Stock Price": 230.1,
        "Annual Revenue (B)": 159.25,
        "Quarter": "Q4"
    },
    {
        "Stock Price": 319.31,
        "Annual Revenue (B)": 302.02,
        "Quarter": "Q3"
    },
    {
        "Stock Price": 291.5,
        "Annual Revenue (B)": 335.64,
        "Quarter": "Q3"
    },
    {
        "Stock Price": 859.53,
        "Annual Revenue (B)": 184.87,
        "Quarter": "Q3"
    },
    {
        "Stock Price": 190.68,
        "Annual Revenue (B)": 167.62,
        "Quarter": "Q3"
    },
    {
        "Stock Price": 374.98,
        "Annual Revenue (B)": 405.79,
        "Quarter": "Q4"
    }
]<start>
- Annual Revenue (B): 203.27
  Quarter: Q4
  Stock Price: 859.53
- Annual Revenue (B): 159.25
  Quarter: Q4
  Stock Price: 230.1
- Annual Revenue (B): 302.02
  Quarter: Q3
  Stock Price: 319.31
- Annual Revenue (B): 335.64
  Quarter: Q3
  Stock Price: 291.5
- Annual Revenue (B): 184.87
  Quarter: Q3
  Stock Price: 859.53
- Annual Revenue (B): 167.62
  Quarter: Q3
  Stock Price: 190.68
- Annual Revenue (B): 405.79
  Quarter: Q4
  Stock Price: 374.98
<end>Convert this MARKDOWN to Plain text:
| Name | Age | Birth Month | City | Income |
| --- | --- | --- | --- | --- |
| King | 65 | May | New York | 420000 |
| Erica | 27 | September | Columbus | 265000 |
| Effie | 64 | May | Jacksonville | 25000 |
| Cesar | 20 | March | Nashville | 230000 |
| Nell | 52 | August | San Diego | 70000 |
| Cory | 49 | January | Los Angeles | 295000 |<start>
Name: King | Age: 65 | Birth Month: May | City: New York | Income: 420000
Name: Erica | Age: 27 | Birth Month: September | City: Columbus | Income: 265000
Name: Effie | Age: 64 | Birth Month: May | City: Jacksonville | Income: 25000
Name: Cesar | Age: 20 | Birth Month: March | City: Nashville | Income: 230000
Name: Nell | Age: 52 | Birth Month: August | City: San Diego | Income: 70000
Name: Cory | Age: 49 | Birth Month: January | City: Los Angeles | Income: 295000
<end>Convert this Csv to yml:
Trip Name,Start Location,End Location,Distance (miles)
Highway Odyssey,Phoenix,Los Angeles,2755.3
Historic Route,Houston,Phoenix,2080.4
Historic Route,Miami,Houston,1620.6
Canyon Trek,New York,San Francisco,996.4
Forest Journey,Houston,Miami,1925.5
Forest Journey,Chicago,Los Angeles,2484.3
Lakeside Retreat,Phoenix,Los Angeles,2390.5
City Explorer,Miami,Phoenix,597.0
Canyon Trek,New York,Houston,2649.1
Mountain Adventure,New York,Phoenix,2280.4
<start>
- Distance (miles): 2755.3
  End Location: Los Angeles
  Start Location: Phoenix
  Trip Name: Highway Odyssey
- Distance (miles): 2080.4
  End Location: Phoenix
  Start Location: Houston
  Trip Name: Historic Route
- Distance (miles): 1620.6
  End Location: Houston
  Start Location: Miami
  Trip Name: Historic Route
- Distance (miles): 996.4
  End Location: San Francisco
  Start Location: New York
  Trip Name: Canyon Trek
- Distance (miles): 1925.5
  End Location: Miami
  Start Location: Houston
  Trip Name: Forest Journey
- Distance (miles): 2484.3
  End Location: Los Angeles
  Start Location: Chicago
  Trip Name: Forest Journey
- Distance (miles): 2390.5
  End Location: Los Angeles
  Start Location: Phoenix
  Trip Name: Lakeside Retreat
- Distance (miles): 597.0
  End Location: Phoenix
  Start Location: Miami
  Trip Name: City Explorer
- Distance (miles): 2649.1
  End Location: Houston
  Start Location: New York
  Trip Name: Canyon Trek
- Distance (miles): 2280.4
  End Location: Phoenix
  Start Location: New York
  Trip Name: Mountain Adventure
<end>Transform this Yaml structure to a markdown format:
- Annual Revenue (B): 458.11
  Company: Foodies
  Market Cap: Small Cap
  Quarter: Q4
  Sector: Finance
  Stock Price: 843.85
- Annual Revenue (B): 310.67
  Company: Foodies
  Market Cap: Small Cap
  Quarter: Q2
  Sector: Aerospace
  Stock Price: 651.52
- Annual Revenue (B): 369.2
  Company: TechCorp
  Market Cap: Small Cap
  Quarter: Q3
  Sector: Technology
  Stock Price: 623.73
- Annual Revenue (B): 410.08
  Company: HealthPlus
  Market Cap: Mid Cap
  Quarter: Q1
  Sector: Biotech
  Stock Price: 279.89
- Annual Revenue (B): 114.63
  Company: GlobalTrade
  Market Cap: Small Cap
  Quarter: Q3
  Sector: Energy
  Stock Price: 563.0
- Annual Revenue (B): 138.98
  Company: FinanceWorks
  Market Cap: Mid Cap
  Quarter: Q4
  Sector: Finance
  Stock Price: 466.71
- Annual Revenue (B): 95.43
  Company: GlobalTrade
  Market Cap: Large Cap
  Quarter: Q3
  Sector: Biotech
  Stock Price: 266.46
- Annual Revenue (B): 278.28
  Company: RetailHub
  Market Cap: Mid Cap
  Quarter: Q4
  Sector: Finance
  Stock Price: 466.71
<start>
| Company | Sector | Market Cap | Stock Price | Annual Revenue (B) | Quarter |
| --- | --- | --- | --- | --- | --- |
| Foodies | Finance | Small Cap | 843.85 | 458.11 | Q4 |
| Foodies | Aerospace | Small Cap | 651.52 | 310.67 | Q2 |
| TechCorp | Technology | Small Cap | 623.73 | 369.2 | Q3 |
| HealthPlus | Biotech | Mid Cap | 279.89 | 410.08 | Q1 |
| GlobalTrade | Energy | Small Cap | 563.0 | 114.63 | Q3 |
| FinanceWorks | Finance | Mid Cap | 466.71 | 138.98 | Q4 |
| GlobalTrade | Biotech | Large Cap | 266.46 | 95.43 | Q3 |
| RetailHub | Finance | Mid Cap | 466.71 | 278.28 | Q4 |
<end>Convert this MARKDOWN to YML:
| Birth Month | Income |
| --- | --- |
| January | 440000 |
| May | 390000 |
| December | 115000 |
| November | 100000 |<start>
- Birth Month: January
  Income: 440000
- Birth Month: May
  Income: 390000
- Birth Month: December
  Income: 115000
- Birth Month: November
  Income: 100000
<end>Can you change this csv into markdown?
Birth Month,Income
July,405000
April,455000
December,105000
November,430000
December,355000
October,205000
<start>
| Birth Month | Income |
| --- | --- |
| July | 405000 |
| April | 455000 |
| December | 105000 |
| November | 430000 |
| December | 355000 |
| October | 205000 |
<end>Can you change this markdown into plain text?
| Device ID | Device Type | Battery Level (%) | Reading Value |
| --- | --- | --- | --- |
| device-0049 | Temperature Sensor | 54.1 | 48.16 |
| device-0045 | Humidity Sensor | 22.8 | -13.25 |
| device-0064 | Humidity Sensor | 70.1 | 77.14 |
| device-0002 | Motion Detector | 22.9 | 20.72 |<start>
Device ID: device-0049 | Device Type: Temperature Sensor | Battery Level (%): 54.1 | Reading Value: 48.16
Device ID: device-0045 | Device Type: Humidity Sensor | Battery Level (%): 22.8 | Reading Value: -13.25
Device ID: device-0064 | Device Type: Humidity Sensor | Battery Level (%): 70.1 | Reading Value: 77.14
Device ID: device-0002 | Device Type: Motion Detector | Battery Level (%): 22.9 | Reading Value: 20.72
<end>Convert this csv to markdown:
Title,Author,Genre,Publication Year,Rating
A Journey Through Time,Rowan Ashborne,Horror,2014,4.7
Tales of the Brave,Orion Frostblade,Thriller,1998,1.7
The Silent Grove,Rowan Ashborne,Science Fiction,2023,1.8
<start>
| Title | Author | Genre | Publication Year | Rating |
| --- | --- | --- | --- | --- |
| A Journey Through Time | Rowan Ashborne | Horror | 2014 | 4.7 |
| Tales of the Brave | Orion Frostblade | Thriller | 1998 | 1.7 |
| The Silent Grove | Rowan Ashborne | Science Fiction | 2023 | 1.8 |
<end>Here's some plain text data, can you convert it to csv?
Company: FinanceWorks | Market Cap: Small Cap | Stock Price: 540.54 | Quarter: Q4
Company: EcoEnergy | Market Cap: Small Cap | Stock Price: 702.76 | Quarter: Q4
Company: HealthPlus | Market Cap: Small Cap | Stock Price: 12.83 | Quarter: Q3
Company: AeroSpace | Market Cap: Mega Cap | Stock Price: 903.04 | Quarter: Q3
Company: HealthPlus | Market Cap: Mega Cap | Stock Price: 112.19 | Quarter: Q4
<start>
Company,Market Cap,Stock Price,Quarter
FinanceWorks,Small Cap,540.54,Q4
EcoEnergy,Small Cap,702.76,Q4
HealthPlus,Small Cap,12.83,Q3
AeroSpace,Mega Cap,903.04,Q3
HealthPlus,Mega Cap,112.19,Q4
<end>Transform this markdown structure to a yaml format:
| Trip Name | Start Location | End Location | Distance (miles) | Duration (hours) | Fuel Used (gallons) |
| --- | --- | --- | --- | --- | --- |
| Desert Drive | Houston | Los Angeles | 539.5 | 8.6 | 43.4 |
| Canyon Trek | Denver | Miami | 2167.1 | 2.4 | 73.0 |
| Forest Journey | Los Angeles | Phoenix | 340.7 | 12.5 | 64.3 |
| Valley Voyage | New York | Los Angeles | 2711.1 | 50.2 | 33.3 |
| City Explorer | Los Angeles | Chicago | 924.4 | 13.1 | 75.1 |
| City Explorer | Houston | Los Angeles | 763.8 | 47.7 | 20.1 |
| Historic Route | Phoenix | Chicago | 1124.9 | 18.9 | 52.3 |
| City Explorer | Denver | New York | 948.5 | 8.7 | 27.2 |
| Canyon Trek | Miami | Los Angeles | 1814.2 | 5.2 | 89.1 |
| Highway Odyssey | San Francisco | New York | 2108.5 | 15.1 | 99.5 |<start>
- Distance (miles): 539.5
  Duration (hours): 8.6
  End Location: Los Angeles
  Fuel Used (gallons): 43.4
  Start Location: Houston
  Trip Name: Desert Drive
- Distance (miles): 2167.1
  Duration (hours): 2.4
  End Location: Miami
  Fuel Used (gallons): 73.0
  Start Location: Denver
  Trip Name: Canyon Trek
- Distance (miles): 340.7
  Duration (hours): 12.5
  End Location: Phoenix
  Fuel Used (gallons): 64.3
  Start Location: Los Angeles
  Trip Name: Forest Journey
- Distance (miles): 2711.1
  Duration (hours): 50.2
  End Location: Los Angeles
  Fuel Used (gallons): 33.3
  Start Location: New York
  Trip Name: Valley Voyage
- Distance (miles): 924.4
  Duration (hours): 13.1
  End Location: Chicago
  Fuel Used (gallons): 75.1
  Start Location: Los Angeles
  Trip Name: City Explorer
- Distance (miles): 763.8
  Duration (hours): 47.7
  End Location: Los Angeles
  Fuel Used (gallons): 20.1
  Start Location: Houston
  Trip Name: City Explorer
- Distance (miles): 1124.9
  Duration (hours): 18.9
  End Location: Chicago
  Fuel Used (gallons): 52.3
  Start Location: Phoenix
  Trip Name: Historic Route
- Distance (miles): 948.5
  Duration (hours): 8.7
  End Location: New York
  Fuel Used (gallons): 27.2
  Start Location: Denver
  Trip Name: City Explorer
- Distance (miles): 1814.2
  Duration (hours): 5.2
  End Location: Los Angeles
  Fuel Used (gallons): 89.1
  Start Location: Miami
  Trip Name: Canyon Trek
- Distance (miles): 2108.5
  Duration (hours): 15.1
  End Location: New York
  Fuel Used (gallons): 99.5
  Start Location: San Francisco
  Trip Name: Highway Odyssey
<end>Transform this MARKDOWN structure to a json format:
| Product Name | SKU | Price | Stock Quantity | Category | Supplier Name |
| --- | --- | --- | --- | --- | --- |
| Thingamajig | SKU-1082 | 228.43 | 318 | Toys | Globex |
| Whatchamacallit | SKU-1044 | 217.31 | 251 | Automotive | ACME Corp |
| Doohickey | SKU-1034 | 165.83 | 431 | Electronics | Umbrella Corp |
| Instrument | SKU-1088 | 161.88 | 367 | Electronics | ACME Corp |
| Whatchamacallit | SKU-1064 | 348.2 | 456 | Toys | Globex |
| Contraption | SKU-1096 | 216.37 | 97 | Automotive | ACME Corp |<start>
[
    {
        "Product Name": "Thingamajig",
        "SKU": "SKU-1082",
        "Price": 228.43,
        "Stock Quantity": 318,
        "Category": "Toys",
        "Supplier Name": "Globex"
    },
    {
        "Product Name": "Whatchamacallit",
        "SKU": "SKU-1044",
        "Price": 217.31,
        "Stock Quantity": 251,
        "Category": "Automotive",
        "Supplier Name": "ACME Corp"
    },
    {
        "Product Name": "Doohickey",
        "SKU": "SKU-1034",
        "Price": 165.83,
        "Stock Quantity": 431,
        "Category": "Electronics",
        "Supplier Name": "Umbrella Corp"
    },
    {
        "Product Name": "Instrument",
        "SKU": "SKU-1088",
        "Price": 161.88,
        "Stock Quantity": 367,
        "Category": "Electronics",
        "Supplier Name": "ACME Corp"
    },
    {
        "Product Name": "Whatchamacallit",
        "SKU": "SKU-1064",
        "Price": 348.2,
        "Stock Quantity": 456,
        "Category": "Toys",
        "Supplier Name": "Globex"
    },
    {
        "Product Name": "Contraption",
        "SKU": "SKU-1096",
        "Price": 216.37,
        "Stock Quantity": 97,
        "Category": "Automotive",
        "Supplier Name": "ACME Corp"
    }
]
<end>Here's some PLAIN TEXT data, can you convert it to Markdown?
Trip Name: Coast to Coast | Start Location: Houston | Duration (hours): 22.4
Trip Name: Valley Voyage | Start Location: Denver | Duration (hours): 15.0
Trip Name: Historic Route | Start Location: Denver | Duration (hours): 8.5
<start>
| Trip Name | Start Location | Duration (hours) |
| --- | --- | --- |
| Coast to Coast | Houston | 22.4 |
| Valley Voyage | Denver | 15.0 |
| Historic Route | Denver | 8.5 |
<end>Here's some CSV data, can you convert it to plain text?
Device ID,Location,Battery Level (%),Reading Value,Timestamp
device-0024,Hallway,27.2,-9.65,2023-02-23 13:23:51
device-0025,Hallway,93.8,-36.14,2021-02-08 01:22:24
device-0076,Kitchen,23.3,-30.98,2023-03-10 23:01:50
device-0018,Garage,92.8,-39.22,2023-11-01 16:33:59
device-0036,Living Room,43.2,26.03,2021-08-02 14:06:32
device-0038,Bedroom,18.4,29.17,2023-06-26 03:44:03
device-0035,Living Room,91.0,-34.65,2021-03-01 19:03:27
device-0069,Bathroom,19.3,25.15,2023-08-01 21:05:21
device-0046,Living Room,34.7,-39.41,2022-06-09 10:16:15
<start>
Device ID: device-0024 | Location: Hallway | Battery Level (%): 27.2 | Reading Value: -9.65 | Timestamp: 2023-02-23 13:23:51
Device ID: device-0025 | Location: Hallway | Battery Level (%): 93.8 | Reading Value: -36.14 | Timestamp: 2021-02-08 01:22:24
Device ID: device-0076 | Location: Kitchen | Battery Level (%): 23.3 | Reading Value: -30.98 | Timestamp: 2023-03-10 23:01:50
Device ID: device-0018 | Location: Garage | Battery Level (%): 92.8 | Reading Value: -39.22 | Timestamp: 2023-11-01 16:33:59
Device ID: device-0036 | Location: Living Room | Battery Level (%): 43.2 | Reading Value: 26.03 | Timestamp: 2021-08-02 14:06:32
Device ID: device-0038 | Location: Bedroom | Battery Level (%): 18.4 | Reading Value: 29.17 | Timestamp: 2023-06-26 03:44:03
Device ID: device-0035 | Location: Living Room | Battery Level (%): 91.0 | Reading Value: -34.65 | Timestamp: 2021-03-01 19:03:27
Device ID: device-0069 | Location: Bathroom | Battery Level (%): 19.3 | Reading Value: 25.15 | Timestamp: 2023-08-01 21:05:21
Device ID: device-0046 | Location: Living Room | Battery Level (%): 34.7 | Reading Value: -39.41 | Timestamp: 2022-06-09 10:16:15
<end>Can you change this Csv into json?
Title,Author,Genre,Publication Year,Rating
Legends of the Rift,Kara Firebrand,Fantasy,2021,4.3
The Crystal Key,Kara Firebrand,Science Fiction,1969,2.6
Whispers of the Abyss,Galen Starfire,Science Fiction,1993,3.8
The Last Sky,Elara Moonshadow,Science Fiction,1993,3.1
A Journey Through Time,Thorne Ironwood,Science Fiction,1962,4.2
The Last Sky,Orion Frostblade,Romance,2021,3.1
The Last Sky,Kara Firebrand,Science Fiction,1986,1.1
The Crystal Key,Sylvia Nightshade,Science Fiction,1956,2.3
<start>
[
    {
        "Title": "Legends of the Rift",
        "Author": "Kara Firebrand",
        "Genre": "Fantasy",
        "Publication Year": 2021,
        "Rating": 4.3
    },
    {
        "Title": "The Crystal Key",
        "Author": "Kara Firebrand",
        "Genre": "Science Fiction",
        "Publication Year": 1969,
        "Rating": 2.6
    },
    {
        "Title": "Whispers of the Abyss",
        "Author": "Galen Starfire",
        "Genre": "Science Fiction",
        "Publication Year": 1993,
        "Rating": 3.8
    },
    {
        "Title": "The Last Sky",
        "Author": "Elara Moonshadow",
        "Genre": "Science Fiction",
        "Publication Year": 1993,
        "Rating": 3.1
    },
    {
        "Title": "A Journey Through Time",
        "Author": "Thorne Ironwood",
        "Genre": "Science Fiction",
        "Publication Year": 1962,
        "Rating": 4.2
    },
    {
        "Title": "The Last Sky",
        "Author": "Orion Frostblade",
        "Genre": "Romance",
        "Publication Year": 2021,
        "Rating": 3.1
    },
    {
        "Title": "The Last Sky",
        "Author": "Kara Firebrand",
        "Genre": "Science Fiction",
        "Publication Year": 1986,
        "Rating": 1.1
    },
    {
        "Title": "The Crystal Key",
        "Author": "Sylvia Nightshade",
        "Genre": "Science Fiction",
        "Publication Year": 1956,
        "Rating": 2.3
    }
]
<end>Here's some Yaml data, can you convert it to MARKDOWN?
- Cuisine: French
  Price Range: $
  Rating: 2
  Restaurant Name: BBQ Barn
- Cuisine: Italian
  Price Range: $$$$$
  Rating: 5
  Restaurant Name: Vegan Delight
- Cuisine: French
  Price Range: $$$$$
  Rating: 4
  Restaurant Name: Taco Town
<start>
| Restaurant Name | Cuisine | Rating | Price Range |
| --- | --- | --- | --- |
| BBQ Barn | French | 2 | $ |
| Vegan Delight | Italian | 5 | $$$$$ |
| Taco Town | French | 4 | $$$$$ |
<end>Here's some PLAIN TEXT data, can you convert it to Yaml?
Company: HealthPlus | Sector: Retail | Market Cap: Mega Cap | Stock Price: 309.86 | Quarter: Q2
Company: Foodies | Sector: Energy | Market Cap: Small Cap | Stock Price: 163.07 | Quarter: Q3
Company: TechCorp | Sector: Retail | Market Cap: Small Cap | Stock Price: 955.48 | Quarter: Q1
<start>
- Company: HealthPlus
  Market Cap: Mega Cap
  Quarter: Q2
  Sector: Retail
  Stock Price: 309.86
- Company: Foodies
  Market Cap: Small Cap
  Quarter: Q3
  Sector: Energy
  Stock Price: 163.07
- Company: TechCorp
  Market Cap: Small Cap
  Quarter: Q1
  Sector: Retail
  Stock Price: 955.48
<end>Here's some csv data, can you convert it to Plain text?
Name,Age,City,Income
Virgil,43,Denver,320000
Homer,50,Columbus,465000
Don,19,Columbus,275000
Alan,50,Portland,245000
Justin,61,Jacksonville,55000
Ellie,65,Memphis,280000
Sonia,54,Nashville,115000
Lila,63,Phoenix,365000
Brady,58,Chicago,85000
Wilfred,59,San Antonio,215000
<start>
Name: Virgil | Age: 43 | City: Denver | Income: 320000
Name: Homer | Age: 50 | City: Columbus | Income: 465000
Name: Don | Age: 19 | City: Columbus | Income: 275000
Name: Alan | Age: 50 | City: Portland | Income: 245000
Name: Justin | Age: 61 | City: Jacksonville | Income: 55000
Name: Ellie | Age: 65 | City: Memphis | Income: 280000
Name: Sonia | Age: 54 | City: Nashville | Income: 115000
Name: Lila | Age: 63 | City: Phoenix | Income: 365000
Name: Brady | Age: 58 | City: Chicago | Income: 85000
Name: Wilfred | Age: 59 | City: San Antonio | Income: 215000
<end>Convert this PLAIN TEXT to Markdown:
Restaurant Name: The Steakhouse | Cuisine: Japanese | Rating: 1 | Price Range: $$
Restaurant Name: Curry Corner | Cuisine: French | Rating: 5 | Price Range: $$$$
Restaurant Name: Pasta Palace | Cuisine: French | Rating: 1 | Price Range: $$
<start>
| Restaurant Name | Cuisine | Rating | Price Range |
| --- | --- | --- | --- |
| The Steakhouse | Japanese | 1 | $$ |
| Curry Corner | French | 5 | $$$$ |
| Pasta Palace | French | 1 | $$ |
<end>Transform this yaml structure to a plain text format:
- Price Range: $
  Rating: 3
- Price Range: $$$
  Rating: 3
- Price Range: $
  Rating: 3
- Price Range: $$
  Rating: 5
- Price Range: $$$
  Rating: 4
- Price Range: $$$$$
  Rating: 3
<start>
Rating: 3 | Price Range: $
Rating: 3 | Price Range: $$$
Rating: 3 | Price Range: $
Rating: 5 | Price Range: $$
Rating: 4 | Price Range: $$$
Rating: 3 | Price Range: $$$$$
<end>Can you change this yaml into JSON?
- Age: 62
  Birth Month: September
  Name: Naomi
- Age: 36
  Birth Month: April
  Name: Randy
- Age: 59
  Birth Month: January
  Name: Alejandro
- Age: 66
  Birth Month: December
  Name: Norman
- Age: 38
  Birth Month: December
  Name: Pat
- Age: 63
  Birth Month: June
  Name: Virgil
<start>
[
    {
        "Name": "Naomi",
        "Age": 62,
        "Birth Month": "September"
    },
    {
        "Name": "Randy",
        "Age": 36,
        "Birth Month": "April"
    },
    {
        "Name": "Alejandro",
        "Age": 59,
        "Birth Month": "January"
    },
    {
        "Name": "Norman",
        "Age": 66,
        "Birth Month": "December"
    },
    {
        "Name": "Pat",
        "Age": 38,
        "Birth Month": "December"
    },
    {
        "Name": "Virgil",
        "Age": 63,
        "Birth Month": "June"
    }
]
<end>Transform this yaml structure to a JSON format:
- Distance (miles): 840.3
  End Location: Houston
  Fuel Used (gallons): 29.0
  Start Location: Miami
  Trip Name: Coast to Coast
- Distance (miles): 669.8
  End Location: San Francisco
  Fuel Used (gallons): 94.1
  Start Location: Miami
  Trip Name: Valley Voyage
- Distance (miles): 2945.8
  End Location: Chicago
  Fuel Used (gallons): 38.1
  Start Location: Los Angeles
  Trip Name: Coast to Coast
<start>
[
    {
        "Trip Name": "Coast to Coast",
        "Start Location": "Miami",
        "End Location": "Houston",
        "Distance (miles)": 840.3,
        "Fuel Used (gallons)": 29.0
    },
    {
        "Trip Name": "Valley Voyage",
        "Start Location": "Miami",
        "End Location": "San Francisco",
        "Distance (miles)": 669.8,
        "Fuel Used (gallons)": 94.1
    },
    {
        "Trip Name": "Coast to Coast",
        "Start Location": "Los Angeles",
        "End Location": "Chicago",
        "Distance (miles)": 2945.8,
        "Fuel Used (gallons)": 38.1
    }
]
<end>Convert this plain text to markdown:
Device ID: device-0029 | Device Type: Pressure Sensor | Location: Living Room | Battery Level (%): 64.9 | Reading Value: -15.01 | Timestamp: 2021-12-03 03:08:16
Device ID: device-0098 | Device Type: Temperature Sensor | Location: Office | Battery Level (%): 18.6 | Reading Value: 1.55 | Timestamp: 2023-06-12 04:29:54
Device ID: device-0095 | Device Type: Humidity Sensor | Location: Garage | Battery Level (%): 94.0 | Reading Value: 63.18 | Timestamp: 2021-05-18 14:45:44
Device ID: device-0022 | Device Type: Temperature Sensor | Location: Bathroom | Battery Level (%): 81.6 | Reading Value: -4.03 | Timestamp: 2022-01-28 21:19:30
Device ID: device-0001 | Device Type: Pressure Sensor | Location: Garden | Battery Level (%): 69.1 | Reading Value: -36.51 | Timestamp: 2022-02-08 23:30:45
Device ID: device-0052 | Device Type: Temperature Sensor | Location: Bathroom | Battery Level (%): 74.1 | Reading Value: 52.4 | Timestamp: 2021-04-10 01:46:42
Device ID: device-0003 | Device Type: Motion Detector | Location: Bedroom | Battery Level (%): 74.7 | Reading Value: 27.65 | Timestamp: 2023-01-20 18:51:54
Device ID: device-0036 | Device Type: Pressure Sensor | Location: Garage | Battery Level (%): 70.4 | Reading Value: -35.44 | Timestamp: 2021-01-05 12:05:24
Device ID: device-0005 | Device Type: Temperature Sensor | Location: Office | Battery Level (%): 64.6 | Reading Value: -21.33 | Timestamp: 2022-10-22 10:26:59
<start>
| Device ID | Device Type | Location | Battery Level (%) | Reading Value | Timestamp |
| --- | --- | --- | --- | --- | --- |
| device-0029 | Pressure Sensor | Living Room | 64.9 | -15.01 | 2021-12-03 03:08:16 |
| device-0098 | Temperature Sensor | Office | 18.6 | 1.55 | 2023-06-12 04:29:54 |
| device-0095 | Humidity Sensor | Garage | 94.0 | 63.18 | 2021-05-18 14:45:44 |
| device-0022 | Temperature Sensor | Bathroom | 81.6 | -4.03 | 2022-01-28 21:19:30 |
| device-0001 | Pressure Sensor | Garden | 69.1 | -36.51 | 2022-02-08 23:30:45 |
| device-0052 | Temperature Sensor | Bathroom | 74.1 | 52.4 | 2021-04-10 01:46:42 |
| device-0003 | Motion Detector | Bedroom | 74.7 | 27.65 | 2023-01-20 18:51:54 |
| device-0036 | Pressure Sensor | Garage | 70.4 | -35.44 | 2021-01-05 12:05:24 |
| device-0005 | Temperature Sensor | Office | 64.6 | -21.33 | 2022-10-22 10:26:59 |
<end>Please transform the following json data into PLAIN TEXT:
[
    {
        "Product Name": "Apparatus",
        "SKU": "SKU-1058",
        "Price": 393.79,
        "Stock Quantity": 174,
        "Category": "Electronics"
    },
    {
        "Product Name": "Whatchamacallit",
        "SKU": "SKU-1028",
        "Price": 131.29,
        "Stock Quantity": 397,
        "Category": "Toys"
    },
    {
        "Product Name": "Doohickey",
        "SKU": "SKU-1057",
        "Price": 281.56,
        "Stock Quantity": 85,
        "Category": "Automotive"
    },
    {
        "Product Name": "Whatchamacallit",
        "SKU": "SKU-1065",
        "Price": 106.92,
        "Stock Quantity": 128,
        "Category": "Electronics"
    },
    {
        "Product Name": "Whatchamacallit",
        "SKU": "SKU-1066",
        "Price": 145.6,
        "Stock Quantity": 149,
        "Category": "Automotive"
    },
    {
        "Product Name": "Doohickey",
        "SKU": "SKU-1010",
        "Price": 244.74,
        "Stock Quantity": 499,
        "Category": "Toys"
    }
]<start>
Product Name: Apparatus | SKU: SKU-1058 | Price: 393.79 | Stock Quantity: 174 | Category: Electronics
Product Name: Whatchamacallit | SKU: SKU-1028 | Price: 131.29 | Stock Quantity: 397 | Category: Toys
Product Name: Doohickey | SKU: SKU-1057 | Price: 281.56 | Stock Quantity: 85 | Category: Automotive
Product Name: Whatchamacallit | SKU: SKU-1065 | Price: 106.92 | Stock Quantity: 128 | Category: Electronics
Product Name: Whatchamacallit | SKU: SKU-1066 | Price: 145.6 | Stock Quantity: 149 | Category: Automotive
Product Name: Doohickey | SKU: SKU-1010 | Price: 244.74 | Stock Quantity: 499 | Category: Toys
<end>Can you change this PLAIN TEXT into CSV?
Location: Denver | Condition: Snowy | Temperature (C): 13.5 | Humidity (%): 74 | Wind Speed (km/h): 13.1 | Day: Tuesday
Location: Phoenix | Condition: Stormy | Temperature (C): 11.4 | Humidity (%): 26 | Wind Speed (km/h): 13.1 | Day: Saturday
Location: Phoenix | Condition: Snowy | Temperature (C): 4.3 | Humidity (%): 41 | Wind Speed (km/h): 15.6 | Day: Sunday
<start>
Location,Condition,Temperature (C),Humidity (%),Wind Speed (km/h),Day
Denver,Snowy,13.5,74,13.1,Tuesday
Phoenix,Stormy,11.4,26,13.1,Saturday
Phoenix,Snowy,4.3,41,15.6,Sunday
<end>Can you change this YML into json?
- Database Name: UserDB
  Queries per Second: 621.83
  Timestamp: '2022-09-16 08:41:10'
- Database Name: SalesDB
  Queries per Second: 3587.96
  Timestamp: '2023-07-10 10:27:45'
- Database Name: AnalyticsDB
  Queries per Second: 3645.45
  Timestamp: '2021-07-16 19:23:20'
- Database Name: OrdersDB
  Queries per Second: 4860.28
  Timestamp: '2022-08-06 18:54:15'
- Database Name: ProductsDB
  Queries per Second: 4334.81
  Timestamp: '2023-01-20 12:12:36'
<start>
[
    {
        "Database Name": "UserDB",
        "Queries per Second": 621.83,
        "Timestamp": "2022-09-16 08:41:10"
    },
    {
        "Database Name": "SalesDB",
        "Queries per Second": 3587.96,
        "Timestamp": "2023-07-10 10:27:45"
    },
    {
        "Database Name": "AnalyticsDB",
        "Queries per Second": 3645.45,
        "Timestamp": "2021-07-16 19:23:20"
    },
    {
        "Database Name": "OrdersDB",
        "Queries per Second": 4860.28,
        "Timestamp": "2022-08-06 18:54:15"
    },
    {
        "Database Name": "ProductsDB",
        "Queries per Second": 4334.81,
        "Timestamp": "2023-01-20 12:12:36"
    }
]
<end>Can you change this json into Markdown?
[
    {
        "Market Cap": "Mega Cap",
        "Stock Price": 562.59,
        "Quarter": "Q2"
    },
    {
        "Market Cap": "Mega Cap",
        "Stock Price": 917.02,
        "Quarter": "Q1"
    },
    {
        "Market Cap": "Mega Cap",
        "Stock Price": 672.95,
        "Quarter": "Q4"
    },
    {
        "Market Cap": "Mega Cap",
        "Stock Price": 109.68,
        "Quarter": "Q1"
    },
    {
        "Market Cap": "Mid Cap",
        "Stock Price": 152.16,
        "Quarter": "Q1"
    },
    {
        "Market Cap": "Mega Cap",
        "Stock Price": 763.78,
        "Quarter": "Q1"
    },
    {
        "Market Cap": "Mega Cap",
        "Stock Price": 658.14,
        "Quarter": "Q4"
    }
]<start>
| Market Cap | Stock Price | Quarter |
| --- | --- | --- |
| Mega Cap | 562.59 | Q2 |
| Mega Cap | 917.02 | Q1 |
| Mega Cap | 672.95 | Q4 |
| Mega Cap | 109.68 | Q1 |
| Mid Cap | 152.16 | Q1 |
| Mega Cap | 763.78 | Q1 |
| Mega Cap | 658.14 | Q4 |
<end>Here's some csv data, can you convert it to YAML?
Restaurant Name,Cuisine,Location,Rating,Price Range
The Steakhouse,Japanese,Seattle,1,$$$$
Curry Corner,American,Phoenix,2,$$
Burger Haven,American,San Francisco,1,$
Pizza Planet,Indian,Phoenix,2,$$$$$
Curry Corner,Mexican,Chicago,1,$
BBQ Barn,Mediterranean,Miami,5,$
BBQ Barn,Mediterranean,Los Angeles,1,$$$$$
<start>
- Cuisine: Japanese
  Location: Seattle
  Price Range: $$$$
  Rating: 1
  Restaurant Name: The Steakhouse
- Cuisine: American
  Location: Phoenix
  Price Range: $$
  Rating: 2
  Restaurant Name: Curry Corner
- Cuisine: American
  Location: San Francisco
  Price Range: $
  Rating: 1
  Restaurant Name: Burger Haven
- Cuisine: Indian
  Location: Phoenix
  Price Range: $$$$$
  Rating: 2
  Restaurant Name: Pizza Planet
- Cuisine: Mexican
  Location: Chicago
  Price Range: $
  Rating: 1
  Restaurant Name: Curry Corner
- Cuisine: Mediterranean
  Location: Miami
  Price Range: $
  Rating: 5
  Restaurant Name: BBQ Barn
- Cuisine: Mediterranean
  Location: Los Angeles
  Price Range: $$$$$
  Rating: 1
  Restaurant Name: BBQ Barn
<end>Can you change this markdown into Csv?
| Open Price | High Price | Low Price | Volume |
| --- | --- | --- | --- |
| 1143.29 | 1498.8 | 1024.41 | 4675803 |
| 515.78 | 1375.72 | 462.41 | 4973787 |
| 835.39 | 844.7 | 323.5 | 236085 |
| 1046.78 | 1046.78 | 828.52 | 1038448 |
| 1375.41 | 1375.41 | 347.43 | 3432799 |<start>
Open Price,High Price,Low Price,Volume
1143.29,1498.8,1024.41,4675803
515.78,1375.72,462.41,4973787
835.39,844.7,323.5,236085
1046.78,1046.78,828.52,1038448
1375.41,1375.41,347.43,3432799
<end>Here's some json data, can you convert it to Plain text?
[
    {
        "Title": "The Forgotten World",
        "Author": "Elara Moonshadow",
        "Genre": "Thriller",
        "Publication Year": 1951,
        "Rating": 3.8
    },
    {
        "Title": "Tales of the Brave",
        "Author": "Orion Frostblade",
        "Genre": "Science Fiction",
        "Publication Year": 1981,
        "Rating": 2.9
    },
    {
        "Title": "The Forgotten World",
        "Author": "Isla Windrider",
        "Genre": "Thriller",
        "Publication Year": 2013,
        "Rating": 4.0
    },
    {
        "Title": "The Last Sky",
        "Author": "Orion Frostblade",
        "Genre": "Mystery",
        "Publication Year": 1980,
        "Rating": 2.5
    },
    {
        "Title": "The Crystal Key",
        "Author": "Luna Silverleaf",
        "Genre": "Non-Fiction",
        "Publication Year": 1983,
        "Rating": 3.4
    }
]<start>
Title: The Forgotten World | Author: Elara Moonshadow | Genre: Thriller | Publication Year: 1951 | Rating: 3.8
Title: Tales of the Brave | Author: Orion Frostblade | Genre: Science Fiction | Publication Year: 1981 | Rating: 2.9
Title: The Forgotten World | Author: Isla Windrider | Genre: Thriller | Publication Year: 2013 | Rating: 4.0
Title: The Last Sky | Author: Orion Frostblade | Genre: Mystery | Publication Year: 1980 | Rating: 2.5
Title: The Crystal Key | Author: Luna Silverleaf | Genre: Non-Fiction | Publication Year: 1983 | Rating: 3.4
<end>Please transform the following plain text data into Yaml:
Database Name: LogsDB | Queries per Second: 4198.56 | Cache Hit Ratio (%): 73.03 | Connection Count: 320 | Timestamp: 2022-08-03 01:33:50
Database Name: InventoryDB | Queries per Second: 2718.33 | Cache Hit Ratio (%): 76.77 | Connection Count: 311 | Timestamp: 2021-11-07 16:41:22
Database Name: ProductsDB | Queries per Second: 4181.5 | Cache Hit Ratio (%): 86.34 | Connection Count: 355 | Timestamp: 2021-05-11 01:09:51
Database Name: ProfilesDB | Queries per Second: 2166.22 | Cache Hit Ratio (%): 80.9 | Connection Count: 339 | Timestamp: 2022-03-17 02:27:34
Database Name: AnalyticsDB | Queries per Second: 1355.49 | Cache Hit Ratio (%): 80.75 | Connection Count: 96 | Timestamp: 2022-08-18 09:59:38
Database Name: AnalyticsDB | Queries per Second: 1293.9 | Cache Hit Ratio (%): 82.47 | Connection Count: 256 | Timestamp: 2023-01-20 02:40:50
Database Name: ProductsDB | Queries per Second: 2001.49 | Cache Hit Ratio (%): 86.34 | Connection Count: 44 | Timestamp: 2021-06-08 18:22:22
Database Name: SessionsDB | Queries per Second: 4618.95 | Cache Hit Ratio (%): 95.15 | Connection Count: 94 | Timestamp: 2022-10-08 14:27:38
<start>
- Cache Hit Ratio (%): 73.03
  Connection Count: 320
  Database Name: LogsDB
  Queries per Second: 4198.56
  Timestamp: '2022-08-03 01:33:50'
- Cache Hit Ratio (%): 76.77
  Connection Count: 311
  Database Name: InventoryDB
  Queries per Second: 2718.33
  Timestamp: '2021-11-07 16:41:22'
- Cache Hit Ratio (%): 86.34
  Connection Count: 355
  Database Name: ProductsDB
  Queries per Second: 4181.5
  Timestamp: '2021-05-11 01:09:51'
- Cache Hit Ratio (%): 80.9
  Connection Count: 339
  Database Name: ProfilesDB
  Queries per Second: 2166.22
  Timestamp: '2022-03-17 02:27:34'
- Cache Hit Ratio (%): 80.75
  Connection Count: 96
  Database Name: AnalyticsDB
  Queries per Second: 1355.49
  Timestamp: '2022-08-18 09:59:38'
- Cache Hit Ratio (%): 82.47
  Connection Count: 256
  Database Name: AnalyticsDB
  Queries per Second: 1293.9
  Timestamp: '2023-01-20 02:40:50'
- Cache Hit Ratio (%): 86.34
  Connection Count: 44
  Database Name: ProductsDB
  Queries per Second: 2001.49
  Timestamp: '2021-06-08 18:22:22'
- Cache Hit Ratio (%): 95.15
  Connection Count: 94
  Database Name: SessionsDB
  Queries per Second: 4618.95
  Timestamp: '2022-10-08 14:27:38'
<end>Convert this markdown to CSV:
| Cuisine | Location |
| --- | --- |
| Mediterranean | Los Angeles |
| American | San Francisco |
| Japanese | Seattle |
| Indian | New York |
| Indian | Seattle |
| Mexican | Houston |
| Chinese | New York |<start>
Cuisine,Location
Mediterranean,Los Angeles
American,San Francisco
Japanese,Seattle
Indian,New York
Indian,Seattle
Mexican,Houston
Chinese,New York
<end>Can you change this yaml into CSV?
- Connection Count: 21
  Database Name: MetricsDB
  Queries per Second: 1238.37
  Timestamp: '2021-10-19 23:55:32'
- Connection Count: 325
  Database Name: OrdersDB
  Queries per Second: 975.06
  Timestamp: '2022-10-25 13:27:57'
- Connection Count: 497
  Database Name: ProductsDB
  Queries per Second: 2627.44
  Timestamp: '2022-08-18 02:39:03'
- Connection Count: 358
  Database Name: OrdersDB
  Queries per Second: 1019.59
  Timestamp: '2021-04-21 01:22:49'
- Connection Count: 197
  Database Name: InventoryDB
  Queries per Second: 2231.64
  Timestamp: '2023-04-07 21:30:09'
- Connection Count: 201
  Database Name: OrdersDB
  Queries per Second: 1874.74
  Timestamp: '2021-07-27 08:09:16'
- Connection Count: 164
  Database Name: OrdersDB
  Queries per Second: 4414.38
  Timestamp: '2023-02-14 10:22:38'
- Connection Count: 157
  Database Name: InventoryDB
  Queries per Second: 2901.83
  Timestamp: '2022-11-26 15:20:45'
- Connection Count: 141
  Database Name: InventoryDB
  Queries per Second: 3568.31
  Timestamp: '2023-11-26 11:13:59'
- Connection Count: 390
  Database Name: LogsDB
  Queries per Second: 2113.27
  Timestamp: '2022-09-23 09:16:53'
<start>
Database Name,Queries per Second,Connection Count,Timestamp
MetricsDB,1238.37,21,2021-10-19 23:55:32
OrdersDB,975.06,325,2022-10-25 13:27:57
ProductsDB,2627.44,497,2022-08-18 02:39:03
OrdersDB,1019.59,358,2021-04-21 01:22:49
InventoryDB,2231.64,197,2023-04-07 21:30:09
OrdersDB,1874.74,201,2021-07-27 08:09:16
OrdersDB,4414.38,164,2023-02-14 10:22:38
InventoryDB,2901.83,157,2022-11-26 15:20:45
InventoryDB,3568.31,141,2023-11-26 11:13:59
LogsDB,2113.27,390,2022-09-23 09:16:53
<end>Here's some plain text data, can you convert it to yaml?
Company: HealthPlus | Sector: Retail | Market Cap: Small Cap | Stock Price: 484.39 | Annual Revenue (B): 440.53
Company: TechCorp | Sector: Biotech | Market Cap: Mega Cap | Stock Price: 959.49 | Annual Revenue (B): 87.61
Company: HealthPlus | Sector: Retail | Market Cap: Mid Cap | Stock Price: 921.25 | Annual Revenue (B): 292.88
Company: FinanceWorks | Sector: Energy | Market Cap: Large Cap | Stock Price: 77.73 | Annual Revenue (B): 473.98
<start>
- Annual Revenue (B): 440.53
  Company: HealthPlus
  Market Cap: Small Cap
  Sector: Retail
  Stock Price: 484.39
- Annual Revenue (B): 87.61
  Company: TechCorp
  Market Cap: Mega Cap
  Sector: Biotech
  Stock Price: 959.49
- Annual Revenue (B): 292.88
  Company: HealthPlus
  Market Cap: Mid Cap
  Sector: Retail
  Stock Price: 921.25
- Annual Revenue (B): 473.98
  Company: FinanceWorks
  Market Cap: Large Cap
  Sector: Energy
  Stock Price: 77.73
<end>Please transform the following MARKDOWN data into JSON:
| Company | Sector | Market Cap | Stock Price | Annual Revenue (B) | Quarter |
| --- | --- | --- | --- | --- | --- |
| GlobalTrade | Automotive | Large Cap | 295.52 | 271.2 | Q4 |
| FinanceWorks | Retail | Mid Cap | 651.09 | 440.14 | Q2 |
| Foodies | Biotech | Small Cap | 122.16 | 420.07 | Q3 |
| BioPharm | Automotive | Large Cap | 536.7 | 264.15 | Q4 |
| HealthPlus | Finance | Mid Cap | 852.89 | 335.79 | Q1 |
| AutoDrive | Finance | Mid Cap | 340.68 | 343.4 | Q2 |
| Foodies | Energy | Mega Cap | 974.85 | 440.14 | Q3 |
| EcoEnergy | Retail | Large Cap | 412.17 | 213.44 | Q2 |
| BioPharm | Aerospace | Mid Cap | 241.64 | 412.14 | Q3 |<start>
[
    {
        "Company": "GlobalTrade",
        "Sector": "Automotive",
        "Market Cap": "Large Cap",
        "Stock Price": 295.52,
        "Annual Revenue (B)": 271.2,
        "Quarter": "Q4"
    },
    {
        "Company": "FinanceWorks",
        "Sector": "Retail",
        "Market Cap": "Mid Cap",
        "Stock Price": 651.09,
        "Annual Revenue (B)": 440.14,
        "Quarter": "Q2"
    },
    {
        "Company": "Foodies",
        "Sector": "Biotech",
        "Market Cap": "Small Cap",
        "Stock Price": 122.16,
        "Annual Revenue (B)": 420.07,
        "Quarter": "Q3"
    },
    {
        "Company": "BioPharm",
        "Sector": "Automotive",
        "Market Cap": "Large Cap",
        "Stock Price": 536.7,
        "Annual Revenue (B)": 264.15,
        "Quarter": "Q4"
    },
    {
        "Company": "HealthPlus",
        "Sector": "Finance",
        "Market Cap": "Mid Cap",
        "Stock Price": 852.89,
        "Annual Revenue (B)": 335.79,
        "Quarter": "Q1"
    },
    {
        "Company": "AutoDrive",
        "Sector": "Finance",
        "Market Cap": "Mid Cap",
        "Stock Price": 340.68,
        "Annual Revenue (B)": 343.4,
        "Quarter": "Q2"
    },
    {
        "Company": "Foodies",
        "Sector": "Energy",
        "Market Cap": "Mega Cap",
        "Stock Price": 974.85,
        "Annual Revenue (B)": 440.14,
        "Quarter": "Q3"
    },
    {
        "Company": "EcoEnergy",
        "Sector": "Retail",
        "Market Cap": "Large Cap",
        "Stock Price": 412.17,
        "Annual Revenue (B)": 213.44,
        "Quarter": "Q2"
    },
    {
        "Company": "BioPharm",
        "Sector": "Aerospace",
        "Market Cap": "Mid Cap",
        "Stock Price": 241.64,
        "Annual Revenue (B)": 412.14,
        "Quarter": "Q3"
    }
]
<end>Please transform the following csv data into Yml:
Title,Genre,Publication Year,Rating
The Silent Grove,Historical,2011,4.4
The Crystal Key,Romance,2011,3.8
A Journey Through Time,Non-Fiction,1972,3.8
<start>
- Genre: Historical
  Publication Year: 2011
  Rating: 4.4
  Title: The Silent Grove
- Genre: Romance
  Publication Year: 2011
  Rating: 3.8
  Title: The Crystal Key
- Genre: Non-Fiction
  Publication Year: 1972
  Rating: 3.8
  Title: A Journey Through Time
<end>Convert this plain text to csv:
Database Name: SalesDB | Queries per Second: 4868.63 | Cache Hit Ratio (%): 81.28 | Connection Count: 29 | Average Latency (ms): 1.11 | Timestamp: 2021-10-11 16:44:50
Database Name: SessionsDB | Queries per Second: 4369.31 | Cache Hit Ratio (%): 80.37 | Connection Count: 448 | Average Latency (ms): 34.45 | Timestamp: 2023-06-04 07:48:18
Database Name: OrdersDB | Queries per Second: 1165.46 | Cache Hit Ratio (%): 76.96 | Connection Count: 320 | Average Latency (ms): 88.18 | Timestamp: 2022-09-06 01:20:16
<start>
Database Name,Queries per Second,Cache Hit Ratio (%),Connection Count,Average Latency (ms),Timestamp
SalesDB,4868.63,81.28,29,1.11,2021-10-11 16:44:50
SessionsDB,4369.31,80.37,448,34.45,2023-06-04 07:48:18
OrdersDB,1165.46,76.96,320,88.18,2022-09-06 01:20:16
<end>Can you change this csv into Yaml?
Company,Sector,Annual Revenue (B)
RetailHub,Finance,430.71
TechCorp,Technology,183.98
FinanceWorks,Finance,212.13
<start>
- Annual Revenue (B): 430.71
  Company: RetailHub
  Sector: Finance
- Annual Revenue (B): 183.98
  Company: TechCorp
  Sector: Technology
- Annual Revenue (B): 212.13
  Company: FinanceWorks
  Sector: Finance
<end>Convert this PLAIN TEXT to CSV:
Location: Office | Reading Value: 18.66 | Timestamp: 2022-11-16 14:39:49
Location: Garden | Reading Value: 57.92 | Timestamp: 2023-03-18 00:47:28
Location: Bathroom | Reading Value: -20.24 | Timestamp: 2023-04-13 13:27:34
Location: Garden | Reading Value: 75.15 | Timestamp: 2023-11-25 05:58:29
Location: Kitchen | Reading Value: 29.64 | Timestamp: 2022-03-23 02:58:01
Location: Hallway | Reading Value: 69.38 | Timestamp: 2022-02-04 23:12:50
Location: Living Room | Reading Value: -21.52 | Timestamp: 2022-10-09 17:48:17
Location: Office | Reading Value: 22.49 | Timestamp: 2022-01-14 12:30:58
Location: Garden | Reading Value: 39.58 | Timestamp: 2022-11-15 21:10:22
Location: Garden | Reading Value: 54.46 | Timestamp: 2021-08-01 22:34:29
<start>
Location,Reading Value,Timestamp
Office,18.66,2022-11-16 14:39:49
Garden,57.92,2023-03-18 00:47:28
Bathroom,-20.24,2023-04-13 13:27:34
Garden,75.15,2023-11-25 05:58:29
Kitchen,29.64,2022-03-23 02:58:01
Hallway,69.38,2022-02-04 23:12:50
Living Room,-21.52,2022-10-09 17:48:17
Office,22.49,2022-01-14 12:30:58
Garden,39.58,2022-11-15 21:10:22
Garden,54.46,2021-08-01 22:34:29
<end>Can you change this PLAIN TEXT into YML?
Queries per Second: 2932.36 | Cache Hit Ratio (%): 80.22 | Connection Count: 222 | Average Latency (ms): 74.94
Queries per Second: 1273.06 | Cache Hit Ratio (%): 94.83 | Connection Count: 159 | Average Latency (ms): 48.23
Queries per Second: 3367.16 | Cache Hit Ratio (%): 87.99 | Connection Count: 485 | Average Latency (ms): 76.67
Queries per Second: 958.5 | Cache Hit Ratio (%): 74.15 | Connection Count: 452 | Average Latency (ms): 61.67
Queries per Second: 3051.68 | Cache Hit Ratio (%): 87.7 | Connection Count: 73 | Average Latency (ms): 67.13
Queries per Second: 1321.18 | Cache Hit Ratio (%): 72.08 | Connection Count: 111 | Average Latency (ms): 10.51
Queries per Second: 2656.39 | Cache Hit Ratio (%): 77.3 | Connection Count: 222 | Average Latency (ms): 59.43
Queries per Second: 4408.55 | Cache Hit Ratio (%): 91.9 | Connection Count: 267 | Average Latency (ms): 88.94
<start>
- Average Latency (ms): 74.94
  Cache Hit Ratio (%): 80.22
  Connection Count: 222
  Queries per Second: 2932.36
- Average Latency (ms): 48.23
  Cache Hit Ratio (%): 94.83
  Connection Count: 159
  Queries per Second: 1273.06
- Average Latency (ms): 76.67
  Cache Hit Ratio (%): 87.99
  Connection Count: 485
  Queries per Second: 3367.16
- Average Latency (ms): 61.67
  Cache Hit Ratio (%): 74.15
  Connection Count: 452
  Queries per Second: 958.5
- Average Latency (ms): 67.13
  Cache Hit Ratio (%): 87.7
  Connection Count: 73
  Queries per Second: 3051.68
- Average Latency (ms): 10.51
  Cache Hit Ratio (%): 72.08
  Connection Count: 111
  Queries per Second: 1321.18
- Average Latency (ms): 59.43
  Cache Hit Ratio (%): 77.3
  Connection Count: 222
  Queries per Second: 2656.39
- Average Latency (ms): 88.94
  Cache Hit Ratio (%): 91.9
  Connection Count: 267
  Queries per Second: 4408.55
<end>Convert this csv to Markdown:
Product Name,SKU,Supplier Name
Instrument,SKU-1020,Wonka Industries
Gizmo,SKU-1028,Wayne Enterprises
Apparatus,SKU-1062,Wonka Industries
Whatchamacallit,SKU-1043,Wonka Industries
Gizmo,SKU-1065,Wayne Enterprises
Gizmo,SKU-1002,Wayne Enterprises
Contraption,SKU-1008,Umbrella Corp
Whatchamacallit,SKU-1030,Globex
<start>
| Product Name | SKU | Supplier Name |
| --- | --- | --- |
| Instrument | SKU-1020 | Wonka Industries |
| Gizmo | SKU-1028 | Wayne Enterprises |
| Apparatus | SKU-1062 | Wonka Industries |
| Whatchamacallit | SKU-1043 | Wonka Industries |
| Gizmo | SKU-1065 | Wayne Enterprises |
| Gizmo | SKU-1002 | Wayne Enterprises |
| Contraption | SKU-1008 | Umbrella Corp |
| Whatchamacallit | SKU-1030 | Globex |
<end>Can you change this csv into Json?
Queries per Second,Cache Hit Ratio (%),Connection Count,Average Latency (ms),Timestamp
2970.85,84.33,143,60.48,2021-11-23 21:43:45
3580.58,86.87,17,80.43,2021-06-21 07:45:23
4806.82,86.08,89,37.84,2023-10-07 06:46:58
2809.33,87.96,414,74.37,2023-11-10 09:56:17
1942.29,96.96,352,97.0,2023-05-12 20:08:04
840.18,72.72,125,17.82,2021-02-07 22:29:43
3051.85,96.96,156,25.6,2022-02-22 13:02:40
1707.46,91.87,85,12.35,2022-07-07 07:49:37
2970.85,90.83,21,2.71,2021-02-09 08:59:09
<start>
[
    {
        "Queries per Second": 2970.85,
        "Cache Hit Ratio (%)": 84.33,
        "Connection Count": 143,
        "Average Latency (ms)": 60.48,
        "Timestamp": "2021-11-23 21:43:45"
    },
    {
        "Queries per Second": 3580.58,
        "Cache Hit Ratio (%)": 86.87,
        "Connection Count": 17,
        "Average Latency (ms)": 80.43,
        "Timestamp": "2021-06-21 07:45:23"
    },
    {
        "Queries per Second": 4806.82,
        "Cache Hit Ratio (%)": 86.08,
        "Connection Count": 89,
        "Average Latency (ms)": 37.84,
        "Timestamp": "2023-10-07 06:46:58"
    },
    {
        "Queries per Second": 2809.33,
        "Cache Hit Ratio (%)": 87.96,
        "Connection Count": 414,
        "Average Latency (ms)": 74.37,
        "Timestamp": "2023-11-10 09:56:17"
    },
    {
        "Queries per Second": 1942.29,
        "Cache Hit Ratio (%)": 96.96,
        "Connection Count": 352,
        "Average Latency (ms)": 97.0,
        "Timestamp": "2023-05-12 20:08:04"
    },
    {
        "Queries per Second": 840.18,
        "Cache Hit Ratio (%)": 72.72,
        "Connection Count": 125,
        "Average Latency (ms)": 17.82,
        "Timestamp": "2021-02-07 22:29:43"
    },
    {
        "Queries per Second": 3051.85,
        "Cache Hit Ratio (%)": 96.96,
        "Connection Count": 156,
        "Average Latency (ms)": 25.6,
        "Timestamp": "2022-02-22 13:02:40"
    },
    {
        "Queries per Second": 1707.46,
        "Cache Hit Ratio (%)": 91.87,
        "Connection Count": 85,
        "Average Latency (ms)": 12.35,
        "Timestamp": "2022-07-07 07:49:37"
    },
    {
        "Queries per Second": 2970.85,
        "Cache Hit Ratio (%)": 90.83,
        "Connection Count": 21,
        "Average Latency (ms)": 2.71,
        "Timestamp": "2021-02-09 08:59:09"
    }
]
<end>Can you change this Yaml into Plain text?
- Box Office Earnings (M): 703.49
  Genre: Action
  Release Year: 2022
  Title: Starbound Odyssey
- Box Office Earnings (M): 302.62
  Genre: Horror
  Release Year: 2020
  Title: Beyond the Veil
- Box Office Earnings (M): 735.37
  Genre: Adventure
  Release Year: 2001
  Title: Escape from Earth
- Box Office Earnings (M): 581.12
  Genre: Adventure
  Release Year: 1981
  Title: The Great Expedition
- Box Office Earnings (M): 558.13
  Genre: Horror
  Release Year: 1996
  Title: Starbound Odyssey
<start>
Title: Starbound Odyssey | Genre: Action | Release Year: 2022 | Box Office Earnings (M): 703.49
Title: Beyond the Veil | Genre: Horror | Release Year: 2020 | Box Office Earnings (M): 302.62
Title: Escape from Earth | Genre: Adventure | Release Year: 2001 | Box Office Earnings (M): 735.37
Title: The Great Expedition | Genre: Adventure | Release Year: 1981 | Box Office Earnings (M): 581.12
Title: Starbound Odyssey | Genre: Horror | Release Year: 1996 | Box Office Earnings (M): 558.13
<end>Transform this json structure to a YML format:
[
    {
        "Date": "2013-02-06",
        "High Price": 814.58,
        "Low Price": 267.79,
        "Volume": 9899701
    },
    {
        "Date": "2012-06-28",
        "High Price": 1431.62,
        "Low Price": 932.03,
        "Volume": 3707213
    },
    {
        "Date": "2015-07-02",
        "High Price": 1219.0,
        "Low Price": 504.11,
        "Volume": 3707213
    },
    {
        "Date": "2020-10-06",
        "High Price": 1084.77,
        "Low Price": 808.03,
        "Volume": 588912
    },
    {
        "Date": "2018-12-04",
        "High Price": 1093.62,
        "Low Price": 613.28,
        "Volume": 6715487
    },
    {
        "Date": "2017-02-25",
        "High Price": 1138.25,
        "Low Price": 800.29,
        "Volume": 1168723
    },
    {
        "Date": "2022-12-23",
        "High Price": 1244.33,
        "Low Price": 900.61,
        "Volume": 2073591
    },
    {
        "Date": "2023-02-17",
        "High Price": 1244.33,
        "Low Price": 560.35,
        "Volume": 6378300
    },
    {
        "Date": "2017-07-09",
        "High Price": 1341.82,
        "Low Price": 79.93,
        "Volume": 5471682
    }
]<start>
- Date: '2013-02-06'
  High Price: 814.58
  Low Price: 267.79
  Volume: 9899701
- Date: '2012-06-28'
  High Price: 1431.62
  Low Price: 932.03
  Volume: 3707213
- Date: '2015-07-02'
  High Price: 1219.0
  Low Price: 504.11
  Volume: 3707213
- Date: '2020-10-06'
  High Price: 1084.77
  Low Price: 808.03
  Volume: 588912
- Date: '2018-12-04'
  High Price: 1093.62
  Low Price: 613.28
  Volume: 6715487
- Date: '2017-02-25'
  High Price: 1138.25
  Low Price: 800.29
  Volume: 1168723
- Date: '2022-12-23'
  High Price: 1244.33
  Low Price: 900.61
  Volume: 2073591
- Date: '2023-02-17'
  High Price: 1244.33
  Low Price: 560.35
  Volume: 6378300
- Date: '2017-07-09'
  High Price: 1341.82
  Low Price: 79.93
  Volume: 5471682
<end>Can you change this CSV into MARKDOWN?
Start Location,End Location,Distance (miles),Duration (hours),Fuel Used (gallons)
San Francisco,Chicago,2799.1,7.5,14.4
San Francisco,Chicago,2265.0,52.5,64.1
New York,Chicago,1433.2,2.2,63.5
<start>
| Start Location | End Location | Distance (miles) | Duration (hours) | Fuel Used (gallons) |
| --- | --- | --- | --- | --- |
| San Francisco | Chicago | 2799.1 | 7.5 | 14.4 |
| San Francisco | Chicago | 2265.0 | 52.5 | 64.1 |
| New York | Chicago | 1433.2 | 2.2 | 63.5 |
<end>Transform this plain text structure to a markdown format:
Company: FinanceTrust | Date: 2014-10-26 | Open Price: 567.39 | Close Price: 1280.2 | High Price: 1451.3 | Low Price: 567.39 | Volume: 7712962
Company: TechnoCorp | Date: 2018-01-07 | Open Price: 1457.5 | Close Price: 1453.66 | High Price: 1457.5 | Low Price: 995.25 | Volume: 5732142
Company: MediaGroup | Date: 2022-10-28 | Open Price: 740.99 | Close Price: 297.1 | High Price: 740.99 | Low Price: 297.1 | Volume: 3967129
Company: AutoMotive | Date: 2014-12-10 | Open Price: 995.25 | Close Price: 785.68 | High Price: 1361.19 | Low Price: 300.66 | Volume: 6126274
Company: FoodChain | Date: 2022-01-06 | Open Price: 412.47 | Close Price: 498.17 | High Price: 1138.19 | Low Price: 412.47 | Volume: 7186281
Company: AutoMotive | Date: 2012-08-01 | Open Price: 16.69 | Close Price: 1136.37 | High Price: 1136.37 | Low Price: 16.69 | Volume: 236023
<start>
| Company | Date | Open Price | Close Price | High Price | Low Price | Volume |
| --- | --- | --- | --- | --- | --- | --- |
| FinanceTrust | 2014-10-26 | 567.39 | 1280.2 | 1451.3 | 567.39 | 7712962 |
| TechnoCorp | 2018-01-07 | 1457.5 | 1453.66 | 1457.5 | 995.25 | 5732142 |
| MediaGroup | 2022-10-28 | 740.99 | 297.1 | 740.99 | 297.1 | 3967129 |
| AutoMotive | 2014-12-10 | 995.25 | 785.68 | 1361.19 | 300.66 | 6126274 |
| FoodChain | 2022-01-06 | 412.47 | 498.17 | 1138.19 | 412.47 | 7186281 |
| AutoMotive | 2012-08-01 | 16.69 | 1136.37 | 1136.37 | 16.69 | 236023 |
<end>Transform this MARKDOWN structure to a Csv format:
| Restaurant Name | Location | Price Range |
| --- | --- | --- |
| Sushi World | Seattle | $$$$ |
| Sushi World | Miami | $$$$$ |
| Taco Town | Houston | $ |<start>
Restaurant Name,Location,Price Range
Sushi World,Seattle,$$$$
Sushi World,Miami,$$$$$
Taco Town,Houston,$
<end>