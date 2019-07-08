K_MOST_FREQ_WORDS=10
JOB_OUTPUT_FILE=job_output.log

letters:
	python letter_freq.py input/walden.txt

words:
	python word_freq.py input/walden.txt

k_words:
	@echo Running word_freq on input/walden.txt with output file $(JOB_OUTPUT_FILE)
	python word_freq.py input/walden.txt > $(JOB_OUTPUT_FILE)
	@echo Showing the $(K_MOST_FREQ_WORDS) most common words in $(JOB_OUTPUT_FILE)
	sort -rn -k2 $(JOB_OUTPUT_FILE) | head -n $(K_MOST_FREQ_WORDS)