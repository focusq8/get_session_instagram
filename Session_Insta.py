from  requests import get , post
from  os import system
from uuid import uuid4
from os import system
def login_one_session():
    global req_login , headers_login , username

    system('cls||clear')

    username = input("[+] username: ")
    password = input("[+] password: ") 

    url = 'https://i.instagram.com/api/v1/accounts/login/'

    headers_login = {

        'X-Pigeon-Session-Id': str(uuid4()),
        'X-IG-Device-ID': str(uuid4()),
        'User-Agent': 'Instagram 135.0.0.00.000 Android (25/7.1.2; 192dpi; 720x1280; google; G011A; G011A; intel; en_US; 289692181)',
        'X-IG-Connection-Type': 'WIFI',
        'X-IG-Capabilities': '3brTvw8=',
        "Connection" : 'keep-alive',
        "Accept-Language": "en-US",
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        "Accept-Encoding": "gzip, deflate",
        'Host': 'i.instagram.com'

        }
        
    data = {
        'username': username,
        'enc_password': f"#PWD_INSTAGRAM:0:&:{password}",
        "adid": uuid4(),
        "guid": uuid4(),
        "device_id": uuid4(),
        "phone_id": uuid4(),
        "google_tokens": "[]",
        'login_attempt_count': '0'
        }

    req_login = post(url, headers=headers_login, data=data)
    system('cls||clear')

    if 'logged_in_user' in req_login.text:
        print(f"[+] Logged in with {username}")
        sessionid = req_login.cookies.get("sessionid")
        with open(f'{username}.txt', 'w') as file:
            file.write(f'{sessionid}')
            file.close()
            print(f"[$] Saved as {username}.txt")

    elif "challenge_required" in req_login.text:
        print(f"{username} is secured")
        send_code_session()

    else:
        input(req_login.text)


def login_list_sessions():

    global req_login, headers_login , username
    system('cls||clear')
    print(f"[+] get list sessions accounts [+]\n\n\n")

    file = input("[+] Enter Your File Name: ")
    if '.txt' in file:
        pass
    else:
        files  = file + '.txt'

    open_file = open(file,"r").read().splitlines()

    for combo in open_file:
        username = combo.split(":")[0]
        password = combo.split(":")[1]

        url = 'https://i.instagram.com/api/v1/accounts/login/'

        headers_login = {

            'X-Pigeon-Session-Id': str(uuid4()),
            'X-IG-Device-ID': str(uuid4()),
            'User-Agent': 'Instagram 135.0.0.00.000 Android (25/7.1.2; 192dpi; 720x1280; google; G011A; G011A; intel; en_US; 289692181)',
            'X-IG-Connection-Type': 'WIFI',
            'X-IG-Capabilities': '3brTvw8=',
            "Connection" : 'keep-alive',
            "Accept-Language": "en-US",
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            "Accept-Encoding": "gzip, deflate",
            'Host': 'i.instagram.com'

            }
            
        data = {
            'username': username,
            'enc_password': f"#PWD_INSTAGRAM:0:&:{password}",
            "adid": uuid4(),
            "guid": uuid4(),
            "device_id": uuid4(),
            "phone_id": uuid4(),
            "google_tokens": "[]",
            'login_attempt_count': '0'
            }

        req_login = post(url, headers=headers_login, data=data)
        if 'logged_in_user' in req_login.text:
            print(f"[+] Logged in with {username}")
            sessionid = req_login.cookies.get("sessionid")
            with open(f'{username}.txt', 'w') as file:
                file.write(f'{sessionid}')
                file.close()
                print(f"[$] Saved as {username}.txt")

        elif "challenge_required" in req_login.text:
            print(f"{username} is secured")
            send_code_session()

        else:
            input(req_login.text)


def send_code_session():
    get_cookies = req_login.cookies
    info = get(url=f"https://i.instagram.com/api/v1{req_login.json()['challenge']['api_path']}",
    headers=headers_login, cookies=get_cookies)

    if "phone_number" in info.json()["step_data"] and "email" in info.json()["step_data"]:
        print(f'[0] Phone_Number: {info.json()["step_data"]["phone_number"]} \n[1] Email: {info.json()["step_data"]["email"]}')


    elif "phone_number" in info.json()["step_data"]:
        print(f'[0] Phone_Number: {info.json()["step_data"]["phone_number"]}')

    elif "email" in info.json()["step_data"]:
        print(f'[1] Email: {info.json()["step_data"]["email"]}')

    else:
        print("wrong")

    get_code_session()  

def get_code_session():

    get_cookies = req_login.cookies
    choice = input('choose a number: ')
    secure_data = {'choice': str(choice),'device_id': f"android-{uuid4}",'guid': uuid4,'_csrftoken': 'massing'}
    send_choice = post(url=f"https://i.instagram.com/api/v1{req_login.json()['challenge']['api_path']}",
    headers=headers_login,data=secure_data, cookies=get_cookies)

    if "step_data" not in send_choice.text:
        print(f' {send_choice.text}')
    elif "step_data" in send_choice.text:
        print( f'code sent to: {send_choice.json()["step_data"]["contact_point"]}')
        code = input('\nEnter the code: ')
        code_data = {
            'security_code': str(code),
            'device_id': f"android-{uuid4}",
            'guid': uuid4,
            '_csrftoken': 'massing'
            }

    send_code = post(url=f"https://i.instagram.com/api/v1{req_login.json()['challenge']['api_path']}",
    headers=headers_login, data=code_data, cookies=get_cookies)

    if "logged_in_user" in send_code.text:
        print(f'logged in with {username}')
        get_session = send_code.cookies["sessionid"]
        with open(f'{username}.txt', 'w') as file:
            file.write(f'{get_session}')
            file.close()
            print(f"[$] Saved as {username}.txt")

        
    elif "Please check the code we sent you and try again." in send_code.text:
        print('you entered wrong code , try again')
        get_code_session()

    elif "This field is required." in send_code.text:
        print("Enter the code!")
        get_code_session()                                    
    else:
        print(f' {send_code.text}')
        get_code_session()


if __name__ == "__main__":
    def begin():
        choose = input("""
    
[ 1 ] get session one account
[ 2 ] get list sessions accounts

please choose your number: """)

        if choose == "1":
            login_one_session()
        elif choose == "2":
            login_list_sessions()
        else:
            system('cls||clear')
            begin()
    begin()

