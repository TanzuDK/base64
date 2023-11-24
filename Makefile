up:
	docker compose up

build:
	docker compose build

down:
	docker compose down

loadtest:
	locust -f locust/locustfile.py -H https://base64-api.base64.gke.tanzu.dk 