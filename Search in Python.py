import re

txt="My name is Sourav Paul"

t=re.search("Sourav",txt)

if t:
    print("Found")
else:
    print("Not Found")
