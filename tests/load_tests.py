import random

from locust import HttpUser, between, task

class Carpark_User(HttpUser):
    wait_time = between(1, 10)

    @task
    def index(self):
        self.client.get("/")

    @task
    def add_car(self):
        rand_reg = str(random.randint(0, 20))
        with self.client.post("/add", {"reg": rand_reg, "type": "Car"}, catch_response=True) as response:
            if response.status_code <= 400:
                response.success()

    @task
    def remove_car(self):
        with self.client.post("/remove", {"reg": str(random.randint(0, 20))}, catch_response=True) as response:
            if response.status_code == 404:
                response.success()


