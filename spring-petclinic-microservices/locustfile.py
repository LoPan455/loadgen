import array
import time
from locust import HttpUser, task, between, run_single_user, constant_pacing
from urllib.parse import urlparse
import random
import names


class SpringPetClinicUser(HttpUser):
    # host = "http://localhost:8080/api"
    wait_time = constant_pacing(1)
    pet_to_owner_map = [
        [1, 1], [2, 2], [3, 3], [4, 3], [5, 4], [6, 5], [7, 6], [8, 6], [9, 7], [10, 8], [11, 9], [12, 10], [13, 10]
    ]

    @task
    def get_vets(self):
        self.client.get("api/vet/vets")

    @task
    def find_owners(self):
        self.client.get("api/customer/owners/")

    @task
    def get_owners_by_id(self):
        owner_id = random.randrange(1, 10)
        self.client.get(f"api/gateway/owners/{owner_id}")

    @task
    def get_pet_by_owner(self):
        pet_owner_pair = self.pet_to_owner_map[random.randrange(0, (len(self.pet_to_owner_map) - 1))]
        pet_id = pet_owner_pair[0]
        owner_id = pet_owner_pair[1]
        self.client.get(f"api/customer/owners/{owner_id}/pets/{pet_id}")

# @task
# def get_owner_by_id_and_add_pet(self):
#     owner_id = random.randrange(1, 10)
#     pet_name = names.get_first_name()
#     with self.client.post(
#             f"/owners/{owner_id}/pets/new",
#             data={"name": pet_name, "type": "hamster", "birthDate": "2015-02-12"}) as newPetResponse:
#         return urlparse(newPetResponse.url).path

# @task
# def edit_owner(self):
#     owner_id = random.randrange(1, 10)
#     first_name = names.get_first_name()
#     last_name = names.get_last_name()
#     with self.client.post(f"/owners/{owner_id}/edit", data={"firstName": first_name, "lastName": last_name}) as editedOwnerResponse:
#         return urlparse(editedOwnerResponse.url).path

# @task
# def add_new_owner_and_pet(self):
#     owner_path = self.add_owner()
#     pet_response = self.add_pet(owner_path)

# @task
# def add_visit(self):
#     owner_id = random.randrange(1, 10)
#     # There isn't a way to get all pets for an owner via the api, so we have to build this
#     # relationship list from the SQL script that's run at Startup to ensure we don't create a visit for a pet with
#     # an incorrect owner
#     pet_owner_map = [
#         [1, 1], [2, 2], [3, 3], [4, 3], [5, 4], [6, 5], [7, 6], [8, 6], [9, 7], [10, 8], [11, 9], [12, 10], [13, 10]
#     ]
#     # Pick a random pair of valid owner-pet relationship
#     owner_pet_relationship = pet_owner_map[random.randrange(0, pet_owner_map.__len__() - 1)]
#     # Pets IDs are the first element in each tuple
#     pet_id = owner_pet_relationship[0]
#     # Owner IDs are the second element in each tuple
#     owner_id = owner_pet_relationship[1]
#     with self.client.post(
#         f"/owners/{owner_id}/pets/{pet_id}/visits/new/",
#         data={"date": "2022-04-24", "description": "Making sure my pet is healthy", "petId": pet_id}
#     ) as visitResponse:
#         return visitResponse

# def add_owner(self):
#     first_name = names.get_first_name()
#     last_name = names.get_last_name()
#     with self.client.post(
#             "/owners/new",
#             data={
#                 "firstName": first_name,
#                 "lastName": last_name,
#                 "address": "143 Peace Ave South",
#                 "city": "Anytown",
#                 "telephone": "6125551212"}, catch_response=True) as newOwnerResponse:
#         return urlparse(newOwnerResponse.url).path

# def add_pet(self, owner_path):
#     pet_name = names.get_first_name()
#     return self.client.post(f"{owner_path}/pets/new",
#                             data={"id": "", "name": pet_name, "birthDate": "2020-01-02", "type": "dog"})


# if launched directly, e.g. "python3 locustfile.py", not "locust -f locustfile.py"
if __name__ == "__main__":
    run_single_user(SpringPetClinicUser)
