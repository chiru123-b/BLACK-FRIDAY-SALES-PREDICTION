# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 10:00:24 2022

@author: chiranjeevi
"""

import numpy as np
import pickle
import pandas as pd
#from flasgger import Swagger
import streamlit as st 

from PIL import Image

#app=Flask(__name__)
#Swagger(app)

pickle_in = open("lm.pkl","rb")
lm=pickle.load(pickle_in)



def welcome():
    return "Welcome All"

#@app.route('/predict',methods=["Get"])
def predict(Gender, Age, Occupation, City_Category,
       Stay_In_Current_City_Years, Marital_Status, Product_Category_1,
       Product_Category_2):
    
    
   prediction=classifier.predict([[Gender, Age, Occupation, City_Category,
       Stay_In_Current_City_Years, Marital_Status, Product_Category_1,
       Product_Category_2]])
   print(prediction)
   
   
       
def main():
    st.title('Black friday sales prediction')
    Gender=st.text_input('Gender')
    Occupation=st.text_input('Age')
    Occupation=st.text_input('Occupation')
    Stay_In_Current_City_Years=st.text_input(' City_Category')
    BodyTemp=st.text_input('Stay_In_Current_City_Years')
    Marital_Status=st.text_input('Marital_Status')
    Product_Category_1=st.text_input('Product_Category_1')
    Product_Category_2=st.text_input('Product_Category_2')
    
    
    Purchase= ''
    if  st.button('maternal  health risk'):
        Purchase=predict([Gender, Age, Occupation, City_Category,
       Stay_In_Current_City_Years, Marital_Status, Product_Category_1,
       Product_Category_2])
        
        
    st.success(Purchase)
        
if __name__=='__main__':
    main()
    