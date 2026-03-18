import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

st.set_page_config(page_title="Simple Streamlit Dashboard", layout="wide")
st.title("Simple Streamlit Dashboard")

# Generate sample data
np.random.seed(42)
n = 200
df = pd.DataFrame({
    'x': np.random.randn(n).cumsum(),
    'y': np.random.randn(n).cumsum(),
    'category': np.random.choice(['A', 'B', 'C'], size=n),
    'value': np.random.rand(n) * 100,
})

# Sidebar controls
st.sidebar.header("Filters")
cat = st.sidebar.multiselect("Category", options=sorted(df['category'].unique()), default=sorted(df['category'].unique()))
x_min, x_max = float(df['x'].min()), float(df['x'].max())
x_range = st.sidebar.slider("X range", min_value=x_min, max_value=x_max, value=(x_min, x_max))
show_reg = st.sidebar.checkbox("Show regression line", value=False)

# Filter data
filtered = df[df['category'].isin(cat)]
filtered = filtered[(filtered['x'] >= x_range[0]) & (filtered['x'] <= x_range[1])]

# Chart
st.subheader("Scatter plot")
chart = alt.Chart(filtered).mark_circle(size=60).encode(
    x='x',
    y='y',
    color='category',
    tooltip=['x', 'y', 'category', 'value']
).interactive()

if show_reg and not filtered.empty:
    reg = chart.transform_regression('x', 'y').mark_line(color='black')
    layered = alt.layer(chart, reg).resolve_scale(color='independent')
    st.altair_chart(layered, use_container_width=True)
else:
    st.altair_chart(chart, use_container_width=True)

st.subheader("Data")
st.dataframe(filtered.reset_index(drop=True))

st.caption("Run: python -m pip install -r requirements.txt && streamlit run streamlit_app.py")
