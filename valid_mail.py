#Email validation
import re

def solve(m):
   pat = "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$" or "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[in]$" or "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[com]$"
   if re.match(pat,m):
      return ("Valid")
   return ("Invalid")

m = input("Enter email for validation ")
print(solve(m))
