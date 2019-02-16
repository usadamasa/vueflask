BASEDIR = $(CURDIR)

.PHONY: init_backend
init_backend:
	cd backend/python \
		&& pipenv install \

.PHONY: init_frontend
init_frontend:
	cd frontend/vue \
		&& npm install \
		&& npm run build

.PHONY: init
init: init_frontend init_backend

.PHONY: run
run:
	cd backend/python \
		&& pipenv shell FLASK_APP=$(CURDIR)/run.py FLASK_DEBUG=1 flask run
