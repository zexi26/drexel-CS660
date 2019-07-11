INPUT_FILE=sampleBook.txt
DOWNLOAD_LINK=http://www.gutenberg.org/files/2600/2600-0.txt
NUM_COPIES=1000
N_COPIES_FILE=$(NUM_COPIES)_$(INPUT_FILE)
SCRIPT=../Lab2/Part2/letter_freq.py

run: download copy time_normal time_copy

download:
	wget $(DOWNLOAD_LINK) -O $(INPUT_FILE)

copy:
	for i in {1..$(NUM_COPIES)}; do cat $(INPUT_FILE) >> $(N_COPIES_FILE); done

time_normal:
	time python3 $(SCRIPT) $(INPUT_FILE)

time_copy:
	time python3 $(SCRIPT) $(N_COPIES_FILE)
