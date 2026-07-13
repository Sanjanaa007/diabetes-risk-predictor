import streamlit as st
import joblib
import pandas as pd

st.set_page_config(page_title="Diabetes Risk Predictor", page_icon="🩺", layout="centered")

# ----------------------------
# Load model (cached so it's not reloaded on every interaction)
# ----------------------------
@st.cache_resource
def load_model():
    return joblib.load("model_best.pkl")

model = load_model()

st.title("🩺 Diabetes Risk Predictor")
st.write("Fill in the health indicators below. This uses a KNN model trained on the BRFSS 2015 dataset.")

# ----------------------------
# Input widgets — must match the exact column order used in training
# (df.drop("Diabetes_binary", axis=1) columns, in order)
# ----------------------------
col1, col2 = st.columns(2)

with col1:
    HighBP = st.selectbox("High Blood Pressure", [0, 1], format_func=lambda x: "Yes" if x else "No")
    HighChol = st.selectbox("High Cholesterol", [0, 1], format_func=lambda x: "Yes" if x else "No")
    CholCheck = st.selectbox("Cholesterol Check in 5 yrs", [0, 1], format_func=lambda x: "Yes" if x else "No")
    BMI = st.number_input("BMI", min_value=10.0, max_value=100.0, value=25.0, step=0.1)
    Smoker = st.selectbox("Smoked 100+ cigarettes in life", [0, 1], format_func=lambda x: "Yes" if x else "No")
    Stroke = st.selectbox("Ever had a stroke", [0, 1], format_func=lambda x: "Yes" if x else "No")
    HeartDiseaseorAttack = st.selectbox("Heart Disease / Attack history", [0, 1], format_func=lambda x: "Yes" if x else "No")
    PhysActivity = st.selectbox("Physical Activity (past 30 days)", [0, 1], format_func=lambda x: "Yes" if x else "No")
    Fruits = st.selectbox("Eats fruit daily", [0, 1], format_func=lambda x: "Yes" if x else "No")
    Veggies = st.selectbox("Eats vegetables daily", [0, 1], format_func=lambda x: "Yes" if x else "No")
    HvyAlcoholConsump = st.selectbox("Heavy Alcohol Consumption", [0, 1], format_func=lambda x: "Yes" if x else "No")

with col2:
    AnyHealthcare = st.selectbox("Has any healthcare coverage", [0, 1], format_func=lambda x: "Yes" if x else "No")
    NoDocbcCost = st.selectbox("Skipped doctor due to cost", [0, 1], format_func=lambda x: "Yes" if x else "No")
    GenHlth = st.slider("General Health (1=Excellent, 5=Poor)", 1, 5, 3)
    MentHlth = st.slider("Poor mental health days (past 30)", 0, 30, 0)
    PhysHlth = st.slider("Poor physical health days (past 30)", 0, 30, 0)
    DiffWalk = st.selectbox("Difficulty walking/climbing stairs", [0, 1], format_func=lambda x: "Yes" if x else "No")
    Sex = st.selectbox("Sex", [0, 1], format_func=lambda x: "Female" if x == 0 else "Male")
    Age = st.slider("Age category (1=18-24 ... 13=80+)", 1, 13, 5)
    Education = st.slider("Education level (1=none, 6=college grad)", 1, 6, 4)
    Income = st.slider("Income level (1=lowest, 8=highest)", 1, 8, 5)

# ----------------------------
# Predict
# ----------------------------
if st.button("Predict Diabetes Risk", type="primary"):
    input_data = pd.DataFrame([{
        "HighBP": HighBP,
        "HighChol": HighChol,
        "CholCheck": CholCheck,
        "BMI": BMI,
        "Smoker": Smoker,
        "Stroke": Stroke,
        "HeartDiseaseorAttack": HeartDiseaseorAttack,
        "PhysActivity": PhysActivity,
        "Fruits": Fruits,
        "Veggies": Veggies,
        "HvyAlcoholConsump": HvyAlcoholConsump,
        "AnyHealthcare": AnyHealthcare,
        "NoDocbcCost": NoDocbcCost,
        "GenHlth": GenHlth,
        "MentHlth": MentHlth,
        "PhysHlth": PhysHlth,
        "DiffWalk": DiffWalk,
        "Sex": Sex,
        "Age": Age,
        "Education": Education,
        "Income": Income,
    }])

    prediction = model.predict(input_data)[0]
    proba = model.predict_proba(input_data)[0]

    if prediction == 1:
        st.error(f"⚠️ Higher risk of diabetes predicted (confidence: {proba[1]*100:.1f}%)")
    else:
        st.success(f"✅ Lower risk of diabetes predicted (confidence: {proba[0]*100:.1f}%)")

    st.caption("This is a machine learning estimate for educational purposes only, not a medical diagnosis.")
