import pickle


with open('models/logistic.pkl', 'rb') as f:
    lr = pickle.load(f)


def predict(sample):
    return lr.predict(sample).tolist()[0]