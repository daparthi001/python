import findspark
findspark.init()

from pyspark.conf import SparkConf
from pyspark.sql import SparkSession, Row

def loadMovieNames():
    movieNames = {}
    with open("/home/edupy/Desktop/Datasets/ml-100k/u.item") as f:
        for line in f:
            fields = line.split('|')
            movieNames[int(fields[0])] = fields[1]
    return movieNames

# Create a SparkSession
spark = SparkSession.builder.config(conf=SparkConf()).appName("PopularMovies").getOrCreate()

# Load up our movie ID -> name dictionary
nameDict = loadMovieNames()

# Get the raw data
lines = spark.sparkContext.textFile("file:///home/edupy/Desktop/Datasets/ml-100k/u.data")
# Convert it to a RDD of Row objects
movies = lines.map(lambda x: Row(movieID =int(x.split()[1])))
# Convert that to a DataFrame
movieDataset = spark.createDataFrame(movies)

# Some SQL-style magic to sort all movies by popularity in one line!
topMovieIDs = movieDataset.groupBy("movieID").count().orderBy("count", ascending=False).cache()

# Show the results at this point:
topMovieIDs.show()

# Grab the top 10
top10 = topMovieIDs.take(10)

# Print the results
print("\n")
for result in top10:
    # Each row has movieID, count as above.
    print("%s: %d" % (nameDict[result[0]], result[1]))

# Stop the session
spark.stop()
