# Usage
### MRJob
#### Preprocessing
This will process the spam.csv into a format appropriate for mrjob. The resulting 
file will be named **input.txt**.

```bash
python preprocess_mrjob.py spam.csv
```

#### Training
This will create the training data to be used in the classifier job.

```bash
python nb_train_mrjob.py input/input.txt > training.json
```

#### Classifying
This will classify the given input text based on the training data.

```bash
python nb_classify_mrjob.py input/input.txt --training_data=training.json > results.json
```

#### Evaluating
This will compute statistics for the results, comparing against the input.

**Note**: Training data *should* be split into (training, test); for this demonstration 
it has not been split.

**Note**: This assumes the input is named **input/input.txt** and the output is named 
**results.json** (for now).

```bash
python evaluate.py
```

##### First Implementation
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