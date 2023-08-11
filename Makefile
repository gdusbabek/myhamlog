clean:
	rm -rf .pytest_cache
	rm -rf myhamlog/__pycache__
	rm -rf build
	rm -rf dist
	rm -rf n3fjp_gdusbabek.egg-info

realclean: clean
	rm -f Pipfile.lock
	rm -rf `pipenv --venv`

pipenv:
	pipenv install -d -e .

dist:
	python3 setup.py sdist bdist_wheel

test:
	pipenv run pytest
