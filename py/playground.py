from sys import argv

script , file = argv 

def read_all(f):
    print(f.read())

def rewind(f):
    f.seek(0)
    
def print_a_line(line_count, f):
    print(line_count, f.readline())


current_file = open(file)

