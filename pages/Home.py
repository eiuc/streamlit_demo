import streamlit as st
import time
import pandas as pd
from streamlit_elements import elements, mui, html
st.set_page_config(
    page_title="Hello",
    page_icon="👋",
layout = "wide"

)

st.write("# Welcome to Streamlit! 👋")

st.sidebar.success("Select a demo above.")

st.markdown(
    """
    Streamlit is an open-source app framework built specifically for
    Machine Learning and Data Science projects.
    **👈 Select a demo from the sidebar** to see some examples
    of what Streamlit can do!
    ### Want to learn more?
    - Check out [streamlit.io](https://streamlit.io)
    - Jump into our [documentation](https://docs.streamlit.io)
    - Ask a question in our [community
        forums](https://discuss.streamlit.io)
    ### See more complex demos
    - Use a neural net to [analyze the Udacity Self-driving Car Image
        Dataset](https://github.com/streamlit/demo-self-driving)
    - Explore a [New York City rideshare dataset](https://github.com/streamlit/demo-uber-nyc-pickups)
"""
)
with st.form("my_form"):
   st.write("Inside the form")
   slider_val = st.slider("Form slider")
   checkbox_val = st.checkbox("Form checkbox")

   # Every form must have a submit button.
   submitted = st.form_submit_button("Submit")
   if submitted:
       st.write("slider", slider_val, "checkbox", checkbox_val)

st.write("Outside the form")

name = st.text_input('Name')
if not name:
  st.warning('Please input a name.')
  st.stop()
st.success('Thank you for inputting a name.')
add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone")
)
with st.sidebar:
    with st.echo():
        st.write("This code will be printed to the sidebar.")

    with st.spinner("Loading..."):

        st.success("Done!")



placeholder = st.empty()

# Replace the placeholder with some text:
placeholder.text("Hello")

# Replace the text with a chart:
placeholder.line_chart({"data": [1, 5, 2, 6]})

# Replace the chart with several elements:
with placeholder.container():
    st.write("This is one element")
    st.write("This is another")

# Clear all those elements:
placeholder.empty()
column1, column2 = st.columns([0.7,0.3])

# 在第一列中添加文本和图像
with column1:
    st.header('第一列')
    st.write('这是一些测试文本。')
    tab1, tab2, tab3 = st.tabs(["Cat 世界", "Dog 世界", "Owl 世界"])

    with tab1:
        st.header("A cat")
        st.image("https://static.streamlit.io/examples/cat.jpg", width=400)

    with tab2:
        st.header("A dog")
        st.image("https://static.streamlit.io/examples/dog.jpg", width=400)

    with tab3:
        st.header("An owl")
        st.image("https://static.streamlit.io/examples/owl.jpg", width=400)


# 在第二列中添加文本和图像
with column2:
    st.header('第二列')
    st.write('这是另一些测试文本。')
    tab1, tab2, tab3 = st.tabs(["Cat 世界", "Dog 世界", "Owl 世界"])

    with tab1:
        st.header("A cat")
        st.image("https://static.streamlit.io/examples/cat.jpg", width=200)

    with tab2:
        st.header("A dog")
        st.image("https://static.streamlit.io/examples/dog.jpg", width=200)

    with tab3:
        st.header("An owl")
        st.image("https://static.streamlit.io/examples/owl.jpg", width=200)

data_df = pd.DataFrame(
    {
        "sales": [
            [0, 4, 26, 80, 100, 40],
            [80, 20, 80, 35, 40, 100],
            [10, 20, 80, 80, 70, 0],
            [10, 100, 20, 100, 30, 100],
        ],
    }
)

st.data_editor(
    data_df,
    column_config={
        "sales": st.column_config.LineChartColumn(
            "Sales (last 6 months)",
            width="medium",
            help="The sales volume in the last 6 months",
            y_min=0,
            y_max=100,
         ),
    },
    hide_index=True,
)

col1, col2, col3 = st.columns(3)
col1.metric("Temperature", "70 °F", "1.2 °F")
col2.metric("CPI", "9 ", "-8%")
col3.metric("Humidity", "86%", "4%")
st.caption('This is a string that explains something above.')
st.caption('A caption with _italics_ :blue[colors] and emojis :sunglasses:')
st.title('This is a title')
st.divider()
st.header('This is a header')
st.subheader('This is a subheader')
import altair as alt
import numpy as np
df = pd.DataFrame(
    np.random.randn(200, 3),
    columns=['a', 'b', 'c'])
st.write(df)

c = alt.Chart(df).mark_circle().encode(
    x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])

st.write(c)
chart_data = pd.DataFrame(
   np.random.randn(1000, 2) / [50, 50] + [30.67, 104.06],
   columns=['lat', 'lon'])
chart_data['height'] = 1000
st.write(chart_data)
import pydeck as pdk
st.pydeck_chart(pdk.Deck(
    map_style=None,
    initial_view_state=pdk.ViewState(
        latitude=37.76,
        longitude=104.06,
        zoom=11,
        pitch=30,
    ),
    layers=[
        pdk.Layer(
           'HexagonLayer',
           data=chart_data,
           get_position='[lon, lat]',
           radius=200,
           elevation_scale=4,
           elevation_range=[0, 1000],
           elevation_attribute='height',
           pickable=True,
           extruded=True,
        ),
        # pdk.Layer(
        #     'ScatterplotLayer',
        #     data=chart_data,
        #     get_position='[lon, lat]',
        #     get_color='[200, 30, 0, 160]',
        #     get_radius=200,
        # ),
    ],
))
if "visibility" not in st.session_state:
    st.session_state.visibility = "visible"
    st.session_state.disabled = False

col1, col2 = st.columns(2)

with col1:
    st.checkbox("Disable text input widget", key="disabled")
    st.radio(
        "Set text input label visibility 👉",
        key="visibility",
        options=["visible", "hidden", "collapsed"],
    )
    st.text_input(
        "Placeholder for the other text input widget",
        "This is a placeholder",
        key="placeholder",
    )

with col2:
    text_input = st.text_input(
        "Enter some text 👇",
        label_visibility=st.session_state.visibility,
        disabled=st.session_state.disabled,
        placeholder=st.session_state.placeholder,
    )

    if text_input:
        st.write("You entered: ", text_input)
txt = st.text_area('Text to analyze', '''
    It was the best of times, it was the worst of times, it was
    the age of wisdom, it was the age of foolishness, it was
    the epoch of belief, it was the epoch of incredulity, it
    was the season of Light, it was the season of Darkness, it
    was the spring of hope, it was the winter of despair, (...)
    ''')
