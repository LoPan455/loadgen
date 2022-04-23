import time
from locust import HttpUser, task, between, run_single_user


class QuickStartUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def hello_world(self):
        self.client.get("/hello")
        self.client.get("/world")
