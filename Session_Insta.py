from  requests import get , post
import json
from uuid import uuid4


def login_one_session():
  
  global login_req

  username = input("Enter Your Username: ")
  password = input("Enter Your password: ")
  login_url = 'https://www.instagram.com/accounts/login/ajax/'

  login_header = {
      'accept': '*/*',
      'accept-encoding': 'gzip, deflate, br',
      'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
      'content-length': '291',
      'content-type': 'application/x-www-form-urlencoded',
      'cookie': 'ig_nrcb=1; mid=YfyRDwALAAE2u2Xao59RvgY4Kie1; ig_did=24EAD7A2-41F3-458B-81B2-4C4E87CE77AE; csrftoken=Gqpabe6S9nfg1355Y2zelxzotxiiUAD7',
      'origin': 'https://www.instagram.com',
      'referer': 'https://www.instagram.com/',
      'sec-fetch-dest': 'empty',
      'sec-fetch-mode': 'cors',
      'sec-fetch-site': 'same-origin',
      'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36 Edg/98.0.1108.43",
      'x-csrftoken': 'Gqpabe6S9nfg1355Y2zelxzotxiiUAD7',
      'x-ig-app-id': '936619743392459',
      'x-ig-www-claim': '0',
      'x-instagram-ajax': '9a16d12cf843',
      'x-requested-with': 'XMLHttpRequest'
    }
  login_data = {
        'username': username,
      'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:&:{password}',
      'queryParams': '{}',
      'optIntoOneTap': 'false'
      }

  login_req = post(url=login_url, headers=login_header, data=login_data)

  if '"checkpoint_required"' in login_req.text:
    print(f"@{username} Is Secured \n\n")
    send_code_one_session()

  elif '"authenticated":true' in login_req.text:
      sessionid = login_req.cookies.get("sessionid")
      with open(f'{username}.txt', 'w') as file:
          file.write(f'{sessionid}')
          file.close()
          print(f"[$] Saved as {username}.txt")
          input()
          exit()
  else:
      print(login_req.text)


def send_code_one_session():	

  global security_code , checkpoint_url

  get_checkpoint_url = json.loads(login_req.text)
  if "checkpoint_url" in get_checkpoint_url:
    checkpoint_url = get_checkpoint_url.get("checkpoint_url")
    # print(checkpoint_url)

  send_code_url = f'https://www.instagram.com{checkpoint_url}'
  send_code_header = {

    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9,ar;q=0.8',
    'Alt-Used': 'www.instagram.com',
    'Connection': 'keep-alive',
    'Content-Length': '63',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Cookie': 'ig_nrcb=1; mid=YfyRDwALAAE2u2Xao59RvgY4Kie1; ig_did=24EAD7A2-41F3-458B-81B2-4C4E87CE77AE; csrftoken=Gqpabe6S9nfg1355Y2zelxzotxiiUAD7',
    'Host': 'www.instagram.com',
    'Origin': 'https://www.instagram.com',
    'Referer': 'https://www.instagram.com',
    'TE': 'Trailers',
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36 Edg/98.0.1108.43",
    'X-ASBD-ID': '437806',
    'X-CSRFToken': 'Gqpabe6S9nfg1355Y2zelxzotxiiUAD7',
    'X-IG-App-ID': '936619743392459',
    'X-IG-WWW-Claim': '0',
    'X-Instagram-AJAX': '9a16d12cf843',
    'X-Requested-With': 'XMLHttpRequest'
    }

  code = 1

  send_code_date = {
    'choice': code
    }

  send_code_req = post(url=send_code_url, headers=send_code_header, data=send_code_date)

  if ("security_code") in send_code_req.text:

    choose_number = input("""[ 1 ] Enter the code ?    [ 2 ] Accept login without code ?
    
choose the number: """)

    if choose_number == '1':
       security_code= input("\nEnter your code: ")
       get_code_one_session()

    elif choose_number == '2':
       security_code = input('\nChosse this was me in your account and press enter: ')
       get_code_one_session()

    else:
      print("Please chose 1 or 2 ")
      send_code_one_session()
	

def get_code_one_session():
  get_code_url = f'https://www.instagram.com{checkpoint_url}'
   
  get_code_header = {
      'Accept': '*/*',
      'Accept-Encoding': 'gzip, deflate, br',
      'Accept-Language': 'en-US,en;q=0.9,ar;q=0.8',
      'Alt-Used': 'www.instagram.com',
      'Connection': 'keep-alive',
      'Content-Length': '63',
      'Content-Type': 'application/x-www-form-urlencoded',
      'Cookie': 'ig_nrcb=1; mid=YfyRDwALAAE2u2Xao59RvgY4Kie1; ig_did=24EAD7A2-41F3-458B-81B2-4C4E87CE77AE; csrftoken=Gqpabe6S9nfg1355Y2zelxzotxiiUAD7',
      'Host': 'www.instagram.com',
      'Origin': 'https://www.instagram.com',
      'Referer': 'https://www.instagram.com',
      'TE': 'Trailers',
      'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36 Edg/98.0.1108.43",
      'X-ASBD-ID': '437806',
      'X-CSRFToken': 'Gqpabe6S9nfg1355Y2zelxzotxiiUAD7',
      'X-IG-App-ID': '936619743392459',
      'X-IG-WWW-Claim': '0',
      'X-Instagram-AJAX': '9a16d12cf843',
      'X-Requested-With': 'XMLHttpRequest'
      }
  
  get_code_data = {
      
      "security_code" : security_code
      }

  get_code_req = post(url=get_code_url, headers=get_code_header, data=get_code_data)

  if '"status":"ok"' in get_code_req.text:
      print("login done")
      sessionid = get_code_req.cookies.get("sessionid")
      with open(f'{username}.txt', 'w') as file:
          file.write(f'{sessionid}')
          file.close()
          print(f"[$] Saved as {username}.txt")
          input()
          exit()
  
  elif '"status":"fail"' in get_code_req.text:
      print("code is wrong")
      send_code_one_session()

  else:
      print(" error")


def login_list_sessions():
    global req_login, headers_login , username

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
            send_code_list_sessions()

        else:
            input(req_login.text)


def send_code_list_sessions():
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

    get_code_list_sessions()  

def get_code_list_sessions():

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
        get_code_list_sessions()

    elif "This field is required." in send_code.text:
        print("Enter the code!")
        get_code_list_sessions()                                    
    else:
        print(f' {send_code.text}')
        get_code_list_sessions()


if __name__ == "__main__":

    choose = input("""
    
[ 1 ] get session account
[ 2 ] get list sessions accounts

please choose your number: """)


    if choose == "1":
        login_one_session()
    elif choose == "2":
        login_list_sessions()

