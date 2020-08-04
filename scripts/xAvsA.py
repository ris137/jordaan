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

df = pd.read_csv('data\PL\AllTeams1920.csv')

# rank_every_attribute(data=df,
#                      club_name='Arsenal')
df['AstRatio'] = df['xA'] / df['Ast']
fig = go.Figure(data=go.Scatter(x=df['xA'],
                                y=df['Ast'],
                                mode='markers',
                                marker_size=df['Ast'],
                                hovertext=df['Squad'],
                                marker=dict(size=8,
                                            color=list(map(setColor, df['Squad'])),
                                            opacity=list(map(setOpacity, df['Squad']))
                                            )))
fig.update_layout(
    title='Expected Assists vs Assists',
    xaxis_title='Expected Assists',
    yaxis_title='Assists',
    plot_bgcolor='white',
    paper_bgcolor='whitesmoke'
)
fig.write_html('xAvsAssists.html',
               auto_open=True)
