# -*- coding: utf-8 -*-

# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import dash_daq as daq
from dash.dependencies import Input, Output, State

import time

import RobotGUI_dash_CL as guicl
import RobotGUI_dash_CP as guicp

from multiprocessing import Pipe 


#import plotly.express as px
#import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']



guiconnect = Pipe()


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP]) #external_stylesheets)
app.config.suppress_callback_exceptions = True

app.layout = html.Div(children=[
    html.H1(children='CALICE positionning robot'),
    
    html.Div(children=guicp.cp_tools),
    
    dcc.Tabs(id = "tabs", value = ' tab-cp ', children = [ 
        dcc.Tab (label = ' Control pannel ', value =' tab-cp '), 
        dcc.Tab (label =' Programm ', value =' tab-cl '), 
    ]), 
    
    html.Div(id ='tabs-content') 
    
])


#callback pour le bouton 'connect'
@app.callback([Output(component_id='connect-indicator', component_property='color'),
               Output(component_id='connect-indicator', component_property='value')], 
              [Input(component_id='button_connect', component_property='n_clicks')]) 
def connect_click(click):
    print('Send message for connect function, wait return flag')
    guiconnect[0].send(['Connection request'])
    if click%2 == 0:
        return "#FF5E5E", False
    else:
        time.sleep(5)
        return "#00CC96", True


        
#callback pour le bouton 'STOP'
@app.callback([Output(component_id='stop-indicator', component_property='color'),
               Output(component_id='stop-indicator', component_property='value')], 
              [Input(component_id='button_stop', component_property='n_clicks')]) 
def connect_stop(click):
    print('Send message for connect function, wait return flag')
    guiconnect[0].send(['STOP request'])
    return "#FF6E5E", True




        
        
#callback pour contrôler le contenu de l'onglet 
@app.callback(Output(component_id='tabs-content', component_property='children'), 
              [Input(component_id='tabs', component_property='value')]) 
def render_content(tab): 
    print('Tabs value')
    if tab == ' tab-cp ':
        print('got tab-cp')    
        return guicp.pannel_CP()
    elif tab ==' tab-cl ': 
        print('got tab-cl')
        #return html.Div([html.H1 (' command line here ')])
        return guicl.pannel_CL()


        
#callback pour le boutton "run"
@app.callback(Output(component_id='status_div', component_property='children'), 
              [Input(component_id='button_run', component_property='n_clicks')],
              [State(component_id='select_action', component_property='value'),
               State(component_id='select_location', component_property='value'),
               State(component_id='switch_Ztouch', component_property='on'),
               State(component_id='switch_TableLock', component_property='on')
              ]) 
def run_callback(c,a,l,zt,tl):
    print(c,a,l,zt,tl)
    guiconnect[0].send(['Command', a, l, zt, tl])
    return guicp.status_return(c,a,l,zt,tl)

    

 
if __name__ == '__main__':
    app.run_server(debug=True)