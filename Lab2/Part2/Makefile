K_MOST_FREQ_WORDS=10
JOB_OUTPUT_FILE=_output.log
INPUT_FILE=input/sampleBook.txt
DOWNLOAD_LINK=http://www.gutenberg.org/files/2600/2600-0.txt

.PHONY: all letters words k_words

all: letter_freq word_count_sort k_words

get_input: 
	wget $(DOWNLOAD_LINK) -O $(INPUT_FILE)

letter_freq: get_input
	@echo "============================="
	@echo Running letter_freq.py on $(INPUT_FILE)
	@echo Job output placed in $@$(JOB_OUTPUT_FILE)
	@echo "============================="
	python3 letter_freq.py $(INPUT_FILE) > $@$(JOB_OUTPUT_FILE)
	@echo "============================="
	@echo

word_count_sort: get_input
	@echo "============================="
	@echo Running word_count_sort.py on $(INPUT_FILE)
	@echo Job output placed in $@$(JOB_OUTPUT_FILE)
	@echo "============================="
	python3 word_count_sort.py $(INPUT_FILE) > $@$(JOB_OUTPUT_FILE)
	@echo "============================="
	@echo

k_words: get_input
	@echo "============================="
	@echo Running k_words.py with k=15 on $(INPUT_FILE)
	@echo Job output placed in $@$(JOB_OUTPUT_FILE)
	@echo "============================="
	python3 k_words.py $(INPUT_FILE) --k=15 > $@$(JOB_OUTPUT_FILE)
	@echo "============================="
	@echo
