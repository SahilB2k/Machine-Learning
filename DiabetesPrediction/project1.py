import numpy as np
import pickle


loaded_model=pickle.load(open('C:/Users/sahil jadhav/OneDrive/Desktop/Datasets/Trained_model.sav','rb')) 

input_Data=(1883350,9,103,78,25,304,29.58219193,1.282869847,43)
input_Data_as_numpy_array=np.asarray(input_Data)

input_data_reshaped=input_Data_as_numpy_array.reshape(1,-1)

prediction=loaded_model.predict(input_data_reshaped)
print(prediction)

if(prediction[0]==0):
  print('The person is not diabetic')
else:
  print('The person is diabetic')