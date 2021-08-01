from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST', "GET"])
def predict():
    if request.method == "POST":
        int_features = [x for x in request.form.values()]
        for x in int_features:
            if x == 'd':
                int_features.extend([1, 0])
                int_features.remove('d')
            if x == 'p':
                int_features.extend([0, 1])
                int_features.remove('p')
            if x == 'g':
                int_features.extend([0, 0])
                int_features.remove('g')
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)
    output = round(prediction[0], 2)

    return render_template('output.html', output=output)


if __name__ == '__main__':
    app.run(debug=True)
