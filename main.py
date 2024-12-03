import cv2
import numpy as np
import streamlit as st
import tensorflow as tf
from tensorflow.keras.preprocessing import image
from keras.models import model_from_json
json_file = open('model.json', 'r')
model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(model_json)
loaded_model.load_weights("model.weights.h5")
st.header("Test Your Vision")
col1, col2, col3 = st.columns(3)
with col2:
    image_path = 'Eyeimage.png' 
    st.image(image_path)
uploaded_file = st.file_uploader("Choose a image file", type="jpg")
classes_dict ={0:'Cataract', 1:'Diabetic Retinopathy', 2:'Glaucoma', 3:'Normal'}
if uploaded_file is not None:
    file_bytes=np.asarray(bytearray(uploaded_file.read()),dtype=np.uint8)
    opencv_img=cv2.imdecode(file_bytes,1)
    opencv_img=cv2.cvtColor(opencv_img,cv2.COLOR_BGR2RGB)
    resized=cv2.resize(opencv_img,(224,224))
    st.image(resized,channels="RGB")
    #preprocessing of the image
    img_array = image.img_to_array(resized)
    img_array = np.expand_dims(img_array, axis=0)
    Generate_pred=st.button("Generate Prediction")
    if Generate_pred:
        prediction=loaded_model.predict(img_array).argmax()
        st.subheader("Prediction for the image is {}".format(classes_dict[prediction]))