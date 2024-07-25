import streamlit as st
import pandas as pd

def load_data(name):
    """
    Read an uploaded CSV file and return a Pandas DataFrame.

    Args:
        uploaded_file (file): The uploaded CSV file.

    Returns:
        pd.DataFrame: A DataFrame containing the data from the CSV file.
    """
    data = None
    uploaded_file = st.file_uploader(f"Upload a CSV file", type=["csv"], key=name)
    if (uploaded_file):
        data = pd.read_csv(uploaded_file)
    return data