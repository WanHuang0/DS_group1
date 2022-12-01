"""
## Setup
"""
import numpy as np
from tensorflow import keras

def scale(x_data):
    '''
    Scale value of matrices,
    and expand the dimension of matrices by adding one new axis
    
    x_data (ndarray): image matrices
    
    Returns: image matrices
    '''
    # Scale images to the [0, 1] range
    x_data = x_data.astype("float32") / 255
    # Make sure images have one extra dimension
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
       



    