# All our targets are phony (no files to check), so performance should increase if implicit rule search is skipped.
.PHONY: tests

tests:
	./bin/run_tests.sh
