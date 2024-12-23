.PHONY: lock, quality, tests

#Target to invoke the poetry lock process
lock:
	@echo "Starting poetry lock process..."
	@python3 -m pip install -q poetry==1.8.5
	@poetry lock

help:
	@echo "Help to use"

clean:
	@rm *.csv