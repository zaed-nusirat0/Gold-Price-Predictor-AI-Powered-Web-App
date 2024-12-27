from flask import Flask ,request,render_template,jsonify
import joblib
import numpy as np

model=joblib.load('model.pkl')

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')
@app.route('/predict', methods=['POST'])
def predict():
    try:
        
        spx = float(request.form['spx'])
        uso = float(request.form['uso'])
        slv = float(request.form['slv'])
        eur_usd = float(request.form['eur_usd'])
        year = float(request.form['year'])

        input_data = np.array([[spx, uso, slv, eur_usd, year]])

        predicted_value = model.predict(input_data)[0]

        return render_template('result.html', prediction=round(predicted_value,2))

    except Exception as e:
        return jsonify({"error": str(e)})
if __name__ == '__main__':
        app.run(host='0.0.0.0', port=8000, debug=True)

