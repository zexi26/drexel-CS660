# CS 660 Lab 4
## Collaborators
- Evan Lavender
- Merlin Cherian
- Saffat Hasan
- Zexi Yu

## Usage
```bash
python3 inverted_index.py input/
```

# Google Cloud Runs
Input - 98 books from gutenberg

#### Baseline implementation from section 4.3 with sorting in reducer.
```bash
python3 inverted_index_bl.py -r dataproc guten1/* 
  17 min 23 sec
  
python3 inverted_index_bl.py -r dataproc guten1/* --instance-type n1-standard-2 --num-core-instances 7
  4 min 9 sec
  
python3 inverted_index_bl.py -r dataproc guten1/* --instance-type n1-highcpu-4 --num-core-instances 5
  2 min 45 sec	
  
python3 inverted_index_bl.py -r dataproc guten1/* --instance-type n1-highcpu-8 --num-core-instances 2
  2 min 30 sec	
```
#### Revised implementation from section 4.4 using SORT_VALUES instead of value-to-key conversion.
```bash
python3 inverted_index_rev.py -r dataproc guten1/*
```

#### Revised implementation that uses ```mapper_raw``` to read entire file.
```bash
python3 inverted_index_raw.py -r dataproc guten1/*
```
