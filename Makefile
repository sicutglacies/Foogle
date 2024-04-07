run:
	streamlit run app/main.py

gen_reqs:
	poetry export --without-hashes --without-urls | awk '{ print $1 }' FS=';' > requirements.txt

install:
	poetry install
	python -m nltk.downloader punkt

format:
	ruff check --fix

lint:
	ruff check .
