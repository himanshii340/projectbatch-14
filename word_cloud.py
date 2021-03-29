# -*- coding: utf-8 -*-
from wordcloud import WordCloud,STOPWORDS
import numpy as np
from PIL import Image
import pandas as pd
import webbrowser
import dash
import plotly.graph_objs as go
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output , State

# Declaring Global variables
app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
project_name = None


dataset = pd.read_csv('finaletsy_reviews.csv' , index_col=False ,skiprows=[0], names= ["Review"])
#dataset.columns
#dataset['Review'][0].
words=[]
words.append(dataset['Review'][0])
for i in dataset['Review']:
        words.append(i);
        formed_string = " ".join(words)
        
formed_string=formed_string.lower()
#formed_string

# Defining My Functions
def open_browser():
    webbrowser.open_new('http://127.0.0.1:8050/')
    
    
def open_browser():
    webbrowser.open_new('http://127.0.0.1:8050/')

def create_word_cloud(string):
  cloud =WordCloud(background_color='black' ,max_words =100,stopwords= set(STOPWORDS),repeat=False)
  cloud.generate(string)
  cloud.to_file("wordcloud4.png")
create_word_cloud(formed_string)


def create_app_ui():
    main_layout = html.Div([
        html.H1(id = 'heading', children = "Sentiment Analysis with Insights",
                            style= {'background-color':'#01331f',
                    'padding':'1em', 'color': 'white', 'font-family': 'Helvetica Neue', 'font-size':' 60px', 'font-weight': 'bold',
                    'letter-spacing': '-1px', 'line-height' :' 1', 'text-align': 'center'}),
        
        html.H3(id='second_head',children = "SECTION- 2",
                            
                            style={'text-align':'center','color': '#d4c009'}
                        
                            ),
        
        html.Img(id='image_review' , src = app.get_asset_url('wordcloud4.png') , alt= 'word cloud',
                 width='600',height ='350',
                 style= {'margin-left': '350px'}
                 ),
        
        
        
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
    app.title =project_name
    app.layout = create_app_ui()
    app.run_server()
    
    
    
    print("End of my project")
    project_name = None
    scrappedReviews = None
    app = None
    
        
# Calling the main function 
if __name__ == '__main__':
    main()
