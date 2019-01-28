hadoop fs -rm -r /user/hadoop/trade/trade-output # to remove existing results
hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
-file ./mapper_rdf.py    -mapper ./mapper_rdf.py \
-file ./reducer_rdf.py   -reducer ./reducer_rdf.py \
-input /user/hadoop/trade/data/* -output /user/hadoop/trade/trade-output
