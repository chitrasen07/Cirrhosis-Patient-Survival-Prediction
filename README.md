# 🩺 Cirrhosis Patient Survival Prediction

A comprehensive machine learning project for predicting the survival status of patients with liver cirrhosis using clinical features from the Mayo Clinic study (1974–1984).

## 📊 Project Overview

This project implements an end-to-end machine learning pipeline to predict patient outcomes based on 17 clinical features. The model classifies patients into three categories:
- **D (Death)** - Patient deceased
- **C (Censored)** - Patient still alive at end of study
- **CL (Censored due to liver transplantation)** - Patient received liver transplant

## 🗂️ Dataset Information

- **Source:** Mayo Clinic study (1974–1984)
- **Instances:** 418 patients
- **Features:** 17 clinical features including:
  - Demographics: Age, Sex
  - Treatment: Drug (D-penicillamine vs Placebo)
  - Clinical signs: Ascites, Hepatomegaly, Spiders, Edema
  - Lab values: Bilirubin, Cholesterol, Albumin, Copper, Alkaline Phosphatase, SGOT, Triglycerides, Platelets, Prothrombin
  - Disease stage: Stage (1-4)

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- Jupyter Notebook

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/Cirrhosis-Patient-Survival-Prediction.git
cd Cirrhosis-Patient-Survival-Prediction
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

3. Place your `cirrhosis.csv` dataset in the project root directory.

### Running the Project

1. Open the Jupyter notebook:
```bash
jupyter notebook cirrhosis_survival_prediction.ipynb
```

2. Run all cells sequentially to:
   - Load and preprocess the data
   - Perform exploratory data analysis
   - Train multiple ML models
   - Evaluate and compare model performance
   - Save the best model

## 📈 Project Structure

```
Cirrhosis-Patient-Survival-Prediction/
├── cirrhosis_survival_prediction.ipynb  # Main Jupyter notebook
├── cirrhosis.csv                         # Dataset (not included)
├── cirrhosis_model.pkl                   # Trained model (generated)
├── cirrhosis_scaler.pkl                  # Feature scaler (generated)
├── feature_names.pkl                     # Feature names (generated)
├── requirements.txt                      # Python dependencies
└── README.md                            # Project documentation
```

## 🔬 Methodology

### 1. Data Preprocessing
- Handle missing values (drop rows with missing Drug values, impute numeric means)
- One-hot encode categorical variables
- Convert target variable to numeric (D→0, C→1, CL→2)
- Scale features using StandardScaler

### 2. Exploratory Data Analysis
- Correlation heatmap
- Target variable distribution analysis
- Feature distribution plots
- Boxplots comparing features across different status groups

### 3. Model Building
Five different classifiers are trained and evaluated:
- Logistic Regression
- Random Forest
- XGBoost
- Support Vector Machine
- K-Nearest Neighbors

### 4. Model Evaluation
- Accuracy, Precision, Recall, F1-Score
- Confusion Matrix
- Classification Report
- Feature Importance Analysis

### 5. Hyperparameter Tuning
- RandomizedSearchCV for the best performing model
- Cross-validation with 5 folds

## 📊 Results

The notebook provides:
- Detailed comparison of all models
- Confusion matrix heatmap
- Feature importance visualization
- Model performance metrics

## 🔮 Making Predictions

Use the `predict_status()` function to make predictions on new patient data:

```python
import pandas as pd
import joblib

# Load the saved artifacts
model = joblib.load('cirrhosis_model.pkl')
scaler = joblib.load('cirrhosis_scaler.pkl')
features = joblib.load('feature_names.pkl')

# Prepare patient data
patient_data = pd.DataFrame([...])  # Your patient features

# Make prediction
predicted_status, probabilities = predict_status(patient_data)
print(f"Predicted Status: {predicted_status}")
```

## 🎨 Optional: Streamlit Web App

The notebook includes code for creating an interactive Streamlit web application. To use it:

1. Save the Streamlit code as `app.py`
2. Install Streamlit: `pip install streamlit`
3. Run: `streamlit run app.py`

## 📚 Dependencies

- pandas
- numpy
- matplotlib
- seaborn
- scikit-learn
- xgboost
- joblib
- jupyter
- streamlit (optional)

See `requirements.txt` for specific versions.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is open source and available under the MIT License.

## 👥 Authors

- Your Name

## 🙏 Acknowledgments

- Mayo Clinic for providing the original dataset
- scikit-learn and XGBoost communities for excellent ML libraries

## 📧 Contact

For questions or feedback, please open an issue on GitHub.

---

**Note:** This project is for educational and research purposes. Always consult with healthcare professionals for medical decisions.
