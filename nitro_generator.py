import string
import time
import random
import os

os.system("pip install requests")
import requests

ALPHA_NUM = string.ascii_uppercase + string.digits + string.ascii_lowercase
END = time.time() + 3600 * 3
def generateRandomString(length):
	result = ''
	for i in range(length):
		result += random.choice(ALPHA_NUM)
	return result
while time.time() < END:
	code = generateRandomString(16)
	url =  f"https://discordapp.com/api/v9/entitlements/gift-codes/{code}?with_application=false&with_subscription_plan=true"
	r = requests.get(url)
	if r.status_code == 200:
		print(f"Valid nitro: {code}")