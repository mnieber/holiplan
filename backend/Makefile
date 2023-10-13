#
# Postgres
#

create-db:
	PGPASSWORD=${POSTGRES_PASSWORD} psql -h ${POSTGRES_HOST} -d postgres -U postgres -c "CREATE USER ${DJANGO_DATABASE_USER} WITH CREATEDB PASSWORD '${DJANGO_DATABASE_PASSWORD}';" || true
	PGPASSWORD=${DJANGO_DATABASE_PASSWORD} psql -h ${POSTGRES_HOST} -d postgres -U ${DJANGO_DATABASE_USER} -c "CREATE DATABASE ${DJANGO_DATABASE_NAME};" || true
	PGPASSWORD=${POSTGRES_PASSWORD} psql -h ${POSTGRES_HOST} -d postgres -U postgres -c "GRANT ALL PRIVILEGES ON DATABASE ${DJANGO_DATABASE_NAME} TO ${DJANGO_DATABASE_USER};"

#
# Python
#

install:
	pip install -r .requirements/dev.txt

pip-compile:
	pip-compile .requirements/base.in -o .requirements/base.txt
	pip-compile .requirements/dev.in -o .requirements/dev.txt

#
# Django
#

collect-static:
	python manage.py collectstatic --link

create-superuser:
	python manage.py createsuperuser --noinput || true

migrate:
	python manage.py migrate

run-server:
	python manage.py runserver 0.0.0.0:8000

#
# Stack
#

init-dev: \
	create-db \
	pip-compile \
	install \
	migrate \
	collect-static \
	create-superuser
