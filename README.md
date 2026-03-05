# Electricity Theft Detection using Machine Learning

## Overview

This project detects suspicious electricity consumption patterns using Machine Learning.
It analyzes electricity usage data and identifies abnormal behavior that may indicate electricity theft.

An interactive Streamlit dashboard is used to visualize results and analyze consumer electricity usage.

## Features

* Machine Learning based anomaly detection
* Interactive Streamlit dashboard
* Electricity consumption visualization
* Suspicious consumer detection
* Consumer usage analysis
* Downloadable prediction report

## Machine Learning Model

The project uses **Isolation Forest**, an anomaly detection algorithm that identifies unusual electricity consumption patterns.

## Technologies Used

Python
Streamlit
Pandas
Scikit-learn
Plotly
Joblib

## Project Structure

electricity-theft-detection
│
├── app.py
├── train_model.py
├── predict.py
├── requirements.txt
│
├── data
│   └── electricity_data.csv
│
└── models
└── theft_model.pkl

## Installation

Install required libraries:

pip install -r requirements.txt

## Dataset

The dataset used is the SGCC Electricity Theft Detection dataset.

Because the dataset is large, it is not included in this repository.

Download it from:
https://www.kaggle.com/datasets/bensalem14/sgcc-dataset

After downloading, place it inside:

data/electricity_data.csv

## Running the Project

Train the model:

python train_model.py

Run the Streamlit dashboard:

streamlit run app.py

## Output

The system classifies consumers into:

* Normal
* Suspicious

Suspicious consumers may indicate possible electricity theft and require further investigation.
