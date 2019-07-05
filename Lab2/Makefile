run: word-count words

NUM_PARAGRAPHS=1

create-temp-file:
	@echo "Creating temporary file with sample text"
	$(eval tmpfile := $(shell mktemp))
	@curl http://metaphorpsum.com/paragraphs/$(NUM_PARAGRAPHS) > $(tmpfile) 2> /dev/null

word-count: create-temp-file
	@echo "============================="
	@echo "===== RUNNING word-count ===="
	@echo "============================="
	@python3 wc.py    < $(tmpfile) 2> /dev/null
	@echo

words: create-temp-file
	@echo "============================="
	@echo "===== RUNNING words ========="
	@echo "============================="
	@python3 words.py < $(tmpfile) 2> /dev/null
	@echo
