# Employee Tenure Predictor

This project predicts employee turnover risk using machine learning and provides an interactive web app for HR analytics.

## Overview
The Employee Tenure Predictor analyzes HR data to estimate the probability that an employee will leave the company. It uses a Random Forest model trained on historical HR data and offers a Streamlit web interface for easy predictions and risk interpretation.

## Features
- **Streamlit Web App**: User-friendly interface for entering employee data and viewing turnover risk.
- **Risk Zones**: Employees are categorized into Safe, Low, Medium, or High risk zones based on predicted probability.
- **Data Science Notebook**: Full data analysis, feature engineering, and model training in Jupyter Notebook.
- **Reusable Model Artifacts**: Trained model and feature list are saved for use in the app.

## File Structure

- `streamlit_app.py` — Streamlit app for interactive turnover prediction.
- `requirements.txt` — Python dependencies for the project.
- `Notebooks/CapstoneUnit3.ipynb` — Data analysis, EDA, and model training notebook.
- `Notebooks/HR_comma_sep.csv` — HR dataset used for model training.
- `Notebooks/rf_model.pkl` — Trained Random Forest model (binary file).
- `Notebooks/model_features.pkl` — List of model features (binary file).

## Quick Start

1. **Install dependencies**
	```bash
	pip install -r requirements.txt
	```
2. **Run the Streamlit app**
	```bash
	streamlit run streamlit_app.py
	```
3. **Open your browser** to the provided local URL to use the app.

    ```bash
	https://andie-andrews.streamlit.app/
	```

## Usage

Enter employee details (satisfaction, evaluation, projects, hours, tenure, accident, promotion) in the app. The model will output the probability of turnover and assign a risk zone:

- **Safe Zone (Green):** Probability < 20%
- **Low Risk (Yellow):** 20%–60%
- **Medium Risk (Orange):** 60%–90%
- **High Risk (Red):** > 90%

## Data & Model

- **Dataset:** `HR_comma_sep.csv` — Contains employee records with satisfaction, evaluation, workload, tenure, department, salary, and turnover status.
- **Notebook:** `CapstoneUnit3.ipynb` — Includes data cleaning, EDA, feature engineering, model training, and risk zone validation.
- **Model:** Random Forest classifier, saved as `rf_model.pkl` with feature columns in `model_features.pkl`.

## Example

![Streamlit App Screenshot](/image.png)

## Notes
- Predictions are based on historical data and are not definitive.
- For details on model development, see the Jupyter notebook in the Notebooks folder.

