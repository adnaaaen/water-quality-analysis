import streamlit as st
import numpy as np
from utils import helper

st.set_page_config(
    page_title="Home | Water Quality ",
    page_icon="💧",
    layout="wide",
    initial_sidebar_state="collapsed",
)
sidebar_content = helper.create_sidebar()

with st.sidebar:
    for item in sidebar_content:
        st.page_link(page=item["page"], label=item["label"], icon=item["icon"])


st.markdown("## **Ground Water Quality Analysis**")


st.markdown("#### **Objective**")
objective_text = """
This project aims to develop an interactive machine learning (ML) application that assesses and predicts the quality of ground water in various regions of India. This app leverages machine learning to predict water quality based on various parameters.
"""
st.write(objective_text)


st.markdown("#### **About Data**")
dataset_caption = """
This dataset, titled "Ground Water Quality 2021," provides comprehensive information on groundwater quality across various states and districts in India. The data has been collected for the year 2021
"""
st.write(dataset_caption)

# about dataset
st.caption("Sample Rows")

df = helper.get_df()

st.write(df.sample(5))
# download dataset
downloadable_df = helper.convert_df(df)
st.download_button(
    label="Download Dataset",
    data=downloadable_df,
    file_name="ground_water_quality.csv",
    mime="text/csv",
    icon=":material/download:",
)


one, two, three = st.columns(3)
with one:
    st.metric(label="Rows", value=df.shape[0])
    st.metric(
        label="Catagorical Features", value=len(df.select_dtypes(include="O").columns)
    )

with two:
    st.metric(label="Columns", value=df.shape[1])
    st.metric(label="No.of States", value=df["STATE"].nunique())

with three:
    st.metric(
        label="Numerical Features",
        value=len(df.select_dtypes(include=np.number).columns),
    )
    st.metric(label="No.of Districts", value=df["DISTRICT"].nunique())


st.caption("**Created by Adnan**")
