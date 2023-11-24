up:
	docker compose up

build:
	docker compose build

down:
	docker compose down

loadtest-cli:
	docker run -p 8089:8089 -v ./locust/:/mnt/locust locustio/locust -f /mnt/locust/locustfile.py -H https://base64-api.base64.gke.tanzu.dk --headless -u 1000 -r 100 -t 1m

loadtest-ui:
	docker run -p 8089:8089 -v ./locust/:/mnt/locust locustio/locust -f /mnt/locust/locustfile.py -H https://base64-api.base64.gke.tanzu.dk -u 1000 -r 10 -t 1m