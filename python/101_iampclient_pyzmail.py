import imapclient
import imaplib
import pprint
import datetime


# Increasing the size limit
imaplib._MAXLINE = 10_000_000


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
# pprint.pprint(imap_obj.list_folders())
imap_obj.select_folder("INBOX", readonly=True)

# Getting UIDs
UIDs = imap_obj.search(["SINCE", datetime.date(2022, 9, 15)])
print(UIDs)
