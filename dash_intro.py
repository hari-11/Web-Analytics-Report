# %%
from dash import Dash, html, dcc
import plotly.express as px
import plotly.graph_objs as go
import pandas as pd
from dash import dash_table
import dash_bootstrap_components as dbc

app = Dash(__name__, external_stylesheets=[dbc.themes.CYBORG])
server = app.server
colors = {
    'background': '#111111',
    'text': 'WHITE',
}
# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

#new
# fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

fig = go.Figure(data=[
    go.Bar(name='SF', x=df[df["City"] == 'SF']["Fruit"], y=df[df["City"] == 'SF']["Amount"]),
    go.Bar(name='Montreal', x=df[df["City"] == 'Montreal']["Fruit"], y=df[df["City"] == 'Montreal']["Amount"])
], layout= go.Layout(
    paper_bgcolor = 'white',
    plot_bgcolor = 'rgba(0,0,0,0)',))

fig.update_layout(barmode='group')

app.layout = html.Div(children=[
    html.H1(children='TEST ANALYTICS',
            style={
                'textAlign': 'center',
                'color': colors['text'],
                'font-size': 35
        }),

    html.Div(children='''
        Dash: A web application framework for your data.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    ),


    html.Div(dash_table.DataTable(
        df.to_dict('records'),
        [{"name": i, "id": i} for i in df.columns],
        # style_cell={'textAlign': 'right'},
        style_cell_conditional=[
        {
            'if': {'column_id': 'FRUIT'},
            'textAlign': 'left'
        }],
        style_header={
            'backgroundColor': 'grey',
            'color': 'rgb(50, 50, 50)'
        },
        style_data={
            'backgroundColor': 'rgba(0,0,0,0)',
            'color': 'grey'
        },
    )

    )])

if __name__ == '__main__':
    app.run_server(debug=True)
    # from waitress import serve
    # serve(app, host="0.0.0.0", port=8080)
# %%

# %%
