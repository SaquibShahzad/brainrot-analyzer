import datetime
import dash
from dash import dcc
from dash import html
import plotly.express as px
import pandas as pd
# from googleapiclient.discovery import build  # Uncomment and configure when using the real API

API_KEY = "YOUR_API_KEY"  # Replace with your actual YouTube API key or OAuth2 credentials


def get_youtube_history():
    """
    Simulates fetching YouTube watch history for the last month.
    Note: Replace this simulation with actual API calls and authentication as needed.
    """
    simulated_history = [
        {"title": "Video A", "category": "Music", "publishedAt": "2023-09-15T12:00:00Z"},
        {"title": "Video B", "category": "Gaming", "publishedAt": "2023-09-20T15:30:00Z"},
        {"title": "Video C", "category": "Education", "publishedAt": "2023-09-25T09:45:00Z"},
        {"title": "Video D", "category": "Music", "publishedAt": "2023-09-28T16:20:00Z"},
        {"title": "Video E", "category": "Gaming", "publishedAt": "2023-09-30T18:05:00Z"},
        {"title": "Video F", "category": "Comedy", "publishedAt": "2023-09-10T11:00:00Z"},
        {"title": "Video G", "category": "News", "publishedAt": "2023-09-18T14:15:00Z"},
        {"title": "Video H", "category": "Sports", "publishedAt": "2023-09-22T19:40:00Z"},
        {"title": "Video I", "category": "Documentary", "publishedAt": "2023-09-27T08:50:00Z"}
    ]
    one_month_ago = datetime.datetime.utcnow() - datetime.timedelta(days=30)
    filtered_history = [
        video for video in simulated_history 
        if datetime.datetime.strptime(video["publishedAt"], "%Y-%m-%dT%H:%M:%SZ") > one_month_ago
    ]
    # return filtered_history
    return simulated_history


def classify_history(history):
    """
    Classify the history items by category and count them.
    """
    categories = {}
    for video in history:
        cat = video.get("category", "Unknown")
        categories[cat] = categories.get(cat, 0) + 1
    return categories


# Fetch and process YouTube history data
history_data = get_youtube_history()
classification = classify_history(history_data)

df = pd.DataFrame({
    "Category": list(classification.keys()),
    "Count": list(classification.values())
})

# Build the Dash app
app = dash.Dash(__name__)

app.layout = html.Div(
    children=[
        html.Div([
            html.Img(
                src='https://unsplash.com/photos/white-ceramic-mug-with-coffee-KzeOMdcEswk',
                style={'width': '100%', 'height': 'auto', 'borderRadius': '8px', 'boxShadow': '0px 4px 8px rgba(0, 0, 0, 0.1)'}
            ),
            html.H1(
                "YouTube Browsing History Dashboard",
                style={'fontSize': '6em', 'marginTop': '20px', 'color': '#333'}
            )
        ], style={'backgroundColor': '#fff', 'padding': '20px', 'borderRadius': '10px', 'boxShadow': '0px 4px 12px rgba(0,0,0,0.15)', 'marginBottom': '30px'}),
        html.Div([
            html.Label("Increase Font Sizes:", style={'fontSize': '2em', 'color': '#555', 'marginBottom': '10px'}),
            dcc.Slider(
                id='font-slider',
                min=0,
                max=20,
                step=1,
                value=10,
                marks={i: str(i) for i in range(0, 21, 5)},
                tooltip={'placement': 'bottom', 'always_visible': True}
            )
        ], style={'marginBottom': '40px'}),
        dcc.Graph(id="category-bar", style={'marginBottom': '40px', 'border': '1px solid #ddd', 'borderRadius': '8px', 'boxShadow': '0px 4px 8px rgba(0, 0, 0, 0.05)' }),
        html.Br(),
        html.Div([
            html.Label("Select Brainrot Categories:", style={'fontSize': '3em', 'color': '#555', 'marginBottom': '20px'}),
            dcc.Dropdown(
                id='brainrot-categories',
                options=[{'label': cat, 'value': cat} for cat in classification.keys()],
                multi=True,
                placeholder='Select categories you consider brainrot',
                style={'fontSize': '1.5em', 'padding': '10px'}
            )
        ], style={'marginBottom': '40px'}),
        dcc.Graph(id='brainrot-pie-chart', style={'marginBottom': '40px', 'border': '1px solid #ddd', 'borderRadius': '8px', 'boxShadow': '0px 4px 8px rgba(0, 0, 0, 0.05)' })
    ],
    style={'maxWidth': '2400px', 'margin': '0 auto', 'padding': '30px', 'backgroundColor': '#f9f9f9', 'fontFamily': 'Arial, sans-serif'}
)


@app.callback(
    dash.Output('category-bar', 'figure'),
    [dash.Input('font-slider', 'value')]
)
def update_figure(font_offset):
    # Create a bar chart using Plotly Express
    fig = px.bar(df, x="Category", y="Count", color="Category", title="YouTube Browsing History Categories (Last Month)")

    # Increase font sizes based on slider offset
    fig.update_layout(
        title_font=dict(size=30 + font_offset),
        xaxis=dict(
            title=dict(font=dict(size=24 + font_offset)),
            tickfont=dict(size=20 + font_offset)
        ),
        yaxis=dict(
            title=dict(font=dict(size=24 + font_offset)),
            tickfont=dict(size=20 + font_offset)
        ),
        legend=dict(
            title=dict(font=dict(size=24 + font_offset)),
            font=dict(size=20 + font_offset)
        )
    )
    return fig


@app.callback(
    dash.Output('brainrot-pie-chart', 'figure'),
    [
        dash.Input('brainrot-categories', 'value'),
        dash.Input('font-slider', 'value')
    ]
)
def update_pie(selected_categories, font_offset):
    total_count = df['Count'].sum()
    brainrot_count = df[df['Category'].isin(selected_categories)]['Count'].sum() if selected_categories else 0
    non_brainrot_count = total_count - brainrot_count

    fig = px.pie(
        names=["Brainrot", "Non-Brainrot"],
        values=[brainrot_count, non_brainrot_count],
        title="Brainrot Content Percentage"
    )
    fig.update_traces(textinfo='percent+label')

    # Apply slider font offset to the pie chart title and legend
    fig.update_layout(
        title_font=dict(size=30 + font_offset),
        legend=dict(font=dict(size=20 + font_offset))
    )
    return fig


if __name__ == "__main__":
    app.run_server(debug=True)
