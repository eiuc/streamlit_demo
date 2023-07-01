import streamlit as st
st.write('这是AI工具')
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