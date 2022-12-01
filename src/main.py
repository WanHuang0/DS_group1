"""
## Setup
"""
from tensorflow import keras
import data_process as data
from train import train_nn 

"""
## Prepare the data
"""
# Model / data parameters
num_classes = 10
input_shape = (28, 28, 1)

# Load the data and split it between train and test sets
(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

# Scale input data
x_train = data.scale(x_train)
x_test = data.scale(x_test)

# Convert to binary matrices
y_train = data.convertBin(y_train, num_classes)
y_test = data.convertBin(y_test, num_classes)

# Print dimensions of training set and number of samples
print("x_train shape:", x_train.shape)
print(x_train.shape[0], "samples")  
print("x_test shape:", x_test.shape)
print(x_test.shape[0], "samples") 

"""
## Train and save the model
"""
train_nn(x_train, y_train)


"""
## Predict with the trained model
"""
trained_model = keras.models.load_model("model_nn.h5")
y_pred = trained_model.predict(x_test)


"""
## Evaluate the trained model
"""
score = trained_model.evaluate(x_test, y_test, verbose=0)
print("Test loss:", score[0])
print("Test accuracy:", score[1])


