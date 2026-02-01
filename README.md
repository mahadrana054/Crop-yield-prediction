# 🌾 Crop Yield Prediction System
This project is an end-to-end Crop Yield Prediction application that estimates agricultural yield based on key environmental and regional factors. It integrates a machine learning model, a FastAPI backend, and a Streamlit frontend, all containerized using Docker for smooth deployment.

# 📌 Project Overview
The goal of this project is to predict crop yield using historical agricultural and climate data. The system follows a production-style architecture:
Machine Learning Model for yield prediction
FastAPI for serving predictions as REST APIs
Streamlit for an interactive web-based user interface
Docker for containerization and easy deploy

# 📊 Features Used for Prediction

The model predicts crop yield using the following input features:

1. Area – Country or region
2. Item – Crop type
3. Year – Year of production
4. Average Rainfall (mm/year)
5. Pesticides Used (tonnes)
6. Average Temperature (°C)

# 🤖 Model Performance

Multiple regression models were evaluated. Below are the results:

| MODEL                | MAE       | R2_sore   |
|----------------------|-----------|-----------|
| Lasso Regression     | 29005.83  | 0.6748    |
| Ridge Regression     | 28979.92  | 0.6740    |
| Decision Tree        | 4279.63   | 0.9734    |
| K-Nearest Neighbors  | 4609.15   | 0.9815    |

✅ Decision Tree and KNN models performed best, with high accuracy and low error.

