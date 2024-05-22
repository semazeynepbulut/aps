from app.data.data_generation.generate_data import GenerateData
from app.core.config import settings
import matplotlib.pyplot as plt
import streamlit as st
import seaborn as sns
import pandas as pd
import numpy as np
import io

st.title(settings.PROJECT_NAME)
_NUMERIC_CONTINOUS_COLUMNS = [
    "Age",
    "Flight Distance",
    "Departure Delay in Minutes",
    "Arrival Delay in Minutes",
]
_NUMERIC_CONTINOUS_COLUMNS_SML = [
    "Age",
    "Departure Delay in Minutes",
    "Arrival Delay in Minutes",
]


@st.cache_data
def data_generation():
    data = GenerateData.generate()
    return data


def get_numeric_data(data: pd.DataFrame) -> pd.DataFrame:
    return data.select_dtypes(include=np.number).drop(["id"], axis=1)


def info(data: pd.DataFrame):

    buffer = io.StringIO()
    data.info(buf=buffer)
    info_str = buffer.getvalue()

    st.text(info_str)


def data_inspection(data: pd.DataFrame):
    st.subheader("Head of dataframe", divider="red")
    st.table(data.head())

    st.subheader("Get the summary information of the dataset", divider="red")
    info(data=data)

    st.subheader("Display basic statistics for numerical columns", divider="red")
    st.table(data.describe())


def descriptive_statistics(data: pd.DataFrame):
    st.subheader("Checking for missing values", divider="red")
    missing_values = data.isnull().sum()
    st.table(missing_values)

    st.subheader("Checking for median values", divider="red")
    median_values = get_numeric_data(data=data).median()
    st.table(median_values)

    st.subheader("Checking for mode values", divider="red")
    mode_values = get_numeric_data(data=data).mode().iloc[0]
    st.table(mode_values)


def line_chart_for_delay_columns(data: pd.DataFrame):
    st.text(
        "It is a known fact in the airline industry that there is a correlation between flight departure and arrival delays, so these two columns likely have a minimum correlation of 80%.",
    )
    chart_data = data[["Departure Delay in Minutes", "Arrival Delay in Minutes"]]
    st.line_chart(chart_data, color=["#FF0000", "#0000FF"])


def box_plot(data: pd.DataFrame):
    # Boxplots to check distributions and outliers
    fig = plt.figure(figsize=(28, 10))
    sns.boxplot(data=data)
    plt.title("Boxplots of Numerical Columns")
    st.pyplot(fig=fig)


def visualize(data: pd.DataFrame):
    line_chart_for_delay_columns(data=data)
    st.text("Flight distance should be normalize")
    box_plot(data=data[_NUMERIC_CONTINOUS_COLUMNS])
    st.text("Delay in minutes columns and age have still different value range")
    box_plot(data=data[_NUMERIC_CONTINOUS_COLUMNS_SML])
    box_plot(data=data.drop(_NUMERIC_CONTINOUS_COLUMNS, axis=1))


def data_visualization_task():
    df = data_generation()
    data_inspection(data=df)
    descriptive_statistics(data=df)
    visualize(data=get_numeric_data(data=df))
