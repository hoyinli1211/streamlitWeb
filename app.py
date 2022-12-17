import streamlit as st
from streamlit_option_menu import option_menu

with st.sidebar:
    selected = option_menu(None, ["Home", 'Upload', 'Tasks', 'Settings'], 
                           icons=['house', 'cloud-upload', 'list-task', 'gear'], 
                           menu_icon="cast", default_index=0, orientation='vertical')
    selected

if selected == 'Home':
    st.title('This is the home page')
elif selected == 'Upload':
    st.title('This is the upload page')
elif selected == 'Taks':
    st.title('Task1')
elif selected == 'Settings':
    st.title('Configuration')
else:
    pass
