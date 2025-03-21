import pandas as pd
import dash
from dash import dcc, html, Input, Output
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import os

# Initialize the Dash app
app = dash.Dash(__name__, title='Car Data Analysis Dashboard')
server = app.server

# Load the dataset
df = pd.read_csv('car_dataset.csv')

# Create layouts for the four visualizations
def create_price_year_boxplot():
    fig = px.box(df, x='year', y='price', title='Car Price Distribution by Year')
    fig.update_layout(
        xaxis_title='Year',
        yaxis_title='Price ($)',
        plot_bgcolor='white',
        paper_bgcolor='white',
        font=dict(size=12)
    )
    return fig

def create_price_mileage_scatter():
    fig = px.scatter(df, x='mileage', y='price', color='transmission',
                     title='Price vs Mileage by Transmission Type')
    fig.update_layout(
        xaxis_title='Mileage',
        yaxis_title='Price ($)',
        plot_bgcolor='white',
        paper_bgcolor='white',
        font=dict(size=12)
    )
    return fig

def create_color_distribution():
    color_counts = df['color'].value_counts().reset_index()
    color_counts.columns = ['color', 'count']  # Rename columns
    fig = px.bar(color_counts, x='color', y='count',
                 title='Car Color Distribution')
    fig.update_layout(
        xaxis_title='Color',
        yaxis_title='Count',
        plot_bgcolor='white',
        paper_bgcolor='white',
        font=dict(size=12)
    )
    return fig

def create_model_distribution():
    model_counts = df['model'].value_counts().head(10).reset_index()
    model_counts.columns = ['model', 'count']  # Rename columns
    fig = px.bar(model_counts, x='model', y='count',
                 title='Top 10 Car Models')
    fig.update_layout(
        xaxis_title='Model',
        yaxis_title='Count',
        plot_bgcolor='white',
        paper_bgcolor='white',
        font=dict(size=12)
    )
    return fig

# App layout
app.layout = html.Div([
    # Header
    html.Div([
        html.H1("Car Data Analysis Dashboard", style={'textAlign': 'center', 'color': '#2c3e50', 'margin-bottom': '10px'}),
        html.H4("Analysis of Used Cars Dataset", style={'textAlign': 'center', 'color': '#7f8c8d', 'margin-top': '0px'})
    ], style={'padding': '20px'}),
    
    # Metadata Section
    html.Div([
        html.H3("Dataset Overview", style={'color': '#2c3e50'}),
        html.Div([
            html.P(f"Total Records: {len(df)}"),
            html.P(f"Years Range: {df['year'].min()} - {df['year'].max()}"),
            html.P(f"Price Range: ${df['price'].min()} - ${df['price'].max()}"),
            html.P(f"Transmission Types: {', '.join(df['transmission'].unique())}")
        ], style={'padding': '10px', 'backgroundColor': '#f8f9fa', 'borderRadius': '5px'})
    ], style={'margin': '20px', 'padding': '10px'}),
    
    # Visualizations
    html.Div([
        html.Div([
            html.H3("Price Distribution by Year", style={'textAlign': 'center', 'color': '#2c3e50'}),
            dcc.Graph(id='price-year-boxplot', figure=create_price_year_boxplot())
        ], style={'width': '48%', 'display': 'inline-block', 'vertical-align': 'top', 
                  'border': '1px solid #ddd', 'border-radius': '5px', 'padding': '10px'}),
        
        html.Div([
            html.H3("Price vs Mileage", style={'textAlign': 'center', 'color': '#2c3e50'}),
            dcc.Graph(id='price-mileage-scatter', figure=create_price_mileage_scatter())
        ], style={'width': '48%', 'display': 'inline-block', 'vertical-align': 'top', 
                  'border': '1px solid #ddd', 'border-radius': '5px', 'padding': '10px'})
    ], style={'margin': '20px'}),
    
    html.Div([
        html.Div([
            html.H3("Color Distribution", style={'textAlign': 'center', 'color': '#2c3e50'}),
            dcc.Graph(id='color-distribution', figure=create_color_distribution())
        ], style={'width': '48%', 'display': 'inline-block', 'vertical-align': 'top',
                  'border': '1px solid #ddd', 'border-radius': '5px', 'padding': '10px'}),
        
        html.Div([
            html.H3("Top 10 Car Models", style={'textAlign': 'center', 'color': '#2c3e50'}),
            dcc.Graph(id='model-distribution', figure=create_model_distribution())
        ], style={'width': '48%', 'display': 'inline-block', 'vertical-align': 'top',
                  'border': '1px solid #ddd', 'border-radius': '5px', 'padding': '10px'})
    ], style={'margin': '20px'}),
    
    # Footer
    html.Div([
        html.Hr(),
        html.P("Car Data Analysis | Created for Data Analysis Capstone Project | 2025",
               style={'textAlign': 'center', 'color': '#7f8c8d'})
    ])
], style={'font-family': 'Arial, sans-serif', 'margin': '0 auto', 'max-width': '1200px'})

# Run the app
if __name__ == '__main__':
    app.run(debug=True, port=8050)
