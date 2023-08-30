import re
def regexp(email):
    return re.search("[a-z 0-9]\w+@[a-z]+\.[a-z]{1,3}$",email)
email = "kavyap23@gmail.com"
print(regexp(email))