# Student Performance Prediction

A machine learning project that predicts a student's **exam score** based on study habits, lifestyle, and academic factors.

It uses a **Linear Regression model** with a full Scikit-learn Pipeline and is deployed using a **Flask web app**.

## Overview

This project:

* Cleans and processes student data
* Handles missing values
* Encodes categorical features
* Trains a Linear Regression model
* Evaluates performance
* Saves the trained model
* Predicts exam scores for new students
* Deploys via Flask

## Dataset

The project uses the **<a href="https://www.kaggle.com/datasets/jayaantanaath/student-habits-vs-academic-performance">Student Habits and Performance** dataset.

The target variable is:

```text
exam_score
```

### Features Used

The model uses the following 11 features:

| Feature                    | Type      |
| -------------------------- | --------- |
| `study_hours_per_day`      | Numerical |
| `social_media_hours`       | Numerical |
| `netflix_hours`            | Numerical |
| `part_time_job`            | Nominal   |
| `attendance_percentage`    | Numerical |
| `sleep_hours`              | Numerical |
| `diet_quality`             | Ordinal   |
| `exercise_frequency`       | Numerical |
| `parental_education_level` | Ordinal   |
| `internet_quality`         | Ordinal   |
| `mental_health_rating`     | Numerical |


## Model

The project currently uses:

**Linear Regression**

The complete preprocessing and model are stored together in a single Pipeline.

```text
Preprocessing Pipeline
        +
Linear Regression
        ↓
student_performance_linear_regression.pkl
```

## Model Evaluation

The model is evaluated using:

* Mean Absolute Error (MAE)
* Mean Squared Error (MSE)
* Root Mean Squared Error (RMSE)
* R² Score


## Flask Web Application

The trained model is deployed using Flask.

Users can enter student information through a web form, and the application predicts the student's exam score.


## Project Structure

```text
Student-Performance-Prediction/
│
├── app.py
│
├── model/
│   └── student_performance_linear_regression.pkl
│
├── templates/
│   └── index.html
│
├── static/
│   └── css/
│       └── style.css
│
├── Dataset/
│   └── student_habits_performance.csv
│
├── notebooks/
│   ├── Exploratory_Data_Analysis.ipynb
│   ├── model_trainig.ipunb
|   └── prediction.ipynb
|
├── requirements.txt
│
└── README.md
```


## Installation

### 1. Clone the repository

```bash
git clone <https://github.com/ayankb/Student-Performance-Prediction.git>
```

Move into the project directory:

```bash
cd Student-Performance-Prediction
```

### 2. Create a Virtual Environment

```bash
python -m venv .env
```

Activate the environment:

```bash
.env\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

## Run the Flask Application

```bash
python app.py
```

The application will run locally at:

```text
http://127.0.0.1:5000
```

Open the address in your web browser.

## Prediction Flow

```text
User Input → DataFrame → Pipeline → Prediction → Exam Score
```

## Tech Stack

* Python
* Pandas, NumPy
* Scikit-learn
* Flask
* Matplotlib
* Jupyter Notebook
* HTML
* CSS

