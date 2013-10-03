HERE = $(shell pwd)

.PHONY: all build

all: build

clean:
	vagrant destroy
	rm authorized_keys

auth_keys:
	cat ~/.ssh/id_rsa.pub > $(HERE)/authorized_keys
	cat files/vagrant.pub >> $(HERE)/authorized_keys

build: auth_keys
	pip install ansible
	vagrant up
