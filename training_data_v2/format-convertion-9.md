Here's some Json data, can you convert it to yml?
[
    {
        "Queries per Second": 4239.84,
        "Cache Hit Ratio (%)": 85.74,
        "Connection Count": 465
    },
    {
        "Queries per Second": 1019.5,
        "Cache Hit Ratio (%)": 80.43,
        "Connection Count": 77
    },
    {
        "Queries per Second": 3459.74,
        "Cache Hit Ratio (%)": 88.76,
        "Connection Count": 154
    },
    {
        "Queries per Second": 1158.37,
        "Cache Hit Ratio (%)": 97.14,
        "Connection Count": 391
    },
    {
        "Queries per Second": 3862.42,
        "Cache Hit Ratio (%)": 85.88,
        "Connection Count": 363
    },
    {
        "Queries per Second": 3459.74,
        "Cache Hit Ratio (%)": 72.38,
        "Connection Count": 113
    }
]<start>
- Cache Hit Ratio (%): 85.74
  Connection Count: 465
  Queries per Second: 4239.84
- Cache Hit Ratio (%): 80.43
  Connection Count: 77
  Queries per Second: 1019.5
- Cache Hit Ratio (%): 88.76
  Connection Count: 154
  Queries per Second: 3459.74
- Cache Hit Ratio (%): 97.14
  Connection Count: 391
  Queries per Second: 1158.37
- Cache Hit Ratio (%): 85.88
  Connection Count: 363
  Queries per Second: 3862.42
- Cache Hit Ratio (%): 72.38
  Connection Count: 113
  Queries per Second: 3459.74
<end>Please transform the following markdown data into json:
| Start Location | Duration (hours) | Fuel Used (gallons) |
| --- | --- | --- |
| Houston | 47.0 | 76.7 |
| New York | 32.7 | 49.7 |
| Los Angeles | 38.7 | 10.8 |
| Chicago | 63.5 | 86.9 |
| Houston | 22.9 | 59.2 |
| San Francisco | 61.1 | 86.7 |
| Houston | 12.4 | 98.7 |
| Los Angeles | 18.6 | 10.5 |
| Miami | 22.9 | 62.3 |
| Los Angeles | 24.1 | 67.5 |<start>
[
    {
        "Start Location": "Houston",
        "Duration (hours)": 47.0,
        "Fuel Used (gallons)": 76.7
    },
    {
        "Start Location": "New York",
        "Duration (hours)": 32.7,
        "Fuel Used (gallons)": 49.7
    },
    {
        "Start Location": "Los Angeles",
        "Duration (hours)": 38.7,
        "Fuel Used (gallons)": 10.8
    },
    {
        "Start Location": "Chicago",
        "Duration (hours)": 63.5,
        "Fuel Used (gallons)": 86.9
    },
    {
        "Start Location": "Houston",
        "Duration (hours)": 22.9,
        "Fuel Used (gallons)": 59.2
    },
    {
        "Start Location": "San Francisco",
        "Duration (hours)": 61.1,
        "Fuel Used (gallons)": 86.7
    },
    {
        "Start Location": "Houston",
        "Duration (hours)": 12.4,
        "Fuel Used (gallons)": 98.7
    },
    {
        "Start Location": "Los Angeles",
        "Duration (hours)": 18.6,
        "Fuel Used (gallons)": 10.5
    },
    {
        "Start Location": "Miami",
        "Duration (hours)": 22.9,
        "Fuel Used (gallons)": 62.3
    },
    {
        "Start Location": "Los Angeles",
        "Duration (hours)": 24.1,
        "Fuel Used (gallons)": 67.5
    }
]
<end>Can you change this JSON into yml?
[
    {
        "End Location": "Chicago",
        "Distance (miles)": 2305.4,
        "Duration (hours)": 40.2
    },
    {
        "End Location": "Miami",
        "Distance (miles)": 2342.5,
        "Duration (hours)": 32.6
    },
    {
        "End Location": "Houston",
        "Distance (miles)": 706.8,
        "Duration (hours)": 14.7
    },
    {
        "End Location": "Chicago",
        "Distance (miles)": 2166.1,
        "Duration (hours)": 58.6
    },
    {
        "End Location": "New York",
        "Distance (miles)": 268.0,
        "Duration (hours)": 56.4
    },
    {
        "End Location": "Phoenix",
        "Distance (miles)": 1271.6,
        "Duration (hours)": 66.4
    },
    {
        "End Location": "Miami",
        "Distance (miles)": 706.8,
        "Duration (hours)": 40.2
    },
    {
        "End Location": "San Francisco",
        "Distance (miles)": 661.6,
        "Duration (hours)": 7.3
    },
    {
        "End Location": "Miami",
        "Distance (miles)": 2667.2,
        "Duration (hours)": 20.3
    },
    {
        "End Location": "Los Angeles",
        "Distance (miles)": 1124.8,
        "Duration (hours)": 44.5
    }
]<start>
- Distance (miles): 2305.4
  Duration (hours): 40.2
  End Location: Chicago
- Distance (miles): 2342.5
  Duration (hours): 32.6
  End Location: Miami
- Distance (miles): 706.8
  Duration (hours): 14.7
  End Location: Houston
- Distance (miles): 2166.1
  Duration (hours): 58.6
  End Location: Chicago
- Distance (miles): 268.0
  Duration (hours): 56.4
  End Location: New York
- Distance (miles): 1271.6
  Duration (hours): 66.4
  End Location: Phoenix
- Distance (miles): 706.8
  Duration (hours): 40.2
  End Location: Miami
- Distance (miles): 661.6
  Duration (hours): 7.3
  End Location: San Francisco
- Distance (miles): 2667.2
  Duration (hours): 20.3
  End Location: Miami
- Distance (miles): 1124.8
  Duration (hours): 44.5
  End Location: Los Angeles
<end>Please transform the following MARKDOWN data into CSV:
| Queries per Second | Cache Hit Ratio (%) | Average Latency (ms) | Timestamp |
| --- | --- | --- | --- |
| 1370.59 | 91.13 | 81.72 | 2022-11-10 14:55:06 |
| 2586.1 | 81.29 | 16.65 | 2023-05-15 02:24:20 |
| 921.0 | 92.75 | 27.16 | 2021-04-12 05:34:12 |
| 1333.92 | 71.25 | 28.29 | 2023-11-26 14:54:18 |
| 1333.92 | 89.48 | 87.43 | 2022-12-24 15:17:42 |
| 2017.48 | 87.72 | 56.97 | 2022-07-02 03:15:49 |
| 2586.1 | 73.78 | 19.99 | 2021-01-05 20:18:04 |
| 4302.18 | 89.3 | 24.57 | 2022-11-10 07:28:41 |
| 2876.55 | 71.71 | 81.72 | 2022-02-24 11:06:32 |
| 2016.97 | 94.07 | 28.11 | 2021-04-02 01:26:35 |<start>
Queries per Second,Cache Hit Ratio (%),Average Latency (ms),Timestamp
1370.59,91.13,81.72,2022-11-10 14:55:06
2586.1,81.29,16.65,2023-05-15 02:24:20
921.0,92.75,27.16,2021-04-12 05:34:12
1333.92,71.25,28.29,2023-11-26 14:54:18
1333.92,89.48,87.43,2022-12-24 15:17:42
2017.48,87.72,56.97,2022-07-02 03:15:49
2586.1,73.78,19.99,2021-01-05 20:18:04
4302.18,89.3,24.57,2022-11-10 07:28:41
2876.55,71.71,81.72,2022-02-24 11:06:32
2016.97,94.07,28.11,2021-04-02 01:26:35
<end>Here's some csv data, can you convert it to Markdown?
Start Location,End Location,Distance (miles),Duration (hours)
Houston,San Francisco,614.8,8.9
Houston,Chicago,1849.2,50.6
Denver,San Francisco,353.5,7.0
Miami,Phoenix,418.1,46.8
Houston,Los Angeles,350.6,36.5
Los Angeles,Denver,685.1,39.5
New York,San Francisco,1330.9,7.6
Miami,Los Angeles,1038.6,12.6
Los Angeles,San Francisco,2373.8,59.7
<start>
| Start Location | End Location | Distance (miles) | Duration (hours) |
| --- | --- | --- | --- |
| Houston | San Francisco | 614.8 | 8.9 |
| Houston | Chicago | 1849.2 | 50.6 |
| Denver | San Francisco | 353.5 | 7.0 |
| Miami | Phoenix | 418.1 | 46.8 |
| Houston | Los Angeles | 350.6 | 36.5 |
| Los Angeles | Denver | 685.1 | 39.5 |
| New York | San Francisco | 1330.9 | 7.6 |
| Miami | Los Angeles | 1038.6 | 12.6 |
| Los Angeles | San Francisco | 2373.8 | 59.7 |
<end>Convert this Csv to json:
Company,Sector,Market Cap,Stock Price,Annual Revenue (B),Quarter
RetailHub,Healthcare,Large Cap,788.91,412.04,Q3
TechCorp,Automotive,Small Cap,97.68,100.03,Q1
FinanceWorks,Technology,Mega Cap,628.95,197.99,Q3
RetailHub,Biotech,Small Cap,731.19,406.5,Q2
<start>
[
    {
        "Company": "RetailHub",
        "Sector": "Healthcare",
        "Market Cap": "Large Cap",
        "Stock Price": 788.91,
        "Annual Revenue (B)": 412.04,
        "Quarter": "Q3"
    },
    {
        "Company": "TechCorp",
        "Sector": "Automotive",
        "Market Cap": "Small Cap",
        "Stock Price": 97.68,
        "Annual Revenue (B)": 100.03,
        "Quarter": "Q1"
    },
    {
        "Company": "FinanceWorks",
        "Sector": "Technology",
        "Market Cap": "Mega Cap",
        "Stock Price": 628.95,
        "Annual Revenue (B)": 197.99,
        "Quarter": "Q3"
    },
    {
        "Company": "RetailHub",
        "Sector": "Biotech",
        "Market Cap": "Small Cap",
        "Stock Price": 731.19,
        "Annual Revenue (B)": 406.5,
        "Quarter": "Q2"
    }
]
<end>Please transform the following markdown data into PLAIN TEXT:
| Company | Sector | Market Cap | Stock Price | Annual Revenue (B) | Quarter |
| --- | --- | --- | --- | --- | --- |
| RetailHub | Aerospace | Mega Cap | 333.13 | 479.35 | Q4 |
| RetailHub | Biotech | Mega Cap | 221.36 | 316.22 | Q3 |
| AutoDrive | Biotech | Large Cap | 10.43 | 201.05 | Q4 |
| AutoDrive | Biotech | Mid Cap | 113.3 | 297.07 | Q1 |
| GlobalTrade | Healthcare | Small Cap | 499.02 | 142.59 | Q2 |
| TechCorp | Retail | Large Cap | 513.3 | 291.4 | Q4 |<start>
Company: RetailHub | Sector: Aerospace | Market Cap: Mega Cap | Stock Price: 333.13 | Annual Revenue (B): 479.35 | Quarter: Q4
Company: RetailHub | Sector: Biotech | Market Cap: Mega Cap | Stock Price: 221.36 | Annual Revenue (B): 316.22 | Quarter: Q3
Company: AutoDrive | Sector: Biotech | Market Cap: Large Cap | Stock Price: 10.43 | Annual Revenue (B): 201.05 | Quarter: Q4
Company: AutoDrive | Sector: Biotech | Market Cap: Mid Cap | Stock Price: 113.3 | Annual Revenue (B): 297.07 | Quarter: Q1
Company: GlobalTrade | Sector: Healthcare | Market Cap: Small Cap | Stock Price: 499.02 | Annual Revenue (B): 142.59 | Quarter: Q2
Company: TechCorp | Sector: Retail | Market Cap: Large Cap | Stock Price: 513.3 | Annual Revenue (B): 291.4 | Quarter: Q4
<end>Here's some Plain text data, can you convert it to Markdown?
Age: 58 | Birth Month: April | City: Portland | Income: 140000
Age: 30 | Birth Month: June | City: New York | Income: 400000
Age: 46 | Birth Month: October | City: Indianapolis | Income: 435000
Age: 23 | Birth Month: October | City: Indianapolis | Income: 335000
<start>
| Age | Birth Month | City | Income |
| --- | --- | --- | --- |
| 58 | April | Portland | 140000 |
| 30 | June | New York | 400000 |
| 46 | October | Indianapolis | 435000 |
| 23 | October | Indianapolis | 335000 |
<end>Please transform the following json data into Plain text:
[
    {
        "Company": "FinanceTrust",
        "Open Price": 206.96,
        "Close Price": 1481.78,
        "High Price": 1481.78
    },
    {
        "Company": "FoodChain",
        "Open Price": 294.25,
        "Close Price": 73.0,
        "High Price": 1375.63
    },
    {
        "Company": "TechnoCorp",
        "Open Price": 827.83,
        "Close Price": 1264.09,
        "High Price": 1264.09
    },
    {
        "Company": "RetailWorld",
        "Open Price": 1301.67,
        "Close Price": 635.86,
        "High Price": 1301.67
    },
    {
        "Company": "TechnoCorp",
        "Open Price": 827.83,
        "Close Price": 1087.54,
        "High Price": 1170.36
    },
    {
        "Company": "FinanceTrust",
        "Open Price": 1073.47,
        "Close Price": 31.21,
        "High Price": 1073.47
    }
]<start>
Company: FinanceTrust | Open Price: 206.96 | Close Price: 1481.78 | High Price: 1481.78
Company: FoodChain | Open Price: 294.25 | Close Price: 73.0 | High Price: 1375.63
Company: TechnoCorp | Open Price: 827.83 | Close Price: 1264.09 | High Price: 1264.09
Company: RetailWorld | Open Price: 1301.67 | Close Price: 635.86 | High Price: 1301.67
Company: TechnoCorp | Open Price: 827.83 | Close Price: 1087.54 | High Price: 1170.36
Company: FinanceTrust | Open Price: 1073.47 | Close Price: 31.21 | High Price: 1073.47
<end>Please transform the following Csv data into MARKDOWN:
Sector,Market Cap,Stock Price,Annual Revenue (B),Quarter
Biotech,Mega Cap,145.19,69.13,Q4
Aerospace,Small Cap,517.83,178.21,Q1
Aerospace,Large Cap,297.35,414.6,Q3
Energy,Large Cap,725.55,186.03,Q1
Aerospace,Mid Cap,662.33,216.89,Q4
Healthcare,Large Cap,486.09,445.43,Q4
Biotech,Small Cap,946.64,110.81,Q4
Technology,Small Cap,361.73,417.42,Q1
Finance,Mega Cap,96.48,492.75,Q4
Biotech,Small Cap,819.81,221.9,Q4
<start>
| Sector | Market Cap | Stock Price | Annual Revenue (B) | Quarter |
| --- | --- | --- | --- | --- |
| Biotech | Mega Cap | 145.19 | 69.13 | Q4 |
| Aerospace | Small Cap | 517.83 | 178.21 | Q1 |
| Aerospace | Large Cap | 297.35 | 414.6 | Q3 |
| Energy | Large Cap | 725.55 | 186.03 | Q1 |
| Aerospace | Mid Cap | 662.33 | 216.89 | Q4 |
| Healthcare | Large Cap | 486.09 | 445.43 | Q4 |
| Biotech | Small Cap | 946.64 | 110.81 | Q4 |
| Technology | Small Cap | 361.73 | 417.42 | Q1 |
| Finance | Mega Cap | 96.48 | 492.75 | Q4 |
| Biotech | Small Cap | 819.81 | 221.9 | Q4 |
<end>Convert this Json to plain text:
[
    {
        "Date": "2016-08-06",
        "Open Price": 220.94,
        "High Price": 991.26,
        "Low Price": 220.94,
        "Volume": 8807915
    },
    {
        "Date": "2016-07-25",
        "Open Price": 327.93,
        "High Price": 405.47,
        "Low Price": 72.57,
        "Volume": 5326219
    },
    {
        "Date": "2017-08-09",
        "Open Price": 186.83,
        "High Price": 843.24,
        "Low Price": 186.83,
        "Volume": 7679648
    }
]<start>
Date: 2016-08-06 | Open Price: 220.94 | High Price: 991.26 | Low Price: 220.94 | Volume: 8807915
Date: 2016-07-25 | Open Price: 327.93 | High Price: 405.47 | Low Price: 72.57 | Volume: 5326219
Date: 2017-08-09 | Open Price: 186.83 | High Price: 843.24 | Low Price: 186.83 | Volume: 7679648
<end>Can you change this YAML into JSON?
- Close Price: 1053.31
  Date: '2013-03-21'
  High Price: 1053.31
  Low Price: 225.76
  Open Price: 225.76
  Volume: 1793642
- Close Price: 1175.17
  Date: '2016-04-10'
  High Price: 1175.17
  Low Price: 245.93
  Open Price: 1175.17
  Volume: 5290341
- Close Price: 389.58
  Date: '2016-08-02'
  High Price: 541.71
  Low Price: 288.86
  Open Price: 541.71
  Volume: 8719023
<start>
[
    {
        "Date": "2013-03-21",
        "Open Price": 225.76,
        "Close Price": 1053.31,
        "High Price": 1053.31,
        "Low Price": 225.76,
        "Volume": 1793642
    },
    {
        "Date": "2016-04-10",
        "Open Price": 1175.17,
        "Close Price": 1175.17,
        "High Price": 1175.17,
        "Low Price": 245.93,
        "Volume": 5290341
    },
    {
        "Date": "2016-08-02",
        "Open Price": 541.71,
        "Close Price": 389.58,
        "High Price": 541.71,
        "Low Price": 288.86,
        "Volume": 8719023
    }
]
<end>Please transform the following Yml data into Csv:
- Cuisine: Japanese
  Rating: 3
  Restaurant Name: Sushi World
- Cuisine: Chinese
  Rating: 5
  Restaurant Name: The Steakhouse
- Cuisine: Indian
  Rating: 5
  Restaurant Name: Sushi World
- Cuisine: French
  Rating: 1
  Restaurant Name: The Golden Spoon
- Cuisine: Japanese
  Rating: 1
  Restaurant Name: The Steakhouse
- Cuisine: Indian
  Rating: 1
  Restaurant Name: Taco Town
- Cuisine: American
  Rating: 2
  Restaurant Name: Pizza Planet
- Cuisine: Indian
  Rating: 3
  Restaurant Name: The Golden Spoon
- Cuisine: Japanese
  Rating: 4
  Restaurant Name: Curry Corner
- Cuisine: Japanese
  Rating: 5
  Restaurant Name: BBQ Barn
<start>
Restaurant Name,Cuisine,Rating
Sushi World,Japanese,3
The Steakhouse,Chinese,5
Sushi World,Indian,5
The Golden Spoon,French,1
The Steakhouse,Japanese,1
Taco Town,Indian,1
Pizza Planet,American,2
The Golden Spoon,Indian,3
Curry Corner,Japanese,4
BBQ Barn,Japanese,5
<end>Can you change this CSV into yaml?
Queries per Second,Cache Hit Ratio (%),Connection Count,Average Latency (ms),Timestamp
1728.84,78.67,410,35.81,2021-06-19 14:24:55
2731.06,73.96,302,63.09,2022-07-17 14:54:47
776.5,72.2,455,40.6,2021-04-11 11:59:08
535.46,93.17,488,44.21,2023-06-28 08:22:48
66.51,78.67,312,36.02,2021-04-10 00:36:15
<start>
- Average Latency (ms): 35.81
  Cache Hit Ratio (%): 78.67
  Connection Count: 410
  Queries per Second: 1728.84
  Timestamp: '2021-06-19 14:24:55'
- Average Latency (ms): 63.09
  Cache Hit Ratio (%): 73.96
  Connection Count: 302
  Queries per Second: 2731.06
  Timestamp: '2022-07-17 14:54:47'
- Average Latency (ms): 40.6
  Cache Hit Ratio (%): 72.2
  Connection Count: 455
  Queries per Second: 776.5
  Timestamp: '2021-04-11 11:59:08'
- Average Latency (ms): 44.21
  Cache Hit Ratio (%): 93.17
  Connection Count: 488
  Queries per Second: 535.46
  Timestamp: '2023-06-28 08:22:48'
- Average Latency (ms): 36.02
  Cache Hit Ratio (%): 78.67
  Connection Count: 312
  Queries per Second: 66.51
  Timestamp: '2021-04-10 00:36:15'
<end>Please transform the following Markdown data into json:
| Title | Author | Genre | Publication Year | Rating |
| --- | --- | --- | --- | --- |
| Shadows of Solitude | Kara Firebrand | Horror | 1957 | 1.3 |
| The Crystal Key | Rowan Ashborne | Romance | 1987 | 2.3 |
| Legends of the Rift | Kara Firebrand | Historical | 2001 | 4.7 |
| Echoes of Eternity | Thorne Ironwood | Romance | 1999 | 2.3 |
| Tales of the Brave | Galen Starfire | Science Fiction | 1974 | 4.8 |
| A Journey Through Time | Galen Starfire | Romance | 2001 | 3.4 |
| Whispers of the Abyss | Rowan Ashborne | Romance | 1966 | 1.4 |
| Echoes of Eternity | Galen Starfire | Science Fiction | 1952 | 3.9 |
| Legends of the Rift | Orion Frostblade | Horror | 1989 | 5.0 |
| The Silent Grove | Isla Windrider | Romance | 1989 | 1.7 |<start>
[
    {
        "Title": "Shadows of Solitude",
        "Author": "Kara Firebrand",
        "Genre": "Horror",
        "Publication Year": 1957,
        "Rating": 1.3
    },
    {
        "Title": "The Crystal Key",
        "Author": "Rowan Ashborne",
        "Genre": "Romance",
        "Publication Year": 1987,
        "Rating": 2.3
    },
    {
        "Title": "Legends of the Rift",
        "Author": "Kara Firebrand",
        "Genre": "Historical",
        "Publication Year": 2001,
        "Rating": 4.7
    },
    {
        "Title": "Echoes of Eternity",
        "Author": "Thorne Ironwood",
        "Genre": "Romance",
        "Publication Year": 1999,
        "Rating": 2.3
    },
    {
        "Title": "Tales of the Brave",
        "Author": "Galen Starfire",
        "Genre": "Science Fiction",
        "Publication Year": 1974,
        "Rating": 4.8
    },
    {
        "Title": "A Journey Through Time",
        "Author": "Galen Starfire",
        "Genre": "Romance",
        "Publication Year": 2001,
        "Rating": 3.4
    },
    {
        "Title": "Whispers of the Abyss",
        "Author": "Rowan Ashborne",
        "Genre": "Romance",
        "Publication Year": 1966,
        "Rating": 1.4
    },
    {
        "Title": "Echoes of Eternity",
        "Author": "Galen Starfire",
        "Genre": "Science Fiction",
        "Publication Year": 1952,
        "Rating": 3.9
    },
    {
        "Title": "Legends of the Rift",
        "Author": "Orion Frostblade",
        "Genre": "Horror",
        "Publication Year": 1989,
        "Rating": 5.0
    },
    {
        "Title": "The Silent Grove",
        "Author": "Isla Windrider",
        "Genre": "Romance",
        "Publication Year": 1989,
        "Rating": 1.7
    }
]
<end>Transform this CSV structure to a markdown format:
Name,Age,Birth Month,Income
Juan,22,December,330000
Gael,33,May,215000
Georgia,56,May,175000
Abel,39,December,355000
Wesley,21,September,130000
Vicky,63,September,370000
Eugene,35,October,380000
Leslie,53,March,355000
Kerri,47,February,110000
Karina,57,February,335000
<start>
| Name | Age | Birth Month | Income |
| --- | --- | --- | --- |
| Juan | 22 | December | 330000 |
| Gael | 33 | May | 215000 |
| Georgia | 56 | May | 175000 |
| Abel | 39 | December | 355000 |
| Wesley | 21 | September | 130000 |
| Vicky | 63 | September | 370000 |
| Eugene | 35 | October | 380000 |
| Leslie | 53 | March | 355000 |
| Kerri | 47 | February | 110000 |
| Karina | 57 | February | 335000 |
<end>Here's some csv data, can you convert it to markdown?
Title,Author
The Forgotten World,Draven Blackthorn
A Journey Through Time,Thorne Ironwood
The Forgotten World,Rowan Ashborne
A Journey Through Time,Thorne Ironwood
Whispers of the Abyss,Rowan Ashborne
The Crystal Key,Galen Starfire
Echoes of Eternity,Kara Firebrand
The Crystal Key,Kara Firebrand
The Forgotten World,Thorne Ironwood
A Journey Through Time,Galen Starfire
<start>
| Title | Author |
| --- | --- |
| The Forgotten World | Draven Blackthorn |
| A Journey Through Time | Thorne Ironwood |
| The Forgotten World | Rowan Ashborne |
| A Journey Through Time | Thorne Ironwood |
| Whispers of the Abyss | Rowan Ashborne |
| The Crystal Key | Galen Starfire |
| Echoes of Eternity | Kara Firebrand |
| The Crystal Key | Kara Firebrand |
| The Forgotten World | Thorne Ironwood |
| A Journey Through Time | Galen Starfire |
<end>Can you change this markdown into Yml?
| Device Type | Battery Level (%) | Reading Value | Timestamp |
| --- | --- | --- | --- |
| Temperature Sensor | 74.9 | 56.44 | 2021-12-27 03:28:18 |
| Pressure Sensor | 99.5 | 27.2 | 2022-04-28 22:46:01 |
| Motion Detector | 40.0 | 1.72 | 2023-09-15 20:54:37 |
| Motion Detector | 76.0 | 59.25 | 2021-12-26 02:53:44 |
| Pressure Sensor | 54.9 | 59.25 | 2023-08-15 08:57:57 |
| Pressure Sensor | 28.7 | 38.1 | 2021-02-07 23:24:36 |
| Temperature Sensor | 93.1 | 49.34 | 2023-04-15 01:11:01 |
| Pressure Sensor | 26.2 | 78.72 | 2022-09-12 16:02:29 |
| Pressure Sensor | 54.0 | 70.57 | 2023-06-03 14:00:11 |<start>
- Battery Level (%): 74.9
  Device Type: Temperature Sensor
  Reading Value: 56.44
  Timestamp: '2021-12-27 03:28:18'
- Battery Level (%): 99.5
  Device Type: Pressure Sensor
  Reading Value: 27.2
  Timestamp: '2022-04-28 22:46:01'
- Battery Level (%): 40.0
  Device Type: Motion Detector
  Reading Value: 1.72
  Timestamp: '2023-09-15 20:54:37'
- Battery Level (%): 76.0
  Device Type: Motion Detector
  Reading Value: 59.25
  Timestamp: '2021-12-26 02:53:44'
- Battery Level (%): 54.9
  Device Type: Pressure Sensor
  Reading Value: 59.25
  Timestamp: '2023-08-15 08:57:57'
- Battery Level (%): 28.7
  Device Type: Pressure Sensor
  Reading Value: 38.1
  Timestamp: '2021-02-07 23:24:36'
- Battery Level (%): 93.1
  Device Type: Temperature Sensor
  Reading Value: 49.34
  Timestamp: '2023-04-15 01:11:01'
- Battery Level (%): 26.2
  Device Type: Pressure Sensor
  Reading Value: 78.72
  Timestamp: '2022-09-12 16:02:29'
- Battery Level (%): 54.0
  Device Type: Pressure Sensor
  Reading Value: 70.57
  Timestamp: '2023-06-03 14:00:11'
<end>Can you change this YAML into PLAIN TEXT?
- Market Cap: Large Cap
  Sector: Healthcare
  Stock Price: 846.24
- Market Cap: Mid Cap
  Sector: Retail
  Stock Price: 458.75
- Market Cap: Small Cap
  Sector: Energy
  Stock Price: 479.8
- Market Cap: Mid Cap
  Sector: Aerospace
  Stock Price: 991.34
- Market Cap: Mid Cap
  Sector: Aerospace
  Stock Price: 408.82
- Market Cap: Mid Cap
  Sector: Healthcare
  Stock Price: 160.35
<start>
Sector: Healthcare | Market Cap: Large Cap | Stock Price: 846.24
Sector: Retail | Market Cap: Mid Cap | Stock Price: 458.75
Sector: Energy | Market Cap: Small Cap | Stock Price: 479.8
Sector: Aerospace | Market Cap: Mid Cap | Stock Price: 991.34
Sector: Aerospace | Market Cap: Mid Cap | Stock Price: 408.82
Sector: Healthcare | Market Cap: Mid Cap | Stock Price: 160.35
<end>Transform this Json structure to a PLAIN TEXT format:
[
    {
        "Product Name": "Widget",
        "SKU": "SKU-1037",
        "Price": 277.13,
        "Stock Quantity": 105
    },
    {
        "Product Name": "Doohickey",
        "SKU": "SKU-1006",
        "Price": 191.89,
        "Stock Quantity": 2
    },
    {
        "Product Name": "Widget",
        "SKU": "SKU-1012",
        "Price": 405.15,
        "Stock Quantity": 357
    },
    {
        "Product Name": "Apparatus",
        "SKU": "SKU-1010",
        "Price": 419.19,
        "Stock Quantity": 292
    }
]<start>
Product Name: Widget | SKU: SKU-1037 | Price: 277.13 | Stock Quantity: 105
Product Name: Doohickey | SKU: SKU-1006 | Price: 191.89 | Stock Quantity: 2
Product Name: Widget | SKU: SKU-1012 | Price: 405.15 | Stock Quantity: 357
Product Name: Apparatus | SKU: SKU-1010 | Price: 419.19 | Stock Quantity: 292
<end>Can you change this CSV into JSON?
Sector,Stock Price,Annual Revenue (B),Quarter
Technology,856.3,486.52,Q3
Technology,719.96,395.85,Q2
Retail,35.65,303.48,Q2
Healthcare,790.94,292.36,Q3
Aerospace,20.6,363.6,Q2
Healthcare,759.14,144.89,Q3
<start>
[
    {
        "Sector": "Technology",
        "Stock Price": 856.3,
        "Annual Revenue (B)": 486.52,
        "Quarter": "Q3"
    },
    {
        "Sector": "Technology",
        "Stock Price": 719.96,
        "Annual Revenue (B)": 395.85,
        "Quarter": "Q2"
    },
    {
        "Sector": "Retail",
        "Stock Price": 35.65,
        "Annual Revenue (B)": 303.48,
        "Quarter": "Q2"
    },
    {
        "Sector": "Healthcare",
        "Stock Price": 790.94,
        "Annual Revenue (B)": 292.36,
        "Quarter": "Q3"
    },
    {
        "Sector": "Aerospace",
        "Stock Price": 20.6,
        "Annual Revenue (B)": 363.6,
        "Quarter": "Q2"
    },
    {
        "Sector": "Healthcare",
        "Stock Price": 759.14,
        "Annual Revenue (B)": 144.89,
        "Quarter": "Q3"
    }
]
<end>Here's some PLAIN TEXT data, can you convert it to MARKDOWN?
Name: Lacey | Age: 30 | Birth Month: November
Name: Claude | Age: 47 | Birth Month: July
Name: Meredith | Age: 27 | Birth Month: March
Name: Cassandra | Age: 23 | Birth Month: July
Name: Homer | Age: 55 | Birth Month: October
Name: Jaxon | Age: 43 | Birth Month: May
Name: Krista | Age: 67 | Birth Month: December
Name: Mayme | Age: 57 | Birth Month: October
Name: Nina | Age: 47 | Birth Month: August
<start>
| Name | Age | Birth Month |
| --- | --- | --- |
| Lacey | 30 | November |
| Claude | 47 | July |
| Meredith | 27 | March |
| Cassandra | 23 | July |
| Homer | 55 | October |
| Jaxon | 43 | May |
| Krista | 67 | December |
| Mayme | 57 | October |
| Nina | 47 | August |
<end>Can you change this Yml into Json?
- Box Office Earnings (M): 92.64
  Director: Orin Shadowalker
  Genre: Drama
  Release Year: 2018
  Title: Dreamwalker
- Box Office Earnings (M): 942.05
  Director: Rylan Frostblade
  Genre: Thriller
  Release Year: 1970
  Title: Escape from Earth
- Box Office Earnings (M): 128.83
  Director: Orin Shadowalker
  Genre: Horror
  Release Year: 1978
  Title: Edge of Infinity
- Box Office Earnings (M): 930.53
  Director: Mara Moonshadow
  Genre: Thriller
  Release Year: 2012
  Title: The Great Expedition
<start>
[
    {
        "Title": "Dreamwalker",
        "Director": "Orin Shadowalker",
        "Genre": "Drama",
        "Release Year": 2018,
        "Box Office Earnings (M)": 92.64
    },
    {
        "Title": "Escape from Earth",
        "Director": "Rylan Frostblade",
        "Genre": "Thriller",
        "Release Year": 1970,
        "Box Office Earnings (M)": 942.05
    },
    {
        "Title": "Edge of Infinity",
        "Director": "Orin Shadowalker",
        "Genre": "Horror",
        "Release Year": 1978,
        "Box Office Earnings (M)": 128.83
    },
    {
        "Title": "The Great Expedition",
        "Director": "Mara Moonshadow",
        "Genre": "Thriller",
        "Release Year": 2012,
        "Box Office Earnings (M)": 930.53
    }
]
<end>Here's some JSON data, can you convert it to Markdown?
[
    {
        "Company": "AeroSystems",
        "High Price": 462.74,
        "Low Price": 57.98,
        "Volume": 3778457
    },
    {
        "Company": "GreenEnergy",
        "High Price": 1342.04,
        "Low Price": 1265.36,
        "Volume": 9320922
    },
    {
        "Company": "AutoMotive",
        "High Price": 950.67,
        "Low Price": 704.05,
        "Volume": 3462512
    },
    {
        "Company": "BioLife",
        "High Price": 337.57,
        "Low Price": 57.98,
        "Volume": 9320922
    },
    {
        "Company": "BioLife",
        "High Price": 1075.81,
        "Low Price": 323.35,
        "Volume": 8811880
    }
]<start>
| Company | High Price | Low Price | Volume |
| --- | --- | --- | --- |
| AeroSystems | 462.74 | 57.98 | 3778457 |
| GreenEnergy | 1342.04 | 1265.36 | 9320922 |
| AutoMotive | 950.67 | 704.05 | 3462512 |
| BioLife | 337.57 | 57.98 | 9320922 |
| BioLife | 1075.81 | 323.35 | 8811880 |
<end>Can you change this yaml into Csv?
- Annual Revenue (B): 361.18
  Company: GlobalTrade
  Market Cap: Mid Cap
  Quarter: Q4
  Sector: Biotech
  Stock Price: 180.8
- Annual Revenue (B): 110.68
  Company: GlobalTrade
  Market Cap: Large Cap
  Quarter: Q3
  Sector: Energy
  Stock Price: 170.86
- Annual Revenue (B): 150.13
  Company: RetailHub
  Market Cap: Mid Cap
  Quarter: Q3
  Sector: Automotive
  Stock Price: 956.75
- Annual Revenue (B): 297.75
  Company: GlobalTrade
  Market Cap: Mega Cap
  Quarter: Q4
  Sector: Technology
  Stock Price: 796.1
- Annual Revenue (B): 101.33
  Company: FinanceWorks
  Market Cap: Mega Cap
  Quarter: Q4
  Sector: Healthcare
  Stock Price: 755.13
- Annual Revenue (B): 209.38
  Company: HealthPlus
  Market Cap: Small Cap
  Quarter: Q4
  Sector: Healthcare
  Stock Price: 459.25
- Annual Revenue (B): 236.69
  Company: AeroSpace
  Market Cap: Mid Cap
  Quarter: Q1
  Sector: Energy
  Stock Price: 512.31
- Annual Revenue (B): 265.73
  Company: EcoEnergy
  Market Cap: Large Cap
  Quarter: Q3
  Sector: Energy
  Stock Price: 337.32
- Annual Revenue (B): 411.29
  Company: Foodies
  Market Cap: Large Cap
  Quarter: Q1
  Sector: Aerospace
  Stock Price: 234.8
- Annual Revenue (B): 79.66
  Company: BioPharm
  Market Cap: Mega Cap
  Quarter: Q2
  Sector: Automotive
  Stock Price: 872.82
<start>
Company,Sector,Market Cap,Stock Price,Annual Revenue (B),Quarter
GlobalTrade,Biotech,Mid Cap,180.8,361.18,Q4
GlobalTrade,Energy,Large Cap,170.86,110.68,Q3
RetailHub,Automotive,Mid Cap,956.75,150.13,Q3
GlobalTrade,Technology,Mega Cap,796.1,297.75,Q4
FinanceWorks,Healthcare,Mega Cap,755.13,101.33,Q4
HealthPlus,Healthcare,Small Cap,459.25,209.38,Q4
AeroSpace,Energy,Mid Cap,512.31,236.69,Q1
EcoEnergy,Energy,Large Cap,337.32,265.73,Q3
Foodies,Aerospace,Large Cap,234.8,411.29,Q1
BioPharm,Automotive,Mega Cap,872.82,79.66,Q2
<end>Can you change this markdown into csv?
| Date | Open Price | Close Price | High Price | Low Price | Volume |
| --- | --- | --- | --- | --- | --- |
| 2022-07-25 | 1312.53 | 1121.3 | 1312.53 | 1020.75 | 7410601 |
| 2017-07-19 | 768.0 | 479.63 | 772.44 | 479.63 | 2525616 |
| 2011-03-12 | 445.02 | 471.4 | 516.75 | 445.02 | 2572212 |
| 2012-04-28 | 1312.53 | 387.26 | 1312.53 | 387.26 | 5587926 |
| 2015-03-10 | 50.21 | 1020.75 | 1020.75 | 50.21 | 2764046 |
| 2015-02-28 | 772.44 | 106.27 | 1215.54 | 106.27 | 324956 |
| 2022-05-16 | 983.74 | 768.0 | 994.72 | 768.0 | 9685579 |
| 2019-06-20 | 336.07 | 76.98 | 1318.63 | 76.98 | 4465568 |
| 2017-02-20 | 492.83 | 1391.42 | 1391.42 | 492.83 | 3601055 |
| 2013-06-12 | 958.45 | 50.21 | 1202.84 | 50.21 | 3236585 |<start>
Date,Open Price,Close Price,High Price,Low Price,Volume
2022-07-25,1312.53,1121.3,1312.53,1020.75,7410601
2017-07-19,768.0,479.63,772.44,479.63,2525616
2011-03-12,445.02,471.4,516.75,445.02,2572212
2012-04-28,1312.53,387.26,1312.53,387.26,5587926
2015-03-10,50.21,1020.75,1020.75,50.21,2764046
2015-02-28,772.44,106.27,1215.54,106.27,324956
2022-05-16,983.74,768.0,994.72,768.0,9685579
2019-06-20,336.07,76.98,1318.63,76.98,4465568
2017-02-20,492.83,1391.42,1391.42,492.83,3601055
2013-06-12,958.45,50.21,1202.84,50.21,3236585
<end>Transform this plain text structure to a Json format:
Database Name: LogsDB | Queries per Second: 964.71 | Cache Hit Ratio (%): 91.56 | Connection Count: 84 | Average Latency (ms): 86.48 | Timestamp: 2023-04-07 05:47:12
Database Name: OrdersDB | Queries per Second: 68.0 | Cache Hit Ratio (%): 85.77 | Connection Count: 414 | Average Latency (ms): 72.79 | Timestamp: 2021-10-04 05:34:44
Database Name: ProductsDB | Queries per Second: 1179.17 | Cache Hit Ratio (%): 81.57 | Connection Count: 159 | Average Latency (ms): 22.63 | Timestamp: 2022-03-16 23:28:26
<start>
[
    {
        "Database Name": "LogsDB",
        "Queries per Second": 964.71,
        "Cache Hit Ratio (%)": 91.56,
        "Connection Count": 84,
        "Average Latency (ms)": 86.48,
        "Timestamp": "2023-04-07 05:47:12"
    },
    {
        "Database Name": "OrdersDB",
        "Queries per Second": 68.0,
        "Cache Hit Ratio (%)": 85.77,
        "Connection Count": 414,
        "Average Latency (ms)": 72.79,
        "Timestamp": "2021-10-04 05:34:44"
    },
    {
        "Database Name": "ProductsDB",
        "Queries per Second": 1179.17,
        "Cache Hit Ratio (%)": 81.57,
        "Connection Count": 159,
        "Average Latency (ms)": 22.63,
        "Timestamp": "2022-03-16 23:28:26"
    }
]
<end>Can you change this plain text into json?
Restaurant Name: Pasta Palace | Cuisine: Chinese | Location: New York | Rating: 3 | Price Range: $$$$$
Restaurant Name: Pizza Planet | Cuisine: Japanese | Location: New York | Rating: 1 | Price Range: $$$
Restaurant Name: Curry Corner | Cuisine: Chinese | Location: Miami | Rating: 1 | Price Range: $$$
Restaurant Name: Curry Corner | Cuisine: Mediterranean | Location: San Francisco | Rating: 2 | Price Range: $$
Restaurant Name: The Golden Spoon | Cuisine: Mexican | Location: Phoenix | Rating: 5 | Price Range: $$
<start>
[
    {
        "Restaurant Name": "Pasta Palace",
        "Cuisine": "Chinese",
        "Location": "New York",
        "Rating": 3,
        "Price Range": "$$$$$"
    },
    {
        "Restaurant Name": "Pizza Planet",
        "Cuisine": "Japanese",
        "Location": "New York",
        "Rating": 1,
        "Price Range": "$$$"
    },
    {
        "Restaurant Name": "Curry Corner",
        "Cuisine": "Chinese",
        "Location": "Miami",
        "Rating": 1,
        "Price Range": "$$$"
    },
    {
        "Restaurant Name": "Curry Corner",
        "Cuisine": "Mediterranean",
        "Location": "San Francisco",
        "Rating": 2,
        "Price Range": "$$"
    },
    {
        "Restaurant Name": "The Golden Spoon",
        "Cuisine": "Mexican",
        "Location": "Phoenix",
        "Rating": 5,
        "Price Range": "$$"
    }
]
<end>Convert this plain text to yml:
Age: 29 | City: Baltimore
Age: 19 | City: Indianapolis
Age: 34 | City: Washington
Age: 48 | City: Austin
Age: 66 | City: San Francisco
Age: 51 | City: Washington
Age: 36 | City: Columbus
Age: 30 | City: Chicago
<start>
- Age: 29
  City: Baltimore
- Age: 19
  City: Indianapolis
- Age: 34
  City: Washington
- Age: 48
  City: Austin
- Age: 66
  City: San Francisco
- Age: 51
  City: Washington
- Age: 36
  City: Columbus
- Age: 30
  City: Chicago
<end>Can you change this yml into Json?
- Market Cap: Small Cap
  Quarter: Q2
  Sector: Biotech
- Market Cap: Small Cap
  Quarter: Q2
  Sector: Biotech
- Market Cap: Small Cap
  Quarter: Q1
  Sector: Energy
<start>
[
    {
        "Sector": "Biotech",
        "Market Cap": "Small Cap",
        "Quarter": "Q2"
    },
    {
        "Sector": "Biotech",
        "Market Cap": "Small Cap",
        "Quarter": "Q2"
    },
    {
        "Sector": "Energy",
        "Market Cap": "Small Cap",
        "Quarter": "Q1"
    }
]
<end>Can you change this csv into PLAIN TEXT?
Company,Date,Close Price,Low Price,Volume
AeroSystems,2017-11-28,823.89,415.77,3002271
AutoMotive,2011-02-05,791.9,791.9,3504239
TechnoCorp,2010-07-15,1183.8,523.11,2616987
MediaGroup,2014-11-18,1373.38,475.12,4896308
RetailWorld,2021-09-12,1392.11,882.11,4368358
AutoMotive,2021-01-03,71.85,71.44,7548718
BioLife,2013-05-16,553.03,81.47,5923052
HealthGen,2017-04-10,1231.54,977.89,4540071
<start>
Company: AeroSystems | Date: 2017-11-28 | Close Price: 823.89 | Low Price: 415.77 | Volume: 3002271
Company: AutoMotive | Date: 2011-02-05 | Close Price: 791.9 | Low Price: 791.9 | Volume: 3504239
Company: TechnoCorp | Date: 2010-07-15 | Close Price: 1183.8 | Low Price: 523.11 | Volume: 2616987
Company: MediaGroup | Date: 2014-11-18 | Close Price: 1373.38 | Low Price: 475.12 | Volume: 4896308
Company: RetailWorld | Date: 2021-09-12 | Close Price: 1392.11 | Low Price: 882.11 | Volume: 4368358
Company: AutoMotive | Date: 2021-01-03 | Close Price: 71.85 | Low Price: 71.44 | Volume: 7548718
Company: BioLife | Date: 2013-05-16 | Close Price: 553.03 | Low Price: 81.47 | Volume: 5923052
Company: HealthGen | Date: 2017-04-10 | Close Price: 1231.54 | Low Price: 977.89 | Volume: 4540071
<end>Here's some Markdown data, can you convert it to plain text?
| Condition | Temperature (C) | Humidity (%) | Wind Speed (km/h) | Day |
| --- | --- | --- | --- | --- |
| Sunny | 39.3 | 62 | 2.6 | Saturday |
| Sunny | 18.3 | 58 | 16.7 | Saturday |
| Rainy | -5.3 | 90 | 8.1 | Monday |
| Rainy | 34.2 | 90 | 7.2 | Sunday |
| Rainy | 6.6 | 79 | 12.6 | Tuesday |
| Snowy | 13.7 | 93 | 27.3 | Wednesday |
| Windy | 10.1 | 33 | 21.2 | Wednesday |
| Rainy | 19.0 | 56 | 29.6 | Wednesday |<start>
Condition: Sunny | Temperature (C): 39.3 | Humidity (%): 62 | Wind Speed (km/h): 2.6 | Day: Saturday
Condition: Sunny | Temperature (C): 18.3 | Humidity (%): 58 | Wind Speed (km/h): 16.7 | Day: Saturday
Condition: Rainy | Temperature (C): -5.3 | Humidity (%): 90 | Wind Speed (km/h): 8.1 | Day: Monday
Condition: Rainy | Temperature (C): 34.2 | Humidity (%): 90 | Wind Speed (km/h): 7.2 | Day: Sunday
Condition: Rainy | Temperature (C): 6.6 | Humidity (%): 79 | Wind Speed (km/h): 12.6 | Day: Tuesday
Condition: Snowy | Temperature (C): 13.7 | Humidity (%): 93 | Wind Speed (km/h): 27.3 | Day: Wednesday
Condition: Windy | Temperature (C): 10.1 | Humidity (%): 33 | Wind Speed (km/h): 21.2 | Day: Wednesday
Condition: Rainy | Temperature (C): 19.0 | Humidity (%): 56 | Wind Speed (km/h): 29.6 | Day: Wednesday
<end>Can you change this YML into Csv?
- Director: Rylan Frostblade
  Genre: Adventure
  Title: Edge of Infinity
- Director: Zara Stormrider
  Genre: Drama
  Title: Starbound Odyssey
- Director: Rylan Frostblade
  Genre: Horror
  Title: Beyond the Veil
- Director: Orin Shadowalker
  Genre: Comedy
  Title: The Final Voyage
- Director: Talon Blackthorn
  Genre: Comedy
  Title: Escape from Earth
- Director: Lira Silverleaf
  Genre: Thriller
  Title: Edge of Infinity
<start>
Title,Director,Genre
Edge of Infinity,Rylan Frostblade,Adventure
Starbound Odyssey,Zara Stormrider,Drama
Beyond the Veil,Rylan Frostblade,Horror
The Final Voyage,Orin Shadowalker,Comedy
Escape from Earth,Talon Blackthorn,Comedy
Edge of Infinity,Lira Silverleaf,Thriller
<end>Transform this Markdown structure to a PLAIN TEXT format:
| Company | Date | Open Price | Close Price | High Price | Low Price | Volume |
| --- | --- | --- | --- | --- | --- | --- |
| MediaGroup | 2014-09-15 | 1364.38 | 1381.43 | 1381.43 | 425.56 | 5470527 |
| HealthGen | 2010-02-20 | 901.56 | 1278.53 | 1278.53 | 901.56 | 1157093 |
| MediaGroup | 2020-01-26 | 1458.56 | 1448.19 | 1458.56 | 1063.04 | 3745734 |<start>
Company: MediaGroup | Date: 2014-09-15 | Open Price: 1364.38 | Close Price: 1381.43 | High Price: 1381.43 | Low Price: 425.56 | Volume: 5470527
Company: HealthGen | Date: 2010-02-20 | Open Price: 901.56 | Close Price: 1278.53 | High Price: 1278.53 | Low Price: 901.56 | Volume: 1157093
Company: MediaGroup | Date: 2020-01-26 | Open Price: 1458.56 | Close Price: 1448.19 | High Price: 1458.56 | Low Price: 1063.04 | Volume: 3745734
<end>Can you change this plain text into json?
Company: RetailHub | Sector: Retail | Market Cap: Mega Cap | Annual Revenue (B): 380.95 | Quarter: Q1
Company: TechCorp | Sector: Technology | Market Cap: Small Cap | Annual Revenue (B): 56.99 | Quarter: Q1
Company: Foodies | Sector: Retail | Market Cap: Mid Cap | Annual Revenue (B): 206.5 | Quarter: Q4
<start>
[
    {
        "Company": "RetailHub",
        "Sector": "Retail",
        "Market Cap": "Mega Cap",
        "Annual Revenue (B)": 380.95,
        "Quarter": "Q1"
    },
    {
        "Company": "TechCorp",
        "Sector": "Technology",
        "Market Cap": "Small Cap",
        "Annual Revenue (B)": 56.99,
        "Quarter": "Q1"
    },
    {
        "Company": "Foodies",
        "Sector": "Retail",
        "Market Cap": "Mid Cap",
        "Annual Revenue (B)": 206.5,
        "Quarter": "Q4"
    }
]
<end>Transform this Plain text structure to a Markdown format:
Location: Denver | Condition: Windy | Temperature (C): 17.8 | Humidity (%): 72 | Wind Speed (km/h): 30.0 | Day: Wednesday
Location: Denver | Condition: Foggy | Temperature (C): 2.8 | Humidity (%): 23 | Wind Speed (km/h): 15.7 | Day: Monday
Location: Seattle | Condition: Cloudy | Temperature (C): 2.5 | Humidity (%): 43 | Wind Speed (km/h): 18.7 | Day: Sunday
Location: Miami | Condition: Snowy | Temperature (C): -0.8 | Humidity (%): 79 | Wind Speed (km/h): 9.4 | Day: Tuesday
Location: Phoenix | Condition: Sunny | Temperature (C): 24.7 | Humidity (%): 56 | Wind Speed (km/h): 26.9 | Day: Thursday
Location: Denver | Condition: Cloudy | Temperature (C): 12.3 | Humidity (%): 30 | Wind Speed (km/h): 28.6 | Day: Monday
Location: Los Angeles | Condition: Stormy | Temperature (C): 18.3 | Humidity (%): 41 | Wind Speed (km/h): 12.5 | Day: Saturday
<start>
| Location | Condition | Temperature (C) | Humidity (%) | Wind Speed (km/h) | Day |
| --- | --- | --- | --- | --- | --- |
| Denver | Windy | 17.8 | 72 | 30.0 | Wednesday |
| Denver | Foggy | 2.8 | 23 | 15.7 | Monday |
| Seattle | Cloudy | 2.5 | 43 | 18.7 | Sunday |
| Miami | Snowy | -0.8 | 79 | 9.4 | Tuesday |
| Phoenix | Sunny | 24.7 | 56 | 26.9 | Thursday |
| Denver | Cloudy | 12.3 | 30 | 28.6 | Monday |
| Los Angeles | Stormy | 18.3 | 41 | 12.5 | Saturday |
<end>Transform this csv structure to a json format:
Title,Author,Publication Year
The Forgotten World,Luna Silverleaf,1950
The Forgotten World,Galen Starfire,1963
Legends of the Rift,Thorne Ironwood,1959
Echoes of Eternity,Elara Moonshadow,1966
The Forgotten World,Sylvia Nightshade,1975
Tales of the Brave,Kara Firebrand,2013
The Forgotten World,Isla Windrider,1966
The Crystal Key,Galen Starfire,1959
The Forgotten World,Draven Blackthorn,1995
Tales of the Brave,Sylvia Nightshade,1958
<start>
[
    {
        "Title": "The Forgotten World",
        "Author": "Luna Silverleaf",
        "Publication Year": 1950
    },
    {
        "Title": "The Forgotten World",
        "Author": "Galen Starfire",
        "Publication Year": 1963
    },
    {
        "Title": "Legends of the Rift",
        "Author": "Thorne Ironwood",
        "Publication Year": 1959
    },
    {
        "Title": "Echoes of Eternity",
        "Author": "Elara Moonshadow",
        "Publication Year": 1966
    },
    {
        "Title": "The Forgotten World",
        "Author": "Sylvia Nightshade",
        "Publication Year": 1975
    },
    {
        "Title": "Tales of the Brave",
        "Author": "Kara Firebrand",
        "Publication Year": 2013
    },
    {
        "Title": "The Forgotten World",
        "Author": "Isla Windrider",
        "Publication Year": 1966
    },
    {
        "Title": "The Crystal Key",
        "Author": "Galen Starfire",
        "Publication Year": 1959
    },
    {
        "Title": "The Forgotten World",
        "Author": "Draven Blackthorn",
        "Publication Year": 1995
    },
    {
        "Title": "Tales of the Brave",
        "Author": "Sylvia Nightshade",
        "Publication Year": 1958
    }
]
<end>Can you change this Csv into Plain text?
Title,Genre,Publication Year,Rating
The Last Sky,Fantasy,1951,4.2
The Crystal Key,Horror,1960,1.9
The Last Sky,Non-Fiction,1968,2.9
Whispers of the Abyss,Fantasy,1963,3.8
<start>
Title: The Last Sky | Genre: Fantasy | Publication Year: 1951 | Rating: 4.2
Title: The Crystal Key | Genre: Horror | Publication Year: 1960 | Rating: 1.9
Title: The Last Sky | Genre: Non-Fiction | Publication Year: 1968 | Rating: 2.9
Title: Whispers of the Abyss | Genre: Fantasy | Publication Year: 1963 | Rating: 3.8
<end>Transform this Plain text structure to a csv format:
Name: Jeffery | Birth Month: December | City: Houston | Income: 220000
Name: Allen | Birth Month: June | City: San Antonio | Income: 295000
Name: Malachi | Birth Month: April | City: San Diego | Income: 85000
Name: Lou | Birth Month: June | City: Jacksonville | Income: 375000
<start>
Name,Birth Month,City,Income
Jeffery,December,Houston,220000
Allen,June,San Antonio,295000
Malachi,April,San Diego,85000
Lou,June,Jacksonville,375000
<end>Convert this plain text to Yml:
Trip Name: Forest Journey | End Location: Denver | Distance (miles): 1112.9 | Duration (hours): 10.2 | Fuel Used (gallons): 75.7
Trip Name: Lakeside Retreat | End Location: San Francisco | Distance (miles): 1326.1 | Duration (hours): 63.7 | Fuel Used (gallons): 98.0
Trip Name: Valley Voyage | End Location: Miami | Distance (miles): 1934.6 | Duration (hours): 49.9 | Fuel Used (gallons): 82.7
<start>
- Distance (miles): 1112.9
  Duration (hours): 10.2
  End Location: Denver
  Fuel Used (gallons): 75.7
  Trip Name: Forest Journey
- Distance (miles): 1326.1
  Duration (hours): 63.7
  End Location: San Francisco
  Fuel Used (gallons): 98.0
  Trip Name: Lakeside Retreat
- Distance (miles): 1934.6
  Duration (hours): 49.9
  End Location: Miami
  Fuel Used (gallons): 82.7
  Trip Name: Valley Voyage
<end>Convert this plain text to Csv:
Company: FoodChain | Open Price: 1052.51 | Close Price: 1221.06 | Volume: 5034435
Company: GreenEnergy | Open Price: 1233.58 | Close Price: 1345.1 | Volume: 1388345
Company: BioLife | Open Price: 825.84 | Close Price: 618.24 | Volume: 975559
Company: GreenEnergy | Open Price: 84.73 | Close Price: 966.01 | Volume: 4985086
Company: BioLife | Open Price: 823.8 | Close Price: 221.68 | Volume: 9754715
Company: GreenEnergy | Open Price: 1481.77 | Close Price: 1035.63 | Volume: 3903549
<start>
Company,Open Price,Close Price,Volume
FoodChain,1052.51,1221.06,5034435
GreenEnergy,1233.58,1345.1,1388345
BioLife,825.84,618.24,975559
GreenEnergy,84.73,966.01,4985086
BioLife,823.8,221.68,9754715
GreenEnergy,1481.77,1035.63,3903549
<end>Please transform the following Plain text data into yml:
Title: Beyond the Veil | Director: Selene Darkwhisper | Genre: Action | Release Year: 2001 | Box Office Earnings (M): 243.35
Title: Edge of Infinity | Director: Aria Ravenwood | Genre: Adventure | Release Year: 1980 | Box Office Earnings (M): 389.56
Title: The Final Voyage | Director: Drake Nightshade | Genre: Drama | Release Year: 1970 | Box Office Earnings (M): 803.7
Title: Edge of Infinity | Director: Talon Blackthorn | Genre: Sci-Fi | Release Year: 1993 | Box Office Earnings (M): 18.28
Title: Mystery of the Depths | Director: Drake Nightshade | Genre: Action | Release Year: 2010 | Box Office Earnings (M): 803.7
Title: The Final Voyage | Director: Talon Blackthorn | Genre: Fantasy | Release Year: 1999 | Box Office Earnings (M): 513.85
Title: Mystery of the Depths | Director: Selene Darkwhisper | Genre: Thriller | Release Year: 1977 | Box Office Earnings (M): 253.14
Title: Mystery of the Depths | Director: Selene Darkwhisper | Genre: Sci-Fi | Release Year: 2013 | Box Office Earnings (M): 267.1
Title: The Great Expedition | Director: Mara Moonshadow | Genre: Comedy | Release Year: 1977 | Box Office Earnings (M): 694.2
Title: Dreamwalker | Director: Lira Silverleaf | Genre: Horror | Release Year: 2017 | Box Office Earnings (M): 558.98
<start>
- Box Office Earnings (M): 243.35
  Director: Selene Darkwhisper
  Genre: Action
  Release Year: 2001
  Title: Beyond the Veil
- Box Office Earnings (M): 389.56
  Director: Aria Ravenwood
  Genre: Adventure
  Release Year: 1980
  Title: Edge of Infinity
- Box Office Earnings (M): 803.7
  Director: Drake Nightshade
  Genre: Drama
  Release Year: 1970
  Title: The Final Voyage
- Box Office Earnings (M): 18.28
  Director: Talon Blackthorn
  Genre: Sci-Fi
  Release Year: 1993
  Title: Edge of Infinity
- Box Office Earnings (M): 803.7
  Director: Drake Nightshade
  Genre: Action
  Release Year: 2010
  Title: Mystery of the Depths
- Box Office Earnings (M): 513.85
  Director: Talon Blackthorn
  Genre: Fantasy
  Release Year: 1999
  Title: The Final Voyage
- Box Office Earnings (M): 253.14
  Director: Selene Darkwhisper
  Genre: Thriller
  Release Year: 1977
  Title: Mystery of the Depths
- Box Office Earnings (M): 267.1
  Director: Selene Darkwhisper
  Genre: Sci-Fi
  Release Year: 2013
  Title: Mystery of the Depths
- Box Office Earnings (M): 694.2
  Director: Mara Moonshadow
  Genre: Comedy
  Release Year: 1977
  Title: The Great Expedition
- Box Office Earnings (M): 558.98
  Director: Lira Silverleaf
  Genre: Horror
  Release Year: 2017
  Title: Dreamwalker
<end>Can you change this markdown into JSON?
| SKU | Price | Stock Quantity | Supplier Name |
| --- | --- | --- | --- |
| SKU-1044 | 329.68 | 37 | Wonka Industries |
| SKU-1090 | 272.73 | 352 | ACME Corp |
| SKU-1098 | 79.24 | 141 | Umbrella Corp |
| SKU-1014 | 491.14 | 28 | ACME Corp |<start>
[
    {
        "SKU": "SKU-1044",
        "Price": 329.68,
        "Stock Quantity": 37,
        "Supplier Name": "Wonka Industries"
    },
    {
        "SKU": "SKU-1090",
        "Price": 272.73,
        "Stock Quantity": 352,
        "Supplier Name": "ACME Corp"
    },
    {
        "SKU": "SKU-1098",
        "Price": 79.24,
        "Stock Quantity": 141,
        "Supplier Name": "Umbrella Corp"
    },
    {
        "SKU": "SKU-1014",
        "Price": 491.14,
        "Stock Quantity": 28,
        "Supplier Name": "ACME Corp"
    }
]
<end>Transform this csv structure to a YAML format:
Product Name,SKU,Price,Stock Quantity,Supplier Name
Gadget,SKU-1029,423.16,33,Globex
Doohickey,SKU-1060,401.18,244,Wayne Enterprises
Gadget,SKU-1034,13.58,379,Umbrella Corp
Doohickey,SKU-1072,337.71,270,Wayne Enterprises
Doohickey,SKU-1013,123.83,125,ACME Corp
Contraption,SKU-1092,279.64,134,Globex
Doohickey,SKU-1069,217.69,233,Umbrella Corp
Instrument,SKU-1066,412.36,9,Wonka Industries
Apparatus,SKU-1078,490.6,352,Globex
<start>
- Price: 423.16
  Product Name: Gadget
  SKU: SKU-1029
  Stock Quantity: 33
  Supplier Name: Globex
- Price: 401.18
  Product Name: Doohickey
  SKU: SKU-1060
  Stock Quantity: 244
  Supplier Name: Wayne Enterprises
- Price: 13.58
  Product Name: Gadget
  SKU: SKU-1034
  Stock Quantity: 379
  Supplier Name: Umbrella Corp
- Price: 337.71
  Product Name: Doohickey
  SKU: SKU-1072
  Stock Quantity: 270
  Supplier Name: Wayne Enterprises
- Price: 123.83
  Product Name: Doohickey
  SKU: SKU-1013
  Stock Quantity: 125
  Supplier Name: ACME Corp
- Price: 279.64
  Product Name: Contraption
  SKU: SKU-1092
  Stock Quantity: 134
  Supplier Name: Globex
- Price: 217.69
  Product Name: Doohickey
  SKU: SKU-1069
  Stock Quantity: 233
  Supplier Name: Umbrella Corp
- Price: 412.36
  Product Name: Instrument
  SKU: SKU-1066
  Stock Quantity: 9
  Supplier Name: Wonka Industries
- Price: 490.6
  Product Name: Apparatus
  SKU: SKU-1078
  Stock Quantity: 352
  Supplier Name: Globex
<end>Can you change this markdown into Plain text?
| Database Name | Queries per Second | Cache Hit Ratio (%) | Connection Count | Average Latency (ms) | Timestamp |
| --- | --- | --- | --- | --- | --- |
| LogsDB | 1572.99 | 79.79 | 294 | 49.06 | 2022-06-11 17:13:19 |
| OrdersDB | 2678.93 | 74.72 | 416 | 53.14 | 2021-02-05 14:28:17 |
| SalesDB | 528.0 | 73.59 | 180 | 46.76 | 2022-08-26 07:46:19 |
| SessionsDB | 1412.71 | 87.57 | 310 | 59.5 | 2022-06-12 02:42:40 |
| ProfilesDB | 4443.47 | 99.03 | 226 | 8.67 | 2023-04-08 09:14:14 |
| UserDB | 1689.8 | 93.13 | 250 | 87.89 | 2022-04-07 06:55:08 |<start>
Database Name: LogsDB | Queries per Second: 1572.99 | Cache Hit Ratio (%): 79.79 | Connection Count: 294 | Average Latency (ms): 49.06 | Timestamp: 2022-06-11 17:13:19
Database Name: OrdersDB | Queries per Second: 2678.93 | Cache Hit Ratio (%): 74.72 | Connection Count: 416 | Average Latency (ms): 53.14 | Timestamp: 2021-02-05 14:28:17
Database Name: SalesDB | Queries per Second: 528.0 | Cache Hit Ratio (%): 73.59 | Connection Count: 180 | Average Latency (ms): 46.76 | Timestamp: 2022-08-26 07:46:19
Database Name: SessionsDB | Queries per Second: 1412.71 | Cache Hit Ratio (%): 87.57 | Connection Count: 310 | Average Latency (ms): 59.5 | Timestamp: 2022-06-12 02:42:40
Database Name: ProfilesDB | Queries per Second: 4443.47 | Cache Hit Ratio (%): 99.03 | Connection Count: 226 | Average Latency (ms): 8.67 | Timestamp: 2023-04-08 09:14:14
Database Name: UserDB | Queries per Second: 1689.8 | Cache Hit Ratio (%): 93.13 | Connection Count: 250 | Average Latency (ms): 87.89 | Timestamp: 2022-04-07 06:55:08
<end>Transform this csv structure to a Markdown format:
Database Name,Queries per Second,Cache Hit Ratio (%),Average Latency (ms),Timestamp
MetricsDB,2603.32,97.08,66.83,2023-06-07 19:59:07
UserDB,1338.26,86.13,80.87,2022-11-16 22:06:10
ProfilesDB,1338.26,86.13,69.69,2022-03-02 04:27:16
ProductsDB,1033.58,91.84,61.42,2023-10-07 10:01:21
InventoryDB,305.6,88.5,90.21,2021-11-01 10:39:16
OrdersDB,1057.96,89.59,91.56,2021-04-12 18:27:03
SalesDB,530.9,94.26,79.08,2021-10-27 11:38:48
AnalyticsDB,925.84,79.65,88.78,2021-08-11 20:39:53
InventoryDB,1268.12,86.3,84.0,2022-03-12 00:41:01
SalesDB,1904.36,74.91,68.64,2023-07-15 13:41:43
<start>
| Database Name | Queries per Second | Cache Hit Ratio (%) | Average Latency (ms) | Timestamp |
| --- | --- | --- | --- | --- |
| MetricsDB | 2603.32 | 97.08 | 66.83 | 2023-06-07 19:59:07 |
| UserDB | 1338.26 | 86.13 | 80.87 | 2022-11-16 22:06:10 |
| ProfilesDB | 1338.26 | 86.13 | 69.69 | 2022-03-02 04:27:16 |
| ProductsDB | 1033.58 | 91.84 | 61.42 | 2023-10-07 10:01:21 |
| InventoryDB | 305.6 | 88.5 | 90.21 | 2021-11-01 10:39:16 |
| OrdersDB | 1057.96 | 89.59 | 91.56 | 2021-04-12 18:27:03 |
| SalesDB | 530.9 | 94.26 | 79.08 | 2021-10-27 11:38:48 |
| AnalyticsDB | 925.84 | 79.65 | 88.78 | 2021-08-11 20:39:53 |
| InventoryDB | 1268.12 | 86.3 | 84.0 | 2022-03-12 00:41:01 |
| SalesDB | 1904.36 | 74.91 | 68.64 | 2023-07-15 13:41:43 |
<end>Here's some CSV data, can you convert it to plain text?
Company,Date,Open Price,Close Price,High Price,Low Price,Volume
RetailWorld,2022-11-23,145.35,713.84,713.84,145.35,1631284
FinanceTrust,2010-09-18,1081.2,736.81,1081.2,736.81,6827633
AutoMotive,2010-07-13,841.57,1498.96,1498.96,426.8,4946206
HealthGen,2023-12-06,789.61,954.07,954.07,426.8,7834569
TechnoCorp,2023-01-22,282.77,547.4,976.49,282.77,4946206
FinanceTrust,2018-05-18,983.04,208.58,1126.31,208.58,3253304
HealthGen,2021-08-05,1354.97,421.39,1354.97,421.39,9728233
RetailWorld,2010-11-08,180.26,180.26,453.42,180.26,6834718
AutoMotive,2013-11-10,1276.4,531.41,1276.4,531.41,8645571
<start>
Company: RetailWorld | Date: 2022-11-23 | Open Price: 145.35 | Close Price: 713.84 | High Price: 713.84 | Low Price: 145.35 | Volume: 1631284
Company: FinanceTrust | Date: 2010-09-18 | Open Price: 1081.2 | Close Price: 736.81 | High Price: 1081.2 | Low Price: 736.81 | Volume: 6827633
Company: AutoMotive | Date: 2010-07-13 | Open Price: 841.57 | Close Price: 1498.96 | High Price: 1498.96 | Low Price: 426.8 | Volume: 4946206
Company: HealthGen | Date: 2023-12-06 | Open Price: 789.61 | Close Price: 954.07 | High Price: 954.07 | Low Price: 426.8 | Volume: 7834569
Company: TechnoCorp | Date: 2023-01-22 | Open Price: 282.77 | Close Price: 547.4 | High Price: 976.49 | Low Price: 282.77 | Volume: 4946206
Company: FinanceTrust | Date: 2018-05-18 | Open Price: 983.04 | Close Price: 208.58 | High Price: 1126.31 | Low Price: 208.58 | Volume: 3253304
Company: HealthGen | Date: 2021-08-05 | Open Price: 1354.97 | Close Price: 421.39 | High Price: 1354.97 | Low Price: 421.39 | Volume: 9728233
Company: RetailWorld | Date: 2010-11-08 | Open Price: 180.26 | Close Price: 180.26 | High Price: 453.42 | Low Price: 180.26 | Volume: 6834718
Company: AutoMotive | Date: 2013-11-10 | Open Price: 1276.4 | Close Price: 531.41 | High Price: 1276.4 | Low Price: 531.41 | Volume: 8645571
<end>Please transform the following csv data into Markdown:
Cache Hit Ratio (%),Connection Count,Average Latency (ms)
89.13,321,52.61
91.47,98,88.55
73.73,457,56.49
93.93,335,18.46
73.1,374,88.55
84.76,469,20.98
90.38,64,53.35
94.62,228,49.06
86.1,500,14.38
<start>
| Cache Hit Ratio (%) | Connection Count | Average Latency (ms) |
| --- | --- | --- |
| 89.13 | 321 | 52.61 |
| 91.47 | 98 | 88.55 |
| 73.73 | 457 | 56.49 |
| 93.93 | 335 | 18.46 |
| 73.1 | 374 | 88.55 |
| 84.76 | 469 | 20.98 |
| 90.38 | 64 | 53.35 |
| 94.62 | 228 | 49.06 |
| 86.1 | 500 | 14.38 |
<end>Here's some markdown data, can you convert it to PLAIN TEXT?
| Company | Sector | Market Cap |
| --- | --- | --- |
| BioPharm | Aerospace | Small Cap |
| TechCorp | Healthcare | Large Cap |
| TechCorp | Technology | Large Cap |
| RetailHub | Aerospace | Small Cap |
| GlobalTrade | Finance | Mid Cap |
| FinanceWorks | Healthcare | Mid Cap |
| BioPharm | Energy | Mid Cap |<start>
Company: BioPharm | Sector: Aerospace | Market Cap: Small Cap
Company: TechCorp | Sector: Healthcare | Market Cap: Large Cap
Company: TechCorp | Sector: Technology | Market Cap: Large Cap
Company: RetailHub | Sector: Aerospace | Market Cap: Small Cap
Company: GlobalTrade | Sector: Finance | Market Cap: Mid Cap
Company: FinanceWorks | Sector: Healthcare | Market Cap: Mid Cap
Company: BioPharm | Sector: Energy | Market Cap: Mid Cap
<end>Can you change this json into markdown?
[
    {
        "Device ID": "device-0045",
        "Battery Level (%)": 86.1,
        "Reading Value": 64.8,
        "Timestamp": "2021-07-19 22:21:56"
    },
    {
        "Device ID": "device-0061",
        "Battery Level (%)": 74.5,
        "Reading Value": -30.23,
        "Timestamp": "2022-10-18 02:31:37"
    },
    {
        "Device ID": "device-0083",
        "Battery Level (%)": 10.4,
        "Reading Value": 6.96,
        "Timestamp": "2022-08-19 11:11:32"
    }
]<start>
| Device ID | Battery Level (%) | Reading Value | Timestamp |
| --- | --- | --- | --- |
| device-0045 | 86.1 | 64.8 | 2021-07-19 22:21:56 |
| device-0061 | 74.5 | -30.23 | 2022-10-18 02:31:37 |
| device-0083 | 10.4 | 6.96 | 2022-08-19 11:11:32 |
<end>Convert this Markdown to Json:
| Company | Date | Open Price | High Price | Low Price | Volume |
| --- | --- | --- | --- | --- | --- |
| MediaGroup | 2011-09-26 | 708.38 | 942.63 | 449.22 | 9152227 |
| BioLife | 2013-10-15 | 1109.55 | 1109.55 | 442.39 | 1858976 |
| RetailWorld | 2022-12-13 | 1268.12 | 1346.11 | 481.13 | 4175504 |
| FinanceTrust | 2020-08-24 | 474.01 | 474.01 | 10.89 | 229978 |
| AutoMotive | 2011-08-08 | 582.73 | 582.73 | 260.09 | 9299410 |
| AeroSystems | 2023-01-03 | 454.97 | 454.97 | 270.43 | 7473072 |<start>
[
    {
        "Company": "MediaGroup",
        "Date": "2011-09-26",
        "Open Price": 708.38,
        "High Price": 942.63,
        "Low Price": 449.22,
        "Volume": 9152227
    },
    {
        "Company": "BioLife",
        "Date": "2013-10-15",
        "Open Price": 1109.55,
        "High Price": 1109.55,
        "Low Price": 442.39,
        "Volume": 1858976
    },
    {
        "Company": "RetailWorld",
        "Date": "2022-12-13",
        "Open Price": 1268.12,
        "High Price": 1346.11,
        "Low Price": 481.13,
        "Volume": 4175504
    },
    {
        "Company": "FinanceTrust",
        "Date": "2020-08-24",
        "Open Price": 474.01,
        "High Price": 474.01,
        "Low Price": 10.89,
        "Volume": 229978
    },
    {
        "Company": "AutoMotive",
        "Date": "2011-08-08",
        "Open Price": 582.73,
        "High Price": 582.73,
        "Low Price": 260.09,
        "Volume": 9299410
    },
    {
        "Company": "AeroSystems",
        "Date": "2023-01-03",
        "Open Price": 454.97,
        "High Price": 454.97,
        "Low Price": 270.43,
        "Volume": 7473072
    }
]
<end>Here's some markdown data, can you convert it to YML?
| Title | Rating |
| --- | --- |
| Shadows of Solitude | 3.5 |
| Legends of the Rift | 1.3 |
| A Journey Through Time | 3.1 |
| A Journey Through Time | 2.5 |
| The Last Sky | 4.8 |
| Tales of the Brave | 4.1 |
| Tales of the Brave | 2.0 |<start>
- Rating: 3.5
  Title: Shadows of Solitude
- Rating: 1.3
  Title: Legends of the Rift
- Rating: 3.1
  Title: A Journey Through Time
- Rating: 2.5
  Title: A Journey Through Time
- Rating: 4.8
  Title: The Last Sky
- Rating: 4.1
  Title: Tales of the Brave
- Rating: 2.0
  Title: Tales of the Brave
<end>Convert this CSV to Markdown:
Product Name,SKU,Stock Quantity,Category,Supplier Name
Device,SKU-1098,487,Toys,Globex
Apparatus,SKU-1046,60,Household,Wonka Industries
Device,SKU-1082,240,Sports,Wayne Enterprises
Doohickey,SKU-1077,178,Automotive,ACME Corp
Apparatus,SKU-1050,431,Household,Umbrella Corp
Gizmo,SKU-1054,264,Electronics,Globex
Doohickey,SKU-1042,393,Sports,Wonka Industries
Widget,SKU-1058,451,Toys,Globex
Doohickey,SKU-1004,227,Sports,ACME Corp
Whatchamacallit,SKU-1038,66,Sports,Wonka Industries
<start>
| Product Name | SKU | Stock Quantity | Category | Supplier Name |
| --- | --- | --- | --- | --- |
| Device | SKU-1098 | 487 | Toys | Globex |
| Apparatus | SKU-1046 | 60 | Household | Wonka Industries |
| Device | SKU-1082 | 240 | Sports | Wayne Enterprises |
| Doohickey | SKU-1077 | 178 | Automotive | ACME Corp |
| Apparatus | SKU-1050 | 431 | Household | Umbrella Corp |
| Gizmo | SKU-1054 | 264 | Electronics | Globex |
| Doohickey | SKU-1042 | 393 | Sports | Wonka Industries |
| Widget | SKU-1058 | 451 | Toys | Globex |
| Doohickey | SKU-1004 | 227 | Sports | ACME Corp |
| Whatchamacallit | SKU-1038 | 66 | Sports | Wonka Industries |
<end>Here's some CSV data, can you convert it to JSON?
Condition,Temperature (C),Wind Speed (km/h),Day
Sunny,7.5,26.2,Monday
Rainy,9.7,7.8,Wednesday
Windy,39.8,4.2,Monday
Sunny,5.9,2.3,Sunday
Snowy,3.7,23.9,Monday
Foggy,-4.0,13.2,Tuesday
Windy,27.6,25.7,Friday
<start>
[
    {
        "Condition": "Sunny",
        "Temperature (C)": 7.5,
        "Wind Speed (km/h)": 26.2,
        "Day": "Monday"
    },
    {
        "Condition": "Rainy",
        "Temperature (C)": 9.7,
        "Wind Speed (km/h)": 7.8,
        "Day": "Wednesday"
    },
    {
        "Condition": "Windy",
        "Temperature (C)": 39.8,
        "Wind Speed (km/h)": 4.2,
        "Day": "Monday"
    },
    {
        "Condition": "Sunny",
        "Temperature (C)": 5.9,
        "Wind Speed (km/h)": 2.3,
        "Day": "Sunday"
    },
    {
        "Condition": "Snowy",
        "Temperature (C)": 3.7,
        "Wind Speed (km/h)": 23.9,
        "Day": "Monday"
    },
    {
        "Condition": "Foggy",
        "Temperature (C)": -4.0,
        "Wind Speed (km/h)": 13.2,
        "Day": "Tuesday"
    },
    {
        "Condition": "Windy",
        "Temperature (C)": 27.6,
        "Wind Speed (km/h)": 25.7,
        "Day": "Friday"
    }
]
<end>Transform this MARKDOWN structure to a plain text format:
| Cache Hit Ratio (%) | Connection Count | Timestamp |
| --- | --- | --- |
| 87.3 | 17 | 2021-07-13 09:05:10 |
| 72.14 | 376 | 2023-05-20 14:43:36 |
| 73.42 | 117 | 2021-11-21 04:16:48 |
| 73.0 | 159 | 2021-08-15 09:42:29 |<start>
Cache Hit Ratio (%): 87.3 | Connection Count: 17 | Timestamp: 2021-07-13 09:05:10
Cache Hit Ratio (%): 72.14 | Connection Count: 376 | Timestamp: 2023-05-20 14:43:36
Cache Hit Ratio (%): 73.42 | Connection Count: 117 | Timestamp: 2021-11-21 04:16:48
Cache Hit Ratio (%): 73.0 | Connection Count: 159 | Timestamp: 2021-08-15 09:42:29
<end>Please transform the following markdown data into yml:
| Location | Condition | Humidity (%) | Wind Speed (km/h) |
| --- | --- | --- | --- |
| New York | Rainy | 39 | 2.5 |
| Houston | Stormy | 89 | 0.6 |
| Los Angeles | Foggy | 95 | 10.2 |<start>
- Condition: Rainy
  Humidity (%): 39
  Location: New York
  Wind Speed (km/h): 2.5
- Condition: Stormy
  Humidity (%): 89
  Location: Houston
  Wind Speed (km/h): 0.6
- Condition: Foggy
  Humidity (%): 95
  Location: Los Angeles
  Wind Speed (km/h): 10.2
<end>Here's some yml data, can you convert it to csv?
- Battery Level (%): 61.4
  Device ID: device-0032
  Device Type: Temperature Sensor
  Location: Hallway
  Reading Value: -34.53
  Timestamp: '2023-06-07 20:10:03'
- Battery Level (%): 85.2
  Device ID: device-0097
  Device Type: Temperature Sensor
  Location: Hallway
  Reading Value: 12.11
  Timestamp: '2022-10-14 17:22:05'
- Battery Level (%): 83.6
  Device ID: device-0019
  Device Type: Pressure Sensor
  Location: Office
  Reading Value: -27.9
  Timestamp: '2022-11-15 04:17:04'
- Battery Level (%): 58.0
  Device ID: device-0097
  Device Type: Light Sensor
  Location: Garden
  Reading Value: 41.51
  Timestamp: '2021-09-10 13:40:03'
<start>
Device ID,Device Type,Location,Battery Level (%),Reading Value,Timestamp
device-0032,Temperature Sensor,Hallway,61.4,-34.53,2023-06-07 20:10:03
device-0097,Temperature Sensor,Hallway,85.2,12.11,2022-10-14 17:22:05
device-0019,Pressure Sensor,Office,83.6,-27.9,2022-11-15 04:17:04
device-0097,Light Sensor,Garden,58.0,41.51,2021-09-10 13:40:03
<end>Convert this yml to json:
- Cuisine: Chinese
  Price Range: $
  Rating: 5
  Restaurant Name: Sushi World
- Cuisine: Japanese
  Price Range: $$$$$
  Rating: 1
  Restaurant Name: Curry Corner
- Cuisine: Italian
  Price Range: $$$$
  Rating: 5
  Restaurant Name: Burger Haven
- Cuisine: French
  Price Range: $$
  Rating: 4
  Restaurant Name: Curry Corner
- Cuisine: Mediterranean
  Price Range: $$$
  Rating: 2
  Restaurant Name: Curry Corner
- Cuisine: Mexican
  Price Range: $$$
  Rating: 1
  Restaurant Name: Taco Town
- Cuisine: Italian
  Price Range: $$$
  Rating: 4
  Restaurant Name: Pizza Planet
- Cuisine: Chinese
  Price Range: $$$$$
  Rating: 1
  Restaurant Name: The Golden Spoon
<start>
[
    {
        "Restaurant Name": "Sushi World",
        "Cuisine": "Chinese",
        "Rating": 5,
        "Price Range": "$"
    },
    {
        "Restaurant Name": "Curry Corner",
        "Cuisine": "Japanese",
        "Rating": 1,
        "Price Range": "$$$$$"
    },
    {
        "Restaurant Name": "Burger Haven",
        "Cuisine": "Italian",
        "Rating": 5,
        "Price Range": "$$$$"
    },
    {
        "Restaurant Name": "Curry Corner",
        "Cuisine": "French",
        "Rating": 4,
        "Price Range": "$$"
    },
    {
        "Restaurant Name": "Curry Corner",
        "Cuisine": "Mediterranean",
        "Rating": 2,
        "Price Range": "$$$"
    },
    {
        "Restaurant Name": "Taco Town",
        "Cuisine": "Mexican",
        "Rating": 1,
        "Price Range": "$$$"
    },
    {
        "Restaurant Name": "Pizza Planet",
        "Cuisine": "Italian",
        "Rating": 4,
        "Price Range": "$$$"
    },
    {
        "Restaurant Name": "The Golden Spoon",
        "Cuisine": "Chinese",
        "Rating": 1,
        "Price Range": "$$$$$"
    }
]
<end>Here's some plain text data, can you convert it to Markdown?
Start Location: Phoenix | End Location: Los Angeles | Distance (miles): 1267.9 | Fuel Used (gallons): 62.0
Start Location: New York | End Location: Denver | Distance (miles): 2356.0 | Fuel Used (gallons): 29.3
Start Location: Chicago | End Location: Houston | Distance (miles): 857.3 | Fuel Used (gallons): 91.0
Start Location: Los Angeles | End Location: Houston | Distance (miles): 672.5 | Fuel Used (gallons): 62.0
Start Location: Los Angeles | End Location: Denver | Distance (miles): 1924.3 | Fuel Used (gallons): 12.8
Start Location: Denver | End Location: New York | Distance (miles): 1750.9 | Fuel Used (gallons): 53.2
Start Location: San Francisco | End Location: New York | Distance (miles): 1407.8 | Fuel Used (gallons): 65.4
Start Location: San Francisco | End Location: Miami | Distance (miles): 2795.5 | Fuel Used (gallons): 54.0
Start Location: New York | End Location: Houston | Distance (miles): 1630.2 | Fuel Used (gallons): 24.6
<start>
| Start Location | End Location | Distance (miles) | Fuel Used (gallons) |
| --- | --- | --- | --- |
| Phoenix | Los Angeles | 1267.9 | 62.0 |
| New York | Denver | 2356.0 | 29.3 |
| Chicago | Houston | 857.3 | 91.0 |
| Los Angeles | Houston | 672.5 | 62.0 |
| Los Angeles | Denver | 1924.3 | 12.8 |
| Denver | New York | 1750.9 | 53.2 |
| San Francisco | New York | 1407.8 | 65.4 |
| San Francisco | Miami | 2795.5 | 54.0 |
| New York | Houston | 1630.2 | 24.6 |
<end>Here's some json data, can you convert it to yaml?
[
    {
        "Sector": "Aerospace",
        "Market Cap": "Mega Cap",
        "Stock Price": 782.77,
        "Annual Revenue (B)": 87.7,
        "Quarter": "Q2"
    },
    {
        "Sector": "Biotech",
        "Market Cap": "Mega Cap",
        "Stock Price": 556.11,
        "Annual Revenue (B)": 246.06,
        "Quarter": "Q1"
    },
    {
        "Sector": "Retail",
        "Market Cap": "Large Cap",
        "Stock Price": 470.57,
        "Annual Revenue (B)": 254.29,
        "Quarter": "Q1"
    },
    {
        "Sector": "Finance",
        "Market Cap": "Small Cap",
        "Stock Price": 379.68,
        "Annual Revenue (B)": 351.82,
        "Quarter": "Q1"
    },
    {
        "Sector": "Healthcare",
        "Market Cap": "Small Cap",
        "Stock Price": 393.68,
        "Annual Revenue (B)": 458.28,
        "Quarter": "Q3"
    },
    {
        "Sector": "Technology",
        "Market Cap": "Small Cap",
        "Stock Price": 773.88,
        "Annual Revenue (B)": 77.3,
        "Quarter": "Q1"
    },
    {
        "Sector": "Aerospace",
        "Market Cap": "Mega Cap",
        "Stock Price": 469.11,
        "Annual Revenue (B)": 314.74,
        "Quarter": "Q1"
    },
    {
        "Sector": "Biotech",
        "Market Cap": "Small Cap",
        "Stock Price": 298.51,
        "Annual Revenue (B)": 408.23,
        "Quarter": "Q4"
    }
]<start>
- Annual Revenue (B): 87.7
  Market Cap: Mega Cap
  Quarter: Q2
  Sector: Aerospace
  Stock Price: 782.77
- Annual Revenue (B): 246.06
  Market Cap: Mega Cap
  Quarter: Q1
  Sector: Biotech
  Stock Price: 556.11
- Annual Revenue (B): 254.29
  Market Cap: Large Cap
  Quarter: Q1
  Sector: Retail
  Stock Price: 470.57
- Annual Revenue (B): 351.82
  Market Cap: Small Cap
  Quarter: Q1
  Sector: Finance
  Stock Price: 379.68
- Annual Revenue (B): 458.28
  Market Cap: Small Cap
  Quarter: Q3
  Sector: Healthcare
  Stock Price: 393.68
- Annual Revenue (B): 77.3
  Market Cap: Small Cap
  Quarter: Q1
  Sector: Technology
  Stock Price: 773.88
- Annual Revenue (B): 314.74
  Market Cap: Mega Cap
  Quarter: Q1
  Sector: Aerospace
  Stock Price: 469.11
- Annual Revenue (B): 408.23
  Market Cap: Small Cap
  Quarter: Q4
  Sector: Biotech
  Stock Price: 298.51
<end>Can you change this MARKDOWN into Plain text?
| Restaurant Name | Price Range |
| --- | --- |
| Sushi World | $$$$ |
| Curry Corner | $$ |
| Burger Haven | $$$ |
| Pasta Palace | $ |<start>
Restaurant Name: Sushi World | Price Range: $$$$
Restaurant Name: Curry Corner | Price Range: $$
Restaurant Name: Burger Haven | Price Range: $$$
Restaurant Name: Pasta Palace | Price Range: $
<end>Transform this plain text structure to a Csv format:
Device ID: device-0068 | Location: Kitchen | Battery Level (%): 48.7 | Reading Value: -27.97 | Timestamp: 2022-05-11 00:39:18
Device ID: device-0054 | Location: Garden | Battery Level (%): 71.3 | Reading Value: 2.18 | Timestamp: 2022-04-14 22:04:21
Device ID: device-0073 | Location: Garage | Battery Level (%): 37.3 | Reading Value: 75.42 | Timestamp: 2022-05-01 17:42:52
Device ID: device-0090 | Location: Garage | Battery Level (%): 75.3 | Reading Value: -39.7 | Timestamp: 2022-01-10 01:52:54
Device ID: device-0027 | Location: Living Room | Battery Level (%): 13.2 | Reading Value: -22.44 | Timestamp: 2022-05-19 11:11:11
Device ID: device-0084 | Location: Hallway | Battery Level (%): 70.2 | Reading Value: -8.86 | Timestamp: 2021-11-08 02:57:53
Device ID: device-0099 | Location: Kitchen | Battery Level (%): 80.3 | Reading Value: -8.34 | Timestamp: 2023-11-13 14:12:33
Device ID: device-0017 | Location: Kitchen | Battery Level (%): 56.9 | Reading Value: 49.45 | Timestamp: 2021-04-15 21:46:43
Device ID: device-0066 | Location: Kitchen | Battery Level (%): 67.0 | Reading Value: -23.54 | Timestamp: 2022-03-20 09:39:07
Device ID: device-0059 | Location: Office | Battery Level (%): 49.4 | Reading Value: -31.34 | Timestamp: 2021-02-05 04:49:40
<start>
Device ID,Location,Battery Level (%),Reading Value,Timestamp
device-0068,Kitchen,48.7,-27.97,2022-05-11 00:39:18
device-0054,Garden,71.3,2.18,2022-04-14 22:04:21
device-0073,Garage,37.3,75.42,2022-05-01 17:42:52
device-0090,Garage,75.3,-39.7,2022-01-10 01:52:54
device-0027,Living Room,13.2,-22.44,2022-05-19 11:11:11
device-0084,Hallway,70.2,-8.86,2021-11-08 02:57:53
device-0099,Kitchen,80.3,-8.34,2023-11-13 14:12:33
device-0017,Kitchen,56.9,49.45,2021-04-15 21:46:43
device-0066,Kitchen,67.0,-23.54,2022-03-20 09:39:07
device-0059,Office,49.4,-31.34,2021-02-05 04:49:40
<end>Can you change this CSV into markdown?
Location,Condition,Temperature (C),Humidity (%),Wind Speed (km/h),Day
Chicago,Stormy,-6.7,73,13.6,Sunday
Phoenix,Snowy,-1.8,74,0.4,Sunday
Denver,Foggy,28.8,84,7.3,Friday
Phoenix,Foggy,-7.5,35,15.1,Friday
Houston,Rainy,8.8,58,17.9,Saturday
Denver,Stormy,37.1,71,10.9,Friday
<start>
| Location | Condition | Temperature (C) | Humidity (%) | Wind Speed (km/h) | Day |
| --- | --- | --- | --- | --- | --- |
| Chicago | Stormy | -6.7 | 73 | 13.6 | Sunday |
| Phoenix | Snowy | -1.8 | 74 | 0.4 | Sunday |
| Denver | Foggy | 28.8 | 84 | 7.3 | Friday |
| Phoenix | Foggy | -7.5 | 35 | 15.1 | Friday |
| Houston | Rainy | 8.8 | 58 | 17.9 | Saturday |
| Denver | Stormy | 37.1 | 71 | 10.9 | Friday |
<end>Convert this yml to plain text:
- Battery Level (%): 13.0
  Device Type: Temperature Sensor
  Location: Kitchen
  Reading Value: -1.73
  Timestamp: '2022-11-03 18:01:25'
- Battery Level (%): 29.7
  Device Type: Pressure Sensor
  Location: Office
  Reading Value: -1.73
  Timestamp: '2022-08-25 03:37:52'
- Battery Level (%): 58.0
  Device Type: Humidity Sensor
  Location: Living Room
  Reading Value: -24.12
  Timestamp: '2022-06-05 07:16:56'
- Battery Level (%): 42.5
  Device Type: Temperature Sensor
  Location: Kitchen
  Reading Value: 53.22
  Timestamp: '2022-09-16 05:33:21'
- Battery Level (%): 23.5
  Device Type: Motion Detector
  Location: Office
  Reading Value: -38.71
  Timestamp: '2023-09-18 07:13:14'
- Battery Level (%): 32.0
  Device Type: Light Sensor
  Location: Living Room
  Reading Value: 58.15
  Timestamp: '2022-05-01 22:56:25'
- Battery Level (%): 83.1
  Device Type: Humidity Sensor
  Location: Office
  Reading Value: 53.22
  Timestamp: '2022-08-23 06:32:46'
- Battery Level (%): 81.7
  Device Type: Humidity Sensor
  Location: Hallway
  Reading Value: -29.73
  Timestamp: '2022-04-01 02:36:37'
- Battery Level (%): 50.0
  Device Type: Pressure Sensor
  Location: Bedroom
  Reading Value: 64.18
  Timestamp: '2022-11-06 18:09:28'
<start>
Device Type: Temperature Sensor | Location: Kitchen | Battery Level (%): 13.0 | Reading Value: -1.73 | Timestamp: 2022-11-03 18:01:25
Device Type: Pressure Sensor | Location: Office | Battery Level (%): 29.7 | Reading Value: -1.73 | Timestamp: 2022-08-25 03:37:52
Device Type: Humidity Sensor | Location: Living Room | Battery Level (%): 58.0 | Reading Value: -24.12 | Timestamp: 2022-06-05 07:16:56
Device Type: Temperature Sensor | Location: Kitchen | Battery Level (%): 42.5 | Reading Value: 53.22 | Timestamp: 2022-09-16 05:33:21
Device Type: Motion Detector | Location: Office | Battery Level (%): 23.5 | Reading Value: -38.71 | Timestamp: 2023-09-18 07:13:14
Device Type: Light Sensor | Location: Living Room | Battery Level (%): 32.0 | Reading Value: 58.15 | Timestamp: 2022-05-01 22:56:25
Device Type: Humidity Sensor | Location: Office | Battery Level (%): 83.1 | Reading Value: 53.22 | Timestamp: 2022-08-23 06:32:46
Device Type: Humidity Sensor | Location: Hallway | Battery Level (%): 81.7 | Reading Value: -29.73 | Timestamp: 2022-04-01 02:36:37
Device Type: Pressure Sensor | Location: Bedroom | Battery Level (%): 50.0 | Reading Value: 64.18 | Timestamp: 2022-11-06 18:09:28
<end>Here's some YAML data, can you convert it to Json?
- Distance (miles): 348.4
  Duration (hours): 62.9
  End Location: Phoenix
  Start Location: Los Angeles
- Distance (miles): 1303.1
  Duration (hours): 1.4
  End Location: Chicago
  Start Location: Los Angeles
- Distance (miles): 2531.8
  Duration (hours): 31.8
  End Location: Chicago
  Start Location: San Francisco
- Distance (miles): 225.8
  Duration (hours): 56.6
  End Location: Denver
  Start Location: Houston
- Distance (miles): 169.9
  Duration (hours): 24.0
  End Location: New York
  Start Location: San Francisco
- Distance (miles): 689.3
  Duration (hours): 15.1
  End Location: Chicago
  Start Location: Phoenix
- Distance (miles): 2599.8
  Duration (hours): 19.6
  End Location: San Francisco
  Start Location: Chicago
- Distance (miles): 2531.8
  Duration (hours): 39.5
  End Location: New York
  Start Location: Denver
- Distance (miles): 940.7
  Duration (hours): 19.6
  End Location: Phoenix
  Start Location: San Francisco
<start>
[
    {
        "Start Location": "Los Angeles",
        "End Location": "Phoenix",
        "Distance (miles)": 348.4,
        "Duration (hours)": 62.9
    },
    {
        "Start Location": "Los Angeles",
        "End Location": "Chicago",
        "Distance (miles)": 1303.1,
        "Duration (hours)": 1.4
    },
    {
        "Start Location": "San Francisco",
        "End Location": "Chicago",
        "Distance (miles)": 2531.8,
        "Duration (hours)": 31.8
    },
    {
        "Start Location": "Houston",
        "End Location": "Denver",
        "Distance (miles)": 225.8,
        "Duration (hours)": 56.6
    },
    {
        "Start Location": "San Francisco",
        "End Location": "New York",
        "Distance (miles)": 169.9,
        "Duration (hours)": 24.0
    },
    {
        "Start Location": "Phoenix",
        "End Location": "Chicago",
        "Distance (miles)": 689.3,
        "Duration (hours)": 15.1
    },
    {
        "Start Location": "Chicago",
        "End Location": "San Francisco",
        "Distance (miles)": 2599.8,
        "Duration (hours)": 19.6
    },
    {
        "Start Location": "Denver",
        "End Location": "New York",
        "Distance (miles)": 2531.8,
        "Duration (hours)": 39.5
    },
    {
        "Start Location": "San Francisco",
        "End Location": "Phoenix",
        "Distance (miles)": 940.7,
        "Duration (hours)": 19.6
    }
]
<end>Here's some csv data, can you convert it to JSON?
Company,Sector,Market Cap
Foodies,Energy,Small Cap
BioPharm,Biotech,Mid Cap
HealthPlus,Technology,Small Cap
BioPharm,Aerospace,Mega Cap
<start>
[
    {
        "Company": "Foodies",
        "Sector": "Energy",
        "Market Cap": "Small Cap"
    },
    {
        "Company": "BioPharm",
        "Sector": "Biotech",
        "Market Cap": "Mid Cap"
    },
    {
        "Company": "HealthPlus",
        "Sector": "Technology",
        "Market Cap": "Small Cap"
    },
    {
        "Company": "BioPharm",
        "Sector": "Aerospace",
        "Market Cap": "Mega Cap"
    }
]
<end>Please transform the following json data into PLAIN TEXT:
[
    {
        "Trip Name": "Forest Journey",
        "Distance (miles)": 1644.2,
        "Duration (hours)": 45.5,
        "Fuel Used (gallons)": 33.9
    },
    {
        "Trip Name": "Lakeside Retreat",
        "Distance (miles)": 997.9,
        "Duration (hours)": 64.1,
        "Fuel Used (gallons)": 12.0
    },
    {
        "Trip Name": "Forest Journey",
        "Distance (miles)": 1489.1,
        "Duration (hours)": 57.7,
        "Fuel Used (gallons)": 34.5
    },
    {
        "Trip Name": "Canyon Trek",
        "Distance (miles)": 1398.6,
        "Duration (hours)": 27.4,
        "Fuel Used (gallons)": 21.8
    },
    {
        "Trip Name": "Desert Drive",
        "Distance (miles)": 1583.8,
        "Duration (hours)": 57.8,
        "Fuel Used (gallons)": 94.5
    },
    {
        "Trip Name": "Historic Route",
        "Distance (miles)": 200.4,
        "Duration (hours)": 55.4,
        "Fuel Used (gallons)": 91.0
    }
]<start>
Trip Name: Forest Journey | Distance (miles): 1644.2 | Duration (hours): 45.5 | Fuel Used (gallons): 33.9
Trip Name: Lakeside Retreat | Distance (miles): 997.9 | Duration (hours): 64.1 | Fuel Used (gallons): 12.0
Trip Name: Forest Journey | Distance (miles): 1489.1 | Duration (hours): 57.7 | Fuel Used (gallons): 34.5
Trip Name: Canyon Trek | Distance (miles): 1398.6 | Duration (hours): 27.4 | Fuel Used (gallons): 21.8
Trip Name: Desert Drive | Distance (miles): 1583.8 | Duration (hours): 57.8 | Fuel Used (gallons): 94.5
Trip Name: Historic Route | Distance (miles): 200.4 | Duration (hours): 55.4 | Fuel Used (gallons): 91.0
<end>Here's some JSON data, can you convert it to Markdown?
[
    {
        "Company": "AutoDrive",
        "Stock Price": 559.32,
        "Annual Revenue (B)": 164.33,
        "Quarter": "Q2"
    },
    {
        "Company": "BioPharm",
        "Stock Price": 644.78,
        "Annual Revenue (B)": 100.51,
        "Quarter": "Q4"
    },
    {
        "Company": "AutoDrive",
        "Stock Price": 215.12,
        "Annual Revenue (B)": 73.14,
        "Quarter": "Q2"
    },
    {
        "Company": "EcoEnergy",
        "Stock Price": 665.99,
        "Annual Revenue (B)": 241.26,
        "Quarter": "Q1"
    },
    {
        "Company": "AeroSpace",
        "Stock Price": 321.55,
        "Annual Revenue (B)": 460.84,
        "Quarter": "Q2"
    },
    {
        "Company": "AutoDrive",
        "Stock Price": 625.03,
        "Annual Revenue (B)": 50.76,
        "Quarter": "Q3"
    },
    {
        "Company": "RetailHub",
        "Stock Price": 984.07,
        "Annual Revenue (B)": 257.68,
        "Quarter": "Q2"
    }
]<start>
| Company | Stock Price | Annual Revenue (B) | Quarter |
| --- | --- | --- | --- |
| AutoDrive | 559.32 | 164.33 | Q2 |
| BioPharm | 644.78 | 100.51 | Q4 |
| AutoDrive | 215.12 | 73.14 | Q2 |
| EcoEnergy | 665.99 | 241.26 | Q1 |
| AeroSpace | 321.55 | 460.84 | Q2 |
| AutoDrive | 625.03 | 50.76 | Q3 |
| RetailHub | 984.07 | 257.68 | Q2 |
<end>Here's some YAML data, can you convert it to csv?
- Average Latency (ms): 17.45
  Database Name: OrdersDB
  Timestamp: '2022-10-20 16:41:10'
- Average Latency (ms): 20.78
  Database Name: LogsDB
  Timestamp: '2023-01-02 11:24:50'
- Average Latency (ms): 77.8
  Database Name: AnalyticsDB
  Timestamp: '2021-06-19 06:42:30'
<start>
Database Name,Average Latency (ms),Timestamp
OrdersDB,17.45,2022-10-20 16:41:10
LogsDB,20.78,2023-01-02 11:24:50
AnalyticsDB,77.8,2021-06-19 06:42:30
<end>Here's some json data, can you convert it to YML?
[
    {
        "Condition": "Foggy",
        "Temperature (C)": 4.4,
        "Humidity (%)": 81,
        "Wind Speed (km/h)": 8.1
    },
    {
        "Condition": "Stormy",
        "Temperature (C)": 31.1,
        "Humidity (%)": 60,
        "Wind Speed (km/h)": 9.8
    },
    {
        "Condition": "Snowy",
        "Temperature (C)": 25.6,
        "Humidity (%)": 74,
        "Wind Speed (km/h)": 18.9
    },
    {
        "Condition": "Snowy",
        "Temperature (C)": 10.8,
        "Humidity (%)": 67,
        "Wind Speed (km/h)": 29.6
    },
    {
        "Condition": "Rainy",
        "Temperature (C)": 13.7,
        "Humidity (%)": 74,
        "Wind Speed (km/h)": 11.7
    },
    {
        "Condition": "Snowy",
        "Temperature (C)": 27.1,
        "Humidity (%)": 66,
        "Wind Speed (km/h)": 29.5
    },
    {
        "Condition": "Snowy",
        "Temperature (C)": 5.2,
        "Humidity (%)": 98,
        "Wind Speed (km/h)": 15.5
    },
    {
        "Condition": "Stormy",
        "Temperature (C)": 5.2,
        "Humidity (%)": 97,
        "Wind Speed (km/h)": 8.6
    },
    {
        "Condition": "Cloudy",
        "Temperature (C)": 10.8,
        "Humidity (%)": 69,
        "Wind Speed (km/h)": 29.6
    }
]<start>
- Condition: Foggy
  Humidity (%): 81
  Temperature (C): 4.4
  Wind Speed (km/h): 8.1
- Condition: Stormy
  Humidity (%): 60
  Temperature (C): 31.1
  Wind Speed (km/h): 9.8
- Condition: Snowy
  Humidity (%): 74
  Temperature (C): 25.6
  Wind Speed (km/h): 18.9
- Condition: Snowy
  Humidity (%): 67
  Temperature (C): 10.8
  Wind Speed (km/h): 29.6
- Condition: Rainy
  Humidity (%): 74
  Temperature (C): 13.7
  Wind Speed (km/h): 11.7
- Condition: Snowy
  Humidity (%): 66
  Temperature (C): 27.1
  Wind Speed (km/h): 29.5
- Condition: Snowy
  Humidity (%): 98
  Temperature (C): 5.2
  Wind Speed (km/h): 15.5
- Condition: Stormy
  Humidity (%): 97
  Temperature (C): 5.2
  Wind Speed (km/h): 8.6
- Condition: Cloudy
  Humidity (%): 69
  Temperature (C): 10.8
  Wind Speed (km/h): 29.6
<end>Transform this yml structure to a csv format:
- Humidity (%): 41
  Location: Miami
  Wind Speed (km/h): 21.8
- Humidity (%): 96
  Location: Miami
  Wind Speed (km/h): 19.2
- Humidity (%): 42
  Location: Seattle
  Wind Speed (km/h): 11.0
<start>
Location,Humidity (%),Wind Speed (km/h)
Miami,41,21.8
Miami,96,19.2
Seattle,42,11.0
<end>Convert this PLAIN TEXT to markdown:
Location: Chicago | Temperature (C): 24.9 | Humidity (%): 26 | Wind Speed (km/h): 11.0 | Day: Friday
Location: Denver | Temperature (C): -9.6 | Humidity (%): 80 | Wind Speed (km/h): 9.5 | Day: Thursday
Location: Los Angeles | Temperature (C): 11.3 | Humidity (%): 50 | Wind Speed (km/h): 29.7 | Day: Thursday
Location: Seattle | Temperature (C): 21.1 | Humidity (%): 21 | Wind Speed (km/h): 23.1 | Day: Wednesday
Location: New York | Temperature (C): -2.2 | Humidity (%): 84 | Wind Speed (km/h): 1.4 | Day: Thursday
Location: New York | Temperature (C): -3.8 | Humidity (%): 44 | Wind Speed (km/h): 5.5 | Day: Thursday
Location: Los Angeles | Temperature (C): 1.7 | Humidity (%): 100 | Wind Speed (km/h): 5.9 | Day: Saturday
Location: Los Angeles | Temperature (C): 32.4 | Humidity (%): 96 | Wind Speed (km/h): 24.2 | Day: Wednesday
Location: Denver | Temperature (C): 22.3 | Humidity (%): 23 | Wind Speed (km/h): 21.0 | Day: Monday
Location: Denver | Temperature (C): 15.4 | Humidity (%): 38 | Wind Speed (km/h): 11.6 | Day: Friday
<start>
| Location | Temperature (C) | Humidity (%) | Wind Speed (km/h) | Day |
| --- | --- | --- | --- | --- |
| Chicago | 24.9 | 26 | 11.0 | Friday |
| Denver | -9.6 | 80 | 9.5 | Thursday |
| Los Angeles | 11.3 | 50 | 29.7 | Thursday |
| Seattle | 21.1 | 21 | 23.1 | Wednesday |
| New York | -2.2 | 84 | 1.4 | Thursday |
| New York | -3.8 | 44 | 5.5 | Thursday |
| Los Angeles | 1.7 | 100 | 5.9 | Saturday |
| Los Angeles | 32.4 | 96 | 24.2 | Wednesday |
| Denver | 22.3 | 23 | 21.0 | Monday |
| Denver | 15.4 | 38 | 11.6 | Friday |
<end>Transform this CSV structure to a markdown format:
Cache Hit Ratio (%),Connection Count,Average Latency (ms)
74.91,383,15.99
84.59,332,37.78
78.59,267,73.57
<start>
| Cache Hit Ratio (%) | Connection Count | Average Latency (ms) |
| --- | --- | --- |
| 74.91 | 383 | 15.99 |
| 84.59 | 332 | 37.78 |
| 78.59 | 267 | 73.57 |
<end>Transform this csv structure to a YAML format:
Condition,Temperature (C),Wind Speed (km/h)
Foggy,-8.2,14.1
Foggy,16.0,10.3
Windy,34.8,3.0
Sunny,29.9,12.7
<start>
- Condition: Foggy
  Temperature (C): -8.2
  Wind Speed (km/h): 14.1
- Condition: Foggy
  Temperature (C): 16.0
  Wind Speed (km/h): 10.3
- Condition: Windy
  Temperature (C): 34.8
  Wind Speed (km/h): 3.0
- Condition: Sunny
  Temperature (C): 29.9
  Wind Speed (km/h): 12.7
<end>Convert this yml to Plain text:
- Duration (hours): 24.9
  End Location: San Francisco
  Start Location: Miami
- Duration (hours): 22.0
  End Location: Denver
  Start Location: Los Angeles
- Duration (hours): 63.9
  End Location: Denver
  Start Location: Houston
- Duration (hours): 40.0
  End Location: Houston
  Start Location: Denver
- Duration (hours): 7.9
  End Location: Houston
  Start Location: Chicago
- Duration (hours): 15.5
  End Location: New York
  Start Location: Houston
- Duration (hours): 38.3
  End Location: New York
  Start Location: Houston
- Duration (hours): 21.9
  End Location: Los Angeles
  Start Location: Chicago
- Duration (hours): 8.7
  End Location: Phoenix
  Start Location: Los Angeles
- Duration (hours): 46.3
  End Location: Denver
  Start Location: Phoenix
<start>
Start Location: Miami | End Location: San Francisco | Duration (hours): 24.9
Start Location: Los Angeles | End Location: Denver | Duration (hours): 22.0
Start Location: Houston | End Location: Denver | Duration (hours): 63.9
Start Location: Denver | End Location: Houston | Duration (hours): 40.0
Start Location: Chicago | End Location: Houston | Duration (hours): 7.9
Start Location: Houston | End Location: New York | Duration (hours): 15.5
Start Location: Houston | End Location: New York | Duration (hours): 38.3
Start Location: Chicago | End Location: Los Angeles | Duration (hours): 21.9
Start Location: Los Angeles | End Location: Phoenix | Duration (hours): 8.7
Start Location: Phoenix | End Location: Denver | Duration (hours): 46.3
<end>Here's some MARKDOWN data, can you convert it to CSV?
| Director | Box Office Earnings (M) |
| --- | --- |
| Mara Moonshadow | 501.85 |
| Mara Moonshadow | 784.44 |
| Mara Moonshadow | 186.43 |
| Talon Blackthorn | 768.9 |<start>
Director,Box Office Earnings (M)
Mara Moonshadow,501.85
Mara Moonshadow,784.44
Mara Moonshadow,186.43
Talon Blackthorn,768.9
<end>Here's some CSV data, can you convert it to Markdown?
Database Name,Cache Hit Ratio (%),Connection Count,Average Latency (ms),Timestamp
LogsDB,71.31,247,43.69,2021-12-18 20:45:32
MetricsDB,70.04,241,40.72,2022-05-01 16:45:22
SalesDB,82.96,10,3.34,2022-09-04 22:15:04
<start>
| Database Name | Cache Hit Ratio (%) | Connection Count | Average Latency (ms) | Timestamp |
| --- | --- | --- | --- | --- |
| LogsDB | 71.31 | 247 | 43.69 | 2021-12-18 20:45:32 |
| MetricsDB | 70.04 | 241 | 40.72 | 2022-05-01 16:45:22 |
| SalesDB | 82.96 | 10 | 3.34 | 2022-09-04 22:15:04 |
<end>Transform this YAML structure to a MARKDOWN format:
- Average Latency (ms): 38.3
  Database Name: LogsDB
  Queries per Second: 2064.56
- Average Latency (ms): 52.91
  Database Name: SessionsDB
  Queries per Second: 401.33
- Average Latency (ms): 18.74
  Database Name: ProductsDB
  Queries per Second: 1834.32
- Average Latency (ms): 96.61
  Database Name: UserDB
  Queries per Second: 557.04
<start>
| Database Name | Queries per Second | Average Latency (ms) |
| --- | --- | --- |
| LogsDB | 2064.56 | 38.3 |
| SessionsDB | 401.33 | 52.91 |
| ProductsDB | 1834.32 | 18.74 |
| UserDB | 557.04 | 96.61 |
<end>Here's some csv data, can you convert it to markdown?
Location,Temperature (C),Humidity (%),Wind Speed (km/h),Day
Miami,-4.6,28,0.8,Tuesday
Seattle,24.2,28,21.1,Monday
New York,23.4,64,12.6,Thursday
<start>
| Location | Temperature (C) | Humidity (%) | Wind Speed (km/h) | Day |
| --- | --- | --- | --- | --- |
| Miami | -4.6 | 28 | 0.8 | Tuesday |
| Seattle | 24.2 | 28 | 21.1 | Monday |
| New York | 23.4 | 64 | 12.6 | Thursday |
<end>Can you change this json into yaml?
[
    {
        "Product Name": "Device",
        "SKU": "SKU-1086",
        "Price": 257.5,
        "Stock Quantity": 388
    },
    {
        "Product Name": "Gizmo",
        "SKU": "SKU-1035",
        "Price": 241.3,
        "Stock Quantity": 428
    },
    {
        "Product Name": "Device",
        "SKU": "SKU-1094",
        "Price": 271.1,
        "Stock Quantity": 317
    },
    {
        "Product Name": "Doohickey",
        "SKU": "SKU-1062",
        "Price": 76.84,
        "Stock Quantity": 450
    },
    {
        "Product Name": "Instrument",
        "SKU": "SKU-1006",
        "Price": 50.87,
        "Stock Quantity": 380
    },
    {
        "Product Name": "Gadget",
        "SKU": "SKU-1017",
        "Price": 468.2,
        "Stock Quantity": 474
    },
    {
        "Product Name": "Thingamajig",
        "SKU": "SKU-1039",
        "Price": 353.62,
        "Stock Quantity": 242
    }
]<start>
- Price: 257.5
  Product Name: Device
  SKU: SKU-1086
  Stock Quantity: 388
- Price: 241.3
  Product Name: Gizmo
  SKU: SKU-1035
  Stock Quantity: 428
- Price: 271.1
  Product Name: Device
  SKU: SKU-1094
  Stock Quantity: 317
- Price: 76.84
  Product Name: Doohickey
  SKU: SKU-1062
  Stock Quantity: 450
- Price: 50.87
  Product Name: Instrument
  SKU: SKU-1006
  Stock Quantity: 380
- Price: 468.2
  Product Name: Gadget
  SKU: SKU-1017
  Stock Quantity: 474
- Price: 353.62
  Product Name: Thingamajig
  SKU: SKU-1039
  Stock Quantity: 242
<end>Transform this json structure to a markdown format:
[
    {
        "Company": "FinanceTrust",
        "Open Price": 1405.23,
        "Close Price": 533.1,
        "Low Price": 420.38,
        "Volume": 477165
    },
    {
        "Company": "TechnoCorp",
        "Open Price": 368.87,
        "Close Price": 1087.5,
        "Low Price": 368.87,
        "Volume": 8345807
    },
    {
        "Company": "GreenEnergy",
        "Open Price": 698.08,
        "Close Price": 422.44,
        "Low Price": 422.44,
        "Volume": 351560
    },
    {
        "Company": "GreenEnergy",
        "Open Price": 596.0,
        "Close Price": 686.65,
        "Low Price": 301.2,
        "Volume": 3399240
    },
    {
        "Company": "GreenEnergy",
        "Open Price": 187.87,
        "Close Price": 665.65,
        "Low Price": 187.87,
        "Volume": 2798264
    },
    {
        "Company": "AeroSystems",
        "Open Price": 1005.11,
        "Close Price": 1187.96,
        "Low Price": 735.1,
        "Volume": 4116856
    }
]<start>
| Company | Open Price | Close Price | Low Price | Volume |
| --- | --- | --- | --- | --- |
| FinanceTrust | 1405.23 | 533.1 | 420.38 | 477165 |
| TechnoCorp | 368.87 | 1087.5 | 368.87 | 8345807 |
| GreenEnergy | 698.08 | 422.44 | 422.44 | 351560 |
| GreenEnergy | 596.0 | 686.65 | 301.2 | 3399240 |
| GreenEnergy | 187.87 | 665.65 | 187.87 | 2798264 |
| AeroSystems | 1005.11 | 1187.96 | 735.1 | 4116856 |
<end>Here's some yml data, can you convert it to Csv?
- Category: Sports
  Price: 307.97
  Product Name: Device
  SKU: SKU-1098
  Stock Quantity: 129
  Supplier Name: Wayne Enterprises
- Category: Toys
  Price: 347.75
  Product Name: Widget
  SKU: SKU-1000
  Stock Quantity: 200
  Supplier Name: Wayne Enterprises
- Category: Electronics
  Price: 71.42
  Product Name: Whatchamacallit
  SKU: SKU-1062
  Stock Quantity: 444
  Supplier Name: ACME Corp
<start>
Product Name,SKU,Price,Stock Quantity,Category,Supplier Name
Device,SKU-1098,307.97,129,Sports,Wayne Enterprises
Widget,SKU-1000,347.75,200,Toys,Wayne Enterprises
Whatchamacallit,SKU-1062,71.42,444,Electronics,ACME Corp
<end>Here's some YML data, can you convert it to Plain text?
- Box Office Earnings (M): 427.28
  Director: Zara Stormrider
  Genre: Action
  Release Year: 1996
  Title: Escape from Earth
- Box Office Earnings (M): 16.03
  Director: Cade Firebrand
  Genre: Sci-Fi
  Release Year: 1976
  Title: Dreamwalker
- Box Office Earnings (M): 152.21
  Director: Mara Moonshadow
  Genre: Fantasy
  Release Year: 2008
  Title: The Endless Horizon
- Box Office Earnings (M): 56.38
  Director: Mara Moonshadow
  Genre: Sci-Fi
  Release Year: 1979
  Title: The Final Voyage
- Box Office Earnings (M): 313.2
  Director: Aria Ravenwood
  Genre: Action
  Release Year: 2011
  Title: Edge of Infinity
- Box Office Earnings (M): 924.97
  Director: Orin Shadowalker
  Genre: Action
  Release Year: 2015
  Title: The Final Voyage
- Box Office Earnings (M): 538.38
  Director: Aria Ravenwood
  Genre: Drama
  Release Year: 1996
  Title: The Final Voyage
- Box Office Earnings (M): 701.15
  Director: Rylan Frostblade
  Genre: Sci-Fi
  Release Year: 1989
  Title: The Great Expedition
- Box Office Earnings (M): 990.11
  Director: Aria Ravenwood
  Genre: Thriller
  Release Year: 1975
  Title: Dreamwalker
<start>
Title: Escape from Earth | Director: Zara Stormrider | Genre: Action | Release Year: 1996 | Box Office Earnings (M): 427.28
Title: Dreamwalker | Director: Cade Firebrand | Genre: Sci-Fi | Release Year: 1976 | Box Office Earnings (M): 16.03
Title: The Endless Horizon | Director: Mara Moonshadow | Genre: Fantasy | Release Year: 2008 | Box Office Earnings (M): 152.21
Title: The Final Voyage | Director: Mara Moonshadow | Genre: Sci-Fi | Release Year: 1979 | Box Office Earnings (M): 56.38
Title: Edge of Infinity | Director: Aria Ravenwood | Genre: Action | Release Year: 2011 | Box Office Earnings (M): 313.2
Title: The Final Voyage | Director: Orin Shadowalker | Genre: Action | Release Year: 2015 | Box Office Earnings (M): 924.97
Title: The Final Voyage | Director: Aria Ravenwood | Genre: Drama | Release Year: 1996 | Box Office Earnings (M): 538.38
Title: The Great Expedition | Director: Rylan Frostblade | Genre: Sci-Fi | Release Year: 1989 | Box Office Earnings (M): 701.15
Title: Dreamwalker | Director: Aria Ravenwood | Genre: Thriller | Release Year: 1975 | Box Office Earnings (M): 990.11
<end>Please transform the following Plain text data into MARKDOWN:
Product Name: Gizmo | SKU: SKU-1072 | Price: 66.96
Product Name: Doohickey | SKU: SKU-1031 | Price: 414.23
Product Name: Instrument | SKU: SKU-1080 | Price: 184.77
<start>
| Product Name | SKU | Price |
| --- | --- | --- |
| Gizmo | SKU-1072 | 66.96 |
| Doohickey | SKU-1031 | 414.23 |
| Instrument | SKU-1080 | 184.77 |
<end>Transform this YML structure to a JSON format:
- Age: 30
  Birth Month: March
  City: Houston
  Income: 450000
  Name: Kylie
- Age: 56
  Birth Month: September
  City: San Jose
  Income: 55000
  Name: Aimee
- Age: 65
  Birth Month: October
  City: Chicago
  Income: 185000
  Name: Tanner
- Age: 69
  Birth Month: June
  City: Milwaukee
  Income: 450000
  Name: Violet
- Age: 40
  Birth Month: July
  City: Houston
  Income: 115000
  Name: Brandy
- Age: 34
  Birth Month: May
  City: San Antonio
  Income: 285000
  Name: Devin
- Age: 63
  Birth Month: February
  City: Indianapolis
  Income: 85000
  Name: Tucker
- Age: 27
  Birth Month: October
  City: Louisville
  Income: 115000
  Name: Londyn
- Age: 39
  Birth Month: September
  City: Dallas
  Income: 250000
  Name: Roxanne
- Age: 60
  Birth Month: August
  City: Detroit
  Income: 440000
  Name: Trinity
<start>
[
    {
        "Name": "Kylie",
        "Age": 30,
        "Birth Month": "March",
        "City": "Houston",
        "Income": 450000
    },
    {
        "Name": "Aimee",
        "Age": 56,
        "Birth Month": "September",
        "City": "San Jose",
        "Income": 55000
    },
    {
        "Name": "Tanner",
        "Age": 65,
        "Birth Month": "October",
        "City": "Chicago",
        "Income": 185000
    },
    {
        "Name": "Violet",
        "Age": 69,
        "Birth Month": "June",
        "City": "Milwaukee",
        "Income": 450000
    },
    {
        "Name": "Brandy",
        "Age": 40,
        "Birth Month": "July",
        "City": "Houston",
        "Income": 115000
    },
    {
        "Name": "Devin",
        "Age": 34,
        "Birth Month": "May",
        "City": "San Antonio",
        "Income": 285000
    },
    {
        "Name": "Tucker",
        "Age": 63,
        "Birth Month": "February",
        "City": "Indianapolis",
        "Income": 85000
    },
    {
        "Name": "Londyn",
        "Age": 27,
        "Birth Month": "October",
        "City": "Louisville",
        "Income": 115000
    },
    {
        "Name": "Roxanne",
        "Age": 39,
        "Birth Month": "September",
        "City": "Dallas",
        "Income": 250000
    },
    {
        "Name": "Trinity",
        "Age": 60,
        "Birth Month": "August",
        "City": "Detroit",
        "Income": 440000
    }
]
<end>Can you change this csv into Plain text?
Trip Name,Start Location,End Location,Duration (hours),Fuel Used (gallons)
Lakeside Retreat,New York,Houston,24.6,38.5
Highway Odyssey,San Francisco,Denver,2.2,87.7
Mountain Adventure,Chicago,Denver,44.9,73.4
Canyon Trek,New York,Houston,21.8,37.7
Highway Odyssey,San Francisco,Denver,13.6,20.6
Canyon Trek,Los Angeles,Phoenix,48.7,38.9
Forest Journey,San Francisco,Miami,50.0,80.8
Highway Odyssey,Houston,Miami,54.4,60.8
<start>
Trip Name: Lakeside Retreat | Start Location: New York | End Location: Houston | Duration (hours): 24.6 | Fuel Used (gallons): 38.5
Trip Name: Highway Odyssey | Start Location: San Francisco | End Location: Denver | Duration (hours): 2.2 | Fuel Used (gallons): 87.7
Trip Name: Mountain Adventure | Start Location: Chicago | End Location: Denver | Duration (hours): 44.9 | Fuel Used (gallons): 73.4
Trip Name: Canyon Trek | Start Location: New York | End Location: Houston | Duration (hours): 21.8 | Fuel Used (gallons): 37.7
Trip Name: Highway Odyssey | Start Location: San Francisco | End Location: Denver | Duration (hours): 13.6 | Fuel Used (gallons): 20.6
Trip Name: Canyon Trek | Start Location: Los Angeles | End Location: Phoenix | Duration (hours): 48.7 | Fuel Used (gallons): 38.9
Trip Name: Forest Journey | Start Location: San Francisco | End Location: Miami | Duration (hours): 50.0 | Fuel Used (gallons): 80.8
Trip Name: Highway Odyssey | Start Location: Houston | End Location: Miami | Duration (hours): 54.4 | Fuel Used (gallons): 60.8
<end>Transform this plain text structure to a Yml format:
Trip Name: Canyon Trek | Start Location: Denver | End Location: San Francisco | Distance (miles): 1391.0 | Fuel Used (gallons): 47.1
Trip Name: Valley Voyage | Start Location: Houston | End Location: Miami | Distance (miles): 1658.6 | Fuel Used (gallons): 98.7
Trip Name: Lakeside Retreat | Start Location: Houston | End Location: San Francisco | Distance (miles): 2490.5 | Fuel Used (gallons): 61.8
Trip Name: Desert Drive | Start Location: Phoenix | End Location: Chicago | Distance (miles): 1807.5 | Fuel Used (gallons): 27.7
Trip Name: Historic Route | Start Location: Chicago | End Location: Los Angeles | Distance (miles): 1805.4 | Fuel Used (gallons): 46.6
Trip Name: City Explorer | Start Location: Miami | End Location: Los Angeles | Distance (miles): 980.3 | Fuel Used (gallons): 96.0
Trip Name: Canyon Trek | Start Location: Chicago | End Location: San Francisco | Distance (miles): 2585.2 | Fuel Used (gallons): 95.1
Trip Name: City Explorer | Start Location: Chicago | End Location: Phoenix | Distance (miles): 674.4 | Fuel Used (gallons): 39.7
Trip Name: Forest Journey | Start Location: Chicago | End Location: Miami | Distance (miles): 567.8 | Fuel Used (gallons): 99.1
Trip Name: Highway Odyssey | Start Location: Los Angeles | End Location: Phoenix | Distance (miles): 1492.1 | Fuel Used (gallons): 34.8
<start>
- Distance (miles): 1391.0
  End Location: San Francisco
  Fuel Used (gallons): 47.1
  Start Location: Denver
  Trip Name: Canyon Trek
- Distance (miles): 1658.6
  End Location: Miami
  Fuel Used (gallons): 98.7
  Start Location: Houston
  Trip Name: Valley Voyage
- Distance (miles): 2490.5
  End Location: San Francisco
  Fuel Used (gallons): 61.8
  Start Location: Houston
  Trip Name: Lakeside Retreat
- Distance (miles): 1807.5
  End Location: Chicago
  Fuel Used (gallons): 27.7
  Start Location: Phoenix
  Trip Name: Desert Drive
- Distance (miles): 1805.4
  End Location: Los Angeles
  Fuel Used (gallons): 46.6
  Start Location: Chicago
  Trip Name: Historic Route
- Distance (miles): 980.3
  End Location: Los Angeles
  Fuel Used (gallons): 96.0
  Start Location: Miami
  Trip Name: City Explorer
- Distance (miles): 2585.2
  End Location: San Francisco
  Fuel Used (gallons): 95.1
  Start Location: Chicago
  Trip Name: Canyon Trek
- Distance (miles): 674.4
  End Location: Phoenix
  Fuel Used (gallons): 39.7
  Start Location: Chicago
  Trip Name: City Explorer
- Distance (miles): 567.8
  End Location: Miami
  Fuel Used (gallons): 99.1
  Start Location: Chicago
  Trip Name: Forest Journey
- Distance (miles): 1492.1
  End Location: Phoenix
  Fuel Used (gallons): 34.8
  Start Location: Los Angeles
  Trip Name: Highway Odyssey
<end>Convert this csv to MARKDOWN:
Company,Date,Open Price,High Price,Low Price,Volume
RetailWorld,2013-03-22,1091.54,1246.92,141.18,7463330
RetailWorld,2012-06-02,249.57,1407.81,249.57,3286369
BioLife,2017-08-20,698.28,1190.8,698.28,9645982
MediaGroup,2017-10-02,1372.24,1372.24,670.17,3530988
FoodChain,2010-06-01,1239.31,1239.31,200.29,5755635
AutoMotive,2011-10-26,565.45,1255.69,565.45,2532957
AeroSystems,2011-11-13,944.85,1240.37,318.0,7602130
HealthGen,2015-03-18,748.47,1480.1,748.47,2532957
FoodChain,2010-10-06,296.89,1460.57,296.89,4017808
<start>
| Company | Date | Open Price | High Price | Low Price | Volume |
| --- | --- | --- | --- | --- | --- |
| RetailWorld | 2013-03-22 | 1091.54 | 1246.92 | 141.18 | 7463330 |
| RetailWorld | 2012-06-02 | 249.57 | 1407.81 | 249.57 | 3286369 |
| BioLife | 2017-08-20 | 698.28 | 1190.8 | 698.28 | 9645982 |
| MediaGroup | 2017-10-02 | 1372.24 | 1372.24 | 670.17 | 3530988 |
| FoodChain | 2010-06-01 | 1239.31 | 1239.31 | 200.29 | 5755635 |
| AutoMotive | 2011-10-26 | 565.45 | 1255.69 | 565.45 | 2532957 |
| AeroSystems | 2011-11-13 | 944.85 | 1240.37 | 318.0 | 7602130 |
| HealthGen | 2015-03-18 | 748.47 | 1480.1 | 748.47 | 2532957 |
| FoodChain | 2010-10-06 | 296.89 | 1460.57 | 296.89 | 4017808 |
<end>Transform this Yaml structure to a PLAIN TEXT format:
- Birth Month: November
  City: Las Vegas
  Income: 470000
  Name: Mckenzie
- Birth Month: April
  City: Denver
  Income: 445000
  Name: Spencer
- Birth Month: July
  City: Las Vegas
  Income: 165000
  Name: Stefanie
- Birth Month: January
  City: Charlotte
  Income: 420000
  Name: Ashlyn
- Birth Month: August
  City: Oklahoma City
  Income: 110000
  Name: Abraham
- Birth Month: September
  City: Detroit
  Income: 250000
  Name: Jackson
<start>
Name: Mckenzie | Birth Month: November | City: Las Vegas | Income: 470000
Name: Spencer | Birth Month: April | City: Denver | Income: 445000
Name: Stefanie | Birth Month: July | City: Las Vegas | Income: 165000
Name: Ashlyn | Birth Month: January | City: Charlotte | Income: 420000
Name: Abraham | Birth Month: August | City: Oklahoma City | Income: 110000
Name: Jackson | Birth Month: September | City: Detroit | Income: 250000
<end>Transform this Json structure to a Plain text format:
[
    {
        "Name": "Maddox",
        "City": "Detroit",
        "Income": 90000
    },
    {
        "Name": "Marjorie",
        "City": "Columbus",
        "Income": 495000
    },
    {
        "Name": "Gerard",
        "City": "Milwaukee",
        "Income": 290000
    }
]<start>
Name: Maddox | City: Detroit | Income: 90000
Name: Marjorie | City: Columbus | Income: 495000
Name: Gerard | City: Milwaukee | Income: 290000
<end>Can you change this yaml into PLAIN TEXT?
- Market Cap: Small Cap
  Quarter: Q1
  Sector: Automotive
- Market Cap: Mega Cap
  Quarter: Q2
  Sector: Finance
- Market Cap: Large Cap
  Quarter: Q4
  Sector: Retail
<start>
Sector: Automotive | Market Cap: Small Cap | Quarter: Q1
Sector: Finance | Market Cap: Mega Cap | Quarter: Q2
Sector: Retail | Market Cap: Large Cap | Quarter: Q4
<end>Please transform the following Markdown data into json:
| Trip Name | End Location | Fuel Used (gallons) |
| --- | --- | --- |
| City Explorer | San Francisco | 88.1 |
| Forest Journey | New York | 75.0 |
| Mountain Adventure | Denver | 31.1 |
| City Explorer | Houston | 31.0 |
| Forest Journey | San Francisco | 87.5 |
| Valley Voyage | San Francisco | 18.8 |
| Mountain Adventure | Chicago | 7.5 |<start>
[
    {
        "Trip Name": "City Explorer",
        "End Location": "San Francisco",
        "Fuel Used (gallons)": 88.1
    },
    {
        "Trip Name": "Forest Journey",
        "End Location": "New York",
        "Fuel Used (gallons)": 75.0
    },
    {
        "Trip Name": "Mountain Adventure",
        "End Location": "Denver",
        "Fuel Used (gallons)": 31.1
    },
    {
        "Trip Name": "City Explorer",
        "End Location": "Houston",
        "Fuel Used (gallons)": 31.0
    },
    {
        "Trip Name": "Forest Journey",
        "End Location": "San Francisco",
        "Fuel Used (gallons)": 87.5
    },
    {
        "Trip Name": "Valley Voyage",
        "End Location": "San Francisco",
        "Fuel Used (gallons)": 18.8
    },
    {
        "Trip Name": "Mountain Adventure",
        "End Location": "Chicago",
        "Fuel Used (gallons)": 7.5
    }
]
<end>Here's some YML data, can you convert it to markdown?
- Rating: 1
  Restaurant Name: Burger Haven
- Rating: 4
  Restaurant Name: Sushi World
- Rating: 2
  Restaurant Name: The Steakhouse
- Rating: 2
  Restaurant Name: Pasta Palace
- Rating: 2
  Restaurant Name: Sushi World
- Rating: 1
  Restaurant Name: Taco Town
- Rating: 2
  Restaurant Name: The Steakhouse
- Rating: 2
  Restaurant Name: Curry Corner
- Rating: 1
  Restaurant Name: Pizza Planet
<start>
| Restaurant Name | Rating |
| --- | --- |
| Burger Haven | 1 |
| Sushi World | 4 |
| The Steakhouse | 2 |
| Pasta Palace | 2 |
| Sushi World | 2 |
| Taco Town | 1 |
| The Steakhouse | 2 |
| Curry Corner | 2 |
| Pizza Planet | 1 |
<end>Convert this markdown to CSV:
| Location | Condition | Humidity (%) | Day |
| --- | --- | --- | --- |
| Denver | Windy | 66 | Monday |
| Phoenix | Snowy | 88 | Thursday |
| Los Angeles | Stormy | 71 | Sunday |
| Houston | Foggy | 55 | Saturday |
| Denver | Foggy | 64 | Saturday |
| Miami | Sunny | 25 | Monday |<start>
Location,Condition,Humidity (%),Day
Denver,Windy,66,Monday
Phoenix,Snowy,88,Thursday
Los Angeles,Stormy,71,Sunday
Houston,Foggy,55,Saturday
Denver,Foggy,64,Saturday
Miami,Sunny,25,Monday
<end>Convert this Plain text to JSON:
Name: Shaun | Age: 41 | Income: 305000
Name: Grant | Age: 62 | Income: 170000
Name: Dennis | Age: 54 | Income: 440000
Name: Tyler | Age: 46 | Income: 265000
Name: Jason | Age: 23 | Income: 275000
Name: Quinn | Age: 46 | Income: 360000
<start>
[
    {
        "Name": "Shaun",
        "Age": 41,
        "Income": 305000
    },
    {
        "Name": "Grant",
        "Age": 62,
        "Income": 170000
    },
    {
        "Name": "Dennis",
        "Age": 54,
        "Income": 440000
    },
    {
        "Name": "Tyler",
        "Age": 46,
        "Income": 265000
    },
    {
        "Name": "Jason",
        "Age": 23,
        "Income": 275000
    },
    {
        "Name": "Quinn",
        "Age": 46,
        "Income": 360000
    }
]
<end>Here's some yaml data, can you convert it to markdown?
- Cuisine: Mediterranean
  Location: Phoenix
  Rating: 3
  Restaurant Name: Burger Haven
- Cuisine: Mediterranean
  Location: Chicago
  Rating: 1
  Restaurant Name: Pasta Palace
- Cuisine: Mediterranean
  Location: Los Angeles
  Rating: 4
  Restaurant Name: Curry Corner
- Cuisine: American
  Location: New York
  Rating: 5
  Restaurant Name: The Steakhouse
- Cuisine: Mexican
  Location: Miami
  Rating: 1
  Restaurant Name: Curry Corner
- Cuisine: Mediterranean
  Location: Chicago
  Rating: 3
  Restaurant Name: BBQ Barn
- Cuisine: Chinese
  Location: New York
  Rating: 4
  Restaurant Name: BBQ Barn
- Cuisine: Italian
  Location: Phoenix
  Rating: 4
  Restaurant Name: Pasta Palace
<start>
| Restaurant Name | Cuisine | Location | Rating |
| --- | --- | --- | --- |
| Burger Haven | Mediterranean | Phoenix | 3 |
| Pasta Palace | Mediterranean | Chicago | 1 |
| Curry Corner | Mediterranean | Los Angeles | 4 |
| The Steakhouse | American | New York | 5 |
| Curry Corner | Mexican | Miami | 1 |
| BBQ Barn | Mediterranean | Chicago | 3 |
| BBQ Barn | Chinese | New York | 4 |
| Pasta Palace | Italian | Phoenix | 4 |
<end>Transform this csv structure to a plain text format:
Title,Author
A Journey Through Time,Luna Silverleaf
The Last Sky,Rowan Ashborne
Echoes of Eternity,Luna Silverleaf
Echoes of Eternity,Isla Windrider
The Forgotten World,Sylvia Nightshade
Tales of the Brave,Orion Frostblade
<start>
Title: A Journey Through Time | Author: Luna Silverleaf
Title: The Last Sky | Author: Rowan Ashborne
Title: Echoes of Eternity | Author: Luna Silverleaf
Title: Echoes of Eternity | Author: Isla Windrider
Title: The Forgotten World | Author: Sylvia Nightshade
Title: Tales of the Brave | Author: Orion Frostblade
<end>Convert this plain text to markdown:
Title: Echoes of Eternity | Author: Luna Silverleaf
Title: The Forgotten World | Author: Elara Moonshadow
Title: The Forgotten World | Author: Galen Starfire
Title: Whispers of the Abyss | Author: Galen Starfire
Title: Whispers of the Abyss | Author: Kara Firebrand
Title: Shadows of Solitude | Author: Kara Firebrand
Title: The Last Sky | Author: Sylvia Nightshade
Title: A Journey Through Time | Author: Sylvia Nightshade
Title: Shadows of Solitude | Author: Sylvia Nightshade
Title: The Last Sky | Author: Isla Windrider
<start>
| Title | Author |
| --- | --- |
| Echoes of Eternity | Luna Silverleaf |
| The Forgotten World | Elara Moonshadow |
| The Forgotten World | Galen Starfire |
| Whispers of the Abyss | Galen Starfire |
| Whispers of the Abyss | Kara Firebrand |
| Shadows of Solitude | Kara Firebrand |
| The Last Sky | Sylvia Nightshade |
| A Journey Through Time | Sylvia Nightshade |
| Shadows of Solitude | Sylvia Nightshade |
| The Last Sky | Isla Windrider |
<end>Can you change this yaml into MARKDOWN?
- Day: Friday
  Humidity (%): 50
  Location: Miami
  Temperature (C): 4.3
  Wind Speed (km/h): 21.3
- Day: Wednesday
  Humidity (%): 36
  Location: Denver
  Temperature (C): 12.8
  Wind Speed (km/h): 17.7
- Day: Monday
  Humidity (%): 73
  Location: Seattle
  Temperature (C): 36.6
  Wind Speed (km/h): 26.2
- Day: Tuesday
  Humidity (%): 98
  Location: Miami
  Temperature (C): -8.7
  Wind Speed (km/h): 18.4
<start>
| Location | Temperature (C) | Humidity (%) | Wind Speed (km/h) | Day |
| --- | --- | --- | --- | --- |
| Miami | 4.3 | 50 | 21.3 | Friday |
| Denver | 12.8 | 36 | 17.7 | Wednesday |
| Seattle | 36.6 | 73 | 26.2 | Monday |
| Miami | -8.7 | 98 | 18.4 | Tuesday |
<end>Here's some Yml data, can you convert it to Csv?
- Price: 385.73
  Product Name: Gizmo
  SKU: SKU-1087
  Supplier Name: Wayne Enterprises
- Price: 46.91
  Product Name: Instrument
  SKU: SKU-1089
  Supplier Name: Globex
- Price: 64.84
  Product Name: Instrument
  SKU: SKU-1080
  Supplier Name: Wonka Industries
- Price: 202.61
  Product Name: Device
  SKU: SKU-1098
  Supplier Name: Umbrella Corp
- Price: 28.32
  Product Name: Gadget
  SKU: SKU-1018
  Supplier Name: Wonka Industries
- Price: 448.32
  Product Name: Contraption
  SKU: SKU-1034
  Supplier Name: ACME Corp
- Price: 197.19
  Product Name: Thingamajig
  SKU: SKU-1058
  Supplier Name: ACME Corp
- Price: 46.2
  Product Name: Contraption
  SKU: SKU-1054
  Supplier Name: Umbrella Corp
<start>
Product Name,SKU,Price,Supplier Name
Gizmo,SKU-1087,385.73,Wayne Enterprises
Instrument,SKU-1089,46.91,Globex
Instrument,SKU-1080,64.84,Wonka Industries
Device,SKU-1098,202.61,Umbrella Corp
Gadget,SKU-1018,28.32,Wonka Industries
Contraption,SKU-1034,448.32,ACME Corp
Thingamajig,SKU-1058,197.19,ACME Corp
Contraption,SKU-1054,46.2,Umbrella Corp
<end>Please transform the following Yaml data into plain text:
- Distance (miles): 1341.6
  End Location: Miami
  Fuel Used (gallons): 41.9
  Start Location: San Francisco
- Distance (miles): 1082.7
  End Location: San Francisco
  Fuel Used (gallons): 96.3
  Start Location: Los Angeles
- Distance (miles): 958.8
  End Location: New York
  Fuel Used (gallons): 46.9
  Start Location: Denver
- Distance (miles): 2664.7
  End Location: Denver
  Fuel Used (gallons): 46.0
  Start Location: Los Angeles
- Distance (miles): 170.6
  End Location: Los Angeles
  Fuel Used (gallons): 59.6
  Start Location: Denver
<start>
Start Location: San Francisco | End Location: Miami | Distance (miles): 1341.6 | Fuel Used (gallons): 41.9
Start Location: Los Angeles | End Location: San Francisco | Distance (miles): 1082.7 | Fuel Used (gallons): 96.3
Start Location: Denver | End Location: New York | Distance (miles): 958.8 | Fuel Used (gallons): 46.9
Start Location: Los Angeles | End Location: Denver | Distance (miles): 2664.7 | Fuel Used (gallons): 46.0
Start Location: Denver | End Location: Los Angeles | Distance (miles): 170.6 | Fuel Used (gallons): 59.6
<end>Please transform the following plain text data into YML:
Title: Edge of Infinity | Director: Drake Nightshade | Genre: Drama | Release Year: 2014 | Box Office Earnings (M): 111.08
Title: Starbound Odyssey | Director: Drake Nightshade | Genre: Adventure | Release Year: 1979 | Box Office Earnings (M): 684.76
Title: The Great Expedition | Director: Rylan Frostblade | Genre: Thriller | Release Year: 1988 | Box Office Earnings (M): 975.0
Title: Mystery of the Depths | Director: Rylan Frostblade | Genre: Comedy | Release Year: 2007 | Box Office Earnings (M): 449.31
Title: Beyond the Veil | Director: Mara Moonshadow | Genre: Thriller | Release Year: 2012 | Box Office Earnings (M): 458.16
Title: Rise of the Titans | Director: Orin Shadowalker | Genre: Fantasy | Release Year: 1983 | Box Office Earnings (M): 31.48
Title: The Endless Horizon | Director: Lira Silverleaf | Genre: Comedy | Release Year: 1973 | Box Office Earnings (M): 367.57
<start>
- Box Office Earnings (M): 111.08
  Director: Drake Nightshade
  Genre: Drama
  Release Year: 2014
  Title: Edge of Infinity
- Box Office Earnings (M): 684.76
  Director: Drake Nightshade
  Genre: Adventure
  Release Year: 1979
  Title: Starbound Odyssey
- Box Office Earnings (M): 975.0
  Director: Rylan Frostblade
  Genre: Thriller
  Release Year: 1988
  Title: The Great Expedition
- Box Office Earnings (M): 449.31
  Director: Rylan Frostblade
  Genre: Comedy
  Release Year: 2007
  Title: Mystery of the Depths
- Box Office Earnings (M): 458.16
  Director: Mara Moonshadow
  Genre: Thriller
  Release Year: 2012
  Title: Beyond the Veil
- Box Office Earnings (M): 31.48
  Director: Orin Shadowalker
  Genre: Fantasy
  Release Year: 1983
  Title: Rise of the Titans
- Box Office Earnings (M): 367.57
  Director: Lira Silverleaf
  Genre: Comedy
  Release Year: 1973
  Title: The Endless Horizon
<end>Here's some json data, can you convert it to plain text?
[
    {
        "Restaurant Name": "Burger Haven",
        "Rating": 2,
        "Price Range": "$$$$"
    },
    {
        "Restaurant Name": "Taco Town",
        "Rating": 1,
        "Price Range": "$$"
    },
    {
        "Restaurant Name": "Taco Town",
        "Rating": 4,
        "Price Range": "$$$$$"
    },
    {
        "Restaurant Name": "Pasta Palace",
        "Rating": 2,
        "Price Range": "$$"
    },
    {
        "Restaurant Name": "Sushi World",
        "Rating": 5,
        "Price Range": "$$$$"
    }
]<start>
Restaurant Name: Burger Haven | Rating: 2 | Price Range: $$$$
Restaurant Name: Taco Town | Rating: 1 | Price Range: $$
Restaurant Name: Taco Town | Rating: 4 | Price Range: $$$$$
Restaurant Name: Pasta Palace | Rating: 2 | Price Range: $$
Restaurant Name: Sushi World | Rating: 5 | Price Range: $$$$
<end>Please transform the following Plain text data into JSON:
Location: Denver | Condition: Cloudy | Temperature (C): 31.4 | Humidity (%): 80
Location: Miami | Condition: Stormy | Temperature (C): 6.9 | Humidity (%): 83
Location: Seattle | Condition: Stormy | Temperature (C): 10.0 | Humidity (%): 67
Location: Denver | Condition: Stormy | Temperature (C): -8.0 | Humidity (%): 31
Location: Denver | Condition: Windy | Temperature (C): -8.1 | Humidity (%): 72
Location: Seattle | Condition: Foggy | Temperature (C): 35.8 | Humidity (%): 30
Location: Chicago | Condition: Snowy | Temperature (C): 15.7 | Humidity (%): 88
<start>
[
    {
        "Location": "Denver",
        "Condition": "Cloudy",
        "Temperature (C)": 31.4,
        "Humidity (%)": 80
    },
    {
        "Location": "Miami",
        "Condition": "Stormy",
        "Temperature (C)": 6.9,
        "Humidity (%)": 83
    },
    {
        "Location": "Seattle",
        "Condition": "Stormy",
        "Temperature (C)": 10.0,
        "Humidity (%)": 67
    },
    {
        "Location": "Denver",
        "Condition": "Stormy",
        "Temperature (C)": -8.0,
        "Humidity (%)": 31
    },
    {
        "Location": "Denver",
        "Condition": "Windy",
        "Temperature (C)": -8.1,
        "Humidity (%)": 72
    },
    {
        "Location": "Seattle",
        "Condition": "Foggy",
        "Temperature (C)": 35.8,
        "Humidity (%)": 30
    },
    {
        "Location": "Chicago",
        "Condition": "Snowy",
        "Temperature (C)": 15.7,
        "Humidity (%)": 88
    }
]
<end>Please transform the following markdown data into csv:
| Company | High Price | Low Price | Volume |
| --- | --- | --- | --- |
| TechnoCorp | 1120.67 | 884.44 | 8467818 |
| AutoMotive | 1312.29 | 479.15 | 212424 |
| FinanceTrust | 1475.82 | 183.19 | 5171694 |<start>
Company,High Price,Low Price,Volume
TechnoCorp,1120.67,884.44,8467818
AutoMotive,1312.29,479.15,212424
FinanceTrust,1475.82,183.19,5171694
<end>Transform this json structure to a markdown format:
[
    {
        "Title": "The Final Voyage",
        "Director": "Cade Firebrand",
        "Genre": "Action",
        "Release Year": 2004,
        "Box Office Earnings (M)": 569.27
    },
    {
        "Title": "The Great Expedition",
        "Director": "Zara Stormrider",
        "Genre": "Horror",
        "Release Year": 1991,
        "Box Office Earnings (M)": 842.73
    },
    {
        "Title": "The Endless Horizon",
        "Director": "Zara Stormrider",
        "Genre": "Sci-Fi",
        "Release Year": 2003,
        "Box Office Earnings (M)": 458.73
    }
]<start>
| Title | Director | Genre | Release Year | Box Office Earnings (M) |
| --- | --- | --- | --- | --- |
| The Final Voyage | Cade Firebrand | Action | 2004 | 569.27 |
| The Great Expedition | Zara Stormrider | Horror | 1991 | 842.73 |
| The Endless Horizon | Zara Stormrider | Sci-Fi | 2003 | 458.73 |
<end>Here's some YAML data, can you convert it to plain text?
- Battery Level (%): 64.7
  Reading Value: 76.7
  Timestamp: '2022-10-27 11:57:59'
- Battery Level (%): 80.5
  Reading Value: 68.5
  Timestamp: '2022-08-14 19:37:38'
- Battery Level (%): 56.6
  Reading Value: 84.43
  Timestamp: '2023-12-16 02:12:00'
- Battery Level (%): 38.2
  Reading Value: 48.59
  Timestamp: '2021-06-13 21:04:37'
- Battery Level (%): 26.1
  Reading Value: 21.49
  Timestamp: '2023-05-16 03:01:30'
- Battery Level (%): 54.1
  Reading Value: 9.58
  Timestamp: '2023-03-26 08:41:06'
<start>
Battery Level (%): 64.7 | Reading Value: 76.7 | Timestamp: 2022-10-27 11:57:59
Battery Level (%): 80.5 | Reading Value: 68.5 | Timestamp: 2022-08-14 19:37:38
Battery Level (%): 56.6 | Reading Value: 84.43 | Timestamp: 2023-12-16 02:12:00
Battery Level (%): 38.2 | Reading Value: 48.59 | Timestamp: 2021-06-13 21:04:37
Battery Level (%): 26.1 | Reading Value: 21.49 | Timestamp: 2023-05-16 03:01:30
Battery Level (%): 54.1 | Reading Value: 9.58 | Timestamp: 2023-03-26 08:41:06
<end>Can you change this csv into yaml?
Name,Age,Birth Month,City,Income
Will,47,May,San Jose,85000
Georgia,29,April,Jacksonville,190000
Jeanne,29,May,Milwaukee,120000
Caitlyn,35,October,New York,305000
Deanna,54,March,New York,60000
Sonya,49,December,New York,345000
Beverly,23,May,Fort Worth,60000
Everly,64,January,Seattle,295000
<start>
- Age: 47
  Birth Month: May
  City: San Jose
  Income: 85000
  Name: Will
- Age: 29
  Birth Month: April
  City: Jacksonville
  Income: 190000
  Name: Georgia
- Age: 29
  Birth Month: May
  City: Milwaukee
  Income: 120000
  Name: Jeanne
- Age: 35
  Birth Month: October
  City: New York
  Income: 305000
  Name: Caitlyn
- Age: 54
  Birth Month: March
  City: New York
  Income: 60000
  Name: Deanna
- Age: 49
  Birth Month: December
  City: New York
  Income: 345000
  Name: Sonya
- Age: 23
  Birth Month: May
  City: Fort Worth
  Income: 60000
  Name: Beverly
- Age: 64
  Birth Month: January
  City: Seattle
  Income: 295000
  Name: Everly
<end>Can you change this csv into json?
Database Name,Queries per Second,Cache Hit Ratio (%),Connection Count,Timestamp
AnalyticsDB,3402.52,70.85,68,2023-12-02 21:27:42
UserDB,3055.56,86.22,14,2022-09-05 21:44:06
AnalyticsDB,723.54,90.2,90,2023-11-22 20:26:48
ProductsDB,1283.66,84.67,470,2022-06-08 20:00:44
SalesDB,644.79,73.35,445,2022-07-28 14:21:14
<start>
[
    {
        "Database Name": "AnalyticsDB",
        "Queries per Second": 3402.52,
        "Cache Hit Ratio (%)": 70.85,
        "Connection Count": 68,
        "Timestamp": "2023-12-02 21:27:42"
    },
    {
        "Database Name": "UserDB",
        "Queries per Second": 3055.56,
        "Cache Hit Ratio (%)": 86.22,
        "Connection Count": 14,
        "Timestamp": "2022-09-05 21:44:06"
    },
    {
        "Database Name": "AnalyticsDB",
        "Queries per Second": 723.54,
        "Cache Hit Ratio (%)": 90.2,
        "Connection Count": 90,
        "Timestamp": "2023-11-22 20:26:48"
    },
    {
        "Database Name": "ProductsDB",
        "Queries per Second": 1283.66,
        "Cache Hit Ratio (%)": 84.67,
        "Connection Count": 470,
        "Timestamp": "2022-06-08 20:00:44"
    },
    {
        "Database Name": "SalesDB",
        "Queries per Second": 644.79,
        "Cache Hit Ratio (%)": 73.35,
        "Connection Count": 445,
        "Timestamp": "2022-07-28 14:21:14"
    }
]
<end>Please transform the following JSON data into PLAIN TEXT:
[
    {
        "Database Name": "UserDB",
        "Cache Hit Ratio (%)": 94.76,
        "Connection Count": 231
    },
    {
        "Database Name": "ProductsDB",
        "Cache Hit Ratio (%)": 82.18,
        "Connection Count": 114
    },
    {
        "Database Name": "SalesDB",
        "Cache Hit Ratio (%)": 76.92,
        "Connection Count": 231
    },
    {
        "Database Name": "SessionsDB",
        "Cache Hit Ratio (%)": 71.51,
        "Connection Count": 80
    }
]<start>
Database Name: UserDB | Cache Hit Ratio (%): 94.76 | Connection Count: 231
Database Name: ProductsDB | Cache Hit Ratio (%): 82.18 | Connection Count: 114
Database Name: SalesDB | Cache Hit Ratio (%): 76.92 | Connection Count: 231
Database Name: SessionsDB | Cache Hit Ratio (%): 71.51 | Connection Count: 80
<end>Can you change this markdown into Csv?
| Company | Sector | Market Cap | Annual Revenue (B) | Quarter |
| --- | --- | --- | --- | --- |
| TechCorp | Technology | Mid Cap | 496.82 | Q3 |
| GlobalTrade | Retail | Small Cap | 468.99 | Q4 |
| HealthPlus | Retail | Mid Cap | 326.35 | Q1 |
| AeroSpace | Finance | Small Cap | 412.37 | Q1 |
| EcoEnergy | Technology | Small Cap | 226.76 | Q3 |<start>
Company,Sector,Market Cap,Annual Revenue (B),Quarter
TechCorp,Technology,Mid Cap,496.82,Q3
GlobalTrade,Retail,Small Cap,468.99,Q4
HealthPlus,Retail,Mid Cap,326.35,Q1
AeroSpace,Finance,Small Cap,412.37,Q1
EcoEnergy,Technology,Small Cap,226.76,Q3
<end>Convert this json to Plain text:
[
    {
        "SKU": "SKU-1016",
        "Price": 383.19,
        "Category": "Electronics"
    },
    {
        "SKU": "SKU-1037",
        "Price": 423.29,
        "Category": "Sports"
    },
    {
        "SKU": "SKU-1099",
        "Price": 196.42,
        "Category": "Toys"
    },
    {
        "SKU": "SKU-1019",
        "Price": 296.82,
        "Category": "Electronics"
    },
    {
        "SKU": "SKU-1001",
        "Price": 135.91,
        "Category": "Toys"
    },
    {
        "SKU": "SKU-1094",
        "Price": 150.87,
        "Category": "Electronics"
    }
]<start>
SKU: SKU-1016 | Price: 383.19 | Category: Electronics
SKU: SKU-1037 | Price: 423.29 | Category: Sports
SKU: SKU-1099 | Price: 196.42 | Category: Toys
SKU: SKU-1019 | Price: 296.82 | Category: Electronics
SKU: SKU-1001 | Price: 135.91 | Category: Toys
SKU: SKU-1094 | Price: 150.87 | Category: Electronics
<end>Please transform the following MARKDOWN data into Plain text:
| Company | Sector | Stock Price | Annual Revenue (B) | Quarter |
| --- | --- | --- | --- | --- |
| FinanceWorks | Technology | 318.94 | 132.42 | Q4 |
| GlobalTrade | Aerospace | 223.53 | 342.89 | Q4 |
| GlobalTrade | Biotech | 509.67 | 132.42 | Q4 |
| AutoDrive | Biotech | 211.06 | 276.15 | Q4 |<start>
Company: FinanceWorks | Sector: Technology | Stock Price: 318.94 | Annual Revenue (B): 132.42 | Quarter: Q4
Company: GlobalTrade | Sector: Aerospace | Stock Price: 223.53 | Annual Revenue (B): 342.89 | Quarter: Q4
Company: GlobalTrade | Sector: Biotech | Stock Price: 509.67 | Annual Revenue (B): 132.42 | Quarter: Q4
Company: AutoDrive | Sector: Biotech | Stock Price: 211.06 | Annual Revenue (B): 276.15 | Quarter: Q4
<end>Here's some JSON data, can you convert it to plain text?
[
    {
        "Location": "New York",
        "Condition": "Foggy",
        "Humidity (%)": 37
    },
    {
        "Location": "New York",
        "Condition": "Sunny",
        "Humidity (%)": 74
    },
    {
        "Location": "Denver",
        "Condition": "Snowy",
        "Humidity (%)": 48
    },
    {
        "Location": "Phoenix",
        "Condition": "Sunny",
        "Humidity (%)": 96
    },
    {
        "Location": "Miami",
        "Condition": "Snowy",
        "Humidity (%)": 22
    },
    {
        "Location": "Denver",
        "Condition": "Cloudy",
        "Humidity (%)": 75
    }
]<start>
Location: New York | Condition: Foggy | Humidity (%): 37
Location: New York | Condition: Sunny | Humidity (%): 74
Location: Denver | Condition: Snowy | Humidity (%): 48
Location: Phoenix | Condition: Sunny | Humidity (%): 96
Location: Miami | Condition: Snowy | Humidity (%): 22
Location: Denver | Condition: Cloudy | Humidity (%): 75
<end>Please transform the following yaml data into markdown:
- Genre: Historical
  Rating: 1.3
  Title: The Silent Grove
- Genre: Fantasy
  Rating: 3.7
  Title: The Crystal Key
- Genre: Thriller
  Rating: 4.3
  Title: Tales of the Brave
- Genre: Mystery
  Rating: 2.1
  Title: The Forgotten World
<start>
| Title | Genre | Rating |
| --- | --- | --- |
| The Silent Grove | Historical | 1.3 |
| The Crystal Key | Fantasy | 3.7 |
| Tales of the Brave | Thriller | 4.3 |
| The Forgotten World | Mystery | 2.1 |
<end>Can you change this plain text into YAML?
Queries per Second: 1279.52 | Cache Hit Ratio (%): 75.13 | Connection Count: 117 | Average Latency (ms): 43.46 | Timestamp: 2023-05-07 02:35:09
Queries per Second: 288.55 | Cache Hit Ratio (%): 76.1 | Connection Count: 231 | Average Latency (ms): 62.21 | Timestamp: 2022-06-19 15:04:25
Queries per Second: 4229.08 | Cache Hit Ratio (%): 91.22 | Connection Count: 115 | Average Latency (ms): 5.97 | Timestamp: 2023-12-18 09:52:46
Queries per Second: 1459.84 | Cache Hit Ratio (%): 92.85 | Connection Count: 462 | Average Latency (ms): 49.6 | Timestamp: 2021-02-07 01:47:34
Queries per Second: 1459.84 | Cache Hit Ratio (%): 71.0 | Connection Count: 351 | Average Latency (ms): 56.56 | Timestamp: 2023-01-02 08:34:42
Queries per Second: 4609.92 | Cache Hit Ratio (%): 98.37 | Connection Count: 237 | Average Latency (ms): 64.85 | Timestamp: 2023-05-01 23:59:52
Queries per Second: 1400.19 | Cache Hit Ratio (%): 71.49 | Connection Count: 162 | Average Latency (ms): 99.37 | Timestamp: 2021-11-27 18:23:50
Queries per Second: 3470.56 | Cache Hit Ratio (%): 96.37 | Connection Count: 436 | Average Latency (ms): 5.25 | Timestamp: 2021-02-08 02:17:02
<start>
- Average Latency (ms): 43.46
  Cache Hit Ratio (%): 75.13
  Connection Count: 117
  Queries per Second: 1279.52
  Timestamp: '2023-05-07 02:35:09'
- Average Latency (ms): 62.21
  Cache Hit Ratio (%): 76.1
  Connection Count: 231
  Queries per Second: 288.55
  Timestamp: '2022-06-19 15:04:25'
- Average Latency (ms): 5.97
  Cache Hit Ratio (%): 91.22
  Connection Count: 115
  Queries per Second: 4229.08
  Timestamp: '2023-12-18 09:52:46'
- Average Latency (ms): 49.6
  Cache Hit Ratio (%): 92.85
  Connection Count: 462
  Queries per Second: 1459.84
  Timestamp: '2021-02-07 01:47:34'
- Average Latency (ms): 56.56
  Cache Hit Ratio (%): 71.0
  Connection Count: 351
  Queries per Second: 1459.84
  Timestamp: '2023-01-02 08:34:42'
- Average Latency (ms): 64.85
  Cache Hit Ratio (%): 98.37
  Connection Count: 237
  Queries per Second: 4609.92
  Timestamp: '2023-05-01 23:59:52'
- Average Latency (ms): 99.37
  Cache Hit Ratio (%): 71.49
  Connection Count: 162
  Queries per Second: 1400.19
  Timestamp: '2021-11-27 18:23:50'
- Average Latency (ms): 5.25
  Cache Hit Ratio (%): 96.37
  Connection Count: 436
  Queries per Second: 3470.56
  Timestamp: '2021-02-08 02:17:02'
<end>Please transform the following plain text data into Markdown:
Cuisine: Chinese | Rating: 4 | Price Range: $$
Cuisine: Indian | Rating: 4 | Price Range: $$
Cuisine: Indian | Rating: 4 | Price Range: $$$$
Cuisine: Italian | Rating: 3 | Price Range: $$
Cuisine: Japanese | Rating: 1 | Price Range: $
Cuisine: Chinese | Rating: 5 | Price Range: $$$$
Cuisine: Italian | Rating: 4 | Price Range: $$$
Cuisine: Mediterranean | Rating: 3 | Price Range: $$
<start>
| Cuisine | Rating | Price Range |
| --- | --- | --- |
| Chinese | 4 | $$ |
| Indian | 4 | $$ |
| Indian | 4 | $$$$ |
| Italian | 3 | $$ |
| Japanese | 1 | $ |
| Chinese | 5 | $$$$ |
| Italian | 4 | $$$ |
| Mediterranean | 3 | $$ |
<end>Convert this Markdown to Plain text:
| Product Name | Price | Supplier Name |
| --- | --- | --- |
| Device | 334.59 | ACME Corp |
| Contraption | 129.3 | Wayne Enterprises |
| Device | 188.23 | Wonka Industries |
| Whatchamacallit | 455.77 | Wonka Industries |
| Thingamajig | 253.56 | Globex |
| Thingamajig | 396.29 | Wayne Enterprises |
| Whatchamacallit | 45.3 | Wonka Industries |
| Doohickey | 451.58 | Umbrella Corp |<start>
Product Name: Device | Price: 334.59 | Supplier Name: ACME Corp
Product Name: Contraption | Price: 129.3 | Supplier Name: Wayne Enterprises
Product Name: Device | Price: 188.23 | Supplier Name: Wonka Industries
Product Name: Whatchamacallit | Price: 455.77 | Supplier Name: Wonka Industries
Product Name: Thingamajig | Price: 253.56 | Supplier Name: Globex
Product Name: Thingamajig | Price: 396.29 | Supplier Name: Wayne Enterprises
Product Name: Whatchamacallit | Price: 45.3 | Supplier Name: Wonka Industries
Product Name: Doohickey | Price: 451.58 | Supplier Name: Umbrella Corp
<end>Please transform the following Markdown data into yaml:
| Birth Month | Income |
| --- | --- |
| March | 375000 |
| July | 280000 |
| September | 340000 |
| April | 180000 |
| March | 475000 |
| July | 465000 |
| May | 295000 |
| March | 130000 |
| March | 405000 |
| December | 135000 |<start>
- Birth Month: March
  Income: 375000
- Birth Month: July
  Income: 280000
- Birth Month: September
  Income: 340000
- Birth Month: April
  Income: 180000
- Birth Month: March
  Income: 475000
- Birth Month: July
  Income: 465000
- Birth Month: May
  Income: 295000
- Birth Month: March
  Income: 130000
- Birth Month: March
  Income: 405000
- Birth Month: December
  Income: 135000
<end>Please transform the following json data into markdown:
[
    {
        "Company": "EcoEnergy",
        "Sector": "Automotive",
        "Stock Price": 195.7,
        "Annual Revenue (B)": 216.32,
        "Quarter": "Q3"
    },
    {
        "Company": "GlobalTrade",
        "Sector": "Finance",
        "Stock Price": 766.98,
        "Annual Revenue (B)": 284.71,
        "Quarter": "Q4"
    },
    {
        "Company": "BioPharm",
        "Sector": "Finance",
        "Stock Price": 332.65,
        "Annual Revenue (B)": 213.12,
        "Quarter": "Q1"
    },
    {
        "Company": "BioPharm",
        "Sector": "Healthcare",
        "Stock Price": 751.99,
        "Annual Revenue (B)": 298.88,
        "Quarter": "Q3"
    },
    {
        "Company": "HealthPlus",
        "Sector": "Retail",
        "Stock Price": 576.65,
        "Annual Revenue (B)": 367.92,
        "Quarter": "Q1"
    },
    {
        "Company": "AutoDrive",
        "Sector": "Retail",
        "Stock Price": 184.67,
        "Annual Revenue (B)": 188.27,
        "Quarter": "Q2"
    }
]<start>
| Company | Sector | Stock Price | Annual Revenue (B) | Quarter |
| --- | --- | --- | --- | --- |
| EcoEnergy | Automotive | 195.7 | 216.32 | Q3 |
| GlobalTrade | Finance | 766.98 | 284.71 | Q4 |
| BioPharm | Finance | 332.65 | 213.12 | Q1 |
| BioPharm | Healthcare | 751.99 | 298.88 | Q3 |
| HealthPlus | Retail | 576.65 | 367.92 | Q1 |
| AutoDrive | Retail | 184.67 | 188.27 | Q2 |
<end>Transform this json structure to a csv format:
[
    {
        "Restaurant Name": "BBQ Barn",
        "Cuisine": "Italian",
        "Location": "Miami",
        "Rating": 2,
        "Price Range": "$$"
    },
    {
        "Restaurant Name": "The Steakhouse",
        "Cuisine": "Chinese",
        "Location": "Houston",
        "Rating": 5,
        "Price Range": "$$$$$"
    },
    {
        "Restaurant Name": "Taco Town",
        "Cuisine": "French",
        "Location": "Phoenix",
        "Rating": 1,
        "Price Range": "$$$"
    },
    {
        "Restaurant Name": "Sushi World",
        "Cuisine": "Indian",
        "Location": "Miami",
        "Rating": 4,
        "Price Range": "$$$"
    },
    {
        "Restaurant Name": "Curry Corner",
        "Cuisine": "Mediterranean",
        "Location": "New York",
        "Rating": 1,
        "Price Range": "$$$"
    },
    {
        "Restaurant Name": "Burger Haven",
        "Cuisine": "Italian",
        "Location": "Phoenix",
        "Rating": 3,
        "Price Range": "$$"
    },
    {
        "Restaurant Name": "The Golden Spoon",
        "Cuisine": "Mediterranean",
        "Location": "Los Angeles",
        "Rating": 4,
        "Price Range": "$$$"
    },
    {
        "Restaurant Name": "Curry Corner",
        "Cuisine": "American",
        "Location": "Los Angeles",
        "Rating": 2,
        "Price Range": "$$"
    },
    {
        "Restaurant Name": "The Steakhouse",
        "Cuisine": "Indian",
        "Location": "New York",
        "Rating": 5,
        "Price Range": "$$$$$"
    }
]<start>
Restaurant Name,Cuisine,Location,Rating,Price Range
BBQ Barn,Italian,Miami,2,$$
The Steakhouse,Chinese,Houston,5,$$$$$
Taco Town,French,Phoenix,1,$$$
Sushi World,Indian,Miami,4,$$$
Curry Corner,Mediterranean,New York,1,$$$
Burger Haven,Italian,Phoenix,3,$$
The Golden Spoon,Mediterranean,Los Angeles,4,$$$
Curry Corner,American,Los Angeles,2,$$
The Steakhouse,Indian,New York,5,$$$$$
<end>Can you change this csv into yaml?
Location,Condition,Temperature (C),Wind Speed (km/h),Day
Chicago,Stormy,30.6,9.9,Thursday
Houston,Foggy,35.9,15.4,Tuesday
Los Angeles,Snowy,33.2,24.6,Thursday
Denver,Foggy,37.3,9.0,Friday
<start>
- Condition: Stormy
  Day: Thursday
  Location: Chicago
  Temperature (C): 30.6
  Wind Speed (km/h): 9.9
- Condition: Foggy
  Day: Tuesday
  Location: Houston
  Temperature (C): 35.9
  Wind Speed (km/h): 15.4
- Condition: Snowy
  Day: Thursday
  Location: Los Angeles
  Temperature (C): 33.2
  Wind Speed (km/h): 24.6
- Condition: Foggy
  Day: Friday
  Location: Denver
  Temperature (C): 37.3
  Wind Speed (km/h): 9.0
<end>Please transform the following Json data into Yaml:
[
    {
        "Title": "Whispers of the Abyss",
        "Publication Year": 2012
    },
    {
        "Title": "The Last Sky",
        "Publication Year": 1980
    },
    {
        "Title": "Tales of the Brave",
        "Publication Year": 1952
    },
    {
        "Title": "Echoes of Eternity",
        "Publication Year": 1975
    },
    {
        "Title": "The Last Sky",
        "Publication Year": 2007
    },
    {
        "Title": "Tales of the Brave",
        "Publication Year": 1970
    },
    {
        "Title": "Shadows of Solitude",
        "Publication Year": 1986
    }
]<start>
- Publication Year: 2012
  Title: Whispers of the Abyss
- Publication Year: 1980
  Title: The Last Sky
- Publication Year: 1952
  Title: Tales of the Brave
- Publication Year: 1975
  Title: Echoes of Eternity
- Publication Year: 2007
  Title: The Last Sky
- Publication Year: 1970
  Title: Tales of the Brave
- Publication Year: 1986
  Title: Shadows of Solitude
<end>Transform this Markdown structure to a Json format:
| Company | Date | High Price | Low Price |
| --- | --- | --- | --- |
| AeroSystems | 2019-03-03 | 1196.84 | 492.06 |
| FoodChain | 2022-04-06 | 759.15 | 393.93 |
| FoodChain | 2011-05-02 | 858.9 | 545.13 |<start>
[
    {
        "Company": "AeroSystems",
        "Date": "2019-03-03",
        "High Price": 1196.84,
        "Low Price": 492.06
    },
    {
        "Company": "FoodChain",
        "Date": "2022-04-06",
        "High Price": 759.15,
        "Low Price": 393.93
    },
    {
        "Company": "FoodChain",
        "Date": "2011-05-02",
        "High Price": 858.9,
        "Low Price": 545.13
    }
]
<end>Can you change this Plain text into CSV?
Device ID: device-0056 | Device Type: Motion Detector | Location: Bedroom | Battery Level (%): 17.8 | Reading Value: 32.44 | Timestamp: 2022-06-25 18:33:20
Device ID: device-0027 | Device Type: Light Sensor | Location: Office | Battery Level (%): 99.8 | Reading Value: 74.8 | Timestamp: 2022-11-08 16:52:20
Device ID: device-0014 | Device Type: Light Sensor | Location: Garage | Battery Level (%): 42.3 | Reading Value: -10.78 | Timestamp: 2022-07-15 04:35:21
Device ID: device-0096 | Device Type: Pressure Sensor | Location: Bedroom | Battery Level (%): 99.8 | Reading Value: 33.34 | Timestamp: 2021-06-17 06:33:32
Device ID: device-0033 | Device Type: Pressure Sensor | Location: Bedroom | Battery Level (%): 13.5 | Reading Value: 39.17 | Timestamp: 2022-12-07 18:40:50
Device ID: device-0092 | Device Type: Pressure Sensor | Location: Hallway | Battery Level (%): 86.1 | Reading Value: -15.06 | Timestamp: 2022-03-01 23:44:23
Device ID: device-0100 | Device Type: Light Sensor | Location: Hallway | Battery Level (%): 93.4 | Reading Value: 5.54 | Timestamp: 2022-11-01 23:48:41
<start>
Device ID,Device Type,Location,Battery Level (%),Reading Value,Timestamp
device-0056,Motion Detector,Bedroom,17.8,32.44,2022-06-25 18:33:20
device-0027,Light Sensor,Office,99.8,74.8,2022-11-08 16:52:20
device-0014,Light Sensor,Garage,42.3,-10.78,2022-07-15 04:35:21
device-0096,Pressure Sensor,Bedroom,99.8,33.34,2021-06-17 06:33:32
device-0033,Pressure Sensor,Bedroom,13.5,39.17,2022-12-07 18:40:50
device-0092,Pressure Sensor,Hallway,86.1,-15.06,2022-03-01 23:44:23
device-0100,Light Sensor,Hallway,93.4,5.54,2022-11-01 23:48:41
<end>Here's some Plain text data, can you convert it to csv?
Device ID: device-0001 | Location: Garage | Timestamp: 2023-09-04 02:04:48
Device ID: device-0009 | Location: Kitchen | Timestamp: 2022-07-06 18:57:46
Device ID: device-0047 | Location: Bathroom | Timestamp: 2021-10-14 12:28:26
Device ID: device-0040 | Location: Garage | Timestamp: 2023-10-24 03:14:41
Device ID: device-0097 | Location: Garden | Timestamp: 2022-09-09 04:46:31
Device ID: device-0059 | Location: Garage | Timestamp: 2022-04-12 10:23:16
<start>
Device ID,Location,Timestamp
device-0001,Garage,2023-09-04 02:04:48
device-0009,Kitchen,2022-07-06 18:57:46
device-0047,Bathroom,2021-10-14 12:28:26
device-0040,Garage,2023-10-24 03:14:41
device-0097,Garden,2022-09-09 04:46:31
device-0059,Garage,2022-04-12 10:23:16
<end>Please transform the following csv data into markdown:
Age,City,Income
61,Austin,20000
39,Oklahoma City,195000
31,Oklahoma City,400000
<start>
| Age | City | Income |
| --- | --- | --- |
| 61 | Austin | 20000 |
| 39 | Oklahoma City | 195000 |
| 31 | Oklahoma City | 400000 |
<end>Here's some Csv data, can you convert it to Plain text?
Director,Genre
Talon Blackthorn,Horror
Zara Stormrider,Thriller
Selene Darkwhisper,Fantasy
Selene Darkwhisper,Action
Mara Moonshadow,Adventure
Talon Blackthorn,Action
Mara Moonshadow,Action
Orin Shadowalker,Sci-Fi
<start>
Director: Talon Blackthorn | Genre: Horror
Director: Zara Stormrider | Genre: Thriller
Director: Selene Darkwhisper | Genre: Fantasy
Director: Selene Darkwhisper | Genre: Action
Director: Mara Moonshadow | Genre: Adventure
Director: Talon Blackthorn | Genre: Action
Director: Mara Moonshadow | Genre: Action
Director: Orin Shadowalker | Genre: Sci-Fi
<end>Convert this Markdown to Json:
| Device ID | Device Type | Reading Value |
| --- | --- | --- |
| device-0027 | Temperature Sensor | 78.96 |
| device-0006 | Temperature Sensor | -36.22 |
| device-0056 | Temperature Sensor | -8.11 |
| device-0082 | Temperature Sensor | -21.12 |
| device-0092 | Light Sensor | 9.58 |
| device-0070 | Light Sensor | 39.69 |
| device-0002 | Light Sensor | 29.22 |
| device-0044 | Pressure Sensor | 25.99 |
| device-0068 | Motion Detector | 58.48 |<start>
[
    {
        "Device ID": "device-0027",
        "Device Type": "Temperature Sensor",
        "Reading Value": 78.96
    },
    {
        "Device ID": "device-0006",
        "Device Type": "Temperature Sensor",
        "Reading Value": -36.22
    },
    {
        "Device ID": "device-0056",
        "Device Type": "Temperature Sensor",
        "Reading Value": -8.11
    },
    {
        "Device ID": "device-0082",
        "Device Type": "Temperature Sensor",
        "Reading Value": -21.12
    },
    {
        "Device ID": "device-0092",
        "Device Type": "Light Sensor",
        "Reading Value": 9.58
    },
    {
        "Device ID": "device-0070",
        "Device Type": "Light Sensor",
        "Reading Value": 39.69
    },
    {
        "Device ID": "device-0002",
        "Device Type": "Light Sensor",
        "Reading Value": 29.22
    },
    {
        "Device ID": "device-0044",
        "Device Type": "Pressure Sensor",
        "Reading Value": 25.99
    },
    {
        "Device ID": "device-0068",
        "Device Type": "Motion Detector",
        "Reading Value": 58.48
    }
]
<end>Transform this MARKDOWN structure to a csv format:
| Cuisine | Rating |
| --- | --- |
| Mediterranean | 2 |
| Mediterranean | 2 |
| French | 4 |
| Mediterranean | 5 |
| Japanese | 5 |
| American | 4 |
| French | 2 |<start>
Cuisine,Rating
Mediterranean,2
Mediterranean,2
French,4
Mediterranean,5
Japanese,5
American,4
French,2
<end>Convert this json to csv:
[
    {
        "Sector": "Technology",
        "Market Cap": "Mid Cap",
        "Annual Revenue (B)": 61.19,
        "Quarter": "Q4"
    },
    {
        "Sector": "Energy",
        "Market Cap": "Large Cap",
        "Annual Revenue (B)": 171.86,
        "Quarter": "Q4"
    },
    {
        "Sector": "Aerospace",
        "Market Cap": "Large Cap",
        "Annual Revenue (B)": 479.04,
        "Quarter": "Q4"
    },
    {
        "Sector": "Finance",
        "Market Cap": "Small Cap",
        "Annual Revenue (B)": 434.2,
        "Quarter": "Q1"
    },
    {
        "Sector": "Energy",
        "Market Cap": "Mid Cap",
        "Annual Revenue (B)": 417.78,
        "Quarter": "Q1"
    },
    {
        "Sector": "Technology",
        "Market Cap": "Mid Cap",
        "Annual Revenue (B)": 462.21,
        "Quarter": "Q2"
    },
    {
        "Sector": "Aerospace",
        "Market Cap": "Mega Cap",
        "Annual Revenue (B)": 67.32,
        "Quarter": "Q2"
    }
]<start>
Sector,Market Cap,Annual Revenue (B),Quarter
Technology,Mid Cap,61.19,Q4
Energy,Large Cap,171.86,Q4
Aerospace,Large Cap,479.04,Q4
Finance,Small Cap,434.2,Q1
Energy,Mid Cap,417.78,Q1
Technology,Mid Cap,462.21,Q2
Aerospace,Mega Cap,67.32,Q2
<end>Here's some json data, can you convert it to YML?
[
    {
        "Location": "New York",
        "Condition": "Foggy",
        "Temperature (C)": -1.6,
        "Humidity (%)": 28,
        "Wind Speed (km/h)": 24.6,
        "Day": "Saturday"
    },
    {
        "Location": "New York",
        "Condition": "Cloudy",
        "Temperature (C)": 9.6,
        "Humidity (%)": 67,
        "Wind Speed (km/h)": 10.9,
        "Day": "Tuesday"
    },
    {
        "Location": "Phoenix",
        "Condition": "Windy",
        "Temperature (C)": 5.7,
        "Humidity (%)": 87,
        "Wind Speed (km/h)": 10.9,
        "Day": "Saturday"
    },
    {
        "Location": "Houston",
        "Condition": "Stormy",
        "Temperature (C)": 25.1,
        "Humidity (%)": 34,
        "Wind Speed (km/h)": 17.0,
        "Day": "Tuesday"
    },
    {
        "Location": "Seattle",
        "Condition": "Cloudy",
        "Temperature (C)": -3.4,
        "Humidity (%)": 53,
        "Wind Speed (km/h)": 22.4,
        "Day": "Thursday"
    },
    {
        "Location": "Seattle",
        "Condition": "Cloudy",
        "Temperature (C)": 10.3,
        "Humidity (%)": 40,
        "Wind Speed (km/h)": 5.2,
        "Day": "Thursday"
    }
]<start>
- Condition: Foggy
  Day: Saturday
  Humidity (%): 28
  Location: New York
  Temperature (C): -1.6
  Wind Speed (km/h): 24.6
- Condition: Cloudy
  Day: Tuesday
  Humidity (%): 67
  Location: New York
  Temperature (C): 9.6
  Wind Speed (km/h): 10.9
- Condition: Windy
  Day: Saturday
  Humidity (%): 87
  Location: Phoenix
  Temperature (C): 5.7
  Wind Speed (km/h): 10.9
- Condition: Stormy
  Day: Tuesday
  Humidity (%): 34
  Location: Houston
  Temperature (C): 25.1
  Wind Speed (km/h): 17.0
- Condition: Cloudy
  Day: Thursday
  Humidity (%): 53
  Location: Seattle
  Temperature (C): -3.4
  Wind Speed (km/h): 22.4
- Condition: Cloudy
  Day: Thursday
  Humidity (%): 40
  Location: Seattle
  Temperature (C): 10.3
  Wind Speed (km/h): 5.2
<end>Transform this plain text structure to a csv format:
Trip Name: Highway Odyssey | Start Location: Miami | End Location: Houston | Distance (miles): 2730.9 | Duration (hours): 30.2 | Fuel Used (gallons): 15.4
Trip Name: City Explorer | Start Location: Miami | End Location: Houston | Distance (miles): 701.2 | Duration (hours): 22.6 | Fuel Used (gallons): 44.7
Trip Name: Forest Journey | Start Location: Denver | End Location: New York | Distance (miles): 2972.8 | Duration (hours): 30.8 | Fuel Used (gallons): 23.4
Trip Name: Mountain Adventure | Start Location: Houston | End Location: Chicago | Distance (miles): 1538.8 | Duration (hours): 23.2 | Fuel Used (gallons): 27.2
Trip Name: Canyon Trek | Start Location: Los Angeles | End Location: Miami | Distance (miles): 611.7 | Duration (hours): 41.8 | Fuel Used (gallons): 33.9
Trip Name: Forest Journey | Start Location: Houston | End Location: Phoenix | Distance (miles): 719.4 | Duration (hours): 29.9 | Fuel Used (gallons): 60.3
Trip Name: Mountain Adventure | Start Location: Houston | End Location: Phoenix | Distance (miles): 1538.8 | Duration (hours): 55.8 | Fuel Used (gallons): 60.3
Trip Name: Canyon Trek | Start Location: San Francisco | End Location: Phoenix | Distance (miles): 1974.1 | Duration (hours): 3.2 | Fuel Used (gallons): 19.1
Trip Name: City Explorer | Start Location: Miami | End Location: Houston | Distance (miles): 2410.5 | Duration (hours): 12.5 | Fuel Used (gallons): 87.8
Trip Name: Forest Journey | Start Location: Denver | End Location: New York | Distance (miles): 2421.9 | Duration (hours): 66.6 | Fuel Used (gallons): 17.5
<start>
Trip Name,Start Location,End Location,Distance (miles),Duration (hours),Fuel Used (gallons)
Highway Odyssey,Miami,Houston,2730.9,30.2,15.4
City Explorer,Miami,Houston,701.2,22.6,44.7
Forest Journey,Denver,New York,2972.8,30.8,23.4
Mountain Adventure,Houston,Chicago,1538.8,23.2,27.2
Canyon Trek,Los Angeles,Miami,611.7,41.8,33.9
Forest Journey,Houston,Phoenix,719.4,29.9,60.3
Mountain Adventure,Houston,Phoenix,1538.8,55.8,60.3
Canyon Trek,San Francisco,Phoenix,1974.1,3.2,19.1
City Explorer,Miami,Houston,2410.5,12.5,87.8
Forest Journey,Denver,New York,2421.9,66.6,17.5
<end>Please transform the following JSON data into Csv:
[
    {
        "Name": "Valentina",
        "Age": 67,
        "City": "Las Vegas"
    },
    {
        "Name": "Asher",
        "Age": 34,
        "City": "San Diego"
    },
    {
        "Name": "Gilbert",
        "Age": 24,
        "City": "Baltimore"
    },
    {
        "Name": "Natasha",
        "Age": 22,
        "City": "San Jose"
    },
    {
        "Name": "Yvette",
        "Age": 61,
        "City": "New York"
    },
    {
        "Name": "Robin",
        "Age": 33,
        "City": "Portland"
    },
    {
        "Name": "Jenna",
        "Age": 26,
        "City": "San Diego"
    },
    {
        "Name": "Yolanda",
        "Age": 69,
        "City": "Seattle"
    },
    {
        "Name": "Joy",
        "Age": 58,
        "City": "Los Angeles"
    }
]<start>
Name,Age,City
Valentina,67,Las Vegas
Asher,34,San Diego
Gilbert,24,Baltimore
Natasha,22,San Jose
Yvette,61,New York
Robin,33,Portland
Jenna,26,San Diego
Yolanda,69,Seattle
Joy,58,Los Angeles
<end>Here's some plain text data, can you convert it to markdown?
Trip Name: City Explorer | Start Location: Houston | End Location: Chicago | Distance (miles): 2711.6 | Duration (hours): 25.1 | Fuel Used (gallons): 99.9
Trip Name: Valley Voyage | Start Location: Miami | End Location: San Francisco | Distance (miles): 1125.9 | Duration (hours): 35.6 | Fuel Used (gallons): 57.8
Trip Name: Desert Drive | Start Location: Houston | End Location: New York | Distance (miles): 2319.0 | Duration (hours): 16.0 | Fuel Used (gallons): 64.0
<start>
| Trip Name | Start Location | End Location | Distance (miles) | Duration (hours) | Fuel Used (gallons) |
| --- | --- | --- | --- | --- | --- |
| City Explorer | Houston | Chicago | 2711.6 | 25.1 | 99.9 |
| Valley Voyage | Miami | San Francisco | 1125.9 | 35.6 | 57.8 |
| Desert Drive | Houston | New York | 2319.0 | 16.0 | 64.0 |
<end>Can you change this CSV into MARKDOWN?
Company,Sector,Stock Price,Quarter
TechCorp,Energy,946.72,Q4
FinanceWorks,Healthcare,224.01,Q4
RetailHub,Healthcare,179.73,Q1
BioPharm,Biotech,897.9,Q3
<start>
| Company | Sector | Stock Price | Quarter |
| --- | --- | --- | --- |
| TechCorp | Energy | 946.72 | Q4 |
| FinanceWorks | Healthcare | 224.01 | Q4 |
| RetailHub | Healthcare | 179.73 | Q1 |
| BioPharm | Biotech | 897.9 | Q3 |
<end>Please transform the following PLAIN TEXT data into MARKDOWN:
Name: Alexander | Age: 52 | Birth Month: September
Name: Katrina | Age: 60 | Birth Month: March
Name: Angelo | Age: 25 | Birth Month: November
Name: Mabel | Age: 63 | Birth Month: August
Name: Delaney | Age: 25 | Birth Month: June
<start>
| Name | Age | Birth Month |
| --- | --- | --- |
| Alexander | 52 | September |
| Katrina | 60 | March |
| Angelo | 25 | November |
| Mabel | 63 | August |
| Delaney | 25 | June |
<end>Convert this JSON to yml:
[
    {
        "Temperature (C)": 1.2,
        "Wind Speed (km/h)": 14.8,
        "Day": "Friday"
    },
    {
        "Temperature (C)": 28.6,
        "Wind Speed (km/h)": 18.9,
        "Day": "Sunday"
    },
    {
        "Temperature (C)": 39.9,
        "Wind Speed (km/h)": 6.8,
        "Day": "Monday"
    },
    {
        "Temperature (C)": 8.6,
        "Wind Speed (km/h)": 1.2,
        "Day": "Thursday"
    },
    {
        "Temperature (C)": 1.6,
        "Wind Speed (km/h)": 5.2,
        "Day": "Saturday"
    },
    {
        "Temperature (C)": 7.5,
        "Wind Speed (km/h)": 16.3,
        "Day": "Monday"
    },
    {
        "Temperature (C)": 25.8,
        "Wind Speed (km/h)": 1.1,
        "Day": "Saturday"
    },
    {
        "Temperature (C)": 29.8,
        "Wind Speed (km/h)": 9.0,
        "Day": "Tuesday"
    }
]<start>
- Day: Friday
  Temperature (C): 1.2
  Wind Speed (km/h): 14.8
- Day: Sunday
  Temperature (C): 28.6
  Wind Speed (km/h): 18.9
- Day: Monday
  Temperature (C): 39.9
  Wind Speed (km/h): 6.8
- Day: Thursday
  Temperature (C): 8.6
  Wind Speed (km/h): 1.2
- Day: Saturday
  Temperature (C): 1.6
  Wind Speed (km/h): 5.2
- Day: Monday
  Temperature (C): 7.5
  Wind Speed (km/h): 16.3
- Day: Saturday
  Temperature (C): 25.8
  Wind Speed (km/h): 1.1
- Day: Tuesday
  Temperature (C): 29.8
  Wind Speed (km/h): 9.0
<end>Convert this JSON to csv:
[
    {
        "Product Name": "Contraption",
        "SKU": "SKU-1055",
        "Price": 240.03,
        "Stock Quantity": 443
    },
    {
        "Product Name": "Gadget",
        "SKU": "SKU-1013",
        "Price": 429.15,
        "Stock Quantity": 24
    },
    {
        "Product Name": "Widget",
        "SKU": "SKU-1099",
        "Price": 430.89,
        "Stock Quantity": 345
    },
    {
        "Product Name": "Device",
        "SKU": "SKU-1080",
        "Price": 254.96,
        "Stock Quantity": 74
    }
]<start>
Product Name,SKU,Price,Stock Quantity
Contraption,SKU-1055,240.03,443
Gadget,SKU-1013,429.15,24
Widget,SKU-1099,430.89,345
Device,SKU-1080,254.96,74
<end>Here's some Plain text data, can you convert it to yml?
Condition: Stormy | Temperature (C): -0.7 | Humidity (%): 61 | Day: Tuesday
Condition: Snowy | Temperature (C): 27.4 | Humidity (%): 86 | Day: Friday
Condition: Cloudy | Temperature (C): 12.6 | Humidity (%): 59 | Day: Sunday
Condition: Foggy | Temperature (C): -3.2 | Humidity (%): 92 | Day: Sunday
Condition: Snowy | Temperature (C): 12.0 | Humidity (%): 45 | Day: Saturday
<start>
- Condition: Stormy
  Day: Tuesday
  Humidity (%): 61
  Temperature (C): -0.7
- Condition: Snowy
  Day: Friday
  Humidity (%): 86
  Temperature (C): 27.4
- Condition: Cloudy
  Day: Sunday
  Humidity (%): 59
  Temperature (C): 12.6
- Condition: Foggy
  Day: Sunday
  Humidity (%): 92
  Temperature (C): -3.2
- Condition: Snowy
  Day: Saturday
  Humidity (%): 45
  Temperature (C): 12.0
<end>Convert this MARKDOWN to plain text:
| Trip Name | Start Location | End Location | Distance (miles) | Fuel Used (gallons) |
| --- | --- | --- | --- | --- |
| Historic Route | New York | Houston | 2737.7 | 72.7 |
| Historic Route | Phoenix | Miami | 2005.8 | 52.5 |
| Canyon Trek | Miami | Los Angeles | 1834.0 | 19.2 |
| Valley Voyage | Chicago | New York | 1786.8 | 91.6 |
| Coast to Coast | Los Angeles | New York | 360.0 | 52.3 |
| Coast to Coast | Phoenix | Denver | 279.9 | 70.8 |<start>
Trip Name: Historic Route | Start Location: New York | End Location: Houston | Distance (miles): 2737.7 | Fuel Used (gallons): 72.7
Trip Name: Historic Route | Start Location: Phoenix | End Location: Miami | Distance (miles): 2005.8 | Fuel Used (gallons): 52.5
Trip Name: Canyon Trek | Start Location: Miami | End Location: Los Angeles | Distance (miles): 1834.0 | Fuel Used (gallons): 19.2
Trip Name: Valley Voyage | Start Location: Chicago | End Location: New York | Distance (miles): 1786.8 | Fuel Used (gallons): 91.6
Trip Name: Coast to Coast | Start Location: Los Angeles | End Location: New York | Distance (miles): 360.0 | Fuel Used (gallons): 52.3
Trip Name: Coast to Coast | Start Location: Phoenix | End Location: Denver | Distance (miles): 279.9 | Fuel Used (gallons): 70.8
<end>Convert this MARKDOWN to Json:
| Genre | Release Year | Box Office Earnings (M) |
| --- | --- | --- |
| Comedy | 2014 | 492.36 |
| Sci-Fi | 2023 | 694.04 |
| Fantasy | 1995 | 296.66 |
| Fantasy | 1979 | 397.75 |
| Drama | 1995 | 420.08 |
| Thriller | 2023 | 520.86 |
| Comedy | 1983 | 925.75 |
| Comedy | 1988 | 106.82 |
| Action | 2023 | 365.4 |<start>
[
    {
        "Genre": "Comedy",
        "Release Year": 2014,
        "Box Office Earnings (M)": 492.36
    },
    {
        "Genre": "Sci-Fi",
        "Release Year": 2023,
        "Box Office Earnings (M)": 694.04
    },
    {
        "Genre": "Fantasy",
        "Release Year": 1995,
        "Box Office Earnings (M)": 296.66
    },
    {
        "Genre": "Fantasy",
        "Release Year": 1979,
        "Box Office Earnings (M)": 397.75
    },
    {
        "Genre": "Drama",
        "Release Year": 1995,
        "Box Office Earnings (M)": 420.08
    },
    {
        "Genre": "Thriller",
        "Release Year": 2023,
        "Box Office Earnings (M)": 520.86
    },
    {
        "Genre": "Comedy",
        "Release Year": 1983,
        "Box Office Earnings (M)": 925.75
    },
    {
        "Genre": "Comedy",
        "Release Year": 1988,
        "Box Office Earnings (M)": 106.82
    },
    {
        "Genre": "Action",
        "Release Year": 2023,
        "Box Office Earnings (M)": 365.4
    }
]
<end>Please transform the following plain text data into MARKDOWN:
Device ID: device-0034 | Device Type: Temperature Sensor | Location: Hallway | Battery Level (%): 34.2
Device ID: device-0082 | Device Type: Temperature Sensor | Location: Garage | Battery Level (%): 90.4
Device ID: device-0075 | Device Type: Motion Detector | Location: Kitchen | Battery Level (%): 85.6
Device ID: device-0084 | Device Type: Humidity Sensor | Location: Garage | Battery Level (%): 31.5
<start>
| Device ID | Device Type | Location | Battery Level (%) |
| --- | --- | --- | --- |
| device-0034 | Temperature Sensor | Hallway | 34.2 |
| device-0082 | Temperature Sensor | Garage | 90.4 |
| device-0075 | Motion Detector | Kitchen | 85.6 |
| device-0084 | Humidity Sensor | Garage | 31.5 |
<end>Can you change this markdown into plain text?
| Title | Author | Rating |
| --- | --- | --- |
| The Forgotten World | Luna Silverleaf | 4.2 |
| Whispers of the Abyss | Elara Moonshadow | 2.4 |
| The Crystal Key | Draven Blackthorn | 2.6 |
| The Silent Grove | Rowan Ashborne | 3.4 |
| The Silent Grove | Rowan Ashborne | 3.1 |
| The Forgotten World | Kara Firebrand | 2.4 |
| The Forgotten World | Isla Windrider | 4.5 |
| A Journey Through Time | Orion Frostblade | 1.9 |
| Echoes of Eternity | Draven Blackthorn | 3.8 |
| The Forgotten World | Luna Silverleaf | 2.9 |<start>
Title: The Forgotten World | Author: Luna Silverleaf | Rating: 4.2
Title: Whispers of the Abyss | Author: Elara Moonshadow | Rating: 2.4
Title: The Crystal Key | Author: Draven Blackthorn | Rating: 2.6
Title: The Silent Grove | Author: Rowan Ashborne | Rating: 3.4
Title: The Silent Grove | Author: Rowan Ashborne | Rating: 3.1
Title: The Forgotten World | Author: Kara Firebrand | Rating: 2.4
Title: The Forgotten World | Author: Isla Windrider | Rating: 4.5
Title: A Journey Through Time | Author: Orion Frostblade | Rating: 1.9
Title: Echoes of Eternity | Author: Draven Blackthorn | Rating: 3.8
Title: The Forgotten World | Author: Luna Silverleaf | Rating: 2.9
<end>Please transform the following Plain text data into json:
Name: Christy | Birth Month: January | Income: 175000
Name: Jerry | Birth Month: September | Income: 150000
Name: Beulah | Birth Month: May | Income: 115000
Name: Molly | Birth Month: September | Income: 310000
Name: Lois | Birth Month: July | Income: 370000
Name: Lee | Birth Month: November | Income: 480000
Name: Doris | Birth Month: July | Income: 385000
Name: Minnie | Birth Month: September | Income: 400000
Name: Laurie | Birth Month: August | Income: 195000
Name: Curtis | Birth Month: March | Income: 240000
<start>
[
    {
        "Name": "Christy",
        "Birth Month": "January",
        "Income": 175000
    },
    {
        "Name": "Jerry",
        "Birth Month": "September",
        "Income": 150000
    },
    {
        "Name": "Beulah",
        "Birth Month": "May",
        "Income": 115000
    },
    {
        "Name": "Molly",
        "Birth Month": "September",
        "Income": 310000
    },
    {
        "Name": "Lois",
        "Birth Month": "July",
        "Income": 370000
    },
    {
        "Name": "Lee",
        "Birth Month": "November",
        "Income": 480000
    },
    {
        "Name": "Doris",
        "Birth Month": "July",
        "Income": 385000
    },
    {
        "Name": "Minnie",
        "Birth Month": "September",
        "Income": 400000
    },
    {
        "Name": "Laurie",
        "Birth Month": "August",
        "Income": 195000
    },
    {
        "Name": "Curtis",
        "Birth Month": "March",
        "Income": 240000
    }
]
<end>Here's some json data, can you convert it to plain text?
[
    {
        "Trip Name": "City Explorer",
        "Start Location": "New York",
        "End Location": "San Francisco",
        "Distance (miles)": 678.7,
        "Duration (hours)": 39.1
    },
    {
        "Trip Name": "Canyon Trek",
        "Start Location": "Chicago",
        "End Location": "Los Angeles",
        "Distance (miles)": 1112.2,
        "Duration (hours)": 3.7
    },
    {
        "Trip Name": "Lakeside Retreat",
        "Start Location": "Denver",
        "End Location": "San Francisco",
        "Distance (miles)": 1155.9,
        "Duration (hours)": 20.0
    },
    {
        "Trip Name": "Desert Drive",
        "Start Location": "New York",
        "End Location": "Houston",
        "Distance (miles)": 427.8,
        "Duration (hours)": 28.4
    },
    {
        "Trip Name": "Canyon Trek",
        "Start Location": "New York",
        "End Location": "Phoenix",
        "Distance (miles)": 361.9,
        "Duration (hours)": 69.0
    },
    {
        "Trip Name": "Highway Odyssey",
        "Start Location": "Los Angeles",
        "End Location": "Phoenix",
        "Distance (miles)": 1332.4,
        "Duration (hours)": 40.7
    },
    {
        "Trip Name": "Canyon Trek",
        "Start Location": "Chicago",
        "End Location": "New York",
        "Distance (miles)": 901.9,
        "Duration (hours)": 2.5
    },
    {
        "Trip Name": "Highway Odyssey",
        "Start Location": "Miami",
        "End Location": "Chicago",
        "Distance (miles)": 1574.0,
        "Duration (hours)": 6.2
    },
    {
        "Trip Name": "Lakeside Retreat",
        "Start Location": "Los Angeles",
        "End Location": "Phoenix",
        "Distance (miles)": 2971.1,
        "Duration (hours)": 27.4
    },
    {
        "Trip Name": "Canyon Trek",
        "Start Location": "San Francisco",
        "End Location": "New York",
        "Distance (miles)": 901.9,
        "Duration (hours)": 5.0
    }
]<start>
Trip Name: City Explorer | Start Location: New York | End Location: San Francisco | Distance (miles): 678.7 | Duration (hours): 39.1
Trip Name: Canyon Trek | Start Location: Chicago | End Location: Los Angeles | Distance (miles): 1112.2 | Duration (hours): 3.7
Trip Name: Lakeside Retreat | Start Location: Denver | End Location: San Francisco | Distance (miles): 1155.9 | Duration (hours): 20.0
Trip Name: Desert Drive | Start Location: New York | End Location: Houston | Distance (miles): 427.8 | Duration (hours): 28.4
Trip Name: Canyon Trek | Start Location: New York | End Location: Phoenix | Distance (miles): 361.9 | Duration (hours): 69.0
Trip Name: Highway Odyssey | Start Location: Los Angeles | End Location: Phoenix | Distance (miles): 1332.4 | Duration (hours): 40.7
Trip Name: Canyon Trek | Start Location: Chicago | End Location: New York | Distance (miles): 901.9 | Duration (hours): 2.5
Trip Name: Highway Odyssey | Start Location: Miami | End Location: Chicago | Distance (miles): 1574.0 | Duration (hours): 6.2
Trip Name: Lakeside Retreat | Start Location: Los Angeles | End Location: Phoenix | Distance (miles): 2971.1 | Duration (hours): 27.4
Trip Name: Canyon Trek | Start Location: San Francisco | End Location: New York | Distance (miles): 901.9 | Duration (hours): 5.0
<end>Convert this yaml to MARKDOWN:
- Battery Level (%): 86.6
  Device ID: device-0078
  Reading Value: -38.04
  Timestamp: '2022-11-19 04:33:16'
- Battery Level (%): 33.2
  Device ID: device-0033
  Reading Value: 37.5
  Timestamp: '2021-08-09 22:48:26'
- Battery Level (%): 86.2
  Device ID: device-0044
  Reading Value: -22.27
  Timestamp: '2022-01-08 22:35:05'
- Battery Level (%): 29.8
  Device ID: device-0036
  Reading Value: -17.53
  Timestamp: '2023-07-05 06:27:24'
- Battery Level (%): 94.2
  Device ID: device-0083
  Reading Value: -3.68
  Timestamp: '2022-08-18 07:38:27'
<start>
| Device ID | Battery Level (%) | Reading Value | Timestamp |
| --- | --- | --- | --- |
| device-0078 | 86.6 | -38.04 | 2022-11-19 04:33:16 |
| device-0033 | 33.2 | 37.5 | 2021-08-09 22:48:26 |
| device-0044 | 86.2 | -22.27 | 2022-01-08 22:35:05 |
| device-0036 | 29.8 | -17.53 | 2023-07-05 06:27:24 |
| device-0083 | 94.2 | -3.68 | 2022-08-18 07:38:27 |
<end>Please transform the following YML data into PLAIN TEXT:
- Humidity (%): 90
  Location: Phoenix
  Temperature (C): 2.7
- Humidity (%): 60
  Location: New York
  Temperature (C): 11.6
- Humidity (%): 75
  Location: Houston
  Temperature (C): 13.9
- Humidity (%): 23
  Location: Denver
  Temperature (C): 32.6
<start>
Location: Phoenix | Temperature (C): 2.7 | Humidity (%): 90
Location: New York | Temperature (C): 11.6 | Humidity (%): 60
Location: Houston | Temperature (C): 13.9 | Humidity (%): 75
Location: Denver | Temperature (C): 32.6 | Humidity (%): 23
<end>Here's some Plain text data, can you convert it to YAML?
Trip Name: Mountain Adventure | Start Location: Los Angeles | Distance (miles): 1604.5 | Duration (hours): 49.0 | Fuel Used (gallons): 48.8
Trip Name: Valley Voyage | Start Location: Houston | Distance (miles): 2330.2 | Duration (hours): 23.4 | Fuel Used (gallons): 53.1
Trip Name: City Explorer | Start Location: Phoenix | Distance (miles): 2507.7 | Duration (hours): 26.6 | Fuel Used (gallons): 23.2
<start>
- Distance (miles): 1604.5
  Duration (hours): 49.0
  Fuel Used (gallons): 48.8
  Start Location: Los Angeles
  Trip Name: Mountain Adventure
- Distance (miles): 2330.2
  Duration (hours): 23.4
  Fuel Used (gallons): 53.1
  Start Location: Houston
  Trip Name: Valley Voyage
- Distance (miles): 2507.7
  Duration (hours): 26.6
  Fuel Used (gallons): 23.2
  Start Location: Phoenix
  Trip Name: City Explorer
<end>Can you change this Json into yml?
[
    {
        "Device ID": "device-0004",
        "Device Type": "Pressure Sensor",
        "Battery Level (%)": 67.6
    },
    {
        "Device ID": "device-0073",
        "Device Type": "Light Sensor",
        "Battery Level (%)": 88.2
    },
    {
        "Device ID": "device-0049",
        "Device Type": "Temperature Sensor",
        "Battery Level (%)": 41.6
    },
    {
        "Device ID": "device-0022",
        "Device Type": "Pressure Sensor",
        "Battery Level (%)": 44.1
    },
    {
        "Device ID": "device-0028",
        "Device Type": "Motion Detector",
        "Battery Level (%)": 57.9
    },
    {
        "Device ID": "device-0039",
        "Device Type": "Pressure Sensor",
        "Battery Level (%)": 42.0
    },
    {
        "Device ID": "device-0005",
        "Device Type": "Motion Detector",
        "Battery Level (%)": 61.5
    }
]<start>
- Battery Level (%): 67.6
  Device ID: device-0004
  Device Type: Pressure Sensor
- Battery Level (%): 88.2
  Device ID: device-0073
  Device Type: Light Sensor
- Battery Level (%): 41.6
  Device ID: device-0049
  Device Type: Temperature Sensor
- Battery Level (%): 44.1
  Device ID: device-0022
  Device Type: Pressure Sensor
- Battery Level (%): 57.9
  Device ID: device-0028
  Device Type: Motion Detector
- Battery Level (%): 42.0
  Device ID: device-0039
  Device Type: Pressure Sensor
- Battery Level (%): 61.5
  Device ID: device-0005
  Device Type: Motion Detector
<end>Convert this YML to Markdown:
- Annual Revenue (B): 374.3
  Company: HealthPlus
  Market Cap: Small Cap
  Quarter: Q3
  Stock Price: 87.08
- Annual Revenue (B): 217.32
  Company: EcoEnergy
  Market Cap: Mid Cap
  Quarter: Q3
  Stock Price: 988.06
- Annual Revenue (B): 464.28
  Company: EcoEnergy
  Market Cap: Mega Cap
  Quarter: Q4
  Stock Price: 199.76
- Annual Revenue (B): 374.3
  Company: AutoDrive
  Market Cap: Mega Cap
  Quarter: Q3
  Stock Price: 927.75
- Annual Revenue (B): 482.81
  Company: AutoDrive
  Market Cap: Small Cap
  Quarter: Q2
  Stock Price: 72.14
- Annual Revenue (B): 322.31
  Company: FinanceWorks
  Market Cap: Mid Cap
  Quarter: Q4
  Stock Price: 968.72
- Annual Revenue (B): 454.89
  Company: GlobalTrade
  Market Cap: Small Cap
  Quarter: Q1
  Stock Price: 988.06
- Annual Revenue (B): 298.86
  Company: TechCorp
  Market Cap: Small Cap
  Quarter: Q2
  Stock Price: 953.22
- Annual Revenue (B): 300.37
  Company: EcoEnergy
  Market Cap: Mega Cap
  Quarter: Q4
  Stock Price: 939.26
- Annual Revenue (B): 207.79
  Company: HealthPlus
  Market Cap: Mega Cap
  Quarter: Q1
  Stock Price: 811.68
<start>
| Company | Market Cap | Stock Price | Annual Revenue (B) | Quarter |
| --- | --- | --- | --- | --- |
| HealthPlus | Small Cap | 87.08 | 374.3 | Q3 |
| EcoEnergy | Mid Cap | 988.06 | 217.32 | Q3 |
| EcoEnergy | Mega Cap | 199.76 | 464.28 | Q4 |
| AutoDrive | Mega Cap | 927.75 | 374.3 | Q3 |
| AutoDrive | Small Cap | 72.14 | 482.81 | Q2 |
| FinanceWorks | Mid Cap | 968.72 | 322.31 | Q4 |
| GlobalTrade | Small Cap | 988.06 | 454.89 | Q1 |
| TechCorp | Small Cap | 953.22 | 298.86 | Q2 |
| EcoEnergy | Mega Cap | 939.26 | 300.37 | Q4 |
| HealthPlus | Mega Cap | 811.68 | 207.79 | Q1 |
<end>Convert this MARKDOWN to CSV:
| Product Name | SKU | Price | Stock Quantity | Category | Supplier Name |
| --- | --- | --- | --- | --- | --- |
| Apparatus | SKU-1008 | 251.51 | 488 | Household | ACME Corp |
| Gizmo | SKU-1045 | 55.85 | 59 | Toys | Wonka Industries |
| Gizmo | SKU-1050 | 273.87 | 435 | Automotive | Globex |<start>
Product Name,SKU,Price,Stock Quantity,Category,Supplier Name
Apparatus,SKU-1008,251.51,488,Household,ACME Corp
Gizmo,SKU-1045,55.85,59,Toys,Wonka Industries
Gizmo,SKU-1050,273.87,435,Automotive,Globex
<end>Here's some plain text data, can you convert it to Json?
Name: Charlotte | Age: 43 | Birth Month: August | City: San Jose
Name: Misty | Age: 65 | Birth Month: September | City: Nashville
Name: Leona | Age: 32 | Birth Month: June | City: Milwaukee
Name: Jalen | Age: 53 | Birth Month: December | City: Memphis
Name: Rosemarie | Age: 43 | Birth Month: March | City: Boston
Name: Benny | Age: 60 | Birth Month: May | City: Milwaukee
Name: Madelyn | Age: 40 | Birth Month: October | City: Oklahoma City
Name: Adrianna | Age: 46 | Birth Month: November | City: Chicago
Name: Gayle | Age: 59 | Birth Month: December | City: Seattle
<start>
[
    {
        "Name": "Charlotte",
        "Age": 43,
        "Birth Month": "August",
        "City": "San Jose"
    },
    {
        "Name": "Misty",
        "Age": 65,
        "Birth Month": "September",
        "City": "Nashville"
    },
    {
        "Name": "Leona",
        "Age": 32,
        "Birth Month": "June",
        "City": "Milwaukee"
    },
    {
        "Name": "Jalen",
        "Age": 53,
        "Birth Month": "December",
        "City": "Memphis"
    },
    {
        "Name": "Rosemarie",
        "Age": 43,
        "Birth Month": "March",
        "City": "Boston"
    },
    {
        "Name": "Benny",
        "Age": 60,
        "Birth Month": "May",
        "City": "Milwaukee"
    },
    {
        "Name": "Madelyn",
        "Age": 40,
        "Birth Month": "October",
        "City": "Oklahoma City"
    },
    {
        "Name": "Adrianna",
        "Age": 46,
        "Birth Month": "November",
        "City": "Chicago"
    },
    {
        "Name": "Gayle",
        "Age": 59,
        "Birth Month": "December",
        "City": "Seattle"
    }
]
<end>Transform this markdown structure to a Json format:
| Name | City | Income |
| --- | --- | --- |
| Xander | Milwaukee | 210000 |
| Justin | Chicago | 365000 |
| Bertie | Milwaukee | 425000 |
| Charley | Memphis | 370000 |<start>
[
    {
        "Name": "Xander",
        "City": "Milwaukee",
        "Income": 210000
    },
    {
        "Name": "Justin",
        "City": "Chicago",
        "Income": 365000
    },
    {
        "Name": "Bertie",
        "City": "Milwaukee",
        "Income": 425000
    },
    {
        "Name": "Charley",
        "City": "Memphis",
        "Income": 370000
    }
]
<end>Convert this CSV to yml:
Stock Quantity,Category,Supplier Name
257,Toys,Wonka Industries
287,Household,ACME Corp
194,Toys,Umbrella Corp
421,Toys,Wayne Enterprises
15,Sports,Umbrella Corp
<start>
- Category: Toys
  Stock Quantity: 257
  Supplier Name: Wonka Industries
- Category: Household
  Stock Quantity: 287
  Supplier Name: ACME Corp
- Category: Toys
  Stock Quantity: 194
  Supplier Name: Umbrella Corp
- Category: Toys
  Stock Quantity: 421
  Supplier Name: Wayne Enterprises
- Category: Sports
  Stock Quantity: 15
  Supplier Name: Umbrella Corp
<end>Can you change this Json into CSV?
[
    {
        "Location": "Miami",
        "Temperature (C)": 21.5,
        "Wind Speed (km/h)": 20.1,
        "Day": "Saturday"
    },
    {
        "Location": "Seattle",
        "Temperature (C)": 7.2,
        "Wind Speed (km/h)": 20.4,
        "Day": "Tuesday"
    },
    {
        "Location": "Phoenix",
        "Temperature (C)": 35.2,
        "Wind Speed (km/h)": 15.5,
        "Day": "Sunday"
    },
    {
        "Location": "Denver",
        "Temperature (C)": 31.0,
        "Wind Speed (km/h)": 11.7,
        "Day": "Thursday"
    },
    {
        "Location": "New York",
        "Temperature (C)": 8.4,
        "Wind Speed (km/h)": 21.8,
        "Day": "Wednesday"
    },
    {
        "Location": "Los Angeles",
        "Temperature (C)": 18.4,
        "Wind Speed (km/h)": 2.0,
        "Day": "Friday"
    },
    {
        "Location": "Houston",
        "Temperature (C)": 22.1,
        "Wind Speed (km/h)": 14.7,
        "Day": "Sunday"
    },
    {
        "Location": "Phoenix",
        "Temperature (C)": -5.0,
        "Wind Speed (km/h)": 24.2,
        "Day": "Thursday"
    }
]<start>
Location,Temperature (C),Wind Speed (km/h),Day
Miami,21.5,20.1,Saturday
Seattle,7.2,20.4,Tuesday
Phoenix,35.2,15.5,Sunday
Denver,31.0,11.7,Thursday
New York,8.4,21.8,Wednesday
Los Angeles,18.4,2.0,Friday
Houston,22.1,14.7,Sunday
Phoenix,-5.0,24.2,Thursday
<end>Transform this Json structure to a Csv format:
[
    {
        "Product Name": "Widget",
        "Price": 112.31,
        "Category": "Household"
    },
    {
        "Product Name": "Doohickey",
        "Price": 312.54,
        "Category": "Sports"
    },
    {
        "Product Name": "Apparatus",
        "Price": 214.5,
        "Category": "Automotive"
    },
    {
        "Product Name": "Instrument",
        "Price": 468.23,
        "Category": "Household"
    },
    {
        "Product Name": "Doohickey",
        "Price": 253.76,
        "Category": "Sports"
    },
    {
        "Product Name": "Whatchamacallit",
        "Price": 395.23,
        "Category": "Automotive"
    },
    {
        "Product Name": "Instrument",
        "Price": 68.97,
        "Category": "Toys"
    },
    {
        "Product Name": "Widget",
        "Price": 70.26,
        "Category": "Household"
    },
    {
        "Product Name": "Device",
        "Price": 345.03,
        "Category": "Sports"
    }
]<start>
Product Name,Price,Category
Widget,112.31,Household
Doohickey,312.54,Sports
Apparatus,214.5,Automotive
Instrument,468.23,Household
Doohickey,253.76,Sports
Whatchamacallit,395.23,Automotive
Instrument,68.97,Toys
Widget,70.26,Household
Device,345.03,Sports
<end>Please transform the following Csv data into yml:
Device ID,Device Type,Location,Battery Level (%),Reading Value,Timestamp
device-0031,Motion Detector,Kitchen,23.3,47.6,2023-11-11 02:00:13
device-0034,Humidity Sensor,Garage,55.1,-4.78,2021-08-16 21:49:56
device-0018,Humidity Sensor,Bedroom,68.0,61.6,2022-03-15 17:40:55
device-0029,Motion Detector,Hallway,68.0,84.41,2023-10-02 01:31:08
device-0062,Temperature Sensor,Bedroom,90.6,78.94,2021-07-03 14:33:42
device-0045,Pressure Sensor,Kitchen,24.6,17.98,2022-04-09 19:00:20
device-0013,Light Sensor,Garden,44.6,76.69,2022-05-20 08:54:19
device-0030,Humidity Sensor,Garage,99.3,43.54,2022-05-06 00:33:00
device-0094,Humidity Sensor,Bathroom,12.7,30.37,2023-11-20 07:31:04
device-0085,Motion Detector,Bathroom,14.4,31.36,2023-03-10 17:32:54
<start>
- Battery Level (%): 23.3
  Device ID: device-0031
  Device Type: Motion Detector
  Location: Kitchen
  Reading Value: 47.6
  Timestamp: '2023-11-11 02:00:13'
- Battery Level (%): 55.1
  Device ID: device-0034
  Device Type: Humidity Sensor
  Location: Garage
  Reading Value: -4.78
  Timestamp: '2021-08-16 21:49:56'
- Battery Level (%): 68.0
  Device ID: device-0018
  Device Type: Humidity Sensor
  Location: Bedroom
  Reading Value: 61.6
  Timestamp: '2022-03-15 17:40:55'
- Battery Level (%): 68.0
  Device ID: device-0029
  Device Type: Motion Detector
  Location: Hallway
  Reading Value: 84.41
  Timestamp: '2023-10-02 01:31:08'
- Battery Level (%): 90.6
  Device ID: device-0062
  Device Type: Temperature Sensor
  Location: Bedroom
  Reading Value: 78.94
  Timestamp: '2021-07-03 14:33:42'
- Battery Level (%): 24.6
  Device ID: device-0045
  Device Type: Pressure Sensor
  Location: Kitchen
  Reading Value: 17.98
  Timestamp: '2022-04-09 19:00:20'
- Battery Level (%): 44.6
  Device ID: device-0013
  Device Type: Light Sensor
  Location: Garden
  Reading Value: 76.69
  Timestamp: '2022-05-20 08:54:19'
- Battery Level (%): 99.3
  Device ID: device-0030
  Device Type: Humidity Sensor
  Location: Garage
  Reading Value: 43.54
  Timestamp: '2022-05-06 00:33:00'
- Battery Level (%): 12.7
  Device ID: device-0094
  Device Type: Humidity Sensor
  Location: Bathroom
  Reading Value: 30.37
  Timestamp: '2023-11-20 07:31:04'
- Battery Level (%): 14.4
  Device ID: device-0085
  Device Type: Motion Detector
  Location: Bathroom
  Reading Value: 31.36
  Timestamp: '2023-03-10 17:32:54'
<end>Please transform the following PLAIN TEXT data into Json:
Title: Edge of Infinity | Director: Zara Stormrider | Release Year: 2011 | Box Office Earnings (M): 997.9
Title: Mystery of the Depths | Director: Zara Stormrider | Release Year: 1997 | Box Office Earnings (M): 300.99
Title: Rise of the Titans | Director: Aria Ravenwood | Release Year: 2015 | Box Office Earnings (M): 422.91
<start>
[
    {
        "Title": "Edge of Infinity",
        "Director": "Zara Stormrider",
        "Release Year": 2011,
        "Box Office Earnings (M)": 997.9
    },
    {
        "Title": "Mystery of the Depths",
        "Director": "Zara Stormrider",
        "Release Year": 1997,
        "Box Office Earnings (M)": 300.99
    },
    {
        "Title": "Rise of the Titans",
        "Director": "Aria Ravenwood",
        "Release Year": 2015,
        "Box Office Earnings (M)": 422.91
    }
]
<end>Transform this Yaml structure to a CSV format:
- Average Latency (ms): 94.57
  Cache Hit Ratio (%): 96.46
  Connection Count: 149
  Database Name: LogsDB
  Timestamp: '2021-07-07 22:43:01'
- Average Latency (ms): 17.78
  Cache Hit Ratio (%): 70.15
  Connection Count: 405
  Database Name: InventoryDB
  Timestamp: '2021-08-07 14:52:44'
- Average Latency (ms): 92.8
  Cache Hit Ratio (%): 78.36
  Connection Count: 202
  Database Name: ProfilesDB
  Timestamp: '2022-11-04 09:24:38'
- Average Latency (ms): 74.72
  Cache Hit Ratio (%): 87.76
  Connection Count: 322
  Database Name: AnalyticsDB
  Timestamp: '2022-08-07 01:11:37'
- Average Latency (ms): 25.1
  Cache Hit Ratio (%): 70.27
  Connection Count: 209
  Database Name: SessionsDB
  Timestamp: '2021-07-14 10:23:51'
- Average Latency (ms): 95.35
  Cache Hit Ratio (%): 85.59
  Connection Count: 282
  Database Name: AnalyticsDB
  Timestamp: '2023-04-03 11:46:02'
- Average Latency (ms): 27.22
  Cache Hit Ratio (%): 85.59
  Connection Count: 490
  Database Name: OrdersDB
  Timestamp: '2021-06-09 14:48:49'
- Average Latency (ms): 46.47
  Cache Hit Ratio (%): 86.29
  Connection Count: 44
  Database Name: MetricsDB
  Timestamp: '2022-10-14 16:52:48'
- Average Latency (ms): 8.67
  Cache Hit Ratio (%): 83.93
  Connection Count: 278
  Database Name: SessionsDB
  Timestamp: '2023-02-15 23:54:03'
<start>
Database Name,Cache Hit Ratio (%),Connection Count,Average Latency (ms),Timestamp
LogsDB,96.46,149,94.57,2021-07-07 22:43:01
InventoryDB,70.15,405,17.78,2021-08-07 14:52:44
ProfilesDB,78.36,202,92.8,2022-11-04 09:24:38
AnalyticsDB,87.76,322,74.72,2022-08-07 01:11:37
SessionsDB,70.27,209,25.1,2021-07-14 10:23:51
AnalyticsDB,85.59,282,95.35,2023-04-03 11:46:02
OrdersDB,85.59,490,27.22,2021-06-09 14:48:49
MetricsDB,86.29,44,46.47,2022-10-14 16:52:48
SessionsDB,83.93,278,8.67,2023-02-15 23:54:03
<end>Here's some csv data, can you convert it to yml?
Location,Humidity (%),Wind Speed (km/h),Day
Chicago,63,8.3,Tuesday
Phoenix,81,22.4,Monday
Phoenix,62,11.3,Friday
Phoenix,81,22.6,Saturday
Houston,29,20.3,Tuesday
<start>
- Day: Tuesday
  Humidity (%): 63
  Location: Chicago
  Wind Speed (km/h): 8.3
- Day: Monday
  Humidity (%): 81
  Location: Phoenix
  Wind Speed (km/h): 22.4
- Day: Friday
  Humidity (%): 62
  Location: Phoenix
  Wind Speed (km/h): 11.3
- Day: Saturday
  Humidity (%): 81
  Location: Phoenix
  Wind Speed (km/h): 22.6
- Day: Tuesday
  Humidity (%): 29
  Location: Houston
  Wind Speed (km/h): 20.3
<end>Can you change this yml into json?
- Birth Month: November
  City: Seattle
  Income: 175000
  Name: Sylvia
- Birth Month: November
  City: El Paso
  Income: 390000
  Name: Albert
- Birth Month: July
  City: Las Vegas
  Income: 25000
  Name: Renee
- Birth Month: September
  City: Seattle
  Income: 245000
  Name: Devon
- Birth Month: February
  City: Nashville
  Income: 445000
  Name: Randall
- Birth Month: November
  City: Louisville
  Income: 345000
  Name: Austin
- Birth Month: February
  City: Indianapolis
  Income: 385000
  Name: Carla
- Birth Month: March
  City: Los Angeles
  Income: 245000
  Name: Kara
- Birth Month: September
  City: Phoenix
  Income: 430000
  Name: Camden
- Birth Month: January
  City: Washington
  Income: 30000
  Name: Rachel
<start>
[
    {
        "Name": "Sylvia",
        "Birth Month": "November",
        "City": "Seattle",
        "Income": 175000
    },
    {
        "Name": "Albert",
        "Birth Month": "November",
        "City": "El Paso",
        "Income": 390000
    },
    {
        "Name": "Renee",
        "Birth Month": "July",
        "City": "Las Vegas",
        "Income": 25000
    },
    {
        "Name": "Devon",
        "Birth Month": "September",
        "City": "Seattle",
        "Income": 245000
    },
    {
        "Name": "Randall",
        "Birth Month": "February",
        "City": "Nashville",
        "Income": 445000
    },
    {
        "Name": "Austin",
        "Birth Month": "November",
        "City": "Louisville",
        "Income": 345000
    },
    {
        "Name": "Carla",
        "Birth Month": "February",
        "City": "Indianapolis",
        "Income": 385000
    },
    {
        "Name": "Kara",
        "Birth Month": "March",
        "City": "Los Angeles",
        "Income": 245000
    },
    {
        "Name": "Camden",
        "Birth Month": "September",
        "City": "Phoenix",
        "Income": 430000
    },
    {
        "Name": "Rachel",
        "Birth Month": "January",
        "City": "Washington",
        "Income": 30000
    }
]
<end>Transform this JSON structure to a plain text format:
[
    {
        "Product Name": "Gizmo",
        "SKU": "SKU-1051",
        "Stock Quantity": 222,
        "Category": "Household",
        "Supplier Name": "Wonka Industries"
    },
    {
        "Product Name": "Thingamajig",
        "SKU": "SKU-1061",
        "Stock Quantity": 186,
        "Category": "Automotive",
        "Supplier Name": "Wonka Industries"
    },
    {
        "Product Name": "Gadget",
        "SKU": "SKU-1093",
        "Stock Quantity": 202,
        "Category": "Household",
        "Supplier Name": "Wayne Enterprises"
    },
    {
        "Product Name": "Contraption",
        "SKU": "SKU-1021",
        "Stock Quantity": 130,
        "Category": "Household",
        "Supplier Name": "Wonka Industries"
    },
    {
        "Product Name": "Widget",
        "SKU": "SKU-1095",
        "Stock Quantity": 413,
        "Category": "Toys",
        "Supplier Name": "Globex"
    },
    {
        "Product Name": "Contraption",
        "SKU": "SKU-1055",
        "Stock Quantity": 206,
        "Category": "Automotive",
        "Supplier Name": "Wayne Enterprises"
    },
    {
        "Product Name": "Whatchamacallit",
        "SKU": "SKU-1096",
        "Stock Quantity": 4,
        "Category": "Toys",
        "Supplier Name": "Wayne Enterprises"
    },
    {
        "Product Name": "Gadget",
        "SKU": "SKU-1029",
        "Stock Quantity": 312,
        "Category": "Toys",
        "Supplier Name": "ACME Corp"
    },
    {
        "Product Name": "Contraption",
        "SKU": "SKU-1083",
        "Stock Quantity": 226,
        "Category": "Sports",
        "Supplier Name": "Wonka Industries"
    }
]<start>
Product Name: Gizmo | SKU: SKU-1051 | Stock Quantity: 222 | Category: Household | Supplier Name: Wonka Industries
Product Name: Thingamajig | SKU: SKU-1061 | Stock Quantity: 186 | Category: Automotive | Supplier Name: Wonka Industries
Product Name: Gadget | SKU: SKU-1093 | Stock Quantity: 202 | Category: Household | Supplier Name: Wayne Enterprises
Product Name: Contraption | SKU: SKU-1021 | Stock Quantity: 130 | Category: Household | Supplier Name: Wonka Industries
Product Name: Widget | SKU: SKU-1095 | Stock Quantity: 413 | Category: Toys | Supplier Name: Globex
Product Name: Contraption | SKU: SKU-1055 | Stock Quantity: 206 | Category: Automotive | Supplier Name: Wayne Enterprises
Product Name: Whatchamacallit | SKU: SKU-1096 | Stock Quantity: 4 | Category: Toys | Supplier Name: Wayne Enterprises
Product Name: Gadget | SKU: SKU-1029 | Stock Quantity: 312 | Category: Toys | Supplier Name: ACME Corp
Product Name: Contraption | SKU: SKU-1083 | Stock Quantity: 226 | Category: Sports | Supplier Name: Wonka Industries
<end>Convert this plain text to Json:
Location: New York | Rating: 1
Location: New York | Rating: 1
Location: Seattle | Rating: 5
Location: San Francisco | Rating: 5
<start>
[
    {
        "Location": "New York",
        "Rating": 1
    },
    {
        "Location": "New York",
        "Rating": 1
    },
    {
        "Location": "Seattle",
        "Rating": 5
    },
    {
        "Location": "San Francisco",
        "Rating": 5
    }
]
<end>Please transform the following YML data into MARKDOWN:
- Price: 142.77
  Product Name: Whatchamacallit
  SKU: SKU-1005
  Stock Quantity: 456
  Supplier Name: Wayne Enterprises
- Price: 167.28
  Product Name: Gadget
  SKU: SKU-1005
  Stock Quantity: 430
  Supplier Name: Globex
- Price: 22.98
  Product Name: Device
  SKU: SKU-1042
  Stock Quantity: 29
  Supplier Name: Wayne Enterprises
- Price: 411.59
  Product Name: Gizmo
  SKU: SKU-1061
  Stock Quantity: 356
  Supplier Name: Wayne Enterprises
- Price: 411.34
  Product Name: Gizmo
  SKU: SKU-1033
  Stock Quantity: 82
  Supplier Name: Wayne Enterprises
- Price: 352.25
  Product Name: Doohickey
  SKU: SKU-1074
  Stock Quantity: 148
  Supplier Name: Umbrella Corp
- Price: 226.15
  Product Name: Thingamajig
  SKU: SKU-1061
  Stock Quantity: 329
  Supplier Name: ACME Corp
- Price: 81.35
  Product Name: Gizmo
  SKU: SKU-1088
  Stock Quantity: 209
  Supplier Name: ACME Corp
- Price: 45.51
  Product Name: Doohickey
  SKU: SKU-1081
  Stock Quantity: 81
  Supplier Name: Wonka Industries
<start>
| Product Name | SKU | Price | Stock Quantity | Supplier Name |
| --- | --- | --- | --- | --- |
| Whatchamacallit | SKU-1005 | 142.77 | 456 | Wayne Enterprises |
| Gadget | SKU-1005 | 167.28 | 430 | Globex |
| Device | SKU-1042 | 22.98 | 29 | Wayne Enterprises |
| Gizmo | SKU-1061 | 411.59 | 356 | Wayne Enterprises |
| Gizmo | SKU-1033 | 411.34 | 82 | Wayne Enterprises |
| Doohickey | SKU-1074 | 352.25 | 148 | Umbrella Corp |
| Thingamajig | SKU-1061 | 226.15 | 329 | ACME Corp |
| Gizmo | SKU-1088 | 81.35 | 209 | ACME Corp |
| Doohickey | SKU-1081 | 45.51 | 81 | Wonka Industries |
<end>Please transform the following yaml data into Json:
- Close Price: 134.19
  Company: HealthGen
  Date: '2023-10-07'
  High Price: 1296.57
  Low Price: 134.19
  Volume: 4120807
- Close Price: 583.85
  Company: RetailWorld
  Date: '2023-10-06'
  High Price: 1316.42
  Low Price: 583.85
  Volume: 9353393
- Close Price: 101.58
  Company: GreenEnergy
  Date: '2016-12-09'
  High Price: 1343.43
  Low Price: 24.99
  Volume: 8434330
- Close Price: 190.82
  Company: HealthGen
  Date: '2015-12-14'
  High Price: 1096.59
  Low Price: 190.82
  Volume: 6282383
- Close Price: 452.12
  Company: HealthGen
  Date: '2023-01-17'
  High Price: 1355.48
  Low Price: 452.12
  Volume: 4010380
<start>
[
    {
        "Company": "HealthGen",
        "Date": "2023-10-07",
        "Close Price": 134.19,
        "High Price": 1296.57,
        "Low Price": 134.19,
        "Volume": 4120807
    },
    {
        "Company": "RetailWorld",
        "Date": "2023-10-06",
        "Close Price": 583.85,
        "High Price": 1316.42,
        "Low Price": 583.85,
        "Volume": 9353393
    },
    {
        "Company": "GreenEnergy",
        "Date": "2016-12-09",
        "Close Price": 101.58,
        "High Price": 1343.43,
        "Low Price": 24.99,
        "Volume": 8434330
    },
    {
        "Company": "HealthGen",
        "Date": "2015-12-14",
        "Close Price": 190.82,
        "High Price": 1096.59,
        "Low Price": 190.82,
        "Volume": 6282383
    },
    {
        "Company": "HealthGen",
        "Date": "2023-01-17",
        "Close Price": 452.12,
        "High Price": 1355.48,
        "Low Price": 452.12,
        "Volume": 4010380
    }
]
<end>Convert this Plain text to MARKDOWN:
Name: Nicole | Birth Month: September | Income: 270000
Name: Barbara | Birth Month: February | Income: 55000
Name: George | Birth Month: November | Income: 225000
Name: Harrison | Birth Month: March | Income: 155000
Name: Roxanne | Birth Month: December | Income: 380000
Name: Leo | Birth Month: October | Income: 400000
<start>
| Name | Birth Month | Income |
| --- | --- | --- |
| Nicole | September | 270000 |
| Barbara | February | 55000 |
| George | November | 225000 |
| Harrison | March | 155000 |
| Roxanne | December | 380000 |
| Leo | October | 400000 |
<end>Please transform the following markdown data into yaml:
| Device ID | Battery Level (%) | Reading Value | Timestamp |
| --- | --- | --- | --- |
| device-0033 | 22.0 | 73.83 | 2023-09-20 06:39:57 |
| device-0055 | 49.0 | 77.63 | 2023-10-03 16:41:45 |
| device-0032 | 50.3 | 72.2 | 2023-07-04 20:22:43 |
| device-0091 | 26.9 | 41.02 | 2023-01-16 03:47:02 |
| device-0041 | 74.2 | -6.54 | 2022-09-22 11:27:42 |
| device-0010 | 70.5 | 1.51 | 2023-06-08 16:49:31 |
| device-0068 | 13.7 | -12.28 | 2022-09-21 00:13:25 |
| device-0050 | 61.2 | 32.92 | 2023-10-12 12:22:17 |
| device-0020 | 45.2 | 79.62 | 2022-01-16 01:05:08 |<start>
- Battery Level (%): 22.0
  Device ID: device-0033
  Reading Value: 73.83
  Timestamp: '2023-09-20 06:39:57'
- Battery Level (%): 49.0
  Device ID: device-0055
  Reading Value: 77.63
  Timestamp: '2023-10-03 16:41:45'
- Battery Level (%): 50.3
  Device ID: device-0032
  Reading Value: 72.2
  Timestamp: '2023-07-04 20:22:43'
- Battery Level (%): 26.9
  Device ID: device-0091
  Reading Value: 41.02
  Timestamp: '2023-01-16 03:47:02'
- Battery Level (%): 74.2
  Device ID: device-0041
  Reading Value: -6.54
  Timestamp: '2022-09-22 11:27:42'
- Battery Level (%): 70.5
  Device ID: device-0010
  Reading Value: 1.51
  Timestamp: '2023-06-08 16:49:31'
- Battery Level (%): 13.7
  Device ID: device-0068
  Reading Value: -12.28
  Timestamp: '2022-09-21 00:13:25'
- Battery Level (%): 61.2
  Device ID: device-0050
  Reading Value: 32.92
  Timestamp: '2023-10-12 12:22:17'
- Battery Level (%): 45.2
  Device ID: device-0020
  Reading Value: 79.62
  Timestamp: '2022-01-16 01:05:08'
<end>Here's some csv data, can you convert it to Json?
Company,Date,Close Price,High Price,Low Price,Volume
FinanceTrust,2018-12-25,821.15,821.15,292.62,1429666
GreenEnergy,2010-10-19,1412.95,1412.95,963.21,1134215
AutoMotive,2021-10-25,1218.45,1218.45,1078.55,1134215
MediaGroup,2010-09-09,1271.64,1271.64,339.24,6964792
AeroSystems,2018-09-03,1020.06,1020.06,153.79,9118236
GreenEnergy,2010-12-05,201.0,1237.13,201.0,1517488
<start>
[
    {
        "Company": "FinanceTrust",
        "Date": "2018-12-25",
        "Close Price": 821.15,
        "High Price": 821.15,
        "Low Price": 292.62,
        "Volume": 1429666
    },
    {
        "Company": "GreenEnergy",
        "Date": "2010-10-19",
        "Close Price": 1412.95,
        "High Price": 1412.95,
        "Low Price": 963.21,
        "Volume": 1134215
    },
    {
        "Company": "AutoMotive",
        "Date": "2021-10-25",
        "Close Price": 1218.45,
        "High Price": 1218.45,
        "Low Price": 1078.55,
        "Volume": 1134215
    },
    {
        "Company": "MediaGroup",
        "Date": "2010-09-09",
        "Close Price": 1271.64,
        "High Price": 1271.64,
        "Low Price": 339.24,
        "Volume": 6964792
    },
    {
        "Company": "AeroSystems",
        "Date": "2018-09-03",
        "Close Price": 1020.06,
        "High Price": 1020.06,
        "Low Price": 153.79,
        "Volume": 9118236
    },
    {
        "Company": "GreenEnergy",
        "Date": "2010-12-05",
        "Close Price": 201.0,
        "High Price": 1237.13,
        "Low Price": 201.0,
        "Volume": 1517488
    }
]
<end>Can you change this MARKDOWN into YML?
| Company | Sector | Market Cap |
| --- | --- | --- |
| AutoDrive | Biotech | Mega Cap |
| RetailHub | Healthcare | Mega Cap |
| AeroSpace | Automotive | Small Cap |
| RetailHub | Healthcare | Mid Cap |<start>
- Company: AutoDrive
  Market Cap: Mega Cap
  Sector: Biotech
- Company: RetailHub
  Market Cap: Mega Cap
  Sector: Healthcare
- Company: AeroSpace
  Market Cap: Small Cap
  Sector: Automotive
- Company: RetailHub
  Market Cap: Mid Cap
  Sector: Healthcare
<end>Please transform the following plain text data into Markdown:
SKU: SKU-1003 | Price: 59.45 | Stock Quantity: 299
SKU: SKU-1027 | Price: 124.39 | Stock Quantity: 381
SKU: SKU-1047 | Price: 255.66 | Stock Quantity: 288
SKU: SKU-1094 | Price: 438.75 | Stock Quantity: 184
SKU: SKU-1091 | Price: 214.85 | Stock Quantity: 174
<start>
| SKU | Price | Stock Quantity |
| --- | --- | --- |
| SKU-1003 | 59.45 | 299 |
| SKU-1027 | 124.39 | 381 |
| SKU-1047 | 255.66 | 288 |
| SKU-1094 | 438.75 | 184 |
| SKU-1091 | 214.85 | 174 |
<end>Transform this YAML structure to a Json format:
- Average Latency (ms): 87.3
  Cache Hit Ratio (%): 76.67
  Connection Count: 63
- Average Latency (ms): 96.88
  Cache Hit Ratio (%): 84.17
  Connection Count: 434
- Average Latency (ms): 88.51
  Cache Hit Ratio (%): 81.02
  Connection Count: 284
- Average Latency (ms): 83.59
  Cache Hit Ratio (%): 92.81
  Connection Count: 408
- Average Latency (ms): 49.96
  Cache Hit Ratio (%): 75.13
  Connection Count: 239
<start>
[
    {
        "Cache Hit Ratio (%)": 76.67,
        "Connection Count": 63,
        "Average Latency (ms)": 87.3
    },
    {
        "Cache Hit Ratio (%)": 84.17,
        "Connection Count": 434,
        "Average Latency (ms)": 96.88
    },
    {
        "Cache Hit Ratio (%)": 81.02,
        "Connection Count": 284,
        "Average Latency (ms)": 88.51
    },
    {
        "Cache Hit Ratio (%)": 92.81,
        "Connection Count": 408,
        "Average Latency (ms)": 83.59
    },
    {
        "Cache Hit Ratio (%)": 75.13,
        "Connection Count": 239,
        "Average Latency (ms)": 49.96
    }
]
<end>Can you change this json into yaml?
[
    {
        "Company": "TechnoCorp",
        "Date": "2016-07-15",
        "Open Price": 116.37,
        "Close Price": 611.74,
        "Low Price": 116.37,
        "Volume": 7741582
    },
    {
        "Company": "FinanceTrust",
        "Date": "2018-03-21",
        "Open Price": 569.47,
        "Close Price": 1445.0,
        "Low Price": 448.0,
        "Volume": 326946
    },
    {
        "Company": "TechnoCorp",
        "Date": "2023-02-14",
        "Open Price": 382.5,
        "Close Price": 596.14,
        "Low Price": 382.5,
        "Volume": 4473781
    }
]<start>
- Close Price: 611.74
  Company: TechnoCorp
  Date: '2016-07-15'
  Low Price: 116.37
  Open Price: 116.37
  Volume: 7741582
- Close Price: 1445.0
  Company: FinanceTrust
  Date: '2018-03-21'
  Low Price: 448.0
  Open Price: 569.47
  Volume: 326946
- Close Price: 596.14
  Company: TechnoCorp
  Date: '2023-02-14'
  Low Price: 382.5
  Open Price: 382.5
  Volume: 4473781
<end>Convert this Yaml to Csv:
- Box Office Earnings (M): 844.06
  Director: Aria Ravenwood
  Genre: Fantasy
  Title: Beyond the Veil
- Box Office Earnings (M): 444.33
  Director: Selene Darkwhisper
  Genre: Comedy
  Title: Starbound Odyssey
- Box Office Earnings (M): 23.76
  Director: Mara Moonshadow
  Genre: Adventure
  Title: Mystery of the Depths
<start>
Title,Director,Genre,Box Office Earnings (M)
Beyond the Veil,Aria Ravenwood,Fantasy,844.06
Starbound Odyssey,Selene Darkwhisper,Comedy,444.33
Mystery of the Depths,Mara Moonshadow,Adventure,23.76
<end>Convert this markdown to PLAIN TEXT:
| Location | Condition | Temperature (C) | Humidity (%) | Day |
| --- | --- | --- | --- | --- |
| Chicago | Cloudy | 30.8 | 68 | Tuesday |
| Phoenix | Foggy | 31.6 | 94 | Thursday |
| Denver | Cloudy | 16.1 | 52 | Friday |
| Phoenix | Foggy | 16.2 | 94 | Saturday |
| Denver | Snowy | 12.1 | 91 | Thursday |
| Chicago | Stormy | 15.1 | 68 | Wednesday |
| Miami | Stormy | 4.2 | 30 | Thursday |
| Los Angeles | Stormy | 21.4 | 37 | Sunday |<start>
Location: Chicago | Condition: Cloudy | Temperature (C): 30.8 | Humidity (%): 68 | Day: Tuesday
Location: Phoenix | Condition: Foggy | Temperature (C): 31.6 | Humidity (%): 94 | Day: Thursday
Location: Denver | Condition: Cloudy | Temperature (C): 16.1 | Humidity (%): 52 | Day: Friday
Location: Phoenix | Condition: Foggy | Temperature (C): 16.2 | Humidity (%): 94 | Day: Saturday
Location: Denver | Condition: Snowy | Temperature (C): 12.1 | Humidity (%): 91 | Day: Thursday
Location: Chicago | Condition: Stormy | Temperature (C): 15.1 | Humidity (%): 68 | Day: Wednesday
Location: Miami | Condition: Stormy | Temperature (C): 4.2 | Humidity (%): 30 | Day: Thursday
Location: Los Angeles | Condition: Stormy | Temperature (C): 21.4 | Humidity (%): 37 | Day: Sunday
<end>Can you change this json into csv?
[
    {
        "Restaurant Name": "The Steakhouse",
        "Cuisine": "Chinese",
        "Price Range": "$$$$"
    },
    {
        "Restaurant Name": "Pasta Palace",
        "Cuisine": "American",
        "Price Range": "$"
    },
    {
        "Restaurant Name": "The Golden Spoon",
        "Cuisine": "American",
        "Price Range": "$$$$"
    },
    {
        "Restaurant Name": "Pasta Palace",
        "Cuisine": "American",
        "Price Range": "$"
    },
    {
        "Restaurant Name": "The Steakhouse",
        "Cuisine": "French",
        "Price Range": "$$$$"
    }
]<start>
Restaurant Name,Cuisine,Price Range
The Steakhouse,Chinese,$$$$
Pasta Palace,American,$
The Golden Spoon,American,$$$$
Pasta Palace,American,$
The Steakhouse,French,$$$$
<end>Transform this PLAIN TEXT structure to a csv format:
Title: Mystery of the Depths | Director: Zara Stormrider | Genre: Adventure | Release Year: 2020 | Box Office Earnings (M): 966.74
Title: The Endless Horizon | Director: Talon Blackthorn | Genre: Horror | Release Year: 1971 | Box Office Earnings (M): 979.16
Title: Beyond the Veil | Director: Zara Stormrider | Genre: Sci-Fi | Release Year: 2017 | Box Office Earnings (M): 496.63
Title: Mystery of the Depths | Director: Orin Shadowalker | Genre: Comedy | Release Year: 2017 | Box Office Earnings (M): 627.87
Title: Dreamwalker | Director: Cade Firebrand | Genre: Sci-Fi | Release Year: 2018 | Box Office Earnings (M): 454.68
<start>
Title,Director,Genre,Release Year,Box Office Earnings (M)
Mystery of the Depths,Zara Stormrider,Adventure,2020,966.74
The Endless Horizon,Talon Blackthorn,Horror,1971,979.16
Beyond the Veil,Zara Stormrider,Sci-Fi,2017,496.63
Mystery of the Depths,Orin Shadowalker,Comedy,2017,627.87
Dreamwalker,Cade Firebrand,Sci-Fi,2018,454.68
<end>Please transform the following plain text data into yml:
Company: HealthGen | Date: 2010-06-05 | Close Price: 125.53 | High Price: 912.49 | Low Price: 125.53 | Volume: 2889774
Company: RetailWorld | Date: 2011-11-03 | Close Price: 295.24 | High Price: 1202.25 | Low Price: 74.57 | Volume: 9110066
Company: FoodChain | Date: 2010-12-06 | Close Price: 474.49 | High Price: 636.59 | Low Price: 262.2 | Volume: 2469388
Company: GreenEnergy | Date: 2016-11-22 | Close Price: 465.13 | High Price: 1346.72 | Low Price: 110.25 | Volume: 5509112
Company: BioLife | Date: 2019-05-28 | Close Price: 39.99 | High Price: 313.74 | Low Price: 39.99 | Volume: 550394
Company: RetailWorld | Date: 2017-06-23 | Close Price: 843.38 | High Price: 1266.39 | Low Price: 560.54 | Volume: 5185557
Company: AutoMotive | Date: 2013-04-11 | Close Price: 828.53 | High Price: 1231.79 | Low Price: 275.88 | Volume: 8083983
Company: MediaGroup | Date: 2014-06-02 | Close Price: 1109.48 | High Price: 1202.25 | Low Price: 891.22 | Volume: 3788300
Company: RetailWorld | Date: 2023-10-19 | Close Price: 1280.23 | High Price: 1280.23 | Low Price: 12.68 | Volume: 7424908
Company: BioLife | Date: 2023-04-12 | Close Price: 897.04 | High Price: 1265.14 | Low Price: 897.04 | Volume: 8774309
<start>
- Close Price: 125.53
  Company: HealthGen
  Date: '2010-06-05'
  High Price: 912.49
  Low Price: 125.53
  Volume: 2889774
- Close Price: 295.24
  Company: RetailWorld
  Date: '2011-11-03'
  High Price: 1202.25
  Low Price: 74.57
  Volume: 9110066
- Close Price: 474.49
  Company: FoodChain
  Date: '2010-12-06'
  High Price: 636.59
  Low Price: 262.2
  Volume: 2469388
- Close Price: 465.13
  Company: GreenEnergy
  Date: '2016-11-22'
  High Price: 1346.72
  Low Price: 110.25
  Volume: 5509112
- Close Price: 39.99
  Company: BioLife
  Date: '2019-05-28'
  High Price: 313.74
  Low Price: 39.99
  Volume: 550394
- Close Price: 843.38
  Company: RetailWorld
  Date: '2017-06-23'
  High Price: 1266.39
  Low Price: 560.54
  Volume: 5185557
- Close Price: 828.53
  Company: AutoMotive
  Date: '2013-04-11'
  High Price: 1231.79
  Low Price: 275.88
  Volume: 8083983
- Close Price: 1109.48
  Company: MediaGroup
  Date: '2014-06-02'
  High Price: 1202.25
  Low Price: 891.22
  Volume: 3788300
- Close Price: 1280.23
  Company: RetailWorld
  Date: '2023-10-19'
  High Price: 1280.23
  Low Price: 12.68
  Volume: 7424908
- Close Price: 897.04
  Company: BioLife
  Date: '2023-04-12'
  High Price: 1265.14
  Low Price: 897.04
  Volume: 8774309
<end>Convert this CSV to YAML:
Author,Genre,Publication Year,Rating
Luna Silverleaf,Mystery,1951,1.2
Rowan Ashborne,Science Fiction,1983,4.4
Rowan Ashborne,Romance,1991,2.5
Orion Frostblade,Thriller,1984,2.5
Galen Starfire,Mystery,2023,3.2
Sylvia Nightshade,Horror,1969,1.2
<start>
- Author: Luna Silverleaf
  Genre: Mystery
  Publication Year: 1951
  Rating: 1.2
- Author: Rowan Ashborne
  Genre: Science Fiction
  Publication Year: 1983
  Rating: 4.4
- Author: Rowan Ashborne
  Genre: Romance
  Publication Year: 1991
  Rating: 2.5
- Author: Orion Frostblade
  Genre: Thriller
  Publication Year: 1984
  Rating: 2.5
- Author: Galen Starfire
  Genre: Mystery
  Publication Year: 2023
  Rating: 3.2
- Author: Sylvia Nightshade
  Genre: Horror
  Publication Year: 1969
  Rating: 1.2
<end>Convert this JSON to Markdown:
[
    {
        "Location": "Seattle",
        "Condition": "Rainy",
        "Temperature (C)": 32.9,
        "Humidity (%)": 32,
        "Wind Speed (km/h)": 1.6,
        "Day": "Saturday"
    },
    {
        "Location": "Seattle",
        "Condition": "Foggy",
        "Temperature (C)": 32.3,
        "Humidity (%)": 97,
        "Wind Speed (km/h)": 16.2,
        "Day": "Sunday"
    },
    {
        "Location": "Chicago",
        "Condition": "Snowy",
        "Temperature (C)": -7.1,
        "Humidity (%)": 39,
        "Wind Speed (km/h)": 19.2,
        "Day": "Sunday"
    },
    {
        "Location": "New York",
        "Condition": "Rainy",
        "Temperature (C)": 1.6,
        "Humidity (%)": 84,
        "Wind Speed (km/h)": 14.4,
        "Day": "Wednesday"
    },
    {
        "Location": "Houston",
        "Condition": "Windy",
        "Temperature (C)": 12.9,
        "Humidity (%)": 41,
        "Wind Speed (km/h)": 28.9,
        "Day": "Sunday"
    },
    {
        "Location": "Denver",
        "Condition": "Rainy",
        "Temperature (C)": -8.1,
        "Humidity (%)": 27,
        "Wind Speed (km/h)": 27.8,
        "Day": "Wednesday"
    },
    {
        "Location": "Phoenix",
        "Condition": "Windy",
        "Temperature (C)": 2.6,
        "Humidity (%)": 53,
        "Wind Speed (km/h)": 8.8,
        "Day": "Saturday"
    },
    {
        "Location": "Miami",
        "Condition": "Windy",
        "Temperature (C)": -1.6,
        "Humidity (%)": 100,
        "Wind Speed (km/h)": 20.4,
        "Day": "Thursday"
    },
    {
        "Location": "Los Angeles",
        "Condition": "Windy",
        "Temperature (C)": 11.4,
        "Humidity (%)": 54,
        "Wind Speed (km/h)": 20.5,
        "Day": "Wednesday"
    }
]<start>
| Location | Condition | Temperature (C) | Humidity (%) | Wind Speed (km/h) | Day |
| --- | --- | --- | --- | --- | --- |
| Seattle | Rainy | 32.9 | 32 | 1.6 | Saturday |
| Seattle | Foggy | 32.3 | 97 | 16.2 | Sunday |
| Chicago | Snowy | -7.1 | 39 | 19.2 | Sunday |
| New York | Rainy | 1.6 | 84 | 14.4 | Wednesday |
| Houston | Windy | 12.9 | 41 | 28.9 | Sunday |
| Denver | Rainy | -8.1 | 27 | 27.8 | Wednesday |
| Phoenix | Windy | 2.6 | 53 | 8.8 | Saturday |
| Miami | Windy | -1.6 | 100 | 20.4 | Thursday |
| Los Angeles | Windy | 11.4 | 54 | 20.5 | Wednesday |
<end>Please transform the following MARKDOWN data into JSON:
| Title | Director | Genre | Release Year | Box Office Earnings (M) |
| --- | --- | --- | --- | --- |
| Escape from Earth | Drake Nightshade | Sci-Fi | 2023 | 351.58 |
| Edge of Infinity | Orin Shadowalker | Drama | 2017 | 90.81 |
| Mystery of the Depths | Orin Shadowalker | Adventure | 2013 | 519.71 |
| The Final Voyage | Zara Stormrider | Thriller | 1984 | 287.27 |
| Escape from Earth | Orin Shadowalker | Comedy | 1980 | 282.05 |
| Rise of the Titans | Selene Darkwhisper | Horror | 1996 | 815.93 |
| The Final Voyage | Zara Stormrider | Action | 2017 | 178.93 |
| Rise of the Titans | Selene Darkwhisper | Action | 2023 | 542.3 |
| The Great Expedition | Rylan Frostblade | Thriller | 2013 | 723.77 |<start>
[
    {
        "Title": "Escape from Earth",
        "Director": "Drake Nightshade",
        "Genre": "Sci-Fi",
        "Release Year": 2023,
        "Box Office Earnings (M)": 351.58
    },
    {
        "Title": "Edge of Infinity",
        "Director": "Orin Shadowalker",
        "Genre": "Drama",
        "Release Year": 2017,
        "Box Office Earnings (M)": 90.81
    },
    {
        "Title": "Mystery of the Depths",
        "Director": "Orin Shadowalker",
        "Genre": "Adventure",
        "Release Year": 2013,
        "Box Office Earnings (M)": 519.71
    },
    {
        "Title": "The Final Voyage",
        "Director": "Zara Stormrider",
        "Genre": "Thriller",
        "Release Year": 1984,
        "Box Office Earnings (M)": 287.27
    },
    {
        "Title": "Escape from Earth",
        "Director": "Orin Shadowalker",
        "Genre": "Comedy",
        "Release Year": 1980,
        "Box Office Earnings (M)": 282.05
    },
    {
        "Title": "Rise of the Titans",
        "Director": "Selene Darkwhisper",
        "Genre": "Horror",
        "Release Year": 1996,
        "Box Office Earnings (M)": 815.93
    },
    {
        "Title": "The Final Voyage",
        "Director": "Zara Stormrider",
        "Genre": "Action",
        "Release Year": 2017,
        "Box Office Earnings (M)": 178.93
    },
    {
        "Title": "Rise of the Titans",
        "Director": "Selene Darkwhisper",
        "Genre": "Action",
        "Release Year": 2023,
        "Box Office Earnings (M)": 542.3
    },
    {
        "Title": "The Great Expedition",
        "Director": "Rylan Frostblade",
        "Genre": "Thriller",
        "Release Year": 2013,
        "Box Office Earnings (M)": 723.77
    }
]
<end>Transform this yaml structure to a PLAIN TEXT format:
- Age: 60
  Birth Month: May
  City: Denver
  Income: 130000
  Name: Johnathan
- Age: 64
  Birth Month: October
  City: Indianapolis
  Income: 245000
  Name: Edward
- Age: 20
  Birth Month: September
  City: Denver
  Income: 65000
  Name: Arnold
- Age: 34
  Birth Month: June
  City: Charlotte
  Income: 290000
  Name: Kristin
- Age: 38
  Birth Month: May
  City: Dallas
  Income: 235000
  Name: Skylar
- Age: 47
  Birth Month: February
  City: San Francisco
  Income: 250000
  Name: Alta
- Age: 49
  Birth Month: May
  City: Charlotte
  Income: 415000
  Name: Leila
- Age: 35
  Birth Month: August
  City: Memphis
  Income: 405000
  Name: Arnold
- Age: 21
  Birth Month: September
  City: San Jose
  Income: 25000
  Name: Simon
<start>
Name: Johnathan | Age: 60 | Birth Month: May | City: Denver | Income: 130000
Name: Edward | Age: 64 | Birth Month: October | City: Indianapolis | Income: 245000
Name: Arnold | Age: 20 | Birth Month: September | City: Denver | Income: 65000
Name: Kristin | Age: 34 | Birth Month: June | City: Charlotte | Income: 290000
Name: Skylar | Age: 38 | Birth Month: May | City: Dallas | Income: 235000
Name: Alta | Age: 47 | Birth Month: February | City: San Francisco | Income: 250000
Name: Leila | Age: 49 | Birth Month: May | City: Charlotte | Income: 415000
Name: Arnold | Age: 35 | Birth Month: August | City: Memphis | Income: 405000
Name: Simon | Age: 21 | Birth Month: September | City: San Jose | Income: 25000
<end>Here's some yaml data, can you convert it to Plain text?
- Author: Luna Silverleaf
  Publication Year: 1968
  Rating: 4.8
- Author: Thorne Ironwood
  Publication Year: 1959
  Rating: 1.4
- Author: Luna Silverleaf
  Publication Year: 1990
  Rating: 3.7
- Author: Elara Moonshadow
  Publication Year: 1969
  Rating: 3.7
- Author: Orion Frostblade
  Publication Year: 2019
  Rating: 3.6
<start>
Author: Luna Silverleaf | Publication Year: 1968 | Rating: 4.8
Author: Thorne Ironwood | Publication Year: 1959 | Rating: 1.4
Author: Luna Silverleaf | Publication Year: 1990 | Rating: 3.7
Author: Elara Moonshadow | Publication Year: 1969 | Rating: 3.7
Author: Orion Frostblade | Publication Year: 2019 | Rating: 3.6
<end>Please transform the following JSON data into PLAIN TEXT:
[
    {
        "Trip Name": "Valley Voyage",
        "Start Location": "Denver",
        "End Location": "Houston",
        "Distance (miles)": 672.8,
        "Duration (hours)": 35.5,
        "Fuel Used (gallons)": 27.6
    },
    {
        "Trip Name": "Canyon Trek",
        "Start Location": "Houston",
        "End Location": "Phoenix",
        "Distance (miles)": 224.8,
        "Duration (hours)": 31.7,
        "Fuel Used (gallons)": 84.6
    },
    {
        "Trip Name": "Valley Voyage",
        "Start Location": "New York",
        "End Location": "San Francisco",
        "Distance (miles)": 1043.8,
        "Duration (hours)": 12.7,
        "Fuel Used (gallons)": 42.9
    }
]<start>
Trip Name: Valley Voyage | Start Location: Denver | End Location: Houston | Distance (miles): 672.8 | Duration (hours): 35.5 | Fuel Used (gallons): 27.6
Trip Name: Canyon Trek | Start Location: Houston | End Location: Phoenix | Distance (miles): 224.8 | Duration (hours): 31.7 | Fuel Used (gallons): 84.6
Trip Name: Valley Voyage | Start Location: New York | End Location: San Francisco | Distance (miles): 1043.8 | Duration (hours): 12.7 | Fuel Used (gallons): 42.9
<end>Transform this csv structure to a plain text format:
Market Cap,Annual Revenue (B),Quarter
Mega Cap,433.02,Q1
Mega Cap,481.61,Q3
Mega Cap,297.41,Q1
Large Cap,439.74,Q4
Mid Cap,494.19,Q2
Small Cap,192.98,Q3
<start>
Market Cap: Mega Cap | Annual Revenue (B): 433.02 | Quarter: Q1
Market Cap: Mega Cap | Annual Revenue (B): 481.61 | Quarter: Q3
Market Cap: Mega Cap | Annual Revenue (B): 297.41 | Quarter: Q1
Market Cap: Large Cap | Annual Revenue (B): 439.74 | Quarter: Q4
Market Cap: Mid Cap | Annual Revenue (B): 494.19 | Quarter: Q2
Market Cap: Small Cap | Annual Revenue (B): 192.98 | Quarter: Q3
<end>Please transform the following markdown data into yml:
| Name | Birth Month | Income |
| --- | --- | --- |
| Elva | May | 325000 |
| Brooklynn | September | 280000 |
| Alta | May | 340000 |<start>
- Birth Month: May
  Income: 325000
  Name: Elva
- Birth Month: September
  Income: 280000
  Name: Brooklynn
- Birth Month: May
  Income: 340000
  Name: Alta
<end>Transform this Yml structure to a json format:
- Distance (miles): 730.6
  Fuel Used (gallons): 23.3
  Start Location: Los Angeles
  Trip Name: Desert Drive
- Distance (miles): 2329.6
  Fuel Used (gallons): 13.5
  Start Location: Houston
  Trip Name: Historic Route
- Distance (miles): 1115.1
  Fuel Used (gallons): 39.6
  Start Location: Los Angeles
  Trip Name: City Explorer
- Distance (miles): 1159.1
  Fuel Used (gallons): 9.0
  Start Location: San Francisco
  Trip Name: Desert Drive
- Distance (miles): 730.6
  Fuel Used (gallons): 41.8
  Start Location: New York
  Trip Name: Highway Odyssey
- Distance (miles): 318.4
  Fuel Used (gallons): 5.1
  Start Location: Houston
  Trip Name: Historic Route
- Distance (miles): 1771.3
  Fuel Used (gallons): 71.8
  Start Location: Miami
  Trip Name: Valley Voyage
- Distance (miles): 1154.5
  Fuel Used (gallons): 33.7
  Start Location: San Francisco
  Trip Name: Mountain Adventure
- Distance (miles): 1685.0
  Fuel Used (gallons): 90.5
  Start Location: Denver
  Trip Name: Canyon Trek
- Distance (miles): 1685.0
  Fuel Used (gallons): 7.9
  Start Location: Denver
  Trip Name: Coast to Coast
<start>
[
    {
        "Trip Name": "Desert Drive",
        "Start Location": "Los Angeles",
        "Distance (miles)": 730.6,
        "Fuel Used (gallons)": 23.3
    },
    {
        "Trip Name": "Historic Route",
        "Start Location": "Houston",
        "Distance (miles)": 2329.6,
        "Fuel Used (gallons)": 13.5
    },
    {
        "Trip Name": "City Explorer",
        "Start Location": "Los Angeles",
        "Distance (miles)": 1115.1,
        "Fuel Used (gallons)": 39.6
    },
    {
        "Trip Name": "Desert Drive",
        "Start Location": "San Francisco",
        "Distance (miles)": 1159.1,
        "Fuel Used (gallons)": 9.0
    },
    {
        "Trip Name": "Highway Odyssey",
        "Start Location": "New York",
        "Distance (miles)": 730.6,
        "Fuel Used (gallons)": 41.8
    },
    {
        "Trip Name": "Historic Route",
        "Start Location": "Houston",
        "Distance (miles)": 318.4,
        "Fuel Used (gallons)": 5.1
    },
    {
        "Trip Name": "Valley Voyage",
        "Start Location": "Miami",
        "Distance (miles)": 1771.3,
        "Fuel Used (gallons)": 71.8
    },
    {
        "Trip Name": "Mountain Adventure",
        "Start Location": "San Francisco",
        "Distance (miles)": 1154.5,
        "Fuel Used (gallons)": 33.7
    },
    {
        "Trip Name": "Canyon Trek",
        "Start Location": "Denver",
        "Distance (miles)": 1685.0,
        "Fuel Used (gallons)": 90.5
    },
    {
        "Trip Name": "Coast to Coast",
        "Start Location": "Denver",
        "Distance (miles)": 1685.0,
        "Fuel Used (gallons)": 7.9
    }
]
<end>Please transform the following PLAIN TEXT data into yaml:
Trip Name: Historic Route | End Location: Phoenix | Duration (hours): 70.9
Trip Name: Highway Odyssey | End Location: Chicago | Duration (hours): 58.0
Trip Name: Valley Voyage | End Location: Chicago | Duration (hours): 45.7
Trip Name: Forest Journey | End Location: San Francisco | Duration (hours): 62.9
Trip Name: Lakeside Retreat | End Location: Denver | Duration (hours): 13.2
Trip Name: Lakeside Retreat | End Location: Miami | Duration (hours): 13.1
Trip Name: Lakeside Retreat | End Location: Chicago | Duration (hours): 13.2
Trip Name: Forest Journey | End Location: Chicago | Duration (hours): 32.2
Trip Name: Historic Route | End Location: New York | Duration (hours): 26.1
Trip Name: Canyon Trek | End Location: Denver | Duration (hours): 41.9
<start>
- Duration (hours): 70.9
  End Location: Phoenix
  Trip Name: Historic Route
- Duration (hours): 58.0
  End Location: Chicago
  Trip Name: Highway Odyssey
- Duration (hours): 45.7
  End Location: Chicago
  Trip Name: Valley Voyage
- Duration (hours): 62.9
  End Location: San Francisco
  Trip Name: Forest Journey
- Duration (hours): 13.2
  End Location: Denver
  Trip Name: Lakeside Retreat
- Duration (hours): 13.1
  End Location: Miami
  Trip Name: Lakeside Retreat
- Duration (hours): 13.2
  End Location: Chicago
  Trip Name: Lakeside Retreat
- Duration (hours): 32.2
  End Location: Chicago
  Trip Name: Forest Journey
- Duration (hours): 26.1
  End Location: New York
  Trip Name: Historic Route
- Duration (hours): 41.9
  End Location: Denver
  Trip Name: Canyon Trek
<end>Convert this PLAIN TEXT to json:
Restaurant Name: The Steakhouse | Cuisine: Mexican | Location: Miami | Rating: 5 | Price Range: $$$$
Restaurant Name: Vegan Delight | Cuisine: Mexican | Location: Chicago | Rating: 2 | Price Range: $$$$$
Restaurant Name: Pizza Planet | Cuisine: Italian | Location: Houston | Rating: 1 | Price Range: $$$$$
Restaurant Name: Sushi World | Cuisine: Italian | Location: Miami | Rating: 3 | Price Range: $$$
Restaurant Name: Pizza Planet | Cuisine: Indian | Location: New York | Rating: 5 | Price Range: $$$$
Restaurant Name: Sushi World | Cuisine: Indian | Location: Los Angeles | Rating: 1 | Price Range: $$$$$
<start>
[
    {
        "Restaurant Name": "The Steakhouse",
        "Cuisine": "Mexican",
        "Location": "Miami",
        "Rating": 5,
        "Price Range": "$$$$"
    },
    {
        "Restaurant Name": "Vegan Delight",
        "Cuisine": "Mexican",
        "Location": "Chicago",
        "Rating": 2,
        "Price Range": "$$$$$"
    },
    {
        "Restaurant Name": "Pizza Planet",
        "Cuisine": "Italian",
        "Location": "Houston",
        "Rating": 1,
        "Price Range": "$$$$$"
    },
    {
        "Restaurant Name": "Sushi World",
        "Cuisine": "Italian",
        "Location": "Miami",
        "Rating": 3,
        "Price Range": "$$$"
    },
    {
        "Restaurant Name": "Pizza Planet",
        "Cuisine": "Indian",
        "Location": "New York",
        "Rating": 5,
        "Price Range": "$$$$"
    },
    {
        "Restaurant Name": "Sushi World",
        "Cuisine": "Indian",
        "Location": "Los Angeles",
        "Rating": 1,
        "Price Range": "$$$$$"
    }
]
<end>Please transform the following Csv data into markdown:
SKU,Price,Category,Supplier Name
SKU-1065,174.73,Automotive,Wayne Enterprises
SKU-1020,242.01,Automotive,Umbrella Corp
SKU-1094,174.53,Automotive,Wayne Enterprises
SKU-1073,199.36,Household,Wonka Industries
SKU-1061,392.11,Household,Globex
SKU-1062,294.96,Toys,Globex
SKU-1090,279.56,Sports,Wonka Industries
SKU-1004,412.1,Automotive,Globex
<start>
| SKU | Price | Category | Supplier Name |
| --- | --- | --- | --- |
| SKU-1065 | 174.73 | Automotive | Wayne Enterprises |
| SKU-1020 | 242.01 | Automotive | Umbrella Corp |
| SKU-1094 | 174.53 | Automotive | Wayne Enterprises |
| SKU-1073 | 199.36 | Household | Wonka Industries |
| SKU-1061 | 392.11 | Household | Globex |
| SKU-1062 | 294.96 | Toys | Globex |
| SKU-1090 | 279.56 | Sports | Wonka Industries |
| SKU-1004 | 412.1 | Automotive | Globex |
<end>Here's some csv data, can you convert it to plain text?
Title,Author,Genre,Publication Year,Rating
Tales of the Brave,Rowan Ashborne,Fantasy,1995,4.5
Legends of the Rift,Rowan Ashborne,Horror,1996,4.6
The Last Sky,Luna Silverleaf,Fantasy,2022,2.6
Legends of the Rift,Kara Firebrand,Mystery,2020,2.2
Tales of the Brave,Luna Silverleaf,Romance,2003,4.5
A Journey Through Time,Rowan Ashborne,Horror,1956,3.5
Echoes of Eternity,Kara Firebrand,Non-Fiction,2020,1.1
<start>
Title: Tales of the Brave | Author: Rowan Ashborne | Genre: Fantasy | Publication Year: 1995 | Rating: 4.5
Title: Legends of the Rift | Author: Rowan Ashborne | Genre: Horror | Publication Year: 1996 | Rating: 4.6
Title: The Last Sky | Author: Luna Silverleaf | Genre: Fantasy | Publication Year: 2022 | Rating: 2.6
Title: Legends of the Rift | Author: Kara Firebrand | Genre: Mystery | Publication Year: 2020 | Rating: 2.2
Title: Tales of the Brave | Author: Luna Silverleaf | Genre: Romance | Publication Year: 2003 | Rating: 4.5
Title: A Journey Through Time | Author: Rowan Ashborne | Genre: Horror | Publication Year: 1956 | Rating: 3.5
Title: Echoes of Eternity | Author: Kara Firebrand | Genre: Non-Fiction | Publication Year: 2020 | Rating: 1.1
<end>Can you change this MARKDOWN into Plain text?
| Release Year | Box Office Earnings (M) |
| --- | --- |
| 1991 | 308.52 |
| 1993 | 308.52 |
| 2021 | 784.32 |
| 2017 | 75.84 |
| 2002 | 609.66 |
| 2017 | 102.68 |
| 2012 | 526.06 |
| 1988 | 351.36 |<start>
Release Year: 1991 | Box Office Earnings (M): 308.52
Release Year: 1993 | Box Office Earnings (M): 308.52
Release Year: 2021 | Box Office Earnings (M): 784.32
Release Year: 2017 | Box Office Earnings (M): 75.84
Release Year: 2002 | Box Office Earnings (M): 609.66
Release Year: 2017 | Box Office Earnings (M): 102.68
Release Year: 2012 | Box Office Earnings (M): 526.06
Release Year: 1988 | Box Office Earnings (M): 351.36
<end>Can you change this CSV into MARKDOWN?
Open Price,Close Price,High Price,Volume
504.62,976.89,976.89,5475807
1443.13,1182.0,1489.82,3769806
884.8,1418.69,1418.69,3419744
696.2,882.37,882.37,8349369
422.69,1124.85,1190.79,4763025
1281.53,144.6,1281.53,8670523
1197.24,1205.73,1205.73,1535649
882.37,354.03,1459.06,1150735
<start>
| Open Price | Close Price | High Price | Volume |
| --- | --- | --- | --- |
| 504.62 | 976.89 | 976.89 | 5475807 |
| 1443.13 | 1182.0 | 1489.82 | 3769806 |
| 884.8 | 1418.69 | 1418.69 | 3419744 |
| 696.2 | 882.37 | 882.37 | 8349369 |
| 422.69 | 1124.85 | 1190.79 | 4763025 |
| 1281.53 | 144.6 | 1281.53 | 8670523 |
| 1197.24 | 1205.73 | 1205.73 | 1535649 |
| 882.37 | 354.03 | 1459.06 | 1150735 |
<end>Transform this yml structure to a Csv format:
- Box Office Earnings (M): 590.38
  Director: Orin Shadowalker
  Genre: Fantasy
  Title: The Great Expedition
- Box Office Earnings (M): 92.77
  Director: Drake Nightshade
  Genre: Sci-Fi
  Title: Beyond the Veil
- Box Office Earnings (M): 178.65
  Director: Talon Blackthorn
  Genre: Action
  Title: Rise of the Titans
- Box Office Earnings (M): 993.64
  Director: Lira Silverleaf
  Genre: Drama
  Title: The Final Voyage
- Box Office Earnings (M): 33.45
  Director: Selene Darkwhisper
  Genre: Sci-Fi
  Title: The Final Voyage
- Box Office Earnings (M): 151.94
  Director: Mara Moonshadow
  Genre: Fantasy
  Title: Edge of Infinity
<start>
Title,Director,Genre,Box Office Earnings (M)
The Great Expedition,Orin Shadowalker,Fantasy,590.38
Beyond the Veil,Drake Nightshade,Sci-Fi,92.77
Rise of the Titans,Talon Blackthorn,Action,178.65
The Final Voyage,Lira Silverleaf,Drama,993.64
The Final Voyage,Selene Darkwhisper,Sci-Fi,33.45
Edge of Infinity,Mara Moonshadow,Fantasy,151.94
<end>Convert this PLAIN TEXT to Yaml:
Location: Denver | Temperature (C): 23.9 | Wind Speed (km/h): 1.1
Location: Phoenix | Temperature (C): 14.9 | Wind Speed (km/h): 0.5
Location: Denver | Temperature (C): -7.3 | Wind Speed (km/h): 7.5
Location: Los Angeles | Temperature (C): 21.5 | Wind Speed (km/h): 17.2
Location: Houston | Temperature (C): -6.7 | Wind Speed (km/h): 26.3
Location: Houston | Temperature (C): 28.8 | Wind Speed (km/h): 12.9
Location: Miami | Temperature (C): 29.7 | Wind Speed (km/h): 7.0
Location: Los Angeles | Temperature (C): 32.0 | Wind Speed (km/h): 13.6
Location: Seattle | Temperature (C): -8.6 | Wind Speed (km/h): 4.0
<start>
- Location: Denver
  Temperature (C): 23.9
  Wind Speed (km/h): 1.1
- Location: Phoenix
  Temperature (C): 14.9
  Wind Speed (km/h): 0.5
- Location: Denver
  Temperature (C): -7.3
  Wind Speed (km/h): 7.5
- Location: Los Angeles
  Temperature (C): 21.5
  Wind Speed (km/h): 17.2
- Location: Houston
  Temperature (C): -6.7
  Wind Speed (km/h): 26.3
- Location: Houston
  Temperature (C): 28.8
  Wind Speed (km/h): 12.9
- Location: Miami
  Temperature (C): 29.7
  Wind Speed (km/h): 7.0
- Location: Los Angeles
  Temperature (C): 32.0
  Wind Speed (km/h): 13.6
- Location: Seattle
  Temperature (C): -8.6
  Wind Speed (km/h): 4.0
<end>Convert this yaml to markdown:
- Genre: Drama
  Title: Escape from Earth
- Genre: Thriller
  Title: Starbound Odyssey
- Genre: Comedy
  Title: The Final Voyage
- Genre: Fantasy
  Title: The Great Expedition
- Genre: Adventure
  Title: Mystery of the Depths
- Genre: Sci-Fi
  Title: Mystery of the Depths
- Genre: Sci-Fi
  Title: Mystery of the Depths
<start>
| Title | Genre |
| --- | --- |
| Escape from Earth | Drama |
| Starbound Odyssey | Thriller |
| The Final Voyage | Comedy |
| The Great Expedition | Fantasy |
| Mystery of the Depths | Adventure |
| Mystery of the Depths | Sci-Fi |
| Mystery of the Depths | Sci-Fi |
<end>Convert this Markdown to CSV:
| Title | Author | Genre | Publication Year | Rating |
| --- | --- | --- | --- | --- |
| The Last Sky | Orion Frostblade | Non-Fiction | 2008 | 3.7 |
| The Crystal Key | Galen Starfire | Horror | 2000 | 4.2 |
| Echoes of Eternity | Draven Blackthorn | Science Fiction | 2002 | 2.5 |
| Echoes of Eternity | Rowan Ashborne | Science Fiction | 1954 | 4.6 |
| A Journey Through Time | Isla Windrider | Thriller | 1963 | 4.5 |
| Shadows of Solitude | Rowan Ashborne | Horror | 1969 | 4.6 |<start>
Title,Author,Genre,Publication Year,Rating
The Last Sky,Orion Frostblade,Non-Fiction,2008,3.7
The Crystal Key,Galen Starfire,Horror,2000,4.2
Echoes of Eternity,Draven Blackthorn,Science Fiction,2002,2.5
Echoes of Eternity,Rowan Ashborne,Science Fiction,1954,4.6
A Journey Through Time,Isla Windrider,Thriller,1963,4.5
Shadows of Solitude,Rowan Ashborne,Horror,1969,4.6
<end>Can you change this YAML into MARKDOWN?
- Distance (miles): 827.2
  End Location: Los Angeles
  Fuel Used (gallons): 46.7
  Start Location: Chicago
  Trip Name: Desert Drive
- Distance (miles): 404.6
  End Location: Houston
  Fuel Used (gallons): 87.6
  Start Location: San Francisco
  Trip Name: Canyon Trek
- Distance (miles): 2279.9
  End Location: Denver
  Fuel Used (gallons): 39.9
  Start Location: Los Angeles
  Trip Name: Forest Journey
<start>
| Trip Name | Start Location | End Location | Distance (miles) | Fuel Used (gallons) |
| --- | --- | --- | --- | --- |
| Desert Drive | Chicago | Los Angeles | 827.2 | 46.7 |
| Canyon Trek | San Francisco | Houston | 404.6 | 87.6 |
| Forest Journey | Los Angeles | Denver | 2279.9 | 39.9 |
<end>Transform this Csv structure to a plain text format:
Title,Author,Publication Year,Rating
Legends of the Rift,Luna Silverleaf,1999,4.6
The Crystal Key,Thorne Ironwood,1966,1.9
Tales of the Brave,Kara Firebrand,1957,2.5
The Forgotten World,Draven Blackthorn,2012,2.8
The Last Sky,Draven Blackthorn,1951,4.5
Shadows of Solitude,Draven Blackthorn,2011,2.4
Legends of the Rift,Kara Firebrand,1954,3.1
Tales of the Brave,Sylvia Nightshade,1979,3.9
Whispers of the Abyss,Luna Silverleaf,2023,4.4
<start>
Title: Legends of the Rift | Author: Luna Silverleaf | Publication Year: 1999 | Rating: 4.6
Title: The Crystal Key | Author: Thorne Ironwood | Publication Year: 1966 | Rating: 1.9
Title: Tales of the Brave | Author: Kara Firebrand | Publication Year: 1957 | Rating: 2.5
Title: The Forgotten World | Author: Draven Blackthorn | Publication Year: 2012 | Rating: 2.8
Title: The Last Sky | Author: Draven Blackthorn | Publication Year: 1951 | Rating: 4.5
Title: Shadows of Solitude | Author: Draven Blackthorn | Publication Year: 2011 | Rating: 2.4
Title: Legends of the Rift | Author: Kara Firebrand | Publication Year: 1954 | Rating: 3.1
Title: Tales of the Brave | Author: Sylvia Nightshade | Publication Year: 1979 | Rating: 3.9
Title: Whispers of the Abyss | Author: Luna Silverleaf | Publication Year: 2023 | Rating: 4.4
<end>Please transform the following CSV data into Markdown:
Name,Income
Terrence,395000
Amber,225000
Loretta,80000
Marion,150000
Julia,420000
Dustin,185000
Caitlin,310000
Ruben,50000
Ramona,150000
Frieda,205000
<start>
| Name | Income |
| --- | --- |
| Terrence | 395000 |
| Amber | 225000 |
| Loretta | 80000 |
| Marion | 150000 |
| Julia | 420000 |
| Dustin | 185000 |
| Caitlin | 310000 |
| Ruben | 50000 |
| Ramona | 150000 |
| Frieda | 205000 |
<end>