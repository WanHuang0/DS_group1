"""
## Setup
"""
from tensorflow import keras
import data_process as data
from train import train_nn 
import wandb

wandb.login()


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
## Run experiments
"""
def run_experiment():
    '''
    Run experiments with different hyperparameters
    '''
    wandb.init(project='DS-project')
      
    batch_size = wandb.config.batch_size
    epochs = wandb.config.epochs
    optimizer = wandb.config.optimizer
    
    history = train_nn(x_train, y_train, batch_size=batch_size, epochs=epochs, optimizer=optimizer)
    
    train_loss = history.history["loss"]
    train_acc = history.history["accuracy"]
    val_loss = history.history["val_loss"]
    val_acc = history.history["val_accuracy"]
    
    for epoch in range(1, epochs+1, 1):
        wandb.log({
          'epoch': epoch, 
          'batch_size': batch_size,
          'train_acc': train_acc[epoch-1], 
          'train_loss': train_loss[epoch-1],
          'val_loss': val_loss[epoch-1],
          'val_acc': val_acc[epoch-1]
        })

# Define sweep
sweep_configuration = {
    'method': 'random',
    'name': 'sweep',
    'metric': {'goal': 'maximize', 'name': 'val_acc'},
    'parameters': 
    {
        'batch_size': {'values': [16, 32, 64]},
        'epochs': {'values': [3, 4, 5]},
        'optimizer': {'values': ['adam', "SGD"]}
      }
}
    
# Initialize sweep by passing in config
sweep_id = wandb.sweep(sweep=sweep_configuration, project='DS-project')

# Call to `wandb.agent` to start a sweep
wandb.agent(sweep_id, function=run_experiment, count=1)

# Close wandb run 
wandb.finish()