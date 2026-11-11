import streamlit as st
import numpy as np
import pandas as pd
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier


st.write("""
         
         # Iris Flower Prediction App
         
         This app predicts Iris flower type based on user's input feature data
         
         """)

st.sidebar.header('User Input Parameters')

def user_input_features():
    sepal_length = st.sidebar.slider('Sepal length',4.3,7.9,5.4)
    sepal_width = st.sidebar.slider('Sepal width',2.0,4.4,3.4)
    petal_length = st.sidebar.slider('Petal length',1.0,6.9,1.3)
    petal_width = st.sidebar.slider('Petal width',0.1,2.5,0.2)
    data ={
        'Sepal length': sepal_length,
        'Sepal width': sepal_width,
        'Petal length': petal_length,
        'Petal width': petal_width
    }
    features= pd.DataFrame(data,index=[0])
    return features

df = user_input_features()

st.subheader('User Input Parameters')
st.write(df)

iris = datasets.load_iris()
X = iris.data
Y = iris.target

clf = RandomForestClassifier()
clf.fit(X,Y)

prediction = clf.predict(df)
predict_proba = clf.predict_proba(df)

st.subheader('Class labels and their corresponding index number')
st.write(iris.target_names)


st.subheader('Prediction')
st.write(iris.target_names[prediction])

st.subheader('Prediction Probability')
st.write(predict_proba)



         
         
