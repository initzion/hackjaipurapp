import dash
import dash_core_components as dcc
import dash_html_components as html
from layout import html_layout

from twittergraph import TWT_graph
from youtubegraph import YT_graph
from redditgraph import REDDIT_graph


global yt_vid_comments
yt_vid_comments = []


app = dash.Dash(__name__)

server=app.server

app.index_string = html_layout

tabs_styles = {
    'height': '44px',

}
tab_style = {
    'border': '3px solid #111111',
    'padding': '6px',
    'fontWeight': 'bold',
    'background':'#111111'
}

tab_selected_style = {
    'borderTop': '3px solid #000000',
    'borderBottom': '3px solid #282828',
    'color': '#ffffff',
    'padding': '6px',
    'fontWeight': 'bold',
    'background':'#282828'

}






#LAYOUT OF THE MAIN DASH APP


app.layout = html.Div([
    dcc.Tabs(value='tab-0',children=
    [dcc.Tab(label='Home', value='tab-0', style=tab_style, selected_style=tab_selected_style, children=[
            html.P(""),
            html.H3("SentimentZION "),
            html.Div(
                [html.H4("Be a part of the change !!!"),
                    html.P("We at SentimentZION are focused to paint the true picture of the world for you. The information that is provided is mined from social media and analysed by us, we provided an overview of data from websites like YouTube, Twitter, and Reddit about your topic for a relevant timeframe."),
                    html.H4("DIVERSIFY!!!"),
                    html.P("Rightly said , Diversity is the inclusion of all individuals as technology and that is where our website focuses on!!! "),
                    html.H4("CREATING AWARENESS!!!"),
                    html.P("Awareness is the first step towards creating a better society and community as increasing the use of technology increases the dangers related to it."),
                    html.H3("FAQ "),
                    html.H4("What am I seeing?"),
                    html.P("Graphs which depict the analysis of the sentiments of the people."),
                    html.H4("What is the source of the data collection?"),
                    html.P("These data are collected from the comments of the social media sites like YouTube, Twitter and Reddit."),
                    html.H4("How is the data analyzed?"),
                    html.P("The most important part of our website is the analysis of the data. The comments that are retrieved are analysed through a sentimental analysis model which rates the comments from a scale of -1 to 1. -1 being most negative, 0 being neutral and 1 being most positive."),
                    html.H4("How far is the data correct?"),
                    html.P("The data is as efficient as it could be. The comments are analysed through textblob Natural Language Processing(NLP). So the output is quite efficient."),
                    html.H4("What is the significance?"),
                    html.P("Most social networks project the views of the most vocal but a minority of users on their platforms, however, the majority of the users' opinion is not taken into consideration. That is where our website effects the most."),
                    html.H4("The comments are updating! Are the graphs getting updated?"),
                    html.P("Yes, the graphs are live visual representation of the comments. As the comments get updated, the graphs too get updated.")

                    ])

        ]),
        dcc.Tab(label='Dashboard', value='tab-1', style=tab_style, selected_style=tab_selected_style, children=[
            html.Div([
                #html.Div(html.H1(children="Team Zion")),
                html.P(""),
                html.H3("Enter the term you want to analyse"),
                html.Div([
                    dcc.Input(
                        id = "yquery-input",
                        placeholder = "Enter the query you want to search",
                        type = "text",
                        value = "Covid19",
                        style={"margin-right": "15px"}
                    ),
                   html.Button('Submit', id='ysubmit-val', n_clicks=0),
                   html.P(""),
                ]),
                html.Div(
                    dcc.Graph(id="y-graph1", config={'displayModeBar': False})
                    ),
                html.P(""),
                html.Div(
                    dcc.Graph(id="y-graph2",)
                    ),
                html.P(""),
                html.Div(
                    dcc.Graph(id="y-graph3",)
                    ),
                html.P(""),
                html.Div(
                    dcc.Graph(id="y-graph4",)
                    )

            ])
        ]),
    ])
])


#FUNCTION TO UPDATE THE GRAPHS ONPRESS OF SUBMIT BUTTON

@app.callback(
    [dash.dependencies.Output("y-graph1","figure"),
    dash.dependencies.Output("y-graph2","figure"),
    dash.dependencies.Output("y-graph3","figure"),
    dash.dependencies.Output("y-graph4","figure")],
    [dash.dependencies.Input('ysubmit-val', 'n_clicks')],
    [dash.dependencies.State("yquery-input","value")])
def update_figyt(n_clicks,input_value):
    figure = YT_graph(n_clicks,input_value)
    figure1 = figure[0]
    figure2 = figure[1]
    figure3 = figure[2]
    figure4 = figure[3]

    return figure1, figure2, figure3, figure4





if __name__ == "__main__":
    app.run_server(debug = True)

