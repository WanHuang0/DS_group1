"""
## Setup
"""
from flask import Flask, render_template, request
from PIL import Image
import numpy as np
from keras.models import load_model
import db


# Create instance of flask
app = Flask(__name__, template_folder='templates')

def init():
    '''
    Load the pre-trained Keras model
    '''  
    global model
    model = load_model('model/model_nn.h5')

@app.route('/')
def upload_file():
   return render_template('index.html')
	
@app.route('/uploader', methods = ['POST'])
def upload_image_file():
   if request.method == 'POST':
        img = Image.open(request.files['file'].stream).convert("L")
        img = img.resize((28,28))
        
        # Convert image to numpy array
        im2arr = np.array(img)
        im2arr = im2arr.reshape(1,28,28,1)
        
        # Make inference
        y_pred = model.predict(im2arr)
        y_pred = np.argmax(y_pred)
        
        # save input converted image data and prediction in database
        db.insert_input(im2arr)
        db.insert_prediction(y_pred)
        return 'Predicted Number: ' + str(y_pred)
		
if __name__ == '__main__':
    print(("* Loading Keras model and Flask starting server..."
        "please wait until server has fully started"))
    init()
    app.run(debug = True,host="0.0.0.0", port=5000)
