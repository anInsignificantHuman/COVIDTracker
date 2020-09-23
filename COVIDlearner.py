# This file uses Machine Learning to estimate data for today and tomorrow

# Imports And Setup
from sklearn.linear_model import LinearRegression
line_fitter = LinearRegression()

# Predicts Values
def predict(y):
    global line_fitter
    line_fitter.fit([[1], [2]], y)
    predictions = line_fitter.predict([[3], [4]])
    return [float(str(predictions[0]).replace("[", "").replace("]", "")), float(str(predictions[1]).replace("[", "").replace("]", ""))]