# Spark
instance-type | num-core-instances | time| accuracy
------------- | ------------------ | ----| --------
default       | default  | 46.230 sec   | 92.77%
n1-standard-2 | 7        | 46.039 sec   | 93.10%
n1-highcpu-4  | 5        | 44.525 sec   | 93.31%
n1-highcpu-8  | 2        | 43.680 sec   | 93.48%

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
