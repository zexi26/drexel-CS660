SCRIPT=../Lab2/Part2/letter_freq.py

run: download time_normal time_copy

download:
	python3 main.py $(COPIES)

time_normal:
	time python3 $(SCRIPT) sampleBook.txt

time_copy:
	time python3 $(SCRIPT) ${COPIES}_sampleBook.txt
