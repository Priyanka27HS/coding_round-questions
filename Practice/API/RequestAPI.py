import requests
import random
import json
import string

# base url :
base_url = "https://gorest.co.in"

# Auth token
auth_token = "Bearer df23e33be2e44dfccdfe5ec3bcf2f37430e7229215225d5ed60168d01bc241d7"


# get random email id :
def generate_random_email():
    domain = "gmail.com"
    email_length = 10
    random_string = ''.join(random.choice(string.ascii_lowercase) for _ in range(email_length))
    email = random_string + "@" + domain
    return email


# GET Request
def get_request():
    url = base_url + "/public/v2/users/"
    print("Get Url: " + url)
    headers = {"Authorization": auth_token}
    response = requests.get(url, headers=headers)
    assert response.status_code == 200
    json_data = response.json()
    json_str = json.dumps(json_data, indent=4)
    print("Json Get response body: ", json_str)


# POST Request
def post_request():
    url = base_url + "/public/v2/users/"
    print("Post Url: " + url)
    headers = {"Authorization": auth_token}
    data = {
        "name": "Suresh",
        "email": generate_random_email(),
        "gender": "male",
        "status": "active"
    }
    response = requests.post(url, json=data, headers=headers)
    assert response.status_code == 201
    json_data = response.json()
    json_str = json.dumps(json_data, indent=4)
    print("Json Post response body: ", json_str)
    user_id = json_data["id"]
    assert "name" in json_data
    assert json_data["name"] == "Suresh"
    return user_id


# PUT Request - update user info
def put_request(user_id):
    url = base_url + f"/public/v2/users/{user_id}"
    print("Put Url: " + url)
    headers = {"Authorization": auth_token}
    data = {
        "name": "Suresh Geetha",
        "email": generate_random_email(),
        "gender": "male",
        "status": "inactive"
    }
    response = requests.put(url, json=data, headers=headers)
    assert response.status_code == 200
    json_data = response.json()
    json_str = json.dumps(json_data, indent=4)
    print("Json Put response body: ", json_str)
    assert json_data["id"] == user_id
    assert json_data["name"] == "Suresh Geetha"


# DELETE Request
def delete_request(user_id):
    url = base_url + f"/public/v2/users/{user_id}"
    print("Delete Url: " + url)
    headers = {"Authorization": auth_token}
    response = requests.delete(url, headers=headers)
    assert response.status_code == 204
    print("Delete a user is done...")


# call request method
get_request()
user_id = post_request()
put_request(user_id)
delete_request(user_id)
