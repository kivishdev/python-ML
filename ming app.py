from flask import Flask, request, render_template
import pickle

app = Flask(__name__)

# Load the trained model
with open('heart_health_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Route to render each HTML template
@app.route('/')
def welcome():
    return render_template('welcome.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/contact_us')
def contact_us():
    return render_template('contact us.html')

@app.route('/About_us')
def about_us():
    return render_template('About us.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/forgetpassword')
def forget_password():
    return render_template('forgetpassword.html')

# Route to render the prediction form page
@app.route('/prediction_form')
def prediction_form():
    return render_template('prediction form.html')

# Route to handle form submission and display prediction results
@app.route('/predict', methods=['POST'])
def predict():
    # Extract input data from the form
    age = float(request.form['age'])
    sex = 1 if request.form['sex'] == 'male' else 0
    smoking = 1 if request.form['smoking'] == 'Yes' else 0
    diabetes = 1 if request.form['Diabetes'] == 'Yes' else 0
    obesity = 1 if request.form['Obesity'] == 'Yes' else 0
    anaemia = 1 if request.form['Anaemia'] == 'Yes' else 0
    high_blood_pressure = 1 if request.form['HighBloodPressure'] == 'Yes' else 0  # Corrected field name here
    cholesterol = float(request.form['cholestrol'])  # Corrected field name here
    ecg_result = 1 if request.form['ECGResult'] == 'Yes' else 0  # Updated field name here

    # Make predictions using the loaded model
    prediction = model.predict([[age, sex, smoking, diabetes, obesity, anaemia, high_blood_pressure, cholesterol, ecg_result]])[0]

    # Map the prediction to a human-readable label
    prediction_label = "Heart Failure" if prediction == 1 else "No Heart Failure"

    # Render prediction results page and pass prediction data
    return render_template('prediction_resut.html', prediction=prediction_label)

if __name__ == '__main__':
    app.run(debug=True)

