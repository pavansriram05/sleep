import numpy as np
import streamlit as st
import pickle

import warnings
warnings.filterwarnings("ignore")


#loading the saved model

loaded_model = pickle.load(open('trained_adb_model2.sav','rb'))

def sleep_disorder_prediction(input_data):
    input_data_as_np_array = np.asarray(input_data)#converting the input data into array

    input_data_reshaped = input_data_as_np_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

#pred = loaded_model.predict(input_data_reshaped)
    pred = loaded_model.predict_proba(input_data_reshaped)
    risk = pred[:,1]
    risk_percent = round(risk[0]*100, 2)
    print(risk_percent)
    if (prediction[0] == 0):
        return 'the person is not at a risk of sleep disorder'
    else:
        return 'the person is at a risk of sleep disorder'
    
def percentage_of_risk(input_data):
    input_data_as_np_array = np.asarray(input_data)#converting the input data into array

    input_data_reshaped = input_data_as_np_array.reshape(1,-1)

    
#pred = loaded_model.predict(input_data_reshaped)
    pred = loaded_model.predict_proba(input_data_reshaped)
    risk = pred[:,1]
    risk_percent = round(risk[0]*100, 2)

    print(risk_percent)

    return str(risk_percent)

#USER INTERFACE

st.set_page_config(page_title="Sleep disorder",page_icon=':sparkles',layout='wide')# to set the title for the tab
st.title(':sleeping: Sleep Disorder Risk Prediction')
st.markdown('<style>div.block-container{padding-top:1rem;}<style>',unsafe_allow_html=True)

BMI=0

gender= st.selectbox("Gender",['Male','Female'])
Age= st.slider("Age",0,100,1)
occupation= st.selectbox("Occupation",['Other', 'Doctor', 'Teacher', 'Nurse', 'Engineer', 'Accountant','Lawyer', 'Salesperson'])
Sleep_duration = st.text_input("Sleep duration")
Quality_of_sleep= st.slider("quality of sleep",0.0,10.0,0.5)
physical_activity= st.text_input("Physical_activity")
stress_level= st.text_input("stree level")
bmi= st.selectbox("BMI category",['Over weight','Normal','obese'])
heart_rate= st.text_input("heart rate")
daily_steps= st.text_input("daily_steps")
bp_upper= st.text_input("bp_upper")
bp_lower= st.text_input("bp_lower")

#encoding the categorical inputs
if (gender=='Male'):
       Gender = 1
elif (gender=='Female'):
      Gender = 0
        
if (occupation=='Accountant'):
      Occupation = 0
elif (occupation=='Doctor'):
      Occupation = 1
elif (occupation=='Engineer'):
      Occupation = 2
elif (occupation=='Lawyer'):
      Occupation = 3
elif (occupation=='Nurse'):
      Occupation = 4
elif (occupation=='Other'):
      Occupation = 5
elif (occupation=='Salesperson'):
      Occupation = 6
elif (occupation=='Teacher'):
      Occupation = 7   
        
if (bmi=='Overweight'):
      BMI = 2
elif (bmi=='Normal'):
     BMI = 0
elif (bmi=='Obese'):
     BMI = 1

input_features=[ Gender,Age, Occupation, Sleep_duration, Quality_of_sleep,physical_activity, stress_level,BMI,heart_rate,daily_steps,bp_upper,bp_lower]

#prediction

diagnosis = " "
percent_of_risk = " "

if st.button('risk prediction'):
    diagnosis = sleep_disorder_prediction(input_features)

st.write(diagnosis)

if st.button('percentage of risk'):
    percent_of_risk = percentage_of_risk(input_features)

st.write(percent_of_risk)
