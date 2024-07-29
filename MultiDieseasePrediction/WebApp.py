import pickle
import streamlit as st
from streamlit_option_menu import option_menu

diabetes_model = pickle.load(open('C:/Users/sahil jadhav/OneDrive/Desktop/Deployed ML projects/MultiDieseasePrediction/Diabetes_model.sav','rb'))

heart_disease_model = pickle.load(open('C:/Users/sahil jadhav/OneDrive/Desktop/Deployed ML projects/MultiDieseasePrediction/heartDisease_model.sav','rb'))

Parkinson_model = pickle.load(open('C:/Users/sahil jadhav/OneDrive/Desktop/Deployed ML projects/MultiDieseasePrediction/Parkinson_model.sav','rb'))

with st.sidebar:

    selected = option_menu('Multiple Disease Prediction System',
                           
                           ['Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Parkinsons Prediction'],
                            icons=['activity','heart','person'],
                            default_index=0)

# Diabates Prediction Page /
if (selected == 'Diabetes Prediction'):

    #page Title
    st.title('Diabetes Prediction using ML')

    col1,col2,col3 = st.columns(3)

    with col1:
        Pregnancies = st.text_input('Number of Pregancies')

    with col2:
        Glucose=st.text_input('Blood Glucose Level')

    with col3:
        BloodPressure=st.text_input('Blood Pressure Level')

    with col1:
        SkinThickness=st.text_input('Skin Thickness Value')

    with col2:
        Insulin=st.text_input('Insulin Level')

    with col3:
        Bmi=st.text_input('BMI value')

    with col1:
        DiabetesPedigreeFunction=st.text_input('Diabetes Pedigree Function Value')

    with col2:
        Age=st.text_input('Age')

    diab_diagnosis=''

    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,Bmi,DiabetesPedigreeFunction,Age]])

        if (diab_prediction==1):
            diab_diagnosis= 'The  Person is Diabetic'
        else:
            diab_diagnosis = 'The Person is Not Diabetic'        
    st.success(diab_diagnosis)
        
if (selected ==' heart Disease Prediction'):

    # page title 
    st.title('Heart Disease Prediction')

    col1,col2,col3=st.columns(3)

    with col1:
        age=st.text_input('Age')

    with col2:
        sex = st.text_input('Sex')

    with col3:
        cp=st.text_input('Chest Pain')

    with col1:
        trestbps=st.text_input('Testing Blood Pressure')

    with col2:
        chol=st.text_input('Cholestrol')

    




  
