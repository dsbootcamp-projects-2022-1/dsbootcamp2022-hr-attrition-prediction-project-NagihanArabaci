import pickle

# TODO
model_path = 'models/*****'


with open('models/logistic_regression, 'rb') as f:
    model = pickle.load(f)


def predict(sample):
    return model.predict(sample).tolist()[0]