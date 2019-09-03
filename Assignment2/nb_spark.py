from pyspark.mllib.classification import NaiveBayes
from pyspark.mllib.feature import HashingTF
from pyspark.mllib.regression import LabeledPoint
from pyspark.shell import sc

if __name__ == "__main__":
    # load input files
    print("Loading input file ...")
    emails = sc.textFile("./input/enron_spark_input.txt")

    print("\tTotal number of emails: %i" % emails.count())

    spam_rdd = emails.filter(lambda x: int(x.split("\t")[0]) == 1)
    spam = spam_rdd.map(lambda x: x.split("\t")[1])
    ham_rdd = emails.filter(lambda x: int(x.split("\t")[0]) == 0)
    ham = ham_rdd.map(lambda x: x.split("\t")[1])

    print("\tTotal number of spam emails: %i" % spam.count())
    print("\tTotal number of ham emails: %i" % ham.count())

    # hash words
    print("Hashing words into features ...")
    tf = HashingTF(numFeatures=5000)
    spam_features = spam.map(lambda email: tf.transform(email.split(" ")))
    ham_features = ham.map(lambda email: tf.transform(email.split(" ")))

    # label the features
    print("Labeling features ...")
    spam_samples = spam_features.map(lambda features: LabeledPoint(1, features))
    ham_samples = ham_features.map(lambda features: LabeledPoint(0, features))

    # split the data into [training, test]
    print("Splitting data into training and testing sets ...")
    samples = spam_samples.union(ham_samples)
    [training_data, test_data] = samples.randomSplit([0.8, 0.2])
    training_data.cache()
    test_data.cache()

    # train the model
    print("Training the model ...")
    model = NaiveBayes.train(training_data, 1.0)

    # evaluate the model
    print("Evaluating the model ...")
    prediction_and_label = test_data.map(lambda p: (model.predict(p.features), p.label))
    accuracy = 1.0 * prediction_and_label.filter(lambda pl: pl[0] == pl[1]).count() / test_data.count()
    print("model accuracy: %s" % accuracy)
