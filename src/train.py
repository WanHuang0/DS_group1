"""
## Setup
"""
from tensorflow import keras
import neuralnet_architecture as nn


"""
## Train the model
"""
def train_nn(x_train, y_train, batch_size = 128, epochs = 1, optimizer = "adam"):
    '''
    Train the model
    
    x_train (ndarray): images from training set
    y_train (array): lables from training set
    batch_size (integer): the number of training examples in a single batch
    epochs (integer): number of epochs
    
    Returns: trained neural network model
    '''
    # Initialize the object and build the architecture
    model = nn.Model()
    built_model = model.build()
    
    built_model.compile(loss="categorical_crossentropy", optimizer=optimizer, metrics=["accuracy"])
    history = built_model.fit(x_train, y_train, batch_size=batch_size, epochs=epochs, validation_split=0.1)
    keras.models.save_model(built_model, "/model/model_nn.h5")
    return history



