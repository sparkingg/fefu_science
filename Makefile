PACKAGE = science
APPS_DIR = apps

APPS = $(sort $(dir $(wildcard $(PACKAGE)/$(APPS_DIR)/*/)))

install:
	@poetry install

start_app:
	@mkdir $(PACKAGE)/$(APPS_DIR)/$(APP)
	@poetry run python $(PACKAGE)/manage.py startapp $(APP) $(PACKAGE)/$(APPS_DIR)/$(APP)

selfcheck:
	@poetry check

build: selfcheck
	@poetry build

run:
	@poetry run python $(PACKAGE)/manage.py runserver

make_migrations:
	@poetry run python $(PACKAGE)/manage.py makemigrations

migrate:
	@poetry run python $(PACKAGE)/manage.py migrate

make_messages:
	@django-admin makemessages -l ru

compile_messages:
	@django-admin compilemessages

test:
	@poetry run coverage run $(PACKAGE)/manage.py test $(APPS)
	@poetry run coverage html

create_template_dir:
	@mkdir -p $(PACKAGE)/$(APPS_DIR)/$(APP)/templates/$(APP)

create_crud_templates: create_template_dir
	@touch $(PACKAGE)/$(APPS_DIR)/$(APP)/templates/$(APP)/$(MODEL)_create.html
	@touch $(PACKAGE)/$(APPS_DIR)/$(APP)/templates/$(APP)/$(MODEL)_read.html
	@touch $(PACKAGE)/$(APPS_DIR)/$(APP)/templates/$(APP)/$(MODEL)_update.html
	@touch $(PACKAGE)/$(APPS_DIR)/$(APP)/templates/$(APP)/$(MODEL)_delete.html
	@touch $(PACKAGE)/$(APPS_DIR)/$(APP)/templates/$(APP)/$(MODEL)_table.html

report:
	@poetry run coverage report

.PHONY: install test selfcheck build run make_migrations migrate make_messages compile_messages report
