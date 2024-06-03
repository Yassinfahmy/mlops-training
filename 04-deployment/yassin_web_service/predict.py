from flask import Flask, request, jsonify
import pickle


with open('lin_reg.bin', 'rb') as model_file:
    dict_vectorizer, model = pickle.load(model_file)

def prepare_features(ride):
    # pu_id = str(ride["PULocationID"]) + '_' + str(ride["DOLocationID"])
    features = {
        'PU_DO' : '50_30',
        'trip_distance': ride['trip_distance']
    }
    return features

def predict(features):
    features = prepare_features(features)
    X = dict_vectorizer.transform(features)
    return float(model.predict(X)[0])


app = Flask('Duration-Prediction')

@app.route('/predict', methods=['POST'])
def predict_endpoint():
    ride = request.get_json()

    features = prepare_features(ride)
    y = predict(features)

    result = {
        'duration':y
    }
    return jsonify(result)

if __name__ =="__main__":
    app.run(debug=True, host='0.0.0.0', port=9696) 
