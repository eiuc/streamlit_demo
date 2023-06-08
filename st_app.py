import streamlit as st
from langchain.llms import OpenAI
import os
import openai
st.title('🦜🔗 Quickstart App')
openai.proxy = {'http':'127.0.0.1:7890', 'https': '127.0.0.1:7890'}
# openai_api_key = st.sidebar.text_input('OpenAI API Key')
openai_api_key = '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'
from streamlit_elements import elements, mui, html
def generate_response(input_text):
  llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
  st.info(llm(input_text))

with st.form('my_form'):
  text = st.text_area('Enter text:', 'What are the three key pieces of advice for learning how to code?')
  submitted = st.form_submit_button('Submit')
  if not openai_api_key.startswith('sk-'):
    st.warning('Please enter your OpenAI API key!', icon='⚠')
  if submitted and openai_api_key.startswith('sk-'):
    generate_response(text)

with elements("dashboard"): #可拖动的streamlit

  # You can create a draggable and resizable dashboard using
  # any element available in Streamlit Elements.

  from streamlit_elements import dashboard

  # First, build a default layout for every element you want to include in your dashboard

  layout = [
    # Parameters: element_identifier, x_pos, y_pos, width, height, [item properties...]
    dashboard.Item("first_item", 0, 0, 2, 2),
    dashboard.Item("second_item", 2, 0, 2, 2, isDraggable=False, moved=False),
    dashboard.Item("third_item", 0, 2, 1, 1, isResizable=False),
  ]

  # Next, create a dashboard layout using the 'with' syntax. It takes the layout
  # as first parameter, plus additional properties you can find in the GitHub links below.

  with dashboard.Grid(layout):
    mui.Paper("First item", key="first_item")
    mui.Paper("Second item (cannot drag)", key="second_item")
    mui.Paper("Third item (cannot resize)", key="third_item")


  # If you want to retrieve updated layout values as the user move or resize dashboard items,
  # you can pass a callback to the onLayoutChange event parameter.

  def handle_layout_change(updated_layout):
    # You can save the layout in a file, or do anything you want with it.
    # You can pass it back to dashboard.Grid() if you want to restore a saved layout.
    print(updated_layout)


  with dashboard.Grid(layout, onLayoutChange=handle_layout_change):
    mui.Paper("First item", key="first_item")
    mui.Paper("Second item (cannot drag)", key="second_item")
    mui.Paper("Third item (cannot resize)", key="third_item")