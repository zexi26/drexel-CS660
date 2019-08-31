PROGRAM_NAME=wordcount.py
CLUSTER=cluster-5455
BUCKET_NAME=cs660-saffat

# USAGE:
# make run CLUSTER=cluster-5455 \
	# BUCKET_NAME=cs660-saffat \
	# PROGRAM_NAME=wordcount.py
#

run:
	gcloud dataproc jobs submit pyspark ${PROGRAM_NAME} \
		--cluster=${CLUSTER} \
		-- gs://${BUCKET_NAME}/input/ gs://${BUCKET_NAME}/output

setup:
	@echo Copying over spam/ and ham/ folders
	gsutil cp ham/*  gs://${BUCKET_NAME}/input/
	@echo Copied all contents of ${PWD}/ham  to gs://${BUCKET_NAME}/input/ham
	gsutil cp spam/* gs://${BUCKET_NAME}/input/
	@echo Copied all contents of ${PWD}/spam to gs://${BUCKET_NAME}/input/spam

clean:
	@echo Deleting all contents in ${BUCKET_NAME}...
	-gsutil rm gs://${BUCKET_NAME}/**
