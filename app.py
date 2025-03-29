import pickle
from flask import Flask, render_template, request

with open('salary_model.pkl', 'rb') as file:
    model = pickle.load(file)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST','GET'])
def predict():
    if request.method == 'POST':
        y = int(request.form['years'])
        h = int(request.form['hours'])

        pred_result=int(model.predict([[y,h]]))
        return render_template('index.html', result=pred_result) 

if __name__=='__main__':
    app.run(debug=True)