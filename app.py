from pycaret.classification import load_model, predict_model
import streamlit as st
import pandas as pd
import numpy as np


def predict_thyroid(model, data):
    
    predictions_data = predict_model(estimator = model, data = data)
    
    return predictions_data['Label'][0]
    
model = load_model('random_forest_model')


st.title('Thyroid Classifier Web App')
st.write('This is a web app to classify the patient wheather he/she having Thyroid or not based on\
         several features that you can see in the sidebar. Please adjust the\
         value of each feature. After that, click on the Predict button at the bottom to\
         see the prediction of the classifier.')

st.sidebar.subheader('Select the Correct Parameter')

TSH = st.sidebar.slider(label = 'TSH', min_value = 0.0,
                          max_value = 1000.0 ,
                          value = 10.0,
                          step = 0.1) 

T4U = st.sidebar.slider(label = 'T4U', min_value = 0.0,
                          max_value = 1000.0 ,
                          value = 10.0,
                          step = 0.1) 

T3 = st.sidebar.slider(label = 'T3', min_value = 0.0,
                          max_value = 100.0 ,
                          value = 10.0,
                          step = 0.1)

T4U = st.sidebar.slider(label = 'T4U', min_value = 0.0,
                          max_value = 100.0 ,
                          value = 1.0,
                          step = 0.1)
                          
FTI = st.sidebar.slider(label = 'FTI', min_value = 0.0,
                          max_value = 1000.0 ,
                          value = 10.0,
                          step = 0.1)                          


features = {'TSH':TSH,'T3':T3,'TT4': TT4, 'T4U': T4U,
            'FTI': FTI}
 

features_df  = pd.DataFrame([features])

st.table(features_df)  

if st.button('Predict'):
    
    prediction = predict_thyroid(model, features_df)
    
    st.write(' Based on feature values, patient is '+ str(prediction))
    
