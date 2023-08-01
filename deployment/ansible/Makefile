SHELL := bash
APP_NAME=$$(cat myvars.yml | grep app_name | awk '{print $$2}')
PROJECT_USER=$$(cat myvars.yml | grep project_user | awk '{print $$2}')
ANSIBLE_USER=$$(cat myhosts.ini | awk '/ansible_user=/{print $$2}' | cut -c14-)
ANSIBLE_HOST=$$(cat myhosts.ini | awk '/ansible_user=/{print $$3}' | cut -c14-)
TARGET="$(ANSIBLE_USER)@$(ANSIBLE_HOST)"
.ONESHELL:
.SHELLFLAGS := -eu -o pipefail -c
.SILENT:
.PHONY: all

login:
	ssh $(TARGET)

provision:
	ansible-playbook provision.yml -i myhosts.ini --extra-vars "@myvars.yml" --extra-vars "app_version=$(APP_VERSION)"

deploy:
	ansible-playbook provision.yml -i myhosts.ini --tags deploy --extra-vars "@myvars.yml" --extra-vars "app_version=$(APP_VERSION)"

status:
	ssh -t $(TARGET) "systemctl status $(APP_NAME) --no-pager"
	ssh -t $(TARGET) "systemctl status $(APP_NAME)_queue --no-pager"
	ssh -t $(TARGET) "systemctl status postgresql --no-pager"
	ssh -t $(TARGET) "systemctl status redis --no-pager"
	ssh -t $(TARGET) "systemctl status caddy --no-pager"

appservicelog:
	ssh -t $(TARGET) "journalctl -u $(APP_NAME) -n 200 -f --utc"

queueservicelog:
	ssh -t $(TARGET) "journalctl -u $(APP_NAME)_queue -n 200 -f --utc"

webserverservicelog:
	ssh -t $(TARGET) "journalctl -u caddy -n 200 -f --utc"

webserveraccesslog:
	ssh -t $(TARGET) "tail -n 200 -f /var/log/caddy/access.log | jq"

monitor:
	ssh -t $(TARGET) "tiptop"

createsuperuser:
	ssh -t $(TARGET) "cd /srv/$(APP_NAME) && sudo -u $(PROJECT_USER) poetry run ./manage.py createsuperuser"

upgrade:
	ansible-playbook system_upgrade.yml -i myhosts.ini --extra-vars "@myvars.yml"