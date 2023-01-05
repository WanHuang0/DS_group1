
"""
## Predict with the trained model
"""
def predict(model, x_data):
    '''
    Predict digits given handwritten digits images
    
    model: trained model
    x_data (ndarray): input images 
    
    return: probability distributions over classes
    '''
    y_pred = model.predict(x_data)
    return y_pred




