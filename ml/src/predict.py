import pickle

def predict(input_data):
    # Load the model
    with open('campaign_success_model.pkl', 'rb') as file:
        model = pickle.load(file)

    # Predict
    prediction = model.predict(input_data)
    return prediction
  
 
 
 
