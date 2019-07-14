SCRIPT=../Lab2/Part2/letter_freq.py

run: download time_normal time_copy time_dataproc_default time_dataproc_8_2 time_dataproc_4_4

download:
	python3 main.py $(COPIES)

time_normal:
	time python3 $(SCRIPT) sampleBook.txt

time_copy:
	time python3 $(SCRIPT) ${COPIES}_sampleBook.txt

time_dataproc_default:
	time python3 $(SCRIPT) -r dataproc ${COPIES}_sampleBook.txt

time_dataproc_8_2:
	time python3 $(SCRIPT) -r dataproc ${COPIES}_sampleBook.txt --instance-type n1-highcpu-8 --num-core-instances 2

time_dataproc_4_4:
	time python3 $(SCRIPT) -r dataproc ${COPIES}_sampleBook.txt --instance-type n1-highcpu-4 --num-core-instances 4
