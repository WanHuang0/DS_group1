"""
## Setup
"""
from tensorflow import keras
from tensorflow.keras import layers 


"""
## Build the model
"""
class Model:

    def __init__(self):
        '''
        Initializes a Model object
        '''
        pass
        
    def build(self, input_shape = (28, 28, 1), num_classes = 10):
        '''
        Build architecture of neural network
        
        input_shape (tuple): dimension of input data
        num_classes (integer): number of classes
            
        Returns: neural network model
        '''
        self.shape = input_shape
        self.classes = num_classes
        self.model = keras.Sequential(
            [
                keras.Input(shape=self.shape),
                layers.Conv2D(32, kernel_size=(3, 3), activation="relu"),
                layers.MaxPooling2D(pool_size=(2, 2)),
                layers.Conv2D(64, kernel_size=(3, 3), activation="relu"),
                layers.MaxPooling2D(pool_size=(2, 2)),
                layers.Flatten(),
                layers.Dropout(0.5),
                layers.Dense(self.classes, activation="softmax"),
            ]
        )
        # Show the structure of neural network model
        self.summary = self.model.summary
        return self.model


