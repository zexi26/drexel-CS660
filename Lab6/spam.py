"""
# CS660 Lab 6 (Spam Detector)

## Collaborators
- Evan Lavender
- Merlin Cherian
- Saffat Hasan
- Zexi Yu


# Part 1
<https://en.wikipedia.org/wiki/Naive_Bayes_spam_filtering>

IDK???

# Part 2

### Notes
$P(S) = \frac{25}{100} = \frac{1}{4}$

$P(H) = \frac{75}{100} = \frac{3}{4}$

$P(B | S) = \frac{4}{5}, P(B | H) = \frac{1}{15}$

$P(C | S) = \frac{3}{5}, P(C | H) = \frac{2}{15}$

$P(W | S) = \frac{1}{5}, P(W | H) = \frac{6}{15}$

### Calculations
$ P(S | B, C) = \frac{P(B, C | S)P(S)}{P(B, C | S)P(S) + P(B, C | H)P(H)} = $
$ \frac{\frac{4}{5}\frac{3}{5}\frac{1}{4}}{\frac{4}{5}\frac{3}{5}\frac{1}{4} + \frac{1}{15}\frac{2}{15}\frac{3}{4}} = $
$ \frac{\frac{3}{25}}{\frac{19}{150}} =  \frac{18}{19} \approx \mathbf{0.947} $

$ P(S | B) = \frac{P(B | S)P(S)}{P(B | S)P(S) + P(B | H)P(H)} = $
$ \frac{\frac{4}{5}\frac{1}{4}}{\frac{4}{5}\frac{1}{4} + \frac{1}{15}\frac{3}{4}} = $
$ \frac{\frac{1}{5}}{\frac{1}{4}} = \frac{4}{5} =  \mathbf{0.8} $

$ P(S | B, C, W) = \frac{P(B, C, W | S)P(S)}{P(B, C, W | S)P(S) + P(B, C, W | H)P(H)} = $
$ \frac{\frac{4}{5}\frac{3}{5}\frac{1}{5}\frac{1}{4}}{\frac{4}{5}\frac{3}{5}\frac{1}{5}\frac{1}{4} + \frac{1}{15}\frac{2}{15}\frac{6}{15}\frac{3}{4}} = $
$ \frac{\frac{3}{125}}{\frac{2}{75}} = \frac{9}{10} = \mathbf{0.9} $

### Comparison
The addition of the word "CHEAP" to the email containing "BUY" *increases* the probability of
the email being classified as spam spam. Both words have a high individual probability of being present in a spam email,
therefore it is intuitive that the two of them together results in an increased spam classification probability.

Conversely, the addition of the word "WORK" *decreases* the probability. The simple explanation is that because
"WORK" appears in a higher number of *non-spam* emails, its presence *decreases* the probability of the email being spam.

# Part 3

### Building a SPAM filter using Naive Bayes
#### What is the problem? (Spam or not Spam: that is the question)
The problem of determining whether an email is spam or *not* spam is a categorization/classification problem.
Given an email (instance), and a set of categories: {"spam", "not spam"}, how can we determine what category the
email belongs to?

#### Bayesian Methods for Classification
We can use **Bayes theorem** to build a **generative model** that approximates how data is produced.

$$  P(C | X) = \frac{P(X | C) P(C)}{P(X)} $$

Because we only need the most probable category, we can simplify this to:

$$ argmax_{c \in C} \text{ } P(X | c) P(c) $$

If we assume all hypotheses are *a priori* equally likely, we must only consider
the $P(X | c)$ term.

#### Learning the Model
Thanks to the Naive Bayes Conditional Independence Assumption, we can use the following
simplification:

$$ P(x_i, x_2, ..., x_n | c_j) = \prod_{i} P(x_i | c_j) $$

Given a set of training data (emails) of size $N$, where $count(X=x)$ is the number
of emails for which $X=x$, e.g. spam=true. For each category $c$ and each value $x$
for a variable $X$

$ P(c) = \frac{count(C = c)}{|N|} $

$ P(x | c) = \frac{count(X = x, C = c)}{count(C = c)} $

In other words, the probability of an email belonging to a certain category is equal
to the total number of emails with that category, divided by the total number of
training emails. The second equation can be intuited as the probability of a word
showing up in an email, knowing that the email belongs to category $c$, is equal to
the total count of that word among emails with that category, divided by the total
number of training emails with that category.

With training, we calculate the **prior probability** of each word belonging to a
category (spam or not-spam). There exists a problem with this though.

#### Overfitting
What if the training data is not adequate; it may be missing a case. Zero probabilities
overwhelm any other evidence. To fix this, we modify the $P(x | c)$ equation above
to:

$ P(x | c) = \frac{count(X = x, C = c) + 1}{count(C = c) + |X|} $

#### Underflow
Multiplying lots of probabilities can result in floating-point underflow. For this,
we can take advantage of a property of the $\log$ function: $\log(xy) = \log(x) + \log(y) $.
So, we take the $\log$ of each probability and *sum* them together instead of multiply.

# Part 4
"""
from operator import add
from random import random

import handout
from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()

doc = handout.Handout("handout")

"""## Word Count"""

lines = spark.read.text("./input/words.txt").rdd.map(lambda r: r[0])
counts = lines.flatMap(lambda x: x.split(" ")).map(lambda x: (x, 1)).reduceByKey(add)

output = counts.collect()

for word, count in output:
    doc.add_text("%s: %i" % (word, count))
doc.show()

"""## Pi Estimation"""

partitions = 2
n = 1000000 * partitions


def f(_):
    x = random() * 2 - 1
    y = random() * 2 - 1
    return 1 if x ** 2 + y ** 2 <= 1 else 0


count = spark.sparkContext.parallelize(range(1, n + 1), partitions).map(f).reduce(add)
doc.add_text("Pi is roughly %f" % (4.0 * count / n))
doc.show()

spark.stop()
