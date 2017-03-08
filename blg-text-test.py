from pyspark.ml.classification import LogisticRegression
from pyspark.ml.linalg import Vectors
from pyspark.sql import Row, SparkSession
from pprint import pprint
import random
import utils

# todo: percentage of punctuation that is exclamation points

spark = SparkSession.builder.appName("Binomial logistic regression - Noise Test").getOrCreate()

def random_loud_and_quiet_string(n = 100):
    percent_uppercase = random.random()
    noise_level = 1.0 if percent_uppercase > 0.1 else 0.0
    s = utils.random_case_string(percent_uppercase, n)
    return (s, noise_level, Vectors.dense(percent_uppercase))

def random_loud_and_quiet_strings(n = 100):
    return [random_loud_and_quiet_string() for _ in range(n)]

data = random_loud_and_quiet_strings(1000)

training = spark.createDataFrame(data, ["text", "label", "features"])

lr = LogisticRegression()

lrModel = lr.fit(training)

testDataStrings = [
    "Don't let the FAKE NEWS tell you that there is big infighting in the Trump Admin.",
    "This is your most unconvincing Tweet to date. Oh, and we're back on the FAKE NEWS trail to deflect. So predictable. So SAD!",
    "Paul Ryan literally cannot help but laugh at you live on television when you speak nonsense.",
    "A Tweet desperately trying to convince the world you're all getting along with each other fools nobody, 45."
]

testDataTuples = [utils.percent_upper_case(s) for s in testDataStrings]

testData = [(s, Vectors.dense(percentUpper)) for s, percentUpper in testDataTuples]

testDataFrame = spark.createDataFrame(testData, ["text", "features"])

predictions = lrModel.transform(testDataFrame)

predictions.show(n=100, truncate=False)
