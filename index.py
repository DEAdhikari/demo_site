import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt

#https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Transaction Analyzer",
                   page_icon=":bar_chart:",
                   )

dataset = pd.read_excel(
    io='GenAIExcelAnalysis.xlsx',
    engine='openpyxl',
    sheet_name='Sheet1',
    skiprows=3,
    usecols='A:E',
    )

#st.dataframe(dataset)

#Sidebar Code
st.sidebar.header("Please Filter Here:")
transactioNames = st.sidebar.multiselect(
    "Select Transaction Names",
    options=dataset["TransactionName"].unique(),
    default=dataset["TransactionName"].unique()
)

dataset_selection = dataset.query(
    "TransactionName == @transactioNames"
)

#Main Page - bar chart is an emoji. you can get any emoji from internei
st.title(":bar_chart:  Transaction Analysis")
st.markdown("##")

#with st.expander("Transaction Table"):
#st.dataframe(dataset_selection)


st.bar_chart(dataset_selection.set_index('TransactionName'), stack=False)   




