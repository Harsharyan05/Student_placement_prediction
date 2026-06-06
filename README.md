# 🎓 Student Placement Predictor

A Machine Learning-powered web application that predicts whether a student is likely to be placed based on academic performance, educational background, work experience, and employability factors.

---

# 🚀 Project Overview

This project uses Machine Learning to analyze student records and predict placement outcomes.

The solution covers the complete ML lifecycle:

* Data Collection
* Data Cleaning
* Feature Engineering
* Model Training
* Model Evaluation
* FastAPI Backend Development
* REST API Creation
* Cloud Deployment

---

# 🎯 Problem Statement

Can we predict whether a student will get placed based on their:

* SSC Performance
* HSC Performance
* Degree Performance
* MBA Performance
* Work Experience
* Employability Test Score
* Academic Background

This project solves that problem using supervised machine learning classification techniques.

---

# 🏗️ System Architecture

```mermaid
flowchart TD

A[Placement Dataset] --> B[Data Cleaning]

B --> C[Feature Engineering]

C --> D[One-Hot Encoding]

D --> E[Train-Test Split]

E --> F[Random Forest Classifier]

F --> G[placement_model.pkl]

G --> H[FastAPI Backend]

H --> I[Swagger UI]

H --> J[Postman]

I --> K[Prediction Response]

J --> K
```

---

# 🔄 Machine Learning Workflow

```mermaid
flowchart LR

A[Raw Dataset] --> B[EDA]

B --> C[Missing Value Analysis]

C --> D[Categorical Encoding]

D --> E[Feature Selection]

E --> F[Model Training]

F --> G[Model Evaluation]

G --> H[Model Serialization]

H --> I[API Development]

I --> J[Cloud Deployment]
```

---

# 📂 Project Structure

```text
student-placement-predictor/

│
├── placement.csv
├── train_model.py
├── app.py
├── placement_model.pkl
├── feature_names.pkl
├── requirements.txt
├── README.md
```

---

# 📊 Dataset Information

Dataset Source:

Campus Placement Dataset (Kaggle)

Features:

| Feature        | Description                   |
| -------------- | ----------------------------- |
| gender         | Student Gender                |
| ssc_p          | Secondary School Percentage   |
| ssc_b          | SSC Board                     |
| hsc_p          | Higher Secondary Percentage   |
| hsc_b          | HSC Board                     |
| hsc_s          | HSC Stream                    |
| degree_p       | Degree Percentage             |
| degree_t       | Degree Type                   |
| workex         | Work Experience               |
| etest_p        | Employability Test Percentage |
| specialisation | MBA Specialisation            |
| mba_p          | MBA Percentage                |

Target Variable:

```text
status
```

Values:

```text
Placed
Not Placed
```

---

# 📈 Feature Engineering Pipeline

```mermaid
flowchart TD

A[Categorical Features]

A --> B[Gender]

A --> C[SSC Board]

A --> D[HSC Board]

A --> E[Degree Type]

A --> F[Work Experience]

A --> G[Specialisation]

B --> H[One-Hot Encoding]
C --> H
D --> H
E --> H
F --> H
G --> H

H --> I[Machine Learning Features]
```

---

# 🧠 Model Training Pipeline

```mermaid
flowchart TD

A[placement.csv]

A --> B[Load Dataset]

B --> C[Drop Salary Column]

C --> D[Encode Categorical Features]

D --> E[Train-Test Split]

E --> F[Random Forest]

E --> G[Gradient Boosting]

E --> H[XGBoost]

F --> I[Model Comparison]
G --> I
H --> I

I --> J[Best Model Selection]

J --> K[placement_model.pkl]
```

---

# 🤖 Models Evaluated

The following machine learning algorithms were evaluated:

* Random Forest Classifier
* Gradient Boosting Classifier
* XGBoost Classifier

Best Performing Model:

```text
Random Forest Classifier
```

Accuracy Achieved:

```text
83.72%
```

---

# 🌐 API Architecture

```mermaid
sequenceDiagram

participant User
participant Swagger
participant FastAPI
participant ML_Model

User->>Swagger: Enter Student Details

Swagger->>FastAPI: POST /predict

FastAPI->>ML_Model: Predict()

ML_Model-->>FastAPI: Placement Result

FastAPI-->>Swagger: JSON Response

Swagger-->>User: Placed / Not Placed
```

---

# ⚙️ API Endpoints

## Home Endpoint

```http
GET /
```

Response:

```json
{
    "message": "Student Placement Prediction API Running"
}
```

---

## Prediction Endpoint

```http
POST /predict
```

Example Request:

```json
{
  "gender": "M",
  "ssc_p": 75,
  "ssc_b": "Central",
  "hsc_p": 70,
  "hsc_b": "Central",
  "hsc_s": "Science",
  "degree_p": 72,
  "degree_t": "Sci&Tech",
  "workex": "No",
  "etest_p": 80,
  "specialisation": "Mkt&HR",
  "mba_p": 70
}
```

Example Response:

```json
{
  "prediction": "Placed"
}
```

---

# 🎯 Prediction Pipeline

```mermaid
flowchart LR

A[Student Input]

A --> B[API Request]

B --> C[Data Transformation]

C --> D[Feature Alignment]

D --> E[Random Forest Model]

E --> F[Prediction]

F --> G[Placed]

F --> H[Not Placed]
```

---

# ☁️ Deployment Architecture

```mermaid
flowchart LR

A[Local Development]

A --> B[Git]

B --> C[GitHub Repository]

C --> D[Render Cloud]

D --> E[Public API]

E --> F[Swagger Docs]

E --> G[External Applications]
```

---

# 🚀 Run Locally

Install Dependencies:

```bash
pip install -r requirements.txt
```

Start FastAPI Server:

```bash
uvicorn app:app --reload
```

Open:

```text
http://127.0.0.1:8000/docs
```

---

# 🛠️ Tech Stack

### Machine Learning

* Python
* Pandas
* NumPy
* Scikit-Learn
* XGBoost
* Joblib

### Backend

* FastAPI
* Uvicorn

### Deployment

* Git
* GitHub
* Render

---

# 📌 Key Learning Outcomes

This project demonstrates practical experience in:

✅ Data Cleaning

✅ Feature Engineering

✅ Machine Learning Classification

✅ Model Evaluation

✅ FastAPI Development

✅ REST API Design

✅ Swagger Documentation

✅ Git & GitHub

✅ Cloud Deployment using Render

---

# 📈 Future Improvements

* Hyperparameter Tuning
* Cross Validation
* Feature Importance Analysis
* Streamlit Dashboard
* Docker Containerization
* CI/CD Pipeline
* Automated Model Retraining

---

# 👨‍💻 Author

**Harsh Aryan**

B.Tech Electronics & Communication Engineering

Interests:

* Machine Learning
* Data Science
* Artificial Intelligence
* Backend Development
* Cloud Deployment
