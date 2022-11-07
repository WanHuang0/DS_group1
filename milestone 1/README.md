# Milestone 1
## task 1 
Explain the data set

1. The MNIST database is a large database of handwritten digits that is commonly used for training various image processing systems. 
It solves the classification problems. Specifically, it is used to classify a given image of handwritten digit into one of 10 classes 
representing integer value from 0 to 9.
2. MNIST consists of 70,000 handwritten images of digits (60,000 images in the training set and 10,000 in the test set). The images are
28x28 pixel grayscale. All images are labeled with the respective digit that they represent. There are a total of 10 classes of digits (from 0 to 9).

## task 4
Explain how to run the code

1. 
2. python version 3.8, packages tensorflow and numpy are required.
3.

## Task 5
Explaining what the code does

### What is the input to and the output from the neural network

The Neural Network is constructed from 3 type of layers:
- Input layer — initial data for the neural network.
- Hidden layers — intermediate layer between input and output layer and place where all the computation is done.
- Output layer — produce the result for given inputs.


### What is Keras? And how does it relate to Tensorflow?
Keras is the high-level API of TensorFlow: an approachable, highly-productive interface for solving machine learning problems, with a focus on modern deep learning. 
It provides essential abstractions and building blocks for developing and shipping machine learning solutions with high iteration velocity.

Keras empowers engineers and researchers to take full advantage of the scalability and cross-platform capabilities of TensorFlow: you can run Keras on large clusters of GPUs, and you can export your Keras models to run in the browser or on a mobile device.

TensorFlow is an end-to-end, open-source machine learning platform. You can think of it as an infrastructure layer for differentiable programming. It combines four key abilities:

- Efficiently executing low-level tensor operations on CPU, GPU, or TPU.
- Computing the gradient of arbitrary differentiable expressions.
- Scaling computation to many devices, such as clusters of hundreds of GPUs.
- Exporting programs ("graphs") to external runtimes such as servers, browsers, mobile and embedded devices.


### How is the data loaded
The data are loaded to Python through Keras.
```
(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()
```

### Which dependencies are imported

Following dependencies are imported:
```
import numpy as np
from tensorflow import keras
from tensorflow.keras import layers
```

### What kind of neural network architecture are you dealing with?

We are dealing here with a Convolutional Neural Network (CNN).
Convolutional Neural Networks is a type of Feed-Forward Neural Networks used in tasks like image analysis, natural language processing, and other complex image classification problems.

A CNN has hidden layers of convolutional layers that form the base of ConvNets. 






