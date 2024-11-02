import streamlit as st
import pandas as pd
import io

st.write("Here's our first attempt at using data to create a table:")
df = pd.read_csv("data.csv")
st.write(df)


