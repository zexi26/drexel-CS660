# CS660 Assignment 2
## Collaborators
- Evan Lavender
- Merlin Cherian
- Saffat Hasan
- Zexi Yu

## Usage
### Spark
#### Preprocessing
This will process the enron1 dataset into a simpler format for Spark. The output 
file created will be **enron_spark_input.txt**.
```bash
python preprocess_spark.py
```

#### Training & Evaluating

num_features | accuracy
------------ | --------
100    | 0.8353293413173652
1000   | 0.8942486085343229
5000   | 0.9520153550863724
10000  | 0.9601634320735445
25000  | 0.9797979797979798
50000  | 0.9809428284854563
75000  | 0.9853717388025939
100000 | 0.9887268901247558
125000 | 0.9859302499625805

#### Conclusion
The Enron spam dataset was preprocessed to create a single input file. Each line consists of the classification 
(1 for spam, 0 for ham) and the contents of the email, separated by a tab (\\t) character. Increasing the number of 
features used in the classification seems to directly increase accuracy, but only until a certain point. Runtime was 
fairly consistent at ~12 sec.

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

```bash
real    0m5.678s
user    0m5.912s
sys     0m0.752s
```

#### Classifying
This will classify the given input text based on the training data.

```bash
python nb_classify_mrjob.py input/enron_mrjob_test.txt --training_data=training.json > results.json
```

```bash
real    0m3.076s
user    0m3.303s
sys     0m0.795s
```

#### Evaluating
This will compute statistics for the results, comparing against the input.

**Note**: This assumes the output is named **results.json** (for now).

```bash
python evaluate.py input/enron_mrjob_test.txt
```

```bash
Results Summary:
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

real    0m0.050s
user    0m0.048s
sys     0m0.000s
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

#### Conclusion
The Enron spam dataset was preprocessed to create a single input file. Each line consists of the classification 
(1 for spam, 0 for ham) and the contents of the email, separated by a tab (\\t) character. Included with each category 
is an id generated for the document. This is used for evaluation afterwards. 

The training job outputs the document count, token count, and token frequency for each category. The classifying job 
outputs a document id and the classification for the document. An evaluator script can then compare the output with the 
input to determine accuracy. 
