import time
from locust import HttpUser, task, between, run_single_user, constant_pacing
from urllib.parse import urlparse
import random
import names


class SpringPetClinicUser(HttpUser):
    host = "http://localhost:8080"
    wait_time = constant_pacing(2)

    @task
    def get_vets(self):
        self.client.get("/vets.html")
        self.client.get("/vets.html?page:2")
        self.client.get("/vets.html?page:3")

    @task
    def find_owners(self):
        self.client.get("/owners/find")

    @task
    def get_owners_by_id(self):
        owner_id = random.randrange(1, 10)
        self.client.get(f"/owners/{owner_id}")

    @task
    def get_owner_by_id_and_add_pet(self):
        owner_id = random.randrange(1, 10)
        pet_name = names.get_first_name()
        with self.client.post(
                f"/owners/{owner_id}/pets/new",
                data={"name": pet_name, "type": "hamster", "birthDate": "2015-02-12"}) as newPetResponse:
            return urlparse(newPetResponse.url).path

    @task
    def edit_owner(self):
        owner_id = random.randrange(1, 10)
        first_name = names.get_first_name()
        last_name = names.get_last_name()
        with self.client.post(f"/owners/{owner_id}/edit", data={"firstName": first_name, "lastName": last_name}) as editedOwnerResponse:
            return urlparse(editedOwnerResponse.url).path

    @task
    def add_new_owner_and_pet(self):
        owner_path = self.add_owner()
        self.add_pet(owner_path)

    def add_owner(self):
        first_name = names.get_first_name()
        last_name = names.get_last_name()
        with self.client.post(
                "/owners/new",
                data={
                    "firstName": first_name,
                    "lastName": last_name,
                    "address": "143 Peace Ave South",
                    "city": "Anytown",
                    "telephone": "6125551212"}, catch_response=True) as newOwnerResponse:
            return urlparse(newOwnerResponse.url).path

    def add_pet(self, owner_path):
        pet_name = names.get_first_name()
        return self.client.post(f"{owner_path}/pets/new",
                                data={"id": "", "name": pet_name, "birthDate": "2020-01-02", "type": "dog"})


# if launched directly, e.g. "python3 locustfile.py", not "locust -f locustfile.py"
if __name__ == "__main__":
    run_single_user(SpringPetClinicUser)
