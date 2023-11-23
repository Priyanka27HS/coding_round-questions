import requests
import json

# base url
base_url = "https://gorest.co.in"

# Auth token
auth_token = "Bearer df23e33be2e44dfccdfe5ec3bcf2f37430e7229215225d5ed60168d01bc241d7"


# GET Request
def get_req():
    url = base_url + "/public/v2/users"
    print("Get Url : ", url)
    headers = {"Authorization": auth_token}
    response = requests.get(url, headers=headers)
    assert response.status_code == 200
    json_data = response.json()
    # convert json data to response
    json_str = json.dumps(json_data, indent=4)
    print("Json response body is : ", json_str)


# POST Request
def post_req():
    url = base_url + "/public/v2/users"
    print("Post Url : ", url)
    headers = {"Authorization": auth_token}
    data = {
        "name": "Chandan Johar Sr.",
        "email": "chandan_johar_sr123@lindgren.example",
        "gender": "male",
        "status": "active"
    }


# PUT Request


# DELETE Request

# call
get_req()

