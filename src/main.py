"""
## Setup
"""
from tensorflow import keras
import data_process as data
import train


"""
## Load the processed test data
"""
x_test, y_test = data.x_test, data.y_test


"""
## Train and save the model
"""
train


"""
## Load the model
"""
model = keras.models.load_model("model_nn.h5")


"""
## Predict with the trained model
"""
y_pred = model.predict(x_test)


"""
## Evaluate the trained model
"""
score = model.evaluate(x_test, y_test, verbose=0)
print("Test loss:", score[0])
print("Test accuracy:", score[1])


