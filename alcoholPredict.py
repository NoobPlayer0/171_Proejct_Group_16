import streamlit as st
import pickle
import numpy as np

# load the modle we save
def load_model():
    with open('saved_steps.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

data = load_model()

rf = data["model"]

sex = data["sex"]
age = data["age"]
famsize = data["famsize"]
Medu = data["Medu"]
Fedu = data["Fedu"]
Mjob = data["Mjob"]
Fjob = data["Fjob"]
studytime = data["studytime"]
famrel = data["famrel"]
freetime = data["freetime"]
goout = data["goout"]
health = data["health"]
absences = data["absences"]
grade = data["Grade"]

# this is a function that display the web app
def show_predict_page():
    st.title("Alcohol Consumption Prediction")

    st.write("""### We need some information to predict the alcohol consumption level""")

    gender = (0, 1,)
    familysize = (0,1,)
    medu = (0,1,2,3,4,)
    fedu = (0,1,2,3,4,)
    mjob = (0,1,2,3,4)
    fjob = (0,1,2,3,4)
    studyt = (0,1,2,3)
    ag = (0,1,2,3,4,5,6,7)

    gen = st.selectbox("Sex", gender)
    fams = st.selectbox("Familiy Size", familysize)
    edu1 = st.selectbox("Mother Education Level", medu)
    edu2 = st.selectbox("Father Education Level", fedu)
    job1 = st.selectbox("Mother's Job", mjob)
    job2 = st.selectbox("Father's Job", fjob)
    stu = st.selectbox("Weekly Study Time", studyt)
    ages = st.selectbox("Age", ag)
    # ages = st.slider("Age", 0, 7, 1)

    famrela = st.slider("Quality of family relationships (from 1 - very bad to 5 - excellent)", 1,5,1)
    freet = st.slider("Free time after school (from 1 - very low to 5 - very high)", 1,5,1)
    hangout = st.slider("Going out with friends (from 1 - very low to 5 - very high)", 1,5,1)
    healthy = st.slider("Current health status (from 1 - very bad to 5 - very good)", 1,5,1)
    abs = st.slider("Number of school absences (from 0 to 93)", 0,93,1)
    grades = st.slider("Final Grades", 0,20,1)

    # create a button so that user can cinfirm their input data
    okButton = st.button("Predict Alcohol Consumption")
    if okButton:
        X = np.array([[gen, fams, edu1, edu2, job1, job2, stu, ages, famrela, freet, hangout, healthy, abs, grades]])

        X[:, 0] = sex.transform(X[:,0])
        X[:, 1] = famsize.transform(X[:,1])
        X[:, 2] = Medu.transform(X[:,2])
        X[:, 3] = Fedu.transform(X[:,3])
        X[:, 4] = Mjob.transform(X[:,4])
        X[:, 5] = Fjob.transform(X[:,5])
        X[:, 6] = studytime.transform(X[:,6])
        X[:, 7] = age.transform(X[:,7])
        X = X.astype(float)

        alc = rf.predict(X)
        st.subheader(f"The predicted alcohol consumption level is {alc[0]}")
        st.text('The result with a higher number indicates a higher alcohol consumption')
