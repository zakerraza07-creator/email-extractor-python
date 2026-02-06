
from functools import reduce
from re import*


# creating text file
with open("data.txt","w") as file:
    file.write("my email is test@gmail.com \ncontact at me admin@yahoo.com\n"
               "fake mail:user@abc.org\nanother one:demo123@gmail.con")



# reading file
with open("data.txt","r") as f:
    text=f.read()

# extract email
email=findall(r"[a-zA-Z0-9._]+@[a-zA-Z0-9]+\.[a-z]+",text)
print(email)

# normalize email (lowercase)
email_lower=list(map(lambda e:e.lower(),email))

# filter valid emails
valid_emails=list(filter(lambda e:e.endswith("@gmail.com"),email_lower))
print("valid emails",valid_emails)

# count total valid emails
total_emails=reduce(lambda a,b:a+1,valid_emails,0)
print("total valid emails",total_emails)


# write valid email to new file

with open("data2.txt","w") as f:
    for Email in valid_emails:
        f.write(Email+"\n")




