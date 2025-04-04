import pandas as pd
import numpy as np
import plotly.express as px
import plotly.offline as pyo
from dash import html
from dash import dcc
import dash
import plotly.graph_objects as go

gap = px.data.gapminder()
app = dash.Dash()

app.layout = html.Div([
    html.H1('My First Dashbord',
            style={'color':'red','text-align':'center'}),
    html.Div(children=[
        dcc.Graph(id = 'sca',figure={'data':[go.Scatter(
            x=gap['pop'] , y=gap['gdpPercap'] , mode='markers',
            )],'layout':go.Layout(title = 'Scatter Plot')})
    ]
    ,style={'border':'1px black solid','float':'left','width':'100%','height':'50px'}),
    html.Div(dcc.Graph(id='box-plot',figure={'data':[go.Box(
        x = gap['gdpPercap'])],
        'layout':go.Layout(title='Box-Plot')}),
        style={'border':'1px black solid','float':'left','width':'49.5%','height':'350px'}),
])
if __name__ == "__main__":
    app.run(debug=True)