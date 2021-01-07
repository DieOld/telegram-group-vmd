COMPOSE ?= docker-compose -f compose-base.yml

build:
	$(COMPOSE) build

run: build
run:
	$(COMPOSE) up -d

logs:
	$(COMPOSE) logs -f bot

version:
	$(eval GIT_TAG ?= $(shell git describe --abbrev=0))
	$(eval VERSION ?= $(shell read -p "Version: " VERSION; echo $$VERSION))
	echo "Tagged release $(VERSION)\n" > Changelog-$(VERSION).txt
	git log --oneline --no-decorate --no-merges $(GIT_TAG)..HEAD >> Changelog-$(VERSION).txt
	git tag -a -e -F Changelog-$(VERSION).txt $(VERSION)
