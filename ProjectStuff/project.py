import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.graph_objs as go

#Loads CSV files from Datasets
df1 = pd.read_csv('../DS/Hyg')
df2 = pd.read_csv('../DS/San')
df3 = pd.read_csv('../DS/Wat')
app = dash.Dash()


# Stack bar chart data

#worst hygiene stacked
stackbarchart_df1 = df1.apply(lambda x: x.str.strip() if x.dtype == "object" else x)


stackbarchart_df1 = stackbarchart_df1.sort_values(by=['%No_Facility'], ascending=[False]).head(20).reset_index()
trace1_stackbarchart = go.Bar(x=stackbarchart_df1['Location'], y=stackbarchart_df1['%Basic'], name='Basic',
                              marker={'color': '#CD7F32'})
trace2_stackbarchart = go.Bar(x=stackbarchart_df1['Location'], y=stackbarchart_df1['%Limited'], name='Limited',
                              marker={'color': '#9EA0A1'})
trace3_stackbarchart = go.Bar(x=stackbarchart_df1['Location'], y=stackbarchart_df1['%No_Facility'], name='No Facility',
                              marker={'color': '#FFD700'})
worst_hyg_stackbarchart = [trace1_stackbarchart, trace2_stackbarchart, trace3_stackbarchart]

#worst sanitation
stackbarchart_df2 = df2.apply(lambda x: x.str.strip() if x.dtype == "object" else x)


stackbarchart_df2 = stackbarchart_df2.sort_values(by=['%Open_Defecation'], ascending=[False]).head(20).reset_index()
san_trace1_stackbarchart = go.Bar(x=stackbarchart_df2['Location'], y=stackbarchart_df2['%Basic'], name='Basic',
                              marker={'color': '#CD7F32'})
san_trace2_stackbarchart = go.Bar(x=stackbarchart_df2['Location'], y=stackbarchart_df2['%Limited'], name='Limited',
                              marker={'color': '#9EA0A1'})
san_trace3_stackbarchart = go.Bar(x=stackbarchart_df2['Location'], y=stackbarchart_df2['%Unimproved'], name='Unimproved',
                              marker={'color': '#FFD700'})
san_trace4_stackbarchart = go.Bar(x=stackbarchart_df2['Location'], y=stackbarchart_df2['%Open_Defecation'],name= 'Open Defecation',
                                  marker={'color': '#ef3e18'})
worst_san_stackbarchart = [san_trace1_stackbarchart, san_trace2_stackbarchart, san_trace3_stackbarchart,san_trace4_stackbarchart]

#worst water accesibility
stackbarchart_df3 = df3.apply(lambda x: x.str.strip() if x.dtype == "object" else x)


stackbarchart_df3 = stackbarchart_df3.sort_values(by=['%Basic'], ascending=[True]).head(20).reset_index()
wat_trace1_stackbarchart = go.Bar(x=stackbarchart_df3['Location'], y=stackbarchart_df3['%Basic'], name='Basic',
                              marker={'color': '#CD7F32'})
wat_trace2_stackbarchart = go.Bar(x=stackbarchart_df3['Location'], y=stackbarchart_df3['%Limited'], name='Limited',
                              marker={'color': '#9EA0A1'})
wat_trace3_stackbarchart = go.Bar(x=stackbarchart_df3['Location'], y=stackbarchart_df3['%Unimproved'], name='Unimproved',
                              marker={'color': '#FFD700'})
wat_trace4_stackbarchart = go.Bar(x=stackbarchart_df3['Location'], y=stackbarchart_df3['%Surface'], name='Surface',
                                  marker={'color': '#ef3e18'})
worst_wat_stackbarchart = [wat_trace1_stackbarchart, wat_trace2_stackbarchart, wat_trace3_stackbarchart,wat_trace4_stackbarchart]



#Layout
app.layout = html.Div(children=[
    html.H1(children='Python Dash',
            style={
                'textAlign': 'center',
                'color': '#ef3e18',
            }
            ),
    html.Div('Web dashboard for Group 20', style={'textAlign': 'center'}),
    html.Div('Hyg Levels', style={'textAlign': 'center'}),
    html.Br(),
    html.Br(),
    html.Hr(style={'color': '#7FDBFF'}),
    html.H3('The 20 countries with the worst hygiene accessibility', style={'color': '#df1e56'}),
    html.Div(
        'This stack bar chart represent the 20 countries with the lowest levels of access to hygiene facilities.'),
    dcc.Graph(id='graph1',
              figure={
                  'data': worst_hyg_stackbarchart,
                  'layout': go.Layout(title='Does it Work',
                                      xaxis={'title': 'Location'}, yaxis={'title': 'Percent'},
                                      barmode='stack')
              }
              ),
html.Hr(style={'color': '#7FDBFF'}),
    html.H3('Worst Sanitation Access Stacked Bar Chart', style={'color': '#df1e56'}),
    html.Div(
        '20 countries with worst sanitation'),
    dcc.Graph(id='graph2',
              figure={
                  'data': worst_san_stackbarchart,
                  'layout': go.Layout(title='Worst Sanitation',
                                      xaxis={'title': 'Location'}, yaxis={'title': 'Percent'},
                                      barmode='stack')
              }
              ),
html.Hr(style={'color': '#7FDBFF'}),
    html.H3('Drinking Water Stacked Bar Chart', style={'color': '#df1e56'}),
    html.Div(
        '20 countries with worst access to basic drinking water'),
    dcc.Graph(id='graph3',
              figure={
                  'data': worst_wat_stackbarchart,
                  'layout': go.Layout(title='Worst Drinking Water Accessibility',
                                      xaxis={'title': 'Location'}, yaxis={'title': 'Percent'},
                                      barmode='stack')
              }
              )


])





if __name__ == '__main__':
    app.run_server()