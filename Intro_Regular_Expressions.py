import re
Meeting = 'Hello from prince@gmail.com about the meeting @ 3 P.M'
emails = re.findall('\S+@\S+', Meeting)
print(emails)