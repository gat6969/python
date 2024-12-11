import re


pattern = r'^[a-zA-Z0-9][._-]*[a-zA-Z0-9]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$'


emails = input("Enter email addresses separated by commas: ").split(',')


valid_emails = [email.strip() for email in emails if re.match(pattern, email.strip())]


print("Valid Email Addresses:")
print(valid_emails)
