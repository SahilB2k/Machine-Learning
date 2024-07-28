import numpy as np

import pickle

loaded_model=pickle.load(open('C:/Users/sahil jadhav/OneDrive/Desktop/Deployed ML projects/MultiDieseasePrediction/HeartDisease_model.sav','rb'))

input_data=(63,1,3,145,233,1,0,150,0,2.3,0,0,1
)

input_data_as_numpy_array=np.asarray(input_data)
input_data_reshaped=input_data_as_numpy_array.reshape(1,-1)
prediction=loaded_model.predict(input_data_reshaped)
print(prediction)

if(prediction==1):
  print('The person has Heart Disease')
else:
  print('The person is Normal')