"""
## Setup
"""
import numpy as np
from tensorflow import keras

"""
## Prepare the data
"""
# Model / data parameters
num_classes = 10
input_shape = (28, 28, 1)

# Load the data and split it between train and test sets
(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

def scale(x_data):
    '''
    Scale value of matrices,
    and expand the dimension of matrices by adding one new axis
    
    x_data (ndarray): image matrices
    
    Returns: image matrices
    '''
    # Scale images to the [0, 1] range
    x_data = x_data.astype("float32") / 255
    # Make sure images have shape (28, 28, 1)
    x_data = np.expand_dims(x_data, -1)
    return x_data

def convertBin(y_data, num_classes):
    '''
    Convert class vectors to binary class matrices
    
    num_classes (integer): number of classes 
    
    Returns: a binary class matrices
    '''
    y_data = keras.utils.to_categorical(y_data, num_classes)    
    return y_data
       
# Process data
x_train = scale(x_train)
x_test = scale(x_test)
y_train = convertBin(y_train, num_classes)
y_test = convertBin(y_test, num_classes)


if __name__ == '__main__':
    # dimensions of training set and number of samples
    print("train shape:", x_train.shape)
    print(x_train.shape[0], "samples")
    # dimensions of test set and number of samples
    print("test shape:", x_test.shape)
    print(x_test.shape[0], "samples")
    