# import streamlit as st
# import plotly.figure_factory as ff
# import numpy as np
# import plotly.express as px

# x1 = np.random.randn(200)+2
# x2 = np.random.randn(200)
# x3 = np.random.randn(200)-2

# hist_data = [x1, x2, x3]

# grouplabels = ['group1', 'group2', 'group3']

# # print(hist_data)

# fig = px.line(x=hist_data[0], y=hist_data[1])

# # fig = ff.create_2d_density(hist_data[0], hist_data[1])

# # fig = ff.create_distplot(hist_data, grouplabels)

# st.plotly_chart(fig, use_container_width=True)


import yfinance as  yf
import streamlit as st
# import plotly.express as px
import plotly.graph_objects as go
import datetime as dt


data = yf.download('USDINR=X', start=dt.date.today()-dt.timedelta(days=30), end=dt.date.today()+dt.timedelta(days=1))

# fig = px.line(data['Close'], markers=True)
# st.plotly_chart(fig, use_container_width=True)


# fig = go.Figure(data=go.Line(data['Close'], mode='markers'))
# fig.update_layout(hovermode='closest')

# st.plotly_chart(fig, use_container_width=True)



# import plotly.graph_objects as go

# # Create some example data
# x = [1, 2, 3, 4, 5]
# y = [10, 15, 13, 17, 12]

# # Create a line trace
# trace = go.Scatter(x=x, y=y, mode='lines', hovertemplate='x: %{x}<br>y: %{y}')

# # Create the figure
# fig = go.Figure(data=trace)
# fig.update_layout(hovermode='closest')

# Show the plot
# fig.show()


import plotly.graph_objects as go
from plotly.offline import init_notebook_mode, iplot
init_notebook_mode(connected=True)

# Create some example data
x = [1, 2, 3, 4, 5]
y = [10, 15, 13, 17, 12]

# Create a line trace
trace = go.Scatter(x=x, y=y, mode='lines')

# Create the figure
fig = go.Figure(data=trace)

# Add a vertical line shape
fig.update_layout(
    shapes=[
        dict(
            type='line',
            x0=3,
            y0=min(y),
            x1=3,
            y1=max(y),
            line=dict(color='red', width=2),
            xref='x',
            yref='y',
            name='vertical_line'
        )
    ]
)

# Enable the JavaScript event handling
fig.update_layout(
    updatemenus=[
        dict(
            type="buttons",
            buttons=[
                dict(
                    label="Enable Move",
                    method="relayout",
                    args=[
                        {"updatemenus": None},
                        {
                            "dragmode": "x",
                            "shapes[0].x0": True,
                            "shapes[0].x1": True,
                        },
                    ],
                )
            ],
        )
    ]
)

# Show the plot
# iplot(fig)


st.plotly_chart(fig, use_container_width=True)
