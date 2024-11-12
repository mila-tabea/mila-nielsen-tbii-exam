import streamlit as st
from decode_qrcode_page import decode_qrcode_page

st.set_page_config(
    page_title="Qr Code Generator v2")

options=['Generate QR Code', 'Decode QR Code','About me']
page_selection= st.sidebar.selectbox("Menu", options)

if page_selection == "Generate QR Code":
    st.title("Generate QR Code")
elif page_selection == "Decode QR Code":
    decode_qrcode_page()
elif page_selection == "About me":
    st.write("Hi, my name is Mila ")