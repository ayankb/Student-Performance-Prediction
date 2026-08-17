from flask import Flask, render_template, request
import pandas as pd
import numpy as np
import joblib


app = Flask(__name__)


model = joblib.load(
    "models/student_performance_linear_regression.pkl"
)


@app.route("/", methods=["GET", "POST"])
def home():

    prediction = None
    error = None

    if request.method == "POST":
        data = request.form

        try:
            study_hours = float(data["study_hours_per_day"])
            social_media_hours = float(data["social_media_hours"])
            netflix_hours = float(data["netflix_hours"])
            part_time_job = data["part_time_job"]
            attendance = float(data["attendance_percentage"])
            sleep_hours = float(data["sleep_hours"])
            diet_quality = data["diet_quality"]
            exercise_frequency = float(data["exercise_frequency"])
            parental_education = data["parental_education_level"]
            internet_quality = data["internet_quality"]
            mental_health = float(data["mental_health_rating"])

            features = ['study_hours_per_day', 'social_media_hours', 'netflix_hours', 'part_time_job', 'attendance_percentage', 'sleep_hours', 
                        'diet_quality', 'exercise_frequency', 'parental_education_level', 'internet_quality', 'mental_health_rating']

            new_input = pd.DataFrame(
                np.array([study_hours, social_media_hours, netflix_hours, part_time_job, attendance, sleep_hours, diet_quality, 
                                               exercise_frequency, parental_education, internet_quality, mental_health]).reshape(1, 11), 
                                               columns=features
                )

            prediction = round(model.predict(new_input)[0], 2)
            prediction = np.clip(prediction, 0, 100)


        except ValueError as e:

            error = str(e)


        except Exception as e:

            print("Error:", e)

            error = (
                "Something went wrong. "
                "Please check your input and try again."
            )

    return render_template("index.html", prediction=prediction, error=error)


if __name__ == "__main__":
    app.run(debug=True)
