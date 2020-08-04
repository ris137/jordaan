import pandas as pd
import plotly.graph_objects as go


def setColor(x):
    if x == 'Arsenal':
        return 'red'
    return 'black'


def setOpacity(x):
    if x == 'Arsenal':
        return 1
    return 0.5

from rank_every_attribute import rank_every_attribute

df = pd.read_csv('data\PL\AllTeamsShots1920.csv')

rank_every_attribute(data=df,
                     club_name='Arsenal')

fig = go.Figure(data=go.Scatter(x=df['Sh'],
                                y=df['SoT'],
                                mode='markers',
                                marker_size=df['SoT%'],
                                hovertext=df['Squad'],
                                marker=dict(size=8,
                                            color=list(map(setColor, df['Squad'])),
                                            opacity=list(map(setOpacity, df['Squad']))
                                            )))
fig.update_layout(
    title='Shots vs Shots on Target',
    xaxis_title='Shots',
    yaxis_title='Shots on Target',
    plot_bgcolor='white',
    paper_bgcolor='whitesmoke'
)
fig.write_html('ShvsSoT.html',
               auto_open=True)
