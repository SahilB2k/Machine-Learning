import numpy as np
import pickle
import streamlit as st
import xgboost

loaded_model=pickle.load(open(r'C:\Users\sahil jadhav\OneDrive\Desktop\ML\Deployment\Trained_model.sav','rb')) 


def diabetes_pred(input_data):
    # Convert input_data to numpy array and ensure it has the correct datatype
    input_data = np.array(input_data, dtype=float).reshape(1, -1)
    prediction = loaded_model.predict(input_data)
    return prediction[0]
# creating a func for prediction


    
def main():

    # giving a title 
    st.title('Diabetes Prediction Web App')

    # geting the input data from user
    Pregnancies=st.text_input('Number of Pregnancies')
    Glucose=st.text_input('Blood Glucose Level')
    BloodPressure=st.text_input('Blood Pressure Level')
    SkinThickness=st.text_input('Skin Thickness Value')
    Insulin=st.text_input('Insulin Level')
    Bmi=st.text_input('BMI value')
    DiabetesPedigreeFunction=st.text_input('Diabetes Pedigree Function Value')
    Age=st.text_input('Age')

    # code for prediction 

    diagnosis = '' 

    # creating a button for prediction 
    if st.button("Diabetes Test Result"):
        diagnosis = diabetes_pred([Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,Bmi,DiabetesPedigreeFunction,Age])

        if diagnosis == 1:
            diagnosis = 'Diabetic'
        else:
            diagnosis = 'Non-Diabetic'

        

        
    st.success(diagnosis)
    

if __name__ == '__main__':
    main()
    

