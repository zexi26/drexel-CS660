K_MOST_FREQ_WORDS=10
JOB_OUTPUT_FILE=_output.log
INPUT_FILE=input/walden.txt

.PHONY: all letters words k_words

all: letter_freq word_count_sort k_words

letter_freq:
	@echo "============================="
	@echo Running letter_freq.py on $(INPUT_FILE)
	@echo Job output placed in $@$(JOB_OUTPUT_FILE)
	@echo "============================="
	python letter_freq.py $(INPUT_FILE) > $@$(JOB_OUTPUT_FILE)
	@echo "============================="
	@echo

word_count_sort:
	@echo "============================="
	@echo Running word_count_sort.py on $(INPUT_FILE)
	@echo Job output placed in $@$(JOB_OUTPUT_FILE)
	@echo "============================="
	python word_count_sort.py $(INPUT_FILE) > $@$(JOB_OUTPUT_FILE)
	@echo "============================="
	@echo

k_words:
	@echo "============================="
	@echo Running k_words.py with k=15 on $(INPUT_FILE)
	@echo Job output placed in $@$(JOB_OUTPUT_FILE)
	@echo "============================="
	python k_words.py $(INPUT_FILE) --k=15 > $@$(JOB_OUTPUT_FILE)
	@echo "============================="
	@echo