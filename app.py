import streamlit as st
from streamlit_option_menu import option_menu

with st.sidebar:
    selected = option_menu(None, ["Home", 'Upload', 'Tasks', 'Settings'], 
                           icons=['house', 'cloud-upload', 'list-task', 'gear'], 
                           menu_icon="cast", default_index=0, orientation='vertical')
    selected
