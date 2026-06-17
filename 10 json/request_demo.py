import requests

BASE_URL = "https://jsonplaceholder.typicode.com/users"

# CREATE
response = requests.post(
    BASE_URL,
    json={
        "name": "Aman",
        "email": "aman@gmail.com"
    }
)

print("Created:", response.json())

# READ
response = requests.get(f"{BASE_URL}/1")
print("Fetched:", response.json())

# UPDATE
response = requests.put(
    f"{BASE_URL}/1",
    json={
        "id": 1,
        "name": "Updated Aman",
        "email": "updated@gmail.com"
    }
)

print("Updated:", response.json())

# DELETE
response = requests.delete(f"{BASE_URL}/1")
print("Deleted Status:", response.status_code)