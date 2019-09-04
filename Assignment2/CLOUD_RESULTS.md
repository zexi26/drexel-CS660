# Spark (num_features = 1000)
instance-type | num-core-instances | time| accuracy
------------- | ------------------ | ----| --------
default       | default  | 1 min 13 sec | 92.38%
n1-standard-2 | 7        | 1 min 04 sec  | 92.77%
n1-highcpu-4  | 5        | 0 min 59 sec | 93.09%
n1-highcpu-8  | 2        | 0 min 51 sec | 93.22%


# MRJob
## Train
instance-type | num-core-instances | time
------------- | ------------------ | ----
default       | default  | 4 min 49 sec
n1-standard-2 | 7        | 2 min 33 sec
n1-highcpu-4  | 5        | 1 min 33 sec
n1-highcpu-8  | 2        | 0 min 58 sec

## Classify
instance-type | num-core-instances | time
------------- | ------------------ | ----
default       | default  | 4 min 05 sec
n1-standard-2 | 7        | 2 min 16 sec
n1-highcpu-4  | 5        | 1 min 17 sec
n1-highcpu-8  | 2        | 0 min 49 sec
