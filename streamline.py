import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(page_title="Data Visualization App", layout="wide")

st.title("📊 Data Visualization Dashboard")

# -----------------------------
# File Upload
# -----------------------------
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    # -----------------------------
    # Show Data
    # -----------------------------
    st.subheader("Dataset Preview")
    st.dataframe(df)

    # -----------------------------
    # Column Selection
    # -----------------------------
    columns = df.columns.tolist()

    x_col = st.selectbox("Select X-axis", columns)
    y_col = st.selectbox("Select Y-axis", columns)

    # -----------------------------
    # Chart Type Selection
    # -----------------------------
    chart_type = st.selectbox(
        "Select Chart Type",
        ["Line Chart", "Bar Chart", "Scatter Plot"]
    )

    # -----------------------------
    # Plotting
    # -----------------------------
    st.subheader("Chart")

    fig, ax = plt.subplots()

    if chart_type == "Line Chart":
        ax.plot(df[x_col], df[y_col], marker='o')

    elif chart_type == "Bar Chart":
        ax.bar(df[x_col], df[y_col])

    elif chart_type == "Scatter Plot":
        ax.scatter(df[x_col], df[y_col])

    ax.set_xlabel(x_col)
    ax.set_ylabel(y_col)
    ax.set_title(f"{chart_type}: {x_col} vs {y_col}")

    st.pyplot(fig)

    # -----------------------------
    # Basic Stats
    # -----------------------------
    st.subheader("Basic Statistics")
    st.write(df.describe())

else:
    st.info("Please upload a CSV file to begin.")

# -----------------------------
# Sidebar Info
# -----------------------------
st.sidebar.title("About")
st.sidebar.info(
    """
    This is a simple data visualization app built with Streamlit.

    Features:
    - Upload CSV
    - Interactive charts
    - Basic statistics

    Good for:
    - Data Analytics Projects
    - Cybersecurity Logs Visualization
    - Portfolio Demo
    """
)
