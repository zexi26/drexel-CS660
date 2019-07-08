K_MOST_FREQ_WORDS=10
JOB_OUTPUT_FILE=job_output.log
INPUT_FILE=input/walden.txt

letters:
	python letter_freq.py $(INPUT_FILE)

words:
	python word_freq.py $(INPUT_FILE)

k_words:
	@echo Running word_freq on $(INPUT_FILE) with output file $(JOB_OUTPUT_FILE)
	python word_freq.py $(INPUT_FILE) > $(JOB_OUTPUT_FILE)
	@echo Showing the $(K_MOST_FREQ_WORDS) most common words in $(JOB_OUTPUT_FILE)
	sort -rn -k2 $(JOB_OUTPUT_FILE) | head -n $(K_MOST_FREQ_WORDS)