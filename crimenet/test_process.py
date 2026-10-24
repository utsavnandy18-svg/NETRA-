import requests

login_resp = requests.post("https://crimenet.onrender.com/api/v1/auth/login", data={"username": "admin", "password": "admin123"})
token = login_resp.json()["access_token"]
print("Token:", token[:10])

proc_resp = requests.post(
    "https://crimenet.onrender.com/api/v1/process", 
    json={"upload_ids": ["test"], "options": {}},
    headers={"Authorization": f"Bearer {token}"}
)
print(proc_resp.json())
