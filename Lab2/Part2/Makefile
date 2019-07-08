K_MOST_FREQ_WORDS=10
JOB_OUTPUT_FILE=_output.log
INPUT_FILE=input/walden.txt

.PHONY: all letters words k_words

all: letters words k_words

letters:
	@echo "============================="
	@echo Running letter_freq.py on $(INPUT_FILE)
	@echo Job output placed in $@$(JOB_OUTPUT_FILE)
	@echo "============================="
	python letter_freq.py $(INPUT_FILE) > $@$(JOB_OUTPUT_FILE)
	@echo "============================="
	@echo

words:
	@echo "============================="
	@echo Running letter_freq.py on $(INPUT_FILE)
	@echo Job output placed in $@$(JOB_OUTPUT_FILE)
	@echo "============================="
	python word_freq.py $(INPUT_FILE) > $@$(JOB_OUTPUT_FILE)
	@echo "============================="
	@echo

k_words:
	@echo "============================="
	@echo Running letter_freq.py on $(INPUT_FILE)
	@echo Job output placed in $@$(JOB_OUTPUT_FILE)
	@echo "============================="
	python word_freq.py $(INPUT_FILE) > $@$(JOB_OUTPUT_FILE)
	@echo Showing the $(K_MOST_FREQ_WORDS) most common words in $@$(JOB_OUTPUT_FILE)
	sort -rn -k2 $@$(JOB_OUTPUT_FILE) | head -n $(K_MOST_FREQ_WORDS)
	@echo "============================="
	@echo