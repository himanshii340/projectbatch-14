# -*- coding: utf-8 -*-
### using this file to segregate positive and negative reviews
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
from dash.dependencies import Input, Output
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer


#declaring global variables and loading important file
list1=[]
scrappedReviews =pd.read_csv("finaletsy_reviews.csv")
global pickle_model
file = open("pickle_model.pkl", 'rb') 
pickle_model = pickle.load(file)

global vocab
file = open("feature.pkl", 'rb') 
vocab = pickle.load(file)

#using the following code to extract whether a review is '1' or '0' for all reviews in our finaletsy_review.csv file
for x in scrappedReviews['0']:
            transformer = TfidfTransformer()
            loaded_vec = CountVectorizer(decode_error="replace",vocabulary=vocab)
            vectorised_review = transformer.fit_transform(loaded_vec.fit_transform([x]))
            list1.append(pickle_model.predict(vectorised_review))

    # Add code to test the sentiment of using both the model
    # 0 == negative   1 == positive
    
            list1.append(pickle_model.predict(vectorised_review))
        
#dividing list 1 into list2 and list3        
list2= []
list3= []
for i in range(len(list1)):
    if list1[i]==1:
        list2.append("positive")
    else:
        list3.append("negative")
        
# in the end, list2 holds all the positive reviews and list3 holds all negative reviews
#we then calculate their lengths and use it to make pie chart as shown in file("pie2.py")
