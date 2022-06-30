from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import dash_auth
import dash_bootstrap_components as dbc

import pandas as pd
colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}
external_stylesheets = [dbc.themes.DARKLY]
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv')


app = Dash(__name__, external_stylesheets=external_stylesheets)
VALIDATION_LOGIN = {
    'admin': 'admin1234'
}

auth = dash_auth.BasicAuth(
    app,
    VALIDATION_LOGIN
)
app.layout = html.Div([
    html.H1(
        children='Hello Dash',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),
    dcc.Graph(id='graph'),
    html.Div(children=[
        html.Label(children='Chart: ', style={
            'margin-right': '10px'
        }),
        dcc.RadioItems(['Bubble chart', 'Column chart'], 'Bubble chart', id='type-char')
    ], style={
        'display': 'flex',
        'justify-content': 'center',
        'font-size': '15pt',
        'padding': '10px 0',
        'align-items': 'center'
    }),
    html.Div(children=[
        html.Label(children='Quota: ', style={
            'margin-right': '10px'
        }),
        dcc.Dropdown(
        options={
            'gdpPercap': 'Gdp per capita',
            'lifeExp': 'Life expectancy',
            'pop': 'Pop'
        },
        value='gdpPercap',style={'min-width': '300px'}, id='quota')
    ], style={
        'display': 'flex',
        'justify-content': 'center',
        'font-size': '15pt',
        'padding': '10px 0',
        'align-items': 'center'
    }),
    dcc.Slider(
        df['year'].min(),
        df['year'].max(),
        step=None,
        value=df['year'].min(),
        marks={str(year): str(year) for year in df['year'].unique()},
        id='year-slider'
    )
])

@app.callback(
    Output('graph', 'figure'),
    Input('type-char', 'value'),
    Input('quota', 'value'),
    Input('year-slider', 'value'),
    )
def update_figure(type_char, quota, year_slider):
    filtered_df = df[df.year == year_slider]
    if type_char == 'Bubble chart':
        fig = px.scatter(filtered_df, x=quota, y="lifeExp",
                size="pop", color="continent",
                log_x=True, size_max=55)
    else:
        fig = px.bar(filtered_df, x="country", y=quota, color="continent", barmode="group")

    fig.update_layout(
        transition_duration=500,
        plot_bgcolor=colors['background'],
        paper_bgcolor=colors['background'],
        font_color=colors['text']
    )
 
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
