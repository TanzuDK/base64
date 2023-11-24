from locust import HttpUser, task


class Base64(HttpUser):
    @task
    def base64(self):
        self.client.post("/encode", json={"data":"Hello World"})
        self.client.post("/decode", json={"data":"VGFuenUgUm9ja3MhISE="})
