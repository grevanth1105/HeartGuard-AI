from flask import Flask, render_template, request, redirect, url_for, session, flash
import pandas as pd
import joblib
from datetime import datetime
import json
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = "super_secret_key"

model = joblib.load("KNN_heart.pkl")
scaler = joblib.load("scaler.pkl")
expected_columns = joblib.load("columns.pkl")

def init_db():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, username TEXT UNIQUE, password TEXT)')
    conn.commit()
    conn.close()

init_db()

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        name = request.form.get("name")
        username = request.form.get("username")
        password = request.form.get("password")
        hashed_password = generate_password_hash(password)

        try:
            conn = sqlite3.connect('users.db')
            c = conn.cursor()
            c.execute("INSERT INTO users (name, username, password) VALUES (?, ?, ?)", (name, username, hashed_password))
            conn.commit()
            conn.close()
            return redirect(url_for('login'))
        except sqlite3.IntegrityError:
            flash("Username already exists.", "danger")
            return redirect(url_for('signup'))
            
    return render_template("signup.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        c.execute("SELECT * FROM users WHERE username = ?", (username,))
        user = c.fetchone()
        conn.close()

        if user and check_password_hash(user[3], password):
            session['user_id'] = user[0]
            session['name'] = user[1]
            session['username'] = user[2]
            return redirect(url_for('predict'))
        else:
            flash("Invalid credentials.", "danger")
            return redirect(url_for('login'))
            
    return render_template("login.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for('home'))

@app.route("/predict", methods=["GET", "POST"])
def predict():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    prediction = None
    report_data = None

    if request.method == "POST":
        age = int(request.form.get("Age"))
        sex = request.form.get("Sex")
        chest_pain = request.form.get("ChestPainType")
        exercise_angina = request.form.get("ExerciseAngina")
        resting_bp = int(request.form.get("RestingBP"))
        cholesterol = int(request.form.get("Cholesterol"))
        fasting_bs = int(request.form.get("FastingBS"))
        resting_ecg = request.form.get("RestingECG")
        max_hr = int(request.form.get("MaxHR"))
        oldpeak = float(request.form.get("Oldpeak"))
        st_slope = request.form.get("ST_Slope")

        raw_input = {
            'Age': age,
            'RestingBP': resting_bp,
            'Cholesterol': cholesterol,
            'FastingBS': fasting_bs,
            'MaxHR': max_hr,
            'Oldpeak': oldpeak,
            'Sex_' + sex: 1,
            'ChestPainType_' + chest_pain: 1,
            'RestingECG_' + resting_ecg: 1,
            'ExerciseAngina_' + exercise_angina: 1,
            'ST_Slope_' + st_slope: 1
        }

        input_df = pd.DataFrame([raw_input])

        for col in expected_columns:
            if col not in input_df.columns:
                input_df[col] = 0

        input_df = input_df[expected_columns]
        scaled_input = scaler.transform(input_df)
        prediction = int(model.predict(scaled_input)[0])

        report_text = f"""
HEARTGUARD AI - MEDICAL RISK ASSESSMENT REPORT
----------------------------------------------
Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
Assessed By: {session.get('name', session['username'])}

PATIENT VITALS:
- Age: {age}
- Sex: {sex}
- Resting BP: {resting_bp} mm Hg
- Cholesterol: {cholesterol} mg/dL
- Max Heart Rate: {max_hr}
- Fasting BS > 120: {"Yes" if fasting_bs == 1 else "No"}

HEART METRICS:
- Chest Pain Type: {chest_pain}
- Resting ECG: {resting_ecg}
- Exercise Angina: {exercise_angina}
- ST Slope: {st_slope}
- Oldpeak: {oldpeak}

PREDICTION RESULT:
{"[HIGH RISK] - Immediate consultation recommended." if prediction == 1 else "[LOW RISK] - Maintain healthy lifestyle."}
----------------------------------------------
Disclaimer: This tool is for informational purposes only.
"""
        report_data = json.dumps(report_text)

    return render_template("predict.html", prediction=prediction, report_data=report_data)

if __name__ == "__main__":
    app.run(debug=True)