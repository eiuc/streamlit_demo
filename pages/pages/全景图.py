import streamlit as st
tab1, tab2 = st.tabs(["行业", "概念"])
with tab1:
    st.header("A cat")
    st.image("https://static.streamlit.io/examples/cat.jpg", width=400)
with tab2:
    st.header("A dog")
    st.image("https://static.streamlit.io/examples/dog.jpg", width=200)

st.markdown(
    """

    **👈wait to realize**  

    ### gaph pattern

    ### mutual authentication

"""
)