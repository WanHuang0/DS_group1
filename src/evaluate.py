"""
## Evaluate the tested model
"""

def evaluate(model, x_test, y_test):
    '''
    Evaluate model performance
    
    model: trained model
    x_test (ndarray):  images from test set
    y_test (array):  lables from test set
    
    Output: test loss and accuracy
    '''    
    score = model.evaluate(x_test, y_test, verbose=0)    
    print("Test loss:", score[0])
    print("Test accuracy:", score[1])
    
    