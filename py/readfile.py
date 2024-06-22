def read_wordlist(file_path):
    with open(file_path, 'r') as file:
        # Read each line and strip newline characters
        return [line.strip() for line in file]

# Path to the wordlist file
wordlist_path = "C:\\Users\\net\\Desktop\\SecLists\\Passwords\\xato-net-10-million-passwords-1000000.txt"

# Load the wordlist from the file
wordlist = read_wordlist(wordlist_path)
print(wordlist)
    