import string
import time
import random
import os

os.system("pip install requests > /dev/null")
import requests

ALPHA_NUM = string.ascii_uppercase + string.digits + string.ascii_lowercase
END = time.time() + 3600 * 6 - 30
def generateRandomString(length):
	result = ''
	for i in range(length):
		result += random.choice(ALPHA_NUM)
	return result
tested = 0
valid = 0
while time.time() < END:
	code = generateRandomString(16)
	url =  f"https://discordapp.com/api/v9/entitlements/gift-codes/{code}?with_application=false&with_subscription_plan=true"
	while 1:
		try:
			r = requests.get(url)
			break
		except:
			continue
	if r.status_code == 200:
		print(f"Valid nitro: {code}")
		valid += 1
	tested += 1
print(f"the program tested {tested} codes. {valid} of them are valid")
