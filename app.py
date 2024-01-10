from flask import Flask, request, render_template,jsonify
import joblib

app = Flask(__name__)
with open('model.pkl', 'rb') as f:
    model = joblib.load(f)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/aboutus')
def aboutus():
     return render_template('aboutus.html')
@app.route('/signup')
def signup():
     return render_template('signup.html')
@app.route('/login')
def login():
     return render_template('login.html')
@app.route('/chatbot')
def chatbot():
    return render_template('chatbot.html') 

@app.route('/predict', methods=['POST'])
def predict():
    try:
        age = int(request.form['age'])
        sex = 1 if request.form['sex'] == 'female' else 0
        cp = int(request.form['cp'])
        trestbps = int(request.form['trestbps'])
        chol = int(request.form['chol'])

        # Perform prediction using machine learning model
        prediction = model.predict([[age, sex, cp, trestbps, chol]])
        if prediction[0] == 0:
            message = "You don't have a heart disease.But it's better to be careful.Consider referring to our diet and precautions sessions."
        else:
            message = "You may have a heart disease. So it's better to consult a doctor."

        return message
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)

if __name__ == '__main__':
    app.run(debug=True)














