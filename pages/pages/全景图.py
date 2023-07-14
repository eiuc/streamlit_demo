import pandas as pd
import streamlit as st
import requests
st.set_page_config(
    page_title="全景图页面",
    page_icon="￥",
layout = "wide"

)
tab1, tab2, tab3 = st.tabs(["行业", "概念","公司"])
@st.cache_data
def get_level(level=[1,2]):
    dic={}
    for i,l in enumerate(level):
        url = f'http://127.0.0.1:5000/industry_cv/{l}'
        jdata = requests.get(url).json()

        df = pd.read_json(jdata, orient='records')

        df = df.dropna()
        dic[i]=df
    return dic
@st.cache_data
def get_concept():
    url = f'http://127.0.0.1:5000/concept'
    jdata = requests.get(url).json()

    df = pd.read_json(jdata, orient='records')

    df = df.dropna()

    return df
@st.cache_data
def get_company():
    url = f'http://127.0.0.1:5000/company'
    jdata = requests.get(url).json()

    df = pd.read_json(jdata, orient='records')

    df = df.dropna()

    return df
with tab1:
   st.header("行业全景")
   dic = get_level()
   df = dic[0]
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
   df2 = dic[1]
   styled_df = df2.style.background_gradient(cmap='coolwarm')
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
   # st.image("https://static.streamlit.io/examples/dog.jpg", width=200)
   df = get_concept()
   styled_df = df.style.background_gradient(cmap='coolwarm')
   st.write('概念')
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
   # 创建一个具有固定高度的容器
   page_height = 600
   html = f"""
       <div style="height:{page_height}px; overflow:auto;">
           <p>概念</p>
           <iframe src="http://quote.eastmoney.com/center/boardlist.html#concept_board" width="100%" height="{page_height}px"></iframe>
       </div>
       """
   # 在 Streamlit 应用中显示容器和嵌入的网页
   st.markdown(html, unsafe_allow_html=True)
with tab3:
   st.header("公司全景")
   # st.image("https://static.streamlit.io/examples/dog.jpg", width=200)
   df = get_company()
   styled_df = df.style.background_gradient(cmap='coolwarm')
   st.write('概念')
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


