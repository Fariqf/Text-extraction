import pandas as pd
import easyocr as ocr
import cv2
import streamlit as st
import numpy as np
st.title("Text-Extractor")
from PIL import Image
image = st.file_uploader(label = "Upload your image here",type=['png','jpg','jpeg'])

@st.cache_data
def load_model(): 
    reader = ocr.Reader(['hi', 'en'], gpu=False) 
    return reader
reader = load_model() #load model

if image is not None:

    input_image = Image.open(image) #read image
    st.image(input_image) #display image

    with st.spinner("🤖 AI is at Work! "):
        

        result = reader.readtext(np.array(input_image))

        result_text = [] #empty list for results


        for text in result:
            result_text.append(text[1])

        st.write(result_text)
        st.success("Here you go!")
        st.balloons()
else:
    st.write("Upload an Image")
st.caption("Made with ❤️ by @fariq22")