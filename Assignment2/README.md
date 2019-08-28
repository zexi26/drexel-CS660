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

```bash
Results Summary:
1: [747, 904]
0: [4823, 4666]
true-spam: 729
false-spam: 175
true-ham: 4648
false-ham: 18
precision: 0.8064159292035398
recall: 0.9759036144578314
f-measure: 0.8831011508176863
```