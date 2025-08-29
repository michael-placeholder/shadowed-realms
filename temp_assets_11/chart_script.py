import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Create the data
data = [
    {"Category": "UI Systems", "Script Count": 8, "Total Value": 270, "Monthly Revenue": 1789, "Avg Price": 34},
    {"Category": "AI Systems", "Script Count": 4, "Total Value": 415, "Monthly Revenue": 1038, "Avg Price": 104},
    {"Category": "Environment", "Script Count": 3, "Total Value": 255, "Monthly Revenue": 680, "Avg Price": 85},
    {"Category": "Core Framework", "Script Count": 1, "Total Value": 200, "Monthly Revenue": 600, "Avg Price": 200},
    {"Category": "Combat", "Script Count": 1, "Total Value": 125, "Monthly Revenue": 500, "Avg Price": 125},
    {"Category": "VFX", "Script Count": 2, "Total Value": 75, "Monthly Revenue": 413, "Avg Price": 38},
    {"Category": "Gameplay", "Script Count": 2, "Total Value": 70, "Monthly Revenue": 420, "Avg Price": 35},
    {"Category": "Programming", "Script Count": 2, "Total Value": 90, "Monthly Revenue": 405, "Avg Price": 45},
    {"Category": "Character", "Script Count": 1, "Total Value": 75, "Monthly Revenue": 375, "Avg Price": 75},
    {"Category": "Inventory", "Script Count": 1, "Total Value": 45, "Monthly Revenue": 360, "Avg Price": 45}
]

df = pd.DataFrame(data)

# Sort by Monthly Revenue (descending) to highlight most valuable
df = df.sort_values('Monthly Revenue', ascending=False)

# Define colors
colors = ['#1FB8CD', '#DB4545', '#2E8B57', '#5D878F', '#D2BA4C', '#B4413C', '#964325', '#944454', '#13343B', '#DB4545']

# Create bar chart
fig = go.Figure()

fig.add_trace(go.Bar(
    x=df['Category'],
    y=df['Monthly Revenue'],
    name='Monthly Rev',
    marker_color=colors[:len(df)],
    customdata=df[['Script Count', 'Total Value', 'Avg Price']],
    hovertemplate='<b>%{x}</b><br>' +
                  'Monthly Rev: $%{y:.0f}<br>' +
                  'Scripts: %{customdata[0]}<br>' +
                  'Total Value: $%{customdata[1]}<br>' +
                  'Avg Price: $%{customdata[2]}<br>' +
                  '<extra></extra>'
))

fig.update_layout(
    title='Shadowed Realms Revenue by Category',
    xaxis_title='Category',
    yaxis_title='Monthly Rev ($)',
    showlegend=False
)

fig.update_xaxes(tickangle=45)
fig.update_traces(cliponaxis=False)

# Format y-axis to show values in thousands
fig.update_yaxes(tickformat='$.0f')

fig.write_image('shadowed_realms_revenue.png', width=800, height=600)