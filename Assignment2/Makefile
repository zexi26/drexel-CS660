# Performs MrJob tasks

.PHONY: all preprocess train classify evaluate clean

all: preprocess train classify evaluate

preprocess:
	$(MAKE) -C input/ all

train:
	time python3 nb_train_mrjob.py input/enron_mrjob_train.txt > training.json

classify:
	time python3 nb_classify_mrjob.py input/enron_mrjob_test.txt --training_data=training.json > results.json

evaluate:
	python3 evaluate.py input/enron_mrjob_test.txt

clean:
	$(MAKE) -C input/ clean
	-rm training.json results.json
