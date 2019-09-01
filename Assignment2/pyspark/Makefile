PROGRAM_NAME=naive_bayes_classifier.py
CLUSTER=cluster-5455
BUCKET_NAME=cs660-saffat
PYTHON=/usr/bin/python3

# File name from data set
DATA_SET=enron1
DATA_FILE=${DATA_SET}.tar.gz
DATA_URL=http://www.aueb.gr/users/ion/data/enron-spam/preprocessed/${DATA_FILE}

# Local Variables
LOCAL_INPUT_FOLDER=${PWD}/input
LOCAL_SPAM_FOLDER=${LOCAL_INPUT_FOLDER}/spam
LOCAL_HAM_FOLDER=${LOCAL_INPUT_FOLDER}/ham
LOCAL_OUTPUT_FOLDER=${PWD}/output

# Google Storage Variables
GS_INPUT_FOLDER=gs://${BUCKET_NAME}/input
GS_SPAM_FOLDER=${GS_INPUT_FOLDER}/spam
GS_HAM_FOLDER=${GS_INPUT_FOLDER}/ham
GS_OUTPUT_FOLDER=gs://${BUCKET_NAME}/output

# HOW TO MAKE A BUCKET:		https://cloud.google.com/storage/docs/creating-buckets
# HOW TO MAKE A CLUSTER:	https://cloud.google.com/dataproc/docs/tutorials/jupyter-notebook
#
# Common Errors:
# 	"Failed to import PySpark" -> pip3 install pyspark
# 	"JAVA_HOME is not set" -> sudo apt-get install default-jre
#
# USAGE:
# make run CLUSTER=cluster-5455 \
	# BUCKET_NAME=cs660-saffat \
	# PROGRAM_NAME=wordcount.py

.PHONY=all local-run local-clean run view setup clean

local-all: local-clean local-setup local-run

local-run:
	PYSPARK_DRIVER_PYTHON=${PYTHON} PYSPARK_PYTHON=${PYTHON} ${PYTHON} ${PROGRAM_NAME} ${LOCAL_INPUT_FOLDER} ${LOCAL_OUTPUT_FOLDER}

local-setup:
	# Get the data tar.gz
	wget ${DATA_URL}
	# Untar it to enron1/ (DATA_SET)
	tar -xf ${DATA_FILE}
	# Create folders we will copy to
	mkdir -p ${LOCAL_SPAM_FOLDER} ${LOCAL_HAM_FOLDER} ${LOCAL_OUTPUT_FOLDER}
	# Move files from enron1/[sp|h]am to input/[sp|h]am
	mv ${DATA_SET}/ham/* ${LOCAL_HAM_FOLDER}
	mv ${DATA_SET}/spam/* ${LOCAL_SPAM_FOLDER}
	rm -rf ${DATA_SET} ${DATA_FILE}

local-clean:
	rm -rf ${LOCAL_HAM_FOLDER} ${LOCAL_SPAM_FOLDER} ${LOCAL_OUTPUT_FOLDER} ${DATA_FILE}*

all: clean setup run

run:
	gcloud dataproc jobs submit pyspark ${PROGRAM_NAME} \
		--cluster=${CLUSTER} \
		-- ${GS_INPUT_FOLDER} ${GS_OUTPUT_FOLDER}

view:
	@echo Signficant output can be seen at:
	@gsutil ls ${GS_OUTPUT_FOLDER}/**/part*

setup: local-setup
	@echo Copying over spam/ and ham/ folders
	gsutil -m cp input/ham/* ${GS_INPUT_FOLDER}/
	@echo Copied all contents of ${PWD}/ham  to ${GS_INPUT_FOLDER}/ham
	gsutil -m cp input/spam/* ${GS_INPUT_FOLDER}/
	@echo Copied all contents of ${PWD}/spam to ${GS_INPUT_FOLDER}/spam

clean:
	@echo Deleting all input/output contents in ${BUCKET_NAME}
	-gsutil -m rm ${GS_INPUT_FOLDER}/**
	-gsutil -m rm ${GS_OUTPUT_FOLDER}/**
