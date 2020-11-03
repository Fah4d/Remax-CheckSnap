import requests
import json
import time
remax = """

██████╗░███████╗███╗░░░███╗░█████╗░██╗░░██╗  ░██████╗░██╗░░██╗
██╔══██╗██╔════╝████╗░████║██╔══██╗╚██╗██╔╝  ██╔════╝░██║░░██║
██████╔╝█████╗░░██╔████╔██║███████║░╚███╔╝░  ██║░░██╗░███████║
██╔══██╗██╔══╝░░██║╚██╔╝██║██╔══██║░██╔██╗░  ██║░░╚██╗██╔══██║
██║░░██║███████╗██║░╚═╝░██║██║░░██║██╔╝╚██╗  ╚██████╔╝██║░░██║
╚═╝░░╚═╝╚══════╝╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝  ░╚═════╝░╚═╝░░╚═╝

            Remax Alghamdi - insta : @ 0637871936 .
            
"""

print(remax)
time.sleep(3)

CountryCode = str(input("Key of Country ( example : SA ) : "))
phonenumber = int(input("Enter The PhoneNumber : "))

def check():
	url = "https://accounts.snapchat.com/accounts/validate_phone_number"
	cookies = {
			"xsrf_token":'BtpZ6sL9OenEJJYbQXFEsg'
	}
	headers = {
	"accept": "*/*",
	"accept-encoding": "gzip, deflate, br",
	"accept-language": "ar,en;q=0.9,en-US;q=0.8",
	"content-type": "application/x-www-form-urlencoded; charset=utf-8",
	"sec-fetch-dest": "empty",
	"sec-fetch-mode": "same-origin",
	"sec-fetch-site": "same-origin",
	"user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Mobile Safari/537.36"
	}
	data = {"phone_country_code":CountryCode,"phone_number":phonenumber,"xsrf_token":"BtpZ6sL9OenEJJYbQXFEsg"}
	req = requests.post(url,data=data,headers=headers,cookies=cookies).json()
	text = str(req)
	print(text)
	if text.find('OK')>=0:
	    print("Unlinked !")
	else:
	    print("linked !")

check()

print('')
input("press enter to close the program.")
