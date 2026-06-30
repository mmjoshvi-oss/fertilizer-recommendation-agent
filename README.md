# 🌱 Fertilizer Prediction System

## 📌 Project Overview

The **Fertilizer Prediction System** is a Machine Learning-based web application that recommends the most suitable fertilizer for a crop based on environmental conditions and soil properties. The application helps farmers, agricultural professionals, and researchers choose the appropriate fertilizer to improve crop productivity and reduce unnecessary fertilizer usage.

The prediction model is built using the **Random Forest Classifier** algorithm and deployed with **Streamlit**, providing a simple and interactive user interface.

---

# 🎯 Objectives

* Predict the most suitable fertilizer for a given crop.
* Reduce fertilizer misuse.
* Improve agricultural productivity.
* Demonstrate the practical application of Machine Learning in agriculture.
* Provide a user-friendly web interface for fertilizer recommendations.

---

# 🚀 Features

* 🌱 Predicts the best fertilizer instantly.
* 🤖 Random Forest Machine Learning model.
* 📊 Simple and interactive Streamlit interface.
* ⚡ Fast prediction with high accuracy.
* 💻 Responsive web application.
* ☁️ Easy deployment on Streamlit Community Cloud.

---

# 🧠 Machine Learning Details

### Algorithm Used

* Random Forest Classifier

### Programming Language

* Python

### Libraries Used

* Scikit-learn
* Pandas
* NumPy
* Streamlit
* Pickle

---

# 📂 Project Structure

```text
Fertilizer-Prediction/
│
├── app.py
├── fertilizer_prediction_model.pkl
├── Fertilizer Prediction.csv
├── requirements.txt
├── runtime.txt
├── README.md
└── .gitignore
```

---

# 📊 Dataset Description

The model uses agricultural and environmental parameters to predict the most suitable fertilizer.

### Input Features

| Feature     | Description                 |
| ----------- | --------------------------- |
| Temperature | Temperature in °C           |
| Humidity    | Relative Humidity (%)       |
| Moisture    | Soil Moisture (%)           |
| Soil Type   | Type of Soil                |
| Crop Type   | Crop grown                  |
| Nitrogen    | Nitrogen content in soil    |
| Potassium   | Potassium content in soil   |
| Phosphorous | Phosphorous content in soil |

### Target Variable

* Fertilizer Name

---

# 🔄 Application Workflow

1. User enters soil and environmental information.
2. The application preprocesses the input data.
3. The trained Random Forest model predicts the fertilizer.
4. The predicted fertilizer is displayed instantly.

---

# 🛠 Technologies Used

### Programming

* Python

### Machine Learning

* Random Forest Classifier
* Scikit-learn

### Data Processing

* Pandas
* NumPy

### Web Framework

* Streamlit

### Version Control

* Git
* GitHub

---

# 💻 Installation

## Clone the Repository

```bash
git clone https://github.com/your-username/Fertilizer-Prediction.git
```

---

## Navigate to the Project

```bash
cd Fertilizer-Prediction
```

---

## Install Required Libraries

```bash
pip install -r requirements.txt
```

---

## Run the Application

```bash
streamlit run app.py
```

---

# 🌐 Deployment

The project can be deployed using **Streamlit Community Cloud**.

The repository should contain:

* app.py
* fertilizer_prediction_model.pkl
* requirements.txt
* runtime.txt
* README.md

---

# 📈 Model Performance

The model was trained using the **Random Forest Classifier**.

### Evaluation Metrics

* Accuracy
* Precision
* Recall
* F1-Score
* Confusion Matrix

These metrics were used to evaluate the model's predictive performance.

---

# 📸 User Interface

The application provides an easy-to-use interface where users can:

* Enter environmental conditions.
* Select soil type.
* Select crop type.
* Enter soil nutrient values.
* Click **Predict Fertilizer**.
* View the recommended fertilizer instantly.

---

# 📈 Future Enhancements

* 🌦️ Live Weather API Integration
* 📍 GPS-based Soil Detection
* 🤖 AI Agricultural Chatbot
* 📊 Fertilizer Usage Dashboard
* 📱 Mobile Application
* ☁️ Cloud Database Integration
* 🌍 Multi-language Support
* 📄 Download Prediction Report as PDF

---

# 👨‍💻 Author

**Your Name**

B.Tech Student

Machine Learning Enthusiast

Python Developer

---

# 📜 License

This project is developed for educational and research purposes.

---

# ⭐ Support

If you found this project useful, please consider giving it a ⭐ on GitHub.

Your support helps improve and maintain the project.

---

## Thank You

Thank you for visiting this repository. Happy Learning and Happy Coding! 🚀🌱
