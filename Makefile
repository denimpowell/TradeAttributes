
.DEFAULT_GOAL = build
APP_NAME = "trade_attributes"


# Runs the development appplication.  Assumes a local app_files directory with input file present
run:
	PYTHONPATH=src python3 src/trade_attributes.py ./app_files


# Runs the tests, you must have pytest package installed
run_tests:
	PYTHONPATH=src python3 -m pytest -s test


# Builds the deployable image
build:
	docker build --tag $(APP_NAME) .


# Example of running the application in production, using the same input file from the test
# The generated file will be placed in the ./app_files directory upon completion
demo: clean run_tests
	rm ./app_files/output.csv
	docker run -v `pwd`/app_files:/app_files $(APP_NAME)
	cat ./app_files/output.csv

# Sudo on the clean, as demo target leaves a file created by root (docker)
clean:
	sudo rm -rf ./app_files
