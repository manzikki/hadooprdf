hadoop fs -rm -r trade-output # to remove existing results
hadoop jar /usr/local/Cellar/hadoop/3.1.0/libexec/share/hadoop/tools/lib/hadoop-streaming-3.1.0.jar \
-file ./mapper_rdf.py    -mapper ./mapper_rdf.py \
-file ./reducer_rdf.py   -reducer ./reducer_rdf.py \
-input trade/* -output trade-output