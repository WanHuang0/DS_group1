# Milestone 5
In our project we include the following modules. Each performs independent functionalities.
- `data_process.py` prepare data
- `neuralnet_architecture.py` build neural network architecture
- `train.py` train the model
- `predict.py` make inference
- `evaluate.py` evaluate model performance
- `experiment.py` tune hyperparameters and log experiment results
- `db.py` manage database
- `main.py` act as the point of execution
- `app.py` flask application

To run our machine learning model, first we enter
```
docker-compose up -d
```
then we input
```
docker run -it --network=src_app-tier -p 5000:5000 --env-file=.env src_app bash
```
which is followed by command
```
python3 main.py
```
It will train and save the model.

Next, by running 
```
python3 app.py
```
we start flask application. We can see the frontend on http://127.0.0.1:5000/.
Every time after uploading image and making prediction, we can see the relevant data is stored in database `mnist`.
We can inspect it with pgadmin (http://127.0.0.1:5050/)


## Hash digest of python packages
|Package|Version|Hash Digest|
|:------:|:---------:|------:|
|Tensorflow|2.11.0|d973458241c8771bf95d4ba68ad5d67b094f72dd181c2d562ffab538c1b0dad7|
|numpy|1.23.5|f9a909a8bae284d46bbfdefbdd4a262ba19d3bc9921b1e76126b1d21c3c34135|
|psycopg2|2.9.5|920bf418000dd17669d2904472efeab2b20546efd0548139618f8fa305d1d7ad|
|Pillow|9.3.0|0b07fffc13f474264c336298d1b4ce01d9c5a011415b79d4ee5527bb69ae6f65|
|wandb|0.13.7|b88fe5e75b01f537838dee3fe43c00e15d9d6dd08671503374858fb2e539fcd4|
|flask|2.2.2|642c450d19c4ad482f96729bd2a8f6d32554aa1e231f4f6b4e7e5264b16cca2b|