PY = python
PYFLAGS =
DOC = doxygen
DOCFLAGS =
DOCCONFIG = circleDoxygen

SRC= ./src/testCircles.py

.FORCE: test doc clean

test:
	$(PY) $(PYFLAGS) $(SRC)

doc:
	$(DOC) $(DOCFLAGS) $(DOCCONFIG)
	cd latex && make

clean:
	rm -rf html
	rm -rf latex


