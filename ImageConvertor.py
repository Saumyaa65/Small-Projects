import streamlit as st
from PIL import Image

st.subheader("Color to Grayscale Converter")

uploaded_image = st.file_uploader("Upload Image")

with st.expander("Start camera"):
    cam_inp=st.camera_input("camera")

if cam_inp:
    img=Image.open(cam_inp)
    gray_img=img.convert("L")
    st.image(gray_img)

if uploaded_image:
    img = Image.open(uploaded_image)
    gray_img = img.convert("L")
    st.image(gray_img)