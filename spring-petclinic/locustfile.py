import time
from locust import HttpUser, task, between, run_single_user
from urllib.parse import urlparse
import random


class SpringPetClinicUser(HttpUser):
    host = "http://localhost:8080"
    wait_time = between(1, 3)

    @task
    def get_vets(self):
        self.client.get("/vets.html")
        self.client.get("/vets.html?page:2")

    @task
    def find_owners(self):
        self.client.get("/owners/find")

    @task
    def get_owners_by_id(self):
        ownder_id = random.randrange(1, 10)
        self.client.get(f"/owners/{ownder_id}")

    @task
    def add_new_owner_and_pet(self):
        owner_path = self.add_owner()
        self.add_pet(owner_path)

    def add_owner(self):
        with self.client.post(
                "/owners/new",
                data={
                    "firstName": "Thomas",
                    "lastName": "Johander",
                    "address": "2841 Colfax Ave South",
                    "city": "Minneapolis",
                    "telephone": "9524129195"}, catch_response=True) as newOwnerResponse:
            return urlparse(newOwnerResponse.url).path

    def add_pet(self, owner_path):
        return self.client.post(f"{owner_path}/pets/new",
                                data={"id": "", "name": "fluffy", "birthDate": "2020-01-02", "type": "dog"})


# if launched directly, e.g. "python3 locustfile.py", not "locust -f locustfile.py"
if __name__ == "__main__":
    run_single_user(SpringPetClinicUser)
