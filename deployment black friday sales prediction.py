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