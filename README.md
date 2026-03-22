# HeartGuard AI - Clinical Risk Assessment

HeartGuard AI is a predictive healthcare application designed to assess cardiovascular disease risk using advanced Machine Learning. Built with a Flask backend and a modern, responsive UI, this tool allows both patients and healthcare providers to input clinical vitals and diagnostic metrics to generate real-time risk profiles and downloadable PDF reports.

## Key Features
* **Predictive Diagnostics:** Utilizes a K-Nearest Neighbors (KNN) model trained on clinical data to predict heart disease probability.
* **Secure Authentication:** Built-in user registration and login system with hashed passwords using Werkzeug and SQLite.
* **Clinical Dashboard:** A sleek, dark-themed, and responsive interface built with Bootstrap 5.
* **Automated Reporting:** Generates instant, downloadable clinical PDF reports using jsPDF.
* **Accessible Terminology:** Integrated medical glossary to help non-technical users understand their diagnostic inputs.

---

## 💻 Technologies Used

**Backend & Database:**
* Python 3
* Flask
* SQLite (via `sqlite3`)
* Werkzeug (Security/Hashing)

**Machine Learning:**
* Scikit-Learn (KNN Model)
* Pandas (Data Handling)
* Joblib (Model Serialization)

**Frontend:**
* HTML5 / CSS3
* Bootstrap 5
* jsPDF (Client-side PDF generation)

---

## 📸 Screenshots

<img width="1919" height="911" alt="Screenshot 2026-03-22 213432" src="https://github.com/user-attachments/assets/0a088618-b597-4cfd-918c-9b3a143d106e" />
<img width="1919" height="906" alt="Screenshot 2026-03-22 213546" src="https://github.com/user-attachments/assets/6cd2c090-2f22-41ab-8df9-bdb89cb5c0b3" />
<img width="1918" height="910" alt="Screenshot 2026-03-22 213619" src="https://github.com/user-attachments/assets/e4cbdcf6-e9ed-4255-9c71-2bd2241c85fa" />
<img width="1919" height="915" alt="Screenshot 2026-03-22 213645" src="https://github.com/user-attachments/assets/7504e87d-bd96-4731-a8c4-2f15d3f09986" />



---

## 🚀 Setup & Installation Instructions

Follow these steps to run the project locally on your machine.

**1. Clone the repository**
```bash
git clone [https://github.com/YOUR-USERNAME/HeartGuard-AI.git](https://github.com/YOUR-USERNAME/HeartGuard-AI.git)
cd HeartGuard-AI
```
**2. Create a virtual environment**
```bash
python -m venv venv
```
3. Activate the virtual environment
For Windows:
```bash
.\venv\Scripts\activate
```
For macOS/Linux:
```bash
source venv/bin/activate
```
4. Install dependencies
```bash
pip install -r requirements.txt
```
**5. Run the application**
```bash
python app.py
```
The SQLite database (users.db) will be automatically generated upon the first run.

**6. Access the web app**
Open your web browser and navigate to:
[http://127.0.0.1:5000](http://127.0.0.1:5000)

⚠️ Medical Disclaimer
HeartGuard AI is a predictive tool based on machine learning models and is intended for informational purposes only. It is not a substitute for professional medical advice, diagnosis, or treatment. Always consult a qualified healthcare provider for an accurate clinical evaluation.
