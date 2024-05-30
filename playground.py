from pathlib import Path

file_path = Path('C:/Users/net/Desktop/SecLists/Passwords/xato-net-10-million-passwords-100000.txt')

if not file_path.is_file():
    print(f"File not found : {file_path}")
else : 
    try:
        content = file_path.read_text()
        passwords = content.splitlines()
        
        for password in passwords:
            print(password)
    except Exception as e:
        print(f"An error occured: {e}")