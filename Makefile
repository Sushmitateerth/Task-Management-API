build:
	docker build -t task-management .

run: build
	docker run task-management

.PHONY: build run