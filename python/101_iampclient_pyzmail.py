import imapclient
import pprint


# Connecting to an IMAP server
imap_obj = imapclient.IMAPClient("imap.gmail.com", ssl=True)
# print(imap_obj)


# Logging in to the IMAP server
user_email = input("Enter the full mail address: ")
user_pwd = input("Enter the password to login: ")
# print(imap_obj.login(user_email, user_pwd))
imap_obj.login(user_email, user_pwd)


# Searching for Email
# Selecting a folder
pprint.pprint(imap_obj.list_folders())
