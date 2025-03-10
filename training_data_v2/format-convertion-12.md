Here's some csv data, can you convert it to yml?
Company,Annual Revenue (B),Quarter
BioPharm,449.71,Q3
RetailHub,297.21,Q1
FinanceWorks,306.35,Q2
HealthPlus,291.65,Q1
FinanceWorks,51.42,Q4
AutoDrive,151.21,Q2
<start>
- Annual Revenue (B): 449.71
  Company: BioPharm
  Quarter: Q3
- Annual Revenue (B): 297.21
  Company: RetailHub
  Quarter: Q1
- Annual Revenue (B): 306.35
  Company: FinanceWorks
  Quarter: Q2
- Annual Revenue (B): 291.65
  Company: HealthPlus
  Quarter: Q1
- Annual Revenue (B): 51.42
  Company: FinanceWorks
  Quarter: Q4
- Annual Revenue (B): 151.21
  Company: AutoDrive
  Quarter: Q2
<end>Convert this markdown to CSV:
| Cache Hit Ratio (%) | Connection Count | Timestamp |
| --- | --- | --- |
| 77.83 | 359 | 2021-02-09 11:05:25 |
| 79.92 | 378 | 2022-03-14 17:14:16 |
| 89.48 | 85 | 2022-04-19 17:56:58 |
| 80.47 | 228 | 2021-12-23 18:38:12 |
| 91.03 | 127 | 2021-08-19 00:04:50 |
| 93.84 | 56 | 2023-11-02 17:09:00 |
| 76.01 | 352 | 2023-06-10 01:06:36 |<start>
Cache Hit Ratio (%),Connection Count,Timestamp
77.83,359,2021-02-09 11:05:25
79.92,378,2022-03-14 17:14:16
89.48,85,2022-04-19 17:56:58
80.47,228,2021-12-23 18:38:12
91.03,127,2021-08-19 00:04:50
93.84,56,2023-11-02 17:09:00
76.01,352,2023-06-10 01:06:36
<end>Transform this csv structure to a MARKDOWN format:
Device Type,Battery Level (%),Reading Value
Humidity Sensor,31.7,67.23
Temperature Sensor,91.8,54.97
Humidity Sensor,34.9,69.22
Pressure Sensor,91.8,69.18
Temperature Sensor,80.5,-37.03
Light Sensor,80.9,36.51
Humidity Sensor,71.4,54.21
Humidity Sensor,78.8,26.36
Temperature Sensor,42.7,26.36
<start>
| Device Type | Battery Level (%) | Reading Value |
| --- | --- | --- |
| Humidity Sensor | 31.7 | 67.23 |
| Temperature Sensor | 91.8 | 54.97 |
| Humidity Sensor | 34.9 | 69.22 |
| Pressure Sensor | 91.8 | 69.18 |
| Temperature Sensor | 80.5 | -37.03 |
| Light Sensor | 80.9 | 36.51 |
| Humidity Sensor | 71.4 | 54.21 |
| Humidity Sensor | 78.8 | 26.36 |
| Temperature Sensor | 42.7 | 26.36 |
<end>Here's some plain text data, can you convert it to Json?
Name: Janis | Age: 24 | City: Los Angeles | Income: 405000
Name: Terrance | Age: 42 | City: Las Vegas | Income: 165000
Name: Roy | Age: 42 | City: Nashville | Income: 85000
Name: Steve | Age: 18 | City: Memphis | Income: 270000
Name: Casey | Age: 51 | City: Portland | Income: 195000
Name: Sonya | Age: 21 | City: Las Vegas | Income: 380000
Name: Genesis | Age: 33 | City: El Paso | Income: 390000
Name: Brenda | Age: 68 | City: Louisville | Income: 25000
Name: Dennis | Age: 58 | City: New York | Income: 75000
Name: Sherman | Age: 64 | City: San Antonio | Income: 270000
<start>
[
    {
        "Name": "Janis",
        "Age": 24,
        "City": "Los Angeles",
        "Income": 405000
    },
    {
        "Name": "Terrance",
        "Age": 42,
        "City": "Las Vegas",
        "Income": 165000
    },
    {
        "Name": "Roy",
        "Age": 42,
        "City": "Nashville",
        "Income": 85000
    },
    {
        "Name": "Steve",
        "Age": 18,
        "City": "Memphis",
        "Income": 270000
    },
    {
        "Name": "Casey",
        "Age": 51,
        "City": "Portland",
        "Income": 195000
    },
    {
        "Name": "Sonya",
        "Age": 21,
        "City": "Las Vegas",
        "Income": 380000
    },
    {
        "Name": "Genesis",
        "Age": 33,
        "City": "El Paso",
        "Income": 390000
    },
    {
        "Name": "Brenda",
        "Age": 68,
        "City": "Louisville",
        "Income": 25000
    },
    {
        "Name": "Dennis",
        "Age": 58,
        "City": "New York",
        "Income": 75000
    },
    {
        "Name": "Sherman",
        "Age": 64,
        "City": "San Antonio",
        "Income": 270000
    }
]
<end>Can you change this Markdown into csv?
| Company | Open Price | Close Price | High Price | Low Price | Volume |
| --- | --- | --- | --- | --- | --- |
| AutoMotive | 1090.52 | 1355.74 | 1355.74 | 1090.52 | 2319814 |
| HealthGen | 1101.7 | 1144.01 | 1144.01 | 1101.7 | 9381903 |
| MediaGroup | 1243.2 | 562.03 | 1243.2 | 229.12 | 1922483 |
| RetailWorld | 525.5 | 327.13 | 1102.23 | 292.69 | 3903670 |
| AutoMotive | 907.2 | 210.89 | 907.2 | 210.89 | 5711590 |
| GreenEnergy | 1467.3 | 1154.03 | 1467.3 | 1154.03 | 5518014 |
| AeroSystems | 862.63 | 570.68 | 862.63 | 570.68 | 5518590 |
| AeroSystems | 1459.49 | 1480.72 | 1480.72 | 123.08 | 1005388 |
| MediaGroup | 1090.52 | 1295.12 | 1295.12 | 123.08 | 1669937 |
| AeroSystems | 42.81 | 1282.48 | 1442.73 | 42.81 | 7449196 |<start>
Company,Open Price,Close Price,High Price,Low Price,Volume
AutoMotive,1090.52,1355.74,1355.74,1090.52,2319814
HealthGen,1101.7,1144.01,1144.01,1101.7,9381903
MediaGroup,1243.2,562.03,1243.2,229.12,1922483
RetailWorld,525.5,327.13,1102.23,292.69,3903670
AutoMotive,907.2,210.89,907.2,210.89,5711590
GreenEnergy,1467.3,1154.03,1467.3,1154.03,5518014
AeroSystems,862.63,570.68,862.63,570.68,5518590
AeroSystems,1459.49,1480.72,1480.72,123.08,1005388
MediaGroup,1090.52,1295.12,1295.12,123.08,1669937
AeroSystems,42.81,1282.48,1442.73,42.81,7449196
<end>Convert this Markdown to Json:
| Device Type | Location | Reading Value | Timestamp |
| --- | --- | --- | --- |
| Motion Detector | Office | -26.36 | 2023-11-06 02:43:31 |
| Pressure Sensor | Bathroom | 30.92 | 2021-05-28 18:29:27 |
| Humidity Sensor | Garden | 14.19 | 2023-09-26 09:32:00 |<start>
[
    {
        "Device Type": "Motion Detector",
        "Location": "Office",
        "Reading Value": -26.36,
        "Timestamp": "2023-11-06 02:43:31"
    },
    {
        "Device Type": "Pressure Sensor",
        "Location": "Bathroom",
        "Reading Value": 30.92,
        "Timestamp": "2021-05-28 18:29:27"
    },
    {
        "Device Type": "Humidity Sensor",
        "Location": "Garden",
        "Reading Value": 14.19,
        "Timestamp": "2023-09-26 09:32:00"
    }
]
<end>Can you change this markdown into csv?
| Trip Name | Start Location | End Location | Distance (miles) | Duration (hours) | Fuel Used (gallons) |
| --- | --- | --- | --- | --- | --- |
| Historic Route | Houston | New York | 1065.2 | 8.1 | 13.4 |
| Lakeside Retreat | Los Angeles | Miami | 2614.5 | 10.9 | 7.7 |
| Coast to Coast | Phoenix | San Francisco | 1080.1 | 52.9 | 81.1 |
| City Explorer | Houston | San Francisco | 1479.8 | 11.0 | 30.4 |
| Mountain Adventure | San Francisco | Phoenix | 2493.4 | 49.1 | 99.1 |
| Forest Journey | Miami | Phoenix | 1205.4 | 46.2 | 66.2 |<start>
Trip Name,Start Location,End Location,Distance (miles),Duration (hours),Fuel Used (gallons)
Historic Route,Houston,New York,1065.2,8.1,13.4
Lakeside Retreat,Los Angeles,Miami,2614.5,10.9,7.7
Coast to Coast,Phoenix,San Francisco,1080.1,52.9,81.1
City Explorer,Houston,San Francisco,1479.8,11.0,30.4
Mountain Adventure,San Francisco,Phoenix,2493.4,49.1,99.1
Forest Journey,Miami,Phoenix,1205.4,46.2,66.2
<end>Transform this Json structure to a Plain text format:
[
    {
        "Market Cap": "Small Cap",
        "Stock Price": 654.44,
        "Annual Revenue (B)": 242.7,
        "Quarter": "Q2"
    },
    {
        "Market Cap": "Mega Cap",
        "Stock Price": 672.54,
        "Annual Revenue (B)": 53.04,
        "Quarter": "Q4"
    },
    {
        "Market Cap": "Mid Cap",
        "Stock Price": 905.03,
        "Annual Revenue (B)": 272.53,
        "Quarter": "Q2"
    },
    {
        "Market Cap": "Mid Cap",
        "Stock Price": 850.71,
        "Annual Revenue (B)": 169.9,
        "Quarter": "Q4"
    },
    {
        "Market Cap": "Small Cap",
        "Stock Price": 126.01,
        "Annual Revenue (B)": 447.15,
        "Quarter": "Q3"
    }
]<start>
Market Cap: Small Cap | Stock Price: 654.44 | Annual Revenue (B): 242.7 | Quarter: Q2
Market Cap: Mega Cap | Stock Price: 672.54 | Annual Revenue (B): 53.04 | Quarter: Q4
Market Cap: Mid Cap | Stock Price: 905.03 | Annual Revenue (B): 272.53 | Quarter: Q2
Market Cap: Mid Cap | Stock Price: 850.71 | Annual Revenue (B): 169.9 | Quarter: Q4
Market Cap: Small Cap | Stock Price: 126.01 | Annual Revenue (B): 447.15 | Quarter: Q3
<end>Please transform the following Csv data into Markdown:
Name,Age,Birth Month,City,Income
Landon,28,March,Charlotte,370000
Liam,28,September,Fort Worth,455000
Dennis,44,July,Oklahoma City,235000
<start>
| Name | Age | Birth Month | City | Income |
| --- | --- | --- | --- | --- |
| Landon | 28 | March | Charlotte | 370000 |
| Liam | 28 | September | Fort Worth | 455000 |
| Dennis | 44 | July | Oklahoma City | 235000 |
<end>Can you change this plain text into MARKDOWN?
Device ID: device-0042 | Device Type: Humidity Sensor | Location: Living Room | Battery Level (%): 93.5 | Timestamp: 2021-06-17 23:06:00
Device ID: device-0100 | Device Type: Temperature Sensor | Location: Garage | Battery Level (%): 32.0 | Timestamp: 2021-02-11 17:20:12
Device ID: device-0075 | Device Type: Humidity Sensor | Location: Kitchen | Battery Level (%): 57.0 | Timestamp: 2023-07-27 23:08:01
Device ID: device-0049 | Device Type: Light Sensor | Location: Living Room | Battery Level (%): 18.8 | Timestamp: 2021-04-24 02:27:27
Device ID: device-0089 | Device Type: Temperature Sensor | Location: Garage | Battery Level (%): 61.8 | Timestamp: 2021-03-24 09:33:01
Device ID: device-0038 | Device Type: Motion Detector | Location: Garden | Battery Level (%): 63.4 | Timestamp: 2023-04-23 22:55:58
Device ID: device-0082 | Device Type: Light Sensor | Location: Living Room | Battery Level (%): 49.5 | Timestamp: 2021-12-07 19:20:59
Device ID: device-0066 | Device Type: Motion Detector | Location: Bedroom | Battery Level (%): 14.2 | Timestamp: 2021-11-08 14:02:26
<start>
| Device ID | Device Type | Location | Battery Level (%) | Timestamp |
| --- | --- | --- | --- | --- |
| device-0042 | Humidity Sensor | Living Room | 93.5 | 2021-06-17 23:06:00 |
| device-0100 | Temperature Sensor | Garage | 32.0 | 2021-02-11 17:20:12 |
| device-0075 | Humidity Sensor | Kitchen | 57.0 | 2023-07-27 23:08:01 |
| device-0049 | Light Sensor | Living Room | 18.8 | 2021-04-24 02:27:27 |
| device-0089 | Temperature Sensor | Garage | 61.8 | 2021-03-24 09:33:01 |
| device-0038 | Motion Detector | Garden | 63.4 | 2023-04-23 22:55:58 |
| device-0082 | Light Sensor | Living Room | 49.5 | 2021-12-07 19:20:59 |
| device-0066 | Motion Detector | Bedroom | 14.2 | 2021-11-08 14:02:26 |
<end>Please transform the following MARKDOWN data into Json:
| Company | Date | Low Price | Volume |
| --- | --- | --- | --- |
| AutoMotive | 2013-12-03 | 373.33 | 2270911 |
| RetailWorld | 2022-09-24 | 294.83 | 6660517 |
| MediaGroup | 2021-07-06 | 373.33 | 8854580 |<start>
[
    {
        "Company": "AutoMotive",
        "Date": "2013-12-03",
        "Low Price": 373.33,
        "Volume": 2270911
    },
    {
        "Company": "RetailWorld",
        "Date": "2022-09-24",
        "Low Price": 294.83,
        "Volume": 6660517
    },
    {
        "Company": "MediaGroup",
        "Date": "2021-07-06",
        "Low Price": 373.33,
        "Volume": 8854580
    }
]
<end>Can you change this YAML into PLAIN TEXT?
- Age: 26
  Birth Month: November
  City: Seattle
  Income: 195000
- Age: 36
  Birth Month: July
  City: Fort Worth
  Income: 70000
- Age: 67
  Birth Month: February
  City: San Antonio
  Income: 370000
- Age: 48
  Birth Month: September
  City: New York
  Income: 405000
- Age: 56
  Birth Month: June
  City: San Francisco
  Income: 495000
- Age: 43
  Birth Month: March
  City: Charlotte
  Income: 90000
<start>
Age: 26 | Birth Month: November | City: Seattle | Income: 195000
Age: 36 | Birth Month: July | City: Fort Worth | Income: 70000
Age: 67 | Birth Month: February | City: San Antonio | Income: 370000
Age: 48 | Birth Month: September | City: New York | Income: 405000
Age: 56 | Birth Month: June | City: San Francisco | Income: 495000
Age: 43 | Birth Month: March | City: Charlotte | Income: 90000
<end>Convert this csv to yaml:
Start Location,Distance (miles),Fuel Used (gallons)
Houston,806.6,48.9
San Francisco,916.0,64.2
Los Angeles,2036.9,43.7
Denver,1887.2,59.6
Phoenix,187.0,19.2
Houston,202.4,26.7
Miami,2760.8,49.2
New York,202.4,5.8
San Francisco,1003.8,64.2
New York,2036.9,59.6
<start>
- Distance (miles): 806.6
  Fuel Used (gallons): 48.9
  Start Location: Houston
- Distance (miles): 916.0
  Fuel Used (gallons): 64.2
  Start Location: San Francisco
- Distance (miles): 2036.9
  Fuel Used (gallons): 43.7
  Start Location: Los Angeles
- Distance (miles): 1887.2
  Fuel Used (gallons): 59.6
  Start Location: Denver
- Distance (miles): 187.0
  Fuel Used (gallons): 19.2
  Start Location: Phoenix
- Distance (miles): 202.4
  Fuel Used (gallons): 26.7
  Start Location: Houston
- Distance (miles): 2760.8
  Fuel Used (gallons): 49.2
  Start Location: Miami
- Distance (miles): 202.4
  Fuel Used (gallons): 5.8
  Start Location: New York
- Distance (miles): 1003.8
  Fuel Used (gallons): 64.2
  Start Location: San Francisco
- Distance (miles): 2036.9
  Fuel Used (gallons): 59.6
  Start Location: New York
<end>Transform this csv structure to a Markdown format:
Company,Close Price,Low Price,Volume
BioLife,1467.08,857.88,166618
GreenEnergy,461.28,461.28,7596679
FoodChain,1439.86,232.52,9074640
AutoMotive,461.28,450.89,442946
HealthGen,1083.15,417.9,5566681
TechnoCorp,1291.41,810.89,8208217
HealthGen,1216.81,586.43,8080236
RetailWorld,883.48,452.01,9203389
<start>
| Company | Close Price | Low Price | Volume |
| --- | --- | --- | --- |
| BioLife | 1467.08 | 857.88 | 166618 |
| GreenEnergy | 461.28 | 461.28 | 7596679 |
| FoodChain | 1439.86 | 232.52 | 9074640 |
| AutoMotive | 461.28 | 450.89 | 442946 |
| HealthGen | 1083.15 | 417.9 | 5566681 |
| TechnoCorp | 1291.41 | 810.89 | 8208217 |
| HealthGen | 1216.81 | 586.43 | 8080236 |
| RetailWorld | 883.48 | 452.01 | 9203389 |
<end>Here's some Plain text data, can you convert it to yaml?
Company: FinanceTrust | Date: 2016-04-19 | Open Price: 56.83 | Close Price: 169.66 | High Price: 1205.62 | Volume: 4035983
Company: MediaGroup | Date: 2014-10-07 | Open Price: 56.83 | Close Price: 283.61 | High Price: 283.61 | Volume: 8525527
Company: MediaGroup | Date: 2012-12-21 | Open Price: 1369.35 | Close Price: 1057.97 | High Price: 1369.35 | Volume: 324165
<start>
- Close Price: 169.66
  Company: FinanceTrust
  Date: '2016-04-19'
  High Price: 1205.62
  Open Price: 56.83
  Volume: 4035983
- Close Price: 283.61
  Company: MediaGroup
  Date: '2014-10-07'
  High Price: 283.61
  Open Price: 56.83
  Volume: 8525527
- Close Price: 1057.97
  Company: MediaGroup
  Date: '2012-12-21'
  High Price: 1369.35
  Open Price: 1369.35
  Volume: 324165
<end>Convert this plain text to markdown:
Title: The Endless Horizon | Director: Cade Firebrand
Title: Beyond the Veil | Director: Aria Ravenwood
Title: Mystery of the Depths | Director: Selene Darkwhisper
Title: Dreamwalker | Director: Cade Firebrand
Title: Mystery of the Depths | Director: Drake Nightshade
Title: The Final Voyage | Director: Rylan Frostblade
Title: Escape from Earth | Director: Selene Darkwhisper
<start>
| Title | Director |
| --- | --- |
| The Endless Horizon | Cade Firebrand |
| Beyond the Veil | Aria Ravenwood |
| Mystery of the Depths | Selene Darkwhisper |
| Dreamwalker | Cade Firebrand |
| Mystery of the Depths | Drake Nightshade |
| The Final Voyage | Rylan Frostblade |
| Escape from Earth | Selene Darkwhisper |
<end>Please transform the following yml data into csv:
- Close Price: 82.88
  Company: HealthGen
  Date: '2018-03-23'
  High Price: 895.34
  Low Price: 82.88
  Open Price: 895.34
  Volume: 6368690
- Close Price: 1366.94
  Company: TechnoCorp
  Date: '2022-10-10'
  High Price: 1366.94
  Low Price: 517.11
  Open Price: 517.11
  Volume: 684686
- Close Price: 588.62
  Company: TechnoCorp
  Date: '2016-04-07'
  High Price: 1410.09
  Low Price: 588.62
  Open Price: 900.77
  Volume: 7915660
- Close Price: 1359.34
  Company: AutoMotive
  Date: '2015-03-11'
  High Price: 1475.04
  Low Price: 239.34
  Open Price: 1475.04
  Volume: 2031986
- Close Price: 437.49
  Company: BioLife
  Date: '2015-05-12'
  High Price: 1434.24
  Low Price: 437.49
  Open Price: 1434.24
  Volume: 3118957
- Close Price: 1263.71
  Company: GreenEnergy
  Date: '2017-06-08'
  High Price: 1263.71
  Low Price: 267.31
  Open Price: 267.31
  Volume: 9226811
- Close Price: 599.49
  Company: AutoMotive
  Date: '2013-05-27'
  High Price: 1075.04
  Low Price: 217.22
  Open Price: 1075.04
  Volume: 2832765
- Close Price: 603.07
  Company: AeroSystems
  Date: '2021-12-25'
  High Price: 603.07
  Low Price: 113.91
  Open Price: 113.91
  Volume: 3153284
- Close Price: 519.35
  Company: FoodChain
  Date: '2022-07-03'
  High Price: 1359.34
  Low Price: 519.35
  Open Price: 1359.34
  Volume: 9388229
<start>
Company,Date,Open Price,Close Price,High Price,Low Price,Volume
HealthGen,2018-03-23,895.34,82.88,895.34,82.88,6368690
TechnoCorp,2022-10-10,517.11,1366.94,1366.94,517.11,684686
TechnoCorp,2016-04-07,900.77,588.62,1410.09,588.62,7915660
AutoMotive,2015-03-11,1475.04,1359.34,1475.04,239.34,2031986
BioLife,2015-05-12,1434.24,437.49,1434.24,437.49,3118957
GreenEnergy,2017-06-08,267.31,1263.71,1263.71,267.31,9226811
AutoMotive,2013-05-27,1075.04,599.49,1075.04,217.22,2832765
AeroSystems,2021-12-25,113.91,603.07,603.07,113.91,3153284
FoodChain,2022-07-03,1359.34,519.35,1359.34,519.35,9388229
<end>Can you change this JSON into Plain text?
[
    {
        "Distance (miles)": 295.2,
        "Duration (hours)": 15.2,
        "Fuel Used (gallons)": 55.1
    },
    {
        "Distance (miles)": 2960.9,
        "Duration (hours)": 33.3,
        "Fuel Used (gallons)": 13.9
    },
    {
        "Distance (miles)": 1860.3,
        "Duration (hours)": 9.7,
        "Fuel Used (gallons)": 92.0
    },
    {
        "Distance (miles)": 2538.4,
        "Duration (hours)": 6.7,
        "Fuel Used (gallons)": 87.7
    },
    {
        "Distance (miles)": 1165.0,
        "Duration (hours)": 49.0,
        "Fuel Used (gallons)": 28.3
    },
    {
        "Distance (miles)": 424.6,
        "Duration (hours)": 15.0,
        "Fuel Used (gallons)": 24.8
    },
    {
        "Distance (miles)": 1879.2,
        "Duration (hours)": 44.2,
        "Fuel Used (gallons)": 17.6
    }
]<start>
Distance (miles): 295.2 | Duration (hours): 15.2 | Fuel Used (gallons): 55.1
Distance (miles): 2960.9 | Duration (hours): 33.3 | Fuel Used (gallons): 13.9
Distance (miles): 1860.3 | Duration (hours): 9.7 | Fuel Used (gallons): 92.0
Distance (miles): 2538.4 | Duration (hours): 6.7 | Fuel Used (gallons): 87.7
Distance (miles): 1165.0 | Duration (hours): 49.0 | Fuel Used (gallons): 28.3
Distance (miles): 424.6 | Duration (hours): 15.0 | Fuel Used (gallons): 24.8
Distance (miles): 1879.2 | Duration (hours): 44.2 | Fuel Used (gallons): 17.6
<end>Please transform the following PLAIN TEXT data into yaml:
Company: HealthGen | Open Price: 1055.46 | Close Price: 1130.6 | High Price: 1130.6 | Low Price: 536.03 | Volume: 7152554
Company: FinanceTrust | Open Price: 275.18 | Close Price: 587.47 | High Price: 1359.17 | Low Price: 275.18 | Volume: 5548432
Company: RetailWorld | Open Price: 1216.34 | Close Price: 193.23 | High Price: 1216.34 | Low Price: 193.23 | Volume: 8732750
Company: TechnoCorp | Open Price: 1273.46 | Close Price: 570.47 | High Price: 1273.46 | Low Price: 570.47 | Volume: 7785955
Company: RetailWorld | Open Price: 1321.84 | Close Price: 806.7 | High Price: 1321.84 | Low Price: 806.7 | Volume: 6331314
Company: AeroSystems | Open Price: 280.51 | Close Price: 697.71 | High Price: 697.71 | Low Price: 280.51 | Volume: 8130242
Company: RetailWorld | Open Price: 800.95 | Close Price: 463.34 | High Price: 800.95 | Low Price: 463.34 | Volume: 6256829
Company: HealthGen | Open Price: 858.69 | Close Price: 73.26 | High Price: 1201.76 | Low Price: 73.26 | Volume: 2324873
Company: BioLife | Open Price: 1216.34 | Close Price: 805.11 | High Price: 1216.34 | Low Price: 805.11 | Volume: 6256829
Company: RetailWorld | Open Price: 518.16 | Close Price: 839.79 | High Price: 839.79 | Low Price: 518.16 | Volume: 5511932
<start>
- Close Price: 1130.6
  Company: HealthGen
  High Price: 1130.6
  Low Price: 536.03
  Open Price: 1055.46
  Volume: 7152554
- Close Price: 587.47
  Company: FinanceTrust
  High Price: 1359.17
  Low Price: 275.18
  Open Price: 275.18
  Volume: 5548432
- Close Price: 193.23
  Company: RetailWorld
  High Price: 1216.34
  Low Price: 193.23
  Open Price: 1216.34
  Volume: 8732750
- Close Price: 570.47
  Company: TechnoCorp
  High Price: 1273.46
  Low Price: 570.47
  Open Price: 1273.46
  Volume: 7785955
- Close Price: 806.7
  Company: RetailWorld
  High Price: 1321.84
  Low Price: 806.7
  Open Price: 1321.84
  Volume: 6331314
- Close Price: 697.71
  Company: AeroSystems
  High Price: 697.71
  Low Price: 280.51
  Open Price: 280.51
  Volume: 8130242
- Close Price: 463.34
  Company: RetailWorld
  High Price: 800.95
  Low Price: 463.34
  Open Price: 800.95
  Volume: 6256829
- Close Price: 73.26
  Company: HealthGen
  High Price: 1201.76
  Low Price: 73.26
  Open Price: 858.69
  Volume: 2324873
- Close Price: 805.11
  Company: BioLife
  High Price: 1216.34
  Low Price: 805.11
  Open Price: 1216.34
  Volume: 6256829
- Close Price: 839.79
  Company: RetailWorld
  High Price: 839.79
  Low Price: 518.16
  Open Price: 518.16
  Volume: 5511932
<end>Can you change this Markdown into Csv?
| Product Name | SKU | Price | Stock Quantity | Category | Supplier Name |
| --- | --- | --- | --- | --- | --- |
| Gadget | SKU-1070 | 300.25 | 53 | Sports | Globex |
| Whatchamacallit | SKU-1054 | 28.95 | 31 | Toys | Wayne Enterprises |
| Device | SKU-1096 | 401.64 | 235 | Automotive | Umbrella Corp |
| Instrument | SKU-1001 | 40.11 | 308 | Sports | Wonka Industries |
| Contraption | SKU-1031 | 256.86 | 363 | Toys | Wayne Enterprises |
| Thingamajig | SKU-1009 | 288.39 | 166 | Household | Globex |
| Apparatus | SKU-1014 | 237.01 | 15 | Automotive | Globex |
| Apparatus | SKU-1046 | 95.3 | 167 | Household | ACME Corp |
| Apparatus | SKU-1005 | 119.37 | 406 | Automotive | Globex |
| Contraption | SKU-1078 | 373.76 | 247 | Household | Umbrella Corp |<start>
Product Name,SKU,Price,Stock Quantity,Category,Supplier Name
Gadget,SKU-1070,300.25,53,Sports,Globex
Whatchamacallit,SKU-1054,28.95,31,Toys,Wayne Enterprises
Device,SKU-1096,401.64,235,Automotive,Umbrella Corp
Instrument,SKU-1001,40.11,308,Sports,Wonka Industries
Contraption,SKU-1031,256.86,363,Toys,Wayne Enterprises
Thingamajig,SKU-1009,288.39,166,Household,Globex
Apparatus,SKU-1014,237.01,15,Automotive,Globex
Apparatus,SKU-1046,95.3,167,Household,ACME Corp
Apparatus,SKU-1005,119.37,406,Automotive,Globex
Contraption,SKU-1078,373.76,247,Household,Umbrella Corp
<end>Please transform the following PLAIN TEXT data into yaml:
Product Name: Device | SKU: SKU-1017 | Price: 125.06 | Stock Quantity: 119 | Category: Sports | Supplier Name: Umbrella Corp
Product Name: Apparatus | SKU: SKU-1042 | Price: 224.89 | Stock Quantity: 186 | Category: Toys | Supplier Name: Globex
Product Name: Thingamajig | SKU: SKU-1077 | Price: 126.59 | Stock Quantity: 216 | Category: Electronics | Supplier Name: Wonka Industries
Product Name: Thingamajig | SKU: SKU-1055 | Price: 35.86 | Stock Quantity: 300 | Category: Toys | Supplier Name: Globex
Product Name: Instrument | SKU: SKU-1088 | Price: 68.26 | Stock Quantity: 245 | Category: Electronics | Supplier Name: Globex
Product Name: Instrument | SKU: SKU-1041 | Price: 315.29 | Stock Quantity: 120 | Category: Automotive | Supplier Name: Wayne Enterprises
Product Name: Contraption | SKU: SKU-1072 | Price: 127.68 | Stock Quantity: 301 | Category: Automotive | Supplier Name: Wayne Enterprises
Product Name: Gizmo | SKU: SKU-1024 | Price: 266.82 | Stock Quantity: 89 | Category: Automotive | Supplier Name: Wayne Enterprises
<start>
- Category: Sports
  Price: 125.06
  Product Name: Device
  SKU: SKU-1017
  Stock Quantity: 119
  Supplier Name: Umbrella Corp
- Category: Toys
  Price: 224.89
  Product Name: Apparatus
  SKU: SKU-1042
  Stock Quantity: 186
  Supplier Name: Globex
- Category: Electronics
  Price: 126.59
  Product Name: Thingamajig
  SKU: SKU-1077
  Stock Quantity: 216
  Supplier Name: Wonka Industries
- Category: Toys
  Price: 35.86
  Product Name: Thingamajig
  SKU: SKU-1055
  Stock Quantity: 300
  Supplier Name: Globex
- Category: Electronics
  Price: 68.26
  Product Name: Instrument
  SKU: SKU-1088
  Stock Quantity: 245
  Supplier Name: Globex
- Category: Automotive
  Price: 315.29
  Product Name: Instrument
  SKU: SKU-1041
  Stock Quantity: 120
  Supplier Name: Wayne Enterprises
- Category: Automotive
  Price: 127.68
  Product Name: Contraption
  SKU: SKU-1072
  Stock Quantity: 301
  Supplier Name: Wayne Enterprises
- Category: Automotive
  Price: 266.82
  Product Name: Gizmo
  SKU: SKU-1024
  Stock Quantity: 89
  Supplier Name: Wayne Enterprises
<end>Convert this markdown to plain text:
| Trip Name | Start Location | End Location | Distance (miles) | Duration (hours) |
| --- | --- | --- | --- | --- |
| Historic Route | Houston | Phoenix | 2488.2 | 64.1 |
| Desert Drive | Chicago | San Francisco | 1314.8 | 64.2 |
| Desert Drive | Houston | San Francisco | 2572.6 | 45.7 |<start>
Trip Name: Historic Route | Start Location: Houston | End Location: Phoenix | Distance (miles): 2488.2 | Duration (hours): 64.1
Trip Name: Desert Drive | Start Location: Chicago | End Location: San Francisco | Distance (miles): 1314.8 | Duration (hours): 64.2
Trip Name: Desert Drive | Start Location: Houston | End Location: San Francisco | Distance (miles): 2572.6 | Duration (hours): 45.7
<end>Here's some Yml data, can you convert it to csv?
- Box Office Earnings (M): 650.54
  Director: Talon Blackthorn
  Release Year: 1979
- Box Office Earnings (M): 469.68
  Director: Cade Firebrand
  Release Year: 2006
- Box Office Earnings (M): 569.03
  Director: Selene Darkwhisper
  Release Year: 1981
<start>
Director,Release Year,Box Office Earnings (M)
Talon Blackthorn,1979,650.54
Cade Firebrand,2006,469.68
Selene Darkwhisper,1981,569.03
<end>Here's some markdown data, can you convert it to YML?
| Title | Author | Publication Year | Rating |
| --- | --- | --- | --- |
| A Journey Through Time | Galen Starfire | 1961 | 1.4 |
| A Journey Through Time | Galen Starfire | 1957 | 3.6 |
| The Crystal Key | Kara Firebrand | 2023 | 1.4 |<start>
- Author: Galen Starfire
  Publication Year: 1961
  Rating: 1.4
  Title: A Journey Through Time
- Author: Galen Starfire
  Publication Year: 1957
  Rating: 3.6
  Title: A Journey Through Time
- Author: Kara Firebrand
  Publication Year: 2023
  Rating: 1.4
  Title: The Crystal Key
<end>Please transform the following Csv data into plain text:
Product Name,Price,Stock Quantity,Category
Whatchamacallit,418.69,145,Automotive
Contraption,379.85,214,Automotive
Contraption,84.69,267,Automotive
Whatchamacallit,88.09,30,Electronics
Gadget,385.18,327,Sports
Doohickey,191.99,407,Electronics
Device,261.37,162,Automotive
Widget,88.31,300,Electronics
Widget,427.26,48,Electronics
<start>
Product Name: Whatchamacallit | Price: 418.69 | Stock Quantity: 145 | Category: Automotive
Product Name: Contraption | Price: 379.85 | Stock Quantity: 214 | Category: Automotive
Product Name: Contraption | Price: 84.69 | Stock Quantity: 267 | Category: Automotive
Product Name: Whatchamacallit | Price: 88.09 | Stock Quantity: 30 | Category: Electronics
Product Name: Gadget | Price: 385.18 | Stock Quantity: 327 | Category: Sports
Product Name: Doohickey | Price: 191.99 | Stock Quantity: 407 | Category: Electronics
Product Name: Device | Price: 261.37 | Stock Quantity: 162 | Category: Automotive
Product Name: Widget | Price: 88.31 | Stock Quantity: 300 | Category: Electronics
Product Name: Widget | Price: 427.26 | Stock Quantity: 48 | Category: Electronics
<end>Can you change this Json into markdown?
[
    {
        "Stock Quantity": 201,
        "Category": "Electronics",
        "Supplier Name": "Wayne Enterprises"
    },
    {
        "Stock Quantity": 228,
        "Category": "Automotive",
        "Supplier Name": "Globex"
    },
    {
        "Stock Quantity": 338,
        "Category": "Sports",
        "Supplier Name": "Umbrella Corp"
    },
    {
        "Stock Quantity": 220,
        "Category": "Electronics",
        "Supplier Name": "Wayne Enterprises"
    }
]<start>
| Stock Quantity | Category | Supplier Name |
| --- | --- | --- |
| 201 | Electronics | Wayne Enterprises |
| 228 | Automotive | Globex |
| 338 | Sports | Umbrella Corp |
| 220 | Electronics | Wayne Enterprises |
<end>Convert this plain text to markdown:
Trip Name: Historic Route | End Location: Houston | Distance (miles): 825.2 | Fuel Used (gallons): 67.8
Trip Name: Valley Voyage | End Location: Miami | Distance (miles): 149.2 | Fuel Used (gallons): 35.1
Trip Name: Lakeside Retreat | End Location: New York | Distance (miles): 931.4 | Fuel Used (gallons): 12.3
Trip Name: Coast to Coast | End Location: Phoenix | Distance (miles): 1239.1 | Fuel Used (gallons): 58.6
Trip Name: Desert Drive | End Location: San Francisco | Distance (miles): 1049.3 | Fuel Used (gallons): 39.6
Trip Name: Forest Journey | End Location: San Francisco | Distance (miles): 1442.9 | Fuel Used (gallons): 78.0
Trip Name: Lakeside Retreat | End Location: Phoenix | Distance (miles): 2372.0 | Fuel Used (gallons): 66.6
Trip Name: Highway Odyssey | End Location: Denver | Distance (miles): 2220.9 | Fuel Used (gallons): 81.3
Trip Name: Canyon Trek | End Location: Phoenix | Distance (miles): 1843.2 | Fuel Used (gallons): 85.9
Trip Name: Mountain Adventure | End Location: San Francisco | Distance (miles): 2253.5 | Fuel Used (gallons): 19.5
<start>
| Trip Name | End Location | Distance (miles) | Fuel Used (gallons) |
| --- | --- | --- | --- |
| Historic Route | Houston | 825.2 | 67.8 |
| Valley Voyage | Miami | 149.2 | 35.1 |
| Lakeside Retreat | New York | 931.4 | 12.3 |
| Coast to Coast | Phoenix | 1239.1 | 58.6 |
| Desert Drive | San Francisco | 1049.3 | 39.6 |
| Forest Journey | San Francisco | 1442.9 | 78.0 |
| Lakeside Retreat | Phoenix | 2372.0 | 66.6 |
| Highway Odyssey | Denver | 2220.9 | 81.3 |
| Canyon Trek | Phoenix | 1843.2 | 85.9 |
| Mountain Adventure | San Francisco | 2253.5 | 19.5 |
<end>Here's some YAML data, can you convert it to plain text?
- Device ID: device-0042
  Device Type: Pressure Sensor
  Location: Hallway
  Reading Value: 27.7
  Timestamp: '2021-03-19 19:27:40'
- Device ID: device-0075
  Device Type: Light Sensor
  Location: Hallway
  Reading Value: 0.78
  Timestamp: '2023-04-26 20:01:47'
- Device ID: device-0037
  Device Type: Humidity Sensor
  Location: Living Room
  Reading Value: -17.51
  Timestamp: '2023-11-21 12:47:38'
- Device ID: device-0008
  Device Type: Motion Detector
  Location: Living Room
  Reading Value: 11.04
  Timestamp: '2023-01-08 17:17:38'
- Device ID: device-0015
  Device Type: Temperature Sensor
  Location: Hallway
  Reading Value: 30.26
  Timestamp: '2022-10-15 09:15:16'
<start>
Device ID: device-0042 | Device Type: Pressure Sensor | Location: Hallway | Reading Value: 27.7 | Timestamp: 2021-03-19 19:27:40
Device ID: device-0075 | Device Type: Light Sensor | Location: Hallway | Reading Value: 0.78 | Timestamp: 2023-04-26 20:01:47
Device ID: device-0037 | Device Type: Humidity Sensor | Location: Living Room | Reading Value: -17.51 | Timestamp: 2023-11-21 12:47:38
Device ID: device-0008 | Device Type: Motion Detector | Location: Living Room | Reading Value: 11.04 | Timestamp: 2023-01-08 17:17:38
Device ID: device-0015 | Device Type: Temperature Sensor | Location: Hallway | Reading Value: 30.26 | Timestamp: 2022-10-15 09:15:16
<end>Please transform the following JSON data into PLAIN TEXT:
[
    {
        "Device Type": "Temperature Sensor",
        "Location": "Garage",
        "Reading Value": -32.22
    },
    {
        "Device Type": "Humidity Sensor",
        "Location": "Living Room",
        "Reading Value": 81.58
    },
    {
        "Device Type": "Pressure Sensor",
        "Location": "Kitchen",
        "Reading Value": 28.14
    },
    {
        "Device Type": "Humidity Sensor",
        "Location": "Garage",
        "Reading Value": -24.79
    },
    {
        "Device Type": "Light Sensor",
        "Location": "Garage",
        "Reading Value": 64.15
    },
    {
        "Device Type": "Motion Detector",
        "Location": "Bedroom",
        "Reading Value": 13.3
    },
    {
        "Device Type": "Humidity Sensor",
        "Location": "Office",
        "Reading Value": -33.72
    },
    {
        "Device Type": "Temperature Sensor",
        "Location": "Hallway",
        "Reading Value": 1.34
    },
    {
        "Device Type": "Temperature Sensor",
        "Location": "Hallway",
        "Reading Value": 54.63
    },
    {
        "Device Type": "Light Sensor",
        "Location": "Bathroom",
        "Reading Value": -23.59
    }
]<start>
Device Type: Temperature Sensor | Location: Garage | Reading Value: -32.22
Device Type: Humidity Sensor | Location: Living Room | Reading Value: 81.58
Device Type: Pressure Sensor | Location: Kitchen | Reading Value: 28.14
Device Type: Humidity Sensor | Location: Garage | Reading Value: -24.79
Device Type: Light Sensor | Location: Garage | Reading Value: 64.15
Device Type: Motion Detector | Location: Bedroom | Reading Value: 13.3
Device Type: Humidity Sensor | Location: Office | Reading Value: -33.72
Device Type: Temperature Sensor | Location: Hallway | Reading Value: 1.34
Device Type: Temperature Sensor | Location: Hallway | Reading Value: 54.63
Device Type: Light Sensor | Location: Bathroom | Reading Value: -23.59
<end>Can you change this csv into Markdown?
Condition,Temperature (C),Humidity (%),Wind Speed (km/h),Day
Stormy,30.7,93,0.7,Thursday
Snowy,-7.9,94,10.6,Saturday
Foggy,22.9,74,2.4,Thursday
Cloudy,0.4,41,18.7,Friday
Foggy,-5.7,32,9.1,Sunday
Snowy,26.5,87,28.3,Friday
Foggy,8.2,90,18.4,Thursday
Foggy,23.4,87,1.4,Friday
<start>
| Condition | Temperature (C) | Humidity (%) | Wind Speed (km/h) | Day |
| --- | --- | --- | --- | --- |
| Stormy | 30.7 | 93 | 0.7 | Thursday |
| Snowy | -7.9 | 94 | 10.6 | Saturday |
| Foggy | 22.9 | 74 | 2.4 | Thursday |
| Cloudy | 0.4 | 41 | 18.7 | Friday |
| Foggy | -5.7 | 32 | 9.1 | Sunday |
| Snowy | 26.5 | 87 | 28.3 | Friday |
| Foggy | 8.2 | 90 | 18.4 | Thursday |
| Foggy | 23.4 | 87 | 1.4 | Friday |
<end>Transform this plain text structure to a Markdown format:
Device ID: device-0040 | Location: Office | Battery Level (%): 52.3 | Reading Value: 50.53 | Timestamp: 2023-05-01 03:33:03
Device ID: device-0064 | Location: Kitchen | Battery Level (%): 26.7 | Reading Value: -28.22 | Timestamp: 2022-04-24 05:51:18
Device ID: device-0100 | Location: Garage | Battery Level (%): 69.2 | Reading Value: 45.48 | Timestamp: 2023-09-01 03:19:02
Device ID: device-0094 | Location: Kitchen | Battery Level (%): 98.1 | Reading Value: -3.63 | Timestamp: 2021-06-21 15:22:40
Device ID: device-0046 | Location: Garage | Battery Level (%): 35.8 | Reading Value: -37.94 | Timestamp: 2023-05-22 02:31:59
Device ID: device-0086 | Location: Living Room | Battery Level (%): 94.8 | Reading Value: -19.23 | Timestamp: 2022-02-11 12:06:34
Device ID: device-0013 | Location: Living Room | Battery Level (%): 14.5 | Reading Value: -28.22 | Timestamp: 2021-06-08 23:00:49
Device ID: device-0091 | Location: Office | Battery Level (%): 42.3 | Reading Value: 40.99 | Timestamp: 2022-02-27 07:43:35
Device ID: device-0038 | Location: Garage | Battery Level (%): 30.7 | Reading Value: 51.24 | Timestamp: 2021-03-11 09:28:37
<start>
| Device ID | Location | Battery Level (%) | Reading Value | Timestamp |
| --- | --- | --- | --- | --- |
| device-0040 | Office | 52.3 | 50.53 | 2023-05-01 03:33:03 |
| device-0064 | Kitchen | 26.7 | -28.22 | 2022-04-24 05:51:18 |
| device-0100 | Garage | 69.2 | 45.48 | 2023-09-01 03:19:02 |
| device-0094 | Kitchen | 98.1 | -3.63 | 2021-06-21 15:22:40 |
| device-0046 | Garage | 35.8 | -37.94 | 2023-05-22 02:31:59 |
| device-0086 | Living Room | 94.8 | -19.23 | 2022-02-11 12:06:34 |
| device-0013 | Living Room | 14.5 | -28.22 | 2021-06-08 23:00:49 |
| device-0091 | Office | 42.3 | 40.99 | 2022-02-27 07:43:35 |
| device-0038 | Garage | 30.7 | 51.24 | 2021-03-11 09:28:37 |
<end>Can you change this MARKDOWN into Json?
| Name | Birth Month | City | Income |
| --- | --- | --- | --- |
| Jazmin | June | Detroit | 20000 |
| Xander | August | San Diego | 355000 |
| Carl | June | Baltimore | 445000 |
| Elizabeth | October | Milwaukee | 460000 |
| Mya | May | Detroit | 405000 |<start>
[
    {
        "Name": "Jazmin",
        "Birth Month": "June",
        "City": "Detroit",
        "Income": 20000
    },
    {
        "Name": "Xander",
        "Birth Month": "August",
        "City": "San Diego",
        "Income": 355000
    },
    {
        "Name": "Carl",
        "Birth Month": "June",
        "City": "Baltimore",
        "Income": 445000
    },
    {
        "Name": "Elizabeth",
        "Birth Month": "October",
        "City": "Milwaukee",
        "Income": 460000
    },
    {
        "Name": "Mya",
        "Birth Month": "May",
        "City": "Detroit",
        "Income": 405000
    }
]
<end>Transform this yml structure to a plain text format:
- Box Office Earnings (M): 790.43
  Director: Zara Stormrider
  Title: Escape from Earth
- Box Office Earnings (M): 193.98
  Director: Drake Nightshade
  Title: Dreamwalker
- Box Office Earnings (M): 515.39
  Director: Cade Firebrand
  Title: The Endless Horizon
- Box Office Earnings (M): 767.8
  Director: Lira Silverleaf
  Title: Mystery of the Depths
- Box Office Earnings (M): 339.56
  Director: Mara Moonshadow
  Title: Mystery of the Depths
- Box Office Earnings (M): 334.99
  Director: Drake Nightshade
  Title: Escape from Earth
- Box Office Earnings (M): 314.09
  Director: Talon Blackthorn
  Title: Dreamwalker
- Box Office Earnings (M): 339.56
  Director: Aria Ravenwood
  Title: Starbound Odyssey
<start>
Title: Escape from Earth | Director: Zara Stormrider | Box Office Earnings (M): 790.43
Title: Dreamwalker | Director: Drake Nightshade | Box Office Earnings (M): 193.98
Title: The Endless Horizon | Director: Cade Firebrand | Box Office Earnings (M): 515.39
Title: Mystery of the Depths | Director: Lira Silverleaf | Box Office Earnings (M): 767.8
Title: Mystery of the Depths | Director: Mara Moonshadow | Box Office Earnings (M): 339.56
Title: Escape from Earth | Director: Drake Nightshade | Box Office Earnings (M): 334.99
Title: Dreamwalker | Director: Talon Blackthorn | Box Office Earnings (M): 314.09
Title: Starbound Odyssey | Director: Aria Ravenwood | Box Office Earnings (M): 339.56
<end>Here's some markdown data, can you convert it to yml?
| Trip Name | Start Location | Distance (miles) | Duration (hours) | Fuel Used (gallons) |
| --- | --- | --- | --- | --- |
| Valley Voyage | New York | 2332.7 | 16.9 | 46.4 |
| City Explorer | Miami | 2618.4 | 21.9 | 84.4 |
| Canyon Trek | San Francisco | 2139.9 | 5.7 | 47.1 |
| Desert Drive | Los Angeles | 1682.0 | 33.9 | 37.4 |
| Forest Journey | San Francisco | 2218.6 | 61.2 | 59.9 |
| Historic Route | Denver | 1528.5 | 26.8 | 88.6 |
| Mountain Adventure | Houston | 1434.9 | 56.2 | 46.2 |
| Forest Journey | Chicago | 758.9 | 51.2 | 34.5 |
| Desert Drive | New York | 107.5 | 32.1 | 13.2 |
| Highway Odyssey | Denver | 2662.4 | 4.2 | 30.4 |<start>
- Distance (miles): 2332.7
  Duration (hours): 16.9
  Fuel Used (gallons): 46.4
  Start Location: New York
  Trip Name: Valley Voyage
- Distance (miles): 2618.4
  Duration (hours): 21.9
  Fuel Used (gallons): 84.4
  Start Location: Miami
  Trip Name: City Explorer
- Distance (miles): 2139.9
  Duration (hours): 5.7
  Fuel Used (gallons): 47.1
  Start Location: San Francisco
  Trip Name: Canyon Trek
- Distance (miles): 1682.0
  Duration (hours): 33.9
  Fuel Used (gallons): 37.4
  Start Location: Los Angeles
  Trip Name: Desert Drive
- Distance (miles): 2218.6
  Duration (hours): 61.2
  Fuel Used (gallons): 59.9
  Start Location: San Francisco
  Trip Name: Forest Journey
- Distance (miles): 1528.5
  Duration (hours): 26.8
  Fuel Used (gallons): 88.6
  Start Location: Denver
  Trip Name: Historic Route
- Distance (miles): 1434.9
  Duration (hours): 56.2
  Fuel Used (gallons): 46.2
  Start Location: Houston
  Trip Name: Mountain Adventure
- Distance (miles): 758.9
  Duration (hours): 51.2
  Fuel Used (gallons): 34.5
  Start Location: Chicago
  Trip Name: Forest Journey
- Distance (miles): 107.5
  Duration (hours): 32.1
  Fuel Used (gallons): 13.2
  Start Location: New York
  Trip Name: Desert Drive
- Distance (miles): 2662.4
  Duration (hours): 4.2
  Fuel Used (gallons): 30.4
  Start Location: Denver
  Trip Name: Highway Odyssey
<end>Transform this plain text structure to a yaml format:
Device ID: device-0074 | Device Type: Humidity Sensor | Location: Bedroom | Battery Level (%): 95.6 | Reading Value: 9.04 | Timestamp: 2021-02-28 20:11:02
Device ID: device-0012 | Device Type: Pressure Sensor | Location: Hallway | Battery Level (%): 91.3 | Reading Value: 39.37 | Timestamp: 2021-03-06 04:03:54
Device ID: device-0049 | Device Type: Light Sensor | Location: Bedroom | Battery Level (%): 17.0 | Reading Value: 27.57 | Timestamp: 2022-08-21 19:08:31
<start>
- Battery Level (%): 95.6
  Device ID: device-0074
  Device Type: Humidity Sensor
  Location: Bedroom
  Reading Value: 9.04
  Timestamp: '2021-02-28 20:11:02'
- Battery Level (%): 91.3
  Device ID: device-0012
  Device Type: Pressure Sensor
  Location: Hallway
  Reading Value: 39.37
  Timestamp: '2021-03-06 04:03:54'
- Battery Level (%): 17.0
  Device ID: device-0049
  Device Type: Light Sensor
  Location: Bedroom
  Reading Value: 27.57
  Timestamp: '2022-08-21 19:08:31'
<end>Please transform the following json data into csv:
[
    {
        "Company": "GreenEnergy",
        "Date": "2016-06-20",
        "Open Price": 146.55,
        "High Price": 1188.36
    },
    {
        "Company": "GreenEnergy",
        "Date": "2016-08-25",
        "Open Price": 848.49,
        "High Price": 910.48
    },
    {
        "Company": "FoodChain",
        "Date": "2014-12-14",
        "Open Price": 1064.66,
        "High Price": 1188.36
    },
    {
        "Company": "RetailWorld",
        "Date": "2019-04-22",
        "Open Price": 784.5,
        "High Price": 1250.24
    },
    {
        "Company": "AutoMotive",
        "Date": "2013-02-06",
        "Open Price": 848.49,
        "High Price": 848.49
    },
    {
        "Company": "TechnoCorp",
        "Date": "2013-03-01",
        "Open Price": 573.98,
        "High Price": 969.5
    },
    {
        "Company": "GreenEnergy",
        "Date": "2020-07-14",
        "Open Price": 337.36,
        "High Price": 359.16
    },
    {
        "Company": "MediaGroup",
        "Date": "2015-11-07",
        "Open Price": 194.76,
        "High Price": 1313.4
    },
    {
        "Company": "MediaGroup",
        "Date": "2016-04-05",
        "Open Price": 924.62,
        "High Price": 1223.35
    }
]<start>
Company,Date,Open Price,High Price
GreenEnergy,2016-06-20,146.55,1188.36
GreenEnergy,2016-08-25,848.49,910.48
FoodChain,2014-12-14,1064.66,1188.36
RetailWorld,2019-04-22,784.5,1250.24
AutoMotive,2013-02-06,848.49,848.49
TechnoCorp,2013-03-01,573.98,969.5
GreenEnergy,2020-07-14,337.36,359.16
MediaGroup,2015-11-07,194.76,1313.4
MediaGroup,2016-04-05,924.62,1223.35
<end>Convert this json to csv:
[
    {
        "Name": "Lowell",
        "Age": 25,
        "Birth Month": "May",
        "Income": 335000
    },
    {
        "Name": "Gail",
        "Age": 61,
        "Birth Month": "November",
        "Income": 55000
    },
    {
        "Name": "Jesus",
        "Age": 36,
        "Birth Month": "May",
        "Income": 370000
    },
    {
        "Name": "Mallory",
        "Age": 34,
        "Birth Month": "September",
        "Income": 420000
    },
    {
        "Name": "Graham",
        "Age": 34,
        "Birth Month": "March",
        "Income": 355000
    },
    {
        "Name": "Roger",
        "Age": 44,
        "Birth Month": "January",
        "Income": 445000
    },
    {
        "Name": "Heather",
        "Age": 31,
        "Birth Month": "November",
        "Income": 170000
    },
    {
        "Name": "Bobbie",
        "Age": 43,
        "Birth Month": "November",
        "Income": 420000
    },
    {
        "Name": "Jasmin",
        "Age": 37,
        "Birth Month": "November",
        "Income": 85000
    }
]<start>
Name,Age,Birth Month,Income
Lowell,25,May,335000
Gail,61,November,55000
Jesus,36,May,370000
Mallory,34,September,420000
Graham,34,March,355000
Roger,44,January,445000
Heather,31,November,170000
Bobbie,43,November,420000
Jasmin,37,November,85000
<end>Convert this CSV to json:
Restaurant Name,Cuisine,Rating
Pizza Planet,Mexican,4
Pasta Palace,French,1
Sushi World,Chinese,5
Pizza Planet,Japanese,5
The Steakhouse,Indian,5
The Golden Spoon,French,2
Pasta Palace,American,1
Curry Corner,Chinese,2
<start>
[
    {
        "Restaurant Name": "Pizza Planet",
        "Cuisine": "Mexican",
        "Rating": 4
    },
    {
        "Restaurant Name": "Pasta Palace",
        "Cuisine": "French",
        "Rating": 1
    },
    {
        "Restaurant Name": "Sushi World",
        "Cuisine": "Chinese",
        "Rating": 5
    },
    {
        "Restaurant Name": "Pizza Planet",
        "Cuisine": "Japanese",
        "Rating": 5
    },
    {
        "Restaurant Name": "The Steakhouse",
        "Cuisine": "Indian",
        "Rating": 5
    },
    {
        "Restaurant Name": "The Golden Spoon",
        "Cuisine": "French",
        "Rating": 2
    },
    {
        "Restaurant Name": "Pasta Palace",
        "Cuisine": "American",
        "Rating": 1
    },
    {
        "Restaurant Name": "Curry Corner",
        "Cuisine": "Chinese",
        "Rating": 2
    }
]
<end>Please transform the following YML data into json:
- Category: Sports
  Price: 115.23
  Product Name: Widget
  SKU: SKU-1088
  Supplier Name: ACME Corp
- Category: Sports
  Price: 304.31
  Product Name: Whatchamacallit
  SKU: SKU-1004
  Supplier Name: Wonka Industries
- Category: Household
  Price: 213.03
  Product Name: Thingamajig
  SKU: SKU-1043
  Supplier Name: Wonka Industries
- Category: Household
  Price: 480.83
  Product Name: Instrument
  SKU: SKU-1018
  Supplier Name: ACME Corp
- Category: Toys
  Price: 465.26
  Product Name: Apparatus
  SKU: SKU-1000
  Supplier Name: ACME Corp
- Category: Automotive
  Price: 497.81
  Product Name: Doohickey
  SKU: SKU-1005
  Supplier Name: Umbrella Corp
- Category: Automotive
  Price: 388.91
  Product Name: Doohickey
  SKU: SKU-1085
  Supplier Name: Umbrella Corp
- Category: Household
  Price: 325.08
  Product Name: Gizmo
  SKU: SKU-1023
  Supplier Name: Umbrella Corp
- Category: Toys
  Price: 234.03
  Product Name: Gadget
  SKU: SKU-1002
  Supplier Name: Wonka Industries
<start>
[
    {
        "Product Name": "Widget",
        "SKU": "SKU-1088",
        "Price": 115.23,
        "Category": "Sports",
        "Supplier Name": "ACME Corp"
    },
    {
        "Product Name": "Whatchamacallit",
        "SKU": "SKU-1004",
        "Price": 304.31,
        "Category": "Sports",
        "Supplier Name": "Wonka Industries"
    },
    {
        "Product Name": "Thingamajig",
        "SKU": "SKU-1043",
        "Price": 213.03,
        "Category": "Household",
        "Supplier Name": "Wonka Industries"
    },
    {
        "Product Name": "Instrument",
        "SKU": "SKU-1018",
        "Price": 480.83,
        "Category": "Household",
        "Supplier Name": "ACME Corp"
    },
    {
        "Product Name": "Apparatus",
        "SKU": "SKU-1000",
        "Price": 465.26,
        "Category": "Toys",
        "Supplier Name": "ACME Corp"
    },
    {
        "Product Name": "Doohickey",
        "SKU": "SKU-1005",
        "Price": 497.81,
        "Category": "Automotive",
        "Supplier Name": "Umbrella Corp"
    },
    {
        "Product Name": "Doohickey",
        "SKU": "SKU-1085",
        "Price": 388.91,
        "Category": "Automotive",
        "Supplier Name": "Umbrella Corp"
    },
    {
        "Product Name": "Gizmo",
        "SKU": "SKU-1023",
        "Price": 325.08,
        "Category": "Household",
        "Supplier Name": "Umbrella Corp"
    },
    {
        "Product Name": "Gadget",
        "SKU": "SKU-1002",
        "Price": 234.03,
        "Category": "Toys",
        "Supplier Name": "Wonka Industries"
    }
]
<end>Transform this yaml structure to a markdown format:
- Condition: Windy
  Day: Wednesday
  Humidity (%): 52
  Location: Denver
  Temperature (C): -1.2
  Wind Speed (km/h): 27.1
- Condition: Snowy
  Day: Monday
  Humidity (%): 33
  Location: Denver
  Temperature (C): -7.5
  Wind Speed (km/h): 20.8
- Condition: Stormy
  Day: Monday
  Humidity (%): 54
  Location: Los Angeles
  Temperature (C): 10.5
  Wind Speed (km/h): 17.4
<start>
| Location | Condition | Temperature (C) | Humidity (%) | Wind Speed (km/h) | Day |
| --- | --- | --- | --- | --- | --- |
| Denver | Windy | -1.2 | 52 | 27.1 | Wednesday |
| Denver | Snowy | -7.5 | 33 | 20.8 | Monday |
| Los Angeles | Stormy | 10.5 | 54 | 17.4 | Monday |
<end>Here's some plain text data, can you convert it to csv?
Title: The Forgotten World | Author: Rowan Ashborne | Publication Year: 2002 | Rating: 3.1
Title: Shadows of Solitude | Author: Rowan Ashborne | Publication Year: 1956 | Rating: 4.1
Title: Tales of the Brave | Author: Isla Windrider | Publication Year: 1971 | Rating: 2.4
Title: Tales of the Brave | Author: Draven Blackthorn | Publication Year: 1996 | Rating: 2.5
Title: Tales of the Brave | Author: Sylvia Nightshade | Publication Year: 1994 | Rating: 1.2
Title: The Crystal Key | Author: Galen Starfire | Publication Year: 1971 | Rating: 4.1
<start>
Title,Author,Publication Year,Rating
The Forgotten World,Rowan Ashborne,2002,3.1
Shadows of Solitude,Rowan Ashborne,1956,4.1
Tales of the Brave,Isla Windrider,1971,2.4
Tales of the Brave,Draven Blackthorn,1996,2.5
Tales of the Brave,Sylvia Nightshade,1994,1.2
The Crystal Key,Galen Starfire,1971,4.1
<end>Please transform the following Markdown data into PLAIN TEXT:
| Title | Genre |
| --- | --- |
| The Crystal Key | Thriller |
| Whispers of the Abyss | Historical |
| The Crystal Key | Romance |
| The Silent Grove | Mystery |
| The Silent Grove | Thriller |
| The Crystal Key | Fantasy |
| Legends of the Rift | Mystery |
| A Journey Through Time | Non-Fiction |
| The Silent Grove | Mystery |<start>
Title: The Crystal Key | Genre: Thriller
Title: Whispers of the Abyss | Genre: Historical
Title: The Crystal Key | Genre: Romance
Title: The Silent Grove | Genre: Mystery
Title: The Silent Grove | Genre: Thriller
Title: The Crystal Key | Genre: Fantasy
Title: Legends of the Rift | Genre: Mystery
Title: A Journey Through Time | Genre: Non-Fiction
Title: The Silent Grove | Genre: Mystery
<end>Please transform the following yaml data into PLAIN TEXT:
- Cache Hit Ratio (%): 90.56
  Connection Count: 119
  Database Name: InventoryDB
  Queries per Second: 541.84
  Timestamp: '2021-03-14 20:27:30'
- Cache Hit Ratio (%): 78.98
  Connection Count: 353
  Database Name: ProductsDB
  Queries per Second: 4644.26
  Timestamp: '2023-03-07 22:03:22'
- Cache Hit Ratio (%): 73.42
  Connection Count: 339
  Database Name: MetricsDB
  Queries per Second: 3372.17
  Timestamp: '2022-03-05 21:37:43'
- Cache Hit Ratio (%): 77.97
  Connection Count: 494
  Database Name: AnalyticsDB
  Queries per Second: 430.7
  Timestamp: '2023-09-10 13:02:41'
- Cache Hit Ratio (%): 82.12
  Connection Count: 91
  Database Name: InventoryDB
  Queries per Second: 4773.93
  Timestamp: '2023-10-27 02:51:41'
- Cache Hit Ratio (%): 93.43
  Connection Count: 271
  Database Name: OrdersDB
  Queries per Second: 373.72
  Timestamp: '2023-01-18 23:48:03'
- Cache Hit Ratio (%): 98.64
  Connection Count: 57
  Database Name: SalesDB
  Queries per Second: 1920.43
  Timestamp: '2023-02-08 22:28:41'
<start>
Database Name: InventoryDB | Queries per Second: 541.84 | Cache Hit Ratio (%): 90.56 | Connection Count: 119 | Timestamp: 2021-03-14 20:27:30
Database Name: ProductsDB | Queries per Second: 4644.26 | Cache Hit Ratio (%): 78.98 | Connection Count: 353 | Timestamp: 2023-03-07 22:03:22
Database Name: MetricsDB | Queries per Second: 3372.17 | Cache Hit Ratio (%): 73.42 | Connection Count: 339 | Timestamp: 2022-03-05 21:37:43
Database Name: AnalyticsDB | Queries per Second: 430.7 | Cache Hit Ratio (%): 77.97 | Connection Count: 494 | Timestamp: 2023-09-10 13:02:41
Database Name: InventoryDB | Queries per Second: 4773.93 | Cache Hit Ratio (%): 82.12 | Connection Count: 91 | Timestamp: 2023-10-27 02:51:41
Database Name: OrdersDB | Queries per Second: 373.72 | Cache Hit Ratio (%): 93.43 | Connection Count: 271 | Timestamp: 2023-01-18 23:48:03
Database Name: SalesDB | Queries per Second: 1920.43 | Cache Hit Ratio (%): 98.64 | Connection Count: 57 | Timestamp: 2023-02-08 22:28:41
<end>Here's some json data, can you convert it to csv?
[
    {
        "Release Year": 2000,
        "Box Office Earnings (M)": 539.49
    },
    {
        "Release Year": 1979,
        "Box Office Earnings (M)": 376.76
    },
    {
        "Release Year": 1996,
        "Box Office Earnings (M)": 458.46
    },
    {
        "Release Year": 1985,
        "Box Office Earnings (M)": 467.75
    },
    {
        "Release Year": 1976,
        "Box Office Earnings (M)": 107.15
    },
    {
        "Release Year": 1973,
        "Box Office Earnings (M)": 379.52
    }
]<start>
Release Year,Box Office Earnings (M)
2000,539.49
1979,376.76
1996,458.46
1985,467.75
1976,107.15
1973,379.52
<end>Transform this json structure to a Csv format:
[
    {
        "Sector": "Automotive",
        "Stock Price": 875.2,
        "Annual Revenue (B)": 320.46
    },
    {
        "Sector": "Biotech",
        "Stock Price": 83.31,
        "Annual Revenue (B)": 79.18
    },
    {
        "Sector": "Retail",
        "Stock Price": 852.28,
        "Annual Revenue (B)": 465.8
    },
    {
        "Sector": "Technology",
        "Stock Price": 476.68,
        "Annual Revenue (B)": 495.53
    },
    {
        "Sector": "Biotech",
        "Stock Price": 510.11,
        "Annual Revenue (B)": 310.21
    },
    {
        "Sector": "Retail",
        "Stock Price": 427.01,
        "Annual Revenue (B)": 468.4
    },
    {
        "Sector": "Healthcare",
        "Stock Price": 637.65,
        "Annual Revenue (B)": 260.1
    }
]<start>
Sector,Stock Price,Annual Revenue (B)
Automotive,875.2,320.46
Biotech,83.31,79.18
Retail,852.28,465.8
Technology,476.68,495.53
Biotech,510.11,310.21
Retail,427.01,468.4
Healthcare,637.65,260.1
<end>Can you change this json into Plain text?
[
    {
        "Restaurant Name": "The Golden Spoon",
        "Cuisine": "Mexican",
        "Location": "Miami",
        "Price Range": "$$"
    },
    {
        "Restaurant Name": "The Steakhouse",
        "Cuisine": "Mexican",
        "Location": "Los Angeles",
        "Price Range": "$$$$$"
    },
    {
        "Restaurant Name": "Curry Corner",
        "Cuisine": "Mediterranean",
        "Location": "Houston",
        "Price Range": "$$$$"
    },
    {
        "Restaurant Name": "BBQ Barn",
        "Cuisine": "Mediterranean",
        "Location": "Houston",
        "Price Range": "$"
    },
    {
        "Restaurant Name": "The Steakhouse",
        "Cuisine": "Chinese",
        "Location": "Los Angeles",
        "Price Range": "$$"
    },
    {
        "Restaurant Name": "Curry Corner",
        "Cuisine": "Italian",
        "Location": "Seattle",
        "Price Range": "$"
    }
]<start>
Restaurant Name: The Golden Spoon | Cuisine: Mexican | Location: Miami | Price Range: $$
Restaurant Name: The Steakhouse | Cuisine: Mexican | Location: Los Angeles | Price Range: $$$$$
Restaurant Name: Curry Corner | Cuisine: Mediterranean | Location: Houston | Price Range: $$$$
Restaurant Name: BBQ Barn | Cuisine: Mediterranean | Location: Houston | Price Range: $
Restaurant Name: The Steakhouse | Cuisine: Chinese | Location: Los Angeles | Price Range: $$
Restaurant Name: Curry Corner | Cuisine: Italian | Location: Seattle | Price Range: $
<end>Here's some JSON data, can you convert it to yaml?
[
    {
        "Market Cap": "Mega Cap",
        "Annual Revenue (B)": 318.04,
        "Quarter": "Q3"
    },
    {
        "Market Cap": "Large Cap",
        "Annual Revenue (B)": 244.01,
        "Quarter": "Q2"
    },
    {
        "Market Cap": "Mid Cap",
        "Annual Revenue (B)": 244.01,
        "Quarter": "Q3"
    }
]<start>
- Annual Revenue (B): 318.04
  Market Cap: Mega Cap
  Quarter: Q3
- Annual Revenue (B): 244.01
  Market Cap: Large Cap
  Quarter: Q2
- Annual Revenue (B): 244.01
  Market Cap: Mid Cap
  Quarter: Q3
<end>Convert this Json to plain text:
[
    {
        "Restaurant Name": "Pizza Planet",
        "Cuisine": "Mediterranean",
        "Rating": 1
    },
    {
        "Restaurant Name": "Curry Corner",
        "Cuisine": "American",
        "Rating": 5
    },
    {
        "Restaurant Name": "BBQ Barn",
        "Cuisine": "Indian",
        "Rating": 1
    },
    {
        "Restaurant Name": "Pizza Planet",
        "Cuisine": "American",
        "Rating": 4
    },
    {
        "Restaurant Name": "The Steakhouse",
        "Cuisine": "French",
        "Rating": 1
    }
]<start>
Restaurant Name: Pizza Planet | Cuisine: Mediterranean | Rating: 1
Restaurant Name: Curry Corner | Cuisine: American | Rating: 5
Restaurant Name: BBQ Barn | Cuisine: Indian | Rating: 1
Restaurant Name: Pizza Planet | Cuisine: American | Rating: 4
Restaurant Name: The Steakhouse | Cuisine: French | Rating: 1
<end>Convert this CSV to json:
Title,Author,Genre,Publication Year,Rating
A Journey Through Time,Luna Silverleaf,Science Fiction,1955,2.4
The Forgotten World,Orion Frostblade,Mystery,1975,1.2
The Crystal Key,Kara Firebrand,Historical,1999,4.5
<start>
[
    {
        "Title": "A Journey Through Time",
        "Author": "Luna Silverleaf",
        "Genre": "Science Fiction",
        "Publication Year": 1955,
        "Rating": 2.4
    },
    {
        "Title": "The Forgotten World",
        "Author": "Orion Frostblade",
        "Genre": "Mystery",
        "Publication Year": 1975,
        "Rating": 1.2
    },
    {
        "Title": "The Crystal Key",
        "Author": "Kara Firebrand",
        "Genre": "Historical",
        "Publication Year": 1999,
        "Rating": 4.5
    }
]
<end>Please transform the following YML data into CSV:
- Battery Level (%): 33.6
  Device Type: Pressure Sensor
  Reading Value: 43.38
- Battery Level (%): 13.8
  Device Type: Pressure Sensor
  Reading Value: 53.37
- Battery Level (%): 68.6
  Device Type: Motion Detector
  Reading Value: 36.2
- Battery Level (%): 60.5
  Device Type: Pressure Sensor
  Reading Value: 36.2
- Battery Level (%): 79.0
  Device Type: Motion Detector
  Reading Value: 63.17
- Battery Level (%): 51.0
  Device Type: Motion Detector
  Reading Value: 74.5
- Battery Level (%): 95.8
  Device Type: Light Sensor
  Reading Value: 42.59
- Battery Level (%): 47.7
  Device Type: Light Sensor
  Reading Value: 63.17
<start>
Device Type,Battery Level (%),Reading Value
Pressure Sensor,33.6,43.38
Pressure Sensor,13.8,53.37
Motion Detector,68.6,36.2
Pressure Sensor,60.5,36.2
Motion Detector,79.0,63.17
Motion Detector,51.0,74.5
Light Sensor,95.8,42.59
Light Sensor,47.7,63.17
<end>Here's some plain text data, can you convert it to Yml?
Database Name: ProfilesDB | Queries per Second: 2572.27 | Cache Hit Ratio (%): 81.78 | Connection Count: 237 | Timestamp: 2021-08-14 06:03:06
Database Name: UserDB | Queries per Second: 4375.14 | Cache Hit Ratio (%): 89.13 | Connection Count: 370 | Timestamp: 2021-07-09 08:59:04
Database Name: OrdersDB | Queries per Second: 107.94 | Cache Hit Ratio (%): 78.87 | Connection Count: 460 | Timestamp: 2021-01-09 15:57:51
Database Name: AnalyticsDB | Queries per Second: 540.31 | Cache Hit Ratio (%): 91.03 | Connection Count: 149 | Timestamp: 2021-09-20 12:28:14
Database Name: SessionsDB | Queries per Second: 491.62 | Cache Hit Ratio (%): 90.61 | Connection Count: 472 | Timestamp: 2023-10-19 10:07:37
Database Name: InventoryDB | Queries per Second: 4319.51 | Cache Hit Ratio (%): 90.04 | Connection Count: 215 | Timestamp: 2021-09-22 16:40:16
Database Name: OrdersDB | Queries per Second: 4515.13 | Cache Hit Ratio (%): 81.78 | Connection Count: 100 | Timestamp: 2021-06-08 17:25:07
Database Name: LogsDB | Queries per Second: 3599.4 | Cache Hit Ratio (%): 70.68 | Connection Count: 420 | Timestamp: 2022-10-19 23:02:23
Database Name: ProfilesDB | Queries per Second: 2435.16 | Cache Hit Ratio (%): 90.9 | Connection Count: 56 | Timestamp: 2022-12-26 14:16:53
Database Name: SalesDB | Queries per Second: 1637.62 | Cache Hit Ratio (%): 88.69 | Connection Count: 180 | Timestamp: 2022-04-25 17:25:01
<start>
- Cache Hit Ratio (%): 81.78
  Connection Count: 237
  Database Name: ProfilesDB
  Queries per Second: 2572.27
  Timestamp: '2021-08-14 06:03:06'
- Cache Hit Ratio (%): 89.13
  Connection Count: 370
  Database Name: UserDB
  Queries per Second: 4375.14
  Timestamp: '2021-07-09 08:59:04'
- Cache Hit Ratio (%): 78.87
  Connection Count: 460
  Database Name: OrdersDB
  Queries per Second: 107.94
  Timestamp: '2021-01-09 15:57:51'
- Cache Hit Ratio (%): 91.03
  Connection Count: 149
  Database Name: AnalyticsDB
  Queries per Second: 540.31
  Timestamp: '2021-09-20 12:28:14'
- Cache Hit Ratio (%): 90.61
  Connection Count: 472
  Database Name: SessionsDB
  Queries per Second: 491.62
  Timestamp: '2023-10-19 10:07:37'
- Cache Hit Ratio (%): 90.04
  Connection Count: 215
  Database Name: InventoryDB
  Queries per Second: 4319.51
  Timestamp: '2021-09-22 16:40:16'
- Cache Hit Ratio (%): 81.78
  Connection Count: 100
  Database Name: OrdersDB
  Queries per Second: 4515.13
  Timestamp: '2021-06-08 17:25:07'
- Cache Hit Ratio (%): 70.68
  Connection Count: 420
  Database Name: LogsDB
  Queries per Second: 3599.4
  Timestamp: '2022-10-19 23:02:23'
- Cache Hit Ratio (%): 90.9
  Connection Count: 56
  Database Name: ProfilesDB
  Queries per Second: 2435.16
  Timestamp: '2022-12-26 14:16:53'
- Cache Hit Ratio (%): 88.69
  Connection Count: 180
  Database Name: SalesDB
  Queries per Second: 1637.62
  Timestamp: '2022-04-25 17:25:01'
<end>Please transform the following CSV data into yml:
Trip Name,Start Location,End Location,Distance (miles),Duration (hours),Fuel Used (gallons)
Forest Journey,San Francisco,Houston,592.3,33.7,34.2
Highway Odyssey,Chicago,New York,325.0,16.1,27.7
Canyon Trek,San Francisco,Los Angeles,67.4,64.7,42.8
Canyon Trek,Houston,Denver,2845.3,17.3,21.6
Highway Odyssey,San Francisco,Denver,836.2,45.3,34.2
Lakeside Retreat,Houston,New York,67.4,8.0,84.1
Forest Journey,San Francisco,New York,1441.0,55.7,91.3
Historic Route,Los Angeles,Houston,199.8,48.7,22.2
<start>
- Distance (miles): 592.3
  Duration (hours): 33.7
  End Location: Houston
  Fuel Used (gallons): 34.2
  Start Location: San Francisco
  Trip Name: Forest Journey
- Distance (miles): 325.0
  Duration (hours): 16.1
  End Location: New York
  Fuel Used (gallons): 27.7
  Start Location: Chicago
  Trip Name: Highway Odyssey
- Distance (miles): 67.4
  Duration (hours): 64.7
  End Location: Los Angeles
  Fuel Used (gallons): 42.8
  Start Location: San Francisco
  Trip Name: Canyon Trek
- Distance (miles): 2845.3
  Duration (hours): 17.3
  End Location: Denver
  Fuel Used (gallons): 21.6
  Start Location: Houston
  Trip Name: Canyon Trek
- Distance (miles): 836.2
  Duration (hours): 45.3
  End Location: Denver
  Fuel Used (gallons): 34.2
  Start Location: San Francisco
  Trip Name: Highway Odyssey
- Distance (miles): 67.4
  Duration (hours): 8.0
  End Location: New York
  Fuel Used (gallons): 84.1
  Start Location: Houston
  Trip Name: Lakeside Retreat
- Distance (miles): 1441.0
  Duration (hours): 55.7
  End Location: New York
  Fuel Used (gallons): 91.3
  Start Location: San Francisco
  Trip Name: Forest Journey
- Distance (miles): 199.8
  Duration (hours): 48.7
  End Location: Houston
  Fuel Used (gallons): 22.2
  Start Location: Los Angeles
  Trip Name: Historic Route
<end>Transform this Plain text structure to a MARKDOWN format:
City: Baltimore | Income: 440000
City: Milwaukee | Income: 260000
City: Memphis | Income: 210000
City: Milwaukee | Income: 415000
City: San Jose | Income: 385000
<start>
| City | Income |
| --- | --- |
| Baltimore | 440000 |
| Milwaukee | 260000 |
| Memphis | 210000 |
| Milwaukee | 415000 |
| San Jose | 385000 |
<end>Can you change this Json into CSV?
[
    {
        "Database Name": "SessionsDB",
        "Queries per Second": 1121.42,
        "Cache Hit Ratio (%)": 98.68,
        "Connection Count": 348,
        "Average Latency (ms)": 77.99,
        "Timestamp": "2023-05-19 03:38:19"
    },
    {
        "Database Name": "ProductsDB",
        "Queries per Second": 3798.48,
        "Cache Hit Ratio (%)": 80.97,
        "Connection Count": 471,
        "Average Latency (ms)": 49.95,
        "Timestamp": "2022-04-09 05:27:09"
    },
    {
        "Database Name": "MetricsDB",
        "Queries per Second": 2252.36,
        "Cache Hit Ratio (%)": 90.02,
        "Connection Count": 438,
        "Average Latency (ms)": 93.11,
        "Timestamp": "2021-03-23 20:20:23"
    },
    {
        "Database Name": "ProfilesDB",
        "Queries per Second": 480.11,
        "Cache Hit Ratio (%)": 89.68,
        "Connection Count": 225,
        "Average Latency (ms)": 30.85,
        "Timestamp": "2021-10-20 07:02:12"
    }
]<start>
Database Name,Queries per Second,Cache Hit Ratio (%),Connection Count,Average Latency (ms),Timestamp
SessionsDB,1121.42,98.68,348,77.99,2023-05-19 03:38:19
ProductsDB,3798.48,80.97,471,49.95,2022-04-09 05:27:09
MetricsDB,2252.36,90.02,438,93.11,2021-03-23 20:20:23
ProfilesDB,480.11,89.68,225,30.85,2021-10-20 07:02:12
<end>Transform this Json structure to a PLAIN TEXT format:
[
    {
        "Name": "Jaime",
        "Age": 67,
        "Birth Month": "February",
        "Income": 120000
    },
    {
        "Name": "Randolph",
        "Age": 22,
        "Birth Month": "May",
        "Income": 460000
    },
    {
        "Name": "Mateo",
        "Age": 50,
        "Birth Month": "January",
        "Income": 140000
    }
]<start>
Name: Jaime | Age: 67 | Birth Month: February | Income: 120000
Name: Randolph | Age: 22 | Birth Month: May | Income: 460000
Name: Mateo | Age: 50 | Birth Month: January | Income: 140000
<end>Please transform the following csv data into markdown:
Trip Name,Start Location,Distance (miles)
City Explorer,Miami,2654.2
Forest Journey,Denver,482.1
Valley Voyage,Chicago,407.7
Lakeside Retreat,Denver,1554.5
Highway Odyssey,New York,2077.1
Coast to Coast,Chicago,2351.5
Forest Journey,Miami,1429.2
Lakeside Retreat,Denver,993.1
City Explorer,New York,2577.7
<start>
| Trip Name | Start Location | Distance (miles) |
| --- | --- | --- |
| City Explorer | Miami | 2654.2 |
| Forest Journey | Denver | 482.1 |
| Valley Voyage | Chicago | 407.7 |
| Lakeside Retreat | Denver | 1554.5 |
| Highway Odyssey | New York | 2077.1 |
| Coast to Coast | Chicago | 2351.5 |
| Forest Journey | Miami | 1429.2 |
| Lakeside Retreat | Denver | 993.1 |
| City Explorer | New York | 2577.7 |
<end>Can you change this PLAIN TEXT into MARKDOWN?
Trip Name: Historic Route | Start Location: Chicago | End Location: Houston | Duration (hours): 70.4 | Fuel Used (gallons): 42.5
Trip Name: Historic Route | Start Location: Phoenix | End Location: Los Angeles | Duration (hours): 47.2 | Fuel Used (gallons): 53.7
Trip Name: Forest Journey | Start Location: Houston | End Location: Denver | Duration (hours): 1.5 | Fuel Used (gallons): 28.1
Trip Name: Mountain Adventure | Start Location: Denver | End Location: Miami | Duration (hours): 28.3 | Fuel Used (gallons): 28.1
Trip Name: Historic Route | Start Location: Chicago | End Location: Los Angeles | Duration (hours): 47.7 | Fuel Used (gallons): 67.8
Trip Name: Highway Odyssey | Start Location: Miami | End Location: New York | Duration (hours): 64.6 | Fuel Used (gallons): 59.1
Trip Name: Highway Odyssey | Start Location: New York | End Location: Phoenix | Duration (hours): 66.3 | Fuel Used (gallons): 42.5
<start>
| Trip Name | Start Location | End Location | Duration (hours) | Fuel Used (gallons) |
| --- | --- | --- | --- | --- |
| Historic Route | Chicago | Houston | 70.4 | 42.5 |
| Historic Route | Phoenix | Los Angeles | 47.2 | 53.7 |
| Forest Journey | Houston | Denver | 1.5 | 28.1 |
| Mountain Adventure | Denver | Miami | 28.3 | 28.1 |
| Historic Route | Chicago | Los Angeles | 47.7 | 67.8 |
| Highway Odyssey | Miami | New York | 64.6 | 59.1 |
| Highway Odyssey | New York | Phoenix | 66.3 | 42.5 |
<end>Convert this JSON to MARKDOWN:
[
    {
        "Name": "Irma",
        "Birth Month": "February",
        "City": "San Jose",
        "Income": 395000
    },
    {
        "Name": "Kate",
        "Birth Month": "January",
        "City": "Chicago",
        "Income": 25000
    },
    {
        "Name": "Eunice",
        "Birth Month": "March",
        "City": "Seattle",
        "Income": 415000
    },
    {
        "Name": "Jessie",
        "Birth Month": "July",
        "City": "Baltimore",
        "Income": 495000
    },
    {
        "Name": "Piper",
        "Birth Month": "June",
        "City": "Dallas",
        "Income": 275000
    },
    {
        "Name": "Agnes",
        "Birth Month": "November",
        "City": "San Antonio",
        "Income": 340000
    },
    {
        "Name": "Brian",
        "Birth Month": "February",
        "City": "Houston",
        "Income": 245000
    },
    {
        "Name": "Summer",
        "Birth Month": "September",
        "City": "Portland",
        "Income": 215000
    }
]<start>
| Name | Birth Month | City | Income |
| --- | --- | --- | --- |
| Irma | February | San Jose | 395000 |
| Kate | January | Chicago | 25000 |
| Eunice | March | Seattle | 415000 |
| Jessie | July | Baltimore | 495000 |
| Piper | June | Dallas | 275000 |
| Agnes | November | San Antonio | 340000 |
| Brian | February | Houston | 245000 |
| Summer | September | Portland | 215000 |
<end>Convert this csv to Markdown:
Release Year,Box Office Earnings (M)
1997,920.41
1991,285.28
1981,767.93
1970,455.19
1980,729.11
1985,609.76
1972,943.74
1980,639.67
<start>
| Release Year | Box Office Earnings (M) |
| --- | --- |
| 1997 | 920.41 |
| 1991 | 285.28 |
| 1981 | 767.93 |
| 1970 | 455.19 |
| 1980 | 729.11 |
| 1985 | 609.76 |
| 1972 | 943.74 |
| 1980 | 639.67 |
<end>Here's some markdown data, can you convert it to YAML?
| Name | Age | Birth Month | City | Income |
| --- | --- | --- | --- | --- |
| Sallie | 60 | June | Nashville | 440000 |
| Micah | 43 | February | Nashville | 60000 |
| Gus | 30 | January | Columbus | 80000 |
| Rosie | 41 | July | Los Angeles | 365000 |
| Dean | 51 | February | San Diego | 115000 |
| Gabrielle | 53 | April | El Paso | 400000 |<start>
- Age: 60
  Birth Month: June
  City: Nashville
  Income: 440000
  Name: Sallie
- Age: 43
  Birth Month: February
  City: Nashville
  Income: 60000
  Name: Micah
- Age: 30
  Birth Month: January
  City: Columbus
  Income: 80000
  Name: Gus
- Age: 41
  Birth Month: July
  City: Los Angeles
  Income: 365000
  Name: Rosie
- Age: 51
  Birth Month: February
  City: San Diego
  Income: 115000
  Name: Dean
- Age: 53
  Birth Month: April
  City: El Paso
  Income: 400000
  Name: Gabrielle
<end>Please transform the following json data into plain text:
[
    {
        "Company": "RetailWorld",
        "Date": "2021-05-26",
        "Close Price": 1061.76,
        "Low Price": 1061.76,
        "Volume": 3742054
    },
    {
        "Company": "HealthGen",
        "Date": "2017-09-15",
        "Close Price": 388.44,
        "Low Price": 388.44,
        "Volume": 6320136
    },
    {
        "Company": "AeroSystems",
        "Date": "2011-12-26",
        "Close Price": 179.91,
        "Low Price": 179.91,
        "Volume": 4801654
    },
    {
        "Company": "AutoMotive",
        "Date": "2023-05-09",
        "Close Price": 1433.6,
        "Low Price": 781.7,
        "Volume": 1844797
    },
    {
        "Company": "FoodChain",
        "Date": "2018-03-05",
        "Close Price": 883.5,
        "Low Price": 372.59,
        "Volume": 1870042
    }
]<start>
Company: RetailWorld | Date: 2021-05-26 | Close Price: 1061.76 | Low Price: 1061.76 | Volume: 3742054
Company: HealthGen | Date: 2017-09-15 | Close Price: 388.44 | Low Price: 388.44 | Volume: 6320136
Company: AeroSystems | Date: 2011-12-26 | Close Price: 179.91 | Low Price: 179.91 | Volume: 4801654
Company: AutoMotive | Date: 2023-05-09 | Close Price: 1433.6 | Low Price: 781.7 | Volume: 1844797
Company: FoodChain | Date: 2018-03-05 | Close Price: 883.5 | Low Price: 372.59 | Volume: 1870042
<end>Can you change this markdown into yml?
| Device ID | Device Type | Timestamp |
| --- | --- | --- |
| device-0030 | Motion Detector | 2023-02-13 03:07:52 |
| device-0020 | Motion Detector | 2023-08-01 06:57:29 |
| device-0092 | Light Sensor | 2023-12-16 19:10:10 |
| device-0001 | Humidity Sensor | 2021-09-28 14:13:46 |
| device-0005 | Pressure Sensor | 2023-08-01 15:15:15 |
| device-0038 | Motion Detector | 2021-07-21 04:31:46 |
| device-0078 | Light Sensor | 2021-03-28 19:54:27 |
| device-0018 | Motion Detector | 2023-06-24 15:12:30 |
| device-0064 | Light Sensor | 2023-02-25 10:32:07 |
| device-0077 | Pressure Sensor | 2023-11-27 16:18:44 |<start>
- Device ID: device-0030
  Device Type: Motion Detector
  Timestamp: '2023-02-13 03:07:52'
- Device ID: device-0020
  Device Type: Motion Detector
  Timestamp: '2023-08-01 06:57:29'
- Device ID: device-0092
  Device Type: Light Sensor
  Timestamp: '2023-12-16 19:10:10'
- Device ID: device-0001
  Device Type: Humidity Sensor
  Timestamp: '2021-09-28 14:13:46'
- Device ID: device-0005
  Device Type: Pressure Sensor
  Timestamp: '2023-08-01 15:15:15'
- Device ID: device-0038
  Device Type: Motion Detector
  Timestamp: '2021-07-21 04:31:46'
- Device ID: device-0078
  Device Type: Light Sensor
  Timestamp: '2021-03-28 19:54:27'
- Device ID: device-0018
  Device Type: Motion Detector
  Timestamp: '2023-06-24 15:12:30'
- Device ID: device-0064
  Device Type: Light Sensor
  Timestamp: '2023-02-25 10:32:07'
- Device ID: device-0077
  Device Type: Pressure Sensor
  Timestamp: '2023-11-27 16:18:44'
<end>Convert this PLAIN TEXT to markdown:
Birth Month: April | Income: 175000
Birth Month: April | Income: 25000
Birth Month: September | Income: 410000
Birth Month: September | Income: 230000
Birth Month: February | Income: 495000
Birth Month: November | Income: 180000
Birth Month: November | Income: 320000
Birth Month: March | Income: 280000
Birth Month: June | Income: 340000
<start>
| Birth Month | Income |
| --- | --- |
| April | 175000 |
| April | 25000 |
| September | 410000 |
| September | 230000 |
| February | 495000 |
| November | 180000 |
| November | 320000 |
| March | 280000 |
| June | 340000 |
<end>Can you change this JSON into yml?
[
    {
        "Director": "Zara Stormrider",
        "Release Year": 2008,
        "Box Office Earnings (M)": 532.61
    },
    {
        "Director": "Selene Darkwhisper",
        "Release Year": 2010,
        "Box Office Earnings (M)": 123.08
    },
    {
        "Director": "Drake Nightshade",
        "Release Year": 2007,
        "Box Office Earnings (M)": 768.17
    },
    {
        "Director": "Lira Silverleaf",
        "Release Year": 1984,
        "Box Office Earnings (M)": 187.64
    }
]<start>
- Box Office Earnings (M): 532.61
  Director: Zara Stormrider
  Release Year: 2008
- Box Office Earnings (M): 123.08
  Director: Selene Darkwhisper
  Release Year: 2010
- Box Office Earnings (M): 768.17
  Director: Drake Nightshade
  Release Year: 2007
- Box Office Earnings (M): 187.64
  Director: Lira Silverleaf
  Release Year: 1984
<end>Please transform the following Csv data into plain text:
Company,Date,Open Price,High Price,Low Price,Volume
FoodChain,2014-07-24,644.7,1365.17,521.07,4300326
BioLife,2010-07-10,877.07,877.07,237.88,7825882
MediaGroup,2011-04-10,927.16,1287.54,146.57,2728173
AutoMotive,2022-11-07,877.07,1067.59,219.65,9445024
FoodChain,2017-10-05,1399.73,1399.73,272.87,2944796
RetailWorld,2023-05-06,1185.33,1250.64,1185.33,529519
AeroSystems,2022-04-11,1241.88,1241.88,272.87,5149988
FinanceTrust,2017-11-01,1317.58,1317.58,237.88,7648487
BioLife,2011-04-14,146.57,1482.79,146.57,9288344
GreenEnergy,2012-02-16,403.57,1153.64,194.62,185365
<start>
Company: FoodChain | Date: 2014-07-24 | Open Price: 644.7 | High Price: 1365.17 | Low Price: 521.07 | Volume: 4300326
Company: BioLife | Date: 2010-07-10 | Open Price: 877.07 | High Price: 877.07 | Low Price: 237.88 | Volume: 7825882
Company: MediaGroup | Date: 2011-04-10 | Open Price: 927.16 | High Price: 1287.54 | Low Price: 146.57 | Volume: 2728173
Company: AutoMotive | Date: 2022-11-07 | Open Price: 877.07 | High Price: 1067.59 | Low Price: 219.65 | Volume: 9445024
Company: FoodChain | Date: 2017-10-05 | Open Price: 1399.73 | High Price: 1399.73 | Low Price: 272.87 | Volume: 2944796
Company: RetailWorld | Date: 2023-05-06 | Open Price: 1185.33 | High Price: 1250.64 | Low Price: 1185.33 | Volume: 529519
Company: AeroSystems | Date: 2022-04-11 | Open Price: 1241.88 | High Price: 1241.88 | Low Price: 272.87 | Volume: 5149988
Company: FinanceTrust | Date: 2017-11-01 | Open Price: 1317.58 | High Price: 1317.58 | Low Price: 237.88 | Volume: 7648487
Company: BioLife | Date: 2011-04-14 | Open Price: 146.57 | High Price: 1482.79 | Low Price: 146.57 | Volume: 9288344
Company: GreenEnergy | Date: 2012-02-16 | Open Price: 403.57 | High Price: 1153.64 | Low Price: 194.62 | Volume: 185365
<end>Please transform the following markdown data into Json:
| Name | Birth Month | City | Income |
| --- | --- | --- | --- |
| Katrina | June | Phoenix | 425000 |
| Lena | December | Detroit | 245000 |
| Samuel | February | Seattle | 185000 |<start>
[
    {
        "Name": "Katrina",
        "Birth Month": "June",
        "City": "Phoenix",
        "Income": 425000
    },
    {
        "Name": "Lena",
        "Birth Month": "December",
        "City": "Detroit",
        "Income": 245000
    },
    {
        "Name": "Samuel",
        "Birth Month": "February",
        "City": "Seattle",
        "Income": 185000
    }
]
<end>Convert this csv to yaml:
Age,City
44,Portland
25,San Diego
56,El Paso
67,New York
28,Baltimore
56,Dallas
<start>
- Age: 44
  City: Portland
- Age: 25
  City: San Diego
- Age: 56
  City: El Paso
- Age: 67
  City: New York
- Age: 28
  City: Baltimore
- Age: 56
  City: Dallas
<end>Can you change this Yml into csv?
- Birth Month: June
  Income: 435000
- Birth Month: April
  Income: 230000
- Birth Month: December
  Income: 100000
- Birth Month: August
  Income: 390000
<start>
Birth Month,Income
June,435000
April,230000
December,100000
August,390000
<end>Can you change this JSON into YML?
[
    {
        "Trip Name": "Canyon Trek",
        "Start Location": "Phoenix",
        "Duration (hours)": 49.9
    },
    {
        "Trip Name": "Mountain Adventure",
        "Start Location": "New York",
        "Duration (hours)": 17.5
    },
    {
        "Trip Name": "Valley Voyage",
        "Start Location": "Chicago",
        "Duration (hours)": 70.0
    },
    {
        "Trip Name": "Historic Route",
        "Start Location": "Los Angeles",
        "Duration (hours)": 29.2
    },
    {
        "Trip Name": "Historic Route",
        "Start Location": "Chicago",
        "Duration (hours)": 63.5
    },
    {
        "Trip Name": "City Explorer",
        "Start Location": "Los Angeles",
        "Duration (hours)": 61.5
    }
]<start>
- Duration (hours): 49.9
  Start Location: Phoenix
  Trip Name: Canyon Trek
- Duration (hours): 17.5
  Start Location: New York
  Trip Name: Mountain Adventure
- Duration (hours): 70.0
  Start Location: Chicago
  Trip Name: Valley Voyage
- Duration (hours): 29.2
  Start Location: Los Angeles
  Trip Name: Historic Route
- Duration (hours): 63.5
  Start Location: Chicago
  Trip Name: Historic Route
- Duration (hours): 61.5
  Start Location: Los Angeles
  Trip Name: City Explorer
<end>Please transform the following JSON data into YAML:
[
    {
        "Location": "Houston",
        "Condition": "Snowy",
        "Temperature (C)": 19.3,
        "Humidity (%)": 100,
        "Wind Speed (km/h)": 29.8
    },
    {
        "Location": "Seattle",
        "Condition": "Windy",
        "Temperature (C)": 31.1,
        "Humidity (%)": 46,
        "Wind Speed (km/h)": 23.0
    },
    {
        "Location": "Phoenix",
        "Condition": "Foggy",
        "Temperature (C)": -1.5,
        "Humidity (%)": 55,
        "Wind Speed (km/h)": 29.4
    },
    {
        "Location": "Miami",
        "Condition": "Snowy",
        "Temperature (C)": 9.5,
        "Humidity (%)": 92,
        "Wind Speed (km/h)": 26.2
    }
]<start>
- Condition: Snowy
  Humidity (%): 100
  Location: Houston
  Temperature (C): 19.3
  Wind Speed (km/h): 29.8
- Condition: Windy
  Humidity (%): 46
  Location: Seattle
  Temperature (C): 31.1
  Wind Speed (km/h): 23.0
- Condition: Foggy
  Humidity (%): 55
  Location: Phoenix
  Temperature (C): -1.5
  Wind Speed (km/h): 29.4
- Condition: Snowy
  Humidity (%): 92
  Location: Miami
  Temperature (C): 9.5
  Wind Speed (km/h): 26.2
<end>Please transform the following MARKDOWN data into Yaml:
| Author | Rating |
| --- | --- |
| Draven Blackthorn | 1.9 |
| Galen Starfire | 4.5 |
| Isla Windrider | 3.6 |
| Rowan Ashborne | 3.2 |
| Luna Silverleaf | 3.0 |
| Draven Blackthorn | 2.6 |
| Galen Starfire | 2.0 |
| Galen Starfire | 3.0 |
| Orion Frostblade | 4.8 |
| Sylvia Nightshade | 4.7 |<start>
- Author: Draven Blackthorn
  Rating: 1.9
- Author: Galen Starfire
  Rating: 4.5
- Author: Isla Windrider
  Rating: 3.6
- Author: Rowan Ashborne
  Rating: 3.2
- Author: Luna Silverleaf
  Rating: 3.0
- Author: Draven Blackthorn
  Rating: 2.6
- Author: Galen Starfire
  Rating: 2.0
- Author: Galen Starfire
  Rating: 3.0
- Author: Orion Frostblade
  Rating: 4.8
- Author: Sylvia Nightshade
  Rating: 4.7
<end>Transform this Plain text structure to a yaml format:
Name: Janice | Age: 39 | Birth Month: April | City: Portland | Income: 160000
Name: Laurie | Age: 56 | Birth Month: March | City: Detroit | Income: 480000
Name: Cathy | Age: 22 | Birth Month: October | City: Fort Worth | Income: 335000
Name: Reuben | Age: 23 | Birth Month: January | City: San Diego | Income: 210000
<start>
- Age: 39
  Birth Month: April
  City: Portland
  Income: 160000
  Name: Janice
- Age: 56
  Birth Month: March
  City: Detroit
  Income: 480000
  Name: Laurie
- Age: 22
  Birth Month: October
  City: Fort Worth
  Income: 335000
  Name: Cathy
- Age: 23
  Birth Month: January
  City: San Diego
  Income: 210000
  Name: Reuben
<end>Please transform the following YAML data into json:
- Age: 56
  Birth Month: October
  Name: Caitlin
- Age: 35
  Birth Month: November
  Name: Valerie
- Age: 46
  Birth Month: November
  Name: Tricia
- Age: 25
  Birth Month: March
  Name: Robin
- Age: 54
  Birth Month: April
  Name: Ariana
- Age: 47
  Birth Month: October
  Name: Nancy
- Age: 53
  Birth Month: August
  Name: Genevieve
- Age: 54
  Birth Month: July
  Name: Ora
- Age: 37
  Birth Month: October
  Name: Winnie
<start>
[
    {
        "Name": "Caitlin",
        "Age": 56,
        "Birth Month": "October"
    },
    {
        "Name": "Valerie",
        "Age": 35,
        "Birth Month": "November"
    },
    {
        "Name": "Tricia",
        "Age": 46,
        "Birth Month": "November"
    },
    {
        "Name": "Robin",
        "Age": 25,
        "Birth Month": "March"
    },
    {
        "Name": "Ariana",
        "Age": 54,
        "Birth Month": "April"
    },
    {
        "Name": "Nancy",
        "Age": 47,
        "Birth Month": "October"
    },
    {
        "Name": "Genevieve",
        "Age": 53,
        "Birth Month": "August"
    },
    {
        "Name": "Ora",
        "Age": 54,
        "Birth Month": "July"
    },
    {
        "Name": "Winnie",
        "Age": 37,
        "Birth Month": "October"
    }
]
<end>Convert this Json to YAML:
[
    {
        "Temperature (C)": 18.3,
        "Humidity (%)": 59,
        "Wind Speed (km/h)": 22.2,
        "Day": "Sunday"
    },
    {
        "Temperature (C)": 28.1,
        "Humidity (%)": 99,
        "Wind Speed (km/h)": 27.2,
        "Day": "Thursday"
    },
    {
        "Temperature (C)": 37.8,
        "Humidity (%)": 75,
        "Wind Speed (km/h)": 14.2,
        "Day": "Saturday"
    },
    {
        "Temperature (C)": 18.6,
        "Humidity (%)": 77,
        "Wind Speed (km/h)": 8.4,
        "Day": "Friday"
    },
    {
        "Temperature (C)": -1.1,
        "Humidity (%)": 88,
        "Wind Speed (km/h)": 28.4,
        "Day": "Saturday"
    },
    {
        "Temperature (C)": 8.1,
        "Humidity (%)": 25,
        "Wind Speed (km/h)": 25.3,
        "Day": "Friday"
    },
    {
        "Temperature (C)": 16.3,
        "Humidity (%)": 86,
        "Wind Speed (km/h)": 0.8,
        "Day": "Friday"
    }
]<start>
- Day: Sunday
  Humidity (%): 59
  Temperature (C): 18.3
  Wind Speed (km/h): 22.2
- Day: Thursday
  Humidity (%): 99
  Temperature (C): 28.1
  Wind Speed (km/h): 27.2
- Day: Saturday
  Humidity (%): 75
  Temperature (C): 37.8
  Wind Speed (km/h): 14.2
- Day: Friday
  Humidity (%): 77
  Temperature (C): 18.6
  Wind Speed (km/h): 8.4
- Day: Saturday
  Humidity (%): 88
  Temperature (C): -1.1
  Wind Speed (km/h): 28.4
- Day: Friday
  Humidity (%): 25
  Temperature (C): 8.1
  Wind Speed (km/h): 25.3
- Day: Friday
  Humidity (%): 86
  Temperature (C): 16.3
  Wind Speed (km/h): 0.8
<end>Transform this plain text structure to a Csv format:
Director: Rylan Frostblade | Release Year: 1996
Director: Lira Silverleaf | Release Year: 1972
Director: Drake Nightshade | Release Year: 2023
Director: Orin Shadowalker | Release Year: 2009
<start>
Director,Release Year
Rylan Frostblade,1996
Lira Silverleaf,1972
Drake Nightshade,2023
Orin Shadowalker,2009
<end>Here's some markdown data, can you convert it to CSV?
| Company | Sector | Market Cap | Stock Price | Annual Revenue (B) | Quarter |
| --- | --- | --- | --- | --- | --- |
| AeroSpace | Aerospace | Large Cap | 625.16 | 214.49 | Q2 |
| HealthPlus | Finance | Mega Cap | 351.42 | 476.18 | Q4 |
| AutoDrive | Energy | Small Cap | 331.92 | 308.82 | Q2 |<start>
Company,Sector,Market Cap,Stock Price,Annual Revenue (B),Quarter
AeroSpace,Aerospace,Large Cap,625.16,214.49,Q2
HealthPlus,Finance,Mega Cap,351.42,476.18,Q4
AutoDrive,Energy,Small Cap,331.92,308.82,Q2
<end>Here's some csv data, can you convert it to plain text?
Title,Author,Genre,Publication Year
The Silent Grove,Galen Starfire,Thriller,1988
The Last Sky,Thorne Ironwood,Mystery,1979
The Silent Grove,Elara Moonshadow,Mystery,2006
The Forgotten World,Rowan Ashborne,Mystery,1956
The Crystal Key,Thorne Ironwood,Non-Fiction,2014
Shadows of Solitude,Thorne Ironwood,Science Fiction,1952
Echoes of Eternity,Rowan Ashborne,Horror,2013
Legends of the Rift,Luna Silverleaf,Horror,1985
Tales of the Brave,Kara Firebrand,Fantasy,1968
Shadows of Solitude,Sylvia Nightshade,Science Fiction,1977
<start>
Title: The Silent Grove | Author: Galen Starfire | Genre: Thriller | Publication Year: 1988
Title: The Last Sky | Author: Thorne Ironwood | Genre: Mystery | Publication Year: 1979
Title: The Silent Grove | Author: Elara Moonshadow | Genre: Mystery | Publication Year: 2006
Title: The Forgotten World | Author: Rowan Ashborne | Genre: Mystery | Publication Year: 1956
Title: The Crystal Key | Author: Thorne Ironwood | Genre: Non-Fiction | Publication Year: 2014
Title: Shadows of Solitude | Author: Thorne Ironwood | Genre: Science Fiction | Publication Year: 1952
Title: Echoes of Eternity | Author: Rowan Ashborne | Genre: Horror | Publication Year: 2013
Title: Legends of the Rift | Author: Luna Silverleaf | Genre: Horror | Publication Year: 1985
Title: Tales of the Brave | Author: Kara Firebrand | Genre: Fantasy | Publication Year: 1968
Title: Shadows of Solitude | Author: Sylvia Nightshade | Genre: Science Fiction | Publication Year: 1977
<end>Please transform the following yml data into plain text:
- Category: Sports
  Price: 217.46
  Product Name: Gadget
  SKU: SKU-1023
  Stock Quantity: 94
  Supplier Name: Wayne Enterprises
- Category: Automotive
  Price: 242.87
  Product Name: Gizmo
  SKU: SKU-1073
  Stock Quantity: 406
  Supplier Name: Wayne Enterprises
- Category: Electronics
  Price: 201.88
  Product Name: Gadget
  SKU: SKU-1007
  Stock Quantity: 450
  Supplier Name: Globex
<start>
Product Name: Gadget | SKU: SKU-1023 | Price: 217.46 | Stock Quantity: 94 | Category: Sports | Supplier Name: Wayne Enterprises
Product Name: Gizmo | SKU: SKU-1073 | Price: 242.87 | Stock Quantity: 406 | Category: Automotive | Supplier Name: Wayne Enterprises
Product Name: Gadget | SKU: SKU-1007 | Price: 201.88 | Stock Quantity: 450 | Category: Electronics | Supplier Name: Globex
<end>Here's some json data, can you convert it to YAML?
[
    {
        "Name": "Ryker",
        "Age": 23,
        "Birth Month": "February",
        "City": "Milwaukee",
        "Income": 175000
    },
    {
        "Name": "Jaxson",
        "Age": 54,
        "Birth Month": "February",
        "City": "Phoenix",
        "Income": 220000
    },
    {
        "Name": "Beulah",
        "Age": 18,
        "Birth Month": "February",
        "City": "Milwaukee",
        "Income": 390000
    },
    {
        "Name": "Jace",
        "Age": 64,
        "Birth Month": "June",
        "City": "Las Vegas",
        "Income": 355000
    },
    {
        "Name": "Vanessa",
        "Age": 20,
        "Birth Month": "August",
        "City": "Jacksonville",
        "Income": 450000
    },
    {
        "Name": "Clifford",
        "Age": 46,
        "Birth Month": "July",
        "City": "Boston",
        "Income": 385000
    }
]<start>
- Age: 23
  Birth Month: February
  City: Milwaukee
  Income: 175000
  Name: Ryker
- Age: 54
  Birth Month: February
  City: Phoenix
  Income: 220000
  Name: Jaxson
- Age: 18
  Birth Month: February
  City: Milwaukee
  Income: 390000
  Name: Beulah
- Age: 64
  Birth Month: June
  City: Las Vegas
  Income: 355000
  Name: Jace
- Age: 20
  Birth Month: August
  City: Jacksonville
  Income: 450000
  Name: Vanessa
- Age: 46
  Birth Month: July
  City: Boston
  Income: 385000
  Name: Clifford
<end>Transform this Yaml structure to a Json format:
- Category: Toys
  Price: 313.13
  SKU: SKU-1032
  Stock Quantity: 444
- Category: Sports
  Price: 280.78
  SKU: SKU-1010
  Stock Quantity: 94
- Category: Automotive
  Price: 166.4
  SKU: SKU-1078
  Stock Quantity: 125
- Category: Sports
  Price: 127.43
  SKU: SKU-1089
  Stock Quantity: 381
- Category: Toys
  Price: 117.59
  SKU: SKU-1085
  Stock Quantity: 277
- Category: Automotive
  Price: 92.34
  SKU: SKU-1077
  Stock Quantity: 49
- Category: Sports
  Price: 499.95
  SKU: SKU-1007
  Stock Quantity: 257
<start>
[
    {
        "SKU": "SKU-1032",
        "Price": 313.13,
        "Stock Quantity": 444,
        "Category": "Toys"
    },
    {
        "SKU": "SKU-1010",
        "Price": 280.78,
        "Stock Quantity": 94,
        "Category": "Sports"
    },
    {
        "SKU": "SKU-1078",
        "Price": 166.4,
        "Stock Quantity": 125,
        "Category": "Automotive"
    },
    {
        "SKU": "SKU-1089",
        "Price": 127.43,
        "Stock Quantity": 381,
        "Category": "Sports"
    },
    {
        "SKU": "SKU-1085",
        "Price": 117.59,
        "Stock Quantity": 277,
        "Category": "Toys"
    },
    {
        "SKU": "SKU-1077",
        "Price": 92.34,
        "Stock Quantity": 49,
        "Category": "Automotive"
    },
    {
        "SKU": "SKU-1007",
        "Price": 499.95,
        "Stock Quantity": 257,
        "Category": "Sports"
    }
]
<end>Please transform the following json data into Csv:
[
    {
        "Product Name": "Apparatus",
        "SKU": "SKU-1095",
        "Stock Quantity": 390,
        "Category": "Electronics"
    },
    {
        "Product Name": "Thingamajig",
        "SKU": "SKU-1027",
        "Stock Quantity": 331,
        "Category": "Electronics"
    },
    {
        "Product Name": "Widget",
        "SKU": "SKU-1036",
        "Stock Quantity": 182,
        "Category": "Electronics"
    },
    {
        "Product Name": "Device",
        "SKU": "SKU-1088",
        "Stock Quantity": 92,
        "Category": "Automotive"
    },
    {
        "Product Name": "Instrument",
        "SKU": "SKU-1062",
        "Stock Quantity": 249,
        "Category": "Electronics"
    },
    {
        "Product Name": "Device",
        "SKU": "SKU-1081",
        "Stock Quantity": 118,
        "Category": "Household"
    },
    {
        "Product Name": "Widget",
        "SKU": "SKU-1038",
        "Stock Quantity": 1,
        "Category": "Sports"
    },
    {
        "Product Name": "Device",
        "SKU": "SKU-1024",
        "Stock Quantity": 377,
        "Category": "Electronics"
    }
]<start>
Product Name,SKU,Stock Quantity,Category
Apparatus,SKU-1095,390,Electronics
Thingamajig,SKU-1027,331,Electronics
Widget,SKU-1036,182,Electronics
Device,SKU-1088,92,Automotive
Instrument,SKU-1062,249,Electronics
Device,SKU-1081,118,Household
Widget,SKU-1038,1,Sports
Device,SKU-1024,377,Electronics
<end>Convert this YML to Plain text:
- Battery Level (%): 64.4
  Device Type: Pressure Sensor
  Location: Kitchen
  Reading Value: -18.19
  Timestamp: '2023-01-13 13:02:35'
- Battery Level (%): 69.7
  Device Type: Temperature Sensor
  Location: Bathroom
  Reading Value: 57.04
  Timestamp: '2022-08-21 10:19:35'
- Battery Level (%): 98.8
  Device Type: Temperature Sensor
  Location: Bathroom
  Reading Value: 73.03
  Timestamp: '2023-11-01 23:31:23'
- Battery Level (%): 54.6
  Device Type: Temperature Sensor
  Location: Bathroom
  Reading Value: -39.61
  Timestamp: '2021-03-25 00:13:56'
- Battery Level (%): 86.4
  Device Type: Motion Detector
  Location: Garage
  Reading Value: -28.33
  Timestamp: '2022-01-22 23:27:15'
- Battery Level (%): 19.2
  Device Type: Humidity Sensor
  Location: Garden
  Reading Value: 49.17
  Timestamp: '2022-11-13 13:07:29'
- Battery Level (%): 96.0
  Device Type: Humidity Sensor
  Location: Bedroom
  Reading Value: -18.19
  Timestamp: '2023-06-25 17:51:40'
- Battery Level (%): 53.7
  Device Type: Pressure Sensor
  Location: Bedroom
  Reading Value: 42.79
  Timestamp: '2021-04-24 00:23:39'
- Battery Level (%): 28.1
  Device Type: Light Sensor
  Location: Garage
  Reading Value: 10.42
  Timestamp: '2023-06-02 16:13:48'
- Battery Level (%): 19.2
  Device Type: Temperature Sensor
  Location: Bathroom
  Reading Value: 1.1
  Timestamp: '2021-12-08 06:40:58'
<start>
Device Type: Pressure Sensor | Location: Kitchen | Battery Level (%): 64.4 | Reading Value: -18.19 | Timestamp: 2023-01-13 13:02:35
Device Type: Temperature Sensor | Location: Bathroom | Battery Level (%): 69.7 | Reading Value: 57.04 | Timestamp: 2022-08-21 10:19:35
Device Type: Temperature Sensor | Location: Bathroom | Battery Level (%): 98.8 | Reading Value: 73.03 | Timestamp: 2023-11-01 23:31:23
Device Type: Temperature Sensor | Location: Bathroom | Battery Level (%): 54.6 | Reading Value: -39.61 | Timestamp: 2021-03-25 00:13:56
Device Type: Motion Detector | Location: Garage | Battery Level (%): 86.4 | Reading Value: -28.33 | Timestamp: 2022-01-22 23:27:15
Device Type: Humidity Sensor | Location: Garden | Battery Level (%): 19.2 | Reading Value: 49.17 | Timestamp: 2022-11-13 13:07:29
Device Type: Humidity Sensor | Location: Bedroom | Battery Level (%): 96.0 | Reading Value: -18.19 | Timestamp: 2023-06-25 17:51:40
Device Type: Pressure Sensor | Location: Bedroom | Battery Level (%): 53.7 | Reading Value: 42.79 | Timestamp: 2021-04-24 00:23:39
Device Type: Light Sensor | Location: Garage | Battery Level (%): 28.1 | Reading Value: 10.42 | Timestamp: 2023-06-02 16:13:48
Device Type: Temperature Sensor | Location: Bathroom | Battery Level (%): 19.2 | Reading Value: 1.1 | Timestamp: 2021-12-08 06:40:58
<end>Can you change this YAML into markdown?
- Battery Level (%): 99.1
  Device ID: device-0093
  Device Type: Temperature Sensor
  Location: Hallway
- Battery Level (%): 93.8
  Device ID: device-0063
  Device Type: Motion Detector
  Location: Garage
- Battery Level (%): 71.5
  Device ID: device-0087
  Device Type: Light Sensor
  Location: Garden
- Battery Level (%): 53.9
  Device ID: device-0083
  Device Type: Light Sensor
  Location: Bedroom
<start>
| Device ID | Device Type | Location | Battery Level (%) |
| --- | --- | --- | --- |
| device-0093 | Temperature Sensor | Hallway | 99.1 |
| device-0063 | Motion Detector | Garage | 93.8 |
| device-0087 | Light Sensor | Garden | 71.5 |
| device-0083 | Light Sensor | Bedroom | 53.9 |
<end>Can you change this Yaml into Csv?
- Age: 41
  Birth Month: July
  City: Charlotte
  Income: 480000
  Name: Ross
- Age: 54
  Birth Month: August
  City: Houston
  Income: 95000
  Name: Katherine
- Age: 43
  Birth Month: May
  City: Jacksonville
  Income: 120000
  Name: Jasmin
- Age: 28
  Birth Month: September
  City: Detroit
  Income: 20000
  Name: Peyton
- Age: 19
  Birth Month: June
  City: Oklahoma City
  Income: 310000
  Name: Hugh
<start>
Name,Age,Birth Month,City,Income
Ross,41,July,Charlotte,480000
Katherine,54,August,Houston,95000
Jasmin,43,May,Jacksonville,120000
Peyton,28,September,Detroit,20000
Hugh,19,June,Oklahoma City,310000
<end>Convert this PLAIN TEXT to csv:
Sector: Biotech | Market Cap: Mid Cap | Stock Price: 308.18 | Annual Revenue (B): 370.02 | Quarter: Q1
Sector: Technology | Market Cap: Small Cap | Stock Price: 842.18 | Annual Revenue (B): 87.47 | Quarter: Q1
Sector: Biotech | Market Cap: Mid Cap | Stock Price: 52.46 | Annual Revenue (B): 320.94 | Quarter: Q1
Sector: Finance | Market Cap: Small Cap | Stock Price: 429.59 | Annual Revenue (B): 103.36 | Quarter: Q3
Sector: Technology | Market Cap: Large Cap | Stock Price: 753.55 | Annual Revenue (B): 302.95 | Quarter: Q2
Sector: Aerospace | Market Cap: Mega Cap | Stock Price: 975.93 | Annual Revenue (B): 177.92 | Quarter: Q2
Sector: Automotive | Market Cap: Small Cap | Stock Price: 320.52 | Annual Revenue (B): 418.75 | Quarter: Q4
Sector: Aerospace | Market Cap: Small Cap | Stock Price: 22.98 | Annual Revenue (B): 353.74 | Quarter: Q1
<start>
Sector,Market Cap,Stock Price,Annual Revenue (B),Quarter
Biotech,Mid Cap,308.18,370.02,Q1
Technology,Small Cap,842.18,87.47,Q1
Biotech,Mid Cap,52.46,320.94,Q1
Finance,Small Cap,429.59,103.36,Q3
Technology,Large Cap,753.55,302.95,Q2
Aerospace,Mega Cap,975.93,177.92,Q2
Automotive,Small Cap,320.52,418.75,Q4
Aerospace,Small Cap,22.98,353.74,Q1
<end>Transform this markdown structure to a json format:
| Date | Open Price | Close Price | High Price | Low Price | Volume |
| --- | --- | --- | --- | --- | --- |
| 2015-03-18 | 885.63 | 453.42 | 885.63 | 453.42 | 6276991 |
| 2016-02-10 | 1233.48 | 1206.34 | 1233.48 | 1206.34 | 6276991 |
| 2021-09-27 | 1088.35 | 1352.25 | 1352.25 | 185.55 | 3614202 |
| 2022-10-17 | 527.98 | 1461.02 | 1461.02 | 527.98 | 6651974 |
| 2023-09-04 | 300.97 | 554.15 | 947.07 | 300.97 | 2182941 |
| 2023-06-18 | 185.55 | 987.9 | 987.9 | 185.55 | 191477 |
| 2017-04-23 | 950.38 | 1456.5 | 1456.5 | 185.55 | 1659561 |
| 2017-08-27 | 453.42 | 899.54 | 899.54 | 453.42 | 2970997 |
| 2010-05-05 | 300.97 | 632.62 | 1265.78 | 300.97 | 2015664 |<start>
[
    {
        "Date": "2015-03-18",
        "Open Price": 885.63,
        "Close Price": 453.42,
        "High Price": 885.63,
        "Low Price": 453.42,
        "Volume": 6276991
    },
    {
        "Date": "2016-02-10",
        "Open Price": 1233.48,
        "Close Price": 1206.34,
        "High Price": 1233.48,
        "Low Price": 1206.34,
        "Volume": 6276991
    },
    {
        "Date": "2021-09-27",
        "Open Price": 1088.35,
        "Close Price": 1352.25,
        "High Price": 1352.25,
        "Low Price": 185.55,
        "Volume": 3614202
    },
    {
        "Date": "2022-10-17",
        "Open Price": 527.98,
        "Close Price": 1461.02,
        "High Price": 1461.02,
        "Low Price": 527.98,
        "Volume": 6651974
    },
    {
        "Date": "2023-09-04",
        "Open Price": 300.97,
        "Close Price": 554.15,
        "High Price": 947.07,
        "Low Price": 300.97,
        "Volume": 2182941
    },
    {
        "Date": "2023-06-18",
        "Open Price": 185.55,
        "Close Price": 987.9,
        "High Price": 987.9,
        "Low Price": 185.55,
        "Volume": 191477
    },
    {
        "Date": "2017-04-23",
        "Open Price": 950.38,
        "Close Price": 1456.5,
        "High Price": 1456.5,
        "Low Price": 185.55,
        "Volume": 1659561
    },
    {
        "Date": "2017-08-27",
        "Open Price": 453.42,
        "Close Price": 899.54,
        "High Price": 899.54,
        "Low Price": 453.42,
        "Volume": 2970997
    },
    {
        "Date": "2010-05-05",
        "Open Price": 300.97,
        "Close Price": 632.62,
        "High Price": 1265.78,
        "Low Price": 300.97,
        "Volume": 2015664
    }
]
<end>Here's some plain text data, can you convert it to json?
Age: 43 | Birth Month: June | Income: 490000
Age: 58 | Birth Month: October | Income: 415000
Age: 54 | Birth Month: September | Income: 145000
Age: 50 | Birth Month: December | Income: 420000
Age: 61 | Birth Month: June | Income: 20000
Age: 51 | Birth Month: January | Income: 50000
Age: 65 | Birth Month: September | Income: 405000
Age: 64 | Birth Month: April | Income: 295000
Age: 42 | Birth Month: October | Income: 105000
<start>
[
    {
        "Age": 43,
        "Birth Month": "June",
        "Income": 490000
    },
    {
        "Age": 58,
        "Birth Month": "October",
        "Income": 415000
    },
    {
        "Age": 54,
        "Birth Month": "September",
        "Income": 145000
    },
    {
        "Age": 50,
        "Birth Month": "December",
        "Income": 420000
    },
    {
        "Age": 61,
        "Birth Month": "June",
        "Income": 20000
    },
    {
        "Age": 51,
        "Birth Month": "January",
        "Income": 50000
    },
    {
        "Age": 65,
        "Birth Month": "September",
        "Income": 405000
    },
    {
        "Age": 64,
        "Birth Month": "April",
        "Income": 295000
    },
    {
        "Age": 42,
        "Birth Month": "October",
        "Income": 105000
    }
]
<end>Can you change this Yaml into CSV?
- Genre: Non-Fiction
  Rating: 3.9
  Title: The Crystal Key
- Genre: Mystery
  Rating: 2.7
  Title: Whispers of the Abyss
- Genre: Science Fiction
  Rating: 3.8
  Title: Legends of the Rift
- Genre: Historical
  Rating: 4.2
  Title: Shadows of Solitude
- Genre: Science Fiction
  Rating: 4.1
  Title: The Silent Grove
- Genre: Mystery
  Rating: 1.9
  Title: A Journey Through Time
<start>
Title,Genre,Rating
The Crystal Key,Non-Fiction,3.9
Whispers of the Abyss,Mystery,2.7
Legends of the Rift,Science Fiction,3.8
Shadows of Solitude,Historical,4.2
The Silent Grove,Science Fiction,4.1
A Journey Through Time,Mystery,1.9
<end>Convert this yaml to PLAIN TEXT:
- Cuisine: Mexican
  Restaurant Name: Vegan Delight
- Cuisine: American
  Restaurant Name: Burger Haven
- Cuisine: Italian
  Restaurant Name: Pizza Planet
- Cuisine: French
  Restaurant Name: Pizza Planet
- Cuisine: Mexican
  Restaurant Name: Curry Corner
- Cuisine: Japanese
  Restaurant Name: Curry Corner
<start>
Restaurant Name: Vegan Delight | Cuisine: Mexican
Restaurant Name: Burger Haven | Cuisine: American
Restaurant Name: Pizza Planet | Cuisine: Italian
Restaurant Name: Pizza Planet | Cuisine: French
Restaurant Name: Curry Corner | Cuisine: Mexican
Restaurant Name: Curry Corner | Cuisine: Japanese
<end>Here's some json data, can you convert it to MARKDOWN?
[
    {
        "Trip Name": "Valley Voyage",
        "End Location": "Denver",
        "Distance (miles)": 1665.7,
        "Fuel Used (gallons)": 58.2
    },
    {
        "Trip Name": "Mountain Adventure",
        "End Location": "Los Angeles",
        "Distance (miles)": 451.7,
        "Fuel Used (gallons)": 52.3
    },
    {
        "Trip Name": "Canyon Trek",
        "End Location": "Miami",
        "Distance (miles)": 2610.9,
        "Fuel Used (gallons)": 40.2
    },
    {
        "Trip Name": "City Explorer",
        "End Location": "Los Angeles",
        "Distance (miles)": 2877.8,
        "Fuel Used (gallons)": 20.3
    },
    {
        "Trip Name": "Lakeside Retreat",
        "End Location": "Miami",
        "Distance (miles)": 1962.7,
        "Fuel Used (gallons)": 75.7
    },
    {
        "Trip Name": "Lakeside Retreat",
        "End Location": "Los Angeles",
        "Distance (miles)": 1731.2,
        "Fuel Used (gallons)": 58.9
    },
    {
        "Trip Name": "Desert Drive",
        "End Location": "New York",
        "Distance (miles)": 976.8,
        "Fuel Used (gallons)": 55.9
    },
    {
        "Trip Name": "Historic Route",
        "End Location": "Miami",
        "Distance (miles)": 601.2,
        "Fuel Used (gallons)": 50.8
    },
    {
        "Trip Name": "Historic Route",
        "End Location": "Miami",
        "Distance (miles)": 2119.4,
        "Fuel Used (gallons)": 87.4
    },
    {
        "Trip Name": "Forest Journey",
        "End Location": "Phoenix",
        "Distance (miles)": 1449.5,
        "Fuel Used (gallons)": 40.2
    }
]<start>
| Trip Name | End Location | Distance (miles) | Fuel Used (gallons) |
| --- | --- | --- | --- |
| Valley Voyage | Denver | 1665.7 | 58.2 |
| Mountain Adventure | Los Angeles | 451.7 | 52.3 |
| Canyon Trek | Miami | 2610.9 | 40.2 |
| City Explorer | Los Angeles | 2877.8 | 20.3 |
| Lakeside Retreat | Miami | 1962.7 | 75.7 |
| Lakeside Retreat | Los Angeles | 1731.2 | 58.9 |
| Desert Drive | New York | 976.8 | 55.9 |
| Historic Route | Miami | 601.2 | 50.8 |
| Historic Route | Miami | 2119.4 | 87.4 |
| Forest Journey | Phoenix | 1449.5 | 40.2 |
<end>Can you change this Plain text into Csv?
Restaurant Name: Taco Town | Cuisine: Japanese | Location: Houston
Restaurant Name: Taco Town | Cuisine: Italian | Location: Chicago
Restaurant Name: BBQ Barn | Cuisine: Chinese | Location: Chicago
Restaurant Name: Pizza Planet | Cuisine: Mediterranean | Location: New York
Restaurant Name: Vegan Delight | Cuisine: Chinese | Location: Los Angeles
Restaurant Name: The Golden Spoon | Cuisine: Chinese | Location: Los Angeles
Restaurant Name: Burger Haven | Cuisine: French | Location: Los Angeles
Restaurant Name: Pasta Palace | Cuisine: American | Location: New York
Restaurant Name: The Steakhouse | Cuisine: Italian | Location: Chicago
Restaurant Name: The Steakhouse | Cuisine: American | Location: Phoenix
<start>
Restaurant Name,Cuisine,Location
Taco Town,Japanese,Houston
Taco Town,Italian,Chicago
BBQ Barn,Chinese,Chicago
Pizza Planet,Mediterranean,New York
Vegan Delight,Chinese,Los Angeles
The Golden Spoon,Chinese,Los Angeles
Burger Haven,French,Los Angeles
Pasta Palace,American,New York
The Steakhouse,Italian,Chicago
The Steakhouse,American,Phoenix
<end>Transform this plain text structure to a yml format:
Trip Name: City Explorer | Start Location: Chicago | Distance (miles): 780.2 | Duration (hours): 11.6
Trip Name: Lakeside Retreat | Start Location: Houston | Distance (miles): 2106.6 | Duration (hours): 51.1
Trip Name: Highway Odyssey | Start Location: Denver | Distance (miles): 1952.7 | Duration (hours): 59.7
<start>
- Distance (miles): 780.2
  Duration (hours): 11.6
  Start Location: Chicago
  Trip Name: City Explorer
- Distance (miles): 2106.6
  Duration (hours): 51.1
  Start Location: Houston
  Trip Name: Lakeside Retreat
- Distance (miles): 1952.7
  Duration (hours): 59.7
  Start Location: Denver
  Trip Name: Highway Odyssey
<end>Please transform the following Yaml data into PLAIN TEXT:
- Birth Month: June
  City: New York
  Income: 35000
- Birth Month: July
  City: Louisville
  Income: 440000
- Birth Month: October
  City: Jacksonville
  Income: 485000
- Birth Month: May
  City: Nashville
  Income: 495000
- Birth Month: August
  City: San Antonio
  Income: 230000
<start>
Birth Month: June | City: New York | Income: 35000
Birth Month: July | City: Louisville | Income: 440000
Birth Month: October | City: Jacksonville | Income: 485000
Birth Month: May | City: Nashville | Income: 495000
Birth Month: August | City: San Antonio | Income: 230000
<end>Convert this csv to yaml:
Restaurant Name,Cuisine,Location,Price Range
Taco Town,Japanese,Seattle,$$
Taco Town,Mediterranean,Houston,$$
Taco Town,Italian,Los Angeles,$$
<start>
- Cuisine: Japanese
  Location: Seattle
  Price Range: $$
  Restaurant Name: Taco Town
- Cuisine: Mediterranean
  Location: Houston
  Price Range: $$
  Restaurant Name: Taco Town
- Cuisine: Italian
  Location: Los Angeles
  Price Range: $$
  Restaurant Name: Taco Town
<end>Transform this Plain text structure to a Csv format:
Product Name: Device | SKU: SKU-1014 | Stock Quantity: 189 | Category: Toys | Supplier Name: ACME Corp
Product Name: Whatchamacallit | SKU: SKU-1013 | Stock Quantity: 159 | Category: Automotive | Supplier Name: Wonka Industries
Product Name: Contraption | SKU: SKU-1066 | Stock Quantity: 46 | Category: Electronics | Supplier Name: Umbrella Corp
Product Name: Widget | SKU: SKU-1020 | Stock Quantity: 201 | Category: Sports | Supplier Name: Globex
<start>
Product Name,SKU,Stock Quantity,Category,Supplier Name
Device,SKU-1014,189,Toys,ACME Corp
Whatchamacallit,SKU-1013,159,Automotive,Wonka Industries
Contraption,SKU-1066,46,Electronics,Umbrella Corp
Widget,SKU-1020,201,Sports,Globex
<end>Here's some JSON data, can you convert it to YAML?
[
    {
        "Database Name": "AnalyticsDB",
        "Queries per Second": 3111.69,
        "Average Latency (ms)": 6.5,
        "Timestamp": "2022-05-26 06:56:29"
    },
    {
        "Database Name": "OrdersDB",
        "Queries per Second": 2320.7,
        "Average Latency (ms)": 26.32,
        "Timestamp": "2022-02-03 12:10:53"
    },
    {
        "Database Name": "AnalyticsDB",
        "Queries per Second": 934.44,
        "Average Latency (ms)": 98.12,
        "Timestamp": "2022-12-05 23:59:31"
    }
]<start>
- Average Latency (ms): 6.5
  Database Name: AnalyticsDB
  Queries per Second: 3111.69
  Timestamp: '2022-05-26 06:56:29'
- Average Latency (ms): 26.32
  Database Name: OrdersDB
  Queries per Second: 2320.7
  Timestamp: '2022-02-03 12:10:53'
- Average Latency (ms): 98.12
  Database Name: AnalyticsDB
  Queries per Second: 934.44
  Timestamp: '2022-12-05 23:59:31'
<end>Convert this plain text to yml:
Location: Chicago | Condition: Stormy | Humidity (%): 28 | Wind Speed (km/h): 8.6
Location: Phoenix | Condition: Foggy | Humidity (%): 81 | Wind Speed (km/h): 28.1
Location: Seattle | Condition: Windy | Humidity (%): 78 | Wind Speed (km/h): 20.3
Location: Los Angeles | Condition: Stormy | Humidity (%): 31 | Wind Speed (km/h): 4.5
Location: Denver | Condition: Stormy | Humidity (%): 53 | Wind Speed (km/h): 16.6
Location: Phoenix | Condition: Windy | Humidity (%): 50 | Wind Speed (km/h): 5.4
<start>
- Condition: Stormy
  Humidity (%): 28
  Location: Chicago
  Wind Speed (km/h): 8.6
- Condition: Foggy
  Humidity (%): 81
  Location: Phoenix
  Wind Speed (km/h): 28.1
- Condition: Windy
  Humidity (%): 78
  Location: Seattle
  Wind Speed (km/h): 20.3
- Condition: Stormy
  Humidity (%): 31
  Location: Los Angeles
  Wind Speed (km/h): 4.5
- Condition: Stormy
  Humidity (%): 53
  Location: Denver
  Wind Speed (km/h): 16.6
- Condition: Windy
  Humidity (%): 50
  Location: Phoenix
  Wind Speed (km/h): 5.4
<end>Can you change this Json into Markdown?
[
    {
        "Company": "GlobalTrade",
        "Sector": "Aerospace",
        "Market Cap": "Large Cap",
        "Stock Price": 902.0,
        "Annual Revenue (B)": 408.13
    },
    {
        "Company": "BioPharm",
        "Sector": "Biotech",
        "Market Cap": "Large Cap",
        "Stock Price": 425.95,
        "Annual Revenue (B)": 141.7
    },
    {
        "Company": "AeroSpace",
        "Sector": "Finance",
        "Market Cap": "Large Cap",
        "Stock Price": 277.45,
        "Annual Revenue (B)": 303.53
    },
    {
        "Company": "HealthPlus",
        "Sector": "Biotech",
        "Market Cap": "Mega Cap",
        "Stock Price": 772.1,
        "Annual Revenue (B)": 168.75
    },
    {
        "Company": "RetailHub",
        "Sector": "Automotive",
        "Market Cap": "Large Cap",
        "Stock Price": 360.76,
        "Annual Revenue (B)": 201.99
    },
    {
        "Company": "FinanceWorks",
        "Sector": "Technology",
        "Market Cap": "Large Cap",
        "Stock Price": 276.92,
        "Annual Revenue (B)": 204.05
    },
    {
        "Company": "RetailHub",
        "Sector": "Biotech",
        "Market Cap": "Mid Cap",
        "Stock Price": 276.92,
        "Annual Revenue (B)": 214.94
    }
]<start>
| Company | Sector | Market Cap | Stock Price | Annual Revenue (B) |
| --- | --- | --- | --- | --- |
| GlobalTrade | Aerospace | Large Cap | 902.0 | 408.13 |
| BioPharm | Biotech | Large Cap | 425.95 | 141.7 |
| AeroSpace | Finance | Large Cap | 277.45 | 303.53 |
| HealthPlus | Biotech | Mega Cap | 772.1 | 168.75 |
| RetailHub | Automotive | Large Cap | 360.76 | 201.99 |
| FinanceWorks | Technology | Large Cap | 276.92 | 204.05 |
| RetailHub | Biotech | Mid Cap | 276.92 | 214.94 |
<end>Here's some CSV data, can you convert it to JSON?
Location,Condition,Temperature (C),Humidity (%),Wind Speed (km/h),Day
Los Angeles,Windy,12.4,40,12.3,Friday
Chicago,Cloudy,32.5,97,23.6,Thursday
Miami,Stormy,31.9,82,26.2,Tuesday
Phoenix,Sunny,23.0,93,12.4,Monday
Seattle,Sunny,32.5,45,26.3,Sunday
Seattle,Foggy,9.1,22,25.7,Wednesday
Chicago,Windy,14.9,80,25.7,Monday
<start>
[
    {
        "Location": "Los Angeles",
        "Condition": "Windy",
        "Temperature (C)": 12.4,
        "Humidity (%)": 40,
        "Wind Speed (km/h)": 12.3,
        "Day": "Friday"
    },
    {
        "Location": "Chicago",
        "Condition": "Cloudy",
        "Temperature (C)": 32.5,
        "Humidity (%)": 97,
        "Wind Speed (km/h)": 23.6,
        "Day": "Thursday"
    },
    {
        "Location": "Miami",
        "Condition": "Stormy",
        "Temperature (C)": 31.9,
        "Humidity (%)": 82,
        "Wind Speed (km/h)": 26.2,
        "Day": "Tuesday"
    },
    {
        "Location": "Phoenix",
        "Condition": "Sunny",
        "Temperature (C)": 23.0,
        "Humidity (%)": 93,
        "Wind Speed (km/h)": 12.4,
        "Day": "Monday"
    },
    {
        "Location": "Seattle",
        "Condition": "Sunny",
        "Temperature (C)": 32.5,
        "Humidity (%)": 45,
        "Wind Speed (km/h)": 26.3,
        "Day": "Sunday"
    },
    {
        "Location": "Seattle",
        "Condition": "Foggy",
        "Temperature (C)": 9.1,
        "Humidity (%)": 22,
        "Wind Speed (km/h)": 25.7,
        "Day": "Wednesday"
    },
    {
        "Location": "Chicago",
        "Condition": "Windy",
        "Temperature (C)": 14.9,
        "Humidity (%)": 80,
        "Wind Speed (km/h)": 25.7,
        "Day": "Monday"
    }
]
<end>Can you change this plain text into yaml?
Cache Hit Ratio (%): 89.81 | Connection Count: 327 | Average Latency (ms): 63.4
Cache Hit Ratio (%): 98.22 | Connection Count: 367 | Average Latency (ms): 99.9
Cache Hit Ratio (%): 70.77 | Connection Count: 234 | Average Latency (ms): 44.82
Cache Hit Ratio (%): 90.42 | Connection Count: 470 | Average Latency (ms): 76.92
Cache Hit Ratio (%): 78.35 | Connection Count: 301 | Average Latency (ms): 24.42
<start>
- Average Latency (ms): 63.4
  Cache Hit Ratio (%): 89.81
  Connection Count: 327
- Average Latency (ms): 99.9
  Cache Hit Ratio (%): 98.22
  Connection Count: 367
- Average Latency (ms): 44.82
  Cache Hit Ratio (%): 70.77
  Connection Count: 234
- Average Latency (ms): 76.92
  Cache Hit Ratio (%): 90.42
  Connection Count: 470
- Average Latency (ms): 24.42
  Cache Hit Ratio (%): 78.35
  Connection Count: 301
<end>Here's some json data, can you convert it to Plain text?
[
    {
        "Title": "Starbound Odyssey",
        "Director": "Rylan Frostblade",
        "Genre": "Fantasy",
        "Release Year": 2013,
        "Box Office Earnings (M)": 868.3
    },
    {
        "Title": "Dreamwalker",
        "Director": "Orin Shadowalker",
        "Genre": "Drama",
        "Release Year": 1990,
        "Box Office Earnings (M)": 340.81
    },
    {
        "Title": "Rise of the Titans",
        "Director": "Drake Nightshade",
        "Genre": "Horror",
        "Release Year": 2012,
        "Box Office Earnings (M)": 240.07
    },
    {
        "Title": "Mystery of the Depths",
        "Director": "Mara Moonshadow",
        "Genre": "Drama",
        "Release Year": 1980,
        "Box Office Earnings (M)": 434.57
    },
    {
        "Title": "Rise of the Titans",
        "Director": "Talon Blackthorn",
        "Genre": "Sci-Fi",
        "Release Year": 1981,
        "Box Office Earnings (M)": 359.66
    },
    {
        "Title": "Edge of Infinity",
        "Director": "Orin Shadowalker",
        "Genre": "Adventure",
        "Release Year": 1986,
        "Box Office Earnings (M)": 187.01
    },
    {
        "Title": "Edge of Infinity",
        "Director": "Selene Darkwhisper",
        "Genre": "Adventure",
        "Release Year": 2010,
        "Box Office Earnings (M)": 727.84
    },
    {
        "Title": "The Endless Horizon",
        "Director": "Zara Stormrider",
        "Genre": "Adventure",
        "Release Year": 1995,
        "Box Office Earnings (M)": 689.3
    },
    {
        "Title": "Starbound Odyssey",
        "Director": "Zara Stormrider",
        "Genre": "Fantasy",
        "Release Year": 2004,
        "Box Office Earnings (M)": 906.98
    },
    {
        "Title": "The Final Voyage",
        "Director": "Drake Nightshade",
        "Genre": "Thriller",
        "Release Year": 1977,
        "Box Office Earnings (M)": 11.63
    }
]<start>
Title: Starbound Odyssey | Director: Rylan Frostblade | Genre: Fantasy | Release Year: 2013 | Box Office Earnings (M): 868.3
Title: Dreamwalker | Director: Orin Shadowalker | Genre: Drama | Release Year: 1990 | Box Office Earnings (M): 340.81
Title: Rise of the Titans | Director: Drake Nightshade | Genre: Horror | Release Year: 2012 | Box Office Earnings (M): 240.07
Title: Mystery of the Depths | Director: Mara Moonshadow | Genre: Drama | Release Year: 1980 | Box Office Earnings (M): 434.57
Title: Rise of the Titans | Director: Talon Blackthorn | Genre: Sci-Fi | Release Year: 1981 | Box Office Earnings (M): 359.66
Title: Edge of Infinity | Director: Orin Shadowalker | Genre: Adventure | Release Year: 1986 | Box Office Earnings (M): 187.01
Title: Edge of Infinity | Director: Selene Darkwhisper | Genre: Adventure | Release Year: 2010 | Box Office Earnings (M): 727.84
Title: The Endless Horizon | Director: Zara Stormrider | Genre: Adventure | Release Year: 1995 | Box Office Earnings (M): 689.3
Title: Starbound Odyssey | Director: Zara Stormrider | Genre: Fantasy | Release Year: 2004 | Box Office Earnings (M): 906.98
Title: The Final Voyage | Director: Drake Nightshade | Genre: Thriller | Release Year: 1977 | Box Office Earnings (M): 11.63
<end>Transform this json structure to a MARKDOWN format:
[
    {
        "Company": "AeroSpace",
        "Sector": "Biotech",
        "Market Cap": "Large Cap",
        "Stock Price": 518.77,
        "Annual Revenue (B)": 322.66,
        "Quarter": "Q1"
    },
    {
        "Company": "EcoEnergy",
        "Sector": "Biotech",
        "Market Cap": "Small Cap",
        "Stock Price": 461.39,
        "Annual Revenue (B)": 282.68,
        "Quarter": "Q2"
    },
    {
        "Company": "HealthPlus",
        "Sector": "Automotive",
        "Market Cap": "Large Cap",
        "Stock Price": 798.8,
        "Annual Revenue (B)": 58.42,
        "Quarter": "Q1"
    },
    {
        "Company": "EcoEnergy",
        "Sector": "Biotech",
        "Market Cap": "Mega Cap",
        "Stock Price": 835.01,
        "Annual Revenue (B)": 337.49,
        "Quarter": "Q2"
    },
    {
        "Company": "BioPharm",
        "Sector": "Energy",
        "Market Cap": "Small Cap",
        "Stock Price": 502.98,
        "Annual Revenue (B)": 331.26,
        "Quarter": "Q1"
    },
    {
        "Company": "HealthPlus",
        "Sector": "Automotive",
        "Market Cap": "Small Cap",
        "Stock Price": 705.93,
        "Annual Revenue (B)": 454.37,
        "Quarter": "Q3"
    },
    {
        "Company": "TechCorp",
        "Sector": "Technology",
        "Market Cap": "Small Cap",
        "Stock Price": 378.07,
        "Annual Revenue (B)": 105.09,
        "Quarter": "Q2"
    },
    {
        "Company": "RetailHub",
        "Sector": "Finance",
        "Market Cap": "Small Cap",
        "Stock Price": 913.24,
        "Annual Revenue (B)": 147.13,
        "Quarter": "Q1"
    }
]<start>
| Company | Sector | Market Cap | Stock Price | Annual Revenue (B) | Quarter |
| --- | --- | --- | --- | --- | --- |
| AeroSpace | Biotech | Large Cap | 518.77 | 322.66 | Q1 |
| EcoEnergy | Biotech | Small Cap | 461.39 | 282.68 | Q2 |
| HealthPlus | Automotive | Large Cap | 798.8 | 58.42 | Q1 |
| EcoEnergy | Biotech | Mega Cap | 835.01 | 337.49 | Q2 |
| BioPharm | Energy | Small Cap | 502.98 | 331.26 | Q1 |
| HealthPlus | Automotive | Small Cap | 705.93 | 454.37 | Q3 |
| TechCorp | Technology | Small Cap | 378.07 | 105.09 | Q2 |
| RetailHub | Finance | Small Cap | 913.24 | 147.13 | Q1 |
<end>Can you change this csv into MARKDOWN?
Sector,Market Cap,Stock Price,Quarter
Finance,Mega Cap,75.62,Q3
Retail,Large Cap,427.93,Q1
Energy,Mega Cap,657.6,Q2
Aerospace,Small Cap,464.06,Q4
Automotive,Mid Cap,656.86,Q2
Energy,Mid Cap,588.03,Q4
Biotech,Small Cap,466.74,Q2
Aerospace,Mega Cap,166.42,Q4
Aerospace,Small Cap,75.62,Q2
<start>
| Sector | Market Cap | Stock Price | Quarter |
| --- | --- | --- | --- |
| Finance | Mega Cap | 75.62 | Q3 |
| Retail | Large Cap | 427.93 | Q1 |
| Energy | Mega Cap | 657.6 | Q2 |
| Aerospace | Small Cap | 464.06 | Q4 |
| Automotive | Mid Cap | 656.86 | Q2 |
| Energy | Mid Cap | 588.03 | Q4 |
| Biotech | Small Cap | 466.74 | Q2 |
| Aerospace | Mega Cap | 166.42 | Q4 |
| Aerospace | Small Cap | 75.62 | Q2 |
<end>Here's some plain text data, can you convert it to yaml?
SKU: SKU-1088 | Price: 419.43 | Stock Quantity: 182 | Category: Automotive | Supplier Name: Wonka Industries
SKU: SKU-1034 | Price: 69.26 | Stock Quantity: 406 | Category: Automotive | Supplier Name: Umbrella Corp
SKU: SKU-1021 | Price: 178.75 | Stock Quantity: 114 | Category: Electronics | Supplier Name: Wonka Industries
SKU: SKU-1074 | Price: 355.63 | Stock Quantity: 399 | Category: Electronics | Supplier Name: Globex
SKU: SKU-1082 | Price: 88.36 | Stock Quantity: 429 | Category: Household | Supplier Name: ACME Corp
SKU: SKU-1008 | Price: 482.81 | Stock Quantity: 499 | Category: Toys | Supplier Name: Wayne Enterprises
SKU: SKU-1017 | Price: 125.85 | Stock Quantity: 132 | Category: Sports | Supplier Name: ACME Corp
<start>
- Category: Automotive
  Price: 419.43
  SKU: SKU-1088
  Stock Quantity: 182
  Supplier Name: Wonka Industries
- Category: Automotive
  Price: 69.26
  SKU: SKU-1034
  Stock Quantity: 406
  Supplier Name: Umbrella Corp
- Category: Electronics
  Price: 178.75
  SKU: SKU-1021
  Stock Quantity: 114
  Supplier Name: Wonka Industries
- Category: Electronics
  Price: 355.63
  SKU: SKU-1074
  Stock Quantity: 399
  Supplier Name: Globex
- Category: Household
  Price: 88.36
  SKU: SKU-1082
  Stock Quantity: 429
  Supplier Name: ACME Corp
- Category: Toys
  Price: 482.81
  SKU: SKU-1008
  Stock Quantity: 499
  Supplier Name: Wayne Enterprises
- Category: Sports
  Price: 125.85
  SKU: SKU-1017
  Stock Quantity: 132
  Supplier Name: ACME Corp
<end>Please transform the following Json data into csv:
[
    {
        "Product Name": "Doohickey",
        "SKU": "SKU-1070",
        "Stock Quantity": 59,
        "Category": "Household",
        "Supplier Name": "Globex"
    },
    {
        "Product Name": "Thingamajig",
        "SKU": "SKU-1007",
        "Stock Quantity": 226,
        "Category": "Toys",
        "Supplier Name": "Globex"
    },
    {
        "Product Name": "Thingamajig",
        "SKU": "SKU-1049",
        "Stock Quantity": 456,
        "Category": "Sports",
        "Supplier Name": "Umbrella Corp"
    },
    {
        "Product Name": "Widget",
        "SKU": "SKU-1000",
        "Stock Quantity": 500,
        "Category": "Automotive",
        "Supplier Name": "Globex"
    },
    {
        "Product Name": "Whatchamacallit",
        "SKU": "SKU-1025",
        "Stock Quantity": 132,
        "Category": "Automotive",
        "Supplier Name": "Globex"
    },
    {
        "Product Name": "Widget",
        "SKU": "SKU-1048",
        "Stock Quantity": 5,
        "Category": "Automotive",
        "Supplier Name": "ACME Corp"
    },
    {
        "Product Name": "Contraption",
        "SKU": "SKU-1024",
        "Stock Quantity": 9,
        "Category": "Sports",
        "Supplier Name": "Umbrella Corp"
    }
]<start>
Product Name,SKU,Stock Quantity,Category,Supplier Name
Doohickey,SKU-1070,59,Household,Globex
Thingamajig,SKU-1007,226,Toys,Globex
Thingamajig,SKU-1049,456,Sports,Umbrella Corp
Widget,SKU-1000,500,Automotive,Globex
Whatchamacallit,SKU-1025,132,Automotive,Globex
Widget,SKU-1048,5,Automotive,ACME Corp
Contraption,SKU-1024,9,Sports,Umbrella Corp
<end>Please transform the following YML data into csv:
- Annual Revenue (B): 362.73
  Company: FinanceWorks
  Market Cap: Mega Cap
  Quarter: Q1
- Annual Revenue (B): 320.91
  Company: GlobalTrade
  Market Cap: Mega Cap
  Quarter: Q2
- Annual Revenue (B): 419.33
  Company: HealthPlus
  Market Cap: Mega Cap
  Quarter: Q4
- Annual Revenue (B): 388.19
  Company: FinanceWorks
  Market Cap: Small Cap
  Quarter: Q3
- Annual Revenue (B): 449.18
  Company: RetailHub
  Market Cap: Large Cap
  Quarter: Q3
- Annual Revenue (B): 357.36
  Company: TechCorp
  Market Cap: Mid Cap
  Quarter: Q2
- Annual Revenue (B): 107.99
  Company: Foodies
  Market Cap: Mid Cap
  Quarter: Q3
- Annual Revenue (B): 93.27
  Company: RetailHub
  Market Cap: Large Cap
  Quarter: Q4
- Annual Revenue (B): 395.3
  Company: HealthPlus
  Market Cap: Small Cap
  Quarter: Q2
<start>
Company,Market Cap,Annual Revenue (B),Quarter
FinanceWorks,Mega Cap,362.73,Q1
GlobalTrade,Mega Cap,320.91,Q2
HealthPlus,Mega Cap,419.33,Q4
FinanceWorks,Small Cap,388.19,Q3
RetailHub,Large Cap,449.18,Q3
TechCorp,Mid Cap,357.36,Q2
Foodies,Mid Cap,107.99,Q3
RetailHub,Large Cap,93.27,Q4
HealthPlus,Small Cap,395.3,Q2
<end>Can you change this markdown into Csv?
| Company | Sector | Market Cap | Stock Price | Annual Revenue (B) |
| --- | --- | --- | --- | --- |
| AutoDrive | Aerospace | Mega Cap | 167.57 | 362.54 |
| AeroSpace | Technology | Mega Cap | 271.43 | 205.67 |
| TechCorp | Energy | Mid Cap | 978.41 | 377.61 |
| Foodies | Healthcare | Small Cap | 171.2 | 50.86 |
| AeroSpace | Finance | Mega Cap | 857.81 | 172.43 |
| AutoDrive | Finance | Large Cap | 525.24 | 414.43 |
| AutoDrive | Energy | Mega Cap | 852.54 | 205.67 |<start>
Company,Sector,Market Cap,Stock Price,Annual Revenue (B)
AutoDrive,Aerospace,Mega Cap,167.57,362.54
AeroSpace,Technology,Mega Cap,271.43,205.67
TechCorp,Energy,Mid Cap,978.41,377.61
Foodies,Healthcare,Small Cap,171.2,50.86
AeroSpace,Finance,Mega Cap,857.81,172.43
AutoDrive,Finance,Large Cap,525.24,414.43
AutoDrive,Energy,Mega Cap,852.54,205.67
<end>Here's some CSV data, can you convert it to PLAIN TEXT?
Name,Age,Birth Month,City,Income
Claudia,65,January,Dallas,405000
Camden,60,November,San Francisco,125000
Alma,43,April,Austin,445000
Sophie,68,May,Columbus,55000
Pam,31,January,Los Angeles,150000
Tonya,27,October,New York,415000
<start>
Name: Claudia | Age: 65 | Birth Month: January | City: Dallas | Income: 405000
Name: Camden | Age: 60 | Birth Month: November | City: San Francisco | Income: 125000
Name: Alma | Age: 43 | Birth Month: April | City: Austin | Income: 445000
Name: Sophie | Age: 68 | Birth Month: May | City: Columbus | Income: 55000
Name: Pam | Age: 31 | Birth Month: January | City: Los Angeles | Income: 150000
Name: Tonya | Age: 27 | Birth Month: October | City: New York | Income: 415000
<end>Please transform the following markdown data into Csv:
| Company | Annual Revenue (B) | Quarter |
| --- | --- | --- |
| AeroSpace | 310.42 | Q4 |
| AutoDrive | 306.31 | Q4 |
| AeroSpace | 303.86 | Q4 |
| EcoEnergy | 377.01 | Q1 |
| Foodies | 302.93 | Q2 |
| AutoDrive | 319.45 | Q1 |
| HealthPlus | 490.51 | Q2 |<start>
Company,Annual Revenue (B),Quarter
AeroSpace,310.42,Q4
AutoDrive,306.31,Q4
AeroSpace,303.86,Q4
EcoEnergy,377.01,Q1
Foodies,302.93,Q2
AutoDrive,319.45,Q1
HealthPlus,490.51,Q2
<end>Transform this Yaml structure to a Plain text format:
- Age: 61
  Income: 295000
- Age: 46
  Income: 305000
- Age: 29
  Income: 465000
- Age: 53
  Income: 305000
<start>
Age: 61 | Income: 295000
Age: 46 | Income: 305000
Age: 29 | Income: 465000
Age: 53 | Income: 305000
<end>Here's some plain text data, can you convert it to MARKDOWN?
Location: Garden | Battery Level (%): 14.0 | Reading Value: 43.08 | Timestamp: 2021-07-01 15:50:10
Location: Hallway | Battery Level (%): 64.0 | Reading Value: 71.39 | Timestamp: 2021-03-04 06:24:37
Location: Garden | Battery Level (%): 55.5 | Reading Value: 33.55 | Timestamp: 2022-08-03 06:53:39
Location: Bathroom | Battery Level (%): 51.4 | Reading Value: -16.5 | Timestamp: 2023-04-07 04:34:48
<start>
| Location | Battery Level (%) | Reading Value | Timestamp |
| --- | --- | --- | --- |
| Garden | 14.0 | 43.08 | 2021-07-01 15:50:10 |
| Hallway | 64.0 | 71.39 | 2021-03-04 06:24:37 |
| Garden | 55.5 | 33.55 | 2022-08-03 06:53:39 |
| Bathroom | 51.4 | -16.5 | 2023-04-07 04:34:48 |
<end>Convert this yaml to PLAIN TEXT:
- Cuisine: Japanese
  Location: Phoenix
  Price Range: $$
  Restaurant Name: Curry Corner
- Cuisine: American
  Location: Los Angeles
  Price Range: $$$$
  Restaurant Name: Vegan Delight
- Cuisine: Italian
  Location: Chicago
  Price Range: $
  Restaurant Name: Pasta Palace
<start>
Restaurant Name: Curry Corner | Cuisine: Japanese | Location: Phoenix | Price Range: $$
Restaurant Name: Vegan Delight | Cuisine: American | Location: Los Angeles | Price Range: $$$$
Restaurant Name: Pasta Palace | Cuisine: Italian | Location: Chicago | Price Range: $
<end>Here's some plain text data, can you convert it to Markdown?
Title: The Great Expedition | Director: Selene Darkwhisper | Release Year: 1982
Title: Edge of Infinity | Director: Zara Stormrider | Release Year: 1970
Title: Mystery of the Depths | Director: Selene Darkwhisper | Release Year: 2016
<start>
| Title | Director | Release Year |
| --- | --- | --- |
| The Great Expedition | Selene Darkwhisper | 1982 |
| Edge of Infinity | Zara Stormrider | 1970 |
| Mystery of the Depths | Selene Darkwhisper | 2016 |
<end>Here's some csv data, can you convert it to Markdown?
Device ID,Device Type,Battery Level (%),Reading Value,Timestamp
device-0068,Humidity Sensor,68.7,27.31,2021-12-20 03:53:45
device-0040,Humidity Sensor,91.8,54.16,2023-12-07 07:29:39
device-0001,Temperature Sensor,21.5,75.83,2021-11-28 18:40:39
device-0010,Temperature Sensor,70.4,-32.7,2021-08-23 17:20:20
device-0055,Light Sensor,27.7,67.94,2021-07-16 04:14:48
device-0091,Temperature Sensor,92.0,-14.53,2021-08-12 13:16:05
device-0011,Light Sensor,86.8,27.72,2022-08-04 11:46:42
device-0010,Humidity Sensor,21.0,-12.9,2021-07-24 22:02:52
<start>
| Device ID | Device Type | Battery Level (%) | Reading Value | Timestamp |
| --- | --- | --- | --- | --- |
| device-0068 | Humidity Sensor | 68.7 | 27.31 | 2021-12-20 03:53:45 |
| device-0040 | Humidity Sensor | 91.8 | 54.16 | 2023-12-07 07:29:39 |
| device-0001 | Temperature Sensor | 21.5 | 75.83 | 2021-11-28 18:40:39 |
| device-0010 | Temperature Sensor | 70.4 | -32.7 | 2021-08-23 17:20:20 |
| device-0055 | Light Sensor | 27.7 | 67.94 | 2021-07-16 04:14:48 |
| device-0091 | Temperature Sensor | 92.0 | -14.53 | 2021-08-12 13:16:05 |
| device-0011 | Light Sensor | 86.8 | 27.72 | 2022-08-04 11:46:42 |
| device-0010 | Humidity Sensor | 21.0 | -12.9 | 2021-07-24 22:02:52 |
<end>Transform this plain text structure to a JSON format:
Temperature (C): 13.0 | Humidity (%): 87 | Wind Speed (km/h): 12.6
Temperature (C): 35.3 | Humidity (%): 64 | Wind Speed (km/h): 23.3
Temperature (C): 31.1 | Humidity (%): 46 | Wind Speed (km/h): 10.5
Temperature (C): 12.5 | Humidity (%): 24 | Wind Speed (km/h): 23.8
Temperature (C): 27.6 | Humidity (%): 27 | Wind Speed (km/h): 22.1
Temperature (C): 14.1 | Humidity (%): 79 | Wind Speed (km/h): 10.5
Temperature (C): 19.2 | Humidity (%): 79 | Wind Speed (km/h): 21.4
Temperature (C): 23.6 | Humidity (%): 24 | Wind Speed (km/h): 19.9
Temperature (C): 10.8 | Humidity (%): 59 | Wind Speed (km/h): 22.4
<start>
[
    {
        "Temperature (C)": 13.0,
        "Humidity (%)": 87,
        "Wind Speed (km/h)": 12.6
    },
    {
        "Temperature (C)": 35.3,
        "Humidity (%)": 64,
        "Wind Speed (km/h)": 23.3
    },
    {
        "Temperature (C)": 31.1,
        "Humidity (%)": 46,
        "Wind Speed (km/h)": 10.5
    },
    {
        "Temperature (C)": 12.5,
        "Humidity (%)": 24,
        "Wind Speed (km/h)": 23.8
    },
    {
        "Temperature (C)": 27.6,
        "Humidity (%)": 27,
        "Wind Speed (km/h)": 22.1
    },
    {
        "Temperature (C)": 14.1,
        "Humidity (%)": 79,
        "Wind Speed (km/h)": 10.5
    },
    {
        "Temperature (C)": 19.2,
        "Humidity (%)": 79,
        "Wind Speed (km/h)": 21.4
    },
    {
        "Temperature (C)": 23.6,
        "Humidity (%)": 24,
        "Wind Speed (km/h)": 19.9
    },
    {
        "Temperature (C)": 10.8,
        "Humidity (%)": 59,
        "Wind Speed (km/h)": 22.4
    }
]
<end>Convert this JSON to yml:
[
    {
        "Restaurant Name": "Pizza Planet",
        "Cuisine": "Chinese",
        "Location": "Los Angeles",
        "Rating": 1,
        "Price Range": "$$$$$"
    },
    {
        "Restaurant Name": "The Golden Spoon",
        "Cuisine": "American",
        "Location": "San Francisco",
        "Rating": 4,
        "Price Range": "$"
    },
    {
        "Restaurant Name": "Sushi World",
        "Cuisine": "Mediterranean",
        "Location": "New York",
        "Rating": 4,
        "Price Range": "$$"
    },
    {
        "Restaurant Name": "Pasta Palace",
        "Cuisine": "Japanese",
        "Location": "Seattle",
        "Rating": 1,
        "Price Range": "$$$"
    },
    {
        "Restaurant Name": "Vegan Delight",
        "Cuisine": "Indian",
        "Location": "San Francisco",
        "Rating": 2,
        "Price Range": "$$"
    }
]<start>
- Cuisine: Chinese
  Location: Los Angeles
  Price Range: $$$$$
  Rating: 1
  Restaurant Name: Pizza Planet
- Cuisine: American
  Location: San Francisco
  Price Range: $
  Rating: 4
  Restaurant Name: The Golden Spoon
- Cuisine: Mediterranean
  Location: New York
  Price Range: $$
  Rating: 4
  Restaurant Name: Sushi World
- Cuisine: Japanese
  Location: Seattle
  Price Range: $$$
  Rating: 1
  Restaurant Name: Pasta Palace
- Cuisine: Indian
  Location: San Francisco
  Price Range: $$
  Rating: 2
  Restaurant Name: Vegan Delight
<end>Convert this CSV to Json:
Director,Genre,Release Year,Box Office Earnings (M)
Mara Moonshadow,Comedy,2009,492.31
Lira Silverleaf,Thriller,1991,408.61
Zara Stormrider,Fantasy,1989,413.03
Drake Nightshade,Thriller,2022,518.14
<start>
[
    {
        "Director": "Mara Moonshadow",
        "Genre": "Comedy",
        "Release Year": 2009,
        "Box Office Earnings (M)": 492.31
    },
    {
        "Director": "Lira Silverleaf",
        "Genre": "Thriller",
        "Release Year": 1991,
        "Box Office Earnings (M)": 408.61
    },
    {
        "Director": "Zara Stormrider",
        "Genre": "Fantasy",
        "Release Year": 1989,
        "Box Office Earnings (M)": 413.03
    },
    {
        "Director": "Drake Nightshade",
        "Genre": "Thriller",
        "Release Year": 2022,
        "Box Office Earnings (M)": 518.14
    }
]
<end>Can you change this CSV into YML?
Database Name,Queries per Second,Connection Count,Average Latency (ms),Timestamp
SalesDB,1609.17,178,93.65,2022-03-10 22:25:37
ProfilesDB,2418.79,20,28.68,2023-05-22 07:35:58
OrdersDB,992.17,483,18.36,2023-07-26 15:50:41
OrdersDB,835.39,102,9.12,2022-10-07 22:26:24
ProductsDB,2549.46,495,35.84,2022-02-28 19:04:30
<start>
- Average Latency (ms): 93.65
  Connection Count: 178
  Database Name: SalesDB
  Queries per Second: 1609.17
  Timestamp: '2022-03-10 22:25:37'
- Average Latency (ms): 28.68
  Connection Count: 20
  Database Name: ProfilesDB
  Queries per Second: 2418.79
  Timestamp: '2023-05-22 07:35:58'
- Average Latency (ms): 18.36
  Connection Count: 483
  Database Name: OrdersDB
  Queries per Second: 992.17
  Timestamp: '2023-07-26 15:50:41'
- Average Latency (ms): 9.12
  Connection Count: 102
  Database Name: OrdersDB
  Queries per Second: 835.39
  Timestamp: '2022-10-07 22:26:24'
- Average Latency (ms): 35.84
  Connection Count: 495
  Database Name: ProductsDB
  Queries per Second: 2549.46
  Timestamp: '2022-02-28 19:04:30'
<end>Can you change this JSON into CSV?
[
    {
        "Database Name": "UserDB",
        "Queries per Second": 3811.8,
        "Timestamp": "2021-09-12 23:14:39"
    },
    {
        "Database Name": "AnalyticsDB",
        "Queries per Second": 1100.99,
        "Timestamp": "2021-04-02 09:35:57"
    },
    {
        "Database Name": "LogsDB",
        "Queries per Second": 2890.86,
        "Timestamp": "2022-05-27 13:13:11"
    },
    {
        "Database Name": "LogsDB",
        "Queries per Second": 1460.03,
        "Timestamp": "2023-07-13 16:48:03"
    },
    {
        "Database Name": "OrdersDB",
        "Queries per Second": 2046.56,
        "Timestamp": "2022-01-09 21:36:06"
    }
]<start>
Database Name,Queries per Second,Timestamp
UserDB,3811.8,2021-09-12 23:14:39
AnalyticsDB,1100.99,2021-04-02 09:35:57
LogsDB,2890.86,2022-05-27 13:13:11
LogsDB,1460.03,2023-07-13 16:48:03
OrdersDB,2046.56,2022-01-09 21:36:06
<end>Please transform the following csv data into markdown:
Product Name,Price,Stock Quantity
Whatchamacallit,282.22,254
Instrument,213.34,328
Instrument,200.61,431
Doohickey,146.59,119
Instrument,76.59,98
Contraption,170.85,251
Instrument,233.54,315
Whatchamacallit,139.35,400
<start>
| Product Name | Price | Stock Quantity |
| --- | --- | --- |
| Whatchamacallit | 282.22 | 254 |
| Instrument | 213.34 | 328 |
| Instrument | 200.61 | 431 |
| Doohickey | 146.59 | 119 |
| Instrument | 76.59 | 98 |
| Contraption | 170.85 | 251 |
| Instrument | 233.54 | 315 |
| Whatchamacallit | 139.35 | 400 |
<end>Convert this json to plain text:
[
    {
        "Company": "BioLife",
        "Date": "2021-12-17",
        "Open Price": 276.78,
        "Close Price": 934.02,
        "Low Price": 227.36,
        "Volume": 5396881
    },
    {
        "Company": "HealthGen",
        "Date": "2011-03-19",
        "Open Price": 595.23,
        "Close Price": 362.52,
        "Low Price": 362.52,
        "Volume": 6420880
    },
    {
        "Company": "GreenEnergy",
        "Date": "2014-06-17",
        "Open Price": 1384.38,
        "Close Price": 227.36,
        "Low Price": 227.36,
        "Volume": 2782818
    },
    {
        "Company": "MediaGroup",
        "Date": "2013-09-04",
        "Open Price": 641.51,
        "Close Price": 385.59,
        "Low Price": 192.38,
        "Volume": 9423586
    }
]<start>
Company: BioLife | Date: 2021-12-17 | Open Price: 276.78 | Close Price: 934.02 | Low Price: 227.36 | Volume: 5396881
Company: HealthGen | Date: 2011-03-19 | Open Price: 595.23 | Close Price: 362.52 | Low Price: 362.52 | Volume: 6420880
Company: GreenEnergy | Date: 2014-06-17 | Open Price: 1384.38 | Close Price: 227.36 | Low Price: 227.36 | Volume: 2782818
Company: MediaGroup | Date: 2013-09-04 | Open Price: 641.51 | Close Price: 385.59 | Low Price: 192.38 | Volume: 9423586
<end>Convert this plain text to csv:
Name: Alexandria | Birth Month: March | City: Baltimore | Income: 20000
Name: Sofia | Birth Month: July | City: Fort Worth | Income: 140000
Name: Lewis | Birth Month: March | City: Milwaukee | Income: 335000
Name: Kristine | Birth Month: July | City: El Paso | Income: 300000
Name: Courtney | Birth Month: June | City: Seattle | Income: 125000
Name: Irma | Birth Month: March | City: Los Angeles | Income: 105000
Name: Kristopher | Birth Month: July | City: El Paso | Income: 100000
Name: Leonard | Birth Month: May | City: Houston | Income: 455000
<start>
Name,Birth Month,City,Income
Alexandria,March,Baltimore,20000
Sofia,July,Fort Worth,140000
Lewis,March,Milwaukee,335000
Kristine,July,El Paso,300000
Courtney,June,Seattle,125000
Irma,March,Los Angeles,105000
Kristopher,July,El Paso,100000
Leonard,May,Houston,455000
<end>Transform this plain text structure to a JSON format:
Company: GlobalTrade | Stock Price: 390.16 | Quarter: Q2
Company: TechCorp | Stock Price: 453.91 | Quarter: Q2
Company: AeroSpace | Stock Price: 532.07 | Quarter: Q1
Company: HealthPlus | Stock Price: 868.31 | Quarter: Q2
Company: Foodies | Stock Price: 281.03 | Quarter: Q1
Company: HealthPlus | Stock Price: 904.4 | Quarter: Q4
Company: BioPharm | Stock Price: 792.7 | Quarter: Q2
Company: EcoEnergy | Stock Price: 974.19 | Quarter: Q4
Company: BioPharm | Stock Price: 456.15 | Quarter: Q2
<start>
[
    {
        "Company": "GlobalTrade",
        "Stock Price": 390.16,
        "Quarter": "Q2"
    },
    {
        "Company": "TechCorp",
        "Stock Price": 453.91,
        "Quarter": "Q2"
    },
    {
        "Company": "AeroSpace",
        "Stock Price": 532.07,
        "Quarter": "Q1"
    },
    {
        "Company": "HealthPlus",
        "Stock Price": 868.31,
        "Quarter": "Q2"
    },
    {
        "Company": "Foodies",
        "Stock Price": 281.03,
        "Quarter": "Q1"
    },
    {
        "Company": "HealthPlus",
        "Stock Price": 904.4,
        "Quarter": "Q4"
    },
    {
        "Company": "BioPharm",
        "Stock Price": 792.7,
        "Quarter": "Q2"
    },
    {
        "Company": "EcoEnergy",
        "Stock Price": 974.19,
        "Quarter": "Q4"
    },
    {
        "Company": "BioPharm",
        "Stock Price": 456.15,
        "Quarter": "Q2"
    }
]
<end>Please transform the following markdown data into csv:
| Sector | Annual Revenue (B) | Quarter |
| --- | --- | --- |
| Aerospace | 438.43 | Q3 |
| Healthcare | 266.77 | Q2 |
| Aerospace | 461.27 | Q4 |<start>
Sector,Annual Revenue (B),Quarter
Aerospace,438.43,Q3
Healthcare,266.77,Q2
Aerospace,461.27,Q4
<end>Can you change this Plain text into json?
Company: GlobalTrade | Sector: Biotech | Market Cap: Large Cap | Stock Price: 826.25 | Annual Revenue (B): 263.49 | Quarter: Q2
Company: GlobalTrade | Sector: Aerospace | Market Cap: Small Cap | Stock Price: 226.06 | Annual Revenue (B): 398.86 | Quarter: Q1
Company: Foodies | Sector: Retail | Market Cap: Small Cap | Stock Price: 658.59 | Annual Revenue (B): 111.09 | Quarter: Q3
Company: EcoEnergy | Sector: Finance | Market Cap: Mega Cap | Stock Price: 114.93 | Annual Revenue (B): 163.68 | Quarter: Q4
Company: AutoDrive | Sector: Technology | Market Cap: Mega Cap | Stock Price: 112.07 | Annual Revenue (B): 355.48 | Quarter: Q1
Company: BioPharm | Sector: Finance | Market Cap: Mega Cap | Stock Price: 954.16 | Annual Revenue (B): 163.68 | Quarter: Q1
Company: FinanceWorks | Sector: Retail | Market Cap: Small Cap | Stock Price: 939.97 | Annual Revenue (B): 344.27 | Quarter: Q2
Company: Foodies | Sector: Retail | Market Cap: Small Cap | Stock Price: 565.7 | Annual Revenue (B): 185.76 | Quarter: Q2
Company: FinanceWorks | Sector: Automotive | Market Cap: Mid Cap | Stock Price: 636.45 | Annual Revenue (B): 435.52 | Quarter: Q2
<start>
[
    {
        "Company": "GlobalTrade",
        "Sector": "Biotech",
        "Market Cap": "Large Cap",
        "Stock Price": 826.25,
        "Annual Revenue (B)": 263.49,
        "Quarter": "Q2"
    },
    {
        "Company": "GlobalTrade",
        "Sector": "Aerospace",
        "Market Cap": "Small Cap",
        "Stock Price": 226.06,
        "Annual Revenue (B)": 398.86,
        "Quarter": "Q1"
    },
    {
        "Company": "Foodies",
        "Sector": "Retail",
        "Market Cap": "Small Cap",
        "Stock Price": 658.59,
        "Annual Revenue (B)": 111.09,
        "Quarter": "Q3"
    },
    {
        "Company": "EcoEnergy",
        "Sector": "Finance",
        "Market Cap": "Mega Cap",
        "Stock Price": 114.93,
        "Annual Revenue (B)": 163.68,
        "Quarter": "Q4"
    },
    {
        "Company": "AutoDrive",
        "Sector": "Technology",
        "Market Cap": "Mega Cap",
        "Stock Price": 112.07,
        "Annual Revenue (B)": 355.48,
        "Quarter": "Q1"
    },
    {
        "Company": "BioPharm",
        "Sector": "Finance",
        "Market Cap": "Mega Cap",
        "Stock Price": 954.16,
        "Annual Revenue (B)": 163.68,
        "Quarter": "Q1"
    },
    {
        "Company": "FinanceWorks",
        "Sector": "Retail",
        "Market Cap": "Small Cap",
        "Stock Price": 939.97,
        "Annual Revenue (B)": 344.27,
        "Quarter": "Q2"
    },
    {
        "Company": "Foodies",
        "Sector": "Retail",
        "Market Cap": "Small Cap",
        "Stock Price": 565.7,
        "Annual Revenue (B)": 185.76,
        "Quarter": "Q2"
    },
    {
        "Company": "FinanceWorks",
        "Sector": "Automotive",
        "Market Cap": "Mid Cap",
        "Stock Price": 636.45,
        "Annual Revenue (B)": 435.52,
        "Quarter": "Q2"
    }
]
<end>Convert this json to csv:
[
    {
        "Restaurant Name": "Burger Haven",
        "Price Range": "$$$$"
    },
    {
        "Restaurant Name": "The Steakhouse",
        "Price Range": "$$$"
    },
    {
        "Restaurant Name": "The Steakhouse",
        "Price Range": "$$$"
    },
    {
        "Restaurant Name": "The Golden Spoon",
        "Price Range": "$$$$$"
    },
    {
        "Restaurant Name": "Curry Corner",
        "Price Range": "$$$$$"
    },
    {
        "Restaurant Name": "Pizza Planet",
        "Price Range": "$"
    },
    {
        "Restaurant Name": "The Golden Spoon",
        "Price Range": "$$$$$"
    },
    {
        "Restaurant Name": "Burger Haven",
        "Price Range": "$"
    },
    {
        "Restaurant Name": "Sushi World",
        "Price Range": "$"
    },
    {
        "Restaurant Name": "Pasta Palace",
        "Price Range": "$"
    }
]<start>
Restaurant Name,Price Range
Burger Haven,$$$$
The Steakhouse,$$$
The Steakhouse,$$$
The Golden Spoon,$$$$$
Curry Corner,$$$$$
Pizza Planet,$
The Golden Spoon,$$$$$
Burger Haven,$
Sushi World,$
Pasta Palace,$
<end>Please transform the following PLAIN TEXT data into Json:
Restaurant Name: Curry Corner | Cuisine: Mediterranean | Location: Phoenix | Price Range: $$$
Restaurant Name: Burger Haven | Cuisine: American | Location: Miami | Price Range: $$$$$
Restaurant Name: Taco Town | Cuisine: American | Location: San Francisco | Price Range: $$$$$
Restaurant Name: Burger Haven | Cuisine: Mediterranean | Location: Miami | Price Range: $$$$$
<start>
[
    {
        "Restaurant Name": "Curry Corner",
        "Cuisine": "Mediterranean",
        "Location": "Phoenix",
        "Price Range": "$$$"
    },
    {
        "Restaurant Name": "Burger Haven",
        "Cuisine": "American",
        "Location": "Miami",
        "Price Range": "$$$$$"
    },
    {
        "Restaurant Name": "Taco Town",
        "Cuisine": "American",
        "Location": "San Francisco",
        "Price Range": "$$$$$"
    },
    {
        "Restaurant Name": "Burger Haven",
        "Cuisine": "Mediterranean",
        "Location": "Miami",
        "Price Range": "$$$$$"
    }
]
<end>Can you change this plain text into JSON?
Cuisine: Mexican | Location: San Francisco
Cuisine: American | Location: San Francisco
Cuisine: American | Location: Los Angeles
Cuisine: Mexican | Location: San Francisco
Cuisine: Japanese | Location: New York
Cuisine: French | Location: Phoenix
<start>
[
    {
        "Cuisine": "Mexican",
        "Location": "San Francisco"
    },
    {
        "Cuisine": "American",
        "Location": "San Francisco"
    },
    {
        "Cuisine": "American",
        "Location": "Los Angeles"
    },
    {
        "Cuisine": "Mexican",
        "Location": "San Francisco"
    },
    {
        "Cuisine": "Japanese",
        "Location": "New York"
    },
    {
        "Cuisine": "French",
        "Location": "Phoenix"
    }
]
<end>Here's some JSON data, can you convert it to yaml?
[
    {
        "Database Name": "AnalyticsDB",
        "Queries per Second": 784.48,
        "Cache Hit Ratio (%)": 92.25,
        "Connection Count": 421,
        "Average Latency (ms)": 95.59,
        "Timestamp": "2022-09-25 17:22:48"
    },
    {
        "Database Name": "SalesDB",
        "Queries per Second": 263.63,
        "Cache Hit Ratio (%)": 88.46,
        "Connection Count": 472,
        "Average Latency (ms)": 65.41,
        "Timestamp": "2022-01-18 11:33:43"
    },
    {
        "Database Name": "OrdersDB",
        "Queries per Second": 1756.47,
        "Cache Hit Ratio (%)": 82.42,
        "Connection Count": 394,
        "Average Latency (ms)": 15.01,
        "Timestamp": "2023-05-04 20:47:27"
    },
    {
        "Database Name": "ProfilesDB",
        "Queries per Second": 1043.95,
        "Cache Hit Ratio (%)": 97.88,
        "Connection Count": 264,
        "Average Latency (ms)": 25.06,
        "Timestamp": "2023-05-17 15:51:04"
    },
    {
        "Database Name": "MetricsDB",
        "Queries per Second": 626.82,
        "Cache Hit Ratio (%)": 80.78,
        "Connection Count": 86,
        "Average Latency (ms)": 42.52,
        "Timestamp": "2021-11-03 22:10:56"
    },
    {
        "Database Name": "LogsDB",
        "Queries per Second": 2586.47,
        "Cache Hit Ratio (%)": 88.0,
        "Connection Count": 101,
        "Average Latency (ms)": 63.15,
        "Timestamp": "2022-03-27 20:59:18"
    },
    {
        "Database Name": "InventoryDB",
        "Queries per Second": 1526.04,
        "Cache Hit Ratio (%)": 76.84,
        "Connection Count": 282,
        "Average Latency (ms)": 14.74,
        "Timestamp": "2023-03-04 16:13:46"
    },
    {
        "Database Name": "MetricsDB",
        "Queries per Second": 1203.12,
        "Cache Hit Ratio (%)": 76.16,
        "Connection Count": 326,
        "Average Latency (ms)": 1.71,
        "Timestamp": "2021-02-09 16:38:50"
    },
    {
        "Database Name": "UserDB",
        "Queries per Second": 3613.73,
        "Cache Hit Ratio (%)": 85.16,
        "Connection Count": 332,
        "Average Latency (ms)": 91.02,
        "Timestamp": "2022-07-18 15:29:40"
    }
]<start>
- Average Latency (ms): 95.59
  Cache Hit Ratio (%): 92.25
  Connection Count: 421
  Database Name: AnalyticsDB
  Queries per Second: 784.48
  Timestamp: '2022-09-25 17:22:48'
- Average Latency (ms): 65.41
  Cache Hit Ratio (%): 88.46
  Connection Count: 472
  Database Name: SalesDB
  Queries per Second: 263.63
  Timestamp: '2022-01-18 11:33:43'
- Average Latency (ms): 15.01
  Cache Hit Ratio (%): 82.42
  Connection Count: 394
  Database Name: OrdersDB
  Queries per Second: 1756.47
  Timestamp: '2023-05-04 20:47:27'
- Average Latency (ms): 25.06
  Cache Hit Ratio (%): 97.88
  Connection Count: 264
  Database Name: ProfilesDB
  Queries per Second: 1043.95
  Timestamp: '2023-05-17 15:51:04'
- Average Latency (ms): 42.52
  Cache Hit Ratio (%): 80.78
  Connection Count: 86
  Database Name: MetricsDB
  Queries per Second: 626.82
  Timestamp: '2021-11-03 22:10:56'
- Average Latency (ms): 63.15
  Cache Hit Ratio (%): 88.0
  Connection Count: 101
  Database Name: LogsDB
  Queries per Second: 2586.47
  Timestamp: '2022-03-27 20:59:18'
- Average Latency (ms): 14.74
  Cache Hit Ratio (%): 76.84
  Connection Count: 282
  Database Name: InventoryDB
  Queries per Second: 1526.04
  Timestamp: '2023-03-04 16:13:46'
- Average Latency (ms): 1.71
  Cache Hit Ratio (%): 76.16
  Connection Count: 326
  Database Name: MetricsDB
  Queries per Second: 1203.12
  Timestamp: '2021-02-09 16:38:50'
- Average Latency (ms): 91.02
  Cache Hit Ratio (%): 85.16
  Connection Count: 332
  Database Name: UserDB
  Queries per Second: 3613.73
  Timestamp: '2022-07-18 15:29:40'
<end>Transform this CSV structure to a PLAIN TEXT format:
Title,Director,Genre,Release Year
The Endless Horizon,Talon Blackthorn,Adventure,2015
Mystery of the Depths,Rylan Frostblade,Horror,2015
Dreamwalker,Selene Darkwhisper,Action,1992
Edge of Infinity,Zara Stormrider,Thriller,1987
Dreamwalker,Orin Shadowalker,Sci-Fi,2005
<start>
Title: The Endless Horizon | Director: Talon Blackthorn | Genre: Adventure | Release Year: 2015
Title: Mystery of the Depths | Director: Rylan Frostblade | Genre: Horror | Release Year: 2015
Title: Dreamwalker | Director: Selene Darkwhisper | Genre: Action | Release Year: 1992
Title: Edge of Infinity | Director: Zara Stormrider | Genre: Thriller | Release Year: 1987
Title: Dreamwalker | Director: Orin Shadowalker | Genre: Sci-Fi | Release Year: 2005
<end>Transform this yaml structure to a Json format:
- Close Price: 810.56
  Company: AutoMotive
  Date: '2020-07-05'
  Low Price: 704.91
  Open Price: 704.91
  Volume: 1112689
- Close Price: 947.13
  Company: FoodChain
  Date: '2017-03-01'
  Low Price: 515.9
  Open Price: 515.9
  Volume: 7949146
- Close Price: 1440.06
  Company: GreenEnergy
  Date: '2020-11-27'
  Low Price: 232.35
  Open Price: 232.35
  Volume: 4154277
- Close Price: 1386.09
  Company: MediaGroup
  Date: '2022-09-22'
  Low Price: 809.54
  Open Price: 1414.98
  Volume: 9876038
- Close Price: 1418.92
  Company: FinanceTrust
  Date: '2011-05-10'
  Low Price: 232.35
  Open Price: 232.35
  Volume: 7104362
<start>
[
    {
        "Company": "AutoMotive",
        "Date": "2020-07-05",
        "Open Price": 704.91,
        "Close Price": 810.56,
        "Low Price": 704.91,
        "Volume": 1112689
    },
    {
        "Company": "FoodChain",
        "Date": "2017-03-01",
        "Open Price": 515.9,
        "Close Price": 947.13,
        "Low Price": 515.9,
        "Volume": 7949146
    },
    {
        "Company": "GreenEnergy",
        "Date": "2020-11-27",
        "Open Price": 232.35,
        "Close Price": 1440.06,
        "Low Price": 232.35,
        "Volume": 4154277
    },
    {
        "Company": "MediaGroup",
        "Date": "2022-09-22",
        "Open Price": 1414.98,
        "Close Price": 1386.09,
        "Low Price": 809.54,
        "Volume": 9876038
    },
    {
        "Company": "FinanceTrust",
        "Date": "2011-05-10",
        "Open Price": 232.35,
        "Close Price": 1418.92,
        "Low Price": 232.35,
        "Volume": 7104362
    }
]
<end>Please transform the following CSV data into PLAIN TEXT:
Trip Name,End Location,Distance (miles),Duration (hours),Fuel Used (gallons)
Desert Drive,Miami,2486.6,41.2,48.2
Coast to Coast,Los Angeles,2267.4,50.6,86.4
City Explorer,Los Angeles,743.0,60.4,57.6
<start>
Trip Name: Desert Drive | End Location: Miami | Distance (miles): 2486.6 | Duration (hours): 41.2 | Fuel Used (gallons): 48.2
Trip Name: Coast to Coast | End Location: Los Angeles | Distance (miles): 2267.4 | Duration (hours): 50.6 | Fuel Used (gallons): 86.4
Trip Name: City Explorer | End Location: Los Angeles | Distance (miles): 743.0 | Duration (hours): 60.4 | Fuel Used (gallons): 57.6
<end>Convert this Json to markdown:
[
    {
        "Title": "The Endless Horizon",
        "Director": "Lira Silverleaf",
        "Genre": "Drama",
        "Release Year": 2018,
        "Box Office Earnings (M)": 952.79
    },
    {
        "Title": "Beyond the Veil",
        "Director": "Talon Blackthorn",
        "Genre": "Sci-Fi",
        "Release Year": 1973,
        "Box Office Earnings (M)": 895.32
    },
    {
        "Title": "The Endless Horizon",
        "Director": "Lira Silverleaf",
        "Genre": "Adventure",
        "Release Year": 1983,
        "Box Office Earnings (M)": 721.32
    },
    {
        "Title": "Starbound Odyssey",
        "Director": "Cade Firebrand",
        "Genre": "Horror",
        "Release Year": 2017,
        "Box Office Earnings (M)": 566.53
    },
    {
        "Title": "Escape from Earth",
        "Director": "Talon Blackthorn",
        "Genre": "Action",
        "Release Year": 2004,
        "Box Office Earnings (M)": 907.09
    }
]<start>
| Title | Director | Genre | Release Year | Box Office Earnings (M) |
| --- | --- | --- | --- | --- |
| The Endless Horizon | Lira Silverleaf | Drama | 2018 | 952.79 |
| Beyond the Veil | Talon Blackthorn | Sci-Fi | 1973 | 895.32 |
| The Endless Horizon | Lira Silverleaf | Adventure | 1983 | 721.32 |
| Starbound Odyssey | Cade Firebrand | Horror | 2017 | 566.53 |
| Escape from Earth | Talon Blackthorn | Action | 2004 | 907.09 |
<end>Please transform the following Yml data into csv:
- Average Latency (ms): 35.88
  Cache Hit Ratio (%): 93.29
  Connection Count: 404
  Database Name: ProfilesDB
  Queries per Second: 1484.84
  Timestamp: '2023-12-09 22:59:00'
- Average Latency (ms): 72.72
  Cache Hit Ratio (%): 93.29
  Connection Count: 435
  Database Name: UserDB
  Queries per Second: 567.64
  Timestamp: '2022-12-07 18:25:31'
- Average Latency (ms): 80.39
  Cache Hit Ratio (%): 95.95
  Connection Count: 140
  Database Name: AnalyticsDB
  Queries per Second: 3108.01
  Timestamp: '2022-12-19 18:37:22'
- Average Latency (ms): 40.45
  Cache Hit Ratio (%): 84.41
  Connection Count: 136
  Database Name: MetricsDB
  Queries per Second: 4009.77
  Timestamp: '2023-12-02 07:30:47'
- Average Latency (ms): 30.72
  Cache Hit Ratio (%): 87.12
  Connection Count: 158
  Database Name: AnalyticsDB
  Queries per Second: 2036.04
  Timestamp: '2021-07-02 12:43:02'
- Average Latency (ms): 48.72
  Cache Hit Ratio (%): 76.2
  Connection Count: 417
  Database Name: UserDB
  Queries per Second: 2190.28
  Timestamp: '2022-11-08 23:03:58'
- Average Latency (ms): 54.32
  Cache Hit Ratio (%): 76.19
  Connection Count: 214
  Database Name: MetricsDB
  Queries per Second: 4485.38
  Timestamp: '2022-10-26 04:03:04'
- Average Latency (ms): 2.9
  Cache Hit Ratio (%): 93.46
  Connection Count: 293
  Database Name: LogsDB
  Queries per Second: 3968.51
  Timestamp: '2021-10-13 05:42:44'
- Average Latency (ms): 38.88
  Cache Hit Ratio (%): 78.06
  Connection Count: 200
  Database Name: SessionsDB
  Queries per Second: 4546.7
  Timestamp: '2022-10-05 02:23:25'
<start>
Database Name,Queries per Second,Cache Hit Ratio (%),Connection Count,Average Latency (ms),Timestamp
ProfilesDB,1484.84,93.29,404,35.88,2023-12-09 22:59:00
UserDB,567.64,93.29,435,72.72,2022-12-07 18:25:31
AnalyticsDB,3108.01,95.95,140,80.39,2022-12-19 18:37:22
MetricsDB,4009.77,84.41,136,40.45,2023-12-02 07:30:47
AnalyticsDB,2036.04,87.12,158,30.72,2021-07-02 12:43:02
UserDB,2190.28,76.2,417,48.72,2022-11-08 23:03:58
MetricsDB,4485.38,76.19,214,54.32,2022-10-26 04:03:04
LogsDB,3968.51,93.46,293,2.9,2021-10-13 05:42:44
SessionsDB,4546.7,78.06,200,38.88,2022-10-05 02:23:25
<end>Transform this MARKDOWN structure to a Plain text format:
| Restaurant Name | Cuisine | Rating |
| --- | --- | --- |
| Curry Corner | Mediterranean | 5 |
| Burger Haven | American | 3 |
| Curry Corner | Italian | 5 |<start>
Restaurant Name: Curry Corner | Cuisine: Mediterranean | Rating: 5
Restaurant Name: Burger Haven | Cuisine: American | Rating: 3
Restaurant Name: Curry Corner | Cuisine: Italian | Rating: 5
<end>Convert this csv to YML:
Temperature (C),Wind Speed (km/h),Day
10.2,26.3,Saturday
38.6,9.3,Sunday
14.7,4.2,Saturday
38.3,24.3,Monday
<start>
- Day: Saturday
  Temperature (C): 10.2
  Wind Speed (km/h): 26.3
- Day: Sunday
  Temperature (C): 38.6
  Wind Speed (km/h): 9.3
- Day: Saturday
  Temperature (C): 14.7
  Wind Speed (km/h): 4.2
- Day: Monday
  Temperature (C): 38.3
  Wind Speed (km/h): 24.3
<end>Convert this plain text to YML:
Device ID: device-0014 | Device Type: Temperature Sensor | Location: Hallway | Battery Level (%): 10.3 | Reading Value: 66.97 | Timestamp: 2022-01-04 21:06:56
Device ID: device-0088 | Device Type: Motion Detector | Location: Living Room | Battery Level (%): 54.1 | Reading Value: -1.64 | Timestamp: 2022-04-13 13:27:41
Device ID: device-0017 | Device Type: Pressure Sensor | Location: Kitchen | Battery Level (%): 32.4 | Reading Value: -38.49 | Timestamp: 2022-08-12 18:07:41
Device ID: device-0041 | Device Type: Temperature Sensor | Location: Bathroom | Battery Level (%): 72.6 | Reading Value: 18.58 | Timestamp: 2022-07-24 18:29:51
Device ID: device-0052 | Device Type: Motion Detector | Location: Bathroom | Battery Level (%): 22.0 | Reading Value: 21.38 | Timestamp: 2023-06-02 02:46:48
Device ID: device-0032 | Device Type: Light Sensor | Location: Bathroom | Battery Level (%): 97.7 | Reading Value: -33.15 | Timestamp: 2023-12-24 02:46:37
Device ID: device-0027 | Device Type: Motion Detector | Location: Garden | Battery Level (%): 85.3 | Reading Value: 32.32 | Timestamp: 2022-02-01 18:20:59
Device ID: device-0044 | Device Type: Humidity Sensor | Location: Hallway | Battery Level (%): 70.6 | Reading Value: 69.84 | Timestamp: 2021-10-04 09:04:44
Device ID: device-0037 | Device Type: Light Sensor | Location: Bathroom | Battery Level (%): 33.7 | Reading Value: 81.44 | Timestamp: 2022-09-12 13:16:14
Device ID: device-0045 | Device Type: Light Sensor | Location: Kitchen | Battery Level (%): 62.8 | Reading Value: -20.51 | Timestamp: 2021-11-18 01:19:46
<start>
- Battery Level (%): 10.3
  Device ID: device-0014
  Device Type: Temperature Sensor
  Location: Hallway
  Reading Value: 66.97
  Timestamp: '2022-01-04 21:06:56'
- Battery Level (%): 54.1
  Device ID: device-0088
  Device Type: Motion Detector
  Location: Living Room
  Reading Value: -1.64
  Timestamp: '2022-04-13 13:27:41'
- Battery Level (%): 32.4
  Device ID: device-0017
  Device Type: Pressure Sensor
  Location: Kitchen
  Reading Value: -38.49
  Timestamp: '2022-08-12 18:07:41'
- Battery Level (%): 72.6
  Device ID: device-0041
  Device Type: Temperature Sensor
  Location: Bathroom
  Reading Value: 18.58
  Timestamp: '2022-07-24 18:29:51'
- Battery Level (%): 22.0
  Device ID: device-0052
  Device Type: Motion Detector
  Location: Bathroom
  Reading Value: 21.38
  Timestamp: '2023-06-02 02:46:48'
- Battery Level (%): 97.7
  Device ID: device-0032
  Device Type: Light Sensor
  Location: Bathroom
  Reading Value: -33.15
  Timestamp: '2023-12-24 02:46:37'
- Battery Level (%): 85.3
  Device ID: device-0027
  Device Type: Motion Detector
  Location: Garden
  Reading Value: 32.32
  Timestamp: '2022-02-01 18:20:59'
- Battery Level (%): 70.6
  Device ID: device-0044
  Device Type: Humidity Sensor
  Location: Hallway
  Reading Value: 69.84
  Timestamp: '2021-10-04 09:04:44'
- Battery Level (%): 33.7
  Device ID: device-0037
  Device Type: Light Sensor
  Location: Bathroom
  Reading Value: 81.44
  Timestamp: '2022-09-12 13:16:14'
- Battery Level (%): 62.8
  Device ID: device-0045
  Device Type: Light Sensor
  Location: Kitchen
  Reading Value: -20.51
  Timestamp: '2021-11-18 01:19:46'
<end>Convert this MARKDOWN to JSON:
| Company | Date | Open Price | Close Price | High Price | Low Price | Volume |
| --- | --- | --- | --- | --- | --- | --- |
| AeroSystems | 2013-11-11 | 1401.75 | 59.35 | 1401.75 | 59.35 | 144715 |
| GreenEnergy | 2021-11-27 | 546.8 | 882.61 | 882.61 | 546.8 | 5608863 |
| AeroSystems | 2017-11-01 | 649.67 | 171.06 | 1117.86 | 171.06 | 3139506 |
| BioLife | 2016-10-20 | 992.68 | 1149.48 | 1149.48 | 381.11 | 6479233 |
| FoodChain | 2019-11-03 | 428.05 | 954.84 | 954.84 | 428.05 | 1783301 |
| FinanceTrust | 2010-12-02 | 1237.93 | 509.7 | 1237.93 | 38.38 | 7749514 |
| MediaGroup | 2022-09-26 | 1129.49 | 372.44 | 1129.49 | 372.44 | 653457 |<start>
[
    {
        "Company": "AeroSystems",
        "Date": "2013-11-11",
        "Open Price": 1401.75,
        "Close Price": 59.35,
        "High Price": 1401.75,
        "Low Price": 59.35,
        "Volume": 144715
    },
    {
        "Company": "GreenEnergy",
        "Date": "2021-11-27",
        "Open Price": 546.8,
        "Close Price": 882.61,
        "High Price": 882.61,
        "Low Price": 546.8,
        "Volume": 5608863
    },
    {
        "Company": "AeroSystems",
        "Date": "2017-11-01",
        "Open Price": 649.67,
        "Close Price": 171.06,
        "High Price": 1117.86,
        "Low Price": 171.06,
        "Volume": 3139506
    },
    {
        "Company": "BioLife",
        "Date": "2016-10-20",
        "Open Price": 992.68,
        "Close Price": 1149.48,
        "High Price": 1149.48,
        "Low Price": 381.11,
        "Volume": 6479233
    },
    {
        "Company": "FoodChain",
        "Date": "2019-11-03",
        "Open Price": 428.05,
        "Close Price": 954.84,
        "High Price": 954.84,
        "Low Price": 428.05,
        "Volume": 1783301
    },
    {
        "Company": "FinanceTrust",
        "Date": "2010-12-02",
        "Open Price": 1237.93,
        "Close Price": 509.7,
        "High Price": 1237.93,
        "Low Price": 38.38,
        "Volume": 7749514
    },
    {
        "Company": "MediaGroup",
        "Date": "2022-09-26",
        "Open Price": 1129.49,
        "Close Price": 372.44,
        "High Price": 1129.49,
        "Low Price": 372.44,
        "Volume": 653457
    }
]
<end>Convert this csv to PLAIN TEXT:
Location,Condition,Temperature (C),Wind Speed (km/h),Day
Denver,Stormy,38.7,20.7,Thursday
Chicago,Rainy,7.4,0.1,Thursday
Seattle,Snowy,25.5,28.1,Friday
Miami,Windy,16.3,14.4,Sunday
Phoenix,Windy,14.1,22.7,Thursday
Miami,Cloudy,22.8,14.4,Friday
Miami,Cloudy,25.5,8.8,Saturday
Denver,Windy,39.4,4.0,Friday
Miami,Sunny,31.7,26.9,Tuesday
<start>
Location: Denver | Condition: Stormy | Temperature (C): 38.7 | Wind Speed (km/h): 20.7 | Day: Thursday
Location: Chicago | Condition: Rainy | Temperature (C): 7.4 | Wind Speed (km/h): 0.1 | Day: Thursday
Location: Seattle | Condition: Snowy | Temperature (C): 25.5 | Wind Speed (km/h): 28.1 | Day: Friday
Location: Miami | Condition: Windy | Temperature (C): 16.3 | Wind Speed (km/h): 14.4 | Day: Sunday
Location: Phoenix | Condition: Windy | Temperature (C): 14.1 | Wind Speed (km/h): 22.7 | Day: Thursday
Location: Miami | Condition: Cloudy | Temperature (C): 22.8 | Wind Speed (km/h): 14.4 | Day: Friday
Location: Miami | Condition: Cloudy | Temperature (C): 25.5 | Wind Speed (km/h): 8.8 | Day: Saturday
Location: Denver | Condition: Windy | Temperature (C): 39.4 | Wind Speed (km/h): 4.0 | Day: Friday
Location: Miami | Condition: Sunny | Temperature (C): 31.7 | Wind Speed (km/h): 26.9 | Day: Tuesday
<end>Convert this JSON to yaml:
[
    {
        "Company": "MediaGroup",
        "Date": "2014-01-13",
        "Open Price": 567.51,
        "Close Price": 774.74,
        "Volume": 7402551
    },
    {
        "Company": "FoodChain",
        "Date": "2010-01-11",
        "Open Price": 1429.81,
        "Close Price": 432.61,
        "Volume": 1579197
    },
    {
        "Company": "TechnoCorp",
        "Date": "2022-10-04",
        "Open Price": 1113.59,
        "Close Price": 567.51,
        "Volume": 346004
    }
]<start>
- Close Price: 774.74
  Company: MediaGroup
  Date: '2014-01-13'
  Open Price: 567.51
  Volume: 7402551
- Close Price: 432.61
  Company: FoodChain
  Date: '2010-01-11'
  Open Price: 1429.81
  Volume: 1579197
- Close Price: 567.51
  Company: TechnoCorp
  Date: '2022-10-04'
  Open Price: 1113.59
  Volume: 346004
<end>Can you change this markdown into yml?
| Trip Name | Start Location | End Location | Distance (miles) | Duration (hours) | Fuel Used (gallons) |
| --- | --- | --- | --- | --- | --- |
| Valley Voyage | Phoenix | Miami | 894.3 | 7.2 | 69.7 |
| Mountain Adventure | San Francisco | Chicago | 81.1 | 6.3 | 87.2 |
| City Explorer | San Francisco | Phoenix | 1705.5 | 63.5 | 7.3 |
| Historic Route | Denver | Phoenix | 2483.0 | 27.8 | 98.7 |
| City Explorer | New York | Los Angeles | 2255.1 | 16.0 | 52.5 |
| Valley Voyage | Los Angeles | San Francisco | 2908.8 | 45.9 | 24.5 |
| Highway Odyssey | Chicago | San Francisco | 556.2 | 33.3 | 38.0 |
| Desert Drive | Miami | Houston | 139.8 | 12.5 | 26.9 |
| Mountain Adventure | Houston | Denver | 556.2 | 33.3 | 27.8 |
| Highway Odyssey | San Francisco | New York | 1967.8 | 67.4 | 97.9 |<start>
- Distance (miles): 894.3
  Duration (hours): 7.2
  End Location: Miami
  Fuel Used (gallons): 69.7
  Start Location: Phoenix
  Trip Name: Valley Voyage
- Distance (miles): 81.1
  Duration (hours): 6.3
  End Location: Chicago
  Fuel Used (gallons): 87.2
  Start Location: San Francisco
  Trip Name: Mountain Adventure
- Distance (miles): 1705.5
  Duration (hours): 63.5
  End Location: Phoenix
  Fuel Used (gallons): 7.3
  Start Location: San Francisco
  Trip Name: City Explorer
- Distance (miles): 2483.0
  Duration (hours): 27.8
  End Location: Phoenix
  Fuel Used (gallons): 98.7
  Start Location: Denver
  Trip Name: Historic Route
- Distance (miles): 2255.1
  Duration (hours): 16.0
  End Location: Los Angeles
  Fuel Used (gallons): 52.5
  Start Location: New York
  Trip Name: City Explorer
- Distance (miles): 2908.8
  Duration (hours): 45.9
  End Location: San Francisco
  Fuel Used (gallons): 24.5
  Start Location: Los Angeles
  Trip Name: Valley Voyage
- Distance (miles): 556.2
  Duration (hours): 33.3
  End Location: San Francisco
  Fuel Used (gallons): 38.0
  Start Location: Chicago
  Trip Name: Highway Odyssey
- Distance (miles): 139.8
  Duration (hours): 12.5
  End Location: Houston
  Fuel Used (gallons): 26.9
  Start Location: Miami
  Trip Name: Desert Drive
- Distance (miles): 556.2
  Duration (hours): 33.3
  End Location: Denver
  Fuel Used (gallons): 27.8
  Start Location: Houston
  Trip Name: Mountain Adventure
- Distance (miles): 1967.8
  Duration (hours): 67.4
  End Location: New York
  Fuel Used (gallons): 97.9
  Start Location: San Francisco
  Trip Name: Highway Odyssey
<end>Convert this Yml to csv:
- Cuisine: Mexican
  Price Range: $$
- Cuisine: Italian
  Price Range: $$$
- Cuisine: Mediterranean
  Price Range: $
<start>
Cuisine,Price Range
Mexican,$$
Italian,$$$
Mediterranean,$
<end>Convert this Markdown to csv:
| Device ID | Location | Reading Value | Timestamp |
| --- | --- | --- | --- |
| device-0089 | Office | 36.69 | 2021-07-05 23:36:43 |
| device-0067 | Office | 26.03 | 2022-02-04 09:48:02 |
| device-0027 | Garage | 41.32 | 2022-12-24 13:31:01 |
| device-0076 | Living Room | 10.04 | 2022-10-06 11:58:17 |
| device-0092 | Hallway | 38.24 | 2023-09-26 16:26:13 |<start>
Device ID,Location,Reading Value,Timestamp
device-0089,Office,36.69,2021-07-05 23:36:43
device-0067,Office,26.03,2022-02-04 09:48:02
device-0027,Garage,41.32,2022-12-24 13:31:01
device-0076,Living Room,10.04,2022-10-06 11:58:17
device-0092,Hallway,38.24,2023-09-26 16:26:13
<end>Convert this Csv to yaml:
Restaurant Name,Cuisine,Rating
Taco Town,American,4
Sushi World,Mexican,5
BBQ Barn,Japanese,5
The Golden Spoon,Italian,2
Pasta Palace,Mediterranean,5
Burger Haven,Mexican,1
Vegan Delight,American,5
<start>
- Cuisine: American
  Rating: 4
  Restaurant Name: Taco Town
- Cuisine: Mexican
  Rating: 5
  Restaurant Name: Sushi World
- Cuisine: Japanese
  Rating: 5
  Restaurant Name: BBQ Barn
- Cuisine: Italian
  Rating: 2
  Restaurant Name: The Golden Spoon
- Cuisine: Mediterranean
  Rating: 5
  Restaurant Name: Pasta Palace
- Cuisine: Mexican
  Rating: 1
  Restaurant Name: Burger Haven
- Cuisine: American
  Rating: 5
  Restaurant Name: Vegan Delight
<end>Transform this Csv structure to a markdown format:
Cuisine,Location,Price Range
Mediterranean,New York,$
Japanese,Los Angeles,$$$$$
Chinese,San Francisco,$$$$
Italian,New York,$$$$$
Japanese,New York,$$
Chinese,San Francisco,$$$
Mexican,Phoenix,$$$$$
Indian,Phoenix,$$
American,Los Angeles,$$$$
American,New York,$$$$$
<start>
| Cuisine | Location | Price Range |
| --- | --- | --- |
| Mediterranean | New York | $ |
| Japanese | Los Angeles | $$$$$ |
| Chinese | San Francisco | $$$$ |
| Italian | New York | $$$$$ |
| Japanese | New York | $$ |
| Chinese | San Francisco | $$$ |
| Mexican | Phoenix | $$$$$ |
| Indian | Phoenix | $$ |
| American | Los Angeles | $$$$ |
| American | New York | $$$$$ |
<end>Please transform the following markdown data into yml:
| Date | Close Price | Low Price | Volume |
| --- | --- | --- | --- |
| 2015-04-13 | 516.8 | 418.85 | 8640462 |
| 2022-10-26 | 1470.16 | 259.46 | 4687713 |
| 2020-09-19 | 313.49 | 156.13 | 1628293 |
| 2019-06-17 | 1237.46 | 873.06 | 1628293 |
| 2017-05-11 | 1258.11 | 377.13 | 1189415 |
| 2010-10-25 | 1031.17 | 260.97 | 4152639 |
| 2015-03-21 | 16.52 | 16.52 | 4039773 |
| 2023-06-07 | 653.0 | 387.1 | 5867919 |
| 2020-05-05 | 1486.69 | 387.1 | 7910691 |
| 2014-09-22 | 472.87 | 472.87 | 174440 |<start>
- Close Price: 516.8
  Date: '2015-04-13'
  Low Price: 418.85
  Volume: 8640462
- Close Price: 1470.16
  Date: '2022-10-26'
  Low Price: 259.46
  Volume: 4687713
- Close Price: 313.49
  Date: '2020-09-19'
  Low Price: 156.13
  Volume: 1628293
- Close Price: 1237.46
  Date: '2019-06-17'
  Low Price: 873.06
  Volume: 1628293
- Close Price: 1258.11
  Date: '2017-05-11'
  Low Price: 377.13
  Volume: 1189415
- Close Price: 1031.17
  Date: '2010-10-25'
  Low Price: 260.97
  Volume: 4152639
- Close Price: 16.52
  Date: '2015-03-21'
  Low Price: 16.52
  Volume: 4039773
- Close Price: 653.0
  Date: '2023-06-07'
  Low Price: 387.1
  Volume: 5867919
- Close Price: 1486.69
  Date: '2020-05-05'
  Low Price: 387.1
  Volume: 7910691
- Close Price: 472.87
  Date: '2014-09-22'
  Low Price: 472.87
  Volume: 174440
<end>Transform this CSV structure to a YAML format:
Restaurant Name,Price Range
Pasta Palace,$$$
Sushi World,$$
Pasta Palace,$$$$
<start>
- Price Range: $$$
  Restaurant Name: Pasta Palace
- Price Range: $$
  Restaurant Name: Sushi World
- Price Range: $$$$
  Restaurant Name: Pasta Palace
<end>Please transform the following plain text data into Yml:
Database Name: SalesDB | Queries per Second: 2007.98 | Connection Count: 79 | Average Latency (ms): 31.79 | Timestamp: 2021-08-20 14:56:08
Database Name: SalesDB | Queries per Second: 4586.85 | Connection Count: 393 | Average Latency (ms): 84.9 | Timestamp: 2021-09-23 21:39:42
Database Name: ProductsDB | Queries per Second: 2351.01 | Connection Count: 170 | Average Latency (ms): 34.32 | Timestamp: 2021-12-28 08:53:33
Database Name: ProfilesDB | Queries per Second: 2411.15 | Connection Count: 262 | Average Latency (ms): 88.85 | Timestamp: 2022-07-16 01:20:38
Database Name: InventoryDB | Queries per Second: 1783.56 | Connection Count: 206 | Average Latency (ms): 68.71 | Timestamp: 2021-05-05 10:47:35
Database Name: LogsDB | Queries per Second: 4193.18 | Connection Count: 230 | Average Latency (ms): 87.28 | Timestamp: 2021-08-22 03:37:05
Database Name: AnalyticsDB | Queries per Second: 588.51 | Connection Count: 428 | Average Latency (ms): 47.46 | Timestamp: 2021-09-19 13:15:07
<start>
- Average Latency (ms): 31.79
  Connection Count: 79
  Database Name: SalesDB
  Queries per Second: 2007.98
  Timestamp: '2021-08-20 14:56:08'
- Average Latency (ms): 84.9
  Connection Count: 393
  Database Name: SalesDB
  Queries per Second: 4586.85
  Timestamp: '2021-09-23 21:39:42'
- Average Latency (ms): 34.32
  Connection Count: 170
  Database Name: ProductsDB
  Queries per Second: 2351.01
  Timestamp: '2021-12-28 08:53:33'
- Average Latency (ms): 88.85
  Connection Count: 262
  Database Name: ProfilesDB
  Queries per Second: 2411.15
  Timestamp: '2022-07-16 01:20:38'
- Average Latency (ms): 68.71
  Connection Count: 206
  Database Name: InventoryDB
  Queries per Second: 1783.56
  Timestamp: '2021-05-05 10:47:35'
- Average Latency (ms): 87.28
  Connection Count: 230
  Database Name: LogsDB
  Queries per Second: 4193.18
  Timestamp: '2021-08-22 03:37:05'
- Average Latency (ms): 47.46
  Connection Count: 428
  Database Name: AnalyticsDB
  Queries per Second: 588.51
  Timestamp: '2021-09-19 13:15:07'
<end>Transform this csv structure to a plain text format:
Company,Sector,Market Cap,Stock Price,Quarter
AutoDrive,Aerospace,Small Cap,253.42,Q1
EcoEnergy,Technology,Small Cap,324.37,Q4
AutoDrive,Finance,Large Cap,658.76,Q4
EcoEnergy,Energy,Mid Cap,883.29,Q4
EcoEnergy,Aerospace,Mid Cap,417.87,Q1
BioPharm,Healthcare,Mid Cap,229.68,Q3
TechCorp,Energy,Mid Cap,229.68,Q4
<start>
Company: AutoDrive | Sector: Aerospace | Market Cap: Small Cap | Stock Price: 253.42 | Quarter: Q1
Company: EcoEnergy | Sector: Technology | Market Cap: Small Cap | Stock Price: 324.37 | Quarter: Q4
Company: AutoDrive | Sector: Finance | Market Cap: Large Cap | Stock Price: 658.76 | Quarter: Q4
Company: EcoEnergy | Sector: Energy | Market Cap: Mid Cap | Stock Price: 883.29 | Quarter: Q4
Company: EcoEnergy | Sector: Aerospace | Market Cap: Mid Cap | Stock Price: 417.87 | Quarter: Q1
Company: BioPharm | Sector: Healthcare | Market Cap: Mid Cap | Stock Price: 229.68 | Quarter: Q3
Company: TechCorp | Sector: Energy | Market Cap: Mid Cap | Stock Price: 229.68 | Quarter: Q4
<end>Can you change this MARKDOWN into JSON?
| Temperature (C) | Humidity (%) | Wind Speed (km/h) | Day |
| --- | --- | --- | --- |
| 9.6 | 56 | 23.2 | Saturday |
| 34.9 | 89 | 6.5 | Saturday |
| 5.8 | 67 | 29.7 | Friday |
| 34.1 | 68 | 21.2 | Tuesday |
| -0.6 | 50 | 15.5 | Thursday |<start>
[
    {
        "Temperature (C)": 9.6,
        "Humidity (%)": 56,
        "Wind Speed (km/h)": 23.2,
        "Day": "Saturday"
    },
    {
        "Temperature (C)": 34.9,
        "Humidity (%)": 89,
        "Wind Speed (km/h)": 6.5,
        "Day": "Saturday"
    },
    {
        "Temperature (C)": 5.8,
        "Humidity (%)": 67,
        "Wind Speed (km/h)": 29.7,
        "Day": "Friday"
    },
    {
        "Temperature (C)": 34.1,
        "Humidity (%)": 68,
        "Wind Speed (km/h)": 21.2,
        "Day": "Tuesday"
    },
    {
        "Temperature (C)": -0.6,
        "Humidity (%)": 50,
        "Wind Speed (km/h)": 15.5,
        "Day": "Thursday"
    }
]
<end>Please transform the following markdown data into PLAIN TEXT:
| Name | Age | Birth Month | City | Income |
| --- | --- | --- | --- | --- |
| Danny | 18 | March | El Paso | 255000 |
| Hailey | 35 | April | Chicago | 125000 |
| Aaliyah | 26 | August | Portland | 395000 |
| Elsie | 37 | May | Fort Worth | 475000 |
| Keith | 63 | July | San Antonio | 30000 |
| Todd | 34 | September | Nashville | 495000 |
| Nora | 52 | August | Seattle | 205000 |
| Leo | 64 | January | Memphis | 65000 |
| Bobbie | 19 | February | New York | 385000 |
| Kathy | 61 | November | Louisville | 210000 |<start>
Name: Danny | Age: 18 | Birth Month: March | City: El Paso | Income: 255000
Name: Hailey | Age: 35 | Birth Month: April | City: Chicago | Income: 125000
Name: Aaliyah | Age: 26 | Birth Month: August | City: Portland | Income: 395000
Name: Elsie | Age: 37 | Birth Month: May | City: Fort Worth | Income: 475000
Name: Keith | Age: 63 | Birth Month: July | City: San Antonio | Income: 30000
Name: Todd | Age: 34 | Birth Month: September | City: Nashville | Income: 495000
Name: Nora | Age: 52 | Birth Month: August | City: Seattle | Income: 205000
Name: Leo | Age: 64 | Birth Month: January | City: Memphis | Income: 65000
Name: Bobbie | Age: 19 | Birth Month: February | City: New York | Income: 385000
Name: Kathy | Age: 61 | Birth Month: November | City: Louisville | Income: 210000
<end>Please transform the following Plain text data into json:
Date: 2019-07-06 | Close Price: 131.86 | Low Price: 20.71 | Volume: 8008488
Date: 2017-05-07 | Close Price: 582.98 | Low Price: 547.82 | Volume: 4561275
Date: 2012-01-12 | Close Price: 1319.25 | Low Price: 370.92 | Volume: 8135302
Date: 2015-06-24 | Close Price: 337.5 | Low Price: 157.83 | Volume: 3571796
Date: 2018-07-11 | Close Price: 788.22 | Low Price: 655.29 | Volume: 7126255
Date: 2019-02-25 | Close Price: 689.07 | Low Price: 20.71 | Volume: 3571796
Date: 2015-02-17 | Close Price: 20.71 | Low Price: 20.71 | Volume: 758081
Date: 2015-01-18 | Close Price: 227.92 | Low Price: 227.92 | Volume: 9969330
Date: 2022-04-05 | Close Price: 337.5 | Low Price: 337.5 | Volume: 682719
<start>
[
    {
        "Date": "2019-07-06",
        "Close Price": 131.86,
        "Low Price": 20.71,
        "Volume": 8008488
    },
    {
        "Date": "2017-05-07",
        "Close Price": 582.98,
        "Low Price": 547.82,
        "Volume": 4561275
    },
    {
        "Date": "2012-01-12",
        "Close Price": 1319.25,
        "Low Price": 370.92,
        "Volume": 8135302
    },
    {
        "Date": "2015-06-24",
        "Close Price": 337.5,
        "Low Price": 157.83,
        "Volume": 3571796
    },
    {
        "Date": "2018-07-11",
        "Close Price": 788.22,
        "Low Price": 655.29,
        "Volume": 7126255
    },
    {
        "Date": "2019-02-25",
        "Close Price": 689.07,
        "Low Price": 20.71,
        "Volume": 3571796
    },
    {
        "Date": "2015-02-17",
        "Close Price": 20.71,
        "Low Price": 20.71,
        "Volume": 758081
    },
    {
        "Date": "2015-01-18",
        "Close Price": 227.92,
        "Low Price": 227.92,
        "Volume": 9969330
    },
    {
        "Date": "2022-04-05",
        "Close Price": 337.5,
        "Low Price": 337.5,
        "Volume": 682719
    }
]
<end>Convert this yaml to json:
- Annual Revenue (B): 362.57
  Company: AeroSpace
  Quarter: Q2
- Annual Revenue (B): 77.42
  Company: AeroSpace
  Quarter: Q2
- Annual Revenue (B): 126.94
  Company: BioPharm
  Quarter: Q2
- Annual Revenue (B): 329.83
  Company: BioPharm
  Quarter: Q3
- Annual Revenue (B): 277.43
  Company: AutoDrive
  Quarter: Q1
<start>
[
    {
        "Company": "AeroSpace",
        "Annual Revenue (B)": 362.57,
        "Quarter": "Q2"
    },
    {
        "Company": "AeroSpace",
        "Annual Revenue (B)": 77.42,
        "Quarter": "Q2"
    },
    {
        "Company": "BioPharm",
        "Annual Revenue (B)": 126.94,
        "Quarter": "Q2"
    },
    {
        "Company": "BioPharm",
        "Annual Revenue (B)": 329.83,
        "Quarter": "Q3"
    },
    {
        "Company": "AutoDrive",
        "Annual Revenue (B)": 277.43,
        "Quarter": "Q1"
    }
]
<end>Please transform the following CSV data into PLAIN TEXT:
Company,Sector,Market Cap,Stock Price,Annual Revenue (B),Quarter
RetailHub,Finance,Mid Cap,756.44,446.28,Q3
FinanceWorks,Finance,Small Cap,51.79,347.99,Q1
FinanceWorks,Retail,Mega Cap,833.94,412.14,Q1
<start>
Company: RetailHub | Sector: Finance | Market Cap: Mid Cap | Stock Price: 756.44 | Annual Revenue (B): 446.28 | Quarter: Q3
Company: FinanceWorks | Sector: Finance | Market Cap: Small Cap | Stock Price: 51.79 | Annual Revenue (B): 347.99 | Quarter: Q1
Company: FinanceWorks | Sector: Retail | Market Cap: Mega Cap | Stock Price: 833.94 | Annual Revenue (B): 412.14 | Quarter: Q1
<end>Convert this CSV to Markdown:
Device ID,Device Type,Location,Battery Level (%),Reading Value,Timestamp
device-0051,Temperature Sensor,Bathroom,99.6,83.42,2021-12-28 19:08:22
device-0051,Motion Detector,Hallway,99.6,49.69,2021-01-04 16:02:31
device-0007,Pressure Sensor,Bathroom,12.3,14.01,2022-04-02 02:27:40
device-0052,Pressure Sensor,Hallway,21.9,6.28,2021-07-17 12:21:20
device-0093,Motion Detector,Living Room,78.6,5.55,2023-04-16 02:49:19
<start>
| Device ID | Device Type | Location | Battery Level (%) | Reading Value | Timestamp |
| --- | --- | --- | --- | --- | --- |
| device-0051 | Temperature Sensor | Bathroom | 99.6 | 83.42 | 2021-12-28 19:08:22 |
| device-0051 | Motion Detector | Hallway | 99.6 | 49.69 | 2021-01-04 16:02:31 |
| device-0007 | Pressure Sensor | Bathroom | 12.3 | 14.01 | 2022-04-02 02:27:40 |
| device-0052 | Pressure Sensor | Hallway | 21.9 | 6.28 | 2021-07-17 12:21:20 |
| device-0093 | Motion Detector | Living Room | 78.6 | 5.55 | 2023-04-16 02:49:19 |
<end>Convert this Csv to markdown:
Location,Condition,Temperature (C),Humidity (%),Wind Speed (km/h),Day
New York,Rainy,18.9,43,24.8,Saturday
Miami,Rainy,-5.9,95,12.0,Thursday
New York,Windy,-8.4,51,19.8,Monday
Chicago,Sunny,-5.8,55,2.4,Saturday
Los Angeles,Foggy,35.1,42,16.7,Sunday
Denver,Foggy,34.3,38,2.1,Wednesday
New York,Foggy,23.9,69,16.7,Thursday
Houston,Windy,12.6,49,16.7,Sunday
<start>
| Location | Condition | Temperature (C) | Humidity (%) | Wind Speed (km/h) | Day |
| --- | --- | --- | --- | --- | --- |
| New York | Rainy | 18.9 | 43 | 24.8 | Saturday |
| Miami | Rainy | -5.9 | 95 | 12.0 | Thursday |
| New York | Windy | -8.4 | 51 | 19.8 | Monday |
| Chicago | Sunny | -5.8 | 55 | 2.4 | Saturday |
| Los Angeles | Foggy | 35.1 | 42 | 16.7 | Sunday |
| Denver | Foggy | 34.3 | 38 | 2.1 | Wednesday |
| New York | Foggy | 23.9 | 69 | 16.7 | Thursday |
| Houston | Windy | 12.6 | 49 | 16.7 | Sunday |
<end>Here's some yaml data, can you convert it to plain text?
- Close Price: 711.32
  Date: '2012-10-10'
  High Price: 1061.01
  Low Price: 711.32
  Volume: 716735
- Close Price: 1321.43
  Date: '2020-04-02'
  High Price: 1321.43
  Low Price: 73.05
  Volume: 8539952
- Close Price: 1397.91
  Date: '2021-04-20'
  High Price: 1397.91
  Low Price: 367.58
  Volume: 7102641
- Close Price: 379.6
  Date: '2019-01-21'
  High Price: 388.61
  Low Price: 122.31
  Volume: 5650155
- Close Price: 963.93
  Date: '2014-11-24'
  High Price: 1238.53
  Low Price: 828.29
  Volume: 5336111
- Close Price: 768.77
  Date: '2011-02-02'
  High Price: 1191.19
  Low Price: 768.77
  Volume: 2496770
- Close Price: 1467.98
  Date: '2020-03-07'
  High Price: 1467.98
  Low Price: 652.21
  Volume: 4853963
- Close Price: 949.86
  Date: '2012-04-15'
  High Price: 1187.87
  Low Price: 949.86
  Volume: 9743489
- Close Price: 1441.7
  Date: '2018-09-28'
  High Price: 1441.7
  Low Price: 334.85
  Volume: 2524295
- Close Price: 855.77
  Date: '2015-06-17'
  High Price: 1238.53
  Low Price: 318.87
  Volume: 324538
<start>
Date: 2012-10-10 | Close Price: 711.32 | High Price: 1061.01 | Low Price: 711.32 | Volume: 716735
Date: 2020-04-02 | Close Price: 1321.43 | High Price: 1321.43 | Low Price: 73.05 | Volume: 8539952
Date: 2021-04-20 | Close Price: 1397.91 | High Price: 1397.91 | Low Price: 367.58 | Volume: 7102641
Date: 2019-01-21 | Close Price: 379.6 | High Price: 388.61 | Low Price: 122.31 | Volume: 5650155
Date: 2014-11-24 | Close Price: 963.93 | High Price: 1238.53 | Low Price: 828.29 | Volume: 5336111
Date: 2011-02-02 | Close Price: 768.77 | High Price: 1191.19 | Low Price: 768.77 | Volume: 2496770
Date: 2020-03-07 | Close Price: 1467.98 | High Price: 1467.98 | Low Price: 652.21 | Volume: 4853963
Date: 2012-04-15 | Close Price: 949.86 | High Price: 1187.87 | Low Price: 949.86 | Volume: 9743489
Date: 2018-09-28 | Close Price: 1441.7 | High Price: 1441.7 | Low Price: 334.85 | Volume: 2524295
Date: 2015-06-17 | Close Price: 855.77 | High Price: 1238.53 | Low Price: 318.87 | Volume: 324538
<end>Can you change this markdown into plain text?
| SKU | Price | Supplier Name |
| --- | --- | --- |
| SKU-1047 | 94.55 | Wonka Industries |
| SKU-1000 | 285.27 | Globex |
| SKU-1058 | 94.95 | Globex |<start>
SKU: SKU-1047 | Price: 94.55 | Supplier Name: Wonka Industries
SKU: SKU-1000 | Price: 285.27 | Supplier Name: Globex
SKU: SKU-1058 | Price: 94.95 | Supplier Name: Globex
<end>Please transform the following JSON data into csv:
[
    {
        "Title": "Edge of Infinity",
        "Director": "Talon Blackthorn",
        "Genre": "Adventure",
        "Release Year": 2016,
        "Box Office Earnings (M)": 500.86
    },
    {
        "Title": "Dreamwalker",
        "Director": "Mara Moonshadow",
        "Genre": "Fantasy",
        "Release Year": 1971,
        "Box Office Earnings (M)": 957.8
    },
    {
        "Title": "Escape from Earth",
        "Director": "Zara Stormrider",
        "Genre": "Thriller",
        "Release Year": 1972,
        "Box Office Earnings (M)": 790.67
    },
    {
        "Title": "Escape from Earth",
        "Director": "Cade Firebrand",
        "Genre": "Thriller",
        "Release Year": 1994,
        "Box Office Earnings (M)": 211.81
    }
]<start>
Title,Director,Genre,Release Year,Box Office Earnings (M)
Edge of Infinity,Talon Blackthorn,Adventure,2016,500.86
Dreamwalker,Mara Moonshadow,Fantasy,1971,957.8
Escape from Earth,Zara Stormrider,Thriller,1972,790.67
Escape from Earth,Cade Firebrand,Thriller,1994,211.81
<end>Here's some json data, can you convert it to markdown?
[
    {
        "Database Name": "ProductsDB",
        "Cache Hit Ratio (%)": 86.51,
        "Connection Count": 361,
        "Timestamp": "2022-08-25 03:32:43"
    },
    {
        "Database Name": "SalesDB",
        "Cache Hit Ratio (%)": 76.34,
        "Connection Count": 489,
        "Timestamp": "2023-07-22 14:59:59"
    },
    {
        "Database Name": "UserDB",
        "Cache Hit Ratio (%)": 82.8,
        "Connection Count": 379,
        "Timestamp": "2022-08-19 00:15:34"
    },
    {
        "Database Name": "ProductsDB",
        "Cache Hit Ratio (%)": 94.8,
        "Connection Count": 313,
        "Timestamp": "2022-08-15 13:24:19"
    },
    {
        "Database Name": "AnalyticsDB",
        "Cache Hit Ratio (%)": 72.96,
        "Connection Count": 227,
        "Timestamp": "2022-04-24 12:25:11"
    },
    {
        "Database Name": "SessionsDB",
        "Cache Hit Ratio (%)": 81.68,
        "Connection Count": 27,
        "Timestamp": "2023-02-22 05:31:21"
    }
]<start>
| Database Name | Cache Hit Ratio (%) | Connection Count | Timestamp |
| --- | --- | --- | --- |
| ProductsDB | 86.51 | 361 | 2022-08-25 03:32:43 |
| SalesDB | 76.34 | 489 | 2023-07-22 14:59:59 |
| UserDB | 82.8 | 379 | 2022-08-19 00:15:34 |
| ProductsDB | 94.8 | 313 | 2022-08-15 13:24:19 |
| AnalyticsDB | 72.96 | 227 | 2022-04-24 12:25:11 |
| SessionsDB | 81.68 | 27 | 2023-02-22 05:31:21 |
<end>Can you change this JSON into Csv?
[
    {
        "Date": "2012-04-28",
        "Open Price": 1248.28,
        "Close Price": 792.87,
        "High Price": 1248.28,
        "Low Price": 792.87,
        "Volume": 3684921
    },
    {
        "Date": "2020-10-10",
        "Open Price": 639.56,
        "Close Price": 1469.4,
        "High Price": 1469.4,
        "Low Price": 639.56,
        "Volume": 563452
    },
    {
        "Date": "2020-08-03",
        "Open Price": 488.52,
        "Close Price": 525.27,
        "High Price": 792.87,
        "Low Price": 488.52,
        "Volume": 2948657
    },
    {
        "Date": "2017-08-03",
        "Open Price": 1285.66,
        "Close Price": 60.87,
        "High Price": 1285.66,
        "Low Price": 60.87,
        "Volume": 4586863
    },
    {
        "Date": "2011-08-20",
        "Open Price": 1002.07,
        "Close Price": 1246.03,
        "High Price": 1320.31,
        "Low Price": 1002.07,
        "Volume": 740136
    },
    {
        "Date": "2018-01-15",
        "Open Price": 652.11,
        "Close Price": 1277.15,
        "High Price": 1277.15,
        "Low Price": 652.11,
        "Volume": 563452
    },
    {
        "Date": "2018-02-16",
        "Open Price": 1299.28,
        "Close Price": 660.81,
        "High Price": 1299.28,
        "Low Price": 324.23,
        "Volume": 7834776
    }
]<start>
Date,Open Price,Close Price,High Price,Low Price,Volume
2012-04-28,1248.28,792.87,1248.28,792.87,3684921
2020-10-10,639.56,1469.4,1469.4,639.56,563452
2020-08-03,488.52,525.27,792.87,488.52,2948657
2017-08-03,1285.66,60.87,1285.66,60.87,4586863
2011-08-20,1002.07,1246.03,1320.31,1002.07,740136
2018-01-15,652.11,1277.15,1277.15,652.11,563452
2018-02-16,1299.28,660.81,1299.28,324.23,7834776
<end>Transform this plain text structure to a csv format:
Start Location: Denver | End Location: New York | Distance (miles): 404.9 | Duration (hours): 61.5 | Fuel Used (gallons): 56.4
Start Location: Houston | End Location: Los Angeles | Distance (miles): 713.9 | Duration (hours): 43.5 | Fuel Used (gallons): 10.3
Start Location: New York | End Location: Chicago | Distance (miles): 2007.2 | Duration (hours): 42.0 | Fuel Used (gallons): 77.1
Start Location: Houston | End Location: Los Angeles | Distance (miles): 2423.3 | Duration (hours): 31.3 | Fuel Used (gallons): 72.5
Start Location: New York | End Location: San Francisco | Distance (miles): 2007.2 | Duration (hours): 10.1 | Fuel Used (gallons): 71.1
<start>
Start Location,End Location,Distance (miles),Duration (hours),Fuel Used (gallons)
Denver,New York,404.9,61.5,56.4
Houston,Los Angeles,713.9,43.5,10.3
New York,Chicago,2007.2,42.0,77.1
Houston,Los Angeles,2423.3,31.3,72.5
New York,San Francisco,2007.2,10.1,71.1
<end>Transform this Markdown structure to a csv format:
| Queries per Second | Connection Count | Average Latency (ms) | Timestamp |
| --- | --- | --- | --- |
| 3748.07 | 488 | 92.91 | 2021-03-07 06:37:14 |
| 1994.87 | 50 | 30.33 | 2023-11-18 02:02:15 |
| 3081.01 | 50 | 20.96 | 2021-05-25 15:10:08 |<start>
Queries per Second,Connection Count,Average Latency (ms),Timestamp
3748.07,488,92.91,2021-03-07 06:37:14
1994.87,50,30.33,2023-11-18 02:02:15
3081.01,50,20.96,2021-05-25 15:10:08
<end>Transform this plain text structure to a markdown format:
Name: Peggy | Age: 60 | Birth Month: October | City: Louisville | Income: 20000
Name: Clifford | Age: 43 | Birth Month: December | City: Indianapolis | Income: 195000
Name: Mathew | Age: 36 | Birth Month: July | City: New York | Income: 260000
Name: Maggie | Age: 63 | Birth Month: June | City: New York | Income: 280000
Name: Anne | Age: 28 | Birth Month: May | City: Memphis | Income: 400000
Name: Khloe | Age: 65 | Birth Month: May | City: Boston | Income: 200000
Name: Mamie | Age: 55 | Birth Month: December | City: Denver | Income: 225000
Name: Donovan | Age: 68 | Birth Month: February | City: Jacksonville | Income: 85000
Name: Carl | Age: 31 | Birth Month: July | City: Boston | Income: 275000
<start>
| Name | Age | Birth Month | City | Income |
| --- | --- | --- | --- | --- |
| Peggy | 60 | October | Louisville | 20000 |
| Clifford | 43 | December | Indianapolis | 195000 |
| Mathew | 36 | July | New York | 260000 |
| Maggie | 63 | June | New York | 280000 |
| Anne | 28 | May | Memphis | 400000 |
| Khloe | 65 | May | Boston | 200000 |
| Mamie | 55 | December | Denver | 225000 |
| Donovan | 68 | February | Jacksonville | 85000 |
| Carl | 31 | July | Boston | 275000 |
<end>Here's some Csv data, can you convert it to json?
Name,City,Income
Timothy,Detroit,410000
Alana,San Antonio,65000
Greyson,Dallas,295000
Craig,Washington,25000
Deborah,Louisville,20000
<start>
[
    {
        "Name": "Timothy",
        "City": "Detroit",
        "Income": 410000
    },
    {
        "Name": "Alana",
        "City": "San Antonio",
        "Income": 65000
    },
    {
        "Name": "Greyson",
        "City": "Dallas",
        "Income": 295000
    },
    {
        "Name": "Craig",
        "City": "Washington",
        "Income": 25000
    },
    {
        "Name": "Deborah",
        "City": "Louisville",
        "Income": 20000
    }
]
<end>Convert this csv to json:
Device ID,Battery Level (%),Reading Value,Timestamp
device-0002,18.8,82.32,2022-03-15 00:32:28
device-0071,85.2,68.87,2023-10-20 09:29:10
device-0008,52.5,-35.08,2023-07-24 14:47:15
device-0030,74.4,-32.76,2022-11-02 04:33:28
device-0082,48.3,19.48,2022-06-01 10:45:46
device-0014,54.4,-3.49,2022-04-22 16:03:44
device-0041,45.1,17.58,2023-06-17 12:10:29
device-0036,56.0,-12.39,2023-08-08 03:15:31
device-0091,63.5,17.58,2023-10-17 21:53:51
<start>
[
    {
        "Device ID": "device-0002",
        "Battery Level (%)": 18.8,
        "Reading Value": 82.32,
        "Timestamp": "2022-03-15 00:32:28"
    },
    {
        "Device ID": "device-0071",
        "Battery Level (%)": 85.2,
        "Reading Value": 68.87,
        "Timestamp": "2023-10-20 09:29:10"
    },
    {
        "Device ID": "device-0008",
        "Battery Level (%)": 52.5,
        "Reading Value": -35.08,
        "Timestamp": "2023-07-24 14:47:15"
    },
    {
        "Device ID": "device-0030",
        "Battery Level (%)": 74.4,
        "Reading Value": -32.76,
        "Timestamp": "2022-11-02 04:33:28"
    },
    {
        "Device ID": "device-0082",
        "Battery Level (%)": 48.3,
        "Reading Value": 19.48,
        "Timestamp": "2022-06-01 10:45:46"
    },
    {
        "Device ID": "device-0014",
        "Battery Level (%)": 54.4,
        "Reading Value": -3.49,
        "Timestamp": "2022-04-22 16:03:44"
    },
    {
        "Device ID": "device-0041",
        "Battery Level (%)": 45.1,
        "Reading Value": 17.58,
        "Timestamp": "2023-06-17 12:10:29"
    },
    {
        "Device ID": "device-0036",
        "Battery Level (%)": 56.0,
        "Reading Value": -12.39,
        "Timestamp": "2023-08-08 03:15:31"
    },
    {
        "Device ID": "device-0091",
        "Battery Level (%)": 63.5,
        "Reading Value": 17.58,
        "Timestamp": "2023-10-17 21:53:51"
    }
]
<end>Convert this plain text to csv:
Device Type: Pressure Sensor | Location: Hallway | Battery Level (%): 97.4 | Reading Value: 31.11 | Timestamp: 2023-01-06 07:57:29
Device Type: Humidity Sensor | Location: Garage | Battery Level (%): 62.6 | Reading Value: -6.71 | Timestamp: 2022-10-02 09:19:17
Device Type: Motion Detector | Location: Bathroom | Battery Level (%): 82.7 | Reading Value: 77.75 | Timestamp: 2021-03-17 16:08:20
Device Type: Light Sensor | Location: Living Room | Battery Level (%): 59.5 | Reading Value: 18.06 | Timestamp: 2023-01-01 09:34:28
Device Type: Temperature Sensor | Location: Bedroom | Battery Level (%): 34.8 | Reading Value: -17.23 | Timestamp: 2023-03-01 09:14:55
Device Type: Motion Detector | Location: Bathroom | Battery Level (%): 91.1 | Reading Value: 42.94 | Timestamp: 2023-08-20 07:42:17
Device Type: Pressure Sensor | Location: Kitchen | Battery Level (%): 36.4 | Reading Value: -6.22 | Timestamp: 2023-04-17 10:15:54
Device Type: Motion Detector | Location: Garage | Battery Level (%): 33.7 | Reading Value: -29.11 | Timestamp: 2021-11-22 02:51:28
Device Type: Light Sensor | Location: Garage | Battery Level (%): 85.2 | Reading Value: 31.11 | Timestamp: 2021-08-13 11:31:54
<start>
Device Type,Location,Battery Level (%),Reading Value,Timestamp
Pressure Sensor,Hallway,97.4,31.11,2023-01-06 07:57:29
Humidity Sensor,Garage,62.6,-6.71,2022-10-02 09:19:17
Motion Detector,Bathroom,82.7,77.75,2021-03-17 16:08:20
Light Sensor,Living Room,59.5,18.06,2023-01-01 09:34:28
Temperature Sensor,Bedroom,34.8,-17.23,2023-03-01 09:14:55
Motion Detector,Bathroom,91.1,42.94,2023-08-20 07:42:17
Pressure Sensor,Kitchen,36.4,-6.22,2023-04-17 10:15:54
Motion Detector,Garage,33.7,-29.11,2021-11-22 02:51:28
Light Sensor,Garage,85.2,31.11,2021-08-13 11:31:54
<end>Please transform the following MARKDOWN data into json:
| Rating | Price Range |
| --- | --- |
| 1 | $$$$$ |
| 3 | $ |
| 5 | $$$$ |
| 4 | $$ |
| 5 | $$$$ |
| 3 | $$$$ |
| 2 | $$$$ |
| 4 | $$$$$ |
| 5 | $$$$$ |
| 3 | $$$ |<start>
[
    {
        "Rating": 1,
        "Price Range": "$$$$$"
    },
    {
        "Rating": 3,
        "Price Range": "$"
    },
    {
        "Rating": 5,
        "Price Range": "$$$$"
    },
    {
        "Rating": 4,
        "Price Range": "$$"
    },
    {
        "Rating": 5,
        "Price Range": "$$$$"
    },
    {
        "Rating": 3,
        "Price Range": "$$$$"
    },
    {
        "Rating": 2,
        "Price Range": "$$$$"
    },
    {
        "Rating": 4,
        "Price Range": "$$$$$"
    },
    {
        "Rating": 5,
        "Price Range": "$$$$$"
    },
    {
        "Rating": 3,
        "Price Range": "$$$"
    }
]
<end>Please transform the following csv data into Markdown:
Restaurant Name,Cuisine,Location,Price Range
Pasta Palace,Japanese,Phoenix,$$$
BBQ Barn,American,Seattle,$$
Taco Town,Chinese,Los Angeles,$$$$$
Sushi World,Chinese,Chicago,$$
Pasta Palace,Japanese,San Francisco,$$$$
Curry Corner,Italian,Los Angeles,$$
Curry Corner,Indian,Los Angeles,$$$
Vegan Delight,Mediterranean,Phoenix,$$$$$
Burger Haven,Indian,Houston,$$
<start>
| Restaurant Name | Cuisine | Location | Price Range |
| --- | --- | --- | --- |
| Pasta Palace | Japanese | Phoenix | $$$ |
| BBQ Barn | American | Seattle | $$ |
| Taco Town | Chinese | Los Angeles | $$$$$ |
| Sushi World | Chinese | Chicago | $$ |
| Pasta Palace | Japanese | San Francisco | $$$$ |
| Curry Corner | Italian | Los Angeles | $$ |
| Curry Corner | Indian | Los Angeles | $$$ |
| Vegan Delight | Mediterranean | Phoenix | $$$$$ |
| Burger Haven | Indian | Houston | $$ |
<end>Convert this markdown to YML:
| Company | Sector | Market Cap | Stock Price | Quarter |
| --- | --- | --- | --- | --- |
| AutoDrive | Healthcare | Small Cap | 610.98 | Q1 |
| AeroSpace | Biotech | Large Cap | 115.76 | Q2 |
| TechCorp | Energy | Mega Cap | 14.42 | Q3 |
| RetailHub | Biotech | Mega Cap | 503.89 | Q4 |
| GlobalTrade | Energy | Large Cap | 671.58 | Q2 |
| HealthPlus | Technology | Small Cap | 318.8 | Q4 |
| EcoEnergy | Automotive | Large Cap | 318.8 | Q3 |<start>
- Company: AutoDrive
  Market Cap: Small Cap
  Quarter: Q1
  Sector: Healthcare
  Stock Price: 610.98
- Company: AeroSpace
  Market Cap: Large Cap
  Quarter: Q2
  Sector: Biotech
  Stock Price: 115.76
- Company: TechCorp
  Market Cap: Mega Cap
  Quarter: Q3
  Sector: Energy
  Stock Price: 14.42
- Company: RetailHub
  Market Cap: Mega Cap
  Quarter: Q4
  Sector: Biotech
  Stock Price: 503.89
- Company: GlobalTrade
  Market Cap: Large Cap
  Quarter: Q2
  Sector: Energy
  Stock Price: 671.58
- Company: HealthPlus
  Market Cap: Small Cap
  Quarter: Q4
  Sector: Technology
  Stock Price: 318.8
- Company: EcoEnergy
  Market Cap: Large Cap
  Quarter: Q3
  Sector: Automotive
  Stock Price: 318.8
<end>Here's some markdown data, can you convert it to Json?
| Trip Name | Start Location | End Location | Distance (miles) | Duration (hours) |
| --- | --- | --- | --- | --- |
| City Explorer | Chicago | Phoenix | 804.9 | 21.4 |
| Lakeside Retreat | San Francisco | Los Angeles | 1296.0 | 3.8 |
| Desert Drive | Phoenix | Chicago | 626.5 | 57.3 |
| Highway Odyssey | Miami | Houston | 2517.6 | 2.8 |<start>
[
    {
        "Trip Name": "City Explorer",
        "Start Location": "Chicago",
        "End Location": "Phoenix",
        "Distance (miles)": 804.9,
        "Duration (hours)": 21.4
    },
    {
        "Trip Name": "Lakeside Retreat",
        "Start Location": "San Francisco",
        "End Location": "Los Angeles",
        "Distance (miles)": 1296.0,
        "Duration (hours)": 3.8
    },
    {
        "Trip Name": "Desert Drive",
        "Start Location": "Phoenix",
        "End Location": "Chicago",
        "Distance (miles)": 626.5,
        "Duration (hours)": 57.3
    },
    {
        "Trip Name": "Highway Odyssey",
        "Start Location": "Miami",
        "End Location": "Houston",
        "Distance (miles)": 2517.6,
        "Duration (hours)": 2.8
    }
]
<end>Convert this markdown to JSON:
| Start Location | Duration (hours) | Fuel Used (gallons) |
| --- | --- | --- |
| Phoenix | 61.6 | 61.9 |
| Houston | 55.2 | 67.8 |
| Los Angeles | 35.7 | 13.0 |
| Houston | 55.5 | 68.1 |
| Miami | 43.9 | 82.4 |<start>
[
    {
        "Start Location": "Phoenix",
        "Duration (hours)": 61.6,
        "Fuel Used (gallons)": 61.9
    },
    {
        "Start Location": "Houston",
        "Duration (hours)": 55.2,
        "Fuel Used (gallons)": 67.8
    },
    {
        "Start Location": "Los Angeles",
        "Duration (hours)": 35.7,
        "Fuel Used (gallons)": 13.0
    },
    {
        "Start Location": "Houston",
        "Duration (hours)": 55.5,
        "Fuel Used (gallons)": 68.1
    },
    {
        "Start Location": "Miami",
        "Duration (hours)": 43.9,
        "Fuel Used (gallons)": 82.4
    }
]
<end>Please transform the following MARKDOWN data into PLAIN TEXT:
| Queries per Second | Cache Hit Ratio (%) | Average Latency (ms) |
| --- | --- | --- |
| 2343.22 | 78.46 | 9.1 |
| 3148.85 | 71.08 | 61.06 |
| 1512.29 | 91.38 | 7.33 |
| 1632.23 | 88.02 | 39.72 |
| 2319.76 | 94.25 | 97.24 |<start>
Queries per Second: 2343.22 | Cache Hit Ratio (%): 78.46 | Average Latency (ms): 9.1
Queries per Second: 3148.85 | Cache Hit Ratio (%): 71.08 | Average Latency (ms): 61.06
Queries per Second: 1512.29 | Cache Hit Ratio (%): 91.38 | Average Latency (ms): 7.33
Queries per Second: 1632.23 | Cache Hit Ratio (%): 88.02 | Average Latency (ms): 39.72
Queries per Second: 2319.76 | Cache Hit Ratio (%): 94.25 | Average Latency (ms): 97.24
<end>Transform this PLAIN TEXT structure to a markdown format:
Queries per Second: 1662.77 | Cache Hit Ratio (%): 93.74 | Connection Count: 140 | Timestamp: 2023-01-22 04:24:03
Queries per Second: 1348.67 | Cache Hit Ratio (%): 81.78 | Connection Count: 146 | Timestamp: 2021-12-10 05:48:53
Queries per Second: 2243.4 | Cache Hit Ratio (%): 84.98 | Connection Count: 371 | Timestamp: 2022-10-26 19:48:42
Queries per Second: 1234.29 | Cache Hit Ratio (%): 80.06 | Connection Count: 487 | Timestamp: 2023-12-19 07:54:13
Queries per Second: 3126.01 | Cache Hit Ratio (%): 72.21 | Connection Count: 352 | Timestamp: 2023-12-15 20:24:07
Queries per Second: 1737.61 | Cache Hit Ratio (%): 98.69 | Connection Count: 195 | Timestamp: 2021-01-22 04:18:54
<start>
| Queries per Second | Cache Hit Ratio (%) | Connection Count | Timestamp |
| --- | --- | --- | --- |
| 1662.77 | 93.74 | 140 | 2023-01-22 04:24:03 |
| 1348.67 | 81.78 | 146 | 2021-12-10 05:48:53 |
| 2243.4 | 84.98 | 371 | 2022-10-26 19:48:42 |
| 1234.29 | 80.06 | 487 | 2023-12-19 07:54:13 |
| 3126.01 | 72.21 | 352 | 2023-12-15 20:24:07 |
| 1737.61 | 98.69 | 195 | 2021-01-22 04:18:54 |
<end>Convert this markdown to Csv:
| Company | Date | Close Price | High Price |
| --- | --- | --- | --- |
| RetailWorld | 2012-05-23 | 288.2 | 873.44 |
| AeroSystems | 2010-08-20 | 697.28 | 834.65 |
| TechnoCorp | 2011-01-19 | 233.51 | 1196.21 |
| AutoMotive | 2019-01-06 | 41.04 | 465.87 |
| FoodChain | 2012-05-06 | 1003.09 | 1241.23 |
| HealthGen | 2011-09-07 | 1449.19 | 1457.86 |
| HealthGen | 2014-02-10 | 641.11 | 1241.23 |
| BioLife | 2013-02-11 | 15.97 | 1046.3 |
| GreenEnergy | 2013-07-21 | 1472.62 | 1472.62 |
| GreenEnergy | 2020-04-21 | 274.53 | 1299.09 |<start>
Company,Date,Close Price,High Price
RetailWorld,2012-05-23,288.2,873.44
AeroSystems,2010-08-20,697.28,834.65
TechnoCorp,2011-01-19,233.51,1196.21
AutoMotive,2019-01-06,41.04,465.87
FoodChain,2012-05-06,1003.09,1241.23
HealthGen,2011-09-07,1449.19,1457.86
HealthGen,2014-02-10,641.11,1241.23
BioLife,2013-02-11,15.97,1046.3
GreenEnergy,2013-07-21,1472.62,1472.62
GreenEnergy,2020-04-21,274.53,1299.09
<end>Convert this YAML to markdown:
- Day: Friday
  Humidity (%): 96
  Location: Seattle
- Day: Saturday
  Humidity (%): 64
  Location: Los Angeles
- Day: Sunday
  Humidity (%): 73
  Location: New York
- Day: Tuesday
  Humidity (%): 26
  Location: Chicago
- Day: Thursday
  Humidity (%): 22
  Location: Los Angeles
<start>
| Location | Humidity (%) | Day |
| --- | --- | --- |
| Seattle | 96 | Friday |
| Los Angeles | 64 | Saturday |
| New York | 73 | Sunday |
| Chicago | 26 | Tuesday |
| Los Angeles | 22 | Thursday |
<end>Please transform the following Csv data into JSON:
Age,Birth Month,City,Income
46,June,Baltimore,120000
58,December,Seattle,325000
34,June,Washington,290000
34,June,El Paso,155000
18,October,Fort Worth,470000
<start>
[
    {
        "Age": 46,
        "Birth Month": "June",
        "City": "Baltimore",
        "Income": 120000
    },
    {
        "Age": 58,
        "Birth Month": "December",
        "City": "Seattle",
        "Income": 325000
    },
    {
        "Age": 34,
        "Birth Month": "June",
        "City": "Washington",
        "Income": 290000
    },
    {
        "Age": 34,
        "Birth Month": "June",
        "City": "El Paso",
        "Income": 155000
    },
    {
        "Age": 18,
        "Birth Month": "October",
        "City": "Fort Worth",
        "Income": 470000
    }
]
<end>Can you change this plain text into MARKDOWN?
Name: Christy | Age: 57 | Birth Month: March
Name: Leland | Age: 39 | Birth Month: February
Name: Marjorie | Age: 36 | Birth Month: April
Name: Alicia | Age: 66 | Birth Month: August
<start>
| Name | Age | Birth Month |
| --- | --- | --- |
| Christy | 57 | March |
| Leland | 39 | February |
| Marjorie | 36 | April |
| Alicia | 66 | August |
<end>Can you change this json into CSV?
[
    {
        "Start Location": "New York",
        "End Location": "San Francisco",
        "Distance (miles)": 1870.2,
        "Duration (hours)": 49.2,
        "Fuel Used (gallons)": 35.0
    },
    {
        "Start Location": "Miami",
        "End Location": "San Francisco",
        "Distance (miles)": 1352.4,
        "Duration (hours)": 35.1,
        "Fuel Used (gallons)": 87.1
    },
    {
        "Start Location": "Denver",
        "End Location": "San Francisco",
        "Distance (miles)": 1784.5,
        "Duration (hours)": 40.0,
        "Fuel Used (gallons)": 93.2
    },
    {
        "Start Location": "Miami",
        "End Location": "Denver",
        "Distance (miles)": 2828.5,
        "Duration (hours)": 6.0,
        "Fuel Used (gallons)": 31.0
    }
]<start>
Start Location,End Location,Distance (miles),Duration (hours),Fuel Used (gallons)
New York,San Francisco,1870.2,49.2,35.0
Miami,San Francisco,1352.4,35.1,87.1
Denver,San Francisco,1784.5,40.0,93.2
Miami,Denver,2828.5,6.0,31.0
<end>Here's some plain text data, can you convert it to YAML?
Queries per Second: 911.38 | Cache Hit Ratio (%): 98.13 | Average Latency (ms): 71.02 | Timestamp: 2021-01-12 08:18:02
Queries per Second: 3013.46 | Cache Hit Ratio (%): 97.29 | Average Latency (ms): 66.19 | Timestamp: 2021-11-07 10:46:19
Queries per Second: 4020.71 | Cache Hit Ratio (%): 76.48 | Average Latency (ms): 80.64 | Timestamp: 2022-03-10 18:59:08
Queries per Second: 4882.85 | Cache Hit Ratio (%): 75.99 | Average Latency (ms): 65.25 | Timestamp: 2022-10-15 00:59:24
Queries per Second: 3902.4 | Cache Hit Ratio (%): 99.72 | Average Latency (ms): 29.38 | Timestamp: 2021-10-04 10:43:42
Queries per Second: 3110.34 | Cache Hit Ratio (%): 91.8 | Average Latency (ms): 37.91 | Timestamp: 2023-12-17 06:48:12
Queries per Second: 4222.57 | Cache Hit Ratio (%): 73.71 | Average Latency (ms): 24.06 | Timestamp: 2021-09-01 18:39:30
Queries per Second: 1095.28 | Cache Hit Ratio (%): 91.15 | Average Latency (ms): 32.61 | Timestamp: 2023-09-09 20:40:30
<start>
- Average Latency (ms): 71.02
  Cache Hit Ratio (%): 98.13
  Queries per Second: 911.38
  Timestamp: '2021-01-12 08:18:02'
- Average Latency (ms): 66.19
  Cache Hit Ratio (%): 97.29
  Queries per Second: 3013.46
  Timestamp: '2021-11-07 10:46:19'
- Average Latency (ms): 80.64
  Cache Hit Ratio (%): 76.48
  Queries per Second: 4020.71
  Timestamp: '2022-03-10 18:59:08'
- Average Latency (ms): 65.25
  Cache Hit Ratio (%): 75.99
  Queries per Second: 4882.85
  Timestamp: '2022-10-15 00:59:24'
- Average Latency (ms): 29.38
  Cache Hit Ratio (%): 99.72
  Queries per Second: 3902.4
  Timestamp: '2021-10-04 10:43:42'
- Average Latency (ms): 37.91
  Cache Hit Ratio (%): 91.8
  Queries per Second: 3110.34
  Timestamp: '2023-12-17 06:48:12'
- Average Latency (ms): 24.06
  Cache Hit Ratio (%): 73.71
  Queries per Second: 4222.57
  Timestamp: '2021-09-01 18:39:30'
- Average Latency (ms): 32.61
  Cache Hit Ratio (%): 91.15
  Queries per Second: 1095.28
  Timestamp: '2023-09-09 20:40:30'
<end>Convert this json to Csv:
[
    {
        "Name": "Adam",
        "Age": 45,
        "Birth Month": "June",
        "City": "San Francisco",
        "Income": 45000
    },
    {
        "Name": "Connor",
        "Age": 55,
        "Birth Month": "August",
        "City": "Houston",
        "Income": 425000
    },
    {
        "Name": "Aaron",
        "Age": 59,
        "Birth Month": "March",
        "City": "Los Angeles",
        "Income": 215000
    },
    {
        "Name": "Estella",
        "Age": 31,
        "Birth Month": "December",
        "City": "Baltimore",
        "Income": 105000
    },
    {
        "Name": "Celia",
        "Age": 35,
        "Birth Month": "August",
        "City": "Houston",
        "Income": 445000
    },
    {
        "Name": "Silas",
        "Age": 18,
        "Birth Month": "October",
        "City": "Dallas",
        "Income": 125000
    },
    {
        "Name": "Clara",
        "Age": 51,
        "Birth Month": "October",
        "City": "San Jose",
        "Income": 170000
    }
]<start>
Name,Age,Birth Month,City,Income
Adam,45,June,San Francisco,45000
Connor,55,August,Houston,425000
Aaron,59,March,Los Angeles,215000
Estella,31,December,Baltimore,105000
Celia,35,August,Houston,445000
Silas,18,October,Dallas,125000
Clara,51,October,San Jose,170000
<end>Here's some PLAIN TEXT data, can you convert it to json?
Start Location: New York | End Location: Houston | Distance (miles): 2397.1 | Duration (hours): 42.5
Start Location: Chicago | End Location: San Francisco | Distance (miles): 1674.0 | Duration (hours): 21.0
Start Location: Denver | End Location: San Francisco | Distance (miles): 915.6 | Duration (hours): 63.8
Start Location: Houston | End Location: Phoenix | Distance (miles): 2950.1 | Duration (hours): 44.2
Start Location: Phoenix | End Location: Houston | Distance (miles): 161.7 | Duration (hours): 68.3
Start Location: Houston | End Location: Los Angeles | Distance (miles): 1109.4 | Duration (hours): 71.7
Start Location: Miami | End Location: Houston | Distance (miles): 731.0 | Duration (hours): 6.3
<start>
[
    {
        "Start Location": "New York",
        "End Location": "Houston",
        "Distance (miles)": 2397.1,
        "Duration (hours)": 42.5
    },
    {
        "Start Location": "Chicago",
        "End Location": "San Francisco",
        "Distance (miles)": 1674.0,
        "Duration (hours)": 21.0
    },
    {
        "Start Location": "Denver",
        "End Location": "San Francisco",
        "Distance (miles)": 915.6,
        "Duration (hours)": 63.8
    },
    {
        "Start Location": "Houston",
        "End Location": "Phoenix",
        "Distance (miles)": 2950.1,
        "Duration (hours)": 44.2
    },
    {
        "Start Location": "Phoenix",
        "End Location": "Houston",
        "Distance (miles)": 161.7,
        "Duration (hours)": 68.3
    },
    {
        "Start Location": "Houston",
        "End Location": "Los Angeles",
        "Distance (miles)": 1109.4,
        "Duration (hours)": 71.7
    },
    {
        "Start Location": "Miami",
        "End Location": "Houston",
        "Distance (miles)": 731.0,
        "Duration (hours)": 6.3
    }
]
<end>Can you change this Csv into MARKDOWN?
Restaurant Name,Cuisine,Location,Rating,Price Range
The Golden Spoon,Italian,New York,3,$$$$$
The Steakhouse,Italian,San Francisco,2,$$
Taco Town,Italian,San Francisco,2,$
Sushi World,Mediterranean,Los Angeles,3,$$
Sushi World,Indian,Los Angeles,2,$$$
<start>
| Restaurant Name | Cuisine | Location | Rating | Price Range |
| --- | --- | --- | --- | --- |
| The Golden Spoon | Italian | New York | 3 | $$$$$ |
| The Steakhouse | Italian | San Francisco | 2 | $$ |
| Taco Town | Italian | San Francisco | 2 | $ |
| Sushi World | Mediterranean | Los Angeles | 3 | $$ |
| Sushi World | Indian | Los Angeles | 2 | $$$ |
<end>Can you change this Markdown into Yaml?
| Restaurant Name | Cuisine | Rating | Price Range |
| --- | --- | --- | --- |
| Sushi World | French | 3 | $$$ |
| Vegan Delight | Chinese | 3 | $$ |
| Curry Corner | French | 1 | $ |
| Taco Town | Japanese | 2 | $$$$$ |
| Pasta Palace | Indian | 2 | $$$$$ |
| Burger Haven | American | 5 | $$$ |
| The Golden Spoon | Mexican | 2 | $ |
| BBQ Barn | Chinese | 2 | $$$$$ |
| The Steakhouse | Mediterranean | 3 | $$$ |<start>
- Cuisine: French
  Price Range: $$$
  Rating: 3
  Restaurant Name: Sushi World
- Cuisine: Chinese
  Price Range: $$
  Rating: 3
  Restaurant Name: Vegan Delight
- Cuisine: French
  Price Range: $
  Rating: 1
  Restaurant Name: Curry Corner
- Cuisine: Japanese
  Price Range: $$$$$
  Rating: 2
  Restaurant Name: Taco Town
- Cuisine: Indian
  Price Range: $$$$$
  Rating: 2
  Restaurant Name: Pasta Palace
- Cuisine: American
  Price Range: $$$
  Rating: 5
  Restaurant Name: Burger Haven
- Cuisine: Mexican
  Price Range: $
  Rating: 2
  Restaurant Name: The Golden Spoon
- Cuisine: Chinese
  Price Range: $$$$$
  Rating: 2
  Restaurant Name: BBQ Barn
- Cuisine: Mediterranean
  Price Range: $$$
  Rating: 3
  Restaurant Name: The Steakhouse
<end>Transform this MARKDOWN structure to a Csv format:
| Device ID | Reading Value | Timestamp |
| --- | --- | --- |
| device-0078 | 28.1 | 2023-12-08 05:00:45 |
| device-0076 | -3.36 | 2022-03-12 06:47:58 |
| device-0071 | 18.36 | 2023-09-13 16:31:05 |
| device-0053 | 0.43 | 2022-10-13 19:02:10 |
| device-0047 | 42.99 | 2021-01-23 03:47:48 |
| device-0063 | -1.81 | 2021-02-10 20:29:33 |<start>
Device ID,Reading Value,Timestamp
device-0078,28.1,2023-12-08 05:00:45
device-0076,-3.36,2022-03-12 06:47:58
device-0071,18.36,2023-09-13 16:31:05
device-0053,0.43,2022-10-13 19:02:10
device-0047,42.99,2021-01-23 03:47:48
device-0063,-1.81,2021-02-10 20:29:33
<end>Can you change this markdown into YAML?
| Title | Director | Genre | Release Year | Box Office Earnings (M) |
| --- | --- | --- | --- | --- |
| Edge of Infinity | Cade Firebrand | Horror | 1999 | 554.17 |
| Edge of Infinity | Rylan Frostblade | Comedy | 2018 | 860.67 |
| The Endless Horizon | Talon Blackthorn | Fantasy | 1976 | 680.38 |
| Rise of the Titans | Cade Firebrand | Horror | 2004 | 41.66 |
| Mystery of the Depths | Talon Blackthorn | Horror | 2017 | 749.66 |
| Rise of the Titans | Drake Nightshade | Adventure | 1987 | 749.66 |
| Mystery of the Depths | Orin Shadowalker | Fantasy | 1990 | 798.4 |
| Dreamwalker | Zara Stormrider | Sci-Fi | 2015 | 480.16 |
| The Endless Horizon | Zara Stormrider | Drama | 1976 | 772.43 |<start>
- Box Office Earnings (M): 554.17
  Director: Cade Firebrand
  Genre: Horror
  Release Year: 1999
  Title: Edge of Infinity
- Box Office Earnings (M): 860.67
  Director: Rylan Frostblade
  Genre: Comedy
  Release Year: 2018
  Title: Edge of Infinity
- Box Office Earnings (M): 680.38
  Director: Talon Blackthorn
  Genre: Fantasy
  Release Year: 1976
  Title: The Endless Horizon
- Box Office Earnings (M): 41.66
  Director: Cade Firebrand
  Genre: Horror
  Release Year: 2004
  Title: Rise of the Titans
- Box Office Earnings (M): 749.66
  Director: Talon Blackthorn
  Genre: Horror
  Release Year: 2017
  Title: Mystery of the Depths
- Box Office Earnings (M): 749.66
  Director: Drake Nightshade
  Genre: Adventure
  Release Year: 1987
  Title: Rise of the Titans
- Box Office Earnings (M): 798.4
  Director: Orin Shadowalker
  Genre: Fantasy
  Release Year: 1990
  Title: Mystery of the Depths
- Box Office Earnings (M): 480.16
  Director: Zara Stormrider
  Genre: Sci-Fi
  Release Year: 2015
  Title: Dreamwalker
- Box Office Earnings (M): 772.43
  Director: Zara Stormrider
  Genre: Drama
  Release Year: 1976
  Title: The Endless Horizon
<end>Can you change this plain text into yaml?
Device ID: device-0078 | Device Type: Motion Detector | Battery Level (%): 39.8 | Reading Value: -6.96 | Timestamp: 2022-10-13 23:32:28
Device ID: device-0034 | Device Type: Pressure Sensor | Battery Level (%): 64.4 | Reading Value: -10.76 | Timestamp: 2022-06-07 10:53:48
Device ID: device-0008 | Device Type: Light Sensor | Battery Level (%): 52.6 | Reading Value: 18.73 | Timestamp: 2021-02-24 20:56:05
<start>
- Battery Level (%): 39.8
  Device ID: device-0078
  Device Type: Motion Detector
  Reading Value: -6.96
  Timestamp: '2022-10-13 23:32:28'
- Battery Level (%): 64.4
  Device ID: device-0034
  Device Type: Pressure Sensor
  Reading Value: -10.76
  Timestamp: '2022-06-07 10:53:48'
- Battery Level (%): 52.6
  Device ID: device-0008
  Device Type: Light Sensor
  Reading Value: 18.73
  Timestamp: '2021-02-24 20:56:05'
<end>Transform this markdown structure to a Yaml format:
| Device ID | Device Type | Location | Battery Level (%) | Reading Value | Timestamp |
| --- | --- | --- | --- | --- | --- |
| device-0024 | Light Sensor | Office | 74.9 | -33.03 | 2022-01-13 17:02:51 |
| device-0074 | Temperature Sensor | Garden | 34.3 | 11.61 | 2023-11-18 09:08:53 |
| device-0067 | Temperature Sensor | Bedroom | 41.8 | 60.21 | 2022-03-03 21:53:48 |
| device-0084 | Pressure Sensor | Bathroom | 56.3 | -3.31 | 2021-02-10 20:04:05 |
| device-0034 | Pressure Sensor | Bathroom | 67.0 | 69.57 | 2022-01-17 21:23:04 |
| device-0087 | Temperature Sensor | Bathroom | 65.4 | 28.32 | 2023-01-28 10:28:38 |<start>
- Battery Level (%): 74.9
  Device ID: device-0024
  Device Type: Light Sensor
  Location: Office
  Reading Value: -33.03
  Timestamp: '2022-01-13 17:02:51'
- Battery Level (%): 34.3
  Device ID: device-0074
  Device Type: Temperature Sensor
  Location: Garden
  Reading Value: 11.61
  Timestamp: '2023-11-18 09:08:53'
- Battery Level (%): 41.8
  Device ID: device-0067
  Device Type: Temperature Sensor
  Location: Bedroom
  Reading Value: 60.21
  Timestamp: '2022-03-03 21:53:48'
- Battery Level (%): 56.3
  Device ID: device-0084
  Device Type: Pressure Sensor
  Location: Bathroom
  Reading Value: -3.31
  Timestamp: '2021-02-10 20:04:05'
- Battery Level (%): 67.0
  Device ID: device-0034
  Device Type: Pressure Sensor
  Location: Bathroom
  Reading Value: 69.57
  Timestamp: '2022-01-17 21:23:04'
- Battery Level (%): 65.4
  Device ID: device-0087
  Device Type: Temperature Sensor
  Location: Bathroom
  Reading Value: 28.32
  Timestamp: '2023-01-28 10:28:38'
<end>Here's some Json data, can you convert it to YML?
[
    {
        "Device Type": "Light Sensor",
        "Location": "Office",
        "Battery Level (%)": 44.4,
        "Reading Value": -33.83
    },
    {
        "Device Type": "Temperature Sensor",
        "Location": "Garage",
        "Battery Level (%)": 96.0,
        "Reading Value": 63.77
    },
    {
        "Device Type": "Pressure Sensor",
        "Location": "Kitchen",
        "Battery Level (%)": 60.9,
        "Reading Value": 11.8
    },
    {
        "Device Type": "Pressure Sensor",
        "Location": "Bedroom",
        "Battery Level (%)": 31.5,
        "Reading Value": 7.64
    },
    {
        "Device Type": "Motion Detector",
        "Location": "Living Room",
        "Battery Level (%)": 96.7,
        "Reading Value": -5.6
    }
]<start>
- Battery Level (%): 44.4
  Device Type: Light Sensor
  Location: Office
  Reading Value: -33.83
- Battery Level (%): 96.0
  Device Type: Temperature Sensor
  Location: Garage
  Reading Value: 63.77
- Battery Level (%): 60.9
  Device Type: Pressure Sensor
  Location: Kitchen
  Reading Value: 11.8
- Battery Level (%): 31.5
  Device Type: Pressure Sensor
  Location: Bedroom
  Reading Value: 7.64
- Battery Level (%): 96.7
  Device Type: Motion Detector
  Location: Living Room
  Reading Value: -5.6
<end>Transform this CSV structure to a plain text format:
Product Name,SKU,Price,Stock Quantity,Supplier Name
Widget,SKU-1082,242.75,333,Wayne Enterprises
Gadget,SKU-1053,494.66,454,ACME Corp
Device,SKU-1036,414.49,97,Globex
Gadget,SKU-1051,18.63,437,Globex
Whatchamacallit,SKU-1007,128.91,419,Wayne Enterprises
Instrument,SKU-1053,391.0,362,Wonka Industries
Contraption,SKU-1073,114.24,252,ACME Corp
Thingamajig,SKU-1003,405.57,265,Umbrella Corp
<start>
Product Name: Widget | SKU: SKU-1082 | Price: 242.75 | Stock Quantity: 333 | Supplier Name: Wayne Enterprises
Product Name: Gadget | SKU: SKU-1053 | Price: 494.66 | Stock Quantity: 454 | Supplier Name: ACME Corp
Product Name: Device | SKU: SKU-1036 | Price: 414.49 | Stock Quantity: 97 | Supplier Name: Globex
Product Name: Gadget | SKU: SKU-1051 | Price: 18.63 | Stock Quantity: 437 | Supplier Name: Globex
Product Name: Whatchamacallit | SKU: SKU-1007 | Price: 128.91 | Stock Quantity: 419 | Supplier Name: Wayne Enterprises
Product Name: Instrument | SKU: SKU-1053 | Price: 391.0 | Stock Quantity: 362 | Supplier Name: Wonka Industries
Product Name: Contraption | SKU: SKU-1073 | Price: 114.24 | Stock Quantity: 252 | Supplier Name: ACME Corp
Product Name: Thingamajig | SKU: SKU-1003 | Price: 405.57 | Stock Quantity: 265 | Supplier Name: Umbrella Corp
<end>Transform this markdown structure to a yml format:
| Title | Director | Genre | Release Year | Box Office Earnings (M) |
| --- | --- | --- | --- | --- |
| Mystery of the Depths | Cade Firebrand | Drama | 1979 | 991.08 |
| Beyond the Veil | Aria Ravenwood | Thriller | 1997 | 992.78 |
| Mystery of the Depths | Drake Nightshade | Fantasy | 2004 | 470.37 |<start>
- Box Office Earnings (M): 991.08
  Director: Cade Firebrand
  Genre: Drama
  Release Year: 1979
  Title: Mystery of the Depths
- Box Office Earnings (M): 992.78
  Director: Aria Ravenwood
  Genre: Thriller
  Release Year: 1997
  Title: Beyond the Veil
- Box Office Earnings (M): 470.37
  Director: Drake Nightshade
  Genre: Fantasy
  Release Year: 2004
  Title: Mystery of the Depths
<end>Can you change this csv into plain text?
Product Name,SKU,Price,Category,Supplier Name
Device,SKU-1020,22.54,Sports,Umbrella Corp
Device,SKU-1042,329.34,Electronics,Wayne Enterprises
Gizmo,SKU-1034,251.5,Toys,Wayne Enterprises
Device,SKU-1050,170.17,Automotive,ACME Corp
Instrument,SKU-1033,421.27,Sports,Wayne Enterprises
Instrument,SKU-1096,82.45,Electronics,Umbrella Corp
Gizmo,SKU-1057,270.11,Automotive,Wonka Industries
Instrument,SKU-1071,248.63,Household,Wonka Industries
Device,SKU-1015,471.19,Household,Wonka Industries
Device,SKU-1044,438.83,Electronics,Wayne Enterprises
<start>
Product Name: Device | SKU: SKU-1020 | Price: 22.54 | Category: Sports | Supplier Name: Umbrella Corp
Product Name: Device | SKU: SKU-1042 | Price: 329.34 | Category: Electronics | Supplier Name: Wayne Enterprises
Product Name: Gizmo | SKU: SKU-1034 | Price: 251.5 | Category: Toys | Supplier Name: Wayne Enterprises
Product Name: Device | SKU: SKU-1050 | Price: 170.17 | Category: Automotive | Supplier Name: ACME Corp
Product Name: Instrument | SKU: SKU-1033 | Price: 421.27 | Category: Sports | Supplier Name: Wayne Enterprises
Product Name: Instrument | SKU: SKU-1096 | Price: 82.45 | Category: Electronics | Supplier Name: Umbrella Corp
Product Name: Gizmo | SKU: SKU-1057 | Price: 270.11 | Category: Automotive | Supplier Name: Wonka Industries
Product Name: Instrument | SKU: SKU-1071 | Price: 248.63 | Category: Household | Supplier Name: Wonka Industries
Product Name: Device | SKU: SKU-1015 | Price: 471.19 | Category: Household | Supplier Name: Wonka Industries
Product Name: Device | SKU: SKU-1044 | Price: 438.83 | Category: Electronics | Supplier Name: Wayne Enterprises
<end>Can you change this PLAIN TEXT into markdown?
Title: Mystery of the Depths | Director: Rylan Frostblade
Title: The Endless Horizon | Director: Mara Moonshadow
Title: Beyond the Veil | Director: Selene Darkwhisper
Title: Dreamwalker | Director: Zara Stormrider
Title: Mystery of the Depths | Director: Orin Shadowalker
Title: Edge of Infinity | Director: Lira Silverleaf
Title: Edge of Infinity | Director: Zara Stormrider
Title: Edge of Infinity | Director: Zara Stormrider
<start>
| Title | Director |
| --- | --- |
| Mystery of the Depths | Rylan Frostblade |
| The Endless Horizon | Mara Moonshadow |
| Beyond the Veil | Selene Darkwhisper |
| Dreamwalker | Zara Stormrider |
| Mystery of the Depths | Orin Shadowalker |
| Edge of Infinity | Lira Silverleaf |
| Edge of Infinity | Zara Stormrider |
| Edge of Infinity | Zara Stormrider |
<end>Can you change this YML into MARKDOWN?
- Age: 44
  Birth Month: November
- Age: 65
  Birth Month: January
- Age: 68
  Birth Month: January
- Age: 50
  Birth Month: April
- Age: 35
  Birth Month: February
- Age: 64
  Birth Month: January
<start>
| Age | Birth Month |
| --- | --- |
| 44 | November |
| 65 | January |
| 68 | January |
| 50 | April |
| 35 | February |
| 64 | January |
<end>Please transform the following plain text data into markdown:
Database Name: MetricsDB | Queries per Second: 4310.61 | Cache Hit Ratio (%): 76.45 | Connection Count: 408 | Average Latency (ms): 88.41 | Timestamp: 2023-05-12 11:01:18
Database Name: MetricsDB | Queries per Second: 905.48 | Cache Hit Ratio (%): 83.82 | Connection Count: 181 | Average Latency (ms): 95.88 | Timestamp: 2023-08-04 12:08:36
Database Name: InventoryDB | Queries per Second: 4638.46 | Cache Hit Ratio (%): 87.71 | Connection Count: 246 | Average Latency (ms): 29.81 | Timestamp: 2021-03-22 10:19:37
Database Name: InventoryDB | Queries per Second: 4861.82 | Cache Hit Ratio (%): 71.6 | Connection Count: 486 | Average Latency (ms): 62.35 | Timestamp: 2023-10-06 16:00:36
Database Name: ProductsDB | Queries per Second: 4962.83 | Cache Hit Ratio (%): 76.1 | Connection Count: 479 | Average Latency (ms): 39.52 | Timestamp: 2021-06-25 20:52:00
Database Name: AnalyticsDB | Queries per Second: 4007.9 | Cache Hit Ratio (%): 80.52 | Connection Count: 85 | Average Latency (ms): 68.81 | Timestamp: 2021-08-11 08:05:04
Database Name: SalesDB | Queries per Second: 1702.47 | Cache Hit Ratio (%): 90.41 | Connection Count: 31 | Average Latency (ms): 27.09 | Timestamp: 2021-03-05 06:36:12
Database Name: InventoryDB | Queries per Second: 751.87 | Cache Hit Ratio (%): 93.54 | Connection Count: 207 | Average Latency (ms): 42.97 | Timestamp: 2023-06-22 14:27:16
Database Name: MetricsDB | Queries per Second: 1221.97 | Cache Hit Ratio (%): 89.8 | Connection Count: 92 | Average Latency (ms): 47.21 | Timestamp: 2022-05-28 19:11:28
<start>
| Database Name | Queries per Second | Cache Hit Ratio (%) | Connection Count | Average Latency (ms) | Timestamp |
| --- | --- | --- | --- | --- | --- |
| MetricsDB | 4310.61 | 76.45 | 408 | 88.41 | 2023-05-12 11:01:18 |
| MetricsDB | 905.48 | 83.82 | 181 | 95.88 | 2023-08-04 12:08:36 |
| InventoryDB | 4638.46 | 87.71 | 246 | 29.81 | 2021-03-22 10:19:37 |
| InventoryDB | 4861.82 | 71.6 | 486 | 62.35 | 2023-10-06 16:00:36 |
| ProductsDB | 4962.83 | 76.1 | 479 | 39.52 | 2021-06-25 20:52:00 |
| AnalyticsDB | 4007.9 | 80.52 | 85 | 68.81 | 2021-08-11 08:05:04 |
| SalesDB | 1702.47 | 90.41 | 31 | 27.09 | 2021-03-05 06:36:12 |
| InventoryDB | 751.87 | 93.54 | 207 | 42.97 | 2023-06-22 14:27:16 |
| MetricsDB | 1221.97 | 89.8 | 92 | 47.21 | 2022-05-28 19:11:28 |
<end>Please transform the following csv data into markdown:
Company,Close Price,High Price,Low Price
BioLife,477.62,1338.38,398.98
RetailWorld,563.05,1372.0,563.05
BioLife,827.53,1394.41,215.1
AeroSystems,1173.56,1173.56,423.33
HealthGen,1446.91,1446.91,348.86
MediaGroup,1302.45,1302.45,1289.08
<start>
| Company | Close Price | High Price | Low Price |
| --- | --- | --- | --- |
| BioLife | 477.62 | 1338.38 | 398.98 |
| RetailWorld | 563.05 | 1372.0 | 563.05 |
| BioLife | 827.53 | 1394.41 | 215.1 |
| AeroSystems | 1173.56 | 1173.56 | 423.33 |
| HealthGen | 1446.91 | 1446.91 | 348.86 |
| MediaGroup | 1302.45 | 1302.45 | 1289.08 |
<end>Convert this plain text to Yml:
Trip Name: Highway Odyssey | Duration (hours): 40.2 | Fuel Used (gallons): 62.2
Trip Name: Lakeside Retreat | Duration (hours): 54.1 | Fuel Used (gallons): 100.0
Trip Name: City Explorer | Duration (hours): 51.4 | Fuel Used (gallons): 93.6
Trip Name: Lakeside Retreat | Duration (hours): 40.1 | Fuel Used (gallons): 64.9
Trip Name: Coast to Coast | Duration (hours): 65.8 | Fuel Used (gallons): 71.3
Trip Name: Desert Drive | Duration (hours): 59.5 | Fuel Used (gallons): 85.0
Trip Name: City Explorer | Duration (hours): 51.0 | Fuel Used (gallons): 74.7
Trip Name: Historic Route | Duration (hours): 56.2 | Fuel Used (gallons): 74.7
Trip Name: Coast to Coast | Duration (hours): 72.0 | Fuel Used (gallons): 96.5
Trip Name: Historic Route | Duration (hours): 43.8 | Fuel Used (gallons): 18.4
<start>
- Duration (hours): 40.2
  Fuel Used (gallons): 62.2
  Trip Name: Highway Odyssey
- Duration (hours): 54.1
  Fuel Used (gallons): 100.0
  Trip Name: Lakeside Retreat
- Duration (hours): 51.4
  Fuel Used (gallons): 93.6
  Trip Name: City Explorer
- Duration (hours): 40.1
  Fuel Used (gallons): 64.9
  Trip Name: Lakeside Retreat
- Duration (hours): 65.8
  Fuel Used (gallons): 71.3
  Trip Name: Coast to Coast
- Duration (hours): 59.5
  Fuel Used (gallons): 85.0
  Trip Name: Desert Drive
- Duration (hours): 51.0
  Fuel Used (gallons): 74.7
  Trip Name: City Explorer
- Duration (hours): 56.2
  Fuel Used (gallons): 74.7
  Trip Name: Historic Route
- Duration (hours): 72.0
  Fuel Used (gallons): 96.5
  Trip Name: Coast to Coast
- Duration (hours): 43.8
  Fuel Used (gallons): 18.4
  Trip Name: Historic Route
<end>Here's some markdown data, can you convert it to yaml?
| Database Name | Queries per Second | Cache Hit Ratio (%) | Connection Count | Average Latency (ms) | Timestamp |
| --- | --- | --- | --- | --- | --- |
| LogsDB | 505.79 | 81.36 | 57 | 32.08 | 2022-08-22 05:00:44 |
| LogsDB | 2718.01 | 72.04 | 49 | 19.84 | 2023-10-10 20:55:21 |
| LogsDB | 4358.29 | 72.77 | 444 | 11.06 | 2021-11-24 09:53:56 |
| UserDB | 2042.86 | 84.05 | 287 | 38.8 | 2023-02-24 23:28:49 |
| MetricsDB | 2135.76 | 77.32 | 264 | 11.06 | 2023-06-28 04:21:56 |<start>
- Average Latency (ms): 32.08
  Cache Hit Ratio (%): 81.36
  Connection Count: 57
  Database Name: LogsDB
  Queries per Second: 505.79
  Timestamp: '2022-08-22 05:00:44'
- Average Latency (ms): 19.84
  Cache Hit Ratio (%): 72.04
  Connection Count: 49
  Database Name: LogsDB
  Queries per Second: 2718.01
  Timestamp: '2023-10-10 20:55:21'
- Average Latency (ms): 11.06
  Cache Hit Ratio (%): 72.77
  Connection Count: 444
  Database Name: LogsDB
  Queries per Second: 4358.29
  Timestamp: '2021-11-24 09:53:56'
- Average Latency (ms): 38.8
  Cache Hit Ratio (%): 84.05
  Connection Count: 287
  Database Name: UserDB
  Queries per Second: 2042.86
  Timestamp: '2023-02-24 23:28:49'
- Average Latency (ms): 11.06
  Cache Hit Ratio (%): 77.32
  Connection Count: 264
  Database Name: MetricsDB
  Queries per Second: 2135.76
  Timestamp: '2023-06-28 04:21:56'
<end>Please transform the following Plain text data into JSON:
Queries per Second: 3874.73 | Cache Hit Ratio (%): 94.53 | Average Latency (ms): 97.34
Queries per Second: 3956.67 | Cache Hit Ratio (%): 75.94 | Average Latency (ms): 18.44
Queries per Second: 3310.58 | Cache Hit Ratio (%): 84.62 | Average Latency (ms): 84.73
<start>
[
    {
        "Queries per Second": 3874.73,
        "Cache Hit Ratio (%)": 94.53,
        "Average Latency (ms)": 97.34
    },
    {
        "Queries per Second": 3956.67,
        "Cache Hit Ratio (%)": 75.94,
        "Average Latency (ms)": 18.44
    },
    {
        "Queries per Second": 3310.58,
        "Cache Hit Ratio (%)": 84.62,
        "Average Latency (ms)": 84.73
    }
]
<end>Here's some json data, can you convert it to PLAIN TEXT?
[
    {
        "Humidity (%)": 95,
        "Wind Speed (km/h)": 29.1,
        "Day": "Tuesday"
    },
    {
        "Humidity (%)": 70,
        "Wind Speed (km/h)": 10.2,
        "Day": "Friday"
    },
    {
        "Humidity (%)": 85,
        "Wind Speed (km/h)": 6.7,
        "Day": "Tuesday"
    }
]<start>
Humidity (%): 95 | Wind Speed (km/h): 29.1 | Day: Tuesday
Humidity (%): 70 | Wind Speed (km/h): 10.2 | Day: Friday
Humidity (%): 85 | Wind Speed (km/h): 6.7 | Day: Tuesday
<end>