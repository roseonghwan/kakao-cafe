TEST_PATH = ./

test:
	python3 -m unittest test.py

run:
	python3 main.py

clean:
	rm -rf __pycache__/
