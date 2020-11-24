import requests, time, json
from authlib.jose import jwt

KEY_ID = "54B5HXSLW5"
ISSUER_ID = "7006d34d-7b78-4916-830f-77dc388d9f15"
EXPIRATION_TIME = int(round(time.time() + (20.0 * 60.0))) # 20 minutes timestamp
PATH_TO_KEY = 'C:\\Users\\ilyos\\PycharmProjects\\pythonProject5\\AuthKey_54B5HXSLW5.txt'
with open(PATH_TO_KEY, 'r') as f:
    PRIVATE_KEY = f.read()

header = {
    "alg": "ES256",
    "kid": KEY_ID,
    "typ": "JWT"
}
print(PRIVATE_KEY)
payload = {
    "iss": ISSUER_ID,
    "exp": EXPIRATION_TIME,
    "aud": "appstoreconnect-v1"
}

# Create the JWT
token = jwt.encode(header, payload, PRIVATE_KEY)

# API Request
JWT = 'Bearer ' + token.decode()
print(token)
URL = 'https://api.appstoreconnect.apple.com/v1/apps/1541476369/inAppPurchases'
HEAD = {'Authorization': JWT}
r = requests.get(URL, params={'limit': 200}, headers=HEAD)
print(r.text)
