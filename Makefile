BASEDIR = $(CURDIR)

.PHONY: init_backend
init_backend:
	CC=gcc pipenv install

.PHONY: init_frontend
init_frontend:
	cd frontend/vue \
		&& npm install \
		&& npm run build

.PHONY: build
build: init_frontend init_backend

.PHONY: run
run:
	pipenv shell FLASK_APP=backend/python/run.py FLASK_DEBUG=1 flask run
