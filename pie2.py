# -*- coding: utf-8 -*-
import numpy as np
import pickle
import pandas as pd
import webbrowser
import dash
import plotly.graph_objs as go
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import plotly.express as px
from dash.dependencies import Input, Output , State
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer

#declaring variables
app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
project_name = None

#defining the functions
def open_browser():
    webbrowser.open_new('http://127.0.0.1:8050/')
    
    
def load_model():
    global data
    srr =pd.read_csv("finaletsy_reviews.csv")

    global pickle_model
    global pie_data
    file = open("pickle_model.pkl", 'rb') 
    pickle_model = pickle.load(file)

    global vocab
    file = open("feature.pkl", 'rb') 
    vocab = pickle.load(file)



def figure():
    labels=["Positive reviews","Negative reviews"]
    values_ = [33783, 4965]
    pie = go.Pie(labels=labels,values= values_,pull =[0,0.2],textposition='inside')
    fig=go.Figure(data=[pie])
    return fig
    
def create_app_ui():
    main_layout = html.Div([
        html.H1(id = 'heading', children = "Sentiment Analysis with Insights",
                            style= {'background-color':'#fcb308',
                    'padding':'1em', 'color': 'white', 'font-family': 'Helvetica Neue', 'font-size':' 60px', 'font-weight': 'bold',
                    'letter-spacing': '-1px', 'line-height' :' 1', 'text-align': 'center'}),
        html.H3(id='second_head',children = "SECTION- 1",
                            
                            style={'text-align':'center','color': '#e7131d'}
                        
                            ),
        
        dcc.Graph(id="pie", figure=figure()),
        
     ]
        
    )
    
    return main_layout

def main():
    print("Start of your project")
    
    open_browser()
    #update_app_ui()
    
    
    global scrappedReviews
    global app
    
    project_name = "Sentiment Analysis with Insights"
    app.title = project_name
    app.layout = create_app_ui()
    app.run_server()
    
    
    
    print("End of my project")
    project_name = None
    scrappedReviews = None
    app = None
    
        
# Calling the main function 
if __name__ == '__main__':
    main()
