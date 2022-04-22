install:
	pip install .
	
wheel:
	python3 setup.py bdist_wheel --bdist-dir ~/temp/bdistwheel

