.PHONY: install-deps lab2

lab2:
	$(MAKE) -C Lab2 run

install-deps:
	pip3 install -r requirements.txt
