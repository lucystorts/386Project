import streamlit as st

import pandas as pd
import numpy as np
import plotly.express as px
import statsmodels.api as sm

st.set_page_config(page_title="projectEDA")

st.write("# Project: EDA")

airports = pd.read_csv('2022Airports.csv')

airports.loc[airports['Airport'] == 'Luis Munoz Marin International Airport', 'State'] = 'US Territory'

st.markdown(
    """
    Check out my [blog post](https://lucystorts.github.io/statsblog/2023/12/05/post2/) on the data cleaning 
    and .csv creation process. 

    # Exploratory Data Analysis

    In this EDA, I want to exlpore the relationship bewteen *2022 Delays* proportion and 
    other quantitative variables using a scatterplot. Then, I will to perform a regression 
    analysis for the Q → Q scatterplots.

    After, I will use a barchart to analyze Average Delay on a State level. I included a filter for 
    State so that we can investigate the individual airport Average Delays per state. 
    """)

st.write("## Regression")
#  filters
st.write("#### Scatterplot Filters")
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
st.write("#### Regression Results")
st.write(model.summary())

st.write("#### Regression Analysis") 
st.markdown(
    """ 
    In the regression analysis, there is a stronger relationship between 2022 Enplaned Passengers and Delays than Elevation and Delays.  

    However, the R-squared value between Enplaned Passengers and Delays is only **0.085**, which indicates a weak relationship. 

    The R-squared value between Elevation and Delays is **0.006**, which indicates almost no relationship.

    I think the data might perform better after a transformation. 
    """)

st.write('## Barchart')
st.write('Now, I want to compare *Avg. Delay (Mins)* by *State* in a bar chart sorted from greatest to least average delay.')


stateAvgDelays = airports.groupby('State')['Delays'].mean().reset_index()
stateAvgDelays = stateAvgDelays.sort_values(by='Delays', ascending=True)

bars = px.bar(stateAvgDelays, x='Delays', y='State',color_discrete_sequence=['#4b7b9b',],height=900,
                width=700,
                title='Top 200 Airports 2022: Average Delays by State')

st.plotly_chart(bars)


#  filters
st.write("#### Barchart Filters")

selected_state = st.selectbox("Select State", airports['State'].unique())

# Apply filters to the dataframe
filtered_airports = airports[(airports['State'] == selected_state)]

fig = px.bar(filtered_airports, x='Delays', y='Airport',color_discrete_sequence=['#4b7b9b',],height=450,
                width=800,
                title='Top 200 Airports 2022: Average Delays for '+selected_state+' Airports')

st.plotly_chart(fig)


st.dataframe(filtered_airports)


st.write("#### Barchart Analysis")
st.markdown(
    """  
    The barchart allows us to see the average delay by state. Using the drop down menu, 
    we can investigate the 2022 yearly delay average for each airport in the chosen state.    

    The states with the highest average delay include: 
    - Massachusetts
    - US Territory (Puerto Rico Airport) and 
    - Illinois   

    The states with the lowest average delay include: 
    - Hawaii
    - Alaska and
    - Idaho   
    """)

st.markdown("""Check out my [project repo](https://github.com/lucystorts/386Project) and
        [blog](https://lucystorts.github.io/statsblog/) for more information on this project.
        """
        )
