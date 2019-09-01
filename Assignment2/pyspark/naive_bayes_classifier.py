#!/usr/bin/env python

# Currently based off https://github.com/juliensimon/dlnotebooks/blob/master/spark/spam-classifier/01%20-%20Spam%20classifier.ipynb
# Will need to be adapted to fit the dataproc framework

import pyspark
import sys
import numpy
from pyspark.mllib.regression import LabeledPoint
from pyspark.mllib.feature import HashingTF
from pyspark.mllib.classification import NaiveBayes

if len(sys.argv) != 3:
  raise Exception("Exactly 2 arguments are required: <inputUri> <outputUri>")

inputUri=sys.argv[1]
outputUri=sys.argv[2]

sc = pyspark.SparkContext()

log4jLogger = sc._jvm.org.apache.log4j
log = log4jLogger.LogManager.getLogger(__name__)
log.warn("Hello World!")

spamInputFolder = inputUri + "/spam"
hamInputFolder = inputUri + "/ham"

spam = sc.textFile(spamInputFolder)
ham = sc.textFile(hamInputFolder)

spamWords = spam.map(lambda email: email.split())
hamWords = ham.map(lambda email: email.split())

# Save items as text files
spamWords.saveAsTextFile(sys.argv[2] + "/spam_output")
hamWords.saveAsTextFile(sys.argv[2] + "/ham_output")

# Create a HashingTF instance to map email text to vectors of features.
tf = HashingTF(numFeatures = 200)
spamFeatures = tf.transform(spamWords)
hamFeatures = tf.transform(hamWords)

# Create LabeledPoint datasets for positive (spam) and negative (ham) examples.
spamSamples = spamFeatures.map(lambda features:LabeledPoint(1, features))
hamSamples = hamFeatures.map(lambda features:LabeledPoint(0, features))

# Split the data set 80/20
samples = spamSamples.union(hamSamples)
[training_data, test_data] = samples.randomSplit([0.8, 0.2])
training_data.cache()
test_data.cache()


def score(model):
    predictions = model.predict(test_data.map(lambda x: x.features))
    labels_and_preds = test_data.map(lambda x: x.label).zip(predictions)
    accuracy = labels_and_preds.filter(lambda x: x[0] == x[1]).count() / float(test_data.count())
    return accuracy

algo = NaiveBayes()
model = algo.train(training_data)

print(score(model))

