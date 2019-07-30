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

- Baseline implementation from section 4.3 with sorting in reducer.
- Revised implementation from section 4.4 using SORT_VALUES instead of value-to-key conversion.
- Revised implementation that uses ```mapper_raw``` to read entire file.

```bash
python3 inverted_index_bl.py -r dataproc guten1/*
```

```bash
python3 inverted_index_rev.py -r dataproc guten1/*
```

```bash
python3 inverted_index_raw.py -r dataproc guten1/*
```
