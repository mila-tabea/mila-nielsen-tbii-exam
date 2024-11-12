import numpy as np
import streamlit as st
import cv2

def decode_qrcode_page():
    #create header for the page
    st.header("Decode QR code")

    # add a file uploader widget
    qrcode = st.file_uploader("Upload your QR Code",
                     type=['jpg', 'png', 'jpeg', 'GIF'])

    if qrcode:
        file_bytes = np.asarray(bytearray(qrcode.read()), dtype=np.uint8)
        opencv_image = cv2.imdecode(file_bytes, 1)

        st.image(opencv_image)

        #decode the qr code
        detector = cv2.QRCodeDetector()
        decoded_info, point, straight_qr = detector.detectAndDecode(opencv_image)
        st.write(f"Your QR Code contained {decoded_info}")
        #st.write(point)
        #st.write(straight_qr)