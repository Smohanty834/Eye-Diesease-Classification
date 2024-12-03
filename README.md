# Eye-Diesease-Classification <br/>
Diabetes is a condition that carries an increased risk of developing eye complications. Diabetic eye disease includes complications such as diabetic retinopathy, cataracts and glaucoma.

Diabetes is the leading cause of blindness in working-age adults. People with type 1 and type 2 diabetes are at risk. It’s possible to be unaware that you have severe diabetic eye disease and suddenly go blind. Fortunately, most cases of blindness can be prevented with regular eye examinations and proper care.

## Eye Diseases
Glaucoma: Group of eye diseases that can damage the optic nerve. The optic nerve is responsible for transmitting visual information from the eye to the brain. Glaucoma can lead to permanent vision loss and, in some cases, blindness.

Diabetic retinopathy: It's an eye condition that affects people with diabetes. High blood sugar leaves damaged vessels in the retina. The retina is that part of your eyes that can detect light and send signals to the brain. Damage to these blood vessels can lead to vision loss and blindness in some cases.

Cataracts: Cataracts cloud the natural eye lens, leading to blurry vision and difficulty seeing clearly. Aging is one of the main reasons for this disease, but it can also be caused by factors such as injury, genetics, or medication effects. Cataracts can make natural vision blurry, cloudy, and even double it.

## About
The Project involves the classification of eye dieseases such as Glaucoma, Diabetic Retinopathy and Cataract. the model is prepared using CNN based `Resnet-50` pretrained model for better accuracy. The model is trained on datasets of retinal images, with an accuracy of 96% and is aviled using `Streamlit`.<br/>

The Datasets used are: https://www.kaggle.com/datasets/gunavenkatdoddi/eye-diseases-classification .<br/>
The dataset consists of Normal, Diabetic Retinopathy, Cataract and Glaucoma retinal images where each class have approximately 1000 images. These images are collected from various sorces like IDRiD, Oculur recognition, HRF etc.<br/>

Download The model Weights from here : https://drive.google.com/file/d/13tkFeLqYWk-OrFyq2egwgXbqTtIZNITr/view?usp=sharing

The Process includes Loading the base model, Data Preprocessing, Training, Validation and model access.<br/>

Clone the repository:
   ```bash
   git clone https://github.com/Smohanty834/Eye-Disease-Prediction.git
```
## Features
- Trainable deep learning model using TensorFlow/Keras.
- Pre-trained CNN for image classification.
- Web application for user interaction.

## Requirements
- Python 3.8+
- TensorFlow/Keras
- Streamlit
- OpenCV
- NumPy
- Matplotlib
- Pandas

## Demo
<img src="https://github.com/user-attachments/assets/8a6e8c90-40e1-4810-b0d8-42773e38c8a5" width=500 height=400>
