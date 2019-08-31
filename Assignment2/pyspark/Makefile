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
