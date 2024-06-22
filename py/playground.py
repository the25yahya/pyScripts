import re

string = r"08hsc80HVMEUF  9038450    U |||\{\}}{)_%(#)@+!%*)$!)^josdmgk:d b+-/FFHJJI;       idk      abc    $ #"

pattern = r"[A-Z]"

uppercase_letters = re.findall(pattern, string)

print(uppercase_letters)
