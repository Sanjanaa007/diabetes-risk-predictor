<div align="center">

# 🩺 Diabetes Risk Predictor

### Machine Learning Web App for Early Diabetes Risk Screening

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-KNN-F7931E?style=flat-square&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![License](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)](LICENSE)

**[🚀 Live Demo](https://diabetes-risk-predictor-phe4zadr7iwznhuampnhjk.streamlit.app/)** &nbsp;•&nbsp; **[📊 Dataset](https://www.cdc.gov/brfss/)** &nbsp;•&nbsp; **[🐛 Report Issue](../../issues)**

</div>

---

## 📖 Overview

Diabetes affects over 400 million people worldwide, and early risk identification plays a critical role in preventive care. This project builds an end-to-end machine learning pipeline that predicts diabetes risk from **21 everyday health indicators** — no lab tests required — and ships it as an interactive web app.

Built on the **BRFSS 2015** dataset (CDC's Behavioral Risk Factor Surveillance System survey of 253,680 respondents), the model is trained, validated, and deployed with a strong focus on **avoiding data leakage**, a common pitfall when combining oversampling with cross-validation.

<div align="center">

*(add a screenshot or GIF of your app here — drag an image into the repo and reference it like below)*

`![App Screenshot](screenshot.png)`

</div>

---

## ✨ Highlights

| | |
|---|---|
| 🎯 **Model** | K-Nearest Neighbors, tuned via `GridSearchCV` |
| ⚖️ **Imbalance Handling** | SMOTE oversampling, applied leak-free inside CV folds |
| 🏆 **Best CV F1-macro** | `0.609` |
| ⚙️ **Best Parameters** | `metric=manhattan`, `n_neighbors=11`, `weights=uniform` |
| 🌐 **Deployment** | Live on Streamlit Community Cloud |

---

## 🧠 Methodology

```
Raw Data (253,680 rows, 21 features)
        │
        ▼
Duplicate Removal
        │
        ▼
Stratified Train/Test Split (80/20)
        │
        ▼
┌───────────────────────────────┐
│   Pipeline (per CV fold)      │
│   ─────────────────────       │
│   1. StandardScaler           │
│   2. SMOTE (train fold only)  │
│   3. KNN Classifier           │
└───────────────────────────────┘
        │
        ▼
GridSearchCV (3-fold, scoring = f1_macro)
        │
        ▼
Best Estimator → Evaluated on Held-out Test Set
        │
        ▼
Saved as model_best.pkl → Streamlit App
```

**Why this matters:** SMOTE and scaling are wrapped *inside* the pipeline and refit separately on every cross-validation fold, rather than applied once to the whole training set beforehand. This prevents synthetic samples from leaking information across folds — a subtle bug that inflates validation scores if done incorrectly.

---

## 🛠️ Tech Stack

<div align="center">

![Python](https://img.shields.io/badge/-Python-black?style=flat-square&logo=python)
![Pandas](https://img.shields.io/badge/-Pandas-black?style=flat-square&logo=pandas)
![NumPy](https://img.shields.io/badge/-NumPy-black?style=flat-square&logo=numpy)
![scikit-learn](https://img.shields.io/badge/-scikit--learn-black?style=flat-square&logo=scikitlearn)
![Streamlit](https://img.shields.io/badge/-Streamlit-black?style=flat-square&logo=streamlit)
![Matplotlib](https://img.shields.io/badge/-Matplotlib-black?style=flat-square)
![Seaborn](https://img.shields.io/badge/-Seaborn-black?style=flat-square)

</div>

## 📊 Features Used

<details>
<summary><b>Click to expand full feature list (21 indicators)</b></summary>

| Feature | Description |
|---|---|
| `HighBP` | High blood pressure |
| `HighChol` | High cholesterol |
| `CholCheck` | Cholesterol check within 5 years |
| `BMI` | Body Mass Index |
| `Smoker` | Smoked 100+ cigarettes in lifetime |
| `Stroke` | History of stroke |
| `HeartDiseaseorAttack` | Heart disease or heart attack history |
| `PhysActivity` | Physical activity in past 30 days |
| `Fruits` | Daily fruit consumption |
| `Veggies` | Daily vegetable consumption |
| `HvyAlcoholConsump` | Heavy alcohol consumption |
| `AnyHealthcare` | Has healthcare coverage |
| `NoDocbcCost` | Skipped doctor visit due to cost |
| `GenHlth` | Self-rated general health (1–5) |
| `MentHlth` | Poor mental health days (past 30) |
| `PhysHlth` | Poor physical health days (past 30) |
| `DiffWalk` | Difficulty walking / climbing stairs |
| `Sex` | Biological sex |
| `Age` | Age category (13 brackets) |
| `Education` | Education level |
| `Income` | Income bracket |

</details>

---

## 🚀 Getting Started

```bash
# Clone the repo
git clone https://github.com/Sanjanaa007/diabetes-risk-predictor.git
cd diabetes-risk-predictor

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

The app will open automatically at `http://localhost:8501`.

## 📁 Project Structure

```
diabetes-risk-predictor/
├── app.py                  # Streamlit web application
├── model_best.pkl          # Trained pipeline (Scaler + SMOTE + KNN)
├── requirements.txt        # Python dependencies
└── README.md
```

## 📈 Results Summary

| Metric | Value |
|---|---|
| Cross-Validation F1-macro | **0.609** |
| Optimal `n_neighbors` | 11 |
| Distance metric | Manhattan |
| Weighting | Uniform |

## 🔮 Roadmap

- [ ] Benchmark against Random Forest and XGBoost
- [ ] Add SHAP-based explainability to the app
- [ ] Extend to multiclass prediction (pre-diabetic vs. diabetic)
- [ ] Add unit tests for the preprocessing pipeline

---

## ⚠️ Disclaimer

This project is built for **educational and portfolio purposes**. It is not a certified medical diagnostic tool. Always consult a qualified healthcare professional for medical concerns.

<div align="center">

---

**Built by [Sanjana](https://github.com/Sanjanaa007)** &nbsp;|&nbsp; B.Tech AI & ML, Panimalar Engineering College

⭐ *If you found this project useful, consider giving it a star!*

</div>
