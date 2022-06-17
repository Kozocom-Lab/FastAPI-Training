# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, dcc, html
import plotly.express as px
import pandas as pd

app = Dash(__name__)

df = pd.read_csv('./data-raw.csv')
colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

fig = px.bar(df, x="hoten", y="toán",
                 color="thang", hover_name="nam"
                 )
fig1 = px.scatter(df, x="thang", y="toán",
                 size="ngữ văn", color="thang", hover_name="hóa học",
                 log_x=True, size_max=60)

app.layout = html.Div(children=[
    html.H2(
        children='Hello Dash',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),

    dcc.Graph(
        id='life-exp-vs-gdp',
        figure=fig
    ),

     dcc.Graph(
        id='life-exp-vs-gdp1',
        figure=fig1
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
