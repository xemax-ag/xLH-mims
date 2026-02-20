import streamlit as st
from app_ui.toolbox.page_config import page_config

page_config(page_title='xLH-mims')

#######################################################################################################################

with st.sidebar:
    st.link_button(label='Dokumentation', url=f'/static/docs', use_container_width=True)
    st.link_button(label='API Dokumentation', url=f'/docs', use_container_width=True)

#######################################################################################################################

