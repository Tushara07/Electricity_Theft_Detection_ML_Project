import streamlit as st
import pandas as pd
import plotly.express as px
from predict import detect_theft

st.set_page_config(page_title="Electricity Theft Detection Dashboard", layout="wide")

st.title("Electricity Theft Detection Dashboard")

# Button to load dataset
if st.button("Load Dataset"):

    data = pd.read_csv("data/electricity_data.csv")

    st.subheader("Dataset Overview")
    st.write("Rows:", data.shape[0], "Columns:", data.shape[1])

    st.dataframe(data.head())

    # Run prediction
    result = detect_theft(data)

    st.divider()

    # ================= KPI =================

    total = len(result)
    suspicious = len(result[result["Prediction"] == "Suspicious"])
    normal = len(result[result["Prediction"] == "Normal"])

    col1, col2, col3 = st.columns(3)

    col1.metric("Total Consumers", total)
    col2.metric("Normal Consumers", normal)
    col3.metric("Suspicious Consumers", suspicious)

    st.divider()

    # ================= PIE CHART =================

    st.subheader("Prediction Distribution")

    fig = px.pie(result, names="Prediction", title="Normal vs Suspicious Consumers")

    st.plotly_chart(fig, use_container_width=True)

    st.divider()

    # ================= SUSPICIOUS TABLE =================

    st.subheader("Suspicious Consumers")

    suspicious_data = result[result["Prediction"] == "Suspicious"]

    st.dataframe(suspicious_data)

    st.divider()

    # ================= SEARCH CONSUMER =================

    st.subheader("Consumer Consumption Analysis")

    consumer_id = st.selectbox(
        "Select Consumer ID",
        result["CONS_NO"].unique()
    )

    consumer = result[result["CONS_NO"] == consumer_id]

    st.write("Consumer Status:", consumer["Prediction"].values[0])

    consumption = consumer.drop(
        ["CONS_NO", "FLAG", "Prediction"], axis=1
    ).T

    consumption.columns = ["Consumption"]

    fig2 = px.line(
        consumption,
        title="Electricity Consumption Pattern",
        labels={"index": "Date", "Consumption": "Usage"},
    )

    st.plotly_chart(fig2, use_container_width=True)

    # ================= DOWNLOAD =================

    st.subheader("Download Results")

    csv = result.to_csv(index=False)

    st.download_button(
        "Download Prediction Report",
        csv,
        "electricity_theft_results.csv",
        "text/csv",
    )