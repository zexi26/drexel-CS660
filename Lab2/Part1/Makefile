run: word-count words

OUTPUT_FILE_SUFFIX=_output.log
NUM_PARAGRAPHS=1

word-count: create-temp-file
	@echo "============================="
	@echo "===== RUNNING word-count ===="
	@echo "============================="
	@python3 wc.py    < $(tmpfile) 2> /dev/null | tee $@$(OUTPUT_FILE_SUFFIX)
	@echo
	@echo Output placed in $@$(OUTPUT_FILE_SUFFIX)
	@echo

words: create-temp-file
	@echo "============================="
	@echo "===== RUNNING words ========="
	@echo "============================="
	@python3 words.py < $(tmpfile) 2> /dev/null | tee $@$(OUTPUT_FILE_SUFFIX)
	@echol
	@echo Output placed in $@$(OUTPUT_FILE_SUFFIX)
	@echo

create-temp-file:
	@echo "Creating temporary file with sample text"
	$(eval tmpfile := $(shell mktemp))
	@curl http://metaphorpsum.com/paragraphs/$(NUM_PARAGRAPHS) > $(tmpfile) 2> /dev/null
