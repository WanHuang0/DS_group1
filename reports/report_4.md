# Milestone 4
## Task 1
ML experiment relies on a lot of factors, such as 

- Model architecture
- Code versions
- Dataset versions
- Hyperparameters
- Environment
- Metrics
- ...

We need to keep track on those parameters in order to:
- Better understand the model and the effect of - different parameters on it
- Be able to systematically try and later reproduce many possible experiments
- Collaborate with other team members and share and store the knowledge

Different software tools, which automatically track the hyperparameters of the experiments, help us manage and systematically run the experiments.

---

In order to compare and chose the most suitable ML model and experiment we need to summarize their output in one (often not possible) or several numbers. Those are called **Metrics**. 

**Precision** and **Recall** are performance metrics, used in ML tasks, such as pattern recognition, object detection, classification.
**Presision** (or Positive Predictive Value) - the fraction of relevant instances among the retrieved instances
**Recall** (or Sensitivity) - the fraction of relevant instances that were retrieved.


The Precision and Recall **Trade-off** shows that if you increase the precision then recall will decrease and if you increase the recall then precision will decrease. We can not simultaneously increase both precision and recall.
Usually, precision and recall scores are not discussed in isolation. Instead, either values for one measure are compared for a fixed level at the other measure (e.g. precision at a recall level of 0.75) or both are combined into a single weighted metric using specially designed formulae.

---

**Confusion Matrix** 
One of the basic classification metrics is the Confusion Matrix. It is a tabular visualization of the truth labels versus the model’s predictions. Each row of the confusion matrix represents instances in a predicted class and each column represents instances in an actual class. Confusion Matrix is not entirely a performance metric but provides a basis on which other metrics can evaluate the results. There are 4 classes of a Confusion Matrix. The True Positive signifies how many positive class samples the created model has predicted correctly. True Negative signifies how many negative class samples the created model predicted correctly. False Positive signifies how many negative class samples the created model predicted incorrectly and vice versa goes for False Negative. 

---

**AU-ROC Metric** 
The AUC-ROC is an essential technique to determine and evaluate the performance of a  classification model. Performing this test only increases the value and correctness of a model and in turn, helps improve its accuracy.  Using this method helps us summarize the actual trade-off between the true positive rate and the predictive value for a predictive model using different probability thresholds which is an important aspect of classification problems.

*Firstly - what is a ROC?*
ROC curve, also known as Receiver Operating Characteristics Curve, is a metric used to measure the performance of a classifier model. The ROC curve depicts the rate of true positives with respect to the rate of false positives, therefore highlighting the sensitivity of the classifier model. The ROC is also known as a relative operating characteristic curve, as it is a comparison of two operating characteristics, the True Positive Rate and the False Positive Rate, as the criterion changes. An ideal classifier will have a ROC where the graph would hit a true positive rate of 100% with zero false positives. We generally measure how many correct positive classifications are being gained with an increment in the rate of false positives.  

ROC curve can be used to select a threshold for a classifier, which maximizes the true positives and in turn minimizes the false positives. ROC Curves help determine the exact trade-off between the true positive rate and false-positive rate for a model using different measures of probability thresholds. ROC curves are more appropriate to be used when the observations present are balanced between each class. This method was first used in signal detection but is now also being used in many other areas such as medicine, radiology, natural hazards other than machine learning. A discrete classifier returns only the predicted class and gives a single point on the ROC space. But for probabilistic classifiers, which give a probability or score that reflects the degree to which an instance belongs to one class rather than another, we can create a curve by changing the threshold for the score.

*Second - what is an AUC?*
Area Under Curve or AUC is one of the most widely used metrics for model evaluation. It is generally used for binary classification problems. AUC measures the entire two-dimensional area present underneath the entire ROC curve. AUC of a classifier is equal to the probability that the classifier will rank a randomly chosen positive example higher than that of a randomly chosen negative example. The Area Under the Curve provides the ability for a classifier to distinguish between classes and is used as a summary of the ROC curve. The higher the AUC, it is assumed that the better the performance of the model at distinguishing between the positive and negative classes. 

**Understanding the AUC-ROC**
AUC-ROC is the valued metric used for evaluating the performance in classification models. The AUC-ROC metric clearly helps determine and tell us about the capability of a model in distinguishing the classes. The judging criteria being – Higher the AUC, better the model. AUC-ROC curves are frequently used to depict in a graphical way the connection and trade-off between sensitivity and specificity for every possible cut-off for a test being performed or a combination of tests being performed. The area under the ROC curve gives an idea about the benefit of using the test for the underlying question. AUC – ROC curves are also a performance measurement for the classification problems at various threshold settings. 

The AUC-ROC curve of a test can also be used as a criterion to measure the test’s discriminative ability, telling us how good the test is in a given clinical situation. The closer an AUC-ROC curve is to the upper left corner, the more efficient the test being performed will be. To combine the False Positive Rate and the True Positive Rate into a single metric, we can first compute the two former metrics with many different thresholds for the logistic regression, then plot them on a single graph. The resulting curve metric we consider is the area under this curve, which we call AUC-ROC.

## Task 2
### Choose an appropriate metric for optimizing your ML Model. What is the reasoning behind it?
**Wandb report:** https://api.wandb.ai/report/ds_group1/6616vdy6

**Metric:** Accuracy

**Reasons:** Accuracy is the quintessential classification metric. It is the proportion of true results among the total number of cases examined, i.e.,   
Accuracy = (TP+TN)/(TP+FP+FN+TN)  
It is pretty easy to understand and suited for binary as well as a multiclass classification problem. 
Accuracy is a valid choice of evaluation for classification problems when classes are well balanced and not skewed. We inspect the balance of training and test dataset in task3, and we find the classes are uniform distributed.

## Task 3
refer to ms4_task3.ipynb

## Hash digest of python packages
|Package|Version|Hash Digest|
|:------:|:---------:|------:|
|Tensorflow|2.11.0|d973458241c8771bf95d4ba68ad5d67b094f72dd181c2d562ffab538c1b0dad7|
|numpy|1.23.5|f9a909a8bae284d46bbfdefbdd4a262ba19d3bc9921b1e76126b1d21c3c34135|
|psycopg2|2.9.5|920bf418000dd17669d2904472efeab2b20546efd0548139618f8fa305d1d7ad|
|Pillow|9.3.0|0b07fffc13f474264c336298d1b4ce01d9c5a011415b79d4ee5527bb69ae6f65|
|wandb|0.13.7|b88fe5e75b01f537838dee3fe43c00e15d9d6dd08671503374858fb2e539fcd4|
