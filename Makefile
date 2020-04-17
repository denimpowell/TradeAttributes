
.DEFAULT_GOAL = run_tests



# Runs the development appplication.
# These local run targets assume you have an activated virtualenv with pip.requirements.txt installed
run:
	PYTHONPATH=src python3 src/trade_attributes.py


# Runs the tests, you must have pytest package installed
run_tests:
	PYTHONPATH=src python3 -m pytest -s test