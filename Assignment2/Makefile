# Performs MrJob tasks

all: preprocess train classify evaluate

preprocess:
	$(MAKE) -C input/ all

train:
	python nb_train_mrjob.py input/enron_mrjob_train.txt > training.json

classify:
	python nb_classify_mrjob.py input/enron_mrjob_test.txt --training_data=training.json > results.json

evaluate:
	python evaluate.py input/enron_mrjob_test.txt

clean:
	$(MAKE) -C input/ clean
