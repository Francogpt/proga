import dash_bootstrap_components.themes
import pandas as pd
import plotly.express as px

from dash import Dash, dcc, html, dash_table, callback, Input, Output

#dcc  ---> Dash Core Components
#html ---> Dash Html Components

data = pd.read_csv("data_olimpiadas.csv", index_col=0)

def tarjeta_filtros():
    control = dash_bootstrap_components.Card([
        html.Div(
            dash_bootstrap_components.Label("Gender: "),
            dcc.Dropdown(options=["All","Male", "Female"], value="All")
        ]),
        html.Div([
            dash_bootstrap_components.Label("Medal: "),
            dcc.Dropdown(options=["all", "gold", "silver", "bronze"],
                         value="all", id="ddMedal")
        ]),
        html.Div([
            dash_bootstrap_components.Label("Year: "),
            dash_bootstrap_components.Input(type="number")
        ])
    ])
    return control

def dashboard():
    data_Pais = data.groupby("country", as_index=False).sum(numeric_only=True)
    g1= px.line(data_Pais, x="country", y=["gold","silver","bronze"])
    body = html.Div([
        html.H2("Datos Olimpiadas"),
        html.P("Objetivo: DashBoard: Mostrar los resultados de las medallas de los países"),
        html.Hr(),
        dash_bootstrap_components.Row(
            [
                dash_bootstrap_components.Col(
                    html.Div([
                        html.H3("Filtros"),
                        dash_bootstrap_components.Label("Medal: "),
                        dcc.Dropdown(options=["all", "gold", "silver", "bronze"],
                                     value="all", id="ddMedal"),
                    ]), width=3
                ),
                dash_bootstrap_components.Col(
                    html.Div([
                        dash_bootstrap_components.Row(dcc.Graph(figure=g1, id="figMedal")),
                        dash_bootstrap_components.Row(dash_table.DataTable(data=data.to_dict("records"),page_size=10))
                    ]), width=9
                )
            ]
        ),
    ])
    return body

if __name__ == "__main__":
    app = Dash(__name__, external_stylesheets=[dash_bootstrap_components.themes.BOOTSTRAP])
    app.layout = dashboard()
    app.run(debug=True)

