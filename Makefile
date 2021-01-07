COMPOSE ?= docker-compose -f compose-base.yml

build:
	$(COMPOSE) build

run: build
run:
	$(COMPOSE) up -d

logs:
	$(COMPOSE) logs -f bot