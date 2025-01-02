.PHONY: build up down logs shell test migrate

build:
	docker-compose build

up:
	docker-compose up -d

down:
	docker-compose down

logs:
	docker-compose logs -f

shell:
	docker-compose exec web python manage.py shell

test:
	docker-compose exec web python manage.py test

migrate:
	docker-compose exec web python manage.py migrate