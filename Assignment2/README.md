# Usage
### Spark
#### Preprocessing
This will process the enron1 dataset into a simpler format for Spark. The output 
file created will be **enron_spark_input.txt**.
```bash
python preprocess_spark.py
```

#### Training & Evaluating
##### 100 Features
```bash
python nb_spark.py input/enron_spark_input.txt 100
```

```bash
Loading input file input/enron_spark_input.txt ...
        Total number of emails: 5172                                            
        Total number of spam emails: 1500
        Total number of ham emails: 3672
Hashing words into features ...
Labeling features ...
Splitting data into training and testing sets ...
Training the model ...
Evaluating the model ...                                                        
model accuracy: 0.8353293413173652                                              

real    0m12.151s
user    0m0.784s
sys     0m0.536s
```
##### 1000 Features
```bash
python nb_spark.py input/enron_spark_input.txt 1000
```

```bash
Loading input file input/enron_spark_input.txt ...
        Total number of emails: 5172                                            
        Total number of spam emails: 1500
        Total number of ham emails: 3672
Hashing words into features ...
Labeling features ...
Splitting data into training and testing sets ...
Training the model ...
Evaluating the model ...                                                        
model accuracy: 0.8942486085343229                                              

real    0m12.859s
user    0m0.782s
sys     0m0.583s
```

##### 5000 Features
```bash
python nb_spark.py input/enron_spark_input.txt 5000
```

```bash
Loading input file input/enron_spark_input.txt ...
        Total number of emails: 5172                                            
        Total number of spam emails: 1500
        Total number of ham emails: 3672
Hashing words into features ...
Labeling features ...
Splitting data into training and testing sets ...
Training the model ...
Evaluating the model ...                                                        
model accuracy: 0.9520153550863724                                              

real    0m11.605s
user    0m0.888s
sys     0m0.548s
```

##### 10000 Features
```bash
python nb_spark.py input/enron_spark_input.txt 10000
```

```bash
Loading input file input/enron_spark_input.txt ...
        Total number of emails: 5172                                            
        Total number of spam emails: 1500
        Total number of ham emails: 3672
Hashing words into features ...
Labeling features ...
Splitting data into training and testing sets ...
Training the model ...
Evaluating the model ...                                                        
model accuracy: 0.9601634320735445                                              

real    0m11.827s
user    0m0.839s
sys     0m0.554s
```

##### 25000 Features
```bash
python nb_spark.py input/enron_spark_input.txt 25000
```

```bash
Loading input file input/enron_spark_input.txt ...
        Total number of emails: 5172                                            
        Total number of spam emails: 1500
        Total number of ham emails: 3672
Hashing words into features ...
Labeling features ...
Splitting data into training and testing sets ...
Training the model ...
Evaluating the model ...  
model accuracy: 0.9797979797979798                                              

real    0m11.700s
user    0m0.845s
sys     0m0.536s
```

##### 50000 Features
```bash
python nb_spark.py input/enron_spark_input.txt 50000
```

```bash
Loading input file input/enron_spark_input.txt ...
        Total number of emails: 5172                                            
        Total number of spam emails: 1500
        Total number of ham emails: 3672
Hashing words into features ...
Labeling features ...
Splitting data into training and testing sets ...
Training the model ...
Evaluating the model ... 
model accuracy: 0.9809428284854563                                              

real    0m12.413s
user    0m0.988s
sys     0m0.516s
```
### MRJob
#### Preprocessing
This will process the enron1 dataset into a simpler format for MRJob. Two files
will be created: **enron_mrjob_training.txt** and **enron_mrjob_test.txt**. The 
(training / test) split is **(80 / 20)**.

```bash
python preprocess_enron.py
```

#### Training
This will create the training data to be used in the classifier job.

```bash
python nb_train_mrjob.py input/enron_mrjob_train.txt > training.json
```

#### Classifying
This will classify the given input text based on the training data.

```bash
python nb_classify_mrjob.py input/enron_mrjob_test.txt --training_data=training.json > results.json
```

#### Evaluating
This will compute statistics for the results, comparing against the input.

**Note**: This assumes the output is named **results.json** (for now).

```bash
python evaluate.py input/enron_mrjob_test.txt
```
##### Enron1 Dataset Local
```bash
1: [300, 301]
0: [735, 734]
true-spam: 287
false-spam: 14
true-ham: 721
false-ham: 13
accuracy: 0.9739130434782609
precision: 0.9534883720930233
recall: 0.9566666666666667
f-measure: 0.9550748752079866
```
##### First Implementation (Kaggle Dataset)
```bash
Results Summary:
1: [747, 904]
0: [4823, 4666]
true-spam: 729
false-spam: 175
true-ham: 4648
false-ham: 18
accuracy: 0.9653500897666069
precision: 0.8064159292035398
recall: 0.9759036144578314
f-measure: 0.8831011508176863
```

##### Laplace Smoothing
```bash
Results Summary:
1: [747, 846]
0: [4823, 4724]
true-spam: 717
false-spam: 129
true-ham: 4694
false-ham: 30
accuracy: 0.9714542190305206
precision: 0.8475177304964538
recall: 0.9598393574297188
f-measure: 0.9001883239171374
```

##### Underflow Prevention
```bash
Results Summary:
1: [747, 844]
0: [4823, 4726]
true-spam: 719
false-spam: 125
true-ham: 4698
false-ham: 28
accuracy: 0.9725314183123878
precision: 0.8518957345971564
recall: 0.9625167336010709
f-measure: 0.9038340666247643
```
