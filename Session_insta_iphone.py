from  requests import post

def login_one_session():
    username = input("\n[+] Enter Your Username: ")
    password = input("\n[+] Enter Your Password: ") 

    url = 'https://i.instagram.com/api/v1/accounts/login/'

    headers_login = {

		'Host': 'i.instagram.com',
		'X-Ig-App-Id': '124024574287414',
		'X-Ig-Device-Id': '8CD36001-81F5-4036-BA94-2B48A3997394',
		'X-Ig-Connection-Type': 'WiFi',
		'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
		'X-Ig-Capabilities': '36r/Fwc=',
		'User-Agent': 'Instagram 157.0.0.23.119 (iPhone8,1; iOS 14_1; en_SA@calendar=gregorian; ar-SA; scale=2.00; 750x1334; 241452311) AppleWebKit/420+',
		'X-Mid': 'YhqS7gAAAAHvDii2B2NQuVjiCCl1',
		'Content-Length': '769',
		'Accept-Encoding': 'gzip, deflate',
		'X-Fb-Http-Engine': 'Liger'

        }
        
    data = {

        "username": f"{username}",
		"reg_login":"0",
		"enc_password": f"#PWD_INSTAGRAM:0:&:{password}",
		"device_id":"8CD36001-81F5-4036-BA94-2B48A3997394",
		"login_attempt_count":"0",
		"phone_id":"8CD36001-81F5-4036-BA94-2B48A3997394"

        }

    req_login = post(url, headers=headers_login, data=data)

    if 'logged_in_user' in req_login.text:
        print(f"[+] Logged in with {username}")
        sessionid = req_login.cookies.get("sessionid")
        print(sessionid)
        with open(f'{username}.txt', 'w') as file:
            file.write(f'{sessionid}')
            print(f"[$] Saved as {username}.txt")
    
    elif 'The password you entered is incorrect' in req_login.text:
        print("The password you entered is incorrect\n\n")
        login_one_session()

    elif "The username you entered doesn't appear to belong to an account" in req_login.text:
        print(f"{username} Not Found\n\n")
        login_one_session()

    elif "challenge_required" in req_login.text:
        print(f"{username} is secured")
        login_one_session()
    
    elif "Try Again Later" in req_login.text:
        print(f"Blocked login Try Again Later\n\n")
        login_one_session()

    else:
        input(req_login.text)

login_one_session()