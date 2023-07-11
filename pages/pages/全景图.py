import pandas as pd
import streamlit as st
st.set_page_config(
    page_title="全景图页面",
    page_icon="￥",
layout = "wide"

)
tab1, tab2, tab3 = st.tabs(["行业", "概念","期货"])

def read_excel(fname):
    df = pd.read_csv(fname)
    return df
with tab1:
   st.header("行业全景")
   f = r'E:\项目\pyqt_stock\res\vol\l1_vol_chg20230702.csv'
   df = read_excel(f)
   df = df.dropna()
   styled_df = df.style.background_gradient(cmap='coolwarm')
   st.write('一级行业')
   st.data_editor(
       styled_df,
       column_config={
           "line_chart": st.column_config.LineChartColumn(
               "近一年走势",
               width="medium",
               help="The sales volume in the last 6 months",

           ),
       },
       hide_index=True,
   )
   f = r'E:\项目\pyqt_stock\res\vol\l2_vol_chg20230701.csv'
   df = read_excel(f)
   df = df.dropna()
   styled_df = df.style.background_gradient(cmap='coolwarm')
   st.write('二级行业')
   st.data_editor(
       styled_df,
       column_config={
           "line_chart": st.column_config.LineChartColumn(
               "近一年走势",
               width="medium",
               help="The sales volume in the last 6 months",

           ),
       },
       hide_index=True,
   )

with tab2:
   st.header("概念全景")
   st.image("https://static.streamlit.io/examples/dog.jpg", width=200)


