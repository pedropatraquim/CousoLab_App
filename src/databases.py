from pandas.api.types import (
    is_categorical_dtype,
    is_datetime64_any_dtype,
    is_numeric_dtype,
    is_object_dtype,
)
import pandas as pd
import streamlit as st
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import os
from matplotlib.backends.backend_agg import RendererAgg

# Loading the data
@st.cache
def get_data_shortCDSs():
    return pd.read_csv(os.path.join(os.getcwd(), './assets/databases/shortCDS_table_2020_evo_prot_Pedro.csv'))

@st.cache
def get_data_lncORFs():
    return pd.read_csv(os.path.join(os.getcwd(), './assets/databases/lncORF_table_2020_prot_Pedro.csv'))

@st.cache
def get_data_uORFs():
    return pd.read_csv(os.path.join(os.getcwd(), './assets/databases/uORF_table_2020_prot_Pedro.csv'))

@st.cache
def get_data_canonical():
    return pd.read_csv(os.path.join(os.getcwd(), './assets/databases/canonical_table_2020_prot_Pedro.csv'))

@st.cache
def get_data_shortIsoforms():
    return pd.read_csv(os.path.join(os.getcwd(), './assets/databases/shortisoform_table.csv'))

# Configuration of the page
st.set_page_config(layout="wide")

st.title('Couso lab ORF Databases')
st.markdown("""
This app performs simple visualization of the Couso lab ORF tables
""")


def filter_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    """
    Adds a UI on top of a dataframe to let viewers filter columns

    Args:
        df (pd.DataFrame): Original dataframe

    Returns:
        pd.DataFrame: Filtered dataframe
    """
    modify = st.checkbox("Add filters")

    if not modify:
        return df

    df = df.copy()

    # Try to convert datetimes into a standard format (datetime, no timezone)
    for col in df.columns:
        if is_object_dtype(df[col]):
            try:
                df[col] = pd.to_datetime(df[col])
            except Exception:
                pass

        if is_datetime64_any_dtype(df[col]):
            df[col] = df[col].dt.tz_localize(None)

    modification_container = st.container()

    with modification_container:
        to_filter_columns = st.multiselect("Filter dataframe on", df.columns)
        for column in to_filter_columns:
            left, right = st.columns((1, 20))
            # Treat columns with < 10 unique values as categorical
            if is_categorical_dtype(df[column]) or df[column].nunique() < 10:
                user_cat_input = right.multiselect(
                    f"Values for {column}",
                    df[column].unique(),
                    default=list(df[column].unique()),
                )
                df = df[df[column].isin(user_cat_input)]
            elif is_numeric_dtype(df[column]):
                _min = float(df[column].min())
                _max = float(df[column].max())
                step = (_max - _min) / 100
                user_num_input = right.slider(
                    f"Values for {column}",
                    min_value=_min,
                    max_value=_max,
                    value=(_min, _max),
                    step=step,
                )
                df = df[df[column].between(*user_num_input)]
            elif is_datetime64_any_dtype(df[column]):
                user_date_input = right.date_input(
                    f"Values for {column}",
                    value=(
                        df[column].min(),
                        df[column].max(),
                    ),
                )
                if len(user_date_input) == 2:
                    user_date_input = tuple(map(pd.to_datetime, user_date_input))
                    start_date, end_date = user_date_input
                    df = df.loc[df[column].between(start_date, end_date)]
            else:
                user_text_input = right.text_input(
                    f"Substring or regex in {column}",
                )
                if user_text_input:
                    df = df[df[column].astype(str).str.contains(user_text_input)]

    return df

# User interface
selected_table = st.radio(
    "Select the table to display:",
    options=["shortCDSs", "lncORFs", "uORFs", "Canonical", "Short isoforms"], horizontal=True
)

if selected_table == "shortCDSs":
    df = filter_dataframe(get_data_shortCDSs())
elif selected_table == "lncORFs":
    df = filter_dataframe(get_data_lncORFs())
elif selected_table == "uORFs":
    df = filter_dataframe(get_data_uORFs())
elif selected_table == "Canonical":
    df = filter_dataframe(get_data_canonical())
else:
    df = filter_dataframe(get_data_shortIsoforms())

st.write(df)

st.download_button('Download CSV', df.to_csv(), 'text/csv')
