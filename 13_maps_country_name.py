import pandas as pd
import plotly.express as px

# Sample data with country names and values
data = {'Country': ['USA', 'Canada', 'Mexico', 'Brazil', 'Argentina'],
        'Value': [10, 20, 15, 25, 18]}

df = pd.DataFrame(data)

# Use Plotly Express to create a choropleth map
fig = px.choropleth(df, 
                    locations='Country', 
                    locationmode='country names',
                    color='Value',
                    color_continuous_scale="Viridis",
                    title='Choropleth Map based on Country Names')

# Show the figure
fig.show()