PROGRAM_NAME=wordcount.py
CLUSTER=cluster-5455
BUCKET_NAME=cs660-saffat

INPUT_FOLDER=gs://${BUCKET_NAME}/input
OUTPUT_FOLDER=gs://${BUCKET_NAME}/output

# HOW TO MAKE A BUCKET:		https://cloud.google.com/storage/docs/creating-buckets
# HOW TO MAKE A CLUSTER:	https://cloud.google.com/dataproc/docs/tutorials/jupyter-notebook
#
# USAGE:
# make run CLUSTER=cluster-5455 \
	# BUCKET_NAME=cs660-saffat \
	# PROGRAM_NAME=wordcount.py

run:
	gcloud dataproc jobs submit pyspark ${PROGRAM_NAME} \
		--cluster=${CLUSTER} \
		-- ${INPUT_FOLDER} ${OUTPUT_FOLDER}

view:
	@echo Signficant output can be seen at:
	@gsutil ls ${OUTPUT_FOLDER}/**/part*

setup:
	@echo Copying over spam/ and ham/ folders
	gsutil cp ham/* ${INPUT_FOLDER}/
	@echo Copied all contents of ${PWD}/ham  to ${INPUT_FOLDER}/ham
	gsutil cp spam/* ${INPUT_FOLDER}/
	@echo Copied all contents of ${PWD}/spam to ${INPUT_FOLDER}/spam

clean:
	@echo Deleting all input/output contents in ${BUCKET_NAME}
	-gsutil rm ${INPUT_FOLDER}/**
	-gsutil rm ${OUTPUT_FOLDER}/**
