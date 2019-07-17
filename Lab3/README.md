# CS 660 Lab 3
## Collaborators
- Evan Lavender
- Merlin Cherian
- Saffat Hasan
- Zexi Yu

# Overview


# Part 1
Summary for GFS Paper
1. Read Google File System Paper
2. Read Chapter 3 of “Hadoop the Definitive Guide” on HDFS
3. Prepare summary of the paper including
    1. 10-15 slides with notes
    2. Contribution
    3. Problem and Assumptions
    4. Overview (Design and Implementation)
    5. Performance Summary 

# Part 2
4. Get Google Cloud coupon, logon and explore:
    
    4. Create a VM (default machine with Debian GNU/Linux) – allow http. ssh into the machine and verify python3 works
    
    5. Install pip and mrjob
        ```python
        sudo apt-get install python-pip3
        pip3 install mrjob
        ```
    6. upload mrjob program and input and verify that it works. Time the execution and compare to equivalent python program
        ```bash
        time python3 letter_freq.py sampleBook.txt
        ```
	
      - Output: logs/letter_freq_local.log	logs/letter_freq_vm.log
      - Run time comparison:
      
      		vm: real 27.973s	user 27.696s	sys 0.240s
	  		local: real 30.898s   	user 30.149s    sys 0.451s
        
    7. Create storage bucket in Google storage and upload input file from (6), note time compared to uploading in 6.
    
      - Output: logs/vm_upload.log	logs/cloud_upload.log
      - Run time comparison:
      
      		vm :   real 6.425s	  user 0.600s	sys 0.351s
      		cloud: real  6.354s       user 0.741s   sys 0.471s
      
    8. Use gsutil from VM to copy file from Google storage
        ```python
        gsutil cp gs://my-bucket/sampleBook.txt .
        ```
    9. Create python script to create a large input for (6) by appending a bunch of copies of the input you used in (6). Time MRJob on the larger input.
	- Refer to main.py 
	- Output: logs/output.log
	- Usage example:
        ```bash
        make COPIES=20 run
        ```
	
# Part 3
5. Create a Hadoop cluster using dataproc – see instructions in MRJob documentation

    1. Create python script to create a large input for (4.6) by appending a bunch of copies of the input you used in (4.6). Time MRJob on the larger input.
        ```
        python3 ../Lab2/Part2/letter_freq.py -r dataproc 25_sampleBook.txt
        ```
	- Output: logs/default_25copies.log
	- Runtime: 18:50
    2. Explore different parameter settings and see how they affect the runtime
        ```
        python3 ../Lab2/Part2/letter_freq.py -r dataproc 25_sampleBook.txt --instance-type n1-standard-2 --num-core-instances 7
        ```
	- Output: logs/2cpu7inst_25copies.log
	- Runtime: 07:56
	
        ```
        python3 ../Lab2/Part2/letter_freq.py -r dataproc 25_sampleBook.txt --instance-type n1-highcpu-4 --num-core-instances 5
        ```
	- Output: logs/4cpu5inst_25copies.log
	- Runtime: 03:42
	
        ```
        python3 ../Lab2/Part2/letter_freq.py -r dataproc 25_sampleBook.txt --instance-type n1-highcpu-8 --num-core-instances 2
        ```
	- Output: logs/8cpu2inst_25copies.log
	- Runtime: 02:56


    
    
   

