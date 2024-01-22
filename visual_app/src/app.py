# Copy and pasted from the ForestedAreas.ipynb notebook to here -N.C.

# Dependencies

import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress, pearsonr
import plotly.express as px
import plotly.graph_objects as go
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from scipy.stats import pearsonr
import numpy as np
import dash
from dash import dcc, html
from dash.dependencies import Input, Output

# Load CSV into DF

#Adina
forested_file_path = '../../Adina/Resources/Forested_Areas.csv'
forest_df = pd.read_csv(forested_file_path, encoding='utf-8')

forest_df.head()

#Anika
tax_rate_path = '../../Anika/tax_rate_df.csv'
taxrate_df = pd.read_csv(tax_rate_path, encoding='utf-8')

#Garrett
out_of_pocket_path = '../../Garrett/out_of_pocket_df.csv'
outofpocket_df = pd.read_csv(out_of_pocket_path, encoding='utf-8')


# Create a Dash application
app = dash.Dash(__name__)

# Set up for deployment to server -N.C.
server = app.server

# Define the layout of the application
#app.layout = html.Div(layout = [
#  html.H2("Forested Area (%) vs Life Expectancy (years)"),
#     # Dropdown menu for selecting a country
#  dcc.Dropdown(
#    id='country-dropdown',
#    options=[{'label': i, 'value': i} for i in forest_df['Country'].unique()],
#    value=forest_df['Country'].iloc[0]
#  ),
#     # Graph object for displaying the scatter plot
#  dcc.Graph(id='scatter-plot', figure=fig1),
#  html.Div(className='spacer'),
#  html.H2("Out of Pocket Health Expenses vs Life Expectancy"),
#  dcc.Graph(id='scatter-plot', figure=fig2),
#  html.Div(className='spacer'),
#  html.H2("Total Tax Rates vs Life Expectancy"),
#  dcc.Graph(id='scatter-plot', figure=fig3)
#  ])

# Define a callback function that updates the scatter plot based on the selected country
@app.callback(
 Output('scatter-plot', 'figure'),
 Input('country-dropdown', 'value')
)
def update_scatter_plot(selected_country):
    
 # Filter the DataFrame for the selected country
 filtered_df = forest_df[forest_df['Country'] == selected_country]

 # Define X and y
 X = filtered_df["Forested Area (%)"].values.reshape(-1, 1)
 y = filtered_df["Life Expectancy (years)"]

 # Create a scatter plot
 fig1 = px.scatter(forest_df, x="Forested Area (%)", y="Life Expectancy (years)", color=forest_df['Country'].apply(lambda x: 'green' if x == selected_country else 'blue'), custom_data=['Country'], hover_data=['Country'])
# Return the figure object which will be used to render the scatter plot
 return fig1

# Customize the hovertemplate
 fig.update_traces(hovertemplate="<b>Country:</b> %{customdata[0]}<br><b>Forested Area:</b> %{x}<br><b>Life Expectancy:</b> %{y}<extra></extra>")

 # Remove the legend
 fig.update_layout(showlegend=False)

@app.callback(
 Output('scatter-lot', 'figure')
)
def figure2():
# Define X and y
 X = outofpocket_df["Out of pocket health expenditure"].values.reshape(-1, 1)
 y = outofpocket_df["Life expectancy"]

 # Create a scatter plot
 fig2 = px.scatter(outofpocket_df, x="Out of pocket health expenditure", y="Life Expectancy", color='red')
# Return the figure object which will be used to render the scatter plot
 return fig2

@app.callback(
 Output('scatter-plot', 'figure')
)
def figure3():
 # Define X and y
 X =  taxrate_df["Total Tax Rate (%)"].values.reshape(-1, 1)
 y = taxrate_df["Life Expectancy"]

 # Create a scatter plot
 fig3 = px.scatter(taxrate_df, x="Total Tax Rate (%)", y="Life Expectancy", color='red')
# Return the figure object which will be used to render the scatter plot
 return fig3

# Define the layout of the application
app.layout = html.Div(layout = [
 html.H2("Forested Area (%) vs Life Expectancy (years)"),
    # Dropdown menu for selecting a country
 dcc.Dropdown(
   id='country-dropdown',
   options=[{'label': i, 'value': i} for i in forest_df['Country'].unique()],
   value=forest_df['Country'].iloc[0]
 ),
    # Graph object for displaying the scatter plot
 dcc.Graph(id='scatter-plot', figure=fig1),
 html.Div(className='spacer'),
 html.H2("Out of Pocket Health Expenses vs Life Expectancy"),
 dcc.Graph(id='scatter-plot', figure=fig2),
 html.Div(className='spacer'),
 html.H2("Total Tax Rates vs Life Expectancy"),
 dcc.Graph(id='scatter-plot', figure=fig3)
 ])