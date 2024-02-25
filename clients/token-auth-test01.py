import json
import requests


def client():
    token_h = "Token f25328c69838e89c8f83c160a1816279ffbcda80"
    # credentials = {"username": "admin", "password": "1"}

    # response = requests.post(
    #     "http://127.0.0.1:8000/api/auth/login/", data=credentials
    # )

    headers = {"Authorization": token_h}

    response = requests.get("http://127.0.0.1:8000/api/profiles/", headers=headers)

    print("Status Code: ", response.status_code)
    response_data = response.json()
    print(response_data)


if __name__ == "__main__":
    client()
