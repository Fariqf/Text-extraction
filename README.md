# Text Extraction App
This Streamlit application, named "Text-Extractor," allows you to upload an image and extract text from it using the EasyOCR library. The extracted text is displayed, providing a simple and efficient way to retrieve text information from images.

## Getting Started
### Prerequisites
Python 3.7 or later
Streamlit
easyocr
opencv-python
numpy
Pandas

## Installation
1. Clone this repository:
   git clone https://github.com/fariqf/Text-extraction.git
   cd Text-extraction

2. Install the required packages:
   pip install -r requirements.txt

3. Run the Streamlit app:
   streamlit run app2.py

## How to Use
1. Upload an image containing text using the file uploader.
2. The application will display the uploaded image.
3. The AI will process the image, and the extracted text will be displayed.
4. You can view and utilize the extracted text as needed.
   
## Components
### Text Extraction
The application uses the EasyOCR library, which supports multiple languages, to extract text from the uploaded image.

### Image Display
The uploaded image is displayed using the Streamlit st.image function.
