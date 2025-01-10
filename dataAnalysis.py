import numpy as np
import pandas as pd 
import matplotlib as plt
import seaborn as sns 
import streamlit as st 
import plotly.express as px

@st.cache_data
def load_data(file):
    return pd.read_csv(file)

file =  st.file_uploader("upload file ",type=["csv"])
if file is not None :
    df = load_data(file)
    
    
    n_rows = st.slider("Choose number of rows ", 
                       min_value=5 , max_value=len(df),step=1)
    col_to_show = st.multiselect("Select columns to show " , 
                   df.columns.tolist(),default= df.columns.tolist()
                   )
    numerical_columns = df.select_dtypes(include = np.number).columns.to_list()
    st.write(df[:n_rows][col_to_show])
    
    tab1 , tab2 = st.tabs(["Scatter","histogram"])
    with tab1 :
        col1 ,col2 , col3 = st.columns(3)
        with col1:
            x_axis = st.selectbox("Select colmun on x axis :",numerical_columns)
        with col2:
            y_axis = st.selectbox("Select colmun on y axis :",numerical_columns)
        with col3:    
            color = st.selectbox("Select column to be color : " ,df.columns)
        fig_scatter = px.scatter(df , x= x_axis,y= y_axis ,
                                 color=color)
        st.plotly_chart(fig_scatter)
    
    with tab2 :
        histogram_feature = st.selectbox("Selection feature to histogram ", numerical_columns)
        fig_hist = px.histogram(df,x=histogram_feature)
        st.plotly_chart(fig_hist)
        
