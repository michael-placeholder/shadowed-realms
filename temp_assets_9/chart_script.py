import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Create the data
data = [
    {"Asset Category": "3D Art Assets", "Asset Count": 23, "Total Value": 1675, "Monthly Revenue": 3986, "Average Price": 73, "Revenue Share": "27%"},
    {"Asset Category": "No-Code GUI Tools", "Total Value": 2420, "Asset Count": 20, "Monthly Revenue": 5572, "Average Price": 121, "Revenue Share": "37%"},
    {"Asset Category": "Educational Packages", "Asset Count": 8, "Total Value": 806, "Monthly Revenue": 5385, "Average Price": 101, "Revenue Share": "36%"}
]

df = pd.DataFrame(data)

# Create color palette
colors = ['#1FB8CD', '#DB4545', '#2E8B57']

# Create grouped bar chart
fig = go.Figure()

# Add Total Value bars
fig.add_trace(go.Bar(
    name='Total Value ($)',
    x=df['Asset Category'],
    y=df['Total Value'],
    marker_color=colors[0],
    text=[f'${v:,.0f}' for v in df['Total Value']],
    textposition='auto',
    hovertemplate='<b>%{x}</b><br>Total Value: $%{y:,.0f}<extra></extra>'
))

# Add Monthly Revenue bars
fig.add_trace(go.Bar(
    name='Monthly Rev ($)',
    x=df['Asset Category'],
    y=df['Monthly Revenue'],
    marker_color=colors[1],
    text=[f'${v:,.0f}' for v in df['Monthly Revenue']],
    textposition='auto',
    hovertemplate='<b>%{x}</b><br>Monthly Revenue: $%{y:,.0f}<extra></extra>'
))

# Update layout
fig.update_layout(
    title='Revenue Breakdown by Asset Category',
    xaxis_title='Category',
    yaxis_title='Value ($)',
    barmode='group',
    legend=dict(orientation='h', yanchor='bottom', y=1.05, xanchor='center', x=0.5)
)

# Update x-axis to show shorter category names
fig.update_xaxes(
    ticktext=['3D Art Assets', 'GUI Tools', 'Educational'],
    tickvals=df['Asset Category']
)

# Update traces
fig.update_traces(cliponaxis=False)

# Save the chart
fig.write_image('revenue_breakdown_chart.png')