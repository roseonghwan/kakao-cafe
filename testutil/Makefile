PYTHON = python3
TEST_MODULE = unittest
RM = rm -rf
CACHE = __pycache__/

all: test

test:
	$(PYTHON) -m $(TEST_MODULE) ./...

test cafemenu:
	$(PYTHON) -m $(TEST_MODULE) testCafeMenu.py

test smoothie:
	$(PYTHON) -m $(TEST_MODULE) testSmoothie.py

clean: $(CACHE)
	$(RM) $(CACHE)
