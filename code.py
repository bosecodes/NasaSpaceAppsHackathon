# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 18:03:27 2019

@author: Somdev Basu
"""

import pandas as pd
df = pd.read_csv('accidents.csv')
df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

isLA =  df['City']=='Los Angeles'
df = df[isLA]

df = df[:10000]
df.dropna()

latitudes = df.loc[:, 'Start_Lat']
longitudes = df.loc[:, 'Start_Long']

import gmplot

gmap.heatmap(latitudes[:10000], longitudes[:10000])
gmap.draw( "map11.html" )

import webbrowser
 
a_website = "map11.html"
 
# Open url in a new page (“tab”) of the default browser, if possible
webbrowser.open_new_tab(a_website)
webbrowser.open(a_website, 2) # Equivalent to: webbrowser.open_new_tab(a_website)

# def start_html():
#     return '<html>'

# def end_html():
#     return '</html>'

# def print_html(text):
#     text = str(text)
#     text = text.replace('\n', '<br>')
#     return '<p>' + str(text) + '</p>'


# if __name__ == '__main__':
#         webpage_data =  start_html()
#         webpage_data += print_html("Hi Welcome to Python test page\n")
#         webpage_data += fd.write(print_html("Now it will show a calculation"))
#         webpage_data += print_html("30+2=")
#         webpage_data += print_html(30+2)
#         webpage_data += end_html()
#         with open('map11.html', 'w') as fd: fd.write(webpage_data)