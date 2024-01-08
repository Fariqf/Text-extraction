import cv2
import glob
import pandas as pd
import easyocr
import cv2
import streamlit as st

#select the path
path = "images/*.*"
img_number = 1 
reader = easyocr.Reader(['en'])  #English

df=pd.DataFrame()
for file in glob.glob(path):
    print(file)     #just stop here to see all file names printed
    img= cv2.imread(file, 0)  #now, we can read each file since we have the full path
    results = reader.readtext(img, detail=0, paragraph=True) #Set detail to 0 for simple text output
    df = df._append(pd.DataFrame({'image': file, 'detected_text': results[0]}, index=[0]), ignore_index=True)
    img_number +=1  

print(df)