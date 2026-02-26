import streamlit as st
from app_ui.toolbox.page_config import page_config

page_config(page_title='xLH-mims')

#######################################################################################################################

with st.sidebar:
    st.link_button(label='Dokumentation', url=f'/static/docs', use_container_width=True)
    st.link_button(label='API Dokumentation', url=f'/docs', use_container_width=True)

#######################################################################################################################

st.markdown('### Startseite')
st.link_button(label='Marimo Notebook', url=f'http://localhost:2718/', use_container_width=False)
st.link_button(label='Jupyter Notebook', url=f'http://localhost:8888/lab', use_container_width=False)
st.link_button(label='Open WebUI', url=f'http://localhost:8080/', use_container_width=False)
st.link_button(label='n8n', url=f'http://localhost:5678/', use_container_width=False)
st.link_button(label='Node-RED', url=f'http://localhost:1880/', use_container_width=False)
