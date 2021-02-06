# -*- coding: utf-8 -*-
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import dash_daq as daq


cp_tools = [html.Div(children=[
    dbc.Row(children=[
    dbc.Col(width="auto", children=[dbc.Button('connect', outline=True, color="primary", id='button_connect', n_clicks=0)]),
       
    
    dbc.Col(width="auto", children=[daq.Indicator(
        id='connect-indicator',
        value=False,
        color='#FF5E5E')]), #"#00cc96")  

    dbc.Col(width="auto", children=[dbc.Button('HOME', outline=True, color="secondary", id='button_home', n_clicks=0)]),
       
    
    dbc.Col(width="auto", children=[daq.Indicator(
        id='stop-indicator',
        value=False,
        color='#005E5E')]), #"#00cc96")  

    
    dbc.Col(width="auto", children=[daq.StopButton(
        id='button_stop',
        #label='',
        n_clicks=0
    )])
    
    ])])]

cp_title = [
    html.H1 (' control pannel here ')
    ]   
    
xyz_layout = [html.Div(children=[
    html.H5('Position'),
    dbc.Row(children=[ 
    dbc.Col(width="auto", children=[daq.LEDDisplay(id='led_x',label='X',value="1111.11")]),
    dbc.Col(width="auto", children=[daq.LEDDisplay(id='led_y',label='Y',value="2222.11")]),
    dbc.Col(width="auto", children=[daq.LEDDisplay(id='led_z',label='Z',value="3333.11")]),
    dbc.Col(width="auto", children=[daq.Joystick(id='joystick',label='Manual MOVE', size=80)]),
    ])])]

# xyz_layout = [html.Div(children=[
    # html.H5('Position'),
    # html.Tr(children=[ 
    # html.Td(children=[daq.LEDDisplay(id='led_x',label='X',value="1111.11")]),
    # html.Td(children=[daq.LEDDisplay(id='led_y',label='Y',value="2222.11")]),
    # html.Td(children=[daq.LEDDisplay(id='led_z',label='Z',value="3333.11")])
    # ])])]
    
    


# speed_layout = [html.Div(children=[
    # html.H5('Global Speed'),
    # dcc.Slider(id='slider_global_speed', min=0, max=9, marks={i: '{}'.format(i*1000) for i in range(10)},
    # value=5)  
    # ])]  


speed_layout = [html.Div(children=[
    html.Br(), html.H5('Speed'),
    dbc.Row(children=[
    dbc.Col(width="auto", children=[daq.Knob(id='slider_global_speed', size= 100, label="Global speed",min=0, max=10000, value=5000)]),
    dbc.Col(width="auto", children=[daq.Knob(id='slider_ztouch_speed', size= 100, label="Z touch speed",min=0, max=2500, value=500)])  
    ])
    ])]  
    
    
action_layout = [html.Div(children=[
    html.Br(),
    html.H5('Action'),
    
    dbc.Row(children=[
    dbc.Col(width="auto", children=[daq.BooleanSwitch(
        id='switch_Ztouch',
        on=False,
        label="Contact Z")]),

    dbc.Col(width="auto", children=[daq.BooleanSwitch(
        id='switch_TableLock',
        on=False,
        label="Bobine")])
    ]),
    
    html.Br(),
    
    dbc.InputGroup(children=[
        dbc.InputGroupAddon("Action", addon_type="prepend"),    
        dbc.Select(
            id='select_action',
            options=[
                {'label':'Move wafer','value':'MW'},
                {'label':'Move control','value':'MC'},
                {'label':'Retournement','value':'R'},
                {'label':'Reset retournement','value':'RR'}
            ]
        )
    ]),    

    dbc.InputGroup(children=[
        dbc.InputGroupAddon("Location", addon_type="prepend"),    
        dbc.Select(
            id='select_location',
            options=[
                {'label':'1','value':1},
                {'label':'2','value':2},
                {'label':'3','value':3},
                {'label':'4','value':4}
            ]
        )
    ]),    

    
    dbc.Button("Run", id="button_run", color="success", outline=True)
    
    # dcc.RadioItems(id='radio_action', 
        # options = [
        # {'label':'Move wafer   .','value':'MW'},
        # {'label':'Move control   .','value':'MC'},
        # {'label':'Retournement   .','value':'R'},
        # {'label':'Reset retournement   .','value':'RR'}
        # ],
        # value='MC')#, labelStyle={'display': 'inline-block'})  
    
    
    ])]  


status_layout = [html.Div(id="status_div", children=[

    ])]
    

def status_return(c,a,l,zt,tl):
    chil = [
        dbc.Toast(
            header = "status",
            icon = "primary",
            dismissable=True,
            #style={"position": "fixed", "top": 150, "right": 10, "width": 350},
            children=[html.P("Contenu {} {} {} {} {}".format(c,a,l,zt,tl))
        ])
        
    ]
    return chil

    
def pannel_CP():
    return html.Div(children=xyz_layout + speed_layout + action_layout + status_layout)