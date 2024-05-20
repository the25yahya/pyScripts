import requests
import json

RULES = ["get","g","post","po","put","pu","delete","d"]
CHOICE = input("Wich http method you would like to chose?  GET(G) / POST(PO) / PUT(PU) /DELETE(D) : ").lower() 


if CHOICE in RULES:
    url = input("Enter a valid url , example : http://example.com/api : ")
    headers = {}
    user_headers_choice = input("do you want to specify header fields ( ENTER 'SET' ) or go with the default( ENTER 'DEFAULT' )?").lower() 
    if user_headers_choice == 'set':
        user_headers = input("Enter custom headers in the format 'HeaderName1: Value1, HeaderName2: Value2': ")
            
        for header in user_headers.split(","):
                key, value = header.split(':')
                headers[key.strip()] = value.strip()
    elif user_headers_choice != 'default':
            print("Invalid choice. Default headers will be used.")
    if CHOICE == "get" or CHOICE == "g":
        response = requests.get(url,headers=headers if headers else None)
        print(response.content)
    elif CHOICE == "post" or CHOICE == "po":
        user_params_choice = input("do you want to use Form data(F) or Json data(J) ?").lower()
        if user_params_choice == "f":
            form_data = {}
            form_data_input = input("Enter form data in the format 'key1: value1, key2: value2': ")
            for data_pair in form_data_input.split(','):
                key, value = data_pair.split(':')
                form_data[key.strip()] = value.strip()
            response = requests.post(url,data=form_data,headers=header if headers else None)
            print("="*10, response.status_code, "="*10)
            print(response.content)
        elif user_params_choice == "j":
            json_data = {}
            json_data_input = input("Enter JSON data in valid JSON format: ")
            try:
                json_data = json.loads(json_data_input)
            # Send the POST request with JSON data
                response = requests.post(url, json=json_data, headers=headers)
            # Process the response
                print(response.content)
            except json.JSONDecodeError:
               print("Invalid JSON format.")
         
    
else: print("OPTION NOT AVAILABLE , TRY AGAIN")