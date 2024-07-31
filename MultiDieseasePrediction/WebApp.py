import pickle
import streamlit as st
from streamlit_option_menu import option_menu

diabetes_model = pickle.load(open(r'C:\Users\sahil jadhav\OneDrive\Desktop\Deployed ML projects\MultiDieseasePrediction\Diabetes_model.sav','rb'))

heart_disease_model = pickle.load(open(r'C:\Users\sahil jadhav\OneDrive\Desktop\Deployed ML projects\MultiDieseasePrediction\heartDisease_model.sav','rb'))

Parkinson_model = pickle.load(open(r'C:\Users\sahil jadhav\OneDrive\Desktop\Deployed ML projects\MultiDieseasePrediction\Parkinson_model.sav','rb'))

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
        
if(selected =='Heart Disease Prediction'):

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

    with col3:
        fbs=st.text_input('Flasting Blood Sugar')

    with col1:
        restecg=st.text_input('Resting ElectroCardioGraphic Result')

    with col2:
        thalach=st.text_input('Maximum Heart Rate Achived')

    with col3:
        exang=st.text_input('Exercised Induced Angina')
    
    with col1:
        oldpeak=st.text_input('ST depression INduced by Exercise')

    with col2:
        slope=st.text_input('Slope of the Peak Exercise')

    with col3:
        ca=st.text_input('Major Vessels coloured by Flouroscopy')

    with col1:
        thal=st.text_input('thal:0=normal; 1=fixed; 2=reversable defect')

    heart_diagnosis=''

    if st.button('Heart Disease Test Result'):
        heart_prediction=heart_disease_model.predict([[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]]) 

        if (heart_prediction==1):
            heart_diagnosis= 'The  Person is having Heart Disease'
        else:
            heart_diagnosis = 'The Person is Normal'        
    st.success(heart_diagnosis)

# Parkinson Prediction
if(selected =='Parkinson Prediction'):

    # page title 
    st.title('Parkinson Prediction')

    col1,col2,col3,col4,col5=st.columns(5)

    with col1:
        fo=st.text_input('MDVP:Fo(Hz)')

    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')

    with col3:
        flo=st.text_input('MDVP:Flo(Hz)')

    with col4:
        jitter_percent=st.text_input('MDVP:Jitter(%)')

    with col5:
        jitter_abs=st.text_input('MDVP:Jitter(Abs)')

    with col1:
        Rap=st.text_input('MDVP:RAP')

    with col2:
        Ppq=st.text_input('MDVP:PPQ')

    with col3:
        ddp=st.text_input('Jitter:DDP')

    with col4:
        shimmer=st.text_input(' MDVP:Shimmer ')
    
    with col5:
        apq3=st.text_input('Shimmer:APQ3 ')

    with col1:
        apq5=st.text_input(' Shimmer:APQ5  ')

    with col2:
        apq=st.text_input(' MDVP:APQ ')

    with col3:
        dda=st.text_input('Shimmer:DDA')

    with col4:
        nhr=st.text_input('NHR')
    
    with col5:
        hnr=st.text_input('HNR')
    
    with col1:
        rpde=st.text_input('RPDE')

    with col2:
        dfa=st.text_input('DFA')

    with col3:
        spread1=st.text_input('Spread1')
    
    with col4:
        spread2=st.text_input('Spread2')

    with col5:
        d2=st.text_input('D2')
        
    with col1:
        ppe=st.text_input('PPE')

    parkinson_diagnosis=''

    if st.button('Heart Disease Test Result'):
        parkinson_prediction=Parkinson_model.predict([[fo,fhi,flo,jitter_percent,jitter_abs,Rap,Ppq,ddp,shimmer,apq3,apq5,apq,dda,nhr,hnr,rpde,dfa,spread1,spread2,d2,ppe]]) 

        if (parkinson_prediction==1):
            parkinson_diagnosis_diagnosis= 'The  Person is having Heart Disease'
        else:
            parkinson_diagnosis = 'The Person is Normal'        
    st.success(parkinson_diagnosis)



    


    




  
