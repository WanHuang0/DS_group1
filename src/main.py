"""
## Setup
"""
from tensorflow import keras
import data_process as data
from train import train_nn 
from evaluate import evaluate
from predict import predict
import wandb

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
# Initialize wandb object
wandb.init(project='DS-project') 

train_nn(x_train, y_train)


"""
## Predict with the trained model
"""
trained_model = keras.models.load_model("/model/model_nn.h5")
y_pred = predict(trained_model, x_test)


"""
## Evaluate the trained model
"""
score = evaluate(trained_model, x_test, y_test)

# Close wandb run 
wandb.finish()

