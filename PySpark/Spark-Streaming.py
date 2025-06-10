Spark Streaming:
Spark Streaming is enables processing of real-time streaming data using the same Spark API used for batch processing.

💡 Key Concepts:
                                                                                               
Micro-Batch Processing:
Spark Streaming breaks incoming data into small batches (e.g., every 1 second), processes each batch using Spark jobs, and outputs the results.

DStreams (Discretized Streams):
The basic abstraction in Spark Streaming. A DStream is a continuous stream of data divided into small batches.

Input Sources:
It can read real-time data from:

Kafka

Flume

Kinesis

TCP sockets

HDFS, S3, etc.

Output Sinks:
Results can be saved to:

File systems

Databases

Kafka

Dashboards

🛠️ Example: Reading from socket

from pyspark import SparkContext
from pyspark.streaming import StreamingContext

sc = SparkContext("local[2]", "NetworkWordCount")
ssc = StreamingContext(sc, 1)  # batch interval = 1 second

lines = ssc.socketTextStream("localhost", 9999)
words = lines.flatMap(lambda line: line.split(" "))
word_counts = words.map(lambda word: (word, 1)).reduceByKey(lambda a, b: a + b)

word_counts.pprint()

ssc.start()
ssc.awaitTermination()
✅ Use Cases:
Real-time analytics dashboards

Fraud detection

Log monitoring

Clickstream analysis

Sensor data processing (IoT)

🔁 Alternative to Spark Streaming (Structured Streaming)
Apache Spark now recommends Structured Streaming, a newer, more powerful, and unified API for streaming that works with DataFrames.

Would you like a quick comparison between Spark Streaming and Structured Streaming?
