# 🫀 HeartGuard AI - Clinical Risk Assessment

HeartGuard AI is a predictive healthcare application designed to assess cardiovascular disease risk using advanced Machine Learning. Built with a Flask backend and a modern, responsive UI, this tool allows both patients and healthcare providers to input clinical vitals and diagnostic metrics to generate real-time risk profiles and downloadable PDF reports.

## ✨ Key Features
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

*(Replace the placeholder links below with actual paths to your images once uploaded to your repository)*

| Home Screen | Clinical Dashboard |
| :---: | :---: |
| `<img src="link_to_home_screenshot.png" width="400"/>` | `<img src="link_to_dashboard_screenshot.png" width="400"/>` |

| Risk Assessment Result | Downloadable Report |
| :---: | :---: |
| `<img src="link_to_result_screenshot.png" width="400"/>` | `<img src="link_to_pdf_screenshot.png" width="400"/>` |

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
