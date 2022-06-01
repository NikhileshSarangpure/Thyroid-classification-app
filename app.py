from pycaret.classification import load_model, predict_model
import streamlit as st
import pandas as pd
import numpy as np


def predict_thyroid(model, df):
    
    predictions_data = predict_model(estimator = model, data = df)
    
    return predictions_data['Label'][0]
    
model = load_model('random-forest_model')


st.title('Thyroid Classifier Web App')
st.write('This is a web app to classify the patient wheather he/she having Thyroid or not based on\
         several features that you can see in the sidebar. Please adjust the\
         value of each feature. After that, click on the Predict button at the bottom to\
         see the prediction of the classifier.')


TT4 = st.sidebar.slider(label = 'TT4', min_value = 60.0,
                          max_value = 150.0 ,
                          value = 10.0,
                          step = 0.1)

T4U = st.sidebar.slider(label = 'T4U', min_value = 0.00,
                          max_value = 2.00 ,
                          value = 1.00,
                          step = 0.01)
                          
FTI = st.sidebar.slider(label = 'FTI', min_value = 60.0,
                          max_value = 150.0 ,
                          value = 10.0,
                          step = 0.1)                          


features = {'TT4': TT4, 'T4U': T4U,
            'FTI': FTI}
 

features_df  = pd.DataFrame([features])

st.table(features_df)  

if st.button('Predict'):
    
    prediction = predict_thyroid(model, features_df)
    
    st.write(' Based on feature values, patient is '+ str(prediction))
    
