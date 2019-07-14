chmod +x mapper.py
chmod +x reducer.py

hdfs dfs -rm -r output

hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
-files mapper.py,reducer.py \
-D mapred.reduce.tasks=5 \
-D stream.num.map.output.key.fields=1 \
-D num.key.fields.for.partition=1 \
-D mapred.job.name=sortfile_demo \
-input input/romeo-and-juliet.txt \
-output output -mapper 'mapper.py' -reducer 'reducer.py' \
-partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner

hdfs dfs -ls output/

hdfs dfs -getmerge output/ output.txt

gedit output.txt
