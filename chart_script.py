import pandas as pd
import plotly.graph_objects as go

# Data
data = [
  {"Month": 1, "Assets Created": 15, "Cumulative Portfolio Value": 245, "Conservative Revenue": 74, "Realistic Revenue": 147, "Optimistic Revenue": 245},
  {"Month": 2, "Assets Created": 25, "Cumulative Portfolio Value": 710, "Conservative Revenue": 213, "Realistic Revenue": 426, "Optimistic Revenue": 710},
  {"Month": 3, "Assets Created": 30, "Cumulative Portfolio Value": 1200, "Conservative Revenue": 360, "Realistic Revenue": 720, "Optimistic Revenue": 1200},
  {"Month": 4, "Assets Created": 20, "Cumulative Portfolio Value": 1545, "Conservative Revenue": 464, "Realistic Revenue": 927, "Optimistic Revenue": 1545},
  {"Month": 5, "Assets Created": 25, "Cumulative Portfolio Value": 1945, "Conservative Revenue": 584, "Realistic Revenue": 1167, "Optimistic Revenue": 1945},
  {"Month": 6, "Assets Created": 35, "Cumulative Portfolio Value": 2680, "Conservative Revenue": 804, "Realistic Revenue": 1608, "Optimistic Revenue": 2680}
]

df = pd.DataFrame(data)

# Create the chart
fig = go.Figure()

# Add lines for each scenario using brand colors
fig.add_trace(go.Scatter(x=df['Month'], y=df['Cumulative Portfolio Value'], 
                         mode='lines+markers', name='Portfolio Val', 
                         line=dict(color='#1FB8CD', width=3),
                         hovertemplate='Month %{x}<br>Portfolio: $%{y}<extra></extra>'))

fig.add_trace(go.Scatter(x=df['Month'], y=df['Conservative Revenue'], 
                         mode='lines+markers', name='Conservative', 
                         line=dict(color='#DB4545', width=3),
                         hovertemplate='Month %{x}<br>Conservative: $%{y}<extra></extra>'))

fig.add_trace(go.Scatter(x=df['Month'], y=df['Realistic Revenue'], 
                         mode='lines+markers', name='Realistic', 
                         line=dict(color='#2E8B57', width=3),
                         hovertemplate='Month %{x}<br>Realistic: $%{y}<extra></extra>'))

fig.add_trace(go.Scatter(x=df['Month'], y=df['Optimistic Revenue'], 
                         mode='lines+markers', name='Optimistic', 
                         line=dict(color='#5D878F', width=3),
                         hovertemplate='Month %{x}<br>Optimistic: $%{y}<extra></extra>'))

# Update layout
fig.update_layout(
    title='Shadowed Realms Revenue Projection',
    xaxis_title='Month',
    yaxis_title='Revenue ($)',
    legend=dict(orientation='h', yanchor='bottom', y=1.05, xanchor='center', x=0.5)
)

fig.update_traces(cliponaxis=False)

# Update axes
fig.update_xaxes(dtick=1)
fig.update_yaxes(tickformat='$,')

# Save the chart
fig.write_image('shadowed_realms_revenue_projection.png')