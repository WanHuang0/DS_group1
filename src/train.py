"""
## Setup
"""
from tensorflow import keras
import neuralnet_architecture as nn
import data_process as data


"""
## Train the model
"""
def train(model, x_train, y_train, batch_size = 128, epochs = 15):
    '''
    Train the model
    
    model: built model 
    x_train (ndarray): images from training set
    y_train (array): lables from training set
    batch_size (integer): the number of training examples in a single batch
    epochs (integer): number of epochs
    
    Returns: trained neural network model
    '''
    model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])
    model.fit(x_train, y_train, batch_size=batch_size, epochs=epochs, validation_split=0.1)
    return model

# Initialize the object
model = nn.Model()
model_built = model.build()
   
# Train model
trained = train(model_built, data.x_train, data.y_train)
keras.models.save_model(trained, "model_nn.h5")