from  requests import get , post
from  os import system
from uuid import uuid4
from os import system
def login_one_session():
    global req_login_one_session , headers_one_session , username_one_session

    system('cls||clear')

    username_one_session = input("[+] username: ")
    password = input("[+] password: ") 

    url_one_session = 'https://i.instagram.com/api/v1/accounts/login/'

    headers_one_session = {

        'X-Pigeon-Session-Id': str(uuid4()),
        'X-IG-Device-ID': str(uuid4()),
        'User-Agent': 'Instagram 159.0.0.40.122 Android (25/7.1.2; 240dpi; 1280x720; samsung; SM-G977N; beyond1q; qcom; en_US; 245196089)',
        'X-IG-Connection-Type': 'WIFI',
        'X-IG-Capabilities': '3brTvx8=',
        "Connection" : 'keep-alive',
        "Accept-Language": "en-US",
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        "Accept-Encoding": "gzip, deflate",
        'Host': 'i.instagram.com',
        'Cookie': 'mid=YqejMwABAAExc4QmMCMsnq5YVuEw; csrftoken=BE0qlaD88tnB3vjkLhGksva9WFE2LPYB'
        }
        
    data = {
        'username': username_one_session,
        'enc_password': f"#PWD_INSTAGRAM:0:&:{password}",
        "adid": uuid4(),
        "guid": uuid4(),
        "device_id": uuid4(),
        "phone_id": uuid4(),
        "google_tokens": "[]",
        'login_attempt_count': '0'
        }

    req_login_one_session = post(url=url_one_session, headers=headers_one_session, data=data)
    system('cls||clear')

    if 'logged_in_user' in req_login_one_session.text:
        print(f"[+] Logged in with {username_one_session}")
        sessionid = req_login_one_session.cookies.get("sessionid")
        print(sessionid)
        with open(f'{username_one_session}.txt', 'w') as file:
            file.write(f'{sessionid}')
            print(f"[$] Saved as {username_one_session}.txt")

    elif "The password you entered is incorrect. Please try again." in req_login_one_session.text:
            print(f"{username_one_session} ===> password is wrong\n")
            login_one_session()

    elif "challenge_required" in req_login_one_session.text:
        print(f"{username_one_session} is secured")
        send_code_one_session()

    elif "Please wait a few minutes" in req_login_one_session.text:
        input(f"Blocked login Try Again Later\n\n")
        login_one_session()

    else:
        input(req_login_one_session.text)


def login_list_sessions():

    global req_login_list_sessions, headers_list_sessions , username_list_sessions
    system('cls||clear')
    print(f"[+] get list sessions accounts [+]\n\n\n")

    
    try:
        file = input("[+] Enter Your File Name: ")
        open_file = open(file,"r").read().splitlines()
        if '.txt' in file:
            pass
        else:
            file + '.txt'
    except Exception:
        input("\n\n\nwrite file with .txt")
        login_list_sessions()


    for combo in open_file:
        username_list_sessions = combo.split(":")[0]
        password = combo.split(":")[1]

        url_list_sessions = 'https://i.instagram.com/api/v1/accounts/login/'

        headers_list_sessions = {

            'X-Pigeon-Session-Id': str(uuid4()),
            'X-IG-Device-ID': str(uuid4()),
            'User-Agent': 'Instagram 159.0.0.40.122 Android (25/7.1.2; 240dpi; 1280x720; samsung; SM-G977N; beyond1q; qcom; en_US; 245196089)',
            'X-IG-Connection-Type': 'WIFI',
            'X-IG-Capabilities': '3brTvx8=',
            "Connection" : 'keep-alive',
            "Accept-Language": "en-US",
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            "Accept-Encoding": "gzip, deflate",
            'Host': 'i.instagram.com',
            'Cookie': 'mid=YqejMwABAAExc4QmMCMsnq5YVuEw; csrftoken=BE0qlaD88tnB3vjkLhGksva9WFE2LPYB'

            }
            
        data = {
            'username': username_list_sessions,
            'enc_password': f"#PWD_INSTAGRAM:0:&:{password}",
            "adid": uuid4(),
            "guid": uuid4(),
            "device_id": uuid4(),
            "phone_id": uuid4(),
            "google_tokens": "[]",
            'login_attempt_count': '0'
            }

        req_login_list_sessions = post(url=url_list_sessions, headers=headers_list_sessions, data=data)
        if 'logged_in_user' in req_login_list_sessions.text:
            print(f"[+] Logged in with {username_list_sessions}\n")
            sessionid = req_login_list_sessions.cookies.get("sessionid")
            with open(f'{username_list_sessions}.txt', 'w') as file:
                file.write(f'{sessionid}')
                print(f"[$] Saved as {username_list_sessions}.txt")
        
        elif "The password you entered is incorrect. Please try again." in req_login_list_sessions.text:
            print(f"{username_list_sessions} ===> password is wrong\n")
            login_list_sessions()

        elif "challenge_required" in req_login_list_sessions.text:
            print(f"{username_list_sessions} is secured")
            with open(f'secure_list_sessions.txt', 'w') as file:
                file.write(f'{username_list_sessions}:{password}')
                print(f"[$] Saved as secure_list_sessions.txt")
            send_code_list_sessions()
        
        elif "Please wait a few minutes" in req_login_list_sessions.text:
            print(f"Blocked login Try Again Later\n\n")
            login_list_sessions()

        else:
            input(req_login_list_sessions.text)


def send_code_one_session():
    global api_path_url
    api_path_url = req_login_one_session.json()['challenge']['api_path']
   
    url_send_code = f"https://i.instagram.com/api/v1{api_path_url}"
    req_send_code = get(url=url_send_code,headers=headers_one_session).json()

    if "phone_number" in req_send_code["step_data"] and "email" in req_send_code["step_data"]:
        print(f'[0] Phone_Number: {req_send_code["step_data"]["phone_number"]} \n[1] Email: {req_send_code["step_data"]["email"]}')
        get_code_one_session()
    
    elif 'contact_point' in req_send_code["step_data"]:
        print(f'[1] Email: {req_send_code["step_data"]["contact_point"]}')
        get_code_one_session()
    
    elif 'email' in req_send_code["step_data"]:
        print(f'[1] Email: {req_send_code["step_data"]["email"]}')
        get_code_one_session()
            
    elif "phone_number" in req_send_code["step_data"]:
        print(f'[0] Phone_Number: {req_send_code["step_data"]["phone_number"]}')
        get_code_one_session()

    elif  "phone_number" not in req_send_code["step_data"] and "email" not in req_send_code["step_data"]:
        print("Account needs to confirm it's you ")
    
    else:
        input(req_send_code)
      

def get_code_one_session():

    choice = input('choose a number: ')
    url_get_code = f"https://i.instagram.com/api/v1{api_path_url}"
    get_code_data = {
        'choice': str(choice),
        'device_id': uuid4(),
        'guid': uuid4(),
        '_csrftoken': "BE0qlaD88tnB3vjkLhGksva9WFE2LPYB"
        }
    req_get_code = post(url= url_get_code,headers=headers_one_session,data=get_code_data)
  
    if "step_data" in req_get_code.text:
        print( f'code sent to: {req_get_code.json()["step_data"]["contact_point"]}')
    else:
        input(req_get_code.text)
    security_code = input('\nEnter the security code: ')
    send_code_data = {
            'security_code': str(security_code),
            'device_id': uuid4(),
            'guid': uuid4(),
            '_csrftoken': "BE0qlaD88tnB3vjkLhGksva9WFE2LPYB"
            }
    url_send_code = f"https://i.instagram.com/api/v1{api_path_url}"
    req_send_code = post(url=url_send_code,headers=headers_one_session, data=send_code_data)

    if "logged_in_user" in req_send_code.text:
        print(f'logged in with {username_one_session}')
        get_session = req_send_code.cookies["sessionid"]
        with open(f'{username_one_session}.txt', 'w') as file:
            file.write(f'{get_session}')
            print(get_session)
            input(f"[$] Saved as {username_one_session}.txt")
        
    elif "Please check the code we sent you and try again." in req_send_code.text:
        print('you entered wrong code , try again')
        get_code_one_session()

    elif "This field is required." in req_send_code.text:
        print("Enter the code!")
        get_code_one_session()

    elif '"lock":true'  in req_send_code.text:
        input("you need to active code and change password") 

    else:
        input(req_send_code.text)
        get_code_one_session()

def send_code_list_sessions():
    global api_path_url
    api_path_url = req_login_list_sessions.json()['challenge']['api_path']
   
    url_send_code = f"https://i.instagram.com/api/v1{api_path_url}"
    req_send_code = get(url=url_send_code,headers=headers_list_sessions).json()

    if "phone_number" in req_send_code["step_data"] and "email" in req_send_code["step_data"]:
        print(f'[0] Phone_Number: {req_send_code["step_data"]["phone_number"]} \n[1] Email: {req_send_code["step_data"]["email"]}')
        get_code_list_sessions()
    
    elif 'contact_point' in req_send_code["step_data"]:
            print(f'[1] Email: {req_send_code["step_data"]["contact_point"]}')
            get_code_list_sessions()
    
    elif 'email' in req_send_code["step_data"]:
        print(f'[1] Email: {req_send_code["step_data"]["email"]}')
        get_code_list_sessions()
            
    elif "phone_number" in req_send_code["step_data"]:
        print(f'[0] Phone_Number: {req_send_code["step_data"]["phone_number"]}')
        get_code_list_sessions()

    elif  "phone_number" not in req_send_code["step_data"] and "email" not in req_send_code["step_data"]:
        print("Account needs to confirm it's you ")
    
    else:
        input(req_send_code)
      

def get_code_list_sessions():

    choice = input('choose a number: ')
    url_get_code = f"https://i.instagram.com/api/v1{api_path_url}"
    get_code_data = {
        'choice': str(choice),
        'device_id': uuid4(),
        'guid': uuid4(),
        '_csrftoken': "BE0qlaD88tnB3vjkLhGksva9WFE2LPYB"
        }
    req_get_code = post(url= url_get_code,headers=headers_list_sessions,data=get_code_data)
  
    if "step_data" in req_get_code.text:
        print( f'code sent to: {req_get_code.json()["step_data"]["contact_point"]}')
    else:
        input(req_get_code.text)
    security_code = input('\nEnter the security code: ')
    send_code_data = {
            'security_code': str(security_code),
            'device_id': uuid4(),
            'guid': uuid4(),
            '_csrftoken': "BE0qlaD88tnB3vjkLhGksva9WFE2LPYB"
            }
    url_send_code = f"https://i.instagram.com/api/v1{api_path_url}"
    req_send_code = post(url=url_send_code,headers=headers_list_sessions, data=send_code_data)

    if "logged_in_user" in req_send_code.text:
        print(f'logged in with {username_list_sessions}')
        get_session = req_send_code.cookies["sessionid"]
        with open(f'{username_list_sessions}.txt', 'w') as file:
            file.write(f'{get_session}')
            print(get_session)
            input(f"[$] Saved as {username_list_sessions}.txt")
        
    elif "Please check the code we sent you and try again." in req_send_code.text:
        print('you entered wrong code , try again')
        get_code_list_sessions()

    elif "This field is required." in req_send_code.text:
        print("Enter the code!")
        get_code_list_sessions()

    elif '"lock":true'  in req_send_code.text:
        input("you need to active code and change password") 

    else:
        input(req_send_code.text)
        get_code_list_sessions()



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
