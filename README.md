# 386Project

Lucy Storts   
Stat 386 - Dr. Tass - BYU     
12/14/2023    

## Introduction
As an out-of-state college student, I have spent a lot of time in airports and  a lot of time flying back and forth across the country. I grew up in Ohio and the fastest way for me to visit my family is by plane. I want to investigate 2022 statistics for the most popular airports in the United States.  

I created an extensive table for the top 200 ranked airports in the United States. Data for this ranked list was sourced from the Bureau of Transportation Statistics*1*. 

## Important Files
### DataCleaning.ipynb 
Used to clean and organize the data. 
- The ranked list file that was read into python needed to be cleaned. 
- I cleaned it using a LOCID table*2* and a supplementary LOCID table*3*. 
- Next, I added originating*4* and enplaned*5* passenger data for each airport. 
- Then, I used rapidAPI*6* to get ICAO codes for each row.
- Next, I used a second API*7* and the ICAO values to get long, lat, etc. columns. 
- Last, I found a blog*8* that compiled an updated table of US airports for 2020 and interesting statistics. I accessed the table as a text file and merged it onto my pandas DataFrame. 
- I exported my dataframe to 2022Airports.csv. 

### EDA.ipynb
I performed a simple exploratory data analysis so that I could create a streamlit app and include interactive features. I want to exlpore the relationship bewteen *2022 Delays* proportion and 
other quantitative variables using a scatterplot. Then, I will to perform a regression 
analysis for the Q → Q scatterplots. After, I will use a barchart to analyze Average Delay on a State level. I included a filter for State so that we can investigate the individual airport Average Delays per state. 

### ProjectEDA.py
This file contains the code necessary to create my streamlit app that I used for the exploratory data analysis. 
The *requirements.txt* file includes the libraries needed for the streamlit app. 

[Streamlit EDA](https://airportprojecteda.streamlit.app/)

### Potential Data Folder 
This folder holds all the downloaded data I used to create my data set. References for where the data was found is below. Also, when I created DataCleaning.ipynb, I included notes and documentation for each of the sources I was using. *Note: I did not use all the files.*

## Sources 
*1*  https://www.bts.gov/topics/airlines-and-airports/airport-rankings-2022  
*2*  https://www.faa.gov/data_research   
*3*  Requested unknown LOCID values for the remaining airports from chatGPT (extraLOCID.txt)   
*4*  OriginatingPassengers - U.S. Airports ranked by 2022 Originating Domestic Passengers    
&emsp; Source: Bureau of Transportation Statistics, Origin & Destination Survey   
&emsp; DB1B Ticket, Based on 10 Percent Ticket Sample   
&emsp; O&D numbers are not comparable to T-100 Market Enplanement numbers     
*5*  Bureau of Transportation Statistics DB  
*6*  https://rapidapi.com/proground/api/aviation-reference-data   
*7*   https://airportdb.io/#   
*8*  https://www.stratosjets.com/blog/us-airport-rankings/   

