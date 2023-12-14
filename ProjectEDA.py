import streamlit as st

import pandas as pd
import numpy as np
import plotly.express as px
import statsmodels.api as sm

st.set_page_config(page_title="projectEDA")

st.write("# Project: Airport EDA")

st.markdown(
    """
    ### Introduction 
    
    Introduction
    At the onset of the COVID pandemic in 2020, many opted to stop traveling and there was a 
    noticeable decline in airport travel. By 2022, airports seemed to be back to pre-pandemic 
    business. I want to investigate 2022 statistics for the most popular airports in the United 
    States.  
    """)

airports = pd.read_csv('2022Airports.csv')

airports.loc[airports['Airport'] == 'Luis Munoz Marin International Airport', 'State'] = 'US Territory'

st.write("# Dataset")
st.dataframe(airports) 

st.markdown(
    """
    ### About the Data

    I created an extensive table for the top 200 ranked airports in the United States. Data for 
    this ranked list was sourced from the Bureau of Transportation Statistics. 

    DataCleaning.ipynb is where the data was cleaned and organized. 
    - The ranked list file that was read into python needed to be cleaned. 
    - I cleaned it using a LOCID table and a supplementary LOCID table. 
    - Next, I added originating and enplaned passenger data for each airport. 
    - Then, I used rapidAPI to get ICAO codes for each row.
    - Next, I used a second API and the ICAO values to get long, lat, etc. columns. 
    - Last, I found a blog that compiled an updated table of US airports for 2020 and 
    interesting statistics. I accessed the table as a text file and merged it onto my pandas 
    DataFrame. 

    I saved this table as a csv file which can be viewed above. 

    # EDA

    In this EDA, I want to exlpore the relationship bewteen *2022 Delays* proportion and 
    other quantitative variables using a scatterplot.
        
    Then, I want to perform a regression analysis for the Q → Q scatterplots.
    """)

#  filters
st.write("### Scatterplot Filters")
selected_variable = st.selectbox("Select Variable for X-axis", ['Elevation', '2022 Enplaned Passengers'])

fig = px.scatter(airports, x=selected_variable, y='Delays',
                 hover_data={'Airport': True, 'IATA': True, '2022 Rank': True, selected_variable: True, 'Delays': True},
                 color_discrete_sequence=['#4b7b9b'])

# Add trendline using statsmodels
X = sm.add_constant(airports[selected_variable])
y = airports['Delays']
model = sm.OLS(y, X).fit()
line = pd.DataFrame({selected_variable: [airports[selected_variable].min(), airports[selected_variable].max()]})
line['Delays'] = model.predict(sm.add_constant(line[selected_variable]))

fig.add_scatter(x=line[selected_variable], y=line['Delays'], mode='lines', name='Regression Line', line=dict(color='#00204e', width=2))

# Update layout
fig.update_traces(marker=dict(size=10, line=dict(width=2, color='#00204e')), selector=dict(mode='markers'))
fig.update_layout(title=f'Top 200 Airports 2022: Delays vs. {selected_variable} Insights',
                  xaxis_title=f'{selected_variable}',
                  yaxis_title='Delays (2022 proportion)',
                  height=650,
                  width=800)

st.plotly_chart(fig)

# Get regression results
X = sm.add_constant(airports[selected_variable])
y = airports['Delays']
model = sm.OLS(y, X).fit()

# Display regression results
st.write("### Regression Analysis Results")
st.write(model.summary())

st.write('### Barchart Analysis')
st.write('Now, I want to compare *Avg. Delay (Mins)* by *State* in a bar chart sorted from greatest to least average delay.')


stateAvgDelays = airports.groupby('State')['Delays'].mean().reset_index()
stateAvgDelays = stateAvgDelays.sort_values(by='Delays', ascending=True)

bars = px.bar(stateAvgDelays, x='Delays', y='State',color_discrete_sequence=['#4b7b9b',],height=900,
                width=700,
                title='Top 200 Airports 2022: Average Delays by State')

st.plotly_chart(bars)


#  filters
st.write("### Barchart Filters")

selected_state = st.selectbox("Select State", airports['State'].unique())

# Apply filters to the dataframe
filtered_airports = airports[(airports['State'] == selected_state)]

fig = px.bar(filtered_airports, x='Delays', y='Airport',color_discrete_sequence=['#4b7b9b',],height=450,
                width=800,
                title='Top 200 Airports 2022: Average Delays by State')

st.plotly_chart(fig)


st.dataframe(filtered_airports)


st.write("# Analysis")
st.markdown(
    """ 
    In the regression analysis, there is a stronger relationship between 2022 Enplaned Passengers and Delays than Elevation.   
    However, the R-squared value between Enplaned Passengers and Delays is only **0.085**, which indicated a weak relationship. 

    The R-squared value between Elevation and Delays is only **0.006**, which indicated almost no relationship. 

    The barchart allows us to see the average delay by state. The states with the lowest average delay include Hawaii, Alaska, and Idaho.
    Using the drop down menu, we can investigate the yearly delays for each airport in the chosen state.  


    """)