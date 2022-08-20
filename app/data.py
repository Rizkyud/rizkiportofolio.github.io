import streamlit as st
import pandas as pd
import pymysql.cursors


def app():
    df = pd.read_csv('jantungg.csv')
    df.drop('Unnamed: 0', axis='columns', inplace=True)
    df['age'] = df['age'].astype(int)

    st.subheader("Data diambil dari kaggle :")
    st.markdown(
        "[DOWNLOAD](https://www.kaggle.com/andrewmvd/heart-failure-clinical-data)")
    st.dataframe(df)

    shwdata = st.multiselect(
        'Pilih Kolom yang mau ditampilkan:', df.columns, default=[])
    st.write(df[shwdata])

    st.text('=============RIZKI WAHYUDI====================')
