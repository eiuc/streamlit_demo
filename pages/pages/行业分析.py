import streamlit as st
st.set_page_config(
        page_title="显示网页示例",
        page_icon="🌐",
        layout="wide",
        initial_sidebar_state="expanded",
        )
with open('E:\项目\streamlit_demo\pages\行业申万.txt',encoding='utf-8') as f:
    data = f.read()
    data_l = eval(data)
    industry_data={}
    for item in data_l:
        l1key = item['industryName']
        dic2={}
        l2s = item['children']
        for l2 in l2s:
            l2key = l2['industryName']
            l3s = l2['children']
            l3_l = []
            for l3 in l3s:
                l3_l.append(l3['industryName'])
            dic2[l2key] = l3_l
        industry_data[l1key] = dic2
with st.sidebar:

    st.write('请选择行业：')

    industry_level1 = st.selectbox('一级行业', list(industry_data.keys()))
    industry_level2 = st.selectbox('二级行业', list(industry_data[industry_level1].keys()))
    industry_level3 = st.selectbox('三级行业', industry_data[industry_level1][industry_level2])

    st.session_state.selected_option_1 = None
    st.session_state.selected_option_2 = None
    st.session_state.selected_option_3 = None
    analysis_text = ""
    selected_option = st.radio("请选择行业级别：", ("一级行业", "二级行业", "三级行业"))
    if selected_option == "一级行业":
        analysis_text = f"正在查看 {industry_level1}的行业分析..."
    elif selected_option == "二级行业":
        analysis_text = f"正在查看 {industry_level1} > {industry_level2} 的行业分析..."
    elif selected_option == "三级行业":
        analysis_text = f"正在查看 {industry_level1} > {industry_level2} > {industry_level3} 的行业分析..."


    st.write(analysis_text)

# st.components.v1.iframe("https://data.eastmoney.com/cjsj/hgjck.html")
page_height = 600

# 创建一个具有固定高度的容器
html = f"""
    <div style="height:{page_height}px; overflow:auto;">
        <p>宏观经济</p>
        <iframe src="https://data.eastmoney.com/cjsj/hgjck.html" width="100%" height="{page_height}px"></iframe>
    </div>
    """
# 在 Streamlit 应用中显示容器和嵌入的网页
st.markdown(html, unsafe_allow_html=True)


import plotly.graph_objects as go
from plotly.subplots import make_subplots
from datetime import datetime

# 创建动态 K 线图
def create_dynamic_kline_with_volume():
    # 创建随机的 K 线数据集和成交量，这里只是一个示例
    kline_data = [
        {"date": "2023-06-01", "open": 100, "high": 110, "low": 90, "close": 105},
        {"date": "2023-06-02", "open": 105, "high": 120, "low": 95, "close": 115},
        {"date": "2023-06-03", "open": 115, "high": 125, "low": 100, "close": 120},
        # ... 添加更多数据
    ]
    volume_data = [
        1000,
        1500,
        2000,
        # ... 添加更多数据
    ]

    # 创建布局和子图
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, row_heights=[0.6, 0.4])

    # 转换日期字符串为 Python 的 datetime 对象
    dates = [datetime.strptime(data["date"], "%Y-%m-%d") for data in kline_data]

    # 绘制 K 线图和成交量
    for i, data in enumerate(kline_data):
        color = 'green' if data["close"] >= data["open"] else 'red'
        candlestick = go.Candlestick(
            x=[dates[i]],  # 使用日期作为 x 值
            open=[data["open"]],
            high=[data["high"]],
            low=[data["low"]],
            close=[data["close"]],
            increasing={'line': {'color': color}},
            decreasing={'line': {'color': color}},
            showlegend=False
        )
        fig.add_trace(candlestick, row=1, col=1)

        volume_bar = go.Bar(
            x=[dates[i]],  # 使用日期作为 x 值
            y=[volume_data[i]],
            marker=dict(color=color),
            showlegend=False
        )
        fig.add_trace(volume_bar, row=2, col=1)

    # 设置图表布局
    fig.update_layout(height=600, width=1200)

    return fig

# 在 Streamlit 应用中显示动态 K 线图和成交量
def main():
    st.title("带成交量的动态 K 线图示例")

    # 创建动态 K 线图和成交量
    fig = create_dynamic_kline_with_volume()

    # 使用 Streamlit 显示图表
    st.plotly_chart(fig)

if __name__ == '__main__':
    main()
