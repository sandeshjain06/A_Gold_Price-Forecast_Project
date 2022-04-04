from cProfile import label
from email.utils import format_datetime
from itertools import starmap
from tracemalloc import start
from wsgiref.handlers import format_date_time
import streamlit as st 
import pandas as pd 
import matplotlib.pyplot as plt
import statsmodels.api as sm
import time
from PIL import Image
import datetime
import base64
import streamlit as st


def set_bg_hack_url():
    '''
    A function to unpack an image from url and set as bg.
    Returns
    -------
    The background.
    '''
    st.markdown(
         f"""
         <style>
         .stApp {{
             background: url("D:\Sandesh\Flask\TimeSeries\images\images 7.jpg");
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

set_bg_hack_url()
@st.cache(allow_output_mutation=True)
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()
def set_png_as_page_bg(png_file):
    bin_str = get_base64_of_bin_file(png_file)
    page_bg_img = '''
    <style>
    body {
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
    }
    </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)
    return

set_png_as_page_bg('D:\Sandesh\Flask\TimeSeries\images\images 7.jpg')

st.title("Gold Price Forecasting")

df=pd.read_csv("gold_list.csv")
del df['Unnamed: 0']
df['Dates']=pd.to_datetime(df['Dates'], dayfirst = True)
df['Price']=df['Price'].str.replace(',','')
df_new=df.set_index('Dates').resample('MS').last()
df_new['Price']=df_new['Price'].astype('int')
st.write(df_new)

st.subheader("Gold Price from Year 2011-2021")

st.line_chart(df_new)

# start = df_new["Dates"].strftime("%Y-%m-%d")
# st.write(start)

# start_date = st.date_input("Start Date", value=pd.to_datetime("2021-01-31", format="%Y-%m-%d"))
# end_date = st.date_input("End Date", value=pd.to_datetime("today", format="%Y-%m-%d"))

# convert the dates to string
# start = start_date.strftime("%Y-%m-%d")
# end = end_date.strftime("%Y-%m-%d")

# st.table(pd.Series.loc[start:end])



Predict_values= st.slider("Select no of months to predict",min_value=0,max_value=48)
if Predict_values>0:
    
# 1,2,4,24
    with st.spinner('Loading.....'):

        model_sarimax=sm.tsa.statespace.SARIMAX(df_new['Price'],order=(1,2,1),seasonal_order=(1,2,1,12))
        model_sarimax_fit=model_sarimax.fit()

# df_new['SARIMA_Forecast']=model_sarimax_fit.predict(start=90,end=120 ,dynamic=True)
# df_new[['Price','SARIMA_Forecast']].plot(figsize=(10,5))

    #time.sleep(1)
        #st.balloons()

    future_pred_values=model_sarimax_fit.predict(start=len(df_new)-1,end=len(df_new)-1+Predict_values,typ='levels').rename('Gold Price')
    st.subheader("Gold Price Predicted for " + str(Predict_values) + " Months")
    st.write(future_pred_values)

    st.subheader("Graph Predicted for " + str(Predict_values) + " Months")
    st.line_chart(future_pred_values)


    st.subheader("Gold Price History")
    fig3=plt.figure(figsize=(12,6))
    #st.pyplot(fig3)
    df_new['Price'].plot(label="Actual")
    future_pred_values.plot(label="Predicted")
    #st.line_chart(df_new['Price'])
    st.pyplot(fig3)
 
    future_pred_values=model_sarimax_fit.predict(start=1,end=len(df_new)-1+Predict_values,typ='levels').rename('Gold Price')
    fig4=plt.figure(figsize=(12,6))
    df_new['Price'].plot(label="Actual")
    future_pred_values.plot(label="Predicted")
    st.pyplot(fig4)
    
    st.success('Done!')
    

#plt.title('SARIMA')
#st.success('Gold price values predicted !')

