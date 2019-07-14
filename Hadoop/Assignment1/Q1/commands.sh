chmod +x mapper.py
chmod +x reducer.py

hdfs dfs -rm -r output

hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar -files mapper.py,reducer.py -input input/romeo-and-juliet.txt -output output -mapper 'mapper.py' -reducer 'reducer.py'

hdfs dfs -cat output/part-00000
